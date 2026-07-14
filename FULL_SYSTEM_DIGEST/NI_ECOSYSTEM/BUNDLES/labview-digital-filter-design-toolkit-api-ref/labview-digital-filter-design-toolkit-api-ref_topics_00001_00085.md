# NI DOCUMENT BUNDLE: labview-digital-filter-design-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-digital-filter-design-toolkit-api-ref start=1 end=85 -->
<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/advncd_techniques.html language=enus -->
## TOPIC 00001: Advanced Techniques for Designing Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/advncd_techniques.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/advncd_techniques.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Advanced Techniques for Designing Filters (Digital Filter Design Toolkit)

This book contains an overview of advanced techniques for developing digital filters with the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI and the [DFD Least Pth Norm Design](/csh?topicname=lvdigfiltdestk/dfd_lpth_norm.html) VI. The book [Digital Filter Design](../lvdfdtconcepts/dfd_related_doc.html) contains more information about these advanced techniques.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/analyze_design.html language=enus -->
## TOPIC 00002: Analyzing Floating-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/analyze_design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/analyze_design.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Analyzing Floating-Point Filters (Digital Filter Design Toolkit)

After you [enter the target specifications](../lvdfdtconcepts/enter_filter_spec.html) for a digital filter, you can [analyze](/csh?topicname=lvdfdthowto/design_fp_filter_2.html) the characteristics of the resulting filter in the **Configure Classical Filter Design** dialog box of the [Classical Filter Design](/csh?topicname=lvdigfiltdestk/dfd_classical_filter.html) Express VI by evaluating the [pole-zero plot](../lvdfdtconcepts/poles_and_zeroes.html), the magnitude response, and the filter order.

#### Magnitude Response

The frequency response of a digital filter is defined by *H*(*e*<sup>*j2πf*</sup>), and the magnitude response is defined by |*H*(*e*<sup>*j2πf*</sup>)|. For discrete-time systems, *H*(*e*<sup>*j2πf*</sup>) is periodic with a period of *f*<sub>*s*</sub>. For real-valued digital filters, the magnitude response is symmetric with respect to 0, ±*f*<sub>*s*</sub>, ±2*f*<sub>*s*</sub>, *…*. Therefore, you can calculate the magnitude response for only [0, *f*<sub>*s*</sub>/2], which contains the frequencies between 0 and the Nyquist frequency. The magnitude response graph in the **Configure Classical Filter Design** dialog box includes a green vertical line to indicate the location of *f*<sub>*s*</sub>/2.

#### Filter Order Specification

The Classical Filter Design Express VI automatically computes the minimal filter order required to fulfill the given filter specification and displays the order in the **Filter order** indicator. With the same specification, you can use different algorithms to create digital filters with different filter orders. You can estimate the computational complexity and cost based on the filter order. If you have strict requirements for the system, the filter order can help you determine if the filter is acceptable.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/analyze_fixedpoint.html language=enus -->
## TOPIC 00003: Analyzing Fixed-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/analyze_fixedpoint.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/analyze_fixedpoint.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Analyzing Fixed-Point Filters (Digital Filter Design Toolkit)

The [Filter Analysis](/csh?topicname=lvdigfiltdestk/dfd_check_filter.html) Express VI performs [fixed-point analysis](/csh?topicname=lvdfdthowto/design_fxp_filter_4.html) in the frequency domain. Use the calculated results to optimize the fixed-point filter. You might need to analyze and adjust the filter design iteratively until the calculated results are satisfactory.

Use the Filter Analysis Express VI to observe the response of the fixed-point filter. Ensure that the fixed-point filter is stable by verifying that all poles are within the unit circle and that the filter maintains a satisfactory frequency response. If the fixed-point characteristics do not satisfy the requirements, try one or more of the following options:

- Return to the quantization step and change the quantizer settings.
- Change the implementation structure .
- Change the floating-point reference filter specifications to allow more headroom for finite-precision effects.
- For infinite impulse response (IIR) filters, reduce the pole radius constraint of the reference floating-point filter.

If you notice large distortions in the response, look for underflow or overflow conditions. Use the [DFD FXP Coef Report](/csh?topicname=lvdigfiltdestk/dfd_fxp_coef_report.html) VI to determine if overflows or underflows exist in the quantized coefficients. If you find occurrences of overflows or underflows in the coefficients report, repeat the quantization step by using an increased **iwl** value for the coefficients quantizer. Increasing the **iwl** value helps eliminate overflows and underflows and improve the frequency response of the filter. If you do not find any occurrences of overflows or underflows, try reducing the value of **iwl** to allow more digits of precision for the quantized coefficients. If the minimum allowable **iwl** value still returns large distortions in the frequency response, you need to increase the value of **wl** to minimize the distortion.

|  | Note Underflows and overflows that happen during quantization do not always affect filter responses. Therefore, if the filter response after coefficients quantization is satisfactory, you do not need to make adjustments to avoid overflows or underflows. |
| --- | --- |

Refer to the Step 3 - Analyze Quantized Lowpass (Lowpass) VI in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter directory for an example that demonstrates how to [quantize a floating-point lowpass filter](../lvdfdtconcepts/quantize_fl_filters.html) and analyze the quantized lowpass filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/applinear_iir_design.html language=enus -->
## TOPIC 00004: Approximated Linear Phase IIR Design (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/applinear_iir_design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/applinear_iir_design.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Approximated Linear Phase IIR Design (Digital Filter Design Toolkit)

You can design IIR filters with approximately linear phase using the [DFD Least Pth Norm Design](/csh?topicname=lvdigfiltdestk/dfd_lpth_norm.html) VI. You must set **filter type** to Symmetric or Antisymmetric.

Although it is theoretically impossible to design causal IIR digital filters with exactly linear phase, you can design IIR filters with approximately linear phase. For example, suppose you want to design an approximately linear phase IIR lowpass filter with a passband frequency range of [0, 0.2] and a stopband frequency range of [0.3, 0.5]. You can set the specifications as shown in the following figure:

[IMAGE alt='image' src='lpth-iir-linear-phase-specs.gif']

The following figure shows the magnitude response of the designed filter.

[IMAGE alt='image' src='lpth-iir-linear-phase-respo.gif']

The following figure shows the phase response of the designed filter.

[IMAGE alt='image' src='lpth-iir-approx-linear-phas.gif']

Notice that this filter has greater stopband attenuation than the [linear phase FIR filter designed](../lvdfdtconcepts/lpth_norm_linearfir.html), and this filter keeps the passband phase response roughly linear.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/arbitrary_shaped.html language=enus -->
## TOPIC 00005: Arbitrary Shape Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/arbitrary_shaped.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/arbitrary_shaped.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Arbitrary Shape Filters (Digital Filter Design Toolkit)

If you want to design a linear phase finite impulse response (FIR) filter with an arbitrary magnitude response, you can use the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI. If you want to design a filter in which linear phase is not required but minimizing filter order is important, you can use the [DFD Least Pth Norm Design](/csh?topicname=lvdigfiltdestk/dfd_lpth_norm.html) VI to design an infinite impulse response (IIR) filter.

You can describe an arbitrary frequency response with multiple points using piecewise linear interpolation. The number of points you must supply to describe the shape depends on the target arbitrary shape magnitude response in a certain frequency band. You do not have to space the points evenly. Use more points where the magnitude response is tightly curved and fewer points where the magnitude response is more linear.

#### FIR Filters with Arbitrary Magnitude Responses

To design a linear phase FIR filter with an arbitrary shape magnitude response, use the DFD Remez Design VI and set the **filter type** input to Symmetric or Antisymmetric according to the [linear phase FIR filter type table](../lvdfdtconcepts/linear_min_filters.html#types). Then describe the shape of the filter by specifying multiple points in the **band specs** input.

The following example uses a lowpass filter with a passband frequency ranging from 0 to 0.25 and a stopband frequency ranging from 0.3 to 0.5. Three points at frequencies 0, 0.1, and 0.25 with expected amplitudes of 1, 2, and 1, respectively, describe the shape of the passband range. To design this filter, enter the specifications shown in the following figure into the DFD Remez Design VI.

[IMAGE alt='image' src='arb-fir-mag-specs.gif']

The following figure shows the magnitude response of the designed filter.

[IMAGE alt='image' src='arb-fir-mag-response.gif']

The previous example describes the passband shape with only three points. You also can describe an arbitrary passband shape with as many points as necessary. The following example uses 5,000 evenly-shaped frequency points to describe the passband shape of a sinc compensation lowpass filter. You can use this sinc compensator to correct the amplitude droop caused by a zero-order hold in a digital-to-analog (D/A) converter, as shown in the following figure:

[IMAGE alt='image' src='inv-sinc-compensator.gif']

An amplitude droop measures the amount that the signal power decreases in a specified frequency range. In the previous figure, the **Zero-Order Hold** plot shows the magnitude response of a zero-order hold in the D/A converter. You can see an amplitude droop exists in the frequency range of interest [0, 0.2]. To correct the amplitude droop, you can create a filter that whose magnitude response is similar to the **Anti-Sinc Compensator** plot in the frequency range of interest [0, 0.2]. You can create the filter by describing the passband shape with the corresponding inverse sinc function values of the droop. The following figure shows the magnitude response of the designed filter.

[IMAGE alt='image' src='mag_resp_anti_sinc.gif']

#### IIR Filters with Arbitrary Magnitude Responses

If you want to design an IIR filter with an arbitrary shape magnitude response and the phase response is not important, use the DFD Least Pth Norm Design VI and set the **filter type** input to either Minimum Phase or Maximum Phase. The DFD Least Pth Norm Design VI ignores all other phase specification inputs, including **group delay** and **phase** in the **band specs** input. Define the shape of the magnitude response by entering multiple points in the **band specs** input.

For example, you can design a minimum phase IIR filter with the same arbitrary magnitude response as the previous example. Set the **filter type** input to Minimum Phase and enter the same **band specs** into the DFD Least Pth Norm Design VI. The following figure shows the magnitude response of the designed filter.

[IMAGE alt='image' src='arb-iir-filter.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/cic_filters.html language=enus -->
## TOPIC 00006: Cascaded Integrator Comb Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/cic_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/cic_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cascaded Integrator Comb Filters (Digital Filter Design Toolkit)

A Cascaded Integrator Comb (CIC) filter is a special class of linear phase, finite impulse response (FIR) filter. CIC filters do not require multipliers and use a limited amount of storage. Therefore, CIC filters are more efficient than conventional FIR filters, especially in fixed-point applications. You usually use CIC filters in multirate systems with large sampling frequency conversion factors, such as digital down converters (DDC) and digital up converters (DUC) in communication systems.

#### CIC Filter Basics

CIC filters do not have multipliers and consist of only adders, subtracters, and registers. Therefore, you can implement multirate filters efficiently using the CIC filter structure. CIC filters are defined by the following transfer function:

[IMAGE alt='image' src='equ_lowpass_cic.gif']

| where | z is a complex variable |
| --- | --- |
|  | I is a basic integrator section |
|  | C is a basic comb section |
|  | M is the sampling frequency conversion factor |
|  | R is the differential delay |
|  | N is the number of stages |

Theoretically, *R* and *N* can be any positive integer value, but the LabVIEW Digital Filter Design Toolkit constrains *R* to be either 1 or 2 because you do not need to use other values in most cases. *N* is in the range [1, 8]. The equation above shows that a CIC filter is equivalent to *N* stages of cascaded [FIR filters](../lvdfdtconcepts/fir_filter_specs.html) with unit coefficients. Each FIR filter has a rectangular impulse response. All coefficients of the FIR filters are 1 and therefore symmetric, so the CIC filter has a linear phase response and constant [group delay](../lvdfdtconcepts/grp_phase_delay.html).

Use the [Multirate CIC Design](/csh?topicname=lvdigfiltdestk/dfd_cic_filter.html) Express VI to design a CIC filter. Refer to the CIC Filter Design VI in the labview\examples\Digital Filter Design\Floating-Point Filters\Multirate directory for an example that demonstrates how to use the Multirate CIC Design Express VI to design a CIC filter.

#### Implementing Fixed-Point CIC Filters

The Digital Filter Design Toolkit supports fixed-point implementation of only lowpass CIC filters. To implement fixed-point CIC filters, cascade *N* basic integrator sections (the *I* block) and *N* basic comb sections (the *C* block) together with a sampling frequency conversion factor. The following figure shows an example of a fixed-point implementation of an *N*-stage decimation CIC filter, where *M* is the sampling frequency conversion factor.

[IMAGE alt='image' src='fxp_cic_decimating.gif']

The following figure shows an example of a fixed-point implementation of an *N*-stage interpolation CIC filter.

[IMAGE alt='image' src='fxp_cic_interpolating.gif']

The following figure shows a basic integrator section in detail.

[IMAGE alt='image' src='cic_basic_integrator.gif']

The following figure shows a basic comb section in detail.

[IMAGE alt='image' src='cic_basic_comb.gif']

##### Setting the Internal Precision

In a fixed-point implementation, the maximum bit width required for a CIC decimation filter is the sum of the input bits and the bits that the filter uses in accommodating the maximum filter gain. Using the maximum bit width for each integrator or comb section guarantees that no overflow occurs at the output of the filter. The maximum bit width also ensures that you obtain a full-precision result. However, obtaining the full-precision result requires the maximum field-programmable gate array (FPGA) hardware resources.

In most real-world applications, the required output bit width is smaller than the maximum bit width. Therefore, you can discard the least significant bits (LSBs) from the maximum bit width to obtain a smaller output bit width. Using the [DFD FXP MRate Modeling](/csh?topicname=lvdigfiltdestk/dfd_fxp_mr_mod.html) VI, you can prune the LSBs in each successive integrator or comb section. This operation is known as bit pruning. Bit pruning enables you to obtain a precision that approximates the full precision and to spare the FPGA hardware resources. However, bit pruning introduces additional noise to each processing section, and the amount of LSBs that you discard determines the noise level.

When using the DFD FXP MRate Modeling VI to model a fixed-point CIC filter, you can set the **internal precision** input to Truncated to prune the intermediate bit widths. This option is valid for only multirate FIR filters and fixed-point CIC decimation filters. If you set **internal precision** to Full, this VI applies the maximum bit width to each processing section.

The following figure shows an example of filtering results by using both the Truncated and Full options.

[IMAGE alt='image' src='cic_truncated_full_comp.gif']

In the **Output Signal** graph of the previous figure, you can see that the **Truncated** plot renders nearly the same filtering result as the **Full** plot does. The **Comparing the Full and Truncated Options** graph shows the detailed difference between the two filtering results. The few nonzero values indicate the slight precision difference between the two internal precision options.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/comb_filters.html language=enus -->
## TOPIC 00007: Comb Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/comb_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/comb_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Comb Filters (Digital Filter Design Toolkit)

Use the [DFD IIR Notch Peak Design](/csh?topicname=lvdigfiltdestk/dfd_iir_notch_peak.html) VI to design [notch and peak filters](../lvdfdtconcepts/notch_peak_filters.html) that suppress noise or enhance a signal at one particular frequency. However, you might want to suppress noise or enhance a signal at more than one frequency. For example, you might need to cancel the AC powerline fundamental and harmonics. In that situation, you can use a comb notch/peak filter.

Comb filters also can separate two signals with different frequency harmonics. For example, in color TV systems, comb filters separate the luminance component and chrominance component from the composite video signal.

The following table lists each type of comb filter with its transfer function and magnitude response. Notice that you can create two types of comb notch/peak filters. One type has notches or peaks at the frequencies *kf*<sub>*s/N*</sub>, while the other type has notches or peaks at the frequencies (*k*+1/2)*f*<sub>*s*</sub>/*N*, where *k* is an integer in the range [0, *N*−1].

| Filter | Transfer Function | Magnitude Response (N = 10) |
| --- | --- | --- |
| Notch Type I |  |  |
| Notch Type II |  |  |
| Peak Type I |  |  |
| Peak Type II |  |  |

The following figure shows the implementation of a comb filter.

[IMAGE alt='image' src='structcombfil.gif']

In this figure, you can see that the implementation of the comb filter requires only two adders and two multipliers, which makes the comb filter efficient in many applications.

The following figure shows a typical Type I comb notch filter in which the first notch occurs at *f* = 0, or equivalently, (|*H*(0)| = 0).

[IMAGE alt='image' src='typicombnotchfilter.gif']

The following figure shows a typical Type II comb notch filter in which the first notch occurs at *f* = *f*
 <sub>0</sub>, or equivalently, (|*H*(0)| = 1).

[IMAGE alt='image' src='typiicombnotchfilter.gif']

The following figure shows a typical Type I comb peak filter in which the first peak occurs at *f* = 0, or equivalently, (|*H*(0)| = 1).

[IMAGE alt='image' src='typicombpeakfilter.gif']

The following figure shows a typical Type II comb peak filter in which the first peak occurs at *f* = *f*
 <sub>0</sub>, or equivalently, (|*H*(0)| = 0).

[IMAGE alt='image' src='typiicombpeakfilter.gif']

From the previous figures, you can see that a comb filter is characterized by the parameters *f*
 <sub>0</sub>, *A*<sub>*b*</sub>, and Δ*f*. *f*
 <sub>0</sub> denotes the center frequency of the notch or peak, *A*<sub>*b*</sub> denotes a level on the magnitude squared response of the filter in decibels, and Δ*f* denotes the frequency bandwidth at *A*<sub>*b*</sub>. The default value of *A*<sub>*b*</sub> is −3 dB, which represents the half maximum value of the magnitude squared response. Use the [DFD IIR Comb Design](/csh?topicname=lvdigfiltdestk/dfd_iir_comb_design.html) VI to design a comb notch or peak filter. This VI enables you to design the comb notch or peak filter either by specifying the center frequency and the bandwidth of the notch/peak or by specifying the number of notches/peaks and the bandwidth.

For example, assume a time waveform of a noisy electrocardiogram (ECG) signal sampled at 480 Hz, as shown in the following figure:

[IMAGE alt='image' src='comb_noisy-ecg-signal.gif']

The following figure shows the spectrum of the same noisy signal. In this figure, you can identify noise at 60 Hz, 120 Hz, and 180 Hz.

[IMAGE alt='image' src='comb_noisy-ecg-spectrum.gif']

To remove the noise, you can use the By f0 and Bandwidth instance of the [DFD IIR Comb Design](/csh?topicname=lvdigfiltdestk/dfd_iir_comb_design.html) VI to design a comb notch filter with the following specifications:

| DFD IIR Comb Design VI Inputs | Value |
| --- | --- |
| filter type | Notch Type I |
| f0 [Hz] | 60 |
| Δf [Hz] | 0.5 |
| fs [Hz] | 480 |

The following figure shows the magnitude response of the resulting comb filter.

[IMAGE alt='image' src='comb_mag-response.gif']

The following figure shows that the filtered ECG signal is close to the original noise-free samples.

[IMAGE alt='image' src='comb_filtered-ecg-signal.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/configure_quantizer.html language=enus -->
## TOPIC 00008: Filter Coefficients and Quantizers (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/configure_quantizer.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/configure_quantizer.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Filter Coefficients and Quantizers (Digital Filter Design Toolkit)

In a fixed-point filter implementation, you quantize the coefficients as well as the intermediate operands and results. The LabVIEW Digital Filter Design Toolkit uses quantizers to store different quantization settings for the coefficients and the intermediate operands and results. You must configure all quantizers correctly in a fixed-point filter implementation. The following figure shows an example of a fixed-point model.

[IMAGE alt='image' src='signal-io.gif']

This fixed-point model contains the following quantizers:

- Q *I* is the input quantizer for the input signal of a fixed-point filter.
- Q *S* is the sum quantizer for the summation of a fixed-point adder.
- Q *D* is the delay quantizer for the input of a delay element.
- Q *M* is the multiplicand quantizer for the multiplicand of a fixed-point multiplier, which multiplies a quantized multiplicand by a quantized coefficient.
- Q *C* is the filter coefficients quantizer for the reference floating-point filter. Depending on the group type of the filter coefficients , Q *C* can be coefficients a / k or coefficients b / v .
- Q *P* is the product quantizer for the product of a fixed-point multiplier.
- Q *O* is the output quantizer for the output signal of a fixed-point filter.

Each quantizer has a different effect on a fixed-point filter response depending on the filter structure. You must [create a fixed-point filter model](../lvdfdtconcepts/model_fp_filter.html) and [simulate the behavior of the filter model](../lvdfdtconcepts/sim_fp_filters.html) through trial and error before you use the corresponding fixed-point filter. Although you can determine the effects of coefficient quantization at design time, you cannot determine other quantization effects until you filter the expected input signals. For example, the actual data might be too large or might lead to limit cycles.

When you configure the quantizers, depending on which VI you use, you might need to complete some or all of the following items:

- Specify the quantizer source
- Specify the word length and integer word length
- Handle overflows and underflows
- Specify the rounding mode

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/design_fl_filters.html language=enus -->
## TOPIC 00009: Designing Floating-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/design_fl_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/design_fl_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Floating-Point Filters (Digital Filter Design Toolkit)

This book explains how to use the interactive [Classical Filter Design](/csh?topicname=lvdigfiltdestk/dfd_classical_filter.html) Express VI to design floating-point filters. This book also describes how to analyze and use a designed floating-point filter.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/design_fl_multirate.html language=enus -->
## TOPIC 00010: Designing Floating-Point Multirate Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/design_fl_multirate.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/design_fl_multirate.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Floating-Point Multirate Filters (Digital Filter Design Toolkit)

You can follow the [floating-point single-rate filter design process](../lvdfdtconcepts/dfd_fl_process.html) to design a floating-point multirate filter. This topic explains how to use the [Multirate FIR Design](/csh?topicname=lvdigfiltdestk/dfd_mrate_fir_design.html) Express VI to design a lowpass multirate finite impulse response (FIR) filter. The following figure illustrates the typical magnitude response of a lowpass filter in multirate systems.

[IMAGE alt='image' src='mag_resp_multi_lowpass.gif']

In this figure, *f*<sub>*s*</sub> denotes the sampling frequency of the input signal. When designing filter specifications, you must take the filtering mode into consideration. Because [decimation](../lvdfdtconcepts/dfd_decimation.html) and [interpolation](../lvdfdtconcepts/dfd_interpolation.html) are special cases of [rational resampling](../lvdfdtconcepts/rational_resampling.html), you can use the following filter specifications to design any filter with a rational factor of *L*/*M*.

| Filter Specification | Value Range |
| --- | --- |
| Passband edge frequency | 0 < fpass < min(Lfs/2M, fs/2) |
| Stopband edge frequency | fpass < fstop < Lfs/M−fpass |

Typically, *f*<sub>*pass*</sub> is the highest frequency of interest in the input signal. If *f*<sub>*stop*</sub> < min(*Lf*<sub>*s*</sub>/(2*M*), *f*<sub>*s*</sub>/2), the transition band is free of aliases. If you change the constraints of *f*<sub>*stop*</sub> to min(*Lf*<sub>*s*</sub>/(2*M*), *f*<sub>*s*</sub>/2) < *f*<sub>*stop*</sub> < (*Lf*<sub>*s*</sub>/2*M*−*f*<sub>*pass*</sub>), the filter has a wider transition band and a lower order, which can reduce the computational complexity significantly in filtering operations. However, the transition band then contains aliasing in the frequency conversions.

#### Entering Floating-Point Filter Specifications

After you add the Multirate FIR Design Express VI to the block diagram, the **Configure Multirate Filter Design** dialog box appears, as shown in the following figure:

[IMAGE alt='image' src='config_mrate_filter_design_db.gif']

On the **Floating-Point Design** tab of the configuration dialog box, you can select the filter type and design method from the pull-down menus and specify the filter factor. You then can enter the filter specifications through either the numeric controls on the right side of the tab or the magnitude response graphical interface in the configuration dialog box. The results are equivalent.

##### Using the Numerical Controls

Similar to the [numerical controls for single-rate filter design](../lvdfdtconcepts/enter_filter_spec.html#text_interface), the numerical controls for multirate filter design also contain frequency ranges and ripple constraint settings. In addition to these settings, you also need to specify the sampling frequency of the input signal in the **Input sampling frequency** numeric control. This VI then automatically calculates the sampling frequency of the output signal based on the filter specifications you entered.

##### Using the Graphical Interface

The **Magnitude Response** graph displays the magnitude response of the designed multirate filter. The magnitude axis can be either a linear or a logarithmic scale. Remove the checkmark from the **Magnitude in dB** checkbox to use a linear scale, or keep the checkmark in the **Magnitude in dB** checkbox to use a logarithmic scale.

The **Magnitude Response** graph contains a set of cursors that you can use to specify the [passband and stopband](../lvdfdtconcepts/dfd_filter_spec.html). Use the passband and stopband cursors to change the passband and stopband, respectively, of the multirate filter. Under the linear scale, the distance between unity and the horizontal passband cursor specifies the maximum passband ripple. The location of the vertical passband cursor indicates the passband edge frequency. The stopband cursors work the same when defining the specifications of the stopband. Under the logarithmic scale, the distance between 0 dB and the horizontal stopband cursor specifies the stopband attenuation.

##### Guidelines for Entering Filter Specifications

As you define a filter specification, you must adhere to a set of rules to maintain valid specifications. If you do not adhere to the following rules, the **Configure Multirate Filter Design** dialog box displays a message in the **Tips** indicator with suggestions for repositioning the cursors.

- Keep the horizontal cursors in the range (0, 1) in a linear scale or (−inf, 0 dB) in a logarithmic scale.
- Keep the horizontal passband cursor above the horizontal stopband cursor.
- The Passband edge frequency value must be less than the Nyquist frequency, or you must keep the vertical passband cursor to the left of the Nyquist cursor.
- The Stopband edge frequency value must be greater than the Passband edge frequency value, or you must keep the vertical passband cursor to the left of the stopband cursor.
- If you remove the checkmark from the Transition band aliasing allowed checkbox to avoid aliasing in the transition band, keep the Stopband edge frequency value between the Passband edge frequency value and the Nyquist frequency, or keep the vertical stopband cursor between the vertical passband and Nyquist cursors. If you keep the checkmark in the Transition band aliasing allowed checkbox to allow aliasing in the transition band, keep the vertical stopband cursor between the vertical passband cursor and the vertical stopband limit cursor.

After you finish entering the filter specifications, click the **Update Design** button to apply the new specifications.

Refer to the Step 1 - Design Decimation (MRate) VI in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter directory for an example that demonstrates how to use the Multirate FIR Design Express VI to design a decimation filter.

#### Analyzing the Floating-Point Filter Design

When you design the multirate filter using the Multirate FIR Design Express VI, you can analyze the filter design by [examining the magnitude response and filter order](../lvdfdtconcepts/analyze_design.html) in real time.

#### Using Floating-Point Multirate Filters

After you analyze the filter design, you can either use the multirate filter to process an input signal or [quantize the filter coefficients of the multirate filter](#quantize_design). Use the [Multirate Processing](/csh?topicname=lvdigfiltdestk/dfd_m_process_vis.html) VIs to process a signal with the multirate filter you designed. The Multirate Processing VIs can process an input signal in the following three ways:

- As a single block of data
- As a sequence of data blocks
- As a sequence of data blocks with saved internal filter states

Use the [DFD MRate Filtering for Single Block](/csh?topicname=lvdigfiltdestk/dfd_mr_s_block.html) VI or the [DFD NStage MRate Filtering for Single Block](/csh?topicname=lvdigfiltdestk/dfd_ns_mr_s_block.html) VI to process a single block of data. When processing a single block, the VIs extend the input signal block at both ends to ensure the output signal block has the same length as the input signal block. Use the other Multirate Processing VIs to process multiple signal blocks continuously. These VIs automatically retain the internal states of the filter between blocks, and they allow you to save and restore filter states without causing artifact glitches in the processed data.

You achieve the same results when you process multiple blocks as a sequence of blocks as when you process them together as one single block. To eliminate the delay between the input and output signals, enable the [zero-phase filtering](../lvdfdtconcepts/zero_phase_filtering.html) option when using the Multirate Processing VIs.

Refer to the Step 2 - Perform Decimation Filtering (MRate) VI in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter directory for an example that demonstrates how to use a decimation filter in a filtering application.

#### Quantizing Multirate Filter Coefficients

After you [analyze the filter design](#analyze_design), you can either quantize the filter coefficients of the designed multirate filter and convert the floating-point filter into a fixed-point filter or [use the floating-point multirate filter to process an input signal](#multirate_signal_processing). To quantize the filter coefficients, place a checkmark in the **Quantize filter** checkbox on the **Fixed-Point Quantization** tab, and specify the coefficients [word length](../lvdfdtconcepts/specify_wl_iwl.html), coefficients [scale type](../lvdfdtconcepts/scale_filter_coef.html), and [gain settings](../lvdfdtconcepts/quantize_fl_filters.html#gain_settings).

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/design_fp_filters.html language=enus -->
## TOPIC 00011: Designing Fixed-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/design_fp_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/design_fp_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Fixed-Point Filters (Digital Filter Design Toolkit)

This book explains how you use the [Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/dfd_fxp_tools_vis.html) VIs to implement a fixed-point digital filter from [a floating-point reference filter that you designed](../lvdfdtconcepts/design_fl_filters.html).

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/design_fp_multirate.html language=enus -->
## TOPIC 00012: Designing Fixed-Point Multirate Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/design_fp_multirate.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/design_fp_multirate.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Fixed-Point Multirate Filters (Digital Filter Design Toolkit)

The fixed-point multirate filter design process is different from the [fixed-point single-rate filter design process](../lvdfdtconcepts/dfd_fp_process.html). The following figure illustrates a typical fixed-point multirate filter design process. The grey boxes illustrate the [floating-point filter design process](../lvdfdtconcepts/dfd_fl_process.html) and the arrows on the left indicate to which steps you can return if the filter design fails to meet the requirements in the current step.

[IMAGE alt='image' src='typical_fixed-point_multirate_design_process.gif']

Designing a fixed-point multirate filter involves fewer steps than designing a fixed-point single-rate filter. The following sections describe each step in the fixed-point multirate filter design process and compare the process to the fixed-point single-rate filter design process.

#### Quantizing Floating-Point Multirate Filters

Use the [DFD FXP MRate Quantization](/csh?topicname=lvdigfiltdestk/dfd_fxp_mr_qua.html) VI to quantize floating-point multirate filters. This process is different from [quantizing floating-point single-rate filters](../lvdfdtconcepts/quantize_fl_filters.html).

In the fixed-point single-rate filter design process, [scaling the filter coefficients](../lvdfdtconcepts/scale_filter_coef.html) is a separate step. However, the fixed-point multirate filter design process integrates this step in the quantization process. Specify an appropriate value in the **scale type** input of the DFD FXP MRate Quantization VI to scale the multirate filter coefficients.

Depending on which VI you use to quantize the coefficients of a floating-point single-rate filter, you might need to configure some or all of the following items: the [gain settings](../lvdfdtconcepts/quantize_fl_filters.html#gain_settings), [word length and integer word length](../lvdfdtconcepts/specify_wl_iwl.html), [overflow mode](../lvdfdtconcepts/handle_overflow.html), and [rounding mode](../lvdfdtconcepts/set_rounding_mode.html). However, to quantize the coefficients of a floating-point multirate filter, you only need to set the gain processing target and coefficients word length. The DFD FXP MRate Quantization VI automatically calculates the integer word length of the filter coefficients and configures the settings for the overflow and rounding modes. The VI then uses the resulting values to quantize the filter coefficients.

Refer to the Step 3 - Analyze Quantized Decimation (MRate) VI in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter directory for an example that demonstrates how to quantize a floating-point decimation filter and [analyze the quantized decimation filter](../lvdfdtconcepts/design_fp_multirate.html#analysis).

#### Analyzing Fixed-Point Multirate Filters

[Quantization](#quantization) can cause the characteristics of a fixed-point multirate filter to deviate from the reference floating-point multirate filter. Sometimes quantization even causes the resulting fixed-point multirate filter to fail to meet the target specifications. Therefore, after quantization, you must analyze the behavior of the fixed-point multirate filter. You can use the [Multirate Filter Analysis](/csh?topicname=lvdigfiltdestk/dfd_m_analysis_vis.html) VIs to calculate the frequency response of the fixed-point multirate filter. Based on the frequency response results, you can determine if the fixed-point filter meets the requirements. If the fixed-point filter does not meet the target specifications, try either or both of the following methods:

- Modify the quantization settings for the word length of the coefficients .
- Modify the specifications of the reference floating-point multirate filter to allow larger headroom. A larger headroom helps alleviate fixed-point effects.

To optimize the resulting multirate fixed-point filter, analyze and adjust the filter design iteratively until the frequency response meets the target specifications.

Refer to the Step 3 - Analyze Quantized Decimation (MRate) VI in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter directory for an example that demonstrates how to [quantize a floating-point decimation filter](../lvdfdtconcepts/design_fp_multirate.html#quantization) and analyze the quantized decimation filter.

#### Creating Fixed-Point Multirate Filter Models

When you design a fixed-point multirate filter, fixed-point quantization occurs for the coefficients and for the intermediate operands and results. By using the [DFD FXP MRate Modeling](/csh?topicname=lvdigfiltdestk/dfd_fxp_mr_mod.html) VI, you need to configure only the quantizers for the input and output signals. The DFD FXP MRate Modeling VI automatically configures the quantizers for intermediate operands.

##### Setting the Input Word Length, Input Integer Word Length, and Output Word Length

Use the DFD FXP MRate Modeling VI to specify input word length, input integer word length, and output word length. These word lengths determine the number of bits to use in representing the input and output signals. The DFD FXP MRate Modeling VI automatically configures the integer word length of the output signal.

##### Setting the Rounding Mode

Fixed-point numbers have limited word lengths, so the available dynamic range of fixed-point numbers is lower than the range available with double-precision and floating-point numbers. Therefore, fixed-point numbers can approximate floating-point numbers only. In the LabVIEW Digital Filter Design Toolkit, the [Multirate Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/mr_fxp_tools.html) VIs use up to 48 bits for internal operations. Use the **output rounding mode** input of the DFD FXP MRate Modeling VI to configure the output quantizer.

Refer to the Step 4 - Model and Simulate FXP Decimation (MRate) VI in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter directory for an example that demonstrates how to create a fixed-point model of a multirate filter and [simulate the filtering result](../lvdfdtconcepts/design_fp_multirate.html#simulation).

#### Simulating Fixed-Point Multirate Filters

To determine the [quantization](#quantization) and [modeling](#modeling) effects on a filtering process, you not only need to [analyze](#analysis) the frequency response of a fixed-point filter, but you also need to simulate the filtering process with the actual data. You can use the [DFD FXP MRate Simulation](/csh?topicname=lvdigfiltdestk/dfd_fxp_mr_sim.html) VI to simulate the filtering process. To verify if the fixed-point multirate filter works as you expect, compare the simulation result with the actual filtering result that you obtain by processing the same signal with the reference floating-point multirate filter. Ensure that the simulation result matches the actual filtering result. If the simulation result does not match the actual floating-point filtering result, try making the following adjustments:

- Return to the quantization step. Modify the word length for the filter coefficients and the scale type to avoid overflow or underflow.
- Adjust the specifications and redesign the floating-point multirate filter .

Refer to the Step 4 - Model and Simulate FXP Decimation (MRate) VI in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter directory for an example that demonstrates how to [create a fixed-point model of a multirate filter](../lvdfdtconcepts/design_fp_multirate.html#modeling) and simulate the filtering result.

#### Generating Code from Fixed-Point Multirate Filters

After you [obtain an appropriate fixed-point filter model](#modeling), you can implement the resulting fixed-point filter on target hardware. You can export fixed-point integer coefficients from the filter and then use the coefficients in a filter execution engine. You also can generate LabVIEW FPGA code and then use the LabVIEW FPGA Module to target and deploy the resulting FPGA code to an NI Reconfigurable I/O (RIO) target.

##### Exporting Fixed-Point Integer Coefficients

If you have a filter execution engine for which you need only filter coefficients, you can export the fixed-point multirate filter coefficients to a text file using the [DFD Save to Text File](/csh?topicname=lvdigfiltdestk/dfd_save_to_text.html) VI. You can save the multirate filter coefficients to a text file and load them to the execution target. The text file contains a section that provides all information about the fixed-point integer coefficients and corresponding quantizers.

Refer to the Export Multirate FIR Coefficients to Xilinx COE File VI in the labview\examples\Digital Filter Design\Fixed-Point Filters\Multirate directory for an example that demonstrates how to export fixed-point integer coefficients.

##### Generating LabVIEW FPGA Code

You can use the **Start IP Generator** dialog box or the [DFD FXP MRate Code Generator](/csh?topicname=lvdigfiltdestk/dfd_fxp_mr_gen.html) VI to generate LabVIEW field-programmable gate array (FPGA) code from a multirate filter.

|  | Note To generate LabVIEW FPGA code, you must install the LabVIEW FPGA Module and NI-RIO driver software. To execute the FPGA code, you also need an FPGA target on which to run the code. Refer to the National Instruments Web site for information about these products. |
| --- | --- |

The Digital Filter Design Toolkit [uses LabVIEW projects](/csh?topicname=lvconcepts/using_labview_projects.html) to manage the resulting LabVIEW FPGA code. The following figure shows an example project file that contains LabVIEW FPGA code.

[IMAGE alt='image' src='fpga_project_mrate.gif']

In the previous figure, the *filtername*.lvproj file, where *filtername* denotes the name of the fixed-point filter, contains the following folder and VI in addition to the default items.

- filtername Block —This folder contains the generated filter VI. You can apply the filter to another project by copying and pasting this folder into the target project file.
- filtername_DataOut —This item defines the output FIFO channel from the filter block of a fixed-point multirate filter. If you want to return the filtered signal directly to a host computer, you can modify the property of this file by completing the following steps:
  1. Right-click filtername_DataOut .
  2. Choose Properties from the shortcut menu.
  3. Choose Target to Host-DMA from the Type menu.
  4. Click OK .
- filtername_DataIn —This item defines the input FIFO channel to the filter block of a fixed-point multirate filter. The fixed-point multirate filter uses the FIFO to communicate with other sections of the FPGA code, such as the FPGA I/O Node.
- filtername_Filter.vi —This VI is the top-level VI of the generated LabVIEW FPGA code. To use the LabVIEW FPGA code, drag and drop this VI to the block diagram of the calling VI. [IMAGE alt='image' src='note.gif']
**Note** The LabVIEW FPGA code you generate with the LabVIEW Digital Filter Design Toolkit supports only the fixed-point data type.

The way you use LabVIEW FPGA code is different from the way you use a general LabVIEW VI. The following figure shows an example of a block diagram that uses LabVIEW FPGA code generated from the *filtername*_Filter VI.

[IMAGE alt='image' src='decimate_code.gif']

In the previous figure, the *filtername*_Filter VI is not connected to any other items on the block diagram. However, this VI actually communicates with the items in the loop structures by processing the input signal from the *filtername*_DataIn FIFO and returning the output signal to the *filtername*_DataOut FIFO.

You can generate LabVIEW FPGA code from a fixed-point single-stage multirate filter by using the **Start IP Generator** dialog box or the DFD FXP MRate Code Generator VI. Refer to the MRate Decimation.lvproj file in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter\MRateDecimation directory for an example that demonstrates how to generate LabVIEW FPGA code from a fixed-point single-stage decimation filter and implement the resulting LabVIEW FPGA code on a PXI target.

Refer to the MRate Interpolation.lvproj file in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter\MRateInterpolation directory for an example that demonstrates how to generate LabVIEW FPGA code from a fixed-point single-stage interpolation filter and implement the resulting LabVIEW FPGA code on a CompactRIO target.

You can generate LabVIEW FPGA code from a fixed-point [multistage multirate filter](../lvdfdtconcepts/mstage_mrate_filt.html) by using the **Start IP Generator** dialog box or the [DFD FXP NStage MRate Code Generator](/csh?topicname=lvdigfiltdestk/dfd_ns_mr_gen.html) VI. Refer to the NStageMRate Decimation.lvproj file in the labview\examples\Digital Filter Design\Case Studies\Multistage Multirate Filter\NStageMRate directory for an example that demonstrates how to generate LabVIEW FPGA code from a fixed-point multistage multirate filter and implement the resulting LabVIEW FPGA code on a PXI target.

You also can generate LabVIEW FPGA code from a fixed-point moving average filter by using the **Start IP Generator** dialog box or the [DFD FXP Moving Average Code Generator](/csh?topicname=lvdigfiltdestk/dfd_fxp_ma_gen.html) VI.

##### Postprocessing Filtered Signals

After you deploy fixed-point filter coefficients to the target hardware, you can [postprocess the filtered signal](../lvdfdtconcepts/postprocess_srate.html) using the [DFD FXP MRate Postprocessing](/csh?topicname=lvdigfiltdestk/dfd_fxp_mr_pos.html) VI. Refer to the Step 6 - Postprocessing VI in the labview\examples\Digital Filter Design\Case Studies\Multirate Filter directory for an example that demonstrates how to postprocessing a filtered signal.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/design_methods.html language=enus -->
## TOPIC 00013: Design Methods (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/design_methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/design_methods.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Design Methods (Digital Filter Design Toolkit)

The LabVIEW Digital Filter Design Toolkit provides the following finite impulse response (FIR) filter design methods.

- Kaiser Window
- Dolph-Chebyshev Window
- Equi-Ripple FIR

The Kaiser Window method and the Dolph-Chebyshev Window method allows you to obtain the filter coefficients directly from the analytical equations, so these methods are easier to use than the Equi-Ripple FIR method, which also is known as the [Remez design method](../lvdfdtconcepts/remez_designmethod.html), but the Equi-Ripple FIR method yields optimal filters and often produces the best results for most FIR filter design problems.

In addition to the FIR-based methods, the Digital Filter Design Toolkit supports the following infinite impulse response (IIR) filter design methods.

- Butterworth
- Chebyshev
- Inverse Chebyshev
- Elliptic

The following figure illustrates the magnitude responses of a typical lowpass filter designed by the four IIR filter design methods. Each filter has the same numerator and denominator order values.

[IMAGE alt='image' src='iir-design-methods.gif']

The following table summarizes the main features of the four IIR-based design methods so you can determine the IIR filter design method to use.

| IIR Filter | Ripple in Passband? | Ripple in Stopband? | Transition Bandwidth for a Fixed Order | Order for Given Filter Specifications |
| --- | --- | --- | --- | --- |
| Butterworth | No | No | Widest | Highest |
| Chebyshev | Yes | No | Narrower | Lower |
| Inverse Chebyshev | No | Yes | Narrower | Lower |
| Elliptic | Yes | Yes | Narrowest | Lowest |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/design_mrate.html language=enus -->
## TOPIC 00014: Designing Multirate Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/design_mrate.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/design_mrate.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Multirate Filters (Digital Filter Design Toolkit)

This book contains information about using the LabVIEW Digital Filter Design Toolkit to design [multirate filters](../lvdfdtconcepts/dfdt_concepts_intro.html).

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/design_special_mrate.html language=enus -->
## TOPIC 00015: Designing Special Multirate Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/design_special_mrate.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/design_special_mrate.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Special Multirate Filters (Digital Filter Design Toolkit)

This book discusses how to design [cascaded integrator comb](../lvdfdtconcepts/cic_filters.html), [Nyquist](../lvdfdtconcepts/nyquist_filters.html), and [multistage](../lvdfdtconcepts/mstage_mrate_filt.html) multirate filters.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_basics.html language=enus -->
## TOPIC 00016: Digital Filter Design Basics (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_basics.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_basics.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Digital Filter Design Basics (Digital Filter Design Toolkit)

Before using the LabVIEW Digital Filter Design Toolkit to design a digital filter, you need to obtain an overview of the [general design process](../lvdfdtconcepts/dfd_process.html) and [application areas](../lvdfdtconcepts/digital_filter_app.html) of digital filters.

When you design a digital filter, you begin by creating specifications that define the characteristics you want in the digital filter. You can design both [FIR and IIR filters](../lvdfdtconcepts/fir_and_iir_filters.html) with specific [filter attributes](../lvdfdtconcepts/filter_attributes.html), and you can customize the [sampling frequency](../lvdfdtconcepts/sampling_frequency.html), [filter specifications](../lvdfdtconcepts/dfd_filter_spec.html), and [design method](../lvdfdtconcepts/design_methods.html). After you design a digital filter, you need to analyze the characteristics of the digital filter by evaluating the magnitude and impulse responses, [phase responses and group delays](../lvdfdtconcepts/grp_phase_delay.html), or [poles and zeroes](../lvdfdtconcepts/poles_and_zeroes.html). The Digital Filter Design Toolkit provides the [Filter Analysis](/csh?topicname=lvdigfiltdestk/dfd_analysis_vis.html) VIs to help you evaluate the characteristics of a filter.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_decimation.html language=enus -->
## TOPIC 00017: Decimation (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_decimation.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_decimation.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Decimation (Digital Filter Design Toolkit)

Decimation is the process of reducing the sampling frequency of a signal to a lower sampling frequency that differs from the original frequency by an integer value. Decimation also is known as down-sampling. The lowpass filtering associated with decimation removes high-frequency content from the signal to accommodate the new sampling frequency.

Decimation is useful in applications in which the Nyquist frequency of a signal is much higher than the highest frequency of the signal. Decimation filters help you remove the excess bandwidth and reduce the sampling frequency of the signal. Decimation filters also help you reduce the computational resources required for processing and storing the signal. During the analog-to-digital (A/D) conversion process, decimation filters also can reduce the variance of quantization noise in a signal and maintain the signal power, thus improving the signal-to-noise ratio (SNR).

The following figure shows a typical *M*-fold decimation filter, where *M* is the integer value by which you want to decrease the sampling frequency. This filter contains a lowpass FIR filter *H*(*z*). This lowpass FIR filter is an anti-aliasing filter followed by an *M*-fold decimator. The decimator passes every *M*<sup>th</sup> sample and discards the other samples. After this operation, the decimation filter changes the sampling frequency *f*<sub>*s*</sub> of the input signal *x*(*n*) to a new sampling frequency *f*<sub>*s*</sub>/*M*. The decimation filter then returns an output signal *y*(*n*) with the new sampling frequency.

[IMAGE alt='image' src='decimation_fil.gif']

To prevent aliasing, this system uses the lowpass filter *H*(*z*) before the *M*-fold decimator to suppress the frequency contents above the frequency *f*<sub>*s*</sub>/(2*M*), which is the Nyquist frequency of the output signal. This system produces the same results as an analog anti-aliasing filter with a cutoff frequency of *f*<sub>*s*</sub>/(2*M*) followed by an analog-to-digital (A/D) converter with a sampling frequency of *f*<sub>*s*</sub>/*M*. Because the system shown in the figure above is in the digital domain, *H*(*z*) is a digital anti-aliasing filter.

|  | Note The Multirate Processing VIs use a polyphase implementation, which is more efficient than the procedure in the previous figure, to implement decimation. Refer to the book Multirate Systems and Filter Banks for more information about polyphase implementations. Decimation filters that use a polyphase implementation compute only the final expected output samples, not the samples to discard, thus reducing the computational complexity of the filters. |
| --- | --- |

The following figure illustrates the potentially harmful effects of not using an anti-aliasing filter before the decimator. This figure shows the spectrum of the original signal *x*(*n*) and the spectra of the signals resulting from decimating the original signal by 2, 3, and *M*. Notice the overlapping spectra in parts (c) and (d) of the figure. The overlapping spectra indicate aliasing due to the decimation operation.

[IMAGE alt='image' src='decimation_no_anti-aliasing.gif']

| (a) Spectrum of the original signal x(n) |
| --- |
| (b) Spectrum of the output signal y(n), decimated by a factor of 2 |
| (c) Spectrum of the output signal y(n), decimated by a factor of 3 |
| (d) Spectrum of the output signal y(n), decimated by a factor of M |

To design decimation filters, use the [Multirate Filter Design](/csh?topicname=lvdigfiltdestk/dfd_multi_design_vis.html) VIs with the **filtering mode** input set to Decimation.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_design_fbanks.html language=enus -->
## TOPIC 00018: Designing Filter Banks (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_design_fbanks.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_design_fbanks.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Filter Banks (Digital Filter Design Toolkit)

This book contains information about using the LabVIEW Digital Filter Design Toolkit to design filter banks.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_enter_fbank_spec.html language=enus -->
## TOPIC 00019: Entering Filter Bank Specifications (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_enter_fbank_spec.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_enter_fbank_spec.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Entering Filter Bank Specifications (Digital Filter Design Toolkit)

You can use the [Filter Bank Design](/csh?topicname=lvdigfiltdestk/dfd_fbankdesign.html) Express VI to configure a filter bank interactively. After you add the Express VI to the block diagram, the **Configure DFD Filter Bank Design** dialog box appears, as shown in the following figure.

[IMAGE alt='image' src='configure_dfd_fbank_design_dialog.gif']

From the configuration dialog box, you can select the filter bank type and phase option from the pull-down menus and then enter the filter bank specifications through the numeric controls. You can analyze the filter bank distortions and the frequency responses at the top of the configuration dialog box.

#### Considerations for Filter Bank Specifications

When you define a filter bank specification, take the following factors into consideration:

- With the same filter bank specifications, near-perfect reconstruction (NPR) cosine-modulated filter banks offer better frequency selectivity than perfect reconstruction (PR) cosine-modulated filter banks, as illustrated in the following figure.
 [IMAGE alt='image' src='npr_fbank_freq_selectivity.gif']
- The actual roll-off has a slight difference from the specified roll-off, which specifies the relative transition bandwidth.
- If the specified stopband attenuation is too high, the actual stopband attenuation may not meet the specified stopband attenuation.

#### Analyzing the Filter Bank Design

The top of the **Configure DFD Filter Bank Design** dialog box displays the frequency response and distortion analysis of the filter bank. In the **Distortion Analysis** section, you can examine the [aliasing](dfd_fbank_distortions.html#aliasing), [magnitude distortion](dfd_fbank_distortions.html#mag_phase_distortion), and [phase distortion](dfd_fbank_distortions.html#mag_phase_distortion) in the filter bank. In the **Frequency Responses** section, you can analyze the [frequency selectivity](dfd_fbank_basics.html#freq_selectivity) by examining the frequency responses of the analysis bank. You can examine the magnitude response and phase response of the analysis bank or a specified analysis filter.

Remove the checkmark from the **Magnitude in dB** checkbox to use a linear scale, or keep the checkmark in the **Magnitude in dB** checkbox to use a logarithmic scale. Place a checkmark in the **Unwrap Phase** checkbox to unwrap the phase so it is not limited to [0, 2[IMAGE alt='image' src='pi.gif']).

#### Using Filter Banks

After you design a filter bank, you can use the [Filter Bank Processing](/csh?topicname=lvdigfiltdestk/dfd_fbankprcs.html) VIs to process a signal. You can use the decomposition VIs to decompose an input signal into several subband signals and use the reconstruction VIs to reconstruct a signal from subband signals.

Each polymorphic VI can process two kinds of signal:

- An array of DBLs
- A waveform

Use the [DFD 2-Band Filter Bank Decomposition](/csh?topicname=lvdigfiltdestk/dfd_2bandfbankdecomp.html) VI or the [DFD M-Band Filter Bank Decomposition](/csh?topicname=lvdigfiltdestk/dfd_mbandfbankdecomp.html) VI to decompose the signal into two or more uniformly spaced subband signals. Use the [DFD 2-Band Filter Bank Reconstruction](/csh?topicname=lvdigfiltdestk/dfd_2bandfbankreconstruct.html) VI or the [DFD M-Band Filter Bank Reconstruction](/csh?topicname=lvdigfiltdestk/dfd_mbandfbankreconstruct.html) VI to reconstruct a signal from two or more uniformly spaced subband signals. These VIs automatically retain the internal states of the filter bank between continuous input blocks.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_fbank_basics.html language=enus -->
## TOPIC 00020: Filter Bank Design Basics (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_fbank_basics.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_fbank_basics.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Filter Bank Design Basics (Digital Filter Design Toolkit)

In modern signal processing, many applications use filter banks to decompose a signal into several narrower frequency ranges, which are convenient for further processing. For example, adaptive filter applications use filter banks to reduce computational complexity and improve the convergence performance by decomposing a high-order adaptive filter into several low-order adaptive filters. Audio processing applications use filter banks for room simulation and digital audio compression. Digital communications applications use filter banks in digital transmultiplexers, channel equalization precoding, and discrete multitone modulation. Before using filter banks, you must have some basic knowledge of [multirate filters](design_mrate.html).

#### Filter Bank Structure

A filter bank has two parts: an analysis bank and a synthesis bank. Each bank is a set of [bandpass](dfd_filter_spec.html) filters. The filters in the analysis bank are analysis filters and the filters in the synthesis bank are synthesis filters. The following figure shows the structure of a filter bank.

[IMAGE alt='image' src='filter_bank_structure.gif']

The analysis bank consists of *M* analysis filters *H*<sub>k</sub>(*z*), where *k* represents the *k*th subband. [Uniform filter banks](dfd_fbank_categories.html#fbank_uniformity) in the LabVIEW Digital Filter Design Toolkit have the property that the number of subbands, *M*, is equal to the decimation factor of the subband filters. The analysis filters, *H*<sub>k</sub>(*z*), decompose the input signal, *x*[*n*], into multiple subband signals, *V*<sub>k</sub>[*n*]. Each subband signal carries a specific frequency range of the input signal. The synthesis filters, *F*<sub>k</sub>(*z*), reconstruct the original signal, *y*[*n*], from the processed subband signals, *W*<sub>k</sub>[*n*].

#### Criteria for Designing Filter Banks

When designing filter banks, it is important to consider the signal reconstruction and frequency selectivity.

##### Perfect or Near-Perfect Reconstruction

If you do not apply a processing unit to the subband signals, the synthesis bank reconstructs the original signal, perfectly or near-perfectly. You can evaluate the signal reconstruction by examining [distortions](dfd_fbank_distortions.html) in the filter bank. There are three fundamental distortions in filter banks: [aliasing](dfd_fbank_distortions.html#aliasing), [magnitude distortion](dfd_fbank_distortions.html#mag_phase_distortion), and [phase distortion](dfd_fbank_distortions.html#mag_phase_distortion). If a filter bank is free from these distortions, the filter bank is a perfect reconstruction (PR) filter bank. If these distortions are small, the filter bank is a near-perfect reconstruction (NPR) filter bank. If a filter bank has perfect reconstruction, the output signal is a scaled and delayed version of the input signal.

##### Frequency Selectivity

Frequency selectivity indicates the ability of a filter bank to separate frequency subbands. Each subband contains signal components in a different frequency range. You can evaluate the frequency selectivity by examining the stopband attenuation and the transition bands. To achieve good frequency selectivity, the filter bank must have a high stopband attenuation and narrow transition bands.

It is often difficult to design PR filter banks that achieve good frequency selectivity. However, NPR filter banks can achieve high stopband attenuation and narrow transition bands while introducing only small distortions. Thus, in practice, NPR filter banks often have better frequency selectivity than PR filter banks. Consequently, many real-world applications use NPR filter banks instead of PR filter banks.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_fbank_categories.html language=enus -->
## TOPIC 00021: Categorizing Filter Banks (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_fbank_categories.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_fbank_categories.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Categorizing Filter Banks (Digital Filter Design Toolkit)

You can categorize filter banks according to the bandwidths of the subbands or the number of subbands.

#### Uniform and Non-Uniform Filter Banks

You can categorize filter banks into uniform filter banks and non-uniform filter banks according to the bandwidths of the subbands. The following figure shows the magnitude response of a uniform filter bank.

[IMAGE alt='image' src='uniform_fbank_mag_resp.gif']

The filter bank separates the signal spectrum into uniformly spaced subbands. Uniform filter banks in the LabVIEW Digital Filter Design Toolkit have the property that the number of subbands is equal to the decimation factor of the subband filters. This is known as a critically sampled uniform filter bank. The subband number of a critically sampled uniform filter bank is equivalent to the decimation factor *M*, with subband bandwidth 2[IMAGE alt='image' src='pi.gif']/*M*.

A uniform filter bank has uniformly spaced subband bandwidths, which results in a fixed subband resolution in all frequency areas. The following figure illustrates how a non-uniform filter bank can have different subband resolutions in different frequency areas.

[IMAGE alt='image' src='non_uniform_fbank_mag_resp.gif']

In the previous figure, the subband bandwidth in the lower frequency area is narrower than the subband bandwidth in the higher frequency area. Therefore, this non-uniform filter bank can achieve a higher resolution than a uniform filter bank in the low frequency area.

#### 2-band and M-band Filter Banks

You also can categorize filter banks as 2-band and M-band filter banks according to the number of subbands.

Wavelet analysis uses 2-band filter banks, also called quadrature mirror filter (QMF) filter banks. In a QMF filter bank, the magnitude responses of the lowpass band filter and the highpass band filter in the analysis bank are symmetric about [IMAGE alt='image' src='pi.gif']/2.

One approach to M-band filter bank design is to apply a cosine modulation to a prototype lowpass filter. The M-band cosine-modulated filter banks used in the LabVIEW Digital Filter Design Toolkit are critically sampled filter banks.

The advantages of cosine-modulated filter bank design are as follows.

- You can reduce the design complexity as you need to design only one prototype lowpass filter. The analysis and synthesis filters are frequency-shifted versions of the prototype filter.
- It is feasible to design perfect reconstruction cosine-modulated filter banks.
- The analysis and synthesis filters have real-valued coefficients.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_fbank_distortions.html language=enus -->
## TOPIC 00022: Distortions (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_fbank_distortions.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_fbank_distortions.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Distortions (Digital Filter Design Toolkit)

There are three fundamental distortions in filter banks: aliasing, magnitude distortion, and phase distortion.

#### Aliasing

The following figure shows a [2-band uniform filter bank](dfd_fbank_categories.html#2_band_m_band_fbanks) with no processing unit applied.

[IMAGE alt='image' src='2band_fbank_structure.gif']

In practice, the magnitude responses of the lowpass band analysis filter, *H*<sub>0</sub>(*e*<sup>*jω*</sup>), and the highpass band analysis filter, *H*<sub>1</sub>(*e*<sup>*jω*</sup>), overlap with each other, as shown in the following figure.

[IMAGE alt='image' src='fbank_analysis_filter_overlap.gif']

The following figure shows the spectrum *X*(*e*<sup>*jω*</sup>) of the input signal *x*[*n*].

[IMAGE alt='image' src='fbank_input_signal.gif']

The lowpass band analysis filter, *H*<sub>0</sub>(*z*), filters the input signal to give the lowpass band signal *x*<sub>0</sub>[*n*]. The spectrum of the lowpass band signal, *X*<sub>0</sub>(*e*<sup>*jω*</sup>), is shown in the following figure.

[IMAGE alt='image' src='fbank_lowpass_spectrum.gif']

The filter bank [decimates](dfd_decimation.html) *x*<sub>0</sub>[*n*] by a factor of 2 to give the decimated lowpass band signal *v*<sub>0</sub>[*n*]. After decimation, the spectrum is given by *V*<sub>0</sub>(*e*<sup>*jω*</sup>) = 0.5*X*<sub>0</sub>(*e*<sup>*jω*</sup><sup>/2</sup>) + 0.5*X*<sub>0</sub>(–*e*<sup>*jω*</sup><sup>/2</sup>). The component 0.5*X*<sub>0</sub>(–*e*<sup>*jω*</sup><sup>/2</sup>) overlaps with the component 0.5*X*<sub>0</sub>(*e*<sup>*jω*</sup><sup>/2</sup>), which leads to aliasing in the filter bank, shown as the overlapping area in the following figure.

[IMAGE alt='image' src='fbank_aliasing.gif']

The filter bank then [interpolates](dfd_interpolation.html) *v*<sub>0</sub>[*n*] by a factor of 2. The lowpass band synthesis filter, *F*<sub>0</sub>(*z*), filters the signal and returns the lowpass band output signal *y*<sub>0</sub>[*n*]. The following figure shows the spectrum of the lowpass band output signal, *Y*<sub>0</sub>(*e*<sup>*jω*</sup>).

[IMAGE alt='image' src='fbank_lowpass_output.gif']

In the previous figure, the shaded area is the aliasing component in the lowpass band output signal. Similarly, the following figure shows the spectrum of the highpass band output signal *Y*<sub>1</sub>(*e*<sup>*jω*</sup>). The shaded area is the aliasing component in the highpass band output signal.

[IMAGE alt='image' src='fbank_highpass_output.gif']

You cannot avoid aliasing in the analysis bank if the magnitude response of the lowpass band analysis filter and the highpass band analysis filter overlap with each other. However, you can cancel the aliasing by choosing the correct synthesis filters. The [Filter Bank Design](/csh?topicname=lvdigfiltdestk/dfd_fbankdesignpal.html) VIs automatically choose the correct synthesis filters to cancel aliasing in the analysis bank.

#### Magnitude Distortion and Phase Distortion

Disregarding the aliasing effect, assuming the equivalent frequency response of the filter bank is *T*(*e*<sup>*jω*</sup>) = |*T*(*e*<sup>*jω*</sup>)|*e*<sup>*jΦ(ω)*</sup>, then *Y*(*e*<sup>*jω*</sup>) = *X*(*e*<sup>*jω*</sup>)*T*(*e*<sup>*jω*</sup>) . If |*T*(*e*<sup>*jω*</sup>)| is not flat, the filter bank has a magnitude distortion. The following figure shows the magnitude distortion in a [near-perfect reconstruction](dfd_fbank_basics.html#sig_reconstruct) (NPR) filter bank.

[IMAGE alt='image' src='fbank_magnitude_distortion.gif']

If *T*(*e*<sup>*jω*</sup>) does not have a linear phase, the filter bank has a phase distortion. The filter banks used in the LabVIEW Digital Filter Design Toolkit contain no phase distortion.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_fbank_process.html language=enus -->
## TOPIC 00023: Filter Bank Design Process (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_fbank_process.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_fbank_process.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Filter Bank Design Process (Digital Filter Design Toolkit)

The following figure illustrates the filter bank design process. You first design a filter bank that meets the target specifications. You then [analyze](dfd_enter_fbank_spec.html#analyzing_the_filter_bank_design) the characteristics of the resulting filter bank to determine if the filter bank meets the requirements of the system. If the filter bank does not meet the requirements of the system, you can modify the specifications and repeat the process. After you design an appropriate filter bank, you can [use the filter bank](dfd_enter_fbank_spec.html#using_filter_banks) in the system.

[IMAGE alt='image' src='fbank_design_process.gif']

For a particular design problem, you can use several different techniques and filter bank types to yield an acceptable result. To achieve the best results, you might need to experiment with several different approaches.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_filter_spec.html language=enus -->
## TOPIC 00024: Filter Specifications (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_filter_spec.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_filter_spec.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Filter Specifications (Digital Filter Design Toolkit)

For most digital filters, you typically design the digital filter response in the frequency domain. The frequency response specification for the digital filter typically includes the target magnitude response, phase response, and the allowable deviation for each. The following figure illustrates the magnitude frequency response of a lowpass filter, which allows low frequencies to pass and attenuates high frequencies.

[IMAGE alt='image' src='lowpass.gif']

The frequency range from the passband edge frequency to the stopband edge frequency is the transition band, which has a frequency response that is unspecified. The filter passband and stopband can contain oscillations, which are known as ripples. A typical example of a ripple appears in the circle of the previous figure. *δ*<sub>*p*</sub> indicates the magnitude of the passband ripple, which equals the maximum deviation from the unity. *δ*<sub>*s*</sub> indicates the magnitude response of the stopband ripple, which equals the maximum deviation from zero.

Notice the transition band between the passband and stopband frequencies. In an ideal design, a digital filter has a target gain in the passband and a zero gain (−∞ dB) in the stopband. In a real implementation, a finite transition region between the passband and the stopband, which is known as the transition band, always exists. The gain of the filter in the transition band is unspecified. The gain usually changes gradually through the transition band from 1 (0 dB) in the passband to 0 (−∞ dB) in the stopband.

You can measure the passband ripple and stopband ripple in decibels, as shown in the following equations:

passband ripple = −20log<sub>10</sub>(1−*δ*<sub>*p*</sub>)

stopband ripple = −20log<sub>10</sub>(*δ*<sub>*s*</sub>)

Based on the two equations above, you can convert the passband ripple to or from the decibel representation. For example, if passband ripple equals 0.01 dB, that is, 0.01 = −20log<sub>10</sub>(1−*δ*<sub>*p*</sub>), then *δ*<sub>*p*</sub> = 0.00115. Similarly, if stopband ripple equals 60 dB, that is 60 = −20log<sub>10</sub>(*δ*<sub>*s*</sub>), then *δ*<sub>*s*</sub> = 0.001.

The following figure illustrates the magnitude frequency responses of a highpass filter, which passes high frequencies and attenuates low frequencies.

[IMAGE alt='image' src='highpass.gif']

The following figure illustrates the magnitude frequency responses of a bandpass filter, which passes a certain band of frequencies and attenuates lower and higher frequencies.

[IMAGE alt='image' src='bandpass.gif']

In the previous figure, stopband edge frequency 1 indicates the maximum frequency of the lower frequency range that you want to attenuate, and stopband edge frequency 2 indicates the minimum frequency of the higher frequency range that you want to attenuate. The frequency range between passband edge frequency 1 and 2 indicates the range of frequencies that can pass through the filter.

The following figure illustrates the magnitude frequency response of a bandstop filter, which attenuates a certain band of frequencies and passes all frequencies not within the band.

[IMAGE alt='image' src='bandstop.gif']

In the previous figure, passband edge frequency 1 indicates the maximum frequency of the lower frequency range that can pass through the filter, and passband edge frequency 2 indicates the minimum frequency of the higher frequency range that can pass through the filter. The frequency range between stopband edge frequency 1 and 2 indicates the range of frequencies that you want to attenuate.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_fl_process.html language=enus -->
## TOPIC 00025: Floating-Point Filter Design Process (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_fl_process.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_fl_process.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Floating-Point Filter Design Process (Digital Filter Design Toolkit)

The following figure illustrates the floating-point filter design process. You first design a filter that meets the target specifications. You then [analyze](analyze_design.html) the characteristics of the resulting filter to determine if the filter meets the requirements of the system. If the filter does not meet the requirements of the system, you can modify the specifications and repeat the process. After you design an appropriate filter, you can [use the filter](use_fl_filters.html) in the system.

[IMAGE alt='image' src='fp-diag.gif']

For a particular design problem, you can use several different techniques and filter types to yield an acceptable result. To achieve the best results, you might need to experiment with several different approaches.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_fp_process.html language=enus -->
## TOPIC 00026: Fixed-Point Filter Design Process (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_fp_process.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_fp_process.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Fixed-Point Filter Design Process (Digital Filter Design Toolkit)

Fixed-point signal processing platforms, such as fixed-point digital signal processors (DSPs) and field-programmable gate arrays (FPGAs), are typically more power-efficient and less expensive than floating-point alternatives. However, fixed-point systems are generally more difficult to design. For example, you must consider the effects of coarser quantizations in fixed-point systems.

To design a fixed-point filter, you first must [design a floating-point filter](../lvdfdtconcepts/design_fl_filters.html), also known as a reference filter, that meets the target specifications. In some cases, for example, if you need an infinite impulse response (IIR) filter with a narrow transition band but a high stopband attenuation, you need to design a reference filter that exceeds the target specifications. The excess margin ensures a smooth conversion from a floating-point representation to a fixed-point representation. You then must modify the floating-point filter to accommodate the finite-precision constraints of the target platform while still trying to meet the target specifications. The following figure illustrates the fixed-point filter design process. The grey boxes illustrate the [floating-point filter design process](../lvdfdtconcepts/dfd_fl_process.html), the dotted lines represent optional steps, and the arrows on the left indicate to which steps you can return if the filter design fails to meet the requirements in the current step.

[IMAGE alt='image' src='full-diag.gif']

Designing a fixed-point filter from a reference floating-point filter involves the following steps:

1. Selecting a filter structure . In floating-point filter design, after you select a design method , the LabVIEW Digital Filter Design Toolkit uses a default filter structure according to the specified design method. However, in fixed-point implementations, different filter structures can have different memory and multiplier requirements and might cause different finite word length effects . To obtain the best filtering results, you must convert the default filter structure to an appropriate structure. This step is optional.
2. Scaling the filter coefficients . Every filter structure contains many accumulators , each of which might use a different data range. You can scale the filter coefficients by using the DFD Scale Filter VI to ensure that all of the accumulators use the same data range. Scaling the filter coefficients can help you obtain a better filtering result, especially for IIR Cascaded Second-Order Sections Form structures . This step is optional.
3. Quantizing the floating-point filter . Quantization is the process of approximating a fixed-point value for each reference floating-point value. You then can use the fixed-point values in fixed-point mathematical computation or a hardware implementation. By quantizing the coefficients of the reference floating-point filter, you convert a floating-point filter to a fixed-point filter.
4. Analyzing the fixed-point filter . To determine how the characteristics of the realized fixed-point filter deviate from the characteristics of the reference floating-point filter, you must analyze the fixed-point filter.
5. Creating a fixed-point filter model . To create the fixed-point filter model, you must configure the quantizers for the input and output signals and specify the settings for internal computation.
6. Simulating the fixed-point filter . Before applying the fixed-point filter model in real-world applications, you must simulate the behavior of the filter to verify if the fixed-point filter model works as you require in a simulation. If the fixed-point filter does not provide the required performance in the simulation, you can change the implementation structure, modify quantization settings, or redefine the filter specifications for the reference floating-point filter.
7. Generating code from the fixed-point filter . You can export filter coefficients and automatically generate integer LabVIEW code, LabVIEW FPGA code, and C code from the fixed-point filter for designated hardware targets.

#### Finite Word Length Effects

Converting a floating-point filter to fixed-point can alter the characteristics and performance of the filter significantly. You must analyze the filter and simulate the filtering process with expected input signals. Fixed-point arithmetic can have the following detrimental effects on filter performance.

- Degraded signal-to-noise ratio (SNR) due to the reduced precision of internal registers, adders, subtracters, and multipliers
- Distorted frequency response from a limited word length representation of filter coefficients
- Overflowed or clipped signal information due to insufficient headroom in the signal paths
- Zero-input limit cycles of infinite impulse response (IIR) filters due to nonlinear quantizers in the feedback loop of IIR filters or to the overflow of the summation operations

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_interpolation.html language=enus -->
## TOPIC 00027: Interpolation (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_interpolation.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_interpolation.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Interpolation (Digital Filter Design Toolkit)

Interpolation is the process of increasing the sampling frequency of a signal to a higher sampling frequency that differs from the original frequency by an integer value. Interpolation also is known as up-sampling. The spectrum of the output signal ideally is the same as the input signal spectrum, except the output signal spectrum contains an additional high-frequency region with zero-power density.

The following figure shows a typical *L*-fold interpolation filter, where *L* is the target integer increase in the sampling frequency.

[IMAGE alt='image' src='interpolation_fil.gif']

The interpolation filter contains an *L*-fold expander followed by a lowpass FIR filter *H*(*z*). The *L*-fold expander inserts *L*−1 zeroes between consecutive samples to the original signal *x*(*n*) and changes the sampling frequency *f*<sub>*s*</sub> of the original signal *x*(*n*) to a new sampling frequency *Lf*<sub>*s*</sub>. This process introduces images, as shown in the figure below, to the original signal. The interpolation filter then uses the lowpass FIR filter *H*(*z*) to remove the images. Therefore, this lowpass FIR filter is an anti-imaging filter. The interpolation filter then returns an output signal *y*(*n*) with the new sampling frequency.

|  | Note The Multirate Processing VIs use a polyphase implementation, which is more efficient than the procedure in the previous figure, to implement interpolation. Refer to the book Multirate Systems and Filter Banks for more information about polyphase implementations. Interpolation filters that use a polyphase implementation compute only the nonzero input samples, not the inserted zero samples, thus reducing the computational complexity of the filters. |
| --- | --- |

The following figure shows the spectrum of the original signal *x*(*n*) and the spectra from directly interpolating the signal by 2, 3, and *L* without using an anti-imaging filter. Notice multiple images emerge in the range from 0 to half of the resulting sampling frequency in parts (b), (c), and (d) of the figure. These images demonstrate the effect of interpolation.

[IMAGE alt='image' src='interp_no_anti-aliasing.gif']

| (a) Spectrum of the original signal x(n) |
| --- |
| (b) Spectrum of the signal v(n), interpolated by a factor of 2 |
| (c) Spectrum of the signal v(n), interpolated by a factor of 3 |
| (d) Spectrum of the signal v(n), interpolated by a factor of L |

The interpolation system uses the lowpass filter *H*(*z*) after the expander to attenuate the frequency components of the signal from *f*<sub>*s*</sub>/2 to *Lf*<sub>*s*</sub>/2. In the time domain, the effect of *H*(*z*) is to replace the inserted zero value samples that the expander introduces with the interpolated values. When replacing the inserted zeroes with interpolated values, the anti-imaging lowpass filter *H*(*z*) might alter the original values. Use a [Nyquist interpolation filter](../lvdfdtconcepts/nyquist_filters.html) for *H*(*z*) to maintain the original values.

To design interpolation filters, use the [Multirate Filter Design](/csh?topicname=lvdigfiltdestk/dfd_multi_design_vis.html) VIs with the **filtering mode** input set to Interpolation.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_process.html language=enus -->
## TOPIC 00028: Digital Filter Design Process Overview (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_process.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_process.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Digital Filter Design Process Overview (Digital Filter Design Toolkit)

Digital filter design involves the following three steps:

1. Specifying the design method and target digital filter attributes, or the characteristics you want the digital filter to possess.
2. Analyzing the characteristics of the floating-point digital filter you designed in Step 1.
3. Implementing the filter on fixed-point targets with finite-precision arithmetic.

The design process is iterative. You usually experiment with different design specifications or design methods to obtain the appropriate digital filter for an application. Sometimes you might need to revise the specifications or modify the design method after you simulate the filter, especially when designing fixed-point filters.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_related_doc.html language=enus -->
## TOPIC 00029: Related Documentation (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_related_doc.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Digital Filter Design Toolkit)

You must have Adobe Reader installed to view the PDFs. Refer to the Adobe Systems Incorporated website at www.adobe.com to download the latest version of Adobe Reader. Refer to the National Instruments Product Manuals Library at ni.com/manuals for updated documentation resources.

The following documents contain information that you may find helpful as you use the LabVIEW Digital Filter Design Toolkit:

- LabVIEW Digital Filter Design Toolkit Readme—Use this file to obtain introductory information about the Digital Filter Design Toolkit, such as overview, system requirements, installation instructions, and known issues with LabVIEW. Open this readme by navigating to the labview\readme directory and opening readme_DFDT.html .
- Digital Filter Design Example VIs—Refer to the labview\examples\Digital Filter Design directory for example VIs that demonstrate common tasks using the Digital Filter Design VIs. You also can access these VIs by selecting Help»Find Examples from the pull-down menu and selecting Toolkits and Modules»Digital Filter Design in the NI Example Finder window.
- Adaptive Filters Example VIs—Refer to the labview\examples\Adaptive Filters directory for example VIs that demonstrate common tasks using the Adaptive Filters VIs. You also can access these VIs by selecting Help»Find Examples from the pull-down menu and selecting Toolkits and Modules»Adaptive Filters in the NI Example Finder window.
- Additional LabVIEW documentation .

|  | Note The following resources offer useful background information on the general concepts discussed in this documentation. These resources are provided for general informational purposes only and are not affiliated, sponsored, or endorsed by National Instruments. The content of these resources is not a representation of, may not correspond to, and does not imply current or future functionality in the Digital Filter Design Toolkit or any other National Instruments product. |
| --- | --- |

- Chugani, Mahesh L.; Abhay R. Samant; and Michael Cerna. 1998. LabVIEW Signal Processing . Upper Saddle River, NJ: Prentice Hall.
- Diniz, Paulo S. R.; Eduardo A. B. da Silva; and Sergio L Netto. 2002. Digital Signal Processing: System Analysis and Design . New York: Cambridge University Press.
- Haykin, Simon S. 2001. Adaptive Filter Theory . 4th ed. Prentice Hall.
- Hogenauer, E. B. 1981. “An economical class of digital filters for decimation and interpolation.” IEEE Transactions on Acoustics, Speech, and Signal Processing , ASSP-29 (2): 155–162.
- Ifeachor, E. C., and B. W. Jervis. 2003. Digital Signal Processing: A Practical Approach . 2nd ed. Publishing House of Electronics Industry.
- Jayasimha, S., and P. V. R. N. Rao. 1995. “An iteration scheme for the design of equiripple Mth-band FIR filters.” IEEE Transactions on Signal Processing , vol. 43 (8) (August): 1998–2002.
- Mintzer, F. 1982. “On half-band, third-band, and nth-band FIR filters and their design.” IEEE Transactions on Acoustics, Speech, and Signal Processing , ASSP-30 (5) (October): 734–738.
- Neuvo, Y; C-Y Dong; and S.K. Mitra. 1984. “Interpolated finite impulse response filters.” IEEE Transactions on Acoustics, Speech, and Signal Processing , ASSP-32 (June): 563–570.
- Oppenheim, A. V., and R. W. Schafer. 1989. Discrete-Time Signal Processing . Englewood Cliffs, NJ: Prentice Hall.
- Orfanidis, S. J. 1998. Introduction to Signal Processing . Upper Saddle River, NJ: Prentice Hall.
- Parks, T. W., and C. S. Burrus. 1987. Digital Filter Design . New York: John Wiley & Sons, Inc.
- Rabiner, L. R. 1973. “Approximate design relationships for low-pass FIR digital filters.” IEEE Transactions on Audio and Electroacoustics , vol. 21 (5) (October): 456–460.
- Selesnick, I. W., and C. S. Burrus. 1998. “Generalized digital Butterworth filter design.” IEEE Transactions on Signal Processing , vol. 46 (6) (June): 1688–1694.
- Vaidyanathan, P. P. 1993. Multirate Systems and Filter Banks . Englewood Cliffs, NJ: Prentice Hall.
- Vaidyanathan, P. P., and T. Q. Nguyen. 1987. “A ‘trick’ for the design of FIR half-band filters.” IEEE Transactions on Circuits and Systems , vol. 34 (3) (March): 297–300.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_structure_graph.html language=enus -->
## TOPIC 00030: Understanding Filter Structure Graphs (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_structure_graph.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_structure_graph.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Understanding Filter Structure Graphs (Digital Filter Design Toolkit)

The realization of a digital filter involves summations and multiplications of the output, input, and intermediate operands. You must make the values that pass along the signal path available during the realization process. Therefore, to represent the structure of a filter using a signal flow graph, you not only need adders and multipliers, but you also need delays that help you store the passed values. The following figure shows the symbol of an adder.

[IMAGE alt='image' src='filter_structure_adder.gif']

You can treat a consecutive sequence of adders in a filter structure as an accumulator.

The following figure shows the symbol of a multiplier.

[IMAGE alt='image' src='filter_structure_multiplier.gif']

The following figure shows the symbol of a delay.

[IMAGE alt='image' src='filter_structure_delay.gif']

In the previous figure, *z*<sup>–1</sup> is a delay that stores the value of *x*[*n*]. The z-transform of *x*[*n*–1] is *z*<sup>–1</sup> times the z-transform of *x*[*n*]. The number of adders and multipliers implies computational complexity in the realization of a filter structure, and the number of delays implies memory unit requirements in the hardware. The more adders, multipliers, and delays a filter structure contains, the more computational complexity and memory units the filter requires. You can view the signal flow graphs of the following filter structures:

- FIR structures
- IIR Cascaded Second-Order Sections Form structures
- IIR Direct Form structures
- Lattice Allpass structures
- Lattice AR structures
- Lattice ARMA structures
- Lattice MA structures

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfd_supported_target.html language=enus -->
## TOPIC 00031: Supported Execution Targets (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfd_supported_target.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfd_supported_target.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported Execution Targets (Digital Filter Design Toolkit)

You can use the LabVIEW Digital Filter Design Toolkit to execute a digital filter on many different types of targets. The following table shows the supported target types and any additional software you must install to execute a digital filter on that type of target.

| Type of Target | Additional Required Software |
| --- | --- |
| A computer running Windows | — |
| A National Instruments field-programmable gate array (FPGA) target, such as an NI Reconfigurable I/O (NI-RIO) device. To use a digital filter on an FPGA target, you first must generate FPGA code for that filter. | LabVIEW FPGA Module NI-RIO driver software |
| A 32-bit microprocessor. To use a digital filter on a 32-bit microprocessor, you first must generate fixed-point C code for that filter. | LabVIEW with embedded target support The LabVIEW add-on for the embedded target |
| An NI Real-Time (RT) target, such as an NI PXI or CompactRIO controller, running a real-time operating system (RTOS). The Digital Filter Design VIs support native execution on these operating systems. | LabVIEW Real-Time Module Driver software for any hardware devices |

|  | Note Refer to the National Instruments Web site for information about the National Instruments products this table mentions. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfdt_concepts_intro.html language=enus -->
## TOPIC 00032: Digital Filter Design Concepts (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfdt_concepts_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfdt_concepts_intro.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Digital Filter Design Concepts (Digital Filter Design Toolkit)

This book contains information about the digital filter design process. You can use the LabVIEW Digital Filter Design Toolkit to design floating-point and fixed-point digital filters. You need fundamental knowledge about digital signal processing to understand the content in this book. The book [Discrete-Time Signal Processing](../lvdfdtconcepts/dfd_related_doc.html) provides necessary information to help you develop a firm base in the fundamentals.

You can use the Digital Filter Design Toolkit to design the following types of filters:

- Single-rate filters —Single-rate filters are digital filters that do not change the sampling frequency of a signal during the filtering process. Therefore, if you apply a single-rate filter to an input signal, the output signal has the same sampling frequency as the input signal. The Designing Floating-Point Filters book contains more information about designing single-rate filters.
- Multirate filters —Multirate filters are digital filters that convert the sampling frequency of an input signal to a new sampling frequency. Multirate filters increase or decrease the sampling frequency of the input signal while minimizing passband distortion, aliasing, and imaging in the signal. Therefore, the sampling frequency of the output signal from a multirate filter is different from that of the input signal. Multirate filters can reduce computational complexity and data volume in one system, or multirate filters can change the frequency as necessary to be compatible with other systems. In multirate signal processing, the primary consideration is the selection and modification of the proper sampling frequency. The Designing Multirate Filters book contains more information about designing multirate filters.
- Filter Banks —Filter banks are arrays of band-pass filters that separate an input signal into several components, each of which carries a single frequency subband. You can perform signal processing on the separated components individually. The Designing Filter Banks book contains more information about designing filter banks.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/dfdt_features.html language=enus -->
## TOPIC 00033: Digital Filter Design Toolkit Features

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/dfdt_features.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/dfdt_features.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Digital Filter Design Toolkit Features

The LabVIEW Digital Filter Design Toolkit includes a variety of tools to help you design digital filters. For example, the Digital Filter Design Toolkit includes Express VIs that you can use to interact graphically with filter specifications to design appropriate digital filters. In addition to the tools that help you quickly create digital filters, the Digital Filter Design Toolkit includes tools for single-rate and multirate digital filter design, floating-point to fixed-point conversion, filter analysis, simulation on a desktop computer, and filter bank design and analysis.

The Digital Filter Design Toolkit also includes tools for designing, analyzing, simulating, and using adaptive filters for different applications and with different adaptive filter algorithms. The following sections describe the major features that the Digital Filter Design Toolkit provides.

#### Comprehensive Analysis Tools

You can use the [Filter Analysis](/csh?topicname=lvdigfiltdestk/dfd_analysis_vis.html) VIs to evaluate the characteristics of digital filters. You can examine the frequency response, group delay, phase delay, impulse response, step response, and pole-zero placement of a digital filter.

#### Large Selection of Filter Structures

When you design digital filters with the Digital Filter Design Toolkit, you can [select](../lvdfdtconcepts/select_structure.html) from one of 23 possible filter structures, which range from the direct form and cascaded form structures to the lattice auto-regressive (AR), lattice moving average (MA), and lattice ARMA structures.

Filter structures are mathematically equivalent when you use floating-point computation. However, different structures can perform differently in fixed-point implementations and can lead to different computation complexity and memory usage in fixed-point or floating-point implementations. Selecting an appropriate filter structure is critical for digital filter design, especially for fixed-point digital filters in which the precision of the filter coefficients and filtering operations is more limited than for floating-point digital filters.

#### Multirate Digital Filter Design

The [Multirate Filter Design](/csh?topicname=lvdigfiltdestk/dfd_multi_design_vis.html) VIs help you [design, analyze, and implement](../lvdfdtconcepts/design_mrate.html) single-stage multirate filters, multistage multirate filters, halfband filters, Nyquist filters, raised cosine filters, and cascaded integrator comb (CIC) filters.

#### Special Digital Filter Design

The [Special Filter Design](/csh?topicname=lvdigfiltdestk/dfd_special_vis.html) VIs help you [design](../lvdfdtconcepts/special_filt_design.html) IIR notch/peak filters, IIR comb filters, maximally flat filters, narrowband filters, and group delay compensators.

#### Adaptive Filter Design

The [Adaptive Filters](/csh?topicname=lvaft/aft_vis.html) VIs help you create adaptive filters with different [algorithms](/csh?topicname=lvaftconcepts/aft_algorithms.html) and to perform adaptive filtering on input signals. Adaptive filters extract meaningful signal features by adjusting filter coefficients automatically according to the dynamic conditions of the input signals and the environment.

#### Fixed-Point Filter Design and Code Generation

The [Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/dfd_fxp_tools_vis.html) VIs and [Multirate Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/mr_fxp_tools.html) VIs help you [quantize, analyze, model, and simulate](../lvdfdtconcepts/design_fp_filters.html) the fixed-point filter design, including single-rate and multirate filters. You can save the resulting fixed-point filter information as C code, which you then can implement on digital signal processing (DSP) chips. You also can save the resulting fixed-point information as LabVIEW code, which you then can implement on NI Reconfigurable I/O (RIO) targets.

The [Fixed-Point](/csh?topicname=lvaft/fixed-point_vis_aft.html) VIs help you [simulate](/csh?topicname=lvaftconcepts/aft_sim_fxp.html) the behaviors of a fixed-point adaptive filter, [save](/csh?topicname=lvaftconcepts/aft_sim_fxp.html) the fixed-point settings to an XML file, and load the fixed-point settings from an XML file. You also can [generate LabVIEW FPGA code](/csh?topicname=lvaftconcepts/aft_codegen.html) for the fixed-point adaptive filter so that you can implement the fixed-point adaptive filter on NI Reconfigurable I/O (RIO) targets.

#### Generalized Remez and Least Pth Norm Design Algorithms

You can use algorithms such as the [generalized Remez method](../lvdfdtconcepts/remez_designmethod.html) and the [least pth norm method](../lvdfdtconcepts/lpth_norm_design.html) to specify an arbitrary magnitude and a phase response for a digital filter. The Digital Filter Design Toolkit includes automatic order-estimation VIs to assist you in estimating the filter order.

#### Filter Bank Design and Analysis

The Digital Filter Design Toolkit includes VIs that you can use to [design and analyze](../lvdfdtconcepts/dfd_design_fbanks.html) filter banks. You can use the VIs to [design](/csh?topicname=lvdigfiltdestk/dfd_fbankdesignpal.html) a 2-band quadrature mirror filter (QMF) or M-band cosine-modulated filter bank, [analyze](/csh?topicname=lvdigfiltdestk/dfd_fbankanlys.html) the characteristics of a filter bank, [decompose or reconstruct](/csh?topicname=lvdigfiltdestk/dfd_fbankprcs.html) signals with filter banks, [retrieve](/csh?topicname=lvdigfiltdestk/dfd_fbankutil.html) filter bank parameters, and create a filter bank from a prototype filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/differentiators.html language=enus -->
## TOPIC 00034: Differentiators (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/differentiators.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/differentiators.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Differentiators (Digital Filter Design Toolkit)

The ideal frequency response of a differentiator is as follows:

*H*(*f*) = *jf*

where *f* is the normalized frequency with the range [0, 0.5]. The frequency response has a constant 90° phase shift at all frequencies.

If you compare this equation with Equation B in the [Linear Phase Filters](../lvdfdtconcepts/linear_min_filters.html) topic, you can see that an ideal differentiator has a linear phase and is a Type III or Type IV linear phase FIR filter.

You can use the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI to design a differentiator by setting the **filter type** input to Differentiator. Because the passband magnitude response of a differentiator is sloped, a smaller approximation error at frequencies where the frequency response has a smaller absolute gain is useful. The DFD Remez Design VI uses an in-band weighting function inversely proportional to the frequency to achieve a constant amplitude percentage ripple size. The following sections describe how to create Type IV and Type III differentiators.

#### Designing Type IV Differentiators

If you need the frequency range from DC to the Nyquist frequency to have a differentiator response, you can design a Type IV differentiator. A [Type III differentiator](#type_iii_differentiator) cannot maintain a strict differentiator response near the Nyquist frequency because the magnitude response of the Type III differentiator is constrained to zero at the Nyquist frequency.

When you design a Type IV differentiator using the DFD Remez Design VI, you can specify a single band that constrains two points with equal weights. For example, consider a frequency range of [0, 0.5] with an amplitude range of [0, 1]. To design a Type IV differentiator using this band, enter the specifications shown in the following figure into the DFD Remez Design VI.

[IMAGE alt='image' src='diff-type-4-specs.gif']

In the previous figure, the odd order number 19 determines that the resulting differentiator is a Type IV differentiator. The following figure shows the magnitude response of the resulting Type VI differentiator.

[IMAGE alt='image' src='diff-type-4-response.gif']

In the previous figure, you can see that the magnitude response of the designed filter is sloped and the ripple size is small.

#### Designing Type III Differentiators

If you need to use a differentiator in combination with a lowpass filter, use a Type III differentiator. Type III differentiators have a differentiator response in a lowpass passband, and they have a stopband that extends to the Nyquist frequency. For example, you can create a Type III differentiator that covers a frequency range of [0, 0.45] with an amplitude range of [0, 0.9]. The following figure shows a single-band specification without the target response at 0.5 Hz specified.

[IMAGE alt='image' src='diff-type-3-specs.gif']

The following figure shows the magnitude response of the resulting Type III differentiator.

[IMAGE alt='image' src='diff-type-3-response.gif']

In the previous figure, the even order number 20 determines that the resulting differentiator is a Type III differentiator. You can see that the magnitude response of the designed filter becomes zero at 0.5 Hz and the ripple size is larger than that of the Type IV differentiator. To achieve the same ripple size, you need to specify a larger value for the **order** input.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/digital_filter_app.html language=enus -->
## TOPIC 00035: Digital Filter Applications (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/digital_filter_app.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/digital_filter_app.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Digital Filter Applications (Digital Filter Design Toolkit)

Filters are signal processing elements that alter the frequency spectrum of an input signal. You might use filters for the following applications:

- Attenuating noise in a signal where the noise power and signal power are concentrated at different frequencies. For example, you might use a notch filter to attenuate a 60 Hz powerline interference present in a signal.
- Extracting signal components from a signal that contains different signal components concentrated at different frequencies. For example, you might use a bandpass filter to extract a particular radio station signal from a broadband radio signal.
- Reshaping the frequency spectrum of the input signal. For example, you might use an A-weighting filter to approximate the frequency response of a human ear. As another example, you might use an equalizer filter to undo magnitude and phase distortion caused by passing a signal through a linear time-invariant communications channel.

You can use either fixed-point or floating-point arithmetic to implement digital signal processing systems. Although floating-point implementations are typically easier to design, fixed-point implementations are often less expensive and more efficient in power than floating-point implementations. Floating-point designs are typically appropriate in applications that run on desktop computers, and fixed-point designs are often more appropriate in embedded applications, in which you need to minimize cost or power consumption.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/enter_filter_spec.html language=enus -->
## TOPIC 00036: Entering Floating-Point Filter Specifications (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/enter_filter_spec.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/enter_filter_spec.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Entering Floating-Point Filter Specifications (Digital Filter Design Toolkit)

You can use the [Classical Filter Design](/csh?topicname=lvdigfiltdestk/dfd_classical_filter.html) Express VI to [configure a classical digital filter](/csh?topicname=lvdfdthowto/design_fp_filter_1.html) interactively. After you add the Express VI to the block diagram, the **Configure Classical Filter Design** dialog box appears, as shown in the following figure:

[IMAGE alt='image' src='dfd-classical-filter-design.gif']

From the configuration dialog box, you can select the filter type and design method from the pull-down menus and then enter the filter specifications through either the numeric controls on the left side of the configuration dialog box or the graphical interface on the right side of the configuration dialog box. The results are equivalent.

#### Using the Numerical Controls

Classical digital filter specifications include frequency ranges and ripple constraints. You can specify the maximum allowable deviation *δ*<sub>*p*</sub> from unity gain in the passband in the **Passband ripple** numeric control. You can specify the maximum allowable deviation *δ*<sub>*s*</sub> from the zero gain in the stopband in the **Stopband attenuation** numeric control.

You can specify deviations in either a logarithmic or a linear scale. The Classical Filter Design Express VI uses a logarithmic scale by default. To use a linear scale, remove the checkmark from the **Magnitude in dB** checkbox in the configuration dialog box.

The following equations show the relationship between the logarithmic and linear scales.

passband ripple = −20log<sub>10</sub>(1−*δ*<sub>*p*</sub>)

stopband ripple = −20log<sub>10</sub>(*δ*<sub>*s*</sub>)

Based on the two equations above, you can convert the passband ripple to or from the decibel representation. For example, if passband ripple equals 0.01 dB, that is, 0.01 = −20log<sub>10</sub>(1−*δ*<sub>*p*</sub>), then *δ*<sub>*p*</sub> = 0.00115. Similarly, if stopband ripple equals 60 dB, that is 60 = −20log<sub>10</sub>(*δ*<sub>*s*</sub>), then *δ*<sub>*s*</sub> = 0.001.

#### Using the Graphical Interface

The right side of the **Configure Classical Filter Design** dialog box displays the magnitude response of the designed digital filter. The magnitude axis can be either a linear or a logarithmic scale. Remove the checkmark from the **Magnitude in dB** checkbox to use a linear scale, or keep the checkmark in the **Magnitude in dB** checkbox to use a logarithmic scale. The Frequency axis, in hertz, covers the range from 0 to half the sampling frequency, which is the Nyquist frequency.

The **Magnitude Response** graph contains a set of cursors that you can use to specify the passband and stopband. Use the passband cursor to change the passband. Under the linear scale, the distance between unity and the horizontal passband cursor specifies the maximum passband ripple. The location of the vertical passband cursor indicates the passband edge frequency. The stopband cursors work the same when defining the specifications of the stopband. The distance between the horizontal passband cursor and the horizontal stopband cursor specifies the stopband attenuation.

#### Guidelines for Entering Filter Specifications

As you define a filter specification, you must adhere to a set of rules to maintain valid specifications. If you do not adhere to the following rules, the **Error message** indicator of the **Configure Classical Filter Design** dialog box displays a message with suggestions for repositioning the cursors.

- Keep horizontal cursors in the range (0, 1) in a linear scale or (−inf, 0 dB) in a logarithmic scale.
- Keep the horizontal passband cursor above the horizontal stopband cursor.

#### Selecting the Design Method

After you enter the target digital filter specifications into the numeric controls or graphical interface, select a [design method](../lvdfdtconcepts/design_methods.html).

When you design a digital filter with the Classical Filter Design Express VI, the design method and the filter specifications that you specify control the shape of the frequency response. You cannot alter the phase response, even though the phase response for filters generated with the FIR methods in this VI are linear phase. If you want to specify the magnitude response and phase response, use the [Advanced FIR Filter Design](/csh?topicname=lvdigfiltdestk/dfd_adv_fir_vis.html) VIs, the [Advanced IIR Filter Design](/csh?topicname=lvdigfiltdestk/dfd_adv_iir_vis.html) VIs, or the [Special Filter Design](/csh?topicname=lvdigfiltdestk/dfd_special_vis.html) VIs.

Refer to the Step 1 - Design Lowpass (Lowpass) VI in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter\ directory for an example that demonstrates how to use the Classical Filter Design Express VI to design a lowpass filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/exact_gain_control.html language=enus -->
## TOPIC 00037: Exact Gain Control Design (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/exact_gain_control.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/exact_gain_control.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Exact Gain Control Design (Digital Filter Design Toolkit)

When you enter bands into the **band specs** input, the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI uses complex or magnitude approximation to create the design of the filter. You can use exact gain control to constrain the amplitude response of the filter to particular values at particular frequencies.

To use exact gain control in the DFD Remez Design VI, enter in the **freqs of exact gain** input a list of frequencies that you want to constrain to ideal amplitudes. If you also specify those frequencies in the **band specs** input, the DFD Remez Design VI uses the corresponding amplitudes. If you do not enter those frequencies in the **band specs** input, the DFD Remez Design VI interpolates the amplitudes linearly.

Consider a filter that has the same magnitude response as the filter in the [Single-Point Band Design](../lvdfdtconcepts/single-point_bands.html) topic. You can achieve sharper notches by applying exact gain control at 0.15 Hz and 0.35 Hz. By entering those single-point band frequency points in the **freqs of exact gain** input, the redesigned notch filter has a magnitude response as shown in the following figure:

[IMAGE alt='image' src='notch-filter-exact-gain-con.gif']

Notice that the graph has sharper notches than the notch filter in the [Single-Point Band Design](../lvdfdtconcepts/single-point_bands.html) topic.

The following figure shows the magnitude response of a 12<sup>th</sup> order lowpass equi-ripple filter without any exact gain frequencies. The passband range is [0, 0.25] and the stopband range is [0.3, 0.5] with equal weights in both bands. Notice that the gain at DC, or the magnitude response at 0 Hz, is not exactly one.

[IMAGE alt='image' src='lowpass-filter-no-exact-gai.gif']

If you want to force the gain to one at DC, enter 0 into the **freqs of exact gain** input and run the VI again. The following figure shows the magnitude response of the resulting filter.

[IMAGE alt='image' src='lowpass-filter-with-exact-g.gif']

Notice that the DC gain becomes exactly one without any noticeable ripple size increase.

The following figure shows the magnitude response of a 12<sup>th</sup> order highpass filter with a stopband frequency range of [0, 0.2] and a passband frequency range of [0.3, 0.5].

[IMAGE alt='image' src='highpass-filter-no-exact-ga.gif']

The signal is relatively clean except for a noise component at 0.1 Hz and the second harmonic at 0.2 Hz. To attenuate the noise power at those frequencies, you can enter 0.1 and 0.2 into the **freqs of exact gain** input.

The following figure shows the magnitude response of the filter with exact gains specified at 0.1 Hz and 0.2 Hz. Notice that the magnitude response at 0.1 Hz and 0.2 Hz is exactly zero.

[IMAGE alt='image' src='highpass-filter-with-exact.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/extract_fp_coef.html language=enus -->
## TOPIC 00038: Exporting Fixed-Point Integer Coefficients (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/extract_fp_coef.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/extract_fp_coef.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Exporting Fixed-Point Integer Coefficients (Digital Filter Design Toolkit)

If you have a filter execution engine for which you need only filter coefficients, you can export the fixed-point filter coefficients to a text file using the [DFD Save to Text File](/csh?topicname=lvdigfiltdestk/dfd_save_to_text.html) VI. You can save the coefficients to a text file and download them to the execution target. The text file contains a section that provides all information about the fixed-point integer coefficients and corresponding quantizers.

Refer to the Export FIR Coefficients to Xilinx COE File VI in the labview\examples\Digital Filter Design\Fixed-Point Filters\Single-Rate directory for an example that demonstrates how to export fixed-point integer coefficients.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/filter_attributes.html language=enus -->
## TOPIC 00039: Filter Attributes (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/filter_attributes.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/filter_attributes.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Filter Attributes (Digital Filter Design Toolkit)

The filters that you design using the LabVIEW Digital Filter Design Toolkit have the following attributes:

- Digital —The expected filter input signal is a series of discrete digital values. The set of discrete digital coefficients determines the filter frequency response. Digital filters have many advantages over analog filters. For example, the frequency response of digital filters generally does not depend on the parametric variation of electronic components, power supply noise, or power supply droop.
- Linear —The output signal of the digital filter is a linear function of the input signal. You cannot use the digital filter to equalize nonlinear distortion caused by passing a signal through a nonlinear peak-clipping or truncating channel.
- Time-invariant —The frequency response of the digital filter is fixed versus time. Alternatively, adaptive filters, which the Digital Filter Design Toolkit does not support, can adapt their frequency responses versus time in response to time-variant target responses.
- Causal —The output signal of a digital filter cannot change in response to a change in an input signal until the input signal changes. The Digital Filter Design Toolkit specifically creates digital filters that you treat as causal in applications, but you can use them in some noncausal applications. For example, a common digital signal processing (DSP) technique for linearizing the phase of a filter with a nonlinear phase is to pass the input signal through the filter, time-reverse the input signal, and then pass the signal through the filter again. In this case, the filter is noncausal.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/fir_and_iir_filters.html language=enus -->
## TOPIC 00040: FIR and IIR Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/fir_and_iir_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/fir_and_iir_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### FIR and IIR Filters (Digital Filter Design Toolkit)

You can design both finite impulse response (FIR) and infinite impulse response (IIR) digital filters using the LabVIEW Digital Filter Design Toolkit:

- FIR —The output signal of the filter, after you set the input signal from nonzero to zero, can be nonzero for only a finite number of sample times before the output signal also becomes zero.
- IIR —The output signal of the filter can be nonzero infinitely after you set the input signal from nonzero to zero.

The choice between FIR and IIR filters affects both the filter design process and the implementation of the filter.

#### Mathematical Definitions

In the time domain, the filtering process for FIR filters is defined mathematically as a convolution of *M*+1 filter coefficients *h*<sub>*k*</sub> with a sequence of input data samples *x*[*n*]:

|  | (A) |
| --- | --- |

where *y*[*n*] is the output of the filter and *M* is the filter order. The number of coefficients for the FIR filter is defined as the number of [taps](/csh?topicname=lvanlsconcepts/lvac_taps.html), which is *M*+1.

If a single nonzero value is present at the input of the filter but all subsequent input samples are zeroes, the output of the filter in Equation A becomes zero after the filter processes *M*+1 input data samples. Because the duration of the nonzero response in this case is finite for *M*+1, the filter in Equation A is an FIR filter.

In 1962, Charles Rader and Bernard Gold at MIT Lincoln Laboratory, motivated by a digital vocoder (voice coder) application, devised the idea of using recursive digital filters. This innovation led to the IIR filter, which has a time-domain response defined by the following equation:

|  | (B) |
| --- | --- |

| where | N is the numerator order |
| --- | --- |
|  | M is the denominator order |
|  | ai is the set of reverse coefficients |
|  | bk is the set of forward coefficients |

The filter defined by Equation B operates on the current input *x*[*n*] and the previous input *x*[*n*−*k*] and the current output *y*[*n*] and the previous output *y*[*n*−*i*]. The impulse response of the filter in this case is infinite because the filter might generate nonzero outputs arbitrarily for an indefinite amount of time in response to a single nonzero input sample.

For most filtering applications, FIR filters are sufficient. In general, FIR filters use the available precision better, and they are more numerically robust. However, in some cases FIR filter orders become impractically large. For example, if you need a large number of FIR filter coefficients—perhaps hundreds or more—an FIR filter might be too difficult or expensive to implement because the implementation might require more memory, power, processing time, and engineering time.

#### FIR Filters versus IIR Filters

One difference between FIR and IIR filters is the impulse response, which is finite or infinite, respectively. When you design a filter, you must consider other differences between FIR and IIR filters that might affect the design. For example, FIR filter implementations typically require more multiplications and summations than IIR filters with similar filtering performance. However, because certain computer architectures, for example digital signal processors (DSPs), are frequently better suited to performing FIR filtering, the computation speed of an IIR filter is not necessarily faster than an FIR filter. The following table compares the attributes of [causal](../lvdfdtconcepts/filter_attributes.html) FIR and IIR filters.

| Attribute | FIR Filter | IIR Filter |
| --- | --- | --- |
| Exact linear phase response | Possible | Not possible |
| Stability | Always stable | Conditionally stable |
| Fixed-point version | Easy to implement | Can be complicated to implement |
| Computational complexity | More computations | Fewer computations |
| Data path precision typically required | Less precision required | Greater precision required |
| Zero-input limit cycles1 | Cannot produce limit cycles | Might produce limit cycles |
| 1 “Zero-input limit cycle behavior refers to the effect that the output may continue to oscillate indefinitely with a periodic pattern while the input remains equal to zero. And it is a consequence either of the nonlinear quantizers in the feedback loop of IIR filter or of overflow of additions.” (Oppenheim and Schafer) |  |  |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/fir_filter_specs.html language=enus -->
## TOPIC 00041: FIR Structures (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/fir_filter_specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/fir_filter_specs.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### FIR Structures (Digital Filter Design Toolkit)

The transfer function of an FIR filter is defined as follows:

[IMAGE alt='image' src='equ_fir_transfer_function.gif']

where *z* is a complex variable, *M* is the filter order, and *h* is the set of filter coefficients.

#### FIR Direct Form

For FIR filters, the FIR Direct Form structure is the most straightforward structure from a filter transfer function perspective. The following figure represents the FIR Direct Form structure. The number of delays equals the filter order. Refer to the [Understanding Filter Structure Graphs](../lvdfdtconcepts/dfd_structure_graph.html) topic for information that helps you read and understand a filter structure graph.

[IMAGE alt='image' src='fir_direct_form.gif']

#### FIR Direct Form Transposed

The FIR Direct Form Transposed structure is the alternate direct form implementation for FIR filters. The following figure represents the FIR Direct Form Transposed structure.

[IMAGE alt='image' src='fir_direct_form_transposed.gif']

Both direct form structures contain the same number of delays. However, in the FIR Direct Form structure, the word length of the delays equals that of the input signal *x*[*n*]. In the FIR Direct Form Transposed structure, the word length of the delays equals that of the [accumulator](../lvdfdtconcepts/dfd_structure_graph.html). In most cases, the word length of the input signal is less than the word length of the accumulator. Therefore, the FIR Direct Form structure requires less memory for saving internal states than the transposed structure.

Both direct form structures also contain the same number of multipliers, which equals *M*+1. However, if you perform the multiplications in parallel and then perform summations on the multiplication products for both structures, the FIR Direct Form Transposed structure has better timing performance because the delays following the adders in this structure can store the summation results temporarily for performing the summations in parallel. However, the FIR Direct Form structure does not contain delays for the adders so the summations in this structure take more time. If you perform the multiplications and additions serially using a loop structure, the FIR Direct Form structure is more efficient because this structure requires less memory.

#### FIR Symmetric

Use the FIR Symmetric structures for symmetric linear phase FIR filters, which use the symmetry of the filter coefficients to reduce the number of multipliers from *M*+1 to *M*/2+1, when *M* is an even number, or (*M*+1)/2, when *M* is an odd number. The following figure represents the FIR Symmetric structure when the filter order is an even number.

[IMAGE alt='image' src='fir_direct_form_sym_evenord.gif']

The following figure represents the FIR Symmetric structure when the filter order is an odd number.

[IMAGE alt='image' src='fir_direct_form_sym_oddorde.gif']

#### FIR Antisymmetric

Use the FIR Antisymmetric structure for antisymmetric linear phase FIR filters, which use the antisymmetry of the filter coefficients to reduce the number of multipliers from *M*+1 to *M*/2, when *M* is an even number, or (*M*+1)/2, when *M* is an odd number. The following figure represents the FIR Antisymmetric structure when the filter order is an even number.

[IMAGE alt='image' src='fir_direct_form_antisym_2.gif']

The following figure represents the FIR Antisymmetric structure when the filter order is an odd number.

[IMAGE alt='image' src='fir_direct_form_antisym.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/fir_mag_approx.html language=enus -->
## TOPIC 00042: Minimum and Maximum Phase FIR Design (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/fir_mag_approx.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/fir_mag_approx.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Minimum and Maximum Phase FIR Design (Digital Filter Design Toolkit)

The [Designing Special Filters](../lvdfdtconcepts/special_filt_design.html) book discusses linear phase finite impulse response (FIR) filter designs, which are actually amplitude approximations that use the following complex approximation criterion:

[IMAGE alt='image' src='equ_fir_mag_approx_1.gif']

where *D*(*ω*<sub>*i*</sub>) is the ideal frequency response, *H*(*ω*<sub>*i*</sub>) is the frequency response of the designed filter, and *W*(*i*) is the positive weight at the *i*<sup>th</sup> frequency point.

Many applications require linear phase to ensure that the frequency components of an input signal pass through the filter with the same delay. If you have an application that does not require linear phase, you can control the magnitude response of the filter and allow the filtering process to change the delay relationship between different frequency components arbitrarily. You can use the following expression for this type of magnitude approximation problem.

[IMAGE alt='image' src='equ_fir_mag_approx_2.gif']

Without the phase constraint, you can achieve the same approximation error magnitude with a lower filter order or a smaller approximation error magnitude with the same filter order. Both options reduce the implementation cost.

More than one set of filter coefficients can have the same magnitude response. In the *z*-plane you can create a new set of coefficients with the same magnitude response, unless all zeroes are on the unit circle, through the allpass transformation of flipping zeroes to their conjugate reciprocal locations relative to the unit circle. You can specify minimum phase or maximum phase to eliminate the ambiguity about which set of FIR filter coefficients you are using.

All zeroes in a minimum phase FIR filter are inside or on the unit circle. Minimum phase filters sometimes are called minimum energy delay filters because the energy of the impulse response is maximally concentrated toward the beginning of the impulse response.

All zeroes in a maximum phase FIR filter are outside or on the unit circle. The energy of the impulse response is maximally concentrated toward the end of the impulse response. Given a certain magnitude response, the impulse responses of the minimum and the maximum phase FIR filters are time-reversed.

The following figure shows the magnitude response of a 16<sup>th</sup> order FIR filter.

[IMAGE alt='image' src='min_max-phase-response.gif']

You can use two different sets of filter coefficients to match the magnitude response of the FIR filter. The following figure shows the impulse response and zeroes of a minimum phase filter with the same magnitude response of the 16<sup>th</sup> order FIR filter.

[IMAGE alt='image' src='minimum-phase-impulse-respo.gif']

The following figure shows the impulse response and zeroes of a maximum phase filter with the same magnitude response of the 16<sup>th</sup> order FIR filter.

[IMAGE alt='image' src='max-phase-impulse-response.gif']

Minimum phase filters are especially useful in control applications. A filtering process in a control loop typically requires the response to an input stimulus to be as quick as possible. A large delay in the filtering process can cause a negative feedback control loop to become unstable.

One disadvantage of linear phase FIR filters is that the system delay, also called the group delay, is fixed to half the filter order, which might be unacceptably long when the filter order is large. Use minimum phase filters in situations where minimizing delay is critical unless the system requires a linear phase filter or the linear phase filter order is relatively small.

You can design minimum or maximum phase FIR filters using the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI. Set the **filter type** input to Minimum Phase or Maximum Phase and the remaining specifications just as you [design a linear phase filter](../lvdfdtconcepts/linear_min_filters.html). Refer to the [Exact Gain Control Design](../lvdfdtconcepts/exact_gain_control.html) and [Ripple Constraint Design](../lvdfdtconcepts/ripple_constraint.html) topics for information about designing minimum and maximum phase filters with exact gain control or ripple constraints.

You can create a minimum phase filter by designing a linear phase filter and converting it to a minimum phase filter by flipping the zeroes that are outside the unit circle to their conjugate reciprocal position inside the unit circle. Although the new minimum phase filter possesses the same magnitude response as the original linear phase filter, the new filter is not optimal relative to the filter magnitude specification. You can achieve a closer match to the magnitude specification or a lower filter order by specifying a minimum phase filter directly.

|  | Note Minimum phase filters can achieve better results in terms of a lower ripple or lower order for a given magnitude specification than equivalent linear phase filters. Therefore, minimum phase can be a better choice than linear phase in applications where the phase response is not constrained. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/gen_fp_c_code.html language=enus -->
## TOPIC 00043: Generating Fixed-Point C Code (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/gen_fp_c_code.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/gen_fp_c_code.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generating Fixed-Point C Code (Digital Filter Design Toolkit)

You usually program target digital signal processing (DSP) hardware using C code. To [generate C code](/csh?topicname=lvdfdthowto/generate_c_code.html) from the fixed-point filter model, use the C Code instance of the [DFD FXP Code Generator](/csh?topicname=lvdigfiltdestk/dfd_fxp_codegen.html) VI. You can compile the generated code to run on a fixed-point DSP.

|  | Note C code can yield a less compact and less efficient implementation than a hand-written, assembly-coded implementation. If you need to improve the performance of a filter, you can translate the C code to assembly code manually. |
| --- | --- |

The DFD FXP Code Generator VI produces three files, where *filtername* is the string you wire to the **filter name** input:

- nidfdtyp.h contains the definitions of the data types in the C source files that the DFD FXP Code Generator VI generates. You might need to redefine the data types in this file if you want to compile the generated code to run on a 64-bit target.
- *filtername*.h contains type definitions, global variable declarations, and function prototypes.
- *filtername*.c contains the code that implements the filter, including the filter coefficients, information about the implementation structure and quantizer settings in the fixed-point model, and the following functions:
  - *filtername*_State *filtername*_CreateState() creates the memory space needed to store the internal states of the filter.
  - void*filtername*_DisposeState(*filtername*_State state) disposes of the memory space used to store the internal states of the filter.
  - void*filtername*_InitState(*filtername*_State state) initializes the internal states to zeroes. Call this function for the first block when processing a large data sequence that consists of multiple data blocks.
  - I16*filtername*_Filtering(I16 sampleIn, *filtername*_State state) implements the fixed-point filter.
  - static I16 *filtername*_Coef[] contains the quantized coefficients of the fixed-point filter.

Refer to the LabVIEW C Code Generation VI in the labview\examples\Digital Filter Design\Fixed-Point Filters\Single-Rate directory for an example that demonstrates how to generate LabVIEW C code from a fixed-point filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/gen_int_lv_code.html language=enus -->
## TOPIC 00044: Generating Integer LabVIEW Code (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/gen_int_lv_code.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/gen_int_lv_code.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generating Integer LabVIEW Code (Digital Filter Design Toolkit)

Integer LabVIEW code can run on any platform or target on which you can run LabVIEW VIs. Integer LabVIEW code is useful when you simulate the behavior of a fixed-point filter on Windows. You can use the [DFD FXP Code Generator](/csh?topicname=lvdigfiltdestk/dfd_fxp_codegen.html) VI to [generate integer LabVIEW code](/csh?topicname=lvdfdthowto/generate_integer_lv.html) from a fixed-point filter. The LabVIEW Digital Filter Design Toolkit [uses LabVIEW projects](/csh?topicname=lvconcepts/using_labview_projects.html) to manage the resulting integer LabVIEW code. The following figure shows an example project file that contains integer LabVIEW code.

[IMAGE alt='image' src='filtername_project.gif']

In the previous figure, the *filtername*.lvproj file, where *filtername* denotes the name of the fixed-point filter, contains the following folders and VIs in addition to the default items.

- filtername Block —This folder contains all generated VIs and subVIs related to the fixed-point filter from which you generate integer LabVIEW code. You can apply the filter to another project by adding this folder into the target project file.
- Filter SubVIs —This folder contains the generated subVIs. You usually do not need to modify these subVIs.
- filtername_Filter.vi —This VI is the top-level VI of the generated integer LabVIEW code. To use the integer LabVIEW code, add this VI to the block diagram.

Refer to the Integer LabVIEW Code Generation VI in the labview\examples\Digital Filter Design\Fixed-Point Filters\Single-Rate directory for an example that demonstrates how to generate integer LabVIEW code from a fixed-point filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/gen_lv_fpga.html language=enus -->
## TOPIC 00045: Generating LabVIEW FPGA Code (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/gen_lv_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/gen_lv_fpga.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generating LabVIEW FPGA Code (Digital Filter Design Toolkit)

LabVIEW field-programmable gate array (FPGA) code is a type of code specifically optimized to run on NI Reconfigurable I/O (RIO) devices such as the NI PXI-7831R. LabVIEW FPGA code takes advantage of the specific features, such as the single-cycle Timed Loop (SCTL) and memory items, of the LabVIEW FPGA Module. Therefore, this type of code can run on an FPGA target efficiently. You can use the **Start IP Generator** dialog box or the [DFD FXP Code Generator](/csh?topicname=lvdigfiltdestk/dfd_fxp_codegen.html) VI to [generate LabVIEW FPGA code](/csh?topicname=lvdfdthowto/generate_fpga_code.html) for filters with the following filter structures:

- FIR structures
- IIR Cascaded Second-Order Sections Form structures
- Lattice MA structures
- Lattice ARMA structures

|  | Note If you want to generate LabVIEW FPGA code from an IIR filter, National Instruments recommends you use the IIR Cascaded Second-Order Sections Form II Transposed structure for this filter. |
| --- | --- |

|  | Note To generate LabVIEW FPGA code, you must install the LabVIEW FPGA Module and NI-RIO driver software. To execute the FPGA code, you also need an FPGA target on which to run the code. Refer to the National Instruments Web site for information about these products. |
| --- | --- |

The LabVIEW Digital Filter Design Toolkit [uses LabVIEW projects](/csh?topicname=lvconcepts/using_labview_projects.html) to manage the resulting LabVIEW FPGA code. The following figure shows an example project file that contains LabVIEW FPGA code.

[IMAGE alt='image' src='fpga_project.gif']

In the previous figure, the *filtername*.lvproj file, where *filtername* denotes the name of the fixed-point filter, contains the following folder and VI in addition to the default items.

- filtername Block —This folder contains the generated filter VI. You can apply the filter to another project by copying and pasting this folder into the target project file.
- filtername_Filter.vi —This VI is the top-level VI of the generated LabVIEW FPGA code. To use the LabVIEW FPGA code, drag and drop this VI to the block diagram of the calling VI. [IMAGE alt='image' src='note.gif']
**Note** The LabVIEW FPGA code you generate with the LabVIEW Digital Filter Design Toolkit supports only the fixed-point data type.

Refer to the LabVIEW FPGA Code Generation VI in the labview\examples\Digital Filter Design\Fixed-Point Filters\Single-Rate directory for an example that demonstrates how to generate LabVIEW FPGA code from a fixed-point filter.

You can generate both one-channel and multichannel LabVIEW FPGA code from a fixed-point filter. Refer to the Lowpass.lvproj file in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter\Lowpass directory for an example that demonstrates how to generate one-channel LabVIEW FPGA code from a lowpass, finite impulse response (FIR) filter and implement the resulting LabVIEW FPGA code on a PXI target.

Refer to the Highpass.lvproj file in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter\Highpass directory for an example that demonstrates how to generate one-channel LabVIEW FPGA code from a highpass, finite impulse response (FIR) filter and implement the resulting LabVIEW FPGA code on a CompactRIO target.

To use multichannel LabVIEW FPGA code, you must interleave the input data. Refer to the Notch.lvproj file in the labview\examples\Digital Filter Design\Case Studies\Notch Filter\Notch directory for an example that demonstrates how to generate eight-channel LabVIEW FPGA code from an infinite impulse response (IIR) notch filter and implement the resulting LabVIEW FPGA code on a PXI target.

#### Resolving LabVIEW FPGA Code Compilation Failures

Sometimes the LabVIEW FPGA code might not compile successfully. One potential cause of a compilation failure is that the computation resources on the FPGA target might not meet the requirements of the fixed-point filter. For example, the NI PXI-7831R has 40 built-in 18x18 multipliers. Therefore, you cannot apply filters that require more than 40 built-in multipliers to the NI PXI-7831R. Another potential cause of a compilation failure is that the fixed-point filter is too complicated to implement in an SCTL or that the design clock rate is too high. A more complicated fixed-point filter requires more FPGA hardware resources. The compilation might fail when the FPGA hardware resources are not sufficient. For example, the compilation runs properly when the fixed-point filter uses only 40% of the FPGA hardware resources but the compilation might fail if the fixed-point filter uses about 85% of the FPGA hardware resources. If you encounter compilation failures, try converting the filter structure to one that requires fewer resources or setting the design clock rate to a lower frequency.

The following table lists the number of multiplication units that each filter structure uses. One multiplication unit might require multiple FPGA built-in multipliers, depending on the type of multiplication unit. For example, an [I16xI16](/csh?topicname=lvhowto/integers.html) multiplication unit requires only one FPGA built-in multiplier, but an I16xI32 multiplication unit requires two FPGA built-in multipliers.

|  | Note Increasing the FPGA target clock rate reduces the amount of code that you can execute in the SCTL because the clock cycle is shorter. |
| --- | --- |

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
| Some filter structures use two groups of multiplication units because the structures contain two sets of filter coefficients. A and B in the table represent coefficients a/k and coefficients b/v, respectively. One multiplication unit might require different number of FPGA built-in multipliers, as shown in the following table: Multiplicand x Coefficients Number of Multipliers I16xI16 1 I16xI32 2 I32xI16 2 I32xI32 4 The Context Help window displays information about the generated LabVIEW FPGA code, including the estimated execution throughput, when you move the cursor over the filter VI. |  |
| Multiplicand x Coefficients | Number of Multipliers |
| I16xI16 | 1 |
| I16xI32 | 2 |
| I32xI16 | 2 |
| I32xI32 | 4 |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/generating_code.html language=enus -->
## TOPIC 00046: Generating Code from Fixed-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/generating_code.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/generating_code.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generating Code from Fixed-Point Filters (Digital Filter Design Toolkit)

After you obtain an appropriate fixed-point filter model, you can implement the resulting fixed-point filter on the target hardware.

|  | Note Output quantizers generally have different integer word lengths from the input quantizers. Before generating code, check the quantizer settings to confirm or modify the settings you want to use for the fixed-point filter. If you reduce the default output integer word length, National Instruments recommends that you change the overflow mode to Saturate. |
| --- | --- |

The LabVIEW Digital Filter Design Toolkit provides the following options for deploying the filter:

- Export fixed-point integer coefficients . You then can use the coefficients in a filter execution engine.
- Generate fixed-point C code . You then can use a digital signal processing (DSP) C compiler to generate digital filter object code for a general-purpose DSP.
- Generate integer LabVIEW code . You then can simulate the behavior of the fixed-point filter using the integer LabVIEW code.
- Generate LabVIEW field-programmable gate array (FPGA) code . You then can deploy the generated code to an NI Reconfigurable I/O (RIO) target.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/grp_compensator.html language=enus -->
## TOPIC 00047: Group Delay Compensator (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/grp_compensator.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/grp_compensator.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Group Delay Compensator (Digital Filter Design Toolkit)

[Infinite impulse response (IIR)](../lvdfdtconcepts/fir_and_iir_filters.html) filters that you design using Butterworth, Chebyshev, or Elliptic methods usually have a nonconstant group delay, which means that they have nonlinear phase or phase distortion. The greatest deviation from a constant group delay typically occurs at the edge of the passband or somewhere in the transition band.

Given a filter with phase distortion, you can cascade the filter with an allpass filter to linearize the phase response in the specified frequency ranges while keeping the magnitude response unchanged.

Let [IMAGE alt='image' src='equ_tau_zero.gif'] and [IMAGE alt='image' src='equ_tau_ap.gif'] denote the group delay of the given filter and the designed allpass filter at the *i*
 <sup>th</sup> frequency point, respectively. The coefficients vector of the allpass filter [IMAGE alt='image' src='equ_a_arrow.gif'] is determined by the following equation:

[IMAGE alt='image' src='equ_group_delay.gif']

where [IMAGE alt='image' src='equ_tau.gif'] is the target group delay in all user-defined frequency ranges.

A 4<sup>th</sup> order elliptic bandpass filter with a passband frequency ranging from 0.3 to 0.4 has nonconstant group delay in the specified passband. The following figure shows how to compensate the filter group delay in the specified passband to be near constant with an 8<sup>th</sup> order compensator using the [DFD Group Delay Compensator](/csh?topicname=lvdigfiltdestk/dfd_gdelay_compens.html) VI.

[IMAGE alt='image' src='group-delay-compensator.gif']

The block diagram in the above figure uses the DFD Plot Group Delay VI to check the group delay response of the filter. The following figure shows the group delay response of the original filter and the compensated filter.

[IMAGE alt='image' src='group-delay-response.gif']

In the previous figure, you can see that the group delay of the compensated filter is fairly constant in the passband frequency ranging from 0.3 to 0.4. The constant value of the group delay indicates that the compensated filter linearly approximates the phase response in the passband. However, compared to the original filter, the compensated filter also increases the delay and filtering computation.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/grp_phase_delay.html language=enus -->
## TOPIC 00048: Group Delay and Phase Delay (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/grp_phase_delay.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/grp_phase_delay.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Group Delay and Phase Delay (Digital Filter Design Toolkit)

For a filter with a frequency response of *H*(*e*<sup>*jω*</sup>), the phase delay response [IMAGE alt='image' src='equ_pha_del_res.gif'] is defined by the following equation:

[IMAGE alt='image' src='eq1_phase_delay.gif']

The group delay response [IMAGE alt='image' src='equ_gro_del_res.gif'] is defined as the negative derivative of the phase response *ω*, as shown in the following equation:

[IMAGE alt='image' src='eq2_phase_delay.gif']

Both the group delay and phase delay are in samples.

For a generalized linear phase filter with arg[*H*(*e*<sup>*jω*</sup>)] = –[IMAGE alt='image' src='alpha.gif']*ω*+*β*, the group delay is represented by the following equation:

[IMAGE alt='image' src='eq4_phase_delay.gif']

The phase delay is represented by the following equation:

[IMAGE alt='image' src='eq5_phase_delay.gif']

You can represent the phase delay as the time delay in samples experienced by each frequency component of the input signal. The filter is represented by the following illustration:

[IMAGE alt='image' src='box2_freq.gif']

The filter *H*(*e*<sup>*jω*</sup>) shifts all frequency components by a phase *β* and then filters the signal with a new filter *H*<sub>new</sub>(*e*<sup>*jω*</sup>) that has a phase of –[IMAGE alt='image' src='alpha.gif']*ω*. You can interpret the group delay as the time delay in samples experienced by each frequency component through the new filter *H*<sub>new</sub>(*e*<sup>*jω*</sup>).

Linear phase filters are characterized by a constant group delay. The deviation of the group delay from a constant value within the passband indicates the degree of nonlinearity in the phase. Use the group delay to analyze the linearity of a filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/handle_overflow.html language=enus -->
## TOPIC 00049: Handling Overflows and Underflows (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/handle_overflow.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/handle_overflow.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Handling Overflows and Underflows (Digital Filter Design Toolkit)

Fixed-point numbers can represent only numbers of a finite range. Overflows occur when a number is greater than the maximum representable number within the range. Underflows occur when a number is less than the minimum representable number within the range. You can handle overflows and underflows using one of the following two modes:

- Saturation —A quantizer converts the specified number to the maximum representable number in the case of an overflow or to the minimum representable number in the case of an underflow.
- Wrap —A quantizer wraps the specified value from the maximum representable number to the minimum representable number in the case of an overflow and from the minimum representable number to the maximum representable number in the case of an underflow. In the wrap mode, when an overflow or an underflow occurs, the absolute value of the error is 2 iwl , which is greater than the total available dynamic range.

The saturation mode of the output quantizer is preferred over the wrap mode in most real-world applications because the saturation mode helps avoid signal discontinuities, or sudden changes in the amplitudes. However, the saturation mode is more complicated than the wrap mode. For internal quantizers, such as the sum quantizer, the wrap mode is preferred because this mode allows intermediate overflows and underflows within a certain range as long as the final output does not contain overflows or underflows. Use the **overflow mode** input of the [Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/dfd_fxp_tools_vis.html) VIs to specify an appropriate setting for handling overflows and underflows.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/hilbert_transformers.html language=enus -->
## TOPIC 00050: Hilbert Transformers (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/hilbert_transformers.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/hilbert_transformers.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Hilbert Transformers (Digital Filter Design Toolkit)

The ideal frequency response of a Hilbert transformer is as follows:

*H*(*f*) =
 −*j*sgn(*f*)

where *f* is the normalized frequency with the range [0, 0.5]. The frequency response has −90° phase shift for positive frequencies and 90° phase shift for negative frequencies.

If you compare this equation with Equation B in the [Linear Phase Filters](../lvdfdtconcepts/linear_min_filters.html) topic, you can see that an ideal Hilbert transformer has a linear phase and is a Type III or Type IV linear phase FIR filter.

You can use the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI to design a Hilbert transformer by setting the **filter type** input to Hilbert. The following sections explain how to create Type IV and Type III Hilbert transformers.

#### Designing Type IV Hilbert Transformers

Type IV (odd order, antisymmetric) filters make ideal Hilbert transformers. When you design a Type IV Hilbert transformer with the DFD Remez Design VI, you can specify a single band that contains two points with equal weights. For example, consider a frequency range of [0.1, 0.5] with an amplitude of [−1, −1]. To design a Type IV Hilbert transformer with an order of 11 using this band, enter the specifications shown in the following figure into the DFD Remez Design VI.

[IMAGE alt='image' src='hilbert-type-4-specs.gif']

The following figure shows the magnitude response and impulse response of the designed Type IV Hilbert transformer.

[IMAGE alt='image' src='hilbert-type-4-response.gif']

In the previous figure, you can see that magnitude response of the designed filter is fairly constant in the range [0.1, 0.5]. The magnitude response of an ideal Hilbert transformer, which has an infinitely large order, has a constant value in the specified frequency range. The impulse response of the designed filter shows that this filter is antisymmetric.

#### Designing Type III Hilbert Transformers

Type III (even order, antisymmetric) Hilbert transformers are useful if you want to filter out high frequencies. Type III filters constrain the amplitude to zero at the Nyquist frequency of 0.5 Hz. By changing the frequency range of the previous example to [0.05, 0.45] and maintaining the corresponding amplitude at [−1, −1], you can design a bandpass-like Hilbert transformer. For this example, you design a Type III Hilbert transformer with an order of 12 by entering the specifications shown in the following figure into the DFD Remez Design VI.

[IMAGE alt='image' src='hilbert-type-3-specs.gif']

The following figure shows the magnitude response of the resulting Type III Hilbert transformer.

[IMAGE alt='image' src='hilbert-type-3-response.gif']

In the first figure, you can see that the magnitude response of the designed filter is fairly constant in the range [0.05, 0.45] and is zero at 0.5 Hz. The figure also shows that the magnitude response contains ripples. To minimize the ripples, you can specify a larger value for the **order** input.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/iir_direct_specs.html language=enus -->
## TOPIC 00051: IIR Direct Form Structures (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/iir_direct_specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/iir_direct_specs.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### IIR Direct Form Structures (Digital Filter Design Toolkit)

The transfer function of an infinite impulse response (IIR) filter is defined as follows:

[IMAGE alt='image' src='equ_iir_transfer_function.gif']

where *z* is a complex variable, *M* is the order of the numerator, *N* is the order of the denominator, *a* is the set of reverse coefficients, and *b* is the set of forward coefficients.

#### IIR Direct Form I

The IIR Direct Form I structure is the most straightforward IIR structure from a filter transfer function perspective. The following figure represents the IIR Direct Form I structure. Refer to the [Understanding Filter Structure Graphs](../lvdfdtconcepts/dfd_structure_graph.html) topic for information that helps you read and understand a filter structure graph.

[IMAGE alt='image' src='iir_direct_form_i.gif']

|  | Note This figure and the following figures show a special case when N = M. |
| --- | --- |

#### IIR Direct Form II

The following figure represents the IIR Direct Form II structure. You can see that this structure contains fewer mathematical operations and delays.

[IMAGE alt='image' src='iir_direct_form_ii.gif']

#### IIR Direct Form I Transposed

The following figure represents the IIR Direct Form I Transposed structure.

[IMAGE alt='image' src='iir_direct_form_i_transpose.gif']

#### IIR Direct Form II Transposed

The following figure represents the IIR Direct Form II Transposed structure.

[IMAGE alt='image' src='iir_direct_form_ii_transpos.gif']

The IIR Direct Form I and Form II Transposed structures implement forward coefficients first. The Form I Transposed and Form II structures implement reverse coefficients first. Using Form I and Form II and their transposed structures has the same advantages and disadvantages as using the [FIR Direct Form](../lvdfdtconcepts/fir_filter_specs.html#direct) and [FIR Direct Form Transposed](../lvdfdtconcepts/fir_filter_specs.html#transposed) structures. The IIR Direct Form structures usually require few mathematical operations. However, the sensitivity to finite word length effects limits the use of this form in fixed-point implementations. Use the [IIR Cascaded Second-Order Sections Form structures](../lvdfdtconcepts/iir_sos_specs.html) to alleviate [finite word length effects](../lvdfdtconcepts/dfd_fp_process.html#finite_effects).

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/iir_sos_specs.html language=enus -->
## TOPIC 00052: IIR Cascaded Second-Order Sections Form Structures (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/iir_sos_specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/iir_sos_specs.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### IIR Cascaded Second-Order Sections Form Structures (Digital Filter Design Toolkit)

The transfer function of an infinite impulse response (IIR) filter with a Cascaded Second-Order Sections Form structure is defined as follows:

[IMAGE alt='image' src='equ_iir_cascaded_transfer_func.gif']

where *z* is a complex variable, *N* is the number of sections, *a* is the set of reverse coefficients, and *b* is the set of forward coefficients.

#### IIR Cascaded Second-Order Sections Form I

Comparing with the [IIR Direct Form structures](../lvdfdtconcepts/iir_direct_specs.html), the IIR Cascaded Second-Order Sections Form structures have more computational complexity. However, the cascaded structures help alleviate [finite word length effects](../lvdfdtconcepts/dfd_fp_process.html#finite_effects). The following figure represents the IIR Cascaded Second-Order Sections Form I structure. Refer to the [Understanding Filter Structure Graphs](../lvdfdtconcepts/dfd_structure_graph.html) topic for information that helps you read and understand a filter structure graph.

[IMAGE alt='image' src='cascaded_2nd_order_form_i.gif']

#### IIR Cascaded Second-Order Sections Form II

The following figure represents the IIR Cascaded Second-Order Sections Form II structure. Comparing with Form I, this structure uses the same number of mathematical operations but fewer delays.

[IMAGE alt='image' src='cascaded_2nd_order_form_ii.gif']

#### IIR Cascaded Second-Order Sections Form I Transposed

The following figure represents the IIR Cascaded Second-Order Sections Form I Transposed structure.

[IMAGE alt='image' src='cascaded_2nd_order_form_i_t.gif']

#### IIR Cascaded Second-Order Sections Form II Transposed

The following figure represents the IIR Cascaded Second-Order Sections Form II Transposed structure.

[IMAGE alt='image' src='cascaded_2nd_order_form_ii_t.gif']

The IIR Cascaded Second-Order Sections Form I and Form II Transposed structures implement forward coefficients first. The Form I Transposed and Form II structures implement reverse coefficients first. The IIR Cascaded Second-Order Sections Form II structure has the same computational complexity as the Form I, but the Form I requires more memory for saving internal states. The Form II Transposed is the structure that you most frequently use. Using the Form I and Form II and their transposed structures has the same advantages and disadvantages as using the [FIR Direct Form](../lvdfdtconcepts/fir_filter_specs.html#direct) and [FIR Direct Form Transposed](../lvdfdtconcepts/fir_filter_specs.html#transposed) structures.

|  | Note If you want to generate LabVIEW FPGA code from an IIR filter, National Instruments recommends you use the IIR Cascaded Second-Order Sections Form II Transposed structure for this filter. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/labview_dfd_toolkit.html language=enus -->
## TOPIC 00053: Digital Filter Design Toolkit

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/labview_dfd_toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/labview_dfd_toolkit.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Digital Filter Design Toolkit

June 2014, 371988G-01

The LabVIEW Digital Filter Design Toolkit includes tools for designing, analyzing, and processing floating-point and fixed-point digital filters, including multirate filters. The Digital Filter Design Toolkit includes tools for designing, analyzing, and processing filter banks. The Digital Filter Design Toolkit also includes tools for designing, analyzing, simulating, and using adaptive filters.

This help file contains information about the general design process and the tools in the Digital Filter Design Toolkit that you can use in a digital filter or filter bank design. This help file also contains information about the general process and the tools in the Digital Filter Design Toolkit that you can use in an adaptive filter for different applications and with different adaptive filter algorithms.

|  | Note All occurrences of filters in this book refer to single-rate filters unless these topics explicitly use multirate filters. |
| --- | --- |

You can use the [Signal Processing](/csh?topicname=lvanls/signal_processing_vis.html) VIs in the LabVIEW Full or Professional Development System to perform waveform measurements, waveform conditioning, waveform monitoring, waveform generation, signal processing, and point-by-point analysis. The Signal Processing VIs contain some digital filter design VIs similar to VIs in the Digital Filter Design Toolkit. For example, the [Butterworth Coefficients](/csh?topicname=lvanls/butterworth_coefficients.html) VI is similar to the [DFD Butterworth Design](/csh?topicname=lvdigfiltdestk/dfd_butterworth.html) VI and the [Parks-McClellan](/csh?topicname=lvanls/parks_mcclellan.html) VI is similar to the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI. However, the [Digital Filter Design](/csh?topicname=lvdigfiltdestk/dfd_vis.html) VIs provide more capabilities, such as support for arbitrary phase and magnitude specifications and fixed-point filter design.

Although the VIs have similar functionality, the results you obtain might be different because the design algorithms are different. Refer to the National Instruments Web site at ni.com for information about working with the Signal Processing VIs and the Digital Filter Design VIs.

© 2005–2014 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/lattice_allpass.html language=enus -->
## TOPIC 00054: Lattice Allpass Structures (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/lattice_allpass.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/lattice_allpass.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Lattice Allpass Structures (Digital Filter Design Toolkit)

For an allpass filter, you can implement one of the following section types of lattice allpass filter structures:

- Basic section type
- One multiplier section type
- Normalized section type

The following figure represents the basic section type of a lattice allpass filter structure. Refer to the [Understanding Filter Structure Graphs](../lvdfdtconcepts/dfd_structure_graph.html) topic for information that helps you read and understand a filter structure graph.

[IMAGE alt='image' src='lattisallpassbasic.gif']

The total number of the lattice reflection coefficients *k* is *M*, where *M* is the filter order. The total number of multipliers is 2*M*.

The following figure represents the one multiplier section type of a lattice allpass filter structure.

[IMAGE alt='image' src='lattisallpassmulti.gif']

The total number of the lattice reflection coefficients *k* is *M*, which is the same as in the basic section type. However, the total number of multipliers is only *M*, which is half the number that the basic section type requires. Therefore, the one multiplier section type of a lattice allpass structure involves fewer multipliers than other section types. Fewer multipliers require less hardware resources.

The following figure represents the normalized section type of a lattice allpass filter structure.

[IMAGE alt='image' src='lattisallpassnorm.gif']

You can derive *k*' from *k* in the normalized section type by using the formula [IMAGE alt='image' src='eq1_lattice.gif'].

One advantage of the normalized section type structure is that this structure automatically scales the internal signals in each lattice section. Unfortunately, scaling the internal signals increases the implementation complexity.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/lattice_ar_specs.html language=enus -->
## TOPIC 00055: Lattice AR Structures (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/lattice_ar_specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/lattice_ar_specs.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Lattice AR Structures (Digital Filter Design Toolkit)

For an all-pole infinite impulse response (IIR) filter, you can implement one of the following section types of lattice autoregressive (AR) filter structures:

- Basic section type
- One multiplier section type
- Normalized section type

The following figure represents the basic section type of a lattice AR filter structure. Refer to the [Understanding Filter Structure Graphs](../lvdfdtconcepts/dfd_structure_graph.html) topic for information that helps you read and understand a filter structure graph.

[IMAGE alt='image' src='lattisarbasic.gif']

The total number of the lattice reflection coefficients *k* is *M*, where *M* is the filter order. The total number of multipliers is 2*M*.

The following figure represents the one multiplier section type of a lattice AR filter structure.

[IMAGE alt='image' src='lattisarmulti.gif']

The total number of the lattice reflection coefficients k is *M*, which is the same as in the basic section type. However, the total number of multipliers is only *M*, which is half the number that the basic section type requires. Therefore, the one multiplier section type of a lattice AR structure involves fewer multipliers than other section types. Fewer multipliers require less hardware resources.

The following figure represents the normalized section type of a lattice AR filter structure.

[IMAGE alt='image' src='lattisarnorm.gif']

You can derive *k*' from *k* in the normalized section type by using the formula [IMAGE alt='image' src='eq1_lattice.gif'].

One advantage of the normalized section type structure is that this structure automatically scales the internal signals in each lattice section. Unfortunately, scaling the internal signals increases the implementation complexity.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/lattice_arma_specs.html language=enus -->
## TOPIC 00056: Lattice ARMA Structures (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/lattice_arma_specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/lattice_arma_specs.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Lattice ARMA Structures (Digital Filter Design Toolkit)

For an infinite impulse response (IIR) filter, you can implement one of the following section types of lattice autoregressive-moving average (ARMA) filter structures:

- Basic section type
- One multiplier section type
- Normalized section type

The following figure represents the basic section type of a lattice ARMA filter structure. Refer to the [Understanding Filter Structure Graphs](../lvdfdtconcepts/dfd_structure_graph.html) topic for information that helps you read and understand a filter structure graph.

[IMAGE alt='image' src='lattisarmabasic.gif']

The total number of the lattice reflection coefficients *k* is *M*, where *M* is the filter order. The total number of the lattice ladder coefficients *v* is *M*+1. The total number of multipliers is 3*M*+1.

The following figure represents the one multiplier section type of a lattice ARMA filter structure.

[IMAGE alt='image' src='lattisarmamulti.gif']

The total number of coefficients *k* and *v* is 2*M*+1, which is the same as in the basic section type. However, the total number of multipliers is only 2*M*+1, which is less than the number of multipliers in the basic section type. Therefore, the one multiplier section type of a lattice ARMA structure involves fewer multipliers than other section types. Fewer multipliers require less hardware resources.

The following figure represents the normalized section type of a lattice ARMA filter structure.

[IMAGE alt='image' src='lattisarmanorm.gif']

You can derive *k*' from *k* in the normalized section type by using the formula [IMAGE alt='image' src='eq1_lattice.gif'].

One advantage of the normalized section type structure is that this structure automatically scales the internal signals in each lattice section. Unfortunately, scaling the internal signals increases the implementation complexity.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/lattice_ma_specs.html language=enus -->
## TOPIC 00057: Lattice MA Structures (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/lattice_ma_specs.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/lattice_ma_specs.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Lattice MA Structures (Digital Filter Design Toolkit)

For a minimum or maximum phase finite impulse response (FIR) filter, you can implement a lattice moving average (MA) filter structure. The following figure represents the lattice MA filter structure for a minimum phase filter. *M* is the filter order. Refer to the [Understanding Filter Structure Graphs](../lvdfdtconcepts/dfd_structure_graph.html) topic for information that helps you read and understand a filter structure graph.

[IMAGE alt='image' src='lattismaminph.gif']

The following figure represents the lattice MA filter structure for a maximum phase filter.

[IMAGE alt='image' src='lattismamaxph.gif']

For both the minimum and maximum phase type, the total number of the lattice reflection coefficients *k* is *M*. The total number of multipliers is 2*M*.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/linear_min_filters.html language=enus -->
## TOPIC 00058: Linear Phase Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/linear_min_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/linear_min_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Linear Phase Filters (Digital Filter Design Toolkit)

Linear phase digital filters allow all the frequency components of an input signal to pass through the filter with the same delay, which means that the group delay through the filter is a constant value independent of the frequency. Linear phase filters are useful in filtering applications in which you want to minimize signal distortion and spreading over time.

Nonlinear phase response, or dispersion, can be harmless in audio and other applications in which mild phase distortion is often imperceptible to humans. However, phase distortion can be harmful in some applications. For example, in digital communications applications, signal spreading caused by phase distortion can cause interference between time concentrated information symbols.

A minimum phase filter is a type of nonlinear phase filter that optimally minimizes the group delay at all frequencies for a given magnitude response at the expense of phase distortion. Minimum phase filters can be useful in control applications in which minimizing delay is more important than minimizing signal spreading.

#### Mathematical Definition

The digital filter frequency response *H*(*f*) is expressed in terms of magnitude and phase in the following equation:

| H(f) = \|H(f)\|ejφ(f) | (A) |
| --- | --- |

where |*H*(*f*)| and *φ*(*f*) are both real-valued functions of frequency *f* and represent the magnitude and phase of the frequency response.

Only finite impulse response (FIR) filters can have exactly linear phase. You can design linear phase FIR filters using either window-based design methods or the Remez design method. The Remez design method in the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI is more powerful and flexible than window-based design methods.

The equation above reduces to the following equation for a linear phase FIR digital filter.

| H(f) = (j)m A(f)e−jπNf | (B) |
| --- | --- |

| where | m = 0, 1 |
| --- | --- |
|  | A(f) is the amplitude response of the filter |
|  | N is the order of the filter, which is equal to the number of filter taps minus one |
|  | f is the normalized frequency with the range [0, 0.5] |
|  | If the filter coefficients h(n) (where n = 0, 1, .., N) are symmetric, h(n) = h(N−n), and m must be 0 |
|  | If the filter coefficients h(n) are antisymmetric, h(n) = −h(N−n), and m must be 1 |

#### Types of Linear Phase FIR Filters

The following table lists the four types of linear phase FIR filters and the characteristics of each type. The book [Digital Filter Design](../lvdfdtconcepts/dfd_related_doc.html) contains more information about linear phase FIR filters.

| Type | Classification | Frequency Characteristics |
| --- | --- | --- |
| I | Even-order, symmetric | A(f) is symmetric about f = 0 and f = 0.5A(f) is periodic with period 1 |
| II | Odd-order, symmetric | A(f) is symmetric about f = 0 and antisymmetric about f = 0.5A(f) is constrained to 0 at f = 0.5A(f) is periodic with period 2 |
| III | Even-order, antisymmetric | A(f) is antisymmetric about f = 0 and f = 0.5A(f) is constrained to 0 at both f = 0 and f = 0.5A(f) is periodic with period 1 |
| IV | Odd-order, antisymmetric | A(f) is antisymmetric about f = 0 and symmetric about f = 0.5A(f) is constrained to 0 at f = 0A(f) is periodic with period 2 |

Use the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI to design linear phase FIR filters. Set the **order** input and the **filter type** input according to the Classification column of the table above. The DFD Remez Design VI designs the appropriate type of linear phase FIR filter based on the two inputs.

Use the following guidelines to determine the type of linear phase FIR filter you design.

- Type III and IV cannot be lowpass-like filters.
- Type II and III cannot be highpass-like filters.
- Type III and IV work well for differentiators or Hilbert transformers because they can give a constant 90° phase shift.

Experiment with different types. More than one type might produce an acceptable result for some target filter responses, but only one type can meet the target specifications. Select the filter type that has the smoothest frequency response. For example, the following figure illustrates the types of frequency response symmetry for each type of linear phase FIR filter, assuming a sampling frequency of *f*<sub>*s*</sub> = 1. Notice that in this example, a Type I or Type II filter has glitches, or rapid changes, at the frequency point of 1. A Type III or Type IV filter yields the smoothest frequency response because they do not contain glitches.

[IMAGE alt='image' src='freq_resp_types.gif']

The following figure shows the magnitude response requirement of an ITU-468-weighting filter. Notice that the magnitude response is zero at DC and small but nonzero at high frequencies. Therefore, Type IV (odd order, antisymmetric) is the best choice for approximating this response.

[IMAGE alt='image' src='itu468-filter.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/lpth_norm_design.html language=enus -->
## TOPIC 00059: Least Pth Norm Design Method (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/lpth_norm_design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/lpth_norm_design.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Least Pth Norm Design Method (Digital Filter Design Toolkit)

You can use the [DFD Least Pth Norm Design](/csh?topicname=lvdigfiltdestk/dfd_lpth_norm.html) VI to design the following infinite impulse response (IIR) and finite impulse response (FIR) filters.

- Linear phase FIR design
- Approximated linear phase IIR design
- Minimum and maximum phase IIR design

Although you can design linear phase filters using the DFD Remez Design VI, you can design FIR and IIR filters with arbitrary magnitude and phase constraints using the DFD Least Pth Norm Design VI.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/lpth_norm_linearfir.html language=enus -->
## TOPIC 00060: Least Pth Norm Linear Phase FIR Design (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/lpth_norm_linearfir.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/lpth_norm_linearfir.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Least Pth Norm Linear Phase FIR Design (Digital Filter Design Toolkit)

You can design a linear phase FIR filter using the [DFD Least Pth Norm Design](/csh?topicname=lvdigfiltdestk/dfd_lpth_norm.html) VI by setting the following specifications. Set the denominator order to 0, the **filter type** to Symmetric or Antisymmetric, all phases in the band specifications to 0, and the group delay to half of the numerator order.

For example, suppose you want to design a linear phase FIR lowpass filter with a passband frequency range of [0, 0.2] and a stopband frequency range of [0.3, 0.5]. Set the specifications as shown in the following figure:

[IMAGE alt='image' src='lpth-linear-phase-specs.gif']

The following figure shows the magnitude response of the designed filter. Because **p** is 128, the designed filter is almost identical to the result using the Remez equi-ripple design with the same filter specification.

[IMAGE alt='image' src='lpth-linear-phase-mag-respo.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/min_max_iir.html language=enus -->
## TOPIC 00061: Minimum and Maximum Phase IIR Design (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/min_max_iir.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/min_max_iir.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Minimum and Maximum Phase IIR Design (Digital Filter Design Toolkit)

You can use the **Minimum Phase** or **Maximum Phase** option of the **filter type** input if you want a minimum or maximum phase response or if the phase response is not important. When you use the **Minimum Phase** or **Maximum Phase** option, the [DFD Least Pth Norm Design](/csh?topicname=lvdigfiltdestk/dfd_lpth_norm.html) VI ignores the **phase** and **group delay** inputs.

For example, suppose you want to design a minimum phase IIR lowpass filter with a passband frequency range of [0, 0.2] and a stopband frequency range of [0.3, 0.5]. You can set the specifications as shown in the following figure:

[IMAGE alt='image' src='lpth-min-iir-specs.gif']

The following figure shows the magnitude response of the designed filter.

[IMAGE alt='image' src='lpth-min-iir-mag-response.gif']

The following figure shows the phase response of the designed filter.

[IMAGE alt='image' src='lpth-min-iir-phase-response.gif']

Notice that the designed filter has greater stopband attenuation than the [approximately linear phase IIR filter designed](../lvdfdtconcepts/applinear_iir_design.html), but the passband phase response is now highly nonlinear.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/model_fp_filter.html language=enus -->
## TOPIC 00062: Creating Fixed-Point Filter Models (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/model_fp_filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/model_fp_filter.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Fixed-Point Filter Models (Digital Filter Design Toolkit)

In a fixed-point implementation, after [quantizing the coefficients of a reference floating-point filter](../lvdfdtconcepts/quantize_fl_filters.html), you also must configure all other [quantizers](../lvdfdtconcepts/configure_quantizer.html), such as the input, output, and multiplicand quantizers. This process [creates a fixed-point model](/csh?topicname=lvdfdthowto/design_fxp_filter_5.html) for the filter. You must create a fixed-point filter model before you simulate the filtering process or generate code from the filter. You can use either the [DFD FXP Modeling](/csh?topicname=lvdigfiltdestk/dfd_fxp_modeling.html) VI or the [DFD FXP Set Quantizer](/csh?topicname=lvdigfiltdestk/dfd_fxp_set_q.html) VI to create fixed-point filter models. Refer to the *Details* section of the DFD FXP Set Quantizer VI for information about guidelines on the quantizer settings.

|  | Note After quantizing the coefficients of a reference floating-point filter, you automatically obtain a fixed-point filter model with the following default values: input word length = output word length = 16. The Specifying the Word Length and Integer Word Length topic contains more information about the effects of different word length values. |
| --- | --- |

If you use the DFD FXP Modeling VI to create the fixed-point filter model, complete the following steps:

1. Specify the word lengths and integer word lengths for the input signal and word lengths for the output signal.
2. Set the rounding mode for the output signal.

The DFD FXP Modeling VI automatically calculates all quantizer settings of the fixed-point filter model. You can use the [DFD FXP Get Quantizer](/csh?topicname=lvdigfiltdestk/dfd_get_quantizer.html) VI to retrieve the quantizer settings or use the [DFD FXP Set Quantizer](/csh?topicname=lvdigfiltdestk/dfd_fxp_set_q.html) VI to modify the quantizer settings.

|  | Note Output quantizers generally have different integer word lengths from the input quantizers. Before generating code, check the quantizer settings to confirm or modify the settings you want to use for the fixed-point filter. If you reduce the default output integer word length, National Instruments recommends that you change the overflow mode to Saturate. |
| --- | --- |

If you use the DFD FXP Set Quantizer VI to create the fixed-point filter model, you must [configure the quantizers](../lvdfdtconcepts/configure_quantizer.html).

Refer to the Step 4 - Model and Simulate FXP Lowpass (Lowpass) VI in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter directory for an example that demonstrates how to create a fixed-point model of a lowpass filter and [simulate the filtering result](../lvdfdtconcepts/sim_fp_filters.html).

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/mrate_basics.html language=enus -->
## TOPIC 00063: Multirate Filter Basics (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/mrate_basics.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/mrate_basics.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multirate Filter Basics (Digital Filter Design Toolkit)

Use multirate filters in digital signal processing systems when different sampling frequencies exist in different parts of a system, or when you want to reduce computational complexity in systems by using a uniform sampling frequency. You can change the sampling frequency of a filter by using [decimation](../lvdfdtconcepts/dfd_decimation.html), [interpolation](../lvdfdtconcepts/dfd_interpolation.html), or [rational resampling](../lvdfdtconcepts/rational_resampling.html). This book describes the three filtering modes and the [zero-phase filtering](../lvdfdtconcepts/zero_phase_filtering.html) mode, which enables you to eliminate the delay between the input and output signals.

Use [finite impulse response (FIR) structures](../lvdfdtconcepts/fir_filter_specs.html) to implement multirate filters. Compared to infinite impulse response (IIR) structures, FIR structures provide unconditional stability, phase linearity, and better finite-precision performance. Furthermore, FIR structures contain only feedforward signal paths that enable you to simplify the implementation of decimation and interpolation filters. In principle, you can use both lowpass and highpass FIR filters to implement multirate filters. However, the LabVIEW Digital Filter Design Toolkit provides lowpass multirate FIR filters only.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/mstage_mrate_filt.html language=enus -->
## TOPIC 00064: Multistage Multirate Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/mstage_mrate_filt.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/mstage_mrate_filt.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multistage Multirate Filters (Digital Filter Design Toolkit)

The filters you design in the [Designing Floating-Point Multirate Filters](../lvdfdtconcepts/design_fl_multirate.html) and the [Designing Fixed-Point Multirate Filters](../lvdfdtconcepts/design_fp_multirate.html) books are single-stage multirate filters. In single-stage multirate filters, the normalized transition bandwidth of the lowpass FIR filter *H*(*z*) is inversely related to the filter order. The narrower the normalized transition bandwidth, the higher the filter order. A lowpass FIR filter with a narrow normalized transition bandwidth therefore requires more resources to implement.

In decimation and interpolation multirate filters, the normalized transition bandwidth inversely relates to the decimation factor *M* and the interpolation factor *L*. The order of a decimation or interpolation filter increases as *M* or *L* increases, and the resulting multirate filter uses more resources to implement. You can use multistage multirate filters to simplify multirate filters that have large sampling frequency conversion factors.

A multistage filter gradually increases or decreases the sampling frequency by passing the signal through two or more resampling stages. Each stage has a lower decimation or interpolation factor than the corresponding single-stage multirate filter and contains fewer operations. Except when the sampling frequency conversion factor is a prime number, multistage filtering is more efficient than single-stage filtering because you can change the sampling frequency in multiple stages rather than in a single stage. Using multiple stages reduces the computation operations and memory usage. Refer to the book [Multirate Systems and Filter Banks](../lvdfdtconcepts/dfd_related_doc.html) for more information about multistage multirate filter design.

In a multistage decimation system, the overall decimation factor *M* is equal to *M*<sub>1</sub>*M*<sub>2</sub>...*M*<sub>*N*</sub>, where *M*<sub>*i*</sub> is the decimation factor of stage *i*. The following figure illustrates this *N*-stage decimation process.

[IMAGE alt='image' src='multistage_decim_fil.gif']

In a multistage interpolation system, the overall interpolation factor *L* is equal to *L*<sub>1</sub>*L*<sub>2</sub>...*L*<sub>*N*</sub>, where *L*<sub>*i*</sub> is the interpolation factor of stage *i*. The following figure illustrates the *N*-stage interpolation process.

[IMAGE alt='image' src='multistage_interp_fil.gif']

You can use the [DFD NStage MRate Filter Design](/csh?topicname=lvdigfiltdestk/dfd_ns_mr_filter.html) VI to design multistage multirate filters with either of the following approaches:

- Specify the overall sampling frequency change factor and the factors for every stage.
- Specify only the overall sampling frequency change factor and use the DFD NStage MRate Filter Design VI to determine the factors for every stage.

Use the following guidelines when you manually specify factorizations.

- Use two or three stages for optimal or near optimal results.
- Use the largest factor at the highest sampling frequency. Decimate in order from the largest to the smallest factor and interpolate in order from the smallest to the largest factor.

When you implement a fixed-point multistage multirate filter, the output signal [word length](../lvdfdtconcepts/specify_wl_iwl.html) of the previous filter stage must be the same as the input signal word length of the next filter stage. Refer to the Multistage Multirate Filter Design VI in the labview\examples\Digital Filter Design\Floating-Point Filters\Multirate directory for an example that demonstrates how to use the DFD NStage MRate Filter Design VI to design a multistage multirate filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/narrowband_fir.html language=enus -->
## TOPIC 00065: Narrowband FIR Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/narrowband_fir.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/narrowband_fir.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Narrowband FIR Filters (Digital Filter Design Toolkit)

The order of a [finite impulse response (FIR)](../lvdfdtconcepts/fir_and_iir_filters.html) filter is related inversely to the transition bandwidth. Conventional FIR filters with narrow transition bands and high orders might be too complex to implement. You might consider designing narrowband filters using [infinite impulse response (IIR)](../lvdfdtconcepts/fir_and_iir_filters.html) filters. However, narrowband IIR filters typically have nonlinear phase, especially near the transition band, and are numerically sensitive. You might be able to meet the target filter specifications by using narrowband FIR filters instead of using IIR filters.

The [DFD Narrowband Filter Design](/csh?topicname=lvdigfiltdestk/dfd_narrow_filter.html) VI uses interpolated FIR (IFIR) techniques and frequency response masking techniques to design narrowband FIR filters with significantly less computational complexity than conventional FIR solutions, as shown in the following figure:

[IMAGE alt='image' src='narrowband_fil.gif']

| (a) Frequency response of the target narrowband FIR filter H(z) |
| --- |
| (b) Frequency response of a shaping filter G(z) |
| (c) Frequency response of an interpolated filter G(z N) |
| (d) Frequency response of a masking filter I(z) |

To better understand how these techniques work, assume that the target narrowband filter has the frequency response shown in part (a) of the previous figure. The first step is to design a shaping filter as shown in part (b). The shaping filter has a wider transition band than the target narrowband filter and determines the spectrum shape of the target narrowband filter. The next step is to design an interpolated filter with the frequency response shown in part (c). Notice that the coefficients of the interpolated filter *G*(*z*<sup>*N*</sup>) are constructed by inserting *N*−1 zeroes between every two adjacent coefficients of *G*(*z*). The magnitude response of the first image of *G*(*z*<sup>*N*</sup>) in part (c) is the same as that of the target filter *H*(*z*) in part (a). To remove the unwanted images of *G*(*z*<sup>*N*</sup>), you need to cascade the interpolated filter *G*(*z*<sup>*N*</sup>) with a masking filter *I*(*z*), which has the magnitude response shown in part (d).

By cascading the interpolated filter *G*(*z*<sup>*N*</sup>) and the masking filter *I*(*z*) as illustrated in the following figure, you can obtain the target narrowband filter *H*(*z*).

[IMAGE alt='image' src='2_stage_nrwbnd_fil.gif']

This figure shows a two-stage narrowband filter structure. Because *I*(*z*) and *G*(*z*) have a much wider transition band than the original filter *H*(*z*), the overall order of *I*(*z*) and *G*(*z*) is lower than the order of *H*(*z*), which makes the cascaded filters computationally efficient.

Similarly, if the lowpass masking filter *I*(*z*) also is a narrowband filter, you can make it more efficient by using the two-stage narrowband filter structure. The following figure illustrates the diagram of the resulting three-stage structure. This figure uses a [cascaded integrator comb (CIC) filter](../lvdfdtconcepts/cic_filters.html) as the first-stage lowpass masking filter in this case because of the lowpass nature and efficient implementation.

[IMAGE alt='image' src='3_stage_nrwbnd_fil.gif']

Assume a signal with a sampling frequency of 5 kHz. The signal has useful information at frequencies below 100 Hz and noise above 120 Hz. To suppress the noise, you can apply a narrowband lowpass filter with the following specifications:

| Specification | Value |
| --- | --- |
| Passband Range | 0−100 Hz |
| Passband Ripple | 0.05 dB |
| Stopband Range | 120−2500 Hz |
| Stopband Attenuation | 60 dB |

If you design the lowpass FIR filter using the DFD Remez Design VI, the resulting filter has 689 [taps](/csh?topicname=lvanlsconcepts/lvac_taps.html). Given the same specifications, the DFD Narrowband Filter Design VI generates a three-stage narrowband filter. The resulting CIC filter has 5 stages, the interpolated filter *F*(*z*<sup>*M*</sup>) has 18 nonzero coefficients and the interpolated filter *G*(*z*<sup>*N*</sup>) has 27 nonzero coefficients. The CIC narrowband filter is 78% less computationally complex than the lowpass FIR filter you design using the DFD Remez Design VI. The following figure shows the magnitude response of the designed narrowband filter.

[IMAGE alt='image' src='narrowband-response.gif']

To plot the frequency response of narrowband FIR filters, use the [DFD Plot Narrowband Freq Response](/csh?topicname=lvdigfiltdestk/dfd_plot_narrow_freq.html) VI. To perform narrowband filtering, use the [DFD Narrowband Filtering](/csh?topicname=lvdigfiltdestk/dfd_narrow_filtering.html) VI.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/notch_peak_filters.html language=enus -->
## TOPIC 00066: Notch and Peak Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/notch_peak_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/notch_peak_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Notch and Peak Filters (Digital Filter Design Toolkit)

Use notch filters to suppress noise at a specified frequency, such as an AC powerline frequency. Use peak filters to enhance the signal at a particular frequency. The following figure shows a typical notch filter.

[IMAGE alt='image' src='notchfilter.gif']

In a notch filter, *f*
 <sub>0</sub> denotes the center frequency and Δ*f* denotes the frequency bandwidth at *A*<sub>*b*</sub>. The default value of *A*<sub>*b*</sub> is −3 dB. *Q* = *f*
 <sub>0</sub>/Δ*f*, which denotes the sharpness of the notch. Increasing the value of *Q* results in a sharper notch filter.

The following figure shows a typical peak filter.

[IMAGE alt='image' src='peakfilter.gif']

In a peak filter, *Q* denotes the sharpness of the peak. Increasing the value of *Q* results in a sharper peak filter.

The [DFD IIR Notch Peak Design](/csh?topicname=lvdigfiltdestk/dfd_iir_notch_peak.html) VI designs a second-order infinite impulse response (IIR) notch or peak filter using a bilinear transform method. The following equation shows the transfer function of a notch filter.

[IMAGE alt='image' src='equ_notch_trans_func.gif']

The following equation shows the transfer function of a peak filter.

[IMAGE alt='image' src='equ_peak_trans_func.gif']

where *a*
 <sub>0</sub>, *a*
 <sub>1</sub>, *b*
 <sub>0</sub>, and *b*
 <sub>1</sub> are filter coefficients.

For example, assume a time waveform of a noisy electrocardiogram (ECG) signal sampled at 333 Hz, as shown in the following figure:

[IMAGE alt='image' src='noisy-ecg-signal.gif']

The following figure shows the spectrum of the same noisy signal. In this figure, you can identify the noise at 60 Hz.

[IMAGE alt='image' src='noisy-ecg-spectrum.gif']

To remove the noise at 60 Hz, you can design a notch filter using the DFD IIR Notch Peak Design VI with the following specifications:

| DFD IIR Notch Peak Design VI Inputs | Value |
| --- | --- |
| filter type | Notch |
| f0 [Hz] | 60 |
| Q factor | 40 |
| fs [Hz] | 333 |

The following figure shows the magnitude response of the resulting notch filter.

[IMAGE alt='image' src='notch-filter-mag-response.gif']

The following figure shows that the filtered ECG signal is close to the original noise-free samples.

[IMAGE alt='image' src='filtered-ecg-signal.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/nyquist_filters.html language=enus -->
## TOPIC 00067: Nyquist, Raised Cosine, and Halfband Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/nyquist_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/nyquist_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Nyquist, Raised Cosine, and Halfband Filters (Digital Filter Design Toolkit)

Nyquist filters have the following magnitude response specifications:

| Filter Specification | Value Range |
| --- | --- |
| Passband edge frequency | [0, fs/2M−ε] |
| Stopband edge frequency | [fs/2M+ε, fs/2] |

In this table, *M* denotes the sampling frequency conversion factor and *f*<sub>*s*</sub> denotes the sampling frequency of a Nyquist filter. For an [interpolation](../lvdfdtconcepts/dfd_interpolation.html) Nyquist filter, *f*<sub>*s*</sub> equals *L* times the sampling frequency of the input signal, where *L* denotes the interpolation factor. For a [decimation](../lvdfdtconcepts/dfd_decimation.html) Nyquist filter, *f*<sub>*s*</sub> equals the sampling frequency of the input signal. You can specify *ε* indirectly by using the roll off [IMAGE alt='image' src='alpha.gif'], which is defined as the following equation:

[IMAGE alt='image' src='equ_nyquist_roll_off.gif']

The following figure illustrates the magnitude response of a Nyquist filter.

[IMAGE alt='image' src='mag_resp_nyquist_fil.gif']

The following sections describe how to use the LabVIEW Digital Filter Design Toolkit to design Nyquist filters, including [raised cosine filters](#raised_cosine_filters) and [halfband filters](#halfband_filters).

#### Designing Nyquist Filters

Nyquist filters, also called *M*<sup>th</sup> band filters, are a special type of multirate finite impulse response (FIR) filter. Nyquist filter coefficients have periodic zero values every *M*<sup>th</sup> sample, except for the middle coefficient. The following figure shows the coefficients of a Nyquist filter with a sampling frequency conversion factor of 4. The 26<sup>th</sup> coefficient is the middle coefficient and does not have a zero value.

[IMAGE alt='image' src='nyquist-coefficients.gif']

The impulse response of a Nyquist filter *h*(*n*) satisfies the following equation:

[IMAGE alt='image' src='eq1_nyquist.gif']

where *c* and *k* are constants.

The *z*-transform of a Nyquist filter *H*(*z*) satisfies the following equation:

[IMAGE alt='image' src='equ_nyquist.gif']

where *W* = *e*<sup>−</sup><sup>*j*</sup><sup>2</sup><sup>*π*</sup><sup>/</sup><sup>*M*</sup> and *c* = 1/*M*. The frequency response of *H*(*zW*<sup>*k*</sup>) is the shifted version of the frequency response of *H*(*z*), so the frequency responses of all *M* uniformly shifted versions of *H*(*z*) add up to a constant.

Use the [DFD Nyquist Design](/csh?topicname=lvdigfiltdestk/dfd_nyquist_design.html) VI to design Nyquist filters. You can use Nyquist filters to remove images in interpolation. Nyquist filters modify the interpolated zeroes, but they do not change the original samples.

#### Designing Raised Cosine Filters

Raised cosine filters are a special case of Nyquist filters. As with other Nyquist filters, the coefficients of the raised cosine filter have periodic zero values every *M*<sup>th</sup> sample except for the middle coefficient. The ideal frequency response of a raised cosine filter consists of unity gain at low frequencies, a raised cosine shape in the middle, and zero gain at high frequencies. The following equation describes the magnitude response of a raised cosine filter.

[IMAGE alt='image' src='equ_nyquist_raised_cosine_1.gif']

where *f*<sub>*c*</sub> is the cutoff frequency and [IMAGE alt='image' src='alpha.gif'] is the roll off, which satisfies 0 ≤ [IMAGE alt='image' src='alpha.gif'] ≤ 1.

In digital communication systems, if you want to split the overall raised cosine filtering evenly between the transmitter filter and receiver filter, use root-raised cosine filters. The following equation describes the magnitude response of a root-raised cosine filter.

[IMAGE alt='image' src='equ_nyquist_raised_cosine_2.gif']

Use the [DFD Raised Cosine Design](/csh?topicname=lvdigfiltdestk/dfd_raised_cosine.html) VI to design raised cosine filters and root-raised cosine filters.

#### Designing Halfband Filters

Halfband filters are *M*<sup>th</sup> band filters when *M* = 2. The impulse response of a halfband filter *h*(*n*) satisfies the following equation:

[IMAGE alt='image' src='eq1_halfband.gif']

where *c* and *k* are constants. *c* usually equals 0.5.

The magnitude response of a halfband filter is symmetric with respect to the frequency *f*<sub>*s*</sub>/4. The value of the magnitude response at *f*<sub>*s*</sub>/4 is fixed to 0.5. The filter has a linear phase property. Nearly half of the filter coefficients in a halfband filter are zeroes, which greatly reduces the computations required for filtering. Use the [DFD Halfband Design](/csh?topicname=lvdigfiltdestk/dfd_halfband_design.html) VI to design halfband filters.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/poles_and_zeroes.html language=enus -->
## TOPIC 00068: Poles, Zeroes, and Pole-Zero Plots (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/poles_and_zeroes.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/poles_and_zeroes.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Poles, Zeroes, and Pole-Zero Plots (Digital Filter Design Toolkit)

The *z*-transform of a [finite impulse response (FIR)](../lvdfdtconcepts/fir_and_iir_filters.html) filter is defined as follows:

|  | (A) |
| --- | --- |

where *z*≡*e*<sup>*j2πf*</sup>, *b*<sub>*k*</sub> is the set of filter coefficients, and *N* is the order of the FIR filter. In Equation A, *z*<sub>*k*</sub> represents the roots of the polynomial *H*(*z*). *H*(*z*<sub>*k*</sub>) = 0 for all *z*<sub>*k*</sub>, so *z*<sub>*k*</sub> represents the zeroes of the filter *H*(*z*). The number of zeroes in a filter must equal the filter order *N*.

Similarly, the *z*-transform of an infinite impulse response (IIR) filter is defined by the following equation:

|  | (B) |
| --- | --- |

where *z*<sub>*k*</sub> and *p*f<sub>*k*</sub> represent the roots of the numerator polynomial and denominator polynomial, respectively. *p*<sub>*k*</sub> represents the poles of an IIR filter *H*(*z*). IIR filters have poles and zeroes, and FIR filters have only zeroes.

#### Pole-Zero Plots

From a mathematical point of view, the pole-zero plot and frequency response provide the same information. Based on the frequency response, you can obtain a pole-zero plot. Conversely, from the pole-zero plot, you can compute the frequency response.

The following figure illustrates a pole-zero plot for a particular IIR filter. The half-circle corresponds to |*z*| = 1, or the unit circle. The small circles along the half-circle represent zeroes. Each *×* represents a pole.

[IMAGE alt='image' src='zero-pole-plot.gif']

The pole-zero plot and frequency response characterize digital filters from the following perspectives:

- You can determine if a digital filter is stable by determining if the output of the digital filter is bounded for all possible bounded inputs. The necessary and sufficient condition for IIR filters to be stable is that all poles are inside the unit circle. In contrast, FIR filters are always stable because the FIR filters do not have poles.
- You can determine if pole-zero pairs are close enough to cancel out each other effectively. Try deleting close pairs and then check the resulting frequency response. Fewer pole-zero pairs means fewer computations.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/postprocess_srate.html language=enus -->
## TOPIC 00069: Postprocessing Filtered Signals (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/postprocess_srate.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/postprocess_srate.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Postprocessing Filtered Signals (Digital Filter Design Toolkit)

After you deploy fixed-point filter coefficients to the target hardware, the output data uses a fixed-point representation. To convert the output signal of the fixed-point filter into floating-point representation, you must process the fixed-point signal using the [DFD FXP Postprocessing](/csh?topicname=lvdigfiltdestk/dfd_fxp_postp.html) VI.

Refer to the Step 6 - Postprocessing (Lowpass) VI in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter directory for an example that demonstrates how to postprocess a filtered signal.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/quantize_fl_filters.html language=enus -->
## TOPIC 00070: Quantizing Floating-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/quantize_fl_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/quantize_fl_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Quantizing Floating-Point Filters (Digital Filter Design Toolkit)

After [selecting a filter structure](../lvdfdtconcepts/select_structure.html), you must [quantize](/csh?topicname=lvdfdthowto/design_fxp_filter_3.html) the coefficients of the reference floating-point filter. Quantizing the filter coefficients is the process of approximating each floating-point value with a fixed-point value that you use in a fixed-point mathematical computation or hardware implementation. Using the [DFD FXP Quantize Coef](/csh?topicname=lvdigfiltdestk/dfd_fxp_qcoef.html) VI, you can configure the [filter coefficients quantizer](../lvdfdtconcepts/configure_quantizer.html)
 *Q*<sub>*C*</sub> and convert the reference floating-point filter to a fixed-point filter.

If you use the Easy instance of the DFD FXP Quantize Coef VI to quantize the filter coefficients, you must complete the following steps:

1. Specify appropriate word length values for coefficients a/k word length and coefficients b/v word length .
2. Specify the appropriate gain processing target.
3. Specify the appropriate gain word length value. This VI automatically calculates the integer word lengths for coefficients a / k , coefficients b / v , and gain. The VI then uses the resulting values to quantize the filter coefficients.

If you use the Advanced instance of the DFD FXP Quantize Coef VI to quantize the filter coefficients, you must complete the following steps:

1. Configure the coefficients a/k quantizer and coefficients b/v quantizer.
2. Specify the appropriate gain processing target.
3. Specify the appropriate gain word length value. This VI then automatically calculates the integer word length of gain and uses the resulting value to quantize the gain if you set the gain processing input to On Target .

#### Specifying the Gain Processing Target

A filter gain implies a multiplication operation. If you process the filtered signal on a target, for example, an NI Reconfigurable I/O (RIO) target, the filtering process requires hardware resources on the target for the multiplication operation that the filter gain introduces. However, if you want to process the filtered signal on a host computer, you can move the filter gain operation to the host computer and save resources on the target. Use the **gain processing** input of the DFD FXP Quantize Coef VI to specify an appropriate gain processing target.

Refer to the Step 3 - Analyze Quantized Lowpass (Lowpass) VI in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter directory for an example that demonstrates how to quantize a floating-point lowpass filter and [analyze the quantized lowpass filter](../lvdfdtconcepts/analyze_fixedpoint.html).

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/rational_resampling.html language=enus -->
## TOPIC 00071: Rational Resampling (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/rational_resampling.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/rational_resampling.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Rational Resampling (Digital Filter Design Toolkit)

Rational resampling is the process of converting the sampling frequency of a signal to another sampling frequency that differs from the original frequency by a rational factor of *L*/*M*, where both *L* and *M* are integer values. Rational resampling also is known as fractional resampling.

Rational resampling is useful for interfacing with digital signal processing (DSP) systems that operate at different frequencies. By choosing *L* and *M* properly, you can approximate any desired sampling frequency change ratio. For example, you can use rational resampling with *L* = 147 and *M* = 160 to convert a 48 kHz signal from a professional audio system to a 44.1 kHz signal for an audio CD.

|  | Note Decimation and interpolation are special cases of rational resampling. The rational factors of decimation and interpolation are 1/M and L/1, respectively. |
| --- | --- |

You can implement a rational resampling system by cascading an *L*−fold expander with an *M*−fold decimator. You must place the expander before the decimator to avoid discarding useful frequency components in the decimation operation. The following figure shows a rational resampling filter with a rational factor of *L*/*M*.

[IMAGE alt='image' src='rational_resampling_fil.gif']

This rational resampling filter first interpolates the input signal *x*(*n*) with an *L*−fold expander and changes the sampling frequency of the original signal *f*<sub>*s*</sub> to a new sampling frequency *Lf*<sub>*s*</sub>. The expander returns an output signal *v*(*n*) with this new sampling frequency. Both the interpolation filter following the expander and the decimation filter preceding the decimator are lowpass FIR filters, and the two filters operate at the same sampling frequency *Lf*<sub>*s*</sub>. Therefore, you can integrate the two filters into one lowpass filter *H*(*z*) and place the filter between the expander and the decimator. The filter *H*(*z*) returns a new signal *w*(*n*). This rational resampling filter then decimates the signal *w*(*n*) with an *M*−fold decimator and changes the sampling frequency from *Lf*<sub>*s*</sub> to (*L*/*M*)*f*<sub>*s*</sub>. The decimator returns an output signal *y*(*n*) with this new sampling frequency.

When *L*<*M*, this rational resampling filter converts the original sampling frequency to a lower frequency, and *H*(*z*) acts as an anti-aliasing filter. When *L*>*M*, this rational resampling filter converts the original sampling frequency to a higher frequency, and *H*(*z*) acts as an anti-imaging filter. The cutoff frequency of *H*(*z*) is the smaller of the two values *f*<sub>*s*</sub>/2 and *Lf*<sub>*s*</sub>/(2*M*).

|  | Note The Multirate Processing VIs use a polyphase implementation, which is more efficient than the procedure in the previous figure, to implement rational resampling. Refer to the book Multirate Systems and Filter Banks for more information about polyphase implementations. Rational resampling filters that use a polyphase implementation compute only the final expected output samples, not the inserted zero value samples, thus reducing the computational complexity of the filters. |
| --- | --- |

The following figure illustrates the rational resampling of a signal by a factor of 2/3. The different parts in the following figure correspond to the different spectra of the signal at different stages of the rational resampling process, as shown in the previous figure. Because *L*<*M*, the lowpass filter has a cutoff frequency of *Lf*<sub>*s*</sub>/(2*M*) and acts as an anti-aliasing filter. Part (e) of this figure shows the spectrum of the output signal if you use a lowpass filter. You can see that no aliasing occurs. From part (f) of this figure, you can see that if no lowpass filter exists, or if you choose the cutoff frequency of the lowpass filter to be *f*<sub>*s*</sub>/2, aliasing occurs between each spectrum image of the decimated signal. The overlapping spectra indicate aliasing due to the decimation operation.

[IMAGE alt='image' src='rational_no_anti-aliasing.gif']

| (a) Spectrum of the original signal x(n) |
| --- |
| (b) Spectrum of the signal v(n) from directly interpolating the original signal by 2 |
| (c) Magnitude response of the anti-aliasing filter H(z) |
| (d) Spectrum of the signal w(n) from the anti-aliasing filter H(z) |
| (e) Spectrum of the output signal y(n) with the anti-aliasing filter |
| (f) Spectrum of the output signal y(n) without the anti-aliasing filter |

To design rational resampling filters, use the Rational instance of the [DFD MRate Filter Design](/csh?topicname=lvdigfiltdestk/dfd_mr_design.html) VI.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/remez_designmethod.html language=enus -->
## TOPIC 00072: Remez Design Method (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/remez_designmethod.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/remez_designmethod.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Remez Design Method (Digital Filter Design Toolkit)

The Remez algorithm generates finite impulse response (FIR) filters that minimize the maximum error between the target frequency response and the designed filter frequency response. This error specification yields filters with equi-ripple or Chebyshev error behavior.

Several [Digital Filter Design](/csh?topicname=lvdigfiltdestk/dfd_vis.html) VIs use the Remez algorithm. The [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI extends the application of the Remez algorithm to include the following advanced and specialized digital filter designs.

- Type I−IV linear phase FIR filter design
- Differentiator design
- Hilbert transformer design
- Arbitrary shape FIR filter design
- Optimal magnitude approximation design (minimum or maximum phase)
- Single-point band design
- Exact gain control design
- Ripple constraint design

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/ripple_constraint.html language=enus -->
## TOPIC 00073: Ripple Constraint Design (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/ripple_constraint.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/ripple_constraint.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Ripple Constraint Design (Digital Filter Design Toolkit)

A ripple constraint guarantees that the maximum error magnitude between the frequency response of the designed filter and the expected frequency response is equal to or below the constraint. You can specify a ripple constraint for a particular band by entering a positive value into the **ripple constraint** input for that band. When you specify a ripple constraint, the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI uses the value as the upper bound of the ripple level within that band.

|  | Note The ripple constraint in the DFD Remez Design VI works differently than the weighted ripple in the Parks-McClellan VI, which is based on the classical Remez design method. The classical Remez design method applies the ripple levels of different bands proportionally. The classical algorithm guarantees only that the designed filter has the same ripple magnitude ratios between different bands, and not the actual values that you enter. |
| --- | --- |

You might want to design filters with ripple constraints in the following situations:

- You want to specify the filter order and constrain the ripple magnitude in certain bands.
- You want to constrain all bands, and you want the DFD Remez Design VI to determine the minimum filter order that satisfies the requirements.
- You want to constrain all bands and specify the filter order as well. The DFD Remez Design VI reports an error if the constraints cannot be met. Otherwise, the DFD Remez Design VI returns a valid design with the ripple ratios among different bands the same as the ratios of the ripple constraints.

As an example for the first situation, suppose you want to design a 15<sup>th</sup> order lowpass filter, and you want the passband ripple magnitude to be no more than 0.1. You can set the passband frequency range to [0, 0.2] and the stopband frequency range to [0.3, 0.5] and apply equal weights in both bands. The following figure shows the magnitude response of the designed filter.

[IMAGE alt='image' src='lowpass-with-ripple-constra.gif']

Notice that the passband ripple is much smaller than the requirement. To make the passband ripple just touch the upper constraint, you can reduce the initial **weight** in the passband to [0.01, 0.01] and run the VI again. The following figure shows the magnitude response of the redesigned filter.

[IMAGE alt='image' src='lowpass-with-ripple-con-weight.gif']

The smaller **weight** value allows the DFD Remez Design VI to design a filter with a passband ripple that initially exceeds the constraint and then automatically adjust the weight level iteratively until the constraint is met.

As an example for the second situation, suppose you want to design a lowpass filter with the same passband and stopband frequency ranges as the previous example. You can specify the ripple constraints for the passband and the stopband as 0.01 and 0.001, respectively, and set the **minimum order** input to minEven. The following figure shows the magnitude response of the 28<sup>th</sup> order equi-ripple FIR filter that the DFD Remez Design VI returns.

[IMAGE alt='image' src='min-order-fir-all-bands-con.gif']

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/sampling_frequency.html language=enus -->
## TOPIC 00074: Normalized Sampling Frequency (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/sampling_frequency.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/sampling_frequency.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Normalized Sampling Frequency (Digital Filter Design Toolkit)

The symbol *f*<sub>*s*</sub> denotes the sampling frequency, which is the expected rate at which you sample the input signal of a filter. One-half of the sampling frequency is called the Nyquist frequency. In the LabVIEW Digital Filter Design Toolkit, the default sampling frequency is 1, which is the normalized sampling frequency.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/scale_filter_coef.html language=enus -->
## TOPIC 00075: Scaling the Filter Coefficients (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/scale_filter_coef.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/scale_filter_coef.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Scaling the Filter Coefficients (Digital Filter Design Toolkit)

A filter structure consists of many [accumulators](../lvdfdtconcepts/dfd_structure_graph.html). Each accumulator might use a different data range. However, the LabVIEW Digital Filter Design Toolkit provides only one [sum quantizer](../lvdfdtconcepts/configure_quantizer.html) *Q*<sub>*S>*</sub> for all the accumulators. You can [scale the filter coefficients](/csh?topicname=lvdfdthowto/design_fxp_filter_2.html) before [quantizing](../lvdfdtconcepts/quantize_fl_filters.html) them to ensure that all the accumulators use the same data range. Scaling the filter coefficients can help you obtain a better filtering result, especially for [IIR Cascaded Second-Order Sections Form structures](../lvdfdtconcepts/iir_sos_specs.html). Use the [DFD Scale Filter](/csh?topicname=lvdigfiltdestk/dfd_scale_filter.html) VI to scale the coefficients of a floating-point filter.

Refer to the Scale Filter before Targeting to FXP VI in the labview\examples\Digital Filter Design\Fixed-Point Filters\Single-Rate directory for an example that demonstrates how to scale the filter coefficients.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/select_structure.html language=enus -->
## TOPIC 00076: Selecting a Filter Structure (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/select_structure.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/select_structure.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Selecting a Filter Structure (Digital Filter Design Toolkit)

A filter structure specifies how you arithmetically use a set of filter coefficients to process an input signal. For a specified digital filter, dozens of mathematically equivalent implementation structures are available. For a floating-point digital filter, the effects of different implementation structures on the filter behavior are negligible in most cases. For a fixed-point digital filter, different implementation structures can result in different signal outputs.

In addition to [FIR](../lvdfdtconcepts/fir_filter_specs.html) and [IIR](../lvdfdtconcepts/iir_direct_specs.html) structures, the LabVIEW Digital Filter Design Toolkit also provides lattice structures. Lattice structures, including [lattice allpass](../lvdfdtconcepts/lattice_allpass.html), [lattice AR](../lvdfdtconcepts/lattice_ar_specs.html), [lattice ARMA](../lvdfdtconcepts/lattice_arma_specs.html), and [lattice MA](../lvdfdtconcepts/lattice_ma_specs.html), can be good alternatives for fixed-point filter implementation. For example, lattice structures can preserve the stability of fixed-point IIR filters as long as the [lattice reflection coefficients](../lvdfdtconcepts/lattice_arma_specs.html) have moduli less than one, regardless of how limited the arithmetic precision might be.

The Digital Filter Design Toolkit provides the following three categories of lattice structures.

- Basic Section Type —Two multipliers per lattice section. This category offers the most general lattice structure.
- One Multiplier Section Type —Only one multiplier per lattice section. This category saves resources on hardware targets such as field-programmable gate arrays (FPGAs).
- Normalized Section Type —Four multipliers per lattice section. This category automatically scales the internal signals to help minimize the quantization effects in each lattice section at the cost of increasing the implementation complexity.

When you [select a filter structure](/csh?topicname=lvdfdthowto/design_fxp_filter_1.html), you must balance a number of factors, including the filter type, implementation resources, and computational complexity. For IIR filters, you also need to consider the sensitivity to coefficient quantization of each structure. The following table lists the default filter structures that the [Filter Design](/csh?topicname=lvdigfiltdestk/dfd_design_vis.html) VIs use.

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

|  | Note If you want to generate LabVIEW FPGA code from an IIR filter, National Instruments recommends you use the IIR Cascaded Second-Order Sections Form II Transposed structure for this filter. |
| --- | --- |

You can use the [DFD Convert Structure](/csh?topicname=lvdigfiltdestk/dfd_convert_struc.html) VI to select a different filter structure, with the following caveats:

- You cannot convert an IIR structure into or from an FIR structure.
- You cannot convert a lattice allpass structure into or from a lattice AR structure.
- You can convert an FIR filter to an FIR Symmetric filter structure only if the FIR filter has symmetric coefficients.
- You can convert an FIR filter to an FIR Antisymmetric filter structure only if the FIR filter has antisymmetric coefficients.
- You can convert an FIR filter to a lattice MA (minimum phase) filter structure only if the FIR filter is minimum phase.
- You can convert an FIR filter to a lattice MA (maximum phase) filter structure only if the FIR filter is maximum phase.
- You must use an allpass filter if you want to convert a filter structure to a lattice allpass structure.
- You must use an all-pole IIR filter if you want to convert a filter structure to a lattice AR structure.

Refer to the Change Structure of Filter VI in the labview\examples\Digital Filter Design\Getting Started\Apply Filters directory for an example that demonstrates how to change the structure of a filter.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/set_rounding_mode.html language=enus -->
## TOPIC 00077: Setting the Rounding Mode (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/set_rounding_mode.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/set_rounding_mode.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Setting the Rounding Mode (Digital Filter Design Toolkit)

Fixed-point numbers represent discrete values with limited precision. Typically, the precision of fixed-point numbers is less than that of floating-point numbers. Rounding determines the most appropriate fixed-point number to represent a specified floating-point value based on the precision you specify. Use one of the following modes to specify how you want rounding to occur in a [quantizer](../lvdfdtconcepts/configure_quantizer.html).

- Nearest —The nearest mode rounds to the closest representable number. If the two nearest representable numbers are an equal distance apart, this mode rounds to the nearest representable number whose least significant bit is 0 . The rounding error of this mode is zero-mean, but this mode has higher implementation complexity than the Truncation mode due to the computation of choosing the closest representable number.
- Truncation —The truncation mode rounds to the closest representable number less than the original value. This mode is the most common rounding mode in hardware. However, the rounding error of this mode has a nonzero mean.

Use the **rounding mode** input of the [Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/dfd_fxp_tools_vis.html) VIs to set an appropriate rounding option.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/sim_fp_filters.html language=enus -->
## TOPIC 00078: Simulating Fixed-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/sim_fp_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/sim_fp_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulating Fixed-Point Filters (Digital Filter Design Toolkit)

After you [create a fixed-point filter model](../lvdfdtconcepts/model_fp_filter.html), you must [simulate the filtering process](/csh?topicname=lvdfdthowto/design_fxp_filter_6.html) to verify that the fixed-point model works as expected in a complete implementation. You can use the [DFD FXP Simulation](/csh?topicname=lvdigfiltdestk/dfd_fxp_simulation.html) VI and the [DFD FXP Simulation with State](/csh?topicname=lvdigfiltdestk/dfd_fxp_sim_state.html) VI to facilitate this evaluation. To verify the simulation result, you can use the following two options:

- Compare the simulation results with the filter output results that you obtain by processing the same signal with the reference floating-point filter. Ensure that the simulation results are sufficiently similar to the filtering results of the reference floating-point filter.
- Use the DFD FXP Simulation Report VI to monitor the behavior of the fixed-point filter during the simulation process by observing the filtering text report output. The report contains statistical information about all the quantizers —except the coefficients a / k and coefficients b / v quantizers—in the fixed-point model. Each quantizer has five data entries: max value , min value , #overflows , #underflows , and #operations . Ensure that both #overflows and #underflows equal 0 or fall below an appropriate threshold.

Like all other parts of the design process, simulation is a trial-and-error process. If you observe overflow or underflow in the filtering text report or if the simulation result does not match the actual floating-point filtering result, try making the following adjustments:

- Return to the modeling step. Modify the integer word lengths for the related quantizers to eliminate overflows and underflows until both #overflows and #underflows equal 0 or fall below an appropriate threshold. Use max value and min value to estimate the integer word lengths. [IMAGE alt='image' src='tip.gif']
**Tip** The DFD FXP Modeling VI automatically calculates integer word lengths except that of the input signal, so you might not modify these integer word lengths directly. However, you can use the [DFD FXP Get Quantizer](/csh?topicname=lvdigfiltdestk/dfd_get_quantizer.html) VI to retrieve the integer word lengths for the related quantizers and then use the [DFD FXP Set Quantizer](/csh?topicname=lvdigfiltdestk/dfd_fxp_set_q.html) VI to modify the integer word lengths.
- Change the implementation structure .
- Adjust the specifications and redesign the floating-point filter .

|  | Note In the filtering text report, the #operations entry for the product and sum quantizers provides information about the computational requirements of the fixed-point filter. A smaller value implies a faster computational speed. If several filter structures satisfy the performance requirements of the filter, select the filter structure whose product quantizer has the smallest #operations value. |
| --- | --- |

Refer to the Step 4 - Model and Simulate FXP Lowpass (Lowpass) VI in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter directory for an example that demonstrates how to [create a fixed-point model of a lowpass filter](../lvdfdtconcepts/model_fp_filter.html) and simulate the filtering result.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/single-point_bands.html language=enus -->
## TOPIC 00079: Single-Point Band Design (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/single-point_bands.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/single-point_bands.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Single-Point Band Design (Digital Filter Design Toolkit)

A single-point band is a frequency band that consists of a single point. Single-point bands are useful when designing notch and peak filters. You can specify single-point bands with the [DFD Remez Design](/csh?topicname=lvdigfiltdestk/dfd_remez_design.html) VI by entering only one point in the **band specs** input to describe the frequency response.

For example, suppose you want to design a double-notch filter with notch frequencies at 0.15 Hz and 0.35 Hz. The five bands in this example have the frequency ranges of [0, 0.12], [0.15], [0.18, 0.32], [0.35], and [0.38, 0.5]. All passbands, single-point bands, and stopbands are equally weighted. The following figure shows the magnitude response of the designed 30<sup>th</sup> order filter:

[IMAGE alt='image' src='single-point-band.gif']

You might find other uses for single-point band specifications. For example, by adding a single-point band in a transition band, you can force the frequency response to pass close to a particular point. Alternatively, when you encounter transition band anomalies designing a multiband filter, you might be able to remove the anomalies by adding single-point bands within those transition bands.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/special_filt_design.html language=enus -->
## TOPIC 00080: Designing Special Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/special_filt_design.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/special_filt_design.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing Special Filters (Digital Filter Design Toolkit)

This book contains information about using the LabVIEW Digital Filter Design Toolkit to design special [single-rate](../lvdfdtconcepts/dfdt_concepts_intro.html) filters with the [Advanced FIR Filter Design](/csh?topicname=lvdigfiltdestk/dfd_adv_fir_vis.html) VIs, [Advanced IIR Filter Design](/csh?topicname=lvdigfiltdestk/dfd_adv_iir_vis.html) VIs, and the [Special Filter Design](/csh?topicname=lvdigfiltdestk/dfd_special_vis.html) VIs.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/specify_q_source.html language=enus -->
## TOPIC 00081: Specifying the Quantizer Source (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/specify_q_source.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/specify_q_source.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying the Quantizer Source (Digital Filter Design Toolkit)

A fixed-point filter implementation involves many different [quantizers](../lvdfdtconcepts/configure_quantizer.html), such as the coefficients quantizer, the input quantizer, and the product quantizer. Each quantizer has a different effect on a fixed-point filter response. You must specify the appropriate quantizer source when configuring the quantizers. Use the **source** input of the [Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/dfd_fxp_tools_vis.html) VIs to choose an appropriate quantizer source.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/specify_wl_iwl.html language=enus -->
## TOPIC 00082: Specifying the Word Length and Integer Word Length (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/specify_wl_iwl.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/specify_wl_iwl.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying the Word Length and Integer Word Length (Digital Filter Design Toolkit)

The word length indicates the number of bits you want to use in representing a fixed-point number. The integer word length specifies the number of bits, including the sign bit, you use in representing the integer part of a fixed-point number. The difference in bits between the word length and the integer word length determines the digits of precision.

The finite word length of a [quantizer](../lvdfdtconcepts/configure_quantizer.html) can affect the frequency response of the resulting fixed-point filter. The larger word length value you specify, the less the fixed-point representation distorts the frequency response. However, a larger word length value also requires more hardware resources, so you must specify a word length that provides an acceptable tradeoff between distortion and hardware resource consumption.

Use the **wl** and **iwl** inputs of the [Fixed-Point Tools](/csh?topicname=lvdigfiltdestk/dfd_fxp_tools_vis.html) VIs to specify the word length and integer word length, respectively, of a quantizer.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/structure_coef_q.html language=enus -->
## TOPIC 00083: Filter Structures and Filter Coefficients (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/structure_coef_q.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/structure_coef_q.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Filter Structures and Filter Coefficients (Digital Filter Design Toolkit)

Different [filter structures](../lvdfdtconcepts/select_structure.html) use different groups of filter coefficients. The LabVIEW Digital Filter Design Toolkit categorizes filter coefficients into three groups: zeroes, poles, and gain. For example, [FIR filter coefficients](../lvdfdtconcepts/fir_filter_specs.html), [IIR forward coefficients](../lvdfdtconcepts/iir_direct_specs.html), and [lattice ladder coefficients](../lvdfdtconcepts/lattice_arma_specs.html) correspond to zeroes. [IIR reverse coefficients](../lvdfdtconcepts/iir_direct_specs.html) and [lattice reflection coefficients](../lvdfdtconcepts/lattice_arma_specs.html), excluding lattice MA reflection coefficients, correspond to poles. Different groups of filter coefficients have different data ranges. Therefore, in addition to the gain, the Digital Filter Design Toolkit provides the following two quantizers for these groups: coefficients *a*/*k* and coefficients *b*/*v*.

When you [quantize the filter coefficients](../lvdfdtconcepts/quantize_fl_filters.html), configure the appropriate quantizer according to the filter structure type. The following table lists the filter structures, the filter coefficients, and the corresponding quantizers.

| Filter Structure | Filter Coefficients and the Corresponding Quantizer |
| --- | --- |
| FIR structures | All FIR filter coefficients correspond to the coefficients b/v quantizer. |
| IIR Direct Form structures | The reverse coefficients correspond to the coefficients a/k quantizer. The forward coefficients correspond to the coefficients b/v quantizer. |
| IIR Cascaded Second-Order Sections Form structures |  |
| Lattice Allpass structures | The reflection coefficients correspond to the coefficients a/k quantizer. |
| Lattice AR structures |  |
| Lattice MA structures |  |
| Lattice ARMA structures | The reflection coefficients correspond to the coefficients a/k quantizer. The ladder coefficients correspond to the coefficients b/v quantizer. |

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/use_fl_filters.html language=enus -->
## TOPIC 00084: Using Floating-Point Filters (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/use_fl_filters.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/use_fl_filters.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Floating-Point Filters (Digital Filter Design Toolkit)

After you [analyze the filter design](../lvdfdtconcepts/analyze_design.html), you can use the filter to [process](/csh?topicname=lvdfdthowto/design_fp_filter_3.html) an input signal. Use the [Processing](/csh?topicname=lvdigfiltdestk/dfd_processing_vis.html) VIs to process a signal with the filter you designed. The Processing VIs can process an input signal in the following two ways:

- As a sequence of data blocks
- As a sequence of data blocks with saved internal filter states

Refer to the Step 2 - Perform Lowpass Filtering (Lowpass) VI in the labview\examples\Digital Filter Design\Case Studies\Single-Rate Filter directory for an example that demonstrates how to apply a lowpass filter to a filtering application.

<!--NI_TOPIC bundle=labview-digital-filter-design-toolkit-api-ref path=lvdfdtconcepts/zero_phase_filtering.html language=enus -->
## TOPIC 00085: Zero-Phase Filtering (Digital Filter Design Toolkit)

- bundle_id: `labview-digital-filter-design-toolkit-api-ref`
- source_path: `lvdfdtconcepts/zero_phase_filtering.html`
- source_url: https://docs-be.ni.com/bundle/labview-digital-filter-design-toolkit-api-ref/raw/resource/enus/lvdfdtconcepts/zero_phase_filtering.html
- document_id: `labview-digital-filter-design-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Zero-Phase Filtering (Digital Filter Design Toolkit)

Zero-phase filtering helps you eliminate the group delay in the output signal of a filter. All multirate filters you design with the LabVIEW Digital Filter Design Toolkit, except for possible odd-order [cascaded integrator comb (CIC) filters](../lvdfdtconcepts/cic_filters.html), are even-order, linear phase FIR filters. When you [use linear phase FIR filters to process signals](../lvdfdtconcepts/design_fl_multirate.html#multirate_signal_processing), the filters return signals with a constant group delay, as shown in the following figure:

[IMAGE alt='image' src='filtering-with-delay.gif']

In this figure, you can see that the **Output Signal** plot contains a constant set of zero values, which denotes the delay between the output and input signals. If you want to eliminate the delay, you can implement the filter as a zero-phase filter by setting the **zero phase?** input of the [Multirate Processing](/csh?topicname=lvdigfiltdestk/dfd_m_process_vis.html) VIs to TRUE. The following figure shows an example of an output signal that has no delay compared with the input signal.

[IMAGE alt='image' src='zero-phase-filtering.gif']

Because zero-phase filters must be [noncausal](../lvdfdtconcepts/filter_attributes.html), you cannot achieve zero-phase filtering in real-time signal processing. The [Multirate Processing](/csh?topicname=lvdigfiltdestk/dfd_m_process_vis.html) VIs achieve zero-phase by padding and trimming data. For single-block processing, the VIs pad the input data block at the beginning and end and trim the output data so the delay between the input and output is zero. For continuous processing, the VIs trim the initial transition so the delay between the input and the output is zero.

|  | Note Zero-phase filtering works only with even-order multirate filters. All multirate filters you design using the Digital Filter Design Toolkit, except odd-order CIC filters, are even-order filters. |
| --- | --- |
