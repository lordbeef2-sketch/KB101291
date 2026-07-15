# NI DOCUMENT BUNDLE: labview-digital-filter-design-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-digital-filter-design-toolkit start=1 end=99 -->
<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=advanced-techniques-for-designing-filters-dig.html language=enus -->
## TOPIC 00001: Advanced Techniques for Designing Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `advanced-techniques-for-designing-filters-dig.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/advanced-techniques-for-designing-filters-dig.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains an overview of advanced techniques for developing digital filters with the DFD Remez Design VI and the DFD Least Pth Norm Design VI. The LabVIEW Digital Filter Design Toolkit user manual contains more information about these advanced techniques.

### Advanced Techniques for Designing
 Filters

This section contains an overview of advanced techniques for developing digital filters with the
 DFD Remez Design VI and the DFD Least
 Pth Norm Design VI. The *LabVIEW Digital Filter
 Design Toolkit* user manual contains more information about
 these advanced techniques.

Parent topic:

LabVIEW Digital Filter Design Concepts

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=analyze-fixed-point-filters-digital-filter.html language=enus -->
## TOPIC 00002: Analyze Fixed-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `analyze-fixed-point-filters-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/analyze-fixed-point-filters-digital-filter.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Filter Analysis Express VI to observe the response of the fixed-point filter. Use the calculated results to optimize the fixed-point filter.The Filter Analysis Express VI performs fixed-point analysis in the frequency domain. You might need to analyze and adjust the filter design iteratively

### Analyze Fixed-Point Filters

Use the Filter Analysis Express VI to observe the response of the
 fixed-point filter. Use the calculated results to optimize the fixed-point filter.

The Filter Analysis Express VI performs fixed-point analysis in the frequency
 domain. You might need to analyze and adjust the filter design iteratively until the
 calculated results are satisfactory.

Ensure that the fixed-point filter is stable by verifying that all poles are within the unit
 circle and that the filter maintains a satisfactory frequency response. If the
 fixed-point characteristics do not satisfy the requirements, try one or more of the
 following options:

- Return to the quantization step and change the quantizer settings.
- Change the implementation structure.
- Change the floating-point reference filter specifications to allow more headroom for finite-precision effects.
- For Infinite Impulse Response (IIR) filters, reduce the pole radius constraint of the reference
 floating-point filter.

DFD FXP Coef Report

iwl

iwl

iwl

iwl

wl

Note

Parent topic:

Design Fixed-Point Filters

Related concepts:

- Select a Filter Structure
- Enter Floating-Point Filter Specifications

Related tasks:

- Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=analyze-fixed-point-multirate-filters.html language=enus -->
## TOPIC 00003: Analyze Fixed-Point Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `analyze-fixed-point-multirate-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/analyze-fixed-point-multirate-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Multirate Filter Analysis VIs can be used to calculate the frequency response of the fixed-point multirate filter and, based on the frequency response results, it can be determined if the fixed-point filter meets the requirements. Quantization can cause the characteristics of a fixed-point multi

### Analyze Fixed-Point Multirate Filters

The Multirate Filter Analysis VIs can be used to calculate the
 frequency response of the fixed-point multirate filter and, based on the frequency
 response results, it can be determined if the fixed-point filter meets the
 requirements.

Quantization can cause the characteristics of a fixed-point multirate filter to deviate
 from the reference floating-point multirate filter. Sometimes quantization even causes
 the resulting fixed-point multirate filter to fail to meet the target specifications.
 Therefore, after quantization, you must analyze the behavior of the fixed-point
 multirate filter. If the fixed-point filter does not meet the target specifications, try
 either or both of the following methods:

- Modify the quantization settings for the word length of the coefficients.
- Modify the specifications of the reference floating-point multirate filter to allow
 larger headroom. A larger headroom helps alleviate fixed-point effects.

To optimize the resulting multirate fixed-point filter, analyze and adjust the filter
 design iteratively until the frequency response meets the target specifications.

Parent topic:

Design Fixed-Point Multirate Filters

Related concepts:

- Analyze Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=analyze-floating-point-filters-digital-filt.html language=enus -->
## TOPIC 00004: Analyze Floating-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `analyze-floating-point-filters-digital-filt.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/analyze-floating-point-filters-digital-filt.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Magnitude Response After you enter the target specifications for a digital filter, you can analyze the characteristics of the resulting filter in the Configure Classical Filter Design dialog box of the Classical Filter Design Express VI by evaluating the pole-zero plot, the magnitude response, and t

### Analyze Floating-Point Filters

#### Magnitude Response

After
 you enter the target specifications for a digital filter, you can analyze the
 characteristics of the resulting filter in the Configure Classical Filter
 Design dialog box of the Classical Filter Design
 Express VI by evaluating the pole-zero plot, the magnitude response,
 and the filter order.

The frequency response of a digital filter is defined by
 H(e<sup>j2πf</sup>),
 and the magnitude response is defined by
 |H(e<sup>j2πf</sup>)|.
 For discrete-time systems,
 H(e<sup>j2πf</sup>)
 is periodic with a period of f<sub>s</sub>.
 For real-valued digital filters, the magnitude response is symmetric with respect to
 0, ±f<sub>s</sub>,
 ±2f<sub>s</sub>, ….
 Therefore, you can calculate the magnitude response for only [0,
 f<sub>s</sub>/2], which contains the
 frequencies between 0 and the Nyquist frequency. The magnitude response graph in the
 Configure Classical Filter Design dialog box includes a
 green vertical line to indicate the location of
 f<sub>s</sub>/2.

#### Filter Order
 Specification

The Classical Filter Design Express VI
 automatically computes the minimal filter order required to fulfill the given filter
 specification and displays the order in the Filter order
 indicator. With the same specification, you can use different algorithms to create
 digital filters with different filter orders. You can estimate the computational
 complexity and cost based on the filter order. If you have strict requirements for
 the system, the filter order can help you determine if the filter is
 acceptable.

Parent topic:

Design Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=analyze-floatnig-point-multirate-filter-design.html language=enus -->
## TOPIC 00005: Analyze the Floating-Point Multirate Filter Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `analyze-floatnig-point-multirate-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/analyze-floatnig-point-multirate-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you design the multirate filter using the Multirate FIR Design Express VI, you can analyze the filter design by examining the magnitude response and filter order in real time.

### Analyze the Floating-Point Multirate Filter
 Design

When you design the multirate filter using the Multirate FIR Design
 Express VI, you can analyze the filter design by examining
 the magnitude response and filter order in real time.

Parent topic:

Design Floating-Point Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=approximated-linear-phase-iir-design-digital.html language=enus -->
## TOPIC 00006: Approximated Linear Phase IIR Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `approximated-linear-phase-iir-design-digital.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/approximated-linear-phase-iir-design-digital.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Although it is theoretically impossible to design causal IIR digital filters with exactly linear phase, you can design IIR filters with approximately linear phase using the DFD Least Pth Norm Design VI.You must set filter type to Symmetric or Antisymmetric.For example, suppose you want to design an

### Approximated Linear Phase IIR Design

Although it is theoretically impossible to design causal IIR digital filters with exactly
 linear phase, you can design IIR filters with approximately linear phase using the
 DFD Least Pth Norm Design VI.

You must set filter type to Symmetric or
 Antisymmetric.

For example, suppose you want to design an approximately linear phase IIR lowpass filter with a
 passband frequency range of [0, 0.2] and a stopband frequency range of
 [0.3, 0.5]. You can set the specifications as shown in the
 following figure:

Figure 50.

[IMAGE alt='image' src='GUID-CB03016C-9A56-4477-9488-B85498159C5B-a5.gif']

The following figure shows the magnitude response of the designed filter:

Figure 51.

[IMAGE alt='image' src='GUID-ECDCCC63-DF36-4862-AF82-ABE7FB707A3D-a5.gif']

The following figure shows the phase response of the designed filter:

Figure 52.

[IMAGE alt='image' src='GUID-FBE07A52-6592-4D37-9D34-7AC92E46D913-a5.gif']

Notice that this filter has greater stopband attenuation than the linear phase FIR filter designed, and this filter keeps the passband phase response roughly linear.

Parent topic:

Least Pth Norm Design Method

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=arbitrary-shape-filters-digital-filter-design.html language=enus -->
## TOPIC 00007: Arbitrary Shape Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `arbitrary-shape-filters-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/arbitrary-shape-filters-digital-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An arbitrary frequency response can be described with multiple points using piecewise linear interpolation.If you want to design a linear phase Finite Impulse Response (FIR) filter with an arbitrary magnitude response, you can use the DFD Remez Design VI. If you want to design a filter in which line

### Arbitrary Shape Filters

An arbitrary frequency response can be described with multiple points using piecewise
 linear interpolation.

If you want to design a linear phase Finite Impulse Response (FIR) filter with an arbitrary
 magnitude response, you can use the DFD Remez Design VI. If you want
 to design a filter in which linear phase is not required but minimizing filter order is
 important, you can use the DFD Least Pth Norm Design VI to design an
 Infinite Impulse Response (IIR) filter.

The number of points you must supply to describe the shape depends on the target
 arbitrary shape magnitude response in a certain frequency band. You do not have to space
 the points evenly. Use more points where the magnitude response is tightly curved and
 fewer points where the magnitude response is more linear.

#### FIR Filters with Arbitrary Magnitude
 Responses

To design a linear phase FIR filter with an arbitrary shape
 magnitude response, use the DFD Remez Design VI and set the
 filter type input to Symmetric or
 Antisymmetric according to the linear phase FIR filter type
 table. Then describe the shape of the filter by specifying multiple points in the
 band specs input.

The following example uses a
 lowpass filter with a passband frequency ranging from 0 to 0.25 and a stopband
 frequency ranging from 0.3 to 0.5. Three points at frequencies 0, 0.1, and 0.25 with
 expected amplitudes of 1, 2, and 1, respectively, describe the shape of the passband
 range. To design this filter, enter the specifications shown in the following figure
 into the DFD Remez Design VI:

[IMAGE alt='image' src='GUID-E3DC16BC-2429-4AA5-BE83-FB061CB2623B-a5.gif']

The following figure shows the magnitude response of the designed
 filter:

[IMAGE alt='image' src='GUID-2CFF8AAC-95DC-4B2D-869F-8B3E26978B79-a5.gif']

The previous example describes the passband shape with only three points. You
 also can describe an arbitrary passband shape with as many points as necessary. The
 following example uses 5,000 evenly-shaped frequency points to describe the passband
 shape of a sinc compensation lowpass filter. You can use this sinc compensator to
 correct the amplitude droop caused by a zero-order hold in a Digital-to-Analog (D/A)
 converter, as shown in the following figure:

[IMAGE alt='image' src='GUID-35FC6F90-E086-4765-A5F0-4F857FE830DB-a5.gif']

An amplitude droop measures the amount that the signal power decreases in a
 specified frequency range. In the previous figure, the Zero-Order
 Hold plot shows the magnitude response of a zero-order hold in the
 D/A converter. You can see an amplitude droop exists in the frequency range of
 interest [0, 0.2]. To correct the amplitude droop, you can create a filter that
 whose magnitude response is similar to the Anti-Sinc
 Compensator plot in the frequency range of interest [0, 0.2]. You
 can create the filter by describing the passband shape with the corresponding
 inverse sinc function values of the droop. The following figure shows the magnitude
 response of the designed filter:

[IMAGE alt='image' src='GUID-869EBE52-E703-443A-89B4-FE1994E0FAB9-a5.gif']

#### IIR Filters with Arbitrary Magnitude
 Responses

If you want to design an IIR filter with an arbitrary shape
 magnitude response and the phase response is not important, use the DFD
 Least Pth Norm Design VI and set the filter
 type input to either Minimum Phase or
 Maximum Phase. The DFD Least Pth Norm Design
 VI ignores all other phase specification inputs, including group
 delay and phase in the band
 specs input. Define the shape of the magnitude response by entering
 multiple points in the band specs input.

For example,
 you can design a minimum phase IIR filter with the same arbitrary magnitude response
 as the previous example. Set the filter type input to
 Minimum Phase and enter the same band
 specs into the DFD Least Pth Norm Design VI. The
 following figure shows the magnitude response of the designed filter:

[IMAGE alt='image' src='GUID-BCCC72CC-E4E7-4FDB-AF91-F7EBF3D22F03-a5.gif']

Parent topic:

Design Special Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=cascaded-integrator-comb-filters-digital-filt.html language=enus -->
## TOPIC 00008: Cascaded Integrator Comb Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `cascaded-integrator-comb-filters-digital-filt.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/cascaded-integrator-comb-filters-digital-filt.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Cascaded Integrator Comb (CIC) filter is a special class of linear phase, Finite Impulse Response (FIR) filter as they do not require multipliers and use a limited amount of storage, thus CIC filters are more efficient than conventional FIR filters, especially in fixed-point applications.The CIC f

### Cascaded Integrator Comb Filters

A Cascaded Integrator Comb (CIC) filter is a special class of linear phase, Finite
 Impulse Response (FIR) filter as they do not require multipliers and use a limited
 amount of storage, thus CIC filters are more efficient than conventional FIR filters,
 especially in fixed-point applications.

The CIC filters can be used in multirate systems with large sampling frequency conversion
 factors, such as Digital Downconverters (DDC) and Digital Upconverters (DUC) in
 communication systems.

Parent topic:

Design Special Multirate Filters

Related concepts:

- Group Delay and Phase Delay
- FIR Structures

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=categorize-filter-banks-digital-filter-desi.html language=enus -->
## TOPIC 00009: Categorize Filter Banks

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `categorize-filter-banks-digital-filter-desi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/categorize-filter-banks-digital-filter-desi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Uniform and Non-Uniform Filter Banks You can categorize filter banks according to the bandwidths of the subbands or the number of subbands. You can categorize filter banks into uniform filter banks and non-uniform filter banks according to the bandwidths of the subbands. The following figure shows t

### Categorize Filter Banks

#### Uniform and
 Non-Uniform Filter Banks

You can categorize filter banks
 according to the bandwidths of the subbands or the number of
 subbands.

You can categorize filter banks into uniform filter
 banks and non-uniform filter banks according to the bandwidths of
 the subbands. The following figure shows the magnitude response of a
 uniform filter bank:

Figure 38.

[IMAGE alt='image' src='GUID-B39A0698-2310-4F76-B4B8-2007C0C68C97-a5.gif']

The filter bank separates the signal spectrum into uniformly spaced
 subbands. Uniform filter banks in the LabVIEW Digital Filter Design
 Toolkit have the property that the number of subbands is equal to
 the decimation factor of the subband filters. This is known as a
 critically sampled uniform filter bank. The subband number of a
 critically sampled uniform filter bank is equivalent to the
 decimation factor M, with subband bandwidth
 2π/M.

A uniform filter bank has
 uniformly spaced subband bandwidths, which results in a fixed
 subband resolution in all frequency areas. The following figure
 illustrates how a non-uniform filter bank can have different subband
 resolutions in different frequency areas:

Figure 39.

[IMAGE alt='image' src='GUID-A78EE895-8CDE-41D5-8815-E5FC41209801-a5.gif']

In the previous figure, the subband bandwidth in the lower frequency
 area is narrower than the subband bandwidth in the higher frequency
 area. Therefore, this non-uniform filter bank can achieve a higher
 resolution than a uniform filter bank in the low frequency
 area.

#### 2-band and M-band
 Filter Banks

You also can categorize filter banks as
 2-band and M-band filter banks according to the number of
 subbands.

Wavelet analysis uses 2-band filter banks, also
 called Quadrature Mirror Filter (QMF) filter banks. In a QMF filter
 bank, the magnitude responses of the lowpass band filter and the
 highpass band filter in the analysis bank are symmetric about
 π/2.

One approach to M-band filter bank design is to apply a
 cosine modulation to a prototype lowpass filter. The M-band
 cosine-modulated filter banks used in the LabVIEW Digital Filter
 Design Toolkit are critically sampled filter banks.

The
 advantages of cosine-modulated filter bank design are as
 follows:

- You can reduce the design complexity as you need to design only
 one prototype lowpass filter. The analysis and synthesis
 filters are frequency-shifted versions of the prototype
 filter.
- It is feasible to design perfect reconstruction cosine-modulated
 filter banks.
- The analysis and synthesis filters have real-valued
 coefficients.

Parent topic:

Filter Bank Design Basics

Related concepts:

- Filter Bank Design Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=cic-filter-basics.html language=enus -->
## TOPIC 00010: CIC Filter Basics

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `cic-filter-basics.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/cic-filter-basics.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: CIC filters do not have multipliers and consist of only adders, subtracters, and registers. Therefore, you can implement multirate filters efficiently using the CIC filter structure. CIC filters are defined by the following transfer function: H ⁢   ( z )     = H I N ⁢ ( z )   H C N ⁢ ( z ) = ( 1 − z

### CIC Filter Basics

CIC filters do not have multipliers and consist of only adders, subtracters, and
 registers. Therefore, you can implement multirate filters efficiently using the CIC
 filter structure. CIC filters are defined by the following transfer function:

H

⁢

(

z

)

=

H

I

N

⁢

(

z

)

H

C

N

⁢

(

z

)

=

(

1

−

z

−

R

M

)

N

⁢

(

1

−

z

−

1

)

N

=

(

∑

k

=

0

R

M

−

1

z

−

k

)

N

where

- z is a complex variable
- I is a basic integrator section
- C is a basic comb section
- M is the sampling frequency conversion factor
- R is the differential delay
- N is the number of stages

Theoretically, R and N can be any positive
 integer value, but the LabVIEW Digital Filter Design Toolkit constrains
 R to be either 1 or 2
 because you do not need to use other values in most cases. N is
 in the range [1, 8]. The equation above shows that a CIC filter is equivalent to
 N stages of cascaded FIR filters with unit coefficients. Each
 FIR filter has a rectangular impulse response. All coefficients of the FIR filters
 are 1 and therefore symmetric, so the CIC filter has a linear phase
 response and constant group delay.

Use the Multirate CIC Design
 Express VI to design a CIC filter.

Parent topic:

Cascaded Integrator Comb Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=comb-filters-digital-filter-design-toolkit.html language=enus -->
## TOPIC 00011: Comb Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `comb-filters-digital-filter-design-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/comb-filters-digital-filter-design-toolkit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use comb filters to suppress, cancel, or enhance more than one frequency.The DFD IIR Notch Peak Design VI helps you design notch and peak filters that suppress noise or enhance a signal at one particular frequency. However, when you want to suppress noise or enhance a signal at more than one frequen

### Comb Filters

Use comb filters to suppress, cancel, or enhance more than one frequency.

The DFD IIR Notch Peak Design VI helps you design notch and peak filters that
 suppress noise or enhance a signal at one particular frequency. However, when you want
 to suppress noise or enhance a signal at more than one frequency you can use a comb
 notch/peak filter. For example, you might need to cancel the AC powerline fundamental
 and harmonics. A comb filter would accomplish this.

Comb filters also can separate two signals with different frequency harmonics. For example, in
 color TV systems, comb filters separate the luminance component and chrominance
 component from the composite video signal.

The following table lists each type of comb filter with its transfer function and magnitude response. Notice that you can create two types of comb notch/peak filters. One type has notches or peaks at the frequencies kf<sub>s/N</sub>, while the other type has notches or peaks at the frequencies (k+1/2)f<sub>s</sub>/N, where k is an integer in the range [0, N−1].

| Filter | Transfer Function | Magnitude Response (N = 10) |
| --- | --- | --- |
| Notch Type I | b⁢ (1−z−N⁢ )1−az−N |  |
| Notch Type II | b⁢ (1+z−N⁢ )1+az−N |  |
| Peak Type I | b⁢ (1+z−N⁢ )1−az−N |  |
| Peak Type II | b⁢ (1+z−N⁢ )1−az−N |  |

The following figure shows the implementation of a comb filter:

[IMAGE alt='image' src='GUID-3290D00F-02BD-4A0D-A382-7ABBA2C24632-a5.gif']

In this figure, you can see that the implementation of the comb filter requires only two adders
 and two multipliers, which makes the comb filter efficient in many applications.

The following figure shows a typical Type I comb notch filter in which the first notch occurs at
 f = 0, or equivalently, (|H(0)| = 0):

[IMAGE alt='image' src='GUID-231D9F32-F3EA-46E8-8538-6FF3795F49E2-a5.gif']

The following figure shows a typical Type II comb notch filter in which the first notch occurs at
 f = f<sub>0</sub>, or equivalently, (|H(0)| = 1):

[IMAGE alt='image' src='GUID-33B78589-3C01-4346-99D5-1D007103EEAE-a5.gif']

The following figure shows a typical Type I comb peak filter in which the first peak occurs at
 f = 0, or equivalently, (|H(0)| = 1):

[IMAGE alt='image' src='GUID-B0BD0428-B598-4EB2-A855-1D6A3C01701B-a5.gif']

The following figure shows a typical Type II comb peak filter in which the first peak occurs at
 f = f<sub>0</sub>, or equivalently, (|H(0)| = 0):

[IMAGE alt='image' src='GUID-0E677C09-3BDF-4C25-ABB3-2A68F8BD621E-a5.gif']

From the previous figures, you can see that a comb filter is characterized by the parameters
 f<sub>0</sub>, A<sub>b</sub>, and Δf. f<sub>0</sub>
 denotes the center frequency of the notch or peak, A<sub>b</sub> denotes a level on the magnitude squared response of the filter in
 decibels, and Δf denotes the frequency bandwidth at
 A<sub>b</sub>. The default value of
 A<sub>b</sub> is −3 dB, which represents the
 half maximum value of the magnitude squared response. Use the DFD IIR Comb
 Design VI to design a comb notch or peak filter. This VI enables you to
 design the comb notch or peak filter either by specifying the center frequency and the
 bandwidth of the notch/peak or by specifying the number of notches/peaks and the
 bandwidth.

For example, assume a time waveform of a noisy Electrocardiogram (ECG) signal sampled at 480 Hz,
 as shown in the following figure:

[IMAGE alt='image' src='GUID-D2F5D0D3-FACD-4417-99B5-30A4724DCC58-a5.gif']

The following figure shows the spectrum of the same noisy signal. In this figure, you can
 identify noise at 60 Hz, 120 Hz, and 180 Hz:

[IMAGE alt='image' src='GUID-9DFFE868-DCB1-4AB1-9916-4BC73D007263-a5.gif']

To remove the noise, you can use the By f0 and Bandwidth instance of the DFD IIR Comb
 Design VI to design a comb notch filter with the following
 specifications:

| DFD IIR Comb Design VI Inputs | Value |
| --- | --- |
| filter type | Notch Type I |
| f0 [Hz] | 60 |
| Δf [Hz] | 0.5 |
| fs [Hz] | 480 |

The following figure shows the magnitude response of the resulting comb filter:

[IMAGE alt='image' src='GUID-31ABD189-DA65-4CCA-8B52-67E04F554DFE-a5.gif']

The following figure shows that the filtered ECG signal is close to the original noise-free
 samples:

[IMAGE alt='image' src='GUID-3D1E4B5B-4EC4-47F3-A625-6DA33C0A07B5-a5.gif']

Parent topic:

Design Special Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=create-fixed-point-multirate-filter-models.html language=enus -->
## TOPIC 00012: Create Fixed-Point Multirate Filter Models

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `create-fixed-point-multirate-filter-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/create-fixed-point-multirate-filter-models.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Following to designing a fixed-point multirate filter, fixed-point quantization occurs for the coefficients and for the intermediate operands and results. By using the DFD FXP MRate Modeling VI, only the quantizers for the input and output signals require configuration. The DFD FXP MRate Modeling VI

### Create Fixed-Point Multirate Filter
 Models

Following to designing a fixed-point multirate filter, fixed-point quantization occurs
 for the coefficients and for the intermediate operands and results. By using the
 DFD FXP MRate Modeling VI, only the quantizers for the input and
 output signals require configuration.

The DFD FXP MRate Modeling VI automatically configures the quantizers
 for intermediate operands.

#### Setting the Input Word Length, Input
 Integer Word Length, and Output Word Length

Use the DFD FXP MRate Modeling VI to specify input word length,
 input integer word length, and output word length. These word lengths determine the
 number of bits to use in representing the input and output signals. The DFD
 FXP MRate Modeling VI automatically configures the integer word length
 of the output signal.

#### Setting the Rounding Mode

Fixed-point numbers have limited word lengths, so the available dynamic range of
 fixed-point numbers is lower than the range available with double-precision and
 floating-point numbers. Therefore, fixed-point numbers can approximate
 floating-point numbers only. In the LabVIEW Digital Filter Design Toolkit, the
 Multirate Fixed-Point Tools VIs use up to 48 bits for internal operations. Use the
 output rounding mode input of the DFD FXP MRate
 Modeling VI to configure the output quantizer.

Parent topic:

Design Fixed-Point Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=creating-fixed-point-filter-models-digital-fi.html language=enus -->
## TOPIC 00013: Create Fixed-Point Filter Models

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `creating-fixed-point-filter-models-digital-fi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/creating-fixed-point-filter-models-digital-fi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In a fixed-point implementation, after quantizing the coefficients of a reference floating-point filter, you also must configure all other quantizers, such as the input, output, and multiplicand quantizers. This process creates a fixed-point model for the filter. You must create a fixed-point filter

### Create Fixed-Point Filter Models

In a fixed-point implementation, after quantizing the coefficients of a reference
 floating-point filter, you also must configure all other quantizers, such as the
 input, output, and multiplicand quantizers. This process creates a fixed-point model
 for the filter.

DFD FXP
 Modeling

DFD FXP Set Quantizer

Details

DFD FXP Set Quantizer

Note

16

Specifying the Word Length
 and Integer Word Length

If you use the DFD FXP Modeling VI to create the fixed-point
 filter model, complete the following steps:

1. Specify the word lengths and integer word lengths for the input signal and word lengths for the output signal.
2. Set the rounding mode for the output signal.

DFD FXP Modeling

DFD FXP Get Quantizer

DFD FXP Set
 Quantizer

Note

overflow mode

Saturate

If you use the DFD FXP Set Quantizer VI to create the fixed-point filter
 model, you must configure the quantizers.

Parent topic:

Design Fixed-Point Filters

Related concepts:

- Filter Coefficients and Quantizers
- Specify the Word Length and Integer Word Length
- Set the Rounding Mode

Related tasks:

- Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=decimation-digital-filter-design-toolkit.html language=enus -->
## TOPIC 00014: Decimation

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `decimation-digital-filter-design-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/decimation-digital-filter-design-toolkit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Decimation (also known as down-sampling) is the process of reducing the sampling frequency of a signal to a lower sampling frequency that differs from the original frequency by an integer value.The lowpass filtering associated with decimation removes high-frequency content from the signal to accommo

### Decimation

Decimation (also known as down-sampling) is the process of reducing the sampling
 frequency of a signal to a lower sampling frequency that differs from the original
 frequency by an integer value.

The lowpass filtering associated with decimation removes high-frequency content from the signal
 to accommodate the new sampling frequency.

Decimation is useful in applications in which the Nyquist frequency of a signal is much higher
 than the highest frequency of the signal. Decimation filters help you remove the excess
 bandwidth and reduce the sampling frequency of the signal. Decimation filters also help
 you reduce the computational resources required for processing and storing the signal.
 During the Analog-to-Digital (A/D) conversion process, decimation filters also can
 reduce the variance of quantization noise in a signal and maintain the signal power,
 thus improving the Signal-to-Noise Ratio (SNR).

The following figure shows a typical M-fold decimation filter, where
 M is the integer value by which you want to decrease the sampling
 frequency. This filter contains a lowpass FIR filter
 H(z). This lowpass FIR filter is an
 anti-aliasing filter followed by an M-fold decimator. The decimator
 passes every M<sup>th</sup> sample and discards the other samples.
 After this operation, the decimation filter changes the sampling frequency
 f<sub>s</sub> of the input signal
 x(n) to a new sampling frequency
 f<sub>s</sub>/M. The
 decimation filter then returns an output signal
 y(n) with the new sampling frequency.

Figure 16.

[IMAGE alt='image' src='GUID-9A774E1A-88AD-46DE-BD55-6EF66CFC8B53-a5.gif']

H

z

M

f

s

M

f

s

M

f

s

M

H

z

Note

The following figure illustrates the potentially harmful effects of not using an anti-aliasing
 filter before the decimator.

Figure 17.

[IMAGE alt='image' src='GUID-6DFC150D-3B50-4096-9EB4-7C00C4AB45A7-a5.gif']

(a)

x

n

(b)

y

n

(c)

y

n

(d)

y

n

M

This figure shows the spectrum of the original signal
 x(n) and the spectra of the signals resulting
 from decimating the original signal by 2, 3, and M. Notice the
 overlapping spectra in parts (c) and (d) of the figure. The overlapping spectra indicate
 aliasing due to the decimation operation.

To design decimation filters, use the Multirate Filter Design VIs with the
 filtering mode input set to Decimation.

Parent topic:

Multirate Filter Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-filter-banks-digital-filter-design.html language=enus -->
## TOPIC 00015: Designing Filter Banks

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-filter-banks-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-filter-banks-digital-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about using the LabVIEW Digital Filter Design Toolkit to design filter banks.

### Designing Filter Banks

This section contains information about using the
 LabVIEW Digital Filter Design Toolkit to design
 filter banks.

- [Filter Bank Design Process](filter-bank-design-process-digital-filter-des.html)
- [Filter Bank Design Basics](filter-bank-design-basics-digital-filter-desi.html)
- [Enter Filter Bank Specifications](enter-filter-bank-specifications-digital-f.html)

Parent topic:

LabVIEW Digital Filter Design Concepts

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-fixed-point-multirate-filters-digit.html language=enus -->
## TOPIC 00016: Design Fixed-Point Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-fixed-point-multirate-filters-digit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-fixed-point-multirate-filters-digit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates a typical fixed-point multirate filter design process. The grey boxes illustrate the floating-point filter design process and the arrows on the left indicate to which steps you can return if the filter design fails to meet the requirements in the current step. 20 Typ

### Design Fixed-Point Multirate Filters

The following figure illustrates a typical fixed-point multirate filter design process. The grey
 boxes illustrate the floating-point filter design process and the arrows on the left
 indicate to which steps you can return if the filter design fails to meet the
 requirements in the current step.

Figure 20.

[IMAGE alt='image' src='GUID-72071E0E-A5D9-4E92-B0AD-68ABA7DFC163-a5.gif']

Designing a fixed-point multirate filter involves fewer steps than designing a fixed-point
 single-rate filter. The following sections describe each step in the fixed-point
 multirate filter design process and compare the process to the fixed-point single-rate
 filter design process.

- [Quantize Floating-Point Multirate Filter](quantize-floating-point-multirate-filters.html)
- [Analyze Fixed-Point Multirate Filters](analyze-fixed-point-multirate-filters.html)
- [Create Fixed-Point Multirate Filter Models](create-fixed-point-multirate-filter-models.html)
- [Simulate Fixed-Point Multirate Filters](simulate-fixed-point-multirate-filters.html)
- [Generate Code from Fixed-Point Multirate Filters](generating-code-from-fixed-point-multirate-filters.html)

Parent topic:

Design Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-floating-point-filters-digital-filt.html language=enus -->
## TOPIC 00017: Design Floating-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-floating-point-filters-digital-filt.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-floating-point-filters-digital-filt.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to use the interactive Classical Filter Design Express VI to design floating-point filters and also how to analyze and use a designed floating-point filter. You first design a filter that meets the target specifications. You then analyze the resulting filter's characteristi

### Design Floating-Point Filters

This section explains how to use the interactive Classical Filter Design
 Express VI to design floating-point filters and also how to analyze and
 use a designed floating-point filter.

You first design a filter that meets the target specifications. You then analyze the
 resulting filter's characteristics to determine if the filter meets the system's
 requirements. If the filter does not meet the requirements of the system, you can modify
 the specifications and repeat the process. After you design an appropriate filter, you
 can use the filter in the system.

The following figure illustrates the floating-point filter design process:

[IMAGE alt='image' src='GUID-E842D262-768D-4CEB-88FE-0CB1BF4B8E6A-a5.gif']

For a particular design problem, you can use several different techniques and filter
 types to yield an acceptable result. To achieve the best results, you might need to
 experiment with several different approaches.

- [Enter Floating-Point Filter Specifications](enter-floating-point-filter-specifications.html)
- [Analyze Floating-Point Filters](analyze-floating-point-filters-digital-filt.html)
- [Use Floating-Point Filters](using-floating-point-filters-digital-filter-d.html)

Parent topic:

LabVIEW Digital Filter Design Concepts

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-floating-point-multirate-filters-di.html language=enus -->
## TOPIC 00018: Design Floating-Point Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-floating-point-multirate-filters-di.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-floating-point-multirate-filters-di.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The floating-point single-rate filter design process can be followed to design a floating-point multirate filter.The following figure illustrates the typical magnitude response of a lowpass filter in multirate systems: In this figure, f[s] denotes the sampling frequency of the input signal. When des

### Design Floating-Point Multirate
 Filters

The floating-point single-rate filter design process can be followed to design a
 floating-point multirate filter.

The following figure illustrates the typical magnitude response of a lowpass filter in multirate
 systems:

[IMAGE alt='image' src='GUID-F582A47F-0D66-4E20-A6C0-D319EBD7B3F1-a5.gif']

In this figure, f<sub>s</sub> denotes the sampling
 frequency of the input signal. When designing filter specifications, you must take the
 filtering mode into consideration. Because decimation and interpolation are special
 cases of rational resampling, you can use the following filter specifications to design
 any filter with a rational factor of L/M.

| Filter Specification | Value Range |
| --- | --- |
| Passband edge frequency | 0 < f pass < min ( Lf s 2 M , f s 2 ) |
| Stopband edge frequency | f pass < f stop < Lf s M − f pass |

Typically, f<sub>pass</sub> is the highest frequency of
 interest in the input signal. If

f

stop

<

min

(

Lf

s

2

M

,

f

s

2

)

f

stop

min

(

Lf

s

(

2

M

)

,

f

s

2

)

<

f

stop

<

(

Lf

s

2

M

−

f

pass

)

- [Enter Floating-Point Multirate Filters](enter-floating-point-multirate-filter-specs.html)
- [Analyze the Floating-Point Multirate Filter Design](analyze-floatnig-point-multirate-filter-design.html)
- [Use the Floating-Point Multirate Filters](using-floating-point-multirate-filters.html)
- [Quantize Multirate Filter Coefficients](quantize-multirate-filter-coefficients.html)

Parent topic:

Design Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-halfband-filters.html language=enus -->
## TOPIC 00019: Designing Halfband Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-halfband-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-halfband-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Halfband filters are M^th band filters when M = 2.The impulse response of a halfband filter h(n) satisfies the following equation: h ⁢   ( 2 n + k )   = { c n = 0 0 n ≠ 0 where c and k are constants. c usually equals 0.5.The magnitude response of a halfband filter is symmetric with respect to the fr

### Designing Halfband Filters

Halfband filters are M<sup>th</sup> band filters when
 M = 2.

The impulse response of a halfband filter
 h(n) satisfies the following equation:

h

⁢

(

2

n

+

k

)

=

{

c

n

=

0

0

n

≠

0

where c and k are constants.
 c usually equals 0.5.

The magnitude response of a
 halfband filter is symmetric with respect to the frequency
 f<sub>s</sub>/4. The value of the
 magnitude response at f<sub>s</sub>/4 is fixed
 to 0.5. The filter has a linear phase property. Nearly half of the filter
 coefficients in a halfband filter are zeroes, which greatly reduces the computations
 required for filtering. Use the DFD Halfband Design VI to design
 halfband filters.

Parent topic:

Design Nyquist Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-methods-digital-filter-design-toolkit.html language=enus -->
## TOPIC 00020: Design Methods

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-methods-digital-filter-design-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-methods-digital-filter-design-toolkit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: FIR Filter Design Methods The LabVIEW Digital Filter Design Toolkit provides the following FIR filter design methods: Kaiser Window Dolph-Chebyshev Window Equi-Ripple The Kaiser Window method and the Dolph-Chebyshev Window method allows you to get the filter coefficients directly from the analytical

### Design Methods

#### FIR Filter
 Design Methods

The LabVIEW Digital Filter Design Toolkit
 provides the following FIR filter design methods:

- Kaiser Window
- Dolph-Chebyshev Window
- Equi-Ripple

The Kaiser Window method and the Dolph-Chebyshev Window method
 allows you to get the filter coefficients directly from the
 analytical equations, so these methods are easier to use than the
 Equi-Ripple FIR method, which also is known as the Remez design
 method, but the Equi-Ripple FIR method yields optimal filters and
 often produces the best results for most FIR filter design
 problems.

#### IIR Filter
 Design Methods

The LabVIEW Digital Filter Design Toolkit
 provides the following IIR filter design methods:

- Buttersworth
- Chebyshev
- Inverse Chebyshev
- Elliptic

The following figure illustrates the magnitude responses of a typical
 lowpass filter designed by the four IIR filter design methods. Each
 filter has the same numerator and denominator order values:

Figure 5.

[IMAGE alt='image' src='GUID-190CDFD4-AB30-4B0E-8F51-8DEA8D92855F-a5.gif']

The following table summarizes the main features of the four
 IIR-based design methods so you can determine the IIR filter design
 method to use:

| IIR Filter | Ripple in Passband? | Ripple in Stopband? | Transition Bandwidth for a Fixed Order | Order for Given Filter Specifications |
| --- | --- | --- | --- | --- |
| Butterworth | No | No | Widest | Highest |
| Chebyshev | Yes | No | Narrower | Lower |
| Inverse Chebyshev | No | Yes | Narrower | Lower |
| Elliptic | Yes | Yes | Narrowest | Lowest |

Parent topic:

Digital Filter Design Basics

Related concepts:

- Remez Design Method

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-multirate-filters-digital-filter-de.html language=enus -->
## TOPIC 00021: Design Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-multirate-filters-digital-filter-de.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-multirate-filters-digital-filter-de.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about using the LabVIEW Digital Filter Design Toolkit to design multirate filters.

### Design Multirate Filters

This section contains information about using the LabVIEW Digital Filter Design
 Toolkit to design multirate filters.

- [Multirate Filter Basics](multirate-filter-basics-digital-filter-design.html)
- [Design Floating-Point Multirate Filters](design-floating-point-multirate-filters-di.html)
- [Design Fixed-Point Multirate Filters](design-fixed-point-multirate-filters-digit.html)
- [Design Special Multirate Filters](design-special-multirate-filters-digital-f.html)

Parent topic:

LabVIEW Digital Filter Design Concepts

Related concepts:

- LabVIEW Digital Filter Design Concepts

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-raised-cosine-filters.html language=enus -->
## TOPIC 00022: Design Raised Cosine Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-raised-cosine-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-raised-cosine-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Raised cosine filters are a special case of Nyquist filters. As with other Nyquist filters, the coefficients of the raised cosine filter have periodic zero values every M^th sample except for the middle coefficient.The ideal frequency response of a raised cosine filter consists of unity gain at low

### Design Raised Cosine Filters

Raised cosine filters are a special case of Nyquist filters. As with other Nyquist
 filters, the coefficients of the raised cosine filter have periodic zero values
 every M<sup>th</sup> sample except for the middle
 coefficient.

The ideal frequency response of a raised cosine filter consists
 of unity gain at low frequencies, a raised cosine shape in the middle, and zero gain
 at high frequencies. The following equation describes the magnitude response of a
 raised cosine filter:

H

⁢

(

f

)

=

{

1

f

≤

f

c

(

1

−

a

)

1

+

cos

(

π

⁢

(

f

−

f

c

⁢

(

1

−

a

)

)

2

⁢

a

f

c

)

f

c

(

1

−

a

)

≤

f

≤

f

c

(

1

+

a

)

0

f

>

f

c

(

1

+

a

)

where f<sub>c</sub> is the cutoff frequency and
 α is the roll off, which satisfies 0 ≤ α ≤ 1.

In digital communication
 systems, if you want to split the overall raised cosine filtering evenly between the
 transmitter filter and receiver filter, use root-raised cosine filters. The
 following equation describes the magnitude response of a root-raised cosine
 filter:

H

⁢

(

f

)

=

{

1

f

≤

f

c

(

1

−

a

)

1

+

cos

(

π

⁢

(

f

−

f

c

⁢

(

1

−

a

)

)

2

a

f

c

)

2

f

c

(

1

−

a

)

≤

f

≤

f

c

(

1

+

a

)

0

f

>

f

c

(

1

+

a

)

Use the DFD Raised Cosine Design VI to design raised cosine
 filters and root-raised cosine filters.

Parent topic:

Design Nyquist Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-special-filters-digital-filter-desi.html language=enus -->
## TOPIC 00023: Design Special Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-special-filters-digital-filter-desi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-special-filters-digital-filter-desi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about using the LabVIEW Digital Filter Design Toolkit to design special single-rate filters with the Advanced FIR Filter Design VIs, Advanced IIR Filter Design VIs, and the Special Filter Design VIs.

### Design Special Filters

This section contains information about using the LabVIEW Digital Filter Design
 Toolkit to design special single-rate filters with the Advanced FIR
 Filter Design VIs, Advanced IIR Filter
 Design VIs, and the Special Filter
 Design VIs.

- [Linear Phase Filters](linear-phase-filters-digital-filter-design-to.html)
- [Hilbert Transformers](hilbert-transformers-digital-filter-design-to.html)
- [Differentiators](differentiators-digital-filter-design-toolkit.html)
- [Notch and Peak Filters](notch-and-peak-filters-digital-filter-design.html)
- [Comb Filters](comb-filters-digital-filter-design-toolkit.html)
- [Arbitrary Shape Filters](arbitrary-shape-filters-digital-filter-design.html)
- [Group Delay Compensator](group-delay-compensator-digital-filter-design.html)
- [Narrowband FIR Filters](narrowband-fir-filters-digital-filter-design.html)

Parent topic:

LabVIEW Digital Filter Design Concepts

Related concepts:

- LabVIEW Digital Filter Design Concepts

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=design-special-multirate-filters-digital-f.html language=enus -->
## TOPIC 00024: Design Special Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `design-special-multirate-filters-digital-f.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/design-special-multirate-filters-digital-f.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes how to design cascaded integrator comb, Nyquist, and multistage multirate filters.

### Design Special Multirate Filters

This section describes how to design cascaded integrator comb, Nyquist, and multistage
 multirate filters.

- [Cascaded Integrator Comb Filters](cascaded-integrator-comb-filters-digital-filt.html)
- [Design Nyquist Filters](nyquist-filters-di.html)
- [Multistage Multirate Filters](multistage-multirate-filters-digital-filter-d.html)

Parent topic:

Design Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=designing-fixed-point-filters-digital-filter-ov.html language=enus -->
## TOPIC 00025: Design Fixed-Point Filters Overview

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `designing-fixed-point-filters-digital-filter-ov.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/designing-fixed-point-filters-digital-filter-ov.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: To design a fixed-point filter, you first must design a floating-point filter, also known as a reference filter, that meets the target specifications. In some cases, for example, if you need an Infinite Impulse Response (IIR) filter with a narrow transition band but a high stopband attenuation, you

### Design Fixed-Point Filters Overview

To design a fixed-point filter, you first must design a floating-point filter, also known as a
 reference filter, that meets the target specifications. In some cases, for example,
 if you need an Infinite Impulse Response (IIR) filter with a narrow transition band
 but a high stopband attenuation, you need to design a reference filter that exceeds
 the target specifications. The excess margin ensures a smooth conversion from a
 floating-point representation to a fixed-point representation. You then must modify
 the floating-point filter to accommodate the finite-precision constraints of the
 target platform while still trying to meet the target specifications.

Fixed-point signal processing platforms, such as fixed-point Digital Signal Processors (DSPs) and
 Field-Programmable Gate Arrays (FPGAs), are typically more power-efficient and less
 expensive than floating-point alternatives. However, fixed-point systems are
 generally more difficult to design. For example, you must consider the effects of
 coarser quantizations in fixed-point systems.

The following figure illustrates the fixed-point filter design process. The grey boxes
 illustrate the floating-point filter design process, the dotted lines represent optional
 steps, and the arrows on the left indicate to which steps you can return if the filter
 design fails to meet the requirements in the current step.

Figure 7.

[IMAGE alt='image' src='GUID-27C1B32B-E1C6-4436-8118-80F82F497894-a5.gif']

Designing a fixed-point filter from a reference floating-point filter involves the
 following steps:

1. Selecting a filter structure. In floating-point filter
 design, after you select a design method, the LabVIEW Digital Filter Design
 Toolkit uses a default filter structure according to the specified design
 method. However, in fixed-point implementations, different filter structures can
 have different memory and multiplier requirements and might cause different
 finite word length effects. To obtain the best filtering results, you must
 convert the default filter structure to an appropriate structure.
2. Scaling the filter coefficients. Every filter structure
 contains many accumulators, each of which might use a different data range. You
 can scale the filter coefficients by using the DFD Scale
 Filter VI to ensure that all of the accumulators use the same data
 range. Scaling the filter coefficients can help you obtain a better filtering
 result, especially for IIR Cascaded Second-Order Sections Form structures.
3. Quantizing the floating-point filter. Quantization is the process of approximating a
 fixed-point value for each reference floating-point value. You then can use the
 fixed-point values in fixed-point mathematical computation or a hardware implementation.
 By quantizing the coefficients of the reference floating-point filter, you convert a
 floating-point filter to a fixed-point filter.
4. Analyzing the fixed-point filter. To determine how the characteristics of the realized
 fixed-point filter deviate from the characteristics of the reference floating-point
 filter, you must analyze the fixed-point filter.
5. Creating a fixed-point filter model. To create the fixed-point filter model, you must
 configure the quantizers for the input and output signals and specify the settings for
 internal computation.
6. Simulating the fixed-point filter. Before applying the fixed-point filter model in
 real-world applications, you must simulate the behavior of the filter to verify if the
 fixed-point filter model works as you require in a simulation. If the fixed-point filter
 does not provide the required performance in the simulation, you can change the
 implementation structure, modify quantization settings, or redefine the filter
 specifications for the reference floating-point filter.
7. Generating code from the fixed-point filter. You can export filter coefficients and
 automatically generate integer LabVIEW code, LabVIEW FPGA code, and C code from the
 fixed-point filter for designated hardware targets.

#### Finite Word Length Effects

- Degraded Signal-to-Noise Ratio (SNR) due to the reduced precision of internal registers, adders,
 subtracters, and multipliers.
- Distorted frequency response from a limited word length representation of filter
 coefficients.
- Overflowed or clipped signal information due to insufficient headroom in the signal paths.
- Zero-input limit cycles of Infinite Impulse Response (IIR) filters due to nonlinear quantizers
 in the feedback loop of IIR filters or to the overflow of the summation
 operations.

Parent topic:

Design Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=designing-fixed-point-filters-digital-filter.html language=enus -->
## TOPIC 00026: Design Fixed-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `designing-fixed-point-filters-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/designing-fixed-point-filters-digital-filter.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: This section explains how you use the Fixed-Point Tools VIs to implement a fixed-point digital filter from a floating-point reference filter that you designed.

### Design Fixed-Point Filters

This section explains how you use the Fixed-Point Tools VIs to
 implement a fixed-point digital filter from a floating-point reference filter that
 you designed.

- [Design Fixed-Point Filters Overview](designing-fixed-point-filters-digital-filter-ov.html)
- [Select a Filter Structure](select-a-filter-structure-digital-filter-d.html)
- [Scale the Filter Coefficients](scale-the-filter-coefficients-digital-filte.html)
- [Quantize Floating-Point Filters](quantizing-floating-point-filters-digital-fil.html)
- [Analyze Fixed-Point Filters](analyze-fixed-point-filters-digital-filter.html)
- [Create Fixed-Point Filter Models](creating-fixed-point-filter-models-digital-fi.html)
- [Simulate Fixed-Point Filters](simulating-fixed-point-filters-digital-filter.html)
- [Generate Code from Fixed-Point Filters](generate-code-from-fixed-point-filters-digi.html)

Parent topic:

LabVIEW Digital Filter Design Concepts

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=differentiators-digital-filter-design-toolkit.html language=enus -->
## TOPIC 00027: Differentiators

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `differentiators-digital-filter-design-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/differentiators-digital-filter-design-toolkit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the DFD Remez Design VI to design a differentiator by setting the filter type input to Differentiator.The ideal frequency response of a differentiator is as follows:H⁢(f)=jfwhere f is the normalized frequency with the range [0, 0.5]. The frequency response has a constant 90° phase shift at all f

### Differentiators

Use the DFD Remez Design VI to design a differentiator by
 setting the filter type input to
 Differentiator.

The ideal frequency response of a differentiator is as follows:

H

⁢

(

f

)

=

j

f

where f is the normalized frequency with the range [0, 0.5]. The
 frequency response has a constant 90° phase shift at all frequencies.

If you compare this equation with Equation B in the Linear Phase Filters topic, you can
 see that an ideal differentiator has a linear phase and is a Type III or Type IV linear
 phase FIR filter.

Because the passband magnitude response of a differentiator is sloped, a smaller approximation
 error at frequencies where the frequency response has a smaller absolute
 gain is useful. The DFD Remez Design VI uses an in-band
 weighting function inversely proportional to the frequency to achieve a
 constant amplitude percentage ripple size. The following sections describe
 how to create Type IV and Type III differentiators.

#### Designing Type IV
 Differentiators

If you need the frequency range from DC to
 the Nyquist frequency to have a differentiator response, you can
 design a Type IV differentiator. A Type III differentiator cannot
 maintain a strict differentiator response near the Nyquist frequency
 because the magnitude response of the Type III differentiator is
 constrained to zero at the Nyquist frequency.

When you design
 a Type IV differentiator using the DFD Remez
 Design VI, you can specify a single band that
 constrains two points with equal weights. For example, consider a
 frequency range of [0, 0.5] with an amplitude range of [0, 1]. To
 design a Type IV differentiator using this band, enter the
 specifications shown in the following figure into the
 DFD Remez Design VI:

[IMAGE alt='image' src='GUID-31EB601F-84F6-4478-B6C8-749E2782CBDF-a5.gif']

In the previous figure, the odd order number 19 determines that the
 resulting differentiator is a Type IV differentiator. The following
 figure shows the magnitude response of the resulting Type IV
 differentiator:

[IMAGE alt='image' src='GUID-027BE1A0-D457-48D9-A6D5-A2884CA21A5D-a5.gif']

In the previous figure, you can see that the magnitude response of
 the designed filter is sloped and the ripple size is
 small.

#### Designing Type III
 Differentiators

If you need to use a differentiator in
 combination with a lowpass filter, use a Type III differentiator.
 Type III differentiators have a differentiator response in a lowpass
 passband, and they have a stopband that extends to the Nyquist
 frequency. For example, you can create a Type III differentiator
 that covers a frequency range of [0, 0.45] with an amplitude range
 of [0, 0.9]. The following figure shows a single-band specification
 without the target response at 0.5 Hz specified:

[IMAGE alt='image' src='GUID-0A3DF90C-50F7-4C99-8C81-2A316BFB836B-a5.gif']

The following figure shows the magnitude response of the resulting
 Type III differentiator:

[IMAGE alt='image' src='GUID-3C5810E6-524C-4A0E-9A80-1F96744C991E-a5.gif']

In the previous figure, the even order number 20 determines that
 the resulting differentiator is a Type III differentiator. You can
 see that the magnitude response of the designed filter becomes zero
 at 0.5 Hz and the ripple size is larger than that of the Type IV
 differentiator. To achieve the same ripple size, you need to specify
 a larger value for the order
 input.

Parent topic:

Design Special Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=digital-filter-applications-digital-filter-de.html language=enus -->
## TOPIC 00028: Digital Filter Applications

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `digital-filter-applications-digital-filter-de.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/digital-filter-applications-digital-filter-de.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Filters are signal processing elements that alter the frequency spectrum of an input signal.Use the filters for the following applications:Attenuating noise in a signal where the noise power and signal power are concentrated at different frequencies. For example, you might use a notch filter to atte

### Digital Filter Applications

Filters are signal processing elements that alter the frequency spectrum of an
 input signal.

Use the filters for the following applications:

- Attenuating noise in a signal where the noise power and signal power are concentrated at different frequencies. For example, you might use a notch filter to attenuate a 60 Hz powerline interference present in a signal.
- Extracting signal components from a signal that contains different signal components concentrated at different frequencies. For example, you might use a bandpass filter to extract a particular radio station signal from a broadband radio signal.
- Reshaping the frequency spectrum of the input signal. For example, you might use an A-weighting filter to approximate the frequency response of a human ear. As another example, you might use an equalizer filter to undo magnitude and phase distortion caused by passing a signal through a linear time-invariant communications channel.

You can use either fixed-point or floating-point arithmetic to implement digital signal processing systems. Although floating-point implementations are typically easier to design, fixed-point implementations are often less expensive and more efficient in power than floating-point implementations. Floating-point designs are typically appropriate in applications that run on desktop computers, and fixed-point designs are often more appropriate in embedded applications, in which you need to minimize cost or power consumption.

Parent topic:

Digital Filter Design Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=digital-filter-design-basics-digital-filter-d.html language=enus -->
## TOPIC 00029: Digital Filter Design Basics

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `digital-filter-design-basics-digital-filter-d.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/digital-filter-design-basics-digital-filter-d.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before using the LabVIEW Digital Filter Design Toolkit to design a digital filter, you need to get an overview of the general design process and application areas of digital filters.When you design a digital filter, you begin by creating specifications that define the characteristics you want in the

### Digital Filter Design Basics

Before using the LabVIEW Digital Filter Design Toolkit to design a digital filter, you
 need to get an overview of the general design process and application areas of digital
 filters.

When you design a digital filter, you begin by creating specifications that define the
 characteristics you want in the digital filter. You can design both FIR and IIR filters
 with specific filter attributes, and you can customize the sampling frequency, filter
 specifications, and design method. After you design a digital filter, you need to
 analyze the characteristics of the digital filter by evaluating the magnitude and
 impulse responses, phase responses and group delays, or poles and zeroes. The Digital
 Filter Design Toolkit provides the Filter Analysis VIs to help you
 evaluate the characteristics of a filter.

- [Digital Filter Design Process Overview](digital-filter-design-process-overview-digita.html)
- [Filter Attributes](filter-attributes-digital-filter-design-toolk.html)
- [FIR and IIR Filters](fir-and-iir-filters-digital-filter-design-too.html)
- [Filter Specifications](filter-specifications-digital-filter-design-t.html)
- [Design Methods](design-methods-digital-filter-design-toolkit.html)
- [Group Delay and Phase Delay](group-delay-and-phase-delay-digital-filter-de.html)
- [Poles, Zeroes, and Pole-Zero Plots](poles-zeroes-and-pole-zero-plots-digital-filt.html)
- [Digital Filter Applications](digital-filter-applications-digital-filter-de.html)

Parent topic:

LabVIEW Digital Filter Design Concepts

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=digital-filter-design-process-overview-digita.html language=enus -->
## TOPIC 00030: Digital Filter Design Process Overview

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `digital-filter-design-process-overview-digita.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/digital-filter-design-process-overview-digita.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filter design process is iterative. You usually experiment with different design specifications or design methods to get the appropriate digital filter for an application.Sometimes you might need to revise the specifications or modify the design method after you simulate the filter, especially w

### Digital Filter Design Process Overview

The filter design process is iterative. You usually experiment with different design
 specifications or design methods to get the appropriate digital filter for an
 application.

Sometimes you might need to revise the specifications or modify the design method after
 you simulate the filter, especially when designing fixed-point filters.

Digital filter design involves the following three steps:

1. Specifying the design method and target digital filter attributes, or the characteristics you want the digital filter to possess.
2. Analyzing the characteristics of the floating-point digital filter you designed in Step 1.
3. Implementing the filter on fixed-point targets with finite-precision arithmetic.

Parent topic:

Digital Filter Design Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=distortions-digital-filter-design-toolkit.html language=enus -->
## TOPIC 00031: Distortions

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `distortions-digital-filter-design-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/distortions-digital-filter-design-toolkit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are three fundamental distortions in filter banks: aliasing, magnitude distortion, and phase distortion.AliasingThe following figure shows a 2-band uniform filter bank with no processing unit applied. 33 2-Band Uniform Filter Bank In practice, the magnitude responses of the lowpass band analys

### Distortions

There are three fundamental distortions in filter banks: aliasing, magnitude distortion,
 and phase distortion.

#### Aliasing

The following
 figure shows a 2-band uniform filter bank with no processing unit applied.

Figure 33.

[IMAGE alt='image' src='GUID-7BFF1DD1-FE72-4102-8E7D-7CC0198B75C7-a5.gif']

In practice, the magnitude responses of the lowpass band analysis filter,
 H<sub>0</sub>(e<sup>jω</sup>),
 and the highpass band analysis filter,
 H<sub>1</sub>(e<sup>jω</sup>),
 overlap with each other, as shown in the following figure:

Figure 34.

[IMAGE alt='image' src='GUID-B98DF34B-783D-48DD-BA1C-13E93F06B58B-a5.gif']

The following figure shows the spectrum
 X(e<sup>jω</sup>)
 of the input signal x[n]:

Figure 35.

jω

[IMAGE alt='image' src='GUID-CD6EE5D8-CC57-47C0-992E-D573CEDC6251-a5.gif']

The lowpass band analysis filter,
 H<sub>0</sub>(z), filters the input signal
 to give the lowpass band signal
 x<sub>0</sub>[n]. The spectrum of the
 lowpass band signal,
 X<sub>0</sub>(e<sup>jω</sup>),
 is shown in the following figure:

Figure 36.

0

jω

[IMAGE alt='image' src='GUID-D099D4DB-4A67-4634-B3AD-80DFC5C43BAB-a5.gif']

The filter bank
 *decimates* x<sub>0</sub>[n] by
 a factor of 2 to give the decimated lowpass band signal
 v<sub>0</sub>[n]. After decimation, the
 spectrum is given by
 V<sub>0</sub>(e<sup>jω</sup>)
 =
 0.5X<sub>0</sub>(e<sup>jω</sup><sup>/2</sup>)
 +
 0.5X<sub>0</sub>(–e<sup>jω</sup><sup>/2</sup>).
 The component
 0.5X<sub>0</sub>(–e<sup>jω</sup><sup>/2</sup>)
 overlaps with the component
 0.5X<sub>0</sub>(e<sup>jω</sup><sup>/2</sup>),
 which leads to aliasing in the filter bank, shown as the overlapping area in the
 following figure:

[IMAGE alt='image' src='GUID-2CEA69EB-DA87-4445-BBAE-D7F236683ACE-a5.gif']

The filter bank then
 *interpolates* v<sub>0</sub>[n]
 by a factor of 2. The lowpass band synthesis filter,
 F<sub>0</sub>(z), filters the signal and
 returns the lowpass band output signal
 y<sub>0</sub>[n]. The following figure
 shows the spectrum of the lowpass band output signal,
 Y<sub>0</sub>(e<sup>jω</sup>):

[IMAGE alt='image' src='GUID-A36E77AC-E76C-4768-9306-0318A8AC10BC-a5.gif']

In the previous figure, the shaded area is the aliasing component in the lowpass
 band output signal. Similarly, the following figure shows the spectrum of the
 highpass band output signal
 Y<sub>1</sub>(e<sup>jω</sup>).
 The shaded area is the aliasing component in the highpass band output signal.

Figure 37.

1

jω

[IMAGE alt='image' src='GUID-9FF2EA3B-03F2-4F96-B23D-FE8BD753A817-a5.gif']

You cannot avoid aliasing in the analysis bank if the magnitude response of the
 lowpass band analysis filter and the highpass band analysis filter overlap with each
 other. However, you can cancel the aliasing by choosing the correct synthesis
 filters. The Filter Bank Design VIs automatically choose the
 correct synthesis filters to cancel aliasing in the analysis bank.

#### Magnitude Distortion and Phase
 Distortion

Disregarding the aliasing effect, assuming the equivalent
 frequency response of the filter bank is
 T(e<sup>jω</sup>) =
 |T(e<sup>jω</sup>)|e<sup>jΦ(ω)</sup>,
 then Y(e<sup>jω</sup>) =
 X(e<sup>jω</sup>)T(e<sup>jω</sup>)
 . If |T(e<sup>jω</sup>)| is
 not flat, the filter bank has a magnitude distortion. The following figure shows the
 magnitude distortion in a Near-Perfect Reconstruction (NPR) filter bank:

[IMAGE alt='image' src='GUID-BCAEE776-2BFE-4906-A8A3-3389F86599A2-a5.gif']

If T(e<sup>jω</sup>)
 does not have a linear phase, the filter bank has a phase distortion. The filter
 banks used in the LabVIEW Digital Filter Design Toolkit contain no phase
 distortion.

Parent topic:

Filter Bank Design Basics

Related concepts:

- Decimation
- Interpolation

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=enter-filter-bank-specifications-digital-f.html language=enus -->
## TOPIC 00032: Enter Filter Bank Specifications

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `enter-filter-bank-specifications-digital-f.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/enter-filter-bank-specifications-digital-f.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Filter Bank Design Express VI to configure a filter bank interactively.After you add the Express VI to the block diagram, the Configure DFD Filter Bank Design dialog box appears, as shown in the following figure: From the configuration dialog box, you can select the filter bank type and phas

### Enter Filter Bank Specifications

Use the Filter Bank Design Express VI to configure a filter bank
 interactively.

After you add the Express VI to the block diagram, the Configure
 DFD Filter Bank Design dialog box appears, as shown in the following
 figure:

[IMAGE alt='image' src='GUID-7D03D4D4-FD34-4DE0-90AC-2EF4AF615C99-a5.gif']

From the configuration dialog box, you can select the filter bank type and phase option from the pull-down menus and then enter the filter bank specifications through the numeric controls. You can analyze the filter bank distortions and the frequency responses at the top of the configuration dialog box.

#### Considerations fo Filter Bank
 Specifications

When you define a filter bank specification, take into
 consideration the filter bank specifications, the roll-off, and the specified
 stopband attenuation.

- With the same filter bank specifications, Near-Perfect Reconstruction (NPR) cosine-modulated
 filter banks offer better frequency selectivity than Perfect Reconstruction (PR)
 cosine-modulated filter banks, as illustrated in the following figure: [IMAGE alt='image' src='GUID-F63EBFA5-B756-4234-A1FB-88704F3608D3-a5.gif']
- The actual roll-off has a slight difference from the specified roll-off, which
 specifies the relative transition bandwidth.
- If the specified stopband attenuation is too high, the actual stopband
 attenuation may not meet the specified stopband attenuation.

#### Analyzing the Filter Bank
 Design

The top of the Configure DFD Filter Bank
 Design dialog box displays the frequency response and distortion
 analysis of the filter bank. In the Distortion Analysis
 section, you can examine the aliasing, magnitude distortion, and phase distortion in
 the filter bank. In the Frequency Responses section, you can
 analyze the frequency selectivity by examining the frequency responses of the
 analysis bank. You can examine the magnitude response and phase response of the
 analysis bank or a specified analysis filter.

Remove the checkmark from the
 Magnitude in dB checkbox to use a linear scale, or keep
 the checkmark in the Magnitude in dB checkbox to use a
 logarithmic scale. Place a checkmark in the Unwrap Phase
 checkbox to unwrap the phase so it is not limited to [0, 2π).

#### Using Filter
 Banks

After you design a filter bank, you can use the Filter Bank
 Processing VIs to process a signal. You can use the decomposition VIs to decompose
 an input signal into several subband signals and use the reconstruction VIs to
 reconstruct a signal from subband signals.

Each polymorphic VI can process two
 kinds of signal:

- An array of DBLs
- A waveform

Use the DFD 2-Band Filter Bank Decomposition VI or the
 DFD M-Band Filter Bank Decomposition VI to decompose the
 signal into two or more uniformly spaced subband signals. Use the DFD
 2-Band Filter Bank Reconstruction VI or the DFD M-Band Filter
 Bank Reconstruction VI to reconstruct a signal from two or more
 uniformly spaced subband signals. These VIs automatically retain the internal states
 of the filter bank between continuous input blocks.

Parent topic:

Designing Filter Banks

Related concepts:

- Filter Bank Design Basics
- Distortions

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=enter-floating-point-filter-specifications.html language=enus -->
## TOPIC 00033: Enter Floating-Point Filter Specifications

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `enter-floating-point-filter-specifications.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/enter-floating-point-filter-specifications.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Classical Filter Design Express VI to configure a classical digital filter interactively.After you add the Express VI to the block diagram, the Configure Classical Filter Design dialog box appears, as shown in the following figure: From the configuration dialog box, you can select th

### Enter Floating-Point Filter
 Specifications

You can use the Classical Filter Design Express VI to configure a
 classical digital filter interactively.

After you add the Express VI to the block diagram, the Configure
 Classical Filter Design dialog box appears, as shown in the following
 figure:

[IMAGE alt='image' src='GUID-0E392C3B-91B8-4729-BED1-876B7A251200-a5.gif']

From the configuration dialog box, you can select the filter type and design method from the pull-down menus and then enter the filter specifications through either the numeric controls on the left side of the configuration dialog box or the graphical interface on the right side of the configuration dialog box. The results are equivalent.

#### Using the Numerical
 Controls

Classical digital filter specifications include frequency ranges
 and ripple constraints. You can specify the maximum allowable deviation
 δ<sub>p</sub> from unity gain in the
 passband in the Passband ripple numeric control. You can
 specify the maximum allowable deviation
 δ<sub>s</sub> from the zero gain in
 the stopband in the Stopband attenuation numeric
 control.

You can specify deviations in either a logarithmic or a linear scale.
 The Classical Filter Design Express VI uses a logarithmic scale
 by default. To use a linear scale, remove the checkmark from the
 Magnitude in dB checkbox in the configuration dialog
 box.

The following equations show the relationship between the logarithmic and
 linear scales:

Passband

ripple

=

−

20

log

⁡

10

(

1

−

δ

p

)

Stopband

ripple

=

−

20

log

⁡

10

(

δ

s

)

Based on the two equations above, you can convert the passband
 ripple to or from the decibel representation. For example, if passband ripple equals
 0.01 dB, that is, 0.01
 ⁢
 
 =
 
 −
 20
 log
 ⁡
 10
 (
 1
 −
 δ
 p
 ) then δ
 p
 ⁢
 
 =
 
 0.00115 Similarly, if stopband ripple equals 60 dB, that is 60
 ⁢
 =
 
 −
 20
 log
 ⁡
 10
 (
 δ
 s
 ) then δ
 s
 ⁢
 
 =
 
 0.001.

#### Using the Graphical
 Interface

The right side of the Configure Classical Filter
 Design dialog box displays the magnitude response of the designed
 digital filter. The magnitude axis can be either a linear or a logarithmic scale.
 Remove the checkmark from the Magnitude in dB checkbox to use
 a linear scale, or keep the checkmark in the Magnitude in dB
 checkbox to use a logarithmic scale. The frequency axis, in hertz, covers the range
 from 0 to half the sampling frequency, which is the Nyquist frequency.

The
 Magnitude Response graph contains a set of cursors that
 you can use to specify the passband and stopband. Use the passband cursor to change
 the passband. Under the linear scale, the distance between unity and the horizontal
 passband cursor specifies the maximum passband ripple. The location of the vertical
 passband cursor indicates the passband edge frequency. The stopband cursors function
 the same when defining the specifications of the stopband. The distance between the
 horizontal passband cursor and the horizontal stopband cursor specifies the stopband
 attenuation.

#### Guidelines for Entering Filter
 Specifications

As you define a filter specification, you must adhere to a
 set of rules to maintain valid specifications. If you do not adhere to the following
 rules, the Error message indicator of the
 Configure Classical Filter Design dialog box displays a
 message with suggestions for repositioning the cursors.

- Keep horizontal cursors in the range (0, 1) in a linear scale or
 (−inf, 0 dB) in a logarithmic scale.
- Keep the horizontal passband cursor above the horizontal stopband cursor.

#### Selecting the Design
 Method

After you enter the target digital filter specifications into the
 numeric controls or graphical interface, select a design method.

When you
 design a digital filter with the Classical Filter Design Express
 VI, the design method and the filter specifications that you specify control the
 shape of the frequency response. You cannot alter the phase response, even though
 the phase response for filters generated with the FIR methods in this VI are linear
 phase. If you want to specify the magnitude response and phase response, use the
 Advanced FIR Filter Design VIs, the Advanced IIR
 Filter Design VIs, or the Special Filter Design
 VIs.

Parent topic:

Design Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=enter-floating-point-multirate-filter-specs.html language=enus -->
## TOPIC 00034: Enter Floating-Point Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `enter-floating-point-multirate-filter-specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/enter-floating-point-multirate-filter-specs.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filter type and design method can be selected from the pull-down menus in the Configure Multirate Filter Design dialog box where the filter factor can also be specified. The filter specifications can be entered through either the numeric controls on the right side of the tab or the magnitude res

### Enter Floating-Point Multirate Filters

The filter type and design method can be selected from the pull-down menus in the
 Configure Multirate Filter Design dialog box where the filter
 factor can also be specified. The filter specifications can be entered through either
 the numeric controls on the right side of the tab or the magnitude response graphical
 interface in the configuration dialog box. The results are equivalent.

After you add the Multirate FIR Design Express VI to the block
 diagram, the Configure Multirate Filter Design dialog box
 appears, as shown in the following figure:

[IMAGE alt='image' src='GUID-4E69C9E6-13D1-4937-B4DA-451D1A70ED94-a5.gif']

#### Using the Numerical Controls

Similar to the numerical controls for single-rate filter design, the numerical
 controls for multirate filter design also contain frequency ranges and ripple
 constraint settings. In addition to these settings, you also need to specify the
 sampling frequency of the input signal in the Input sampling
 frequency numeric control. This VI then automatically calculates the
 sampling frequency of the output signal based on the filter specifications you
 entered.

#### Using the Graphical Interface

The Magnitude Response graph displays the magnitude response
 of the designed multirate filter. The magnitude axis can be either a linear or a
 logarithmic scale. Remove the checkmark from the Magnitude in
 dB checkbox to use a linear scale, or keep the checkmark in the
 Magnitude in dB checkbox to use a logarithmic
 scale.

The Magnitude Response graph contains a set of
 cursors that you can use to specify the passband and stopband. Use the passband and
 stopband cursors to change the passband and stopband, respectively, of the multirate
 filter. Under the linear scale, the distance between unity and the horizontal
 passband cursor specifies the maximum passband ripple. The location of the vertical
 passband cursor indicates the passband edge frequency. The stopband cursors work the
 same when defining the specifications of the stopband. Under the logarithmic scale,
 the distance between 0 dB and the horizontal stopband cursor specifies the stopband
 attenuation.

#### Guidelines for Entering Filter
 Specifications

As you define a filter specification, you must adhere to a set of rules to maintain
 valid specifications. If you do not adhere to the following rules, the
 Configure Multirate Filter Design dialog box displays a
 message in the Tips indicator with suggestions for
 repositioning the cursors.

- Keep the horizontal cursors in the range (0, 1) in a linear scale or (−inf, 0
 dB) in a logarithmic scale.
- Keep the horizontal passband cursor above the horizontal stopband cursor.
- The Passband edge frequency value must be less than the
 Nyquist frequency, or you must keep the vertical passband cursor to the left of
 the Nyquist cursor.
- The Stopband edge frequency value must be greater than
 the Passband edge frequency value, or you must keep the
 vertical passband cursor to the left of the stopband cursor.
- If you remove the checkmark from the Transition band aliasing
 allowed checkbox to avoid aliasing in the transition band, keep
 the Stopband edge frequency value between the
 Passband edge frequency value and the Nyquist
 frequency, or keep the vertical stopband cursor between the vertical passband
 and Nyquist cursors. If you keep the checkmark in the Transition band
 aliasing allowed checkbox to allow aliasing in the transition
 band, keep the vertical stopband cursor between the vertical passband cursor and
 the vertical stopband limit cursor.

After you finish entering the filter specifications, click the Update
 Design button to apply the new specifications.

Parent topic:

Design Floating-Point Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=exact-gain-control-design-digital-filter-desi.html language=enus -->
## TOPIC 00035: Exact Gain Control Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `exact-gain-control-design-digital-filter-desi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/exact-gain-control-design-digital-filter-desi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use exact gain control to constrain the amplitude response of the filter to particular values at particular frequencies.When you enter bands into the band specs input, the DFD Remez Design VI uses complex or magnitude approximation to create the design of the filter.To use exact gain control

### Exact Gain Control Design

You can use exact gain control to constrain the amplitude response of the filter to
 particular values at particular frequencies.

When you enter bands into the band specs input, the DFD Remez
 Design VI uses complex or magnitude approximation to create the design of
 the filter.

To use exact gain control in the DFD Remez Design VI, enter in the
 freqs of exact gain input a list of frequencies that you want
 to constrain to ideal amplitudes. If you also specify those frequencies in the
 band specs input, the DFD Remez Design VI
 uses the corresponding amplitudes. If you do not enter those frequencies in the
 band specs input, the DFD Remez Design VI
 interpolates the amplitudes linearly.

Consider a filter that has the same magnitude response as the filter in the *Single-Point
 Band Design* section. You can achieve sharper notches by applying exact gain
 control at 0.15 Hz and 0.35 Hz. By entering those single-point band frequency points in
 the freqs of exact gain input, the redesigned notch filter has a
 magnitude response as shown in the following figure:

Figure 40.

[IMAGE alt='image' src='GUID-E500CA63-3E81-4DBF-841C-EFD6B94ED3BD-a5.gif']

Notice that the graph has sharper notches than the notch filter in the *Single-Point Band
 Design* section.

The following figure shows the magnitude response of a 12<sup>th</sup> order lowpass equi-ripple
 filter without any exact gain frequencies. The passband range is [0, 0.25] and the
 stopband range is [0.3, 0.5] with equal weights in both bands. Notice that the gain at
 DC, or the magnitude response at 0 Hz, is not exactly one.

Figure 41.

th

[IMAGE alt='image' src='GUID-FE5D5095-04AE-4545-8F16-9FE28DB2CE75-a5.gif']

If you want to force the gain to one at DC, enter 0 into the freqs of
 exact gain input and run the VI again. The following figure shows the
 magnitude response of the resulting filter:

Figure 42.

12

[IMAGE alt='image' src='GUID-7369F734-A910-4E00-9849-A0B4E2B50BD3-a5.gif']

Notice that the DC gain becomes exactly one without any noticeable ripple size increase.

The following figure shows the magnitude response of a 12<sup>th</sup> order highpass filter with
 a stopband frequency range of [0, 0.2] and a passband frequency range of [0.3, 0.5]:

Figure 43.

th

[IMAGE alt='image' src='GUID-C4C89CEE-1A48-4267-8FCA-1AAD881D7DE5-a5.gif']

The signal is relatively clean except for a noise component at 0.1 Hz and the second harmonic at
 0.2 Hz. To attenuate the noise power at those frequencies, you can enter
 0.1 and 0.2 into the freqs of exact
 gain input.

The following figure shows the magnitude response of the filter with exact gains specified at 0.1
 Hz and 0.2 Hz. Notice that the magnitude response at 0.1 Hz and 0.2 Hz is exactly
 zero.

Figure 44.

[IMAGE alt='image' src='GUID-0D0D6029-B608-4C56-A0A6-9535C71E1D34-a5.gif']

Parent topic:

Remez Design Method

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=export-fixed-point-integer-coefficients-di.html language=enus -->
## TOPIC 00036: Export Fixed-Point Integer Coefficients

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `export-fixed-point-integer-coefficients-di.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/export-fixed-point-integer-coefficients-di.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you have a filter execution engine for which you need only filter coefficients, you can export the fixed-point filter coefficients to a text file using the DFD Save to Text File VI.You can save the coefficients to a text file and download them to the execution target. The text file contains a s

### Export Fixed-Point Integer
 Coefficients

When you have a filter execution engine for which you need only filter coefficients, you
 can export the fixed-point filter coefficients to a text file using the DFD
 Save to Text File VI.

You can save the coefficients to a text file and download them to the execution target. The text
 file contains a section that provides all information about the fixed-point integer
 coefficients and corresponding quantizers.

Parent topic:

Generate Code from Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=filter-attributes-digital-filter-design-toolk.html language=enus -->
## TOPIC 00037: Filter Attributes

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `filter-attributes-digital-filter-design-toolk.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/filter-attributes-digital-filter-design-toolk.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filters available in the LabVIEW Digital Filter Design Toolkit can have the following attributes: digital, linear, time-invariant, or causal.The filters that you design using the LabVIEW Digital Filter Design Toolkit have the following attributes: Digital The expected filter input signal is a se

### Filter Attributes

The filters available in the LabVIEW Digital Filter Design Toolkit can have the
 following attributes: digital, linear, time-invariant, or causal.

The filters that you design using the LabVIEW Digital Filter Design Toolkit have the following
 attributes:

Digital

Linear

Time-invariant

Causal

Parent topic:

Digital Filter Design Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=filter-bank-design-basics-digital-filter-desi.html language=enus -->
## TOPIC 00038: Filter Bank Design Basics

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `filter-bank-design-basics-digital-filter-desi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/filter-bank-design-basics-digital-filter-desi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In modern signal processing, many applications use filter banks to decompose a signal into several narrower frequency ranges, which are convenient for further processing.For example, adaptive filter applications use filter banks to reduce computational complexity and improve the convergence performa

### Filter Bank Design Basics

In modern signal processing, many applications use filter banks to decompose a signal
 into several narrower frequency ranges, which are convenient for further processing.

For example, adaptive filter applications use filter banks to reduce computational complexity and
 improve the convergence performance by decomposing a high-order adaptive filter into
 several low-order adaptive filters. Audio processing applications use filter banks for
 room simulation and digital audio compression. Digital communications applications use
 filter banks in digital transmultiplexers, channel equalization precoding, and discrete
 multitone modulation. Before using filter banks, you must have some basic knowledge of
 multirate filters.

#### Filter Bank Structure

A
 filter bank has two parts: an analysis bank and a synthesis bank. Each bank is a set
 of bandpass filters. The filters in the analysis bank are analysis filters and the
 filters in the synthesis bank are synthesis filters. The following figure shows the
 structure of a filter bank:

[IMAGE alt='image' src='GUID-0BCF9289-C5DA-4C6D-A854-49104EF28406-a5.gif']

The analysis bank consists of M analysis filters
 H<sub>k</sub>(z), where
 k represents the kth subband. Uniform
 filter banks in the LabVIEW Digital Filter Design Toolkit have the property that the
 number of subbands, M, is equal to the decimation factor of the
 subband filters. The analysis filters,
 H<sub>k</sub>(z), decompose the input
 signal, x[n], into multiple subband signals,
 V<sub>k</sub>[n]. Each subband signal
 carries a specific frequency range of the input signal. The synthesis filters,
 F<sub>k</sub>(z), reconstruct the original
 signal, y[n], from the processed subband
 signals, W<sub>k</sub>[n].

When designing filter banks, it is important to consider the signal reconstruction
 and frequency selectivity.

#### Perfect or Near-Perfect
 Reconstruction

If you do not apply a processing unit to the subband
 signals, the synthesis bank reconstructs the original signal, perfectly or
 near-perfectly. You can evaluate the signal reconstruction by examining distortions
 in the filter bank. There are three fundamental distortions in filter banks:
 aliasing, magnitude distortion, and phase distortion. If a filter bank is free from
 these distortions, the filter bank is a Perfect Reconstruction (PR) filter bank. If
 these distortions are small, the filter bank is a Near-Perfect Reconstruction (NPR)
 filter bank. If a filter bank has perfect reconstruction, the output signal is a
 scaled and delayed version of the input signal.

#### Frequency Selectivity

Frequency selectivity indicates the ability of a filter bank to separate frequency
 subbands. Each subband contains signal components in a different frequency range.
 You can evaluate the frequency selectivity by examining the stopband attenuation and
 the transition bands. To achieve good frequency selectivity, the filter bank must
 have a high stopband attenuation and narrow transition bands.

It is often
 difficult to design PR filter banks that achieve good frequency selectivity.
 However, NPR filter banks can achieve high stopband attenuation and narrow
 transition bands while introducing only small distortions. Thus, in practice, NPR
 filter banks often have better frequency selectivity than PR filter banks.
 Consequently, many real-world applications use NPR filter banks instead of PR filter
 banks.

Parent topic:

Designing Filter Banks

Related concepts:

- Design Multirate Filters
- Filter Specifications

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=filter-bank-design-process-digital-filter-des.html language=enus -->
## TOPIC 00039: Filter Bank Design Process

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `filter-bank-design-process-digital-filter-des.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/filter-bank-design-process-digital-filter-des.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After your initial design, assess if the target specifications are met, modify if needed, then implement the finalized filter bank in your system.The following figure illustrates the filter bank design process. First, design a filter bank that meets the target specifications, then analyze the charac

### Filter Bank Design Process

After your initial design, assess if the target specifications are met, modify if
 needed, then implement the finalized filter bank in your system.

The following figure illustrates the filter bank design process. First, design a filter bank that
 meets the target specifications, then analyze the characteristics of the
 resulting filter bank to determine if the filter bank meets the requirements
 of the system. If the filter bank does not meet the requirements of the
 system, you can modify the specifications and repeat the process. After
 designing an appropriate filter bank, you can use the filter bank in the
 system.

Figure 32.

[IMAGE alt='image' src='GUID-D9142070-3C8B-44B8-8438-CC5DDA4CBCC5-a5.gif']

For a particular design problem, you can use several different techniques and filter bank
 types to yield an acceptable result. To achieve the best results, you might need to
 experiment with several different approaches.

Parent topic:

Designing Filter Banks

Related concepts:

- Enter Filter Bank Specifications

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=filter-coefficients-and-quantizers-digital-fi.html language=enus -->
## TOPIC 00040: Filter Coefficients and Quantizers

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `filter-coefficients-and-quantizers-digital-fi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/filter-coefficients-and-quantizers-digital-fi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Digital Filter Design Toolkit uses quantizers to store different quantization settings for the coefficients and the intermediate operands and results. You must configure all quantizers correctly in a fixed-point filter implementation.In a fixed-point filter implementation, you quantize t

### Filter Coefficients and Quantizers

The LabVIEW Digital Filter Design Toolkit uses quantizers to store different
 quantization settings for the coefficients and the intermediate operands and
 results. You must configure all quantizers correctly in a fixed-point filter
 implementation.

In a fixed-point filter implementation, you quantize the coefficients as well as the intermediate
 operands and results. The following figure shows an example of a fixed-point
 model of quantized coefficients, intermediate operands, and results:

[IMAGE alt='image' src='GUID-087D01E3-149F-46D8-AFB3-C235CEBE0A8D-a5.gif']

This fixed-point model contains the following quantizers:

- Q I is the input quantizer for the input signal of a fixed-point filter.
- Q S is the sum quantizer for the summation of a fixed-point adder.
- Q D is the delay quantizer for the input of a delay element.
- Q M is the multiplicand quantizer for the multiplicand of a fixed-point multiplier, which multiplies a quantized multiplicand by a quantized coefficient.
- Q C is the filter coefficients quantizer for the reference floating-point filter. Depending on the group type of the filter coefficients, Q C can be coefficients a / k or coefficients b / v .
- Q P is the product quantizer for the product of a fixed-point multiplier.
- Q O is the output quantizer for the output signal of a fixed-point filter.

Each quantizer has a different effect on a fixed-point filter response depending on the filter
 structure. You must create a fixed-point filter model and simulate the behavior of the
 filter model through trial and error before you use the corresponding fixed-point
 filter. Although you can determine the effects of coefficient quantization at design
 time, you cannot determine other quantization effects until you filter the expected
 input signals. For example, the actual data might be too large or might lead to limit
 cycles.

When you configure the quantizers, depending on which VI you use, you might need to complete some
 or all of the following items:

- Specify the quantizer source.
- Specify the word length and integer word length.
- Handle overflows and underflows.
- Specify the rounding mode.

Parent topic:

Quantize Floating-Point Filters

Related concepts:

- Simulate Fixed-Point Multirate Filters

Related tasks:

- Create Fixed-Point Filter Models

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=filter-specifications-digital-filter-design-t.html language=enus -->
## TOPIC 00041: Filter Specifications

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `filter-specifications-digital-filter-design-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/filter-specifications-digital-filter-design-t.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For most digital filters, you typically design the digital filter response in the frequency domain. The frequency response specification for the digital filter typically includes the target magnitude response, phase response, and the allowable deviation for each.The following figure illustrates the

### Filter Specifications

For most digital filters, you typically design the digital filter response in the
 frequency domain. The frequency response specification for the digital
 filter typically includes the target magnitude response, phase response, and
 the allowable deviation for each.

The following figure illustrates the magnitude frequency response of a lowpass filter, which
 allows low frequencies to pass and attenuates high frequencies:

Figure 1.

[IMAGE alt='image' src='GUID-D8A244C3-3066-44BF-8FED-19599A94511A-a5.gif']

The frequency range from the passband edge frequency to the stopband edge frequency is the
 transition band, which has a frequency response that is unspecified. The filter passband
 and stopband can contain oscillations, which are known as ripples. A typical example of
 a ripple appears in the circle of the previous figure.
 δ<sub>p</sub> indicates the magnitude of
 the passband ripple, which equals the maximum deviation from the unity.
 δ<sub>s</sub> indicates the magnitude response
 of the stopband ripple, which equals the maximum deviation from zero.

Notice the transition band between the passband and stopband frequencies. In an ideal design, a digital filter has a target gain in the passband and a zero gain (−∞ dB) in the stopband. In a real implementation, a finite transition region between the passband and the stopband, which is known as the transition band, always exists. The gain of the filter in the transition band is unspecified. The gain usually changes gradually through the transition band from 1 (0 dB) in the passband to 0 (−∞ dB) in the stopband.

You can measure the passband ripple and stopband ripple in decibels, as shown in the following
 equations:

Passband

ripple

=

−

20

log

⁡

10

(

1

−

δ

p

)

Stopband

ripple

=

−

20

log

⁡

10

(

δ

s

)

Based on the two equations above, you can convert the passband ripple to or from the decibel
 representation. For example, if passband ripple equals 0.01 dB, that is,

0

.

01

=

−

20

log

⁡

10

(

1

−

δ

p

)

δ

p

60

=

−

20

log

⁡

10

(

δ

s

)

δ

s

The following figure illustrates the magnitude frequency responses of a highpass filter, which
 passes high frequencies and attenuates low frequencies:

Figure 2.

[IMAGE alt='image' src='GUID-0BA846B0-9F7F-4ECF-9ABC-1FEF52F5E20F-a5.gif']

The following figure illustrates the magnitude frequency responses of a bandpass filter, which
 passes a certain band of frequencies and attenuates lower and higher frequencies:

Figure 3.

[IMAGE alt='image' src='GUID-99F82FBB-7089-4D68-A817-695A51787029-a5.gif']

In the previous figure, *stopband edge frequency 1* indicates the maximum frequency of
 the lower frequency range that you want to attenuate, and *stopband
 edge frequency 2* indicates the minimum frequency of the
 higher frequency range that you want to attenuate. The frequency range
 between *passband edge frequency 1 and 2* indicates the range of
 frequencies that can pass through the filter.

The following figure illustrates the magnitude frequency response of a bandstop filter, which
 attenuates a certain band of frequencies and passes all frequencies not within the
 band:

Figure 4.

[IMAGE alt='image' src='GUID-582503F4-BD07-4EB3-A9A5-077026D3D30E-a5.gif']

In the previous figure, *passband edge frequency 1* indicates the maximum frequency of
 the lower frequency range that can pass through the filter, and
 *passband edge frequency 2* indicates the minimum
 frequency of the higher frequency range that can pass through the filter.
 The frequency range between *stopband edge frequency 1 and 2*
 indicates the range of frequencies that you want to attenuate.

Parent topic:

Digital Filter Design Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=filter-structure-graphs-digital.html language=enus -->
## TOPIC 00042: Filter Structure Graphs

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `filter-structure-graphs-digital.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/filter-structure-graphs-digital.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The realization of a digital filter involves summations and multiplications of the output, input, and intermediate operands.You must make the values that pass along the signal path available during the realization process. Therefore, to represent the structure of a filter using a signal flow graph,

### Filter Structure Graphs

The realization of a digital filter involves summations and multiplications of the
 output, input, and intermediate operands.

You must make the values that pass along the signal path available during the realization
 process. Therefore, to represent the structure of a filter using a signal flow graph,
 you not only need adders and multipliers, but you also need delays that help you store
 the passed values.

The following figure shows the symbol of an adder:

[IMAGE alt='image' src='GUID-A499C9C9-068C-4D0A-B1F9-4AFC3FC759AE-a5.gif']

You can treat a consecutive sequence of adders in a filter structure as an accumulator.

The following figure shows the symbol of a multiplier:

[IMAGE alt='image' src='GUID-46080C21-B211-4355-9281-E5678CEBE128-a5.gif']

The following figure shows the symbol of a delay:

[IMAGE alt='image' src='GUID-56D6F32E-A55C-45A8-A1EF-6E7BDAA75C5B-a5.gif']

In the previous figure, z<sup>–1</sup> is a delay that stores the value of
 x[n]. The z-transform of
 x[n–1] is z<sup>–1</sup>
 times the z-transform of x[n]. The number of
 adders and multipliers implies computational complexity in the realization of a filter
 structure, and the number of delays implies memory unit requirements in the hardware.
 The more adders, multipliers, and delays a filter structure contains, the more
 computational complexity and memory units the filter requires.

Parent topic:

Select a Filter Structure

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=filter-structures-and-filter-coefficients-dig.html language=enus -->
## TOPIC 00043: Filter Structures and Filter Coefficients

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `filter-structures-and-filter-coefficients-dig.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/filter-structures-and-filter-coefficients-dig.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you quantize the filter coefficients, configure the appropriate quantizer according to the filter structure type.Different filter structures use different groups of filter coefficients. The LabVIEW Digital Filter Design Toolkit categorizes filter coefficients into three groups: zeroes, poles, a

### Filter Structures and Filter
 Coefficients

When you quantize the filter coefficients, configure the appropriate quantizer according
 to the filter structure type.

Different filter structures use different groups of filter coefficients. The LabVIEW
 Digital Filter Design Toolkit categorizes filter coefficients into three groups: zeroes,
 poles, and gain. For example, FIR filter coefficients, IIR forward coefficients, and
 lattice ladder coefficients correspond to zeroes. IIR reverse coefficients and lattice
 reflection coefficients, excluding lattice MA reflection coefficients, correspond to
 poles. Different groups of filter coefficients have different data ranges. Therefore, in
 addition to the gain, the Digital Filter Design Toolkit provides the following two
 quantizers for these groups: coefficients a/k and
 coefficients b/v.

The following table lists the filter structures, the filter coefficients, and the
 corresponding quantizers:

| Filter Structure | Filter Coefficients and the Corresponding Quantizer |
| --- | --- |
| FIR structures | All FIR filter coefficients correspond to the coefficients b/v quantizer. |
| IIR Direct Form structuresIIR Cascaded Second-Order Sections Form structures | The reverse coefficients correspond to the coefficients a/k quantizer. The forward coefficients correspond to the coefficients b/v quantizer. |
| Lattice Allpass structuresLattice AR structuresLattice MA structures | The reflection coefficients correspond to the coefficients a/k quantizer. |
| Lattice ARMA structures | The reflection coefficients correspond to the coefficients a/k quantizer. The ladder coefficients correspond to the coefficients b/v quantizer. |

Parent topic:

Quantize Floating-Point Filters

Related concepts:

- Select a Filter Structure

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=fir-and-iir-filters-digital-filter-design-too.html language=enus -->
## TOPIC 00044: FIR and IIR Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `fir-and-iir-filters-digital-filter-design-too.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/fir-and-iir-filters-digital-filter-design-too.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can design both Finite Impulse Response (FIR) and Infinite Impulse Response (IIR) digital filters using the LabVIEW Digital Filter Design Toolkit. FIR The output signal of the filter, after you set the input signal from nonzero to zero, can be nonzero for only a finite number of sample times bef

### FIR and IIR Filters

You can design both Finite Impulse Response (FIR) and Infinite Impulse Response (IIR)
 digital filters using the LabVIEW Digital Filter Design Toolkit.

FIR

IIR

The choice between FIR and IIR filters affects both the filter design process and the implementation of the filter.

#### Mathematical Definitions

In the time domain, the filtering process for FIR filters is defined mathematically
 as a convolution of M+1 filter coefficients
 h<sub>k</sub> with a sequence of input
 data samples x[n]:

y

⁢

[

n

]

=

∑

k

=

0

M

h

k

x

⁢

[

n

−

k

]

where y[n] is the output of the filter
 and M is the filter order. The number of coefficients for the FIR
 filter is defined as the number of taps, which is M+1.

If a
 single nonzero value is present at the input of the filter but all subsequent input
 samples are zeroes, the output of the filter in Equation A becomes zero after the
 filter processes M+1 input data samples. Because the duration of
 the nonzero response in this case is finite for M+1, the filter
 in Equation A is an FIR filter.

In 1962, Charles Rader and Bernard Gold at MIT
 Lincoln Laboratory, motivated by a digital vocoder (voice coder) application,
 devised the idea of using recursive digital filters. This innovation led to the IIR
 filter, which has a time-domain response defined by the following equation:

∑

i

=

0

M

a

i

y

[

n

−

i

]

=

∑

k

=

0

N

b

k

x

[

n

−

k

]

where

- N is the numerator order
- M is the denominator order
- a i is the set of reverse
 coefficients
- b k is the set of forward
 coefficients

The filter defined by Equation B operates on the current input
 x[n] and the previous input
 x[n−k] and the current
 output y[n] and the previous output
 y[n−i]. The impulse
 response of the filter in this case is infinite because the filter might generate
 nonzero outputs arbitrarily for an indefinite amount of time in response to a single
 nonzero input sample.

For most filtering applications, FIR filters are
 sufficient. In general, FIR filters use the available precision better, and they are
 more numerically robust. However, in some cases FIR filter orders become
 impractically large. For example, if you need a large number of FIR filter
 coefficients an FIR filter might be too difficult or expensive to implement because
 the implementation might require more memory, power, processing time, and
 engineering time.

#### FIR Filters and IIR
 Filters

One difference between FIR and IIR filters is the impulse
 response, which is finite or infinite, respectively. When you design a filter, you
 must consider other differences between FIR and IIR filters that might affect the
 design. For example, FIR filter implementations typically require more
 multiplications and summations than IIR filters with similar filtering performance.
 However, because certain computer architectures, for example Digital Signal
 Processors (DSPs), are frequently better suited to performing FIR filtering, the
 computation speed of an IIR filter is not necessarily faster than an FIR filter. The
 following table compares the attributes of causal FIR and IIR filters.

| Attribute | FIR Filter | IIR Filter |
| --- | --- | --- |
| Exact linear phase response | Possible | Not possible |
| Stability | Always stable | Conditionally stable |
| Fixed-point version | Easy to implement | Can be complicated to implement |
| Computational complexity | More computations | Fewer computations |
| Data path precision typically required | Less precision required | Greater precision required |
| Zero-input limit cycles[1]1 "Zero-input limit cycle behavior refers to the effect that the output may continue to oscillate indefinitely with a periodic pattern while the input remains equal to zero. And it is a consequence either of the nonlinear quantizers in the feedback loop of IIR filter or of overflow of additions.” (Oppenheim and Schafer) | Cannot produce limit cycles | Might produce limit cycles |

Parent topic:

Digital Filter Design Basics

[<sup>1</sup>](#note_ref-d1782e501) "Zero-input limit cycle behavior
 refers to the effect that the output may continue to oscillate
 indefinitely with a periodic pattern while the input remains
 equal to zero. And it is a consequence either of the nonlinear
 quantizers in the feedback loop of IIR filter or of overflow of
 additions.” (Oppenheim and Schafer)

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=fir-structures-digital-filter-design-toolkit.html language=enus -->
## TOPIC 00045: FIR Structures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `fir-structures-digital-filter-design-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/fir-structures-digital-filter-design-toolkit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For an FIR filter, you can implement one of the following section types of FIR filter structures: basic FIR direct form, FIR direct form transposed, FIR symmetric, or FIR antisymmetric.The transfer function of an FIR filter is defined as follows: H(z)  = Gain⁢ ⋅∑n=0M h⁢  [n] z−nwhere z is a complex

### FIR Structures

For an FIR filter, you can implement one of the following section types of FIR filter
 structures: basic FIR direct form, FIR direct form transposed, FIR symmetric, or FIR
 antisymmetric.

The transfer function of an FIR filter is defined as follows:

H

(

z

)

=

G

a

i

n

⁢

⋅

∑

n

=

0

M

h

⁢

[

n

]

z

−

n

where

- z is a complex variable
- M is the filter order
- h is the set of filter coefficients

#### FIR Direct Form

For FIR
 filters, the FIR Direct Form structure is the most straightforward structure from a
 filter transfer function perspective. The number of delays equals the filter order.
 Refer to the *Understanding Filter Structure Graphs* section for
 information that helps you read and understand a filter structure graph. The
 following figure represents the FIR Direct Form structure:

[IMAGE alt='image' src='GUID-A0B942E2-3A6C-45FC-95D5-9491C85D97D6-a5.gif']

#### FIR Direct Form
 Transposed

The FIR Direct Form Transposed structure is the alternate
 direct form implementation for FIR filters. The following figure represents the FIR
 Direct Form Transposed structure:

[IMAGE alt='image' src='GUID-DA48E26A-AEA2-4638-90D8-72AFEF4D51B7-a5.gif']

Both direct form structures contain the same number of delays. However, in the
 FIR Direct Form structure, the word length of the delays equals that of the input
 signal x[n]. In the FIR Direct Form Transposed
 structure, the word length of the delays equals that of the accumulator. In most
 cases, the word length of the input signal is less than the word length of the
 accumulator. Therefore, the FIR Direct Form structure requires less memory for
 saving internal states than the transposed structure.

Both direct form
 structures also contain the same number of multipliers, which equals
 M+1. However, if you perform the multiplications in parallel
 and then perform summations on the multiplication products for both structures, the
 FIR Direct Form Transposed structure has better timing performance because the
 delays following the adders in this structure can store the summation results
 temporarily for performing the summations in parallel. However, the FIR Direct Form
 structure does not contain delays for the adders so the summations in this structure
 take more time. If you perform the multiplications and additions serially using a
 loop structure, the FIR Direct Form structure is more efficient because this
 structure requires less memory.

#### FIR Symmetric

Use the FIR
 Symmetric structures for symmetric linear phase FIR filters, which use the symmetry
 of the filter coefficients to reduce the number of multipliers from
 M+1 to M/2+1, when M is
 an even number, or (M+1)/2, when M is an odd
 number. The following figure represents the FIR Symmetric structure when the filter
 order is an even number:

[IMAGE alt='image' src='GUID-5BAEFE4E-9E15-4872-849A-59CB89DDFB27-a5.gif']

The following figure represents the FIR Symmetric structure when the filter
 order is an odd number:

[IMAGE alt='image' src='GUID-1506812D-169F-417C-A21B-FC0ED2F47D93-a5.gif']

#### FIR Antisymmetric

Use the
 FIR Antisymmetric structure for antisymmetric linear phase FIR filters, which use
 the antisymmetry of the filter coefficients to reduce the number of multipliers from
 M+1 to M/2, when M is
 an even number, or (M+1)/2, when M is an odd
 number. The following figure represents the FIR Antisymmetric structure when the
 filter order is an even number:

[IMAGE alt='image' src='GUID-03FE197D-C22D-49B9-888A-3CD209C60DBE-a5.gif']

The following figure represents the FIR Antisymmetric structure when the filter
 order is an odd number:

[IMAGE alt='image' src='GUID-D185B906-4902-4CD9-AFE4-81911EFE8A7B-a5.gif']

Parent topic:

Select a Filter Structure

Related concepts:

- Filter Structure Graphs

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=generate-code-from-fixed-point-filters-digi.html language=enus -->
## TOPIC 00046: Generate Code from Fixed-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `generate-code-from-fixed-point-filters-digi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/generate-code-from-fixed-point-filters-digi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you obtain an appropriate fixed-point filter model, you can implement the resulting fixed-point filter on the target hardware. Output quantizers generally have different integer word lengths from the input quantizers. Before generating code, check the quantizer settings to confirm or modify th

### Generate Code from Fixed-Point Filters

Note

overflow mode

Saturate

- [Export Fixed-Point Integer Coefficients](export-fixed-point-integer-coefficients-di.html)
- [Generate Fixed-Point C Code](generate-fixed-point-c-code-digital-filter.html)
- [Generate Integer LabVIEW Code](generate-integer-labview-code-digital-filte.html)
- [Generate LabVIEW FPGA Code](generate-labview-fpga-code-digital-filter-d.html)
- [Postprocess Filtered Signals](postprocessing-filtered-signals-digital-filte.html)

Parent topic:

Design Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=generate-fixed-point-c-code-digital-filter.html language=enus -->
## TOPIC 00047: Generate Fixed-Point C Code

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `generate-fixed-point-c-code-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/generate-fixed-point-c-code-digital-filter.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You usually program target Digital Signal Processing (DSP) hardware using C code. To generate C code from the fixed-point filter model, use the C Code instance of the DFD FXP Code Generator VI.You can compile the generated code to run on a fixed-point DSP.C code can yield a less compact and less eff

### Generate Fixed-Point C Code

You usually program target Digital Signal Processing (DSP) hardware using C code. To
 generate C code from the fixed-point filter model, use the C Code instance of the
 DFD FXP Code Generator VI.

Note

The DFD FXP Code Generator VI produces three files, where
 filtername is the string you wire to the filter
 name input:

- nidfdtyp.h contains the definitions of the data types in the C source files
 that the DFD FXP Code Generator VI generates. You might need to
 redefine the data types in this file if you want to compile the generated code to
 run on a 64-bit target.
- filtername.h contains type definitions, global variable declarations, and
 function prototypes.
- filtername.c contains the code that implements the filter, including the
 filter coefficients, information about the implementation structure and quantizer
 settings in the fixed-point model, and the following functions:
  - filtername_State filtername_CreateState() creates the
 memory space needed to store the internal states of the filter.
  - void filtername_DisposeState(filtername_State state) 
 disposes of the memory space used to store the internal states of the
 filter.
  - void filtername_InitState(filtername_State state) 
 initializes the internal states to zeroes. Call this function for the first
 block when processing a large data sequence that consists of multiple data
 blocks.
  - I16 filtername_Filtering(I16 sampleIn, filtername_State
 state) implements the fixed-point filter.
  - static I16 filtername_Coef[] contains the quantized
 coefficients of the fixed-point filter.

Parent topic:

Generate Code from Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=generate-integer-labview-code-digital-filte.html language=enus -->
## TOPIC 00048: Generate Integer LabVIEW Code

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `generate-integer-labview-code-digital-filte.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/generate-integer-labview-code-digital-filte.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Integer LabVIEW code is useful when you simulate the behavior of a fixed-point filter on Windows. You can use the DFD FXP Code Generator VI to generate integer LabVIEW code from a fixed-point filter.Integer LabVIEW code can run on any platform or target on which you can run LabVIEW VIs. The LabVIEW

### Generate Integer LabVIEW Code

Integer LabVIEW code is useful when you simulate the behavior of a fixed-point filter on
 Windows. You can use the DFD FXP Code Generator VI to generate
 integer LabVIEW code from a fixed-point filter.

Integer LabVIEW code can run on any platform or target on which you can run LabVIEW VIs. The
 LabVIEW Digital Filter Design Toolkit uses LabVIEW projects to manage the resulting
 integer LabVIEW code. The following figure shows an example project file that contains
 integer LabVIEW code:

[IMAGE alt='image' src='GUID-3FFE87B6-7794-4D0D-A0A5-F129F2BDDFC5-a5.gif']

In the previous figure, the filtername.lvproj file, where
 filtername denotes the name of the fixed-point filter, contains
 the following folders and VIs in addition to the default items:

filtername

Filter SubVIs

filtername_Filter.vi

Parent topic:

Generate Code from Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=generate-labview-fpga-code-digital-filter-d.html language=enus -->
## TOPIC 00049: Generate LabVIEW FPGA Code

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `generate-labview-fpga-code-digital-filter-d.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/generate-labview-fpga-code-digital-filter-d.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW Field-Programmable Gate Array (FPGA) code is a type of code specifically optimized to run on NI Reconfigurable I/O (RIO) devices such as the PXI-7831R. You can use the Start IP Generator dialog box or the DFD FXP Code Generator VI to generate LabVIEW FPGA code.LabVIEW FPGA code takes advanta

### Generate LabVIEW FPGA Code

LabVIEW Field-Programmable Gate Array (FPGA) code is a type of code specifically
 optimized to run on NI Reconfigurable I/O (RIO) devices such as the PXI-7831R. You can
 use the Start IP Generator dialog box or the DFD FXP
 Code Generator VI to generate LabVIEW FPGA code.

LabVIEW FPGA code takes advantage of the specific features, such as the Single-Cycle Timed Loop
 (SCTL) and memory items, of the LabVIEW FPGA Module. Therefore, this type of code can
 run on an FPGA target efficiently. You can generate LabVIEW FPGA code for filters with
 the following filter structures:

- FIR structures
- IIR Cascaded Second-Order Sections Form structures
- Lattice MA structures
- Lattice ARMA structures

Note

Note

The LabVIEW Digital Filter Design Toolkit uses LabVIEW projects to manage the resulting LabVIEW
 FPGA code. The following figure shows an example project file that contains LabVIEW FPGA
 code:

[IMAGE alt='image' src='GUID-7F73E634-8DFD-42C8-B606-84F885624732-a5.gif']

In the previous figure, the filtername.lvproj file, where
 filtername denotes the name of the fixed-point filter, contains
 the following folder and VI in addition to the default items.

filtername

filtername_Filter.vi

Note

You can generate both one-channel and multichannel LabVIEW FPGA code from a fixed-point
 filter.

To use multichannel LabVIEW FPGA code, you must interleave the input data.

Parent topic:

Generate Code from Fixed-Point Filters

Related concepts:

- FIR Structures
- IIR Cascaded Second-Order Sections Form Structures
- Lattice ARMA Structures
- Lattice MA Structures

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=generating-code-from-fixed-point-multirate-filters.html language=enus -->
## TOPIC 00050: Generate Code from Fixed-Point Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `generating-code-from-fixed-point-multirate-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/generating-code-from-fixed-point-multirate-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After obtaining an appropriate fixed-point filter model, the resulting fixed-point filter can be implemented on target hardware.The fixed-point integer coefficients can be exported from the filter and then used in a filter execution engine. A LabVIEW FPGA code can be generated and then used the LabV

### Generate Code from Fixed-Point Multirate
 Filters

After obtaining an appropriate fixed-point filter model, the resulting fixed-point
 filter can be implemented on target hardware.

The fixed-point integer coefficients can be exported from the filter and then used in a filter
 execution engine. A LabVIEW FPGA code can be generated and then used the LabVIEW
 FPGA Module to target and deploy the resulting FPGA code to an NI Reconfigurable I/O
 (RIO) target.

#### Exporting Fixed-Point Integer
 Coefficients

When using a filter execution engine for which you need only
 filter coefficients, you can export the fixed-point multirate filter coefficients to
 a text file using the DFD Save to Text File VI. You can save the
 multirate filter coefficients to a text file and load them to the execution target.
 The text file contains a section that provides all information about the fixed-point
 integer coefficients and corresponding quantizers.

#### Generating LabVIEW FPGA
 Code

Use the Start IP Generator dialog box or the
 DFD FXP MRate Code Generator VI to generate LabVIEW
 field-programmable gate array (FPGA) code from a multirate filter.

Note

The Digital
 Filter Design Toolkit uses LabVIEW projects to manage the resulting LabVIEW FPGA
 code. The following figure shows an example project file that contains LabVIEW FPGA
 code:

Figure 21.

[IMAGE alt='image' src='GUID-2CF83C29-3888-419A-BA84-EE08380AA857-a5.gif']

In the previous figure, the filtername.lvproj file, where
 filtername denotes the name of the fixed-point filter,
 contains the following folder and VI in addition to the default items:

filtername Block

filtername_DataOut

1. Right-click filtername_DataOut .
2. Choose Properties from the shortcut
 menu.
3. Choose Target to Host-DMA from the
 Type menu.
4. Click OK .

filtername_DataIn

filtername_Filter.vi

Note

The way the LabVIEW FPGA code is used is different from the way a general
 LabVIEW VI is used. The following figure shows an example of a block diagram that
 uses LabVIEW FPGA code generated from the filtername_Filter
 VI.

Figure 22.

[IMAGE alt='image' src='GUID-E8119238-CA20-4987-AE78-A2969DB38594-a5.gif']

In the previous figure, the filtername_Filter VI is not
 connected to any other items on the block diagram. However, this VI actually
 communicates with the items in the loop structures by processing the input signal
 from the filtername_DataIn FIFO and returning the output signal
 to the filtername_DataOut FIFO.

You can generate LabVIEW
 FPGA code from a fixed-point single-stage multirate filter by using the
 Start IP Generatordialog box or the DFD FXP
 MRate Code Generator VI.

You can generate LabVIEW FPGA code from
 a fixed-point multistage multirate filter by using the Start IP Generator dialog box or the DFD FXP NStage MRate Code
 Generator VI.

You also can generate LabVIEW FPGA code from a
 fixed-point moving average filter by using the Start IP Generator dialog box or the DFD FXP Moving Average Code
 Generator VI.

#### Postprocessing Filtered
 Signals

After you deploy fixed-point filter coefficients to the target
 hardware, you can postprocess the filtered signal using the DFD FXP MRate
 Postprocessing VI.

Parent topic:

Design Fixed-Point Multirate Filters

Related concepts:

- Postprocess Filtered Signals

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=group-delay-and-phase-delay-digital-filter-de.html language=enus -->
## TOPIC 00051: Group Delay and Phase Delay

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `group-delay-and-phase-delay-digital-filter-de.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/group-delay-and-phase-delay-digital-filter-de.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section covers the formulas used to calculate and the relationships between the group delay response and the phase delay response of a filter.For a filter with a frequency response of H(e^jω), the phase delay response τ[ρ] is defined by the following equation:τρ⁢ =  −arg⁡ [H(ejω)]ωThe group del

### Group Delay and Phase Delay

This section covers the formulas used to calculate and the relationships between
 the group delay response and the phase delay response of a filter.

For a filter with a frequency response of H(e<sup>jω</sup>), the phase delay response
 τ<sub>ρ</sub> is defined by the following equation:

τ

ρ

⁢

=

−

arg

⁡

[

H

(

e

j

ω

)

]

ω

The group delay response τ<sub>g</sub> is defined as the negative derivative of the phase
 response ω, as shown in the following equation:

τ

g

(

ω

)

=

−

d

d

ω

⁢

arg

[

H

(

e

j

ω

)

]

⁡

Both the group delay and phase delay are in samples.

For a generalized linear phase filter with arg
 
 [
 H
 (
 e
 j
 ω
 )
 ]
 
 
 =
 
 
 −
 α
 ω
 +
 β the group delay is
 represented by the following equation:

τ

g

(

ω

)

=

−

d

d

ω

⁢

arg

[

H

(

e

j

ω

)

]

=

α

The phase delay is represented by the following equation:

τ

ρ

⁢

=

−

arg

⁢

[

H

(

e

j

ω

)

]

ω

⁢

=

α

−

β

ω

You can represent the phase delay as the time delay in samples experienced by each frequency
 component of the input signal. The filter is represented by the following
 equation:

x

(

n

)

→

e

j

β

→

H

n

e

w

(

e

j

ω

)

→

y

(

n

)

The filter H(e<sup>jω</sup>) shifts all frequency components by a phase β and then filters the
 signal with a new filter H<sub>new</sub>(e<sup>jω</sup>) that has a phase of –αω. You
 can interpret the group delay as the time delay in samples experienced by each frequency
 component through the new filter H<sub>new</sub>(e<sup>jω</sup>).

Linear phase filters are characterized by a constant group delay. The deviation of the group delay from a constant value within the passband indicates the degree of nonlinearity in the phase. Use the group delay to analyze the linearity of a filter.

Parent topic:

Digital Filter Design Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=group-delay-compensator-digital-filter-design.html language=enus -->
## TOPIC 00052: Group Delay Compensator

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `group-delay-compensator-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/group-delay-compensator-digital-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Infinite Impulse Response (IIR) filters designed using Butterworth, Chebyshev, or Elliptic methods usually have a nonconstant group delay, which means that they have nonlinear phase or phase distortion. The greatest deviation from a constant group delay typically occurs at the edge of the passband o

### Group Delay Compensator

Infinite Impulse Response (IIR) filters designed using Butterworth, Chebyshev, or
 Elliptic methods usually have a nonconstant group delay, which means that they have
 nonlinear phase or phase distortion. The greatest deviation from a constant group delay
 typically occurs at the edge of the passband or somewhere in the transition band.

Given a filter with phase distortion, you can cascade the filter with an allpass filter to
 linearize the phase response in the specified frequency ranges while keeping the
 magnitude response unchanged.

Let τ<sub>0</sub>(f<sub>i</sub>) and
 τ<sub>ap</sub>(ā,f<sub>i</sub>)
 denote the group delay of the given filter and the designed allpass filter at the
 i<sup>th</sup> frequency point, respectively. The coefficients vector of the allpass
 filter ā is determined by the following equation:

m

i

n

∑

i

τ

a

p

a

⇀

,

f

i

+

τ

0

f

i

-

τ

ρ

where τ is the target group delay in all user-defined frequency ranges.

A 4<sup>th</sup> order elliptic bandpass filter with a passband frequency ranging from 0.3 to 0.4
 has nonconstant group delay in the specified passband. The following figure shows how to
 compensate the filter group delay in the specified passband to be near constant with an
 8<sup>th</sup> order compensator using the DFD Group Delay
 Compensator VI.

Figure 10.

[IMAGE alt='image' src='GUID-FD556B80-AC43-4F4B-975F-61CB523A9341-a5.gif']

The block diagram in the above figure uses the DFD Plot Group Delay VI to
 check the group delay response of the filter. The following figure shows the group delay
 response of the original filter and the compensated filter.

Figure 11.

[IMAGE alt='image' src='GUID-C53ECE4F-7229-4E1B-B868-08EA91DA901B-a5.gif']

In the previous figure, you can see that the group delay of the compensated filter is fairly constant in the passband frequency ranging from 0.3 to 0.4. The constant value of the group delay indicates that the compensated filter linearly approximates the phase response in the passband. However, compared to the original filter, the compensated filter also increases the delay and filtering computation.

Parent topic:

Design Special Filters

Related concepts:

- FIR and IIR Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=handling-overflows-and-underflows-digital-fil.html language=enus -->
## TOPIC 00053: Handle Overflows and Underflows

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `handling-overflows-and-underflows-digital-fil.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/handling-overflows-and-underflows-digital-fil.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can handle overflows and underflows using either saturation or a quantizer wrap.Fixed-point numbers can represent only numbers of a finite range. Overflows occur when a number is greater than the maximum representable number within the range. Underflows occur when a number is less than the minim

### Handle Overflows and Underflows

You can handle overflows and underflows using either saturation or a quantizer wrap.

Fixed-point numbers can represent only numbers of a finite range. Overflows occur when a
 number is greater than the maximum representable number within the range. Underflows
 occur when a number is less than the minimum representable number within the range.

Saturation

Wrap

iwl

The saturation mode of the output quantizer is preferred over the wrap
 mode in most real-world applications because the saturation mode helps avoid signal
 discontinuities, or sudden changes in the amplitudes. However, the saturation
 mode is more complicated than the wrap mode. For internal quantizers,
 such as the sum quantizer, the wrap mode is preferred because this mode allows
 intermediate overflows and underflows within a certain range as long as the final output
 does not contain overflows or underflows. Use the overflow mode
 input of the Fixed-Point Tools VIs to specify an appropriate setting
 for handling overflows and underflows.

Parent topic:

Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=hilbert-transformers-digital-filter-design-to.html language=enus -->
## TOPIC 00054: Hilbert Transformers

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `hilbert-transformers-digital-filter-design-to.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/hilbert-transformers-digital-filter-design-to.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Hilbert transform to extract instantaneous phase information and obtain the single-sideband spectra, obtain the envelope of an oscillating signal, detect echoes, and reduce sampling rates. The ideal frequency response of a Hilbert transformer is as follows: H ⁢   ( f ) =   − j ⁢ sgn ⁡ ( f )

### Hilbert Transformers

Use the Hilbert transform to extract instantaneous phase information and obtain the
 single-sideband spectra, obtain the envelope of an oscillating signal, detect echoes,
 and reduce sampling rates. The ideal frequency response of a Hilbert transformer is as
 follows:

H

⁢

(

f

)

=

−

j

⁢

sgn

⁡

(

f

)

where f is the normalized frequency with the range [0, 0.5]. The
 frequency response has −90° phase shift for positive frequencies and 90° phase shift for
 negative frequencies.

If you compare this equation with Equation B in the *Linear Phase Filters* topic, you
 can see that an ideal Hilbert transformer has a linear phase and is a Type III or Type
 IV linear phase FIR filter.

You can use the DFD Remez Design VI to design a Hilbert transformer by setting
 the filter type input to Hilbert. The
 following sections explain how to create Type IV and Type III Hilbert transformers:

#### Designing Type IV Hilbert
 Transformers

Type IV (odd order, antisymmetric) filters make ideal Hilbert
 transformers. When you design a Type IV Hilbert transformer with the DFD
 Remez Design VI, you can specify a single band that contains two
 points with equal weights. For example, consider a frequency range of [0.1, 0.5]
 with an amplitude of [−1, −1]. To design a Type IV Hilbert transformer with an order
 of 11 using this band, enter the specifications shown in the following figure into
 the DFD Remez Design VI:

[IMAGE alt='image' src='GUID-BFD75CDC-E216-49F4-8263-887D3BCDDEBC-a5.gif']

The following figure shows the magnitude response and impulse response of the
 designed Type IV Hilbert transformer:

[IMAGE alt='image' src='GUID-BA35184D-8E20-4A2E-B14F-639243FC0621-a5.gif']

In the previous figure, you can see that magnitude response of the designed
 filter is fairly constant in the range [0.1, 0.5]. The magnitude response of an
 ideal Hilbert transformer, which has an infinitely large order, has a constant value
 in the specified frequency range. The impulse response of the designed filter shows
 that this filter is antisymmetric.

#### Designing Type III Hilbert
 Transformers

Type III (even order, antisymmetric) Hilbert transformers are
 useful if you want to filter out high frequencies. Type III filters constrain the
 amplitude to zero at the Nyquist frequency of 0.5 Hz. By changing the frequency
 range of the previous example to [0.05, 0.45] and maintaining the corresponding
 amplitude at [−1, −1], you can design a bandpass-like Hilbert transformer. For this
 example, you design a Type III Hilbert transformer with an order of 12 by entering
 the specifications shown in the following figure into the DFD Remez
 Design VI:

[IMAGE alt='image' src='GUID-2B02790A-155D-4B72-9D9A-A874F1CFE79E-a5.gif']

The following figure shows the magnitude response of the resulting Type III
 Hilbert transformer:

[IMAGE alt='image' src='GUID-E65DD0A7-7602-4E2C-A47E-FE698EE94748-a5.gif']

In the first figure, you can see that the magnitude response of the designed
 filter is fairly constant in the range [0.05, 0.45] and is zero at 0.5 Hz. The
 figure also shows that the magnitude response contains ripples. To minimize the
 ripples, you can specify a larger value for the order
 input.

Parent topic:

Design Special Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=iir-cascaded-second-order-sections-form-struc.html language=enus -->
## TOPIC 00055: IIR Cascaded Second-Order Sections Form Structures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `iir-cascaded-second-order-sections-form-struc.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/iir-cascaded-second-order-sections-form-struc.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For an IIR filter with a Cascaded Second-Order Sections Form, you can implement one of the following section types of IIR Cascaded Second-Order Sections filter structures: IIR Cascaded Second-Order Sections Form I IIR Cascaded Second-Order Sections Form II IIR Cascaded Second-Order Sections Form I T

### IIR Cascaded Second-Order Sections Form
 Structures

For an IIR filter with a Cascaded Second-Order Sections Form, you can implement one of the
 following section types of IIR Cascaded Second-Order Sections filter structures:

- IIR Cascaded Second-Order Sections Form I
- IIR Cascaded Second-Order Sections Form II
- IIR Cascaded Second-Order Sections Form I Transposed
- IIR Cascaded Second-Order Sections Form II Transposed

The transfer function of an Infinite Impulse Response (IIR) filter with a Cascaded Second-Order
 Sections Form structure is defined as follows:

H

(

z

)

=

G

a

i

n

⁢

⋅

∏

n

=

0

N

−

1

b

n

⁢

⁢

[

0

]

+

b

n

[

1

]

z

−

1

+

b

n

⁢

[

2

]

z

−

2

1

+

a

n

⁢

[

1

]

z

−

1

+

a

n

⁢

[

2

]

z

−

2

where

- z is a complex variable
- N is the number of sections
- a is the set of reverse coefficients
- b is the set of forward coefficients

#### IIR Cascaded Second-Order Sections
 Form I

Comparing with the IIR Direct Form structures, the IIR Cascaded
 Second-Order Sections Form structures have more computational complexity. However,
 the cascaded structures help alleviate finite word length effects. Refer to the
 Understanding Filter Structure Graphs topic for information that helps you read and
 understand a filter structure graph. The following figure represents the IIR
 Cascaded Second-Order Sections Form I structure:

[IMAGE alt='image' src='GUID-80589C78-122F-451C-9310-7213477D557A-a5.gif']

#### IIR Cascaded Second-Order Sections
 Form II

Comparing with Form I, this structure uses the same number of
 mathematical operations but fewer delays. The following figure represents the IIR
 Cascaded Second-Order Sections Form II structure:

[IMAGE alt='image' src='GUID-2F004200-EBC4-4C0B-854E-7AF58BBDA2C8-a5.gif']

#### IIR Cascaded Second-Order Sections
 Form I Transposed

The following figure represents the IIR Cascaded
 Second-Order Sections Form I Transposed structure:

[IMAGE alt='image' src='GUID-F7BC34A8-0B86-4271-BD55-4E30AD2B5EDD-a5.gif']

#### IIR Cascaded Second-Order Sections
 Form II Transposed

The following figure represents the IIR Cascaded
 Second-Order Sections Form II Transposed structure:

[IMAGE alt='image' src='GUID-C9725CA5-FCA0-4F5E-8B69-8B8E3FF4E74B-a5.gif']

The IIR Cascaded Second-Order Sections Form I and Form II Transposed structures
 implement forward coefficients first. The Form I Transposed and Form II structures
 implement reverse coefficients first. The IIR Cascaded Second-Order Sections Form II
 structure has the same computational complexity as the Form I, but the Form I
 requires more memory for saving internal states. The Form II Transposed is the
 structure that you most frequently use. Using the Form I and Form II and their
 transposed structures has the same advantages and disadvantages as using the FIR
 Direct Form and FIR Direct Form Transposed structures.

Note

Parent topic:

Select a Filter Structure

Related concepts:

- Filter Structure Graphs

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=iir-direct-form-structures-digital-filter-des.html language=enus -->
## TOPIC 00056: IIR Direct Form Structures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `iir-direct-form-structures-digital-filter-des.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/iir-direct-form-structures-digital-filter-des.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For an IIR filter, you can implement one of the following section types of IIR direct form filter structures: IIR direct form I IIR direct form II IIR direct form I transposed IIR direct form II transposed The transfer function of an Infinite Impulse Response (IIR) filter is defined as follows: H (

### IIR Direct Form Structures

For an IIR filter, you can implement one of the following section types of IIR direct form
 filter structures:

- IIR direct form I
- IIR direct form II
- IIR direct form I transposed
- IIR direct form II transposed

The transfer function of an Infinite Impulse Response (IIR) filter is defined as follows:

H

(

z

)

=

G

a

i

n

⋅

∑

n

=

0

M

b

⁢

[

n

]

z

−

n

1

+

∑

n

=

1

N

a

⁢

[

n

]

z

−

n

where

- z is a complex variable
- M is the order of the numerator
- N is the order of the denominator
- a is the set of reverse coefficients
- b is the set of forward coefficients

#### IIR Direct Form I

The IIR
 Direct Form I structure is the most straightforward IIR structure from a filter
 transfer function perspective. Refer to the Understanding Filter Structure Graphs
 topic for information that helps you read and understand a filter structure graph.
 The following figure represents the IIR Direct Form I structure:

[IMAGE alt='image' src='GUID-2EB810A0-CB71-41EF-BD0F-07BAB52DF03A-a5.gif']

Note

N

M

#### IIR Direct Form II

This
 structure contains fewer mathematical operations and delays. The following figure
 represents the IIR Direct Form II structure:

[IMAGE alt='image' src='GUID-6BA62E0F-19D2-496F-9E5F-367A62538E06-a5.gif']

#### IIR Direct Form I
 Transposed

The following figure represents the IIR Direct Form I
 Transposed structure:

[IMAGE alt='image' src='GUID-E00068CF-38FF-419F-9C03-EDBA456BAE95-a5.gif']

#### IIR Direct Form II
 Transposed

The following figure represents the IIR Direct Form II
 Transposed structure:

[IMAGE alt='image' src='GUID-4B984BB2-28F9-4BB6-ACF5-E7DEF0F0D66D-a5.gif']

The IIR Direct Form I and Form II Transposed structures implement forward
 coefficients first. The Form I Transposed and Form II structures implement reverse
 coefficients first. Using Form I and Form II and their transposed structures has the
 same advantages and disadvantages as using the FIR Direct Form and FIR Direct Form
 Transposed structures. The IIR Direct Form structures usually require few
 mathematical operations. However, the sensitivity to finite word length effects
 limits the use of this form in fixed-point implementations. Use the IIR Cascaded
 Second-Order Sections Form structures to alleviate finite word length
 effects.

Parent topic:

Select a Filter Structure

Related concepts:

- Filter Structure Graphs

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=implementing-fixed-point-cic-filters.html language=enus -->
## TOPIC 00057: Implement Fixed-Point CIC Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `implementing-fixed-point-cic-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/implementing-fixed-point-cic-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To implement fixed-point CIC filters, cascade N basic integrator sections (the I block) and N basic comb sections (the C block) together with a sampling frequency conversion factor. The Digital Filter Design Toolkit supports fixed-point implementation of only lowpass CIC filters. The following figur

### Implement Fixed-Point CIC Filters

To implement fixed-point CIC filters, cascade N basic integrator
 sections (the I block) and N basic comb sections
 (the C block) together with a sampling frequency conversion
 factor.

The Digital Filter Design Toolkit supports fixed-point implementation of only lowpass CIC
 filters. The following figure shows an example of a fixed-point implementation of an
 N-stage decimation CIC filter, where M is the
 sampling frequency conversion factor:

Figure 23.

[IMAGE alt='image' src='GUID-9FDD08FF-AFE9-4771-975B-AF31D92714C3-a5.gif']

The following figure shows an example of a fixed-point implementation of an
 N-stage interpolation CIC filter.

Figure 24.

[IMAGE alt='image' src='GUID-2620314D-426C-4D94-A683-3897DD2C181B-a5.gif']

The following figure shows a basic integrator section in detail:

Figure 25.

[IMAGE alt='image' src='GUID-13BB6034-A39C-4A54-AEFC-2A6E3C293AFF-a5.gif']

The following figure shows a basic comb section in detail:

Figure 26.

[IMAGE alt='image' src='GUID-C212CB3D-146C-48B8-82F1-DC61ED1B18B8-a5.gif']

#### Setting the Internal
 Precision

In a fixed-point implementation, the maximum bit width required for a CIC decimation
 filter is the sum of the input bits and the bits that the filter uses in
 accommodating the maximum filter gain. Using the maximum bit width for each
 integrator or comb section guarantees that no overflow occurs at the output of the
 filter. The maximum bit width also ensures that you obtain a full-precision result.
 However, obtaining the full-precision result requires the maximum Field-Programmable
 Gate Array (FPGA) hardware resources.

In most real-world applications, the
 required output bit width is smaller than the maximum bit width. Therefore, you can
 discard the Least Significant Bits (LSBs) from the maximum bit width to obtain a
 smaller output bit width. Using the DFD FXP MRate Modeling VI,
 you can prune the LSBs in each successive integrator or comb section. This operation
 is known as bit pruning. Bit pruning enables you to obtain a precision that
 approximates the full precision and to spare the FPGA hardware resources. However,
 bit pruning introduces additional noise to each processing section, and the amount
 of LSBs that you discard determines the noise level.

When using the
 DFD FXP MRate Modeling VI to model a fixed-point CIC filter,
 you can set the internal precision input to
 Truncated to prune the intermediate bit widths. This option is
 valid for only multirate FIR filters and fixed-point CIC decimation filters. If you
 set internal precision to Full, this VI
 applies the maximum bit width to each processing section.

The following figure
 shows an example of filtering results by using both the
 Truncated and Full options:

Figure 27.

[IMAGE alt='image' src='GUID-FAE3851D-C208-4554-8BF1-7574C939C43E-a5.gif']

In the Output Signal graph of the previous figure, you can
 see that the Truncated plot renders nearly the same filtering
 result as the Full plot does. The Comparing the Full and
 Truncated Options graph shows the detailed difference between the
 two filtering results. The few nonzero values indicate the slight precision
 difference between the two internal precision options.

Parent topic:

Cascaded Integrator Comb Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=interpolation-digital-filter-design-toolkit.html language=enus -->
## TOPIC 00058: Interpolation

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `interpolation-digital-filter-design-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/interpolation-digital-filter-design-toolkit.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Interpolation (also known as up-sampling) is the process of increasing the sampling frequency of a signal to a higher sampling frequency that differs from the original frequency by an integer value.The spectrum of the output signal ideally is the same as the input signal spectrum, except the output

### Interpolation

Interpolation (also known as up-sampling) is the process of increasing the sampling
 frequency of a signal to a higher sampling frequency that differs from the original
 frequency by an integer value.

The spectrum of the output signal ideally is the same as the input signal spectrum, except the
 output signal spectrum contains an additional high-frequency region with zero-power
 density.

The following figure shows a typical L-fold interpolation filter, where
 L is the target integer increase in the sampling frequency.

Figure 18.

[IMAGE alt='image' src='GUID-4328E4DB-71F2-4E65-B402-F6BC7102C3B4-a5.gif']

L

H

z

L

L

x

n

f

s

x

n

Lf

s

H

z

y

n

Note

Multirate
 Systems and Filter Banks

The following figure shows the spectrum of the original signal
 x(n) and the spectra from directly
 interpolating the signal by 2, 3, and L without using an anti-imaging
 filter.

Figure 19.

[IMAGE alt='image' src='GUID-5078C7D9-A92C-4B78-98E6-358B1D7638B0-a5.gif']

(a)

x

n

(b)

v

n

(c)

v

n

(d)

v

n

L

Notice multiple images emerge in the range from 0 to half of the resulting sampling
 frequency in parts (b), (c), and (d) of the figure. These images demonstrate the effect
 of interpolation.

The interpolation system uses the lowpass filter H(z) after
 the expander to attenuate the frequency components of the signal from
 f<sub>s</sub>/2 to
 Lf<sub>s</sub>/2. In the time domain, the
 effect of H(z) is to replace the inserted zero
 value samples that the expander introduces with the interpolated values. When replacing
 the inserted zeroes with interpolated values, the anti-imaging lowpass filter
 H(z) might alter the original values. Use a
 Nyquist interpolation filter for H(z) to maintain
 the original values.

To design interpolation filters, use the Multirate Filter Design VIs with the
 filtering mode input set to
 Interpolation.

Parent topic:

Multirate Filter Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=lattice-allpass-structures-digital-filter-des.html language=enus -->
## TOPIC 00059: Lattice Allpass Structures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `lattice-allpass-structures-digital-filter-des.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/lattice-allpass-structures-digital-filter-des.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For an allpass filter, you can implement one of the following section types of lattice allpass filter structures: basic section type one multiplier section type normalized section type Refer to the Understanding Filter Structure Graphs section for information that helps you read and understand a fil

### Lattice Allpass Structures

For an allpass filter, you can implement one of the following section types of lattice
 allpass filter structures:

- basic section type
- one multiplier section type
- normalized section type

Refer to the *Understanding Filter Structure Graphs* section for information that
 helps you read and understand a filter structure graph. The following figure represents
 the basic section type of a lattice allpass filter structure:

[IMAGE alt='image' src='GUID-8B11E638-A9C5-4B86-9620-B3461F186B6C-a5.gif']

The total number of the lattice reflection coefficients (k) is
 M, where M is the filter order. The total
 number of multipliers is 2M.

The following figure represents the one multiplier section type of a lattice allpass filter
 structure:

[IMAGE alt='image' src='GUID-095935B6-EF27-4E66-A497-CB23D137DAD3-a5.gif']

The total number of the lattice reflection coefficients (k) is
 M, which is the same as in the basic section type. However, the
 total number of multipliers is only M, which is half the number that
 the basic section type requires. Therefore, the one multiplier section type of a lattice
 allpass structure involves fewer multipliers than other section types. Fewer multipliers
 require less hardware resources.

The following figure represents the normalized section type of a lattice allpass filter
 structure:

[IMAGE alt='image' src='GUID-C783B1A1-5F53-4608-8438-38FCD7F97D07-a5.gif']

You can derive k' from k in the normalized section type by
 using the formula:

k

′

⁢

[

m

]

=

1

−

(

k

⁢

[

m

]

)

2

One advantage of the normalized section type structure is that this structure automatically scales the internal signals in each lattice section. Unfortunately, scaling the internal signals increases the implementation complexity.

Parent topic:

Select a Filter Structure

Related concepts:

- Filter Structure Graphs

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=lattice-ar-structures-digital-filter-design-t.html language=enus -->
## TOPIC 00060: Lattice AR Structures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `lattice-ar-structures-digital-filter-design-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/lattice-ar-structures-digital-filter-design-t.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For an all-pole Infinite Impulse Response (IIR) filter, you can implement one of the following section types of lattice Autoregressive (AR) filter structures: basic section type one multiplier section type normalized section type. The following figure represents the basic section type of a lattice A

### Lattice AR Structures

For an all-pole Infinite Impulse Response (IIR) filter, you can implement one of
 the following section types of lattice Autoregressive (AR) filter
 structures:

- basic section type
- one multiplier section type
- normalized section type.

The following figure represents the basic section type of a lattice AR filter structure:

[IMAGE alt='image' src='GUID-2451A32A-6994-4A64-A652-3E08450D1715-a5.gif']

The total number of the lattice reflection coefficients (k) is
 M, where M is the filter
 order. The total number of multipliers is 2M.

The following figure represents the one multiplier section type of a lattice AR filter
 structure:

[IMAGE alt='image' src='GUID-791F317E-2EFB-4DFF-9D6B-E3ECBE607DF4-a5.gif']

The total number of the lattice reflection coefficients k is (M), which is the
 same as in the basic section type. However, the total number of multipliers
 is only M, which is half the number that the basic
 section type requires. Therefore, the one multiplier section type of a
 lattice AR structure involves fewer multipliers than other section types.
 Fewer multipliers require less hardware resources.

The following figure represents the normalized section type of a lattice AR filter structure:

[IMAGE alt='image' src='GUID-581238E2-3809-4821-895E-6B7038484C90-a5.gif']

You can derive k' from k in the normalized section type by
 using the formula:

k

′

⁢

[

m

]

=

1

−

(

k

⁢

[

m

]

)

2

One advantage of the normalized section type structure is that this structure automatically scales the internal signals in each lattice section. Unfortunately, scaling the internal signals increases the implementation complexity.

Refer to the *Understanding Filter Structure Graphs* section for information that
 helps you read and understand a filter structure graph.

Parent topic:

Select a Filter Structure

Related concepts:

- Filter Structure Graphs

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=lattice-arma-structures-digital-filter-design.html language=enus -->
## TOPIC 00061: Lattice ARMA Structures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `lattice-arma-structures-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/lattice-arma-structures-digital-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For an Infinite Impulse Response (IIR) filter, you can implement one of the following section types of lattice Autoregressive-Moving Average (ARMA) filter structures: basic section type one multiplier section type normalized section type. The following figure represents the basic section type of a l

### Lattice ARMA Structures

For an Infinite Impulse Response (IIR) filter, you can implement one of the following
 section types of lattice Autoregressive-Moving Average (ARMA) filter structures:

- basic section type
- one multiplier section type
- normalized section type.

The following figure represents the basic section type of a lattice ARMA filter structure:

[IMAGE alt='image' src='GUID-F9AEDC4C-10AE-429E-95AD-CE4A8DE1046E-a5.gif']

The total number of the lattice reflection coefficients (k) is
 M, where M is the filter order. The total
 number of the lattice ladder coefficients v is
 M+1. The total number of multipliers is 3M+1.

The following figure represents the one multiplier section type of a lattice ARMA filter
 structure:

[IMAGE alt='image' src='GUID-7FF65FF2-FE0B-421B-B233-6BC6681556BE-a5.gif']

The total number of coefficients k and v is
 2M+1, which is the same as in the basic section type. However,
 the total number of multipliers is only 2M+1, which is less than the
 number of multipliers in the basic section type. Therefore, the one multiplier section
 type of a lattice ARMA structure involves fewer multipliers than other section types.
 Fewer multipliers require less hardware resources.

The following figure represents the normalized section type of a lattice ARMA filter
 structure:

[IMAGE alt='image' src='GUID-A467ABAD-7A16-429A-A0DA-F970EB72C666-a5.gif']

You can derive k' from k in the normalized section type by
 using the formula:

k

′

⁢

[

m

]

=

1

−

(

k

⁢

[

m

]

)

2

One advantage of the normalized section type structure is that this structure automatically scales the internal signals in each lattice section. Unfortunately, scaling the internal signals increases the implementation complexity.

Refer to the *Understanding Filter Structure Graphs* topic for information that helps
 you read and understand a filter structure graph.

Parent topic:

Select a Filter Structure

Related concepts:

- Filter Structure Graphs

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=lattice-ma-structures-digital-filter-design-t.html language=enus -->
## TOPIC 00062: Lattice MA Structures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `lattice-ma-structures-digital-filter-design-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/lattice-ma-structures-digital-filter-design-t.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For a minimum or maximum phase Finite Impulse Response (FIR) filter, you can implement a lattice Moving Average (MA) filter structure.The following figure represents the lattice MA filter structure for a minimum phase filter. M is the filter order: The following figure represents the lattice MA filt

### Lattice MA Structures

For a minimum or maximum phase Finite Impulse Response (FIR) filter, you can
 implement a lattice Moving Average (MA) filter structure.

The following figure represents the lattice MA filter structure for a minimum phase filter.
 M is the filter order:

[IMAGE alt='image' src='GUID-242B78FE-61A2-4ED7-8FDF-F187348A9419-a5.gif']

The following figure represents the lattice MA filter structure for a maximum phase filter:

[IMAGE alt='image' src='GUID-239ACD23-662E-4C80-9165-8B542302A4B3-a5.gif']

For both the minimum and maximum phase type, the total number of the lattice reflection
 coefficients (k) is M. The total
 number of multipliers is 2M.

Refer to the *Understanding Filter Structure Graphs* section for information that
 helps you read and understand a filter structure graph.

Parent topic:

Select a Filter Structure

Related concepts:

- Filter Structure Graphs

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=least-pth-norm-design-method-digital-filter-d.html language=enus -->
## TOPIC 00063: Least Pth Norm Design Method

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `least-pth-norm-design-method-digital-filter-d.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/least-pth-norm-design-method-digital-filter-d.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the DFD Least Pth Norm Design VI to design linear phase FIR filters, approximated linear phase IIR filters, and minimum/maximum phase IIR design filters.Although you can design linear phase filters using the DFD Remez Design VI, you can design FIR and IIR filters with arbitrary magnitude

### Least Pth Norm Design Method

You can use the DFD Least Pth Norm Design VI to design linear phase
 FIR filters, approximated linear phase IIR filters, and minimum/maximum phase IIR design
 filters.

Although you can design linear phase filters using the DFD Remez Design VI,
 you can design FIR and IIR filters with arbitrary magnitude and phase constraints using
 the DFD Least Pth Norm Design VI.

- [Least Pth Norm Linear Phase FIR Design](least-pth-norm-linear-phase-fir-design-digita.html)
- [Approximated Linear Phase IIR Design](approximated-linear-phase-iir-design-digital.html)
- [Minimum and Maximum Phase IIR Design](minimum-and-maximum-phase-iir-design-digital.html)

Parent topic:

Advanced Techniques for Designing Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=least-pth-norm-linear-phase-fir-design-digita.html language=enus -->
## TOPIC 00064: Least Pth Norm Linear Phase FIR Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `least-pth-norm-linear-phase-fir-design-digita.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/least-pth-norm-linear-phase-fir-design-digita.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can design a linear phase FIR filter using the DFD Least Pth Norm Design VI by setting the denominator order to 0, the filter type to Symmetric or Antisymmetric, all phases in the band specifications to 0, and the group delay to half of the numerator order.For example, suppose you want to design

### Least Pth Norm Linear Phase FIR Design

You can design a linear phase FIR filter using the DFD Least Pth Norm
 Design VI by setting the denominator order to 0, the
 filter type to Symmetric or
 Antisymmetric, all phases in the band specifications to
 0, and the group delay to half of the numerator order.

For example, suppose you want to design a linear phase FIR lowpass filter with a passband
 frequency range of [0, 0.2] and a stopband frequency range of
 [0.3, 0.5]. Set the specifications as shown in the following
 figure:

Figure 48.

[IMAGE alt='image' src='GUID-C22FCD84-D7D9-4118-A94E-31B9E5C543CB-a5.gif']

The following figure shows the magnitude response of the designed filter. Because
 p is 128, the designed filter is almost
 identical to the result using the Remez equi-ripple design with the same filter
 specification.

Figure 49.

[0,
 0.2]

[IMAGE alt='image' src='GUID-E840D7F8-B436-426C-901D-04648D9BF70B-a5.gif']

Parent topic:

Least Pth Norm Design Method

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=linear-phase-filters-digital-filter-design-to.html language=enus -->
## TOPIC 00065: Linear Phase Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `linear-phase-filters-digital-filter-design-to.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/linear-phase-filters-digital-filter-design-to.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Linear phase digital filters allow all the frequency components of an input signal to pass through the filter with the same delay, which means that the group delay through the filter is a constant value independent of the frequency. Linear phase filters are useful in filtering applications in which

### Linear Phase Filters

Linear phase digital filters allow all the frequency components of an input signal to
 pass through the filter with the same delay, which means that the group delay through
 the filter is a constant value independent of the frequency. Linear phase filters are
 useful in filtering applications in which you want to minimize signal distortion and
 spreading over time.

Nonlinear phase response, or dispersion, can be harmless in audio and other applications in which
 mild phase distortion is often imperceptible to humans. However, phase distortion can be
 harmful in some applications. For example, in digital communications applications,
 signal spreading caused by phase distortion can cause interference between time
 concentrated information symbols.

A minimum phase filter is a type of nonlinear phase filter that optimally minimizes the group delay at all frequencies for a given magnitude response at the expense of phase distortion. Minimum phase filters can be useful in control applications in which minimizing delay is more important than minimizing signal spreading.

#### Mathematical Definition

The
 digital filter frequency response H(f) is
 expressed in terms of magnitude and phase in the following equation:

H

(

f

)

=

|

H

(

f

)

|

e

j

φ

(

f

)

⁢

where |H(f)| and
 φ(f) are both real-valued functions of
 frequency f and represent the magnitude and phase of the
 frequency response.

Only Finite Impulse Response (FIR) filters can have
 exactly linear phase. You can design linear phase FIR filters using either
 window-based design methods or the Remez design method. The Remez design method in
 the DFD Remez Design VI is more powerful and flexible than
 window-based design methods.

The equation above reduces to the following
 equation for a linear phase FIR digital filter:

H

(

f

)

=

(

j

)

m

⁢

A

(

f

)

e

−

j

Π

N

f

⁢

where m= 0, or 1,
 A(f) is the amplitude response of the
 filter, N is the order of the filter, which is equal to the
 number of filter taps minus one, f is the normalized frequency
 with the range [0, 0.5], If the filter coefficients
 h(n) (where n = 0, 1,
 .., N) are symmetric, h(n)
 = h(N−n), and
 m must be 0, If the filter coefficients
 h(n) are antisymmetric,
 h(n) =
 −h(N−n), and
 m must be 1

#### Types of Linear Phase FIR
 Filters

The following table lists the four types of linear phase FIR
 filters and the characteristics of each type. The book *Digital Filter
 Design* contains more information about linear phase FIR filters.

| Type | Classification | Frequency Characteristics |
| --- | --- | --- |
| I | Even-order, symmetric | A(f) is symmetric about f = 0 and f = 0.5A(f) is periodic with period 1 |
| II | Odd-order, symmetric | A(f) is symmetric about f = 0 and antisymmetric about f = 0.5 A(f) is constrained to 0 at f = 0.5 A(f) is periodic with period 2 |
| III | Even-order, antisymmetric | A(f) is antisymmetric about f = 0 and f = 0.5 A(f) is constrained to 0 at both f = 0 and f = 0.5 A(f) is periodic with period 1 |
| IV | Odd-order, antisymmetric | A(f) is antisymmetric about f = 0 and symmetric about f = 0.5A(f) is constrained to 0 at f = 0A(f) is periodic with period 2 |

Use the DFD Remez Design VI to design linear phase FIR
 filters. Set the order input and the filter
 type input according to the Classification column of the table
 above. The DFD Remez Design VI designs the appropriate type of
 linear phase FIR filter based on the two inputs.

Use the following guidelines
 to determine the type of linear phase FIR filter you design:

- Type III and IV cannot be lowpass-like filters.
- Type II and III cannot be highpass-like filters.
- Type III and IV work well for differentiators or Hilbert transformers because
 they can give a constant 90° phase shift.

Experiment with different types. More than one type might produce an acceptable
 result for some target filter responses, but only one type can meet the target
 specifications. Select the filter type that has the smoothest frequency response.
 For example, the following figure illustrates the types of frequency response
 symmetry for each type of linear phase FIR filter, assuming a sampling frequency of
 f<sub>s</sub> = 1. Notice that in this
 example, a Type I or Type II filter has glitches, or rapid changes, at the frequency
 point of 1. A Type III or Type IV filter yields the smoothest frequency response
 because they do not contain glitches.

Figure 8.

[IMAGE alt='image' src='GUID-73A86E42-F102-4633-A799-46B9709B4A4E-a5.gif']

The following figure shows the magnitude response requirement of an
 ITU-468-weighting filter. Notice that the magnitude response is zero at DC and small
 but nonzero at high frequencies. Therefore, Type IV (odd order, antisymmetric) is
 the best choice for approximating this response.

Figure 9.

[IMAGE alt='image' src='GUID-87071829-605B-4641-A011-BF977D19789E-a5.gif']

Parent topic:

Design Special Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=lv-digital-filter-design-concepts-digital-filter.html language=enus -->
## TOPIC 00066: LabVIEW Digital Filter Design Concepts

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `lv-digital-filter-design-concepts-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/lv-digital-filter-design-concepts-digital-filter.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the LabVIEW Digital Filter Design Toolkit to design floating-point and fixed-point digital filters. You need fundamental knowledge about digital signal processing to understand the content in this user manual.You can use the Digital Filter Design Toolkit to design the following types of

### LabVIEW Digital Filter Design Concepts

You can use the LabVIEW Digital Filter Design Toolkit to design floating-point and
 fixed-point digital filters. You need fundamental knowledge about digital signal processing to
 understand the content in this user manual.

You can use the Digital Filter Design Toolkit to design the following types of filters:

Single-rate filters

Design Floating-Point Filters

Multirate filters

Design Multirate Filters

Filter Banks

Design Filter
 Banks

- [Digital Filter Design Basics](digital-filter-design-basics-digital-filter-d.html)
- [Design Floating-Point Filters](design-floating-point-filters-digital-filt.html)
- [Design Fixed-Point Filters](designing-fixed-point-filters-digital-filter.html)
- [Design Special Filters](design-special-filters-digital-filter-desi.html)
- [Design Multirate Filters](design-multirate-filters-digital-filter-de.html)
- [Designing Filter Banks](design-filter-banks-digital-filter-design.html)
- [Advanced Techniques for Designing Filters](advanced-techniques-for-designing-filters-dig.html)

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=lv-digital-filter-design-toolkit-features.html language=enus -->
## TOPIC 00067: LabVIEW Digital Filter Design Toolkit Features

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `lv-digital-filter-design-toolkit-features.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/lv-digital-filter-design-toolkit-features.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Digital Filter Design Toolkit includes a variety of tools to help you design digital filters including analysis tools, filter structures, filter designs, code generation, and design algorithms. For example, the Digital Filter Design Toolkit includes Express VIs that you can use to intera

### LabVIEW Digital Filter Design Toolkit
 Features

The LabVIEW Digital Filter Design Toolkit includes a variety of tools to help you design
 digital filters including analysis tools, filter structures, filter designs, code
 generation, and design algorithms.

For example, the Digital Filter Design Toolkit includes Express VIs that you
 can use to interact graphically with filter specifications to design appropriate digital
 filters. In addition to the tools that help you quickly create digital filters, the
 Digital Filter Design Toolkit includes tools for single-rate and multirate digital
 filter design, floating-point to fixed-point conversion, filter analysis, simulation on
 a desktop computer, and filter bank design and analysis.

The Digital Filter Design Toolkit also includes tools for designing, analyzing, simulating, and
 using adaptive filters for different applications and with different adaptive filter
 algorithms. The following sections describe the major features that the Digital Filter
 Design Toolkit provides.

#### Comprehensive Analysis
 Tools

You can use the Filter Analysis VIs to evaluate
 the characteristics of digital filters. You can examine the frequency response,
 group delay, phase delay, impulse response, step response, and pole-zero placement
 of a digital filter.

#### Large Selection of Filter
 Structures

When you design digital filters with the Digital Filter Design
 Toolkit, you can select from one of 23 possible filter structures, which range from
 the direct form and cascaded form structures to the lattice Auto-Regressive (AR),
 lattice Moving Average (MA), and lattice ARMA structures.

Filter structures
 are mathematically equivalent when you use floating-point computation. However,
 different structures can perform differently in fixed-point implementations and can
 lead to different computation complexity and memory usage in fixed-point or
 floating-point implementations. Selecting an appropriate filter structure is
 critical for digital filter design, especially for fixed-point digital filters in
 which the precision of the filter coefficients and filtering operations is more
 limited than for floating-point digital filters.

#### Multirate Digital Filter
 Design

The Multirate Filter Design VIs help you design,
 analyze, and implement the following filters:

- single-stage multirate filters
- multistage multirate filters
- halfband filters
- Nyquist filters
- raised cosine filters
- Cascaded Integrator Comb (CIC) filters

#### Special Digital Filter
 Design

The Special Filter Design VIs help you design
 IIR notch/peak filters, IIR comb filters, maximally flat filters, narrowband
 filters, and group delay compensators.

#### Adaptive Filter Design

The
 Adaptive Filters VIs help you create adaptive filters with
 different algorithms and to perform adaptive filtering on input signals. Adaptive
 filters extract meaningful signal features by adjusting filter coefficients
 automatically according to the dynamic conditions of the input signals and the
 environment.

#### Fixed-Point Filter Design and Code
 Generation

The Fixed-Point Tools VIs and
 Multirate Fixed-Point Tools VIs help you quantize, analyze,
 model, and simulate the fixed-point filter design, including single-rate and
 multirate filters. You can save the resulting fixed-point filter information as C
 code, which you then can implement on Digital Signal Processing (DSP) chips. You
 also can save the resulting fixed-point information as LabVIEW code, which you then
 can implement on NI Reconfigurable I/O (RIO) targets.

The
 Fixed-Point VIs help you simulate the behaviors of a
 fixed-point adaptive filter, save the fixed-point settings to an
 XML file, and load the fixed-point settings from an
 XML file. You also can generate LabVIEW FPGA code for the
 fixed-point adaptive filter so that you can implement the fixed-point adaptive
 filter on NI Reconfigurable I/O (RIO) targets.

#### Generalized Remez and Least Pth Norm Design Algorithms

You can use algorithms such as the generalized Remez method and the least pth norm method to specify an arbitrary magnitude and a phase response for a digital filter. The Digital Filter Design Toolkit includes automatic order-estimation VIs to assist you in estimating the filter order.

#### Filter Bank Design and
 Analysis

The Digital Filter Design Toolkit includes VIs that you can use
 to design and analyze filter banks. You can use the VIs to design a 2-band
 Quadrature Mirror Filter (QMF) or M-band cosine-modulated filter bank, analyze the
 characteristics of a filter bank, decompose or reconstruct signals with filter
 banks, retrieve filter bank parameters, and create a filter bank from a prototype
 filter.

Related concepts:

- Design Multirate Filters
- Designing Filter Banks
- Advanced Techniques for Designing Filters

Related tasks:

- Design Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=minimum-and-maximum-phase-fir-design-digital.html language=enus -->
## TOPIC 00068: Minimum and Maximum Phase FIR Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `minimum-and-maximum-phase-fir-design-digital.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/minimum-and-maximum-phase-fir-design-digital.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can specify minimum or maximum phase to eliminate ambiguity regarding the chosen set of FIR filter coefficients.The Designing Special Filters section discusses linear phase Finite Impulse Response (FIR) filter designs, which are actually amplitude approximations that use the following complex ap

### Minimum and Maximum Phase FIR Design

You can specify minimum or maximum phase to eliminate ambiguity regarding the chosen set
 of FIR filter coefficients.

The *Designing Special Filters* section discusses linear phase Finite Impulse Response
 (FIR) filter designs, which are actually amplitude approximations that use the following
 complex approximation criterion:

min

⁡

(

max

⁡

(

∑

i

=

0

L

−

1

(

W

(

i

)

⋅

|

H

(

ω

i

)

−

D

(

ω

i

)

|

)

)

)

where D(ω<sub>i</sub>) is the
 ideal frequency response,
 H(ω<sub>i</sub>) is the
 frequency response of the designed filter, and
 W(i) is the positive weight at the
 i<sup>th</sup> frequency point.

Many applications require linear phase to ensure that the frequency components of an
 input signal pass through the filter with the same delay. If you have an application
 that does not require linear phase, you can control the magnitude response of the filter
 and allow the filtering process to change the delay relationship between different
 frequency components arbitrarily. You can use the following expression for this type of
 magnitude approximation problem:

min

⁡

(

max

⁡

(

∑

i

=

0

L

−

1

(

W

(

i

)

⋅

|

H

(

ω

i

)

|

−

|

D

(

ω

i

)

|

)

)

)

Without the phase constraint, you can achieve the same approximation error magnitude with
 a lower filter order or a smaller approximation error magnitude with the same filter
 order. Both options reduce the implementation cost.

More than one set of filter coefficients can have the same magnitude response. In the
 z-plane you can create a new set of coefficients with the same
 magnitude response, unless all zeroes are on the unit circle, through the allpass
 transformation of flipping zeroes to their conjugate reciprocal locations relative to
 the unit circle. You can specify minimum phase or maximum phase to eliminate the
 ambiguity about which set of FIR filter coefficients you are using.

All zeroes in a minimum phase FIR filter are inside or on the unit circle. Minimum phase
 filters sometimes are called minimum energy delay filters because the energy of the
 impulse response is maximally concentrated toward the beginning of the impulse
 response.

All zeroes in a maximum phase FIR filter are outside or on the unit circle. The energy of
 the impulse response is maximally concentrated toward the end of the impulse response.
 Given a certain magnitude response, the impulse responses of the minimum and the maximum
 phase FIR filters are time-reversed.

The following figure shows the magnitude response of a 16<sup>th</sup> order FIR
 filter:

[IMAGE alt='image' src='GUID-CC541161-B42B-4AA9-A84B-635C4E1D279C-a5.gif']

You can use two different sets of filter coefficients to match the magnitude response of
 the FIR filter. The following figure shows the impulse response and zeroes of a minimum
 phase filter with the same magnitude response of the 16<sup>th</sup> order FIR
 filter:

[IMAGE alt='image' src='GUID-1F8DF357-7F03-4016-9493-49265BC16D71-a5.gif']

The following figure shows the impulse response and zeroes of a maximum phase filter with
 the same magnitude response of the 16<sup>th</sup> order FIR filter.

[IMAGE alt='image' src='GUID-4D227FD0-F393-454A-BD94-F7964C7A2C8B-a5.gif']

Minimum phase filters are especially useful in control applications. A filtering process
 in a control loop typically requires the response to an input stimulus to be as quick as
 possible. A large delay in the filtering process can cause a negative feedback control
 loop to become unstable.

One disadvantage of linear phase FIR filters is that the system delay, also called the
 group delay, is fixed to half the filter order, which might be unacceptably long when
 the filter order is large. Use minimum phase filters in situations where minimizing
 delay is critical unless the system requires a linear phase filter or the linear phase
 filter order is relatively small.

You can design minimum or maximum phase FIR filters using the DFD Remez Design
 VI. Set the filter type input to Minimum
 Phase or Maximum Phase and the remaining
 specifications just as you design a linear phase filter. Refer to the *Exact Gain
 Control Design* and *Ripple Constraint Design* sections for
 information about designing minimum and maximum phase filters with exact gain control or
 ripple constraints.

Note

Parent topic:

Remez Design Method

Related concepts:

- Design Special Filters
- Linear Phase Filters
- Ripple Constraint Design

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=minimum-and-maximum-phase-iir-design-digital.html language=enus -->
## TOPIC 00069: Minimum and Maximum Phase IIR Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `minimum-and-maximum-phase-iir-design-digital.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/minimum-and-maximum-phase-iir-design-digital.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Minimum Phase or Maximum Phase option of the filter type input if you want a minimum or maximum phase response or if the phase response is not important.When you use the Minimum Phase or Maximum Phase option, the DFD Least Pth Norm Design VI ignores the phase and group delay inputs.For examp

### Minimum and Maximum Phase IIR Design

Use the Minimum Phase or Maximum Phase option of the
 filter type input if you want a minimum or maximum phase
 response or if the phase response is not important.

When you use the Minimum Phase or Maximum Phase option, the
 DFD Least Pth Norm Design VI ignores the
 phase and group delay inputs.

For example, suppose you want to design a minimum phase IIR lowpass filter with a passband
 frequency range of [0, 0.2] and a stopband frequency range of
 [0.3, 0.5]. You can set the specifications as shown in the
 following figure:

Figure 53.

[IMAGE alt='image' src='GUID-5B00E7FD-7B51-4F2E-A18F-6D21ADEAE486-a5.gif']

The following figure shows the magnitude response of the designed filter:

Figure 54.

[IMAGE alt='image' src='GUID-80DE2432-25FF-4322-92DA-429A77A8C2CC-a5.gif']

The following figure shows the phase response of the designed filter:

Figure 55.

[IMAGE alt='image' src='GUID-94E116A2-93EF-4B25-AA2E-44217150568B-a5.gif']

Notice that the designed filter has greater stopband attenuation than the approximately linear phase IIR filter designed, but the passband phase response is now highly nonlinear.

Parent topic:

Least Pth Norm Design Method

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=multirate-filter-basics-digital-filter-design.html language=enus -->
## TOPIC 00070: Multirate Filter Basics

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `multirate-filter-basics-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/multirate-filter-basics-digital-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multirate filters can be used in digital signal processing systems when different sampling frequencies exist in different parts of a system, or when reduction of computational complexity in systems becomes necessary by using a uniform sampling frequency.The sampling frequency of a filter by using de

### Multirate Filter Basics

Multirate filters can be used in digital signal processing systems when different
 sampling frequencies exist in different parts of a system, or when reduction of
 computational complexity in systems becomes necessary by using a uniform sampling
 frequency.

The sampling frequency of a filter by using decimation, interpolation, or rational resampling can
 be changed. This section describes the three filtering modes and the zero-phase
 filtering mode, which enables you to eliminate the delay between the input and output
 signals.

Use Finite Impulse Response (FIR) structures to implement multirate filters. Compared to Infinite
 Impulse Response (IIR) structures, FIR structures provide unconditional stability, phase
 linearity, and better finite-precision performance. Furthermore, FIR structures contain
 only feedforward signal paths that enable you to simplify the implementation of
 decimation and interpolation filters. In principle, you can use both lowpass and
 highpass FIR filters to implement multirate filters. However, the LabVIEW Digital Filter
 Design Toolkit provides lowpass multirate FIR filters only.

- [Rational Resampling](rational-resampling-digital-filter-design-too.html)
- [Decimation](decimation-digital-filter-design-toolkit.html)
- [Interpolation](interpolation-digital-filter-design-toolkit.html)
- [Zero-Phase Filtering](zero-phase-filtering-digital-filter-design-to.html)

Parent topic:

Design Multirate Filters

Related concepts:

- FIR Structures

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=multistage-multirate-filters-digital-filter-d.html language=enus -->
## TOPIC 00071: Multistage Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `multistage-multirate-filters-digital-filter-d.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/multistage-multirate-filters-digital-filter-d.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multistage filtering, with gradual frequency adjustments, is more efficient than single-stage filtering, because it employs multiple resampling stages, each with a lower decimation/interpolation factor, reducing computation and memory usage, especially when the conversion factor isn't a prime number

### Multistage Multirate Filters

Multistage filtering, with gradual frequency adjustments, is more efficient than
 single-stage filtering, because it employs multiple resampling stages, each with a lower
 decimation/interpolation factor, reducing computation and memory usage, especially when
 the conversion factor isn't a prime number.

The filters you design in the Designing Floating-Point Multirate Filters and the Designing
 Fixed-Point Multirate Filters sections are single-stage multirate filters. In
 single-stage multirate filters, the normalized transition bandwidth of the lowpass FIR
 filter H(z) is inversely related to the filter
 order. The narrower the normalized transition bandwidth, the higher the filter order. A
 lowpass FIR filter with a narrow normalized transition bandwidth therefore requires more
 resources to implement.

In decimation and interpolation multirate filters, the normalized transition bandwidth inversely
 relates to the decimation factor M and the interpolation factor
 L. The order of a decimation or interpolation filter increases as
 M or L increases, and the resulting multirate
 filter uses more resources to implement. You can use multistage multirate filters to
 simplify multirate filters that have large sampling frequency conversion factors.

A multistage filter gradually increases or decreases the sampling frequency by passing the signal
 through two or more resampling stages. Each stage has a lower decimation or
 interpolation factor than the corresponding single-stage multirate filter and contains
 fewer operations. Except when the sampling frequency conversion factor is a prime
 number, multistage filtering is more efficient than single-stage filtering because you
 can change the sampling frequency in multiple stages rather than in a single stage.
 Using multiple stages reduces the computation operations and memory usage. Refer to the
 *Multirate Systems and Filter Banks* section for more information about
 multistage multirate filter design.

In a multistage decimation system, the overall decimation factor M is equal to
 M<sub>1</sub>M<sub>2</sub>...M<sub>N</sub>,
 where M<sub>i</sub> is the decimation factor of
 stage i. The following figure illustrates this
 N-stage decimation process:

Figure 30.

[IMAGE alt='image' src='GUID-0401B44A-061E-48F6-A505-A05766DCA214-a5.gif']

In a multistage interpolation system, the overall interpolation factor L is
 equal to
 L<sub>1</sub>L<sub>2</sub>...L<sub>N</sub>,
 where L<sub>i</sub> is the interpolation factor of
 stage i. The following figure illustrates the
 N-stage interpolation process:

Figure 31.

[IMAGE alt='image' src='GUID-AD37963A-3275-434D-A90C-02145B15621B-a5.gif']

You can use the DFD NStage MRate Filter Design VI to design multistage
 multirate filters with either of the following approaches:

- Specify the overall sampling frequency change factor and the factors for every stage.
- Specify only the overall sampling frequency change factor and use the DFD NStage MRate
 Filter Design VI to determine the factors for every stage.

Use the following guidelines when you manually specify factorizations:

- Use two or three stages for optimal or near optimal results.
- Use the largest factor at the highest sampling frequency. Decimate in order from the largest to the smallest factor and interpolate in order from the smallest to the largest factor.

When you implement a fixed-point multistage multirate filter, the output signal word length of
 the previous filter stage must be the same as the input signal word length of the next
 filter stage.

Parent topic:

Design Special Multirate Filters

Related concepts:

- Design Floating-Point Multirate Filters
- Design Fixed-Point Multirate Filters
- Specify the Word Length and Integer Word Length

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=narrowband-fir-filters-digital-filter-design.html language=enus -->
## TOPIC 00072: Narrowband FIR Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `narrowband-fir-filters-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/narrowband-fir-filters-digital-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Conventional FIR filters with narrow transition bands and high orders might be too complex to implement. In this case, designing narrowband filters using Infinite Impulse Response (IIR) filters should be considered.The order of a Finite Impulse Response (FIR) filter is related inversely to the trans

### Narrowband FIR Filters

Conventional FIR filters with narrow transition bands and high orders might be too
 complex to implement. In this case, designing narrowband filters using Infinite Impulse
 Response (IIR) filters should be considered.

The order of a Finite Impulse Response (FIR) filter is related inversely to the transition
 bandwidth. However, narrowband IIR filters typically have nonlinear phase, especially
 near the transition band, and are numerically sensitive. You might be able to meet the
 target filter specifications by using narrowband FIR filters instead of using IIR
 filters.

The DFD Narrowband Filter Design VI uses Interpolated FIR (IFIR) techniques
 and frequency response masking techniques to design narrowband FIR filters with
 significantly less computational complexity than conventional FIR solutions, as shown in
 the following figure:

[IMAGE alt='image' src='GUID-CF1EEAB7-AC22-4C25-A3CC-E762FAFC5A5B-a5.gif']

(a)

H

z

(b)

G

z

(c)

G

z

N

(d)

I

z

To better understand how these techniques work, assume that the target narrowband filter has the frequency response shown in part (a) of the previous figure. The first step is to design a shaping filter as shown in part (b). The shaping filter has a wider transition band than the target narrowband filter and determines the spectrum shape of the target narrowband filter. The next step is to design an interpolated filter with the frequency response shown in part (c). Notice that the coefficients of the interpolated filter G(z<sup>N</sup>) are constructed by inserting N−1 zeroes between every two adjacent coefficients of G(z). The magnitude response of the first image of G(z<sup>N</sup>) in part (c) is the same as that of the target filter H(z) in part (a). To remove the unwanted images of G(z<sup>N</sup>), you need to cascade the interpolated filter G(z<sup>N</sup>) with a masking filter I(z), which has the magnitude response shown in part (d).

By cascading the interpolated filter G(z<sup>N</sup>) and the masking filter I(z) as illustrated in the following figure, you can obtain the target narrowband filter H(z).

Figure 12.

[IMAGE alt='image' src='GUID-E9F8068B-457E-4EF5-89E8-92DD9E81991F-a5.gif']

This figure shows a two-stage narrowband filter structure. Because I(z) and G(z) have a much wider transition band than the original filter H(z), the overall order of I(z) and G(z) is lower than the order of H(z), which makes the cascaded filters computationally efficient.

Similarly, if the lowpass masking filter I(z) also is a
 narrowband filter, you can make it more efficient by using the two-stage narrowband
 filter structure. The following figure illustrates the diagram of the resulting
 three-stage structure. This figure uses a Cascaded Integrator Comb (CIC) filter as the
 first-stage lowpass masking filter in this case because of the lowpass nature and
 efficient implementation.

Figure 13.

[IMAGE alt='image' src='GUID-21137E20-1DA9-4388-8A3B-439CA68C5708-a5.gif']

Assume a signal with a sampling frequency of 5 kHz. The signal has useful information at
 frequencies below 100 Hz and noise above 120 Hz. To suppress the noise, you can apply a
 narrowband lowpass filter with the following specifications:

| Specification | Value |
| --- | --- |
| Passband Range | 0−100 Hz |
| Passband Ripple | 0.05 dB |
| Stopband Range | 120−2500 Hz |
| Stopband Attenuation | 60 dB |

If you design the lowpass FIR filter using the DFD Remez Design VI,
 the resulting filter has 689 taps. Given the same specifications, the
 DFD Narrowband Filter Design VI generates a three-stage
 narrowband filter. The resulting CIC filter has 5 stages, the interpolated filter
 F(z<sup>M</sup>) has 18
 nonzero coefficients and the interpolated filter
 G(z<sup>N</sup>) has 27
 nonzero coefficients. The CIC narrowband filter is 78% less computationally complex than
 the lowpass FIR filter you design using the DFD Remez Design VI. The
 following figure shows the magnitude response of the designed narrowband filter:

[IMAGE alt='image' src='GUID-FB1A194C-7E56-4F26-86FE-97B9724D2C11-a5.gif']

To plot the frequency response of narrowband FIR filters, use the DFD Plot Narrowband
 Freq Response VI. To perform narrowband filtering, use the DFD
 Narrowband Filtering VI.

Parent topic:

Design Special Filters

Related concepts:

- FIR and IIR Filters
- Cascaded Integrator Comb Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00073: LabVIEW Digital Filter Design Toolkit New Features and Changes

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of LabVIEW Digital Filter Design Toolkit. Discover what is new in the latest releases of LabVIEW Digital Filter Design Toolkit.If you cannot find new features and changes for your version, it might not inclu

### LabVIEW Digital Filter Design
 Toolkit
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of LabVIEW Digital Filter Design
 Toolkit.

LabVIEW Digital Filter Design
 Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW Digital Filter Design Toolkit 2021
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Digital Filter
 Design Toolkit 2021.

- LabVIEW Digital Filter Design Toolkit no longer supports Windows Vista/XP/7/8.x,
 Windows Server 2003/2008/2012, or any 32-bit Windows operating system.
  - Versions of this product that ship after May 1, 2021 may not install or execute
 correctly on these operating systems. For information about operating systems that
 NI supports, visit NI Support for Windows 7, Windows 8.1, Windows Server 2008
 R2, Windows Server 2012 R2, and All 32-Bit Windows .

Related information:

- NI Support for Windows 7, Windows 8.1, Windows Server 2008 R2,
 Windows Server 2012 R2, and All 32-Bit Windows

#### LabVIEW Digital Filter Design Toolkit 2018
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Digital Filter
 Design Toolkit 2018.

- The LabVIEW Digital Filter Design Toolkit 2018 adds support for LabVIEW 2018
 (64-bit).

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=notch-and-peak-filters-digital-filter-design.html language=enus -->
## TOPIC 00074: Notch and Peak Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `notch-and-peak-filters-digital-filter-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/notch-and-peak-filters-digital-filter-design.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use notch filters to suppress noise at a specified frequency, such as an AC powerline frequency. Use peak filters to enhance the signal at a particular frequency.The following figure shows a typical notch filter: In a notch filter, f[0] denotes the center frequency and Δf denotes the frequency bandw

### Notch and Peak Filters

Use notch filters to suppress noise at a specified frequency, such as an AC powerline
 frequency. Use peak filters to enhance the signal at a particular frequency.

The following figure shows a typical notch filter:

[IMAGE alt='image' src='GUID-504CD50F-C6D7-4D0B-B5B0-24955428BEAF-a5.gif']

In a notch filter, f<sub>0</sub> denotes the center frequency and
 Δf denotes the frequency bandwidth at
 A<sub>b</sub>. The default value of
 A<sub>b</sub> is −3 dB. Q
 = f<sub>0</sub>/Δf, which denotes the sharpness of
 the notch. Increasing the value of Q results in a sharper notch
 filter.

The following figure shows a typical peak filter:

[IMAGE alt='image' src='GUID-13DD611F-85F1-454F-940D-D740457BD1BD-a5.gif']

In a peak filter, Q denotes the sharpness of the peak. Increasing the
 value of Q results in a sharper peak filter.

The DFD IIR Notch Peak Design VI designs a second-order Infinite Impulse
 Response (IIR) notch or peak filter using a bilinear transform method. The following
 equation shows the transfer function of a notch filter:

H

⁢

(

z

)

=

b

o

⁢

(

1

+

b

1

b

0

z

−

1

⁢

+

z

−

2

)

1

+

a

0

z

−

1

+

a

1

z

−

2

The following equation shows the transfer function of a peak filter:

H

(

z

)

=

b

0

⁢

(

1

+

z

−

2

)

1

+

a

0

z

−

1

⁢

+

a

1

⁢

z

−

2

where a<sub>0</sub>, a<sub>1</sub>,
 b<sub>0</sub>, and b<sub>1</sub> are filter
 coefficients.

For example, assume a time waveform of a noisy Electrocardiogram (ECG) signal sampled at 333 Hz,
 as shown in the following figure:

[IMAGE alt='image' src='GUID-97F44745-7AD2-4FE7-8BFF-08113C2BA466-a5.gif']

The following figure shows the spectrum of the same noisy signal. In this figure, you can
 identify the noise at 60 Hz:

[IMAGE alt='image' src='GUID-61D68C62-4F1B-4778-9A17-4837D1291FA2-a5.gif']

To remove the noise at 60 Hz, you can design a notch filter using the DFD IIR Notch Peak
 Design VI with the following specifications:

| DFD IIR Notch Peak Design VI Inputs | Value |
| --- | --- |
| filter type | Notch |
| f0 [Hz] | 60 |
| Q factor | 40 |
| fs [Hz] | 333 |

The following figure shows the magnitude response of the resulting notch filter:

[IMAGE alt='image' src='GUID-D0AC60F9-9668-4EEA-87CC-E896A9804857-a5.gif']

The following figure shows that the filtered ECG signal is close to the original
 noise-free samples:

[IMAGE alt='image' src='GUID-CEECA36D-BE6D-40AA-8F9F-1681BFF75CEA-a5.gif']

Parent topic:

Design Special Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=nyquist-filters-di.html language=enus -->
## TOPIC 00075: Design Nyquist Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `nyquist-filters-di.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/nyquist-filters-di.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Nyquist filters, also called M^th band filters, are a special type of multirate Finite Impulse Response (FIR) filter. Nyquist filter coefficients have periodic zero values every M^th sample, except for the middle coefficient.Nyquist filters have the following magnitude response specifications:8 Magn

### Design Nyquist Filters

Nyquist filters, also called M<sup>th</sup> band filters, are a
 special type of multirate Finite Impulse Response (FIR) filter. Nyquist filter
 coefficients have periodic zero values every M<sup>th</sup> sample,
 except for the middle coefficient.

Nyquist filters have the following magnitude response specifications:

| Filter Specification | Value Range |
| --- | --- |
| Passband edge frequency | [0, fs/2M−ε] |
| Stopband edge frequency | [fs/2M+ε, fs/2] |

In this table, M denotes the sampling frequency conversion factor and
 f<sub>s</sub> denotes the sampling frequency
 of a Nyquist filter. For an interpolation Nyquist filter,
 f<sub>s</sub> equals L
 times the sampling frequency of the input signal, where L denotes the
 interpolation factor. For a decimation Nyquist filter,
 f<sub>s</sub> equals the sampling
 frequency of the input signal. You can specify ε indirectly by using
 the roll off α, which is defined as the following equation:

α

⁢

=

ϵ

f

s

/

2

M

The following figure illustrates the magnitude response of a Nyquist filter:

Figure 28.

[IMAGE alt='image' src='GUID-AB68D61C-CF89-4197-8B21-CA12E3067BFC-a5.gif']

The following figure shows the
 coefficients of a Nyquist filter with a sampling frequency conversion factor of 4.
 The 26<sup>th</sup> coefficient is the middle coefficient and does not have a zero
 value.

Figure 29.

[IMAGE alt='image' src='GUID-DAC7C50B-26CC-4BBD-96E8-D65FAF3A4C65-a5.gif']

The impulse response of a Nyquist filter
 h(n) satisfies the following equation:

h

⁢

(

M

⁢

n

⁢

+

k

)

=

{

c

0

⁢

n

=

0

o

t

h

e

r

where c and k are constants.

The
 z-transform of a Nyquist filter
 H(z) satisfies the following equation:

∑

k

=

0

M

−

1

H

⁢

(

z

W

k

)

⁢

=

M

c

⁢

=

1

where W =
 e<sup>−</sup><sup>j</sup><sup>2</sup><sup>π</sup><sup>/</sup><sup>M</sup>
 and c = 1/M. The frequency response of
 H(zW<sup>k</sup>) is
 the shifted version of the frequency response of
 H(z), so the frequency responses of all
 M uniformly shifted versions of
 H(z) add up to a constant.

Use the
 DFD Nyquist Design VI to design Nyquist filters. You can use
 Nyquist filters to remove images in interpolation. Nyquist filters modify the
 interpolated zeroes, but they do not change the original samples.

Parent topic:

Design Special Multirate Filters

Related concepts:

- Decimation
- Interpolation

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=overview.html language=enus -->
## TOPIC 00076: LabVIEW Digital Filter Design Toolkit Overview

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/overview.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual contains information about the general design process and the tools in the Digital Filter Design Toolkit that you can use in a digital filter or filter bank design. This user manual also contains information about the general process and the tools in the Digital Filter Design Toolki

### LabVIEW Digital Filter Design
 Toolkit
 Overview

Note

You can use the Signal Processing VIs in the LabVIEW Full or
 Professional Development System to perform the following tasks:

- waveform measurements
- waveform conditioning
- waveform monitoring
- waveform generation
- signal processing
- point-by-point analysis

The Signal Processing VIs contain some digital filter design VIs
 similar to VIs in the Digital Filter Design Toolkit. For example, the
 Butterworth Coefficients VI is similar to the DFD
 Butterworth Design VI and the Parks-McClellan VI is
 similar to the DFD Remez Design VI. However, the Digital
 Filter Design VIs provide more capabilities, such as support for arbitrary
 phase and magnitude specifications and fixed-point filter design.

Although the VIs have similar functionality, the results you get might be different
 because the design algorithms are different. For information about working with the
 Signal Processing VIs and the Digital Filter
 Design VIs refer to the manufacturer's web site at *ni.com*

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=poles-zeroes-and-pole-zero-plots-digital-filt.html language=enus -->
## TOPIC 00077: Poles, Zeroes, and Pole-Zero Plots

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `poles-zeroes-and-pole-zero-plots-digital-filt.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/poles-zeroes-and-pole-zero-plots-digital-filt.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section covers the equations for a z-transform of FIR and IIR filters in addition to the relationship between the pole-zero plot and frequency response.The z-transform of a Finite Impulse Response (FIR) filter is defined as follows: H ( z )   =   ∑ k = 0 N b k z − k ⁢ =   G a i n ⁢   ⋅ ∏ k = 1

### Poles, Zeroes, and Pole-Zero Plots

This section covers the equations for a z-transform of FIR and IIR filters in addition to
 the relationship between the pole-zero plot and frequency response.

The z-transform of a Finite Impulse Response (FIR) filter is defined as
 follows:

H
 (
 z
 )
 
 =
 
 ∑
 k
 =
 0
 N
 b
 k
 z
 −
 k
 ⁢
 =
 
 G
 a
 i
 n
 ⁢
 
 ⋅
 ∏
 k
 =
 1
 N
 (
 1
 −
 z
 k
 z
 −
 1
 )

where

- z
 ⁢
 
 ≡
 e
 j
 2
 Π
 f
 ,
 b
 k is the set of filter coefficients
- N is the order of the FIR filter
- z k represents the roots of the
 polynomial H ( z )

H(z<sub>k</sub>) = 0 for all
 z<sub>k</sub>, so
 z<sub>k</sub> represents the zeroes of the
 filter H(z). The number of zeroes in a filter must
 equal the filter order N.

Similarly, the z-transform of an Infinite Impulse Response (IIR) filter is
 defined by the following equation:

H
 (
 z
 )
 
 =
 
 ∑
 k
 =
 0
 N
 b
 k
 z
 −
 k
 1
 +
 ∑
 i
 =
 1
 M
 a
 i
 z
 −
 i
 ⁢
 =
 
 G
 a
 i
 n
 ⁢
 
 ⋅
 ∏
 k
 =
 1
 N
 (
 1
 −
 z
 k
 z
 −
 1
 )
 ∏
 k
 =
 1
 M
 (
 1
 −
 p
 k
 z
 −
 1
 )

where

- z k represents the roots of the
 numerator polynomial
- p f k represents the roots of the
 denominator polynomial
- p k represents the poles of an IIR
 filter H ( z )

IIR filters have poles and zeroes, and FIR filters have only zeroes.

#### Pole-Zero Plots

From a
 mathematical point of view, the pole-zero plot and frequency response provide the
 same information. Based on the frequency response, you can obtain a pole-zero plot.
 Conversely, from the pole-zero plot, you can compute the frequency
 response.

The following figure illustrates a pole-zero plot for a particular
 IIR filter. The half-circle corresponds to |z| = 1, or the unit
 circle. The small circles along the half-circle represent zeroes. Each
 × represents a pole.

Figure 6.

[IMAGE alt='image' src='GUID-7FBD09EE-A716-4906-A4E5-3B459AA917D3-a5.gif']

The pole-zero plot and frequency response characterize digital filters from the
 following perspectives:

- You can determine if a digital filter is stable by determining if the output of
 the digital filter is bounded for all possible bounded inputs. The necessary and
 sufficient condition for IIR filters to be stable is that all poles are inside
 the unit circle. In contrast, FIR filters are always stable because the FIR
 filters do not have poles.
- You can determine if pole-zero pairs are close enough to cancel out each other
 effectively. Try deleting close pairs and then check the resulting frequency
 response. Fewer pole-zero pairs means fewer computations.

Parent topic:

Digital Filter Design Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=postprocessing-filtered-signals-digital-filte.html language=enus -->
## TOPIC 00078: Postprocess Filtered Signals

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `postprocessing-filtered-signals-digital-filte.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/postprocessing-filtered-signals-digital-filte.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you deploy fixed-point filter coefficients to the target hardware, the output data uses a fixed-point representation. To convert the output signal of the fixed-point filter into floating-point representation, you must process the fixed-point signal using the DFD FXP Postprocessing VI.

### Postprocess Filtered Signals

After you deploy fixed-point filter coefficients to the target hardware, the output data
 uses a fixed-point representation. To convert the output signal of the fixed-point
 filter into floating-point representation, you must process the fixed-point signal using
 the DFD FXP Postprocessing VI.

Parent topic:

Generate Code from Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=quantize-floating-point-multirate-filters.html language=enus -->
## TOPIC 00079: Quantize Floating-Point Multirate Filter

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `quantize-floating-point-multirate-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/quantize-floating-point-multirate-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Depending on which VI is used to quantize the coefficients of a floating-point single-rate filter, the configuration of some or all of the following items might be required: the gain settings, word length and integer word length, overflow mode, and rounding mode.Use the DFD FXP MRate Quantization VI

### Quantize Floating-Point Multirate
 Filter

Depending on which VI is used to quantize the coefficients of a floating-point
 single-rate filter, the configuration of some or all of the following items might be
 required: the gain settings, word length and integer word length, overflow mode, and
 rounding mode.

Use the DFD FXP MRate Quantization VI to quantize floating-point multirate
 filters. This process is different from quantizing floating-point single-rate
 filters.

In the fixed-point single-rate filter design process, scaling the filter coefficients is a
 separate step. However, the fixed-point multirate filter design process integrates this
 step in the quantization process. Specify an appropriate value in the scale
 type input of the DFD FXP MRate Quantization VI to
 scale the multirate filter coefficients.

To quantize the coefficients of a floating-point multirate filter, you only need to set the gain
 processing target and coefficients word length. The DFD FXP MRate
 Quantization VI automatically calculates the integer word length of the
 filter coefficients and configures the settings for the overflow and rounding modes. The
 VI then uses the resulting values to quantize the filter coefficients.

Parent topic:

Design Fixed-Point Multirate Filters

Related concepts:

- Select a Filter Structure
- Scale the Filter Coefficients
- Specify the Word Length and Integer Word Length
- Handle Overflows and Underflows

Related tasks:

- Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=quantize-multirate-filter-coefficients.html language=enus -->
## TOPIC 00080: Quantize Multirate Filter Coefficients

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `quantize-multirate-filter-coefficients.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/quantize-multirate-filter-coefficients.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Following the analysis of the filter design, the filter coefficients of the multirate filter may be quantized to convert it from floating-point to fixed-point representation. Alternatively, the floating-point multirate filter may be used to process the input signal. To quantize the filter coefficien

### Quantize Multirate Filter Coefficients

Following the analysis of the filter design, the filter coefficients of the
 multirate filter may be quantized to convert it from floating-point to
 fixed-point representation. Alternatively, the floating-point multirate
 filter may be used to process the input signal.

To quantize the filter coefficients, place a checkmark in the Quantize
 filter checkbox on the Fixed-Point Quantization
 tab, and specify the coefficients word length, coefficients scale type, and gain
 settings.

Parent topic:

Design Floating-Point Multirate Filters

Related concepts:

- Scale the Filter Coefficients
- Specify the Word Length and Integer Word Length

Related tasks:

- Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=quantizing-floating-point-filters-digital-fil.html language=enus -->
## TOPIC 00081: Quantize Floating-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `quantizing-floating-point-filters-digital-fil.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/quantizing-floating-point-filters-digital-fil.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: After selecting a filter structure, you must quantize the coefficients of the reference floating-point filter. Quantizing the filter coefficients is the process of approximating each floating-point value with a fixed-point value that you use in a fixed-point mathematical computation or hardware impl

### Quantize Floating-Point Filters

After selecting a filter structure, you must quantize the
 coefficients of the reference floating-point filter. Quantizing the filter coefficients
 is the process of approximating each floating-point value with a fixed-point value that
 you use in a fixed-point mathematical computation or hardware implementation.

DFD FXP Quantize Coef

Q

C

- If you use the Easy instance of the DFD FXP Quantize
 Coef VI to quantize the filter coefficients, you must do the
 following steps:
  1. Specify appropriate word length values for coefficients
 a/k word length and coefficients b/v word
 length .
  2. Specify the appropriate gain processing target.
  3. Specify the appropriate gain word length value. This VI
 automatically calculates the integer word lengths for coefficients
 a / k , coefficients
 b / v , and gain. The VI then
 uses the resulting values to quantize the filter coefficients.
- If you use the Advanced instance of the
 DFD FXP Quantize Coef VI to quantize the filter
 coefficients, you must complete the following steps:
  1. Configure the coefficients a/k quantizer and coefficients b/v
 quantizer.
  2. Specify the appropriate gain processing target.
  3. Specify the appropriate gain word length value. This VI then
 automatically calculates the integer word length of gain and uses
 the resulting value to quantize the gain if you set the
 gain processing input to On
 Target .

Parent topic:

Design Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=rational-resampling-digital-filter-design-too.html language=enus -->
## TOPIC 00082: Rational Resampling

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `rational-resampling-digital-filter-design-too.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/rational-resampling-digital-filter-design-too.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Rational resampling (also known as fractional sampling) is the process of converting the sampling frequency of a signal to another sampling frequency that differs from the original frequency by a rational factor of L/M, where both L and M are integer values.Rational resampling is useful for interfac

### Rational Resampling

Rational resampling (also known as fractional sampling) is the process of converting the
 sampling frequency of a signal to another sampling frequency that differs from the
 original frequency by a rational factor of L/M,
 where both L and M are integer values.

L

M

L

M

Note

M

L

You can implement a rational resampling system by cascading an L−fold expander
 with an M−fold decimator. You must place the expander before the
 decimator to avoid discarding useful frequency components in the decimation operation.
 The following figure shows a rational resampling filter with a rational factor of
 L/M.

Figure 14.

[IMAGE alt='image' src='GUID-1C6CDEDF-8FAC-4719-ACA3-10F741959DD1-a5.gif']

This rational resampling filter first interpolates the input signal
 x(n) with an L−fold
 expander and changes the sampling frequency of the original signal
 f<sub>s</sub> to a new sampling frequency
 Lf<sub>s</sub>. The expander returns an output
 signal v(n) with this new sampling frequency. Both
 the interpolation filter following the expander and the decimation filter preceding the
 decimator are lowpass FIR filters, and the two filters operate at the same sampling
 frequency Lf<sub>s</sub>. Therefore, you can
 integrate the two filters into one lowpass filter
 H(z) and place the filter between the expander
 and the decimator. The filter H(z) returns a new
 signal w(n). This rational resampling filter then
 decimates the signal w(n) with an
 M−fold decimator and changes the sampling frequency from
 Lf<sub>s</sub> to
 (L/M)f<sub>s</sub>.
 The decimator returns an output signal y(n) with
 this new sampling frequency.

L

M

H

z

L

M

H

z

H

z

f

s

Lf

s

M

Note

Multirate
 Processing

Multirate Systems and Filter Banks

The following figure illustrates the rational resampling of a signal by a factor of 2/3.

Figure 15.

[IMAGE alt='image' src='GUID-D9F3B0BD-DF3C-47F9-9258-E141B813CC07-a5.gif']

(a)

x

n

(b)

v

n

(c)

H

z

(d)

w

n

H

z

(e)

y

n

(f)

y

n

The different parts in the figure correspond to the different spectra of the signal at
 different stages of the rational resampling process, as shown in the previous figure.
 Because L<M, the lowpass filter has a cutoff
 frequency of
 Lf<sub>s</sub>/(2M) and acts as
 an anti-aliasing filter. Part (e) of this figure shows the spectrum of the output signal
 if you use a lowpass filter. You can see that no aliasing occurs. From part (f) of this
 figure, you can see that if no lowpass filter exists, or if you choose the cutoff
 frequency of the lowpass filter to be
 f<sub>s</sub>/2, aliasing occurs between each
 spectrum image of the decimated signal. The overlapping spectra indicate aliasing due to
 the decimation operation.

To design rational resampling filters, use the Rational instance of the
 DFD MRate Filter Design VI.

Parent topic:

Multirate Filter Basics

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=remez-design-method-digital-filter-design-too.html language=enus -->
## TOPIC 00083: Remez Design Method

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `remez-design-method-digital-filter-design-too.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/remez-design-method-digital-filter-design-too.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Remez algorithm generates Finite Impulse Response (FIR) filters that minimize the maximum error between the target frequency response and the designed filter frequency response. This error specification yields filters with equi-ripple or Chebyshev error behavior.Several Digital Filter Design VIs

### Remez Design Method

The Remez algorithm generates Finite Impulse Response (FIR) filters that minimize the
 maximum error between the target frequency response and the designed filter frequency
 response. This error specification yields filters with equi-ripple or Chebyshev error
 behavior.

Several Digital Filter Design VIs use the Remez algorithm. The DFD
 Remez Design VI extends the application of the Remez algorithm to include
 the following advanced and specialized digital filter designs.

- [Minimum and Maximum Phase FIR Design](minimum-and-maximum-phase-fir-design-digital.html)
- [Single-Point Band Design](single-point-band-design-digital-filter-desig.html)
- [Exact Gain Control Design](exact-gain-control-design-digital-filter-desi.html)
- [Ripple Constraint Design](ripple-constraint-design-digital-filter-desig.html)

Parent topic:

Advanced Techniques for Designing Filters

Related concepts:

- Design Special Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=resolving-lv-fpga-code-failures.html language=enus -->
## TOPIC 00084: Resolving LabVIEW FPGA Code Compilation Failures

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `resolving-lv-fpga-code-failures.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/resolving-lv-fpga-code-failures.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Sometimes the LabVIEW FPGA code might not compile successfully.One potential cause of a compilation failure is that the computation resources on the FPGA target might not meet the requirements of the fixed-point filter. For example, the PXI-7831R has 40 built-in 18x18 multipliers. Therefore, you can

### Resolving LabVIEW FPGA Code Compilation
 Failures

Sometimes the LabVIEW FPGA code might not
 compile successfully.

One potential cause of a compilation failure is that the
 computation resources on the FPGA target might not meet the requirements of the
 fixed-point filter. For example, the PXI-7831R has 40 built-in 18x18 multipliers.
 Therefore, you cannot apply filters that require more than 40 built-in multipliers
 to the PXI-7831R. Another potential cause of a compilation failure is that the
 fixed-point filter is too complicated to implement in an SCTL or that the design
 clock rate is too high. A more complicated fixed-point filter requires more FPGA
 hardware resources. The compilation might fail when the FPGA hardware resources are
 not sufficient. For example, the compilation runs properly when the fixed-point
 filter uses only 40% of the FPGA hardware resources but the compilation might fail
 if the fixed-point filter uses about 85% of the FPGA hardware resources. If you
 encounter compilation failures, try converting the filter structure to one that
 requires fewer resources or setting the design clock rate to a lower
 frequency.

The following table lists the number of multiplication units that
 each filter structure uses. One multiplication unit might require multiple FPGA
 built-in multipliers, depending on the type of multiplication unit. For example, an
 I16xI16 multiplication unit requires only one FPGA built-in multiplier, but an
 I16xI32 multiplication unit requires two FPGA built-in multipliers.

Note

| Structure | Number of Multiplication Units1 |
| --- | --- |
| FIR Direct Form | 1B |
| FIR Direct Form Transposed | 1B |
| FIR Symmetric (odd order) | 1B |
| FIR Symmetric (even order) | 1B |
| FIR Antisymmetric (odd order) | 1B |
| FIR Antisymmetric (even order) | 1B |
| IIR Cascaded Second-Order Sections Form I | 1A+1B |
| IIR Cascaded Second-Order Sections Form I Transposed | 1A+1B |
| IIR Cascaded Second-Order Sections Form II | 1A+1B |
| IIR Cascaded Second-Order Sections Form II Transposed | 1A+1B |
| Lattice MA (minimum phase) | 1A |
| Lattice MA (maximum phase) | 1A |
| Lattice ARMA (basic sections) | 2A+1B |
| Lattice ARMA (one multiplier sections) | 1A+1B |
| Lattice ARMA (normalized sections) | 2A+1B |

1. Some filter structures use two groups of multiplication units because the structures
 contain two sets of filter coefficients. A and B in the table represent coefficients
 a/k and coefficients
 b/v, respectively. One multiplication unit
 might require different number of FPGA built-in multipliers, as shown in the
 following table: Multiplicand x Coefficients
 Number of Multipliers116x116
 1
 116x132
 2
 132x116
 2
 132x132
 4
2. The Context Help window displays information about the
 generated LabVIEW FPGA code, including the estimated execution throughput, when
 you move the cursor over the filter VI.

Parent topic:

Generate LabVIEW FPGA Code

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=ripple-constraint-design-digital-filter-desig.html language=enus -->
## TOPIC 00085: Ripple Constraint Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `ripple-constraint-design-digital-filter-desig.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/ripple-constraint-design-digital-filter-desig.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A ripple constraint guarantees that the maximum error magnitude between the frequency response of the designed filter and the expected frequency response is equal to or below the constraint.You can specify a ripple constraint for a particular band by entering a positive value into the ripple constra

### Ripple Constraint Design

A ripple constraint guarantees that the maximum error magnitude between the frequency
 response of the designed filter and the expected frequency response is equal to or below
 the constraint.

ripple constraint

DFD Remez Design

Note

DFD Remez Design

Parks-McClellan

You might want to design filters with ripple constraints in the following situations:

- You want to specify the filter order and constrain the ripple magnitude in certain bands.
- You want to constrain all bands, and you want the DFD Remez Design VI to
 determine the minimum filter order that satisfies the requirements.
- You want to constrain all bands and specify the filter order as well. The DFD Remez
 Design VI reports an error if the constraints cannot be met.
 Otherwise, the DFD Remez Design VI returns a valid design with
 the ripple ratios among different bands the same as the ratios of the ripple
 constraints.

As an example for the first situation, suppose you want to design a 15<sup>th</sup> order lowpass
 filter, and you want the passband ripple magnitude to be no more than 0.1. You can set
 the passband frequency range to [0, 0.2] and the stopband frequency
 range to [0.3, 0.5] and apply equal weights in both bands. The
 following figure shows the magnitude response of the designed filter:

Figure 45.

th

[IMAGE alt='image' src='GUID-1D1640EC-224E-4F56-A195-75ECCD71137D-a5.gif']

Notice that the passband ripple is much smaller than the requirement. To make the passband ripple
 just touch the upper constraint, you can reduce the initial
 weight in the passband to [0.01, 0.01] and
 run the VI again. The following figure shows the magnitude response of the redesigned
 filter:

Figure 46.

th

[IMAGE alt='image' src='GUID-AF488624-AB3D-4C5E-94ED-A24FFD20FF0D-a5.gif']

The smaller weight value allows the DFD Remez Design VI
 to design a filter with a passband ripple that initially exceeds the constraint and then
 automatically adjust the weight level iteratively until the constraint is met.

As an example for the second situation, suppose you want to design a lowpass filter with the same
 passband and stopband frequency ranges as the previous example. You can specify the
 ripple constraints for the passband and the stopband as 0.01 and
 0.001, respectively, and set the minimum
 order input to minEven. The following figure shows the
 magnitude response of the 28<sup>th</sup> order equi-ripple FIR filter that the
 DFD Remez Design VI returns:

Figure 47.

th

[IMAGE alt='image' src='GUID-6302898A-3682-4BE3-9A74-E821F3437037-a5.gif']

Parent topic:

Remez Design Method

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=scale-the-filter-coefficients-digital-filte.html language=enus -->
## TOPIC 00086: Scale the Filter Coefficients

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `scale-the-filter-coefficients-digital-filte.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/scale-the-filter-coefficients-digital-filte.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can scale the filter coefficients before quantizing them to ensure that all the accumulators use the same data range.A filter structure consists of many accumulators. Each accumulator might use a different data range. However, the LabVIEW Digital Filter Design Toolkit provides only one sum quant

### Scale the Filter Coefficients

You can scale the filter coefficients before quantizing them to ensure that all the
 accumulators use the same data range.

A filter structure consists of many accumulators. Each accumulator might use a different data
 range. However, the LabVIEW Digital Filter Design Toolkit provides only one sum
 quantizer Q<sub>S></sub> for all the
 accumulators. Scaling the filter coefficients can help you obtain a better filtering
 result, especially for IIR Cascaded Second-Order Sections Form structures. Use the
 DFD Scale Filter VI to scale the coefficients of a floating-point
 filter.

Parent topic:

Design Fixed-Point Filters

Related concepts:

- Filter Structure Graphs
- Filter Coefficients and Quantizers
- IIR Cascaded Second-Order Sections Form Structures

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=select-a-filter-structure-digital-filter-d.html language=enus -->
## TOPIC 00087: Select a Filter Structure

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `select-a-filter-structure-digital-filter-d.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/select-a-filter-structure-digital-filter-d.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A filter structure specifies how you arithmetically use a set of filter coefficients to process an input signal.For a specified digital filter, dozens of mathematically equivalent implementation structures are available. For a floating-point digital filter, the effects of different implementation st

### Select a Filter Structure

A filter structure specifies how you arithmetically use a set of filter coefficients to
 process an input signal.

For a specified digital filter, dozens of mathematically equivalent implementation structures are
 available. For a floating-point digital filter, the effects of different implementation
 structures on the filter behavior are negligible in most cases. For a fixed-point
 digital filter, different implementation structures can result in different signal
 outputs.

In addition to FIR and IIR structures, the LabVIEW Digital Filter Design Toolkit also provides
 lattice structures. Lattice structures, including lattice allpass, lattice AR, lattice
 ARMA, and lattice MA, are good alternatives for fixed-point filter implementation. For
 example, lattice structures can preserve the stability of fixed-point IIR filters as
 long as the lattice reflection coefficients have moduli less than one, regardless of how
 limited the arithmetic precision might be.

The Digital Filter Design Toolkit provides the following categories of lattice structures:

Basic Section Type

One Multiplier Section Type

Normalized Section Type

When you select a filter structure, you must balance a number of factors, including the filter
 type, implementation resources, and computational complexity. For IIR filters, you also
 need to consider the sensitivity to coefficient quantization of each structure. The
 following table lists the default filter structures that the Filter
 Design VIs use:

| Design Method | Default Structure |
| --- | --- |
| Kaiser Window | FIR Direct Form |
| Dolph-Chebyshev Window | FIR Direct Form |
| Windowed FIR | FIR Direct Form |
| Remez/Equi-Ripple | FIR Direct Form |
| Least Pth Norm FIR | FIR Direct Form |
| IIR Notch Peak | IIR Direct Form II |
| IIR Comb | IIR Direct Form II |
| Arbitrary Group Delay | IIR Direct Form II |
| Least Pth Norm IIR | IIR Direct Form II |
| Butterworth | IIR Cascaded Second-Order Sections Form II Transposed |
| Chebyshev | IIR Cascaded Second-Order Sections Form II Transposed |
| Inverse Chebyshev | IIR Cascaded Second-Order Sections Form II Transposed |
| Elliptic | IIR Cascaded Second-Order Sections Form II Transposed |
| Bessel | IIR Cascaded Second-Order Sections Form II Transposed |
| Maxflat | IIR Cascaded Second-Order Sections Form II Transposed |
| Group Delay Compensator | IIR Cascaded Second-Order Sections Form II Transposed |

Note

You can use the DFD Convert Structure VI to select a different filter
 structure, with the following exceptions:

- You cannot convert an IIR structure into or from an FIR structure.
- You cannot convert a lattice allpass structure into or from a lattice AR structure.
- You can convert an FIR filter to an FIR Symmetric filter structure only if the FIR filter has symmetric coefficients.
- You can convert an FIR filter to an FIR Antisymmetric filter structure only if the FIR filter
 has antisymmetric coefficients.
- You can convert an FIR filter to a lattice MA (minimum phase) filter structure only if the FIR
 filter is minimum phase.
- You can convert an FIR filter to a lattice MA (maximum phase) filter structure only if the FIR
 filter is maximum phase.
- You must use an allpass filter if you want to convert a filter structure to a lattice allpass
 structure.
- You must use an all-pole IIR filter if you want to convert a filter structure to a lattice AR
 structure.

Parent topic:

Design Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=set-the-rounding-mode-digital-filter-desi.html language=enus -->
## TOPIC 00088: Set the Rounding Mode

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `set-the-rounding-mode-digital-filter-desi.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/set-the-rounding-mode-digital-filter-desi.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Rounding determines the most appropriate fixed-point number to represent a specified floating-point value based on the precision you specify. Use the rounding mode input of the Fixed-Point Tools VIs to set an appropriate rounding option.Fixed-point numbers represent discrete values with limited prec

### Set the Rounding Mode

Rounding determines the most appropriate fixed-point number to represent a specified
 floating-point value based on the precision you specify. Use the rounding
 mode input of the Fixed-Point Tools VIs to set an
 appropriate rounding option.

Fixed-point numbers represent discrete values with limited precision. Typically, the precision of
 fixed-point numbers is less than that of floating-point numbers. Use one of the
 following modes to specify how you want rounding to occur in a quantizer:

Nearest

0

Truncation

Truncation

Parent topic:

Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=simulate-fixed-point-multirate-filters.html language=enus -->
## TOPIC 00089: Simulate Fixed-Point Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `simulate-fixed-point-multirate-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/simulate-fixed-point-multirate-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To determine the quantization and modeling effects on a filtering process, not only the analyzation of the frequency response of a fixed-point filter is required, but also the simulation of the filtering process with the actual data. You can use the DFD FXP MRate Simulation VI to simulate the filter

### Simulate Fixed-Point Multirate Filters

To determine the quantization and modeling effects on a filtering process, not
 only the analyzation of the frequency response of a fixed-point filter is
 required, but also the simulation of the filtering process with the actual
 data.

You can use the DFD FXP MRate Simulation VI to simulate the
 filtering process. To verify if the fixed-point multirate filter works as
 you expect, compare the simulation result with the actual filtering result
 that you obtain by processing the same signal with the reference
 floating-point multirate filter. Ensure that the simulation result matches
 the actual filtering result. If the simulation result does not match the
 actual floating-point filtering result, try making the following
 adjustments:

- Return to the quantization step. Modify the word length for the filter
 coefficients and the scale type to avoid overflow or underflow.
- Adjust the specifications and redesign the floating-point multirate
 filter.

Parent topic:

Design Fixed-Point Multirate Filters

Related concepts:

- Multistage Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=simulating-fixed-point-filters-digital-filter.html language=enus -->
## TOPIC 00090: Simulate Fixed-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `simulating-fixed-point-filters-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/simulating-fixed-point-filters-digital-filter.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: After you create a fixed-point filter model, you must simulate the filtering process to verify that the fixed-point model works as expected in a complete implementation. You can use the DFD FXP Simulation VI and the DFD FXP Simulation with State VI to facilitate this evaluation.To verify the simulat

### Simulate Fixed-Point Filters

After you create a fixed-point filter model, you must simulate the filtering process
 to verify that the fixed-point model works as expected in a complete implementation.
 You can use the DFD FXP Simulation VI and the DFD FXP
 Simulation with State VI to facilitate this evaluation.

To verify the simulation result, you can use the following two options:

- Compare the simulation results with the filter output results that you obtain by processing the same signal with the reference floating-point filter. Ensure that the simulation results are sufficiently similar to the filtering results of the reference floating-point filter.
- Use the DFD FXP Simulation Report VI to monitor the behavior
 of the fixed-point filter during the simulation process by observing the
 filtering text report output. The report contains
 statistical information about all the quantizers — except the coefficients
 a/k and coefficients
 b/v quantizers—in the fixed-point
 model. Each quantizer has five data entries: max value,
 min value, #overflows,
 #underflows, and #operations.
 Ensure that both #overflows and
 #underflows equal 0 or fall below an
 appropriate threshold.

Like all other parts of the design process, simulation is a trial-and-error process. If you
 observe overflow or underflow in the filtering text report or if the simulation result
 does not match the actual floating-point filtering result, try making the following
 adjustments:

- Return to the modeling step. Modify the integer word lengths for the related quantizers to
 eliminate overflows and underflows until both #overflows 
 and #underflows equal 0 or fall below an appropriate
 threshold. Use max value and min
 value to estimate the integer word lengths. Tip The DFD
 FXP Modeling VI automatically calculates integer word lengths
 except that of the input signal, so you might not modify these integer word
 lengths directly. However, you can use the DFD FXP Get
 Quantizer VI to retrieve the integer word lengths for the
 related quantizers and then use the DFD FXP Set Quantizer
 VI to modify the integer word lengths.
- Change the implementation structure.
- Adjust the specifications and redesign the floating-point filter.

Note

#operations

#operations

Parent topic:

Design Fixed-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=single-point-band-design-digital-filter-desig.html language=enus -->
## TOPIC 00091: Single-Point Band Design

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `single-point-band-design-digital-filter-desig.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/single-point-band-design-digital-filter-desig.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A single-point band is a frequency band that consists of a single point. Single-point bands are useful when designing notch and peak filters.You can specify single-point bands with the DFD Remez Design VI by entering only one point in the band specs input to describe the frequency response.For examp

### Single-Point Band Design

A single-point band is a frequency band that consists of a single point. Single-point
 bands are useful when designing notch and peak filters.

You can specify single-point bands with the DFD Remez Design VI by entering
 only one point in the band specs input to describe the frequency
 response.

For example, suppose you want to design a double-notch filter with notch frequencies at 0.15 Hz
 and 0.35 Hz. The five bands in this example have the frequency ranges of [0, 0.12],
 [0.15], [0.18, 0.32], [0.35], and [0.38, 0.5]. All passbands, single-point bands, and
 stopbands are equally weighted. The following figure shows the magnitude response of the
 designed 30<sup>th</sup> order filter:

[IMAGE alt='image' src='GUID-C44B97D1-C584-488D-9249-03BB15DC7158-a5.gif']

You might find other uses for single-point band specifications. For example, by adding a single-point band in a transition band, you can force the frequency response to pass close to a particular point. Alternatively, when you encounter transition band anomalies designing a multiband filter, you might be able to remove the anomalies by adding single-point bands within those transition bands.

Parent topic:

Remez Design Method

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=specify-the-gain-processing-target.html language=enus -->
## TOPIC 00092: Specify the Gain Processing Target

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `specify-the-gain-processing-target.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/specify-the-gain-processing-target.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the gain processing input of the DFD FXP Quantize Coef VI to specify an appropriate gain processing target. A filter gain implies a multiplication operation. If you process the filtered signal on a target, for example, an NI Reconfigurable I/O (RIO) target, the filtering process requires hardwar

### Specify the Gain Processing Target

Use the gain processing input of the DFD FXP
 Quantize Coef VI to specify an appropriate gain processing
 target.

A filter gain implies a multiplication operation. If you process the filtered
 signal on a target, for example, an NI Reconfigurable I/O (RIO) target, the
 filtering process requires hardware resources on the target for the
 multiplication operation that the filter gain introduces. However, if you
 want to process the filtered signal on a host computer, you can move the
 filter gain operation to the host computer and save resources on the
 target.

Parent topic:

Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=specify-the-quantizer-source-digital-filte.html language=enus -->
## TOPIC 00093: Specify the Quantizer Source

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `specify-the-quantizer-source-digital-filte.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/specify-the-quantizer-source-digital-filte.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must specify the appropriate quantizer source when configuring the quantizers by using the source input of the Fixed-Point Tools VIs to choose an appropriate quantizer source.A fixed-point filter implementation involves many different quantizers, such as the coefficients quantizer, the input qua

### Specify the Quantizer Source

You must specify the appropriate quantizer source when configuring the quantizers by
 using the source input of the Fixed-Point
 Tools VIs to choose an appropriate quantizer source.

A fixed-point filter implementation involves many different quantizers, such as the coefficients
 quantizer, the input quantizer, and the product quantizer. Each quantizer has a
 different effect on a fixed-point filter response.

Parent topic:

Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=specify-the-word-length-and-integer-word-l.html language=enus -->
## TOPIC 00094: Specify the Word Length and Integer Word Length

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `specify-the-word-length-and-integer-word-l.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/specify-the-word-length-and-integer-word-l.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the wl and iwl inputs of the Fixed-Point Tools VIs to specify the word length and integer word length, respectively, of a quantizer.The word length indicates the number of bits you want to use in representing a fixed-point number. The integer word length specifies the number of bits, including t

### Specify the Word Length and Integer Word
 Length

Use the wl and iwl inputs of the
 Fixed-Point Tools VIs to specify the word length and integer word
 length, respectively, of a quantizer.

The word length indicates the number of bits you want to use in representing a fixed-point
 number. The integer word length specifies the number of bits, including the sign bit,
 you use in representing the integer part of a fixed-point number. The difference in bits
 between the word length and the integer word length determines the digits of
 precision.

The finite word length of a quantizer can affect the frequency response of the resulting
 fixed-point filter. The larger word length value you specify, the less the fixed-point
 representation distorts the frequency response. However, a larger word length value also
 requires more hardware resources, so you must specify a word length that provides an
 acceptable tradeoff between distortion and hardware resource consumption.

Parent topic:

Quantize Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=supported-execution-targets-digital-filter-de.html language=enus -->
## TOPIC 00095: Supported Execution Targets

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `supported-execution-targets-digital-filter-de.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/supported-execution-targets-digital-filter-de.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the LabVIEW Digital Filter Design Toolkit to apply a digital filter on many different types of target. The following table describes the target types supported by the LabVIEW Digital Filter Design Toolkit and the software required to run them:Type of TargetAdditional Required SoftwareA c

### Supported Execution Targets

You can use the LabVIEW Digital Filter Design Toolkit to apply a digital filter
 on many different types of target. The following table describes the target
 types supported by the LabVIEW Digital Filter Design Toolkit and the
 software required to run them:

| Type of Target | Additional Required Software |
| --- | --- |
| A computer running Windows | — |
| A NI Field-Programmable Gate Array (FPGA) target, such as an NI Reconfigurable I/O (NI-RIO) device. To use a digital filter on an FPGA target, you first must generate FPGA code for that filter. | LabVIEW FPGA ModuleNI-RIO driver software |
| A 32-bit microprocessor. To use a digital filter on a 32-bit microprocessor, you first must generate fixed-point C code for that filter. | LabVIEW with embedded target supportThe LabVIEW add-on for the embedded target |
| An NI Real-Time (RT) target, such as an NI PXI or CompactRIO controller, running a Real-Time Operating System (RTOS). The Digital Filter Design VIs support native execution on these operating systems. | LabVIEW Real-Time ModuleDriver software for any hardware devices |

Note

ni.com

Related concepts:

- Generate LabVIEW FPGA Code
- Generate Fixed-Point C Code

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00096: LabVIEW Digital Filter Design Toolkit User Manual

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Digital Filter Design Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related

### LabVIEW Digital Filter Design
 Toolkit
 User Manual

The LabVIEW Digital Filter Design
 Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download LabVIEW Digital Filter Design Toolkit
- LabVIEW Digital Filter Design Toolkit Release Notes
- Hardware and Software Operating System Compatibility
- Interactive Activation Guide
- NI Learning Center

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=using-floating-point-filters-digital-filter-d.html language=enus -->
## TOPIC 00097: Use Floating-Point Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `using-floating-point-filters-digital-filter-d.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/using-floating-point-filters-digital-filter-d.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: After analyzing the filter design, you can use the filter to process an input signal in the following ways using the Processing VIs: As a sequence of data blocks. As a sequence of data blocks with saved internal filter states.

### Use Floating-Point Filters

After analyzing the filter design, you can use the filter to process an
 input signal in the following ways using the
 Processing VIs:

- As a sequence of data blocks.
- As a sequence of data blocks with saved internal filter
 states.

Parent topic:

Design Floating-Point Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=using-floating-point-multirate-filters.html language=enus -->
## TOPIC 00098: Use the Floating-Point Multirate Filters

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `using-floating-point-multirate-filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/using-floating-point-multirate-filters.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After analyzing the filter design, either the input signal can be processed using a multirate filter or the filter coefficients of the multirate filter can be quantized. Use the Multirate Processing VIs to process a signal with the multirate filter you designed. The Multirate Processing VIs can proc

### Use the Floating-Point Multirate
 Filters

After analyzing the filter design, either the input signal can be processed using a
 multirate filter or the filter coefficients of the multirate filter can be
 quantized.

Use the Multirate Processing VIs to process a signal with the multirate filter you
 designed. The Multirate Processing VIs can process an input signal in the following
 ways:

- As a single block of data
- As a sequence of data blocks
- As a sequence of data blocks with saved internal filter states

Use the DFD MRate Filtering for Single Block VI or the DFD
 NStage MRate Filtering for Single Block VI to process a single block of
 data. When processing a single block, the VIs extend the input signal block at both ends
 to ensure the output signal block has the same length as the input signal block. Use the
 other Multirate Processing VIs to process multiple signal blocks
 continuously. These VIs automatically retain the internal states of the filter between
 blocks, and they allow you to save and restore filter states without causing artifact
 glitches in the processed data.

You achieve the same results when you process multiple blocks as a sequence of blocks as
 when you process them together as one single block. To eliminate the delay between the
 input and output signals, enable the zero-phase filtering option when using the
 Multirate Processing VIs.

Parent topic:

Design Floating-Point Multirate Filters

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit path=zero-phase-filtering-digital-filter-design-to.html language=enus -->
## TOPIC 00099: Zero-Phase Filtering

- bundle_id: `labview-digital-filter-design-toolkit`
- source_path: `zero-phase-filtering-digital-filter-design-to.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit/raw/resource/enus/zero-phase-filtering-digital-filter-design-to.html
- document_id: `labview-digital-filter-design-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Zero-phase filtering helps you eliminate the group delay in the output signal of a filter.All multirate filters you design with the LabVIEW Digital Filter Design Toolkit, except for possible odd-order Cascaded Integrator Comb (CIC) filters, are even-order, linear phase FIR filters. When you use line

### Zero-Phase Filtering

Zero-phase filtering helps you eliminate the group delay in the output signal of
 a filter.

All multirate filters you design with the LabVIEW Digital Filter Design Toolkit, except for
 possible odd-order Cascaded Integrator Comb (CIC) filters, are even-order,
 linear phase FIR filters. When you use linear phase FIR filters to process
 signals, the filters return signals with a constant group delay, as shown in
 the following figure:

[IMAGE alt='image' src='GUID-A13B6193-BFE0-40DB-815C-05611BE92F07-a5.gif']

In this figure, you can see that the Output Signal plot contains a
 constant set of zero values, which denotes the delay between the output and
 input signals. If you want to eliminate the delay, you can implement the
 filter as a zero-phase filter by setting the zero
 phase? input of the Multirate Processing VIs to
 TRUE. The following figure shows an example of an
 output signal that has no delay compared to the input signal:

[IMAGE alt='image' src='GUID-C1D1976F-8DC1-403E-A473-281F79BB8394-a5.gif']

Multirate Processing

Note

Parent topic:

Multirate Filter Basics

Related concepts:

- Cascaded Integrator Comb Filters
- Filter Attributes
