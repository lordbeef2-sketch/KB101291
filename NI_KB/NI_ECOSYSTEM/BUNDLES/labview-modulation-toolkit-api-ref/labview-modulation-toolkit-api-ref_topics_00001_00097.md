# NI DOCUMENT BUNDLE: labview-modulation-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-modulation-toolkit-api-ref start=1 end=97 -->
<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=analog-demodulation-nodes.html language=enus -->
## TOPIC 00001: Demodulation Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `analog-demodulation-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/analog-demodulation-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Demodulation Nodes

Analog Nodes

MT Demodulate AM

am modulated waveform

MT Demodulate FM

Performs frequency demodulation on the incoming I/Q signal.

MT Demodulate PM

Performs phase demodulation on the incoming I/Q signal.

Parent topic:

Analog Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=bit-recovery-nodes.html language=enus -->
## TOPIC 00002: Bit Recovery Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `bit-recovery-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/bit-recovery-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Bit Recovery Nodes

Demodulation Nodes

MT Detect ASK

Demodulates an amplitude-shift keying (ASK)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Detect CPM

Demodulates a CPM-modulated complex baseband waveform and returns the demodulated information bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Detect FSK

Demodulates a frequency-shift keying (FSK)-modulated complex baseband waveform and returns the demodulated information bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Detect MSK

Demodulates an minimum-shift keying (MSK)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Detect PAM

Demodulates a pulse-amplitude-modulated (PAM) complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Detect PSK

Demodulates a phase-shift keying (PSK)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Detect QAM

Demodulates a quadrature-amplitude modulation (QAM)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Parent topic:

Demodulation Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=coding-nodes.html language=enus -->
## TOPIC 00003: Coding Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `coding-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/coding-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Coding Nodes

Digital Nodes

LDPC Nodes

MT BCH Encoder

Generates a Bose-Chaudhari-Hocquenghem (BCH)-encoded bit stream. The BCH encoding algorithm produces the BCH code word using a systematic or non-systematic encoding scheme.

MT Convolutional Encode

Generates an encoded bit stream based on a specified code rate. The code rate is equal to the ratio of the data word length to the code word length.

MT Golay Encoder

Generates a Golay-encoded bit stream. Choose between the two triple-correcting Golay codes: the Golay (23,12,3) code and the extended Golay (24,12,3) code.

MT Hamming Encoder

Generates an order-m Hamming-encoded bit stream.

MT Puncture Data Stream

Punctures a data stream and returns it at a higher rate.

MT Spread Symbols

input bit stream

spreading code

MT Reed Solomon Symbol Encode

Generates a normal or shortened Reed-Solomon (RS) encoded integer symbol stream.

Parent topic:

Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=decoding-nodes.html language=enus -->
## TOPIC 00004: Decoding Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `decoding-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/decoding-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Decoding Nodes

Digital Nodes

MT BCH Decoder

Performs decoding on a Bose-Chaudhari-Hocquenghem (BCH)-encoded bit stream using the Berlekamp algorithm for binary BCH codes. The BCH decoding algorithm uses either a systematic or non-systematic encoding scheme.

MT Convolutional Decode

Decodes a convolutionally encoded bit stream using different types of the Viterbi decoding algorithm (hard decision/unquantized/soft decision) and specifications (code rate/generator matrix).

MT Depuncture Data Stream

erasure value

input data stream

erasure value

input data stream

MT Despread Symbols

Performs the direct sequence spread spectrum (DSSS) despreading operation on a spread sequence of data bits.

MT Golay Decoder

Decodes a Golay-encoded bit stream. The decoder provides the two triple-correcting Golay codes: the Golay (23,12,3) code and the extended Golay (24,12,3) code. This node uses the Arithmetic decoding algorithm for decoding the Golay (23,12,3) encoded bit stream and the Kasami error-trapping decoding algorithm for decoding the extended Golay (24,12,3) encoded bit stream.

MT Hamming Decoder

Decodes a Hamming-encoded bit stream.

MT LDPC Decoder

Executes iterative probabilistic decoding, or belief propagation, for low-density parity check (LDPC). In this algorithm, at each iteration, messages are passed from message nodes to check nodes and vice versa.

MT Reed Solomon Symbol Decode

Decodes a normal or shortened Reed-Solomon (RS) encoded integer symbol stream.

Parent topic:

Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=deinterleaving-nodes.html language=enus -->
## TOPIC 00005: DeInterleaving Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `deinterleaving-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/deinterleaving-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

DeInterleaving Nodes

Digital Nodes

MT Block DeInterleave (Matrix)

m

n

MT Convolutional DeInterleave

Performs the deinterleaving process with delays that you specify for each branch.

MT DePermute

Rearranges or depermutes the permuted data.

Parent topic:

Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=digital-demodulation-nodes.html language=enus -->
## TOPIC 00006: Demodulation Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `digital-demodulation-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/digital-demodulation-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Demodulation Nodes

Digital Nodes

Bit Recovery Nodes

MT Demodulate ASK

Demodulates an amplitude shift-keying (ASK)-modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, demodulated bit stream, and results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Demodulate CPM

Demodulates a continuous-phase modulation (CPM)-modulated complex baseband waveform and returns the time-aligned demodulated waveform, the demodulated information bit stream, and measurement results obtained during demodulation. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Demodulate FSK

Demodulates an frequency-shift keying (FSK)-modulated complex baseband waveform and returns the time-aligned demodulated waveform, the demodulated information bit stream, and measurement results obtained during demodulation. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Demodulate MSK

Demodulates an minimum shift keying (MSK)-modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, the ideal oversampled waveform, the demodulated bit stream, and the results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Demodulate PAM

Demodulates a pulse-amplitude-modulated (PAM) complex baseband waveform and returns the time-aligned oversampled complex waveform, demodulated bit stream, and results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Demodulate PSK

Demodulates a phase-shift keying (PSK) modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, the demodulated bit stream, and measurement results obtained during demodulation. This node attempts to remove carrier and phase offset by locking to the carrier signal.

MT Demodulate QAM

Demodulates a quadrature-amplitude modulation (QAM)-modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, the demodulated bit stream, and the results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Parent topic:

Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=digital-measurements-nodes.html language=enus -->
## TOPIC 00007: Measurements Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `digital-measurements-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/digital-measurements-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Measurements Nodes

Digital Nodes

MT Calculate BER

Calculates the average bit error rate (BER) against a PN sequence or a reference bit pattern that you specify.

MT Measure Burst Timing

input complex waveform

ideal power curve

MT Measure Quadrature Impairments

Measures and reports quadrature impairments over a single user-specified window for each of the supported modulation types.

MT Measure Rho

Calculates rho given an acquired and ideal waveform.

Parent topic:

Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=digital-modulation-nodes.html language=enus -->
## TOPIC 00008: Modulation Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `digital-modulation-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/digital-modulation-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Modulation Nodes

Digital Nodes

MT Modulate ASK

output complex waveform

MT Modulate CPM

output complex waveform

MT Modulate FSK

output complex waveform

MT Modulate MSK

output complex waveform

MT Modulate PAM

output complex waveform

MT Modulate PSK

output complex waveform

MT Modulate QAM

output complex waveform

Parent topic:

Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=digital-nodes.html language=enus -->
## TOPIC 00009: Digital Nodes

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `digital-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/digital-nodes.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`

Digital Nodes

Modulation Toolkit Nodes

Coding Nodes

Decoding Nodes

DeInterleaving Nodes

Demodulation Nodes

Equalization Nodes

Impairments Nodes

Interleaving Nodes

Measurements Nodes

Modulation Nodes

MT Generate Bits (poly)

Generates the sequence of data bits to be modulated. These nodes can generate Fibonacci or Galois pseudonoise (PN) bit sequences, or bit sequences based on a pattern that you specify.

Utilities Nodes

Visualization Nodes

Parent topic:

Modulation Toolkit Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-align-to-ideal-symbol.html language=enus -->
## TOPIC 00010: MT Align To Ideal Symbols

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-align-to-ideal-symbol.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-align-to-ideal-symbol.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locates the first occurrence of the ideal symbol timing instant in the matched filtered input complex waveform and applies phase-continuous resampling to align the first sample of the input complex waveform to the ideal symbol timing instant.

MT Align To Ideal Symbols

Locates the first occurrence of the ideal symbol timing instant in the matched filtered input complex waveform and applies phase-continuous resampling to align the first sample of the input complex waveform to the ideal symbol timing instant.

Utilities Nodes

MT Align To Ideal Symbols (FSK)

input phase waveform

input phase waveform

MT Align to Ideal Symbols (Generic)

input complex waveform

input complex waveform

MT Align To Ideal Symbols (MSK)

input phase waveform

input phase waveform

MT Align To Ideal Symbols (Offset PSK)

input complex waveform

output complex waveform (offset removed)

output complex waveform (offset removed)

Parent topic:

Utilities Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-apply-flat-fading-profile.html language=enus -->
## TOPIC 00011: MT Apply Flat Fading Profile

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-apply-flat-fading-profile.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-apply-flat-fading-profile.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a flat fading profile to the input complex waveform. The faded waveform can be used to test receiver immunity to fading channels. This node normalizes the fading profile to ensure that the power in the input complex waveform is equal to the fading variance. The Modulation Toolkit 4.0 version

MT Apply Flat Fading Profile

Applies a flat fading profile to the input complex waveform. The faded waveform can be used to test receiver immunity to fading channels.

Note

fading profile

input complex waveform

[IMAGE alt='1378' src='MethodCall.MT_Apply_Flat_Fading_Profile.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### fading profile

The sample-by-sample profile to be applied to the input complex waveform. At each call, this node begins applying this fading profile from the index point where it left off on the previous iteration unless reset? is set to TRUE. Wire the fading profile parameter of MT Generate Fading Profile to this parameter.

##### Setting the right fading profile length

fading profile

input complex waveform

fading profile

input complex waveform

fading profile

input complex waveform

fading profile

reset?

input complex waveform

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether this node begins applying the fading profile at the index point where it left off on the last iteration.

| TRUE | Applies the fading profile at index point 0. |
| --- | --- |
| FALSE | Does not apply the fading profile at index point 0. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### output complex waveform

The faded modulated complex baseband waveform data returned by this node. This parameter is always the same size as the input complex waveform, regardless of the size of the fading profile.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Time of the first value in the Y array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Normalizing the Rician Fading
 Profile

To match the output complex waveform power to the specified fading variance, this VI first
 normalizes the power array of the power delay profile, and the amplitude corresponding to
 power element is then multiplied by the corresponding fading profile,
 f<sub>kl</sub>, where l = 1, 2
 …, L, and L is the profile length.

For the
 selective Rayleigh profile, the power coefficients, Ck2 , corresponding to each path are shown in the following
 equation:

C
 k
 2
 =
 10
 P
 k
 10

The normalized power coefficients can then be
 represented by:

C
 ¯
 k
 2
 =
 C
 k
 2
 ∑
 k
 =
 1
 N
 C
 k
 2

for k =
 1,...,N.

For the selective Rician profile, the power in the
 line-of-sight (LOS) path is given by:

P
 L
 O
 S
 =
 (
 k
 +
 1
 )
 ×
 P
 1

The normalized power coefficients can then be represented by the following equation:

C
 ¯
 k
 2
 =
 C
 k
 2
 (
 k
 L
 O
 S
 +
 1
 )
 ×
 C
 1
 2
 +
 ∑
 k
 =
 2
 N
 C
 k
 2

By multiplying these power coefficients with the
 generated fading profile, f<sub>kl</sub>, for each path, we can obtain
 the amplitude, a<sub>kl</sub>, to apply to the Rician profile as shown in
 the following equation:

a
 k
 l
 =
 C
 ¯
 k
 ×
 f
 k
 l

for k = 1,...,N
 and l = 1,...,L, where L is the
 profile length.

The time array,

τ

k

dt

n

k

input complex waveform

n
 k
 =
 τ
 k
 d
 t

The input complex waveform is then
 delayed for each path by y<sub>k</sub>[n] =
 x[n - n<sub>k</sub>], where
 n = 1,...,M and M is the
 input complex waveform size.

Finally, y<sub>k</sub>[n] is point-by-point
 multiplied with amplitude coefficients to obtain the output complex
 waveform as shown by the following equation:

y
 [
 n
 ]
 =
 ∑
 k
 =
 1
 N
 a
 k
 l
 ×
 x
 [
 n
 −
 n
 k
 ]

In MT Apply Selective Fading
 Profile, the power from the power delay profile, set for each
 path, is applied to the corresponding fading profile generated by
 MT Generate Fading Profile. The power delay
 profile is specified in terms of power, P<sub>k</sub>, and
 time,

τ

k

k

N

power delay profile

τ

k

d

t

k

N

N

input complex
 waveform

y(t)

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

Parent topic:

MT Apply Fading Profile

Parent topic:

MT Apply Fading Profile

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-apply-iq-impairments.html language=enus -->
## TOPIC 00012: MT Apply IQ Impairments

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-apply-iq-impairments.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-apply-iq-impairments.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies various I/Q impairments to the complex baseband modulated waveform. input complex waveform The modulated complex baseband waveform data. t0 Trigger (start) time of the Y array. Default value: 0.0 dt Time interval between data points in the Y array. Default value: 1.0 Y The complex-valued sig

MT Apply IQ Impairments

Applies various I/Q impairments to the complex baseband modulated waveform.

[IMAGE alt='1378' src='MethodCall.MT_Apply_IQ_Impairments.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### q dc offset

The desired DC offset of the Q waveform as a percentage of the input complex waveform. Valid values are -100 to +100, inclusive.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### iq gain imbalance

The desired ratio of I gain to Q gain, in dB. Valid values are between -6.0 and +6.0.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### quadrature skew

The desired quadrature skew of the complex waveform in degrees. Valid values are between -30.0 and +30.0 degrees.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### i dc offset

The desired DC offset of the I waveform as a percentage of full scale of the input complex waveform. Valid values are between -100 and +100.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### impairment definition

A value that indicates which set of equations is used to represent impairments.

In the equations in the following table, is the real component and is the imaginary component of each sample in the input complex waveform. and are the real and imaginary components of the corresponding sample in the output complex waveform. is I DC Offset (%) / 100, and is Q DC Offset (%) / 100.

| Vertical Shear | The definition uses the following equations for I/Q impairments: where φ is the specified quadrature skew, in radians = 10(IQ gain imbalance/20) In matrix form, these equations are represented by where |
| --- | --- |
| Axis Shear | With this option selected, this node uses an impairment definition that simplifies the conversion between measured impairments and their inverse impairments. For example, you may want to measure the I/Q impairments of a system and compensate for those impairments by applying the inverse impairments to the generated or received waveform. Using the Axis Shear definition, given a measured skew and imbalance (in dB), the inverse impairments are -1.0 * skew and -1.0 * imbalance. This definition uses the following equations for IQ impairments: where = 10(IQ gain imbalance/20) φ is the specified quadrature skew, in radians In matrix form, these equations are represented by where |

Default value: Vertical Shear

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency offset

The desired frequency offset, in Hertz (Hz), to apply to the output complex waveform.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether this node continues applying the impairments using the previous iteration states.

| TRUE | Restarts the impairment generation process. |
| --- | --- |
| FALSE | Continues applying the impairments using the previous iteration states. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### output complex waveform

The impaired complex baseband modulated waveform data returned by this node.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Impairments Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-apply-matched-filter-cpm.html language=enus -->
## TOPIC 00013: MT Apply Matched Filter (CPM)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-apply-matched-filter-cpm.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-apply-matched-filter-cpm.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a matched filter to a specified CPM-modulated waveform. The node first performs phase differentiation followed by matched filtering on the phase of the input complex waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring co

MT Apply Matched Filter (CPM)

Applies a matched filter to a specified CPM-modulated waveform. The node first performs phase differentiation followed by matched filtering on the phase of the input complex waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring continuability from one iteration to the next.

Use MT Align To Ideal Symbols to locate and realign the matched-filtered waveform at the ideal symbol timing instant.

[IMAGE alt='1378' src='MethodCall.MT_Apply_Matched_Filter_(CPM).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The continuous-time modulated complex baseband waveform data.

Note

input complex waveform

samples per symbol

MT Resample (Complex Cluster)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing sample-spaced coefficients for the desired matched filter. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. Ensure that the value of samples per symbol matches the matched samples per symbol value used to generate the filter coefficients.

matched filter coefficients

Note

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per information symbol in the input complex waveform.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues matched filtering using the previous iteration states.

| TRUE | Resets the matched filtering process. |
| --- | --- |
| FALSE | Continues performing matched filtering from the previous iteration. Matched filtering begins from the last iteration state on subsequent calls. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### output phase waveform

The output matched filtered continuous-time phase waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Matched Filter

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-apply-matched-filter-fsk.html language=enus -->
## TOPIC 00014: MT Apply Matched Filter (FSK)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-apply-matched-filter-fsk.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-apply-matched-filter-fsk.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a matched filter to an input FSK-modulated waveform. The node first performs phase differentiation, followed by matched filtering on the phase of the input complex waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring cont

MT Apply Matched Filter (FSK)

Applies a matched filter to an input FSK-modulated waveform. The node first performs phase differentiation, followed by matched filtering on the phase of the input complex waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring continuability from one iteration to the next.

Use MT Align To Ideal Symbols to locate and realign the matched-filtered waveform at the ideal symbol timing instant.

[IMAGE alt='1378' src='MethodCall.MT_Apply_Matched_Filter_(FSK).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The continuous-time modulated complex baseband waveform data.

Note

input complex waveform

samples per symbol

MT Resample (Complex Cluster)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing sample-spaced coefficients for the desired matched filter. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. Ensure that the value of samples per symbol matches the matched samples per symbol value used to generate the filter coefficients.

matched filter coefficients

Note

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per information symbol in the input complex waveform.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### symbol phase continuity

Continuity of phase transitions between symbols.

| continuous | Continuous phase transitions between symbols. |
| --- | --- |
| discontinuous | Discontinuous phase transitions between symbols, that is, discontinuous phase FSK (DPFSK). With discontinuous phase-FSK (DPFSK), modulation consists of selecting the appropriate sinusoid based on the input data. Thus, when switching between symbols, there is a discontinuity in the FSK signal phase. To emulate a hardware-based DPFSK source, this node maintains the phase of each independent sinusoid versus time. Thus, the DPFSK modulator acts like a hardware-based (multiple switched tone generator) FSK modulator. |

Default value: 
 continuous

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues matched filtering using the previous iteration states.

| TRUE | Resets the matched filtering process. |
| --- | --- |
| FALSE | Continues performing matched filtering from the previous iteration. Matched filtering begins from the last iteration state on subsequent calls. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### output phase waveform

The output matched filtered continuous-time phase waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Matched Filter

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-apply-matched-filter-generic.html language=enus -->
## TOPIC 00015: MT Apply Matched Filter (Generic)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-apply-matched-filter-generic.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-apply-matched-filter-generic.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a matched filter to a PAM, ASK, QAM, and PSK-modulated input waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring continuability from one iteration to the next. Use MT Align To Ideal Symbols to locate and realign the matc

MT Apply Matched Filter (Generic)

Applies a matched filter to a PAM, ASK, QAM, and PSK-modulated input waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring continuability from one iteration to the next.

Use MT Align To Ideal Symbols to locate and realign the matched-filtered waveform at the ideal symbol timing instant.

[IMAGE alt='1378' src='MethodCall.MT_Apply_Matched_Filter_(Generic).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The continuous-time modulated complex baseband waveform data.

Note

input complex waveform

samples per symbol

MT Resample (Complex Cluster)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing sample-spaced coefficients for the desired matched filter. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. Ensure that the value of samples per symbol matches the matched samples per symbol value used to generate the filter coefficients.

matched filter coefficients

Note

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per information symbol in the input complex waveform.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues matched filtering using the previous iteration states.

| TRUE | Resets the matched filtering process. |
| --- | --- |
| FALSE | Continues performing matched filtering from the previous iteration. Matched filtering begins from the last iteration state on subsequent calls. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### output complex waveform

The output matched filtered continuous-time I/Q baseband waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the Y array. The reciprocal of this value is equal to the system sample rate.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Matched Filter

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-ask-feedfwd-eqlz-lms-spec-coef.html language=enus -->
## TOPIC 00016: MT ASK Feedforward Equalizer (LMS) (Specify coefficients)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-ask-feedfwd-eqlz-lms-spec-coef.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-ask-feedfwd-eqlz-lms-spec-coef.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies adaptive feedforward software equalization using the least-mean-squared (LMS) algorithm to the ASK-demodulated input complex waveform. Allows you to specify equalizer coefficients or their initial conditions. This node assumes that the input sample rate is an even integer multiple of the sym

MT ASK Feedforward Equalizer (LMS) (Specify coefficients)

Applies adaptive feedforward software equalization using the least-mean-squared (LMS) algorithm to the ASK-demodulated input complex waveform.

Allows you to specify equalizer coefficients or their initial conditions.

Note

samples per symbol

ASK system parameters

[IMAGE alt='1378' src='MethodCall.MT_ASK_Feedforward_Equalizer_(LMS)_(Specify_coefficients).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### ASK system parameters

Parameter values defining the ASK system. Wire the ASK system parameters cluster of MT Generate ASK System Parameters (M) or MT Generate ASK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of ASK levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### equalizer coefficients in

The filter coefficients for initializing the feedforward equalizer. The time span of this array (in symbols) is given by the following equation:

size(equalizer coefficients in) / 
 taps per symbol

For best performance and minimization of intersymbol interference, ensure that the time span (in symbols) of the equalizer coefficients filter is greater than the time span (in symbols) of the channel filter.

Note

- The equalizer coefficients in array must contain an odd number of elements.
- The values specified here are used by the equalizer only when reset? is set to TRUE or on the first call to this node. Otherwise, this node maintains an internal buffer of the equalizer coefficients resulting from completion of the previous call.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### training bits

The binary-valued training bits that train the feedforward equalizer during the training phase when the reset? parameter is set to TRUE. This parameter is ignored when reset? is set to FALSE.

Note

- Ensure that the duration of training is long enough to allow the feedforward equalizer to converge before switching to a decision-directed adaptation.
- When working with 
 M -ary modulation schemes { M >2, or bits per symbol >1} in which symbols represent groups of bits, the specified training bits must start on a symbol boundary.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### feedforward equalizer (lms) parameters

The feedforward equalization parameters, which define the equalizer tap spacing (symbol spaced/fractionally spaced) and convergence rate during training and steady-state.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### taps per symbol

The tap-spacing of the equalizer coefficients array, relative to one symbol duration. For error-free operation, set this parameter value to be a factor of the samples per symbol passed from MT Generate System Parameters.

Note

Modulation

symbol

T-spaced

taps per symbol = 1,

which means that every tap of the equalization filter spans the time duration of one symbol.

A 
 fractionally-spaced (T/N-spaced) equalizer has

taps per symbol> 1.

For example, a 
 T/2-spaced equalizer has 
 taps per symbol = 2, meaning that every two taps of the equalization filter span the time duration of one symbol.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### delta (training)

The convergence parameter for feedforward equalization during the training phase. This value adapts the feedforward equalizer coefficients for the duration of the training period when reset? is set to TRUE.

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### delta (steady state)

The steady-state convergence parameter for adapting the equalizer coefficients during the decision-directed phase. Use this value for adapting the feedforward equalizer coefficients when reset? is set to FALSE.

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to continue feedforward equalization using the previous iteration states. This node always resets on first call.

| TRUE | Resets the internal state, restarts, and trains the equalizer. |
| --- | --- |
| FALSE | Continues feedforward equalization using the previous iteration states. This node assumes that the input complex waveform is phase-continuous with the previous iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### output complex waveform

The equalized oversampled waveform generated from the feedforward equalizer as a result of adaptation. This waveform consists of the oversampled data that are compensated for the channel impulse response with zero intersymbol interference. Wire this parameter to the corresponding instance of MT Measure Quadrature Impairments to make modulation measurements such as modulation error ratio (MER) and error vector magnitude (EVM).

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### error

The instantaneous per symbol error in the output of the adaptive feedforward equalizer filter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### equalizer coefficients out

The adaptive feedforward equalizer filter coefficients when equalization is complete for the current iteration.

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The recovered bit stream generated from the adaptive feedforward equalizer. The recovered bit stream is phase-aligned with the output complex waveform at the equalizer output. Wire this parameter to MT Measure Quadrature Impairments for performing modulation measurements such as modulation error ratio (MER) and error vector magnitude (EVM), or to MT Calculate BER after Trigger for making bit error rate (BER) measurements.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Demodulator-to-Equalizer Data Flow

The input complex waveform is assumed to have undergone matched filtering and carrier frequency offset correction during the demodulation process (the recovered complex waveform returned by a Demodulation node meets these criteria). The adaptive equalization process ensures that the convolution of the channel filter and the equalizer coefficient filter yields a delta function thereby removing any intersymbol interference in the equalized output complex waveform.

The following flow chart illustrates demodulator-to-equalizer data flow.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

#### Duration of Training Mode

Because the feedforward equalizer is adaptive, the adaptation is carried out initially in a training mode and is later switched to a decision-directed mode. In the training mode, a user-supplied training bit sequence trains the equalizer to adapt to the channel conditions. In the decision-directed mode, the equalizer tap adaptation is self-directed, and the current equalizer output adapts the equalizer taps for the next iteration.

Tip

The duration of the training mode is set by the number of training bits when reset? is set to TRUE, or when the first instance of this node is called. Training mode equalization is applied to the initial 
 N symbols of the input complex waveform, where 
 N is the number of symbols that can be mapped from the input training bits. Decision-directed equalization is applied to the input complex waveform starting at symbol 
 N+1.

#### Continuous Data Stream

The equalizer is continuable, that is, the same instance of an equalizer can be called multiple times, with each instance operating on an input complex waveform representing a subsequent frame of the same data stream. To operate in this manner, call the equalizer in a loop with the first iteration setting reset? to TRUE and subsequent iterations setting reset? to FALSE.

#### Discontinuous Data Stream

The equalizer can also be applied to a discontinuous data stream, in which the same instance of the equalizer operates on input complex waveforms that do not maintain phase continuity from one to the next. To operate in this manner, call the same instance of the equalizer in a loop with reset? set to TRUE for all iterations.

#### Continuous Equalization on Discontinuous Data

This node allows continuous equalization on discontinuous data. If you are working with discontinuous data and know that your input channel is invariant enough to potentially benefit from continuous equalization, wire equalizer coefficients out to the equalizer coefficients in parameter. To do so, call the equalizer in a loop with reset? set to TRUE and use a feedback node or shift register to wire the output of a previous iteration as the input for the next iteration. This technique also allows continuous training of the equalizer; if supplied with appropriate training bits, the equalizer retrains with every iteration.

Parent topic:

MT ASK Feedforward Equalizer

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-ask-feedfwd-eqlz-lms-spec-length.html language=enus -->
## TOPIC 00017: MT ASK Feedforward Equalizer (LMS) (Specify length)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-ask-feedfwd-eqlz-lms-spec-length.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-ask-feedfwd-eqlz-lms-spec-length.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies adaptive feedforward software equalization using the least-mean-squared (LMS) algorithm to the ASK-demodulated input complex waveform. Allows you to specify the length of the feedforward equalizer in symbols. input complex waveform The modulated complex baseband waveform data. t0 Trigger (st

MT ASK Feedforward Equalizer (LMS) (Specify length)

Applies adaptive feedforward software equalization using the least-mean-squared (LMS) algorithm to the ASK-demodulated input complex waveform. Allows you to specify the length of the feedforward equalizer in symbols.

[IMAGE alt='1378' src='MethodCall.MT_ASK_Feedforward_Equalizer_(LMS)_(Specify_length).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### ASK system parameters

Parameter values defining the ASK system. Wire the ASK system parameters cluster of MT Generate ASK System Parameters (M) or MT Generate ASK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of ASK levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### equalizer length

The duration of the feedforward equalizer filter in symbols.

Note

N = equalizer length (symbols) × samples per symbol + 1

When reset? is set to TRUE, use this parameter to create the 
 N-tap feedforward equalizer with default initial conditions. The default feedforward equalizer coefficients are thereby specified by the Dirac delta impulse response:

, 
 n = 0 .. 
 N-1

when reset? is set to TRUE.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### training bits

The binary-valued training bits that train the feedforward equalizer during the training phase when the reset? parameter is set to TRUE. This parameter is ignored when reset? is set to FALSE.

Note

- Ensure that the duration of training is long enough to allow the feedforward equalizer to converge before switching to a decision-directed adaptation.
- When working with 
 M -ary modulation schemes { M >2, or bits per symbol >1} in which symbols represent groups of bits, the specified training bits must start on a symbol boundary.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### feedforward equalizer (lms) parameters

The feedforward equalization parameters, which define the equalizer tap spacing (symbol spaced/fractionally spaced) and convergence rate during training and steady-state.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### taps per symbol

The tap-spacing of the equalizer coefficients array, relative to one symbol duration. For error-free operation, set this parameter value to be a factor of the samples per symbol passed from MT Generate System Parameters.

Note

Modulation

symbol

T-spaced

taps per symbol = 1,

which means that every tap of the equalization filter spans the time duration of one symbol.

A 
 fractionally-spaced (T/N-spaced) equalizer has

taps per symbol> 1.

For example, a 
 T/2-spaced equalizer has 
 taps per symbol = 2, meaning that every two taps of the equalization filter span the time duration of one symbol.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### delta (training)

The convergence parameter for feedforward equalization during the training phase. This value adapts the feedforward equalizer coefficients for the duration of the training period when reset? is set to TRUE.

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### delta (steady state)

The steady-state convergence parameter for adapting the equalizer coefficients during the decision-directed phase. Use this value for adapting the feedforward equalizer coefficients when reset? is set to FALSE.

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to continue feedforward equalization using the previous iteration states. This node always resets on first call.

| TRUE | Resets the internal state, restarts, and trains the equalizer. |
| --- | --- |
| FALSE | Continues feedforward equalization using the previous iteration states. This node assumes that the input complex waveform is phase-continuous with the previous iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### output complex waveform

The equalized oversampled waveform generated from the feedforward equalizer as a result of adaptation. This waveform consists of the oversampled data that are compensated for the channel impulse response with zero intersymbol interference. Wire this parameter to the corresponding instance of MT Measure Quadrature Impairments to make modulation measurements such as modulation error ratio (MER) and error vector magnitude (EVM).

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### error

The instantaneous per symbol error in the output of the adaptive feedforward equalizer filter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### equalizer coefficients out

The adaptive feedforward equalizer filter coefficients when equalization is complete for the current iteration.

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The recovered bit stream generated from the adaptive feedforward equalizer. The recovered bit stream is phase-aligned with the output complex waveform at the equalizer output. Wire this parameter to MT Measure Quadrature Impairments for performing modulation measurements such as modulation error ratio (MER) and error vector magnitude (EVM), or to MT Calculate BER after Trigger for making bit error rate (BER) measurements.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Demodulator-to-Equalizer Data Flow

The input complex waveform is assumed to have undergone matched filtering and carrier frequency offset correction during the demodulation process (the recovered complex waveform returned by a Demodulation node meets these criteria). The adaptive equalization process ensures that the convolution of the channel filter and the equalizer coefficient filter yields a delta function thereby removing any intersymbol interference in the equalized output complex waveform.

The following flow chart illustrates demodulator-to-equalizer data flow.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

#### Duration of Training Mode

Because the feedforward equalizer is adaptive, the adaptation is carried out initially in a training mode and is later switched to a decision-directed mode. In the training mode, a user-supplied training bit sequence trains the equalizer to adapt to the channel conditions. In the decision-directed mode, the equalizer tap adaptation is self-directed, and the current equalizer output adapts the equalizer taps for the next iteration.

Tip

The duration of the training mode is set by the number of training bits when reset? is set to TRUE, or when the first instance of this node is called. Training mode equalization is applied to the initial 
 N symbols of the input complex waveform, where 
 N is the number of symbols that can be mapped from the input training bits. Decision-directed equalization is applied to the input complex waveform starting at symbol 
 N+1.

#### Continuous Data Stream

The equalizer is continuable, that is, the same instance of an equalizer can be called multiple times, with each instance operating on an input complex waveform representing a subsequent frame of the same data stream. To operate in this manner, call the equalizer in a loop with the first iteration setting reset? to TRUE and subsequent iterations setting reset? to FALSE.

#### Discontinuous Data Stream

The equalizer can also be applied to a discontinuous data stream, in which the same instance of the equalizer operates on input complex waveforms that do not maintain phase continuity from one to the next. To operate in this manner, call the same instance of the equalizer in a loop with reset? set to TRUE for all iterations.

Parent topic:

MT ASK Feedforward Equalizer

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-auto-configure-ccdf.html language=enus -->
## TOPIC 00018: MT Auto Configure CCDF

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-auto-configure-ccdf.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-auto-configure-ccdf.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended I/Q acquisition settings to use with MT Compute CCDF. The recommended settings provide a set of values to configure the PXIe-5650/5651/5652 RF Analog Signal Generator for acquiring the input complex waveform to calculate the complementary cumulative distribution function (CCD

MT Auto Configure CCDF

Returns the recommended I/Q acquisition settings to use with MT Compute CCDF. The recommended settings provide a set of values to configure the PXIe-5650/5651/5652 RF Analog Signal Generator for acquiring the input complex waveform to calculate the complementary cumulative distribution function (CCDF).

[IMAGE alt='1378' src='MethodCall.MT_Auto_Configure_CCDF.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### lowpass filter bandwidth

The bandwidth, in Hertz (Hz), of the lowpass filter. The lowpass filter is the front-end digital filter that is applied to the acquired signal. Use the filter to remove the out-of-band signal content before computing the CCDF.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### count

Number of records to acquire.

The number of records to acquire is computed using the following equation:

Number of records = ceiling (count/(sampling rate * measurement interval)).

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### measurement interval

The time, in seconds, to use to acquire a single record in the CCDF calculation.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### trigger delay

The delay, in seconds, from the trigger event to determine the start of the measurement interval.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### lowpass filter type

A value that indicates the type of filter to use for filtering the samples before calculating the CCDF.

| Gaussian | Uses a Gaussian filter. |
| --- | --- |
| Flat | Uses a flat filter. |
| None | Does not use any filter. |

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### recommended IQ acquisition settings

Recommended settings.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### records

Number of records to acquire.

The number of records to acquire is computed using the following equation:

Number of records = ceiling (count/(sampling rate * measurement interval)).

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sampling rate

Recommended sample rate, in Hz. The sample rate is returned based on the value of the lowpass filter bandwidth parameter, even if you set the lowpass filter type parameter to 
None.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### acquisition time

Amount of time per record to acquire the input complex waveform, in seconds. This value might be larger than the measurement interval and takes into account measurement filter and processing delays.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### pre-trigger delay

Amount of time, in seconds, before the trigger. This value accounts for delays in the measurement process.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### post-trigger delay

Amount of time, in seconds, between the trigger and the acquisition process. This value is used when the actual signal to be measured is generated after the trigger.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### min quiet time

Minimum time, in seconds, during which the signal must remain below a certain value to trigger.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Complementary Cumulative Distribution Function Measurement

The CCDF is a statistical characterization of time-domain waveform that completely describes the power characteristics of a signal.

A CCDF graph relates average signal power (x-axis) to signal power statistics (y-axis) such that each point on the CCDF curve shows how much time a signal spends at or above a given power level. The power level is expressed in dB relative to the average signal power level.

Parent topic:

Analog and Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-bch-encoder-non-sys-msg-gen-prod.html language=enus -->
## TOPIC 00019: MT BCH Encoder (Non-Systematic, Message-Generator Product)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-bch-encoder-non-sys-msg-gen-prod.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-bch-encoder-non-sys-msg-gen-prod.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encodes a sequence of data words non-systematically using the Bose-Chaudhari-Hocquenghem (BCH) algorithm. In the encoded code words, the whole data word sequence might not be explicitly present. The code word is generated as a finite field polynomial multiplication of the data word and the generator

MT BCH Encoder (Non-Systematic, Message-Generator Product)

Encodes a sequence of data words non-systematically using the Bose-Chaudhari-Hocquenghem (BCH) algorithm. In the encoded code words, the whole data word sequence might not be explicitly present. The code word is generated as a finite field polynomial multiplication of the data word and the generator polynomial.

[IMAGE alt='1378' src='MethodCall.MT_BCH_Encoder_(Non-Systematic,_Message-Generator_Product).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

Bit sequence representing the data bits to encode. Use the bits generated by MT Generate Bits to produce this bit stream or wire a custom data bit stream to this parameter.

Tip

output bit stream

input bit stream

k

input bit stream

k

input bit stream

k

reset?

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### n,k,t

Values of the code word length (n), data word length (k), and error correcting capacity (t), in bits. The 
n, k, and 
t values for BCH encoding are interrelated such that specifying two values constrains the third value. Select from a set of well-known (n,k,t) triples that are widely used for BCH encoding or specify an arbitrary triple by entering three comma-separated integers. The encoding scheme takes in a bit data word of k bits and produces a code word of n bits.

Default value: 7, 4, 1

##### Code Word Length Limits

n,k,t

n

n

k

t

n,k,t

MT BCH Encoder

MT BCH Decoder

n

n

m

k

t

n

n,k,t

n,k,t

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the encoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Galois field structure corresponding to the BCH n, k, t values. |
| --- | --- |
| FALSE | Continues encoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to encoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence encoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT BCH Encoder

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-bch-encoder-systematic.html language=enus -->
## TOPIC 00020: MT BCH Encoder (Systematic)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-bch-encoder-systematic.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-bch-encoder-systematic.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encodes a sequence of data words systematically using the Bose-Chaudhari-Hocquenghem (BCH) algorithm. This node arranges the output code word such that the entire data word sequence is maintained and preceded by the parity words. input bit stream Bit sequence representing the data bits to encode. Us

MT BCH Encoder (Systematic)

Encodes a sequence of data words systematically using the Bose-Chaudhari-Hocquenghem (BCH) algorithm. This node arranges the output code word such that the entire data word sequence is maintained and preceded by the parity words.

[IMAGE alt='1378' src='MethodCall.MT_BCH_Encoder_(Systematic).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

Bit sequence representing the data bits to encode. Use the bits generated by MT Generate Bits to produce this bit stream or wire a custom data bit stream to this parameter.

Tip

output bit stream

input bit stream

k

input bit stream

k

input bit stream

k

reset?

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### n,k,t

Values of the code word length (n), data word length (k), and error correcting capacity (t), in bits. The 
n, k, and 
t values for BCH encoding are interrelated such that specifying two values constrains the third value. Select from a set of well-known (n,k,t) triples that are widely used for BCH encoding or specify an arbitrary triple by entering three comma-separated integers. The encoding scheme takes in a bit data word of k bits and produces a code word of n bits.

Default value: 7, 4, 1

##### Code Word Length Limits

n,k,t

n

n

k

t

n,k,t

MT BCH Encoder

MT BCH Decoder

n

n

m

k

t

n

n,k,t

n,k,t

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the encoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Galois field structure corresponding to the BCH n, k, t values. |
| --- | --- |
| FALSE | Continues encoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to encoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence encoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT BCH Encoder

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-bch-encoder.html language=enus -->
## TOPIC 00021: MT BCH Encoder

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-bch-encoder.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-bch-encoder.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a Bose-Chaudhari-Hocquenghem (BCH)-encoded bit stream. The BCH encoding algorithm produces the BCH code word using a systematic or non-systematic encoding scheme.

MT BCH Encoder

Generates a Bose-Chaudhari-Hocquenghem (BCH)-encoded bit stream. The BCH encoding algorithm produces the BCH code word using a systematic or non-systematic encoding scheme.

Coding Nodes

MT BCH Encoder (Non-Systematic, Message-Generator Product)

Encodes a sequence of data words non-systematically using the Bose-Chaudhari-Hocquenghem (BCH) algorithm. In the encoded code words, the whole data word sequence might not be explicitly present. The code word is generated as a finite field polynomial multiplication of the data word and the generator polynomial.

MT BCH Encoder (Systematic)

Encodes a sequence of data words systematically using the Bose-Chaudhari-Hocquenghem (BCH) algorithm. This node arranges the output code word such that the entire data word sequence is maintained and preceded by the parity words.

Parent topic:

Coding Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-compute-ccdf.html language=enus -->
## TOPIC 00022: MT Compute CCDF

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-compute-ccdf.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-compute-ccdf.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the complementary cumulative distribution function (CCDF). input complex waveform Modulated complex waveform data. x0 Start time, in seconds, of the y array. dx Time interval between data points in the y array. y The complex signal values. lowpass filter type A value that indicates the type

MT Compute CCDF

Computes the complementary cumulative distribution function (CCDF).

[IMAGE alt='1378' src='MethodCall.MT_Compute_CCDF.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

Modulated complex waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x0

Start time, in seconds, of the y array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dx

Time interval between data points in the y array.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### y

The complex signal values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### lowpass filter type

A value that indicates the type of filter to use for filtering the samples before calculating the CCDF.

| Gaussian | Uses a Gaussian filter. |
| --- | --- |
| Flat | Uses a flat filter. |
| None | Does not use any filter. |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### lowpass filter bandwidth

The bandwidth, in Hertz (Hz), of the lowpass filter. The lowpass filter is the front-end digital filter that is applied to the acquired signal. Use the filter to remove the out-of-band signal content before computing the CCDF.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to reinitialize the computation of average and peak power. If you set this parameter to TRUE, the node discards information about the accumulated peak and average power values in previous calls to the node.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### measurements

The measurement results.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### average power

The measured average power, in dBm.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### avg pwr percentile

The average power percentile as a percentage.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 10% power

The measured power in 10% of the total power, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 1% power

The measured power in 1% of the total power, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 0.1% power

The measured power in 0.1% of the total power, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 0.01% power

The measured power in 0.01% of the total power, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 0.001% power

The measured power in 0.001% of the total power, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 0.0001% power

The measured power in 0.0001% of the total power, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak power

The measured peak power, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### count

Number of samples across all iterations, including the current iteration.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### CCDF traces

Two CCDF traces. One trace corresponds to the input complex waveform, and the other trace is the CCDF of a Gaussian variate of zero mean and unit variance with the same bin size.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Complementary Cumulative Distribution Function Measurement

The CCDF is a statistical characterization of time-domain waveform that completely describes the power characteristics of a signal.

A CCDF graph relates average signal power (x-axis) to signal power statistics (y-axis) such that each point on the CCDF curve shows how much time a signal spends at or above a given power level. The power level is expressed in dB relative to the average signal power level.

Parent topic:

Analog and Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-conv-decoder-viterbi-hard-gen-matrix.html language=enus -->
## TOPIC 00023: MT Convolutional Decoder (Viterbi Hard Decision, Generator Matrix)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-conv-decoder-viterbi-hard-gen-matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-conv-decoder-viterbi-hard-gen-matrix.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs Viterbi hard decision decoding on a convolutionally encoded bit stream using a custom generator matrix. input bit stream Bit sequence representing the code word to decode. generator matrix The generator connection polynomial matrix that sets the convolutional feedforward node connections in

MT Convolutional Decoder (Viterbi Hard Decision, Generator Matrix)

Performs Viterbi hard decision decoding on a convolutionally encoded bit stream using a custom generator matrix.

[IMAGE alt='1378' src='MethodCall.MT_Convolutional_Decoder_(Viterbi_Hard_Decision,_Generator_Matrix).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

Bit sequence representing the code word to decode.

[IMAGE alt='datatype_icon' src='/assets/img/c1du32.png']

##### generator matrix

The generator connection polynomial matrix that sets the convolutional feedforward node connections in octal format.

The convolutional node is modeled as a linear feedforward shift register arrangement consisting of 
 k rows with 
 K-1 shift registers per row, where 
 k denotes the data word length and 
 K denotes the constraint length. If 
 a<sub>ij</sub> {0 ≤ 
 i ≤ 
 n-1, 0 ≤ 
 j ≤ 
 k-1} denotes a particular element in the generator matrix, the row index 
 i corresponds to the convolutional node output 
 y<sub>i</sub> that is affected by this element, while the column index 
 j corresponds to the 
 jth row in the 
 k row shift register arrangement. Thus 
 a<sub>ij</sub> specifies how the 
 K bits in the 
 jth row of the feedforward shift register matrix affects the 
 ith output of the convolutional node.

For a rate of 2/3, the generator matrix is specified as follows:

The matrix on the right represents the elements in octal format. Zeros are padded at the end of the corresponding code generator sequences such that their total length is a multiple of three digits. The following diagram depicts the rate 2/3 convolutional node corresponding to the previously mentioned generator matrix, with a constraint length equal to 4. In the following diagram, D represents a shift register or memory element.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

Here, 
 y<sub>i</sub><sup>j</sup>, 0 ≤ 
 j ≤ 
 n-1 denotes the 
 jth output of this node, in the 
 ith instance.

Default value:

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### constraint length

The maximum number of encoded bits that can be affected by a single input bit. This value represents (1 + 
maximal memory order), where 
maximal memory order refers to the length of the longest shift register chain in the convolutional encoder.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### initial state

The initial parent state for the decode operation. When reset? is set to TRUE, the trellis structure is set to this state, thereby initializing the Viterbi decoding operation. On the first call to this node, and thereafter when reset? is set to FALSE, the survivor state from the previous iteration is used to continue performing Viterbi decoding and this parameter is ignored.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### traceback depth

The number of trellis stages used in the Viterbi decoding process.

Default value: 15

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the decoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Viterbi algorithm to start decoding from initial state. The relationship of the length of output bit stream, Lout, to the length of input bit stream, Lin, is described by the following equation: Lout = k × [floor(Lin/n) - D] where k is the input data word length, n is the output data word length, and D is the decoder traceback depth in symbols. |
| --- | --- |
| FALSE | Continues decoding from the previous iteration. The length of output bit stream is given by the following equation: Lout = k × floor(Lin/n). |

Tip

L

in

reset?

k/n

L

out

k

L

in

n

D

k×D

k

L

in

n

MT Convolutional Decoder

reset?

- Append max( D,K -1)× k zeros to the end of the message prior to performing convolutional encoding. Here 
 k represents the message word length.
- Append 
 D×n zeros to the end of the encoded bit stream prior to calling MT Convolutional Decoder . Here, 
 D is the traceback depth employed in the convolutional decoder, and 
 n is the code word length.

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence decoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### final state

The survivor state after decoding the entire input bit stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Convolutional Decode

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-conv-decoder-viterbi-hard-rate.html language=enus -->
## TOPIC 00024: MT Convolutional Decoder (Viterbi Hard Decision, Rate)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-conv-decoder-viterbi-hard-rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-conv-decoder-viterbi-hard-rate.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decodes a convolutionally encoded bit stream using a specified code rate. The code rate is equal to the ratio of the data word length to the code word length. input bit stream Bit sequence representing the code word to decode. rate The convolutional code rate, which is a ratio of k/n, where k is the

MT Convolutional Decoder (Viterbi Hard Decision, Rate)

Decodes a convolutionally encoded bit stream using a specified code rate. The code rate is equal to the ratio of the data word length to the code word length.

[IMAGE alt='1378' src='MethodCall.MT_Convolutional_Decoder_(Viterbi_Hard_Decision,_Rate).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

Bit sequence representing the code word to decode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### rate

The convolutional code rate, which is a ratio of 
k/n, where 
k is the input data word length and 
n is the output code word length.

| 1/2 | Supports constraint lengths of 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17 |
| --- | --- |
| 1/3 | Supports constraint lengths of 3,4,5,6,7,8,9,10,11,12,13,14 |
| 1/4 | Supports constraint lengths of 3,4,5,6,7,8,9,10,11,12,13,14 |
| 2/3 | Supports constraint lengths of 2,3,4,5,6 |
| 3/4 | Supports constraint lengths of 2,3,4 |

Default value: 1/2

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### constraint length

The maximum number of encoded bits that can be affected by a single input bit. This value represents (1 + 
maximal memory order), where 
maximal memory order refers to the length of the longest shift register chain in the convolutional encoder.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### initial state

The initial parent state for the decode operation. When reset? is set to TRUE, the trellis structure is set to this state, thereby initializing the Viterbi decoding operation. On the first call to this node, and thereafter when reset? is set to FALSE, the survivor state from the previous iteration is used to continue performing Viterbi decoding and this parameter is ignored.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### traceback depth

The number of trellis stages used in the Viterbi decoding process.

Default value: 15

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the decoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Viterbi algorithm to start decoding from initial state. The relationship of the length of output bit stream, Lout, to the length of input bit stream, Lin, is described by the following equation: Lout = k × [floor(Lin/n) - D] where k is the input data word length, n is the output data word length, and D is the decoder traceback depth in symbols. |
| --- | --- |
| FALSE | Continues decoding from the previous iteration. The length of output bit stream is given by the following equation: Lout = k × floor(Lin/n). |

Tip

L

in

reset?

k/n

L

out

k

L

in

n

D

k×D

k

L

in

n

MT Convolutional Decoder

reset?

- Append max( D,K -1)× k zeros to the end of the message prior to performing convolutional encoding. Here 
 k represents the message word length.
- Append 
 D×n zeros to the end of the encoded bit stream prior to calling MT Convolutional Decoder . Here, 
 D is the traceback depth employed in the convolutional decoder, and 
 n is the code word length.

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence decoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### final state

The survivor state after decoding the entire input bit stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Convolutional Decode

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-conv-decoder-viterbi-soft-rate.html language=enus -->
## TOPIC 00025: MT Convolutional Decoder (Viterbi Soft Decision, Rate)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-conv-decoder-viterbi-soft-rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-conv-decoder-viterbi-soft-rate.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs Viterbi soft decision decoding on a convolutionally encoded bit stream using a specified code rate. The code rate is equal to the ratio of the data word length to the code word length. input integers Bit metrics for quantized demodulated BPSK symbol data. These demodulated BPSK symbols are

MT Convolutional Decoder (Viterbi Soft Decision, Rate)

Performs Viterbi soft decision decoding on a convolutionally encoded bit stream using a specified code rate. The code rate is equal to the ratio of the data word length to the code word length.

[IMAGE alt='1378' src='MethodCall.MT_Convolutional_Decoder_(Viterbi_Soft_Decision,_Rate).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### input integers

Bit metrics for quantized demodulated BPSK symbol data. These demodulated BPSK symbols are quantized to 
n<sub>soft</sub> bits of precision, such that an integer value of 0 represents a strong logic 0 and a value of 2<sup>n</sup><sub>soft</sub> represents a strong logic 1.

Note

Modulation

For higher-order M-PSK/QAM schemes, convert the I/Q symbol values into corresponding quantized bit metrics using a suitable algorithm/heuristic.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### rate

The convolutional code rate, which is a ratio of 
k/n, where 
k is the input data word length and 
n is the output code word length.

| 1/2 | Supports constraint lengths of 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17 |
| --- | --- |
| 1/3 | Supports constraint lengths of 3,4,5,6,7,8,9,10,11,12,13,14 |
| 1/4 | Supports constraint lengths of 3,4,5,6,7,8,9,10,11,12,13,14 |
| 2/3 | Supports constraint lengths of 2,3,4,5,6 |
| 3/4 | Supports constraint lengths of 2,3,4 |

Default value: 1/2

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### constraint length

The maximum number of encoded bits that can be affected by a single input bit. This value represents (1 + 
maximal memory order), where 
maximal memory order refers to the length of the longest shift register chain in the convolutional encoder.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### initial state

The initial parent state for the decode operation. When reset? is set to TRUE, the trellis structure is set to this state, thereby initializing the Viterbi decoding operation. On the first call to this node, and thereafter when reset? is set to FALSE, the survivor state from the previous iteration is used to continue performing Viterbi decoding and this parameter is ignored.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### traceback depth

The number of trellis stages used in the Viterbi decoding process.

Default value: 15

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### soft decision bits

The number of bits used for quantizing the BPSK modulated symbols to integers.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the decoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Viterbi algorithm to start decoding from initial state. The relationship of the length of output bit stream, Lout, to the length of input bit stream, Lin, is described by the following equation: Lout = k × [floor(Lin/n) - D] where k is the input data word length, n is the output data word length, and D is the decoder traceback depth in symbols. |
| --- | --- |
| FALSE | Continues decoding from the previous iteration. The length of output bit stream is given by the following equation: Lout = k × floor(Lin/n). |

Tip

L

in

reset?

k/n

L

out

k

L

in

n

D

k×D

k

L

in

n

MT Convolutional Decoder

reset?

- Append max( D,K -1)× k zeros to the end of the message prior to performing convolutional encoding. Here 
 k represents the message word length.
- Append 
 D×n zeros to the end of the encoded bit stream prior to calling MT Convolutional Decoder . Here, 
 D is the traceback depth employed in the convolutional decoder, and 
 n is the code word length.

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence decoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### final state

The value for the 
k(K-1) shift registers as the right-aligned (least significant) 
k(K-1) bits when this node completes execution, where 
K is the constraint length and 
k is the data word length in bits.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Convolutional Decode

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-conv-decoder-viterbi-unquantized-gen.html language=enus -->
## TOPIC 00026: MT Convolutional Decoder (Viterbi UnQuantized, Generator Matrix)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-conv-decoder-viterbi-unquantized-gen.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-conv-decoder-viterbi-unquantized-gen.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs Viterbi unquantized decoding on a convolutionally encoded bit stream using a custom generator matrix. input symbols The unquantized BPSK demodulated soft symbol data. To generate unquantized BPSK demodulated data from the Modulation nodes, decimate the oversampled data at the output of the

MT Convolutional Decoder (Viterbi UnQuantized, Generator Matrix)

Performs Viterbi unquantized decoding on a convolutionally encoded bit stream using a custom generator matrix.

[IMAGE alt='1378' src='MethodCall.MT_Convolutional_Decoder_(Viterbi_UnQuantized,_Generator_Matrix).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### input symbols

The unquantized BPSK demodulated soft symbol data.

Note

Modulation

For higher order M-PSK/QAM schemes, convert the I/Q symbol values into corresponding bit metrics using a suitable algorithm/heuristic.

[IMAGE alt='datatype_icon' src='/assets/img/c1du32.png']

##### generator matrix

The generator connection polynomial matrix that sets the convolutional feedforward node connections in octal format.

The convolutional node is modeled as a linear feedforward shift register arrangement consisting of 
 k rows with 
 K-1 shift registers per row, where 
 k denotes the data word length and 
 K denotes the constraint length. If 
 a<sub>ij</sub> {0 ≤ 
 i ≤ 
 n-1, 0 ≤ 
 j ≤ 
 k-1} denotes a particular element in the generator matrix, the row index 
 i corresponds to the convolutional node output 
 y<sub>i</sub> that is affected by this element, while the column index 
 j corresponds to the 
 jth row in the 
 k row shift register arrangement. Thus 
 a<sub>ij</sub> specifies how the 
 K bits in the 
 jth row of the feedforward shift register matrix affects the 
 ith output of the convolutional node.

For a rate of 2/3, the generator matrix is specified as follows:

The matrix on the right represents the elements in octal format. Zeros are padded at the end of the corresponding code generator sequences such that their total length is a multiple of three digits. The following diagram depicts the rate 2/3 convolutional node corresponding to the previously mentioned generator matrix, with a constraint length equal to 4. In the following diagram, D represents a shift register or memory element.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

Here, 
 y<sub>i</sub><sup>j</sup>, 0 ≤ 
 j ≤ 
 n-1 denotes the 
 jth output of this node, in the 
 ith instance.

Default value:

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### constraint length

The maximum number of encoded bits that can be affected by a single input bit. This value represents (1 + 
maximal memory order), where 
maximal memory order refers to the length of the longest shift register chain in the convolutional encoder.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### initial state

The initial parent state for the decode operation. When reset? is set to TRUE, the trellis structure is set to this state, thereby initializing the Viterbi decoding operation. On the first call to this node, and thereafter when reset? is set to FALSE, the survivor state from the previous iteration is used to continue performing Viterbi decoding and this parameter is ignored.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### traceback depth

The number of trellis stages used in the Viterbi decoding process.

Default value: 15

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the decoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Viterbi algorithm to start decoding from initial state. The relationship of the length of output bit stream, Lout, to the length of input bit stream, Lin, is described by the following equation: Lout = k × [floor(Lin/n) - D] where k is the input data word length, n is the output data word length, and D is the decoder traceback depth in symbols. |
| --- | --- |
| FALSE | Continues decoding from the previous iteration. The length of output bit stream is given by the following equation: Lout = k × floor(Lin/n). |

Tip

L

in

reset?

k/n

L

out

k

L

in

n

D

k×D

k

L

in

n

MT Convolutional Decoder

reset?

- Append max( D,K -1)× k zeros to the end of the message prior to performing convolutional encoding. Here 
 k represents the message word length.
- Append 
 D×n zeros to the end of the encoded bit stream prior to calling MT Convolutional Decoder . Here, 
 D is the traceback depth employed in the convolutional decoder, and 
 n is the code word length.

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence decoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### final state

The survivor state resulting from the Viterbi UnQuantized decision decoding operation after decoding the entire input bit stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Convolutional Decode

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-convolutional-deinterleaver-generic.html language=enus -->
## TOPIC 00027: MT Convolutional DeInterleaver (Generic)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-convolutional-deinterleaver-generic.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-convolutional-deinterleaver-generic.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the deinterleaving process with delays that you specify for each branch. A convolutional deinterleaver is the inverse of a convolutional interleaver. In convolutional deinterleaving, data elements pass cyclically through a set of branches. That is, in an N branch convolutional deinterleaver

MT Convolutional DeInterleaver (Generic)

Performs the deinterleaving process with delays that you specify for each branch.

A convolutional deinterleaver is the inverse of a convolutional interleaver. In convolutional deinterleaving, data elements pass cyclically through a set of branches. That is, in an 
 *N* branch convolutional deinterleaver, the element 0 goes through branch 0, element 1 goes through branch 1, element 
 *N*-1 goes through branch 
 *N*-1, element 
 *N* goes through branch 0, and so on. Each branch has different delays associated with it. Hence the data sent to each deinterleaver branch is delayed by a specific amount (the amount of delay in that particular branch) before the deinterleaver returns the data. In a convolutional interleaver, if the delay in branch number 
 *n* is 
 *d*<sub>n</sub>, maximum delay is 
 *max_delay* and the minimum delay is 
 *min_delay*, then for the corresponding convolutional deinterleaver, the delay in branch number 
 *n* is: 
 *D*<sub>n</sub> = (*max_delay*+*min_delay*)-*d*<sub>n</sub>.

[IMAGE alt='1378' src='MethodCall.MT_Convolutional_DeInterleaver_(Generic).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### data in

The input data to the deinterleaver.

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### interleaver delays

The number of delays individually for each branch of the corresponding interleaver. The number of elements in this array determines the number of branches, and the value of each element denotes the delay for that branch. For example, if interleaver delays is [3,6,9,2], it implies that there are four branches; branch 0 has 3 delays, branch 1 has 6 delays, and so on.

Note

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### initial state

The shift register values when the convolutional deinterleaver begins operation.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to check the current input parameters. The current input parameters are always checked on the first run of this node.

| TRUE | Checks input parameters. |
| --- | --- |
| FALSE | Does not check input parameters. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### data out

The output of the convolutional deinterleaver.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Examples of Convolutional Interleaving and Deinterleaving

The following example demonstrates convolutional interleaving and deinterleaving. Let the data in be: x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, …

Interleaver Input 
 [IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg'] Interleaver Output

D = unit delay in the path.

Assume for this example that the unit delay = 1, and the initial state shift registers are initialized with values of 0 for both the interleaver and the deinterleaver.

Interleaved Data: x0, 0, 0, 0, x4, x1, 0, 0, x8, x5, x2, 0, x12, x9, …

Deinterleaver Input 
 [IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg'] Deinterleaver Output

Deinterleaved Data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, …

Parent topic:

MT Convolutional DeInterleave

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-convolutional-deinterleaver-standard.html language=enus -->
## TOPIC 00028: MT Convolutional DeInterleaver (Standard)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-convolutional-deinterleaver-standard.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-convolutional-deinterleaver-standard.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the deinterleaving process using a fixed number of branches and fixed unit delay. A convolutional deinterleaver is the inverse of a convolutional interleaver. In convolutional deinterleaving, data elements pass cyclically through a set of branches. That is, in an N branch convolutional dein

MT Convolutional DeInterleaver (Standard)

Performs the deinterleaving process using a fixed number of branches and fixed unit delay.

A convolutional deinterleaver is the inverse of a convolutional interleaver. In convolutional deinterleaving, data elements pass cyclically through a set of branches. That is, in an 
 *N* branch convolutional deinterleaver, the element 0 goes through branch 0, element 1 goes through branch 1, element 
 *N*-1 goes through branch 
 *N*-1, element 
 *N* goes through branch 0, and so on. Each branch has different delays associated with it. Hence the data sent to each deinterleaver branch is delayed by a specific amount (the amount of delay in that particular branch) before the deinterleaver returns the data. In a convolutional interleaver, if the delay in branch number 
 *n* is 
 *d*<sub>n</sub>, maximum delay is 
 *max_delay* and the minimum delay is 
 *min_delay*, then for the corresponding convolutional deinterleaver, the delay in branch number 
 *n* is: 
 *D*<sub>n</sub> = (*max_delay*+*min_delay*)-*d*<sub>n</sub>.

[IMAGE alt='1378' src='MethodCall.MT_Convolutional_DeInterleaver_(Standard).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### data in

The input data to the deinterleaver.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of branches

The number of branches of the convolutional deinterleaver. Data elements pass through the branches in a cyclic fashion. For example, in an 
N branch convolutional deinterleaver, data element 0 goes through branch 0, element 1 goes through branch 1, element 
N-1 goes through branch 
N-1, element 
N returns through branch 0, and so on. Each branch incorporates different delays.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### unit delay

The unit delay value. If this value is defined as 
D, then the number of delays on the 
ith branch is (i×D). If the total number of branches is 
N, then 
i = 0, 1,…, 
N-1.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### initial state

The shift register values when the convolutional deinterleaver begins operation.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to check the current input parameters. The current input parameters are always checked on the first run of this node.

| TRUE | Checks input parameters. |
| --- | --- |
| FALSE | Does not check input parameters. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### data out

The output of the convolutional deinterleaver.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Examples of Convolutional Interleaving and Deinterleaving

The following example demonstrates convolutional interleaving and deinterleaving. Let the data in be: x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, …

Interleaver Input 
 [IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg'] Interleaver Output

D = unit delay in the path.

Assume for this example that the unit delay = 1, and the initial state shift registers are initialized with values of 0 for both the interleaver and the deinterleaver.

Interleaved Data: x0, 0, 0, 0, x4, x1, 0, 0, x8, x5, x2, 0, x12, x9, …

Deinterleaver Input 
 [IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg'] Deinterleaver Output

Deinterleaved Data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, …

Parent topic:

MT Convolutional DeInterleave

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-convolutional-encode.html language=enus -->
## TOPIC 00029: MT Convolutional Encode

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-convolutional-encode.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-convolutional-encode.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates an encoded bit stream based on a specified code rate. The code rate is equal to the ratio of the data word length to the code word length.

MT Convolutional Encode

Generates an encoded bit stream based on a specified code rate. The code rate is equal to the ratio of the data word length to the code word length.

Coding Nodes

MT Convolutional Encoder (Generator Matrix)

Generates an encoded bit stream based on a generator matrix that you set.

MT Convolutional Encoder (Rate)

rate

Parent topic:

Coding Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-demodulate-am-ssb.html language=enus -->
## TOPIC 00030: MT Demodulate AM (SSB)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-demodulate-am-ssb.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-demodulate-am-ssb.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates a single sideband (SSB) amplitude-modulated signal. AM modulated waveform The modulated complex baseband time-domain data for demodulation. t0 The trigger (start) time of the Y array. Default value: 0.0 dt Time interval between data points in the Y array. Default value: 1.0 Y The complex

MT Demodulate AM (SSB)

Demodulates a single sideband (SSB) amplitude-modulated signal.

[IMAGE alt='1378' src='MethodCall.MT_Demodulate_AM_(SSB).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### AM modulated waveform

The modulated complex baseband time-domain data for demodulation.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

The trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued time-domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### modulation index

The expected modulation index of the AM demodulated waveform parameter. This value is used to scale the AM demodulated waveform parameter.

- Set this value to the estimated modulation index of the incoming AM modulated waveform signal to scale the AM demodulated waveform parameter by this value. The resulting scaled AM demodulated waveform can be used to quantify error between the actual and expected modulation index.
- Set this value to 1.0 to return an AM demodulated waveform with no scaling. When you set suppressed carrier? to FALSE, the peak amplitude value of the unscaled AM demodulated waveform represents the true modulation index of the incoming AM modulated waveform.

Note

modulation index

suppressed carrier?

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### pilot extraction filter

Parameters used to locate the pilot tone and extract it from the specified AM modulated signal.

The node designs a bandpass filter for locating the pilot tone, and a band-reject filter for removing the pilot tone from the recovered signal, in a normalized frequency range:

[dt *approx freq. - 0.01 * search (± % of Fsampl)

dt * approx freq.+ 0.01 * search (± % of Fsampl)]

where 
 Fsampl is the sampling rate of the AM modulated waveform parameter.

Note

AM modulated waveform

search (+/-% of Fsampl)

pilot extraction filter

- taps : 81
- approx freq. : 0.01
- search (± % of Fsampl) : 5

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### taps

The number of taps used to design the pilot tone extraction filter.

The number of taps you specify in the pilot extraction filter cluster is also used to set the number of taps used in the pilot removal or rejection filter before recovering the demodulated message signal. If the pilot tone is near the message bandwidth, the default number of taps specified in the pilot extraction tap cluster might be insufficient to provide enough pilot rejection. As a result, the demodulated message signal might be distorted, even though the pilot was successfully extracted. In such cases, NI recommends experimenting by increasing the number of filter taps, although the increase affects the execution speed of the demodulation node.

Default value: 81

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### approx freq.

The estimated frequency, in hertz (Hz), of the pilot tone in the AM modulated waveform parameter.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### search (+/- % of Fsampl)

The search window size as a percentage of the input sample rate (1/dt). To avoid erroneous detection of the pilot tone, ensure that this search window does not include any portion of the message spectrum.

Default value: 0.25

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### costas loop parameters

Optional parameters controlling the Costas loop. Usually Beta is chosen to be less than 0.02 * Alpha. These parameters are used in tracking carrier phase offset in the specified AM modulated waveform. The default settings are typically unchanged except in the presence of severely time-varying carrier phase offset.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Alpha

The parameter, in meters, as required by the Costas loop design.

Default value: 1 m

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Beta

The parameter as required by the Costas loop design.

Default value: 20 u

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### suppressed carrier?

A Boolean that determines whether the carrier has been suppressed in the incoming modulated waveform.

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulation using internal states from previous iterations.

| TRUE | The node redesigns the pilot extraction filter and clears the internal filter states on each call. |
| --- | --- |
| FALSE | The node does not change the pilot extraction filter design across multiple calls, and sets the internal filter state to ensure continuous filter operation. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### AM demodulated waveform

The recovered message signal.

Note

AM demodulated waveform

modulation index

suppressed carrier?

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### measurements

The pilot tone location, carrier offset, and phase offset.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### extracted pilot tone

The location of the pilot tone in the AM modulated waveform frequency spectrum.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency offset

The measured carrier frequency offset, Hz, of the specified AM modulated waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### AM-SSB Demodulation

The AM-SSB demodulation procedure uses the transmitted pilot tone

e

j

ω

p

i

l

o

t

t

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

During the process of AM-SSB demodulation, the received AM-SSB signal (assumed to be sampled at the sample frequency

f

s

f

s

f

s

f

s

Parent topic:

MT Demodulate AM

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-demodulate-am-vsb.html language=enus -->
## TOPIC 00031: MT Demodulate AM (VSB)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-demodulate-am-vsb.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-demodulate-am-vsb.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates a vestigial sideband (VSB) amplitude-modulated signal. AM modulated waveform The modulated complex baseband time-domain data for demodulation. t0 The trigger (start) time of the Y array. Default value: 0.0 dt Time interval between data points in the Y array. Default value: 1.0 Y The comp

MT Demodulate AM (VSB)

Demodulates a vestigial sideband (VSB) amplitude-modulated signal.

[IMAGE alt='1378' src='MethodCall.MT_Demodulate_AM_(VSB).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### AM modulated waveform

The modulated complex baseband time-domain data for demodulation.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

The trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued time-domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### modulation index

The expected modulation index of the AM demodulated waveform parameter. This value is used to scale the AM demodulated waveform parameter.

- Set this value to the estimated modulation index of the incoming AM modulated waveform signal to scale the AM demodulated waveform parameter by this value. The resulting scaled AM demodulated waveform can be used to quantify error between the actual and expected modulation index.
- Set this value to 1.0 to return an AM demodulated waveform with no scaling. When you set suppressed carrier? to FALSE, the peak amplitude value of the unscaled AM demodulated waveform represents the true modulation index of the incoming AM modulated waveform.

Note

modulation index

suppressed carrier?

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### pilot extraction filter

Parameters used to locate the pilot tone and extract it from the specified AM modulated signal.

The node designs a bandpass filter for locating the pilot tone, and a band-reject filter for removing the pilot tone from the recovered signal, in a normalized frequency range:

[dt *approx freq. - 0.01 * search (± % of Fsampl)

dt * approx freq.+ 0.01 * search (± % of Fsampl)]

where 
 Fsampl is the sampling rate of the AM modulated waveform parameter.

Note

AM modulated waveform

search (+/-% of Fsampl)

pilot extraction filter

- taps : 81
- approx freq. : 0.01
- search (± % of Fsampl) : 5

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### taps

The number of taps used to design the pilot tone extraction filter.

The number of taps you specify in the pilot extraction filter cluster is also used to set the number of taps used in the pilot removal or rejection filter before recovering the demodulated message signal. If the pilot tone is near the message bandwidth, the default number of taps specified in the pilot extraction tap cluster might be insufficient to provide enough pilot rejection. As a result, the demodulated message signal might be distorted, even though the pilot was successfully extracted. In such cases, NI recommends experimenting by increasing the number of filter taps, although the increase affects the execution speed of the demodulation node.

Default value: 81

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### approx freq.

The estimated frequency, in hertz (Hz), of the pilot tone in the AM modulated waveform parameter.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### search (+/- % of Fsampl)

The search window size as a percentage of the input sample rate (1/dt). To avoid erroneous detection of the pilot tone, ensure that this search window does not include any portion of the message spectrum.

Default value: 0.25

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### costas loop parameters

Optional parameters controlling the Costas loop. Usually Beta is chosen to be less than 0.02 * Alpha. These parameters are used in tracking carrier phase offset in the specified AM modulated waveform. The default settings are typically unchanged except in the presence of severely time-varying carrier phase offset.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Alpha

The parameter, in meters, as required by the Costas loop design.

Default value: 1 m

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Beta

The parameter as required by the Costas loop design.

Default value: 20 u

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### suppressed carrier?

A Boolean that determines whether the carrier has been suppressed in the incoming modulated waveform.

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulation using internal states from previous iterations.

| TRUE | The node redesigns the pilot extraction filter and clears the internal filter states on each call. |
| --- | --- |
| FALSE | The node does not change the pilot extraction filter design across multiple calls, and sets the internal filter state to ensure continuous filter operation. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### AM demodulated waveform

The recovered message signal.

Note

AM demodulated waveform

modulation index

suppressed carrier?

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### measurements

The pilot tone location, carrier offset, and phase offset.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### extracted pilot tone

The location of the pilot tone in the AM modulated waveform frequency spectrum.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency offset

The measured carrier frequency offset, Hz, of the specified AM modulated waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### AM-VSB Demodulation

The AM-VSB demodulation procedure uses the transmitted pilot tone

e

j

ω

p

i

l

o

t

t

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

During the process of AM-VSB demodulation, the received AM-VSB signal (assumed to be sampled at the sample frequency

f

s

f

s

f

s

f

s

Parent topic:

MT Demodulate AM

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-demodulate-ask.html language=enus -->
## TOPIC 00032: MT Demodulate ASK

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-demodulate-ask.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-demodulate-ask.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates an amplitude shift-keying (ASK)-modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, demodulated bit stream, and results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the carrier signal. MT

MT Demodulate ASK

Demodulates an amplitude shift-keying (ASK)-modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, demodulated bit stream, and results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Note

input complex waveform

samples per symbol

Note

recovered complex waveform

measurements

[IMAGE alt='1378' src='MethodCall.MT_Demodulate_ASK.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### ASK system parameters

Parameter values defining the ASK system. Wire the ASK system parameters cluster of MT Generate ASK System Parameters (M) or MT Generate ASK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of ASK levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing the desired matched filter coefficients. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the matched samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the samples per symbol element of the ASK system parameters cluster that is passed to MT Demodulate ASK.

Note

reset?

reset?

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### synchronization parameters

Parameter values describing the synchronization sequence and the range of bits over which to search for this sequence. Wire the ASK synchronization parameters cluster returned by MT Generate ASK Synchronization Parameters (bit array) or MT Generate ASK Synchronization Parameters (number array) to the synchronization parameters cluster.

Note

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern used to synchronize the bit stream. To prevent false synchronization, select this pattern such that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated, but there is a phase ambiguity in the recovered symbols.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulating using the previous iteration states.

| TRUE | Restarts the demodulator. The node resets on the first call and when reset? is set to TRUE. |
| --- | --- |
| FALSE | Continues demodulating using the previous iteration states. The input complex waveform is contiguous with the input complex waveform from the previous iteration of this node. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. The frequency offset and phase offset corrections are scalar values applied to the entire block.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Time of the first value in the Y array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The demodulated information bit stream.

Note

2,1,...

0,1,1,0...

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### measurements

Measurements performed by the demodulator.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency offset

The measured carrier frequency offset, in hertz (Hz). The measured frequency offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency drift

The measured carrier frequency drift, in Hz. The measured frequency drift is not removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### phase offset

The measured phase offset, in degrees. The measured phase offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sync found index

Symbol index within the input complex waveform where the peak correlation to the sync sequence was found. If no sync sequence is specified in the synchronization parameters cluster, the sync found index parameter returns the offset from the start of the input complex waveform to the first complete symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Successful Locking

Successful locking depends on many factors, including signal quality, modulation type, filtering parameters, and acquisition size. Locking also requires a fairly uniform distribution of symbols in the signal. The demodulator lock rate increases (and failures decrease) as the number of symbols demodulated increases. In general, you can expect to achieve a better than 95% lock when demodulating 10 × 
 M number of symbols, where 
 M is 2<sup>bits per symbol</sup>.

#### Filter Delay

Finite impulse response (FIR) filters are used for different operations such as pulse-shaping, matched filtering, and downconversion filtering. For such filters, the output signal is related to the input signal as shown by the following equation:

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

where

P is the filter order

x[n] is the input signal

y[n] is the output signal

b
 <sub>i</sub> are the filter coefficients

The initial state for all samples in an FIR filter is 0. The filter output until the first input sample reaches the middle tap (the first causal sample) is called the transient response, or filter delay. For an FIR filter that has 
 N taps, the delay is (N-1)/2 samples. This relationship is illustrated in the following figure, where a sine wave is filtered by an FIR filter with 50 taps.

[IMAGE alt='1378' src='GUID-FBE65DFB-5758-4539-ACE6-66570B6DE08D-a5.png']

#### Recovering Samples in Single-Shot Operations

In single-shot operations for modulators and demodulators, the filter delay is truncated before the signal is generated because these samples are not valid. Some samples at the end of the block do not appear at the modulator or demodulator output, and hence appear to have been lost.

- For modulation: Let 
 L be the pulse-shaping filter length, 
 m be the number of samples per symbol, and 
 M be the modulation order. The number of bits to be added to the input bit stream is given by the following formula: N=(L−1)log⁡2MmN=(L−1)log⁡2Mm
- For demodulation: Demodulation use filters during matched filtering. Let 
 L be the length of the matched filter. The number of samples to be added to the input signal prior to filtering is given by the following formula: N=L−12N=L−12 The 
 N extra samples are obtained by repeating the last sample value of the input signal 
 N times to ensure signal continuity.

Parent topic:

Demodulation Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-demodulate-cpm.html language=enus -->
## TOPIC 00033: MT Demodulate CPM

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-demodulate-cpm.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-demodulate-cpm.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates a continuous-phase modulation (CPM)-modulated complex baseband waveform and returns the time-aligned demodulated waveform, the demodulated information bit stream, and measurement results obtained during demodulation. This node attempts to remove carrier and phase offset by locking to the

MT Demodulate CPM

Demodulates a continuous-phase modulation (CPM)-modulated complex baseband waveform and returns the time-aligned demodulated waveform, the demodulated information bit stream, and measurement results obtained during demodulation. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Note

input complex waveform

samples per symbol

Note

recovered complex waveform

measurements

[IMAGE alt='1378' src='MethodCall.MT_Demodulate_CPM.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### CPM system parameters

Parameter values defining the CPM system. Wire the CPM system parameters cluster of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol map

A two-dimensional array of desired frequency deviations. Each column corresponds to a symbol, with the binary representation of the column index being the mapped bit-representation of the symbol. Each row corresponds to a modulation index in the order in which it appears in the modulation index, h(i) parameter of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map).

Default value: Empty array

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing the desired matched filter coefficients. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the matched samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the samples per symbol element of the CPM system parameters cluster that is passed to this node.

##### Dependency on reset? Input

When reset? is set to TRUE, there is a transient response of half the filter length at the start of the demodulated signal, and the returned data is shortened by approximately half the filter length. When reset? is set to FALSE, the VI uses data from the previous iteration to prime the filter, hence eliminating the transient.

Tip

reset?

L/2

P/2

K

K

L

P

K

L

P

K

reset?

synchronization parameters.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### synchronization parameters

Parameter values describing the synchronization sequence and the range of bits over which to search for the sequence. Wire the CPM synchronization parameters cluster returned by MT Generate CPM Synchronization Parameters (bit array) or MT Generate CPM Synchronization Parameters (number array) to this cluster.

Note

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern. Although the data type is complex, only the real portion is used.

The real portion of the mapped symbols is the frequency deviation of the symbol value, and the imaginary portion is 0. To prevent false synchronization, configure this pattern so that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### pulse shaping filter coefficients

An ordered array containing the desired pulse-shaping coefficients. This parameter is used to reproduce the ideal waveform for performing measurements. Wire the 
pulse shaping filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the 
pulse shaping samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the 
samples per symbol parameter of the 
CPM system parameters cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulating using the previous iteration states.

| TRUE | Restarts the demodulator. The node resets on the first call and when reset? is set to TRUE. |
| --- | --- |
| FALSE | Continues demodulating using the previous iteration states. The input complex waveform is contiguous with the input complex waveform from the previous iteration of this node. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### detected complex waveform

The ideal oversampled waveform corresponding to the output bit stream. Wire this parameter to the detected complex waveform parameter of MT Measure CPM Quadrature Impairments.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after frequency offset correction and phase offset correction. The frequency offset and phase offset corrections are scalar values applied to the entire block.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The demodulated information bit stream.

Note

2,1,...

0,1,1,0...

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### measurements

Measurements performed by the demodulator.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency offset

The measured carrier frequency offset, in hertz (Hz). The measured frequency offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency drift

The measured carrier frequency drift, in Hz. The measured frequency drift is not removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### phase offset

The measured phase offset, in degrees. The measured phase offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sync found index

Symbol index within the input complex waveform where the peak correlation to the sync sequence was found. If no sync sequence is specified in the synchronization parameters cluster, the sync found index parameter returns the offset from the start of the input complex waveform to the first complete symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Demodulator Performance

Tip

#### Filter Delay

Finite impulse response (FIR) filters are used for different operations such as pulse-shaping, matched filtering, and downconversion filtering. For such filters, the output signal is related to the input signal as shown by the following equation:

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

where

P is the filter order

x[n] is the input signal

y[n] is the output signal

b
 <sub>i</sub> are the filter coefficients

The initial state for all samples in an FIR filter is 0. The filter output until the first input sample reaches the middle tap (the first causal sample) is called the transient response, or filter delay. For an FIR filter that has 
 N taps, the delay is (N-1)/2 samples. This relationship is illustrated in the following figure, where a sine wave is filtered by an FIR filter with 50 taps.

[IMAGE alt='1378' src='GUID-FBE65DFB-5758-4539-ACE6-66570B6DE08D-a5.png']

#### Recovering Samples in Single-Shot Operations

In single-shot operations for modulators and demodulators, the filter delay is truncated before the signal is generated because these samples are not valid. Some samples at the end of the block do not appear at the modulator or demodulator output, and hence appear to have been lost.

- For modulation: Let 
 L be the pulse-shaping filter length, 
 m be the number of samples per symbol, and 
 M be the modulation order. The number of bits to be added to the input bit stream is given by the following formula: N=(L−1)log⁡2MmN=(L−1)log⁡2Mm
- For demodulation: Demodulation use filters during matched filtering. Let 
 L be the length of the matched filter. The number of samples to be added to the input signal prior to filtering is given by the following formula: N=L−12N=L−12 The 
 N extra samples are obtained by repeating the last sample value of the input signal 
 N times to ensure signal continuity.

Parent topic:

Demodulation Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-demodulate-pm.html language=enus -->
## TOPIC 00034: MT Demodulate PM

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-demodulate-pm.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-demodulate-pm.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs phase demodulation on the incoming I/Q signal. PM modulated waveform The baseband (downconverted) time-domain data for demodulation. t0 The trigger (start) time of the acquired signal. Default value: 0.0 dt Time interval between data points in the acquired signal. Default value: 1.0 Y The c

MT Demodulate PM

Performs phase demodulation on the incoming I/Q signal.

[IMAGE alt='1378' src='MethodCall.MT_Demodulate_PM.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PM modulated waveform

The baseband (downconverted) time-domain data for demodulation.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

The trigger (start) time of the acquired signal.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the acquired signal.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued time-domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### phase deviation

A value that indicates how to scale the PM demodulated waveform. You can set this value to 1.0 or to the expected phase deviation of the incoming PM signal for demodulation.

- Set this value to 1.0 to return a PM demodulated waveform in degrees with no scaling. In this case, the maximum amplitude of the PM demodulated waveform is equal to the actual phase deviation of the incoming PM signal.
- Set this value equal to the expected phase deviation of the incoming PM signal to divide the PM demodulated waveform by this value. You can use the resulting scaled PM demodulated waveform to quantify the degree of error between the expected phase deviation and the actual phase deviation.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### carrier correction?

A Boolean that determines whether to enable carrier correction.

| TRUE | Determines a linear correction to the carrier frequency estimate and compensates for it in the FM demodulated waveform. |
| --- | --- |
| FALSE | Carrier correction is not enabled. Use this option when performing continuous acquisition. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether initialization of an internal node state tracks the ending phase.

| TRUE | The node clears the state information about each call. |
| --- | --- |
| FALSE | The node uses the final phase from the previous call as the starting phase for the next call, ensuring phase continuity between calls. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### PM demodulated waveform

The phase-demodulated information signal.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### carrier offset

The offset, in hertz (Hz), between the incoming modulated carrier frequency and the estimated carrier frequency.

carrier correction?

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### PM Demodulation

This node computes the information signal as a result of the demodulation and returns the data in the PM demodulated waveform.

Parent topic:

Demodulation Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-demodulate-psk.html language=enus -->
## TOPIC 00035: MT Demodulate PSK

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-demodulate-psk.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-demodulate-psk.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates a phase-shift keying (PSK) modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, the demodulated bit stream, and measurement results obtained during demodulation. This node attempts to remove carrier and phase offset by locking to the carrier sign

MT Demodulate PSK

Demodulates a phase-shift keying (PSK) modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, the demodulated bit stream, and measurement results obtained during demodulation. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Note

input complex waveform

samples per symbol

Note

recovered complex waveform

measurements

[IMAGE alt='1378' src='MethodCall.MT_Demodulate_PSK.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PSK system parameters

Parameter values defining the PSK system. Wire the PSK system parameters cluster of MT Generate PSK System Parameters (M) or MT Generate PSK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each Boolean symbol to its desired coordinates in the complex plane. The number of states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### differential PSK

Status of the differential PSK.

| disable | Disables bit sequence encoding. |
| --- | --- |
| enable | Enables bit sequence encoding. |

Default value: 
 enable

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing the desired matched filter coefficients. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the matched samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the samples per symbol element of the PSK system parameters cluster passed to this node.

##### Dependency on reset? Input

When reset? is set to TRUE, there is a transient response of half the filter length at the start of the demodulated signal, and the returned data is shortened by approximately half the filter length. When reset? is set to FALSE, the node uses data from the previous iteration to eliminate the transient.

Tip

reset?

L

K

K

L

K

L

K

reset?

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### synchronization parameters

Parameter values describing the synchronization sequence and the range of bits over which to search for this sequence. Wire the PSK synchronization parameters cluster returned by the PSK bit array or number array instances of MT Generate Synchronization Parameters to this cluster.

Note

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern used to synchronize the bit stream. To prevent false synchronization, select this pattern such that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated, but there is a phase ambiguity in the recovered symbols.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### pulse shaping filter coefficients

An ordered array containing the desired pulse shaping coefficients. This parameter is used to remodulate the bit stream to perform measurements. Wire the pulse shaping filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the pulse shaping samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the samples per symbol element of the PSK system parameters cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulating using the previous iteration states.

| TRUE | Restarts the demodulator. The node resets on the first call and when reset? is set to TRUE. |
| --- | --- |
| FALSE | Continues demodulating using the previous iteration states. The input complex waveform is contiguous with the input complex waveform from the previous iteration of this node. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. The frequency offset and phase offset corrections are scalar values applied to the entire block.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Time of the first value in the Y array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The demodulated information bit stream.

Note

2,1,...

0,1,1,0...

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### measurements

Measurements performed by the demodulator.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency offset

The measured carrier frequency offset, in hertz (Hz). The measured frequency offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency drift

The measured carrier frequency drift, in Hz. The measured frequency drift is not removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### phase offset

The measured phase offset, in degrees. The measured phase offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sync found index

Symbol index within the input complex waveform where the peak correlation to the sync sequence was found. If no sync sequence is specified in the synchronization parameters cluster, the sync found index parameter returns the offset from the start of the input complex waveform to the first complete symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Offset PSK Mode

Offset PSK mode is only supported for 4-PSK (OQPSK), and setting psk type to offset requires some form of band-limiting filtration. Raised cosine and root-raised cosine are the only valid filter types for OQPSK demodulation. Demodulator locking performance degrades with alpha values <0.3 in the raised cosine or root-raised cosine filter design. Set the PSK type parameter to offset in MT Generate PSK System Parameters (M) or MT Generate PSK System Parameters (Map) to access this mode.

#### Matched Filter Demodulation

If the matched filter used in demodulation has a large number of significant taps, the recovered complex waveform might have some transients at the beginning when the reset? parameter is set to TRUE. This results in a few distorted constellation points if the constellation is plotted from the recovered complex waveform after suitable decimation. In such cases, NI recommends deleting the initial part of the recovered complex waveform for a length equal to the length of the matched filter.

#### Successful Locking

Successful locking depends on many factors, including signal quality, modulation type, filtering parameters, and acquisition size. Locking also requires a fairly uniform distribution of symbols in the signal. The demodulator lock rate increases (and failures decrease) as the number of symbols demodulated increases. In general, you can expect to achieve a better than 95% lock when demodulating 10 × 
 M number of symbols, where 
 M is 2<sup>bits per symbol</sup>.

#### Filter Delay

Finite impulse response (FIR) filters are used for different operations such as pulse-shaping, matched filtering, and downconversion filtering. For such filters, the output signal is related to the input signal as shown by the following equation:

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

where

P is the filter order

x[n] is the input signal

y[n] is the output signal

b
 <sub>i</sub> are the filter coefficients

The initial state for all samples in an FIR filter is 0. The filter output until the first input sample reaches the middle tap (the first causal sample) is called the transient response, or filter delay. For an FIR filter that has 
 N taps, the delay is (N-1)/2 samples. This relationship is illustrated in the following figure, where a sine wave is filtered by an FIR filter with 50 taps.

[IMAGE alt='1378' src='GUID-FBE65DFB-5758-4539-ACE6-66570B6DE08D-a5.png']

#### Recovering Samples in Single-Shot Operations

In single-shot operations for modulators and demodulators, the filter delay is truncated before the signal is generated because these samples are not valid. Some samples at the end of the block do not appear at the modulator or demodulator output, and hence appear to have been lost.

- For modulation: Let 
 L be the pulse-shaping filter length, 
 m be the number of samples per symbol, and 
 M be the modulation order. The number of bits to be added to the input bit stream is given by the following formula: N=(L−1)log⁡2MmN=(L−1)log⁡2Mm
- For demodulation: Demodulation use filters during matched filtering. Let 
 L be the length of the matched filter. The number of samples to be added to the input signal prior to filtering is given by the following formula: N=L−12N=L−12 The 
 N extra samples are obtained by repeating the last sample value of the input signal 
 N times to ensure signal continuity.

Parent topic:

Demodulation Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-demodulate-qam.html language=enus -->
## TOPIC 00036: MT Demodulate QAM

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-demodulate-qam.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-demodulate-qam.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates a quadrature-amplitude modulation (QAM)-modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, the demodulated bit stream, and the results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the car

MT Demodulate QAM

Demodulates a quadrature-amplitude modulation (QAM)-modulated complex baseband waveform and returns the time-aligned oversampled complex waveform, the demodulated bit stream, and the results of offset and drift measurements. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Note

input complex waveform

samples per symbol

Note

recovered complex waveform

measurements

[IMAGE alt='1378' src='MethodCall.MT_Demodulate_QAM.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### QAM system parameters

Parameter values defining the QAM system. Wire the QAM system parameters cluster of MT Generate QAM System Parameters (M) or MT Generate QAM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired coordinates in the complex plane. The number of QAM states in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing the desired matched filter coefficients. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the matched samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the samples per symbol element of the QAM system parameters cluster passed to this node.

##### Dependency on reset? Input

When reset? is set to TRUE, there is a transient response of half the filter length at the start of the demodulated signal, and the returned data is shortened by approximately half the filter length. When reset? is set to FALSE, the node uses data from the previous iteration to eliminate the transient.

Tip

reset?

L

K

K

L

K

L

K

reset?

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### synchronization parameters

Parameter values describing the synchronization sequence and the range of bits over which to search for this sequence. Wire the QAM synchronization parameters cluster returned by MT Generate QAM Synchronization Parameters (bit array) or MT Generate QAM Synchronization Parameters (number array) to this cluster.

Note

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern used to synchronize the bit stream. To prevent false synchronization, select this pattern such that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated, but there is a phase ambiguity in the recovered symbols.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulating using the previous iteration states.

| TRUE | Restarts the demodulator. The node resets on the first call and when reset? is set to TRUE. |
| --- | --- |
| FALSE | Continues demodulating using the previous iteration states. The input complex waveform is contiguous with the input complex waveform from the previous iteration of this node. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. The frequency offset and phase offset corrections are scalar values applied to the entire block.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Time of the first value in the Y array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data values in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The demodulated information bit stream.

Note

2,1,...

0,1,1,0...

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### measurements

Measurements performed by the demodulator.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency offset

The measured carrier frequency offset, in hertz (Hz). The measured frequency offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency drift

The measured carrier frequency drift, in Hz. The measured frequency drift is not removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### phase offset

The measured phase offset, in degrees. The measured phase offset is removed from the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sync found index

Symbol index within the input complex waveform where the peak correlation to the sync sequence was found. If no sync sequence is specified in the synchronization parameters cluster, the sync found index parameter returns the offset from the start of the input complex waveform to the first complete symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Matched Filter Demodulation

If the matched filter used in demodulation has a large number of significant taps, the recovered complex waveform might have some transients at the beginning when the reset? parameter is set to TRUE. This results in a few distorted constellation points if the constellation is plotted from the recovered complex waveform after suitable decimation. In such cases, NI recommends deleting the initial part of the recovered complex waveform for a length equal to the length of the matched filter.

#### Successful Locking

Successful locking depends on many factors, including signal quality, modulation type, filtering parameters, and acquisition size. Locking also requires a fairly uniform distribution of symbols in the signal. The demodulator lock rate increases (and failures decrease) as the number of symbols demodulated increases. In general, you can expect to achieve a better than 95% lock when demodulating 10 × 
 M number of symbols, where 
 M is 2<sup>bits per symbol</sup>.

#### Filter Delay

Finite impulse response (FIR) filters are used for different operations such as pulse-shaping, matched filtering, and downconversion filtering. For such filters, the output signal is related to the input signal as shown by the following equation:

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

where

P is the filter order

x[n] is the input signal

y[n] is the output signal

b
 <sub>i</sub> are the filter coefficients

The initial state for all samples in an FIR filter is 0. The filter output until the first input sample reaches the middle tap (the first causal sample) is called the transient response, or filter delay. For an FIR filter that has 
 N taps, the delay is (N-1)/2 samples. This relationship is illustrated in the following figure, where a sine wave is filtered by an FIR filter with 50 taps.

[IMAGE alt='1378' src='GUID-FBE65DFB-5758-4539-ACE6-66570B6DE08D-a5.png']

#### Recovering Samples in Single-Shot Operations

In single-shot operations for modulators and demodulators, the filter delay is truncated before the signal is generated because these samples are not valid. Some samples at the end of the block do not appear at the modulator or demodulator output, and hence appear to have been lost.

- For modulation: Let 
 L be the pulse-shaping filter length, 
 m be the number of samples per symbol, and 
 M be the modulation order. The number of bits to be added to the input bit stream is given by the following formula: N=(L−1)log⁡2MmN=(L−1)log⁡2Mm
- For demodulation: Demodulation use filters during matched filtering. Let 
 L be the length of the matched filter. The number of samples to be added to the input signal prior to filtering is given by the following formula: N=L−12N=L−12 The 
 N extra samples are obtained by repeating the last sample value of the input signal 
 N times to ensure signal continuity.

Parent topic:

Demodulation Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-depermute.html language=enus -->
## TOPIC 00037: MT DePermute

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-depermute.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-depermute.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rearranges or depermutes the permuted data. data in The input data to depermute so that the generated data is the same as the MT Permute. permutation array An array with elements that define the location of the output data samples of the MT Permute. You can use this array to track the locations of e

MT DePermute

Rearranges or depermutes the permuted data.

[IMAGE alt='1378' src='MethodCall.MT_DePermute.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### data in

The input data to depermute so that the generated data is the same as the MT Permute.

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### permutation array

An array with elements that define the location of the output data samples of the MT Permute. You can use this array to track the locations of elements in the original data input to MT Permute.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines how this node handles buffered data.

| TRUE | Clears the buffered data, checks the input parameters on a first call, and reflects any change in the input parameter values during subsequent iterations. |
| --- | --- |
| FALSE | Adds the buffered data to the beginning of data from next iteration, in continuous operations. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### data out

The depermuted data returned by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Theoretical Example of the Depermutation Operation

The following is a theoretical example of the depermutation operation.

If the data in array is 9,21,13,7,17, and the permutation array is 3,2,4,0,1, the data out array would be 7,13,17,9,2, as illustrated in the following figure.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

Parent topic:

DeInterleaving Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-depuncture-data-stream.html language=enus -->
## TOPIC 00038: MT Depuncture Data Stream

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-depuncture-data-stream.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-depuncture-data-stream.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts an erasure value inside the punctured input data stream. The erasure value is equivalent to inserting a null symbol in the position of the input data stream that was previously punctured using MT Puncture Data Stream. This node accepts the double data type as input, because the input data st

MT Depuncture Data Stream

Inserts an erasure value inside the punctured input data stream. The erasure value is equivalent to inserting a null symbol in the position of the input data stream that was previously punctured using MT Puncture Data Stream.

Note

input data stream

erasure value

[IMAGE alt='1378' src='MethodCall.MT_Depuncture_Data_Stream.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### input data stream

The data stream with a rate to be increased by the process of depuncturing. This data stream is usually obtained from the output of a block or convolutional encoder.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### puncture pattern

A binary-valued matrix that determines which elements in the input data stream are omitted.

Note

input data stream

m×n

m

m

input data stream

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### erasure value

The symbol value to be inserted into the punctured data stream before decoding. The erasure value is equivalent to inserting a null symbol in the position of the input data stream that was previously punctured using MT Puncture Data Stream.

Note

n

soft

erasure value

n

soft

erasure value

n

soft

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether this node uses the stored state information from a previous iteration while depuncturing the input data stream in the current iteration.

Note

L

input data
 stream

puncture pattern

L

| TRUE | Clears all previous state information and reinitializes the buffers. |
| --- | --- |
| FALSE | Uses the stored state information from the previous iteration while depuncturing the input data stream in the current iteration. The buffered elements are added to the beginning of the input data stream during the next iteration, prior to the depuncturing operation. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### output data stream

The data stream returned by this node, which consists of all elements in the input data stream in addition to those that were inserted during the depuncturing operation.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Decoding Nodes

Parent topic:

Decoding Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-despread-symbols.html language=enus -->
## TOPIC 00039: MT Despread Symbols

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-despread-symbols.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-despread-symbols.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the direct sequence spread spectrum (DSSS) despreading operation on a spread sequence of data bits. input chip stream The sequence of data chips to despread. spreading code The sequence of bits that determine how the bits in input bit stream are spread. sync confidence threshold The minimum

MT Despread Symbols

Performs the direct sequence spread spectrum (DSSS) despreading operation on a spread sequence of data bits.

[IMAGE alt='1378' src='MethodCall.MT_Despread_Symbols.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input chip stream

The sequence of data chips to despread.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### spreading code

The sequence of bits that determine how the bits in input bit stream are spread.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sync confidence threshold

The minimum correlation required for which you can consider input chip stream to be synchronized with the spreading code. Configure this parameter only if you set reset? to be TRUE. Valid values are between 0.0 (no correlation required) to 1.0 (perfect correlation required), inclusive.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync search depth

The desired number of bits (not chips) over which to search for a sync confidence metric greater than the sync confidence threshold. This parameter is only applicable when reset? is set to TRUE.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether this node synchronizes despreading at each call using the sync search depth and sync confidence threshold parameters.

| TRUE | Synchronizes despreading at each call using the sync search depth and sync confidence threshold parameters. |
| --- | --- |
| FALSE | Ignores the values of sync search depth and sync confidence threshold and continues despreading from the previous iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The despread series of bits returned by this node.

Note

output bit stream

L

input chip stream

L

spreading code

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### sync found index

The synchronization index of the synchronization sequence found within the input chip stream. This parameter returns -1 if no sync is found.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sync confidence metric

The measured confidence metric when input chip stream is aligned using the sync found index. Valid values are 0.0 (0% measured confidence) to 1.0 (100% measured confidence), inclusive.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Direct Sequence Spread Spectrum (DSSS)

Direct Sequence Spread Spectrum (DSSS) is a process by which data is transmitted using a higher bandwidth signal as required by the data rate. Using DSSS allows multiple channels to occupy the same bandwidth, thus mitigating interference from other users at the expense of bandwidth expansion.

DSSS spreads each bit of signal data at the transmitter into 
 L chips using a pseudorandom L-chip spreading code called a code word. The length 
 L of the pseudorandom spreading code is also known as the bandwidth expansion factor because the chips are transmitted at a rate equal to 
 L * bit rate of the data. The spreading code appears random to all receivers except the intended one, which uses the knowledge of the spreading code to demodulate and recover the transmitted information. Thus, multiple channels can occupy the same portion of the frequency spectrum by using code words that have little or no correlation with one another, and little or no autocorrelation for any shift other than zero.

Mathematically, a DSSS signal is described by

y

(

t

)

=

∑

n

=

−

∞

∞

∑

m

=

0

L

−

1

a

n

⁢

c

m

g

(

T

−

n

T

−

m

T

c

)

y

(

t

)

=

∑

n

=

−

∞

∞

∑

m

=

0

L

−

1

a

n

⁢

c

m

g

(

T

−

n

T

−

m

T

c

)

where

y(T) is the transmitted DSSS signal

g(T) is the pulse-shaping signal of duration 
 T<sub>c</sub>

a
 <sub>n</sub> is the n<sup>th</sup> information bearing symbol

c
 <sub>m</sub> is the m<sup>th</sup> element of the L-long pseudorandom spreading code (also known as the chip sequence)

T
 <sub>c</sub> is the chip period

T = L * T<sub>c</sub> is the symbol period

Parent topic:

Decoding Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-detect-ask.html language=enus -->
## TOPIC 00040: MT Detect ASK

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-detect-ask.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-detect-ask.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates an amplitude-shift keying (ASK)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal. MT Detect ASK returns only the demodulated bit stream. Use MT Demodulate ASK to acquire the

MT Detect ASK

Demodulates an amplitude-shift keying (ASK)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Note

Note

input complex waveform

samples per symbol

[IMAGE alt='1378' src='MethodCall.MT_Detect_ASK.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### ASK system parameters

Parameter values defining the ASK system. Wire the ASK system parameters cluster of MT Generate ASK System Parameters (M) or MT Generate ASK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of ASK levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### synchronization parameters

Parameter values describing the synchronization sequence and the range of bits over which to search for this sequence. Wire the ASK synchronization parameters cluster returned by MT Generate ASK Synchronization Parameters (bit array) or MT Generate ASK Synchronization Parameters (number array) to the synchronization parameters cluster.

Note

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern used to synchronize the bit stream. To prevent false synchronization, select this pattern such that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated, but there is a phase ambiguity in the recovered symbols.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing the desired matched filter coefficients. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the matched samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the samples per symbol element of the ASK system parameters cluster that is passed to MT Demodulate ASK.

Note

reset?

reset?

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulating using the previous iteration states.

| TRUE | Restarts the demodulator. The node resets on the first call and when reset? is set to TRUE. |
| --- | --- |
| FALSE | Continues demodulating using the previous iteration states. The input complex waveform is contiguous with the input complex waveform from the previous iteration of this node. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### flush buffers?

A Boolean that determines whether to flush samples from the input complex waveform that are delayed due to the FIR filters used in the demodulation algorithm. Set this parameter to TRUE during single-shot operations and during the last iteration of continuous operations.

| TRUE | Destroys the internal states of the algorithms such that you cannot perform continuous processing on the signal during subsequent iterations. If flush buffers? is set to TRUE, you must set reset? to TRUE on the subsequent iteration. |
| --- | --- |
| FALSE | Stores the internal states of the algorithms so that you can perform continuous processing on the signal during subsequent iterations. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The demodulated information bit stream.

Note

2,1,...

0,1,1,0...

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sync found index

Symbol index within the input complex waveform where the peak correlation to the sync sequence was found. If no sync sequence is specified in the synchronization parameters cluster, the sync found index parameter returns the offset from the start of the input complex waveform to the first complete symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Successful Locking

Successful locking depends on many factors, including signal quality, modulation type, filtering parameters, and acquisition size. Locking also requires a fairly uniform distribution of symbols in the signal. The demodulator lock rate increases (and failures decrease) as the number of symbols demodulated increases. In general, you can expect to achieve a better than 95% lock when demodulating 10 × 
 M number of symbols, where 
 M is 2<sup>bits per symbol</sup>.

Parent topic:

Bit Recovery Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-detect-qam.html language=enus -->
## TOPIC 00041: MT Detect QAM

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-detect-qam.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-detect-qam.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Demodulates a quadrature-amplitude modulation (QAM)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal. MT Detect QAM returns only the demodulated bit stream. Use MT Demodulate QAM to acqu

MT Detect QAM

Demodulates a quadrature-amplitude modulation (QAM)-modulated complex baseband waveform and returns the demodulated bit stream. This node attempts to remove carrier and phase offset by locking to the carrier signal.

Note

Note

input complex waveform

samples per symbol

[IMAGE alt='1378' src='MethodCall.MT_Detect_QAM.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The modulated complex baseband waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### QAM system parameters

Parameter values defining the QAM system. Wire the QAM system parameters cluster of MT Generate QAM System Parameters (M) or MT Generate QAM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired coordinates in the complex plane. The number of QAM states in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### synchronization parameters

Parameter values describing the synchronization sequence and the range of bits over which to search for this sequence. Wire the QAM synchronization parameters cluster returned by MT Generate QAM Synchronization Parameters (bit array) or MT Generate QAM Synchronization Parameters (number array) to this cluster.

Note

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern used to synchronize the bit stream. To prevent false synchronization, select this pattern such that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated, but there is a phase ambiguity in the recovered symbols.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### matched filter coefficients

An ordered array containing the desired matched filter coefficients. Wire the matched filter coefficients parameter of MT Generate Filter Coefficients to this parameter. When generating the filter coefficients, ensure that the value of the matched samples per symbol parameter of MT Generate Filter Coefficients is equal to the value of the samples per symbol element of the QAM system parameters cluster passed to this node.

##### Dependency on reset? Input

When reset? is set to TRUE, there is a transient response of half the filter length at the start of the demodulated signal, and the returned data is shortened by approximately half the filter length. When reset? is set to FALSE, the node uses data from the previous iteration to eliminate the transient.

Tip

reset?

L

K

K

L

K

L

K

reset?

synchronization parameters

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the node continues demodulating using the previous iteration states.

| TRUE | Restarts the demodulator. The node resets on the first call and when reset? is set to TRUE. |
| --- | --- |
| FALSE | Continues demodulating using the previous iteration states. The input complex waveform is contiguous with the input complex waveform from the previous iteration of this node. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### flush buffers?

A Boolean that determines whether to flush samples from the input complex waveform that are delayed due to the FIR filters used in the demodulation algorithm. Set this parameter to TRUE during single-shot operations and during the last iteration of continuous operations.

| TRUE | Destroys the internal states of the algorithms such that you cannot perform continuous processing on the signal during subsequent iterations. If flush buffers? is set to TRUE, you must set reset? to TRUE on the subsequent iteration. |
| --- | --- |
| FALSE | Stores the internal states of the algorithms so that you can perform continuous processing on the signal during subsequent iterations. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The demodulated information bit stream.

Note

2,1,...

0,1,1,0...

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sync found index

Symbol index within the input complex waveform where the peak correlation to the sync sequence was found. If no sync sequence is specified in the synchronization parameters cluster, the sync found index parameter returns the offset from the start of the input complex waveform to the first complete symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Successful Locking

Successful locking depends on many factors, including signal quality, modulation type, filtering parameters, and acquisition size. Locking also requires a fairly uniform distribution of symbols in the signal. The demodulator lock rate increases (and failures decrease) as the number of symbols demodulated increases. In general, you can expect to achieve a better than 95% lock when demodulating 10 × 
 M number of symbols, where 
 M is 2<sup>bits per symbol</sup>.

Parent topic:

Bit Recovery Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-downconvert-passband-complex.html language=enus -->
## TOPIC 00042: MT Downconvert Passband (Complex)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-downconvert-passband-complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-downconvert-passband-complex.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Downconverts a complex baseband signal, which is centered around a non-zero center frequency, to a center frequency of zero. This node can be used in simulated as well as hardware-equipped applications. complex waveform Signal for downconversion in passband form. t0 The trigger (start) time of the a

MT Downconvert Passband (Complex)

Downconverts a complex baseband signal, which is centered around a non-zero center frequency, to a center frequency of zero.
 This node can be used in simulated as well as hardware-equipped applications.

[IMAGE alt='1378' src='MethodCall.MT_Downconvert_Passband_(Complex).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### complex waveform

Signal for downconversion in passband form.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

The trigger (start) time of the acquired signal.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the acquired signal.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex array representing the signal for downconversion.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### carrier frequency

The center frequency of the passband, in hertz (Hz). This frequency is downconverted to 0 Hz. Enter the expected carrier frequency of the incoming signal for downconversion.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### passband bandwidth

The bandwidth, in Hz, of the passband signal data. The node ignores this parameter if you set the reset? parameter to FALSE.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### advanced filter parameters

Filter parameters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### passband ripple

The ripple in the passband, in dB. The ripple is the ratio of the maximum deviation from the average passband amplitude to the average passband amplitude. The value must be greater than zero.

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### stopband start

The start of the stopband, Hz.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### compute filter stopband ?

A Boolean that determines whether to compute the stopband start or use the value that you specify in the stopband start parameter.

| TRUE | Computes the stopband start based on the carrier frequency and passband bandwidth parameters. |
| --- | --- |
| FALSE | Uses the value that you specify in the stopband start parameter. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### stopband gain

The stopband gain, in dB. The gain is the negative of the minimum attenuation of the stopband with respect to the average amplitude of the passband.

Default value: -96

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to use values specified by the initial phase, passband bandwidth, enable filter, passband ripple, and stopband start parameters.

| TRUE | The node uses these parameter values at each call. |
| --- | --- |
| FALSE | The node ignores these parameters and continues using values supplied in the previous call. Reusing previous input values is useful when sequential data blocks represent contiguous signal data. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### initial phase

The initial phase, in degrees, of the software local oscillator used in the downconversion process. The node ignores this parameter if you set the reset? parameter to FALSE. Use the initial phase parameter to match the phase of the incoming modulated carrier and the local oscillator(s) of the downconversion process.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable filter

A Boolean that determines whether to perform software filtration on the downconverted data.

| TRUE | The node filters the downconverted waveform parameter using a software FIR filter. |
| --- | --- |
| FALSE | Disables the downconversion filter and generates unfiltered data in the downconverted waveform parameter. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### downconverted waveform

The downconverted signal in complex envelope format.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

The trigger (start) time of the acquired signal.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued time-domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### ripple

The deviation of the passband gain from the nominal gain of 0 dB.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### filter length

Number of taps in the filter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Downconversion Filter

enable filter

- If carrier frequency is greater than passband bandwidth , the filter stopband begins at carrier frequency.
- If carrier frequency is less than passband bandwidth , the filter stopband begins between carrier frequency and (2 * carrier frequency) - (passband bandwidth/2).

#### Filter Delay

Finite impulse response (FIR) filters are used for different operations such as pulse-shaping, matched filtering, and downconversion filtering. For such filters, the output signal is related to the input signal as shown by the following equation:

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

where

P is the filter order

x[n] is the input signal

y[n] is the output signal

b
 <sub>i</sub> are the filter coefficients

The initial state for all samples in an FIR filter is 0. The filter output until the first input sample reaches the middle tap (the first causal sample) is called the transient response, or filter delay. For an FIR filter that has 
 N taps, the delay is (N-1)/2 samples. This relationship is illustrated in the following figure, where a sine wave is filtered by an FIR filter with 50 taps.

[IMAGE alt='1378' src='GUID-FBE65DFB-5758-4539-ACE6-66570B6DE08D-a5.png']

#### Recovering Samples in Single-Shot Operations

In single-shot operations for modulators and demodulators, the filter delay is truncated before the signal is generated because these samples are not valid. Some samples at the end of the block do not appear at the modulator or demodulator output, and hence appear to have been lost.

- For modulation: Let 
 L be the pulse-shaping filter length, 
 m be the number of samples per symbol, and 
 M be the modulation order. The number of bits to be added to the input bit stream is given by the following formula: N=(L−1)log⁡2MmN=(L−1)log⁡2Mm
- For demodulation: Demodulation use filters during matched filtering. Let 
 L be the length of the matched filter. The number of samples to be added to the input signal prior to filtering is given by the following formula: N=L−12N=L−12 The 
 N extra samples are obtained by repeating the last sample value of the input signal 
 N times to ensure signal continuity.

Parent topic:

MT Downconvert Passband

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-downconvert-passband-real.html language=enus -->
## TOPIC 00043: MT Downconvert Passband (Real)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-downconvert-passband-real.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-downconvert-passband-real.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Downconverts real passband signal data of a user-specified bandwidth. This node can be used in simulated as well as hardware-equipped applications. waveform Signal for downconversion in passband form. carrier frequency The center frequency of the passband, in hertz (Hz). This frequency is downconver

MT Downconvert Passband (Real)

Downconverts real passband signal data of a user-specified bandwidth.
 This node can be used in simulated as well as hardware-equipped applications.

[IMAGE alt='1378' src='MethodCall.MT_Downconvert_Passband_(Real).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Signal for downconversion in passband form.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### carrier frequency

The center frequency of the passband, in hertz (Hz). This frequency is downconverted to 0 Hz. Enter the expected carrier frequency of the incoming signal for downconversion.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### passband bandwidth

The bandwidth, in Hz, of the passband signal data. The node ignores this parameter if you set the reset? parameter to FALSE.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### advanced filter parameters

Filter parameters.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### passband ripple

The ripple in the passband, in dB. The ripple is the ratio of the maximum deviation from the average passband amplitude to the average passband amplitude. The value must be greater than zero.

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### stopband start

The start of the stopband, Hz.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### compute filter stopband ?

A Boolean that determines whether to compute the stopband start or use the value that you specify in the stopband start parameter.

| TRUE | Computes the stopband start based on the carrier frequency and passband bandwidth parameters. |
| --- | --- |
| FALSE | Uses the value that you specify in the stopband start parameter. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### stopband gain

The stopband gain, in dB. The gain is the negative of the minimum attenuation of the stopband with respect to the average amplitude of the passband.

Default value: -96

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to use values specified by the initial phase, passband bandwidth, enable filter, passband ripple, and stopband start parameters.

| TRUE | The node uses these parameter values at each call. |
| --- | --- |
| FALSE | The node ignores these parameters and continues using values supplied in the previous call. Reusing previous input values is useful when sequential data blocks represent contiguous signal data. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### initial phase

The initial phase, in degrees, of the software local oscillator used in the downconversion process. The node ignores this parameter if you set the reset? parameter to FALSE. Use the initial phase parameter to match the phase of the incoming modulated carrier and the local oscillator(s) of the downconversion process.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable filter

A Boolean that determines whether to perform software filtration on the downconverted data.

| TRUE | The node filters the downconverted waveform parameter using a software FIR filter. |
| --- | --- |
| FALSE | Disables the downconversion filter and generates unfiltered data in the downconverted waveform parameter. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### downconverted waveform

The downconverted signal in complex envelope format.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

The trigger (start) time of the acquired signal.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued time-domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### ripple

The deviation of the passband gain from the nominal gain of 0 dB.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### filter length

Number of taps in the filter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Downconversion Filter

enable filter

- If carrier frequency is greater than passband bandwidth , the filter stopband begins at carrier frequency.
- If carrier frequency is less than passband bandwidth , the filter stopband begins between carrier frequency and (2 * carrier frequency) - (passband bandwidth/2).

#### Filter Delay

Finite impulse response (FIR) filters are used for different operations such as pulse-shaping, matched filtering, and downconversion filtering. For such filters, the output signal is related to the input signal as shown by the following equation:

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

y

[

n

]

=

b

0

x

[

n

]

+

b

1

x

[

n

−

1

]

+

...

+

b

P

x

[

n

−

P

]

where

P is the filter order

x[n] is the input signal

y[n] is the output signal

b
 <sub>i</sub> are the filter coefficients

The initial state for all samples in an FIR filter is 0. The filter output until the first input sample reaches the middle tap (the first causal sample) is called the transient response, or filter delay. For an FIR filter that has 
 N taps, the delay is (N-1)/2 samples. This relationship is illustrated in the following figure, where a sine wave is filtered by an FIR filter with 50 taps.

[IMAGE alt='1378' src='GUID-FBE65DFB-5758-4539-ACE6-66570B6DE08D-a5.png']

#### Recovering Samples in Single-Shot Operations

In single-shot operations for modulators and demodulators, the filter delay is truncated before the signal is generated because these samples are not valid. Some samples at the end of the block do not appear at the modulator or demodulator output, and hence appear to have been lost.

- For modulation: Let 
 L be the pulse-shaping filter length, 
 m be the number of samples per symbol, and 
 M be the modulation order. The number of bits to be added to the input bit stream is given by the following formula: N=(L−1)log⁡2MmN=(L−1)log⁡2Mm
- For demodulation: Demodulation use filters during matched filtering. Let 
 L be the length of the matched filter. The number of samples to be added to the input signal prior to filtering is given by the following formula: N=L−12N=L−12 The 
 N extra samples are obtained by repeating the last sample value of the input signal 
 N times to ensure signal continuity.

Parent topic:

MT Downconvert Passband

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-downconvert-passband.html language=enus -->
## TOPIC 00044: MT Downconvert Passband

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-downconvert-passband.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-downconvert-passband.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Downconverts real passband signal data of a user-specified bandwidth.

MT Downconvert Passband

Downconverts real passband signal data of a user-specified bandwidth.

Analog and Digital Nodes

MT Downconvert Passband (Complex)

Downconverts a complex baseband signal, which is centered around a non-zero center frequency, to a center frequency of zero.

MT Downconvert Passband (Real)

Downconverts real passband signal data of a user-specified bandwidth.

Parent topic:

Analog and Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-format-constellation.html language=enus -->
## TOPIC 00045: MT Format Constellation

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-format-constellation.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-format-constellation.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Prepares a signal for presentation on a graph that shows the detected symbol locations and the transitions between those symbols. The node specifies a complex-valued waveform and displays a constellation plot of the waveform contents. This node assumes that the input waveform is a digitally modulate

MT Format Constellation

Prepares a signal for presentation on a graph that shows the detected symbol locations and the transitions between those symbols. The node specifies a complex-valued waveform and displays a constellation plot of the waveform contents.

This node assumes that the input waveform is a digitally modulated complex baseband signal containing samples that fall on symbol boundaries with a sample rate that is an integer multiple of the 
 samples per symbol value.

[IMAGE alt='1378' src='MethodCall.MT_Format_Constellation.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### waveform

Recovered modulated data for plotting as a constellation.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per symbol in the recovered waveform.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### constellation graph

A two-element array of XY data. Wire this parameter directly to an XY graph.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### constellation

An array of doubles representing the constellation plot.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### oversampled data

An array of doubles representing the oversampled data.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Use with Demodulation Nodes

Although this node performs no demodulation or frequency correction, you can use this node to examine the output of many of the digital demodulation nodes. In cases where the demodulator can recover symbol timing, the 
 output complex waveform parameter of the digital demodulation nodes contains a frequency-corrected signal appropriate for plotting using this node.

Parent topic:

Visualization Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-format-eye-diagram.html language=enus -->
## TOPIC 00046: MT Format Eye Diagram

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-format-eye-diagram.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-format-eye-diagram.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a complex- or real-valued waveform, divides it into segments, and displays those segments as plots on a waveform graph.

MT Format Eye Diagram

Specifies a complex- or real-valued waveform, divides it into segments, and displays those segments as plots on a waveform graph.

Visualization Nodes

MT Format Eye Diagram (complex)

symbol rate

eye length

MT Format Eye Diagram (WDT)

symbol rate

eye length

Parent topic:

Visualization Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-bits-galois-primitive.html language=enus -->
## TOPIC 00047: MT Generate Bits (Galois, Primitive Polynomial)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-bits-galois-primitive.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-bits-galois-primitive.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates Galois pseudonoise (PN) bit sequences. The node repeats the selected pattern until it generates the number of total bits that you specify. Use this node to specify the primitive polynomial that determines the connection structure of the linear feedback shift register (LFSR). total bits Tot

MT Generate Bits (Galois, Primitive Polynomial)

Generates Galois pseudonoise (PN) bit sequences. The node repeats the selected pattern until it generates the number of total bits that you specify. Use this node to specify the primitive polynomial that determines the connection structure of the linear feedback shift register (LFSR).

[IMAGE alt='1378' src='MethodCall.MT_Generate_Bits_(Galois,_Primitive_Polynomial).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### total bits

Total number of pseudorandom bits to be generated.

Default value: 128

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### specify primitive polynomial

The primitive polynomial for the PN bit sequence to be generated. The degree of the primitive polynomial determines the PN order.

The primitive polynomial is specified by an 8-bit signed integer array. If the degree of the primitive polynomial is 
 N, for example, 
 p(x) =a0 + 
 a1x + 
 a2x<sup>2</sup> +……+ 
 aNa<sup>N</sup>, the array contains (N + 1) elements. The first element is 
 a0, and the last element is 
 aN. Ensure that the polynomial you provide is a primitive polynomial. For example, if the primitive polynomial is 
 p(x) = 1 + 
 x<sup>14</sup> + 
 x<sup>15</sup>, then 
 N = 15, and the array contains 
 N + 1=16 elements.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### seed in

Initial state of the PN generator shift register.

Default value: -692093454

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to continue generating bits using the previous iteration states.

| TRUE | The PN generator has been initiated with a new PN seed. |
| --- | --- |
| FALSE | The PN sequence generator has resumed from where it had stopped during the previous iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The generated pseudorandom data bits.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### seed out

A seed for use in the seed in parameter during the next call to this node when reset? is set to FALSE.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Definition of Pseudorandom Sequences

Though deterministic in nature, seudorandom or pseudonoise (PN) sequences satisfy many properties of random numbers, such as autocorrelation, crosscorrelation, and so on. PN sequences are used in many applications and standards such as 802.11a and DVB. Some examples of PN sequences are maximal length shift register sequences, or 
 m-sequences, Gold sequences, and Kasami sequences. An m-sequence generates a periodic sequence of length

L

=

2

m

−

1

m-sequences

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

The preceding figure shows the Fibonacci and Galois implementations of m-sequences. As can be seen in these figures, m-sequences contain 
 m shift registers. The shift register set is filled with an m-bit initial seed that can be any value except 0. If the 
 m bits in the 
 m shift registers are all zero, then it is a degenerate case and the output of the generator is 0.

#### Examples of Fibonacci and Galois Implementation of Pseudorandom Sequences

The following examples demonstrate bit generation:

1. The first example depicts the Fibonacci implementation. This structure is used in different standards, including DVB. Inputs are specified as follows: 
 Primitive polynomial: 1+X14+X15 Initial seed: 
 000000010101001 The following figure shows the circuitry: SeedOutput0000000101010010+0=00000001010100100+0=00000010101001000+0=00000101010010000+0=00001010100100000+0=00010101001000000+0=00101010010000000+1=11010100100000011+0=1
2. The second example depicts the Galois implementation. Inputs are specified as follows: 
 Primitive polynomial: 1+X14+X15 Initial seed: 
 000000010101001 The circuitry is shown in the following figure: SeedOutput0000000101010010000000101010010000000101010010000000101010010000000101010010000000101010010000000101010010000000101010010000000111010010000000110010010000000110010010000000110010010000000110011010000000110011110000000110011100000000110011100000000110011100

Parent topic:

MT Generate Bits (poly)

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-bits-user-defined.html language=enus -->
## TOPIC 00048: MT Generate Bits (User Defined)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-bits-user-defined.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-bits-user-defined.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates bit sequences based on a pattern that you specify. The node repeats the selected pattern until it generates the number of bits that you specify. total bits Total number of pseudorandom bits to be generated. Default value: 128 seed in Initial state of the PN generator shift register. Defaul

MT Generate Bits (User Defined)

Generates bit sequences based on a pattern that you specify. The node repeats the selected pattern until it generates the number of bits that you specify.

[IMAGE alt='1378' src='MethodCall.MT_Generate_Bits_(User_Defined).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### total bits

Total number of pseudorandom bits to be generated.

Default value: 128

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### seed in

Initial state of the PN generator shift register.

Default value: -692093454

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### user base bit pattern

The base pattern of bits that you specify.

Default value: empty

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether to continue generating bits using the previous iteration states.

| TRUE | The PN generator has been initiated with a new PN seed. |
| --- | --- |
| FALSE | The PN sequence generator has resumed from where it had stopped during the previous iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The binary data stream corresponding to the value that you specify in the user base bit pattern parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Definition of Pseudorandom Sequences

Though deterministic in nature, seudorandom or pseudonoise (PN) sequences satisfy many properties of random numbers, such as autocorrelation, crosscorrelation, and so on. PN sequences are used in many applications and standards such as 802.11a and DVB. Some examples of PN sequences are maximal length shift register sequences, or 
 m-sequences, Gold sequences, and Kasami sequences. An m-sequence generates a periodic sequence of length

L

=

2

m

−

1

m-sequences

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

The preceding figure shows the Fibonacci and Galois implementations of m-sequences. As can be seen in these figures, m-sequences contain 
 m shift registers. The shift register set is filled with an m-bit initial seed that can be any value except 0. If the 
 m bits in the 
 m shift registers are all zero, then it is a degenerate case and the output of the generator is 0.

#### Examples of Fibonacci and Galois Implementation of Pseudorandom Sequences

The following examples demonstrate bit generation:

1. The first example depicts the Fibonacci implementation. This structure is used in different standards, including DVB. Inputs are specified as follows: 
 Primitive polynomial: 1+X14+X15 Initial seed: 
 000000010101001 The following figure shows the circuitry: SeedOutput0000000101010010+0=00000001010100100+0=00000010101001000+0=00000101010010000+0=00001010100100000+0=00010101001000000+0=00101010010000000+1=11010100100000011+0=1
2. The second example depicts the Galois implementation. Inputs are specified as follows: 
 Primitive polynomial: 1+X14+X15 Initial seed: 
 000000010101001 The circuitry is shown in the following figure: SeedOutput0000000101010010000000101010010000000101010010000000101010010000000101010010000000101010010000000101010010000000101010010000000111010010000000110010010000000110010010000000110010010000000110011010000000110011110000000110011100000000110011100000000110011100

Parent topic:

MT Generate Bits (poly)

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-bits.html language=enus -->
## TOPIC 00049: MT Generate Bits (poly)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-bits.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-bits.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates the sequence of data bits to be modulated. These nodes can generate Fibonacci or Galois pseudonoise (PN) bit sequences, or bit sequences based on a pattern that you specify.

MT Generate Bits (poly)

Generates the sequence of data bits to be modulated. These nodes can generate Fibonacci or Galois pseudonoise (PN) bit sequences, or bit sequences based on a pattern that you specify.

Digital Nodes

MT Generate Bits (Fibonacci, PN Order)

Generates Fibonacci pseudonoise (PN) bit sequences. The node repeats the selected pattern until it generates the number of bits that you specify. Use this node to specify a PN sequence order based on which the node selects a primitive polynomial that returns a maximal length shift register sequence, or m-sequence.

MT Generate Bits (Fibonacci, Primitive Polynomial)

Generates Fibonacci pseudonoise (PN) bit sequences. The node repeats the selected pattern until it generates the number of total bits that you specify. Use this node to specify the primitive polynomial that determines the connection structure of the linear feedback shift register (LFSR).

MT Generate Bits (Galois, PN Order)

Generates Galois pseudonoise (PN) bit sequences. The node repeats the selected pattern until it generates the number of total bits that you specify. Use this node to specify a PN sequence order based on which the node selects a primitive polynomial that returns an m-sequence.

MT Generate Bits (Galois, Primitive Polynomial)

Generates Galois pseudonoise (PN) bit sequences. The node repeats the selected pattern until it generates the number of total bits that you specify. Use this node to specify the primitive polynomial that determines the connection structure of the linear feedback shift register (LFSR).

MT Generate Bits (User Defined)

Generates bit sequences based on a pattern that you specify. The node repeats the selected pattern until it generates the number of bits that you specify.

Parent topic:

Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-cpm-sync-params-bit-array.html language=enus -->
## TOPIC 00050: MT Generate CPM Synchronization Parameters (bit array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-cpm-sync-params-bit-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-cpm-sync-params-bit-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for CPM demodulation using a synchronization sequence directly represented by the sync bits array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits. CPM system parameters

MT Generate CPM Synchronization Parameters (bit array)

Generates synchronization parameters for CPM demodulation using a synchronization sequence directly represented by the sync bits array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_CPM_Synchronization_Parameters_(bit_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### CPM system parameters

Parameter values defining the CPM system. Wire the CPM system parameters cluster of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol map

A two-dimensional array of desired frequency deviations. Each column corresponds to a symbol, with the binary representation of the column index being the mapped bit-representation of the symbol. Each row corresponds to a modulation index in the order in which it appears in the modulation index, h(i) parameter of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map).

Default value: Empty array

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### sync bits

An array of synchronization bits used to generate the CPM synchronization parameter cluster. For example, if you specify a preamble word of 
1111 1111 1111 1110 for symbol synchronization, you can wire a 16-bit array with the above entries to the sync bits parameter. For reliable symbol synchronization, specify an array of length (10 × 
bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### CPM synchronization parameters

Synchronization parameters to pass to the demodulation node.

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern. Although the data type is complex, only the real portion is used.

The real portion of the mapped symbols is the frequency deviation of the symbol value, and the imaginary portion is 0. To prevent false synchronization, configure this pattern so that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-cpm-sync-params-number-array.html language=enus -->
## TOPIC 00051: MT Generate CPM Synchronization Parameters (number array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-cpm-sync-params-number-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-cpm-sync-params-number-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for CPM demodulation using a synchronization sequence defined by a sync numbers array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual

MT Generate CPM Synchronization Parameters (number array)

Generates synchronization parameters for CPM demodulation using a synchronization sequence defined by a sync numbers array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_CPM_Synchronization_Parameters_(number_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### CPM system parameters

Parameter values defining the CPM system. Wire the CPM system parameters cluster of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol map

A two-dimensional array of desired frequency deviations. Each column corresponds to a symbol, with the binary representation of the column index being the mapped bit-representation of the symbol. Each row corresponds to a modulation index in the order in which it appears in the modulation index, h(i) parameter of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map).

Default value: Empty array

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### sync numbers

An array of synchronization numbers in which the binary representation of each number is used to generate the sync bit array. By default, the internal conversion of each sync number into the corresponding synchronization bit sequence is performed with the most significant bit first (left-aligned) approach.

For example, if you specify a preamble word of 
 1111 1111 1111 1110 for symbol synchronization, you can specify sync numbers as an array with a single element 
 xFFFE. Specify the bits per sync number value to be 16. You can also specify sync numbers as an array of two elements (xFF and 
 xFE), and specify the bits per sync number value as 8. For reliable symbol synchronization, specify an array of length (10 × 
 bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per sync number

Number of bits corresponding to each sync number in the sync numbers array.

Default value: 32

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### CPM synchronization parameters

Synchronization parameters to pass to the demodulation node.

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern. Although the data type is complex, only the real portion is used.

The real portion of the mapped symbols is the frequency deviation of the symbol value, and the imaginary portion is 0. To prevent false synchronization, configure this pattern so that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. If this parameter is left empty, the signal is still demodulated.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-cpm-system-parameters-m.html language=enus -->
## TOPIC 00052: MT Generate CPM System Parameters (M)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-cpm-system-parameters-m.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-cpm-system-parameters-m.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts an M-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols. samples per symbol Number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate. Default value: 16 M-CPM The M-ary number,

MT Generate CPM System Parameters (M)

Accepts an 
*M*-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols.

[IMAGE alt='1378' src='MethodCall.MT_Generate_CPM_System_Parameters_(M).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### M-CPM

The M-ary number, which is the number of distinct frequency deviations to use as symbols. This value must be a positive power of 2.

Default value: 2

[IMAGE alt='datatype_icon' src='/assets/img/c1dnclst.png']

##### modulation index, h(i)

Modulation index for the CPM modulation scheme.

Refer to CPM Modulation for more information about modulation indices. The modulation index must be of proper form, that is, the numerator must be lesser than the denominator. The modulation index may vary between symbol intervals.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### numerator

Numerator of the modulation index.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### denominator

Denominator of the modulation index.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### symbol rate

The desired symbol rate, in hertz (Hz).

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### CPM system parameters

Parameter values defining the CPM system. Wire this parameter to the corresponding system parameters cluster of MT Modulate CPM, MT Demodulate CPM, or MT Detect CPM.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol map

A two-dimensional array of desired frequency deviations. Each column corresponds to a symbol, with the binary representation of the column index being the mapped bit-representation of the symbol. Each row corresponds to a modulation index in the order in which it appears in the modulation index, h(i) parameter of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map).

Default value: Empty array

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation (for example, for 4-CPM, 
M = 4).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-cpm-system-parameters-map.html language=enus -->
## TOPIC 00053: MT Generate CPM System Parameters (map)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-cpm-system-parameters-map.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-cpm-system-parameters-map.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate CPM or MT Demodulate CPM. Wire the CPM system parameters passed from this node to the corresponding cluster of MT Modulate CPM, MT Demodulate CPM, and MT Detect CPM. It accepts an input array of symbol values that explicitly define the positions

MT Generate CPM System Parameters (map)

Calculates parameters for use with either MT Modulate CPM or MT Demodulate CPM. Wire the CPM system parameters passed from this node to the corresponding cluster of MT Modulate CPM, MT Demodulate CPM, and MT Detect CPM. It accepts an input array of symbol values that explicitly define the positions of the symbol map.

[IMAGE alt='1378' src='MethodCall.MT_Generate_CPM_System_Parameters_(Map).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### symbol indices

Array of symbol values with an order that corresponds to the symbol map. The number of CPM levels specified here must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/c1dnclst.png']

##### modulation index, h(i)

Modulation index for the CPM modulation scheme.

Refer to CPM Modulation for more information about modulation indices. The modulation index must be of proper form, that is, the numerator must be lesser than the denominator. The modulation index may vary between symbol intervals.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### numerator

Numerator of the modulation index.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### denominator

Denominator of the modulation index.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### symbol rate

The desired symbol rate, in hertz (Hz).

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### CPM system parameters

Parameter values defining the CPM system. Wire this parameter to the corresponding system parameters cluster of MT Modulate CPM, MT Demodulate CPM, or MT Detect CPM.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol map

A two-dimensional array of desired frequency deviations. Each column corresponds to a symbol, with the binary representation of the column index being the mapped bit-representation of the symbol. Each row corresponds to a modulation index in the order in which it appears in the modulation index, h(i) parameter of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map).

Default value: Empty array

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-fsk-system-parameters-m.html language=enus -->
## TOPIC 00054: MT Generate FSK System Parameters (M)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-fsk-system-parameters-m.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-fsk-system-parameters-m.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate FSK or MT Demodulate FSK. This node generates the symbol map for FSK-modulated systems. This node accepts an M-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols. samples per symbol An

MT Generate FSK System Parameters (M)

Calculates parameters for use with either MT Modulate FSK or MT Demodulate FSK. This node generates the symbol map for FSK-modulated systems. This node accepts an 
*M*-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols.

[IMAGE alt='1378' src='MethodCall.MT_Generate_FSK_System_Parameters(M).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### M-FSK

The 
M-ary number, which is the number of distinct frequency deviations, to use as symbols. This value must be a positive power of 2.

Default value: 2

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### FSK deviation

Maximum FSK frequency deviation. At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-f<sub>d</sub>, 
f<sub>d</sub>], where 
f<sub>d</sub> represents the frequency deviation.

Default value: 150,000

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### symbol phase continuity

Continuity of phase transitions between symbols.

| continuous | Continuous phase transitions between symbols. |
| --- | --- |
| discontinuous | Discontinuous phase transitions between symbols, that is, discontinuous phase FSK (DPFSK). With discontinuous phase-FSK (DPFSK), modulation consists of selecting the appropriate sinusoid based on the input data. Thus, when switching between symbols, there is a discontinuity in the FSK signal phase. To emulate a hardware-based DPFSK source, this node maintains the phase of each independent sinusoid versus time. Thus, the DPFSK modulator acts like a hardware-based (multiple switched tone generator) FSK modulator. |

Default value: 
 continuous

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### FSK system parameters

Parameter values defining the FSK system. Wire this cluster to the corresponding system parameters cluster of MT Modulate FSK or MT Demodulate FSK.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number. Applying Carson's rule for FSK modulation, the 98% FSK bandwidth is given by the following formula:

0.5 × (1 + 
 r) × 
 symbol rate + 
 peak frequency deviation

where 0 ≤ 
 r ≤ 1 is the filter parameter.

To satisfy the Nyquist criterion, use the following guideline.

samples per symbol = 2 × ceil(1.5 × 
 bandwidth/symbol rate) to obtain 3× oversampling.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### symbol map

Ordered array that maps each Boolean symbol to its desired deviation frequency. The number of FSK levels in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### symbol phase continuity

Continuity of phase transitions between symbols.

| continuous | Continuous phase transitions between symbols. |
| --- | --- |
| discontinuous | Discontinuous phase transitions between symbols, that is, discontinuous phase FSK (DPFSK). With discontinuous phase-FSK (DPFSK), modulation consists of selecting the appropriate sinusoid based on the input data. Thus, when switching between symbols, there is a discontinuity in the FSK signal phase. To emulate a hardware-based DPFSK source, this node maintains the phase of each independent sinusoid versus time. Thus, the DPFSK modulator acts like a hardware-based (multiple switched tone generator) FSK modulator. |

Default value: 
 continuous

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation. Example: For 16-FSK, 
M = 16.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-fsk-system-parameters-map.html language=enus -->
## TOPIC 00055: MT Generate FSK System Parameters (map)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-fsk-system-parameters-map.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-fsk-system-parameters-map.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate FSK or MT Demodulate FSK. This node accepts an input array of symbol values that explicitly specifies the positions of the symbol map. samples per symbol An even number of samples dedicated to each symbol. Multiply this value by the symbol rate t

MT Generate FSK System Parameters (map)

Calculates parameters for use with either MT Modulate FSK or MT Demodulate FSK. This node accepts an input array of symbol values that explicitly specifies the positions of the symbol map.

[IMAGE alt='1378' src='MethodCall.MT_Generate_FSK_System_Parameters(map).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### symbol values

Array of symbol values with an order that corresponds to the symbol map. The number of FSK levels specified in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

This parameter expects an array of integers. The integers 0 to (M-1), inclusive, must all be included only once in the symbol values array, where 
 M is the 
 M-ary number of the modulation. The symbol locations (FSK frequencies) are evenly spaced between -FSK Deviation and +FSK Deviation, inclusive, with the binary representation (LSB first convention) of the integers that populate the symbol values array that corresponds to the placement of the 
 M-ary bits on the I/Q constellation.

For example, for 4-FSK, if you specify FSK deviation as 150k and symbol values as [0 1 3 2], then:

- 00 (symbol value 0) corresponds to -150k
- 01 (symbol value 1) corresponds to -50k
- 11 (symbol value 3) corresponds to 50k
- 10 (symbol value 2) corresponds to 150k

Therefore the generated FSK symbol map reads [-150k -50k 150k 50k]. Similarly, if you specify the symbol values array as [0 1 2 3], the generated FSK symbol map reads [-150k -50k 50k 150k].

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### FSK deviation

Maximum FSK frequency deviation. At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-f<sub>d</sub>, 
f<sub>d</sub>], where 
f<sub>d</sub> represents the frequency deviation.

Default value: 150,000

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### symbol phase continuity

Continuity of phase transitions between symbols.

| continuous | Continuous phase transitions between symbols. |
| --- | --- |
| discontinuous | Discontinuous phase transitions between symbols, that is, discontinuous phase FSK (DPFSK). With discontinuous phase-FSK (DPFSK), modulation consists of selecting the appropriate sinusoid based on the input data. Thus, when switching between symbols, there is a discontinuity in the FSK signal phase. To emulate a hardware-based DPFSK source, this node maintains the phase of each independent sinusoid versus time. Thus, the DPFSK modulator acts like a hardware-based (multiple switched tone generator) FSK modulator. |

Default value: 
 continuous

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### FSK system parameters

Parameter values defining the FSK system. Wire this cluster to the corresponding system parameters cluster of MT Modulate FSK or MT Demodulate FSK.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number. Applying Carson's rule for FSK modulation, the 98% FSK bandwidth is given by the following formula:

0.5 × (1 + 
 r) × 
 symbol rate + 
 peak frequency deviation

where 0 ≤ 
 r ≤ 1 is the filter parameter.

To satisfy the Nyquist criterion, use the following guideline.

samples per symbol = 2 × ceil(1.5 × 
 bandwidth/symbol rate) to obtain 3× oversampling.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### symbol map

Ordered array that maps each Boolean symbol to its desired deviation frequency. The number of FSK levels in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### symbol phase continuity

Continuity of phase transitions between symbols.

| continuous | Continuous phase transitions between symbols. |
| --- | --- |
| discontinuous | Discontinuous phase transitions between symbols, that is, discontinuous phase FSK (DPFSK). With discontinuous phase-FSK (DPFSK), modulation consists of selecting the appropriate sinusoid based on the input data. Thus, when switching between symbols, there is a discontinuity in the FSK signal phase. To emulate a hardware-based DPFSK source, this node maintains the phase of each independent sinusoid versus time. Thus, the DPFSK modulator acts like a hardware-based (multiple switched tone generator) FSK modulator. |

Default value: 
 continuous

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation. Example: For 16-FSK, 
M = 16.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-msk-sync-params-bit-array.html language=enus -->
## TOPIC 00056: MT Generate MSK Synchronization Parameters (bit array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-msk-sync-params-bit-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-msk-sync-params-bit-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for MSK demodulation using a synchronization sequence directly represented by the sync bits input array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits. MSK system para

MT Generate MSK Synchronization Parameters (bit array)

Generates synchronization parameters for MSK demodulation using a synchronization sequence directly represented by the sync bits input array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_MSK_Synchronization_Parameters_(bit_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### MSK system parameters

Parameter values defining the MSK system. Wire the MSK system parameters cluster returned by MT Generate MSK System Parameters to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### differential encoding enable

A value that indicates whether the bit sequence is differentially encoded.

| disable | Disables bit sequence encoding. |
| --- | --- |
| enable | Enables bit sequence encoding. |

Default value: 
 enable

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform.

For error-free operation, the samples per symbol must be an even number. Applying Carson's rule for MSK modulation [peak frequency deviation = 0.25 × 
 symbol rate (Hz)], the 98% MSK bandwidth is given by 0.5 × (1 + 
 r) × 
 symbol rate + 
 peak frequency deviation, where 0 < 
 r ≤ 1 is the filter parameter. To satisfy Nyquist criterion, a good guideline is given by 
 samples per symbol = 2 × ceil(1.5 × 
 bandwidth/symbol rate) to obtain 3× oversampling.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### sync bits

An array of synchronization bits used to generate the MSK synchronization parameters cluster. For example, if you specify a preamble word of 
1111 1111 1111 1110 for symbol synchronization, you can wire a 16-bit array with the above entries to the sync bits parameter. For reliable symbol synchronization, specify an array of length (10 × 
bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### symbol rate

The desired symbol rate, in hertz (Hz).

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### MSK synchronization parameters

Synchronization parameters to pass to the demodulation node.

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### sync sequence

The mapped symbol pattern used to synchronize the bit stream. To prevent false synchronization, select this pattern such that there is a low probability of accidental correlation to nonsynchronized parts of the data stream. For MSK, the real portion of the mapped symbols is the frequency deviation of the symbol value, and the imaginary portion is 0. If this parameter is left empty, the signal is still demodulated.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-pam-sync-params-bit-array.html language=enus -->
## TOPIC 00057: MT Generate PAM Synchronization Parameters (bit array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-pam-sync-params-bit-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-pam-sync-params-bit-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for PAM demodulation using a synchronization sequence directly represented by the sync bits input array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits. PAM system para

MT Generate PAM Synchronization Parameters (bit array)

Generates synchronization parameters for PAM demodulation using a synchronization sequence directly represented by the sync bits input array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PAM_Synchronization_Parameters_(bit_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PAM system parameters

Parameter values defining the PAM system. Wire the PAM system parameters cluster of MT Generate PAM System Parameters (M) or MT Generate PAM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of PAM levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### sync bits

An array of synchronization bits used to generate the PAM synchronization parameters cluster. For example, if you specify a preamble word of 
1111 1111 1111 1110 for symbol synchronization, you can wire a 16-bit array with the above entries to the sync bits parameter. For reliable symbol synchronization, specify an array of length (10 × 
bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PAM synchronization parameters

Synchronization parameters to pass to the demodulation node.

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### sync sequence

The mapped symbol array from the specified synchronization bits or synchronization numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-pam-sync-params-number-array.html language=enus -->
## TOPIC 00058: MT Generate PAM Synchronization Parameters (number array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-pam-sync-params-number-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-pam-sync-params-number-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for PAM demodulation using a synchronization sequence defined by a sync numbers input array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the

MT Generate PAM Synchronization Parameters (number array)

Generates synchronization parameters for PAM demodulation using a synchronization sequence defined by a sync numbers input array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PAM_Synchronization_Parameters_(number_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PAM system parameters

Parameter values defining the PAM system. Wire the PAM system parameters cluster of MT Generate PAM System Parameters (M) or MT Generate PAM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of PAM levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### sync numbers

An array of synchronization numbers in which the binary representation of each number is used to generate the sync bit array. By default, the internal conversion of each sync number into the corresponding synchronization bit sequence is performed with the most significant bit first (left-aligned) approach.

For example, if you specify a preamble word of 
 1111 1111 1111 1110 for symbol synchronization, you can specify sync numbers as an array with a single element 
 xFFFE. Specify the bits per sync number value to be 16. You can also specify sync numbers as an array of two elements (xFF and 
 xFE), and specify the bits per sync number value as 8. For reliable symbol synchronization, specify an array of length (10 × 
 bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per sync number

Number of bits corresponding to each sync number in the sync numbers array.

Default value: 32

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PAM synchronization parameters

Synchronization parameters to pass to the demodulation node.

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### sync sequence

The mapped symbol array from the specified synchronization bits or synchronization numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-pam-system-parameters-m.html language=enus -->
## TOPIC 00059: MT Generate PAM System Parameters (M)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-pam-system-parameters-m.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-pam-system-parameters-m.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate PAM or MT Demodulate PAM. The node accepts an M-ary value that specifies a predefined symbol map with the number of distinct levels to use as symbols. samples per symbol An even number of samples dedicated to each symbol. Multiply this value by t

MT Generate PAM System Parameters (M)

Calculates parameters for use with either MT Modulate PAM or MT Demodulate PAM. The node accepts an 
*M*-ary value that specifies a predefined symbol map with the number of distinct levels to use as symbols.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PAM_System_Parameters_(M).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### M-PAM

The 
M-ary number, which for PAM is the number of distinct states that represent symbols in the complex baseband modulated waveform. This value must be a positive power of 2.

Note

M

-1, -0.33, 1.00, 0.33

00

01

10

11

Default value: 2

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PAM system parameters

Parameter values defining the PAM system. Wire this cluster to the corresponding system parameters cluster of MT Modulate PAM or MT Demodulate PAM.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of PAM levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation (for example, for 16-PAM, 
M = 16).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-pam-system-parameters-map.html language=enus -->
## TOPIC 00060: MT Generate PAM System Parameters (map)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-pam-system-parameters-map.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-pam-system-parameters-map.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate PAM or MT Demodulate PAM. The node accepts an array of symbol values that explicitly specifies the positions of the symbol map with symbols that are evenly distributed between -1 and 1. samples per symbol An even number of samples dedicated to ea

MT Generate PAM System Parameters (map)

Calculates parameters for use with either MT Modulate PAM or MT Demodulate PAM. The node accepts an array of symbol values that explicitly specifies the positions of the symbol map with symbols that are evenly distributed between -1 and 1.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PAM_system_parameters_(map).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### symbol values

An array of symbol values with an index-based order that corresponds to the symbol map. The length of the symbol values array must be a positive power of 2, and the entries must be unique and in the range 0 to 
M-1, where 
M is the length of the symbol values array.

This node expects an array of integers for the symbol values parameter. The integers 0 through (M-1) must all be included only once in the symbol values array, where 
 M is the 
 M-ary number of the modulation. The binary representation (LSB first convention) of the integers represents the bit pattern that is mapped to the corresponding symbol location in the symbol values array. The symbol locations are evenly spaced between (-1 + 0i) and (1 + 0i), inclusive, along the real axis (I axis).

For example, for 4-PAM, if you specify symbol values as [2 3 0 1], the generated PAM symbol map is [(0.333 + 0i), (1 + 0i), (-1 + 0i), (-0.333 + 0i)].

Note

n

n

M

M

symbol values

symbol

symbol

symbol

symbol

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PAM system parameters

Parameter values defining the PAM system. Wire this cluster to the corresponding system parameters cluster of MT Modulate PAM or MT Demodulate PAM.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of PAM levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation (for example, for 16-PAM, 
M = 16).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-psk-sync-params-bit-array.html language=enus -->
## TOPIC 00061: MT Generate PSK Synchronization Parameters (bit array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-psk-sync-params-bit-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-psk-sync-params-bit-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for PSK demodulation using a synchronization sequence directly represented by the sync bits array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits. PSK system parameters

MT Generate PSK Synchronization Parameters (bit array)

Generates synchronization parameters for PSK demodulation using a synchronization sequence directly represented by the sync bits array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PSK_Synchronization_Parameters_(bit_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PSK system parameters

Parameter values defining the PSK system. Wire the PSK system parameters cluster returned by MT Generate PSK System Parameters (M) or MT Generate PSK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each Boolean symbol to its desired coordinates in the complex plane. The number of PSK states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### differential PSK

Status of the differential PSK.

| disable | Disables bit sequence encoding. |
| --- | --- |
| enable | Enables bit sequence encoding. |

Default value: 
 enable

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### sync bits

An array of synchronization bits used to generate the PSK synchronization parameters cluster. For example, if you specify a preamble word of 
1111 1111 1111 1110 for symbol synchronization, you can wire a 16-bit array with the above entries to the sync bits parameter. For reliable symbol synchronization, specify an array of length (10 × 
bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PSK synchronization parameters

Synchronization parameters to pass to the demodulation node.

Note

PSK synchronization parameters

PSK type

PSK synchronization parameters

shifted

offset

MT Demodulate PSK

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### sync sequence

The mapped symbol array from the specified synchronization bits or synchronization numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-psk-sync-params-number-array.html language=enus -->
## TOPIC 00062: MT Generate PSK Synchronization Parameters (number array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-psk-sync-params-number-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-psk-sync-params-number-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for PSK demodulation using a synchronization sequence defined by a sync numbers array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual

MT Generate PSK Synchronization Parameters (number array)

Generates synchronization parameters for PSK demodulation using a synchronization sequence defined by a sync numbers array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PSK_Synchronization_Parameters_(number_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PSK system parameters

Parameter values defining the PSK system. Wire the PSK system parameters cluster returned by MT Generate PSK System Parameters (M) or MT Generate PSK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each Boolean symbol to its desired coordinates in the complex plane. The number of PSK states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### differential PSK

Status of the differential PSK.

| disable | Disables bit sequence encoding. |
| --- | --- |
| enable | Enables bit sequence encoding. |

Default value: 
 enable

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### sync numbers

An array of synchronization numbers in which the binary representation of each number is used to generate the sync bit array. By default, the internal conversion of each sync number into the corresponding synchronization bit sequence is performed with the most significant bit first (left-aligned) approach.

For example, if you specify a preamble word of 
 1111 1111 1111 1110 for symbol synchronization, you can specify sync numbers as an array with a single element 
 xFFFE. Specify the bits per sync number value to be 16. You can also specify sync numbers as an array of two elements (xFF and 
 xFE), and specify the bits per sync number value as 8. For reliable symbol synchronization, specify an array of length (10 × 
 bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per sync number

Number of bits corresponding to each sync number in the sync numbers array.

Default value: 32

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PSK synchronization parameters

Synchronization parameters to pass to the demodulation node.

Note

PSK synchronization parameters

PSK type

PSK synchronization parameters

shifted

offset

MT Demodulate PSK

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### sync sequence

The mapped symbol array from the specified synchronization bits or synchronization numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-psk-system-parameters-m.html language=enus -->
## TOPIC 00063: MT Generate PSK System Parameters (M)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-psk-system-parameters-m.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-psk-system-parameters-m.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate PSK or MT Demodulate PSK. This node generates the symbol map for PSK-modulated systems. This node accepts an M-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols. Example Symbol Map fo

MT Generate PSK System Parameters (M)

Calculates parameters for use with either MT Modulate PSK or MT Demodulate PSK. This node generates the symbol map for PSK-modulated systems. This node accepts an M-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols.

Example Symbol Map for PSK

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

This symbol map corresponds to input symbol values {0, 1, 3, 2} for a quadrature-phase-shift-keying (QPSK) modulation system.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PSK_System_Parameters(M).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### M-PSK

The 
M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. This value must be a positive power of 2.

Default value: 4

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### differential PSK

A value that indicates how the PSK modulation represents symbols.

Differential operation is used to implement PSK formats such as differential quadrature PSK (DQPSK) and /4-DQPSK.

| disable | Symbols are represented as constellation points. |
| --- | --- |
| enable | Symbols are represented as the transitions between constellation points. |

Default value: 
 disable

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PSK system parameters

Parameter values defining the PSK system. Wire this cluster to the corresponding system parameters clusters of MT Modulate PSK or MT Demodulate PSK.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each Boolean symbol to its desired coordinates in the complex plane. The number of PSK states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### differential PSK

A value that indicates how the PSK modulation represents symbols.

Differential operation is used to implement PSK formats such as differential quadrature PSK (DQPSK) and /4-DQPSK.

| disable | Symbols are represented as constellation points. |
| --- | --- |
| enable | Symbols are represented as the transitions between constellation points. |

Default value: 
 disable

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation (for example, for 16-PSK, 
M = 16).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-psk-system-parameters-map.html language=enus -->
## TOPIC 00064: MT Generate PSK System Parameters (map)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-psk-system-parameters-map.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-psk-system-parameters-map.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate PSK or MT Demodulate PSK. This node generates the symbol map for PSK-modulated systems. The node accepts an array of symbol values that explicitly specifies the positions of the symbol map. Example Symbol Map for PSK This symbol map corresponds t

MT Generate PSK System Parameters (map)

Calculates parameters for use with either MT Modulate PSK or MT Demodulate PSK. This node generates the symbol map for PSK-modulated systems. The node accepts an array of symbol values that explicitly specifies the positions of the symbol map.

Example Symbol Map for PSK

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

This symbol map corresponds to input symbol values {0, 1, 3, 2} for a quadrature-phase-shift-keying (QPSK) modulation system.

[IMAGE alt='1378' src='MethodCall.MT_Generate_PSK_System_Parameters(map).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### symbol values

An array of symbol values with an order that corresponds to the symbol map. The number of PSK states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

This node expects an array of integers for the symbol values parameter. The integers 0 through (M-1) must all be included only once in the symbol values array, where 
 M is the 
 M-ary number of the modulation. The binary representation (LSB first convention) of the integers represents the bit pattern that is mapped to the corresponding symbol location in the symbol values array. The symbol locations are generated with equal angles between all 
 M-ary symbol locations and a distance of unity from the origin.

For example, in 8-PSK, if you specify symbol values as [5 4 2 7 3 0 1 6], the generated PSK symbol map is [(-0.383 - 0.924i), (0.383 - 0.924i), (-0.383 + 0.924i), (-0.924 - 0.383i), (0.383 + 0.924i), (0.924 + 0.383i), (0.924 - 0.383i), (-0.924 + 0.383i)].

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### differential PSK

A value that indicates how the PSK modulation represents symbols.

Differential operation is used to implement PSK formats such as differential quadrature PSK (DQPSK) and /4-DQPSK.

| disable | Symbols are represented as constellation points. |
| --- | --- |
| enable | Symbols are represented as the transitions between constellation points. |

Default value: 
 disable

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### PSK system parameters

Parameter values defining the PSK system. Wire this cluster to the corresponding system parameters clusters of MT Modulate PSK or MT Demodulate PSK.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each Boolean symbol to its desired coordinates in the complex plane. The number of PSK states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### differential PSK

A value that indicates how the PSK modulation represents symbols.

Differential operation is used to implement PSK formats such as differential quadrature PSK (DQPSK) and /4-DQPSK.

| disable | Symbols are represented as constellation points. |
| --- | --- |
| enable | Symbols are represented as the transitions between constellation points. |

Default value: 
 disable

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation (for example, for 16-PSK, 
M = 16).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-qam-sync-params-bit-array.html language=enus -->
## TOPIC 00065: MT Generate QAM Synchronization Parameters (bit array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-qam-sync-params-bit-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-qam-sync-params-bit-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for QAM demodulation using a synchronization sequence directly represented by the sync bits array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits. QAM system parameters

MT Generate QAM Synchronization Parameters (bit array)

Generates synchronization parameters for QAM demodulation using a synchronization sequence directly represented by the sync bits array. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_QAM_Synchronization_Parameters_(bit_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### QAM system parameters

Parameter values defining the QAM system. Wire the QAM system parameters cluster of MT Generate QAM System Parameters (M) or MT Generate QAM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol value must be an even number.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired coordinates in the complex plane. The number of QAM states in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### sync bits

An array of synchronization bits used to generate the QAM synchronization parameters cluster. For example, if you specify a preamble word of 
1111 1111 1111 1110 for symbol synchronization, you can wire a 16-bit array with the above entries to the sync bits parameter. For reliable symbol synchronization, specify an array of length (10 × 
bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### QAM synchronization parameters

Synchronization parameters to pass to the demodulation node.

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### sync sequence

The mapped symbol array from the specified synchronization bits or synchronization numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-qam-sync-params-number-array.html language=enus -->
## TOPIC 00066: MT Generate QAM Synchronization Parameters (number array)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-qam-sync-params-number-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-qam-sync-params-number-array.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates synchronization parameters for QAM demodulation using a synchronization sequence defined by a sync numbers array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual

MT Generate QAM Synchronization Parameters (number array)

Generates synchronization parameters for QAM demodulation using a synchronization sequence defined by a sync numbers array in which each number represents a group of bits. The generated synchronization parameters cluster avoids phase ambiguity at the demodulator, thus allowing recovery of the actual message bits.

[IMAGE alt='1378' src='MethodCall.MT_Generate_QAM_Synchronization_Parameters_(number_array).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### QAM system parameters

Parameter values defining the QAM system. Wire the QAM system parameters cluster of MT Generate QAM System Parameters (M) or MT Generate QAM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol value must be an even number.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired coordinates in the complex plane. The number of QAM states in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### sync numbers

An array of synchronization numbers in which the binary representation of each number is used to generate the sync bit array. By default, the internal conversion of each sync number into the corresponding synchronization bit sequence is performed with the most significant bit first (left-aligned) approach.

For example, if you specify a preamble word of 
 1111 1111 1111 1110 for symbol synchronization, you can specify sync numbers as an array with a single element 
 xFFFE. Specify the bits per sync number value to be 16. You can also specify sync numbers as an array of two elements (xFF and 
 xFE), and specify the bits per sync number value as 8. For reliable symbol synchronization, specify an array of length (10 × 
 bits per symbol).

Note

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per sync number

Number of bits corresponding to each sync number in the sync numbers array.

Default value: 32

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the synchronization parameters in symbols. Set this value to -1 to search the entire waveform for the synchronization symbols.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### QAM synchronization parameters

Synchronization parameters to pass to the demodulation node.

If the synchronization parameter passed to the demodulation node is left empty, the constellation of the demodulated waveform has a 90° carrier phase ambiguity for two-dimensional modulation schemes (QAM, QPSK, and higher order PSK) and a 180° carrier phase ambiguity for one-dimensional modulation schemes (PAM/ASK/BPSK).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### expected sync location

The expected location of the first symbol of the sync sequence.

This value is an index to the input complex waveform. A value of 
 -1 searches the entire input complex waveform and ignores the sync location uncertainty parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### sync sequence

The mapped symbol array from the specified synchronization bits or synchronization numbers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync location uncertainty

Number of symbols before or after the expected sync location where the first symbol of the sync sequence may be located. The node ignores this parameter if the expected sync location parameter is set to -1.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sync indent

Distance that the sync sequence is indented into the information block.

The distance is the number of demodulated symbols preceding the sync sequence. For example, a value of 10 indicates that the output bit stream consists of 10 data symbols, followed by the sync sequence, followed by the remaining data symbols.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate Synchronization Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-qam-system-parameters-m.html language=enus -->
## TOPIC 00067: MT Generate QAM System Parameters (M)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-qam-system-parameters-m.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-qam-system-parameters-m.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate QAM or MT Demodulate QAM. The node accepts an M-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols. samples per symbol An even number of samples dedicated to each symbol. Multiply this

MT Generate QAM System Parameters (M)

Calculates parameters for use with either MT Modulate QAM or MT Demodulate QAM. The node accepts an 
*M*-ary value that specifies a predefined symbol map with the number of distinct symbol map values to use as symbols.

[IMAGE alt='1378' src='MethodCall.MT_Generate_QAM_System_Parameters(M).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### M-QAM

The 
M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. This value must be a positive power of 2 and must be less than 256.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### QAM system parameters

Parameter values defining the QAM system. Wire this cluster to the corresponding system parameters cluster of MT Modulate QAM or MT Demodulate QAM.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### symbol map

An ordered array that maps each symbol value to its desired coordinates in the complex plane. The number of QAM states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol. The length of the vector for the symbols farthest from the origin must be 1.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation (for example, for 16-QAM, 
M = 16).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-qam-system-parameters-map.html language=enus -->
## TOPIC 00068: MT Generate QAM System Parameters (map)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-qam-system-parameters-map.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-qam-system-parameters-map.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates parameters for use with either MT Modulate QAM or MT Demodulate QAM. The node accepts an input array of symbol values that explicitly specifies the positions of the symbol map. samples per symbol An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to

MT Generate QAM System Parameters (map)

Calculates parameters for use with either MT Modulate QAM or MT Demodulate QAM. The node accepts an input array of symbol values that explicitly specifies the positions of the symbol map.

[IMAGE alt='1378' src='MethodCall.MT_Generate_QAM_System_Parameters(map).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### symbol values

An array of symbol values with an order that corresponds to the symbol map. The number of QAM states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol. The length or magnitude of the vector for the symbols farthest from the origin must be 1.

This node expects a two-dimensional, square array of integers for the symbol values parameter. 4-QAM expects a 2×2 array (2 rows, 2 columns), 16-QAM expects a 4×4 array, and so on. The integers 0 through (M-1) must all be included only once in the symbol values array, where 
 M is the 
 M-ary number of the modulation. 
 M must be less than 256. The binary representation (LSB first convention) of the integers represents the bit pattern that is mapped to the corresponding symbol location in the symbol values array.

For example, for 4-QAM, if you specify symbol values as

[3 1]

[0 2]

the generated QAM symbol map is [(-0.707 - 0.707i), (0.707 + 0.707i), (0.707 - 0.707i), (-0.707 + 0.707i)].

In order to create a custom QAM symbol map that does not fit into a square 2 dimensional array, for example 32-QAM, set the additional spaces in the array to negative numbers. The negative number will not be considered as a part of the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### QAM system parameters

Parameter values defining the QAM system. Wire this cluster to the corresponding system parameters cluster of MT Modulate QAM or MT Demodulate QAM.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### samples per symbol

Number of samples per symbol in the modulated output complex waveform. For error-free operation, the samples per symbol must be an even number.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### symbol map

An ordered array that maps each symbol value to its desired coordinates in the complex plane. The number of QAM states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol. The length of the vector for the symbols farthest from the origin must be 1.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per symbol

Number of bits represented by each symbol. This value is equal to Log<sub>2</sub>(M), where 
M is the order of the modulation (for example, for 16-QAM, 
M = 16).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Generate System Parameters

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-symbol-map-circular.html language=enus -->
## TOPIC 00069: MT Generate Symbol Map (Circular)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-symbol-map-circular.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-symbol-map-circular.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a symbol map, using the matrix of symbol values that you specify, a matrix representing the symbol phases in degrees, and an array representing the radii of each discrete circle. Use the symbol map parameter of the system parameters cluster to configure the operation of the demodulation an

MT Generate Symbol Map (Circular)

Generates a symbol map, using the matrix of symbol values that you specify, a matrix representing the symbol phases in degrees, and an array representing the radii of each discrete circle. Use the symbol map parameter of the system parameters cluster to configure the operation of the demodulation and modulation nodes.

The symbol values matrix defines how the 
 *M*-ary binary data are mapped to the discrete I/Q symbols on the constellation diagram. The node maps the specified symbol values to I/Q constellation points using the polar representation

j

π

θ

i

180

symbol values/symbol phases

symbol radii

Note

symbol phases

symbol radii

[IMAGE alt='1378' src='MethodCall.MT_Generate_Symbol_Map_(Circular).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### symbol values

A matrix of integers that define how the 
M-ary (bits per symbol) binary data are mapped to discrete I/Q symbols on the constellation diagram. Use negative values to specify holes (missing points) in the constellation diagram.

Note

This matrix corresponds to the following bit values:

The term 
 XXX here refers to a hole (missing point) on the constellation plot.

Default value: empty

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol phases

Phases, in degrees, corresponding to the location of the elements of the symbol values matrix on the I/Q constellation diagram.

Default value: empty

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol radii

Radii of discrete concentric circles that contain the I/Q constellation points. There is a one-to-one mapping between every entry on the symbol radii array and every row in the symbol values/symbol phases matrix.

Default value: empty

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### symbol map

An ordered array to be bundled with the system parameters cluster that is passed to the digital demodulation and modulation nodes.

The generated symbol maps must be bundled onto the system parameters cluster prior to being passed to the corresponding modulation node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Generic or Combined Amplitude Modulation Scheme

Use MT Generate Symbol Map (Rectangular) to create a custom symbol map for a generic amplitude modulation scheme such as quadrature amplitude modulation (QAM). Use MT Generate Symbol Map (Circular) to create a custom symbol map for a combined amplitude-phase modulation scheme.

#### Example: 8-QAM Symbol Map Creation

The following example demonstrates 8-QAM symbol map creation. Define the symbol values as

[

0

1

2

3

−

1

4

5

6

7

]

Define the I symbol amplitude array as

[

−

1

0

1

]

Define the Q symbol amplitude array as

[

1

0

−

1

]

Define gain as 1.0.

These settings result in the following symbol map.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

Parent topic:

MT Generate Symbol Map

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-generate-symbol-map.html language=enus -->
## TOPIC 00070: MT Generate Symbol Map

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-generate-symbol-map.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-generate-symbol-map.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates an arbitrarily shaped symbol map representing the I/Q constellation points.

MT Generate Symbol Map

Generates an arbitrarily shaped symbol map representing the I/Q constellation points.

Utilities Nodes

MT Generate Symbol Map (Circular)

symbol values

symbol map

system parameters

MT Generate Symbol Map (Rectangular)

symbol map

system parameters

Parent topic:

Utilities Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-get-complex-iq-component.html language=enus -->
## TOPIC 00071: MT Get Complex IQ Component

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-get-complex-iq-component.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-get-complex-iq-component.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the desired component from the IQ (complex) in parameter. I, Q, magnitude, and phase data are available for extraction from the IQ (complex) in parameter. This node returns a complex envelope in the CE component parameter that contains the t0, dt, and Y values for the chosen component. IQ d

MT Get Complex IQ Component

Extracts the desired component from the IQ (complex) in parameter.

I, Q, magnitude, and phase data are available for extraction from the IQ (complex) in parameter. This node returns a complex envelope in the CE component parameter that contains the t0, dt, and Y values for the chosen component.

[IMAGE alt='1378' src='MethodCall.MT_Get_Complex_IQ_Component.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### IQ data in

The baseband (downconverted) time-domain data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

The trigger (start) time of the acquired signal.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the acquired signal.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued time-domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### component choice

The complex envelope data component to extract from the complex envelope contained in the IQ Data (complex) in parameter.

Note

| I | Extracts the in-phase component. |
| --- | --- |
| Q | Extracts the quadrature component. |
| Magnitude | Extracts the magnitude of signal. |
| Phase | Extracts the phase of the signal. |

Default value: 
 I

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether initialization of an internal node state tracks the ending phase.

| TRUE | The node clears the state information about each call. |
| --- | --- |
| FALSE | The node uses the final phase from the previous call as the starting phase for the next call, ensuring phase continuity between calls. |

Default value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### IQ data out

The baseband (downconverted) time-domain data. This node does not modify this data, so this parameter is identical to the IQ data in parameter.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

The trigger (start) time of the acquired signal.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal. The I/Q sampling rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

The complex-valued time-domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### CE component

The complex envelope data component selected in the component choice parameter. Wire this parameter to a LabVIEW waveform graph to display the selected component as a function of time.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Analog and Digital Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-golay-decoder.html language=enus -->
## TOPIC 00072: MT Golay Decoder

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-golay-decoder.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-golay-decoder.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decodes a Golay-encoded bit stream. The decoder provides the two triple-correcting Golay codes: the Golay (23,12,3) code and the extended Golay (24,12,3) code. This node uses the Arithmetic decoding algorithm for decoding the Golay (23,12,3) encoded bit stream and the Kasami error-trapping decoding

MT Golay Decoder

Decodes a Golay-encoded bit stream. The decoder provides the two triple-correcting Golay codes: the Golay (23,12,3) code and the extended Golay (24,12,3) code. This node uses the Arithmetic decoding algorithm for decoding the Golay (23,12,3) encoded bit stream and the Kasami error-trapping decoding algorithm for decoding the extended Golay (24,12,3) encoded bit stream.

[IMAGE alt='1378' src='MethodCall.MT_Golay_Decoder.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The bit sequence representing the Golay-encoded bits to decode. You can use MT Golay Encoder to generate the encoded bit stream.

Tip

output bit stream

input bit stream

input bit stream

input bit stream

input bit stream

reset?

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### golay code type

The values of the code word length (n), data word length (k), and error correcting capacity (t), in bits.

| Golay (23,12,3) | The (n,k,t) values are (23, 12, 3). |
| --- | --- |
| Golay (24,12,3) | The (n,k,t) values are (24, 12, 3). |

Default value: Golay (23,12,3)

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the decoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. |
| --- | --- |
| FALSE | Continues decoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to decoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence decoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Decoding Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-hamming-encoder-non-sys-msg-gen-prod.html language=enus -->
## TOPIC 00073: MT Hamming Encoder (Non-Systematic, Message-Generator Product)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-hamming-encoder-non-sys-msg-gen-prod.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-hamming-encoder-non-sys-msg-gen-prod.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encodes the data words using non-systematic methods. In the encoded code words, the whole data word sequence might not be explicitly present. The code word is generated as a finite field polynomial multiplication of the information and the generator polynomial. Generates an order-m Hamming-encoded b

MT Hamming Encoder (Non-Systematic, Message-Generator Product)

Encodes the data words using non-systematic methods. In the encoded code words, the whole data word sequence might not be explicitly present. The code word is generated as a finite field polynomial multiplication of the information and the generator polynomial.

Generates an order-*m* Hamming-encoded bit stream. The order-*m* Hamming codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in which the data word length equals 2<sup>m</sup>-*m*-1, code word length equals 2<sup>m</sup>-1, and the error correcting capacity equals 1. Valid values of 
 *m* are 2 to 16, inclusive.

[IMAGE alt='1378' src='MethodCall.MT_Hamming_Encoder_(Non-Systematic,_Message-Generator_Product).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

Bit sequence representing the data bits to encode. Use the bits generated by MT Generate Bits to produce this bit stream or wire a custom data bit stream to this parameter.

Tip

output bit stream

input bit stream

k

k

m

m

input bit stream

k

input bit stream

k

reset?

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### hamming order

The Hamming order 
m sets the Hamming code with data word length equaling 2<sup>m</sup>-m-1 and code word length equaling 2<sup>m</sup>-1. Valid values are 2 to 16, inclusive.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the encoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Galois field structure corresponding to the Hamming code values. |
| --- | --- |
| FALSE | Continues encoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to encoding. |

Tip

reset?

reset?

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence encoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Hamming Encoder

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-hamming-encoder-systematic.html language=enus -->
## TOPIC 00074: MT Hamming Encoder (Systematic)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-hamming-encoder-systematic.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-hamming-encoder-systematic.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encodes a sequence of data words systematically. This node arranges the output code word such that the entire data word sequence is maintained and preceded by the parity words. Generates an order-m Hamming-encoded bit stream. The order-m Hamming codes are specialized Bose-Chaudhari-Hocquenghem (BCH)

MT Hamming Encoder (Systematic)

Encodes a sequence of data words systematically. This node arranges the output code word such that the entire data word sequence is maintained and preceded by the parity words.

Generates an order-*m* Hamming-encoded bit stream. The order-*m* Hamming codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in which the data word length equals 2<sup>m</sup>-*m*-1, code word length equals 2<sup>m</sup>-1, and the error correcting capacity equals 1. Valid values of 
 *m* are 2 to 16, inclusive.

[IMAGE alt='1378' src='MethodCall.MT_Hamming_Encoder_(Systematic).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

Bit sequence representing the data bits to encode. Use the bits generated by MT Generate Bits to produce this bit stream or wire a custom data bit stream to this parameter.

Tip

output bit stream

input bit stream

k

k

m

m

input bit stream

k

input bit stream

k

reset?

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### hamming order

The Hamming order 
m sets the Hamming code with data word length equaling 2<sup>m</sup>-m-1 and code word length equaling 2<sup>m</sup>-1. Valid values are 2 to 16, inclusive.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the encoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Galois field structure corresponding to the Hamming code values. |
| --- | --- |
| FALSE | Continues encoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to encoding. |

Tip

reset?

reset?

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

The Hamming-encoded bits.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Hamming Encoder

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-hamming-encoder.html language=enus -->
## TOPIC 00075: MT Hamming Encoder

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-hamming-encoder.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-hamming-encoder.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates an order-m Hamming-encoded bit stream.

MT Hamming Encoder

Generates an order-m Hamming-encoded bit stream.

Coding Nodes

MT Hamming Encoder (Non-Systematic, Message-Generator Product)

Encodes the data words using non-systematic methods. In the encoded code words, the whole data word sequence might not be explicitly present. The code word is generated as a finite field polynomial multiplication of the information and the generator polynomial.

MT Hamming Encoder (Systematic)

Encodes a sequence of data words systematically. This node arranges the output code word such that the entire data word sequence is maintained and preceded by the parity words.

Parent topic:

Coding Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-ldpc-decoder-serial-schedule.html language=enus -->
## TOPIC 00076: MT LDPC Decoder (Serial Schedule)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-ldpc-decoder-serial-schedule.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-ldpc-decoder-serial-schedule.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs LDPC decoding based on the LDPC serial decoding schedule. The LDPC serial decoding schedule is based on a serial update of symbol nodes messages. This update can be considered as shuffling of the flooding schedule. Instead of sending all messages from symbol nodes to check nodes and then al

MT LDPC Decoder (Serial Schedule)

Performs LDPC decoding based on the LDPC serial decoding schedule. The LDPC serial decoding schedule is based on a serial update of symbol nodes messages. This update can be considered as shuffling of the flooding schedule. Instead of sending all messages from symbol nodes to check nodes and then all messages from check nodes to symbol nodes, as done in the flooding schedule, the serial schedule goes over the check nodes in some order and, for each node, sends all messages into the node and then all messages out from the node.

The message that is sent from message node (*v*) to the check node (*c*) must not take into account the message sent in the previous iteration from 
 *c* to 
 *v*. The same is true for messages passed from check nodes to message nodes.

[IMAGE alt='1378' src='MethodCall.MT_LDPC_Decoder_(Serial_Schedule).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### parity check matrix

The sparse parity check matrix generated by MT LDPC Generate Regular Parity Check Matrix or MT LDPC Generate Irregular Parity Check Matrix. You can also set a parity check matrix that is not rank deficient in this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### likelihoods

The likelihoods of the received symbols.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum number of iterations

The maximum number of iterations for the iterative decoding process. The decoder stops iterating after the number of iterations exceeds the value of the maximum number of iterations or if the decoder satisfies other conditions.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the decoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. |
| --- | --- |
| FALSE | Continues decoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to decoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence decoded by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Low-Density Parity Check (LDPC) Encoding

Low-density parity check (LDPC) is a linear error-correcting coding scheme that uses a parity check matrix that provides only a few ones with respect to a much larger number of zeros.

The main advantage of the parity check matrix is that it provides a performance that is almost equal to the capacity of many different channels and linear time complex algorithms for decoding. Furthermore, parity check matrices are suited for implementations that make heavy use of parallelism.

An LDPC code is a block code that has a parity check matrix 
 H, every row and column of which is sparse. A Regular Gallager Code is an LDPC code in which every column of 
 H has a weight, 
 j, and every row has a weight, 
 k. Regular Gallager codes are constructed at random, subject to these constraints.

- the number of ones in each column (j) = 3
- the number of ones in each row (k) = 6
- the number of columns (n) = 12
- the number of rows (m) = 6 (because m⁢=n×j÷k )
- the rate of 
 (n,j,k) LDPC Code is R≥1−(j÷k)

Then

H

=

(

1

1

1

0

0

1

1

0

0

0

1

0

1

1

1

1

1

0

0

0

0

0

0

1

0

0

0

0

0

1

1

1

0

1

1

1

1

0

0

1

0

0

0

1

1

1

0

1

0

1

0

1

1

0

1

1

1

0

0

0

0

0

1

0

1

1

0

0

1

1

1

0

)

H

=

(

1

1

1

0

0

1

1

0

0

0

1

0

1

1

1

1

1

0

0

0

0

0

0

1

0

0

0

0

0

1

1

1

0

1

1

1

1

0

0

1

0

0

0

1

1

1

0

1

0

1

0

1

1

0

1

1

1

0

0

0

0

0

1

0

1

1

0

0

1

1

1

0

)

If the number of ones per column or row is not constant, the code is an irregular LDPC code. Usually, irregular LDPC codes outperform regular LDPC codes.

#### Parity Bits

The decoder assumes that the parity bits are placed at the end of the code word. Hence, it returns the first part of the code word, which are the message bits.

#### Likelihood Calculation

Belief Propagation algorithm is a sub-class of message-passing algorithms. The messages passed along the edges in this algorithm are probabilities, or beliefs. It is advantageous to work with likelihoods, or log-likelihoods instead of probabilities. For a binary random variable 
 x, let

L

(

x

)

=

Pr

⁡

[

x

=

0

]

÷

Pr

⁡

[

x

=

1

]

x

Given another random variable 
 y, the conditional likelihood of 
 x denoted L(x/y) is defined as

Pr

⁡

[

x

=

1

|

y

]

÷

Pr

⁡

[

x

=

0

|

y

]

The likelihood ratio is defined as

L

=

Pr

⁡

[

x

=

1

|

y

]

÷

Pr

⁡

[

x

=

0

|

y

]

For example, for a BSC channel, if the probability of error = 
 p and the probability of no error =

1

−

p

(

1

−

p

)

÷

p

The likelihood calculation depends upon the specific choice of the symbol map used in the modulation scheme. An example of likelihood calculation for a BPSK additive white Gaussian noise (AWGN) channel, if bit 0 is mapped to symbol point 1 and bit 1 is mapped to symbol point -1, is

P

(

x

=

0

)

=

P

y

(

x

=

0

|

y

)

=

1

1

+

e

2

y

σ

2

⁢

⁢

P

(

x

=

0

)

=

P

y

(

x

=

0

|

y

)

=

1

1

+

e

−

2

y

σ

2

⁢

L

=

e

2

y

σ

2

P

(

x

=

0

)

=

P

y

(

x

=

0

|

y

)

=

1

1

+

e

2

y

σ

2

⁢

⁢

P

(

x

=

0

)

=

P

y

(

x

=

0

|

y

)

=

1

1

+

e

−

2

y

σ

2

⁢

L

=

e

2

y

σ

2

where 
 x and 
 y are binary random variables.

Parent topic:

MT LDPC Decoder

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-ldpc-decoder.html language=enus -->
## TOPIC 00077: MT LDPC Decoder

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-ldpc-decoder.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-ldpc-decoder.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes iterative probabilistic decoding, or belief propagation, for low-density parity check (LDPC). In this algorithm, at each iteration, messages are passed from message nodes to check nodes and vice versa.

MT LDPC Decoder

Executes iterative probabilistic decoding, or belief propagation, for low-density parity check (LDPC). In this algorithm, at each iteration, messages are passed from message nodes to check nodes and vice versa.

Decoding Nodes

MT LDPC Decoder (Flooding Schedule)

Decodes LDPC code based on the standard message-passing schedule, which is a version of the flooding schedule. According to the flooding schedule, all the symbol nodes, and subsequently all the check nodes, pass new messages to their neighbors in each iteration.

MT LDPC Decoder (Serial Schedule)

Performs LDPC decoding based on the LDPC serial decoding schedule. The LDPC serial decoding schedule is based on a serial update of symbol nodes messages. This update can be considered as shuffling of the flooding schedule. Instead of sending all messages from symbol nodes to check nodes and then all messages from check nodes to symbol nodes, as done in the flooding schedule, the serial schedule goes over the check nodes in some order and, for each node, sends all messages into the node and then all messages out from the node.

Parent topic:

Decoding Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-ldpc-encoder.html language=enus -->
## TOPIC 00078: MT LDPC Encoder

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-ldpc-encoder.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-ldpc-encoder.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs LDPC encoding on the input bit stream based on the parity check matrix. The parity check matrix can be generated by MT LDPC Generate Regular Parity Check Matrix, MT LDPC Generate Irregular Parity Check Matrix, or you can provide it as an input to MT LDPC Encoder. parity check matrix in The

MT LDPC Encoder

Performs LDPC encoding on the input bit stream based on the parity check matrix. The parity check matrix can be generated by MT LDPC Generate Regular Parity Check Matrix, MT LDPC Generate Irregular Parity Check Matrix, or you can provide it as an input to MT LDPC Encoder.

[IMAGE alt='1378' src='MethodCall.MT_LDPC_Encoder.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### parity check matrix in

The sparse parity check matrix generated by MT LDPC Generate Regular Parity Check Matrix or MT LDPC Generate Irregular Parity Check Matrix. You can also set a parity check matrix that is not rank deficient in this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The incoming bit stream to be mapped to LDPC symbols.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the encoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. |
| --- | --- |
| FALSE | Continues encoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to encoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### parity check matrix out

The preprocessed parity check matrix that is used by the encoder for encoding. You must provide this parity check matrix to the decoder.

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

Bit sequence encoded by this node.

Note

output bit stream

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Low-Density Parity Check (LDPC) Encoding

Low-density parity check (LDPC) is a linear error-correcting coding scheme that uses a parity check matrix that provides only a few ones with respect to a much larger number of zeros.

The main advantage of the parity check matrix is that it provides a performance that is almost equal to the capacity of many different channels and linear time complex algorithms for decoding. Furthermore, parity check matrices are suited for implementations that make heavy use of parallelism.

An LDPC code is a block code that has a parity check matrix 
 H, every row and column of which is sparse. A Regular Gallager Code is an LDPC code in which every column of 
 H has a weight, 
 j, and every row has a weight, 
 k. Regular Gallager codes are constructed at random, subject to these constraints.

- the number of ones in each column (j) = 3
- the number of ones in each row (k) = 6
- the number of columns (n) = 12
- the number of rows (m) = 6 (because m⁢=n×j÷k )
- the rate of 
 (n,j,k) LDPC Code is R≥1−(j÷k)

Then

H

=

(

1

1

1

0

0

1

1

0

0

0

1

0

1

1

1

1

1

0

0

0

0

0

0

1

0

0

0

0

0

1

1

1

0

1

1

1

1

0

0

1

0

0

0

1

1

1

0

1

0

1

0

1

1

0

1

1

1

0

0

0

0

0

1

0

1

1

0

0

1

1

1

0

)

H

=

(

1

1

1

0

0

1

1

0

0

0

1

0

1

1

1

1

1

0

0

0

0

0

0

1

0

0

0

0

0

1

1

1

0

1

1

1

1

0

0

1

0

0

0

1

1

1

0

1

0

1

0

1

1

0

1

1

1

0

0

0

0

0

1

0

1

1

0

0

1

1

1

0

)

If the number of ones per column or row is not constant, the code is an irregular LDPC code. Usually, irregular LDPC codes outperform regular LDPC codes.

Parent topic:

LDPC Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-ldpc-gen-irreg-parity-check-matrix.html language=enus -->
## TOPIC 00079: MT LDPC Generate Irregular Parity Check Matrix

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-ldpc-gen-irreg-parity-check-matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-ldpc-gen-irreg-parity-check-matrix.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates an irregular parity check matrix that is used by MT LDPC Encoder for LDPC encoding. In this node, the number of ones in each column is kept constant, and the number of ones in each row is random. n The number of columns in the parity check matrix. Default value: 12 m The number of rows in

MT LDPC Generate Irregular Parity Check Matrix

Generates an irregular parity check matrix that is used by MT LDPC Encoder for LDPC encoding. In this node, the number of ones in each column is kept constant, and the number of ones in each row is random.

[IMAGE alt='1378' src='MethodCall.MT_LDPC_Generate_Irregular_Parity_Check_Matrix.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### n

The number of columns in the parity check matrix.

Default value: 12

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### m

The number of rows in the irregular parity check matrix.

Default value: 6

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### j

The number of ones in the columns of LDPC code. j must be an odd number.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum number of iterations

The maximum number of iterations to return a parity check matrix that is not rank deficient.

Default value: 30

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### irregular parity check matrix

The irregular parity check matrix generated by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

LDPC Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-ldpc-gen-reg-parity-check-matrix.html language=enus -->
## TOPIC 00080: MT LDPC Generate Regular Parity Check Matrix

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-ldpc-gen-reg-parity-check-matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-ldpc-gen-reg-parity-check-matrix.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a regular parity check matrix that is used by MT LDPC Encoder for LDPC encoding. In this node, the number of ones in each column and the number of ones in each row are kept constant. n The number of columns in the parity check matrix. Default value: 12 j The number of ones in the columns o

MT LDPC Generate Regular Parity Check Matrix

Generates a regular parity check matrix that is used by MT LDPC Encoder for LDPC encoding. In this node, the number of ones in each column and the number of ones in each row are kept constant.

[IMAGE alt='1378' src='MethodCall.MT_LDPC_Generate_Regular_Parity_Check_Matrix.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### n

The number of columns in the parity check matrix.

Default value: 12

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### j

The number of ones in the columns of LDPC code. j must be an odd number.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### k

The number of ones in the rows of LDPC code.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum number of iterations

The maximum number of iterations to return a parity check matrix that is not rank deficient.

Default value: 30

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### regular parity check matrix

The regular parity check matrix generated by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

LDPC Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-map-ask-symbols-to-bits.html language=enus -->
## TOPIC 00081: MT Map ASK Symbols to Bits

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-map-ask-symbols-to-bits.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-map-ask-symbols-to-bits.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps complex-valued ASK symbols to an output bit stream based on a user-specified symbol map. symbols The incoming complex-valued symbols to be mapped to the output bit stream based on the symbol map. symbol map An ordered array that maps each symbol value to its desired coordinates in the complex p

MT Map ASK Symbols to Bits

Maps complex-valued ASK symbols to an output bit stream based on a user-specified symbol map.

[IMAGE alt='1378' src='MethodCall.MT_Map_ASK_Symbols_to_Bits.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbols

The incoming complex-valued symbols to be mapped to the output bit stream based on the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol value to its desired coordinates in the complex plane.

The number of ASK states in the array must be 2<sup>N</sup>, where 
 N is the number of bits per symbol. The length of the vector for the symbols farthest from the origin must be 1. To specify a prebuilt map, unbundle the symbol map element from the ASK system parameters cluster generated by MT Generate ASK System Parameters (M) or MT Generate ASK System Parameters (map).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output bit stream

A bit stream with a one-to-one mapping to the input symbols based on the specified symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

MT Matched Filter

MT Align to Ideal Symbols

MT Decimate Oversampled Waveform

MT Calculate BER

Note

log

⁡

2

(

M

)

M

(

500

)

×

log

⁡

2

(

256

)

=

4000

⁢

⁢

m

e

s

s

a

g

e

⁢

b

i

t

s

Parent topic:

MT Map Symbols to Bits

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-map-bits-to-ask-symbols.html language=enus -->
## TOPIC 00082: MT Map Bits to ASK Symbols

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-map-bits-to-ask-symbols.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-map-bits-to-ask-symbols.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps an incoming bit stream to complex-valued ASK symbols. input bit stream The incoming bit stream to be mapped to symbols. symbol map An ordered array that maps each symbol value to its desired coordinates in the complex plane. The number of ASK states in the array must be 2^N, where N is the numb

MT Map Bits to ASK Symbols

Maps an incoming bit stream to complex-valued ASK symbols.

[IMAGE alt='1378' src='MethodCall.MT_Map_Bits_to_ASK_Symbols.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The incoming bit stream to be mapped to symbols.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol value to its desired coordinates in the complex plane.

The number of ASK states in the array must be 2<sup>N</sup>, where 
 N is the number of bits per symbol. The length of the vector for the symbols farthest from the origin must be 1. To specify a prebuilt map, unbundle the symbol map element from the ASK system parameters cluster generated by MT Generate ASK System Parameters (M) or MT Generate ASK System Parameters (map).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether stored state information is cleared on each call to this node.

When the input bit stream is not comprised of an integer number of symbols, the carryover bits are buffered.

| TRUE | Clears the buffered data, checks the input parameters on a first call, and reflects any change in the input parameter values during subsequent iterations. |
| --- | --- |
| FALSE | Adds the buffered data to the beginning of data from next iteration, in continuous operations. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### symbols

An array of complex-valued symbols with a one-to-one mapping to the input bit stream based on the specified symbol map.

Note

MT Apply Pulse Shaping Filter

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Map Bits to Symbols

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-map-bits-to-cpm-symbols.html language=enus -->
## TOPIC 00083: MT Map Bits to CPM Symbols

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-map-bits-to-cpm-symbols.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-map-bits-to-cpm-symbols.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps an incoming bit stream to symbols comprised of CPM frequency deviations. input bit stream The incoming bit stream to be mapped to symbols. symbol map A two-dimensional array of desired frequency deviations. Each column corresponds to a symbol, with the binary representation of the column index

MT Map Bits to CPM Symbols

Maps an incoming bit stream to symbols comprised of CPM frequency deviations.

[IMAGE alt='1378' src='MethodCall.MT_Map_Bits_to_CPM_Symbols.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The incoming bit stream to be mapped to symbols.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol map

A two-dimensional array of desired frequency deviations.

Each column corresponds to a symbol, with the binary representation of the column index being the mapped bit-representation of the symbol. Each row corresponds to a modulation index in the order in which it appears in the modulation index, h(i) parameter of MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map). To specify a prebuilt map, unbundle the symbol map element from the CPM system parameters cluster generated by MT Generate CPM System Parameters (M) or MT Generate CPM System Parameters (map).

Default value: empty array

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether stored state information is cleared on each call to this node.

When the input bit stream is not comprised of an integer number of symbols, the carryover bits are buffered.

| TRUE | Clears the buffered data, checks the input parameters on a first call, and reflects any change in the input parameter values during subsequent iterations. |
| --- | --- |
| FALSE | Adds the buffered data to the beginning of data from next iteration, in continuous operations. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### symbols

An array of CPM frequency deviations with a one-to-one mapping to the input bit stream based on the specified CPM symbol map.

Note

MT Apply Pulse Shaping Filter MSK, CPM

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Map Bits to Symbols

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-map-bits-to-fsk-symbols.html language=enus -->
## TOPIC 00084: MT Map Bits to FSK Symbols

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-map-bits-to-fsk-symbols.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-map-bits-to-fsk-symbols.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps an incoming bit stream to symbols comprised of FSK frequency deviations. input bit stream The incoming bit stream to be mapped to symbols. symbol map An ordered array that maps each symbol value to its desired deviation frequency. The number of FSK levels in the array must be 2^N, where N is th

MT Map Bits to FSK Symbols

Maps an incoming bit stream to symbols comprised of FSK frequency deviations.

[IMAGE alt='1378' src='MethodCall.MT_Map_Bits_to_FSK_Symbols.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The incoming bit stream to be mapped to symbols.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### symbol map

An ordered array that maps each symbol value to its desired deviation frequency.

The number of FSK levels in the array must be 2<sup>N</sup>, whereN is the number of bits per symbol. To specify a prebuilt map, unbundle the symbol map element from the FSK system parameters cluster generated by MT Generate FSK System Parameters (M) or MT Generate FSK System Parameters (map).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether stored state information is cleared on each call to this node.

When the input bit stream is not comprised of an integer number of symbols, the carryover bits are buffered.

| TRUE | Clears the buffered data, checks the input parameters on a first call, and reflects any change in the input parameter values during subsequent iterations. |
| --- | --- |
| FALSE | Adds the buffered data to the beginning of data from next iteration, in continuous operations. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### symbols

An array of FSK frequency deviations with a one-to-one mapping to the input bit stream based on the specified FSK symbol map.

Note

MT Apply Pulse Shaping Filter (FSK)

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Map Bits to Symbols

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-map-symbols-to-bits.html language=enus -->
## TOPIC 00085: MT Map Symbols to Bits

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-map-symbols-to-bits.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-map-symbols-to-bits.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps complex valued PSK-, QAM-, PAM-, ASK-, FSK-, MSK-, and CPM-modulated symbols to an output bit stream based on the symbol map that you specify.

MT Map Symbols to Bits

Maps complex valued PSK-, QAM-, PAM-, ASK-, FSK-, MSK-, and CPM-modulated symbols to an output bit stream based on the symbol map that you specify.

Utilities Nodes

MT Map ASK Symbols to Bits

output bit stream

MT Map CPM Symbols to Bits

output bit stream

MT Map FSK Symbols to Bits

output bit stream

MT Map MSK Symbols to Bits

output bit stream

MT Map PAM Symbols to Bits

output bit stream

MT Map PSK Symbols to Bits

output bit stream

MT Map QAM Symbols to Bits

output bit stream

Parent topic:

Utilities Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-matched-filter.html language=enus -->
## TOPIC 00086: MT Matched Filter

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-matched-filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-matched-filter.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies specified matched-filter coefficients to the input complex I/Q baseband waveform.

MT Matched Filter

Applies specified matched-filter coefficients to the input complex I/Q baseband waveform.

Utilities Nodes

MT Apply Matched Filter (CPM)

Applies a matched filter to a specified CPM-modulated waveform. The node first performs phase differentiation followed by matched filtering on the phase of the input complex waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring continuability from one iteration to the next.

MT Apply Matched Filter (FSK)

input complex waveform

MT Apply Matched Filter (Generic)

Applies a matched filter to a PAM, ASK, QAM, and PSK-modulated input waveform. The node returns the matched filtered output with a duration equal to an integer number of symbols, thus ensuring continuability from one iteration to the next.

MT Apply Matched Filter (MSK)

input complex waveform

Parent topic:

Utilities Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-measure-ask-quadrature-impairments.html language=enus -->
## TOPIC 00087: MT Measure ASK Quadrature Impairments

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-measure-ask-quadrature-impairments.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-measure-ask-quadrature-impairments.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates and reports amplitude-shift keying (ASK) quadrature impairments on a symbol-by-symbol basis at the symbol timing. Certain measurements like I/Q gain imbalance and quadrature skew are not applicable for the ASK modulation format because of the inherently one-dimensional nature of the ASK c

MT Measure ASK Quadrature Impairments

Calculates and reports amplitude-shift keying (ASK) quadrature impairments on a symbol-by-symbol basis at the symbol timing.

Note

[IMAGE alt='1378' src='MethodCall.MT_Measure_ASK_Quadrature_Impairments.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. Wire the output complex waveform parameter of MT Demodulate ASK to this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The demodulated bit stream from the output bit stream parameter of MT Demodulate ASK.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### impairment measurement window

The window over which impairments are measured.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

Index of the first sample of the measurement window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### width

Number of symbols over which to measure impairments. A value of -1 (default) measures impairments over all symbols. Positive values must be two or greater.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### ASK system parameters

Parameter values defining the ASK system. Wire the ASK system parameters cluster of MT Generate ASK System Parameters (M) or MT Generate ASK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each symbol to its desired level. The number of ASK levels in the array is 2<sup>N</sup>, where 
N is the number of bits per symbol. The vector length for the symbols farthest from the origin is 1.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines how the node handles bits from partial symbols in the input bit stream.

| TRUE | Discards bits making up incomplete symbols. |
| --- | --- |
| FALSE | Saves the leftover bits and starts with them on the next iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### magnitude error

The measured magnitude error as a percentage. Magnitude error is the magnitude difference between the ideal and the actual measured symbol locations.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### DC offset measurements

The measured DC offset of the I or Q waveforms as a percentage of the largest I and Q value in the symbol map of the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### I

The DC offset of the I waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Q

The DC offset of the Q waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### origin offset

The offset, in dB, of the constellation origin from its ideal location.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### phase error

The measured phase error in degrees. Notice that the phase offset is removed by the demodulator and is excluded from this measurement.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EVM

The measured error vector magnitude (EVM) expressed as a percentage.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### modulation error ratio

The measured modulation error ratio in dB.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Measure Quadrature Impairments

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-measure-burst-timing.html language=enus -->
## TOPIC 00088: MT Measure Burst Timing

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-measure-burst-timing.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-measure-burst-timing.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locates a burst within the input complex waveform with peaks correlating to the input ideal power curve. The upper mask, ideal power curve, and lower mask arrays must contain the same number of elements. input complex waveform The time-aligned and oversampled complex waveform data after matched filt

MT Measure Burst Timing

Locates a burst within the input complex waveform with peaks correlating to the input ideal power curve.

Note

upper mask

ideal power curve

lower mask

[IMAGE alt='1378' src='MethodCall.MT_Measure_Burst_Timing.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### input complex waveform

The time-aligned and oversampled complex waveform data after matched filtering and frequency offset correction.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### upper mask

The upper mask threshold for burst power in dB.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### ideal power curve

The best location for the power curve.

This curve is correlated against the input complex waveform to find the peak correlation. The ideal power curve must always be located between the upper mask and the lower mask.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### lower mask

The lower mask threshold for burst power in dB.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### impairment measurement window

The portion of the input complex waveform that is measured for amplitude droop and crest factor. This cluster is specified relative to the start of the region delineated by the upper mask, ideal power curve, and lower mask parameters.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

Index of the first sample of the measurement window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### width

Number of samples over which amplitude droop and crest factor are measured. This value must be 2 or greater.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### amplitude droop

The amplitude droop, in dB, calculated over the specified impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### pass?

A Boolean that determines whether the peak-correlated portion of the input complex waveform meets the upper mask and lower mask specifications.

| TRUE | Indicates that all samples fall within the region defined by the upper mask and lower mask parameters. |
| --- | --- |
| FALSE | Indicates that all samples do not fall within the region defined by the upper mask and lower mask parameters. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### first error sample index

The index value of the first sample in the peak-correlated portion of the input complex waveform that falls outside of the region defined by the upper mask and lower mask parameters. This index value is an offset into the upper mask/lower mask arrays.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### correlated burst index

Index value of the first sample in the peak-correlated portion of the input complex waveform, in samples. This index value is relative to the start of the input complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### crest factor

The measured crest factor of the power envelope calculated over the specified impairment measurement window.

The calculation is defined as the dimensionless quantity

where is the power envelope of the input complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Burst Timing

For burst signals, 
 burst timing refers to the location of the burst obtained by its correlation against an ideal power curve. In addition, an upper and lower mask are used to test whether the burst signal satisfies mask specifications. The following figure illustrates the ideal power curve, upper mask, and lower mask.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

This node compares the peak-correlated section with the upper mask and lower mask parameters to validate that the peak-correlated portion falls within the mask specification. Finally, the node measures and returns the amplitude droop and crest factor of the peak-correlated portion of the input complex waveform.

Parent topic:

Measurements Nodes

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-measure-cpm-quadrature-impairments.html language=enus -->
## TOPIC 00089: MT Measure CPM Quadrature Impairments

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-measure-cpm-quadrature-impairments.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-measure-cpm-quadrature-impairments.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures and reports quadrature impairments over a single user-specified window. This node must be called once for each measurement window. This node calculates continuous phase modulation (CPM) quadrature impairments on a point-by-point basis on the oversampled waveform. recovered complex waveform

MT Measure CPM Quadrature Impairments

Measures and reports quadrature impairments over a single user-specified window. This node must be called once for each measurement window. This node calculates continuous phase modulation (CPM) quadrature impairments on a point-by-point basis on the oversampled waveform.

[IMAGE alt='1378' src='MethodCall.MT_Measure_CPM_Quadrature_Impairments.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. Wire the recovered complex waveform parameter of MT Demodulate CPM to this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### detected complex waveform

The ideal oversampled waveform. Wire the detected complex waveform parameter of MT Demodulate CPM to this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### impairment measurement window

The window over which impairments are measured.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

Index of the first sample of the measurement window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### width

Number of symbols over which to measure impairments. A value of -1 (default) measures impairments over all symbols. Positive values must be two or greater.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### impairment definition

A value that indicates which set of equations is used to represent impairments.

In the equations in the following table, is the real component and is the imaginary component of each sample in the input complex waveform. and are the real and imaginary components of the corresponding sample in the output complex waveform. is I DC Offset (%) / 100, and is Q DC Offset (%) / 100.

| Vertical Shear | The definition uses the following equations for I/Q impairments: where φ is the specified quadrature skew, in radians = 10(IQ gain imbalance/20) In matrix form, these equations are represented by where |
| --- | --- |
| Axis Shear | With this option selected, this node uses an impairment definition that simplifies the conversion between measured impairments and their inverse impairments. For example, you may want to measure the I/Q impairments of a system and compensate for those impairments by applying the inverse impairments to the generated or received waveform. Using the Axis Shear definition, given a measured skew and imbalance (in dB), the inverse impairments are -1.0 * skew and -1.0 * imbalance. This definition uses the following equations for IQ impairments: where = 10(IQ gain imbalance/20) φ is the specified quadrature skew, in radians In matrix form, these equations are represented by where |

Default value: Vertical Shear

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### quadrature skew

The measured quadrature skew of the complex waveform in degrees.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per symbol in the modulated complex waveform.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### magnitude error

The measured magnitude error as a percentage. Magnitude error is the magnitude difference between the ideal and the actual measured symbol locations.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### DC offset measurements

The measured DC offset of the I or Q waveforms as a percentage of the largest I and Q value in the symbol map of the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### I

The DC offset of the I waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Q

The DC offset of the Q waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### origin offset

The offset, in dB, of the constellation origin from its ideal location.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### IQ gain imbalance

The measured ratio of I gain to Q gain, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### phase error

The measured phase error in degrees. Notice that the phase offset is removed by the demodulator and is excluded from this measurement.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EVM

The measured error vector magnitude (EVM) expressed as a percentage.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### modulation error ratio

The measured modulation error ratio in dB.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Measure Quadrature Impairments

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-measure-msk-quadrature-impairments.html language=enus -->
## TOPIC 00090: MT Measure MSK Quadrature Impairments

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-measure-msk-quadrature-impairments.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-measure-msk-quadrature-impairments.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates minimum-shift keying (MSK) quadrature impairments on a point-by-point basis on the oversampled waveform. recovered complex waveform The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. Wire the recovered

MT Measure MSK Quadrature Impairments

Calculates minimum-shift keying (MSK) quadrature impairments on a point-by-point basis on the oversampled waveform.

[IMAGE alt='1378' src='MethodCall.MT_Measure_MSK_Quadrature_Impairments.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. Wire the recovered complex waveform parameter of MT Demodulate MSK to this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### detected complex waveform

The ideal oversampled waveform. Wire the detected complex waveform parameter of MT Demodulate MSK to this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The ideal oversampled waveform as a complex-valued array.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### impairment measurement window

The window over which impairments are measured.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

Index of the first sample of the measurement window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### width

Number of symbols over which to measure impairments. A value of -1 (default) measures impairments over all symbols. Positive values must be two or greater.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

Number of samples per symbol in the modulated complex waveform.

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### impairment definition

A value that indicates which set of equations is used to represent impairments.

In the equations in the following table, is the real component and is the imaginary component of each sample in the input complex waveform. and are the real and imaginary components of the corresponding sample in the output complex waveform. is I DC Offset (%) / 100, and is Q DC Offset (%) / 100.

| Vertical Shear | The definition uses the following equations for I/Q impairments: where φ is the specified quadrature skew, in radians = 10(IQ gain imbalance/20) In matrix form, these equations are represented by where |
| --- | --- |
| Axis Shear | With this option selected, this node uses an impairment definition that simplifies the conversion between measured impairments and their inverse impairments. For example, you may want to measure the I/Q impairments of a system and compensate for those impairments by applying the inverse impairments to the generated or received waveform. Using the Axis Shear definition, given a measured skew and imbalance (in dB), the inverse impairments are -1.0 * skew and -1.0 * imbalance. This definition uses the following equations for IQ impairments: where = 10(IQ gain imbalance/20) φ is the specified quadrature skew, in radians In matrix form, these equations are represented by where |

Default value: Vertical Shear

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### magnitude error

The measured magnitude error as a percentage. Magnitude error is the magnitude difference between the ideal and the actual measured symbol locations.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### DC offset measurements

The measured DC offset of the I or Q waveforms as a percentage of the largest I and Q value in the symbol map of the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### I

The DC offset of the I waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Q

The DC offset of the Q waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### origin offset

The offset, in dB, of the constellation origin from its ideal location.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### quadrature skew

The measured quadrature skew of the complex waveform in degrees.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### IQ gain imbalance

The measured ratio of I gain to Q gain, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### phase error

The measured phase error in degrees. Notice that the phase offset is removed by the demodulator and is excluded from this measurement.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EVM

The measured error vector magnitude (EVM) expressed as a percentage.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### modulation error ratio

The measured modulation error ratio in dB.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Measure Quadrature Impairments

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-measure-pam-quadrature-impairments.html language=enus -->
## TOPIC 00091: MT Measure PAM Quadrature Impairments

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-measure-pam-quadrature-impairments.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-measure-pam-quadrature-impairments.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates and reports pulse-amplitude modulation (PAM) quadrature impairments on a symbol-by-symbol basis at the symbol timing. Certain measurements like I/Q gain imbalance and quadrature skew are not applicable for the PAM modulation format because of the inherently one-dimensional nature of the P

MT Measure PAM Quadrature Impairments

Calculates and reports pulse-amplitude modulation (PAM) quadrature impairments on a symbol-by-symbol basis at the symbol timing.

Note

I/Q gain imbalance

quadrature skew

[IMAGE alt='1378' src='MethodCall.MT_Measure_PAM_Quadrature_Impairments.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. Wire the recovered complex waveform parameter of MT Demodulate PAM to this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The demodulated bit stream from the output bit stream parameter of MT Demodulate PAM.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### impairment measurement window

The window over which impairments are measured.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

Index of the first sample of the measurement window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### width

Number of symbols over which to measure impairments. A value of -1 (default) measures impairments over all symbols. Positive values must be two or greater.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PAM system parameters

Parameter values defining the PAM system. Wire the PAM system parameters cluster of MT Generate PAM System Parameters (M) or MT Generate PAM System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each Boolean symbol to its desired coordinates in the complex plane. The number of states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines how the node handles bits from partial symbols in the input bit stream.

| TRUE | Discards bits making up incomplete symbols. |
| --- | --- |
| FALSE | Saves the leftover bits and starts with them on the next iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### magnitude error

The measured magnitude error as a percentage. Magnitude error is the magnitude difference between the ideal and the actual measured symbol locations.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### DC offset measurements

The measured DC offset of the I or Q waveforms as a percentage of the largest I and Q value in the symbol map of the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### I

The DC offset of the I waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Q

The DC offset of the Q waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### origin offset

The offset, in dB, of the constellation origin from its ideal location.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### phase error

The measured phase error in degrees. Notice that the phase offset is removed by the demodulator and is excluded from this measurement.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EVM

The measured error vector magnitude (EVM) expressed as a percentage.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### modulation error ratio

The measured modulation error ratio in dB.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Measure Quadrature Impairments

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-measure-psk-quadrature-impairments.html language=enus -->
## TOPIC 00092: MT Measure PSK Quadrature Impairments

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-measure-psk-quadrature-impairments.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-measure-psk-quadrature-impairments.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates and reports PSK quadrature impairments on a symbol-by-symbol basis at the symbol timing. recovered complex waveform The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. Wire the recovered complex waveform

MT Measure PSK Quadrature Impairments

Calculates and reports PSK quadrature impairments on a symbol-by-symbol basis at the symbol timing.

[IMAGE alt='1378' src='MethodCall.MT_Measure_PSK_Quadrature_Impairments.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### recovered complex waveform

The time-aligned and oversampled complex waveform data after matched filtering, frequency offset correction, and phase offset correction. Wire the recovered complex waveform parameter of MT Demodulate PSK to this parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the Y array.

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between data points in the Y array.

Default value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

The complex-valued signal-only baseband modulated waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The demodulated bit stream from the output bit stream parameter of MT Demodulate PSK.

[IMAGE alt='datatype_icon' src='/assets/img/cnclst.png']

##### impairment measurement window

The window over which impairments are measured.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

Index of the first sample of the measurement window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### width

Number of symbols over which to measure impairments. A value of -1 (default) measures impairments over all symbols. Positive values must be two or greater.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### PSK system parameters

Parameter values defining the PSK system. Wire the PSK system parameters cluster of MT Generate PSK System Parameters (M) or MT Generate PSK System Parameters (map) to this cluster. Do not alter the values.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per symbol

An even number of samples dedicated to each symbol. Multiply this value by the symbol rate to determine the sample rate.

Note

Default value: 16

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### symbol map

An ordered array that maps each Boolean symbol to its desired coordinates in the complex plane. The number of states in the array must be 2<sup>N</sup>, where 
N is the number of bits per symbol.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### differential PSK

A value that indicates how the PSK modulation represents symbols.

Differential operation is used to implement PSK formats such as differential quadrature PSK (DQPSK) and /4-DQPSK.

| disable | Symbols are represented as constellation points. |
| --- | --- |
| enable | Symbols are represented as the transitions between constellation points. |

Default value: 
 disable

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### PSK type

Type of PSK modulation.

| normal | Sets the modulation type to regular PSK. |
| --- | --- |
| shifted | Rotates the constellation by /M each symbol. |
| offset | Sets the modulation type to offset quadrature phase-shift keying (OQPSK). This modulation scheme is a form of phase-shift keying in which four different phase angles are used. This scheme is sometimes referred to as staggered quadrature phase-shift keying (SQPSK). For offset PSK, the ideal symbol timing for Q is offset by 1/2 of a symbol period from the ideal symbol timing for I. offset is currently only supported for M= 4. |

Default value: 
 normal

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### impairment definition

A value that indicates which set of equations is used to represent impairments.

In the equations in the following table, is the real component and is the imaginary component of each sample in the input complex waveform. and are the real and imaginary components of the corresponding sample in the output complex waveform. is I DC Offset (%) / 100, and is Q DC Offset (%) / 100.

| Vertical Shear | The definition uses the following equations for I/Q impairments: where φ is the specified quadrature skew, in radians = 10(IQ gain imbalance/20) In matrix form, these equations are represented by where |
| --- | --- |
| Axis Shear | With this option selected, this node uses an impairment definition that simplifies the conversion between measured impairments and their inverse impairments. For example, you may want to measure the I/Q impairments of a system and compensate for those impairments by applying the inverse impairments to the generated or received waveform. Using the Axis Shear definition, given a measured skew and imbalance (in dB), the inverse impairments are -1.0 * skew and -1.0 * imbalance. This definition uses the following equations for IQ impairments: where = 10(IQ gain imbalance/20) φ is the specified quadrature skew, in radians In matrix form, these equations are represented by where |

Default value: Vertical Shear

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines how the node handles bits from partial symbols in the input bit stream.

| TRUE | Discards bits making up incomplete symbols. |
| --- | --- |
| FALSE | Saves the leftover bits and starts with them on the next iteration. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### magnitude error

The measured magnitude error as a percentage. Magnitude error is the magnitude difference between the ideal and the actual measured symbol locations.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### DC offset measurements

The measured DC offset of the I or Q waveforms as a percentage of the largest I and Q value in the symbol map of the recovered complex waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### I

The DC offset of the I waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Q

The DC offset of the Q waveform, expressed as a percentage of the largest I or Q value in the symbol map.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### origin offset

The offset, in dB, of the constellation origin from its ideal location.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### quadrature skew

The measured quadrature skew of the complex waveform in degrees.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### IQ gain imbalance

The measured ratio of I gain to Q gain, in dB.

Tip

IQ gain imbalance

quadrature skew

DC offset measurements

modulation error ratio

error vector magnitude

magnitude error

phase error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### phase error

The measured phase error in degrees. Notice that the phase offset is removed by the demodulator and is excluded from this measurement.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EVM

The measured error vector magnitude (EVM) expressed as a percentage.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### RMS measurement

The RMS impairment value calculated over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### peak measurement

The peak impairment value measured over the impairment measurement window.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### peak symbol index

Index of the symbol having the peak magnitude of impairment.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### individual symbol measurements

The impairment value for each individual symbol.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### modulation error ratio

The measured modulation error ratio in dB.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Measure Quadrature Impairments

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-rayleigh-selective-fade-profile-gans.html language=enus -->
## TOPIC 00093: MT Rayleigh Selective Fading Profile (Gans)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-rayleigh-selective-fade-profile-gans.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-rayleigh-selective-fade-profile-gans.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a Rayleigh selective-fading profile for the multipath channel. The envelope for each path statistically obeys the Rayleigh distribution implemented using the Gans fading model. profile length The number of complex-valued fading profile samples (having Rayleigh-distributed envelopes) to gen

MT Rayleigh Selective Fading Profile (Gans)

Generates a Rayleigh selective-fading profile for the multipath channel. The envelope for each path statistically obeys the Rayleigh distribution implemented using the Gans fading model.

[IMAGE alt='1378' src='MethodCall.MT_Rayleigh_Selective_Fading_profile_(Gans).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### profile length

The number of complex-valued fading profile samples (having Rayleigh-distributed envelopes) to generate.

Default value: 1000

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sampling frequency

The system sample rate, in hertz (Hz). This rate is the product of the 
symbol rate × 
samples per symbol.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### doppler spread

The desired input Doppler spread 
f<sub>m</sub> of the channel, in hertz (Hz).

This parameter denotes the measure of the spectral broadening caused by the time rate of change of the channel. Doppler spread is defined as the range of frequencies over which the received Doppler spectrum is essentially nonzero. When a pure sine tone at frequency 
 f<sub>c</sub> is transmitted, the received signal spectrum, called the Doppler spectrum, has components in the range (f<sub>c</sub> - 
 f<sub>m</sub>) to (f<sub>c</sub> + 
 f<sub>m</sub>). The Doppler spread is related to the mobile velocity 
 v, carrier frequency 
 f<sub>c</sub>, and the speed of light 
 c by the relation 
 f<sub>m</sub> = 
 vf<sub>c</sub>/c.

Note

T

c

f

m

Default value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### seed in

The initial state for generating the fading profile. If seed in is set to -1, the generated fading profile is randomly chosen during every call when reset? is set to TRUE. Otherwise, the generated fading profile returns the same set of fading coefficients when reset? is set to TRUE.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of paths

The number of paths in the simulated multipath channel. A fading profile is generated for each of these paths.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### fading variance

The desired variance of the complex-valued Rayleigh distributed fading profile.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the fading profile generation is reset on subsequent calls to this node.

| TRUE | Resets the fading profile generation on every call to this node. |
| --- | --- |
| FALSE | Continues generating the fading profile from the previous iteration on subsequent calls. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### fading profile

A two-dimensional array of complex-valued coefficients. The number of rows corresponds to the number of paths in the channel, and the number of columns is equal to the profile length. Wire this parameter to MT Apply Fading Profile to apply this fading profile to a baseband I/Q signal.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### seed out

The internal state of the node at the end of generation of the fading profile for the current iteration.
 When reset? is set to FALSE, this state is used to continue the fading profile generation at the beginning of the next iteration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Rayleigh Distribution Equation

The Rayleigh distribution describes a flat-fading channel characterized by a single-tap impulse response with a time-varying envelope that is Rayleigh-distributed. This model describes the statistical time-varying nature of the received envelope of a flat fading channel or the envelope of an individual multipath component. The Rayleigh distribution has a probability density function (PDF) given by the following equation:

p

(

r

)

=

r

σ

2

exp

⁡

(

−

r

2

2

σ

2

)

u

(

r

)

p

(

r

)

=

r

σ

2

exp

⁡

(

−

r

2

2

σ

2

)

u

(

r

)

where 
 r is the specified fading variance.

#### Gans Model Equation

The Gans model generates the Rayleigh fading profile by passing quadrature Gaussian I/Q components through a Doppler filter with a U-shaped power spectral density profile. For the selective fading model, the implementation ensures that the generated fading profile for all paths is uncorrelated.

Parent topic:

MT Generate Fading Profile

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-rs-symbol-decoder-shortened.html language=enus -->
## TOPIC 00094: MT RS Symbol Decoder (shortened)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-rs-symbol-decoder-shortened.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-rs-symbol-decoder-shortened.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decodes a Reed-Solomon (RS) encoded integer symbol stream in shortened format. RS codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in which the code elements are drawn from the Galois field, GF(2m). RS codes are extremely powerful at burst error correction. The operations involved in Ree

MT RS Symbol Decoder (shortened)

Decodes a Reed-Solomon (RS) encoded integer symbol stream in shortened format.

RS codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in which the code elements are drawn from the Galois field, GF(2*m*). RS codes are extremely powerful at burst error correction. The operations involved in Reed-Solomon encoding and decoding are performed in the GF(2*m*). The RS encoder operates on code words that are symbols or groups of bits. The parameters code word length (n), symbols and data word length (k), symbols are specified in terms of symbols. Each symbol represents a group of Log<sub>2</sub>(*n*+1) bits.

Using shortened RS codes, the 
 *k* and 
 *n* values represent symbols. Each symbol has a length of 
 *m* bits, which is set using the bits per rs symbol parameter. Create a shortened RS code by setting the shortened values of 
 *n* and 
 *k*, as well as the bits per symbol that correspond to the underlying Galois field arithmetic. For example, you can set 
 *n* = 32, 
 *k* = 28, and bits per rs symbol = 8, to generate a shortened RS (32,28,2) code with an error-correcting capacity of 2 RS symbols. For this code, the underlying Galois field arithmetic is performed in GF(2<sup>*8*</sup>)=256.

[IMAGE alt='1378' src='MethodCall.MT_RS_Symbol_Decoder_(shortened).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### input symbols

The array of integer symbols to be decoded using the Reed-Solomon (RS) decoding scheme. Use the RS symbol encoder nodes to generate the integer symbols required for this parameter.

Note

n

output symbols

input symbols

L

input symbols

n

L

n

L

n

input symbols

reset?

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code word length (n), symbols

The length of the Reed-Solomon (RS) code word. Each RS symbol represents log<sub>2</sub>(n+1) bits.

Default value: 7

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data word length (k), symbols

The length of the Reed-Solomon (RS) data word. Each RS symbol represents log<sub>2</sub>(n+1) bits.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### modulation session

The modulation session for configuring selected properties of the Modulation nodes. Use this parameter to configure the advanced properties in the MT RS Symbol Encoder nodes. If MT RS Symbol Encoder is called with an uninitialized modulation session, the node returns an error.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per rs symbol

The number of bits per Reed-Solomon (RS) symbol. This parameter sets the Galois field over which the encoding operation is performed as GF(2<sup>bits per rs symbol</sup>). Valid values are 3 to 16, inclusive. For example, to set a shortened RS (32,28) code in the Galois field GF(256), set code word length (n), symbol as 32 symbols, data word length (k), symbol as 28 symbols, and bits per rs symbol as 8.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the decoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Galois field structure corresponding to the Reed-Solomon n, k values. |
| --- | --- |
| FALSE | Continues decoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to decoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### output symbols

The decoded integer symbol stream. Wire this parameter to MT UnPack Bits to recover the message bits that comprise the transmitted message data.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Reed Solomon Symbol Decode

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-rs-symbol-encoder-normal.html language=enus -->
## TOPIC 00095: MT RS Symbol Encoder (normal)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-rs-symbol-encoder-normal.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-rs-symbol-encoder-normal.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a Reed-Solomon (RS) encoded integer symbol stream in normal format. RS codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in which the code elements are drawn from the Galois field, GF(2m). RS codes are extremely powerful at burst error correction. The operations involved in Reed

MT RS Symbol Encoder (normal)

Generates a Reed-Solomon (RS) encoded integer symbol stream in normal format.

RS codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in which the code elements are drawn from the Galois field, GF(2*m*). RS codes are extremely powerful at burst error correction. The operations involved in Reed-Solomon encoding and decoding are performed in the GF(2*m*). The RS encoder operates on code words that are symbols or groups of bits. The parameters code word length (n), symbols and data word length (k), symbols are specified in terms of symbols. Each symbol represents a group of Log<sub>2</sub>(*n*+1) bits.

The normal RS (*n,k,t*) code consists of values of 
 *n* of the form 
 *n*=2<sup>*m*</sup>-1, where valid values of 
 *m* are 2 to 16, inclusive. For example, specify 
 *n* = 255, 
 *k* = 233 to produce a RS (255,233,11) code. This code has an error-correcting capacity of 11 RS symbols.

[IMAGE alt='1378' src='MethodCall.MT_RS_Symbol_Encoder_(normal).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### input symbols

The array of integer symbols to be encoded using the RS encoding scheme. Use MT Generate Bits followed by MT Pack Bits to generate the integer symbols required for this parameter.

Note

k

output symbols

input symbols

L

input symbols

k

L

k

L

k

input symbols

reset?

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code word length (n), symbols

The length of the Reed-Solomon (RS) code word. Each RS symbol represents log<sub>2</sub>(n+1) bits.

Default value: 7

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data word length (k), symbols

The length of the Reed-Solomon (RS) data word. Each RS symbol represents log<sub>2</sub>(n+1) bits.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### modulation session

The modulation session for configuring selected properties of the Modulation nodes. Use this parameter to configure the advanced properties in the MT RS Symbol Encoder nodes. If MT RS Symbol Encoder is called with an uninitialized modulation session, the node returns an error.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the encoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Galois field structure corresponding to the Reed-Solomon n, k values. |
| --- | --- |
| FALSE | Continues encoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to encoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### output symbols

The encoded integer symbol stream. Wire this parameter to the MT RS Symbol Decoder nodes to recover the input data stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Reed Solomon Symbol Encode

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-rs-symbol-encoder-shortened.html language=enus -->
## TOPIC 00096: MT RS Symbol Encoder (shortened)

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-rs-symbol-encoder-shortened.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-rs-symbol-encoder-shortened.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a Reed-Solomon (RS) encoded integer symbol stream in a shortened format. In the shortened RS codes, the k and n values represent symbols. Each symbol has a length, m bits, specified using the bits per RS symbol parameter. RS codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in w

MT RS Symbol Encoder (shortened)

Generates a Reed-Solomon (RS) encoded integer symbol stream in a shortened format. In the shortened RS codes, the 
*k* and 
*n* values represent symbols. Each symbol has a length, 
*m* bits, specified using the bits per RS symbol parameter.

RS codes are specialized Bose-Chaudhari-Hocquenghem (BCH) codes in which the code elements are drawn from the Galois field, GF(2*m*). RS codes are extremely powerful at burst error correction. The operations involved in Reed-Solomon encoding and decoding are performed in the GF(2*m*). The RS encoder operates on code words that are symbols or groups of bits. The parameters code word length (n), symbols and data word length (k), symbols are specified in terms of symbols. Each symbol represents a group of Log<sub>2</sub>(*n*+1) bits.

Specify a shortened RS code by stating the shortened values of 
 *n* and 
 *k*, as well as the bits per symbol that correspond to the underlying Galois field arithmetic. For example, you can specify code word length (n), symbols as 32, 
 data word length (k), symbols as 28, and bits per RS symbol as 8 to generate a shortened RS (32,28,2) code with error-correcting capacity of two RS symbols. For this code, the underlying Galois field arithmetic is performed in GF(2<sup>8</sup>) = 256.

[IMAGE alt='1378' src='MethodCall.MT_RS_Symbol_Encoder_(shortened).png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### input symbols

The array of integer symbols to be encoded using the RS encoding scheme. Use MT Generate Bits followed by MT Pack Bits to generate the integer symbols required for this parameter.

Note

k

output symbols

input symbols

L

input symbols

k

L

k

L

k

input symbols

reset?

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code word length (n), symbols

The length of the Reed-Solomon (RS) code word. Each RS symbol represents log<sub>2</sub>(n+1) bits.

Default value: 7

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data word length (k), symbols

The length of the Reed-Solomon (RS) data word. Each RS symbol represents log<sub>2</sub>(n+1) bits.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### modulation session

The modulation session for configuring selected properties of the Modulation nodes. Use this parameter to configure the advanced properties in the MT RS Symbol Encoder nodes. If MT RS Symbol Encoder is called with an uninitialized modulation session, the node returns an error.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per rs symbol

The number of bits per Reed-Solomon (RS) symbol. This parameter sets the Galois field over which the encoding operation is performed as GF(2<sup>bits per rs symbol</sup>). Valid values are 3 to 16, inclusive. For example, to set a shortened RS (32,28) code in the Galois field GF(256), set code word length (n), symbol as 32 symbols, data word length (k), symbol as 28 symbols, and bits per rs symbol as 8.

Default value: 3

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset?

A Boolean that determines whether the internal state of the encoder is cleared.

| TRUE | Clears any buffered bits from previous iterations. Also initializes the Galois field structure corresponding to the Reed-Solomon n, k values. |
| --- | --- |
| FALSE | Continues encoding from the previous iteration. Any buffered bits from the previous iteration are added to the beginning of the input bit stream prior to encoding. |

Default value: TRUE

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### output symbols

The encoded integer symbol stream. Wire this parameter to the MT RS Symbol Decoder nodes to recover the input data stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

MT Reed Solomon Symbol Encode

<!--NI_TOPIC bundle=labview-modulation-toolkit-api-ref path=mt-spread-symbols.html language=enus -->
## TOPIC 00097: MT Spread Symbols

- bundle_id: `labview-modulation-toolkit-api-ref`
- source_path: `mt-spread-symbols.html`
- source_url: https://docs-be.ni.com/bundle/labview-modulation-toolkit-api-ref/raw/resource/enus/mt-spread-symbols.html
- document_id: `labview-modulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the DSSS spreading operation using the spreading code that you specify. The spreading code algorithm performs non-return-to-zero (NRZ) encoding of the input bit stream and the spreading code. However, the output is an array of zeros and ones. input bit stream The sequence of information bit

MT Spread Symbols

Performs the DSSS spreading operation using the spreading code that you specify. The spreading code algorithm performs non-return-to-zero (NRZ) encoding of the input bit stream and the spreading code. However, the output is an array of zeros and ones.

[IMAGE alt='1378' src='MethodCall.MT_Spread_Symbols.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### input bit stream

The sequence of information bits to be spread.

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### spreading code

The sequence of bits that determine how the bits in input bit stream are spread.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1di8.png']

##### output chip stream

The sequence of data bits that is spread for transmission. The number of elements returned in this array equals the product of the input bit stream array length and the spreading code array length.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Spreading Operation

Each bit in the input bit stream is spread according to the following table.

| Spreading Input | Spreading Output |
| --- | --- |
| 0 | Spreading code |
| 1 | Complement of spreading code |

For example, an input bit stream array of 
 1100 and a spreading code value of 
 1010 return an output chip stream array of 
 0101 0101 1010 1010.

#### Direct Sequence Spread Spectrum (DSSS)

Direct Sequence Spread Spectrum (DSSS) is a process by which data is transmitted using a higher bandwidth signal as required by the data rate. Using DSSS allows multiple channels to occupy the same bandwidth, thus mitigating interference from other users at the expense of bandwidth expansion.

DSSS spreads each bit of signal data at the transmitter into 
 L chips using a pseudorandom L-chip spreading code called a code word. The length 
 L of the pseudorandom spreading code is also known as the bandwidth expansion factor because the chips are transmitted at a rate equal to 
 L * bit rate of the data. The spreading code appears random to all receivers except the intended one, which uses the knowledge of the spreading code to demodulate and recover the transmitted information. Thus, multiple channels can occupy the same portion of the frequency spectrum by using code words that have little or no correlation with one another, and little or no autocorrelation for any shift other than zero.

Mathematically, a DSSS signal is described by

y

(

t

)

=

∑

n

=

−

∞

∞

∑

m

=

0

L

−

1

a

n

⁢

c

m

g

(

T

−

n

T

−

m

T

c

)

y

(

t

)

=

∑

n

=

−

∞

∞

∑

m

=

0

L

−

1

a

n

⁢

c

m

g

(

T

−

n

T

−

m

T

c

)

where

y(T) is the transmitted DSSS signal

g(T) is the pulse-shaping signal of duration 
 T<sub>c</sub>

a
 <sub>n</sub> is the n<sup>th</sup> information bearing symbol

c
 <sub>m</sub> is the m<sup>th</sup> element of the L-long pseudorandom spreading code (also known as the chip sequence)

T
 <sub>c</sub> is the chip period

T = L * T<sub>c</sub> is the symbol period

Parent topic:

Coding Nodes
