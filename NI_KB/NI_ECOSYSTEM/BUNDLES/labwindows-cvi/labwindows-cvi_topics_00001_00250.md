# NI DOCUMENT BUNDLE: labwindows-cvi

<!--NI_BUNDLE_CHUNK bundle=labwindows-cvi start=1 end=250 -->
<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/basic_polynomial_operations.html language=enus -->
## TOPIC 00001: Basic Polynomial Operations

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/basic_polynomial_operations.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/basic_polynomial_operations.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Basic Polynomial Operations

The basic polynomial operations include the following operations:

- Finding the order of a polynomial
- Evaluating a polynomial
- Adding, subtracting, multiplying, or dividing polynomials
- Determining the composition of a polynomial
- Determining the greatest common divisor of two polynomials
- Determining the least common multiple of two polynomials
- Calculating the derivative of a polynomial
- Integrating a polynomial
- Finding the number of real roots of a real polynomial

Parent topic:

Polynomials

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/choosing_smoothing_window.html language=enus -->
## TOPIC 00002: Choosing the Correct Smoothing Window

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/choosing_smoothing_window.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/choosing_smoothing_window.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Choosing the Correct Smoothing Window

Selecting a smoothing window is not a simple task. Each smoothing window has its own characteristics and suitability for
 different applications. To choose a smoothing window, you must estimate the frequency content of the signal. If the signal
 contains strong interfering frequency components distant from the frequency of interest, choose a smoothing window with a
 high side lobe roll-off rate. If the signal contains strong interfering signals near the frequency of interest, choose a smoothing
 window with a low maximum side lobe level.

If the frequency of interest contains two or more signals very near to each other, spectral resolution is important. In this
 case, it is best to choose a smoothing window with a very narrow main lobe. If the amplitude accuracy of a single frequency
 component is more important than the exact location of the component in a given frequency bin, choose a smoothing window with
 a wide main lobe. If the signal spectrum is rather flat or broadband in frequency content, use the rectangular window, or
 no window. In general, the Hanning window is satisfactory in 95% of cases. It has good frequency resolution and reduced spectral
 leakage. If you do not know the nature of the signal but you want to apply a smoothing window, start with the Hanning window.

The following table lists different types of signals and the appropriate windows that you can use with them.

| Type of Signal | Window |
| --- | --- |
| Transients whose duration is shorter than the length of the window | Rectangular |
| Transients whose duration is longer than the length of the window | Exponential, Hanning |
| General-purpose applications | Hanning |
| Spectral analysis (frequency-response measurements) | Hanning (for random excitation), Rectangular (for pseudorandom excitation) |
| Separation of two tones with frequencies very close to each other but with widely differing amplitudes | Kaiser-Bessel |
| Separation of two tones with frequencies very close to each other but with almost equal amplitudes | Rectangular |
| Accurate single-tone amplitude measurements | Flat top |
| Sine wave or combination of sine waves | Hanning |
| Sine wave and amplitude accuracy is important | Flat top |
| Narrowband random signal (vibration data) | Hanning |
| Broadband random (white noise) | Rectangular |
| Closely spaced sine waves | Rectangular, Hamming |
| Excitation signals (hammer blow) | Force |
| Response signals | Exponential |
| Unknown content | Hanning |

Initially, you might not have enough information about the signal to select the most appropriate smoothing window for the
 signal. You might need to experiment with different smoothing windows to find the best one. Always compare the performance
 of different smoothing windows to find the best one for the application.

Parent topic:

Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/common_testsignals.html language=enus -->
## TOPIC 00003: Common Test Signals

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/common_testsignals.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/common_testsignals.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Common Test Signals

Common test signals include the sine wave, the square wave, the triangle wave, the sawtooth wave, several types of noise
 waveforms, and multitone signals consisting of a superposition of sine waves.

The most common signal for audio testing is the sine wave. A single sine wave is often used to determine the amount of
 harmonic distortion introduced by a system. Multiple sine waves are widely used to measure the intermodulation distortion
 or to determine the frequency response. The following table lists the signals used for some typical measurements.

| Measurement | Signal |
| --- | --- |
| Total harmonic distortion | Sine wave |
| Intermodulation distortion | Multitone (two sine waves) |
| Frequency response | Multitone (many sine waves, impulse, chirp), broadband noise |
| Interpolation | Sinc |
| Rise time, fall time, overshoot, undershoot | Pulse |
| Jitter | Square wave |

These signals form the basis for many tests and are used to measure the response of a system to a particular stimulus. Some
 of the common test signals available in most signal generators are shown in the following figures.

[IMAGE alt='loc_eps_commontestsignals_all.gif' src='guid-387a92e7-9aca-40a1-9ca2-05eb05a93f18-help-web.png']

The most useful way to view the common test signals is in terms of their frequency content. The common test signals have the
 following frequency content characteristics:

- Sine waves have a single frequency component.
- Square waves consist of the superposition of many sine waves at odd harmonics of the fundamental frequency. The amplitude
 of each harmonic is inversely proportional to its frequency.
- Triangle and sawtooth waves have harmonic components that are multiples of the fundamental frequency.
- An impulse contains all frequencies that can be represented for a given sampling rate and number of samples.
- Chirp signals are sinusoids swept from a start frequency to a stop frequency, thus generating energy across a given frequency
 range. Chirp patterns have discrete frequencies that lie within a certain range. The discrete frequencies of chirp patterns
 depend on the sampling rate, the start and end frequencies, and the number of samples.

Parent topic:

Signal Generation

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/cross_power_spect.html language=enus -->
## TOPIC 00004: Cross Power Spectrum

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/cross_power_spect.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/cross_power_spect.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Cross Power Spectrum

The cross power spectrum is not typically used as a direct measurement but is an important building block for other measurements.

Use the following equation to compute the two-sided cross power spectrum of two time-domain signals *A* and *B*.

[IMAGE alt='image' src='./kset2ftemp2fcross_power_spect.xml_d1395e29.png']

The cross power spectrum is a two-sided complex form, having real and imaginary parts. You can convert the cross power spectrum
 to magnitude and phase in the same way you compute the amplitude and phase spectrums of a power spectrum.

You also can convert the cross power spectrum to a single-sided form. The single-sided cross power spectrum yields the product
 of the rms amplitudes and the phase difference between the two signals *A* and *B*. The units of the single-sided cross power spectrum are in quantity rms squared, for example, V<sub>rms</sub><sup>2</sup>.

The power spectrum is equivalent to the cross power spectrum when signals *A* and *B* are the same signal. Therefore, the power spectrum is often referred to as the auto power spectrum or the auto spectrum.

Parent topic:

Frequency Analysis

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/digital_filtering.html language=enus -->
## TOPIC 00005: Digital Filtering

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/digital_filtering.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/digital_filtering.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Digital Filtering

Use digital filtering to remove unwanted parts of a digital signal such as noise.

Parent topic:

Advanced Analysis Concepts

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/display_transforms_freq_info.html language=enus -->
## TOPIC 00006: Displaying Frequency Information from Transforms

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/display_transforms_freq_info.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/display_transforms_freq_info.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Displaying Frequency Information from Transforms

The discrete implementation of the Fourier transform maps a digital signal into its Fourier series coefficients, or harmonics.
 Unfortunately, neither a time nor a frequency stamp is directly associated with the FFT operation. Therefore, you must specify
 the sampling interval Δ*t*.

Because an acquired array of samples represents a progression of equally spaced samples in time, you can determine the corresponding
 frequency in hertz. The following equation gives the sampling frequency *f*<sub>*s*</sub> for Δ*t*.

*f*<sub>*s*</sub> = 1/Δ*t*

The following figure shows the frequency information from an FFT transform with the sampling interval 1.000E-3.

[IMAGE alt='image' src='guid-8a43149a-4fe3-42d7-90ec-23df9b9bd6a4-help-web.png']

Two other common ways of presenting frequency information are displaying the DC component in the center and displaying one-sided
 spectrums.

Parent topic:

FFT Fundamentals

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/echo_detection.html language=enus -->
## TOPIC 00007: Echo Detection and Hilbert Transform

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/echo_detection.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/echo_detection.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Echo Detection and Hilbert Transform

Echo detection using Hilbert transforms is a common measurement for the analysis of modulation systems.

The following equation describes a time-domain signal.

[IMAGE alt='image' src='./workset2ftemp2fecho_detection.xml_d1822e26.png']

where *A* is the amplitude, *f*<sub>0</sub> is the natural resonant frequency, and *T* is the time decay constant.

The following equation yields the Hilbert transform of the time-domain signal.

[IMAGE alt='image' src='./workset2ftemp2fecho_detection.xml_d1822e101.png']

The following equation yields the natural logarithm of the magnitude of the analytic signal *x*<sub>*A*</sub>(*t*).

[IMAGE alt='image' src='./workset2ftemp2fecho_detection.xml_d1822e180.png']

The result from the previous equation has the form of a line with slope *m* = -1/τ. Therefore, you can extract the time constant of the system by graphing ln|*x*<sub>*A*</sub>(*t*)|.

The following figure shows a time-domain signal containing an echo signal.

[IMAGE alt='image' src='guid-5c2b54d9-d8fb-4355-a1fa-db77614ddbfd-help-web.png']

The following conditions make the echo signal difficult to locate in the previous figure:

- The time delay between the source and the echo signal is short relative to the time decay constant of the system.
- The echo amplitude is small compared to the source.

You can make the echo signal visible by plotting the magnitude of *x*<sub>*A*</sub>(*t*) on a logarithmic scale, as shown on the following figure.

[IMAGE alt='image' src='guid-5a4517c2-3898-4012-8802-a0f54afa71fc-help-web.png']

In the previous figure, the discontinuity is plainly visible and indicates the location of the time delay of the echo.

Parent topic:

Hilbert Transform

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/evaluate_poly_with_matrix.html language=enus -->
## TOPIC 00008: Evaluating a Polynomial with a Matrix

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/evaluate_poly_with_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/evaluate_poly_with_matrix.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Evaluating a Polynomial with a Matrix

The matrix evaluation of a polynomial differs from 2D polynomial evaluation.

When performing matrix evaluation of a polynomial, you must use a square matrix. The following equations define a second-order
 polynomial *P*(*x*) and a square 2 × 2 matrix *G*.

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e32.png']

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e77.png']

In 2D polynomial evaluation, you evaluate *P*(*x*) at each element of matrix *G*, as shown by the following equation.

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e143.png']

When performing matrix polynomial evaluation, you replace the variable *x* with matrix *G*, as shown by the following equation.

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e281.png']

where *I* is the identity matrix of the same size as *G*.

In the following equations, actual values replace the variables *a* and *g* in the previous equations that define a second-order polynomial *P*(*x*) and a square 2 × 2 matrix *G*.

P(*x*) = 5 + 3*x* +2*x*

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e375.png']

The following equation shows the matrix evaluation of the polynomial *P*(*x*) from the first equation above with matrix *G* from the second equation above.

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e418.png']

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e531.png']

[IMAGE alt='image' src='./p2fevaluate_poly_with_matrix.xml_d1933e609.png']

Parent topic:

Polynomials

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/freq_time_domain_diffs.html language=enus -->
## TOPIC 00009: Differences between Frequency Domain and Time Domain

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/freq_time_domain_diffs.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/freq_time_domain_diffs.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Differences between Frequency Domain and Time Domain

The time-domain representation gives the amplitudes of the signal at the instants of time during which it was sampled.
 However, in many cases you need to know the frequency content of a signal rather than the amplitudes of the individual samples.

Fourier's theorem states that any waveform in the time domain can be represented by the weighted sum of sines and cosines.
 The same waveform then can be represented in the frequency domain as a pair of amplitude and phase values at each component
 frequency.

You can generate any waveform by adding sine waves, each with a particular amplitude and phase. The following figure shows
 the original waveform, labeled 
 sum, and its component frequencies. The fundamental frequency is shown at the frequency *f*<sub>0</sub>, the second harmonic at frequency 2*f*<sub>0</sub>, and the third harmonic at frequency 3*f*<sub>0</sub>.

[IMAGE alt='image' src='guid-778eda50-3640-4888-9c76-4f4cac177229-help-web.png']

In the frequency domain, you can separate conceptually the sine waves that add to form the complex time-domain signal. The
 previous figure shows single frequency components, which spread out in the time domain, as distinct impulses in the frequency
 domain. The amplitude of each frequency line is the amplitude of the time waveform for that frequency component. The representation
 of a signal in terms of its individual frequency components is the frequency-domain representation of the signal. The frequency-domain
 representation might provide more insight about the signal and the system from which it was generated.

The samples of a signal obtained from a DAQ device constitute the time-domain representation of the signal. Some measurements,
 such as harmonic distortion, are difficult to quantify by inspecting the time waveform on an oscilloscope. When the same signal
 is displayed in the frequency domain by an FFT Analyzer, also known as a Dynamic Signal Analyzer, you easily can measure the
 harmonic frequencies and amplitudes.

Parent topic:

Frequency Analysis Basics

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/frequency_response_function.html language=enus -->
## TOPIC 00010: Frequency Response

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/frequency_response_function.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/frequency_response_function.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Frequency Response

When analyzing two simultaneously sampled channels, you usually want to know the differences between the two channels rather
 than the properties of each.

In a typical dual-channel analyzer, as shown in the following figure, the instantaneous spectrum is computed using a window
 function and the fast Fourier transform (FFT) for each channel. The averaged FFT spectrum, auto power spectrum, and cross
 power spectrum are computed and used in estimating the frequency response function. You also can use the coherence function
 to check the validity of the frequency response function.

[IMAGE alt='image' src='guid-6596653c-7d2d-4629-8835-ae1302155823-help-web.png']

The frequency response of a system is described by the magnitude, |H|, and phase, ∠H, at each frequency. The gain of the system
 is the same as its magnitude and is the ratio of the output magnitude to the input magnitude at each frequency. The phase
 of the system is the difference of the output phase and input phase at each frequency.

Parent topic:

Frequency Analysis

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/general_ls_linear_fit_theory.html language=enus -->
## TOPIC 00011: General LS Linear Fit Theory

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/general_ls_linear_fit_theory.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/general_ls_linear_fit_theory.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### General LS Linear Fit Theory

For a given set of observation data, the general least-squares (LS) linear fit problem is to find a set of coefficients
 that fits the linear model, as shown in the following equation:

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e20.png']

where

*x*<sub>*i**j*</sub> is the observed data contained in the observation matrix *H*,

*n* is the number of elements in the set of observed data and the number of rows of in *H*,

*b* is the set of coefficients that fit the linear model,

*k* is the number of coefficients.

The following equation defines the observation matrix *H*:

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e192.png']

You can rewrite the general LS linear fit model as the following equation:

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e337.png']

The general LS linear fit model is a multiple linear regression model. A multiple linear regression model uses several variables,
 *x*<sub>*i*0</sub>, *x*<sub>*i*1</sub>, …, *x*<sub>*i**k* - 1</sub>, to predict one variable, *y*<sub>*i*</sub>.

In most analysis situations, you acquire more observation data than coefficients. The general LS linear fit model might not
 yield all the coefficients in set *B*. The fit problem becomes to find the coefficient set *B* that minimizes the difference between the observed data *y*<sub>*i*</sub> and the predicted value *z*<sub>*i*</sub>. The following equation defines *z*<sub>*i*</sub>.

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e412.png']

You can use the least chi-square plane method to find the solution set *B* that minimizes the quantity given by the following equation.

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e468.png']

where *h*<sub>*o**i**j*</sub> = (*x*<sub>*i**j*</sub>/σ<sub>*i*</sub>), *y*<sub>*o**i*</sub> = (*y*<sub>*i*</sub>/σ<sub>*i*</sub>)

for *i* = 0, 1, …, *n* - 1, and *j* = 0, 1, …, *k* - 1.

In the previous equation, σ<sub>*i*</sub> is the standard deviation. If the measurement errors are independent and normally distributed with constant standard deviation,
 σ<sub>*i*</sub> = σ, the previous equation also is the least-square estimation.

You can minimize χ<sup>2</sup> from the previous equation in the following ways:

- Solve normal equations of the least-square problems using LU or Cholesky factorization.
- Minimize χ 2 to find the least-square solution of equations.

To solve normal equations, you first set the partial derivatives of χ<sup>2</sup> to zero with respect to *b*<sub>0</sub>, *b*<sub>1</sub>, …, *b*<sub>*k*-1</sub>, as shown by the following equations:

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e763.png']

You then derive the equations in the previous equation to the following equation form:

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e875.png']

where *H*<sub>0</sub><sup>T</sup> is the transpose of *H* 
 <sub>0</sub>.

Equations of the form given by the previous equation are called normal equations of the least-square problems. You can solve
 them using LU or Cholesky factorization algorithms. However, the solution from the normal equations is susceptible to round-off
 error.

The preferred method of minimizing χ<sup>2</sup> is to find the least-square solution of equations. The following equation defines the form of the least-square solution of
 equations.

[IMAGE alt='image' src='./eneral_ls_linear_fit_theory.xml_d3420e938.png']

You can use QR or SVD factorization to find the solution set B for the previous equation. For QR factorization, you can use
 the Householder algorithm, the Givens algorithm, or the Givens 2 algorithm, which also is known as the fast Givens algorithm.
 Different algorithms can give you different precision. In some cases, if one algorithm cannot solve the equation, another
 algorithm might solve it. You can try different algorithms to find the one best suited for the observation data.

Parent topic:

Curve Fitting

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/harmonic_distortion.html language=enus -->
## TOPIC 00012: Harmonic Distortion

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/harmonic_distortion.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/harmonic_distortion.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Harmonic Distortion

When a signal *x*(*t*) of a particular frequency *f*<sub>1</sub> passes through a nonlinear system, the output of the system consists of *f*<sub>1</sub> and its harmonics. The following expression describes the relationship between *f*<sub>1</sub> and its harmonics.

*f*<sub>1</sub>, *f*<sub>2</sub> = 2*f*<sub>1</sub>, *f*<sub>3</sub> = 3*f*<sub>1</sub>, *f*<sub>4</sub> = 4*f*<sub>1</sub>, …, *f*<sub>*n*</sub> = *n**f*<sub>1</sub>

The degree of nonlinearity of the system determines the number of harmonics and their corresponding amplitudes the system
 generates. In general, as the nonlinearity of a system increases, the harmonics become higher. As the nonlinearity of a system
 decreases, the harmonics become lower.

The following figure shows an example of a nonlinear system where the output *y*(*t*) is the cube of the input signal *x*(*t*).

[IMAGE alt='image' src='guid-06e854e8-3eb8-416e-afcc-927b6a18c583-help-web.png']

The following equation defines the input for the system shown in the previous figure.

*x*(*t*) = cos(ω*t*)

The following equation defines the output of the system shown in the previous figure.

*x*<sup>3</sup>(*t*) = 0.5cos(ω*t*) + 0.25[cos(ω*t*) + cos(3ω*t*)]

In the previous equation, the output contains not only the input fundamental frequency ω but also the third harmonic 3ω.

A common cause of harmonic distortion is clipping. Clipping occurs when a system is driven beyond its capabilities. Symmetrical
 clipping results in odd harmonics. Asymmetrical clipping creates both even and odd harmonics.

Parent topic:

Distortion Measurements

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/hilbert_transform_analytic.html language=enus -->
## TOPIC 00013: Hilbert Transform on an Analytic Signal

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/hilbert_transform_analytic.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/hilbert_transform_analytic.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Hilbert Transform on an Analytic Signal

You can extract instantaneous phase information and the envelope of an input signal using Hilbert transforms.

For example, the cosine signal of the input signal *x*(*t*) is the following equation:

[IMAGE alt='image' src='./2fhilbert_transform_analytic.xml_d6692e37.png']

To find the analytic signal of *x*(*t*), calculate the Hilbert transform of *x*(*t*) using the following equation:

[IMAGE alt='image' src='./2fhilbert_transform_analytic.xml_d6692e102.png']

The analytic signal of *x*(*t*) is defined using the equation

[IMAGE alt='image' src='./2fhilbert_transform_analytic.xml_d6692e162.png']

where the amplitude of *f*(*t*), which is *A*(*t*), is the envelope of *x*(*t*) and where the phase of *f*(*t*), which is ω<sub>0</sub>*t* + φ(*t*), is the instantaneous phase of *x*(*t*).

You can obtain the single-sideband spectra using the Fourier transform on the analytic signal *f*(*t*), as shown in the following equation:

[IMAGE alt='image' src='./2fhilbert_transform_analytic.xml_d6692e291.png']

Parent topic:

Hilbert Transform

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/hilbert_transform_oscillating.html language=enus -->
## TOPIC 00014: Hilbert Transform on an Oscillating Signal

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/hilbert_transform_oscillating.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/hilbert_transform_oscillating.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Hilbert Transform on an Oscillating Signal

You can use the Hilbert transform to isolate the slowly varying envelope from an oscillating signal.

For the signal of the equation

[IMAGE alt='image' src='./lbert_transform_oscillating.xml_d6772e31.png']

the rapidly oscillating component is sin(*w**t*) and the envelope is the exponential *A**exp(-*b**t*).

The Hilbert transform of *f*(*t*) phase shifts the oscillatory component by 90 degrees in the following equation:

[IMAGE alt='image' src='./lbert_transform_oscillating.xml_d6772e103.png']

If the values of *f*(*t*) and *h*(*t*) are in arrays, calculate the envelope function with |*f*(*t*) + *i**h*(*t*)|.

Parent topic:

Hilbert Transform

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/introduction_to_curve_fitting.html language=enus -->
## TOPIC 00015: Least Squares Method

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/introduction_to_curve_fitting.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/introduction_to_curve_fitting.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Least Squares Method

The least squares method of curve fitting fits a curve to a particular data set. The following equation defines the least
 square error.

[IMAGE alt='image' src='./troduction_to_curve_fitting.xml_d3980e23.png']

| where | e(a) is the least square error |
| --- | --- |
|  | y(x) is the observed data set |
|  | f(x, a) is the functional description of the data set |
|  | a is the set of curve coefficients that best describes the curve |

For example, if *a* = {*a*<sub>0</sub>, *a*<sub>1</sub>}, the following equation yields the functional description:

[IMAGE alt='image' src='./troduction_to_curve_fitting.xml_d3980e137.png']

The least squares algorithm finds *a* by solving the system defined by the following equation.

[IMAGE alt='image' src='./troduction_to_curve_fitting.xml_d3980e184.png']

To solve the system defined by the previous equation, you set up and solve the Jacobian system generated by expanding the
 previous equation. After you solve the system for *a*, you can use the functional description *f*(*x*, *a*) to obtain an estimate of the observed data set for any value of *x*.

Parent topic:

Curve Fitting

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/introduction_to_filtering.html language=enus -->
## TOPIC 00016: Introduction to Filtering

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/introduction_to_filtering.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/introduction_to_filtering.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Introduction to Filtering

The filtering process alters the frequency content of a signal. For example, the bass control on a stereo system alters
 the low-frequency content of a signal, while the treble control alters the high-frequency content. Changing the bass and treble
 controls filters the audio signal. Two common filtering applications are removing noise and decimation. Decimation consists
 of lowpass filtering and reducing the sample rate.

The filtering process assumes that you can separate the signal content of interest from the raw signal. Classical linear filtering
 assumes that the signal content of interest is distinct from the remainder of the signal in the frequency domain.

Parent topic:

Digital Filtering

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/introduction_to_optimization.html language=enus -->
## TOPIC 00017: Introduction to Optimization

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/introduction_to_optimization.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/introduction_to_optimization.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Introduction to Optimization

The optimization process either minimizes or maximizes the objective function *f*(*x*) until reaching the optimal value for *f*(*x*). When minimizing *f*(*x*), the optimal solution *x** ∈ *X* satisfies the following condition.

[IMAGE alt='image' src='./ntroduction_to_optimization.xml_d4146e50.png']

The optimization process searches for the value of *x** that minimizes *f*(*x*), subject to the constraint *x** ∈ *X*, where *X* is the constraint set. A value that satisfies the conditions defined in the previous equation is a global minimum.

In the case of maximization, *x** satisfies the following condition.

[IMAGE alt='image' src='./ntroduction_to_optimization.xml_d4146e126.png']

A value satisfying the preceding condition is a global maximum.

Parent topic:

Optimization

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/limit_testing_overview.html language=enus -->
## TOPIC 00018: Limit Testing

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/limit_testing_overview.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/limit_testing_overview.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Limit Testing

You can use limit testing to monitor a waveform and determine if it always satisfies a set of conditions, usually upper
 and lower limits. The region bounded by the specified limits is a mask. The result of a limit or mask test is generally a
 pass or fail. Limits are classified into two types—continuous limits and segmented limits.

You can use the same method to create and control many different automated test systems. Complete the following basic steps
 to set up an automated test system for limit testing.

1. Configure the measurement by specifying arbitrary upper and lower limits. This defines the mask or region of interest.
2. Acquire data using a DAQ device.
3. Monitor the data to make sure it always falls within the specified mask.
4. Log the pass/fail results from step 3 to a file or visually inspect the input data and the points that fall outside the mask.
5. Repeat steps 2 through 4 to continue limit testing.

Parent topic:

Advanced Analysis Concepts

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_dolph_chebyshev_window.html language=enus -->
## TOPIC 00019: Dolph-Chebyshev

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_dolph_chebyshev_window.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_dolph_chebyshev_window.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Dolph-Chebyshev

The following equation defines the Dolph-Chebyshev window.

[IMAGE alt='image' src='./lvac_dolph_chebyshev_window.xml_d11918e20.png']

for *n* = 0, 1, 2, …, *N* - 1

| where | N is the length of the window |
| --- | --- |
|  | s is the height ratio of the main lobe to the side lobe in dB |
|  | is the mth order Chebyshev polynomial |
|  | . |

The following figure shows the Dolph-Chebyshev window for *N* = 32 and lobe ratio 60.

[IMAGE alt='image' src='guid-934a5fd7-e2a4-4406-9484-53b2721906cd-help-web.png']

The *s* parameter adjusts the side lobe level of the Dolph-Chebyshev window. The lower the side lobe level, the wider the main lobe.
 The following figure shows the fast Fourier transforms of Dolph-Chebyshev windows with *s* = 80, 100 and 120 dB, respectively.

[IMAGE alt='image' src='guid-0fa22f2d-9901-49fb-bf62-c1b2798194c8-help-web.png']

All side lobe levels of the symmetric Dolph-Chebyshev window have the same height, as shown in the following figure.

[IMAGE alt='image' src='guid-39066065-bff1-41b1-bf0e-f98ea911c9d4-help-web.png']

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_dot_out_products.html language=enus -->
## TOPIC 00020: Dot Product and Outer Product

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_dot_out_products.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_dot_out_products.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Dot Product and Outer Product

If *X* represents a vector and *Y* represents another vector, the dot product of these two vectors is obtained by multiplying the corresponding elements of
 each vector and adding the results. This is denoted by

[IMAGE alt='image' src='./2ftemp2flvac_dot_out_products.xml_d12042e31.png']

where *n* is the number of elements in *X* and *Y*. Both vectors must have the same number of elements. The dot product is a scalar quantity and has many practical applications.

For example, consider the vectors *a* = 2*i* + 4*j* and *b* = 2*i* + *j* in a two-dimensional rectangular coordinate system, as shown in the following figure.

[IMAGE alt='image' src='guid-6e670de6-a01d-4266-ad4b-e11eb6b7548c-help-web.png']

Then the dot product of these two vectors is given by

[IMAGE alt='image' src='./2ftemp2flvac_dot_out_products.xml_d12042e118.png']

The angle α between these two vectors is given by

[IMAGE alt='image' src='./2ftemp2flvac_dot_out_products.xml_d12042e190.png']

where |*a*| denotes the magnitude of *a*.

As a second application, consider a body on which a constant force *a* acts, as shown in the following figure. The work *W* done by *a* in displacing the body is defined as the product of |*d*| and the component of *a* in the direction of displacement *d*. That is,

[IMAGE alt='image' src='./2ftemp2flvac_dot_out_products.xml_d12042e310.png']

[IMAGE alt='image' src='guid-9dc42150-a7c7-45af-ba11-59668ee94349-help-web.png']

On the other hand, the outer product of these two vectors is a matrix. The (*i*, *j*)th element of this matrix is obtained using the formula

[IMAGE alt='image' src='./2ftemp2flvac_dot_out_products.xml_d12042e357.png']

For example,

[IMAGE alt='image' src='./2ftemp2flvac_dot_out_products.xml_d12042e400.png']

Parent topic:

Basic Matrix Operations

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_downhill_simplex.html language=enus -->
## TOPIC 00021: Downhill Simplex Method

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_downhill_simplex.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_downhill_simplex.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Downhill Simplex Method

The downhill simplex method developed by Nelder and Mead uses a simplex and performs function evaluations without derivatives.

|  | Note Although the downhill simplex method and the linear programming simplex method use the concept of a simplex, the methods have nothing else in common. |
| --- | --- |

Most practical applications involve solution sets that are non-degenerate simplexes. A non-degenerate simplex encloses a finite
 volume of *N* dimensions. If you take any point of the non-degenerate simplex as the origin of the simplex, the remaining *N* points of the simplex define vector directions spanning the *N*-dimensional space.

The downhill simplex method requires that you define an initial simplex by specifying *N* + 1 starting points. No effective means of determining the initial starting point exists. You must judge the best location
 from which to start. After deciding upon an initial starting point *P*<sub>0</sub>, you can use the following equation to determine the other points needed to define the initial simplex.

[IMAGE alt='image' src='./2ftemp2flvac_downhill_simplex.xml_d12148e51.png']

where *e*<sub>*i*</sub> is a unit vector and λ is an estimate of the characteristic length scale of the problem.

Starting with the initial simplex defined by the points from the previous equation, the downhill simplex method performs a
 series of reflections. A reflection moves from a point on the simplex through the opposite face of the simplex to a point
 where the function *f* is smaller. The configuration of the reflections conserves the volume of the simplex, which maintains the non-degeneracy
 of the simplex. The method continues to perform reflections until the function value reaches a predetermined tolerance.

Because of the multidimensional nature of the downhill simplex method, the value it finds for *f*(*x*) might not be the optimal solution. You can verify that the value for *f*(*x*) is the optimal solution by repeating the process. When you repeat the process, use the optimal solution from when you first
 ran the method as *P*<sub>0</sub>. Reinitialize the method to *N* + 1 starting points using the previous equation.

Parent topic:

Nonlinear Programming

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_eigen_values_vectors.html language=enus -->
## TOPIC 00022: Eigenvalues and Eigenvectors

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_eigen_values_vectors.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_eigen_values_vectors.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Eigenvalues and Eigenvectors

To understand eigenvalues and eigenvectors, start with the classical definition. Given an *n* × *n* matrix *A*, the problem is to find a scalar λ and a nonzero vector *x* such that

[IMAGE alt='image' src='./p2flvac_eigen_values_vectors.xml_d12218e43.png']

In the previous equation, λ is a vector of eigenvalues. Similar matrices have the same eigenvalues. In the previous equation,
 *x* is the eigenvector that corresponds to the eigenvalues. An eigenvector of a matrix is a nonzero vector that does not rotate
 when the matrix is applied to it.

Calculating the eigenvalues and eigenvectors are fundamental principles of linear algebra and allow you to solve many problems
 such as systems of differential equations when you understand what they represent. Consider an eigenvector *x* of a matrix *A* as a nonzero vector that does not rotate when *x* is multiplied by *A*, except perhaps to point in precisely the opposite direction. *x* may change length or reverse its direction, but it will not turn sideways. In other words, there is some scalar constant
 λ such that the previous equation holds true. The value λ is an eigenvalue of *A*.

Consider the following example. One of the eigenvectors of the matrix *A*, where

[IMAGE alt='image' src='./p2flvac_eigen_values_vectors.xml_d12218e93.png']

is

[IMAGE alt='image' src='./p2flvac_eigen_values_vectors.xml_d12218e125.png']

Multiplying the matrix *A* and the vector *x* simply causes the vector *x* to be expanded by a factor of 6.85. Hence, the value 6.85 is one of the eigenvalues of the vector *x*. For any constant α, the vector α*x* also is an eigenvector with eigenvalue λ because

[IMAGE alt='image' src='./p2flvac_eigen_values_vectors.xml_d12218e166.png']

In other words, an eigenvector of a matrix determines a direction in which the matrix expands or shrinks any vector lying
 in that direction by a scalar multiple, and the expansion or contraction factor is given by the corresponding eigenvalue.
 A generalized eigenvalue problem is to find a vector λ and a nonzero vector *x* such that

[IMAGE alt='image' src='./p2flvac_eigen_values_vectors.xml_d12218e205.png']

where *B* is another *n* × *n* matrix.

The following are some important properties of eigenvalues and eigenvectors:

- The eigenvalues of a matrix are not necessarily all distinct. In other words, a matrix can have multiple eigenvalues.
- All the eigenvalues of a real matrix need not be real. However, complex eigenvalues of a real matrix must occur in complex
 conjugate pairs.
- The eigenvalues of a diagonal matrix are its diagonal entries, and the eigenvectors are the corresponding columns of an identity
 matrix of the same dimension.
- A real symmetric matrix always has real eigenvalues and eigenvectors.
- Eigenvectors can be scaled arbitrarily.

There are many practical applications in the field of science and engineering for an eigenvalue problem. For example, the
 stability of a structure and its natural modes and frequencies of vibration are determined by the eigenvalues and eigenvectors
 of an appropriate matrix. Eigenvalues also are very useful in analyzing numerical methods, such as convergence analysis of
 iterative methods for solving systems of algebraic equations and the stability analysis of methods for solving systems of
 differential equations.

Depending on the particular application, you might just want to compute the eigenvalues or both the eigenvalues and the eigenvectors.
 Also, a symmetric matrix needs less computation than a nonsymmetrical matrix. Choose the matrix type carefully.

Parent topic:

Linear Algebra

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_elliptic_filters.html language=enus -->
## TOPIC 00023: Elliptic Filters

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_elliptic_filters.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_elliptic_filters.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Elliptic Filters

Elliptic filters have the following characteristics:

- Minimization of peak error in the passband and the stopband
- Equiripples in the passband and the stopband

Compared with the same order Butterworth or Chebyshev filters, the elliptic filters provide the sharpest transition between
 the passband and the stopband, which accounts for their widespread use.

The following figure shows the frequency response of a lowpass elliptic filter.

[IMAGE alt='image' src='guid-775175a1-54da-4158-905f-060ab05e8da0-help-web.png']

In the previous figure, the same maximum tolerable error constrains the ripple in both the passband and the stopband. Also,
 even low-order elliptic filters have a sharp transition edge.

Parent topic:

IIR Filter Types

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_estimating_power_and_frequency.html language=enus -->
## TOPIC 00024: Estimating Power and Frequency

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_estimating_power_and_frequency.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_estimating_power_and_frequency.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Estimating Power and Frequency

If a frequency component is between two frequency lines, the frequency component appears as energy spread among adjacent
 frequency lines with reduced amplitude. The actual peak is between the two frequency lines. You can estimate the actual frequency
 of a discrete frequency component to a greater resolution than the ∆*f* given by the fast Fourier transform (FFT) by performing a weighted average of the frequencies around a detected peak in the
 power spectrum, as shown in the following equation.

[IMAGE alt='image' src='./imating_power_and_frequency.xml_d7606e23.png']

where *j* is the array index of the apparent peak of the frequency of interest.

The span *j* ± 3 is reasonable because it represents a spread wider than the main lobes of Rectangular, Hanning, Hamming, Blackman-Harris,
 Exact Blackman, Blackman, and Flat Top smoothing windows.

You can estimate the power in V<sub>rms</sub><sup>2</sup> of a discrete peak frequency component by summing the power in the bins around the peak. In other words, you compute the
 area under the peak. You can use the following equation to estimate the power of a discrete peak frequency component.

[IMAGE alt='image' src='./imating_power_and_frequency.xml_d7606e132.png']

The previous equation is valid only for a spectrum made up of discrete frequency components. It is not valid for a continuous
 spectrum. Also, if two or more frequency peaks are within six lines of each other, they contribute to inflating the estimated
 powers and skewing the actual frequencies. You can reduce this effect by decreasing the number of lines spanned by the previous
 equation. If two peaks are within six lines of each other, it is likely that they are already interfering with one another
 because of spectral leakage.

If you want the total power in a given frequency range, sum the power in each bin included in the frequency range and divide
 by the noise power bandwidth of the smoothing window.

Parent topic:

Computations on the Spectrum

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_exact_blackman.html language=enus -->
## TOPIC 00025: Exact Blackman

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_exact_blackman.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_exact_blackman.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Exact Blackman

The following equation defines the Exact Blackman window.

[IMAGE alt='image' src='./et2ftemp2flvac_exact_blackman.xml_d12402e20.png']

for *n* = 0, 1, 2, …, *N* - 1 and ω = 2π*n*/*N*

| where | N is the length of the window |
| --- | --- |
|  | a0 = 7938/18608 |
|  | a1 = 9240/18608 |
|  | a2 = 1430/18608. |

The following figure shows the Exact Blackman window for *N* = 32.

[IMAGE alt='image' src='guid-f24bc1f2-cf4b-48a8-bbf7-070f2196cbd0-help-web.png']

The Exact Blackman window is useful for single tone measurement. The Exact Blackman window has a lower main lobe width and
 a lower maximum side lobe level than the Blackman window. However, the Blackman window has a higher side lobe roll-off rate
 than the Exact Blackman window.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_example_of_calculating_dft.html language=enus -->
## TOPIC 00026: Example of Calculating Discrete Fourier Transform

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_example_of_calculating_dft.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_example_of_calculating_dft.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Example of Calculating Discrete Fourier Transform

[IMAGE alt='image' src='./_example_of_calculating_dft.xml_d7670e19.png']

This example uses the following assumptions:

- X [0] corresponds to the DC component, or the average value, of the signal.
- The DC signal has a constant amplitude of +1 V.
- The number of samples is four samples.
- Each of the samples has a value +1, as shown in the following figure. 
 
 [IMAGE alt='image' src='guid-3d671729-cd50-4fe8-9085-9bb64fba3f9f-help-web.png']
- The resulting time sequence for the four samples is given by the following equation. 
 
 *x*[0] = *x*[1] = *x*[2] = *x*[3] = 1

The DFT calculation makes use of Euler's identity, which is given by the following equation.

[IMAGE alt='image' src='./_example_of_calculating_dft.xml_d7670e178.png']

If you use the following equation to calculate the DFT of the sequence shown in the previous figure and use Euler's identity,

[IMAGE alt='image' src='./_example_of_calculating_dft.xml_d7670e229.png']

you get the following equations.

[IMAGE alt='image' src='./_example_of_calculating_dft.xml_d7670e342.png']

[IMAGE alt='image' src='./_example_of_calculating_dft.xml_d7670e455.png']

[IMAGE alt='image' src='./_example_of_calculating_dft.xml_d7670e656.png']

[IMAGE alt='image' src='./_example_of_calculating_dft.xml_d7670e841.png']

where *X*[0] is the DC component and *N* is the number of samples.

Therefore, except for the DC component, all other values for the sequence are zero, which is as expected. However, the calculated
 value of *X*[0] depends on the value of *N*. Because in this example *N* = 4, *X*[0] = 4. If *N* = 10, the calculation results in *X*[0] = 10. This dependency of *X*[ ] on *N* also occurs for the other frequency components. Therefore, you usually divide the DFT output by *N* to obtain the correct magnitude of the frequency component.

Parent topic:

Discrete Fourier Transform (DFT)

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_exponential.html language=enus -->
## TOPIC 00027: Exponential

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_exponential.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_exponential.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Exponential

The shape of the exponential window is that of a decaying exponential. The following equation defines the exponential window.

[IMAGE alt='image' src='./rkset2ftemp2flvac_exponential.xml_d12524e20.png']

for *n* = 0, 1, 2, …, *N* - 1

where *N* is the length of the window, *w* is the window value, and *f* is the final value.

The initial value of the window is one and gradually decays toward zero. You can adjust the final value of the exponential
 window to between 0 and 1.

The following figure shows the exponential window for *N* = 32, with the final value specified as 0.1.

[IMAGE alt='image' src='guid-a45e18c7-0507-4379-a907-35c754d76af0-help-web.png']

The exponential window is useful for analyzing transient response signals whose duration is longer than the length of the
 window. The exponential window damps the end of the signal, ensuring that the signal fully decays by the end of the sample
 block. You can apply the exponential window to signals that decay exponentially, such as the response of structures with light
 damping that are excited by an impact, such as the impact of a hammer.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_fast_fft_sizes.html language=enus -->
## TOPIC 00028: Fast FFT Sizes

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_fast_fft_sizes.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_fast_fft_sizes.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Fast FFT Sizes

When the size of the input sequence is a power of two, *N* = 2<sup>m</sup>, you can implement the computation of the discrete Fourier transform (DFT) with approximately *N*log<sub>2</sub>(*N*) operations, which makes the calculation of the DFT much faster. DSP literature refers to the algorithms for faster DFT calculation
 as fast Fourier transforms (FFTs). Common input sequence sizes that are a power of two include 512, 1,024, and 2,048.

When the size of the input sequence is not a power of two but is factorable as the product of small prime numbers, you can
 use a mixed radix Cooley-Tukey algorithm to efficiently compute the DFT of the input sequence. For example, the following
 equation defines an input sequence size *N* as the product of small prime numbers.

[IMAGE alt='image' src='./et2ftemp2flvac_fast_fft_sizes.xml_d7811e42.png']

for *m*, *k*, *j* = 0, 1, 2, 3, …

For the input sequence size defined by the previous equation, you can compute the DFT with speeds comparable to an FFT whose
 input sequence size is a power of two. Common input sequence sizes that are factorable as the product of small prime numbers
 include 480, 640, 1,000, and 2,000.

Parent topic:

FFT Fundamentals

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_flat_top.html language=enus -->
## TOPIC 00029: Flat Top

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_flat_top.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_flat_top.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Flat Top

The flat top window has the best amplitude accuracy of all the smoothing windows at ±0.02 dB for signals exactly between
 integral cycles. Because the flat top window has a wide main lobe, it has poor frequency resolution. The following equation
 defines the flat top window.

[IMAGE alt='image' src='./2fworkset2ftemp2flvac_flat_top.xml_d12579e20.png']

| where | ω = 2πn/N |
| --- | --- |
|  | a0 = 0.215578948 |
|  | a1 = 0.416631580 |
|  | a2 = 0.277263158 |
|  | a3 = 0.083578947 |
|  | a4 = 0.006947368 |

The following figure shows a flat top window.

[IMAGE alt='image' src='guid-42a2854a-cc5b-4e8d-8e0b-f8972d14c49f-help-web.png']

The flat top window is most useful in accurately measuring the amplitude of single frequency components with little nearby
 spectral energy in the signal.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_force_window.html language=enus -->
## TOPIC 00030: Force

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_force_window.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_force_window.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Force

The following equation defines the force window.

[IMAGE alt='image' src='./kset2ftemp2flvac_force_window.xml_d12734e20.png']

*d* = (0.01)(*N*)(duty cycle), where *N* is the length of the window and duty cycle is the percentage of time the signal remains high versus low over one period.

The following figure shows the force window for *N* = 32 and duty cycle = 50.

[IMAGE alt='image' src='guid-cf781d5d-9d5a-4575-a657-8cd3cd32b92b-help-web.png']

You can use a force window to analyze transients.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_fourth_order_filter.html language=enus -->
## TOPIC 00031: Fourth-Order Filtering

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_fourth_order_filter.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_fourth_order_filter.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Fourth-Order Filtering

For bandpass and bandstop filters, which have two cut-off frequencies, fourth-order filter stages are a more direct form
 of filter design than second-order filter stages. IIR bandpass or bandstop filters resulting from fourth-order filter design
 contain cascaded fourth-order filters.

Each fourth-order filter stage has the following characteristics:

- k = 1, 2, ..., N *s* , where k is the fourth-order filter stage number and N *s* is the total number of fourth-order filter stages.
- N *s* = [( N *a* + 1)/4]
- Each fourth-order filter stage has four reverse coefficients, ( a 1*k* , a 2*k* , a 3*k* , a 4*k* ).
- The total number of reverse coefficients equals 4 N *s* .
- Each fourth-order filter stage has five forward coefficients, ( b 0*k* , b 1*k* , b 2*k* , b 3*k* , b 4*k* ).
- The total number of forward coefficients equals 5 N *s* .

You implement cascade stages in fourth-order filtering in the same manner as in second-order filtering. The following equations
 show how the filtering operation for fourth-order stages proceeds.

[IMAGE alt='image' src='./mp2flvac_fourth_order_filter.xml_d12783e153.png']

[IMAGE alt='image' src='./mp2flvac_fourth_order_filter.xml_d12783e180.png']

[IMAGE alt='image' src='./mp2flvac_fourth_order_filter.xml_d12783e336.png']

where k = 1, 2, ..., *N*<sub>*s*</sub>.

Parent topic:

Cascade Form IIR Filtering

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_frequencyanalysis_basics.html language=enus -->
## TOPIC 00032: Frequency Analysis Basics

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_frequencyanalysis_basics.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_frequencyanalysis_basics.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Frequency Analysis Basics

Use this book to learn basic concepts about frequency analysis.

Parent topic:

Frequency Analysis

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_frf_of_network.html language=enus -->
## TOPIC 00033: Frequency Response of a Network

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_frf_of_network.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_frf_of_network.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Frequency Response of a Network

The following figure shows the method for measuring the frequency response of a network.

[IMAGE alt='image' src='guid-077b66d6-ed30-4e90-9f11-d27b5013ecab-help-web.png']

In the previous figure, you apply a stimulus to the network under test and measure the stimulus and response signals. From
 the measured stimulus and response signals, you compute the frequency response function. The frequency response function gives
 the gain and phase versus frequency of a network. Use the following equation to compute the response function.

[IMAGE alt='image' src='./et2ftemp2flvac_frf_of_network.xml_d13013e35.png']

| where | H(f) is the response function |
| --- | --- |
|  | A is the stimulus signal |
|  | B is the response signal |
|  | SAB(f) is the cross power spectrum of A and B |
|  | SAA(f) is the power spectrum of A |

The frequency response function is a two-sided complex form, having real and imaginary parts. You can convert to the frequency
 response gain and the frequency response phase in the same way you compute the amplitude and phase spectrums of a power spectrum.

To convert to single-sided form, discard the second half of the response function array.

You might want to take several frequency response function readings and compute the average. You can use the same equation
 for computing the response function and substitute the average *S*<sub>*A**B*</sub>(*f*) and the average *S*<sub>*A**A*</sub>(*f*).

Parent topic:

Frequency Response and Network Analysis

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_ft_dft.html language=enus -->
## TOPIC 00034: Fourier Transform and Discrete Fourier Transform

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_ft_dft.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_ft_dft.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Fourier Transform and Discrete Fourier Transform

The Fourier transform provides a method for examining a relationship in terms of the frequency domain. The algorithm used
 to transform samples of the data from the time domain into the frequency domain is the discrete Fourier transform (DFT).

Parent topic:

Frequency Analysis

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_gaussian_window.html language=enus -->
## TOPIC 00035: Gaussian

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_gaussian_window.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_gaussian_window.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Gaussian

The following equation defines the Gaussian window.

[IMAGE alt='image' src='./t2ftemp2flvac_gaussian_window.xml_d13186e20.png']

for *n* = 0, 1, 2, …, *N* - 1

where *N* is the length of the window, *m* = (*N* - 1)/2.0, and σ is the standard deviation of the Gaussian window.

The following figure shows the Gaussian window for *N* = 32 and σ = 0.2.

[IMAGE alt='image' src='guid-3c006ebd-80ea-4cf0-a78c-28abb737394f-help-web.png']

The Gaussian window is useful for time-frequency analysis because the Fourier transform and the derivative of a Gaussian window
 both are Gaussian functions. For example, a Short-Time Fourier Transform with a Gaussian window is the Gabor transform.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_gegenbauer_orth_polynom.html language=enus -->
## TOPIC 00036: Gegenbauer Orthogonal Polynomials

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_gegenbauer_orth_polynom.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_gegenbauer_orth_polynom.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Gegenbauer Orthogonal Polynomials

The recurrence relationship defines Gegenbauer orthogonal polynomials *C*<sub>*n*</sub><sup>a</sup>(*x*) as shown by the following equations.

[IMAGE alt='image' src='./vac_gegenbauer_orth_polynom.xml_d13238e31.png']

[IMAGE alt='image' src='./vac_gegenbauer_orth_polynom.xml_d13238e56.png']

[IMAGE alt='image' src='./vac_gegenbauer_orth_polynom.xml_d13238e85.png']

Gegenbauer orthogonal polynomials satisfy the following equations.

[IMAGE alt='image' src='./vac_gegenbauer_orth_polynom.xml_d13238e224.png']

where Γ(*z*) is a gamma function defined by the following equation.

[IMAGE alt='image' src='./vac_gegenbauer_orth_polynom.xml_d13238e520.png']

Parent topic:

Orthogonal Polynomials

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_general_cosine.html language=enus -->
## TOPIC 00037: General Cosine

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_general_cosine.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_general_cosine.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### General Cosine

The following equation defines the general cosine window.

[IMAGE alt='image' src='./et2ftemp2flvac_general_cosine.xml_d13317e20.png']

for *n* = 0, 1, 2, …, *N* - 1 and ω = 2π*n*/*N*

where *N* is the length of the window and *m* is the number of coefficients that define the general cosine window.

The following figure shows the general cosine window for *N* = 32 with coefficients 0.323215218, 0.471492057, 0.175534280, 0.028497078, and 0.001261367.

[IMAGE alt='image' src='guid-a6813566-1253-4461-a861-f2c171617d7d-help-web.png']

The Hanning, Hamming, Flat Top window, and Blackman windows are special cases of the general cosine window.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_global_minimum.html language=enus -->
## TOPIC 00038: Global Minimum

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_global_minimum.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_global_minimum.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Global Minimum

In terms of solution set *X*, *x** is a global minimum of *f* over *X* if it satisfies the following relationship.

[IMAGE alt='image' src='./et2ftemp2flvac_global_minimum.xml_d13369e27.png']

Parent topic:

Local and Global Minima

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_golden_section.html language=enus -->
## TOPIC 00039: Golden Section Search Method

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_golden_section.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_golden_section.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Golden Section Search Method

The golden section search method finds a local minimum of a 1D function by bracketing the minimum. Bracketing a minimum
 requires a triplet of points, as shown in the following relationship.

*a* < *b* < *c* such that *f*(*b*) < *f*(*a*) and *f*(*b*) < *f*(*c*)

Because the relationship in the previous equation is true, the minimum of the function is within the interval (*a*, *c*). The search method starts by choosing a new point *x* between either *a* and *b* or between *b* and *c*. For example, choose a point *x* between *b* and c and evaluate *f*(*x*). If *f*(*b*) < *f*(*x*), the new bracketing triplet is *a* < *b* < *x*. If *f*(*b*) > *f*(*x*), the new bracketing triplet is *b* < *x* < *c*. In each instance, the middle point, *b* or *x*, is the current optimal minimum found during the current iteration of the search.

Parent topic:

Nonlinear Programming

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_group_delay.html language=enus -->
## TOPIC 00040: Group Delay

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_group_delay.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_group_delay.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Group Delay

One common use for the group delay is as a criterion to evaluate the phase nonlinearity of a filter. The following equation
 defines the group delay:

[IMAGE alt='image' src='./rkset2ftemp2flvac_group_delay.xml_d13560e15.png']

where phase(f) is the phase response.

If the phase response is linear, the group delay of the filter is constant, which means each frequency component experiences
 the same delay. Otherwise, the frequency components have different delays, which cause the smearing phenomenon of the time-domain
 signal.

The following figure compares the effects of a Kaiser FIR lowpass filter and an Elliptic lowpass filter on the same input
 signal.

[IMAGE alt='image' src='guid-ceec44be-bccf-4086-ad40-ad5e4acca91d-help-web.png']

The first waveform, which is the input signal, is a periodic sinc pattern with an order of 12.

The second waveform shows the effects of a Kaiser FIR lowpass filter on the input signal. The Kaiser filter has a linear phase
 response, so the filter delays the input without distorting the signal. The waveform is similar to the input signal, except
 for the delay and the attenuation.

The third waveform shows the effects of an Elliptic lowpass filter on the input signal. The phase response of the Elliptic
 filter is nonlinear, so the frequency components experience different delays. Thus, the shape of the waveform is different
 from the input signal.

Parent topic:

Practical Filters

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_hamming.html language=enus -->
## TOPIC 00041: Hamming

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_hamming.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_hamming.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Hamming

The Hamming window is a modified version of the Hanning window. The shape of the Hamming window is similar to that of a
 cosine wave. The following equation defines the Hamming window.

[IMAGE alt='image' src='./s2fworkset2ftemp2flvac_hamming.xml_d13618e23.png']

for *n* = 0, 1, 2, …, *N* - 1

where *N* is the length of the window and *w* is the window value.

The following figure shows a Hamming window with *N* = 32.

[IMAGE alt='image' src='guid-22d0b827-1941-457f-af49-b0e16b49f6a9-help-web.png']

The Hanning and Hamming windows are similar. However, in the time domain, the Hamming window does not get as close to zero
 near the edges as does the Hanning window.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_hanning.html language=enus -->
## TOPIC 00042: Hanning

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_hanning.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_hanning.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Hanning

The Hanning window has a shape similar to that of half a cycle of a cosine wave. The following equation defines the Hanning
 window.

[IMAGE alt='image' src='./s2fworkset2ftemp2flvac_hanning.xml_d13673e20.png']

for *n* = 0, 1, 2, …, *N* - 1

where *N* is the length of the window and *w* is the window value.

The following figure shows a Hanning window with *N* = 32.

[IMAGE alt='image' src='guid-c80dc912-200b-491e-ba41-5403951c9a08-help-web.png']

The Hanning window is useful for analyzing transients longer than the time duration of the window and for general-purpose
 applications.

Parent topic:

Characteristics of Different Smoothing Windows

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_hilbert_transform.html language=enus -->
## TOPIC 00043: Hilbert Transform

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_hilbert_transform.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_hilbert_transform.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Hilbert Transform

The Hilbert transform of a function *x*(*t*) is defined as

[IMAGE alt='image' src='./temp2flvac_hilbert_transform.xml_d13944e21.png']

Using Fourier identities, you can show the Fourier transform of the Hilbert transform of *x*(*t*) is

[IMAGE alt='image' src='./temp2flvac_hilbert_transform.xml_d13944e103.png']

where *x*(*t*) ⇔ *X*(*f*) is a Fourier transform pair and

[IMAGE alt='image' src='./temp2flvac_hilbert_transform.xml_d13944e167.png']

Parent topic:

Frequency Analysis

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_histogram.html language=enus -->
## TOPIC 00044: Histogram

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_histogram.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_histogram.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Histogram

A histogram is a bar graph that displays frequency data and is an indication of the data distribution. A histogram provides
 a method for graphically displaying data and summarizing key information.

The following equation defines a data sequence.

*X* = {0, 1, 3, 3, 4, 4, 4, 5, 5, 8}

To compute a histogram for *X*, divide the total range of values into the following eight intervals, or bins:

- 0-1
- 1-2
- 2-3
- 3-4
- 4-5
- 5-6
- 6-7
- 7-8

The histogram display for *X* indicates the number of data samples that lie in each interval, excluding the upper boundary. The following figure shows
 the histogram for the sequence in the previous equation.

[IMAGE alt='image' src='guid-069da07b-abd1-4c46-9acd-e0c0e354d00a-help-web.png']

The previous figure shows that no data samples are in the 2-3 and 6-7 intervals. One data sample lies in each of the intervals
 0-1, 1-2, and 7-8. Two data samples lie in each of the intervals 3-4 and 5-6. Three data samples lie in the 4-5 interval.

The number of intervals in the histogram affects the resolution of the histogram. A common method of determining the number
 of intervals to use in a histogram is Sturges' Rule, which is given by the following equation.

Number of Intervals = 1 + 3.3log(size of (*X*))

Parent topic:

Statistics

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_iir_filter_types.html language=enus -->
## TOPIC 00045: IIR Filter Types

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_iir_filter_types.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_iir_filter_types.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### IIR Filter Types

Digital IIR filter designs come from the classical analog designs and include the following filter types:

- Butterworth filters
- Chebyshev filters
- Chebyshev II filters, also known as inverse Chebyshev and Type II Chebyshev filters
- Elliptic filters, also known as Cauer filters
- Bessel filters

The IIR filter designs differ in the sharpness of the transition between the passband and the stopband and where they exhibit
 their various characteristics—in the passband or the stopband.

The following figure illustrates the magnitude responses of a typical lowpass filter designed by the IIR filter design methods.
 Each filter has the same numerator and denominator order values.

[IMAGE alt='image' src='guid-16ca7dc6-085a-47e2-a505-c7ef62342a32-help-web.png']

The following table summarizes the main features of the IIR-based design methods so you can determine the IIR filter design
 method to use.

| IIR Filter | Ripple in Passband? | Ripple in Stopband? | Transition Bandwidth for a Fixed Order | Order for Given Filter Specification |
| --- | --- | --- | --- | --- |
| Butterworth | No | No | Widest | Highest |
| Chebyshev | Yes | No | Narrower | Lower |
| Chebyshev II | No | Yes | Narrower | Lower |
| Elliptic | Yes | Yes | Narrowest | Lowest |

Parent topic:

IIR Filters

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_impuse_response.html language=enus -->
## TOPIC 00046: Impulse Response

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_impuse_response.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_impuse_response.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Impulse Response

An impulse is a short duration signal that goes from zero to a maximum value and back to zero again in a short time. The
 following set of equations provides the mathematical definition of an impulse.

*x*<sub>0</sub> = 1

*x*<sub>*i*</sub> = 0

for all *i* ≠ 0.

The impulse response of a filter is the response of the filter to an impulse and depends on the values upon which the filter
 operates. The following figure shows impulse response.

[IMAGE alt='image' src='guid-8fc111e7-da03-4524-b642-5499c58894f9-help-web.png']

The Fourier transform of the impulse response is the frequency response of the filter. The frequency response of a filter
 provides information about the output of the filter at different frequencies. In other words, the frequency response of a
 filter reflects the gain of the filter at different frequencies. For an ideal filter, the gain is one in the passband and
 zero in the stopband. An ideal filter passes all frequencies in the passband to the output unchanged but passes none of the
 frequencies in the stopband to the output.

Parent topic:

Common Digital Filters

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_line_opt.html language=enus -->
## TOPIC 00047: Line Minimization

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_line_opt.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_line_opt.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Line Minimization

The process of iteratively searching along a vector for the minimum value on the vector is line minimization or line searching.
 Line minimization can help establish a search direction or verify that the chosen search direction is likely to produce an
 optimal solution.

Nonlinear programming search algorithms use line minimization to solve the smaller problems of the optimization problem leading
 to an optimal value for *f*(*x*). The search algorithm searches along a vector until it reaches the minimum value on the vector. After the search algorithm
 reaches the minimum on one vector, the search continues along another vector, usually orthogonal to the first vector. The
 line search continues along the new vector until reaching its minimum value. The line minimization process continues until
 the search algorithm finds the optimal solution.

Parent topic:

Nonlinear Programming

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_linear_simplex.html language=enus -->
## TOPIC 00048: Linear Programming Simplex Method

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_linear_simplex.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_linear_simplex.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Linear Programming Simplex Method

A simplex describes the solution set *X* for a linear programming problem. The constraints on the value of *f*(*x*) define the polygonal surface hyperplanes of the simplex. The hyperplanes intersect at vertices along the surface of the
 simplex. The linear nature of *f*(*x*) means the optimal solution is at one of the vertices of the simplex. The linear programming simplex method iteratively moves
 from one vertex to the adjoining vertex until moving to an adjoining vertex no longer yields a more optimal solution.

|  | Note Although both the linear programming simplex method and the nonlinear downhill simplex method use the concept of a simplex, the methods have nothing else in common. |
| --- | --- |

Parent topic:

Linear Programming

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_matrix_logarithm.html language=enus -->
## TOPIC 00049: Matrix Logarithm

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_matrix_logarithm.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_matrix_logarithm.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Matrix Logarithm

The natural logarithm is the inverse operation of the exponential. The following equation defines the natural logarithm
 of a matrix *A*: *e*<sup>*B*</sup> = *A*, where matrix *B* is the natural logarithm of matrix *A*. A matrix has a logarithm if and only if its inverse matrix exists. For a real matrix *A*, its logarithm matrix *B* can be complex, and the conjugate of matrix *B* is also the natural logarithm of *A*.

To obtain the logarithm of a diagonal matrix, you can calculate the logarithm of each diagonal element of the matrix. For
 example, if

[IMAGE alt='image' src='./2ftemp2flvac_matrix_logarithm.xml_d15968e54.png']

then

[IMAGE alt='image' src='./2ftemp2flvac_matrix_logarithm.xml_d15968e143.png']

Thus, a common method of calculating the logarithm of a matrix is first to diagonalize the matrix and then to calculate the
 logarithm of each diagonal element of the new matrix. For example, consider the following:

- λ is a diagonal matrix whose diagonal elements are the eigenvalues of matrix A
- λ = V -1 A V , where V is the matrix composed of the eigenvectors of matrix A

If the previous two requirements are true, you can use the following equation to calculate the logarithm of *A*: ln(*A*) = *V*(lnλ)*V*<sup>-1</sup>.

If you cannot diagonalize a matrix, you can use other methods, such as the Jordan Canonical Form or Taylor series expansion,
 to calculate the logarithm of the matrix.

The matrix logarithm satisfies the following properties:

- ln( I ) = 0, where 0 is a zero matrix whose elements are zeros
- If ln( X )*ln( Y ) = ln( Y )*ln( X ), then ln( X Y ) = ln( X )+ln( Y )
- If Y is invertible, then ln( Y X Y -1 ) = Y ln( X ) Y -1
- ln( X *) = (ln( X ))*, where X * is the transpose of the real matrix X , or the conjugate transpose of the complex matrix X

Parent topic:

Basic Matrix Operations

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_min_peak_error.html language=enus -->
## TOPIC 00050: Minimizing Peak Error

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_min_peak_error.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_min_peak_error.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Minimizing Peak Error

The Chebyshev, Chebyshev II, and elliptic filters minimize peak error by accounting for the maximum tolerable error in
 their frequency response. The maximum tolerable error is the maximum absolute value of the difference between the ideal filter
 frequency response and the actual filter frequency response. The amount of ripple, in dB, allowed in the frequency response
 of the filter determines the maximum tolerable error. Depending on the type, the filter minimizes peak error in the passband,
 stopband, or both.

Parent topic:

IIR Filter Types

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_parseval_s_theorem.html language=enus -->
## TOPIC 00051: Parseval's Theorem

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_parseval_s_theorem.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_parseval_s_theorem.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Parseval's Theorem

Parseval's Theorem states that the total energy computed in the time domain must equal the total energy computed in the
 frequency domain. It is a statement of conservation of energy. The following equation defines the continuous form of Parseval's
 theorem.

[IMAGE alt='image' src='./emp2flvac_parseval_s_theorem.xml_d8157e22.png']

The following equation defines the discrete form of Parseval's theorem.

[IMAGE alt='image' src='./emp2flvac_parseval_s_theorem.xml_d8157e99.png']

where *x*<sub>*i*</sub> ⇔ *X*<sub>*k*</sub> is a discrete FFT pair and *n* is the number of elements in the sequence.

Parent topic:

Frequency Analysis Basics

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_partial_frac_expansion.html language=enus -->
## TOPIC 00052: Partial Fraction Expansion

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_partial_frac_expansion.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_partial_frac_expansion.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Partial Fraction Expansion

Partial fraction expansion involves splitting a rational polynomial into a summation of low order rational polynomials. Partial
 fraction expansion is a useful tool for *z*-transform and digital filter structure conversion.

Parent topic:

Rational Polynomial Function Operations

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_polynomial_lcm.html language=enus -->
## TOPIC 00053: Least Common Multiple of Two Polynomials

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_polynomial_lcm.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_polynomial_lcm.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Least Common Multiple of Two Polynomials

Finding the least common multiple of two polynomials involves finding the smallest polynomial that is a multiple of each
 polynomial.

*P*(*x*) and *Q*(*x*) are polynomials defined by the following equations, respectively.

[IMAGE alt='image' src='./et2ftemp2flvac_polynomial_lcm.xml_d18337e34.png']

[IMAGE alt='image' src='./et2ftemp2flvac_polynomial_lcm.xml_d18337e65.png']

where *U*(*x*), *V*(*x*), and *R*(*x*) are polynomials.

The following conditions are true for the previous equations:

- U ( x ) and R ( x ) are factors of P ( x ).
- V ( x ) and R ( x ) are factors of Q ( x ).
- P ( x ) is a multiple of U ( x ) and R ( x ).
- Q ( x ) is a multiple of V ( x and R ( x ).
- R ( x ) is a common factor of polynomials P ( x ) and Q ( x ).

If *L*(*x*) is a multiple of both *P*(*x*) and *Q*(*x*), *L*(*x*) is a common multiple of *P*(*x*) and *Q*(*x*). In addition, if *L*(*x*) has the lowest order among all the common multiples of *P*(*x*) and *Q*(*x*), *L*(*x*) is the least common multiple of *P*(*x*) and *Q*(*x*).

If *L*(*x*) is the least common multiple of *P*(*x*) and *Q*(*x*) and if *R*(*x*) is the greatest common divisor of *P*(*x*) and *Q*(*x*), dividing the product of *P*(*x*) and *Q*(*x*) by *R*(*x*) obtains *L*(*x*), as shown by the following equation.

[IMAGE alt='image' src='./et2ftemp2flvac_polynomial_lcm.xml_d18337e381.png']

Parent topic:

Basic Polynomial Operations

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_pop_variance.html language=enus -->
## TOPIC 00054: Population Variance

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_pop_variance.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_pop_variance.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Population Variance

Population variance measures the spread or dispersion of the population. The population variance σ<sup>2</sup> for an input sequence *X* equals the sum of the squares of the deviations of the sample values from the mean divided by *n*, as shown in the following equation.

[IMAGE alt='image' src='./kset2ftemp2flvac_pop_variance.xml_d18604e27.png']

where *n* > 1 and is the number of samples in *X*, and [IMAGE alt='image' src='./kset2ftemp2flvac_pop_variance.xml_d18604e143.png'] is the mean of *X*.

Parent topic:

Variance

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_prediction_interval.html language=enus -->
## TOPIC 00055: Prediction Interval

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_prediction_interval.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_prediction_interval.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Prediction Interval

In some applications, you might repeat the same measurement multiple times. You can use the prediction interval to estimate
 the values of the samples in the next measurement based on the samples in the current measurement. The prediction interval
 predicts the interval of the sample in future measurements with a given probability.

As with the confidence interval, the measurement error must be Gaussian distributed to calculate the prediction interval.
 Also, you must use the least squares method to fit the curve.

The calculation of the prediction interval is similar to the calculation of the confidence interval. However, the confidence
 interval includes only the uncertainty in estimating the curve coefficients, whereas the prediction interval includes both
 the uncertainty in estimating the curve coefficients and the uncertainty in measurement. Thus, the prediction interval generally
 is wider than the confidence interval.

The following figure shows an example of the prediction interval in linear fitting. The black line is the fitting line calculated
 using the least squares method. The area between the prediction bounds is the prediction interval. In this example, the confidence
 level is 0.95, which means there is a 95% probability that the samples in the next measurement fall within the prediction
 interval.

[IMAGE alt='image' src='guid-80c3542e-6c82-40ad-ab54-2b85a5a329e0-help-web.png']

Similarly to the confidence interval, larger measurement noise results in a wider prediction interval. The following figures
 show the prediction intervals of a linear model with different amounts of Gaussian white noise. The standard deviation of
 the noise is 1 in the first figure and 2 in the second figure.

[IMAGE alt='image' src='guid-44d9a5b7-b064-4c63-bb1e-74063420a14f-help-web.png']

[IMAGE alt='image' src='guid-310d8037-3dbc-4fcd-8e1b-bbef9f1d362c-help-web.png']

Parent topic:

Confidence Interval and Prediction Interval

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_prob_dist_density.html language=enus -->
## TOPIC 00056: Probability Distribution and Density Functions

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_prob_dist_density.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_prob_dist_density.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Probability Distribution and Density Functions

The following equation defines the probability distribution function *F*(*x*).

[IMAGE alt='image' src='./temp2flvac_prob_dist_density.xml_d18695e27.png']

where *F*(*x*) is the probability density function, *f*(*x*) ≥ 0 ∀ *x* ∈ domain of *f*, and [IMAGE alt='image' src='./temp2flvac_prob_dist_density.xml_d18695e88.png'].

By performing differentiation, you can derive the following equation from the previous equation.

[IMAGE alt='image' src='./temp2flvac_prob_dist_density.xml_d18695e127.png']

You can use a histogram to obtain a denormalized discrete representation of *f*(*x*). The following equation defines the discrete representation of *f*(*x*).

[IMAGE alt='image' src='./temp2flvac_prob_dist_density.xml_d18695e175.png']

The following equation yields the sum of the elements of the histogram.

[IMAGE alt='image' src='./temp2flvac_prob_dist_density.xml_d18695e218.png']

where *m* is the number of samples in the histogram and *n* is the number of samples in the input sequence representing the function.

Therefore, to obtain an estimate of *F*(*x*) and *f*(*x*), normalize the histogram by a factor of Δ*x* = 1/*n* and let *h*<sub>*j*</sub> = *x*<sub>*j*</sub>.

Parent topic:

Probability

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_rational_polynom_add.html language=enus -->
## TOPIC 00057: Rational Polynomial Function Addition

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_rational_polynom_add.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_rational_polynom_add.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Rational Polynomial Function Addition

The following equations define two rational polynomials.

[IMAGE alt='image' src='./p2flvac_rational_polynom_add.xml_d18979e15.png']

[IMAGE alt='image' src='./p2flvac_rational_polynom_add.xml_d18979e66.png']

The following equation shows the addition of two rational polynomials.

[IMAGE alt='image' src='./p2flvac_rational_polynom_add.xml_d18979e121.png']

Parent topic:

Rational Polynomial Function Operations

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_rational_polynom_divide.html language=enus -->
## TOPIC 00058: Rational Polynomial Function Division

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_rational_polynom_divide.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_rational_polynom_divide.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Rational Polynomial Function Division

The following equations define two rational polynomials.

[IMAGE alt='image' src='./vac_rational_polynom_divide.xml_d19036e15.png']

[IMAGE alt='image' src='./vac_rational_polynom_divide.xml_d19036e66.png']

The following equation shows the division of two rational polynomials.

[IMAGE alt='image' src='./vac_rational_polynom_divide.xml_d19036e121.png']

Parent topic:

Rational Polynomial Function Operations

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_sampling_integer_number_of_cycles.html language=enus -->
## TOPIC 00059: Sampling an Integer Number of Cycles

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_sampling_integer_number_of_cycles.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_sampling_integer_number_of_cycles.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Sampling an Integer Number of Cycles

Spectral leakage occurs only when the sample data set consists of a noninteger number of cycles. The following figure shows
 a sine wave sampled at an integer number of cycles and the Fourier transform of the sine wave.

[IMAGE alt='image' src='guid-8dcf9584-0d6d-4a5c-8202-413a5a60a778-help-web.png']

In the previous figure, Graph 1 shows the sampled time-domain waveform. Graph 2 shows the periodic time waveform of the sine
 wave from Graph 1. In Graph 2, the waveform repeats to fulfill the assumption of periodicity for the Fourier transform. Graph
 3 shows the spectral representation of the waveform.

Because the time record in Graph 2 is periodic with no discontinuities, its spectrum appears in Graph 3 as a single line showing
 the frequency of the sine wave. The waveform in Graph 2 does not have any discontinuities because the data set is from an
 integer number of cycles—in this case, one.

The following methods are the only methods that guarantee you always acquire an integer number of cycles:

- Sample synchronously with respect to the signal you measure. Therefore, you can acquire an integral number of cycles deliberately.
- Capture a transient signal that fits entirely into the time record.

Parent topic:

Spectral Leakage

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_sinad.html language=enus -->
## TOPIC 00060: Signal Noise and Distortion (SINAD)

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_sinad.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_sinad.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Signal Noise and Distortion (SINAD)

Similar to THD + N, SINAD takes into account both harmonics and noise. However, SINAD is the reciprocal of THD + N. The
 following equation yields SINAD.

[IMAGE alt='image' src='./-us2fworkset2ftemp2flvac_sinad.xml_d20310e26.png']

You can use SINAD to characterize the performance of FM receivers in terms of sensitivity, adjacent channel selectivity, and
 alternate channel selectivity.

Parent topic:

Harmonic Distortion

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_single_tone.html language=enus -->
## TOPIC 00061: Single Tone

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_single_tone.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_single_tone.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Single Tone

A single-tone measurement requires a stimulus signal, which is always a single-tone sine wave that excites the device under
 test (DUT) at a specific frequency. A single-tone measurement characterizes the magnitude and phase of one specific frequency
 of the DUT.

Because a single-tone measurement uses a pure-tone stimulus signal, you can choose an arbitrary test frequency and duration.
 Thus you can have the optimal dynamic range and most accurate result of harmonic distortion. However, a single-tone measurement
 requires much test time to cover multiple frequencies because the result is single-point.

Parent topic:

Frequency Response and Stimulus Signal

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_skewness.html language=enus -->
## TOPIC 00062: Skewness

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_skewness.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_skewness.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Skewness

Skewness is a measure of symmetry and corresponds to the third-order moment.

A negative value of skewness indicates that the left side of the probability density function is longer than the right side.
 A positive value of skewness indicates that the right side of the probability density function is longer than the right side.

The following figure shows negative skewness.

[IMAGE alt='image' src='guid-505be66a-5936-4fef-ad43-e22a630825b0-help-web.png']

The following figure shows positive skewness.

[IMAGE alt='image' src='guid-35d14e43-284b-45d7-8eb0-ee8ebb6b0bea-help-web.png']

Parent topic:

Moment about the Mean

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_svd_factorization.html language=enus -->
## TOPIC 00063: SVD Factorization

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_svd_factorization.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_svd_factorization.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SVD Factorization

The Singular Value Decomposition (SVD) method decomposes a matrix into the product of three matrices, such that *A* = *U**S**V*<sup>*T*</sup>. If *A* is a real matrix, *U* and *V* are orthogonal matrices. If *A* is a complex matrix, *U* and *V* are unitary matrices. *S* is a diagonal matrix whose diagonal values are in descending order. The diagonal values in *S* are the nonnegative square roots of the eigenvalues of *A*<sup>*T*</sup>*A* and are defined as the singular values of *A*. The columns of *U* and *V*, which are called left and right singular vectors, are orthonormal eigenvectors of *A**A*<sup>*T*</sup> and *A*<sup>*T*</sup>*A*, respectively, or, when *A* is complex, unitary eigenvectors of *A**A*<sup>*H*</sup> and *A*<sup>*H*</sup>*A*.

SVD has many properties you can use to solve problems. For example, the absolute value of the determinant of matrix *A* equals the product of all the singular values. Also, the 2-norm of *A* is its maximum singular value.

One common method of calculating the SVD factorization is QR iteration.

SVD is useful for solving analysis problems such as computing the rank, norm, condition number, and pseudoinverse of matrices.

Parent topic:

Matrix Factorization

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_weighting.html language=enus -->
## TOPIC 00064: Weighting

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_weighting.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_weighting.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Weighting

When performing RMS or vector averaging, you can weight each new spectral record using either linear or exponential weighting.

Linear weighting combines *N* spectral records with equal weighting. When the number of averages is completed, the analyzer stops averaging and presents
 the averaged results.

Exponential weighting emphasizes new spectral data more than old and is a continuous process.

Weighting is applied according to the following equation.

[IMAGE alt='image' src='./workset2ftemp2flvac_weighting.xml_d21854e35.png']

where *X*<sub>*i*</sub> is the result of the analysis performed on the *i*th block, *Y*<sub>*i*</sub> is the result of the averaging process from *X*<sub>1</sub> to *X*<sub>*i*</sub>, *N* = *i* for linear weighting, and *N* is a constant for exponential weighting (*N* = 1 for *i* = 1).

Parent topic:

Averaging Modes

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/lvac_zero_padding.html language=enus -->
## TOPIC 00065: Zero Padding

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/lvac_zero_padding.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/lvac_zero_padding.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Zero Padding

Zero padding is a technique typically employed to make the size of the input sequence equal to a power of two. In zero
 padding, you add zeros to the end of the input sequence so that the total number of samples is equal to the next higher power
 of two. For example, if you have 10 samples of a signal, you can add six zeros to make the total number of samples equal to
 16, or 32, which is a power of two. The following figure shows padding 10 samples of a signal with zeros to make the total
 number of samples equal 16.

[IMAGE alt='image' src='guid-723a9f4f-5a99-4a85-81fd-d38e10c125c6-help-web.png']

The addition of zeros to the end of the time-domain waveform does not improve the underlying frequency resolution associated
 with the time-domain signal. The only way to improve the frequency resolution of the time-domain signal is to increase the
 acquisition time and acquire longer time records.

In addition to making the total number of samples a power of two so that faster computation is made possible by using the
 fast Fourier transform (FFT), zero padding can lead to an interpolated FFT result, which can produce a higher display resolution.

Parent topic:

FFT Fundamentals

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/matrix_ops_eigen_problems.html language=enus -->
## TOPIC 00066: Basic Matrix Operations

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/matrix_ops_eigen_problems.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/matrix_ops_eigen_problems.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Basic Matrix Operations

Two matrices, *A* and *B*, are equal if they have the same number of rows and columns and their corresponding elements all are equal. Multiplication
 of a matrix *A* by a scalar α is equal to multiplication of all its elements by the scalar. That is,

[IMAGE alt='image' src='./p2fmatrix_ops_eigen_problems.xml_d4561e29.png']

For example,

[IMAGE alt='image' src='./p2fmatrix_ops_eigen_problems.xml_d4561e83.png']

Two (or more) matrices can be added or subtracted only if they have the same number of rows and columns. If both matrices
 *A* and *B* have *m* rows and *n* columns, their sum *C* is an *m* × *n* matrix defined as *C* = *A* ± *B*, where *c*<sub>*i*,*j*</sub> = *a*<sub>*i*,*j*</sub> ± *b*<sub>*i*,*j*</sub>. For example,

[IMAGE alt='image' src='./p2fmatrix_ops_eigen_problems.xml_d4561e195.png']

For multiplication of two matrices, the number of columns of the first matrix must be equal to the number of rows of the second
 matrix. If matrix *A* has *m* rows and *n* columns and matrix *B* has *n* rows and *p* columns, their product *C* is an *m* × *p* matrix defined as *C* = *A**B*, where

[IMAGE alt='image' src='./p2fmatrix_ops_eigen_problems.xml_d4561e304.png']

For example,

[IMAGE alt='image' src='./p2fmatrix_ops_eigen_problems.xml_d4561e373.png']

So you multiply the elements of the first row of *A* by the corresponding elements of the first column of *B* and add all the results to get the elements in the first row and first column of *C*. Similarly, to calculate the element in the *i*th row and the *j*th column of *C*, multiply the elements in the *i*th row of *A* by the corresponding elements in the *j*th column of *C*, and then add them all. This is shown pictorially in the following figure.

[IMAGE alt='image' src='guid-409305fa-c6c4-48c0-9e03-ea86bfa57ac0-help-web.png']

Matrix multiplication, in general, is not commutative, that is, *A**B* ≠ *B**A*. Also, multiplication of a matrix by an identity matrix results in the original matrix.

Parent topic:

Linear Algebra

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/multitone_generation.html language=enus -->
## TOPIC 00067: Multitone Generation

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/multitone_generation.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/multitone_generation.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Multitone Generation

Except for the sine wave, the common test signals do not allow full control over their spectral content. For example, the
 harmonic components of a square wave are fixed in frequency, phase, and amplitude relative to the fundamental. However, you
 can generate multitone signals with a specific amplitude and phase for each individual frequency component.

A multitone signal is the superposition of several sine waves or tones, each with a distinct amplitude, phase, and frequency.
 A multitone signal is typically created so that an integer number of cycles of each individual tone are contained in the signal.
 If an FFT of the entire multitone signal is computed, each of the tones falls exactly onto a single frequency bin, which means
 no spectral spread or leakage occurs.

Multitone signals are a part of many test specifications and allow the fast and efficient stimulus of a system across an arbitrary
 band of frequencies. Multitone test signals are used to determine the frequency response of a device and with appropriate
 selection of frequencies, also can be used to measure such quantities as intermodulation distortion.

Parent topic:

Signal Generation

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/noise_generation.html language=enus -->
## TOPIC 00068: Noise Generation

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/noise_generation.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/noise_generation.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Noise Generation

You can use noise signals to perform frequency response measurements or to simulate certain processes. Several types of
 noise are typically used, namely uniform white noise, Gaussian white noise, and periodic random noise.

The term white in the definition of noise refers to the frequency domain characteristic of noise. Ideal white noise has
 equal power per unit bandwidth, resulting in a flat power spectral density across the frequency range of interest. Thus, the
 power in the frequency range from 100 Hz to 110 Hz is the same as the power in the frequency range from 1,000 Hz to 1,010
 Hz. In practical measurements, achieving the flat power spectral density requires an infinite number of samples. Thus, when
 making measurements of white noise, the power spectra are usually averaged, with more number of averages resulting in a flatter
 power spectrum.

The terms uniform and Gaussian refer to the probability density function (PDF) of the amplitudes of the time-domain samples
 of the noise. For uniform white noise, the PDF of the amplitudes of the time domain samples is uniform within the specified
 maximum and minimum levels. In other words, all amplitude values between some limits are equally likely or probable. Thermal
 noise produced in active components tends to be uniform white in distribution. The following figure shows the distribution
 of the samples of uniform white noise.

[IMAGE alt='loc_fp_uniform_white_noise.gif' src='guid-ca3491b8-d69a-4855-bc82-e5557c99334f-help-web.png']

For Gaussian white noise, the PDF of the amplitudes of the time domain samples is Gaussian. If uniform white noise is passed
 through a linear system, the resulting output is Gaussian white noise. The following figure shows the distribution of the
 samples of Gaussian white noise.

[IMAGE alt='loc_fp_gaussian_white_noise.gif' src='guid-af170e7a-ad24-40b5-a76c-cc9981708042-help-web.png']

Periodic random noise (PRN) is a summation of sinusoidal signals with the same amplitudes but with random phases. PRN consists
 of all sine waves with frequencies that can be represented with an integral number of cycles in the requested number of samples.
 Because PRN contains only integral-cycle sinusoids, you do not need to window PRN before performing spectral analysis. PRN
 is self-windowing and therefore has no spectral leakage.

PRN does not have energy at all frequencies as white noise does but has energy only at discrete frequencies that correspond
 to harmonics of a fundamental frequency. The fundamental frequency is equal to the sampling frequency divided by the number
 of samples. However, the level of noise at each of the discrete frequencies is the same.

You can use PRN to compute the frequency response of a linear system with one time record instead of averaging the frequency
 response over several time records, as you must for non-periodic random noise sources. The following figure shows the spectrum
 of PRN and the averaged spectra of white noise.

[IMAGE alt='loc_fp_psd_of_white_noise_and_prn.gif' src='guid-75e62d28-3a08-443e-940e-e8b232cc193b-help-web.png']

Parent topic:

Signal Generation

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/probability_c.html language=enus -->
## TOPIC 00069: Probability

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/probability_c.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/probability_c.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Probability

In any random experiment, a chance, or probability, always exists that a particular event will or will not occur. The probability
 that event A will occur is the ratio of the number of outcomes favorable to A to the total number of possible outcomes.

You can assign a number between zero and one to an event as an indication of the probability that the event will occur. If
 you are absolutely sure that the event will occur, its probability is 100% or one. If you are sure that the event will not
 occur, its probability is zero.

Parent topic:

Probability and Statistics

<!--NI_TOPIC bundle=labwindows-cvi path=advancedanalysisconcepts/sampling_rate_df.html language=enus -->
## TOPIC 00070: Sampling Rate

- bundle_id: `labwindows-cvi`
- source_path: `advancedanalysisconcepts/sampling_rate_df.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/advancedanalysisconcepts/sampling_rate_df.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Sampling Rate

The sampling rate is important to the success of a filtering operation. The maximum frequency component of the signal of
 interest usually determines the sampling rate. In general, choose a sampling rate 10 times higher than the highest frequency
 component of the signal of interest.

Make exceptions to the previous sampling rate guideline when filter cut-off frequencies must be very close to either DC or
 the Nyquist frequency. Filters with cut-off frequencies close to DC or the Nyquist frequency might have a slow rate of convergence.
 You can take the following actions to overcome the slow convergence:

- If the cut-off is too close to the Nyquist frequency, increase the sampling rate.
- If the cut-off is too close to DC, reduce the sampling rate.

In general, adjust the sampling rate only if you encounter problems.

Parent topic:

Digital Filtering

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/1d_operations_class_advanlys.html language=enus -->
## TOPIC 00071: 1D Operations Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/1d_operations_class_advanlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/1d_operations_class_advanlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### 1D Operations Class Help

This class contains functions that perform arithmetic operations on 1D arrays. Most functions can perform their operations in place, which can be helpful when processing large data sets.

**Library**: [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/1d_operations_class_reganlys.html language=enus -->
## TOPIC 00072: 1D Operations Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/1d_operations_class_reganlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/1d_operations_class_reganlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### 1D Operations Class Help

This class contains functions that perform arithmetic operations on 1D arrays. Most functions can perform their operations in place, which can be helpful when processing large data sets.

**Library**: [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/2d_operations_class_advanlys.html language=enus -->
## TOPIC 00073: 2D Operations Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/2d_operations_class_advanlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/2d_operations_class_advanlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### 2D Operations Class Help

This class contains functions that perform arithmetic operations on 2D arrays. Most functions can perform their operations in place, which can be helpful when processing large data sets.

**Library**: [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/2d_operations_class_reganlys.html language=enus -->
## TOPIC 00074: 2D Operations Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/2d_operations_class_reganlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/2d_operations_class_reganlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### 2D Operations Class Help

This class contains functions that perform arithmetic operations on 2D arrays. Most functions can perform their operations in place, which can be helpful when processing large data sets.

**Library**: [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/absolute_time_class_utility.html language=enus -->
## TOPIC 00075: Absolute Time Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/absolute_time_class_utility.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/absolute_time_class_utility.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Absolute Time Class Help

This class contains functions for working with absolute calendar times.

**Library**: [Utility Library](../../cvi/libref/cviutility_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/activexadvancedobjects.htm language=enus -->
## TOPIC 00076: Completing Advanced Object-Specific Tasks in ActiveX Applications

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/activexadvancedobjects.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/activexadvancedobjects.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Completing Advanced Object-Specific Tasks in ActiveX Applications

The Object Helper Functions class contains functions that you can use to perform advanced object-specific tasks. Calling [CA_ServerLockActiveObject](cvica_serverlockactiveobject.htm) on an ActiveX object results in an additional internal reference to the object, independent of the external ActiveX references to the object. Call CA_ServerLockActiveObject when the ActiveX object displays a user interface that appears on the screen. Lock the object to prevent the user interface from disappearing when the last external reference to the ActiveX object is released. You must call [CA_ServerUnlockActiveObject](cvica_serverunlockactiveobject.htm) when the user interface of a previously locked ActiveX object is being hidden or discarded. Call [CA_ServerDestroyActiveObject](cvica_serverdestroyactiveobject.htm) to destroy, in response to an interactive user command, an ActiveX object that was locked when it appeared. CA_ServerDestroyActiveObject destroys an ActiveX object even though clients might be holding external references to the object. Use CA_ServerDestroyActiveObject only for the preceding purpose.

#### Example Code: Locking, Unlocking, and Destroying User Interface Objects

The following sample demonstrates locking, unlocking, and destroying user interface objects:

/* User ActiveX function for method Show of interface IFoo in object UIObj */ 

HRESULT CVIFUNC UIObjIFooShow (CAServerObjHandle objHandle) 

{ 

   HRESULT hr = S_OK; 

   int panel = 0; 
 

   panel = GetUserInterfacePanel (objHandle); // Internal call: Get the UI panel 
 

   if (panel > 0 && !IsPanelVisible (panel)) { 

      // Lock the object as its lifetime is now determined by the user interface 

      hr = CA_ServerLockActiveObject (objHandle); 

      if (FAILED (hr)) 

         return hr; 

      DisplayPanel (panel); // Display the user interface 

   } 

   return hr; 

} 

/* User ActiveX function for method Hide of interface IFoo in object UIObj */ 

HRESULT CVIFUNC UIObjIFooHide (CAServerObjHandle objHandle) 

{ 

   HRESULT hr = S_OK; 

   int panel = 0; 
 


   panel = GetUserInterfacePanel (objHandle); // Internal call: Get the UI panel 
 

   if (panel > 0 && IsPanelVisible (panel)) { 

      HidePanel (panel); // Hide the user interface 

      // Unlock the object as its lifetime is now determined by COM 

      hr = CA_ServerUnlockActiveObject (objHandle); 

      if (FAILED (hr)) 

         return hr; 

   } 

   return hr; 

} 

/* User interactive callback to quit the user interface of the ActiveX object */ 

int CVICALLBACK QuitCb (int panel, int control, int event, void *callbackData, int eventData1, int eventData2) 

{ 

   if (event == EVENT_COMMIT) { 

      CAServerObjHandle objHandle = 0; 
 

      // Internal call: Get the ActiveX object's handle 

      objHandle = GetActiveXObjHandle (panel); 

      if (objHandle && IsPanelVisible (panel)) { 

         // Destroy the ActiveX object cleanly, as it was locked when it was made visible 


         CA_ServerDestroyActiveObject (objHandle); 

      } 

      // Quit the user interface 

      QuitUserInterface (0); 

   } 

}

#### Example Code: Specifying Error Information

If an ActiveX object provides rich error information you must call [CA_ServerSetErrorInfo](cvica_serverseterrorinfo.htm) in the feature functions to
specify error information for the returned failure code. If the feature functions return a success return value, do not call
CA_ServerSetErrorInfo. On error, a feature function compatible with ErrorInfo must free resources, call
CA_ServerSetErrorInfo, and return immediately after CA_ServerSetErrorInfo returns. The following code sample demonstrates the use of CA_ServerSetErrorInfo:

|  | Note To enable rich error information, enable the Support ErrorInfo option in the Edit ActiveX Object Advanced Options dialog box. |
| --- | --- |

/* User ActiveX function for method Foo of interface IFoo in object Obj */ 

HRESULT CVIFUNC ObjIFooFoo (CAServerObjHandle objHandle) 

{ 

   HRESULT hr = S_OK; 

   char *pcBuf = NULL; 
 

   // Try allocating a 1K buffer 

   pcBuf = CA_AllocMemory (sizeof (char) * 1024); 

   if (pcBuf) { 

      // Make some internal call with buffer 

      hr = MyInternalCall (pcBuf); 

      if (FAILED (hr)) 

         goto Error; 

   } 

   else { 

      hr = E_OUTOFMEMORY; 

      goto Error; 

   } 

   Error: 

      // Clean up resources 

      if (pcBuf) 

         CA_FreeMemory (pcBuf); 

      // Set error info 

      if (FAILED (hr)) { 

         CA_ServerSetErrorInfo ( 

            objHandle, // handle of object setting error 

            &IID_IFoo, // IID of interface setting error 

            "Error occurred", // error description 

            "MyServer.chm", // help file containing more info 

            HLP_CTX_ERROR // help context in help file 

         ); 

      } 

      // Return immediately after setting error info 

      return hr; 

}

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/advanced_functions_class_cviauto.html language=enus -->
## TOPIC 00077: Advanced Functions Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/advanced_functions_class_cviauto.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/advanced_functions_class_cviauto.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Advanced Functions Class Help

Contains advanced functions intended to be [used in conjunction with the code](../../cvi/libref/activexadvancedobjects.htm) that the Create ActiveX Server Wizard generates. This wizard is invoked by the **Tools»Create ActiveX Server** command.

**Library**: [ActiveX Library](../../cvi/libref/cviactivex_automation_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/advanced_functions_class_cvinetv.html language=enus -->
## TOPIC 00078: Advanced Functions Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/advanced_functions_class_cvinetv.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/advanced_functions_class_cvinetv.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Advanced Functions Class Help

This class contains functions you can call for advanced operations. You do not normally need to call these functions.

**Library**: [Network Variable Library](../../cvi/libref/cvinetworkvariablelibrary.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/assigning_values_to_variants_class_cviauto.html language=enus -->
## TOPIC 00079: Assigning Values to Variants Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/assigning_values_to_variants_class_cviauto.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/assigning_values_to_variants_class_cviauto.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Assigning Values to Variants Class Help

This class contains functions that assign values to variants.

**Library**: [ActiveX Library](../../cvi/libref/cviactivex_automation_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_tp_function_thread_id.html language=enus -->
## TOPIC 00080: ATTR_TP_FUNCTION_THREAD_ID

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_tp_function_thread_id.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_tp_function_thread_id.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TP_FUNCTION_THREAD_ID

| Data Type: | unsigned int |
| --- | --- |
| Description: | This attribute specifies the thread ID of the thread that is executing or executed the Thread Function. You can obtain the value of this attribute only while the Thread Function is executing or when the Thread Function has finished executing. Call CmtGetThreadPoolFunctionAttribute with the ATTR_TP_FUNCTION_EXECUTION_STATUS attribute to get the execution state of the function. |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_tsq_growth_increment.html language=enus -->
## TOPIC 00081: ATTR_TSQ_GROWTH_INCREMENT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_tsq_growth_increment.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_tsq_growth_increment.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TSQ_GROWTH_INCREMENT

| Data Type: | size_t |
| --- | --- |
| Description: | This attribute specifies the number of items in the growth increment. When a dynamically sizeable thread safe queue is full and a thread writes items to it, the queue grows its buffer by the smallest multiple of the growth increment needed to hold the new data. You can set this attribute only on queues that are dynamically sizable. |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_tsq_queue_options.html language=enus -->
## TOPIC 00082: ATTR_TSQ_QUEUE_OPTIONS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_tsq_queue_options.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_tsq_queue_options.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TSQ_QUEUE_OPTIONS

| Data Type: | integer |
| --- | --- |
| Description: | This attribute specifies the configuration options for the thread safe queue. The configuration options are flag values that are set through the options parameter to the CmtNewTSQ function. |
| Values: | OPT_TSQ_DYNAMIC_SIZE (1)The thread safe queue grows when it is full and a write operation occurs. OPT_TSQ_AUTO_FLUSH_ALL (2)The thread safe queue removes all old data when it is full and a write operation occurs. OPT_TSQ_AUTO_FLUSH_EXACT (4)The thread safe queue removes enough old data to fit the new data when it is full and a write operation occurs. |
| OPT_TSQ_DYNAMIC_SIZE (1) | The thread safe queue grows when it is full and a write operation occurs. |
| OPT_TSQ_AUTO_FLUSH_ALL (2) | The thread safe queue removes all old data when it is full and a write operation occurs. |
| OPT_TSQ_AUTO_FLUSH_EXACT (4) | The thread safe queue removes enough old data to fit the new data when it is full and a write operation occurs. |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_tsq_queue_size.html language=enus -->
## TOPIC 00083: ATTR_TSQ_QUEUE_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_tsq_queue_size.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_tsq_queue_size.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TSQ_QUEUE_SIZE

| Data Type: | size_t |
| --- | --- |
| Description: | This attribute specifies the size of the queue in number of items. If you set this attribute while a writer thread is active, CmtSetTSQAttribute waits for the writer thread to finish its operation before resizing the queue. |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_tsq_reader_active.html language=enus -->
## TOPIC 00084: ATTR_TSQ_READER_ACTIVE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_tsq_reader_active.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_tsq_reader_active.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TSQ_READER_ACTIVE

| Data Type: | integer |
| --- | --- |
| Description: | This attribute specifies whether a reader thread is currently active. A reader thread is active when it is inside a call to CmtReadTSQData or when it has obtained the read pointer from CmtGetTSQReadPtr and has not released it with CmtReleaseTSQReadPtr. |
| Values: | FALSE (0)False TRUE (1)True |
| FALSE (0) | False |
| TRUE (1) | True |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_udp_callback_data.html language=enus -->
## TOPIC 00085: ATTR_UDP_CALLBACK_DATA

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_udp_callback_data.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_udp_callback_data.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_UDP_CALLBACK_DATA

| Data Type: | pointer |
| --- | --- |
| Description: | This attribute specifies the data passed to the callback function. |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_udp_multicast_output_interface.html language=enus -->
## TOPIC 00086: ATTR_UDP_MULTICAST_OUTPUT_INTERFACE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_udp_multicast_output_interface.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_udp_multicast_output_interface.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_UDP_MULTICAST_OUTPUT_INTERFACE

| Data Type: | string |
| --- | --- |
| Description: | This attribute specifies the local network interface, or IP address, on which to send multicast datagrams. A channel can send multicast datagrams on only one interface at a time, regardless of system configuration. By default, you specify this interface when you create the channel. If you do not specify an interface when you create the channel, LabWindows/CVI uses the system's default interface. For example, if you are sending a multicast from a computer with more than one network card, you must select a single output interface even though the system has multiple IP addresses. |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attr_udp_multicast_ttl.html language=enus -->
## TOPIC 00087: ATTR_UDP_MULTICAST_TTL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attr_udp_multicast_ttl.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attr_udp_multicast_ttl.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_UDP_MULTICAST_TTL

| Data Type: | integer |
| --- | --- |
| Description: | This attribute specifies the reach of a multicast datagram. ATTR_UDP_MULTICAST_TTL represents both a maximum router hop count and a regional boundary for the datagram. For example, multicast routers at a continental boundary only forward datagrams with a TTL of at least 128. A datagram sent with an original TTL of 100 is transmitted until it has been forwarded by 100 routers or until it hits a continental boundary. Default value: 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/attributesforcnsgetendpointattribute.htm language=enus -->
## TOPIC 00088: Attributes for CNSGetEndpointAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/attributesforcnsgetendpointattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/attributesforcnsgetendpointattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### List of Network Stream Endpoint Attributes

The following list contains the network stream endpoint attributes. You can get and set the network stream endpoint attributes using the [CNSGetEndpointAttribute](cvicnsgetendpointattribute.htm) Network Streams Library function.

[Data Type](cnsattributedatatype.html)

[Array Element Type](cnsattributearrayelementtype.html)

[Items Available for Reading](cnsattributeitemsavailforreading.html)

[Items Available for Writing](cnsattributeitemsavailforwriting.html)

[Remote Buffer Size](cnsattributeremotebuffersize.html)

[Remote Buffer Free Space](cnsattributeremotebufferfreespace.html)

[Total Number of Read Items](cnsattributetotalitemsread.html)

[Total Number of Written Items](cnsattributetotalitemswritten.html)

[Is Endpoint Connected](cnsattributeisendpointconnected.html)

[Number of Disconnections](cnsattributenumberofdisconnections.html)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/browser_functions_class_cvinetv.html language=enus -->
## TOPIC 00089: Browser Functions Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/browser_functions_class_cvinetv.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/browser_functions_class_cvinetv.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Browser Functions Class Help

This class contains functions you can use to browse for network variables or create a network variable browser. You also can use the [NetworkVariablePopup](../../toolslib/functionreference/cvinetworkvariablepopup.htm) toolbox function to browse for network variables.

**Library**: [Network Variable Library](../../cvi/libref/cvinetworkvariablelibrary.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/buffer_control_class_ansi_c.html language=enus -->
## TOPIC 00090: Buffer Control Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/buffer_control_class_ansi_c.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/buffer_control_class_ansi_c.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Buffer Control Class Help

This class contains functions for buffering the specified stream.

**Library**: [ANSI C Library](../../cvi/libref/cviansi_c_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/callbacks_class_rs232.html language=enus -->
## TOPIC 00091: Callbacks Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/callbacks_class_rs232.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/callbacks_class_rs232.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Callbacks Class Help

This class contains functions that you can use to install callback functions that are called when certain RS-232
events occur.

**Library**: [RS-232 Library](../../cvi/libref/cvirs232_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/character_operations_class_ansi_c.html language=enus -->
## TOPIC 00092: Character Operations Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/character_operations_class_ansi_c.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/character_operations_class_ansi_c.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Character Operations Class Help

This class contains functions that return information about a specified byte and functions that move character pointers in a specified string.

Refer to the [Programming for Multibyte Character Sets in LabWindows/CVI](../../cvi/programmerref/programmingmultibytechars.htm) topic for information about working with multibyte character sets.

**Library**: [ANSI C Library](../../cvi/libref/cviansi_c_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cnsattributedatatype.html language=enus -->
## TOPIC 00093: CNSAttributeDataType

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cnsattributedatatype.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cnsattributedatatype.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSAttributeDataType

| Data Type: | CNSType |
| --- | --- |
| Description: | This attribute returns the data type of the endpoint. If the returned data type is CNSTypeArray, you can use the CNSAttributeArrayElementType attribute to determine the data type of the array element. |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cnsattributeisendpointconnected.html language=enus -->
## TOPIC 00094: CNSAttributeIsEndpointConnected

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cnsattributeisendpointconnected.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cnsattributeisendpointconnected.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSAttributeIsEndpointConnected

| Data Type: | integer |
| --- | --- |
| Description: | This attribute returns 1 if an endpoint is connected to another endpoint and returns 0 otherwise. This attribute does not contact the remote endpoint to confirm the actual state of the network connection. |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cnsattributetotalitemsread.html language=enus -->
## TOPIC 00095: CNSAttributeTotalItemsRead

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cnsattributetotalitemsread.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cnsattributetotalitemsread.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSAttributeTotalItemsRead

| Data Type: | unsigned long long |
| --- | --- |
| Description: | This attribute returns the number of items the reader endpoint has read from the stream. |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cnsdata.htm language=enus -->
## TOPIC 00096: Network Stream Data

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cnsdata.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cnsdata.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Network Stream Data

Network stream data (CNSData) is an object in the LabWindows/CVI Network Streams Library that encapsulates complex data types. National Instruments recommends that you use a native C data type instead of network stream data when performance is critical.

An example of using network stream data is an application that streams a C structure. The following example shows how to convert a C structure to network stream data and vice versa.

typedef struct {

int int_data; 

 double double_data; 

 char * description;

} structData;

CNSData ToCNSData(structData data) 

{

CNSData cnsData, cnsArray[3]; 
 


 CNSDataCreateScalar(CNSTypeInt32, &cnsArray[0], data.int_data); 

 CNSDataCreateScalar(CNSTypeDouble, &cnsArray[1], data.double_data); 

 CNSDataCreateScalar(CNSTypeString, &cnsArray[2], data.description); 
 


 // Create the CNSData containing the struct 

 CNSDataCreateStruct(cnsArray, 3, &cnsData); 
 


 // Discard the intermediate CNSData objects 

 CNSDataDiscard(cnsArray[0]); 

 CNSDataDiscard(cnsArray[1]); 

 CNSDataDiscard(cnsArray[2]); 
 


 // Return the CNSData containing the struct 

 return cnsData;

}

structData FromCNSData(CNSData cnsData) 

{

structData data; 

 CNSData cnsArray[3]; 
 


 // Unpack the CNSData structure 

 CNSDataGetStructFields(cnsData, cnsArray, 3); 
 


 // Get the data from the CNSData objects 

 CNSDataGetScalarValue(cnsArray[0], &data.int_data); 

 CNSDataGetScalarValue(cnsArray[1], &data.double_data); 

 CNSDataGetScalarValue(cnsArray[2], &data.description); // needs to be freed using CNSFreeMemory 
 


 // Discard the intermediate CNSData objects 

 CNSDataDiscard(cnsArray[0]); 

 CNSDataDiscard(cnsArray[1]); 

 CNSDataDiscard(cnsArray[2]); 
 


 return data;

}

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cnvflushonwriteattribute.html language=enus -->
## TOPIC 00097: CNVFlushOnWriteAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cnvflushonwriteattribute.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cnvflushonwriteattribute.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVFlushOnWriteAttribute

| Data Type: | integer |
| --- | --- |
| Description: | This attribute specifies whether the library flushes all connections in the write operation. This attribute is valid only for connections created with the CNVCreateWriter function. The default value is 1 (TRUE), which results in better performance in most cases. Flushing on write may cause lower throughput in some high bandwidth conditions, in which case you can set this attribute to 0 (FALSE). In high bandwidth conditions, National Instruments recommends using the CNVBufferedWriter connection. |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5.1 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cnvmostrecentdataattribute.html language=enus -->
## TOPIC 00098: CNVMostRecentDataAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cnvmostrecentdataattribute.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cnvmostrecentdataattribute.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVMostRecentDataAttribute

| Data Type: | CNVData |
| --- | --- |
| Description: | This attribute indicates the most recent client-side value of the network variable. This attribute is valid only for subscriber connections. |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.1 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cnvvariableprototypeattribute.html language=enus -->
## TOPIC 00099: CNVVariablePrototypeAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cnvvariableprototypeattribute.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cnvvariableprototypeattribute.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVVariablePrototypeAttribute

| Data Type: | CNVData |
| --- | --- |
| Description: | This attribute specifies the prototypical type of data to store in the network variable. A NULL CNVData value indicates that the variable does not have a prototype; that is, the variable is of variant type and can hold any type of data. |
| LabWindows/CVICompatibility: | LabWindows/CVI 2009 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/combiningmultvarsintotsv.htm language=enus -->
## TOPIC 00100: Combining Multiple Variables into a Single Thread Safe Variable

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/combiningmultvarsintotsv.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/combiningmultvarsintotsv.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Combining Multiple Variables into a Single Thread Safe Variable

If you have two or more variables that are somehow related, you must prevent two threads from modifying the values at the same time. An example of this is an array and a count of the number of valid values in the array. If one thread removes values from the array, it must update both the array and the count before allowing another thread to access the data. Although you could use a single LabWindows/CVI Utility Library thread lock to protect access to both of these values, a safer approach is to define a structure and then use that structure as a thread safe variable. The following example shows how you can use a thread safe variable in this manner to safely add a value to the array.

typedef struct {

int data[500]; 

int count;

} BufType;

DefineThreadSafeVar(BufType, SafeBuf);

void StoreValue(int val) 

{

BufType *safeBufPtr; 

safeBufPtr = GetPointerToSafeBuf(); 

safeBufPtr->data[safeBufPtr->count] = val; 

safeBufPtr->count++; 

ReleasePointerToSafeBuf();

}

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/complex_numbers_class_advanlys.html language=enus -->
## TOPIC 00101: Complex Numbers Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/complex_numbers_class_advanlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/complex_numbers_class_advanlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Complex Numbers Class Help

This class contains functions that perform arithmetic operations on complex numbers.

Complex numbers are represented as follows:

x = xReal + *j**xImag

where *j* is sqrt(–1).

All of these functions allow the complex operations to be done in place.

**Library**: [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/complex_operations_class_advanlys.html language=enus -->
## TOPIC 00102: Complex Operations Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/complex_operations_class_advanlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/complex_operations_class_advanlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Complex Operations Class Help

This class contains functions that perform arithmetic operations on complex numbers and 1D complex arrays.

**Library**: [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/complex_operations_class_reganlys.html language=enus -->
## TOPIC 00103: Complex Operations Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/complex_operations_class_reganlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/complex_operations_class_reganlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Complex Operations Class Help

This class contains functions that perform arithmetic operations on complex numbers and 1D complex arrays.

**Library**: [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/complex_windows_class_advanlys.html language=enus -->
## TOPIC 00104: Windows Class Help

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/complex_windows_class_advanlys.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/complex_windows_class_advanlys.html
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Windows Class Help

This class contains functions that apply windows to an input signal. You can use these functions to reduce the truncation effect normally encountered in data acquisition.

**Library**: [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvi_mbsbtype.htm language=enus -->
## TOPIC 00105: _mbsbtype

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvi_mbsbtype.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvi_mbsbtype.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### _mbsbtype

int _mbsbtype (const char context[], size_t byteOffset);

#### Purpose

Determines the type of the byte in the context string at the given offset.

Refer to the [Programming for Multibyte Character Sets in LabWindows/CVI](../../cvi/programmerref/programmingmultibytechars.htm) topic for information about working with multibyte character sets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| context | const char [] | Contains the context string. |
| byteOffset | size_t | Specifies the offset of the byte in the context string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| byteType | int | Contains the type of the tested byte. The return values are as follows: _MBC_SINGLE—A single byte character _MBC_LEAD—The lead byte of a multibyte character _MBC_TRAIL—The trail byte of a multibyte character _MBC_ILLEGAL—An illegal byte value or an invalid input parameter |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvi_mbscat.htm language=enus -->
## TOPIC 00106: _mbscat

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvi_mbscat.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvi_mbscat.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### _mbscat

char *_mbscat (char targetString[], const char stringToAppend[]);

#### Purpose

Appends a copy of a source string to the end of a target string.
The initial character of the string to append overwrites the NUL byte at the
end of the target string. If copying takes place between objects that
overlap, the behavior is undefined.

Refer to the [Programming for Multibyte Character Sets in LabWindows/CVI](../../cvi/programmerref/programmingmultibytechars.htm) topic for information about working with multibyte character sets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToAppend | const char [] | Contains a pointer to the NUL-terminated string that is appended to the end of targetString. The initial character of this string overwrites the NUL byte at the end of the target string. |
| Output |  |  |
| Name | Type | Description |
| targetString | char [] | Contains the target string to which string_toAppend is appended. The initial character of string_toAppend overwrites the NUL byte at the end of the string specified in this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnedTargetString | char * | Contains a pointer to the modified target string. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvi_mbschr.htm language=enus -->
## TOPIC 00107: _mbschr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvi_mbschr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvi_mbschr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### _mbschr

char *_mbschr (const char stringToSearch[], int charToFind);

#### Purpose

Locates the first occurrence of the specified character in a string. The terminating ASCII NUL byte is considered to
be part of the string.

Refer to the [Programming for Multibyte Character Sets in LabWindows/CVI](../../cvi/programmerref/programmingmultibytechars.htm) topic for information about working with multibyte character sets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToSearch | const char [] | Contains a pointer to the null-terminated string which is searched to locate the specified character. |
| charToFind | int | Contains the character for which to search in the specified string. The input to this parameter can be any valid character, including multibyte characters. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| matchedChar | char * | Contains a pointer to the located character or a NULL pointer if the character does not occur in the string. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvi_mbscmp.htm language=enus -->
## TOPIC 00108: _mbscmp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvi_mbscmp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvi_mbscmp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### _mbscmp

int _mbscmp (const char string1[], const char string2[]);

#### Purpose

Compares two NUL-terminated strings. The comparison is
based upon the value of the characters in the strings as determined by
the system's language settings. The comparison is case-sensitive.

Refer to the [Programming for Multibyte Character Sets in LabWindows/CVI](../../cvi/programmerref/programmingmultibytechars.htm) topic for information about working with multibyte character sets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| string1 | const char [] | Contains a pointer to the string that is compared to string2. |
| string2 | const char [] | Contains a pointer to the string that is compared to string1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| comparisonResult | int | Contains the result of the comparison between the two specified strings. The comparison is based on the value of the characters in the two strings as determined by the system's language settings. The comparison is case-sensitive. The following explains the possible return values: Result Description Positive integer string1 is greater than string2 Zero string1 is equal to string2 Negative integer string1 is less than string2 |
| Result | Description |  |
| Positive integer | string1 is greater than string2 |  |
| Zero | string1 is equal to string2 |  |
| Negative integer | string1 is less than string2 |  |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvi_mbscpy.htm language=enus -->
## TOPIC 00109: _mbscpy

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvi_mbscpy.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvi_mbscpy.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### _mbscpy

char *_mbscpy (char targetString[], const char sourceString[]);

#### Purpose

Copies a source string, including the terminating ASCII
NUL byte, into a target string. If copying takes place between objects
that overlap, the behavior is undefined.

Refer to the [Programming for Multibyte Character Sets in LabWindows/CVI](../../cvi/programmerref/programmingmultibytechars.htm) topic for information about working with multibyte character sets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceString | const char [] | Contains a pointer to the NUL-terminated source string that is copied into the target string. |
| Output |  |  |
| Name | Type | Description |
| targetString | char [] | Contains the target string to which the source string is copied, including the terminating ASCII NUL byte. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnedTargetString | char * | Contains a pointer to the modified target string. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvi_mbscspn.htm language=enus -->
## TOPIC 00110: _mbscspn

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvi_mbscspn.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvi_mbscspn.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### _mbscspn

size_t _mbscspn (const char stringToSearch[], const char characterSet[]);

#### Purpose

Locates the position of the first character in a string
that is from a specified set of characters. The return value corresponds to
the length in bytes of the initial segment of the string that contains no
character from the specified set.

Refer to the [Programming for Multibyte Character Sets in LabWindows/CVI](../../cvi/programmerref/programmingmultibytechars.htm) topic for information about working with multibyte character sets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToSearch | const char [] | Contains a pointer to the string that is searched to locate any of the characters specified in characterSet. |
| characterSet | const char [] | Contains a pointer to the character set containing the characters that are searched for in the specified string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| matchedCharIndex | size_t | Contains the index value of the string corresponding to the first matched character from the character set. If no matching characters are found, the function returns the index of the terminating ASCII NUL byte. This value also corresponds to the length in bytes of the initial segment of the string containing no character from the character set. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvi_mbsdec.htm language=enus -->
## TOPIC 00111: _mbsdec

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvi_mbsdec.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvi_mbsdec.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### _mbsdec

char *_mbsdec (const char string[], char *pointerToCurrentCharacter);

#### Purpose

Moves a character pointer to the previous character in a
[multibyte character string](../../cvi/programmerref/programmingmultibytechars.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| string | const char [] | Contains the string into which the current character pointer is pointing. |
| pointerToCurrentCharacter | char * | Contains a pointer to a character in the input string. The pointer is assumed to point to the beginning of a character, not to a trail byte. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| pointerToPreviousCharacter | char * | Contains a pointer to the character directly in front of the current character or NULL if this character lies in front of the input string. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_loadobjectfromfilebyprogid.htm language=enus -->
## TOPIC 00112: CA_LoadObjectFromFileByProgId

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_loadobjectfromfilebyprogid.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_loadobjectfromfilebyprogid.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_LoadObjectFromFileByProgId

HRESULT CA_LoadObjectFromFileByProgId (const char *filename, const char *progId, const char *serverMachineName, CAObjHandle *objectHandle);

#### Purpose

|  | Note This function has been superseded by CA_LoadObjectFromFileByProgIdEx. The new function takes additional parameters for interface id, support multithreading, locale, and reserved. Calling this function is equivalent to passing the following values for those parameters. Interface Id IID_IDispatch Support Multithreading 0 Locale LOCALE_NEUTRAL Reserved 0 |
| --- | --- |
| Interface Id | IID_IDispatch |
| Support Multithreading | 0 |
| Locale | LOCALE_NEUTRAL |
| Reserved | 0 |

Creates an ActiveX server object and initializes it from a file. The **progID** parameter identifies the ActiveX server object. **filename** specifies the file that contains the initial data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | const char * | Pathname of file that contains the initial data for the object. |
| progId | const char * | Prog ID of the ActiveX server object; located in the server documentation. |
| serverMachineName | const char * | Name or IP address of the computer on which you want to run the ActiveX server. serverMachineName can be either a UNC name ("\\\\server") or a DNS name ("home.server.com"). If you pass NULL for this parameter and there is an ActivateAtStorage registry entry for this server, the server runs on the machine on which the file specified by the filename parameter resides. If you pass NULL for this parameter and there is no ActivateAtStorage registry entry for this server, the server runs on the same machine as your program. |
| Output |  |  |
| Name | Type | Description |
| objectHandle | CAObjHandle | Handle to the requested ActiveX object. You can pass objHandle to other functions in this library to call methods of the ActiveX object or to get and set properties of the ActiveX object. When you no longer need objHandle, discard it by calling CA_DiscardObjHandle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_propertysetbyref.htm language=enus -->
## TOPIC 00113: CA_PropertySetByRef

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_propertysetbyref.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_propertysetbyref.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_PropertySetByRef

HRESULT CA_PropertySetByRef (CAObjHandle objectHandle, ERRORINFO *errorInfo, int propertyID, unsigned int propertyType, ...);

#### Purpose

|  | Note This function has been superseded by CA_PropertySetByRefEx. The new function takes an additional parameter for interface id. Calling this function is equivalent to passing 0 for the interfaceId parameter. |
| --- | --- |

Sets the value of the property of an ActiveX server object. Unlike [CA_PropertySet](../../cvi/libref/cvica_propertyset.htm), CA_PropertySetByRef accepts a pointer to the property value. Unlike [CA_PropertySetByRefV](../../cvi/libref/cvica_propertysetbyrefv.htm), it accepts the pointer as a simple parameter.

|  | Note This function is used by the functions generated by the ActiveX Controller Wizard. It is not intended to be used directly. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | An ActiveX object handle returned in an output parameter of an ActiveX server's function or a function in the Creating ActiveX Objects class in this library. |
| propertyID | int | ID of the ActiveX server property; located in the server type library. |
| propertyType | unsigned int | Data type of the property. propertyType can be any of the fundamental data types for variants, safe arrays, and properties except CAVT_NULL or CAVT_EMPTY. You should add the CAVT_BYREFI modifier, but the ActiveX Library adds it for you if you forget. |
| pointerToPropertyValue | ... | Pointer to the value to which you want to set the property. Pass a value whose type is a pointer to the type specified in the propertyType parameter. |
| Output |  |  |
| Name | Type | Description |
| errorInfo | ERRORINFO | When the ActiveX server method invoked by this function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The descriptive information includes the error code, source, and description. The information also can include a help file and help file context. When the ActiveX server method invoked by this function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument can be stored in the errorParamPos member of this parameter. This parameter can be NULL. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Function failure is indicated by a negative error code. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. If the error code is DISP_E_EXCEPTION (0x80020009 or -2147352567), then the errorInfo parameter contains additional error information. You can use CA_DisplayErrorInfo to display the error information. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_propertysetbyrefvex.htm language=enus -->
## TOPIC 00114: CA_PropertySetByRefVEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_propertysetbyrefvex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_propertysetbyrefvex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_PropertySetByRefVEx

HRESULT CA_PropertySetByRefVEx (CAObjHandle objectHandle, ERRORINFO *errorInfo, const IID *interfaceId, int propertyID, unsigned int propertyType, va_list ptrToPropertyValue_va_list);

#### Purpose

|  | Note This function is used by the functions generated by the ActiveX Controller Instrument Driver Wizard. It is not intended to be used directly. |
| --- | --- |

Sets the value of a Property. Unlike [CA_PropertySetByRefEx](../../cvi/libref/cvica_propertysetbyrefex.htm), you pass the pointer to the value as the only element in a variable argument list (va_list).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | An ActiveX object handle returned in an output parameter of an ActiveX server function or a function in the Creating ActiveX Objects class in this library. |
| interfaceId | const IID * | The interface id specifying the type of interface pointer to be used for the property access. You must pass the UUID of an interface implemented by the object passed in the objectHandle parameter or zero to indicate the current interface id that is stored in that object handle. |
| propertyID | int | The Id of the Property. This Id can be obtained from the object's type library. |
| propertyType | unsigned int | The type of the property specified in the propertyId parameter. You can specify any of the data types for variants and safe arrays except CAVT_NULL. |
| ptrToPropertyValue_va_list | va_list | A variable argument list initialized by the va_start macro. This list must contain a single value whose type is a pointer to the type specified in the propertyType parameter. |
| Output |  |  |
| Name | Type | Description |
| errorInfo | ERRORINFO | When the ActiveX server method invoked by this function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The descriptive information includes the error code, source, and description. The information also can include a help file and help file context. When the ActiveX server method invoked by this function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument can be stored in the errorParamPos member of this parameter. This parameter can be NULL. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_safearrayto2darraybuf.htm language=enus -->
## TOPIC 00115: CA_SafeArrayTo2DArrayBuf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_safearrayto2darraybuf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_safearrayto2darraybuf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_SafeArrayTo2DArrayBuf

HRESULT CA_SafeArrayTo2DArrayBuf (LPSAFEARRAY *safeArray, unsigned int arrayType, void *arrayBuffer, size_t bufferSizeInBytes, size_t *sizeOf1stDimension, size_t *sizeOf2ndDimension);

#### Purpose

|  | Note This function has been superseded by CA_SafeArrayTo2DArrayBufEx. The new function takes an additional parameter for options. Calling CA_SafeArrayTo2DArrayBuf is equivalent to passing 0 for the options parameter with CA_SafeArrayTo2DArrayBufEx. |
| --- | --- |

Converts a 2D safe array into a C-style array you pass as a buffer.

Upon success, CA_SafeArrayTo2DArrayBuf frees the safe array and its contents and sets the safe array pointer to NULL.

CA_SafeArrayTo2DArrayBuf returns an error if the buffer is not big enough to hold the array.

##### Example Code

The following code shows you how to use CA_SafeArrayTo2DArrayBuf:

double dblArray[1024]; 

 LPSAFEARRAY safeArray; 

 unsigned numElemsDim1, numElemsDim2; 

 int index1, index2; 

 /* Call an ActiveX function that returns a safe array. */ 

 . 

 . 

 . 

 /* Convert the safe array into a C-style array. */

CA_SafeArrayTo2DArrayBuf (&safeArray, CAVT_DOUBLE, dblArray, sizeof(dblArray), &numElemsDim1, &numElemsDim2);

for (index1 = 0; index1 < numElemsDim1; index1++)

for (index2 = 0; index2 < numElemsDim2; index2++)

{ 

 double d; 

 d = CA_Get2DArrayElement (dblArray, numElemsDim1, numElemsDim2, index1, index2, double); 

 printf ("%f", d); 

 }

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayType | unsigned int | Data type of the array that CA_SafeArrayTo2DArrayBuf creates from the safe array. arrayType must be the same as the type of the safe array except for the following cases: Creating a C-style array that contains char* elements from a BSTR safe array. Creating a C-style array that contains CAObjHandle elements from an LPDISPATCH safe array. arrayType can be any of the fundamental data types for variants, safe arrays, and properties except CAVT_EMPTY or CAVT_NULL. CA_SafeArrayTo2DArrayBuf ignores the CAVT_ARRAY modifier. |
| bufferSizeInBytes | size_t | Number of bytes in the arrayBuffer parameter. |
| Output |  |  |
| Name | Type | Description |
| safeArray | LPSAFEARRAY | 2D safe array. Pass the address of the safe array pointer. CA_SafeArrayTo2DArrayBuf frees the safe array and its contents and sets the safe array pointer to NULL. |
| arrayBuffer | void * | Buffer to receive the C-style array elements. The type of the array must be the same as arrayType. To access the elements of array, use the CA_Get2DArrayElement macro, which is declared in cviauto.h. If the C-style array contains elements of one of the data types in the following table, use the corresponding function to free each element when you no longer need it. Data Type Function to Free Each Element char * CA_FreeMemory CAObjHandle CA_DiscardObjHandle BSTR CA_FreeBSTR LPUNKNOWN array[i]->lpVtbl->Release() LPDISPATCH array[i]->lpVtbl->Release() VARIANT CA_VariantClear Note CAObjHandles that this function creates do not support multithreading and use LOCALE_NEUTRAL. To use different values for multithreading support and locale you can call CA_SetSupportForMultithreading and CA_SetLocale to specify the desired values for each CAObjHandle. |
| Data Type | Function to Free Each Element |  |
| char * | CA_FreeMemory |  |
| CAObjHandle | CA_DiscardObjHandle |  |
| BSTR | CA_FreeBSTR |  |
| LPUNKNOWN | array[i]->lpVtbl->Release() |  |
| LPDISPATCH | array[i]->lpVtbl->Release() |  |
| VARIANT | CA_VariantClear |  |
|  | Note CAObjHandles that this function creates do not support multithreading and use LOCALE_NEUTRAL. To use different values for multithreading support and locale you can call CA_SetSupportForMultithreading and CA_SetLocale to specify the desired values for each CAObjHandle. |  |
| sizeOf1stDimension | size_t | Number of elements in the first dimension of array. You can pass NULL for this parameter. |
| sizeOf2ndDimension | size_t | Number of elements in the second dimension of array. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_safearrayto2darraybufex.htm language=enus -->
## TOPIC 00116: CA_SafeArrayTo2DArrayBufEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_safearrayto2darraybufex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_safearrayto2darraybufex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_SafeArrayTo2DArrayBufEx

HRESULT CA_SafeArrayTo2DArrayBufEx (LPSAFEARRAY *safeArray, unsigned int arrayType, unsigned int options, void *arrayBuffer, size_t bufferSizeInBytes, size_t *sizeOf1stDimension, size_t *sizeOf2ndDimension);

#### Purpose

Converts a 2D safe array into a C-style array that you pass as a buffer.

This function frees the safe array and its contents and sets the safe array pointer to NULL unless you pass the CVIAUTO_RETAIN_SAFEARRAY flag in the **options** parameter.

CA_SafeArrayTo2DArrayBufEx returns an error if the buffer is not big enough to hold the array.

##### Example Code

double dblArray[1024]; 

 LPSAFEARRAY safeArray; 

 unsigned dim1Size, dim2Size; 

 int index1, index2; 

 /* Call an ActiveX function that */ 

 /* returns Safe Array. */ 

 ... 

 /* Convert the Safe Array into a C-style array */

CA_SafeArrayTo2DArrayBufEx(&safeArray, CAVT_DOUBLE, 0, dblArray, sizeof(dblArray), &dim1Size, &dim2Size);

for (index1 = 0; index1 < dim1Size; index1++)

for (index2 = 0; index2 < dim2Size; index2++)

{ 

 double d; 

 d = CA_Get2DArrayElement(dblArray, dim1Size, dim2Size,

index1, index2, double); 

 printf("%f", d); 

 }

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayType | unsigned int | The type of array to be created from the safe array. The type of the C-style array must be the same as the type of the safe array except for the following cases. Creating a char* array from a BSTR SAFEARRAY. Creating a CAObjHandle array from an LPDISPATCH SAFEARRAY. If you do not know the type of the safe array, you can call CA_VariantGetType and pass its return value as the type. arrayType can contain any of the fundamental data types for variants, safe arrays, and properties except for CAVT_EMPTY or CAVT_NULL. The CAVT_ARRAY flag is ignored by this parameter. |
| options | unsigned int | The option constants to modify the behavior of the safe array conversion function. Pass 0 for the default behavior. Pass CVIAUTO_RETAIN_SAFEARRAY to retain the safe array and its contents. The default behavior is to free the safe array and its contents on function success and set the safe array pointer to NULL. |
| bufferSizeInBytes | size_t | The size, in bytes, of arrayBuffer. |
| Output |  |  |
| Name | Type | Description |
| safeArray | LPSAFEARRAY | A 2D Safe Array. On success, this function frees the safe array and its contents and sets the safe array pointer to NULL unless you pass the CVIAUTO_RETAIN_SAFEARRAY flag in the options parameter. |
| arrayBuffer | void * | The buffer in which the array elements are stored. You can use the CA_Get2DArrayElement macro to access elements of this array. If the array contains elements of one of the data types in the following table, use the corresponding function to free each element when you no longer need it. Data Type Function to Free Each Element char * CA_FreeMemory CAObjHandle CA_DiscardObjHandle BSTR CA_FreeBSTR LPUNKNOWN array[i]->lpVtbl->Release() LPDISPATCH array[i]->lpVtbl->Release() VARIANT CA_VariantClear Note CAObjHandles created by this function do not support multithreading and use LOCALE_NEUTRAL. To use different values for multithreading support and locale you can call CA_SetSupportForMultithreading and CA_SetLocale to specify the desired values for each CAObjHandle. |
| Data Type | Function to Free Each Element |  |
| char * | CA_FreeMemory |  |
| CAObjHandle | CA_DiscardObjHandle |  |
| BSTR | CA_FreeBSTR |  |
| LPUNKNOWN | array[i]->lpVtbl->Release() |  |
| LPDISPATCH | array[i]->lpVtbl->Release() |  |
| VARIANT | CA_VariantClear |  |
|  | Note CAObjHandles created by this function do not support multithreading and use LOCALE_NEUTRAL. |  |
| sizeOf1stDimension | size_t | The number of elements in the first dimension of the array in arrayBuffer. You can pass NULL for this parameter. |
| sizeOf2ndDimension | size_t | The number of elements in the second dimension of the array in arrayBuffer. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_serveraddref.htm language=enus -->
## TOPIC 00117: CA_ServerAddRef

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_serveraddref.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_serveraddref.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_ServerAddRef

unsigned int CA_ServerAddRef (IUnknown *thisInterfacePtr);

#### Purpose

Implementation of the IUnknown::AddRef method used in the ActiveX servers generated by the ActiveX Server Wizard. This function controls the lifetime of a [COM object](../../cvi/libref/cviactivex_com_model.htm). CA_ServerAddRef increments the internal reference count of the object.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| thisInterfacePtr | IUnknown * | The IUnknown interface pointer of your ActiveX object. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| referenceCount | unsigned int | The value of the new reference count on the object. Use this information for diagnostic/testing purposes only, because in certain situations the value might be unstable. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_servergetobjhandlefromiface.htm language=enus -->
## TOPIC 00118: CA_ServerGetObjHandleFromIface

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_servergetobjhandlefromiface.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_servergetobjhandlefromiface.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_ServerGetObjHandleFromIface

HRESULT CA_ServerGetObjHandleFromIface (void *thisInterfacePtr, CAServerObjHandle *serverObjectHandle);

#### Purpose

Gets the handle of the ActiveX object whose interface pointer is passed in the first parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| thisInterfacePtr | void * | An interface pointer of your ActiveX object. |
| Output |  |  |
| Name | Type | Description |
| serverObjectHandle | CAServerObjHandle | The handle to the ActiveX object whose interface pointer was passed in the thisInterfacePtr parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Function failure is indicated by a negative error code. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by the COM runtime and passed on to you by the ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. The error codes defined in <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h are too numerous to display here. These error codes can be returned to your ActiveX clients. |
|  | Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. |  |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_servergettypeinfo.htm language=enus -->
## TOPIC 00119: CA_ServerGetTypeInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_servergettypeinfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_servergettypeinfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_ServerGetTypeInfo

HRESULT CA_ServerGetTypeInfo (IDispatch *thisInterfacePtr, unsigned long typeInfoIndex, LCID locale, ITypeInfo **typeInfoPtr);

#### Purpose

Implementation of the IDispatch::GetTypeInfo method used in the ActiveX
 servers generated by the ActiveX Server Wizard.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| thisInterfacePtr | IDispatch * | The IDispatch interface pointer of your ActiveX object. |
| typeInfoIndex | unsigned long | The type information to return. Pass 0 to retrieve type information for the IDispatch implementation. |
| locale | LCID | The locale identifier for the type information. |
| Output |  |  |
| Name | Type | Description |
| typeInfoPtr | ITypeInfo * | The ITypeInfo interface pointer for the requested type information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Function failure is indicated by a negative error code. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by the COM runtime and passed on to you by the ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. The error codes defined in <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h are too numerous to display here. These error codes can be returned to your ActiveX clients. |
|  | Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. |  |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_servergettypeinfocount.htm language=enus -->
## TOPIC 00120: CA_ServerGetTypeInfoCount

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_servergettypeinfocount.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_servergettypeinfocount.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_ServerGetTypeInfoCount

HRESULT CA_ServerGetTypeInfoCount (IDispatch *thisInterfacePtr, unsigned long *count);

#### Purpose

Implementation of the IDispatch::GetTypeInfoCount method used in the
 ActiveX servers generated by the ActiveX Server Wizard.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| thisInterfacePtr | IDispatch * | The IDispatch interface pointer of your ActiveX object. |
| Output |  |  |
| Name | Type | Description |
| count | unsigned long | If the object has type information interfaces, then the value is 1, or else it is 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Function failure is indicated by a negative error code. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by the COM runtime and passed on to you by the ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. The error codes defined in <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h are too numerous to display here. These error codes can be returned to your ActiveX clients. |
|  | Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. |  |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_serverinvoke.htm language=enus -->
## TOPIC 00121: CA_ServerInvoke

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_serverinvoke.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_serverinvoke.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_ServerInvoke

HRESULT CA_ServerInvoke (IDispatch *thisInterfacePtr, int memberId, const IID *interfaceId, LCID locale, unsigned short flags, DISPPARAMS *dispParams, VARIANT *result, EXCEPINFO *exceptionInfo, unsigned int *argumentErrorIndex);

#### Purpose

Implementation of the IDispatch::Invoke method used in the ActiveX
 servers generated by the ActiveX Server Wizard.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| thisInterfacePtr | IDispatch * | The IDispatch interface pointer of your ActiveX object. |
| memberId | int | Id of the member to call Invoke on. |
| interfaceId | const IID * | Reserved for future use. Must be IID_NULL. |
| locale | LCID | The locale identifier for the type information. |
| flags | unsigned short | Flags describing the context of the Invoke call. You can use the following flags: DISPATCH_METHOD: The member is invoked as a method. If a property has the same name, both this and the DISPATCH_PROPERTYGET flag can be set. DISPATCH_PROPERTYGET: The member is retrieved as a property or data member. DISPATCH_PROPERTYPUT: The member is changed as a property or data member. DISPATCH_PROPERTYPUTREF: The member is changed by a reference assignment, rather than a value assignment. This flag is valid only when the property accepts a reference to an object. |
| dispParams | DISPPARAMS * | Pointer to a structure containing an array of arguments, an array of argument DISPIDs for named arguments, and counts for the number of elements in the arrays. |
| Output |  |  |
| Name | Type | Description |
| result | VARIANT | The result of the Invoke call, or NULL if the caller expects no result. This parameter is ignored if you specify DISPATCH_PROPERTYPUT or DISPATCH_PROPERTYPUTREF. |
| exceptionInfo | EXCEPINFO | The exception information for the Invoke call. This structure is filled in if DISP_E_EXCEPTION is returned. Pass NULL if this information is not required. |
| argumentErrorIndex | unsigned int | The index of the first argument that has an error. Arguments are stored in Disp_Params->rgvarg in reverse order, so the first argument is the one with the highest index in the array (here, Disp_Params is the variable passed in the dispParams parameter). Pass NULL if you do not want this information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Function failure is indicated by a negative error code. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by the COM runtime and passed on to you by the ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. The error codes defined in <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h are too numerous to display here. These error codes can be returned to your ActiveX clients. |
|  | Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. |  |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_serverlockactiveobject.htm language=enus -->
## TOPIC 00122: CA_ServerLockActiveObject

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_serverlockactiveobject.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_serverlockactiveobject.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_ServerLockActiveObject

HRESULT CA_ServerLockActiveObject (CAServerObjHandle serverObjectHandle);

#### Purpose

Locks the ActiveX object whose handle is passed in the first parameter.

This action basically results in an additional reference to the ActiveX object,
apart from the references held by the ActiveX clients. The effect is that the object does not get destroyed even when all the client references to the object are released.

This function is meant to be called when an ActiveX object that has a user interface is made visible on the screen.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| serverObjectHandle | CAServerObjHandle | The handle to an ActiveX object in your ActiveX server. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Function failure is indicated by a negative error code. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by the COM runtime and passed on to you by the ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. The error codes defined in <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h are too numerous to display here. These error codes can be returned to your ActiveX clients. |
|  | Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. |  |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_serverqueryinterface.htm language=enus -->
## TOPIC 00123: CA_ServerQueryInterface

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_serverqueryinterface.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_serverqueryinterface.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_ServerQueryInterface

HRESULT CA_ServerQueryInterface (IUnknown *thisInterfacePtr, const IID *interfaceId, void *newInterfacePtr);

#### Purpose

Implementation of the IUnknown::QueryInterface method used in the ActiveX servers generated by the ActiveX Server Wizard. This function queries a [COM object](../../cvi/libref/cviactivex_com_model.htm) as to whether it implements a specific interface.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| thisInterfacePtr | IUnknown * | The IUnknown interface pointer of your ActiveX object. |
| interfaceId | const IID * | Interface id for the interface requested from the object. |
| Output |  |  |
| Name | Type | Description |
| newInterfacePtr | void * | The interface pointer (of the type passed in the Interface Id parameter) obtained from your ActiveX object. Pass the address of an interface pointer variable of the required interface type. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Function failure is indicated by a negative error code. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by the COM runtime and passed on to you by the ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. The error codes defined in <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h are too numerous to display here. These error codes can be returned to your ActiveX clients. |
|  | Note You should not return the ActiveX Library error codes from your ActiveX server to your ActiveX clients, unless you document them in your server documentation. An acceptable compromise in this case is to return E_UNEXPECTED to the clients. |  |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_variantgetdispatchptr.htm language=enus -->
## TOPIC 00124: CA_VariantGetDispatchPtr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_variantgetdispatchptr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_variantgetdispatchptr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantGetDispatchPtr

HRESULT CA_VariantGetDispatchPtr (const VARIANT *variant, LPDISPATCH **value);

#### Purpose

Copies the value in a variant into a variable that is a pointer to the LPDISPATCH type. An LPDISPATCH value is a dispatch pointer for an ActiveX object interface.

CA_VariantGetDispatchPtr returns an error if the variant does not contain a pointer to an LPDISPATCH value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to a variant that contains an LPDISPATCH pointer. |
| Output |  |  |
| Name | Type | Description |
| value | LPDISPATCH * | LPDISPATCH pointer that CA_VariantGetDispatchPtr copies from the variant. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_variantgetfloatptr.htm language=enus -->
## TOPIC 00125: CA_VariantGetFloatPtr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_variantgetfloatptr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_variantgetfloatptr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantGetFloatPtr

HRESULT CA_VariantGetFloatPtr (const VARIANT *variant, float **value);

#### Purpose

Copies the value in a variant into a single-precision, floating-point pointer variable.

CA_VariantGetFloatPtr returns an error if the variant does not contain a pointer to a single-precision value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to a variant that contains a single-precision pointer. |
| Output |  |  |
| Name | Type | Description |
| value | float * | Single-precision pointer that CA_VariantGetFloatPtr copies from the variant. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_variantgetint.htm language=enus -->
## TOPIC 00126: CA_VariantGetInt

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_variantgetint.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_variantgetint.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantGetInt

HRESULT CA_VariantGetInt (const VARIANT *variant, int *value);

#### Purpose

Copies the value in a variant into an integer variable.

CA_VariantGetInt returns an error if the variant does not contain an integer value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to a variant that contains an integer value. |
| Output |  |  |
| Name | Type | Description |
| value | int | Integer value CA_VariantGetInt copies from the variant. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_variantgetobjhandle.htm language=enus -->
## TOPIC 00127: CA_VariantGetObjHandle

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_variantgetobjhandle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_variantgetobjhandle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantGetObjHandle

HRESULT CA_VariantGetObjHandle (VARIANT *variant, CAObjHandle *value);

#### Purpose

Converts the LPDISPATCH value in a variant into a CAObjHandle.

On success, CA_VariantGetObjHandle marks the variant parameter as empty.

CA_VariantGetObjHandle returns an error if the variant does not contain an LDISPATCH value.

When you no longer need **objHandle**, call [CA_DiscardObjHandle](../../cvi/libref/cvica_discardobjhandle.htm) to free it.

|  | Note CAObjHandles created by this function do not support multithreading and use LOCALE_NEUTRAL. To use different values for multithreading support and locale you can use either of the following approaches: After calling this function, call CA_SetSupportForMultithreading and CA_SetLocale to specify the desired values. Call CA_VariantGetDispatch to get a dispatch pointer from the variant, and pass this pointer to CA_CreateObjHandleFromInterface, which has parameters to specify multithreading support and locale. |
| --- | --- |

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | VARIANT | Pointer to a variant that contains an LPDISPATCH value. CA_VariantGetObjHandle marks the variant as empty on success. |
| value | CAObjHandle | Object handle that CA_VariantGetObjHandle converts from the LPDISPATCH value in the variant. When you no longer need the CAObjHandle, call CA_DiscardObjHandle to free it. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_variantgetsafearray.htm language=enus -->
## TOPIC 00128: CA_VariantGetSafeArray

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_variantgetsafearray.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_variantgetsafearray.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantGetSafeArray

HRESULT CA_VariantGetSafeArray (VARIANT *variant, unsigned int arrayType, LPSAFEARRAY *value);

#### Purpose

Copies the safe array in a variant into a safe array variable.

On success, CA_VariantGetSafeArray marks the variant parameter as empty.

CA_VariantGetSafeArray returns an error if the variant does not contain a safe array.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayType | unsigned int | Type of the safe array. arrayType can contain any of the fundamental data types for variants, safe arrays, and properties except for CAVT_EMPTY, CAVT_NULL, CAVT_CSTRING, and CAVT_OBJHANDLE. If you do not know the type of the safe array, call CA_VariantGetType and pass its return value as the arrayType. CA_VariantGetSafeArray ignores the CAVT_ARRAY modifier. |
| Output |  |  |
| Name | Type | Description |
| variant | VARIANT | Pointer to a variant that contains a safe array. CA_VariantGetSafeArray marks the variant as empty on success. |
| value | LPSAFEARRAY | Safe array that CA_VariantGetSafeArray copies from the variant. Use CA_SafeArrayDestroy to free the returned safe array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_variantgetuintptr.htm language=enus -->
## TOPIC 00129: CA_VariantGetUIntPtr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_variantgetuintptr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_variantgetuintptr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantGetUIntPtr

HRESULT CA_VariantGetUIntPtr (const VARIANT *variant, long **value);

#### Purpose

Copies the value in a variant into an unsigned integer pointer variable.

CA_VariantGetUIntPtr returns an error if the variant does not contain a pointer to an unsigned integer value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to a variant that contains an unsigned integer pointer. |
| Output |  |  |
| Name | Type | Description |
| value | long * | Unsigned integer pointer that CA_VariantGetUIntPtr copies from the variant. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. Negative error codes indicate function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. The LabWindows/CVI ActiveX Library explicitly returns error codes. Other error codes in winerror.h are generated by ActiveX servers and passed on to you by the LabWindows/CVI ActiveX Library. You can use CA_GetAutomationErrorString to get the description of an error code or CA_DisplayErrorInfo to display the description of the error code. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthasbstr.htm language=enus -->
## TOPIC 00130: CA_VariantHasBSTR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthasbstr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthasbstr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasBSTR

HRESULT CA_VariantHasBSTR (const VARIANT *variant);

#### Purpose

Determines whether a variant contains a BSTR value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if the variant contains a BSTR value. 0 if variant does not contain a BSTR value. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthascstring.htm language=enus -->
## TOPIC 00131: CA_VariantHasCString

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthascstring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthascstring.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasCString

HRESULT CA_VariantHasCString (const VARIANT *variant);

#### Purpose

Determines whether a variant contains a value that can be converted into a C-style string. Variants do not contain C-style strings, but you can convert the strings they contain to C-style strings.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if the variant contains a string value. 0 if variant does not contain a string value. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthasdate.htm language=enus -->
## TOPIC 00132: CA_VariantHasDate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthasdate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthasdate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasDate

HRESULT CA_VariantHasDate (const VARIANT *variant);

#### Purpose

Determines whether a variant contains a DATE value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if variant contains a DATE value. 0 if variant does not contain a DATE value. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthasdispatch.htm language=enus -->
## TOPIC 00133: CA_VariantHasDispatch

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthasdispatch.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthasdispatch.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasDispatch

HRESULT CA_VariantHasDispatch (const VARIANT *variant);

#### Purpose

Determines whether a variant contains an IDispatch interface.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if variant contains an IDispatch interface. 0 if variant does not contain an IDispatch interface. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthasdouble.htm language=enus -->
## TOPIC 00134: CA_VariantHasDouble

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthasdouble.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthasdouble.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasDouble

HRESULT CA_VariantHasDouble (const VARIANT *variant);

#### Purpose

Determines whether a variant contains a double-precision value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if variant contains a double-precision value. 0 if variant does not contain a double-precision value. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthaserror.htm language=enus -->
## TOPIC 00135: CA_VariantHasError

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthaserror.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthaserror.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasError

HRESULT CA_VariantHasError (const VARIANT *variant);

#### Purpose

Determines whether a variant contains an SCODE value. SCODE is the data type for an error value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if variant contains an SCODE value. 0 if variant does not contain an SCODE value. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthaslong.htm language=enus -->
## TOPIC 00136: CA_VariantHasLong

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthaslong.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthaslong.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasLong

HRESULT CA_VariantHasLong (const VARIANT *variant);

#### Purpose

Determines whether a variant contains a long integer value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if variant contains a long integer value. 0 if variant does not contain a long integer value. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvica_varianthasuchar.htm language=enus -->
## TOPIC 00137: CA_VariantHasUChar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvica_varianthasuchar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvica_varianthasuchar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CA_VariantHasUChar

HRESULT CA_VariantHasUChar (const VARIANT *variant);

#### Purpose

Determines whether a variant contains an unsigned character value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variant | const VARIANT * | Pointer to the variant variable to inspect. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | HRESULT | 1 if variant contains an unsigned character value. 0 if variant does not contain an unsigned character value. < 0 if variant is invalid. Negative error codes indicate function failure. Refer to <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h for Windows SDK error codes. |

#### Additional Information

**Library:** [ActiveX Library](../../cvi/libref/cviactivex_automation_libfunctiontree.htm)

**Include file:** cviauto.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviclock.htm language=enus -->
## TOPIC 00138: clock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviclock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviclock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### clock

clock_t clock (void);

#### Purpose

Returns the number of system clock cycles that have occurred since
the program started executing. The number of clock ticks can include time used by other processes.
To convert the number of clock cycles to seconds,
divide by CLOCKS_PER_SEC to obtain an approximation to the nearest millisecond.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| timeUsed | clock_t | Contains the number of system clock cycles that have occurred since the program started executing. The number of clock ticks can include time used by other processes. To convert the number of clock cycles to seconds, divide by CLOCKS_PER_SEC to obtain an approximation to the nearest millisecond. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviclose.htm language=enus -->
## TOPIC 00139: close

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviclose.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviclose.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### close

int close (int fileHandle);

#### Purpose

Flushes the system buffers for the specified file handle and closes the associated file. The function can return an error even when the file handle is valid because this function can flush the write buffer.

|  | Note This function is not in the ANSI standard. To use this function, you must include lowlvlio.h in your program or interactive window. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileHandle | int | Contains a file handle that will be closed. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Contains the status returned by the function. If the function succeeds, close returns 0. If an error occurs, close returns -1 and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** lowlvlio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviclosecom.htm language=enus -->
## TOPIC 00140: CloseCom

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviclosecom.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviclosecom.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CloseCom

int CloseCom (int portNumber);

#### Purpose

Closes a COM port.

CloseCom does nothing if the port is not open.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| portNumber | int | A number that indicates the COM port on which to operate. This number maps to the COM port specified by deviceName in the call to OpenCom or OpenComConfig. The portNumber 1, for example, may not necessarily map to COM1. (Linux) The portNumber 1, for example, may not necessarily map to /dev/ttyS0. Valid Range: 1—1,000 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int | The result of this function call. This code is a negative value that specifies the type of error that occurred. |

#### Additional Information

**Library:** [RS-232 Library](../../cvi/libref/cvirs232_library_function_tree.htm)

**Include file:** rs232.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the CloseCom function:

- rs232\commcallback.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- rs232\serial.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviclosecvirte.htm language=enus -->
## TOPIC 00141: CloseCVIRTE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviclosecvirte.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviclosecvirte.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CloseCVIRTE

void CloseCVIRTE (void);

#### Purpose

Releases memory that [InitCVIRTE](../../cvi/libref/cviinitcvirte.htm) allocated in the LabWindows/CVI Run-Time Engine for a particular DLL.

If you call InitCVIRTE from DllMain, call CloseCVIRTE from DllMain. You should call CloseCVIRTE in response to the DLL_PROCESS_DETACH message just before you return from DllMain.

#### Parameters

None.

#### Return Value

None.

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to dll\basic\cvidll.cws for an example of using the CloseCVIRTE function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviclosefile.htm language=enus -->
## TOPIC 00142: CloseFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviclosefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviclosefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CloseFile

int CloseFile (int fileHandle);

#### Purpose

Closes the file associated with **fileHandle**. Call [OpenFile](../../cvi/libref/cviopenfile.htm) to obtain a file handle.

|  | Caution The Windows SDK also contains a function with the same name. Include windows.h before including formatio.h to ensure that there are no compilation errors as a result of this naming conflict. Define the SDK_CONFLICT_PRIORITYSDK_CONFLICT_PRIORITY macro to force LabWindows/CVI to use the Windows SDK implementation of this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileHandle | int | Specifies the file to close. This is the value that OpenFile originally returned. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Result of the close file operation. If this value is –1, an error occurred. You can use GetFmtIOError to get more information about the type of error that occurred. Any value other than –1 indicates the function completed successfully. |

#### Additional Information

**Library:** [Formatting and I/O Library](../../cvi/libref/cviformatting_and_io_library_functi.htm)

**Include file:** formatio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\daqmthread\daqMT.cws for an example of using the CloseFile function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicls.htm language=enus -->
## TOPIC 00143: Cls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Cls

void Cls (void);

#### Purpose

Clears the console window of the program.

#### Parameters

None.

#### Return Value

None.

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to analysis\stats.cws for an example of using the Cls function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtdiscardlock.htm language=enus -->
## TOPIC 00144: CmtDiscardLock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtdiscardlock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtdiscardlock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtDiscardLock

int CmtDiscardLock (CmtThreadLockHandle lockHandle);

#### Purpose

Uninitializes the thread lock.

You must call this function for every thread lock created by calling [CmtNewLock](../../cvi/libref/cvicmtnewlock.htm). If the thread that calls this function currently owns the thread lock, this function returns an error. If another thread currently owns the thread lock, this function waits for the thread to release the lock before uninitializing the lock.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lockHandle | CmtThreadLockHandle | The handle you obtained from CmtNewLock to identify the thread lock. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtDiscardLock function:

- utility\threading\ThreadedGuessers\ThreadedGuessers.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadLockTimeout\ThreadLockTimeout.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\ParallelTestInit\ParallelTestInit.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtdiscardthreadlocalvar.htm language=enus -->
## TOPIC 00145: CmtDiscardThreadLocalVar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtdiscardthreadlocalvar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtdiscardthreadlocalvar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtDiscardThreadLocalVar

int CmtDiscardThreadLocalVar (CmtTLVHandle variableHandle);

#### Purpose

Destroys a thread local variable and frees the resources used by it.

After you call this function, you can no longer access the thread local variable from any thread.

This function calls the **discardCallbackFunction** parameter, which you specified in [CmtNewThreadLocalVar](../../cvi/libref/cvicmtnewthreadlocalvar.htm), once for each thread that accessed the thread local variable. Note that CmtDiscardThreadLocalVar calls the callback in the thread that calls CmtDiscardThreadLocalVar, and not in the individual threads that accessed the thread local variable. Therefore, if you use the thread local variable to store a resource that must be freed from the thread that created it, you must use [PostDeferredCallToThread](../../cvi/uiref/cvipostdeferredcalltothread.htm) to notify the proper thread that it must clean up the resource.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variableHandle | CmtTLVHandle | The handle you obtained from CmtNewThreadLocalVar to identify the thread local variable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtDiscardThreadLocalVar function:

- utility\threading\ThreadLocalVar\ThreadLocalVar.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\OnePanel\OnePanel.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtexitthreadpoolthread.htm language=enus -->
## TOPIC 00146: CmtExitThreadPoolThread

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtexitthreadpoolthread.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtexitthreadpoolthread.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtExitThreadPoolThread

int CmtExitThreadPoolThread (int returnValue);

#### Purpose

Stops execution of the Thread Function immediately from within a Thread
Function.

This function is typically used to terminate execution of a Thread Function when an error occurs.

This function does not terminate the thread. CmtExitThreadPoolThread returns the thread to the thread pool so that it can be used to execute other functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| returnValue | int | The value to return from the Thread Function. Call CmtGetThreadPoolFunctionAttribute with the ATTR_TP_FUNCTION_RETURN_VALUE attribute to get this value from another thread. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtflushtsq.htm language=enus -->
## TOPIC 00147: CmtFlushTSQ

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtflushtsq.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtflushtsq.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtFlushTSQ

int CmtFlushTSQ (CmtTSQHandle queueHandle, int itemsToFlush, int *itemsFlushed);

#### Purpose

Removes items from the thread safe queue.

You can use this function to reset the queue to a known state when you lose data due to queue overflow. This function waits until threads that are currently reading from or writing to the thread safe queue finish their operations before flushing any items.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| queueHandle | CmtTSQHandle | The handle you obtained from CmtNewTSQ to identify the thread safe queue. |
| itemsToFlush | int | The number of items to remove from the thread safe queue. Pass TSQ_FLUSH_ALL to remove all of the items from the queue. |
| Output |  |  |
| Name | Type | Description |
| itemsFlushed | int | Returns the number of items that the thread safe queue removed from the beginning of the queue to make room for the new data. Pass NULL if you do not want this value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtFlushTSQ function:

- apps\daqmthread\daqMT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\DirectPtrAccess\DirectPtrAccess.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\Overflow\Overflow.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtgetcurrentthreadid.htm language=enus -->
## TOPIC 00148: CmtGetCurrentThreadID

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtgetcurrentthreadid.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtgetcurrentthreadid.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtGetCurrentThreadID

unsigned int CmtGetCurrentThreadID (void);

#### Purpose

Returns the ID of the current thread.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentThreadID | unsigned int | The id of the current thread. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to utility\threading\ThreadPool\MultiPanel\MultiPanel.cws for an example of using the CmtGetCurrentThreadID function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtgetcurrentthreadpriority.htm language=enus -->
## TOPIC 00149: CmtGetCurrentThreadPriority

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtgetcurrentthreadpriority.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtgetcurrentthreadpriority.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtGetCurrentThreadPriority

int CmtGetCurrentThreadPriority (int *priority);

#### Purpose

Gets the priority of the current thread.

(Linux) This function is not supported.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| priority | int | The priority of the current thread. On Windows, this priority value in combination with the priority class of the processpriority class of the process determines the base priority level of the thread. The operating system uses this base priority level to schedule threads on the CPU. You can set the priority class of a process with the Windows SDK function SetPriorityClass. The thread priority value can be one of the following: Name Value THREAD_PRIORITY_TIME_CRITICAL 15 THREAD_PRIORITY_HIGHEST 2 THREAD_PRIORITY_ABOVE_NORMAL 1 THREAD_PRIORITY_NORMAL 0 THREAD_PRIORITY_BELOW_NORMAL -1 THREAD_PRIORITY_LOWEST -2 THREAD_PRIORITY_IDLE -15 (RT) On real-time systems the thread priority can be any value from -15 to 15. The default priority of a thread in the system is 0. The operating system scheduler runs at priority level 9. Any threads running at a priority level equal to or higher than 9 are not subject to timeslicing by the scheduler and will run until they yield the CPU or are preempted by a higher priority thread. |
| Name | Value |  |
| THREAD_PRIORITY_TIME_CRITICAL | 15 |  |
| THREAD_PRIORITY_HIGHEST | 2 |  |
| THREAD_PRIORITY_ABOVE_NORMAL | 1 |  |
| THREAD_PRIORITY_NORMAL | 0 |  |
| THREAD_PRIORITY_BELOW_NORMAL | -1 |  |
| THREAD_PRIORITY_LOWEST | -2 |  |
| THREAD_PRIORITY_IDLE | -15 |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtgeterrormessage.htm language=enus -->
## TOPIC 00150: CmtGetErrorMessage

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtgeterrormessage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtgeterrormessage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtGetErrorMessage

int CmtGetErrorMessage (int cmtStatusCode, char cmtStatusMessage[]);

#### Purpose

Converts a CmtStatus error code into a meaningful message string.

If the error code is kCmtSystemError, this function gets the message string from the operating system for the specific error that occurred.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| cmtStatusCode | int | A CmtStatus code returned from a LabWindows/CVI Utility Library multithreading function. |
| Output |  |  |
| Name | Type | Description |
| cmtStatusMessage | char [] | Returns a meaningful message string for a CmtStatus code. Note You must pass a char array that contains at least CMT_MAX_MESSAGE_BUF_SIZE (256) bytes. |
|  | Note You must pass a char array that contains at least CMT_MAX_MESSAGE_BUF_SIZE (256) bytes. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to utility\threading\ThreadLocalVar\ThreadLocalVar.cws for an example of using the CmtGetErrorMessage function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtgetthreadlocalvar.htm language=enus -->
## TOPIC 00151: CmtGetThreadLocalVar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtgetthreadlocalvar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtgetthreadlocalvar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtGetThreadLocalVar

int CmtGetThreadLocalVar (CmtTLVHandle variableHandle, void *variablePointer);

#### Purpose

Gets a pointer to the thread local variable instance for the current thread.

The first time you call this function from a thread, the variable is initialized to the value pointed to by the **variableInitialValue** parameter that you passed to [CmtNewThreadLocalVar](../../cvi/libref/cvicmtnewthreadlocalvar.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variableHandle | CmtTLVHandle | The handle you obtained from CmtNewThreadLocalVar to identify the thread local variable. |
| Output |  |  |
| Name | Type | Description |
| variablePointer | void * | Returns a pointer to the thread local variable instance for the current thread. Pass the address of a pointer to the type of the thread local variable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtGetThreadLocalVar function:

- utility\threading\ThreadLocalVar\ThreadLocalVar.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\OnePanel\OnePanel.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtinstalltsqcallback.htm language=enus -->
## TOPIC 00152: CmtInstallTSQCallback

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtinstalltsqcallback.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtinstalltsqcallback.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtInstallTSQCallback

int CmtInstallTSQCallback (CmtTSQHandle queueHandle, unsigned int event, int eventThresholdValue, CmtTSQCallbackPtr callbackFunction, void *callbackData, unsigned int callbackThreadID, CmtTSQCallbackID *callbackID);

#### Purpose

Specifies callbacks for thread safe queue events.

You can install only one callback per thread safe queue event. You can install a single callback that you want to call for more than one event.

Events are generated when items are added to the thread safe queue, when items are read from the thread safe queue, and when a dynamically sized thread safe queue grows. Your callback is called when the event occurs and the threshold value that you specified for the event has been exceeded. You are not required to uninstall thread safe queue callbacks.

Use callbacks to initiate reads and writes when a specified amount of data or space becomes available. Depending on the nature of your program, this can be a better model than continuously reading and writing data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| queueHandle | CmtTSQHandle | The handle you obtained from CmtNewTSQ to identify the thread safe queue. |
| event | unsigned int | The event that causes the thread safe queue to call your callback. Your callback is called when the event occurs and the threshold value you specify is exceeded. You can specify the following events: EVENT_TSQ_QUEUE_SIZE—A thread safe queue generates this event when its size meets or exceeds the threshold value. Only dynamically sizable queues can generate this event. Use this event if you want to know when the size of the queue meets or exceeds the size you specify in the threshold parameter. EVENT_TSQ_ITEMS_IN_QUEUE—A thread safe queue generates this event when both of the following conditions are true: A thread writes items to the thread safe queue. The number of items in the queue after the new items are added is greater than or equal to the threshold value. EVENT_TSQ_QUEUE_SPACE_FREE—A thread safe queue generates this event when both of the following conditions are true: A thread reads items from the thread safe queue or the thread safe queue is flushed by a call to CmtFlushTSQ. The total amount, in number of items, of free space in the queue after the read or flush is greater than or equal to the threshold value. Remember that you must check to see how much data or free space is in the queue when you get the EVENT_TSQ_QUEUE_SPACE_FREE and EVENT_TSQ_ITEMS_IN_QUEUE events because the queue might contain more than the threshold number of items or free space. The following lists examples. You register a callback for EVENT_TSQ_ITEMS_IN_QUEUE and set the threshold to 50. The writer writes 50 items to the queue. A callback is scheduled, but the thread in which the callback must be called is busy (it is not processing events) and therefore the callback is not called yet. The writer writes another 20 items to the queue. The thread in which the callback must be called is no longer busy (it processes events). The callback is called and the queue contains 70 items. If at this point only 60 items are read, the callback will not be called again when the writer writes 30 items because the number of items in the queue (40) is below the threshold value. |
| eventThresholdValue | int | The value that must be exceeded before the thread safe queue calls your callback function. This value contains different information for each event type. The following table shows the meaning of the value parameter for each event type: Event Value EVENT_TSQ_QUEUE_SIZE The total size, in number of items, of the thread safe queue. EVENT_TSQ_ITEMS_IN_QUEUE The total number of items in the thread safe queue. EVENT_TSQ_QUEUE_SPACE_FREE The total amount of free space, in number of items, in the thread safe queue. |
| Event | Value |  |
| EVENT_TSQ_QUEUE_SIZE | The total size, in number of items, of the thread safe queue. |  |
| EVENT_TSQ_ITEMS_IN_QUEUE | The total number of items in the thread safe queue. |  |
| EVENT_TSQ_QUEUE_SPACE_FREE | The total amount of free space, in number of items, in the thread safe queue. |  |
| callbackFunction | CmtTSQCallbackPtr | The function that the thread safe queue calls when the specified event occurs and the threshold value is exceeded. The function you pass in this parameter must have the following prototype: void CVICALLBACK Callback (CmtTSQHandle queueHandle, unsigned int event, int value, void *callbackData); Upon entry to the callback, the queueHandle parameter contains the handle of the thread safe queue that is generating the event. The callbackData parameter contains the value you passed to the callbackData parameter of this function. The event parameter indicates which event triggered the callback. The value parameter contains different information for each event type. The following table shows the possible event constants and the meaning of their corresponding value parameters: Event Value EVENT_TSQ_QUEUE_SIZE The total size, in number of items, of the thread safe queue. EVENT_TSQ_ITEMS_IN_QUEUE The total number of items in the thread safe queue. EVENT_TSQ_QUEUE_SPACE_FREE The total amount of free space, in number of items, in the thread safe queue. |
| Event | Value |  |
| EVENT_TSQ_QUEUE_SIZE | The total size, in number of items, of the thread safe queue. |  |
| EVENT_TSQ_ITEMS_IN_QUEUE | The total number of items in the thread safe queue. |  |
| EVENT_TSQ_QUEUE_SPACE_FREE | The total amount of free space, in number of items, in the thread safe queue. |  |
| callbackData | void * | A value that you want the thread safe queue to pass to your callback as the callbackData parameter. Do not pass the address of a local variable or any other variable that might not be valid when the function is executed. |
| callbackThreadID | unsigned int | The ID of the thread that you want to use to execute the Callback Function. Call CmtGetCurrentThreadID to get the current thread's ID. The specified thread must process events using RunUserInterface, GetUserEvent, or ProcessSystemEvents. |
| Output |  |  |
| Name | Type | Description |
| callbackID | CmtTSQCallbackID | Returns an ID that uniquely identifies the callback. Use this ID to uninstall the callback. You are not required to uninstall the callback before discarding the thread safe queue. Pass NULL if you do not want the callbackID. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtInstallTSQCallback function:

- apps\daqmthread\daqMT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\BuffNoDataLoss\BuffNoDataLoss.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\DirectPtrAccess\DirectPtrAccess.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\Overflow\Overflow.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtnewlock.htm language=enus -->
## TOPIC 00153: CmtNewLock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtnewlock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtnewlock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtNewLock

int CmtNewLock (const char lockName[], unsigned int options, CmtThreadLockHandle *lockHandle);

#### Purpose

Creates a thread lock.

Use a thread lock in applications with multiple threads to prevent multiple threads from performing some action at the same time.

[CmtGetLock](../../cvi/libref/cvicmtgetlock.htm), [CmtGetLockEx](../../cvi/libref/cvicmtgetlockex.htm), and [CmtReleaseLock](../../cvi/libref/cvicmtreleaselock.htm) take longer to execute if you name the lock or choose to process messages in CmtGetLock.

When you finish using the lock in all threads, you must call [CmtDiscardLock](../../cvi/libref/cvicmtdiscardlock.htm) to uninitialize the lock.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lockName | const char [] | The name you want to give to the lock you are creating. Pass NULL if you do not want to name the lock. Unnamed locks provide better performance than named locks. You must name the lock if you plan to use the lock across multiple processes. The lock name must not be longer than MAX_PATHNAME_LEN characters. Note MAX_PATHNAME_LEN is only reliable for ANSI single byte strings. For UTF-8 strings, call the IsUTF8PathLengthValid function to confirm that the file path is within the operating system character limit. Under Windows systems with Terminal Services running, the lock name can have a Global\\ or Local\\ prefix to explicitly create the object in the global or session name space. The lock name can contain any character, but the backslash character (\\) must be used only with these prefixes. Under Windows systems without Terminal Services running, the Global\\ and Local\\ prefixes are ignored. The lock name can contain any character, but the backslash character must only be used with these prefixes. |
|  | Note MAX_PATHNAME_LEN is only reliable for ANSI single byte strings. For UTF-8 strings, call the IsUTF8PathLengthValid function to confirm that the file path is within the operating system character limit. |  |
| options | unsigned int | Pass OPT_TL_PROCESS_EVENTS_WHILE_WAITING if you want threads to process events while waiting to acquire the lock in CmtGetLock or CmtGetLockEx. Pass OPT_TL_SUPPORT_TIMEOUT if you want to wait for finite intervals when trying to acquire the lock - if you do not pass this option, then threads will wait forever when trying to acquire the lock. You can pass the bitwise OR of the above flags to apply both options. Pass 0 if you do not want to apply any of the above options. To avoid hanging the system, pass OPT_TL_PROCESS_EVENTS_WHILE_WAITING if threads might wait for more than a fraction of a second to acquire the lock or if threads that get the lock send messages or display panels or dialog boxes while they have the lock. You do not need to pass OPT_TL_PROCESS_EVENTS_WHILE_WAITING if you hold the lock for short periods of time and do not perform any user interface or messaging actions while you own the lock. Note It is not always obvious when a window is created. Various LabWindows/CVI and Windows SDK functions create hidden windows. For example, the operating system uses hidden windows to communicate between certain kinds of ActiveX servers and clients. |
|  | Note It is not always obvious when a window is created. Various LabWindows/CVI and Windows SDK functions create hidden windows. For example, the operating system uses hidden windows to communicate between certain kinds of ActiveX servers and clients. |  |
| Output |  |  |
| Name | Type | Description |
| lockHandle | CmtThreadLockHandle | Returns a handle that you use to identify the thread lock in subsequent function calls. The handle is never 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtNewLock function:

- utility\threading\ThreadedGuessers\ThreadedGuessers.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadLockTimeout\ThreadLockTimeout.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\ParallelTestInit\ParallelTestInit.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtnewthreadlocalvar.htm language=enus -->
## TOPIC 00154: CmtNewThreadLocalVar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtnewthreadlocalvar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtnewthreadlocalvar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtNewThreadLocalVar

int CmtNewThreadLocalVar (size_t variableSize, const void *variableInitialValue, CmtTLVCallbackPtr discardCallbackFunction, void *callbackData, CmtTLVHandle *variableHandle);

#### Purpose

Creates a thread local variable.

You can use a thread local variable to store information that varies between threads in your application. When you are finished using the variable from all threads, you can call [CmtDiscardThreadLocalVar](../../cvi/libref/cvicmtdiscardthreadlocalvar.htm) to free the thread local variable. Alternatively, you can allow the threads to exit without calling CmtDiscardThreadLocalVar. The library automatically frees the thread local variable when each thread that accessed it exits.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variableSize | size_t | The size of the data that you want to store in the thread local variable. The sizeof operator is useful for this. The function returns an error if this value is greater than INT_MAX. |
| variableInitialValue | const void * | A pointer to a variable containing the initial value for the thread local variable. When a thread accesses the thread local for the first time, its value is set to this default. Pass NULL to initialize the contents of the variable to 0. For array and structure variables, every element is initialized to 0. Note This function does not support partial initialization of array and structure types. You must pass either NULL or a pointer to an entire instance of the type. |
|  | Note This function does not support partial initialization of array and structure types. You must pass either NULL or a pointer to an entire instance of the type. |  |
| discardCallbackFunction | CmtTLVCallbackPtr | The function that you want the library to call when a thread local variable is discarded. You can use this callback to free resources that you allocated and stored in the thread local variable. The function you pass in this parameter must have the following prototype: void CVICALLBACK Callback (void *threadLocalPtr, int event, void *callbackData, unsigned int threadID); Upon entry to the callback, the threadLocalPtr parameter contains a pointer to the thread local variable. The event parameter indicates the reason that the thread local variable is being discarded. The callbackData parameter contains the value you passed to the callbackData parameter of this function. The threadID parameter indicates which thread is associated with the thread local variable pointed to by the threadLocalPtr parameter. Under most circumstances you can free, directly in this callback, resources that are stored in your thread local variables. However, under certain circumstances, you must call PostDeferredCallToThread to ensure that your resources are freed from the appropriate thread. If both of the following conditions apply, you must post a deferred call to the thread indicated in the value of the threadID parameter: The resources you want to free must be freed from the thread that allocated them. For example, you must free an HWND that you obtained from the Windows SDK function CreateWindow by calling DestroyWindow in the same thread that you called CreateWindow. The threadID parameter does not match the thread ID of the thread in which the callback is called. Use the CmtGetCurrentThreadID function to get the thread ID of the thread in which the callback is called. Keep in mind that when the callback returns, the library frees the thread local variable, so you must make copies of the resources that you want free in your deferred call. For example, if the thread local variable value is a pointer to an HWND, you must pass the HWND directly, not the pointer to the HWND, to your deferred function. The following list indicates the possible event values: Event: EVENT_TLV_DISCARD_THREAD_DETACH Value: The thread that accessed the thread local variable is exiting. Event: EVENT_TLV_DISCARD_FUNCTION_CALLED Value: CmtDiscardThreadLocalVar was called. |
| callbackData | void * | A value that you want to pass to your callback as the callbackData parameter. Do not pass the address of a local variable or any other variable that might not be valid when the function is executed. |
| Output |  |  |
| Name | Type | Description |
| variableHandle | CmtTLVHandle | Returns a handle that you use to identify the thread local variable in subsequent function calls. The handle is never 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtNewThreadLocalVar function:

- utility\threading\ThreadLocalVar\ThreadLocalVar.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\OnePanel\OnePanel.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtnewthreadpool.htm language=enus -->
## TOPIC 00155: CmtNewThreadPool

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtnewthreadpool.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtnewthreadpool.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtNewThreadPool

int CmtNewThreadPool (int maximumNumberOfThreads, CmtThreadPoolHandle *poolHandle);

#### Purpose

Creates a thread pool.

The threads are not created until you schedule a function with [CmtScheduleThreadPoolFunction](../../cvi/libref/cvicmtschedulethreadpoolfunction.htm) or [CmtScheduleThreadPoolFunctionAdv](../../cvi/libref/cvicmtschedulethreadpoolfunctionadv.htm) or you call [CmtPreAllocThreadPoolThreads](../../cvi/libref/cvicmtpreallocthreadpoolthreads.htm).

You do not need to create a thread pool if your program uses the only default
thread pool. To use the default thread pool, pass DEFAULT_THREAD_POOL_HANDLE to the thread pool functions.

Call [CmtDiscardThreadPool](../../cvi/libref/cvicmtdiscardthreadpool.htm) to free the thread pool resources when you finish using the thread pool.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| maximumNumberOfThreads | int | The maximum number of threads in the thread pool. Call CmtGetThreadPoolAttribute or CmtSetThreadPoolAttribute with the ATTR_TP_MAX_NUM_THREADS attribute to read or change this value after the pool has been created. Use either a fixed number of threads or make the maximum number of threads proportional to the number of processors. For example, the maximum number or threads in the default thread pool is 2 + (2 * (number of processors)). Call CmtGetNumProcessors to determine the number of processors at run time. Pass UNLIMITED_THREAD_POOL_THREADS to indicate no limit on the maximum number of threads. In general, this is not recommended because having too many threads in a process can result in poor program performance. |
| Output |  |  |
| Name | Type | Description |
| poolHandle | CmtThreadPoolHandle | The handle that you use to identify the thread pool in subsequent function calls. The handle is never 0. Call CmtDiscardThreadPool to free the thread pool resources when you finish using the thread pool. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtNewThreadPool function:

- utility\threading\ThreadedGuessers\ThreadedGuessers.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadLockTimeout\ThreadLockTimeout.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\MultiPanel\MultiPanel.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\OnePanel\OnePanel.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\ParallelTestInit\ParallelTestInit.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtnewtsv.htm language=enus -->
## TOPIC 00156: CmtNewTSV

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtnewtsv.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtnewtsv.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtNewTSV

int CmtNewTSV (size_t variableSize, CmtTSVHandle *variableHandle);

#### Purpose

Creates a thread safe variable.

Use a thread safe variable to store information that must be accessed from more than one thread in your application. When you finish using the variable from all threads, you must call CmtDiscardThreadSafeVar to uninitialize the thread safe variable.

It is difficult to program with this function directly. It is easier to program with the functions provided by the [DefineThreadSafeScalarVar](definedeclarethreadsafescalarvar.htm), [DefineThreadSafeArrayVar](definedeclarethreadsafearrayvar.htm), [DeclareThreadSafeScalarVar](definedeclarethreadsafescalarvar.htm#declarethreadsafescalarvar), and [DeclareThreadSafeArrayVar](definedeclarethreadsafearrayvar.htm#declarethreadsafearrayvar) [macros](../../cvi/libref/macrosandtsvariables.htm), which are defined in utility.h.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variableSize | size_t | The size, in bytes, of the data that you want to store in the thread safe variable. The sizeof operator is useful for this. The function returns an error if this value is greater than INT_MAX. |
| Output |  |  |
| Name | Type | Description |
| variableHandle | CmtTSVHandle | Returns a handle that you use to identify the thread safe variable in subsequent function calls. The handle is never 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtpreallocthreadpoolthreads.htm language=enus -->
## TOPIC 00157: CmtPreAllocThreadPoolThreads

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtpreallocthreadpoolthreads.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtpreallocthreadpoolthreads.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtPreAllocThreadPoolThreads

int CmtPreAllocThreadPoolThreads (CmtThreadPoolHandle poolHandle, int numberOfThreads, int *numberOfThreadsCreated);

#### Purpose

Call this function only if you want to make sure that a certain number of
threads exist or are available to execute scheduled functions. Call [CmtGetThreadPoolAttribute](../../cvi/libref/cvicmtgetthreadpoolattribute.htm) with the ATTR_TP_NUM_THREADS attribute to determine the number of threads already in the pool.

CmtPreAllocThreadPoolThreads attempts to create a specified number of threads in the pool. If adding the specified number of threads yields more threads than the maximum allowed for the pool, only enough threads are created to reach the maximum. You can use this function to control the time at which your program incurs the overhead of creating threads.

The maximum number of threads in a pool is set when it is created. Call [CmtSetThreadPoolAttribute](../../cvi/libref/cvicmtsetthreadpoolattribute.htm) with the ATTR_TP_MAX_NUM_THREADS attribute to change the maximum.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| poolHandle | CmtThreadPoolHandle | The handle you obtained from CmtNewThreadPool to identify the thread pool. Do not pass DEFAULT_THREAD_POOL_HANDLE to this function. |
| numberOfThreads | int | The additional number of threads to create in the thread pool. Call CmtGetThreadPoolAttribute with the ATTR_TP_NUM_THREADS attribute to determine how many threads have already been created in the thread pool. |
| Output |  |  |
| Name | Type | Description |
| numberOfThreadsCreated | int | The actual number of threads added to the pool. Pass NULL if you do not want this value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtreleasetsqreadptr.htm language=enus -->
## TOPIC 00158: CmtReleaseTSQReadPtr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtreleasetsqreadptr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtreleasetsqreadptr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtReleaseTSQReadPtr

int CmtReleaseTSQReadPtr (CmtTSQHandle queueHandle, int itemsRead);

#### Purpose

Releases a pointer to a thread safe queue's internal buffer that you obtained from [CmtGetTSQReadPtr](../../cvi/libref/cvicmtgettsqreadptr.htm).

The space taken up by the data you read from the thread safe queue is not available for writing from another thread until you release the pointer with this function. After you call this function, the pointer is no longer valid. You cannot use an invalid pointer to read data from the thread safe queue.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| queueHandle | CmtTSQHandle | The handle you obtained from CmtNewTSQ to identify the thread safe queue. |
| itemsRead | int | The number of items that you read from the thread safe queue using the read pointer obtained from CmtGetTSQReadPtr. Pass 0 to leave the data in the queue. This allows you to read the same data more than once. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtReleaseTSQReadPtr function:

- utility\threading\ThreadSafeQueue\DirectPtrAccess\DirectPtrAccess.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\Overflow\Overflow.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtsetthreadpoolattribute.htm language=enus -->
## TOPIC 00159: CmtSetThreadPoolAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtsetthreadpoolattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtsetthreadpoolattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtSetThreadPoolAttribute

int CmtSetThreadPoolAttribute (CmtThreadPoolHandle poolHandle, int attributeID, ...);

#### Purpose

Sets the value of [thread pool attributes](../../cvi/libref/cviattributes_for_cmtgetthreadpoola.htm).

You can set certain attributes only before any threads in the thread pool are created. If you want to modify these attributes, you must do so before you schedule any functions in the thread pool. You cannot set any attributes of the default thread pool.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| poolHandle | CmtThreadPoolHandle | The handle you obtained from CmtNewThreadPool to identify the thread pool. Do not pass DEFAULT_THREAD_POOL_HANDLE to this function. |
| attributeID | int | The ID of a thread pool attribute. |
| attributeValue | ... | The value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to utility\threading\ThreadPool\MultiPanel\MultiPanel.cws for an example of using the CmtSetThreadPoolAttribute function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtsettsqattribute.htm language=enus -->
## TOPIC 00160: CmtSetTSQAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtsettsqattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtsettsqattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtSetTSQAttribute

int CmtSetTSQAttribute (CmtTSQHandle queueHandle, int attributeID, ...);

#### Purpose

Sets the value of [thread safe queue attributes](../../cvi/libref/cviattributes_for_cmtgettsqattribut.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| queueHandle | CmtTSQHandle | The handle you obtained from CmtNewTSQ to identify the thread safe queue. |
| attributeID | int | The ID of a thread safe queue attribute. |
| attributeValue | ... | The value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtsettsv.htm language=enus -->
## TOPIC 00161: CmtSetTSV

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtsettsv.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtsettsv.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtSetTSV

int CmtSetTSV (CmtTSVHandle variableHandle, const void *valuePointer);

#### Purpose

Sets the value of the thread safe variable.

If another thread either has the thread safe variable pointer or is currently setting the value of the thread safe variable, this function waits until the other thread has completed its operation.

Do not use this function if the value you are setting depends on the previous
value of this thread safe variable. For example, if you want to increment the value of a thread safe integer variable, it is not valid to call [CmtGetTSVPtr](../../cvi/libref/cvicmtgettsvptr.htm) to get the value, store the value in a local variable, call [CmtReleaseTSVPtr](../../cvi/libref/cvicmtreleasetsvptr.htm) to release the pointer, increment the local variable, and then CmtSetTSV to set the value to the value of the local variable. This is not valid because another thread might change the value between your calls to CmtReleaseTSVPtr and CmtSetTSV, thereby invalidating the incremented value of the variable.

It is difficult to program with this function directly. It is easier to program with the functions provided by the [DefineThreadSafeScalarVar](definedeclarethreadsafescalarvar.htm), [DefineThreadSafeArrayVar](definedeclarethreadsafearrayvar.htm), [DeclareThreadSafeScalarVar](definedeclarethreadsafescalarvar.htm#declarethreadsafescalarvar), and [DeclareThreadSafeArrayVar](definedeclarethreadsafearrayvar.htm#declarethreadsafearrayvar) [macros](../../cvi/libref/macrosandtsvariables.htm), which are defined in utility.h.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| variableHandle | CmtTSVHandle | The handle you obtained from CmtNewTSV to identify the thread safe variable. |
| valuePointer | const void * | A pointer to a variable that contains the needed value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmttrytogetlock.htm language=enus -->
## TOPIC 00162: CmtTryToGetLock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmttrytogetlock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmttrytogetlock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtTryToGetLock

int CmtTryToGetLock (CmtThreadLockHandle lockHandle, int *obtainedLock);

#### Purpose

Tries to get ownership of the thread lock.

When you finish using the thread lock, you must release the lock by calling [CmtReleaseLock](../../cvi/libref/cvicmtreleaselock.htm) from the same thread that called CmtTryToGetLock.

Only one thread can get ownership of the thread lock at a time. If a thread requests the lock while another thread owns the lock, CmtTryToGetLock returns immediately without obtaining the lock.

You can call CmtTryToGetLock from the same thread more than once, but you must call CmtReleaseLock once for each time that you successfully obtained the lock.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lockHandle | CmtThreadLockHandle | The handle you obtained from CmtNewLock to identify the thread lock. |
| Output |  |  |
| Name | Type | Description |
| obtainedLock | int | Returns 1 if you obtain the lock. Returns 0 if you fail to obtain the lock. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to utility\threading\ThreadLockTimeout\ThreadLockTimeout.cws for an example of using the CmtTryToGetLock function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtuninstallthreadpoolcallback.htm language=enus -->
## TOPIC 00163: CmtUninstallThreadPoolCallback

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtuninstallthreadpoolcallback.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtuninstallthreadpoolcallback.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtUninstallThreadPoolCallback

int CmtUninstallThreadPoolCallback (CmtThreadPoolHandle poolHandle, CmtThreadPoolCallbackID callbackID);

#### Purpose

Uninstalls a callback that you registered with [CmtInstallThreadPoolCallback](../../cvi/libref/cvicmtinstallthreadpoolcallback.htm).

You are not required to uninstall callbacks before discarding a thread pool.

If the callback ID was returned from a CmtInstallThreadPoolCallback call that specified more than one event, the callback is uninstalled for all of the specified events.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| poolHandle | CmtThreadPoolHandle | The handle you obtained from CmtNewThreadPool to identify the thread pool. Do not pass DEFAULT_THREAD_POOL_HANDLE to this function. |
| callbackID | CmtThreadPoolCallbackID | The callbackID that you obtained from CmtInstallThreadPoolCallback. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicmtuninstalltsqcallback.htm language=enus -->
## TOPIC 00164: CmtUninstallTSQCallback

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicmtuninstalltsqcallback.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicmtuninstalltsqcallback.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CmtUninstallTSQCallback

int CmtUninstallTSQCallback (CmtTSQHandle queueHandle, CmtTSQCallbackID callbackID);

#### Purpose

Uninstalls a callback that you registered with [CmtInstallTSQCallback](../../cvi/libref/cvicmtinstalltsqcallback.htm).

You are not required to uninstall callbacks before discarding a thread safe queue.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| queueHandle | CmtTSQHandle | The handle you obtained from CmtNewTSQ to identify the thread safe queue. |
| callbackID | CmtTSQCallbackID | The callbackID that you obtained from CmtInstallTSQCallback. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| cmtStatus | int | The CmtStatus code that the function call returns. This function returns 0 to indicate success and negative values to indicate failure. Pass the CmtStatus code to CmtGetErrorMessage to get a description of the error code. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the CmtUninstallTSQCallback function:

- utility\threading\ThreadSafeQueue\BuffNoDataLoss\BuffNoDataLoss.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\DirectPtrAccess\DirectPtrAccess.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadSafeQueue\Overflow\Overflow.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnsdatacreatearray.htm language=enus -->
## TOPIC 00165: CNSDataCreateArray

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnsdatacreatearray.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnsdatacreatearray.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSDataCreateArray

int CNSDataCreateArray (CNSData array[], size_t dimensions[], size_t numDimensions, CNSData *data);

#### Purpose

Creates a [network stream data object](../../cvi/libref/cnsdata.htm) containing an array.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| array | CNSData [] | The array of network stream data you want to pack into a single network stream data object. |
| dimensions | size_t [] | The dimensions of the array. |
| numDimensions | size_t | The number of dimensions of the array. |
| Output |  |  |
| Name | Type | Description |
| data | CNSData | A reference to the network stream data object you created. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnsdatacreatescalar.htm language=enus -->
## TOPIC 00166: CNSDataCreateScalar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnsdatacreatescalar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnsdatacreatescalar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSDataCreateScalar

int CNSDataCreateScalar (CNSType dataType, CNSData *data, ...);

#### Purpose

Creates a [network stream data object](../../cvi/libref/cnsdata.htm) containing a scalar element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| dataType | CNSType | The data type of the network stream data object you want to create. |
| value | ... | The data that you want to pack inside the network stream data object. |
| Output |  |  |
| Name | Type | Description |
| data | CNSData | A reference to the network stream data object you created. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnsdatacreatestruct.htm language=enus -->
## TOPIC 00167: CNSDataCreateStruct

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnsdatacreatestruct.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnsdatacreatestruct.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSDataCreateStruct

int CNSDataCreateStruct (CNSData fields[], size_t numFields, CNSData *data);

#### Purpose

Creates a [network stream data object](../../cvi/libref/cnsdata.htm) containing a structure.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fields | CNSData [] | The fields of the structure you want to create. |
| numFields | size_t | The number of struct fields in the network stream data object. |
| Output |  |  |
| Name | Type | Description |
| data | CNSData | A reference to the network stream data object you created. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnsdatagetnumstructfields.htm language=enus -->
## TOPIC 00168: CNSDataGetNumStructFields

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnsdatagetnumstructfields.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnsdatagetnumstructfields.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSDataGetNumStructFields

int CNSDataGetNumStructFields (CNSData data, size_t *numFields);

#### Purpose

Gets the number of struct fields of the [network stream data object](../../cvi/libref/cnsdata.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| data | CNSData | The reference to the network stream data object. |
| Output |  |  |
| Name | Type | Description |
| numFields | size_t | The number of struct fields in the network stream data object. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnsdatagetscalarvalue.htm language=enus -->
## TOPIC 00169: CNSDataGetScalarValue

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnsdatagetscalarvalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnsdatagetscalarvalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSDataGetScalarValue

int CNSDataGetScalarValue (CNSData data, void *value);

#### Purpose

Gets the value a [network stream data object](../../cvi/libref/cnsdata.htm) containing a scalar.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| data | CNSData | The reference to the network stream data object. |
| Output |  |  |
| Name | Type | Description |
| value | void | The reference to the scalar. If the data type is a string, you must call CNSFreeMemory to free it. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnsfinish.htm language=enus -->
## TOPIC 00170: CNSFinish

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnsfinish.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnsfinish.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSFinish

int CNSFinish (void);

#### Purpose

Uninitializes the Network Streams Library.

|  | Note You must call this function after your program is done using the Network Streams Library to discard and clean up global resources. If you do not call this function after calling other functions in the Network Streams Library, your program might hang or crash when it closes and LabWindows/CVI might not be able to report the leaked resources in your program. Additionally, you must not call this function from DllMain and atexit handlers functions?doing so may cause your application to deadlock and stop responding. |
| --- | --- |

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

#### Examples

Refer to the following examples that use the CNSFinish function:

- networkstreams\cnsGUI.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkstreams\cnsSimple.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnsnewarrayendpoint.htm language=enus -->
## TOPIC 00171: CNSNewArrayEndpoint

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnsnewarrayendpoint.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnsnewarrayendpoint.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSNewArrayEndpoint

int CNSNewArrayEndpoint (char *endpointUrl, char *otherEndpointUrl, CNSType dataType, size_t numArrays, size_t arraySize, CNSDirection direction, int timeout, intptr_t reserved, CNSEndpoint *endpointID);

#### Purpose

Creates a reader or writer endpoint of a network stream that transmits arrays of the type specified by the **dataType** parameter. Only numeric scalars are supported. Strings are not supported.

Endpoints can be active or passive. An active endpoint tries to connect to another endpoint, while a passive endpoint waits for a connection. If you pass NULL or an empty string to **otherEndpointUrl**, you create a passive endpoint.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| endpointUrl | char * | The URL of the local endpoint. |
| otherEndpointUrl | char * | The URL of the endpoint you want to connect to. If you pass NULL or an empty string to otherEndpointURL, you create a passive endpoint, meaning that the endpoint waits for a connection. |
| dataType | CNSType | The data type of the network stream. |
| numArrays | size_t | The size of the arrays. The minimum size is one element. |
| arraySize | size_t | Determines how to allocate memory for the network stream endpoint buffers. If you want to pre-allocate memory for your network stream data, specify the combined total of the maximum size of each data element in each array, plus an additional 4 bytes to hold the size of the network stream data. If you do not want pre-allocate memory, pass 0 for this parameter. |
| direction | CNSDirection | Specifies whether the endpoint you create with this function is a writer endpoint or reader endpoint. You can specify one of the following values: Value Description CNSDirectionReader Create a reader endpoint CNSDirectionWriter Create a writer endpoint |
| Value | Description |  |
| CNSDirectionReader | Create a reader endpoint |  |
| CNSDirectionWriter | Create a writer endpoint |  |
| timeout | int | The time, in milliseconds, that this endpoint waits to connect to the other endpoint or waits for the other endpoint to connect to it. The default value is CNSWaitForever, which means this endpoint waits indefinitely. If the timeout expires, this function returns an error. |
| reserved | intptr_t | This parameter is reserved for use by the Network Streams Library. You must pass 0 for this parameter. |
| Output |  |  |
| Name | Type | Description |
| endpointID | CNSEndpoint | The handle to the network stream endpoint created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnswritearray.htm language=enus -->
## TOPIC 00172: CNSWriteArray

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnswritearray.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnswritearray.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSWriteArray

int CNSWriteArray (CNSEndpoint endpointID, int timeout, void *array, size_t numElements);

#### Purpose

Writes one array item to a network stream that transmits arrays of this type. You can call this function from the writer endpoint only.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| endpointID | CNSEndpoint | The handle of a network stream endpoint. You can obtain this handle using the CNSNewArrayEndpoint function. |
| timeout | int | The time, in milliseconds, that this function waits for free space in the buffer. The default value is CNSWaitForever, which means this endpoint waits indefinitely. If the timeout expires, this function returns an error. |
| array | void * | The array of scalar elements that you want to write to the network stream. |
| numElements | size_t | The size of the array you want to write to the network stream. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnswritedata.htm language=enus -->
## TOPIC 00173: CNSWriteData

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnswritedata.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnswritedata.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNSWriteData

int CNSWriteData (CNSEndpoint endpointID, int timeout, CNSData data);

#### Purpose

Writes a network stream data object to a network stream. You can call this function from the writer endpoint only.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| endpointID | CNSEndpoint | The handle of a network stream endpoint. You can obtain this handle using the CNSNewEndpoint function. |
| timeout | int | The time, in milliseconds, that this function waits for free space in the buffer. The default value is CNSWaitForever, which means this endpoint waits indefinitely. If the timeout expires, this function returns an error. |
| data | CNSData | A reference to the network stream data object you want to write to the network stream. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| error | int | An error code returned by a Network Streams Library function. |

#### Additional Information

**Library:** [Network Streams Library](../../cvi/libref/networkstreamslibrary.htm)

**Include file:** cvinetstreams.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvcreatearraydatavalue.htm language=enus -->
## TOPIC 00174: CNVCreateArrayDataValue

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvcreatearraydatavalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvcreatearraydatavalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVCreateArrayDataValue

int CNVCreateArrayDataValue (CNVData *data, CNVDataType type, const void *array, size_t numberOfDimensions, size_t dimensions[]);

#### Purpose

Creates network variable data containing the specified array. Currently, this function does not support setting string arrays with a number of dimensions greater than two.

Note that different programming environments may interpret multidimensional arrays in different formats. For example, two-dimensional arrays can be interpreted in row-major or column-major formats. This can affect the dimensions and data of multidimensional arrays communicated between different programming environments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| type | CNVDataType | The type of the specified network variable data. Note that CNVBool refers to a 1-byte boolean type (char or unsigned char), and CNVString refers to a C-style NUL-terminated string. |
| array | const void * | An array of the type specified by the type parameter to set in the network variable data. The length of the array you pass for this parameter must be greater than or equal to the value specified by the dimensions parameter. The Network Variable Library treats this parameter as a flat, contiguous block of memory and reads the elements in row-major order. |
| numberOfDimensions | size_t | The number of dimensions of the network variable array data. |
| dimensions | size_t[] | The array dimensions of the network variable data. The length of the array you pass for this parameter must be greater than or equal to the value specified by the numberOfDimensions parameter. |
| Output |  |  |
| Name | Type | Description |
| data | CNVData | The handle of the network variable data that contains the specified array. Call CNVDisposeData to dispose the handle when you are done using it. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Example

Refer to networkvariable\3DSim\NV3DSim.cws for an example of using the CNVCreateArrayDataValue function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvcreateasyncreader.htm language=enus -->
## TOPIC 00175: CNVCreateAsyncReader

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvcreateasyncreader.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvcreateasyncreader.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVCreateAsyncReader

int CNVCreateAsyncReader (const char *networkVariablePathname, CNVDataCallback dataCallback, CNVStatusCallback statusCallback, void *callbackData, int waitTime, intptr_t reserved, CNVAsyncReader *asynchronousReader);

#### Purpose

Creates an asynchronous reader connection to the network variable that you specify with the **networkVariablePathname** parameter. You can asynchronously read new values of the network variable by calling [CNVReadAsync](../../cvi/libref/cvicnvreadasync.htm). The **dataCallback** is called with the data that an asynchronous read operation returns.

|  | Note The throughput rate of data with reader and asynchronous reader connections is slower than with subscriber and buffered subscriber connections. If throughput rate is critical to your application, consider using a subscriber or buffered subscriber connection instead. |
| --- | --- |

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| networkVariablePathname | const char * | Pathname of the network variable to connect. The format of the pathname is \\\\machineName\\processName\\folderNames\\variableName, which is similar to the format of items on network shares and is not case-sensitive. The following list shows examples of pathnames: \\\\localhost\\my_process\\my_folder1\\my_folder2\\my_variable \\\\test_machine\\my_process\\my_sub_process\\my_variable \\\\192.168.1.100\\my_process\\my_variable \\\\test_machine.my_network.com\\my_process\\my_variable \\\\localhost\\System\\DAQmx\\Server Polling Rate \\\\localhost\\system\\my_variable You can explicitly create and configure your variables using the NI Distributed System Manager that ships with LabWindows/CVI or using the Configuration Functions in the Network Variable Library. You also can use previously created explicit variables. If you specify a new variable name in the system process, as shown in the last example, then the Network Variable Library creates a variable implicitly. Implicit variables can hold values of any type, always have the single-writer restriction, and do not support server-side buffering. The Network Variable Library automatically deletes an implicit variable when all of its clients disconnect, that is, when there are no outstanding connections to it. Carefully decide whether to use implicit or explicit variables depending on your application and deployment needs. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify \\\\localhost\\process'Name\\variable.Name as a URL, enter the following: 'process''Name' as the process name 'variable.Name' as the variable name The resulting URL is \\\\localhost\\\\'process''Name'\\'variable.Name'. This rule does not apply to computer names. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify \\\\localhost\\process'Name\\variable.Name as a URL, enter the following: 'process''Name' as the process name 'variable.Name' as the variable name The resulting URL is \\\\localhost\\\\'process''Name'\\'variable.Name'. This rule does not apply to computer names. |  |
| dataCallback | CNVDataCallback | The function that the library calls when the network variable connection receives data. The system generates data when the value, quality, or timestamp of the variable changes. The library calls this function asynchronously in a worker thread. The function you pass in this parameter must have the following prototype: void CVICALLBACK Callback (void * handle, CNVData data, void * callbackData); Upon entry to the callback, the handle parameter contains the handle of the connection that is generating the event. The data parameter contains the handle of the received network variable data. Call CNVDisposeData to dispose the handle when you are done using it. The callbackData parameter of the callback contains the value you provide in the callbackData parameter of this function. Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event in a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |
|  | Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event in a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |  |
| statusCallback | CNVStatusCallback | The function that the library calls when the connection status of a successfully created network variable changes. Connection status events occur when there is a significant network delay and NI-PSP attempts to reconnect. The library calls this function asynchronously in a worker thread. You can pass NULL if you do not want this notification. The function you pass in this parameter must have the following prototype: void CVICALLBACK Callback (void * handle, CNVConnectionStatus status, int error, void * callbackData); Upon entry to the callback, the handle parameter contains the handle of the connection that is generating the event. The status parameter contains the status of the connection. The error parameter indicates any errors in the connection. The callbackData parameter of the callback contains the value you provide in the callbackData parameter of this function. Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |
|  | Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |  |
| callbackData | void * | The callback data that the library passes to the associated callback functions. |
| waitTime | int | Number of milliseconds the library waits for this operation to complete. Pass CNVWaitForever to wait indefinitely. |
| reserved | intptr_t | You must pass zero. This parameter is reserved for future use. |
| Output |  |  |
| Name | Type | Description |
| asynchronousReader | CNVAsyncReader | Returns a handle that you can use to identify this network variable connection in subsequent function calls. Call CNVDispose to dispose the handle when you are done using it. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvcreatebufferedsubscriber.htm language=enus -->
## TOPIC 00176: CNVCreateBufferedSubscriber

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvcreatebufferedsubscriber.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvcreatebufferedsubscriber.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVCreateBufferedSubscriber

int CNVCreateBufferedSubscriber (const char *networkVariablePathname, CNVStatusCallback statusCallback, void *callbackData, int clientBufferMaxItems, int waitTime, intptr_t reserved, CNVBufferedSubscriber *bufferedSubscriber);

#### Purpose

Creates a client-buffered subscriber connection to the network variable that you specify with the **networkVariablePathName** parameter.

When the status of the established connection changes, the **statusCallback** function is called with the new status. Connection status changes occur when there is a significant network delay and [NI-PSP](../../cvi/libref/cvinetworkvariables.htm#nipsp) attempts to reconnect.

When the value of the network variable changes, it is automatically sent to the client and buffered. You can get the buffered values of the network variable by calling [CNVGetDataFromBuffer](../../cvi/libref/cvicnvgetdatafrombuffer.htm). When the subscription is successful, the buffer contains the current value of the variable; if the variable is uninitialized and does not have a value, the buffer contains data of type CNVEmpty.

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| networkVariablePathname | const char * | Pathname of the network variable to connect. The format of the pathname is \\\\machineName\\processName\\folderNames\\variableName, which is similar to the format of items on network shares and is not case-sensitive. The following list shows examples of pathnames: \\\\localhost\\my_process\\my_folder1\\my_folder2\\my_variable \\\\test_machine\\my_process\\my_sub_process\\my_variable \\\\192.168.1.100\\my_process\\my_variable \\\\test_machine.my_network.com\\my_process\\my_variable \\\\localhost\\System\\DAQmx\\Server Polling Rate \\\\localhost\\system\\my_variable You can explicitly create and configure your variables using the NI Distributed System Manager that ships with LabWindows/CVI or using the Configuration Functions in the Network Variable Library. You also can use previously created explicit variables. If you specify a new variable name in the system process, as shown in the last example, then the Network Variable Library creates a variable implicitly. Implicit variables can hold values of any type, always have the single-writer restriction, and do not support server-side buffering. The Network Variable Library automatically deletes an implicit variable when all of its clients disconnect, that is, when there are no outstanding connections to it. Carefully decide whether to use implicit or explicit variables depending on your application and deployment needs. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify \\\\localhost\\process'Name\\variable.Name as a URL, enter the following: 'process''Name' as the process name 'variable.Name' as the variable name The resulting URL is \\\\localhost\\\\'process''Name'\\'variable.Name'. This rule does not apply to computer names. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify \\\\localhost\\process'Name\\variable.Name as a URL, enter the following: 'process''Name' as the process name 'variable.Name' as the variable name The resulting URL is \\\\localhost\\\\'process''Name'\\'variable.Name'. This rule does not apply to computer names. |  |
| statusCallback | CNVStatusCallback | The function that the library calls when the connection status of a successfully created network variable changes. Connection status events occur when there is a significant network delay and NI-PSP attempts to reconnect. The library calls this function asynchronously in a worker thread. You can pass NULL if you do not want this notification. The function you pass in this parameter must have the following prototype: void CVICALLBACK Callback (void * handle, CNVConnectionStatus status, int error, void * callbackData); Upon entry to the callback, the handle parameter contains the handle of the connection that is generating the event. The status parameter contains the status of the connection. The error parameter indicates any errors in the connection. The callbackData parameter of the callback contains the value you provide in the callbackData parameter of this function. Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |
|  | Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |  |
| callbackData | void * | The callback data that the library passes to the associated callback functions. |
| clientBufferMaxItems | int | Maximum number of items to hold in the client buffer. This value must be greater than one. Note that multiple connections to the same URL share resources within a program. So, in your program, if another connection to the same URL has specified a client buffer that is larger, then the larger value will apply. |
| waitTime | int | Number of milliseconds the library waits for this operation to complete. Pass CNVWaitForever to wait indefinitely. |
| reserved | intptr_t | You must pass zero. This parameter is reserved for future use. |
| Output |  |  |
| Name | Type | Description |
| bufferedSubscriber | CNVBufferedSubscriber | Returns a handle that you can use to identify this network variable connection in subsequent function calls. Call CNVDispose to dispose the handle when you are done using it. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVCreateBufferedSubscriber function:

- networkvariable\Buffering\NVBuffering.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Polling\NVPolling.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvcreatebufferedwriter.htm language=enus -->
## TOPIC 00177: CNVCreateBufferedWriter

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvcreatebufferedwriter.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvcreatebufferedwriter.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVCreateBufferedWriter

int CNVCreateBufferedWriter (const char *networkVariablePathname, CNVDataTransferredCallback dataTransferredCallback, CNVStatusCallback statusCallback, void *callbackData, int clientBufferMaxItems, int waitTime, intptr_t reserved, CNVBufferedWriter *bufferedWriter);

#### Purpose

Creates a buffered writer connection to the network variable that you specify with the **networkVariablePathName** parameter.

The **dataTransferredCallback** function is called when the buffered data is transferred to the server.

When the status of the established connection changes, the **statusCallback** function is called with the new status. Connection status events occur when there is a significant network delay and [NI-PSP](../../cvi/libref/cvinetworkvariables.htm#nipsp) attempts to reconnect.

You can buffer data to be written to the network variable by calling [CNVPutDataInBuffer](../../cvi/libref/cvicnvputdatainbuffer.htm). The system automatically writes the buffered data to the network variable. This can be more efficient than a synchronous write operation because the latter can require two network operations while this requires only one.

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| networkVariablePathname | const char * | Pathname of the network variable to connect. The format of the pathname is \\\\machineName\\processName\\folderNames\\variableName, which is similar to the format of items on network shares and is not case-sensitive. The following list shows examples of pathnames: \\\\localhost\\my_process\\my_folder1\\my_folder2\\my_variable \\\\test_machine\\my_process\\my_sub_process\\my_variable \\\\192.168.1.100\\my_process\\my_variable \\\\test_machine.my_network.com\\my_process\\my_variable \\\\localhost\\System\\DAQmx\\Server Polling Rate \\\\localhost\\system\\my_variable You can explicitly create and configure your variables using the NI Distributed System Manager that ships with LabWindows/CVI or using the Configuration Functions in the Network Variable Library. You also can use previously created explicit variables. If you specify a new variable name in the system process, as shown in the last example, then the Network Variable Library creates a variable implicitly. Implicit variables can hold values of any type, always have the single-writer restriction, and do not support server-side buffering. The Network Variable Library automatically deletes an implicit variable when all of its clients disconnect, that is, when there are no outstanding connections to it. Carefully decide whether to use implicit or explicit variables depending on your application and deployment needs. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify \\\\localhost\\process'Name\\variable.Name as a URL, enter the following: 'process''Name' as the process name 'variable.Name' as the variable name The resulting URL is \\\\localhost\\\\'process''Name'\\'variable.Name'. This rule does not apply to computer names. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify \\\\localhost\\process'Name\\variable.Name as a URL, enter the following: 'process''Name' as the process name 'variable.Name' as the variable name The resulting URL is \\\\localhost\\\\'process''Name'\\'variable.Name'. This rule does not apply to computer names. |  |
| dataTransferredCallback | CNVDataTransferredCallback | The function that the library calls when the server receives and synchronizes the published data. The library calls this function asynchronously in a worker thread. You can pass NULL if you do not want this notification. The function you pass in this parameter must have the following prototype: void CVICALLBACK Callback(void * handle, int error, void * callbackData); Upon entry to the callback, the handle parameter contains the handle of the connection that is generating the event. The error parameter contains any error that occurred while publishing the network variable data. The callbackData parameter contains the value you provide in the callbackData parameter of this function. Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |
|  | Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |  |
| statusCallback | CNVStatusCallback | The function that the library calls when the connection status of a successfully created network variable changes. Connection status events occur when there is a significant network delay and NI-PSP attempts to reconnect. The library calls this function asynchronously in a worker thread. You can pass NULL if you do not want this notification. The function you pass in this parameter must have the following prototype: void CVICALLBACK Callback (void * handle, CNVConnectionStatus status, int error, void * callbackData); Upon entry to the callback, the handle parameter contains the handle of the connection that is generating the event. The status parameter contains the status of the connection. The error parameter indicates any errors in the connection. The callbackData parameter of the callback contains the value you provide in the callbackData parameter of this function. Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |
|  | Note Return from this function as soon as possible to avoid blocking other network variable events and operations. If needed, you can use PostDeferredCallToThread to process this event on a different thread. From within this callback function, you must also avoid calling the Network Variable Library to create or dispose connections and browsers, get or put buffered data, read or write data, get or set connection attributes, and browse for variables to prevent deadlocks. |  |
| callbackData | void * | The callback data that the library passes to the associated callback functions. |
| clientBufferMaxItems | int | Maximum number of items to hold in the client buffer. This value must be greater than one. Note that multiple connections to the same URL share resources within a program. So, in your program, if another connection to the same URL has specified a client buffer that is larger, then the larger value will apply. |
| waitTime | int | Number of milliseconds the library waits for this operation to complete. Pass CNVWaitForever to wait indefinitely. |
| reserved | intptr_t | You must pass zero. This parameter is reserved for future use. |
| Output |  |  |
| Name | Type | Description |
| bufferedWriter | CNVBufferedWriter | Returns a handle that you can use to identify this network variable connection in subsequent function calls. Call CNVDispose to dispose the handle when you are done using it. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVCreateBufferedWriter function:

- networkvariable\Polling\NVPolling.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Publisher\NVPublisher.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvdeleteprocess.htm language=enus -->
## TOPIC 00178: CNVDeleteProcess

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvdeleteprocess.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvdeleteprocess.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVDeleteProcess

int CNVDeleteProcess (const char *processName);

#### Purpose

Deletes the network variable process with the name you specify.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| processName | const char * | The name of the network variable process. Note National Instruments recommends using only alphanumeric characters in process names. You cannot use the backslash (\\) character or the following words, which are reserved by the Network Variable Library, in processName: system, FP, LV, or NI_. Reserved process names are not case-sensitive. This function returns an error if you use any of these reserved words or the backslash character. |
|  | Note National Instruments recommends using only alphanumeric characters in process names. You cannot use the backslash (\\) character or the following words, which are reserved by the Network Variable Library, in processName: system, FP, LV, or NI_. Reserved process names are not case-sensitive. This function returns an error if you use any of these reserved words or the backslash character. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the CNVDeleteProcess function:

- apps\chess\chess.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Configurator\configurator.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\NVConfig\nvconfig.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvdeletevariable.htm language=enus -->
## TOPIC 00179: CNVDeleteVariable

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvdeletevariable.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvdeletevariable.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVDeleteVariable

int CNVDeleteVariable (const char *parentPath, const char *variableName);

#### Purpose

Deletes the network variable you specify.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentPath | const char * | The parent's machine-relative path. You can specify a process name or a process name followed by one or more folder names delimited with the backslash path separator. Do not include a trailing backslash in the path. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |  |
| variableName | const char * | The name of the network variable. Note National Instruments recommends using only alphanumeric characters in variable names. |
|  | Note National Instruments recommends using only alphanumeric characters in variable names. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the CNVDeleteVariable function:

- networkvariable\Configurator\configurator.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\NVConfig\nvconfig.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvfinish.htm language=enus -->
## TOPIC 00180: CNVFinish

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvfinish.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvfinish.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVFinish

void CNVFinish (void);

#### Purpose

Uninitializes the Network Variable Library.

|  | Note You must call this function after your program is done using the Network Variable Library to discard and clean up global resources. If you do not call this function after calling other functions in the Network Variable Library, your program might hang or crash when it closes and LabWindows/CVI might not be able to report the leaked resources in your program. Additionally, you must not call this function from DllMain, atexit handlers and Network Variable Library callback functions—doing so may cause your application to deadlock and stop responding. |
| --- | --- |

#### Parameters

None.

#### Return Value

None.

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVFinish function:

- networkvariable\Polling\NVPolling.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Quality\NVQuality.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvflushallconnections.htm language=enus -->
## TOPIC 00181: CNVFlushAllConnections

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvflushallconnections.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvflushallconnections.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVFlushAllConnections

int CNVFlushAllConnections (int waitTime);

#### Purpose

Flushes the internal buffers of all connections in your program. This function is useful when you are using a buffered writer connection and you want to force a write at a particular point in time, for example, when you have no additional data to send. The internal buffers are automatically flushed once every 10 milliseconds. This timing is reset when you call this function.

If you are using a non-buffered writer connection, you can flush internal buffers using the [CNVFlushOnWriteAttribute](../../cvi/libref/cnvflushonwriteattribute.html) attribute.

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| waitTime | int | Number of milliseconds the library waits for this operation to complete. Pass CNVWaitForever to wait indefinitely. Pass CNVDoNotWait to return without waiting. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvfolderexists.htm language=enus -->
## TOPIC 00182: CNVFolderExists

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvfolderexists.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvfolderexists.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVFolderExists

int CNVFolderExists (const char *parentPath, const char *folderName, int *exists);

#### Purpose

Indicates whether a particular folder is present in the network variable path you specify.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentPath | const char * | The parent's machine-relative path. You can specify a process name or a process name followed by one or more folder names delimited with the backslash path separator. Do not include a trailing backslash in the path. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |  |
| folderName | const char * | The name of the network variable folder. Note National Instruments recommends using only alphanumeric characters in folder names. |
|  | Note National Instruments recommends using only alphanumeric characters in folder names. |  |
| Output |  |  |
| Name | Type | Description |
| exists | int | Returns whether the folder name exists in the network variable path. A non-zero value indicates that the folder name exists in the network variable path; zero indicates that the folder name does not exist. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvfreememory.htm language=enus -->
## TOPIC 00183: CNVFreeMemory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvfreememory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvfreememory.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVFreeMemory

void CNVFreeMemory (void *pointer);

#### Purpose

Frees memory allocated by the Network Variable Library.

It is not safe to free the same memory more than once. You must set your pointer variable to NULL after freeing the memory it points to.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointer | void * | The pointer to free. This memory must have been allocated by the Network Variable Library. |

#### Return Value

None.

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVFreeMemory function:

- networkvariable\Configurator\configurator.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Quality\NVQuality.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvgetconnectionattribute.htm language=enus -->
## TOPIC 00184: CNVGetConnectionAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvgetconnectionattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvgetconnectionattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVGetConnectionAttribute

int CNVGetConnectionAttribute (void *handle, CNVConnectionAttribute attribute, void *value);

#### Purpose

Obtains the value of a connection attribute for subscriber, reader, writer, and other network variable connections.

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | void * | The handle that identifies the network variable connection. |
| attribute | CNVConnectionAttribute | The connection attribute value you want to obtain. |
| Output |  |  |
| Name | Type | Description |
| value | void * | The value of the specified connection attribute. The data type for this parameter depends on the data type of the attribute you specify for the attribute parameter. Pass the address of a variable of the same data type of the attribute you pass to attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVGetConnectionAttribute function:

- apps\chess\chess.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\3DSim\NV3DSim.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Buffering\NVBuffering.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Quality\NVQuality.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvgetdatafrombuffer.htm language=enus -->
## TOPIC 00185: CNVGetDataFromBuffer

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvgetdatafrombuffer.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvgetdatafrombuffer.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVGetDataFromBuffer

int CNVGetDataFromBuffer (CNVBufferedSubscriber bufferedSubscriber, CNVData *data, CNVBufferDataStatus *dataStatus);

#### Purpose

Gets the next buffered value of a network variable using a buffered subscriber connection.

|  | Note This function is not reliable when the system or variable engine has just started up. This function can only check if the network variable process is configured to run, and so, during system startup may return TRUE even though the network variable process is not fully available. If your program needs to check if a network variable process is available during system startup, National Instruments recommends using the CNVBrowse function to browse the network variable process. |
| --- | --- |

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bufferedSubscriber | CNVBufferedSubscriber | The handle that identifies the network variable buffered reader connection. |
| Output |  |  |
| Name | Type | Description |
| data | CNVData | Handle of the network variable data. Call CNVDisposeData to dispose the handle when you are done using it. CNVGetDataFromBuffer returns zero if there is no data in the buffer. |
| dataStatus | CNVBufferDataStatus | The status of the network variable data. You can pass NULL if you do not want this information. The status can be one of the following values. CNVNewDataThis data item is new. CNVNoDataThe buffer is empty. For example, CNVGetDataFromBuffer returns this status when you read a variable before any value has been written to it. CNVStaleDataThis data item is stale—it is the same data you previously read. CNVGetDataFromBuffer returns the stale data in the data parameter. CNVDataWasLostSome data items were overwritten and lost at this point of your data sequence because the buffer capacity was not large enough to hold all the received data items. CNVGetDataFromBuffer returns this status at the point in your data sequence where the data is missing and not on the first call after the data was lost. CNVGetDataFromBuffer returns the data that overwrote the missing data in the data parameter. |
| CNVNewData | This data item is new. |  |
| CNVNoData | The buffer is empty. For example, CNVGetDataFromBuffer returns this status when you read a variable before any value has been written to it. |  |
| CNVStaleData | This data item is stale—it is the same data you previously read. CNVGetDataFromBuffer returns the stale data in the data parameter. |  |
| CNVDataWasLost | Some data items were overwritten and lost at this point of your data sequence because the buffer capacity was not large enough to hold all the received data items. CNVGetDataFromBuffer returns this status at the point in your data sequence where the data is missing and not on the first call after the data was lost. CNVGetDataFromBuffer returns the data that overwrote the missing data in the data parameter. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVGetDataFromBuffer function:

- networkvariable\Buffering\NVBuffering.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Polling\NVPolling.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvgetdatautctimestamp.htm language=enus -->
## TOPIC 00186: CNVGetDataUTCTimestamp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvgetdatautctimestamp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvgetdatautctimestamp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVGetDataUTCTimestamp

int CNVGetDataUTCTimestamp (CNVData data, unsigned __int64 *timestamp);

#### Purpose

Gets the timestamp of the data. The timestamp is an unsigned 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601 in UTC. You can use [CNVGetTimestampInfo](../../cvi/libref/cvicnvgettimestampinfo.htm) to get the year, month, day, hour, minute, and second represented by the timestamp.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| data | CNVData | The handle that identifies the network variable data. |
| Output |  |  |
| Name | Type | Description |
| timestamp | unsigned __int64 | The timestamp of the data in Coordinated Universal Time (UTC). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Zero represents successful execution, one indicates that the data does not have timestamp information, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Example

Refer to networkvariable\Quality\NVQuality.cws for an example of using the CNVGetDataUTCTimestamp function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvgeterrordescription.htm language=enus -->
## TOPIC 00187: CNVGetErrorDescription

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvgeterrordescription.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvgeterrordescription.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVGetErrorDescription

const char *CNVGetErrorDescription (int errorCode);

#### Purpose

Returns the [error message](../../cvi/libref/cvinetvar_error_codes.htm) associated with the Network Variable Library error code specified in the **errorCode** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorCode | int | An error code returned by a Network Variable Library function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| errorDescription | const char * | The error message associated with the error code. Do not modify or free this string. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVGetErrorDescription function:

- networkvariable\Polling\NVPolling.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Publisher\NVPublisher.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvgetregisteredmachines.htm language=enus -->
## TOPIC 00188: CNVGetRegisteredMachines

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvgetregisteredmachines.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvgetregisteredmachines.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVGetRegisteredMachines

int CNVGetRegisteredMachines (char ***registeredMachines, unsigned int *numberOfRegisteredMachines);

#### Purpose

Gets the computers registered for browsing on the current system.

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| registeredMachines | char ** | Returns an array containing the computers registered for browsing. CNVGetRegisteredMachines allocates memory for the array. The numberOfRegisteredMachines parameter returns the length of the allocated array. You must free each element of this array and the array itself using CNVFreeMemory. |
| numberOfRegisteredMachines | unsigned int | The number of machines registered for browsing. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvgetvariableattribute.htm language=enus -->
## TOPIC 00189: CNVGetVariableAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvgetvariableattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvgetvariableattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVGetVariableAttribute

int CNVGetVariableAttribute (const char *parentPath, const char *variableName, CNVVariableAttribute attribute, void *value);

#### Purpose

Obtains the value of a network variable attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentPath | const char * | The parent's machine-relative path. You can specify a process name or a process name followed by one or more folder names delimited with the backslash path separator. Do not include a trailing backslash in the path. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |  |
| variableName | const char * | The name of the network variable. Note National Instruments recommends using only alphanumeric characters in variable names. |
|  | Note National Instruments recommends using only alphanumeric characters in variable names. |  |
| attribute | CNVVariableAttribute | The network variable attribute value to obtain. |
| Output |  |  |
| Name | Type | Description |
| value | void * | The value of the specified network variable attribute. The data type for this parameter depends on the data type of the attribute you specify for the attribute parameter. Pass the address of a variable of the same data type of the attribute you pass to attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to networkvariable\Configurator\configurator.cws for an example of using the CNVGetVariableAttribute function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvgetvariables.htm language=enus -->
## TOPIC 00190: CNVGetVariables

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvgetvariables.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvgetvariables.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVGetVariables

int CNVGetVariables (const char *parentPath, char ***variables, int *numberOfVariables);

#### Purpose

Obtains the names of the variables in the network variable path you specify.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentPath | const char * | The parent's machine-relative path. You can specify a process name or a process name followed by one or more folder names delimited with the backslash path separator. Do not include a trailing backslash in the path. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |  |
| Output |  |  |
| Name | Type | Description |
| variables | char ** | Returns an array containing the names of the variables in the specified variable path. CNVGetVariables allocates memory for the array. The numVariables parameter returns the length of the allocated array. You must free each element of this array and the array itself using CNVFreeMemory. |
| numberOfVariables | int | The number of variables in the specified network variable path. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvnewfolder.htm language=enus -->
## TOPIC 00191: CNVNewFolder

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvnewfolder.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvnewfolder.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVNewFolder

int CNVNewFolder (const char *parentPath, const char *folderName);

#### Purpose

Creates a new folder in the network variable path you specify.

If you specify a **folderName** that already exists, CNVNewFolder returns an error.

|  | Note This library may return CNVDisconnectedError if you browse folders created after creating the network variable browser. If you need to create folders and browse them, National Instruments recommends that you create the browser after you create the folders. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentPath | const char * | The parent's machine-relative path. You can specify a process name or a process name followed by one or more folder names delimited with the backslash path separator. Do not include a trailing backslash in the path. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |  |
| folderName | const char * | The name of the network variable folder. Note National Instruments recommends using only alphanumeric characters in folder names. |
|  | Note National Instruments recommends using only alphanumeric characters in folder names. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

#### Example

Refer to networkvariable\NVConfig\nvconfig.cws for an example of using the CNVNewFolder function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvnewprocess.htm language=enus -->
## TOPIC 00192: CNVNewProcess

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvnewprocess.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvnewprocess.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVNewProcess

int CNVNewProcess (const char *processName);

#### Purpose

Creates a new network variable process with the name you specify. LabWindows/CVI creates the process in the stopped state. You must start the process by calling the [CNVStartProcess](../../cvi/libref/cvicnvstartprocess.htm) function before reading from or writing to the variables in the process.

If you specify a **processName** that already exists, CNVNewProcess returns an error.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| processName | const char * | The name of the network variable process. Note National Instruments recommends using only alphanumeric characters in process names. You cannot use the backslash (\\) character or the following words, which are reserved by the Network Variable Library, in processName: system, FP, LV, or NI_. Reserved process names are not case-sensitive. This function returns an error if you use any of these reserved words or the backslash character. |
|  | Note National Instruments recommends using only alphanumeric characters in process names. You cannot use the backslash (\\) character or the following words, which are reserved by the Network Variable Library, in processName: system, FP, LV, or NI_. Reserved process names are not case-sensitive. This function returns an error if you use any of these reserved words or the backslash character. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the CNVNewProcess function:

- apps\chess\chess.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Configurator\configurator.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\NVConfig\nvconfig.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvnewvariablecollection.htm language=enus -->
## TOPIC 00193: CNVNewVariableCollection

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvnewvariablecollection.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvnewvariablecollection.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVNewVariableCollection

int CNVNewVariableCollection (const char *parentPath, size_t numberOfVariables, const char * variableNames[], unsigned int maxBufferItems, int singleWriter);

#### Purpose

Creates variables in the network variable path you specify. If you specify a **variableName** that already exists, CNVNewVariableCollection overwrites the existing variables.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentPath | const char * | The parent's machine-relative path. You can specify a process name or a process name followed by one or more folder names delimited with the backslash path separator. Do not include a trailing backslash in the path. Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |
|  | Note National Instruments recommends that you use only alphanumeric characters in process, folder, and variable names. If the name contains single quotation mark ('), backslash (\\), period (.), newline (\\n), or carriage return (\\r) characters, you must escape these characters by enclosing the name in single quotation marks. If the contains single quotation mark characters, you also must precede that character with another single quotation mark. For example, to specify process'Name\\folder.Name as a path, enter the following: 'process''Name' as the process name 'folder.Name' as the folder name Thus, the value you specify for parentPath is 'process''Name\\'folder.Name'. |  |
| numberOfVariables | size_t | The number of variables to create. |
| variableNames | const char *[] | The names of the variables to create. Note National Instruments recommends using only alpha-numeric characters in variable names. |
|  | Note National Instruments recommends using only alpha-numeric characters in variable names. |  |
| maxBufferItems | unsigned int | The maximum number of items to buffer on the server for each of the variables. |
| singleWriter | int | Specify whether the variables must have the single-writer restriction. Specify a nonzero value or select Yes in the function panel if the variables must have the single-writer restriction. Specify 0 or select No in the function panel otherwise. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvprocessisrunning.htm language=enus -->
## TOPIC 00194: CNVProcessIsRunning

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvprocessisrunning.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvprocessisrunning.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVProcessIsRunning

int CNVProcessIsRunning (const char *processName, int *isRunning);

#### Purpose

Indicates whether a network variable process is running.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| processName | const char * | The name of the network variable process. Note National Instruments recommends using only alphanumeric characters in process names. You cannot use the backslash (\\) character or the following words, which are reserved by the Network Variable Library, in processName: system, FP, LV, or NI_. Reserved process names are not case-sensitive. This function returns an error if you use any of these reserved words or the backslash character. |
|  | Note National Instruments recommends using only alphanumeric characters in process names. You cannot use the backslash (\\) character or the following words, which are reserved by the Network Variable Library, in processName: system, FP, LV, or NI_. Reserved process names are not case-sensitive. This function returns an error if you use any of these reserved words or the backslash character. |  |
| Output |  |  |
| Name | Type | Description |
| isRunning | int | Returns the state of the network variable process. A non-zero value indicates that the network variable process is running; zero indicates that the process is not running. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to networkvariable\Configurator\configurator.cws for an example of using the CNVProcessIsRunning function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvputdatainbuffer.htm language=enus -->
## TOPIC 00195: CNVPutDataInBuffer

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvputdatainbuffer.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvputdatainbuffer.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVPutDataInBuffer

int CNVPutDataInBuffer (CNVBufferedWriter bufferedWriter, CNVData data, int bufferWaitTime);

#### Purpose

Puts data to write to a network variable in the buffer of a buffered writer connection. If the buffer is full, this function waits until **bufferWaitTime** milliseconds have elapsed. The system automatically writes the buffered data to the network variable.

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bufferedWriter | CNVBufferedWriter | The handle that identifies the network variable buffered writer connection. |
| data | CNVData | The handle that identifies the network variable data. |
| bufferWaitTime | int | Number of milliseconds the Network Variable Library waits if the buffer is full. Pass CNVWaitForever to wait indefinitely. Pass CNVDoNotWait to return immediately with an error if the buffer is full. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the CNVPutDataInBuffer function:

- networkvariable\3DSim\NV3DSim.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- networkvariable\Polling\NVPolling.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvreadasync.htm language=enus -->
## TOPIC 00196: CNVReadAsync

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvreadasync.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvreadasync.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVReadAsync

int CNVReadAsync (CNVAsyncReader asynchronousReader);

#### Purpose

Asynchronously reads the value of a network variable using an asynchronous reader connection.

When the asynchronous read operation completes, the data callback function for this connection is called with the read value. The first time you call this function, it reads the value the network variable had when the asynchronous reader connected to it. On subsequent calls, this function reads new values of the network variable.

|  | Note The throughput rate of data with reader and asynchronous reader connections is slower than with subscriber and buffered subscriber connections. If throughput rate is critical to your application, consider using a subscriber or buffered subscriber connection instead. |
| --- | --- |

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

|  | Note In this operation, the library flushes all network variable connections in your program for better performance. This also affects writer connections by flushing any pending data. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| asynchronousReader | CNVAsyncReader | The handle that identifies the network variable asynchronous reader connection. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvregistermachine.htm language=enus -->
## TOPIC 00197: CNVRegisterMachine

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvregistermachine.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvregistermachine.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVRegisterMachine

int CNVRegisterMachine (const char *machine);

#### Purpose

Registers a computer for browsing on the current system.

|  | Note To avoid deadlocks, do not call this function in a network variable callback function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| machine | const char * | The name or IP address of the computer. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Example

Refer to networkvariable\Browser\NVBrowser.cws for an example of using the CNVRegisterMachine function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicnvsetarraydatavalue.htm language=enus -->
## TOPIC 00198: CNVSetArrayDataValue

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicnvsetarraydatavalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicnvsetarraydatavalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CNVSetArrayDataValue

int CNVSetArrayDataValue (CNVData data, CNVDataType type, const void *array, size_t numberOfDimensions, size_t dimensions[]);

#### Purpose

Sets the specified array in the network variable data. Currently, this function does not support setting string arrays with a number of dimensions greater than two.

Note that different programming environments may interpret multidimensional arrays in different formats. For example, two-dimensional arrays can be interpreted in row-major or column-major formats. This can affect the dimensions and data of multidimensional arrays communicated between different programming environments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| data | CNVData | The handle that identifies the network variable data. |
| type | CNVDataType | The type of the specified network variable data. Note that CNVBool refers to a 1-byte boolean type (char or unsigned char), and CNVString refers to a C-style NUL-terminated string. |
| array | const void * | An array of the type specified by the type parameter to set in the network variable data. The length of the array you pass for this parameter must be greater than or equal to the value specified by the dimensions parameter. The Network Variable Library treats this parameter as a flat, contiguous block of memory and reads the elements in row-major order. |
| numberOfDimensions | size_t | The number of dimensions of the network variable array data. |
| dimensions | size_t[] | The array dimensions of the network variable data. The length of the array you pass for this parameter must be greater than or equal to the value specified by the numberOfDimensions parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. One indicates that a next item was found, zero indicates that a next item was not found, and a negative number indicates that an error occurred. You can call CNVGetErrorDescription to obtain a string that describes the error. |

#### Additional Information

**Library:** [Network Variable Library](../../cvi/libref/cvinetwork_variable_library_function_tree.htm)

**Include file:** cvinetv.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicopy1d.htm language=enus -->
## TOPIC 00199: Copy1D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicopy1d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicopy1d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Copy1D

AnalysisLibErrType Copy1D (double inputArray[], ssize_t numberOfElements, double outputArray[]);

#### Purpose

Copies the elements from one array to another array. 

 

 Use Copy1D to duplicate arrays for in place operations. 

 

 The following example uses the Copy1D function.

double inputArray[10], outputArray[10]; 

AnalysisLibErrType status; 
 

// Generate an array of random numbers 
 
status = Uniform (10, 17, inputArray); 
 

status = Copy1D (inputArray, 10, outputArray);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | The array to copy. |
| numberOfElements | ssize_t | Number of elements to copy to the output array. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | The copy of the input array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\sigproc\sigproc.cws for an example of using the Copy1D function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicopybytes.htm language=enus -->
## TOPIC 00200: CopyBytes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicopybytes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicopybytes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CopyBytes

void CopyBytes (char targetBuffer[], int targetIndex, char sourceBuffer[], int sourceIndex, size_t numberOfBytes);

#### Purpose

Copies the **numberOfBytes** bytes that start at position **sourceIndex** of **sourceBuffer** to position **targetIndex** of **targetBuffer**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetIndex | int | Zero–based index specifying the location within targetBuffer at which to begin copying bytes. |
| sourceBuffer | char [] | Buffer from which to copy bytes. |
| sourceIndex | int | Zero–based index specifying the location of the bytes to be copied within the source buffer. |
| numberOfBytes | size_t | Number of bytes to copy. |
| Output |  |  |
| Name | Type | Description |
| targetBuffer | char [] | Buffer into which to copy bytes. Note You can use CopyBytes even when sourceBuffer and targetBuffer overlap. |
|  | Note You can use CopyBytes even when sourceBuffer and targetBuffer overlap. |  |

#### Return Value

None.

#### Additional Information

**Library:** [Formatting and I/O Library](../../cvi/libref/cviformatting_and_io_library_functi.htm)

**Include file:** formatio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicopyfile.htm language=enus -->
## TOPIC 00201: CopyFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicopyfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicopyfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CopyFile

int CopyFile (char sourceFileName[], char targetFileName[]);

#### Purpose

Copies the contents of an existing file or group of files to another file or group of files.

If the target file is a directory, CopyFile copies the existing file or group of files into the directory.

|  | Caution The Windows SDK also contains a function with the same name. Include windows.h before including utility.h to ensure that there are no compilation errors as a result of this naming conflict. Define the SDK_CONFLICT_PRIORITYSDK_CONFLICT_PRIORITY macro to force LabWindows/CVI to use the Windows SDK implementation of this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceFileName | char [] | The pathname of the existing file to copy. sourceFileName can contain wildcard characters ? and *, in which case CopyFile copies all matching files. If you specify an empty string "", CopyFile copies the file found by the most recent call to GetFirstFile or GetNextFile. Note The pattern matching behavior of * is greedy and matches all subsequent characters in the pattern except the file extension. The * wildcard is useful only at the end of a filename or file extension; for example, foo*.doc*. If you use this wildcard in other locations, it matches the rest of the string; for example, *foo.txt matches bar.txt. |
|  | Note The pattern matching behavior of * is greedy and matches all subsequent characters in the pattern except the file extension. The * wildcard is useful only at the end of a filename or file extension; for example, foo*.doc*. If you use this wildcard in other locations, it matches the rest of the string; for example, *foo.txt matches bar.txt. |  |
| targetFileName | char [] | The pathname of the target file. targetFileName can contain wildcard characters ? and *, in which case CopyFile matches this parameter to sourceFileName. If the target file is a directory, CopyFile copies the existing file or group of files into the directory. Note The pattern matching behavior of * is greedy and matches all subsequent characters in pattern except the file extension. The * wildcard is useful only at the end of a filename or file extension; for example, foo*.doc*. If you use this wildcard in other locations, it matches the rest of the string; for example, *foo.txt matches bar.txt. |
|  | Note The pattern matching behavior of * is greedy and matches all subsequent characters in pattern except the file extension. The * wildcard is useful only at the end of a filename or file extension; for example, foo*.doc*. If you use this wildcard in other locations, it matches the rest of the string; for example, *foo.txt matches bar.txt. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -1 File not found or directory in path not found. -3 General I/O error occurred. -4 Insufficient memory to complete operation. -5 Invalid path for either of the file names, or source and target file names refer to the same file. -6 Access denied. -7 Specified path is a directory, not a file. -8 Disk is full. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | File not found or directory in path not found. |  |
| -3 | General I/O error occurred. |  |
| -4 | Insufficient memory to complete operation. |  |
| -5 | Invalid path for either of the file names, or source and target file names refer to the same file. |  |
| -6 | Access denied. |  |
| -7 | Specified path is a directory, not a file. |  |
| -8 | Disk is full. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicopystring.htm language=enus -->
## TOPIC 00202: CopyString

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicopystring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicopystring.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CopyString

void CopyString (char targetString[], int targetIndex, char sourceString[], int sourceIndex, ssize_t maximumBytes);

#### Purpose

Copies the string that starts at position **sourceIndex** of **sourceString** to position **targetIndex** of **targetString**. CopyString stops copying when it encounters an ASCII NUL byte or when it has copied **maximum#Bytes** bytes. CopyString appends an ASCII NUL if it did not copy an ASCII NUL.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetIndex | int | Zero–based index specifying the location within the target string at which to begin copying bytes. |
| sourceString | char [] | String from which to copy bytes. |
| sourceIndex | int | Zero–based index specifying the location of the bytes to be copied within the source string. |
| maximumBytes | ssize_t | Specifies the maximum number of bytes, excluding the ASCII NUL, to copy into the target. If you do not want to specify a maximum number of bytes to copy, use –1 for maximum#Bytes. Note This value must be no greater than the number of bytes in the target variable, minus one. |
|  | Note This value must be no greater than the number of bytes in the target variable, minus one. |  |
| Output |  |  |
| Name | Type | Description |
| targetString | char [] | Variable into which to copy bytes. If you want to use maximum#Bytes to prevent writing beyond the end of targetString, make sure to allow room for the ASCII NUL. For example, if maximum#Bytes is 40, the destination buffer should contain at least 41 bytes. Note You can use CopyString even when sourceString and targetString overlap. |
|  | Note You can use CopyString even when sourceString and targetString overlap. |  |

#### Return Value

None.

#### Additional Information

**Library:** [Formatting and I/O Library](../../cvi/libref/cviformatting_and_io_library_functi.htm)

**Include file:** formatio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the CopyString function:

- userint\TimeDateUnits.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\toolbar\tooldemo.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicorrelate.htm language=enus -->
## TOPIC 00203: Correlate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicorrelate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicorrelate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Correlate

*Advanced Analysis Library Only*

AnalysisLibErrType Correlate (double arrayX[], ssize_t sizeOfX, double arrayY[], ssize_t sizeOfY, double outputArray[]);

#### Purpose

|  | Note This function has been superseded by CorrelateEx. CorrelateEx includes an additional parameter, which makes it more versatile than Correlate. |
| --- | --- |

Finds the correlation of the input arrays. Correlate obtains the correlation using the following formula:

[IMAGE alt='image' src='correlate.gif']

y<sub>i</sub> = 0 when j < 0 or j ≥ m

x<sub>i</sub> = 0 when j < 0 or j ≥ n

|  | Note This function temporarily allocates memory for use as a work area. If Correlate cannot allocate memory, the function returns an error code. |
| --- | --- |

##### Example Code

/* Generate two arrays with random numbers and find their correlation. *\/ 

double x[256], y[256], cxy[512]; 

int n, m; 

n = 256; 

m = 256; 

Uniform (n, 17, x); 

Uniform (m, 17, y); 

Correlate (x, n, y, m, cxy);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | double [] | First array to compare using the correlation operation. |
| sizeOfX | ssize_t | Number of elements in arrayX. |
| arrayY | double [] | Second array to compare using the correlation operation. |
| sizeOfY | ssize_t | Number of elements in arrayY. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Correlation array. This array must be at least (n + m – 1) elements long, where n is sizeX and m is sizeY. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

#### Examples

Refer to the following examples that use the Correlate function:

- analysis\correlat.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- analysis\phasedif.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicorrelate2d.htm language=enus -->
## TOPIC 00204: Correlate2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicorrelate2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicorrelate2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Correlate2D

*Advanced Analysis Library Only*

AnalysisLibErrType Correlate2D (void *arrayX, ssize_t m1, ssize_t n1, void *arrayY, ssize_t m2, ssize_t n2, int algorithm, void *outputArray);

#### Purpose

Correlate2D

[IMAGE alt='image' src='correlate2dform_13.png']

for i = -(M<sub>1</sub>–1), ..., -1, 0, 1, ..., (M<sub>2</sub>–1) and j = -(N<sub>1</sub>–1), ..., -1, 0, 1, ..., (N<sub>2</sub>–1) 

 

 where M<sub>1</sub> is the number of rows of matrix **arrayX**, 

 

 N<sub>1</sub> is the number of columns of matrix **arrayX**, 

 

 M<sub>2</sub> is the number of rows of matrix **arrayY**, 

 

 N<sub>2</sub> is the number of columns of matrix **arrayY**, 

 

 the indexed elements outside the ranges of **arrayX** and **arrayY** are equal to zero, as shown in the following relationships:

x(m,n) = 0, m < 0 or m ≥ M<sub>1</sub> or n < 0 or n ≥ N<sub>1</sub>

and

y(m,n) = 0, m < 0 or m ≥ M<sub>2</sub> or n < 0 or n ≥ N<sub>2</sub>.

The elements of the output matrix **outputArray**, represented as R<sub>xy</sub> in the following equation, are related to the elements in h as follows:

R<sub>xy</sub>(i,j) = h(i–(M<sub>1</sub>–1), j–(N<sub>1</sub>–1)) for i = 0, 1, 2, ..., M<sub>1</sub>+M<sub>2</sub>–2 and j = 0, 1, 2, ..., N<sub>1</sub>+N<sub>2</sub>–2.

|  | Note This function temporarily allocates memory for use as a work area. If Correlate2D cannot allocate memory, the function returns an error code. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | void * | First input array. |
| rowsInX | ssize_t | Number of rows in arrayX. |
| columnsInX | ssize_t | Number of columns in arrayX. |
| arrayY | void * | Second input array. |
| rowsInY | ssize_t | Number of rows in arrayY. |
| columnsInY | ssize_t | Number of columns in arrayY. |
| algorithm | int | Specifies the correlation method to use. algorithm must be one of the following values. Note that slight numerical differences can exist between the two methods. Constant Value Description ALGORITHM_CONCOR_DIRECT 0 Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. ALGORITHM_CONCOR_FREQ_DOMAIN 1 Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| Constant | Value | Description |
| ALGORITHM_CONCOR_DIRECT | 0 | Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. |
| ALGORITHM_CONCOR_FREQ_DOMAIN | 1 | Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| Output |  |  |
| Name | Type | Description |
| outputArray | void | The correlation of arrayX and arrayY. The size of outputArray is (m1 + m2 – 1)-by-(n1 + n2 – 1). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicorrelateex.htm language=enus -->
## TOPIC 00205: CorrelateEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicorrelateex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicorrelateex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CorrelateEx

*Advanced Analysis Library Only*

AnalysisLibErrType CorrelateEx (double arrayX[], ssize_t sizeOfX, double arrayY[], ssize_t sizeOfY, int algorithm, double outputArray[]);

#### Purpose

Finds the correlation of the input arrays. National Instruments recommends that you use this function instead of [Correlate](../../cvi/libref/cvicorrelate.htm). CorrelateEx includes an additional parameter, which makes it more versatile than Correlate.

Rxy

t

x

t

y

t

[IMAGE alt='image' src='correlateexform_14.png']

where the symbol [IMAGE alt='image' src='correlateexform_1.png'] denotes correlation. 

 

 The discrete implementation of this function is as follows. Let h represent a sequence whose indexing can be negative, let N be the number of elements in the input sequence **arrayX**, let M be the number of elements in the sequence **arrayY**, and assume that the indexed elements of **arrayX** and **arrayY** that lie outside their range are equal to zero, as shown by the following equations:

x<sub>j</sub> = 0, j < 0 or j ≥ N

and

y<sub>j</sub> = 0, j < 0 or j ≥ M.

CorrelateEx

h

[IMAGE alt='image' src='correlateexform_15.png']

for j = -(N–1), -(N–2), ..., -1, 0, 1, ..., (M–2), (M–1)

outputArray

h

i

i

N

i

N

M

t

N

outputArray

outputArray

CorrelateEx

N

|  | Note This function temporarily allocates memory for use as a work area. If CorrelateEx cannot allocate memory, the function returns an error code. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | double [] | First input array. |
| sizeOfX | ssize_t | Number of elements in arrayX. |
| arrayY | double [] | Second input array. |
| sizeOfY | ssize_t | Number of elements in arrayY. |
| algorithm | int | Specifies the correlation method to use. algorithm must be one of the following values. Note that slight numerical differences can exist between the two methods. Constant Value Description ALGORITHM_CONCOR_DIRECT 0 Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. ALGORITHM_CONCOR_FREQ_DOMAIN 1 Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| Constant | Value | Description |
| ALGORITHM_CONCOR_DIRECT | 0 | Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. |
| ALGORITHM_CONCOR_FREQ_DOMAIN | 1 | Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | The correlation of arrayX and arrayY. This array must be at least (n + m – 1) elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicos.htm language=enus -->
## TOPIC 00206: cos

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicos.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicos.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### cos

double cos (double inputValue);

#### Purpose

Computes the cosine of the specified argument. The argument must be measured in radians.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputValue | double | Contains the argument to the function. This value must be measured in radians. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | Contains the resulting cosine value. This value is valid only if inputValue is measured in radians. The function returns NaN when infinity or an unrepresentable number is used as the argument to the function. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the cos function:

- analysis\nonlnfit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\gridview.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicosh.htm language=enus -->
## TOPIC 00207: cosh

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicosh.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicosh.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### cosh

double cosh (double inputValue);

#### Purpose

Computes the hyperbolic cosine of the specified argument.
If an argument is too large enough to cause the function to return infinity, it also causes a range error.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputValue | double | Contains the argument to the function. If this value is large enough to cause the function to return infinity, it also causes a range error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | Contains the resulting hyperbolic cosine value. If the argument to the function is too large, cosh returns Inf and sets errno to ERANGE. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicoshintegral.htm language=enus -->
## TOPIC 00208: CoshIntegral

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicoshintegral.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicoshintegral.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CoshIntegral

*Advanced Analysis Library Only*

double CoshIntegral (double x);

#### Purpose

Computes the hyperbolic cosine integral, which is defined as follows:

[IMAGE alt='image' src='coshintegralform_36.png']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | The input argument of the hyperbolic cosine integral. Refer to the definition formula for the hyperbolic cosine integral for more information about x. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | The value of the hyperbolic cosine integral. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicosintegral.htm language=enus -->
## TOPIC 00209: CosIntegral

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicosintegral.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicosintegral.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CosIntegral

*Advanced Analysis Library Only*

double CosIntegral (double x);

#### Purpose

Computes the cosine integral, which is defined as follows:

[IMAGE alt='image' src='cosintegralform_34.png']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | The input argument of the cosine integral function. Refer to the definition formula for the cosine integral formula for more information about x. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | The value of the cosine integral. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicostaperedwin.htm language=enus -->
## TOPIC 00210: CosTaperedWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicostaperedwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicostaperedwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CosTaperedWin

*Advanced Analysis Library Only*

AnalysisLibErrType CosTaperedWin (double arrayX[], ssize_t numberOfElements);

#### Purpose

|  | Note This function has been superseded by CosTaperedWinEx. |
| --- | --- |

Applies a cosine-tapered window to the input signal. If Y represents the output sequence, CosTaperedWin obtains the elements of Y from the following formula:

[IMAGE alt='image' src='costapwin.gif']

| where |  |
| --- | --- |
|  | n is the number of elements in arrayX |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in x. |
| Output |  |  |
| Name | Type | Description |
| arrayX | double [] | On input, the input signal. On output, this parameter returns the input signal with a cosine-tapered window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicostaperedwinex.htm language=enus -->
## TOPIC 00211: CosTaperedWinEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicostaperedwinex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicostaperedwinex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CosTaperedWinEx

*Advanced Analysis Library Only*

AnalysisLibErrType CosTaperedWinEx (double arrayX[], ssize_t numberOfElements, double ratio);

#### Purpose

y

arrayX

CosTaperedWinEx

y

[IMAGE alt='image' src='costaperedwinexform_7.png']

where n is the number of elements in **arrayX**, [IMAGE alt='image' src='costaperedwinexform_8.png'], and r is the ratio of the total length of the tapered section to the whole signal length as shown in the following figure: 

 

 
[IMAGE alt='image' src='loc_fp_costapdia.gif']\n\n

If r ≤ 0, the window is equivalent to a rectangular window. If r ≥ 1, the window is equivalent to a Hanning window.

This function performs the window operation in place; that is, the windowed data replaces the input data.

CosTaperedWin

CosTaperedWin

CosTaperedWinEx

ratio

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in arrayX. |
| ratio | double | The ratio of the total length of the tapered section to the whole signal length. The window is a cosine tapered window only if 0 < ratio < 1. If ratio <=0, the window is equivalent to a rectangular window. If ratio >=1, the window is equivalent to a Hanning window. |
| Output |  |  |
| Name | Type | Description |
| arrayX | double [] | On input, the input signal. On output, this parameter returns the input signal with a cosine tapered window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicreateffttable.htm language=enus -->
## TOPIC 00212: CreateFFTTable

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicreateffttable.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicreateffttable.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateFFTTable

*Advanced Analysis Library Only*

PFFTTable CreateFFTTable (ssize_t sizeOfTheFFT);

#### Purpose

Creates a reusable FFT table. You must call [DestroyFFTTable](../../cvi/libref/cvidestroyffttable.htm) to free the table this function creates when the table is no longer needed.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sizeOfTheFFT | ssize_t | The FFT size. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| FFTTable | PFFTTable | The pointer to the created table. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicreateudpchannel.htm language=enus -->
## TOPIC 00213: CreateUDPChannel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicreateudpchannel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicreateudpchannel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateUDPChannel

int CreateUDPChannel (unsigned int localPort, unsigned int *channel);

#### Purpose

Creates a UDP channel object that you can use to send and/or receive UDP datagrams.

You must create a UDP channel object to send or receive any unicast, multicast, or broadcast messages. The new channel can receive messages sent only to the specified port number, though it can send messages to any port.

You must call [DisposeUDPChannel](../../cvi/libref/cvidisposeudpchannel.htm) to free resources when you finish using the channel.

Calling CreateUDPChannel is equivalent to calling [CreateUDPChannelConfig](../../cvi/libref/cvicreateudpchannelconfig.htm) with the following parameters:

CreateUDPChannelConfig (localport, UDP_ANY_ADDRESS, 1, NULL, NULL, channel)

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| localPort | unsigned int | The local port number to open for UDP communication. Applications must agree on the port number(s) to use for communication. According to the Internet Assigned Numbers Authority (IANA), do not use ports in the Well Known (0-1023) or Registered (1024-49151) ranges without IANA registration. Instead, use port numbers in the Dynamic/Private range: 49152-65535. Note Unless you need to listen on a specific port, NI recommends that you configure the UDP Support Library to select a free port by passing UDP_ANY_LOCAL_PORT for this parameter. If you need to specify a particular client port, be sure that it is available for use by your application to avoid conflicting with other TCP/UDP applications that may be using that port. |
|  | Note Unless you need to listen on a specific port, NI recommends that you configure the UDP Support Library to select a free port by passing UDP_ANY_LOCAL_PORT for this parameter. If you need to specify a particular client port, be sure that it is available for use by your application to avoid conflicting with other TCP/UDP applications that may be using that port. |  |
| Output |  |  |
| Name | Type | Description |
| channel | unsigned int | A handle that uniquely identifies a UDP channel object. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Zero indicates successful execution and a negative number indicates that an error occurred. Call the GetUDPErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [UDP Support Library](../../cvi/libref/cviudp_library_function_tree.htm)

**Include file:** udpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the CreateUDPChannel function:

- udp\UDPChat.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- udp\UDPWriter.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicreateudpchannelconfig.htm language=enus -->
## TOPIC 00214: CreateUDPChannelConfig

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicreateudpchannelconfig.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicreateudpchannelconfig.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateUDPChannelConfig

int CreateUDPChannelConfig (unsigned int localPort, const char *localInterfaceAddress, unsigned int exclusive, UDPCallbackPtr callbackFunction, void *callbackData, unsigned int *channel);

#### Purpose

Creates and configures a UDP channel object that you can use to send and/or receive UDP datagrams.

You must create a UDP channel object to send or receive any unicast, multicast, or broadcast messages. The new channel can receive messages sent only to the specified port number, though it can send messages to any port.

You must call [DisposeUDPChannel](../../cvi/libref/cvidisposeudpchannel.htm) to free resources when you finish using the channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| localPort | unsigned int | The local port number to open for UDP communication. Applications must agree on the port number(s) to use for communication. According to the Internet Assigned Numbers Authority (IANA), do not use ports in the Well Known (0-1023) or Registered (1024-49151) ranges without IANA registration. Instead, use port numbers in the Dynamic/Private range: 49152-65535. Note Unless you need to listen on a specific port, NI recommends that you configure the UDP Support Library to select a free port by passing UDP_ANY_LOCAL_PORT for this parameter. If you need to specify a particular client port, be sure that it is available for use by your application to avoid conflicting with other TCP/UDP applications that may be using that port. |
|  | Note Unless you need to listen on a specific port, NI recommends that you configure the UDP Support Library to select a free port by passing UDP_ANY_LOCAL_PORT for this parameter. If you need to specify a particular client port, be sure that it is available for use by your application to avoid conflicting with other TCP/UDP applications that may be using that port. |  |
| localInterfaceAddress | const char * | The local network interface on which this channel will communicate. This parameter is relevant only if the computer has multiple network interface cards. You can pass a string representing the IP address in dot-decimal notation, such as 127.0.0.1, or pass an alphanumeric string representing the host name, such as HAL9000. You also can pass UDP_ANY_ADDRESS, NULL, or an empty string to use any available interfaces. In this case, your channel is assigned a single interface on which to send and receive datagrams. |
| exclusive | unsigned int | A boolean value indicating whether to reserve the port for exclusive use. Passing a non-zero value ensures that no application can open or use the port on the same interface until you dispose of this channel. If the port is already open on the interface, the function fails with the error kUDP_PortInUse. Note If the port is not opened exclusively, it is at risk of being hijacked by another application. For example, if your application monitors port 60000 for messages and another application later opens port 60000 on the same interface, it is possible that the other application will receive all messages arriving at that port and your application will receive none of them. Hijacking also can occur if you open a port on any/all local interfaces (UDP_ANY_ADDRESS) and another application subsequently opens the port on a specific local interface. For these reasons, NI recommends that you open your ports exclusively. Multicast traffic is not subject to hijacking and is always delivered to every subscribed channel. (RT) Ports are not subject to hijacking. |
|  | Note If the port is not opened exclusively, it is at risk of being hijacked by another application. For example, if your application monitors port 60000 for messages and another application later opens port 60000 on the same interface, it is possible that the other application will receive all messages arriving at that port and your application will receive none of them. Hijacking also can occur if you open a port on any/all local interfaces (UDP_ANY_ADDRESS) and another application subsequently opens the port on a specific local interface. For these reasons, NI recommends that you open your ports exclusively. Multicast traffic is not subject to hijacking and is always delivered to every subscribed channel. (RT) Ports are not subject to hijacking. |  |
| callbackFunction | UDPCallbackPtr | Pointer to the callback function that processes messages associated with your UDP channel. Events are sent synchronously to the callback function. The callback function must have the following form: int CVICALLBACK UDPCallback (unsigned channel, int eventType, int errCode, void *callbackData); channel specifies the channel that received the event. eventType specifies the type of event that occurred. UDP_DATAREADY, which is the only supported event, indicates that a datagram has arrived on the channel's port and is waiting to be read. Your program must call UDPRead to obtain the data. Note This event is received once per datagram that arrives. errCode indicates the error, if any, associated with the event. callbackData contains the data that was registered with the callback. |
|  | Note This event is received once per datagram that arrives. |  |
| callbackData | void * | A pointer-width value that the UDP Support Library passes to the callback function each time the library invokes the callback for the same channel. You must define the meaning of the callback data. For example, you can use the parameter as a pointer to a data object that you need to access in the callback function to avoid declaring the data object as a global variable. If you do not need to use the callbackData parameter, you can pass zero. |
| Output |  |  |
| Name | Type | Description |
| channel | unsigned int | A handle that uniquely identifies a UDP channel object. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Zero indicates successful execution and a negative number indicates that an error occurred. Call the GetUDPErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [UDP Support Library](../../cvi/libref/cviudp_library_function_tree.htm)

**Include file:** udpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the CreateUDPChannelConfig function:

- udp\DNSResolver.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- udp\UDPWriter.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicrosspowerspectrum.htm language=enus -->
## TOPIC 00215: CrossPowerSpectrum

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicrosspowerspectrum.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicrosspowerspectrum.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CrossPowerSpectrum

*Advanced Analysis Library Only*

AnalysisLibErrType CrossPowerSpectrum (double xArray[], double yArray[], ssize_t numberOfElements, double dt, double magnitudeSxy[], double phaseSxy[], double *df);

#### Purpose

Calculates the single-sided, scaled cross power spectrum of two time-domain
signals. The following formula defines the cross power spectrum:

[IMAGE alt='image' src='crossspec.gif']

where FFT*[X] is the complex conjugate of FFT[X] and **numberOfElements** is the number of points in the arrays.

This function converts the cross power spectrum to single-sided magnitude and phase spectra.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xArray | double [] | Time-domain signal X. |
| yArray | double [] | Time-domain signal Y. |
| numberOfElements | ssize_t | Number of elements in the input array. Default Value: 1024. |
| dt | double | Sampling period of the time-domain signal, usually in seconds. dt = 1/fs, where fs is the sampling frequency of the time-domain signal. Default Value: 1.0. |
| Output |  |  |
| Name | Type | Description |
| magnitudeSxy | double [] | Single-sided magnitude cross power spectrum between signals XArray and YArray in volts rms square if the input signals are in volts. If the input signals are not in volts, the results are in input signal units rms square. This array must be at least numberOfElements/2 elements long. |
| phaseSxy | double [] | Single-sided phase cross spectrum in radians, showing the difference between the phases of signal YArray and signal XArray. This array must be at least numberOfElements/2 elements long. |
| df | double | Points to the frequency interval, in Hertz, if dt is in seconds. df = 1/(numberOfElements × dt) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicrossspectrum.htm language=enus -->
## TOPIC 00216: CrossSpectrum

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicrossspectrum.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicrossspectrum.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CrossSpectrum

*Advanced Analysis Library Only*

AnalysisLibErrType CrossSpectrum (double xArray[], double yArray[], ssize_t numberOfElements, double realSxy[], double imaginarySxy[]);

#### Purpose

Calculates the double-sided cross power spectrum, Sxy, of the input sequences X and Y according to the following formula:

[IMAGE alt='image' src='crossspec.gif']

where FFT*[X] is the complex conjugate of FFT[X].

The input sequences are copied to internal buffers and zero-padded to **numberOfElements** samples before the FFTs are computed. The output arrays are the real and imaginary parts of the cross spectrum CrossSpectrum.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xArray | double [] | Time-domain signal X. |
| yArray | double [] | Time-domain signal Y. |
| numberOfElements | ssize_t | Number of elements in the input arrays. xArray and yArray must have the same length. |
| Output |  |  |
| Name | Type | Description |
| realSxy | double [] | The real part of the double-sided cross power spectrum between signals X and Y. The size of this array must be at least numberOfElements. |
| imaginarySxy | double [] | Imaginary part of the double-sided cross power spectrum between signals X and Y. The size of this array must be at least numberOfElements. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvictime.htm language=enus -->
## TOPIC 00217: ctime

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvictime.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvictime.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ctime

char *ctime (const time_t *calendarTime);

#### Purpose

Converts the current time to a human-readable string. ctime returns a pointer to the formatted string created by the function.

|  | Note Per the C89 specification, this function and the asctime function return a pointer to the same static array of char. Using these functions in conjunction with each other might result in overwriting the previous value of the timeString parameter. For more information about the C89 specification, refer to an external C89 reference. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| calendarTime | const time_t * | Contains the current calendar time as the number of seconds since January 1, 1900 Coordinated Universal Time (UTC). The function converts this value to a human-readable string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| timeString | char * | Contains a pointer to the newly created human-readable string. The string appears in the following format: Sun Apr 12 05:28:07 1973\\n\\0 |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicubicsplinefit.htm language=enus -->
## TOPIC 00218: CubicSplineFit

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicubicsplinefit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicubicsplinefit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CubicSplineFit

*Advanced Analysis Library Only*

AnalysisLibErrType CubicSplineFit (double arrayX[], double arrayY[], double weight[], ssize_t numberOfElements, double balance, double smoothness[], double fittedData[]);

#### Purpose

Uses cubic spline fitting to fit the data set (x,y). This function fits the data set (x,y) by minimizing

[IMAGE alt='image' src='cubicsplinefitform_0.png']

where [IMAGE alt='image' src='cubicsplinefitform_1.png'] is the cubic spline function, and [IMAGE alt='image' src='cubicsplinefitform_2.png'], for [IMAGE alt='image' src='cubicsplinefitform_3.png']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | double [] | The x value of the input data set (x,y). arrayX must be in ascending order. |
| arrayY | double [] | The y value of the input data set (x,y). If fittedData is NULL, the best fit array overwrites arrayY. |
| weight | double [] | The weight of each data point. If weight is NULL, all weights are assumed to be 1. |
| numberOfElements | ssize_t | The length of arrayX, arrayY, weight, and fittedData. numberOfElements must be greater than or equal to 2. |
| balance | double | The trade-off between the smoothness of the cubic spline fit and the accuracy with which it fits the observations. If balance = 0, the function is the linear fitting. If balance = 1, the function is the spline interpolation. If balance is out of the range [0,1], this function automatically calculates a proper value for balance. |
| smoothness | double [] | Controls the smoothness for each interval between two contiguous data points. The larger the smoothness, the smoother the curve. The length of smoothness must be numberOfElements - 1. If smoothness is NULL, all smoothnesses are assumed to be 1. |
| Output |  |  |
| Name | Type | Description |
| fittedData | double [] | The y values calculated using the cubic spline fitting model. If fittedData is NULL, the best fit array overwrites arrayY. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicurrthreadid.htm language=enus -->
## TOPIC 00219: CurrThreadId

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicurrthreadid.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicurrthreadid.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CurrThreadId

int CurrThreadId (void);

#### Purpose

|  | Note This function has been superseded by CmtGetCurrentThreadID. |
| --- | --- |

Returns the ID of the current thread.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentThreadId | int | The ID of the current thread. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicustom_control_overview.htm language=enus -->
## TOPIC 00220: Custom Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicustom_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicustom_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Edit/Create Custom Controls

You can create custom controls to save control configurations. Custom controls are based on existing user interface controls. LabWindows/CVI saves your list of custom controls between sessions. To use a custom control, select **Create»Custom Controls** and select the control you want to use. You can edit the saved configurations of the custom controls by double-clicking the control name and opening the Edit Control dialog box.

To create a custom control, create a control as you normally would. Select **Create»Custom Controls»Edit** to display the Edit Custom Controls dialog box, which contains the following options:

- Add —Opens a dialog box that contains a list of all the controls on the user interface panel, a preview of the control appearance, and the name that will appear in the Create menu. Select the control you want to add as a custom control and click OK .
- Delete —Removes the selected control from the Create menu.
- Edit —Opens the Edit Control dialog box.
- Edit Name —Opens a dialog box in which you can change the name of the control.
- Code —Opens a dialog box in which you can associate the following files with a control:
  - Program File —A .fp file, source file, or object file that implements additional functionality for the control. When you select Code»Generate»All Code or Generate Custom Control Code , LabWindows/CVI automatically adds the program file to the project. For example, you can specify a .fp file that contains functions to create a new custom control.
  - Header File —The include file that accompanies the program. When you select Code»Generate»All Code or Generate Custom Control Code , LabWindows/CVI includes the header file at the top of the source file.
  - Template File for main —Contains code to instantiate a custom control at run time. 
 The template ( .cct_c ) file has the following structure: 
 
 @CONVERT 
 *CustCtrlCreationFunction* (@REPLACE[panel], @REPLACE[control]); 
 @REVERT 
 *RevertCustCtrlToUICtrlFunction* (@REPLACE[panel], @REPLACE[control]); 
 
 The @CONVERT command calls the function that creates the custom control. When you select Code»Generate All Code or Generate Custom Control Code , the @CONVERT command adds the specified function to the main function after the call to LoadPanel . The @REPLACE command replaces [panel] with the panel handle returned by LoadPanel and replaces [control] with the control ID of the custom control. You also can specify [uirfile] to replace the user interface filename in the code. 

The @REVERT command returns the custom control to the user interface control on which it is based when you place the user interface panel in edit mode. This command is used when you enable Operate in UI Editor and place the user interface panel in operate mode and then place the panel in edit mode.
  - Operate in UI Editor —In operate mode, LabWindows/CVI automatically generates a DLL, which allows the control to behave as it would in a complete application. You can interact with the control in operate mode.
- Move Up —Moves the selected control up one line.
- Move Down —Moves the selected control down one line.
- OK —Accepts the modifications you made in the Edit Custom Controls dialog box and closes the dialog box.
- Cancel —Closes the dialog box without accepting any changes.

LabWindows/CVI provides the following custom controls:

- Ok Button
- Quit Button
- Toolslib Controls—LabWindows/CVI controls configured to provide additional functionality.
  - 3D Graph
  - Animation
  - Color Picker
  - Combo Box
  - File Browser
  - Graph Cursors
  - Hot Ring
  - HyperLink
  - IP
  - Password
  - Path
  - Progress Bar
  - Radio Group
  - NI-DAQmx IO Controls—If you have NI-DAQmx installed, you can select from a list of commonly used NI-DAQmx controls, including a task control, a relay control, and a switch control.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicviabsolutetimefromlocalcalendar.htm language=enus -->
## TOPIC 00221: CVIAbsoluteTimeFromLocalCalendar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicviabsolutetimefromlocalcalendar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicviabsolutetimefromlocalcalendar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVIAbsoluteTimeFromLocalCalendar

int CVIAbsoluteTimeFromLocalCalendar (unsigned int year, unsigned int month, unsigned int day, unsigned int hour, unsigned int minute, unsigned int second, double millisecond, CVIAbsoluteTime *absoluteTime);

#### Purpose

Converts local calendar time components to a LabWindows/CVI absolute time value using the current time zone setting for your system.

This function cannot convert the following Coordinated Universal Time (UTC) time values:

- Time values before the year 1970 on Linux or in applications running on an RT target
- Time values before the year 1601 on Windows operating systems

(RT) You can set time zone settings for RT systems in MAX.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| year | unsigned int | The year in local calendar time. Values before the year 1970 are not supported on Linux or in applications running on an RT target. Values before the year 1601 are not supported on Windows operating systems. |
| month | unsigned int | The month in local calendar time. Valid values are 1 (January) to 12 (December). |
| day | unsigned int | The date of the month in local calendar time. Valid values are 1 to 31. |
| hour | unsigned int | The hour in local calendar time. Valid values are 0 to 23. |
| minute | unsigned int | The minute in local calendar time. Valid values are 0 to 59. |
| second | unsigned int | The second in local calendar time. Valid values are 0 to 59. |
| millisecond | double | The millisecond in local calendar time. You can specify only non-negative values that are less than 1,000. |
| Output |  |  |
| Name | Type | Description |
| absoluteTime | CVIAbsoluteTime | Absolute time value in National Instruments Binary Time Format. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | The result of the function call. Negative values represent errors. The following table describes the results that this function returns. Code Constant Description 0 or positive values — Success. –1 kCVITimeInvalidArgumentError An argument passed to the function is invalid. –2 kCVITimeNullPointerError A NULL pointer was passed to the function instead of a valid memory address. –3 kCVITimeOverflowError A numerical calculation resulted in an overflow. –4 kCVITimeDateOutOfRangeError A time value passed to the function is not in the supported range. –5 kCVITimeOperationFailedError The operation failed due to an unspecified system error. |
| Code | Constant | Description |
| 0 or positive values | — | Success. |
| –1 | kCVITimeInvalidArgumentError | An argument passed to the function is invalid. |
| –2 | kCVITimeNullPointerError | A NULL pointer was passed to the function instead of a valid memory address. |
| –3 | kCVITimeOverflowError | A numerical calculation resulted in an overflow. |
| –4 | kCVITimeDateOutOfRangeError | A time value passed to the function is not in the supported range. |
| –5 | kCVITimeOperationFailedError | The operation failed due to an unspecified system error. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicviabsolutetimetolocalcalendar.htm language=enus -->
## TOPIC 00222: CVIAbsoluteTimeToLocalCalendar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicviabsolutetimetolocalcalendar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicviabsolutetimetolocalcalendar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVIAbsoluteTimeToLocalCalendar

int CVIAbsoluteTimeToLocalCalendar (CVIAbsoluteTime absoluteTime, unsigned int *year, unsigned int *month, unsigned int *day, unsigned int *hour, unsigned int *minute, unsigned int *second, double *millisecond, unsigned int *weekDay);

#### Purpose

Converts an absolute time value to local calendar time components using the current time zone setting for your system. You can pass NULL for one or more of the component output parameters that you do not need.

This function cannot convert the following Coordinated Universal Time (UTC) time values:

- Time values before the year 1970 on Linux or in applications running on an RT target
- Time values before the year 1601 on Windows operating systems.

(RT) You can set time zone settings for RT systems in MAX.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| absoluteTime | CVIAbsoluteTime | Absolute time value in National Instruments Binary Time Format. |
| Output |  |  |
| Name | Type | Description |
| year | unsigned int | The year in local calendar time. |
| month | unsigned int | The month in local calendar time. |
| day | unsigned int | The date of the month in local calendar time. |
| hour | unsigned int | The hour in local calendar time. |
| minute | unsigned int | The minute in local calendar time. |
| second | unsigned int | The second in local calendar time. |
| millisecond | double | The millisecond in local calendar time. |
| weekDay | unsigned int | The day of the week. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | The result of the function call. Negative values represent errors. The following table describes the results that this function returns. Code Constant Description 0 or positive values — Success. –1 kCVITimeInvalidArgumentError An argument passed to the function is invalid. –2 kCVITimeNullPointerError A NULL pointer was passed to the function instead of a valid memory address. –3 kCVITimeOverflowError A numerical calculation resulted in an overflow. –4 kCVITimeDateOutOfRangeError A time value passed to the function is not in the supported range. –5 kCVITimeOperationFailedError The operation failed due to an unspecified system error. |
| Code | Constant | Description |
| 0 or positive values | — | Success. |
| –1 | kCVITimeInvalidArgumentError | An argument passed to the function is invalid. |
| –2 | kCVITimeNullPointerError | A NULL pointer was passed to the function instead of a valid memory address. |
| –3 | kCVITimeOverflowError | A numerical calculation resulted in an overflow. |
| –4 | kCVITimeDateOutOfRangeError | A time value passed to the function is not in the supported range. |
| –5 | kCVITimeOperationFailedError | The operation failed due to an unspecified system error. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

#### Example

Refer to utility\clock.cws for an example of using the CVIAbsoluteTimeToLocalCalendar function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvidynamicmemoryinfo.htm language=enus -->
## TOPIC 00223: CVIDynamicMemoryInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvidynamicmemoryinfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvidynamicmemoryinfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVIDynamicMemoryInfo

int CVIDynamicMemoryInfo (const char message[], size_t *allocatedBlocks, size_t *allocatedBytes, unsigned int options);

#### Purpose

Returns information about dynamic memory allocated by the following ANSI C library functions: [malloc](../../cvi/libref/cvimalloc.htm), [calloc](../../cvi/libref/cvicalloc.htm) and [realloc](../../cvi/libref/cvirealloc.htm). The function does not return information about the memory allocated internally in the CVI Run-time Engine.

CVIDynamicMemoryInfo determines the total number of memory blocks allocated and the total number of bytes allocated.

In addition, the function can display this information and additional information for each individual memory block in the debug output window.

Consider [enabling resource tracking](../../cvi/usermanual/prjwindowrestracking.htm)enabling resource tracking if you want to examine dynamic memory and other types of allocated and released resources. Resource tracking is available only in the [LabWindows/CVI Full Development System](../../cvi/basefdsdiffs.htm)LabWindows/CVI Full Development System.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| message | const char [] | A custom message that appears alongside the memory information in the debug output window. This message helps associate a memory dump with the corresponding location in the source code. |
| options | unsigned int | Options to customize the behavior of CVIDynamicMemoryInfo. Currently, the following options are supported: DYNAMIC_MEMORY_SHOW_ALLOCATED_MEMORY—Displays size and content (the first few bytes) of individual memory blocks in the debug output window. DYNAMIC_MEMORY_SHOW_ALLOCATED_MEMORY_SUMMARY—Lists total number and size of all allocated memory blocks in the debug output window. |
| Output |  |  |
| Name | Type | Description |
| allocatedBlocks | size_t | Contains the total number of allocated memory blocks when the function returns. allocatedBlocks can be NULL. |
| allocatedBytes | size_t | Contains the total number of bytes allocated in all memory blocks. allocatedBytess can be NULL. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The return value of this function. CVIDynamicMemoryInfo returns 0 if it completed successfully. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvilowlevelsupportdriverloaded.htm language=enus -->
## TOPIC 00224: CVILowLevelSupportDriverLoaded

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvilowlevelsupportdriverloaded.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvilowlevelsupportdriverloaded.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVILowLevelSupportDriverLoaded

int CVILowLevelSupportDriverLoaded (void);

#### Purpose

|  | Note This function is obsolete. |
| --- | --- |

Indicates whether the LabWindows/CVI low-level support driver was loaded at startup. The following Utility Library functions require the LabWindows/CVI low-level driver:

- inp
- inpw
- inpd
- outp
- outpw
- outpd
- ReadFromPhysicalMemory
- ReadFromPhysicalMemoryEx
- WriteToPhysicalMemory
- WriteToPhysicalMemoryEx
- MapPhysicalMemory
- UnMapPhysicalMemory

|  | Note Most of these functions do not return an error if the low-level support driver is not loaded. To make sure your calls to these functions can execute correctly, call CVILowLevelSupportDriverLoaded at the beginning of your program. |
| --- | --- |

(Linux) This function is not supported.

The LabWindows/CVI libraries automatically load the low-level support driver at startup if it is on disk. The low-level support driver ships with LabWindows/CVI. Enable the **Low-Level Support Driver** option on the Edit Installer dialog box [Drivers & Components](../../cvi/usermanual/editinstallerdc.htm)**Drivers & Components** tab to include the driver with your stand-alone executables or DLLs.

|  | Note The low-level support driver is not supported on 64-bit systems. Only applications running with administrator privileges on 32-bit systems can load the low-level support driver. |
| --- | --- |

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| lowLevelDriverLoaded | int | Indicates whether the LabWindows/CVI low-level support driver was loaded at startup. Code Description 1 Low-level support driver was loaded at startup. 0 Low-level support driver was not loaded at startup. |
| Code | Description |  |
| 1 | Low-level support driver was loaded at startup. |  |
| 0 | Low-level support driver was not loaded at startup. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicviprofgetcurrentthreadprofiling.htm language=enus -->
## TOPIC 00225: CVIProfGetCurrentThreadProfiling

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicviprofgetcurrentthreadprofiling.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicviprofgetcurrentthreadprofiling.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVIProfGetCurrentThreadProfiling

int CVIProfGetCurrentThreadProfiling (int *state);

#### Purpose

Gets the profiling state in the calling thread. This function only affects LabWindows/CVI applications built with [profiling enabled](../../cvi/usermanual/prjbuildopt.htm)profiling enabled.

|  | Notes You must install the LabWindows/CVI Execution Profiler Toolkit to profile LabWindows/CVI applications. The LabWindows/CVI Execution Profiler Toolkit can only profile source code compiled with the LabWindows/CVI compiler. Profiling source code compiled with third-party compilers is not supported. |
| --- | --- |

(Linux) This function is not supported.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| state | int | Pass the address of an integer variable to get the profile state of the calling thread. A non-zero output value indicates that profiling is enabled in the calling thread and zero indicates that profiling is disabled in the calling thread. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Result of the function call. Code Description 0 Operation completed successfully. -1 Memory allocation failed in the Execution Profiler. -2 An invalid argument was passed to the Execution Profiler. -3 An invalid NULL pointer was passed to the Execution Profiler. -4 Could not initialize the Execution Profiler. -5 An unexpected fatal error occurred in the Execution Profiler. -6 An unexpected error occurred in the Execution Profiler, probably because the program executed a non-local goto (lonjmp). |
| Code | Description |  |
| 0 | Operation completed successfully. |  |
| -1 | Memory allocation failed in the Execution Profiler. |  |
| -2 | An invalid argument was passed to the Execution Profiler. |  |
| -3 | An invalid NULL pointer was passed to the Execution Profiler. |  |
| -4 | Could not initialize the Execution Profiler. |  |
| -5 | An unexpected fatal error occurred in the Execution Profiler. |  |
| -6 | An unexpected error occurred in the Execution Profiler, probably because the program executed a non-local goto (lonjmp). |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicviprofsetcurrentthreadprofiling.htm language=enus -->
## TOPIC 00226: CVIProfSetCurrentThreadProfiling

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicviprofsetcurrentthreadprofiling.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicviprofsetcurrentthreadprofiling.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVIProfSetCurrentThreadProfiling

int CVIProfSetCurrentThreadProfiling (int newState);

#### Purpose

Enables or disables profiling in the calling thread. This function only affects LabWindows/CVI applications built with [profiling enabled](../../cvi/usermanual/prjbuildopt.htm)profiling enabled.

|  | Notes You must install the LabWindows/CVI Execution Profiler Toolkit to profile LabWindows/CVI applications. The LabWindows/CVI Execution Profiler Toolkit can only profile source code compiled with the LabWindows/CVI compiler. Profiling source code compiled with third-party compilers is not supported. Some callback functions are called from library-owned threads. If a callback you expect to be profiled is not appearing in the Profile Viewer, consider calling this function directly from that callback. Function calls that occur when profiling is disabled are not reported in the Profile Viewer. However, if a function enables or disables profiling, that function's reported self time includes the total time of calls that occur even when profiling is disabled. The total time of the enabling/disabling function also reflects calls that occur when profiling is disabled. |
| --- | --- |

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newState | int | Specifies the new profiling state. Specify a nonzero value or select Enabled in the function panel to enable profiling in the calling thread. Pass 0 or select Disabled in the function panel to disable profiling in the calling thread. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Result of the function call. Code Description 0 Operation completed successfully. -1 Memory allocation failed in the Execution Profiler. -2 An invalid argument was passed to the Execution Profiler. -3 An invalid NULL pointer was passed to the Execution Profiler. -4 Could not initialize the Execution Profiler. -5 An unexpected fatal error occurred in the Execution Profiler. -6 An unexpected error occurred in the Execution Profiler, probably because the program executed a non-local goto (lonjmp). |
| Code | Description |  |
| 0 | Operation completed successfully. |  |
| -1 | Memory allocation failed in the Execution Profiler. |  |
| -2 | An invalid argument was passed to the Execution Profiler. |  |
| -3 | An invalid NULL pointer was passed to the Execution Profiler. |  |
| -4 | Could not initialize the Execution Profiler. |  |
| -5 | An unexpected fatal error occurred in the Execution Profiler. |  |
| -6 | An unexpected error occurred in the Execution Profiler, probably because the program executed a non-local goto (lonjmp). |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

#### Examples

Refer to the following examples that use the CVIProfSetCurrentThreadProfiling function:

- profiler\PriorityInversion.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- profiler\sort.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- profiler\search.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvirtehasbeendetached.htm language=enus -->
## TOPIC 00227: CVIRTEHasBeenDetached

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvirtehasbeendetached.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvirtehasbeendetached.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVIRTEHasBeenDetached

int CVIRTEHasBeenDetached (void);

#### Purpose

Indicates whether the operating system has detached the LabWindows/CVI Run-Time Engine from your executable process. The operating system detaches the run-time engine from a process in the following cases:

- The process terminates.
- The process dynamically unloads a DLL that uses the run-time engine, and the process does not directly link to the run-time engine.

You might need to use CVIRTEHasBeenDetached if you call LabWindows/CVI library functions in response to a PROCESS_DETACH message in the DllMain function of a DLL. In some cases, the operating system sends a PROCESS_DETACH message to the LabWindows/CVI Run-Time Engine before it sends a PROCESS_DETACH message to your DLL. When the LabWindows/CVI Run-Time Engine receives a PROCESS_DETACH message, it releases all the system resources it has acquired. When, in response to the PROCESS_DETACH message, your DLL calls LabWindows/CVI library functions that assume the system resources are still present, a general protection fault occurs.

A similar case occurs when you call the atexit function in a DLL to register a routine for the ANSI C library to execute when your DLL unloads. The ANSI C library calls your routine when the DLL receives a PROCESS_DETACH message. This can occur after the LabWindows/CVI Run-Time Engine receives a PROCESS_DETACH message. If your registered function calls LabWindows/CVI library functions that assume the system resources are still present, a general protection fault occurs.

To prevent such problems, call LabWindows/CVI functions from the PROCESS_DETACH code and registered functions in your DLL only if CVIRTEHasBeenDetached returns 0.

##### Example Code

int myPanel = 0;

int CreatePanel (void) 

 {

if ((myPanel = LoadPanel (0, "my.uir", MY_PANEL) < 0)

return 0;

atexit (CleanupPanels) 

 return 1;

}

static void CleanupPanels (void) 

 {

if ( ! CVIRTEHasBeenDetached())

if (panel > 0)

DiscardPanel(myPanel);

}

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| runTimeEngineDetached | int | 1 = The run-time engine has already received the PROCESS_DETACH message. Do not call LabWindows/CVI library functions. 0 = The run-time engine has not yet received a PROCESS_DETACH message. You can safely call LabWindows/CVI library functions. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

#### Example

Refer to dll\basic\cvidll.cws for an example of using the CVIRTEHasBeenDetached function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvitimeintervalfromseconds.htm language=enus -->
## TOPIC 00228: CVITimeIntervalFromSeconds

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvitimeintervalfromseconds.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvitimeintervalfromseconds.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVITimeIntervalFromSeconds

int CVITimeIntervalFromSeconds (double seconds, CVITimeInterval *interval);

#### Purpose

Converts **seconds** to a time interval value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| seconds | double | Double-precision number representing a time interval in seconds. You can specify only values between -LLONG_MAX and LLONG_MAX. LLONG_MAX is the largest 64-bit signed integer value that can be represented. |
| Output |  |  |
| Name | Type | Description |
| interval | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | The result of the function call. Negative values represent errors. The following table describes the results that this function returns. Code Constant Description 0 or positive values — Success. –1 kCVITimeInvalidArgumentError An argument passed to the function is invalid. –2 kCVITimeNullPointerError A NULL pointer was passed to the function instead of a valid memory address. –3 kCVITimeOverflowError A numerical calculation resulted in an overflow. –4 kCVITimeDateOutOfRangeError A time value passed to the function is not in the supported range. –5 kCVITimeOperationFailedError The operation failed due to an unspecified system error. |
| Code | Constant | Description |
| 0 or positive values | — | Success. |
| –1 | kCVITimeInvalidArgumentError | An argument passed to the function is invalid. |
| –2 | kCVITimeNullPointerError | A NULL pointer was passed to the function instead of a valid memory address. |
| –3 | kCVITimeOverflowError | A numerical calculation resulted in an overflow. |
| –4 | kCVITimeDateOutOfRangeError | A time value passed to the function is not in the supported range. |
| –5 | kCVITimeOperationFailedError | The operation failed due to an unspecified system error. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvitimeintervalfromtimeunit.htm language=enus -->
## TOPIC 00229: CVITimeIntervalFromTimeUnit

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvitimeintervalfromtimeunit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvitimeintervalfromtimeunit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVITimeIntervalFromTimeUnit

int CVITimeIntervalFromTimeUnit (CVITimeUnit unit, __int64 value, CVITimeInterval *interval);

#### Purpose

Converts the specified time unit value to a time interval value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| unit | CVITimeUnit | The time unit of the argument you pass to the value parameter. You can specify the following values: Constant Value CVITimeUnitAttoseconds CVITimeUnitBase + 30UL CVITimeUnitFemtoseconds CVITimeUnitBase + 33UL CVITimeUnitPicoseconds CVITimeUnitBase + 36UL CVITimeUnitNanoseconds CVITimeUnitBase + 39UL CVITimeUnit100Nanoseconds CVITimeUnitBase + 41UL CVITimeUnitMicroseconds CVITimeUnitBase + 42UL CVITimeUnitMilliseconds CVITimeUnitBase + 45UL CVITimeUnitSeconds CVITimeUnitBase + 48UL CVITimeUnitMinutes CVITimeUnitBase + 50UL CVITimeUnitHours CVITimeUnitBase + 52UL CVITimeUnitDays CVITimeUnitBase + 54UL CVITimeUnitBase is defined as 919263177UL - 48UL. |
| Constant | Value |  |
| CVITimeUnitAttoseconds | CVITimeUnitBase + 30UL |  |
| CVITimeUnitFemtoseconds | CVITimeUnitBase + 33UL |  |
| CVITimeUnitPicoseconds | CVITimeUnitBase + 36UL |  |
| CVITimeUnitNanoseconds | CVITimeUnitBase + 39UL |  |
| CVITimeUnit100Nanoseconds | CVITimeUnitBase + 41UL |  |
| CVITimeUnitMicroseconds | CVITimeUnitBase + 42UL |  |
| CVITimeUnitMilliseconds | CVITimeUnitBase + 45UL |  |
| CVITimeUnitSeconds | CVITimeUnitBase + 48UL |  |
| CVITimeUnitMinutes | CVITimeUnitBase + 50UL |  |
| CVITimeUnitHours | CVITimeUnitBase + 52UL |  |
| CVITimeUnitDays | CVITimeUnitBase + 54UL |  |
| value | __int64 | The value of the time interval in the specified units. |
| Output |  |  |
| Name | Type | Description |
| interval | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | The result of the function call. Negative values represent errors. The following table describes the results that this function returns. Code Constant Description 0 or positive values — Success. –1 kCVITimeInvalidArgumentError An argument passed to the function is invalid. –2 kCVITimeNullPointerError A NULL pointer was passed to the function instead of a valid memory address. –3 kCVITimeOverflowError A numerical calculation resulted in an overflow. –4 kCVITimeDateOutOfRangeError A time value passed to the function is not in the supported range. –5 kCVITimeOperationFailedError The operation failed due to an unspecified system error. |
| Code | Constant | Description |
| 0 or positive values | — | Success. |
| –1 | kCVITimeInvalidArgumentError | An argument passed to the function is invalid. |
| –2 | kCVITimeNullPointerError | A NULL pointer was passed to the function instead of a valid memory address. |
| –3 | kCVITimeOverflowError | A numerical calculation resulted in an overflow. |
| –4 | kCVITimeDateOutOfRangeError | A time value passed to the function is not in the supported range. |
| –5 | kCVITimeOperationFailedError | The operation failed due to an unspecified system error. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvitimeintervaltofractionalunittime.htm language=enus -->
## TOPIC 00230: CVITimeIntervalToFractionalUnitTime

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvitimeintervaltofractionalunittime.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvitimeintervaltofractionalunittime.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVITimeIntervalToFractionalUnitTime

int CVITimeIntervalToFractionalUnitTime (CVITimeInterval interval, CVITimeUnit unit, CVITimeInterval *fractionalTime);

#### Purpose

Returns the fractional time interval smaller than the time **unit** in the time **interval** value.

For example, this function returns a fractional time interval of 0.2 seconds if the input interval is 1.2 seconds and the time unit is seconds. If you specify milliseconds for the time unit and 1.2 seconds as the input interval, CVITimeIntervalToFractionalUnitTime returns a fractional time interval of 0 milliseconds.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| interval | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |
| unit | CVITimeUnit | The time unit. You can specify the following values: Constant Value CVITimeUnitAttoseconds CVITimeUnitBase + 30UL CVITimeUnitFemtoseconds CVITimeUnitBase + 33UL CVITimeUnitPicoseconds CVITimeUnitBase + 36UL CVITimeUnitNanoseconds CVITimeUnitBase + 39UL CVITimeUnit100Nanoseconds CVITimeUnitBase + 41UL CVITimeUnitMicroseconds CVITimeUnitBase + 42UL CVITimeUnitMilliseconds CVITimeUnitBase + 45UL CVITimeUnitSeconds CVITimeUnitBase + 48UL CVITimeUnitMinutes CVITimeUnitBase + 50UL CVITimeUnitHours CVITimeUnitBase + 52UL CVITimeUnitDays CVITimeUnitBase + 54UL CVITimeUnitBase is defined as 919263177UL - 48UL. |
| Constant | Value |  |
| CVITimeUnitAttoseconds | CVITimeUnitBase + 30UL |  |
| CVITimeUnitFemtoseconds | CVITimeUnitBase + 33UL |  |
| CVITimeUnitPicoseconds | CVITimeUnitBase + 36UL |  |
| CVITimeUnitNanoseconds | CVITimeUnitBase + 39UL |  |
| CVITimeUnit100Nanoseconds | CVITimeUnitBase + 41UL |  |
| CVITimeUnitMicroseconds | CVITimeUnitBase + 42UL |  |
| CVITimeUnitMilliseconds | CVITimeUnitBase + 45UL |  |
| CVITimeUnitSeconds | CVITimeUnitBase + 48UL |  |
| CVITimeUnitMinutes | CVITimeUnitBase + 50UL |  |
| CVITimeUnitHours | CVITimeUnitBase + 52UL |  |
| CVITimeUnitDays | CVITimeUnitBase + 54UL |  |
| Output |  |  |
| Name | Type | Description |
| fractionalTime | CVITimeInterval | The fractional time interval value smaller than the specified time unit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | The result of the function call. Negative values represent errors. The following table describes the results that this function returns. Code Constant Description 0 or positive values — Success. –1 kCVITimeInvalidArgumentError An argument passed to the function is invalid. –2 kCVITimeNullPointerError A NULL pointer was passed to the function instead of a valid memory address. –3 kCVITimeOverflowError A numerical calculation resulted in an overflow. –4 kCVITimeDateOutOfRangeError A time value passed to the function is not in the supported range. –5 kCVITimeOperationFailedError The operation failed due to an unspecified system error. |
| Code | Constant | Description |
| 0 or positive values | — | Success. |
| –1 | kCVITimeInvalidArgumentError | An argument passed to the function is invalid. |
| –2 | kCVITimeNullPointerError | A NULL pointer was passed to the function instead of a valid memory address. |
| –3 | kCVITimeOverflowError | A numerical calculation resulted in an overflow. |
| –4 | kCVITimeDateOutOfRangeError | A time value passed to the function is not in the supported range. |
| –5 | kCVITimeOperationFailedError | The operation failed due to an unspecified system error. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvitimeintervaltoseconds.htm language=enus -->
## TOPIC 00231: CVITimeIntervalToSeconds

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvitimeintervaltoseconds.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvitimeintervaltoseconds.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVITimeIntervalToSeconds

int CVITimeIntervalToSeconds (CVITimeInterval interval, double *seconds);

#### Purpose

Converts a time interval value to seconds.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| interval | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |
| Output |  |  |
| Name | Type | Description |
| seconds | double | Double-precision number representing a time interval in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | The result of the function call. Negative values represent errors. The following table describes the results that this function returns. Code Constant Description 0 or positive values — Success. –1 kCVITimeInvalidArgumentError An argument passed to the function is invalid. –2 kCVITimeNullPointerError A NULL pointer was passed to the function instead of a valid memory address. –3 kCVITimeOverflowError A numerical calculation resulted in an overflow. –4 kCVITimeDateOutOfRangeError A time value passed to the function is not in the supported range. –5 kCVITimeOperationFailedError The operation failed due to an unspecified system error. |
| Code | Constant | Description |
| 0 or positive values | — | Success. |
| –1 | kCVITimeInvalidArgumentError | An argument passed to the function is invalid. |
| –2 | kCVITimeNullPointerError | A NULL pointer was passed to the function instead of a valid memory address. |
| –3 | kCVITimeOverflowError | A numerical calculation resulted in an overflow. |
| –4 | kCVITimeDateOutOfRangeError | A time value passed to the function is not in the supported range. |
| –5 | kCVITimeOperationFailedError | The operation failed due to an unspecified system error. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicvitimeintervaltotimeunit.htm language=enus -->
## TOPIC 00232: CVITimeIntervalToTimeUnit

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicvitimeintervaltotimeunit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicvitimeintervaltotimeunit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CVITimeIntervalToTimeUnit

int CVITimeIntervalToTimeUnit (CVITimeInterval interval, CVITimeUnit unit, CVITimeRoundMethod rounding, __int64 *value);

#### Purpose

Converts a time interval value to the specified time unit using the specified rounding method.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| interval | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |
| unit | CVITimeUnit | The time unit of the argument you pass to the value parameter. You can specify the following values: Constant Value CVITimeUnitAttoseconds CVITimeUnitBase + 30UL CVITimeUnitFemtoseconds CVITimeUnitBase + 33UL CVITimeUnitPicoseconds CVITimeUnitBase + 36UL CVITimeUnitNanoseconds CVITimeUnitBase + 39UL CVITimeUnit100Nanoseconds CVITimeUnitBase + 41UL CVITimeUnitMicroseconds CVITimeUnitBase + 42UL CVITimeUnitMilliseconds CVITimeUnitBase + 45UL CVITimeUnitSeconds CVITimeUnitBase + 48UL CVITimeUnitMinutes CVITimeUnitBase + 50UL CVITimeUnitHours CVITimeUnitBase + 52UL CVITimeUnitDays CVITimeUnitBase + 54UL CVITimeUnitBase is defined as 919263177UL - 48UL. |
| Constant | Value |  |
| CVITimeUnitAttoseconds | CVITimeUnitBase + 30UL |  |
| CVITimeUnitFemtoseconds | CVITimeUnitBase + 33UL |  |
| CVITimeUnitPicoseconds | CVITimeUnitBase + 36UL |  |
| CVITimeUnitNanoseconds | CVITimeUnitBase + 39UL |  |
| CVITimeUnit100Nanoseconds | CVITimeUnitBase + 41UL |  |
| CVITimeUnitMicroseconds | CVITimeUnitBase + 42UL |  |
| CVITimeUnitMilliseconds | CVITimeUnitBase + 45UL |  |
| CVITimeUnitSeconds | CVITimeUnitBase + 48UL |  |
| CVITimeUnitMinutes | CVITimeUnitBase + 50UL |  |
| CVITimeUnitHours | CVITimeUnitBase + 52UL |  |
| CVITimeUnitDays | CVITimeUnitBase + 54UL |  |
| rounding | CVITimeRoundMethod | The rounding method to apply when converting a time interval value to the specified units. You can specify the following values: Contant Description CVITimeRoundMethodNear Round toward nearest value or if equidistant, round toward even value. CVITimeRoundMethodTruncate Truncate fraction and round toward zero. CVITimeRoundMethodUp Round toward positive infinity. CVITimeRoundMethodDown Round toward negative infinity. |
| Contant | Description |  |
| CVITimeRoundMethodNear | Round toward nearest value or if equidistant, round toward even value. |  |
| CVITimeRoundMethodTruncate | Truncate fraction and round toward zero. |  |
| CVITimeRoundMethodUp | Round toward positive infinity. |  |
| CVITimeRoundMethodDown | Round toward negative infinity. |  |
| Output |  |  |
| Name | Type | Description |
| value | __int64 | The value of the time interval in the specified units. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | The result of the function call. Negative values represent errors. The following table describes the results that this function returns. Code Constant Description 0 or positive values — Success. –1 kCVITimeInvalidArgumentError An argument passed to the function is invalid. –2 kCVITimeNullPointerError A NULL pointer was passed to the function instead of a valid memory address. –3 kCVITimeOverflowError A numerical calculation resulted in an overflow. –4 kCVITimeDateOutOfRangeError A time value passed to the function is not in the supported range. –5 kCVITimeOperationFailedError The operation failed due to an unspecified system error. |
| Code | Constant | Description |
| 0 or positive values | — | Success. |
| –1 | kCVITimeInvalidArgumentError | An argument passed to the function is invalid. |
| –2 | kCVITimeNullPointerError | A NULL pointer was passed to the function instead of a valid memory address. |
| –3 | kCVITimeOverflowError | A numerical calculation resulted in an overflow. |
| –4 | kCVITimeDateOutOfRangeError | A time value passed to the function is not in the supported range. |
| –5 | kCVITimeOperationFailedError | The operation failed due to an unspecified system error. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxadd.htm language=enus -->
## TOPIC 00233: CxAdd

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxadd.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxadd.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxAdd

AnalysisLibErrType CxAdd (double xReal, double xImaginary, double yReal, double yImaginary, double *outputReal, double *outputImaginary);

#### Purpose

Adds two complex numbers, x and y. CxAdd obtains the resulting complex number, z, using the following formulas:

zReal = xReal + yReal

zImg = xImg + yImg

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x_Real | double | Real part of the first complex number to add. Default Value: 0.0 |
| x_Imaginary | double | Imaginary part of the first complex number to add. Default Value: 0.0 |
| y_Real | double | Real part of the second complex number to add. Default Value: 0.0 |
| y_Imaginary | double | Imaginary part of the second complex number to add. Default Value: 0.0 |
| Output |  |  |
| Name | Type | Description |
| output_Real | double | Real part of the result of the complex addition. |
| output_Imaginary | double | Imaginary part of the result of the complex addition. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxadd1d.htm language=enus -->
## TOPIC 00234: CxAdd1D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxadd1d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxadd1d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxAdd1D

AnalysisLibErrType CxAdd1D (double arrayXReal[], double arrayXImaginary[], double arrayYReal[], double arrayYImaginary[], ssize_t numberOfElements, double outputArrayReal[], double outputArrayImag[]);

#### Purpose

Adds two complex 1D arrays. CxAdd1D obtains the i<sup>th</sup> element of the resulting complex array using the following formulas:

outputReal<sub>i</sub> = arrayXReal<sub>i</sub> + arrayYReal<sub>i</sub>

outputImg<sub>i</sub> = arrayXImg<sub>i</sub> + arrayYImg<sub>i</sub>

CxAdd1D can perform the operations in place; that is, the input and output complex arrays can be the same.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX_Real | double [] | Real part of the first array to add. |
| arrayX_Imaginary | double [] | Imaginary part of the first array to add. |
| arrayY_Real | double [] | Real part of the second array to add. |
| arrayY_Imaginary | double [] | Imaginary part of the second array to add. |
| numberOfElements | ssize_t | Number of elements to add. |
| Output |  |  |
| Name | Type | Description |
| outputArray_Real | double [] | Real part of the result of the complex array addition. |
| outputArray_Imag | double [] | Imaginary part of the result of the complex array addition. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxautocorrelate.htm language=enus -->
## TOPIC 00235: CxAutoCorrelate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxautocorrelate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxautocorrelate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxAutoCorrelate

*Advanced Analysis Library Only*

AnalysisLibErrType CxAutoCorrelate (NIComplexNumber inputArray[], ssize_t sizeOfInputArray, int norm, NIComplexNumber outputArray[]);

#### Purpose

Finds the autocorrelation of the complex input array. The autocorrelation Rxx(t) of a function x(t) is defined as the following:

[IMAGE alt='image' src='cxautocorrelateform_16.png']

where the symbol [IMAGE alt='image' src='cxautocorrelateform_1.png'] denotes correlation. 

 

 For the discrete implementation of this function, let Y represent a sequence whose indexing can be negative, let N be the number of elements in the input sequence **inputArray**, and assume that the indexed elements of **inputArray** that lie outside its range are equal to zero, as shown in the following relationship: 

 

 x<sub>j</sub> = 0 , j < 0 or j ≥ N 

 

 Then CxAutoCorrelate obtains the elements of Y using the following equation:

[IMAGE alt='image' src='cxautocorrelateform_2.png']

for j = -(N–1), -(N–2), ..., -1, 0, 1, ..., (N–2), (N–1) 

 

 The elements of the output sequence **outputArray** are related to the elements in the sequence Y by 

 

 Rxx<sub>i</sub> = y<sub>i-(N–1)</sub> 

 

 for i = 0, 1, 2, ..., 2N–2 

 

 Notice that the number of elements in the output sequence **outputArray** is 2N–1. Because you cannot use negative numbers to index LabWindows/CVI arrays, the corresponding correlation value at t = 0 is the Nth element of the output sequence **outputArray**. Therefore, **outputArray** represents the correlation values that CxAutoCorrelate shifts N times in indexing. 

 

 In order to make the autocorrelation calculation more accurate, normalization is required in some situations. This function provides biased and unbiased normalization.

- Biased normalization 
 
 If norm is ALGORITHM_CONCOR_BIASED_NORMALIZATION , LabWindows/CVI applies biased normalization as follows: 
 
 [IMAGE alt='image' src='cxautocorrelateform_3.png'] for j = -(N–1), -(N–2), ..., -1, 0, 1, ..., (N–2), (N–1), and 

 

 R<sub>xx</sub>(biased) = y<sub>i-(N–1)</sub> 

 

 for i = 0, 1, 2, ..., 2N–2
- Unbiased normalization 
 
 If norm is ALGORITHM_CONCOR_UNBIASED_NORMALIZATION , LabWindows/CVI applies unbiased normalization as follows: [IMAGE alt='image' src='cxautocorrelateform_4.png'] for j = -(N–1), -(N–2), ..., -1, 0, 1, ..., (N–2), (N–1), and 

 

 R<sub>xx</sub>(unbiased) = y<sub>i-(N–1)</sub> 

 

 for i = 0, 1, 2, ..., 2N–2

|  | Note This function temporarily allocates memory for use as a work area. If CxAutoCorrelate cannot allocate memory, the function returns an error code. |
| --- | --- |

##### Example Code

/* Generate one array with random numbers and find its autocorrelation. */ 

NIComplexNumber x[256]; 

NIComplexNumber rxx[512]; 

double input[256]; 

int i; 

int n; 

n = 256; 

WhiteNoise (n, 1, 17, input); 

for(i = 0; i < n; i++) 

{

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

CxAutoCorrelate (x, n, ALGORITHM_CORCOR_NO_NORMALIZATION, rxx);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | The input array for which to compute the autocorrelation operation. |
| sizeOfInputArray | ssize_t | Number of elements in inputArray. |
| norm | int | Specifies the normalization method to use to compute the autocorrelation of inputArray. normalization must be one of the following values: Constant Value Description ALGORITHM_CORCOR_NO_NORMALIZATION 0 No normalization is used in the autocorrelation computation. ALGORITHM_CONCOR_UNBIASED_NORMALIZATION 1 Use sizeOfInputArray to normalize the correlation result. ALGORITHM_CONCOR_BIASED_NORMALIZATION 2 Use the number of elements in inputArray for computing Rxx[j] to normalize Rxx[j], j = 0, 1, ..., (2n-2). |
| Constant | Value | Description |
| ALGORITHM_CORCOR_NO_NORMALIZATION | 0 | No normalization is used in the autocorrelation computation. |
| ALGORITHM_CONCOR_UNBIASED_NORMALIZATION | 1 | Use sizeOfInputArray to normalize the correlation result. |
| ALGORITHM_CONCOR_BIASED_NORMALIZATION | 2 | Use the number of elements in inputArray for computing Rxx[j] to normalize Rxx[j], j = 0, 1, ..., (2n-2). |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | The autocorrelation of inputArray. This array must be at least (2n – 1) elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxautocorrelate2d.htm language=enus -->
## TOPIC 00236: CxAutoCorrelate2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxautocorrelate2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxautocorrelate2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxAutoCorrelate2D

*Advanced Analysis Library Only*

AnalysisLibErrType CxAutoCorrelate2D (void *inputArray, ssize_t rowsInArray, ssize_t columnsInArray, void *outputArray);

#### Purpose

Finds the 2D autocorrelation of the complex input array.

CxAutoCorrelate2D computes the two-dimensional autocorrelation using the following equation:

[IMAGE alt='image' src='cxautocorrelate2dform_5.png']

for i = -(M–1), ..., -1, 0, 1, ..., (M–1) and j = -(N–1), ..., -1, 0, 1, ..., (N–1) 

 

 where M is the number of rows of matrix **inputArray**, and N is the number of columns of matrix **inputArray**. The indexed elements of **inputArray** that lie outside its range are equal to zero, as shown in the following relationship: 

 

 x(m,n) = 0 when m < 0 or m ≥ M or n < 0 or n ≥ N

|  | Note This function temporarily allocates memory for use as a work area. If CxAutoCorrelate2D cannot allocate memory, the function returns an error code. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | void * | The input array for which to compute the autocorrelation operation. |
| rowsInArray | ssize_t | Number of rows in inputArray. |
| columnsInArray | ssize_t | Number of columns in inputArray. |
| Output |  |  |
| Name | Type | Description |
| outputArray | void | The autocorrelation of inputArray. The size of outputArray is (2m – 1)-by-(2n – 1). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxautocorrmtrx.htm language=enus -->
## TOPIC 00237: CxAutoCorrMtrx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxautocorrmtrx.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxautocorrmtrx.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxAutoCorrMtrx

*Advanced Analysis Library Only*

AnalysisLibErrType CxAutoCorrMtrx (NIComplexNumber inputArray[], ssize_t numberOfElements, ssize_t order, int method, void *autocorrelation);

#### Purpose

Computes the autocorrelation matrix of the complex input array **inputArray**. CxAutoCorrMtrx obtains the norm using the following formula: 

 

 [IMAGE alt='image' src='cxautocorrmtrxform_0.png'] 

 

 where A is the autocorrelation matrix, R is the data matrix, and s is the normalization factor. R<sup>H</sup> is the conjugate transpose of matrix R. 

 

 If **method** is AUTO_CORR_AUTOCORRELATION, R is a matrix of size (N+k)-by-(k+1) defined as follows.

[IMAGE alt='image' src='cxautocorrmtrxform_1.png']

where x<sub>i</sub> is the i-th element in **inputArray**, N is the length of **inputArray**, and k is the **order**. The normalization factor, s, is equal to N. 

 

 If **method** is AUTO_CORR_PRE_WINDOWED, R is a matrix of size N-by-(k+1) defined as follows.

[IMAGE alt='image' src='cxautocorrmtrxform_2.png']

The normalization factor, s, is equal to N. 

 

 If **method** is AUTO_CORR_POST_WINDOWED, R is a matrix of size N-by-(k+1) defined as follows.

[IMAGE alt='image' src='cxautocorrmtrxform_3.png']

The normalization factor, s, is equal to N. If **method** is AUTO_CORR_COVARIANCE_MATRIX, R is a matrix of size (N-k)-by-(k+1) defined as follows.

[IMAGE alt='image' src='cxautocorrmtrxform_4.png']

The normalization factor, s, is equal to N-k. 

 

 If **method** is AUTO_CORR_MODIFIED_COVARIANCE, R is a matrix of size 2(N-k)-by-(k+1) defined as follows.

[IMAGE alt='image' src='cxautocorrmtrxform_5.png']

where x<sub>i</sub><sup>*</sup> is the complex conjugate of x<sub>i</sub>. The normalization factor, s, is equal to 2*(N-k).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | The input array. |
| numberOfElements | ssize_t | Number of elements in inputArray. |
| order | ssize_t | The order of the autocorrelation. order must be greater than or equal to zero. |
| method | int | The method used to compute the autocorrelation matrix. Specify one of the following methods: Constant Value Description AUTO_CORR_AUTOCORRELATION 0 Compute the autocorrelation matrix. AUTO_CORR_PRE_WINDOWED 1 Compute the pre-windowed autocorrelation matrix. AUTO_CORR_POST_WINDOWED 2 Compute the post-windowed autocorrelation matrix. AUTO_CORR_COVARIANCE_MATRIX 3 Compute the covariance matrix. AUTO_CORR_MODIFIED_COVARIANCE 4 Compute the modified-covariance matrix. |
| Constant | Value | Description |
| AUTO_CORR_AUTOCORRELATION | 0 | Compute the autocorrelation matrix. |
| AUTO_CORR_PRE_WINDOWED | 1 | Compute the pre-windowed autocorrelation matrix. |
| AUTO_CORR_POST_WINDOWED | 2 | Compute the post-windowed autocorrelation matrix. |
| AUTO_CORR_COVARIANCE_MATRIX | 3 | Compute the covariance matrix. |
| AUTO_CORR_MODIFIED_COVARIANCE | 4 | Compute the modified-covariance matrix. |
| Output |  |  |
| Name | Type | Description |
| autocorrelation | void | The autocorrelation matrix of input array inputArray. The size of the autocorrelation is (order + 1)-by-(order + 1). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbarthannwin.htm language=enus -->
## TOPIC 00238: CxBartHannWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbarthannwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbarthannwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBartHannWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxBartHannWin (NIComplexNumber signal[], ssize_t numberOfElements);

#### Purpose

Applies a modified Bartlett-Hann window to a complex signal. If y represents the output sequence **signal**, CxBartHannWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='cxbarthannwinform_0.png']

for i = 0, 1, 2, ..., n – 1, where n is the number of elements in **signal**. 

 

 This function applies an unsymmetrical modified Bartlett-Hann window to the input signal. If you want to apply a symmetrical modified Bartlett-Hann window, call [SymWin](../../cvi/libref/cvisymwin.htm) instead. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in signal. |
| Output |  |  |
| Name | Type | Description |
| signal | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a modified Bartlett-Hann window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbkmanwin.htm language=enus -->
## TOPIC 00239: CxBkmanWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbkmanwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbkmanwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBkmanWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxBkmanWin (NIComplexNumber arrayX[], ssize_t numberOfElements);

#### Purpose

y

arrayX

CxBkmanWin

y

y<sub>i</sub> = x<sub>i</sub>[0.42 - 0.50cos(w) + 0.08cos(2w)]

i

n

n

arrayX

[IMAGE alt='image' src='cxbkmanwinform_1.png']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in arrayX. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a Blackman window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxblkharriswin.htm language=enus -->
## TOPIC 00240: CxBlkHarrisWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxblkharriswin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxblkharriswin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBlkHarrisWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxBlkHarrisWin (NIComplexNumber arrayX[], ssize_t numberOfElements);

#### Purpose

Applies a 3-term Blackman-Harris window to the complex input signal. If y represents the output sequence, CxBlkHarrisWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='blkharwin.gif']

for i = 0, 1, 2, ..., n – 1

where n is the number of elements in **arrayX**.

This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in arrayX. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a Blackman-Harris window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxblkmannuttallwin.htm language=enus -->
## TOPIC 00241: CxBlkmanNuttallWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxblkmannuttallwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxblkmannuttallwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBlkmanNuttallWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxBlkmanNuttallWin (NIComplexNumber arrayX[], ssize_t numberOfElements);

#### Purpose

Applies a Blackman-Nuttall window to a complex signal. If y represents the output sequence, CxBlkmanNuttallWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='cxblkmannuttallwinform_2.png']

for i = 0, 1, 2, ..., n – 1 

 

 where n is the number of elements in **arrayX**. 

 

 This function applies an unsymmetrical Blackman-Nuttall window to the input signal. If you want to apply a symmetrical Blackman-Nuttall window, call [SymWin](../../cvi/libref/cvisymwin.htm) instead. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in arrayX. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a Blackman-Nuttall window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbohmanwin.htm language=enus -->
## TOPIC 00242: CxBohmanWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbohmanwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbohmanwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBohmanWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxBohmanWin (NIComplexNumber signal[], ssize_t numberOfElements);

#### Purpose

Applies a Bohman window to a complex signal. If y represents the output sequence **signal**, CxBohmanWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='cxbohmanwinform_3.png']

for i = 0, 1, 2, ..., n – 1, where n is the number of elements in **signal**. 

 

 This function applies an unsymmetrical Bohman window to the input signal. If you want to apply a symmetrical Bohman window, call [SymWin](../../cvi/libref/cvisymwin.htm) instead. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in signal. |
| Output |  |  |
| Name | Type | Description |
| signal | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a Bohman window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbssl_bpf.htm language=enus -->
## TOPIC 00243: CxBssl_BPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbssl_bpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbssl_bpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBssl_BPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBssl_BPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Bessel bandpass digital filter. CxBssl_BPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random complex signal and filter it using a fifth-order bandpass Bessel filter. The pass band is from 200.0 to 300.0. */ 

 NIComplexNumber x[256], y[256]; 

 double input[256]; 

 double fs, fl, fh; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBssl_BPF (x, n, fs, fl, fh, order, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbssl_bsf.htm language=enus -->
## TOPIC 00244: CxBssl_BSF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbssl_bsf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbssl_bsf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBssl_BSF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBssl_BSF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Bessel bandstop digital filter. CxBssl_BSF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random complex signal and filter it using a fifth-order bandstop Bessel filter. The stop band is from 200.0 to 300.0. */ 

 NIComplexNumber x[256], y[256]; 

 double input[256]; 

 double fs, fl, fh; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBssl_BSF (x, n, fs, fl, fh, order, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbssl_hpf.htm language=enus -->
## TOPIC 00245: CxBssl_HPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbssl_hpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbssl_hpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBssl_HPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBssl_HPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Bessel highpass digital filter. CxBssl_HPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random complex signal and filter it using a fifth-order highpass Bessel filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double fs, fc; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBssl_HPF (x, n, fs, fc, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbssl_lpf.htm language=enus -->
## TOPIC 00246: CxBssl_LPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbssl_lpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbssl_lpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBssl_LPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBssl_LPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Bessel lowpass digital filter. CxBssl_LPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random complex signal and filter it using a fifth-order lowpass Bessel filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double fs, fc; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBssl_LPF (x, n, fs, fc, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbw_bpf.htm language=enus -->
## TOPIC 00247: CxBw_BPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbw_bpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbw_bpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBw_BPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBw_BPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Butterworth bandpass digital filter. CxBw_BPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order bandpass Butterworth filter. The pass band is from 200.0 to 300.0. */ 

 NIComplexNumber x[256], y[256]; 

 double input[256]; 

 double fs, fl, fh; 

 int status; 

 int order; 

 int i; 

 ssize_t n; 
 


 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBw_BPF (x, n, fs, fl, fh, order, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbw_bsf.htm language=enus -->
## TOPIC 00248: CxBw_BSF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbw_bsf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbw_bsf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBw_BSF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBw_BSF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Butterworth bandstop digital filter. CxBw_BSF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order bandstop Butterworth filter. The stop band is from 200.0 to 300.0. */ 

 NIComplexNumber x[256], y[256]; 

 double input[256]; 

 double fs, fl, fh; 

 int order; 

 int status; 

 int i; 

 ssize_t n; 
 


 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBw_BSF (x, n, fs, fl, fh, order, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbw_hpf.htm language=enus -->
## TOPIC 00249: CxBw_HPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbw_hpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbw_hpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBw_HPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBw_HPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Butterworth highpass digital filter. CxBw_HPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random complex signal and filter it using a fifth-order highpass Butterworth filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double fs, fc; 

 int status; 

 int order; 

 int i; 

 ssize_t n; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBw_HPF (x, n, fs, fc, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxbw_lpf.htm language=enus -->
## TOPIC 00250: CxBw_LPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxbw_lpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxbw_lpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxBw_LPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxBw_LPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Butterworth lowpass digital filter. CxBw_LPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random complex signal and filter it using a fifth-order lowpass Butterworth filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double fs, fc; 

 int status; 

 int order; 

 int i; 

 ssize_t n; 
 


 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxBw_LPF (x, n, fs, fc, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| order | int | Filter order. This value must be greater than 0. Default Value: 5. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later
