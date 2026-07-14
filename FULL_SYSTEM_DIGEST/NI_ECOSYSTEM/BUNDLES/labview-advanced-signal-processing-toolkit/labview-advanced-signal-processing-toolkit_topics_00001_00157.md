# NI DOCUMENT BUNDLE: labview-advanced-signal-processing-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-advanced-signal-processing-toolkit start=1 end=157 -->
<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=2d-signal-processing.html language=enus -->
## TOPIC 00001: 2D Signal Processing

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `2d-signal-processing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/2d-signal-processing.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the LabVIEW Wavelet Analysis Tools, you can extend the Discrete Wavelet Transform (DWT) to 2D signal processing.The following figure shows the PR filter bank implementation of the 2D DWT, which applies the filter banks to both rows and columns of an image:129 PR Filter Bank Implementation of 2

### 2D Signal Processing

Using the LabVIEW Wavelet Analysis Tools, you can extend the Discrete Wavelet
 Transform (DWT) to 2D signal processing.

The following figure shows the PR filter bank implementation of the 2D DWT, which applies the
 filter banks to both rows and columns of an image:

Figure 129.

[IMAGE alt='image' src='GUID-7011C5E0-4148-4C4D-875C-9F0864CC1EB5-a5.gif']

As the previous figure shows, when decomposing 2D signals with two-channel PR filter banks, you
 process rows first and then columns. Consequently, one 2D array splits into the
 following four 2D arrays:

- low-low
- low-high
- high-low
- high-high

Each array is one-fourth of the size of the original 2D array.

The following figure shows an example of decomposing and reconstructing an image file with the 2D
 DWT and the inverse 2D DWT:

Figure 130.

[IMAGE alt='image' src='GUID-D15AF5EE-B739-418C-A4FA-BB250BFD4C58-a5.gif']

The source image decomposes into the following four sub-images:

- low_low — Shows an approximation of the source signal with coarse
 resolution.
- low_high — Shows the details at the discontinuities along the column
 direction.
- high_low — Shows the details at the discontinuities along the row
 direction.
- high_high — Shows the details at the discontinuities along the diagonal
 direction.

You can apply the decomposition iteratively to the low_low image to create a multi-level 2D DWT, which produces an approximation of the source signal with coarse resolution. You can determine the appropriate number of decomposition levels for a signal-processing application by evaluating the quality of the decomposition at different levels.

Use the Multiresolution Analysis 2D Express VI to decompose and reconstruct a
 2D signal.

The following figure shows an example of image compression using the 2D DWT with the FBI
 wavelet:

Figure 131.

[IMAGE alt='image' src='GUID-51952FCF-8D74-4B91-B3AF-CBE8585F3D98-a5.gif']

The histogram of the DWT Coefficients plot shows that the majority of the
 DWT coefficients are small, meaning that you can use a small number of large DWT
 coefficients to approximate the image and achieve data compression.

Parent topic:

Discrete Wavelet Transform

Related concepts:

- Discrete Wavelet Transform
- Example: Designing the FBI Wavelet

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=account-for-factors-that-influence-a-syste.html language=enus -->
## TOPIC 00002: Account for Factors that Influence a System

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `account-for-factors-that-influence-a-syste.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/account-for-factors-that-influence-a-syste.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The key to the system identification process is having some knowledge of the system for which you want to identify a model.This knowledge provides the basis for determining which signals are outputs, which in turn determines sensor placement, and which signals are inputs that you can use to excite t

### Account for Factors that Influence a
 System

The key to the system identification process is having some knowledge of the system for
 which you want to identify a model.

This knowledge provides the basis for determining which signals are outputs, which in turn
 determines sensor placement, and which signals are inputs that you can use to excite the
 system. Simple tests might be necessary to determine influences, coupling, time delays,
 and time constants to aid in the modeling effort.

You also must consider signals that are not directly capable of being manipulated but still
 affect the system. You must include those signals as inputs to the system model. For
 example, consider the effect of wind gusts on the pitch dynamics of an airplane. The
 airplane responds in pitch to the elevator angle as a direct input. A wind gust affects
 the pitch of an airplane, which in turn influences the dynamics of the airplane, but the
 wind gust is not directly adjustable. To create an accurate model of the airplane, you
 might want to include wind gusts as an input variable.

Parent topic:

Acquire Data from a System

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=acquire-a-discrete-time-series.html language=enus -->
## TOPIC 00003: Acquire a Discrete Time Series

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `acquire-a-discrete-time-series.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/acquire-a-discrete-time-series.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can sample a continuous time series to form a corresponding discrete time series using data acquisition hardware, such as NI-DAQ devices.Signals from physical systems are typically continuous. These real-world signals, such as earthquake waveforms in earthquake monitoring, vibration signals from

### Acquire a Discrete Time Series

You can sample a continuous time series to form a corresponding discrete time series
 using data acquisition hardware, such as NI-DAQ devices.

Signals from physical systems are typically continuous. These real-world signals, such as
 earthquake waveforms in earthquake monitoring, vibration signals from mechanical
 devices, or Electroencephalogram (EEG) signals, are sampled to form discrete-time
 representations to enable computer processing.

TSA Read from Files

TSA Read from
 Files

Note

Read
 From Measurement File Express

.lvm

Read Waveform from File

Write Waveforms to File

The following section describes the factors that influence the quality of a discrete time series.

#### Factors that Influence a Discrete
 Time Series

To ensure that the obtained discrete time series accurately
 represents the information contained in the original continuous time series, you
 need to consider the following factors when sampling data from a continuous time
 series:

Sampling rate

- Increase the sampling rate until the Nyquist frequency exceeds the highest
 frequency component in the signal
- Apply an external lowpass filter with SCXI models
- Use an inherently bandlimited sensor

Number of samples—The number of samples, or the
 length of a time series, limits how fine the frequency resolution can be. A time
 series with a large number of samples can provide fine frequency resolution. You
 usually specify a necessary number of samples based on the following formula:

N

≥

f

s

∆

f

where

- N is the number of samples
- f s is the sampling rate
- Δ f required minimum frequency resolution

Amplitude resolution—The amplitude of a discrete time
 series for computer processing also is discrete because you usually acquire the time
 series with an A/D converter. Quantization error of the A/D converter is a
 correlated and nonlinear impairment that reduces measurement quality. You must make
 certain that the data has sufficiently fine amplitude resolution.

Parent topic:

Acquire and Preprocess Time Series

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=acquire-and-preprocess-time-series.html language=enus -->
## TOPIC 00004: Acquire and Preprocess Time Series

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `acquire-and-preprocess-time-series.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/acquire-and-preprocess-time-series.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can acquire data from NI data acquisition hardware and software or from files that contain pre-stored data.The first step in time series analysis is to obtain the time series that you want to analyze. After you obtain a time series, you need to perform some preliminary processing to make the raw

### Acquire and Preprocess Time Series

You can acquire data from NI data acquisition hardware and software or from files that
 contain pre-stored data.

The first step in time series analysis is to obtain the time series that you want to analyze.
 After you obtain a time series, you need to perform some preliminary processing to make
 the raw data suitable for further analysis. Use the Time Series
 Analysis VIs to perform data inspection and preprocessing.

- [Acquire a Discrete Time Series](acquire-a-discrete-time-series.html)
- [Preprocess a Discrete Time Series](preprocess-a-discrete-time-series.html)

Parent topic:

Time Series Analysis Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=acquire-data-from-a-system-advanced-signal.html language=enus -->
## TOPIC 00005: Acquire Data from a System

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `acquire-data-from-a-system-advanced-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/acquire-data-from-a-system-advanced-signal.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can acquire dynamic system data by using NI DAQ hardware and software or you can use data from a file on disk.The first step in identifying an unknown system is acquiring data. You can acquire data in the time domain and/or the frequency domain. You must acquire the input and output data of the

### Acquire Data from a System

You can acquire dynamic system data by using NI DAQ hardware and software or you can use
 data from a file on disk.

The first step in identifying an unknown system is acquiring data. You can acquire data in the
 time domain and/or the frequency domain. You must acquire the input and output data of
 the system synchronously and save synchronous input and output data with constant time
 steps. If the input data and the output data are not synchronous, you cannot use the
 data to identify an unknown system.

For verification and validation reasons, you must acquire two sets of input-output data samples
 or split the data into two sets. You use one set of samples to estimate the mathematical
 model of the system. You use the second set of samples to validate the resulting model.
 If the resulting model does not meet the predefined specifications, such as the Mean
 Square Error (MSE), modify the settings and re-verify the resulting model with the data
 sets.

Identifying a system involves a number of choices with regard to the system output signals you
 want to measure and the input signals you want to manipulate. The choices you make about
 how to manipulate system inputs, types of signal conditioning, signal ranges, and
 sampling behavior affect the validity of the model you obtain. You can use different
 modeling techniques on the same experimental data set. However, if the data set does not
 reflect the behavior of interest, you must acquire a more descriptive data set.

Because the system identification process is often an experimental process, the entire process
 often is time consuming and possibly costly. Therefore, you must think about the design
 of process prior to experimenting with various identification techniques.

- [Account for Factors that Influence a System](account-for-factors-that-influence-a-syste.html)
- [Choose a Stimulus Signal](choose-a-stimulus-signal-advanced-signal-pr.html)
- [Select a Sampling Rate](select-a-sampling-rate-advanced-signal-pro.html)
- [Apply an Anti-Aliasing Filter](apply-an-anti-aliasing-filter-advanced-sig.html)

Parent topic:

System Identification Concepts

Related concepts:

- Validate Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=adaptive-spectrogram.html language=enus -->
## TOPIC 00006: Adaptive Spectrogram

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `adaptive-spectrogram.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/adaptive-spectrogram.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The adaptive spectrogram method shares similarities with the Gabor spectrogram method, differing in their respective signal decomposition techniques.The adaptive spectrograms utilize adaptive expansion for signal decomposition, while Gabor spectrograms employ Gabor expansion. Both methods apply the

### Adaptive Spectrogram

The adaptive spectrogram method shares similarities with the Gabor spectrogram
 method, differing in their respective signal decomposition techniques.

The adaptive spectrograms utilize adaptive expansion for signal decomposition, while
 Gabor spectrograms employ Gabor expansion. Both methods apply the Wigner-Ville
 Distribution (WVD). However, the adaptive spectrogram selectively sums WVD contributions
 from individual functions (auto-terms), excluding cross-terms between pairs of
 functions.

The adaptive spectrogram has a fine and adaptive time-frequency resolution because the elementary
 functions of the adaptive expansion have a fine and adaptive time-frequency resolution.
 The time-frequency resolution of the adaptive transform adapts to the signal
 characteristics. The adaptive spectrogram does not include cross-term interference
 because it ignores all the cross-terms. For example, if a signal is composed of
 chirplets, you can use the adaptive spectrogram to depict accurately how the chirplets
 appear in the time-frequency domain.

The computation time of the adaptive spectrogram increases with the size of the data set. Also,
 if the signal has a nonlinear frequency modulation, the adaptive spectrogram might
 include too much distortion because the adaptive expansion approximates the nonlinear
 modulation as a linear combination of chirplets with linear frequency modulation.

Use the TFA Adaptive Spectrogram VI to compute the adaptive spectrogram.

The following figure shows twenty superimposed, simulated chirplets designed to test the
 time-frequency resolution and performance of the adaptive spectrogram. You cannot
 distinguish the separate chirplets in the time-domain representation in the following
 figure:

Figure 41.

[IMAGE alt='image' src='GUID-BF4B9620-A910-4F7B-846B-640B060124DC-a5.gif']

The following figure shows the adaptive spectrogram of the simulated chirplet signal in the
 previous figure:

Figure 42.

[IMAGE alt='image' src='GUID-A51FD7C3-8B12-4CD1-818B-FE2FE28112AD-a5.gif']

All the chirplets in the previous figure are separated clearly, appear compact, and show that the
 adaptive spectrogram has a high and adaptive time-frequency resolution.

The following figure shows the Gabor spectrogram of the simulated chirplet signal when the order
 is 2 and the window length is 256:

Figure 43.

[IMAGE alt='image' src='GUID-BCCF8ED7-8655-4B6F-AF76-A1CC32150703-a5.gif']

1

The Gabor spectrogram in the previous figure has a lower time-frequency resolution than the
 adaptive spectrogram in the figure of the adaptive spectrogram of the simulated chirplet
 signal, and some of the chirplets blend together, which prevents you from separating the
 two signal components.

Parent topic:

Quadratic Time Frequency Analysis Methods

Related concepts:

- Adaptive Transform and Expansion
- Discrete Gabor Transform and Expansion

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=adaptive-transform-and-expansion.html language=enus -->
## TOPIC 00007: Adaptive Transform and Expansion

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `adaptive-transform-and-expansion.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/adaptive-transform-and-expansion.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The adaptive transform, also called the adaptive chirplet decomposition, computes the weight for each elementary chirplet. Because the sinusoid function is a subset of the chirplet, the adaptive transform is more powerful than the Gabor transform but generally requires more computing time.You can us

### Adaptive Transform and Expansion

The adaptive transform, also called the adaptive chirplet decomposition, computes the
 weight for each elementary chirplet. Because the sinusoid function is a subset of the
 chirplet, the adaptive transform is more powerful than the Gabor transform but generally
 requires more computing time.

You can use the inverse Fourier transform and the discrete Gabor expansion to express
 signals as a linear combination of a series of elementary functions. For example, the
 inverse discrete Fourier transform expresses a signal as the linear combination of
 sinusoids in which the weight of each elementary sinusoid is the corresponding discrete
 Fourier coefficient. The discrete Gabor expansion expresses a signal as the linear
 combination of windowed sinusoids with Gabor transform coefficients.

Like the discrete Gabor transform, the adaptive expansion expresses a signal as a linear
 combination of Gaussian-windowed, linear-chirp functions called chirplets.

In the following equation, the adaptive expansion represents a signal,
 s(t), as the linear combination of a series
 elementary functions, h<sub>k</sub>(t),
 approximately:

s

t

≈

∑

k

=

0

D

-

1

A

k

h

k

t

where

- A k is the corresponding complex amplitude of
 h k ( t )
- D specifies the number of the elementary functions

The adaptive transform computes the complex amplitudes, A<sub>k</sub>.

The adaptive transform and the adaptive expansion are unique to the LabVIEW Time Frequency
 Analysis Tools.

Unlike the discrete Gabor expansion and discrete Gabor transform, the elementary
 functions of the adaptive expansion are time-varying signals themselves with spectral
 content that changes linearly over time. The time centers and the frequency centers of
 the chirplets are not limited to a grid in the time-frequency plane, and they can be any
 real value. Also, the window lengths of all the chirplets do not need to be the same.
 Therefore, the adaptive expansion can have a finer time-frequency resolution and express
 time-varying signals more accurately.

#### Matching Pursuit Method

The
 matching pursuit method is a commonly used implementation of the adaptive transform
 that uses a set of elementary functions called a dictionary. The dictionary size in
 the matching pursuit algorithm determines the speed and accuracy of the resulting
 analysis. A small dictionary requires less computing time but has poorer accuracy. A
 large dictionary results in better accuracy but requires more computing time. Refer
 to the *Introduction to Time-Frequency and Wavelet Transforms* section
 for more information about the matching pursuit method.

The TFA
 Adaptive Transform VI provides an implementation of the adaptive
 transform that is more efficient and accurate than the matching pursuit method. This
 implementation uses the matching pursuit method with a small dictionary size as a
 coarse estimation step and then follows with a refinement step to achieve an
 accurate estimation. The small dictionary size and refinement step make the adaptive
 transform in the Time Frequency Analysis Tools more efficient and
 accurate.

The adaptive transform is used widely in applications, such as radar
 and sonar signal processing, that need to accurately estimate parameters of signals
 with time-variant spectra, especially signals that contain chirplets. After you
 detect the adaptive chirplets in a signal, you also can use adaptive chirplets to
 improve the performance of some pattern-recognition applications.

#### Using the Adaptive Transform and
 Adaptive Expansion

The following figure shows the typical steps to create
 an adaptive transform and adaptive expansion application:

Figure 12.

[IMAGE alt='image' src='GUID-8F016616-3B3D-4E1F-9A8F-360E38EDF5F8-a5.gif']

Usually, you use the adaptive transform to compute the magnitudes and parameters
 of chirplets, select the chirplets that you need for the application, and then apply
 the adaptive expansion to reconstruct the signal. In some applications, you might
 use the parameters of chirplets to make a decision before the expansion.

The
 white line in the following figure represents the real parts of a complex-valued
 signal from a pulse radar receiver, and the red line in this figure represents the
 imaginary parts of the signal.

Figure 13.

[IMAGE alt='image' src='GUID-7A69B649-F842-4589-9C0F-BCF98E8D71F9-a5.gif']

Though not apparent in the previous figure, this signal contains three
 signals—the target signature signal and two instances of strong interference from
 sea clutter, which is the radar signal reflected off of surface sea waves. The
 interference signal is much stronger than the target signature signal so you cannot
 see the target signature in the time-domain representation in the previous figure.
 The goal of this application is to remove the interference signal and extract the
 target signature signal.

Because the target signature signal is a
 time-varying chirp signal, first observe the time-frequency representation of the
 signal before selecting a signal processing method to use. The following figure
 shows the STFT magnitude spectrum of the example signal:

Figure 14.

[IMAGE alt='image' src='GUID-E0201E3D-ED0B-4262-9CD5-2EB507724EBD-a5.gif']

The color corresponds to the magnitude of the STFT coefficients. The color
 spectrum from red to blue corresponds to the magnitude from maximum to minimum. The
 red stripes close to 0 Hz are the sea clutter interference. The green stripe running
 diagonally across the interference signal is the target signature signal. Notice
 that the interference signal is stronger than the target signature signal and that
 the interference and the target signature overlap in the time-frequency plane. A
 conventional time-domain fixed filter is not sufficient for separating these
 components. Because the spectral peak of the target signature changes over time and
 the spectral bandwidths of the interference vary over time, you can use the
 TFA Adaptive Transform VI to decompose the signal into a
 linear combination of chirplets. Next, you can remove the resulting chirplets with a
 chirp rate close to zero and a frequency less than 0.02 Hz in this example. Then you
 can use the TFA Adaptive Expansion VI to reconstruct the target
 signature, as shown in the following figure:

Figure 15.

[IMAGE alt='image' src='GUID-AA67EA68-50FB-4780-A57D-48F5FD3D07AF-a5.gif']

Compared to the interference signal in the figure of the complex signal from the
 pulse radar receiver, the sea clutter signal in the previous figure has been
 suppressed up to 20 dB. The following figure shows the STFT magnitude spectrum of
 the extracted target signature with the interference substantially reduced:

Figure 16.

[IMAGE alt='image' src='GUID-8A5526FA-0D04-4E6B-BD80-DCDC487D964F-a5.gif']

If the signal you want to analyze using any linear time-frequency method contains
 a large constant offset or is non-negative, a single line in the vicinity of 0 Hz
 dominates the resulting time-dependent spectrum. In these situations, you might not
 be able to identify more interesting frequency patterns. To suppress the constant
 offset component, you can apply certain types of preprocessing, but the detrending
 methods for removing the constant-offset components depend on the application. No
 general method works in all cases. Common techniques of detrending include lowpass
 filtering and curve fitting. However, another technique is the wavelet
 transform.

Parent topic:

Linear Time Frequency Analysis Methods

Related concepts:

- Introduction to Wavelet Signal Processing
- LabVIEW Advanced Signal Processing Toolkit User Manual

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=analytic-signals.html language=enus -->
## TOPIC 00008: Analytic Signals

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `analytic-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/analytic-signals.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For real-valued signals, the power spectrum has symmetric components at positive frequencies and at negative frequencies. The corresponding analytic signal of the real-valued signal is a complex-valued signal.This topic contains information that applies to the LabVIEW Time Frequency Analysis Tools.

### Analytic Signals

For real-valued signals, the power spectrum has symmetric components at positive
 frequencies and at negative frequencies. The corresponding analytic signal of the
 real-valued signal is a complex-valued signal.

Note

The analytic signal retains the DC component of the real-valued signal, doubles the components
 with positive frequency, and removes the components with negative frequency. The
 following illustrations show the power spectrum of a real-valued signal,
 s(t), and the power spectrum of the
 corresponding analytic signal.

Figure 2.

[IMAGE alt='image' src='GUID-EE3AD59A-EBAC-44E8-A9E2-AAC600E4FE28-a5.gif']

Figure 3.

[IMAGE alt='image' src='GUID-D07F2AAD-3009-4183-A229-900A7417E0E1-a5.gif']

Notice that the power spectrum of the real-valued signal is symmetric about 0 Hz. In comparison,
 the power spectrum of the analytic signal is not symmetric and contains components with
 positive frequency only. Furthermore, the amplitude of the power spectrum of the
 analytic signal with positive frequency is twice the amplitude of the power spectrum of
 the real-valued signal. Whereas the amplitude of the power spectrum of the real-valued
 signal is 40 at 300 Hz, the amplitude of the power spectrum of the corresponding
 analytic signal is 80 at 300 Hz.

Parent topic:

Fundamentals

Related concepts:

- Overview of LabVIEW Time Frequency Analysis Tools

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=analytic-wavelet-transform.html language=enus -->
## TOPIC 00009: Analytic Wavelet Transform

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `analytic-wavelet-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/analytic-wavelet-transform.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Analytic Wavelet Transform (AWT) is a wavelet transform that provides both the magnitude and phase information of signals in the time-scale or time-frequency domain. The magnitude information returned by the AWT describes the envelopes of signals.The phase information encodes the time-related ch

### Analytic Wavelet Transform

The Analytic Wavelet Transform (AWT) is a wavelet transform that provides both the
 magnitude and phase information of signals in the time-scale or time-frequency domain.
 The magnitude information returned by the AWT describes the envelopes of signals.

The phase information encodes the time-related characteristics of signals, for example, the
 location of a cusp. You usually use the magnitude information for time-frequency
 analysis and phase information for applications such as instantaneous frequency
 estimation.

The AWT computes the inner products of the analyzed signal and a set of complex Morlet wavelets.
 This transform is called the analytic wavelet transform because the complex Morlet
 wavelets are analytic, that is, the power spectra of the Morlet wavelets are zero at
 negative frequencies. The resulting AWT coefficients are complex numbers. These
 coefficients measure the similarity between the analyzed signal and the complex Morlet
 wavelets. The AWT is just one type of complex continuous wavelet transform.

#### Scale and
 Frequency

Wavelets are functions of time and scale, so you can consider a
 wavelet transform as a tool that produces a time-scale representation of signals.
 You also can consider the time-scale representation of signals as a time-frequency
 representation, because wavelets with different scales measure the corresponding
 frequency components in the signal. The frequency of a wavelet is inversely
 proportional to the scale factor.

Using the WA Analytic Wavelet
 Transform VI, you can specify different settings for the scale factor
 to compute the AWT. When you set scale sampling method to
 even scale, this VI computes the wavelet coefficients at
 evenly-distributed integer scales. You usually use the even
 scale option to obtain the time-scale representation of a signal.
 When you set scale sampling method to even
 frequency, this VI computes the wavelet coefficients at scales with
 evenly-distributed frequencies. Notice that the scales are not evenly-distributed.
 You usually use the even frequency option to obtain the
 time-frequency representation of a signal.

Because the time and frequency
 resolutions of wavelets are adaptive, the AWT provides adaptive time and frequency
 resolutions. Conventional time-frequency analysis methods, such as the Short-Time
 Fourier Transform (STFT), only provide uniform time and frequency resolutions in the
 whole time-frequency domain.

The following figure shows a common wavelet test
 signal, the HypChirps signal. This signal contains two frequency components, which
 are hyperbolic functions over time. The frequency components change slowly at the
 beginning and rapidly at the end.

Figure 115.

[IMAGE alt='image' src='GUID-06C90D6B-FE8A-495A-87EC-BD1617E04C0F-a5.gif']

The following figure shows two representations of this HypChirps signal in the
 time-frequency domain based on the STFT method:

Figure 116.

[IMAGE alt='image' src='GUID-C8882E0D-C8FC-413E-BE4C-81F72A669CA0-a5.gif']

In the previous figure, if you use a relatively long window, 256, you obtain fine
 frequency resolution and coarse time resolution. Therefore, you can distinguish the
 frequency components of the HypChirps signal at lower frequencies with a long
 window. If you use a short window, 64, you obtain coarse frequency resolution and
 fine time resolution. Therefore, you can distinguish the frequency components of the
 HypChirps signal at higher frequencies with a short window. However, you cannot
 distinguish the two frequency components at both low and high frequencies in either
 of the STFT spectrograms.

The following figure shows the tiling of the
 STFT-based time-frequency representation:

Figure 117.

[IMAGE alt='image' src='GUID-7FAF364F-6BF5-404C-AE8C-C317ECA7210D-a5.gif']

In the previous figure, you can see that the STFT spectrogram has uniform
 time-frequency resolution across the whole time-frequency domain. You can balance
 the time-frequency resolution by adjusting the window length. The left tiling
 diagram provides better frequency resolution in the STFT Spectrogram
 (Window Length = 256) graph of the STFT spectrograms of the
 HypChirps signal. The right tiling diagram shows better time resolution in the
 STFT Spectrogram (Window Length = 64) graph of STFT
 spectrograms of the HypChirps signal. However, you cannot achieve high time
 resolution and frequency resolution simultaneously.

The following figure shows
 the AWT-based time-frequency representation of the HypChirps signal. In the
 Scalogram graph, you can distinguish the two frequency
 components at both low and high frequencies.

Figure 118.

[IMAGE alt='image' src='GUID-0A6A0A09-E403-473B-A180-0557B3DED055-a5.gif']

The following figure shows the tiling of the AWT-based time-frequency
 representation that provides fine frequency resolution at low frequencies and fine
 time resolution at high frequencies:

Figure 119.

[IMAGE alt='image' src='GUID-197D3C2D-EAE0-49F7-93EB-76D0AAD0A4F8-a5.gif']

Similar to the Continuous Wavelet Transform (CWT), the AWT also adds excess
 information redundancy and is computationally intensive. Moreover, you cannot
 reconstruct the original signal from the AWT coefficients.

#### Wavelet Normalization: Energy versus
 Amplitude

In wavelet analysis, wavelets at different scales often have the
 same energy. Because both the center frequency and the bandwidth of a wavelet are
 inversely proportional to the scale factor, the wavelet at a larger scale has a
 higher magnitude response than a wavelet at a smaller scale. The following figure
 shows the Fourier magnitude spectra of different wavelets with energy
 normalization:

Figure 120.

[IMAGE alt='image' src='GUID-685C551D-0F13-4BA6-B3A2-D35A52D33DC7-a5.gif']

However, some real-world applications require that you use a uniform amplitude
 response to measure the exact amplitude of the signal components, as shown in the
 following figure:

Figure 121.

[IMAGE alt='image' src='GUID-A14A1C79-0167-48BD-AD2E-5A7A2352025A-a5.gif']

With the WA Analytic Wavelet Transform VI, you can analyze a
 signal based on amplitude normalization by selecting
 amplitude in the normalization
 list. If you set scale sampling method to even
 frequency and set normalization to
 amplitude, the WA Analytic Wavelet
 Transform VI generates the scalogram of the HypChirps signal, as shown
 in the following figure:

Figure 122.

[IMAGE alt='image' src='GUID-F2F36386-4AE0-4E18-A80F-EDFC0E785155-a5.gif']

Notice that the magnitude at high frequencies (small scales) also has been
 enlarged. With amplitude normalization, you can obtain the precise magnitude
 evolution over time for each hyperbolic chirp.

Parent topic:

Signal Processing with Continuous Wavelets

Related concepts:

- Introduction to Wavelet Signal Processing
- Introduction to Time Frequency Analysis
- Short-Time Fourier Transform

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=analyze-models-advanced-signal-processing-t.html language=enus -->
## TOPIC 00010: Analyze Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `analyze-models-advanced-signal-processing-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/analyze-models-advanced-signal-processing-t.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use model analysis to observe some characteristics, such as frequency response, stability, and order, of dynamic system models.Use the System Identification VIs to analyze the dynamic system models and present the results in Bode plot, the Nyquist plot, and the pole-zero plot graphs.Bode Plo

### Analyze Models

You can use model analysis to observe some characteristics, such as frequency response,
 stability, and order, of dynamic system models.

Use the System Identification VIs to analyze the dynamic system models and
 present the results in Bode plot, the Nyquist plot, and the pole-zero plot graphs.

#### Bode Plot

A Bode plot
 contains a Bode magnitude plot and a Bode phase plot. These two plots together
 describe the frequency response of the dynamic system model you estimate. A Bode
 magnitude plot describes magnitude versus frequency. A Bode phase plot describes
 phase versus frequency. The following figure shows an example of a Bode plot:

Figure 201.

[IMAGE alt='image' src='GUID-61B30275-2089-4612-8BDD-80A626A5B5B7-a5.gif']

The SI Bode Plot VI calculates the upper and lower limits
 according to the confidence level you set. You can obtain information, such as the
 gain of the system and the cutoff frequency, by evaluating the Bode plot. You can
 display the Bode magnitude and phase using the SI Bode Plot
 Indicator.

#### Nyquist Plot

A Nyquist plot
 describes the gain and phase of a frequency response in polar coordinates by
 plotting the imaginary part of the complex frequency response versus the real part.
 In polar coordinates, a Nyquist plot shows the phase as the angle and the magnitude
 as the distance from the origin. You can use the Nyquist plot to predict the
 stability of a system. The following figure shows an example of a Nyquist plot:

Figure 202.

[IMAGE alt='image' src='GUID-2ED841D4-7893-4F37-A84C-8ECF21614283-a5.gif']

The SI Nyquist Plot VI calculates the upper and lower limits
 according to the confidence level you set. You can use the SI Nyquist
 Plot VI to generate the Nyquist plot and display this plot by using
 the SI Nyquist Plot Indicator.

#### Pole-Zero Plot

The
 pole-zero plot displays the poles and zeros of a system. By observing the locations
 of the poles and zeros, you can conclude whether the system is stable. In a stable
 system, all poles are within the unit circle. The following figure shows a pole-zero
 plot of a stable model:

Figure 203.

[IMAGE alt='image' src='GUID-268BD993-A3E3-41F6-92BA-E6ECC050EFFC-a5.gif']

You can use the SI Pole-Zero Plot VI to generate a pole-zero
 plot and display the plot by using the SI Pole-Zero Plot
 Indicator.

You also can use the pole-zero plot to determine if
 you can reduce model orders. By observing the pole-zero placements, you can
 determine if any pole-zero pairs have overlapping confidence intervals. A confidence
 interval is a region the SI Pole-Zero Plot VI calculates from the
 confidence level you set. The existence of overlapping confidence intervals implies
 that pole-zero cancellations exist and that the model order might be unnecessarily
 high. The pole-zero plot shown in the previous figure is an optimal model with the
 appropriate order because the pole-zero pairs do not have overlapping confidence
 intervals.

If the model order is too high, you can try reducing the model
 order. You then can use the F-test criterion to assess if the reduction in model
 order leads to a significant increase in the prediction error. If the reduction in
 model order leads to a significant increase in the prediction error, do not reduce
 the model order.

Parent topic:

Analyze, Validate, and Convert Models

Related concepts:

- Frequency Response

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=analyze-validate-and-convert-models-ad.html language=enus -->
## TOPIC 00011: Analyze, Validate, and Convert Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `analyze-validate-and-convert-models-ad.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/analyze-validate-and-convert-models-ad.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Utilize the System Identification VIs for analyzing, validating, and converting models between different representations.After estimating a model of a dynamic system, you can observe model characteristics by analyzing the model. You also can verify that the model represents the dynamic system by val

### Analyze, Validate, and Convert Models

Utilize the System Identification VIs for analyzing, validating, and
 converting models between different representations.

After estimating a model of a dynamic system, you can observe model characteristics by analyzing
 the model. You also can verify that the model represents the dynamic system by
 validating the model. Use the System Identification VIs to analyze
 and validate models.

According to linear system theory, you can represent a linear system with different models. Each
 model representation has benefits and drawbacks for characterizing a dynamic system.
 Certain model representations are more suitable for certain analysis techniques. You can
 use the System Identification VIs to convert models from
 one representation to another to identify the best-fit model for the system.

- [Analyze Models](analyze-models-advanced-signal-processing-t.html)
- [Validate Models](validate-models-advanced-signal-processing.html)
- [Converting Models](convert-models-advanced-signal-processing.html)

Parent topic:

System Identification Concepts

Related concepts:

- Model Types and Representations

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=application-example-lossless-compression.html language=enus -->
## TOPIC 00012: Application Example: Lossless Compression

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `application-example-lossless-compression.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/application-example-lossless-compression.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Integer Wavelet Transform (IWT) provides lossless compression.When you apply the DWT to integer signal samples, you convert the original integer signal samples to floating-point wavelet coefficients. In signal compression applications, you typically further quantize these coefficients to an inte

### Application Example: Lossless Compression

The Integer Wavelet Transform (IWT) provides lossless compression.

When you apply the DWT to integer signal samples, you convert the original integer signal samples
 to floating-point wavelet coefficients. In signal compression applications, you
 typically further quantize these coefficients to an integer representation before
 entropy-based encoding. As a result, compression with the DWT is lossy, meaning that
 some information is lost when you compress a signal using the DWT, and that you
 typically cannot reconstruct the original signal perfectly from the coefficients of the
 DWT.

You can use the IWT to convert integer signal samples into integer wavelet coefficients, and you
 can compress these integer coefficients by entropy-based encoding without
 further quantization. As a result, you can reconstruct the original signal
 perfectly from a compressed set of IWT coefficients. The following figure
 shows an example of lossless compression with the IWT:

Figure 149.

[IMAGE alt='image' src='GUID-4D48C971-01E5-41C9-A354-12DC1577543F-a5.gif']

In the Histogram graph, most of the elements in the IWT
 Coefficients plot are zero, meaning that you can obtain a high
 compression ratio using the IWT of this image. You can reconstruct the image perfectly
 with the inverse IWT, as shown in the Reconstructed Image graph.
 The Maximum Difference value of 0 indicates that
 the reconstructed image retains all the information of the original image.

Parent topic:

Integer Wavelet Transform

Related concepts:

- Discrete Wavelet Transform
- Integer Wavelet Transform

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=apply-a-lag-window-advanced-signal-process.html language=enus -->
## TOPIC 00013: Apply a Lag Window

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `apply-a-lag-window-advanced-signal-process.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/apply-a-lag-window-advanced-signal-process.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Applying a lag window improves the accuracy of the frequency response estimation.When computing Φ[uu](e^jω) and Φ[uy](e^jω) to obtain the frequency response G(e^jω), you can apply a lag window ω(τ) to the autocorrelation function R[uu] and the cross-correlation function R[uy] before performing the F

### Apply a Lag Window

Applying a lag window improves the accuracy of the frequency response
 estimation.

When computing
 Φ<sub>uu</sub>(e<sup>jω</sup>)
 and
 Φ<sub>uy</sub>(e<sup>jω</sup>)
 to obtain the frequency response
 G(e<sup>jω</sup>), you
 can apply a lag window ω(τ) to the autocorrelation
 function R<sub>uu</sub> and the cross-correlation
 function R<sub>uy</sub> before performing the FFT
 operation. The benefits of applying a lag window are based on the following
 equations:

ϕ

u

u

e

j

ω

=

∑

τ

=

-

N

N

R

u

u

τ

τ

τ

τ

-

j

ω

ω

m

ϕ

u

y

e

j

ω

=

∑

τ

=

-

N

N

R

u

y

τ

τ

τ

τ

-

j

ω

ω

m

The lag window approaches zero when the lag τ is large. The window weighs out
 the points of R<sub>uu</sub> and
 R<sub>uy</sub> with large lag
 τ, thereby improving the accuracy of the
 frequency response estimation. The SI Estimate Frequency
 Response VI uses a Hanning window as the lag window.

The frequency response with the lag window,
 G'(e<sup>jω</sup>),
 is equivalent to the moving average version of the frequency response
 without the lag window,
 G(e<sup>jω</sup>).
 The average smooths the frequency response, but the smooth frequency
 response also can deviate from the true frequency response. Adjusting the
 length of the lag window can balance the trade-off between variance and bias
 of the frequency response estimation. The larger the length of the lag
 window, the fewer points of
 G(e<sup>jω</sup>)
 the SI Estimate Frequency Response VI averages to compute
 G'(e<sup>jω</sup>),
 and hence the larger the variance and the smaller the bias of the frequency
 estimation.

The following example demonstrates how the length of the lag window affects the frequency
 response estimation. The following figure shows the front panel of a VI that simulates a
 system defined by the following equation:

y(k) – 1.46y(k– 1) + 2.5y(k – 2) – 1.46y(k – 3) + yk – 4 = u(k) + 0.45u(k – 1) + u(k – 2)

Figure 184.

[IMAGE alt='image' src='GUID-CAAB5A1A-CD12-4D77-B336-B7236AFE9742-a5.gif']

The following figure shows the block diagram of this VI:

Figure 185.

[IMAGE alt='image' src='GUID-FB4CA6BD-5FD3-4E99-8E20-1A243FA2F184-a5.gif']

In this example VI, the input signal u(k) is a swept sine
 wave whose normalized frequency is from 0 to 0.5 Hz. The number of data points in the
 input signal is 4096. The length of the lag window therefore must be less than or equal
 to 4096. The following figures show the resulting frequency responses when the window
 length is 4096 and 64, respectively:

Figure 186.

[IMAGE alt='image' src='GUID-E3414E5A-6E36-449F-8921-55B09EAC7250-a5.gif']

Figure 187.

[IMAGE alt='image' src='GUID-4BB840B4-7B5E-42EA-8986-BD4BD9426AA8-a5.gif']

The frequency response curve is smoother and the variance is smaller when the length of the lag
 window is small. However, when the length of the lag window is too small,
 you cannot distinguish between the two close peaks in the frequency
 response, as shown in the previous figure with window length equal to 64.
 When the length of the lag window is large, the SI Estimate
 Frequency Response VI accurately estimates the peaks, as
 shown in the previous figure with window length equal to 4096. The bias is
 small with a large lag window, but the variance of the estimated frequency
 response is large.

Setting the length of the lag window to 5–10% of the number of data points when estimating the
 frequency response often results in a good trade-off between the bias and variance. The
 length also depends on the signals, the properties of the system, and the purpose of
 application. For example, to identify the passband of a system, use a smaller lag
 window. To identify the dynamic properties of a system, such as its natural frequency,
 use a larger lag window.

Parent topic:

Frequency Response

Related concepts:

- Frequency Response

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=apply-an-anti-aliasing-filter-advanced-sig.html language=enus -->
## TOPIC 00014: Apply an Anti-Aliasing Filter

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `apply-an-anti-aliasing-filter-advanced-sig.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/apply-an-anti-aliasing-filter-advanced-sig.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: According to the Nyquist sampling theorem, the sampling rate must be greater than twice the maximum frequency component of the signal of interest. In other words, the maximum frequency of the input signal must be smaller than half the sampling rate.For example, if the maximum frequency component of

### Apply an Anti-Aliasing Filter

According to the Nyquist sampling theorem, the sampling rate must be greater than twice
 the maximum frequency component of the signal of interest. In other words, the maximum
 frequency of the input signal must be smaller than half the sampling rate.

For example, if the maximum frequency component of a signal is 1K Hz, the sampling rate must be
 greater than 2K Hz. In real-world applications, you can set the sampling rate between 3K
 and 5K Hz.

This criterion, in practice, is often difficult to ensure. Even if you are sure that the measured
 signal has an upper limit on its frequency, external factors, such as signals from the
 powerline interference or radio stations, can contain frequencies higher than the
 Nyquist frequency. These frequencies might then alias into the frequency range of
 interest and give you inaccurate results.

To ensure that you limit the frequency content of the input signal, you can add a lowpass filter
 before the sampler and the Analog-to-Digital Converter (ADC). A lowpass filter passes
 low frequencies and attenuates high frequencies. This filter is an anti-aliasing filter
 because by attenuating the frequencies greater than the Nyquist frequency, the filter
 prevents the sampling of aliased components. When you use a filter before the sampler
 and ADC, the anti-aliasing filter is an analog filter with a proper cut-off frequency.
 The cut-off frequency equals the maximum frequency component of the signal of interest.
 Using the anti-aliasing filter satisfies the Nyquist sampling theorem. You must have
 data acquisition hardware that supports anti-aliasing filters to use this filter.

Similarly, you can use a digital filter to remove frequency content above the system bandwidth
 and then downsample the data to the desired sampling rate.

Parent topic:

Acquire Data from a System

Related concepts:

- Filtering and Downsampling

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=ar-model-definitions-advanced-signal-processi.html language=enus -->
## TOPIC 00015: AR Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `ar-model-definitions-advanced-signal-processi.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/ar-model-definitions-advanced-signal-processi.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Autoregressive (AR) model does not include the dynamics between the system input and output. Therefore, the AR model is more suitable for representing signals rather than a system because a system generally has an input and an output.Time series analysis methods, such as power spectrum envelope

### AR Model Definitions

The Autoregressive (AR) model does not include the dynamics between the system input and
 output. Therefore, the AR model is more suitable for representing signals rather than a
 system because a system generally has an input and an output.

Time series analysis methods, such as power spectrum envelope estimation, prewhitening, and
 linear prediction coding, commonly use the AR model.

Use the SI Estimate AR Model VI to estimate AR system models. The following
 equation shows the form of the AR model:

A

z

y

k

=

e

k

where

- y ( k ) represents the system outputs
- e ( k ) is the system disturbance

A(z) is polynomial with respect to the backward shift
 operator z<sup>–1</sup> and defined by the following equation:

A

z

=

1

+

a

1

z

-

1

+

.

.

.

+

a

k

a

z

-

k

a

where k<sub>a</sub> is the model order.

The following figure depicts the signal flow of an AR system model:

Figure 189.

[IMAGE alt='image' src='GUID-AD9D8DF6-81CE-4052-9A59-7A526EABDAB0-a5.gif']

where

- e is the system disturbance
- y represents the system outputs
- A is A ( z )

If you consider A(z) to be a filter,
 A(z)y(k)
 is the filtering of A(z) on the signal
 y(k). The result of the filtering is white
 noise e(k), as shown in the AR model equation.
 Hence, the filter A(z) also is known as the
 prewhitening filter. From the frequency-domain standpoint, the prewhitening filter
 A(z) suppresses the spectrum at frequencies
 where the magnitude of the spectrum is large. Suppressing the high-magnitude frequencies
 results in a flat spectrum.

As shown in the AR model equation, if you know the AR coefficients
 A(z) and the noise
 e(k), you can reconstruct the signal
 y(k).
 A(z) and
 e(k) completely characterize a signal.
 A(z) normally has a small number of
 coefficients. e(k) has a small dynamic range and
 requires a smaller number of bits for encoding. Therefore, you can use the AR model for
 compression purposes in a process known as Linear Prediction Coding (LPC). Speech and
 vibration signal processing methods, such as compression and pattern recognition,
 commonly use LPC. You also can use A(z) and
 e(k) to estimate the power spectrum of the
 signal y(k).

Parent topic:

General-Linear Model Definitions

Related concepts:

- Correlation Analysis Method

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=arma-model-based-prediction.html language=enus -->
## TOPIC 00016: ARMA Model-Based Prediction

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `arma-model-based-prediction.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/arma-model-based-prediction.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can make predictions based on the estimated ARMA model for both univariate and multivariate time series.The ARMA model is a general model that includes both the AR and the MA models. You can apply ARMA model-based prediction to AR or MA model-based prediction by converting an AR or MA model to a

### ARMA Model-Based Prediction

You can make predictions based on the estimated ARMA model for both univariate and
 multivariate time series.

The ARMA model is a general model that includes both the AR and the MA models. You can apply ARMA
 model-based prediction to AR or MA model-based prediction by converting an AR or MA model to
 an ARMA model. Use the TSA ARMA Prediction VI to predict the future values
 of univariate or multivariate time series based on the estimated ARMA or VARMA models.

The following figure shows an example of predicting the monthly temperatures for the following
 year based on the ARMA model of the monthly temperatures during
 the previous eleven years:

Figure 84.

[IMAGE alt='image' src='GUID-B4FFD882-28F5-4A33-85F2-F38B751B6317-a5.gif']

Note

In the previous figure, the Original graph contains the monthly average
 temperatures for twelve consecutive years. Before predicting future values, this example
 estimates the AR model for the temperature time series of the first eleven years. With the
 estimated AR model coefficients and by specifying the MA model coefficients to one, this
 example predicts the monthly temperatures for the twelfth year using the TSA ARMA
 Prediction VI.

The Prediction Result graph in the previous figure compares the predicted
 temperatures with the original temperatures of the twelfth year
 by plotting them together. The prediction may bias from the true
 values but the true values fall into the estimated confidence
 range. The Upper Limit and
 Lower Limit plots in the
 Prediction Result graph
 indicate the confidence range of the prediction. You can see in
 the Confidence Level indicator that the
 prediction result falls into the estimated confidence range with
 the confidence level of 99.73% (3σ).

Parent topic:

Predict Time Series Values

Related concepts:

- Building Autoregressive Models

Related information:

- Related Documentation

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=armax-model-definitions-advanced-signal-proce.html language=enus -->
## TOPIC 00017: ARMAX Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `armax-model-definitions-advanced-signal-proce.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/armax-model-definitions-advanced-signal-proce.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When D(z) and F(z) equal 1, the general-linear polynomial model reduces to an autoregressive-moving average with exogenous terms (ARMAX) model.Unlike the autoregressive with exogenous terms (ARX) model, the system structure of an ARMAX model includes the stochastic dynamics. ARMAX models are useful

### ARMAX Model Definitions

When D(z) and
 F(z) equal 1, the general-linear polynomial
 model reduces to an autoregressive-moving average with exogenous terms (ARMAX)
 model.

Unlike the autoregressive with exogenous terms (ARX) model, the system structure of an ARMAX
 model includes the stochastic dynamics. ARMAX models are useful when you have dominating
 disturbances that enter early in the process, such as at the input. For example, a wind
 gust affecting an aircraft is a dominating disturbance early in the process. The ARMAX
 model has more flexibility than the ARX model in handling models that contain
 disturbances.

Use the SI Estimate ARMAX Model VI to estimate ARMAX models. This VI uses the
 Gauss-Newton method to optimize the mean square value of the prediction error when
 searching for the optimal ARMAX model. This searching process is iterative and might
 converge to a local minimum rather than a global minimum. Therefore, you must validate
 the estimated model. If the estimated model passes the validation test, you can use this
 model even if the SI Estimate ARMAX Model VI might locate only a
 local minimum.

The following equation shows the form of the ARMAX model:

A

z

y

k

=

B

z

u

k

-

n

+

C

z

e

k

where

- y ( k ) represents the system outputs
- u ( k ) represents the system inputs
- n is the system delay
- e ( k ) is the system disturbance

A(z), B(z), and
 C(z) are polynomial with respect to the
 backward shift operator z<sup>–1</sup> and defined by the following equations:

A

z

=

1

+

a

1

z

-

1

+

.

.

.

+

a

k

a

z

-

k

a

B

z

=

b

0

+

b

1

z

-

1

+

.

.

.

+

b

k

b

z

-

k

b

-

1

C

z

=

1

+

c

1

z

-

1

+

.

.

.

+

c

k

c

z

-

k

c

The following figure depicts the signal flow of an ARMAX model:

Figure 191.

[IMAGE alt='image' src='GUID-2AD62765-9BE4-4224-AE27-FEBDFFE957FF-a5.gif']

where

- u represents the system inputs
- y represents the system outputs
- e is the system disturbance
- A is A ( z )
- B is B ( z )
- C is C ( z )

#### SISO

The following is the
 time domain equation for the ARMAX SISO model:

y

k

+

a

1

y

k

-

1

+

.

.

.

+

a

k

a

y

k

-

k

a

=

b

0

u

k

-

n

-

1

+

.

.

.

+

b

k

b

-

1

k

-

n

-

k

b

+

1

+

e

k

+

c

1

e

k

-

1

+

.

.

.

+

c

k

c

e

k

-

k

c

where

- k a is the A 
 order
- k b is the B 
 order
- k c is the C 
 order
- n is the system delay
- e ( k ) is the system disturbance

Parent topic:

General-Linear Model Definitions

Related concepts:

- Validate Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=arx-model-definitions-advanced-signal-process.html language=enus -->
## TOPIC 00018: ARX Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `arx-model-definitions-advanced-signal-process.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/arx-model-definitions-advanced-signal-process.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When C(z), D(z), and F(z) equal 1, the general-linear polynomial model reduces to an autoregressive with exogenous terms (ARX) model.This model is the simplest model that incorporates the stimulus signal. However, the ARX model captures some of the stochastic dynamics as part of the system dynamics.

### ARX Model Definitions

When C(z),
 D(z), and
 F(z) equal 1, the general-linear polynomial
 model reduces to an autoregressive with exogenous terms (ARX) model.

This model is the simplest model that incorporates the stimulus signal. However, the ARX model
 captures some of the stochastic dynamics as part of the system dynamics. In this model,
 the transfer function of the deterministic part
 G(z<sup>–1</sup>, θ) of the system and the transfer function of the stochastic part
 H(z<sup>–1</sup>, θ) of the system have the same set of poles. This coupling can be
 unrealistic. The system dynamics and stochastic dynamics of a system do not share the
 same set of poles all the time. You can reduce this disadvantage if the signal-to-noise
 ratio is high.

When the disturbance e(k) of a system is not white noise,
 the coupling between the deterministic and stochastic dynamics can bias the estimation
 of the ARX model. You can set the model order higher than the actual model order to
 minimize the estimation error, especially when the signal-to-noise ratio is low.
 However, increasing the model order can change some dynamic characteristics of the
 model, such as the stability of the model.

Use the SI Estimate ARX Model VI to estimate ARX models. The identification
 method for the ARX model is the least squares method, which is a special case of the
 prediction error method. The least squares method is the most efficient polynomial
 estimation method because this method solves linear regression equations in analytic
 form. Moreover, the solution is unique.

The following equation shows the form of the ARX model:

A(z)y(k) = B(z)u(k - n) + e(k)

where

- u ( k ) represents the system inputs
- y ( k ) represents the system outputs
- n is the system delay
- e ( k ) is the system disturbance

A(z) and B(z) are
 polynomial with respect to the backward shift operator z<sup>–1</sup> and defined by the following equations:

A

z

=

1

+

a

1

z

-

1

+

.

.

.

+

a

k

a

z

-

k

a

B

z

=

b

0

+

b

1

z

-

1

+

.

.

.

+

b

k

b

z

-

k

b

-

1

The following figure depicts the signal flow of an ARX model:

Figure 190.

[IMAGE alt='image' src='GUID-48339301-CB0E-4BB9-99C4-776962733AB4-a5.gif']

where

- u represents the system inputs
- y represents the system outputs
- e is the system disturbance
- A is A ( z )
- B is B ( z )

#### SISO

The following is the
 time domain equation for the ARX SISO model:

y

k

+

a

1

y

k

-

1

+

.

.

.

+

a

k

a

y

k

-

k

a

=

b

0

u

k

-

n

+

b

1

u

k

-

n

-

1

+

.

.

.

+

b

k

b

-

1

u

k

-

n

-

k

b

+

1

+

e

k

where

- k a is the A 
 order
- k b is the B 
 order
- n is the system delay
- e ( k ) is the system disturbance

Parent topic:

General-Linear Model Definitions

Related concepts:

- Least Squares Method
- Determining Parameters for the Prediction Error Method

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=aspt-new-features-and-changes.html language=enus -->
## TOPIC 00019: LabVIEW Advanced Signal Processing Toolkit New Features and Changes

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `aspt-new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/aspt-new-features-and-changes.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of LabVIEW Advanced Signal Processing Toolkit. Discover what is new in the latest releases of LabVIEW Advanced Signal Processing Toolkit.If you cannot find new features and changes for your version, it might

### LabVIEW Advanced Signal Processing
 Toolkit
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of LabVIEW Advanced Signal Processing
 Toolkit.

LabVIEW Advanced Signal Processing
 Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW Advanced Signal Processing Toolkit
 2021 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Advanced
 Signal Processing Toolkit 2021.

- LabVIEW Advanced Signal Processing Toolkit 2021 no longer supports Windows 7/8.1,
 Windows Server 2008/2012, or any 32-bit Windows operating system.
  - Versions of this product that ship after May 1, 2021 may not install or execute
 correctly on these operating systems. For information about operating systems that
 NI supports, visit NI Support for Windows 7, Windows 8.1, Windows Server 2008
 R2, Windows Server 2012 R2, and All 32-Bit Windows .

Related information:

- NI Support for Windows 7, Windows 8.1, Windows Server 2008 R2,
 Windows Server 2012 R2, and All 32-Bit Windows

#### LabVIEW Advanced Signal Processing Toolkit
 2018 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Advanced
 Signal Processing Toolkit 2018.

- LabVIEW Advanced Signal Processing Toolkit 2018 adds support for LabVIEW 2018
 (64-bit).
- Refer to the Readme for a list of LabVIEW Advanced Signal Processing Toolkit 2018 bug
 fixes.

Related information:

- Readme

#### LabVIEW Advanced Signal Processing Toolkit
 2017 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Advanced
 Signal Processing Toolkit 2017.

- LabVIEW Advanced Signal Processing Toolkit 2017 adds support for NI Linux Real-Time
 (Intel x64-based) targets.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=basic-statistical-values.html language=enus -->
## TOPIC 00020: Basic Statistical Values

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `basic-statistical-values.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/basic-statistical-values.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The basic statistical analysis methods enable you to compute statistical values for a univariate or multivariate time series, including mean, variance, skewness, kurtosis, confidence limits, stationarity, and whiteness. LabVIEW Full and Professional Development Systems also contain Probability and S

### Basic Statistical Values

Note

Probability and
 Statistics

Probability and Statistics

Statistical Analysi

Probability and Statistics

#### Understanding the Mean and Variance
 Values

Mean and variance are fundamental statistical attributes of a time
 series. The arithmetic mean of a time series is the average or expected value of
 that time series. In some cases, the mean value of a time series can be the
 operating point or working point of a physical system that generates the time
 series. In general, you must subtract the value of the operating point from a time
 series before building predictive behavioral models for that time series. Median and
 trimmed mean are more robust than arithmetic mean and geometric mean if the raw data
 does not contain significant outliers. Use the TSA Mean VI to
 obtain the median or different mean values of a time series.

The variance of a
 time series measures the dispersion of the time series data samples around the mean
 value. Use the TSA Deviation and Variance VI to obtain the
 variance value of a time series.

#### Understanding the Skewness and
 Kurtosis Values

The skewness and kurtosis are higher-order statistical
 attributes of a time series. Skewness indicates the symmetry of the Probability
 Density Function (PDF) of the amplitude of a time series. A time series with an
 equal number of large and small amplitude values has a skewness of zero. A time
 series with many small values and few large values is positively skewed (right
 tail), and the skewness value is positive. A time series with many large values and
 few small values is negatively skewed (left tail), and the skewness value is
 negative.

The following figure illustrates two time-series PDFs with opposite
 skewness. Each bin in these histograms indicates the probability that any particular
 sample from the corresponding time series has a value within the range of that
 bin.

Figure 67.

[IMAGE alt='image' src='GUID-77903CD8-D06C-41B7-92A9-05918E47E504-a5.gif']

The Left-Skewed graph shows a time series that is
 positively skewed. The Right-Skewed graph shows a time series
 that is negatively skewed. The green lines in these plots are the best-fit normal
 distributions for the given distributions.

Kurtosis measures the
 tailedness
 of the PDF of a time series. A kurtosis value close to three indicates a
 Gaussian-like
 distribution.
 PDFs with relatively
 fat
 tails have kurtosis greater than three. PDFs with relatively
 thin
 tails have kurtosis less than three. The following figure
 illustrates two time series with different
 kurtosis:

Figure 68.

[IMAGE alt='image' src='GUID-0CC3F3CF-0F63-44E2-B58D-568E890DB232-a5.gif']

The histogram on the left shows a time series with
 fat
 tails
 (kurtosis = 10.9817). The histogram on the right shows a time series with
 thin
 tails
 (kurtosis = 1.90294). The green lines in these plots are the Gaussian PDFs with the
 kurtosis equal to three.

Changes in skewness and kurtosis of a time series
 indicate systematic changes in the associated physical systems. Use the TSA
 Skewness and Kurtosis VI to obtain the skewness and kurtosis values of
 a time series.

#### Understanding the Confidence
 Limits

Confidence limits are user-specified probability bounds for the
 range of statistical parameters. Confidence limits are useful because the estimated
 values of statistical parameters, such as mean and variance, typically differ for
 different sections of a time series. Instead of calculating one value for mean and
 standard deviation for an entire time series, you can generate a range of values for
 the mean and standard deviation over that time series by specifying confidence
 limits.

The estimation interval for a given set of confidence limits indicates
 how much the calculated mean and standard deviation values can vary across the time
 series. A narrow estimation interval for a parameter implies that the parameter
 varies little across the time series.

Use the TSA Confidence
 Limits VI to perform interval estimations on the statistical
 parameters of a time series.

#### Testing the Normal
 Distribution

A time series whose PDF approximates a Gaussian distribution
 are called normally distributed. Many statistical analysis methods work well only
 for time series that are normally distributed. Furthermore, some modeling methods
 assume that the measurement noise in a time series is Gaussian white noise. For
 these methods, you can measure how well the histogram of a time series or
 measurement noise approximates a normal distribution and determine appropriate
 statistical analysis and modeling methods.

A normal distribution test plots
 the calculated distribution for a time series and its best-fit normal distribution
 together. If the two distributions show a close correlation, the calculated
 distribution for the time series is normally distributed.

Use the TSA
 Normal Distribution Test VI to test how normally a time series is
 distributed.

#### Checking the Stationarity and
 Whiteness

Time series analysis methods can produce satisfactory analysis
 results for stationary time series but might not provide satisfactory analysis
 results for nonstationary signals. You can run a stationarity test to check if a
 time series is stationary.

For nonstationary signals, use other analysis
 methods such as time-frequency analysis and wavelet analysis.

Tip

Whiteness tests examine the spectral flatness of a time series and
 indirectly indicate statistical independence of a time series data samples. You also
 can use whiteness tests to analyze the fitness of a particular time-series model
 created with some modeling methods. For those methods, if the residual estimation
 noise for a particular model is white with a specified confidence level, the
 estimated model is a good fit.

Use the TSA Stationarity
 Test VI and the TSA Whiteness Test VI to check the
 stationarity and whiteness of a time series.

Parent topic:

Perform Statistical Analysis

Related concepts:

- Introduction to Time Frequency Analysis
- Introduction to Wavelet Signal Processing

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=bispectrum-estimation-methods.html language=enus -->
## TOPIC 00021: Bispectrum Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `bispectrum-estimation-methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/bispectrum-estimation-methods.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Bispectrum is a higher-order extension of power spectral estimation.A conventional power spectrum decomposes the power of a time series over frequency. In contrast, the bispectrum decomposes the third moment (skewness) of a time series over frequency. You can use the estimated bispectrum to detect a

### Bispectrum Estimation Methods

Bispectrum is a higher-order extension of power spectral estimation.

A conventional power spectrum decomposes the power of a time series over frequency. In contrast,
 the bispectrum decomposes the third moment (skewness) of a time series over
 frequency. You can use the estimated bispectrum to detect asymmetric
 nonlinearities in a time series.

Use the TSA Bispectrum VI to compute the bispectrum of a time series. You can
 use this VI to compute the bispectrum based on the Fast Fourier Transform (FFT) or
 the AR model of the time series.

Parent topic:

Perform Correlation and Spectral Analysis

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=box-jenkins-model-definitions-advanced-signal.html language=enus -->
## TOPIC 00022: Box-Jenkins Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `box-jenkins-model-definitions-advanced-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/box-jenkins-model-definitions-advanced-signal.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When A(z) equals 1, the general-linear polynomial model reduces to the Box-Jenkins model.This model provides a complete model of a system because this model represents disturbance properties separately from system dynamics. This model is useful when you have disturbances that enter late in the proce

### Box-Jenkins Model Definitions

When A(z) equals 1, the general-linear polynomial
 model reduces to the Box-Jenkins model.

This model provides a complete model of a system because this model represents disturbance
 properties separately from system dynamics. This model is useful when you have
 disturbances that enter late in the process, such as measurement noise on the
 output.

Use the SI Estimate BJ Model VI to estimate Box-Jenkins models. The
 identification method of the Box-Jenkins model is the prediction error method, which is
 the same as that of the ARMAX model.

The following equation shows the form of the Box-Jenkins model:

y

k

=

B

z

F

z

u

k

-

n

+

C

z

D

z

e

k

where

- y ( k ) represents the system outputs
- u ( k ) represents the system inputs
- n is the system delay
- e ( k ) is the system disturbance

B(z), C(z),
 D(z), and
 F(z) are polynomial with respect to the
 backward shift operator z<sup>-1</sup> and defined by the following equations:

B

z

=

b

0

+

b

1

z

-

1

+

.

.

.

+

b

k

b

z

-

k

b

-

1

C

z

=

1

+

c

1

z

-

1

+

.

.

.

+

c

k

c

z

-

k

c

D

z

=

1

+

d

1

z

-

1

+

.

.

.

+

d

k

d

z

-

k

d

F

z

=

1

+

f

1

z

-

1

+

.

.

.

+

f

k

f

z

-

k

f

The following figure depicts the signal flow of a Box-Jenkins model:

Figure 192.

[IMAGE alt='image' src='GUID-64D8007A-DB79-49C9-9B7E-A55746D51448-a5.gif']

where

- u is the system inputs
- y is the system outputs
- e is the system disturbance
- v and ω are the auxiliary variables

#### SISO

The following are the
 time domain equations for the Box-Jenkins SISO model:

w

k

+

f

1

w

k

-

1

+

.

.

.

+

f

k

f

w

k

-

k

f

=

b

0

u

k

-

n

+

b

1

u

k

-

n

-

1

+

.

.

.

+

b

k

b

-

1

u

k

-

n

-

k

b

+

1

v

k

+

d

1

v

k

-

1

+

.

.

.

+

d

k

d

v

k

-

k

d

=

e

k

+

c

1

e

k

-

1

+

.

.

.

+

c

k

c

e

k

-

k

c

y

k

=

w

k

+

v

k

where

- k f is the F 
 order
- k b is the B 
 order
- k c is the C 
 order
- k d is the D 
 order
- u ( k ) is the system input
- n is the system delay
- e ( k ) is the system disturbance
- w is the auxiliary variable

Parent topic:

General-Linear Model Definitions

Related concepts:

- Determining Parameters for the Prediction Error Method

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=building-autoregressive-models.html language=enus -->
## TOPIC 00023: Building Autoregressive Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `building-autoregressive-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/building-autoregressive-models.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Autoregressive (AR) models of a time series enable you to predict the current value x[t] of a time series, based on the past values x[t][–1], x[t][–2], ..., x[t–n], plus a prediction error. The parameter n determines the number of past values you use to predict the current value. The following equat

### Building Autoregressive Models

Autoregressive (AR) models of a time series enable you to predict the current value
 x<sub>t</sub> of a time series, based on the past values
 x<sub>t</sub><sub>–1</sub>,
 x<sub>t</sub><sub>–2</sub>, ...,
 x<sub>t–n</sub>, plus a prediction error. The parameter
 n determines the number of past values you use to predict the
 current value. The following equation defines an AR model with an order of
 n:

χ

t

+

a

1

x

t

-

1

+

a

2

x

t

-

2

+

.

.

.

a

n

x

t

-

n

=

e

t

where

- [1, a 1 , a 2 , ...,
 a n ] are the AR coefficients
- e t is the prediction error

Ideally, the residual prediction error is white noise with a mean value of zero.

You can rewrite the previous equation more concisely as follows:

A

q

x

t

=

e

t

A(q)x<sub>t</sub> =
 e<sub>t</sub>

where A(q) is the AR operator, which is defined as
 follows:

A

q

=

1

+

a

1

q

-

1

+

a

2

q

-

2

+

.

.

.

+

a

n

q

-

n

The term q<sup>–k</sup> is the backward shift operator, which is defined as
 follows:

q

-

k

x

t

=

x

t

-

k

From a dynamic-system point of view, a time series is the response of a linear system
 with a white noise as the stimulus. An AR model or other models of the response signal
 describe the linear system. The prediction error of the model is the white noise
 e<sub>t</sub>. The following figure shows a diagram that uses the
 AR model to describe a linear system.

Figure 79.

[IMAGE alt='image' src='GUID-7A66C825-65C8-4506-A7A1-205026378B51-a5.gif']

H(q)

x

t

H(q)

A(q)

H(q)

Note

Because many real-world linear systems can be modeled accurately with AR models, AR models are a
 good first choice for parametric modeling. The computation of AR models also is
 particularly efficient because in contrast with Moving Average (MA) and
 Autoregressive-Moving Average (ARMA) models, you only need to compute linear-regression
 equations. Furthermore, the resulting model is unique and stable. AR models are
 numerically preferable to ARMA models, especially when the model order is high. However,
 AR models may not accurately model linear systems that do not have an AR response, or in
 cases where the measured time series is contaminated with noise or distortion. If an AR
 model is not appropriate, a high model order may be required to whiten the residual
 prediction error e<sub>t</sub>. But if you use a high model order to
 force an AR model to fit a particular time series for which an AR model is not
 appropriate, you may get spurious spectral components in the resulting response.

For a multivariate time series with m variables, you can use an (m ×
 1)–length vector X<sub>t</sub> to represent a multivariate time
 series, where X<sub>t</sub><sup>T</sup> = (x<sub>1</sub><sub>t</sub>,
 ..., x<sub>mt</sub>). To describe the interrelationship between these variables, you can
 extend Equation 5-1 to be a VAR model as follows:

χ

t

+

A

1

X

t

-

1

+

A

2

X

t

-

2

+

.

.

.

A

n

X

t

-

n

=

E

t

where

- n is the model order
- I ,
 A 1 ,
 A 2 , ...,
 A n are square matrices
 of the VAR coefficients
- I is the identity matrix
- m × m is the dimension of each matrix
- E t is the prediction-error
 vector where E t T 
 = ( e 1 t ,
 e 2 t , ...,
 e mt )

Each variable in E<sub>t</sub> ideally is white
 noise with a mean value of zero. If the model fit is good, these variables are not
 correlated with each other.

You can rewrite the previous equation concisely as follows:

A

q

x

t

=

E

t

where A(q) is the AR operator, which is
 defined as follows:

A

q

=

1

+

A

1

q

-

1

+

A

2

q

-

2

+

.

.

.

+

A

n

q

-

n

The resulting VAR model of a multivariate time series is the coefficients matrix.
 However, you cannot obtain the dynamic characteristics of a multi-output system directly
 from the coefficients matrix of the VAR model. You must convert the model coefficients
 matrix into a state transition matrix in a stochastic state-space model. By computing
 the eigenvalues of a state transition matrix, you can obtain the poles of the system
 that generates the corresponding multivariate time series. You then can obtain the
 dynamic characteristics of the system from the poles.

Use the TSA AR Modeling VI or the Time Series Modeling
 Express VI to build AR and VAR models for univariate or multivariate time
 series.

#### Selecting an Appropriate AR
 Order

The first step of estimating a model is to select an appropriate model. For a given
 model, selecting the model order is typically a trial-and-error process. Besides
 using background knowledge about the physical system that generates the time series,
 you also need to use other information, such as the information acquired from
 various statistical analysis methods, to justify the selected model order.

One tool for determining the model order is the partial auto-correlation function of
 the time series. The partial auto-correlation function is a function of lag. The
 partial auto-correlation value becomes very small when the lag equals a suitable AR
 order. The following figure shows an example of estimating the AR order with the
 partial auto-correlation function:

Figure 80.

[IMAGE alt='image' src='GUID-C5891A10-B9A2-4035-9D73-086685FBE8EE-a5.gif']

The value of the Partial Auto-Correlation plot in the previous
 figure becomes zero when lag equals two or greater. Therefore, a suitable AR order
 for this model is two.

Instead of computing the partial auto-correlation function for a time series, you can
 use a set of model-selection criteria to estimate the model order. From a
 least-square fitting standpoint, the higher the model order, the better the model
 fits the time series, because a high-order model has more degrees of freedom.
 However, an unnecessarily high-order may introduce spurious spectral artifacts in
 the resulting response. As a result, the criteria you use to assess the model order
 therefore must not only rely on the model-fitting error but also incorporate a
 penalty when the order increases. Different selections for the penalty determine
 different criteria.

#### Akaike's Information
 Criterion

The Akaike's Information Criterion (AIC) is a weighted
 estimation error based on the unexplained variation of a given time series with a
 penalty term when exceeding the optimal number of parameters to represent the
 system. For the AIC, an optimal model is the one that minimizes the following
 equation:

A

I

C

=

V

n

1

+

2

n

L

where

- L is the number of data points in a time series
- n is the model order
- V n is the prediction error

#### Bayesian Information
 Criterion

The Bayesian Information Criterion (BIC) replaces the term 2n in
 the AIC with the expression (n +
 nln(L)). The BIC penalizes excess model
 order more severely than the AIC does. For the BIC, an optimal model is the one that
 minimizes the following equation:

B

I

C

=

V

n

1

+

n

+

n

l

n

L

L

#### Final Prediction Error
 Criterion

The Final Prediction Error Criterion (FPE) estimates the model-fitting error when you
 use the model to predict new outputs. For the FPE, an optimal model is the one that
 minimizes the following equation:

F

P

E

=

V

n

1

+

2

n

L

-

n

#### Minimal Description Length
 Criterion

The Minimal Description Length Criterion (MDL) is based on
 V<sub>n</sub> plus a penalty for the number of terms used.
 For the MDL, an optimal model is the one that minimizes the following equation:

M

D

L

=

V

n

1

+

n

l

n

L

L

#### Phi Criterion

The Phi
 Criterion (PIC) generates an optimal model that minimizes the following
 equation:

P

H

I

=

V

n

1

+

2

n

l

n

ln

L

L

Use the TSA AR Modeling Order VI to estimate a suitable
 AR model order for a time series. This VI implements the partial auto-correlation
 function and uses the AIC, BIC, FPE, MDL, and PIC methods to search for the optimal
 model order in the range of interest.

If you use the Time Series
 Modeling Express VI to build an AR model interactively, this
 Express VI computes the value of the specified criterion
 function within the order range and highlights the optimal order in the
 Criterion Function graph, as shown in the following
 figure. You also can select a different order manually on the Criterion
 Function graph.

Figure 81.

[IMAGE alt='image' src='GUID-C20D9A7D-4567-4F34-887C-962E861A3296-a5.gif']

Complete the following steps to select an appropriate AR model for AR models you
 build by using the Time Series Modeling Express VI:

1. In the Configure Time Series Modeling dialog box, click the
 Model Settings tab and select
 AR in Type .
2. Click the Order Estimation tab. On the Order
 Estimation page, complete the following steps to estimate a
 suitable AR order for the time series:
  1. In the Method list, select an appropriate
 criterion function.
  2. Specify an appropriate AR order range in the Maximum AR
 order box and the Minimum AR
 order box.
  3. Click the Estimate button.
3. Click the Model Settings tab. In the AR
 order box, specify the value estimated in Step 2. In the
 Method of AR list, specify an appropriate estimation
 method.
4. Verify the estimate model by watching the Noise
 auto-correlation plot of model error. If the estimated model is
 suitable for the univariate time series, the values of the auto-correlation
 without lab t being zero fall into the confidence
 interval.

Parent topic:

Building Models

Related concepts:

- Correlation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=building-autoregressive-moving-average-models.html language=enus -->
## TOPIC 00024: Building Autoregressive-Moving Average Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `building-autoregressive-moving-average-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/building-autoregressive-moving-average-models.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Autoregressive-Moving Average (ARMA) models are more accurate than Autoregressive (AR) models in approximating the response of linear systems with zeros in the response transfer function.The following equation defines an ARMA model with an AR order of n and the Moving Average (MA) order of m:xt+a1xt

### Building Autoregressive-Moving Average Models

Autoregressive-Moving Average (ARMA) models are more accurate than Autoregressive (AR)
 models in approximating the response of linear systems with zeros in the response
 transfer function.

The following equation defines an ARMA model with an AR order of n and the
 Moving Average (MA) order of m:

x

t

+

a

1

x

t

-

1

+

a

2

x

t

-

2

+

.

.

.

a

n

x

t

-

n

=

e

t

+

b

1

e

t

-

1

+

.

.

.

+

b

m

e

t

-

m

where

- [1, a 1 , a 2 , ...,
 a n ] are the AR coefficients
- [1, b 1 , a 2 , ...,
 b m ] are the MA coefficients

You can rewrite the previous equation more concisely as follows:

A

q

x

t

=

B

q

e

t

where

- A(q) is the AR operator
- B(q) is the MA operator defined as follows: B
 q
 =
 1
 +
 b
 1
 q
 -
 1
 +
 b
 2
 q
 -
 2
 +
 .
 .
 .
 +
 b
 m
 q
 -
 m

The following figure shows a diagram that uses an ARMA model to describe a linear system. You can
 consider a time series x<sub>t</sub> as being the response of a
 system whose transfer function H(q) is
 B(q)/A(q). The stimulus of the system is
 e<sub>t</sub>.

Figure 82.

[IMAGE alt='image' src='GUID-F2628448-17DE-4257-A27B-F6E84CCE8771-a5.gif']

H(q) contains both zeros and poles. The roots of the polynomial
 A(q) are the poles of H(q). The roots of the
 polynomial B(q) are the zeros of H(q). The ARMA
 model uses poles and zeros to describe a system. Therefore, comparing with the AR model,
 the ARMA model can give a more accurate description of the dynamic characteristics of a
 physical system that generates time series, if the system has an ARMA response. However,
 because the MA term introduces nonlinearities in the model estimation, you cannot use an
 analytic form to solve the model coefficients. An iterative nonlinear optimization
 procedure is required, which could find a sub-optimal solution erroneously instead of
 finding the globally optimal solution.

You also can estimate a vector ARMA (VARMA) model for a multivariate time series. The
 resulting VARMA model of a multivariate time series is the coefficients matrix. However,
 you cannot obtain the dynamic characteristics of a multi-output system directly from the
 coefficients matrix of the VARMA model. You must convert the model coefficients matrix
 into a state transition matrix in a stochastic state-space model. By computing the
 eigenvalues of a state transition matrix, you can obtain the poles of the system that
 generates the corresponding multivariate time series. You then can obtain the dynamic
 characteristics of the system from the poles.

An MA model is a special case of the ARMA model that does not contain poles. The MA model
 describes a time series according to the following equation:

x

t

=

B

q

e

t

TSA MA Modeling

TSA ARMA Modeling

TSA ARMA
 Modeling

Note

TSA ARMA Modeling

TSA AR Modeling

TSA AR Modeling

TSA ARMA Modeling

You also can use the Time Series Modeling Express VI to build MA, ARMA, and
 VARMA models, interactively.

#### Selecting an Appropriate ARMA
 Order

Before estimating the ARMA model coefficients of a time series, you
 need to specify a suitable order for the model. Generally, you specify an AR order
 of n and an MA order of n– 1, where
 n is an integer. If you know the order of the response of the
 system that generates the time series, you can use that order directly. If you do
 not know the order, you can try orders from low to high to identify the lowest order
 in which the prediction error is sufficiently white. You can use the TSA
 Whiteness Test VI to perform whiteness tests on the residual
 prediction error, by computing auto-correlation and the corresponding confidence
 limit for the auto-correlation.

The variance of the prediction error also
 indicates if the ARMA model at a specified order fits the time series well. The
 smaller the variance of the prediction error is, the better the estimated model fits
 the time series. However, the variance of the prediction error for ARMA models
 decreases monotonically with order. Unnecessarily high orders introduce spurious
 artifacts in the resulting response if the measured time series is contaminated with
 noise or distortion.

The changes in the variance of the prediction error that
 result from changes in the model order can indicate dynamic characteristics of a
 physical system that generates time series. This property is helpful in vibration
 monitoring applications.

Parent topic:

Building Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=building-modal-parametric-models.html language=enus -->
## TOPIC 00025: Building Modal Parametric Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `building-modal-parametric-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/building-modal-parametric-models.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A modal parametric model describes the bulk dynamic characteristics of resonant systems such as buildings and bridges. The dynamic characteristics include natural frequencies, damping factors, resonance magnitudes, and resonance phases.You can use the impulse response function to determine the respo

### Building Modal Parametric Models

A modal parametric model describes the bulk dynamic characteristics of resonant systems
 such as buildings and bridges. The dynamic characteristics include natural frequencies,
 damping factors, resonance magnitudes, and resonance phases.

You can use the impulse response function to determine the response of a linear system to
 stimulus. The impulse response time series for a linear system can be represented
 parametrically with a linear combination of damped complex sinusoids as follows:

h

t

=

∑

i

-

1

n

g

i

e

s

i

t

where

- t is the time index
- n is the model order
- g i is one of the complex magnitudes
- s i is one of the modal poles

s<sub>i</sub> contains a unified frequency
 f<sub>i</sub> and a damping factor
 alpha<sub>i</sub> as follows:

s

i

=

a

i

+

j

2

π

f

i

The parameter g<sub>i</sub> contains a magnitude
 r<sub>i</sub> and a phase θ<sub>i</sub> as follows:

g

i

=

r

i

e

j

θ

i

So a discrete-time system can be defined by a series of resonance components, or modes:
 natural frequencies f<sub>i</sub>, damping factors
 alpha<sub>i</sub>, resonance magnitudes
 r<sub>i</sub>, and resonance phases θ<sub>i</sub>.

For a multivariate impulse response time series, you can build a modal parametric model
 as follows:

H

t

=

∑

i

-

1

n

G

i

e

s

i

t

where H<sub>t</sub> is a (k × 1) vector with
 k variables that come from k sources.
 H<sub>t</sub><sup>T</sup> =
 [h<sub>1</sub><sub>t</sub>,
 h<sub>2</sub><sub>t</sub>, ...,
 h<sub>kt</sub>]. G<sub>i</sub> is a
 (k × 1) complex magnitude vector with k
 variables. G<sub>i</sub><sup>T</sup> =
 [g<sub>1</sub><sub>i</sub>,
 g<sub>2</sub><sub>i</sub>, ...,
 g<sub>ki</sub>]. Each variable in the vector
 G<sub>i</sub> is one of the complex magnitudes.
 s<sub>i</sub> is one of the modal poles.

#### Specifying an Appropriate Model
 Order

The model order determines the number of modes that a modal
 parametric model contains. A model can contain real modes or pairs of complex
 conjugate modes. A real mode generates a resonance component at 0 Hz or at the
 Nyquist frequency. A pair of conjugate complex modes generates a resonance component
 with a positive frequency and discards the conjugate resonance component with the
 corresponding negative frequency. To search for m positive resonance components, you
 must specify the model order to be at least 2 × m. If a time
 series contains a large offset, you need to set the model order to at least 2 ×
 m + 1 to allow for a real mode. Structural vibration time
 series typically do not have offsets, so you can use a model order of 2 ×
 m.

Note

Use the TSA Modal Parametric Modeling VI to build modal
 parametric models for univariate or multivariate time series.

The following
 figure shows an example of computing the modes of a synthesized univariate time
 series consisting of two sinusoids at the frequencies of 120 Hz and 130 Hz:

Figure 83.

[IMAGE alt='image' src='GUID-CC0E58FA-B862-47DD-B3D7-F2E12DD8DBB5-a5.gif']

This example uses the Matrix Pencil method because this
 method is less sensitive to noise than the other available methods. The value of
 Model Order is 4, which equals twice the number of the
 sinusoids in the univariate time series.

The Noise
 Subspace value is set to 90% to compensate for additive noise in the
 measurements. For a fixed number of resonance components, a large dimension for the
 Noise Subspace parameter results in a large dimension for
 the signal subspace you use to describe a time series. A large dimension for the
 signal subspace helps you reduce the modeling error for the time series. However, an
 excessively large dimension may introduce spurious resonance components if the time
 series does not contain much noise. In the previous figure, the
 Modes array accurately indicates the attribute of the
 resonance components that the synthesized time series contains.

Parent topic:

Building Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=building-models.html language=enus -->
## TOPIC 00026: Building Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `building-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/building-models.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: One of the most important applications of time series analysis is building mathematical models for observed time series. The resulting mathematical models can help you better understand the dynamic characteristics of the corresponding physical systems and assist you in monitoring or providing feedba

### Building Models

One of the most important applications of time series analysis is building mathematical
 models for observed time series. The resulting mathematical models can help you better
 understand the dynamic characteristics of the corresponding physical systems and assist
 you in monitoring or providing feedback control for the systems.

You also can use the resulting mathematical models to estimate the power spectrum of a time
 series.

Using the LabVIEW Time Series Analysis Tools, you can build the following types of models:

Polynomial models

Modal parametric models

Stochastic state-space models

Note

System
 Identification

- [Building Autoregressive Models](building-autoregressive-models.html)
- [Building Autoregressive-Moving Average Models](building-autoregressive-moving-average-models.html)
- [Building Modal Parametric Models](building-modal-parametric-models.html)
- [Building Stochastic State-Space Models](building-stochastic-state-space-models.html)

Parent topic:

Time Series Analysis Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=building-stochastic-state-space-models.html language=enus -->
## TOPIC 00027: Building Stochastic State-Space Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `building-stochastic-state-space-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/building-stochastic-state-space-models.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The objective of using such a stochastic state-space model in an output-only context is to infer or estimate the hidden states given the observed outputs and to predict future responses based on the estimated states and the model dynamics.A stochastic state-space model describes an output-only dynam

### Building Stochastic State-Space Models

The objective of using such a stochastic state-space model in an output-only context is
 to infer or estimate the hidden states given the observed outputs and to predict future
 responses based on the estimated states and the model dynamics.

A stochastic state-space model describes an output-only dynamic system according to the
 following equations:

x

k

+

1

=

A

x

k

+

w

k

y

k

+

1

=

C

x

k

+

v

k

where

- y k is the ( m × 1) multivariate time
 series with m variables
- x k is the state vector with n state
 variables, n
- A is the state transition matrix with a dimension of
 n × n
- C is the measurement matrix, or state observation matrix, with a
 dimension of m × n
- w k and v k are the
 ( n × 1) and ( m × 1) noise vectors with a
 mean value of zero, respectively

The matrix A is defined as follows:

A

=

ψ

∧

ψ

-

1

where

- Λ is a diagonal matrix containing the complex eigenvalues λ i ( i = 1, 2, ..., n ) of matrix A
- Ψ contains the eigenvectors as columns

You can obtain the modal pole s<sub>i</sub> from the complex
 eigenvalues λ<sub>i</sub> as follows:

s

i

=

l

n

λ

-

1

The eigen values of the state transition matrix A characterize the dynamic
 behavior of a physical system. By computing the state transition matrix
 A and measurement matrix C, you also can
 obtain the following modal parameters defined in the modal parametric model: natural
 frequencies, damping factors, resonance magnitudes, and resonance phases.

You can obtain the complex magnitude G<sub>i</sub> vector for each
 modal pole s<sub>i</sub> from the measurement matrix
 C, using the state observation equation as follows:

Φ

=

C

ψ

Each column of the matrix Φ is associated with one complex magnitude
 G<sub>i</sub>.

Use the TSA Stochastic State-Space Modeling VI to build stochastic state-space
 models for multivariate time series.

Parent topic:

Building Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=calculate-the-energy-of-a-signal-at-each-ti.html language=enus -->
## TOPIC 00028: Calculate the Energy of a Signal at Each Time Frequency Instant

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `calculate-the-energy-of-a-signal-at-each-ti.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/calculate-the-energy-of-a-signal-at-each-ti.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A main motivation for the development of various time-frequency distributions, such as the Short-Time Fourier Transform (STFT) spectrogram, the Wigner-Ville Distribution (WVD), the Gabor spectrogram, and so on, has been to describe how the energy of a signal varies with time and frequency.Currently,

### Calculate the Energy of a Signal at Each Time
 Frequency Instant

A main motivation for the development of various time-frequency distributions, such as
 the Short-Time Fourier Transform (STFT) spectrogram, the Wigner-Ville Distribution
 (WVD), the Gabor spectrogram, and so on, has been to describe how the energy of a signal
 varies with time and frequency.

Currently, scientists do not know of an algorithm, except for a few special cases, that can
 compute the energy of a signal at each particular time-frequency instant
 (t, f). Strictly speaking, the result of all
 quadratic time-frequency analysis algorithms,
 P(t, f ), is nothing more
 than a certain type of weighted average energy in the vicinity of the point
 (t, f). Different weighting schemes lead to
 different algorithms with different time-frequency resolutions and other properties.

Without going into any detail, the following examples show the effect of different algorithms, or
 different weighting averages, and the resulting time-frequency distribution.

The following figure shows the STFT spectrogram of a test signal that contains ten sine cycles at
 10 Hz. This example uses a Hanning window.

Figure 44.

[IMAGE alt='image' src='GUID-77EDF768-F5D7-428F-B9ED-47F189150D34-a5.gif']

Although the signal starts at 1 s and ends at 2 s, the STFT spectrogram in the previous figure
 shows that energy exists before 1 s and after 2 s. You can use the Gabor spectrogram
 method with an order of four to suppress the energy substantially before 1 s, after 2 s,
 and above or below 10 Hz to achieve a better measurement, as shown in the following
 figure:

Figure 45.

[IMAGE alt='image' src='GUID-0DE35F56-E5B8-4C9C-914B-A3CAC270DBDF-a5.gif']

The previous figure shows that most of the energy of the signal now exists between 1 s and 2 s
 and within 10 Hz. As the order of the Gabor spectrogram increases, the energy
 concentration also increases, and you can come closer to achieving measurement between 1
 s and 2 s and within 10 Hz. However, a Gabor spectrogram with a high order produces
 negative values, which can cause problems with the classical energy definition, which
 requires that the energy be non-negative.

Parent topic:

Quadratic Time Frequency Analysis Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=categorize-signals.html language=enus -->
## TOPIC 00029: Categorize Signals

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `categorize-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/categorize-signals.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In signal processing, you usually categorize signals into stationary, evolutionary nonstationary, or transient nonstationary. Stationary For stationary signals, you assume that the spectral content of stationary signals does not change as a function of time, space, or some other independent variable

### Categorize Signals

In signal processing, you usually categorize signals into stationary, evolutionary
 nonstationary, or transient nonstationary.

Stationary

Nonstationary

Evolutionary

Transient

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=central-time-and-central-frequency.html language=enus -->
## TOPIC 00030: Central Time and Central Frequency

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `central-time-and-central-frequency.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/central-time-and-central-frequency.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the LabVIEW Time Frequency Analysis Tools to decompose a signal as a linear combination of elementary functions. You can observe the central time and central frequency by plotting the time waveform and the time-frequency spectrogram of the signal, respectively.This topic contains information tha

### Central Time and Central Frequency

Use the LabVIEW Time Frequency Analysis Tools to decompose a signal as a linear
 combination of elementary functions. You can observe the central time and
 central frequency by plotting the time waveform and the time-frequency
 spectrogram of the signal, respectively.

Note

You can express a signal as a linear combination of a series of elementary functions. For
 example, the Gabor transform decomposes a signal into a linear combination of Gabor
 elementary functions, which are determined by dual windows. Similarly, the adaptive
 transform decomposes a signal as a linear combination of Gaussian chirplet or Gaussian
 pulse elementary functions, which are calculated by the matching pursuit method.

Each elementary function locates a different position in the time and frequency domains
 of a signal. In the time domain, the position is the central time. In the frequency
 domain, the position is the central frequency.

The following equations define the central time and the central frequency of a signal,
 s(t):

E

=

∫

-

ω

ω

s

t

2

d

t

t

=

1

E

∫

-

ω

ω

t

s

t

2

d

t

ω

1

2

π

E

∫

-

ω

ω

ω

S

ω

2

d

ω

where

- E is the energy, or power, of the signal
- t is time
- ( t ) is the central time of the signal
- (ω) is the central frequency of the signal
- S (ω) is the Fourier transform of the signal

The following illustrations show the time waveform and the time-frequency spectrogram of
 a Gaussian chirplet. You can see that the central time of this chirplet is 15 s and the
 central frequency of this chirplet is 4 Hz.

Figure 4.

[IMAGE alt='image' src='GUID-9899F61E-C948-410D-AFCD-FD9D7087930A-a5.gif']

Parent topic:

Fundamentals

Related concepts:

- Overview of LabVIEW Time Frequency Analysis Tools
- Discrete Gabor Transform and Expansion
- Adaptive Transform and Expansion

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=cepstrum-estimation-methods.html language=enus -->
## TOPIC 00031: Cepstrum Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `cepstrum-estimation-methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/cepstrum-estimation-methods.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the estimated cepstrum to identify echoes or periodic components in a time series.A cepstrum, which is an anagram of the word spectrum, is the Fourier transform of the natural logarithm of a spectrum. A cepstrum also is useful for separating homomorphic or convolved components in a time

### Cepstrum Estimation Methods

You can use the estimated cepstrum to identify echoes or periodic components in a time
 series.

A cepstrum, which is an anagram of the word spectrum, is
 the Fourier transform of the natural logarithm of a spectrum. A cepstrum also is useful
 for separating homomorphic or convolved components in a time series by transforming the
 time series into a domain where the convolution becomes a simple summation
 operation.

Cepstrum estimation methods treat frequency-domain data as time-domain data. Therefore, the
 domain of a cepstrum is called quefrency, which is an anagram of the
 word frequency.

A cepstrum has the following four derivative forms:

- [Estimating the Real Cepstrum of a Time Series](estimating-the-real-cepstrum-of-a-time-series.html)
- [Estimating the Complex Cepstrum of a Time Series](estimating-the-complex-cepstrum-of-a-time-ser.html)
- [Estimating the Power Cepstrum of a Time Series](estimating-the-power-cepstrum-of-a-time-serie.html)
- [Estimating the Time-Cepstrum of a Time Series](estimating-the-time-cepstrum-of-a-time-series.html)

Parent topic:

Perform Correlation and Spectral Analysis

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=chirp-waveform-advanced-signal-processing-too.html language=enus -->
## TOPIC 00032: Chirp Waveform

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `chirp-waveform-advanced-signal-processing-too.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/chirp-waveform-advanced-signal-processing-too.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The chirp waveform, also known as a swept sine wave, is a sinusoid waveform with a frequency that varies continuously over a certain range of values ω [1] ≤ ω ≤ ω [2] for a specific period of time 0 ≤ t ≤ T.The resulting signal has a crest factor C[f] of √2 . You can modify the signal to excite spec

### Chirp Waveform

The chirp waveform, also known as a swept sine wave, is a sinusoid waveform with a
 frequency that varies continuously over a certain range of values ω <sub>1</sub> ≤ ω ≤ ω
 <sub>2</sub> for a specific period of time 0 ≤ t ≤
 T.

The resulting signal has a crest factor C<sub>f</sub> of √2 . You can modify the signal to excite specific signal spectra.

In comparison to other stimulus signals, such as white noise, a chirp waveform is easier to
 generate and control. You can use the Chirp Pattern VI to generate a
 chirp pattern. You then can use the Build Waveform (Analog Waveform) function to convert
 this chirp pattern to a chirp waveform.

The following figure shows an example of a chirp waveform:

Figure 173.

[IMAGE alt='image' src='GUID-6460CD77-B683-40AC-8162-EDC3A370EACA-a5.gif']

Parent topic:

Choose a Stimulus Signal

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=choose-a-stimulus-signal-advanced-signal-pr.html language=enus -->
## TOPIC 00033: Choose a Stimulus Signal

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `choose-a-stimulus-signal-advanced-signal-pr.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/choose-a-stimulus-signal-advanced-signal-pr.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The choice of stimulus signals has an important role in the system behavior and the accuracy of the estimated model. These signals determine the operating points of the system.While the system under test often limits the choice of signals, you must choose stimulus signals to produce a response of th

### Choose a Stimulus Signal

The choice of stimulus signals has an important role in the system behavior and the
 accuracy of the estimated model. These signals determine the operating points of the
 system.

While the system under test often limits the choice of signals, you must choose stimulus signals
 to produce a response of the system under test. The response provides the information
 you need for developing an accurate model. The response is dependent on the physics of
 the system you want to study. Some systems tend to respond faster than others. Other
 systems have large time constants and delays. For these reasons, defining a stimulus
 signal that provides enough excitation to the system is important. You must choose the
 stimulus signal types according to the system under test to ensure the response contains
 the important features of the system dynamics. Use the following guidelines to choose
 input signal types;

- You want to test the system under conditions similar to the actual operating conditions. When you complete experiments in these conditions, you identify the system in the same conditions under which you will implement the resulting model. This criterion is extremely important for nonlinear systems.
- You want the inputs to the system under test to excite the system. Whether the system is excited is dependent on the spectrum of the input signal. Specifically, you must excite the system with an input frequency similar to the frequency at which such inputs change during normal operations.
- You want the amplitude of the step input to cover a wide range of variations. Therefore, in the data you use for model estimation, you must cover the normal operation range of system inputs, especially when you use the calculated model for model-based control. To cover the normal operation range, you can combine the positive and negative step changes of different magnitudes in the system inputs.
- You want the input signal to deliver as much input power to the system as possible. However, in
 the real-world, you must ensure that this input power stays within the limits of the
 physical system. The crest factor C f , defined by the
 following equation, describes this property: cf2=maxtu2tlimN→∞1N∑t=1Nu2t The smaller the crest factor, the better the signal excitation. A better
 signal excitation results in larger total energy delivery and enhanced
 signal-to-noise ratio. The theoretical lower bound for the crest factor is 1.

The following sections describe the types of stimulus signals you can use for exciting the system
 under test.

- [Filtered Gaussian White Noise](filtered-gaussian-white-noise-advanced-signal.html)
- [Random Binary Signal](random-binary-signal-advanced-signal-processi.html)
- [Pseudo-Random Binary Sequence](pseudo-random-binary-sequence-advanced-signal.html)
- [Chirp Waveform](chirp-waveform-advanced-signal-processing-too.html)
- [Step Signals and Step Responses](step-signals-and-step-responses-advanced-sign.html)

Parent topic:

Acquire Data from a System

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=closed-loop-systems-model-estimation-methods.html language=enus -->
## TOPIC 00034: Closed-Loop Systems Model Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `closed-loop-systems-model-estimation-methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/closed-loop-systems-model-estimation-methods.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Closed-loop model estimation methods use data from a closed-loop system to build a model for a dynamic system that a controller regulates.Systems in many real-world applications contain feedback. Feedback is a process in which the output signal of a dynamic system is passed, or fed back, to the inpu

### Closed-Loop Systems Model Estimation
 Methods

Closed-loop model estimation methods use data from a closed-loop system to build a model
 for a dynamic system that a controller regulates.

Systems in many real-world applications contain feedback. Feedback is a process in which the
 output signal of a dynamic system is passed, or fed back, to the input to regulate the
 next output. Systems without feedback are open-loop systems. Systems with feedback are
 closed-loop systems.

In an open-loop system, the stimulus signal and the output noise do not correlate with each other. In a closed-loop system, the stimulus signal correlates to the output noise. Though you can apply many open-loop model estimation methods to closed-loop data, not all open-loop model estimation methods handle the correlation between the stimulus signal and output noise well.

#### Feedback in
 Systems

Feedback is common in control systems. Feedback regulates the
 system outputs on the basis of a reference input. Feedback also reduces the effect
 of input disturbances. One example of a closed-loop system is a system that
 regulates room temperature, as shown in the following figure. In this example, the
 reference input is the temperature T<sub>set</sub> at which you
 want the room to stay. The thermostat senses the actual temperature,
 T<sub>actual</sub>, of the room. Based on the difference
 between T<sub>actual</sub> and
 T<sub>set</sub>, the thermostat activates the heater or the air
 conditioner. The thermostat returns T<sub>actual</sub> as the
 feedback to compare again with T<sub>set</sub>. Then the
 thermostat uses the difference between T<sub>actual</sub>and
 T<sub>set</sub> to regulate the temperature at the next
 moment.

Figure 196.

[IMAGE alt='image' src='GUID-314AC636-90D2-457C-A79E-5A5641CA94EE-a5.gif']

You must verify if feedback exists before choosing a model estimation method
 because not all open-loop model estimation methods work correctly with closed-loop
 data.

Note

SI Detect
 Feedback

SI Estimate Impulse
 Response

The following figure shows a comparison of the impulse responses of
 the dynamic system in a closed-loop system and an open-loop system:

Figure 197.

[IMAGE alt='image' src='GUID-58B3DC1C-DB65-4630-B687-980D44BC74BE-a5.gif']

The values outside the upper limit and lower
 limit range at the negative lag, which appears between –10 and 0 on
 the x-axis, are considered significant values. Significant values in the impulse
 response at negative lags imply feedback in data. As shown in the following figure,
 significant values exist in the Closed-loop data plot.
 Therefore, feedback exists in the closed-loop system. No significant impulse
 response values exist in the Open-loop data plot. Thus,
 feedback does not exist in the open-loop system.

#### Understanding Closed-Loop Model
 Estimation Methods

The following figure shows a system that consists of a
 dynamic system and a controller. In this system, G<sub>0</sub> is
 the dynamic system, F<sub>y</sub> is the controller,
 H is the stochastic part of the dynamic system,
 u is the stimulus signal, y is the
 response signal, r is the reference signal that is an external
 signal, and e is the output noise. In control engineering, this
 system is known as a feedback-path closed-loop system, which is a typical
 closed-loop system.

Figure 198.

[IMAGE alt='image' src='GUID-1E08FF4A-8CAC-4D91-A172-EB13E563AE88-a5.gif']

In some cases, the controller comes before the dynamic system in a closed-loop
 system. This system is known as a feedforward-path closed-loop system, as shown in
 the following figure:

Figure 199.

[IMAGE alt='image' src='GUID-26F45AA2-CC9B-404D-90E2-05F8DDD30331-a5.gif']

Depending on the amount of prior knowledge you have about the feedback, the
 controller, and the reference signal of a system, you can categorize closed-loop
 model estimation approaches into the following three groups:

Direct identification

Indirect identification

Joint input-output identification

You can choose a suitable model identification approach according to the
 information you have about the closed-loop system. The following table summarizes
 the information you must have to use each identification approach:

| Method | Stimulus Signal | Response Signal | Reference Signal | Controller Information |
| --- | --- | --- | --- | --- |
| Direct | Yes | Yes | — | — |
| Indirect | — | Yes | Yes | Yes |
| Joint Input-Output | Yes | Yes | Yes | — |

With the System Identification VIs, you can choose to use
 the direct, indirect, or joint input-output identification approaches for different
 types of closed-loop systems. The direct identification approach supports
 Single-Input Single-Output (SISO), Multiple-Input Single-Output (MISO), and
 Multiple-Input Multiple-Output (MIMO) systems. The indirect and joint input-output
 identification approaches support SISO systems only.

- [Direct Identification](direct-identification-advanced-signal-process.html)
- [Indirect Identification](indirect-identification-advanced-signal-proce.html)
- [Joint Input-Output Identification](joint-input-output-identification-advanced-si.html)
- [Using System Identification VIs for Model Estimation](using-system-identification-vis-for-model-est.html)

Parent topic:

Estimate Models

Related concepts:

- Impulse Response
- Least Squares Method
- Model Types and Representations

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=compare-polynomial-and-state-space-models-a.html language=enus -->
## TOPIC 00035: Compare Polynomial and State-Space Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `compare-polynomial-and-state-space-models-a.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/compare-polynomial-and-state-space-models-a.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Selecting the correct model type and model order is crucial for successfully estimating a parametric model.In general, state-space models provide a more complete representation of the system, especially for Multiple-Input Multiple-Output (MIMO) systems, than polynomial models because state-space mod

### Compare Polynomial and State-Space
 Models

Selecting the correct model type and model order is crucial for successfully estimating a
 parametric model.

In general, state-space models provide a more complete representation of the system, especially
 for Multiple-Input Multiple-Output (MIMO) systems, than polynomial models because
 state-space models are similar to first principle models that can provide more degree of
 freedom in describing MIMO systems.

The identification procedure for state-space models does not involve nonlinear optimization so
 the estimation reaches a solution regardless of the initial guess. Moreover, the
 parameter settings for the state-space model are simpler. You need to select only the
 order, or the number of states, of the model. The order can come from prior knowledge of
 the system. You also can determine the order by analyzing the singular values of the
 information matrix. However, the states that the state-space identification procedure
 identifies might not reflect the physical characteristics of a system accurately. Using
 a similarity transformation, you can identify equivalent models with states that better
 represent the system. Similarity transformations enable you to transform the states
 without misrepresenting the input-output behavior of the system.

When model order is high, state-space models are preferable to polynomial models. Polynomial
 models with high order might encounter numerical problems in computation.

Parent topic:

Parametric Model Estimation Methods

Related concepts:

- Estimating and Validating a State-Space Model

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=continuous-wavelet-transform.html language=enus -->
## TOPIC 00036: Continuous Wavelet Transform

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `continuous-wavelet-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/continuous-wavelet-transform.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the WA Continuous Wavelet Transform VI to compute the CWT by specifying a set of integer values or arbitrary real positive values for the scales and a set of equal-increment values for the shifts.Mathematically, the Continuous Wavelet Transform (CWT) computes the inner products of a continuous s

### Continuous Wavelet Transform

Use the WA Continuous Wavelet Transform VI to compute the CWT by
 specifying a set of integer values or arbitrary real positive values for the scales and
 a set of equal-increment values for the shifts.

Mathematically, the Continuous Wavelet Transform (CWT) computes the inner products of a
 continuous signal with a set of continuous wavelets according to the following
 equation:

W

T

u

,

a

=

s

,

ψ

u

,

a

=

∫

-

∞

∞

s

t

ψ

u

,

a

*

t

d

t

where

- ψ
 u
 ,
 
 a
 =
 1
 a
 ψ
 t
 -
 u
 a
- WT u,a is the resulting wavelet
 coefficients
- ψ u, a denotes a continuous wavelet
- u is the shift factor
- a is the scale factor of the wavelet
- ψ * u,a is the complex conjugate of
 ψ u,a

For the continuous-time signal s(t), the scale
 factor must be a positive real number, whereas the shift factor can be any real number.
 If the continuous wavelet ψ<sub>u,a</sub> meets the admissibility
 condition, you can use the computed wavelet coefficients to reconstruct the original
 signal s(t).

However, you seldom use the above integration to compute the CWT because of the following
 reasons:

- The majority of real-world signals that you encounter are available as discrete-time samples. The analytical form of the signal s ( t ) usually is not accessible.
- The closed-form solution of the integration does not exist except for very special cases.

For these reasons, you usually select a set of discrete values for the scales and shifts of the
 continuous wavelets and then compute the CWT numerically.

The following figure shows the procedure that the WA Continuous Wavelet
 Transform VI follows:

Figure 111.

[IMAGE alt='image' src='GUID-BA805BB2-C6CD-43DB-8960-78B98E32120A-a5.gif']

The procedure involves the following steps:

1. Shifts a specified wavelet continuously along the time axis.
2. Computes the inner product of each shifted wavelet and the analyzed signal.
3. Dilates the wavelet based on the scale you specify.
4. Repeats steps 1 through 3 till the process reaches the maximum scale you specify.

The output of the CWT is the CWT coefficients, which reflect the similarity between the analyzed signal and the wavelets.

You also can compute the squares of the CWT coefficients and form a scalogram, which is analogous
 to the spectrogram in time-frequency analysis. In signal processing, scalograms are
 useful in pattern-matching applications and discontinuity detections. If a signal
 contains different scale characteristics over time, the scalogram can present a
 time-scale view of the signal, which is more useful than the time-frequency view of that
 signal. Use the WA Configure Scalogram Indicator VI to display the
 scalogram on an intensity graph.

The following figure shows a test signal, the Devil's Staircase fractal signal. An important
 characteristic of a fractal signal is self-similarity:

Figure 112.

[IMAGE alt='image' src='GUID-9D5239B9-7065-4D07-9D92-AD0D05C8D0E5-a5.gif']

The following figure shows the scalogram and the STFT spectrogram of the fractal signal,
 respectively:

Figure 113.

[IMAGE alt='image' src='GUID-319504AD-51B8-4DD0-8677-3C8C57FA639C-a5.gif']

In the previous figure, you can see the self-similarity characteristic of the signal clearly in
 the Scalogram graph but not in the STFT
 Spectrogram graph. The STFT Spectrogram graph
 displays the conventional time-frequency analysis result of the signal.

The CWT has the following general disadvantages:

- The CWT adds excess redundancy and is computationally intensive, so you usually use this transform in offline analysis applications.
- The CWT does not provide the phase information of the analyzed signal. For applications in which
 the phase information is useful, use the Analytic Wavelet Transform (AWT).
- You cannot reconstruct the original signal from the CWT coefficients. For applications that
 require signal reconstruction, use the discrete wavelet tools.

#### Application Example: Breakdown Point
 Detection

One useful CWT application is the detection of abrupt
 discontinuities or breakdown points in a signal. The following figure shows an
 example that detects the breakdown points in a noise-contaminated signal using the
 WA Continuous Wavelet Transform VI:

Figure 114.

[IMAGE alt='image' src='GUID-5E424991-3DFD-410C-91A5-8BCBF0F172F4-a5.gif']

The Signal graph in the previous figure shows the
 HeaviSine signal, which is a common wavelet test signal, contaminated with white
 noise. The HeaviSine signal is a sinusoid with two breakdown points — one at 51 and
 the other at 481. The CWT precisely shows the positions of the two breakdown points
 by doing the following steps:

1. Computes the CWT using the Haar wavelet.
2. Calculates the squares of the CWT coefficients of the signal and forms a
 scalogram, as shown in the Scalogram graph in the
 previous figure.
3. Cumulates the CWT coefficients along the scale axis and
 forms a cumulation plot, as shown in the CWT Coefficients
 Cumulation graph in the previous figure.
4. Detects the peak locations in the CWT Coefficients
 Cumulation graph. The peak locations are where the breakdown
 points exist.

Breakdown points and noise can generate large values in the resulting
 coefficients. Breakdown points generate large positive or negative coefficients at
 all scales. Noise generates positive coefficients at some scales and negative
 coefficients at other scales. If you accumulate the coefficients at all scales, the
 coefficients of breakdown points are enlarged while the coefficients of noise at
 different scales counteract one another. Therefore, the peaks in the CWT
 Coefficients Cumulation graph correspond only to the breakdown
 points.

Parent topic:

Signal Processing with Continuous Wavelets

Related concepts:

- STFT Spectrogram
- Discrete Wavelet Transform

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=convert-models-advanced-signal-processing.html language=enus -->
## TOPIC 00037: Converting Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `convert-models-advanced-signal-processing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/convert-models-advanced-signal-processing.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Model Conversion VIs to convert system models from one representation to another, from continuous to discrete models, and from discrete to continuous models.You can convert models you created in this toolkit to models you can use in another toolkit. You also can convert a model after you est

### Converting Models

Use the Model Conversion VIs to convert system models from one
 representation to another, from continuous to discrete models, and from discrete to
 continuous models.

You can convert models you created in this toolkit to models you can use in another toolkit. You
 also can convert a model after you estimate the model or after you analyze or validate
 the model.

You can use the Model Conversion VIs to switch between different model types
 and representations. For example, when estimating a digital system, you can convert an
 existing continuous model to a discrete model to approximate the real-time behavior of
 the system. You do not need to create a new discrete model for the digital system. Using
 the Model Conversion VIs, you also can convert models you create with
 the System Identification VIs into transfer function, zero-pole-gain,
 or state-space models that you then can use with the LabVIEW Control Design and
 Simulation Module. This model conversion process enables you to identify a
 model for an unknown system with the System Identification VIs and
 then design a controller for this system using the Control Design and
 Simulation Module.

Parent topic:

Analyze, Validate, and Convert Models

Related concepts:

- Model Types and Representations
- Parametric Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=correlation-analysis-method-advanced-signal-p.html language=enus -->
## TOPIC 00038: Correlation Analysis Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `correlation-analysis-method-advanced-signal-p.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/correlation-analysis-method-advanced-signal-p.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The correlation analysis method uses the cross correlation between the input and output signals as an estimation of the impulse response.The correlation analysis method is represented by the following equation:yk=∑n=0∞uk-nhn+ekThe input signal must be zero-mean white noise with a spectral density th

### Correlation Analysis Method

The correlation analysis method uses the cross correlation between the input and output
 signals as an estimation of the impulse response.

The correlation analysis method is represented by the following equation:

y

k

=

∑

n

=

0

∞

u

k

-

n

h

n

+

e

k

The input signal must be zero-mean white noise with a spectral density that is equally
 distributed across the whole frequency range. The SI Estimate Impulse
 Response VI can prewhiten input signals that are not white noise.

Assuming the input u(k) of the system is a
 stationary, stochastic process and statistically independent of the disturbance
 e(k), the following equation is true:

R

u

y

τ

=

∑

k

=

0

∞

R

u

u

k

-

τ

h

k

R<sub>uy</sub>represents the cross-correlation function between the
 stimulus signal u(k) and the response signal
 y(k), as defined by the following
 equation:

R

u

y

τ

=

1

N

∑

k

-

m

i

n

τ

,

0

N

-

m

a

x

τ

,

0

-

1

y

k

+

τ

u

k

R<sub>uu</sub> represents the autocorrelation of the stimulus signal
 u(k), as defined by the following
 equation:

R

u

u

τ

=

1

N

∑

k

=

0

N

-

τ

-

1

u

k

+

τ

u

k

N is the number of data points. If the stimulus signal is a zero-mean
 white noise signal, the autocorrelation function reduces to the following equation:

R

u

u

τ

=

σ

u

2

δ

τ

where σ<sub>u</sub> is the standard deviation of the stimulus white
 noise and δ(τ) is the Dirac function. Substituting
 R<sub>uu</sub>(τ) into the cross-correlation
 function between the stimulus signal u(k) and the
 response signal y(k) yields the following
 equation:

R

u

y

τ

=

σ

u

2

∑

k

=

0

∞

δ

k

-

τ

h

k

=

σ

u

2

h

τ

You can rearrange the terms of this equation to obtain the following equation defining
 the impulse response h(k):

h

k

=

R

u

y

k

σ

u

2

#### Prewhitening

The
 correlation analysis method that estimates the impulse response is useful only when
 the input signal u(k) is a zero-mean white
 noise signal. However, the input signal is not white noise in most real-world
 applications. Therefore, you must precondition the input
 u(k) and output
 y(k) signals before you apply the
 correlation analysis method.

Prewhitening is a preconditioning technique for
 the correlation analysis method. Prewhitening involves applying a filter to the
 input signal u(k) and the output signal
 y(k) to obtain a prewhitened input signal
 u'(k) and a prewhitened output signal
 y'(k). If the filter is well designed such
 that u'(k) is white noise, you can perform a
 correlation analysis on u'(k) and
 y'(k) to estimate the impulse response.
 The impulse response that you estimate with
 u'(k) and
 y'(k) is equivalent to the impulse
 response that you estimate with u(k) and
 y(k) because the following equation
 remains true:

y

'

k

=

∑

n

=

0

∞

u

'

k

-

n

h

n

+

e

k

You now must design the prewhitening filter so that
 u'(k) is white noise. The SI
 Estimate Impulse Response VI uses an AR model for this
 purpose.

#### Accuracy of the Impulse
 Response

The accuracy of the impulse response estimation using the
 correlation analysis method depends on the performance of the prewhitening filter,
 specifically whether the filter produces a white noise result
 u'(k) for
 u(k). The performance of the filter
 depends on the signal and the AR order of the filter. The rule of thumb for
 selecting the AR order is trial-and-error. If
 u'(k) is not white enough, the result from
 the correlation method is not reliable. You can increase the AR order to improve the
 accuracy of the impulse response.

The SI Estimate Impulse
 Response VI provides the outputs whiteness test
 and rejected? to indicate whether you have properly set the
 AR order and consequently whether the impulse response estimation is reliable. The
 following example shows how the whiteness property of the input signal affects the
 correlation analysis method and how to use the outputs whiteness
 test and rejected? to justify the impulse
 response estimation.

The following figure shows the front panel of a VI that
 simulates a system defined by the following
 equation:

y(k) =
 0.2u(k) +
 0.8u(k – 1) +
 0.3u(k – 2)

Figure 181.

y

k

u

k

u

k

u

k

[IMAGE alt='image' src='GUID-703A6605-B413-4276-B812-1D70F27972CD-a5.gif']

The following figure shows the block diagram of this VI. This example VI
 demonstrates the accuracy of the impulse response estimation in the following
 circumstances:

- Zero-mean, pseudo-white noise input signal without prewhitening
- Zero-mean, pseudo-white noise input signal with prewhitening
- Nonzero-mean, white noise input signal without prewhitening
- Nonzero-mean white noise input signal with prewhitening

Figure 182.

[IMAGE alt='image' src='GUID-F7E81760-2E84-4285-9EC1-C303D8080B38-a5.gif']

In this example VI, the is white noise? checkbox
 determines whether the SI Estimate Impulse Response VI generates
 zero-mean white noise as an input to the system. When you place a checkmark in the
 is white noise? checkbox and run the VI, the generated
 input signal is zero-mean white noise, and the estimated impulse response closely
 approximates the true impulse response. When you do not place a checkmark in the
 is white noise? checkbox, the generated input signal is
 not zero-mean white noise. As a result, the estimated impulse response is different
 from the true impulse response. These results indicate that the correlation analysis
 method is accurate and reliable when the input signal is zero-mean white
 noise.

The AR order box determines the level of
 prewhitening. When AR order equals 0, the SI
 Estimate Impulse Response VI does not apply prewhitening to the
 system. When AR order is small and you do not place a
 checkmark in the is white noise? checkbox, the variance of
 the impulse response is large because the input signal is not always white noise.
 The greater the value of AR order, the better the VI whitens
 the signal, but the more computation time and memory the VI requires.

The
 whiteness test indicator of this VI shows whether the
 input is zero-mean white noise. This indicator displays the autocorrelation of the
 stimulus signal after whitening. If most of the autocorrelation is within the
 confidence region, the input signal is well prewhitened, and the estimation of the
 impulse response is reliable. If the autocorrelation is outside of the confidence
 region, the estimation is unreliable. When the estimation is unreliable,
 rejected? is TRUE and indicates a 5%
 risk of rejecting an impulse response estimation that might be reliable.

If
 you apply proper prewhitening, the correlation analysis method is accurate and
 reliable for any input signal. To obtain the best prewhitening settings, start with
 a small AR order value, such as 2, and observe the
 whiteness test and rejected?
 outputs of the SI Estimate Impulse Response VI. If necessary,
 increase the value of AR order. Generally, the smaller the
 bandwidth of the input signal, the larger the AR order you
 need. A large AR order slows the estimation performance. The
 default AR order value is 50.

Parent topic:

Impulse Response

Related concepts:

- AR Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=correlation-methods.html language=enus -->
## TOPIC 00039: Correlation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `correlation-methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/correlation-methods.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Correlation analysis can be performed either by correlating a time series with itself, auto-correlation, or by measuring the similarity between two different time series, cross-correlation. Auto-CorrelationAuto-correlation is the correlation of a time series with itself. You can use the auto-correla

### Correlation Methods

Correlation analysis can be performed either by correlating a time series with
 itself, auto-correlation, or by measuring the similarity between two different time
 series, cross-correlation.

#### Auto-Correlation

Auto-correlation is the correlation of a time series
 with itself. You can use the auto-correlation method to capture periodic components
 in a univariate time series without other reference time series. The
 auto-correlation operation preserves the frequency and amplitude information of
 periodic components but does not preserve the phase information.

The following
 figure shows two noise-contaminated, phase-jittered time series and the resulting
 auto-correlation plots. In the Auto-Correlation 1 and
 Auto-Correlation 2 graphs, you can see that
 auto-correlation greatly attenuates the noise in the original time series, thereby
 potentially improving the accuracy and reliability of subsequent frequency or
 periodicity estimates calculated for the time series.

Figure 86.

[IMAGE alt='image' src='GUID-0984D90B-E4E5-4C44-9512-EBD1B183BFE7-a5.gif']

As the previous figure shows, though the time series in the Time
 Series 1 and Time Series 2 have a difference
 in phase, the auto-correlations are close to each other. Therefore, auto-correlation
 does not preserve the phase information, which can be a beneficial property in
 applications such as feature extraction.

When performing auto-correlation of a
 time series, you can choose either biased or unbiased weighting. Biased weighting is
 helpful when you perform spectral analysis with the Fourier transform, because
 biased weighting can reduce spectral leakage, bias, and variance in the resulting
 power spectrum. Unbiased weighting is suitable for periodicity detection in the time
 domain. If you use unbiased weighting, the amplitudes of the auto-correlation values
 do not decrease as the lag increases.

The following figure shows a time series
 of a sinusoidal pattern:

Figure 87.

[IMAGE alt='image' src='GUID-CB6C83EB-FF8A-4A55-9BB3-D618A3A008F3-a5.gif']

The following figure shows the estimated biased and unbiased auto-correlation of
 the sinusoidal pattern, respectively:

Figure 88.

[IMAGE alt='image' src='GUID-6272D429-2C96-4CB6-8DD2-02E55B6982F8-a5.gif']

Use the TSA Auto-Correlation Function VI to perform
 auto-correlation operations on a univariate time series.

You also can perform
 partial auto-correlation on a time series using the TSA Auto-Correlation
 Function VI. Partial auto-correlation is useful for estimating the
 Autoregressive (AR) model order of a time series.

#### Cross-Correlation

Cross-correlation measures the similarity between two
 time series. You can find the features of an unknown time series by computing the
 cross-correlation between the unknown time series and a known time series. For
 example, if you know the frequency of a sinusoid time series but do not know the
 amplitude and phase, you can derive the amplitude and phase of the time series with
 the cross-correlations. The following figure shows the flowchart of obtaining the
 magnitude response and phase response of a physical system with the
 cross-correlation method:

Figure 89.

[IMAGE alt='image' src='GUID-B12C496D-8A27-43D8-BBC4-BEE6F400B392-a5.gif']

In this flowchart, a sinusoid stimulus signal
 x(t) =
 sin(ω<sub>0</sub>t) at a specified frequency ω<sub>0</sub> is
 applied to the physical system. The system then generates the response signal
 y(t) =
 A(ω<sub>0</sub>)sin(ω<sub>0</sub>t +
 φ(ω<sub>0</sub>)). A(ω<sub>0</sub>) and φ(ω<sub>0</sub>)
 define the magnitude response and phase response of the physical system at
 ω<sub>0</sub>, respectively. The term 1/2Asin(φ<sub>0</sub>)
 is obtained by performing cross-correlation between the stimulus signal
 x(t) and the response signal y(t) at τ =
 0, where τ denotes the lag. The term 1/2Acos(ω<sub>0</sub>) is
 obtained by performing cross-correlation between the phase-delayed stimulus signal
 x(t) = cos(ω<sub>0</sub>t) and the
 response signal y(t) at τ = 0. You can obtain the magnitude
 response A(ω<sub>0</sub>) from the square root of
 (1/2Asin(φ<sub>0</sub>))<sup>2</sup> +
 (1/2Acos(φ<sub>0</sub>))<sup>2</sup>. You can obtain the
 phase response φ(ω<sub>0</sub>) from the inverse tangent of the quotient of
 1/2Asin(φ<sub>0</sub>) divided by
 1/2Acos(φ<sub>0</sub>). If you change the frequency of the
 stimulus signal, you can obtain the response of the system at other
 frequencies.

Use the TSA Cross-Correlation Function VI to
 perform cross-correlation on two time series.

Parent topic:

Perform Correlation and Spectral Analysis

Related concepts:

- Building Autoregressive Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=data-scaling-advanced-signal-processing-toolk.html language=enus -->
## TOPIC 00040: Data Scaling

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `data-scaling-advanced-signal-processing-toolk.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/data-scaling-advanced-signal-processing-toolk.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To resolve Multiple-Input Multiple-Output (MIMO) systems whose inputs and outputs have different amplitude ranges, you can scale the data ranges of each input and output.For example, consider the valves A and B in the following figure:177 MIMO System Where Valve A and B Have DIfferent AmplitudesValv

### Data Scaling

To resolve Multiple-Input Multiple-Output (MIMO) systems whose inputs and outputs have
 different amplitude ranges, you can scale the data ranges of each input and output.

For example, consider the valves A and B in the following figure:

Figure 177.

[IMAGE alt='image' src='GUID-FD79C488-B28E-48ED-8A9F-7958338995DF-a5.gif']

Valves A and B operate between 0–100% and 50–60%,
 respectively. The pressure in the respective stream lines are
 P<sub>A</sub> and P<sub>B</sub>. If you assume
 that P<sub>B</sub> can be much larger than
 P<sub>A</sub>, you might need to normalize the range of operation
 of valve B for numerical robustness. You can use the following
 relationship to normalize the range of operation:

∆

L

e

v

e

l

∆

%

A

=

∆

L

e

v

e

l

∆

%

B

-

50

·

10

The SI Normalize VI ensures that all stimulus and response signals have a zero
 mean and unit variance over the sample data range used for model estimation. This
 process standardizes the range of the equation for all signals considered for model
 estimation. This data preprocessing step considers all inputs and outputs equally
 important from the numerical calculation viewpoint.

Parent topic:

Preprocess Data from a System

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=define-and-estimate-partially-known-model.html language=enus -->
## TOPIC 00041: Define and Estimate Partially Known Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `define-and-estimate-partially-known-model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/define-and-estimate-partially-known-model.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Choose a model for the dynamic system and set parameter constraints for the model then estimate the model to represent the dynamic system.Before estimating partially known models, you first must define those models. Use the SI Create Partially Known State-Space Model VI and the SI Create Partially K

### Define and Estimate Partially Known
 Models

Choose a model for the dynamic system and set parameter constraints for the model then
 estimate the model to represent the dynamic system.

Before estimating partially known models, you first must define those models. Use the SI
 Create Partially Known State-Space Model VI and the SI Create
 Partially Known Continuous Transfer Function Model VI to define partially
 known models.

Use the SI Create Partially Known State-Space Model VI to define partially
 known continuous or discrete state-space models.

You can use the SI Create Partially Known State-Space Model VI, for example,
 to define a state-space model that represents an RLC circuit consisting of a resistor
 R, an inductor L, and a capacitor
 C. Using prior knowledge, you describe the relationship of
 R, L, and C with the
 following equations:

A

=

0

1

-

1

L

×

C

-

R

L

B

=

0

1

L

×

C

C

=

1

0

D

=

0

You also can use prior knowledge to define the initial guesses and upper and lower limits of
 R, L, and C. The
 SI Create Partially Known State-Space Model VI uses variables
 rather than numerical values to construct a symbolic model. As the following figure
 shows, you use variable names, such as R, L, and
 C, in the symbolic A, symbolic
 B, symbolic C, and symbolic
 D inputs to define the RLC circuit. Then you specify values for
 R, L, and C in the
 variables input.

Figure 194.

[IMAGE alt='image' src='GUID-49D6B263-2287-42D1-8257-AD8B1D4DAE21-a5.gif']

Use the SI Create Partially Known Continuous Transfer Function Model VI to
 define partially known continuous transfer function models. The following equation
 represents a continuous transfer function model:

k

p

1

+

a

1

s

+

a

2

s

2

.

.

.

∏

i

1

+

T

p

i

s

∏

j

1

+

2

r

j

s

w

j

+

s

w

j

2

e

-

s

T

d

where

- K p is the transfer function gain
- T d is the delay
- T p is the first-order time constant
- w is the natural frequency
- r is the damping ratio
- s represents the time

You can apply the prior knowledge you have about the parameters K,
 T<sub>d</sub>, T<sub>p</sub>,
 w, and r to the static
 gain, delay(s),
 T<sub>p</sub>(s), natural
 freq (rad/s), and damping ratio inputs,
 respectively, of the SI Create Partially Known Continuous Transfer Function
 Model VI by defining the initial guesses and upper and lower limits.

With the System Identification VIs and a partially known model, you can set
 constraints on each parameter of a state-space or continuous transfer function model in
 two ways — with an upper and lower limit or with an initial guess.

- [Setting Parameter Constraints with a Range](setting-parameter-constraints-with-a-range-ad.html)
- [Setting Parameter Constraints with an Initial Guess](setting-parameter-constraints-with-an-initial.html)

Parent topic:

Partially Known Model Estimation Methods

Related concepts:

- State-Space Model Definitions
- Transfer Function Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=design-the-product-p0-z.html language=enus -->
## TOPIC 00042: Design the Product P0(z)

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `design-the-product-p0-z.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/design-the-product-p0-z.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The auxiliary function P[0](z) denotes the product of G[0](z) and H[0](z).Use the following equation to calculate P[0](z):P[0](z) = G[0](z) + H[0](z)You usually use one of the following three types of filters for P[0](z).Maximally-flatGeneral equiripple halfbandPositive equiripple halfbandThe maxima

### Design the Product P0(z)

The auxiliary function P<sub>0</sub>(z) denotes the
 product of G<sub>0</sub>(z) and
 H<sub>0</sub>(z).

Use the following equation to calculate
 P<sub>0</sub>(z):

P<sub>0</sub>(z) =
 G<sub>0</sub>(z) +
 H<sub>0</sub>(z)

You usually use one of the following three types of filters for
 P<sub>0</sub>(z).

- Maximally-flat
- General equiripple halfband
- Positive equiripple halfband

The maximally-flat filter is defined by the following equation:

P<sub>0</sub>(z) = (1 + z<sup>–1</sup>)<sup>2</sup><sup>p</sup>Q(z)

In the Wavelet Design Express VI, the Zero pairs at
 π  (P0) control on the Configure
 Wavelet Design dialog box specifies the value of the parameter
 p, which determines the number of zeros placed at π on the unit
 circle. The more the zeros at π, the smoother the corresponding wavelet. The value of
 p also affects the transition band of the frequency response. A
 large value of presults in a narrow transition band. In the time
 domain, a narrower transition band implies more oscillations in the corresponding
 wavelet. When you specify a value for the parameter p, you can review
 the frequency response shown on the right-hand side of the Configure Wavelet
 Design dialog box.

In a general equiripple halfband filter, halfband refers to a filter in which
 ω<sub>s</sub> + ω<sub>p</sub> = π, where
 ω<sub>s</sub> denotes the stopband frequency and
 ω<sub>p</sub> denotes the passband frequency, as shown in the
 following figure:

Figure 141.

[IMAGE alt='image' src='GUID-D8FA1BF9-E969-4573-8D6D-12559CE3E7F2-a5.gif']

The positive equiripple halfband filter is a special case of general equiripple halfband filters.
 The Fourier transform of this type of filter is always nonnegative. Positive equiripple
 halfband filter is appropriate for orthogonal wavelets because the auxiliary function
 P<sub>0</sub>(z) must be nonnegative.

Use the P<sub>0</sub>type control to specify the P<sub>0</sub>(z) type. When Wavelet Type is set to Orthogonal, you can set P<sub>0</sub>(z) either to Maxflat (default), for a maximally-flat filter, or to Positive Equiripple. When Wavelet Type is set to Biorthogonal, you can set P<sub>0</sub>(z) to Maxflat (default), Positive Equiripple, or General Equiripple.

Because all filters, including P<sub>0</sub>(z),
 G<sub>0</sub>(z), and
 H<sub>0</sub>(z), are real-valued finite
 impulse response (FIR) filters, the zeros of these filters are mirror-symmetric about
 the x-axis in the z-plane. Therefore, for any zero
 z<sub>i</sub>, a corresponding complex
 conjugate z<sub>i</sub>* always exists. If
 z<sub>i</sub> is complex, meaning that if
 z<sub>i</sub> is located off of the x-axis,
 you always can find a corresponding zero on the other side of the x-axis, as shown in
 the following figure. As a result, you only need to see the top half of the z-plane to
 see all of the zeros that are present. After you select
 z<sub>i</sub>, the Wavelet Design
 Express VI automatically includes the complex conjugate
 z<sub>i</sub>*.

Figure 142.

[IMAGE alt='image' src='GUID-966EC1E3-AA54-4FAD-A154-FADD5948F49C-a5.gif']

Two parameters are associated with equiripple filters — # of taps and
 Passband. Use the # of taps control to
 define the number of coefficients of
 P<sub>0</sub>(z). Because
 P<sub>0</sub>(z) is a type-I FIR filter, the
 length of P<sub>0</sub>(z) must be odd. Use the
 Passband control to define the normalized passband frequency,
 ω<sub>p</sub>, of
 P<sub>0</sub>(z). The value of
 ω<sub>p</sub> must be less than 0.5. Longer filters improve
 the sharpness of the transition band and the magnitude of the attenuation in the
 stopband at the expense of extra computation time for implementation.

Parent topic:

Interactively Designing Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=determining-parameters-for-the-prediction-err.html language=enus -->
## TOPIC 00043: Determining Parameters for the Prediction Error Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `determining-parameters-for-the-prediction-err.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/determining-parameters-for-the-prediction-err.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Determining the delay and model order for the prediction error method is typically a trial-and-error process.The identification method for most of the polynomial models is the prediction error method. Follow these steps to find a suitable model, though other methods may also be effective and these s

### Determining Parameters for the Prediction
 Error Method

Determining the delay and model order for the prediction error method is typically a
 trial-and-error process.

The identification method for most of the polynomial models is the prediction error method.
 Follow these steps to find a suitable model, though other methods may also be effective
 and these steps are not exhaustive:

1. Obtain useful information about the model order by observing the number of resonance peaks in
 the nonparametric frequency response function. Normally, the number of peaks in the
 magnitude response equals half the order of
 A ( z ) F ( z ).
2. Obtain a reasonable estimate of the delay by observing the impulse response or by testing reasonable values in a medium-sized ARX model. Choose the delay that provides the best model fit based on prediction errors or another criterion.
3. Test various ARX model orders with this delay, choosing those orders that provide the best
 fit.
4. Reduce the model order by plotting the poles and zeros with confidence intervals and looking for
 potential cancellations of pole-zero pairs. The resulting model might be
 unnecessarily high in order because the ARX model describes both the system dynamics
 and noise properties using the same set of poles. The ARMAX, output-error, and
 Box-Jenkins models use the resulting orders of the poles and zeros as the
 B and F model parameters and the first- or
 second-order models for the noise characteristics.
5. Determine if additional signals influence the output if you cannot obtain a suitable model at this point. You can incorporate measurements of these signals as extra input signals.

If you still cannot obtain a suitable model, additional physical insight into the problem might
 be necessary. Compensating for nonlinear sensors or actuators and handling important
 physical nonlinearities often are necessary in addition to using a ready-made model.

From the prediction error standpoint, the higher the order of the model is, the better the model
 fits the data because the model has more degrees of freedom. However, you need more
 computation time and memory for higher orders. The parsimony principle says to choose
 the model with the smallest degree of freedom, or number of parameters, if all the
 models fit the data well and pass the verification test. The criteria to assess the
 model order therefore not only must rely on the prediction error but also must
 incorporate a penalty when the order increases. Akaike's Information Criterion (AIC),
 Final Prediction Error Criterion (FPE), and the Minimum Description Length Criterion
 (MDL) are criteria you can use to estimate the model order. The SI Estimate
 Orders of System Model VI implements the AIC, FPE, and MDL methods to
 search for the optimal model order in the range of interest. You also can plot the
 prediction error as a function of the model dimension and then visually find the minimum
 in the curve or apply an F-test to obtain an appropriate estimation of the model
 order.

#### Akaike's Information
 Criterion

The Akaike's Information Criterion (AIC) is a weighted estimation error based on the
 unexplained variation of a given time series with a penalty term when exceeding the
 optimal number of parameters to represent the system. For the AIC, an optimal model
 is the one that minimizes the following equation:

A

I

C

=

V

n

1

+

2

p

N

N is the number of data points, V<sub>n</sub>
 is an index related to the prediction error, or the residual sum of squares, and
 p defines the number of parameters in the
 model.

#### Final Prediction Error
 Criterion

The Final Prediction Error Criterion (FPE) estimates the model-fitting error when
 you use the model to predict new outputs. For the FPE, an optimal model is the one
 that minimizes the following equation:

F

P

E

=

V

n

1

+

2

p

N

-

p

You want to choose a model that minimizes the FPE, which represents a balance between
 the number of parameters and the explained variation.

#### Minimum Description Length
 Criterion

The Minimal Description Length Criterion (MDL) is based on V<sub>n</sub> plus a
 penalty for the number of terms used. For the MDL, an optimal model is the one that
 minimizes the following equation:

M

D

L

=

V

n

1

+

p

ln

N

N

You want to choose a model that minimizes the MDL, which allows the shortest
 description of data you measure.

Parent topic:

Parametric Model Estimation Methods

Related concepts:

- General-Linear Model Definitions
- Analyze Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=direct-identification-advanced-signal-process.html language=enus -->
## TOPIC 00044: Direct Identification

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `direct-identification-advanced-signal-process.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/direct-identification-advanced-signal-process.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the stimulus and response signals of a closed-loop system are available but you do not have any other information about the system, you can use only the techniques developed for open-loop models to estimate the closed-loop system.Keep in mind, you cannot apply all open-loop identification methods

### Direct Identification

If the stimulus and response signals of a closed-loop system are available but you do not
 have any other information about the system, you can use only the techniques developed
 for open-loop models to estimate the closed-loop system.

Keep in mind, you cannot apply all open-loop identification methods to estimate the model of a
 dynamic system in a closed-loop system. Some open-loop model identification methods
 assume zero correlation between the stimulus signal and output noise. In closed-loop
 systems, this correlation is nonzero. Therefore, if you use certain open-loop model
 estimation methods, such as the Instrument Variable (IV) method and the correlation
 analysis methods, with closed-loop data, you might estimate a model incorrectly. You can
 use the prediction error method to identify the dynamic system in a closed-loop
 system.

The direct identification approach is used commonly in real-world applications. This approach is
 convenient because you do not need to have additional information about a closed-loop
 system, such as the reference signal or the controller. However, the estimation might
 not be accurate if the model type you select for a dynamic system does not describe the
 output noise of the system accurately. For example, if the output noise of a dynamic
 system is color noise and you select an Output-Error (OE) model, which assumes the
 output noise is white noise, the estimation for the OE model might be biased when you
 use direct identification. The bias might be small, though, if the Signal-to-Noise Ratio
 (SNR) of the system is high.

Parent topic:

Closed-Loop Systems Model Estimation Methods

Related concepts:

- Correlation Analysis Method
- Output-Error Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=discrete-gabor-transform-and-expansion.html language=enus -->
## TOPIC 00045: Discrete Gabor Transform and Expansion

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `discrete-gabor-transform-and-expansion.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/discrete-gabor-transform-and-expansion.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The discrete Gabor transform is an invertible, linear time-frequency transform whose output is called the Gabor coefficients. The discrete Gabor expansion is the inverse of the discrete Gabor transform.Characteristics of time-varying signals that are not obvious in the time domain or in the frequenc

### Discrete Gabor Transform and Expansion

The discrete Gabor transform is an invertible, linear time-frequency transform whose
 output is called the Gabor coefficients. The discrete Gabor expansion is the inverse of
 the discrete Gabor transform.

Characteristics of time-varying signals that are not obvious in the time domain or in the
 frequency domain alone can become clear in the time-frequency domain when you apply the
 discrete Gabor transform. The discrete Gabor expansion is the inverse of the discrete
 Gabor transform. After you extract the useful features of a signal in the time-frequency
 domain, you can apply the discrete Gabor expansion to obtain the time waveform with the
 extracted features. Similarly, after you suppress the useless components, like noise, in
 the time-frequency domain, you can apply the discrete Gabor expansion to obtain the time
 waveform with the noise suppressed.

In the following equation, the Gabor expansion represents a time-domain signal,
 s(i), as the linear combination of elementary
 functions h<sub>m,n</sub>(i):

s

i

=

∑

m

=

0

M

-

1

∑

n

=

0

N

-

1

c

m

,

n

h

m

,

n

i

where

- h m,n ( i ) is the time-frequency
 elementary function
- C m,n is the weight of
 h m,n ( i )
- C m,n is the Gabor coefficients

The Gabor transform computes the Gabor coefficients C<sub>m,n</sub>
 for the signal s(i).

#### Synthesis Window, Analysis Window,
 and Dual Window

Because the discrete Gabor transform is a special case of
 the STFT, you must consider the effects of the window characteristics and understand
 how the window length and type affect the time-frequency resolution of the
 time-frequency representation. The window used with the discrete Gabor transform is
 called the analysis window. The window used with the discrete Gabor expansion is
 called the synthesis window.

The following equation defines the time-shifted
 and frequency-modulated version,
 h<sub>m,n</sub>(i), of a window function,
 h(i):

h

m

,

n

i

=

h

i

-

m

d

M

e

x

p

j

2

π

n

i

N

where

- h ( i ) is the synthesis window
- dM is time step)
- N is frequency bins

C<sub>m,n</sub> reveals how the signal behaves in the joint
 time-frequency domain around the time and the frequency centers of
 h<sub>m,n</sub>(i).

You can use the
 Gabor transform to obtain the Gabor coefficients C<sub>m,n</sub>
 with the following equation:

c

m

,

n

=

∑

i

s

i

γ

·

i

-

m

d

M

e

x

p

-

j

2

π

n

i

N

where

- γ ( i ) is the analysis window
- γ ( i ) and
 h ( i ) are a pair of dual functions
 because you use one for the Gabor transform and the other for the Gabor
 expansion, respectively

Usually, you specify the synthesis window
 h(i) first and then use the TFA
 Dual Window VI to compute the corresponding analysis window
 (γ(i)).

To reconstruct the
 time-domain signal accurately from the Gabor time-frequency representation, you must
 use appropriate, complementary analysis and synthesis windows. You can exchange the
 analysis windows and the synthesis windows, meaning that you can use the synthesis
 windows for the Gabor transform and use the analysis windows for the Gabor
 expansion. Therefore, the analysis windows and the synthesis windows are called dual
 windows. Usually, you first specify the synthesis window, such as a Gaussian window.
 Given a synthesis window, you must use the TFA Dual Window VI to
 compute the corresponding analysis window. You also can use the Dual Window
 Express VI to design the dual windows for the discrete Gabor transform
 and the discrete Gabor expansion interactively.

#### Oversampling Rate

You can consider h<sub>m,n</sub>(i) as the
 discrete atoms in the time-frequency domain as shown in the following grid:

Figure 8.

h

m,n

i

[IMAGE alt='image' src='GUID-9A4AEA26-6E52-4FFC-9020-ED0CBFAEF0FC-a5.gif']

The cross points in the grid are the time and the frequency centers of the
 elementary functions. The time and the frequency centers of
 h<sub>m,n</sub>(i) in normalized units are
 mdM and 2πn/N,
 respectively.

You can consider the Gabor expansion as a way to resample the
 time-domain signal in the joint time-frequency domain. The time sampling interval in
 the joint time-frequency domain is dM. The frequency sampling
 interval in the joint time-frequency domain is 2π/N.

The time centers and frequency centers of the elementary functions used in a
 particular Gabor transform application are discrete and form an equally sampled grid
 in the time-frequency domain, as shown in the previous figure. If the time-frequency
 center of a signal component is not aligned with the time-frequency sampling grid,
 some spectral energy from that signal component might spread erroneously to adjacent
 points in the time-frequency plane. This energy leakage can distort the resulting
 time-frequency spectrum and introduce confusing artifacts in the spectrum.
 Therefore, the discrete Gabor transform and the discrete Gabor expansion are not
 always the best way to analyze time-varying signals.

The number of sampling points in the time-frequency domain is M×N. The ratio of the
 total sampling points in the time-frequency domain and in the time domain, that is,
 MN/L, is called the oversampling rate, where
 L is the signal length. Because M = L/dM,
 the oversampling rate equals N/dM. The oversampling rate must be
 greater than or equal to 1 to reconstruct the time-domain signal from the
 time-frequency domain representation.

#### Using the Discrete Gabor Transform
 and Discrete Gabor Expansion

The following figure shows the typical steps
 for creating applications using the discrete Gabor transform and the discrete Gabor
 expansion:

Figure 9.

[IMAGE alt='image' src='GUID-ADF49800-BF21-40C3-A3FC-6BFDB470C0BB-a5.gif']

To reduce noise or separate components of a time-varying signal, you first use
 the discrete Gabor transform to compute the time-frequency representation of a
 signal, modify the time-frequency representation of the signal, and then apply the
 discrete Gabor expansion to reconstruct the time-domain signal with the modified
 time-frequency representation.

Use the TFA Discrete Gabor
 Transform VI and the TFA Discrete Gabor Expansion
 VI to compute the Gabor transform and Gabor expansion.

Masking and
 thresholding are the most commonly used methods to modify a signal in the
 time-frequency domain. A mask defines which parts of the time-frequency
 representation remain and which parts to set to zero. The threshold defines which
 parts of the time-frequency representation with magnitudes greater than the
 threshold remain and which parts to set to zero. The mask and the threshold are
 similar to filters with time-dependent specifications. This kind of application
 commonly is called time-varying filtering.

Use the TFA Time Varying
 Filter VI and the Time Varying Filter (Thresholding)
 Express VI to perform time-varying filtering interactively, such as in
 noise reduction and feature extraction applications. Many other methods exist to
 modify the time-frequency representation, for example, setting the phase of the
 time-frequency representation to zero or setting the magnitude of the time-frequency
 representation to unity.

The following figure shows an example of a noisy
 signal that contains three chirps:

Figure 10.

[IMAGE alt='image' src='GUID-28BDFBE3-B441-4A47-AE87-7731B410A1CF-a5.gif']

The color corresponds to the magnitude of the Gabor coefficients from the
 discrete Gabor transform. The color spectrum from red to blue corresponds to the
 magnitude from maximum to minimum. The Gabor coefficients that correspond to the
 chirps have a higher magnitude and are concentrated in a relatively small region in
 the time-frequency domain. The Gabor coefficients that correspond to the noise have
 a lower magnitude and are spread over the entire time-frequency domain. By applying
 a thresholding operation, you can preserve the Gabor coefficients that correspond to
 the chirps and reduce to zero the Gabor coefficients that correspond to noise. The
 Time Varying Filter (Thresholding) Express VI reconstructs
 the denoised chirps from these modified Gabor coefficients by using the discrete
 Gabor expansion, as shown in the following figure:

Figure 11.

[IMAGE alt='image' src='GUID-F761A915-5508-44EE-A5FB-13923267931B-a5.gif']

Parent topic:

Linear Time Frequency Analysis Methods

Related concepts:

- Short-Time Fourier Transform

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=discrete-wavelet-transform.html language=enus -->
## TOPIC 00046: Discrete Wavelet Transform

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `discrete-wavelet-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/discrete-wavelet-transform.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Implement Discrete Wavelet Transform (DWT) using discrete filter banks to compute discrete wavelet coefficients.Unlike the Discrete Fourier Transform (DFT), which is a discrete version of the Fourier transform, the Discrete Wavelet Transform (DWT) is not really a discrete version of the Continuous W

### Discrete Wavelet Transform

Implement Discrete Wavelet Transform (DWT) using discrete filter banks to compute
 discrete wavelet coefficients.

Unlike the Discrete Fourier Transform (DFT), which is a discrete version of the Fourier
 transform, the Discrete Wavelet Transform (DWT) is not really a discrete version of the
 Continuous Wavelet Transform (CWT). Instead, the DWT is functionally different from the
 CWT. Two-channel Perfect Reconstruction (PR) filter banks are a common and efficient way
 to implement the DWT. The following figure shows a typical two-channel PR filter bank
 system:

Figure 124.

[IMAGE alt='image' src='GUID-335E0B8E-EB15-492E-AE89-F511FC10E797-a5.gif']

The signal X(z) first is filtered by a filter bank consisting of G<sub>0</sub>(z) and G<sub>1</sub>(z). The outputs of G<sub>0</sub>(z) and G<sub>1</sub>(z) then are downsampled by a factor of 2. After some processing, the modified signals are upsampled by a factor of 2 and filtered by another filter bank consisting of H<sub>0</sub>(z) and H<sub>1</sub>(z).

If no processing takes place between the two filter banks, the sum of outputs of H<sub>0</sub>(z) and H<sub>1</sub>(z) is identical to the original signal X(z), except for the time delay. This system is a two-channel PR filter bank, where G<sub>0</sub>(z) and G<sub>1</sub>(z) form an analysis filter bank, and H<sub>0</sub>(z) and H<sub>1</sub>(z) form a synthesis filter bank.

Traditionally, G<sub>0</sub>(z) and
 H<sub>0</sub>(z) are lowpass filters, and
 G<sub>1</sub>(z) and
 H<sub>1</sub>(z) are highpass filters. The
 subscripts 0 and 1 represent lowpass and highpass
 filters, respectively. The operation ↓2 denotes a decimation of the signal by a factor
 of two. Applying decimation factors to the signal ensures that the number of output
 samples of the two lowpass filters equal the number of original input samples
 X(z). Therefore, no redundant information is
 added during the decomposition. Refer to the LabVIEW Digital Filter Design Toolkit
 documentation for more information about filters.

You can use the two-channel PR filter bank system and consecutively decompose the outputs of
 lowpass filters, as shown in the following figure:

Figure 125.

[IMAGE alt='image' src='GUID-96345623-414E-41F1-A499-E9BCAF519405-a5.gif']

Lowpass filters remove high-frequency fluctuations from the signal and preserve slow trends. The outputs of lowpass filters provide an approximation of the signal. Highpass filters remove the slow trends from the signal and preserve high-frequency fluctuations. The outputs of highpass filters provide detail information about the signal. The outputs of lowpass filters and highpass filters define the approximation coefficients and detail coefficients, respectively. Symbols A and D in the previous figure represent the approximation and detail information, respectively.

wavelet coefficients

Note

The LabVIEW Wavelet Analysis Tools use the subscripts 0 and 1 to describe the decomposition path, where 0 indicates lowpass filtering and 1 indicates highpass filtering. For example, D<sub>2</sub> in the previous figure denotes the output of two cascaded filtering operations—lowpass filtering followed by highpass filtering. Therefore, you can describe this decomposition path with the sequence 01. Similarly, D<sub>L</sub> denotes the output of the filtering operations 000...1 in which the total number of 0 is L–1. The impulse response of 000...1 converges asymptotically to the mother wavelet and the impulse response of 000...0 converges to the scaling function in the wavelet transform.

The DWT is invertible, meaning that you can reconstruct the signal from the DWT coefficients with
 the inverse DWT. The inverse DWT also is implemented with filter banks by cascading the
 synthesis filter banks. The following figure shows the inverse DWT using filter
 banks:

Figure 126.

[IMAGE alt='image' src='GUID-42758AD0-B856-4160-88FD-FBA9A0FEA5D4-a5.gif']

Use the WA Discrete Wavelet Transform VI to compute the DWT of 1D and 2D
 signals. Use the WA Inverse Discrete Wavelet Transform VI to compute
 the inverse DWT of 1D and 2D signals. Use the WA Get Coefficients of Discrete
 Wavelet Transform VI to get DWT coefficients you compute from the
 WA Discrete Wavelet Transform VI and to return the coefficient
 type, such as the approximation coefficients or the detail coefficients, at a specific
 coefficient level. Use the WA Set Coefficients of Discrete Wavelet
 Transform VI to set the coefficients you obtain from the WA Get
 Coefficients of Discrete Wavelet Transform VI.

- [Multiresolution Analysis](multiresolution-analysis.html)
- [2D Signal Processing](2d-signal-processing.html)

Parent topic:

Signal Processing with Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimate-gaussian-chirplets-and-gaussian-pul.html language=enus -->
## TOPIC 00047: Estimate Gaussian Chirplets and Gaussian Pulses

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimate-gaussian-chirplets-and-gaussian-pul.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimate-gaussian-chirplets-and-gaussian-pul.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can consider the elementary functions that the discrete Gabor expansion uses, such as Gaussian-windowed, complex-sinusoid functions or complex, frequency-modulated Gaussian functions, as being a set of time-shifted and frequency-modulated versions of a single prototype function.The following equ

### Estimate Gaussian Chirplets and Gaussian
 Pulses

You can consider the elementary functions that the discrete Gabor expansion uses,
 such as Gaussian-windowed, complex-sinusoid functions or complex,
 frequency-modulated Gaussian functions, as being a set of time-shifted and
 frequency-modulated versions of a single prototype function.

The following equation represents the linear Gaussian chirplet:

h

k

t

=

σ

k

2

π

-

0

.

25

e

x

p

-

t

-

t

k

2

2

σ

k

2

+

j

ω

k

t

-

t

k

+

β

k

2

t

-

t

k

2

where

- (t k , ω k ) is the time-frequency center of the
 chirplet
- σ k is the standard deviation of the Gaussian envelope
- β k is the chirp rate

The following figures show the time waveform and the time-frequency spectrogram of the
 Gaussian chirplet:

Figure 17.

[IMAGE alt='image' src='GUID-994B7953-6CBE-4DE9-8DE7-229C0F2A14B2-a5.gif']

Figure 18.

[IMAGE alt='image' src='GUID-482A4138-3197-4A51-86DC-85C3AFA543E0-a5.gif']

Use the TFA Adaptive Transform VI to select either Gaussian
 chirplet or Gaussian pulse as the
 elementary function to represent a signal. When you choose the Gaussian
 pulse in the elementary functions, this VI forces the chirp rate
 β<sub>k</sub> to 0. The following illustrations show the waveform
 and the time-frequency spectrogram of the linear Gaussian pulse in this
 situation:

Figure 19.

[IMAGE alt='image' src='GUID-6D077506-044D-4D1C-85EA-9C138A5D394F-a5.gif']

Figure 20.

[IMAGE alt='image' src='GUID-E59AF7C5-D8F0-472C-9202-6E2B217BA6AE-a5.gif']

Given a signal, s(t), the adaptive transform computes the
 parameters of each elementary function by using the matching pursuit method
 together with a fast refinement algorithm.

When you specify how many possible terms of Gaussian chirplet or Gaussian pulse exist for the
 signal, the TFA Adaptive Transform VI estimates the
 parameters of the Gaussian chirplets or the Gaussian pulses. The estimated
 Gaussian chirplets or Gaussian pulses can be distributed in the
 time-frequency domain arbitrarily. The time and the frequency centers of the
 Gaussian chirplets or Gaussian pulses are not fixed in a grid. Also, the
 envelopes of the Gaussian chirplets or Gaussian pulses are arbitrary. In
 comparison, the discrete Gabor expansion has a fixed sampling grid and a
 fixed envelope for all the elementary functions.

Parent topic:

Adaptive Transform and Expansion

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimate-models-advanced-signal-processing.html language=enus -->
## TOPIC 00048: Estimate Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimate-models-advanced-signal-processing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimate-models-advanced-signal-processing.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After acquiring and preprocessing the data from a linear time-invariant system, the next step in the system identification process is estimating the model.You can use the System Identification VIs to estimate models by using any of the methods described in the following sections.

### Estimate Models

After acquiring and preprocessing the data from a linear time-invariant system, the next
 step in the system identification process is estimating the model.

You can use the System Identification VIs to estimate models by using any of
 the methods described in the following sections.

- [Nonparametric Model Estimation Methods](nonparametric-model-estimation-methods-advanc.html)
- [Parametric Model Estimation Methods](parametric-model-estimation-methods-advanced.html)
- [Partially Known Model Estimation Methods](partially-known-model-estimation-methods-adva.html)
- [Closed-Loop Systems Model Estimation Methods](closed-loop-systems-model-estimation-methods.html)
- [Recursive Model Estimation Methods](recursive-model-estimation-methods-advanced-s.html)
- [Frequency-Domain Model Estimation Methods](frequency-domain-model-estimation-methods-adv.html)

Parent topic:

System Identification Concepts

Related concepts:

- Acquire Data from a System
- Preprocess Data from a System

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimating-an-arx-model-advanced-signal-proce.html language=enus -->
## TOPIC 00049: Estimating an ARX Model

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimating-an-arx-model-advanced-signal-proce.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimating-an-arx-model-advanced-signal-proce.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: With model estimation, selecting the correct model and order of the model is challenging. The System Identification VIs support Final Prediction Error (FPE) Criterion, Akaike's Information Criterion (AIC), and Minimum Description Length (MDL) Criterion to aid in the process.Sometimes the results you

### Estimating an ARX Model

With model estimation, selecting the correct model and order of the model is challenging.
 The System Identification VIs support Final Prediction Error (FPE)
 Criterion, Akaike's Information Criterion (AIC), and Minimum Description Length (MDL)
 Criterion to aid in the process.

Sometimes the results you obtain with these three criteria might be inconsistent. You can use a
 pole-zero plot for further investigation and to verify the results of the order
 estimation.

The following figure shows a prediction error plot generated by the SI Estimate Orders
 of System Model VI for an ARX model. The y-axis is the prediction error
 and the x-axis is the model dimension. The three different color bars on the chart
 represent the FPE, AIC, and MDL criteria.

Figure 212.

[IMAGE alt='image' src='GUID-817BE6F9-AB0E-456A-9740-95A0A8BBF965-a5.gif']

You can use the AIC, MDL, and a user-defined criterion to determine the A and B orders of the ARX model.

#### Akaike's Information
 Criterion

The following block diagram uses the SI Estimate Orders
 of System Model VI for order estimation. To estimate the orders of a
 model, the SI Estimate Orders of System Model VI requires two
 data sets—one for estimation and one for validation. You do not need to acquire two
 data sets from a system, rather, you can partition one data set into two using the
 SI Split Signals VI. The SI Split Signals
 VI divides the preprocessed data samples into a portion for model estimation and a
 portion for model validation.

In the following figure, the 1st
 portion (%) is 66, which means the SI Estimate Orders of
 System Model VI will use 66% of the data samples for estimation and
 the remainder of the data samples for validation.

Figure 213.

[IMAGE alt='image' src='GUID-EEB5DE49-337D-4BC5-A128-E51786552A06-a5.gif']

The SI Estimate Orders of System Model VI generates the
 prediction error plot for the ARX model and the optimal A
 order and B order based on the AIC criterion. By using the AIC criterion, the lowest
 prediction error corresponds to a model dimension of 19, as shown in the
 prediction error plot. For an ARX model, the model
 dimension is equal to the sum of the A order, B order, and delay values. The
 SI Estimate Orders of System Model VI returns the following
 optimal orders:

- A order = 9
- B order = 10
- delay = 0

#### Verifying the Results

After determining the orders of the model, you want to verify the results to ensure
 the model accurately describes the system. One method is to plot a pole-zero map and
 visually inspect the plot to determine whether there is any redundancy in the data.
 If a pole and a zero overlap, the pole and zero cancel out each other, which
 indicates the estimated optimal order is too high.

The pole-zero plot graph in the following figure shows a
 pole-zero plot with three overlapping pole-zero pairs. Due to numerical error, it is
 unlikely that a zero and a pole perfectly overlap. You can use the confidence region
 to justify whether the pole and the zero cancel out each other.

Figure 214.

[IMAGE alt='image' src='GUID-6D3CE88E-ABD3-448F-B90F-4A57407ED266-a5.gif']

Because there are three pole-zero pairs, you can conclude that the AIC criterion does
 not produce the most optimal orders.

#### Minimum Description Length
 Criterion

Because the AIC criterion produced a model with non-optimal
 orders, you can try estimating the model orders with the MDL criterion. By using the
 MDL criterion, the lowest prediction error corresponds to a model dimension of 12,
 as shown in the prediction error plot. The SI
 Estimate Orders of System Model VI returns the following optimal
 orders:

- A order = 6
- B order = 6
- delay = 0

The following figure shows a pole-zero plot of a model with a model dimension
 of 12:

Figure 215.

[IMAGE alt='image' src='GUID-DB2BE5ED-4615-49BB-83E4-C387A735A47A-a5.gif']

Compare the previous figure, which uses the MDL criterion, and the figure that
 uses the AIC criterion. Because there are no overlapping pole-zero pairs in the
 previous figure, you can conclude that the MDL criterion fits better than the AIC
 criterion in this particular example.

In addition to examining redundancy, you
 also can use the pole-zero plot for other purposes. For example, both the previous
 two figures show poles outside the unit circle. Having poles outside the unit circle
 implies that this model is not optimal because the ARX system based on the AIC or
 MDL criteria is unstable. One way to stabilize the system is to change the
 order.

In addition to the FPE, AIC, and MDL criteria, you can set user-defined
 orders in the SI Estimate Orders of System Model
 VI.

#### User-Defined Criterion

If you know nothing about the system, you might have to rely on trial and error to determine the optimal orders of the model. However, if you have some knowledge about a system, you can customize the estimation to find a model that fits a certain model dimension. For this model, assume you know that the system is stable; therefore, no poles exist outside the unit circle. Because both the AIC and MDL criterion did not produce stable models, the model orders do not describe the system accurately.

On the following block diagram, you can customize the method parameter. Instead of AIC or MDL, you can select <Other> and enter the desired model dimension in the text box. Assume you know that the model dimension is nine.

Figure 216.

[IMAGE alt='image' src='GUID-9A0ACAB2-45B1-469A-B246-0EC45D1C2918-a5.gif']

The following figure shows the corresponding pole-zero
plot graph with a model dimension of nine, which corresponds to the following optimal orders:

- A order = 4
- B order = 5
- delay = 0

Figure 217.

[IMAGE alt='image' src='GUID-57C42E79-ED2B-4588-B99F-CB5CFFFFEC36-a5.gif']

Compare the pole-zero plot in the previous figure with the previous two figures which uses the MDL criterion and the AIC criterion. The figure which uses the user-defined criterion has no overlapping pole-zero pairs and all the poles are within the unit circle. By visually inspecting the pole-zero plot, you can see that this model is stable and not redundant. Using these model orders, you now can estimate and verify the system model.

Parent topic:

Flexible Arm Case Study

Related concepts:

- ARX Model Definitions
- Determining Parameters for the Prediction Error Method
- Analyze Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimating-and-validating-a-state-space-model.html language=enus -->
## TOPIC 00050: Estimating and Validating a State-Space Model

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimating-and-validating-a-state-space-model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimating-and-validating-a-state-space-model.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For a state-space model, order estimation is equivalent to estimating the number of significant singular values, which correspond to the number of states in the model. After identifying a state-space model that represents the system, you can use the same validation and verification technique used in

### Estimating and Validating a State-Space
 Model

For a state-space model, order estimation is equivalent to estimating the number of
 significant singular values, which correspond to the number of states in the model.
 After identifying a state-space model that represents the system, you can use the same
 validation and verification technique used in the *Simulation and Predictio*n
 section and the *Residual Analysis* section.

The examples in this topic use the same flexible robotic arm data and the same preprocessing techniques.

#### Finding the Singular
 Values

The following block diagram shows how to use the SI
 Estimate Orders of System Model VI to find the optimal order and the
 number of significant singular values:

Figure 223.

[IMAGE alt='image' src='GUID-CFBEC28D-C68E-4269-AF5E-1D1C767D523A-a5.gif']

The Singular Values graph in the following figure shows a
 singular value plot with four leading singular values:

Figure 224.

[IMAGE alt='image' src='GUID-719B29BD-4BF0-4137-88C5-F8543B77A2F7-a5.gif']

By looking both at the Singular Values graph and the
 optimal order, you can see that there are four states in
 this state-space model.

#### Validating the Estimated State-Space
 Model

You can validate the state-space model in the same way that you
 validated the ARX model. You use the SI Model Simulation VI and
 the SI Model Prediction VI to determine the accuracy of the
 state-space model.

The following figure shows the complete process, from
 estimating the state-space model to simulating and predicting the response of the
 model:

Figure 225.

[IMAGE alt='image' src='GUID-35AE23DB-64E8-43F7-A57A-DAAD9C28468F-a5.gif']

The simulation and 1-step ahead
 prediction graphs in the following figure show simulation and
 prediction plots for a state-space model:

Figure 226.

[IMAGE alt='image' src='GUID-AB465085-BACB-4FC2-9DEC-2C4311108DCC-a5.gif']

Parent topic:

Flexible Arm Case Study

Related concepts:

- State-Space Model Definitions
- Validate Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimating-the-complex-cepstrum-of-a-time-ser.html language=enus -->
## TOPIC 00051: Estimating the Complex Cepstrum of a Time Series

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimating-the-complex-cepstrum-of-a-time-ser.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimating-the-complex-cepstrum-of-a-time-ser.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Unlike the real cepstrum, the complex cepstrum of a time series preserves the phase information of the original time series. Therefore, you can reconstruct the original time series from the power cepstrum.The complex cepstrum is useful in noise reduction, signal separation, and cepstral filtering.Us

### Estimating the Complex Cepstrum of a Time Series

Unlike the real cepstrum, the complex cepstrum of a time series preserves the phase
 information of the original time series. Therefore, you can reconstruct the original
 time series from the power cepstrum.

The complex cepstrum is useful in noise reduction, signal separation, and cepstral filtering.

Use the TSA Complex Cepstrum VI to compute the complex cepstrum of a time
 series. Use the TSA Inverse Complex Cepstrum VI to reconstruct a time
 series from the complex cepstrum.

The following figure shows an example of removing echoes from a time series by processing the
 complex cepstrum. In this example, the original signal consists of three signal
 components: a decaying sinusoid starting at time 0, added with two distinct echoes of
 that signal later in time, as shown in the Signal with Echoes
 graph:

Figure 97.

[IMAGE alt='image' src='GUID-095BE04A-8F52-4977-BBAF-EB99F71AE672-a5.gif']

As the previous figure shows, you can remove echoes from a time series using the following steps:

- Compute the complex cepstrum of the original time series using the TSA Complex
 Cepstrum VI. The peaks appearing in the Complex
 Cepstrum graph indicate the echo locations.
- Remove the peaks corresponding to the echoes from the complex cepstrum by setting the peak values to zero. The Peak-Removed Complex Cepstrum graph shows that the peaks have been removed.
- Reconstruct the original time series from the modified complex cepstrum using the TSA
 Inverse Complex Cepstrum VI. In the Reconstructed
 Signal graph, you can see that the reconstructed time series does
 not contain echoes.

Parent topic:

Cepstrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimating-the-frequency-response-function-ad.html language=enus -->
## TOPIC 00052: Estimating the Frequency Response Function

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimating-the-frequency-response-function-ad.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimating-the-frequency-response-function-ad.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Frequency Response Function (FRF) represents the frequency-domain relationship between the inputs and outputs of a dynamic system.The FRF contains the magnitude, phase, and frequency information of the dynamic system data. You estimate the FRF when you have time-domain data, but you want to iden

### Estimating the Frequency Response
 Function

The Frequency Response Function (FRF) represents the frequency-domain
 relationship between the inputs and outputs of a dynamic system.

The FRF contains the magnitude, phase, and frequency information of the dynamic system data. You
 estimate the FRF when you have time-domain data, but you want to identify a
 system model in the frequency domain. If you acquire frequency-domain data,
 this data already contains the FRF.

When you estimate the FRF, the following factors can affect the FRF negatively:

- Noise
- Spectral leakage
- Nonlinear distortion

Use the SI Estimate FRF VI to estimate the FRF and to minimize the effects of
 these factors. This VI supports windowing, which helps to minimize spectral
 leakage. This VI also supports averaging, which helps to minimize noise and
 nonlinear distortion.

#### Minimizing Spectral
 Leakage

To minimize the effects of spectral leakage, you
 can apply a window to the time-domain data. The SI Estimate
 FRF VI supports several types of windows for
 different types of signals. The type of window you choose depends on
 the characteristics of the signal. For example, use a Hanning window
 for random excitation signals. For impact excitation signals, use an
 Exponential window.

#### Minimizing Noise and
 Nonlinear Distortion

You can average multiple FRF
 measurements to minimize the effects of nonlinear distortion and
 reduce the effects of noise in the data measurements. Averaging the
 data smooths the frequency response by reducing fluctuations that
 exist in the data.

The SI Estimate FRF VI
 supports both RMS averaging and vector averaging to average dynamic
 system data.

Note

SI Estimate FRF

Parent topic:

Frequency-Domain Model Estimation Methods

Related concepts:

- Acquire Data from a System

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimating-the-power-cepstrum-of-a-time-serie.html language=enus -->
## TOPIC 00053: Estimating the Power Cepstrum of a Time Series

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimating-the-power-cepstrum-of-a-time-serie.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimating-the-power-cepstrum-of-a-time-serie.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The power cepstrum is an efficient tool for finding different harmonic families in the Power Spectral Density (PSD) of a time series.A power cepstrum is the inverse FFT transform of the natural logarithm of the PSD. You can compute the power cepstrum of a time series as follows:C(τ) = FFT^–1(log(PSD

### Estimating the Power Cepstrum of a Time Series

The power cepstrum is an efficient tool for finding different harmonic families in the
 Power Spectral Density (PSD) of a time series.

A power cepstrum is the inverse FFT transform of the natural logarithm of the PSD. You can
 compute the power cepstrum of a time series as follows:

C(τ) = FFT<sup>–1</sup>(log(PSD))

The power cepstrum C(τ) is a real-valued time series.

The following figure shows the PSD and power cepstrum of a gearbox vibration signal,
 respectively:

Figure 98.

[IMAGE alt='image' src='GUID-6266A3B1-0E89-494A-A1B9-CE14CA481CB0-a5.gif']

The PSD graph suggests that the signal contains both periodic and
 non-periodic components. In the Power Cepstrum graph, you can see
 that the power cepstrum gives a more clear indication of harmonic peak families than the
 PSD.

You can modify, or lifter, the power cepstrum and then transform it back to the PSD. The word
 lifter is an anagram of the word filter,
 formed by reversing the first three letters. By liftering the unnecessary harmonic peak
 families, you can remove an individual peak family from the PSD. The following figure
 shows the PSD of the gearbox vibration signal after you lifter all the harmonic peak
 families. Notice that the harmonic peaks in the liftered PSD have disappeared.

Figure 99.

[IMAGE alt='image' src='GUID-96D2D6F9-96CF-461C-8BEF-B675BEADCDEC-a5.gif']

To lifter the harmonic families, complete the following steps:

1. Compute the power cepstrum of the vibration signal from the PSD.
2. Remove harmonic peaks of individual harmonic family that you want to discard from the power cepstrum.
3. Reconstruct the PSD from the liftered power cepstrum.

If a PSD contains several harmonic families, use the TSA Lifter PSDVI to
 separate harmonic peaks in the PSD by computing the power cepstrum and filtering the
 unnecessary harmonic peaks in the cepstrum.

Parent topic:

Cepstrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimating-the-real-cepstrum-of-a-time-series.html language=enus -->
## TOPIC 00054: Estimating the Real Cepstrum of a Time Series

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimating-the-real-cepstrum-of-a-time-series.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimating-the-real-cepstrum-of-a-time-series.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The real cepstrum is derived from the magnitude spectrum of a time series. You cannot reconstruct the original time series from the real cepstrum because the real cepstrum does not preserve the phase information of the original time series.The real cepstrum is useful for feature extraction from homo

### Estimating the Real Cepstrum of a Time Series

The real cepstrum is derived from the magnitude spectrum of a time series. You cannot
 reconstruct the original time series from the real cepstrum because the real cepstrum
 does not preserve the phase information of the original time series.

The real cepstrum is useful for feature extraction from homomorphic time series, such as the
 following applications:

- Speech analysis; specifically in formant and voice pitch tracking
- Machine fault diagnosis; specifically in gearbox and turbine fault detection

Use the TSA Real Cepstrum VI to compute the real cepstrum of a time series. As
 with power spectrum estimation, you can estimate the real cepstrum using the Fast
 Fourier Transform (FFT) or the AR model of the time series.

Parent topic:

Cepstrum Estimation Methods

Related concepts:

- Power Spectrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=estimating-the-time-cepstrum-of-a-time-series.html language=enus -->
## TOPIC 00055: Estimating the Time-Cepstrum of a Time Series

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `estimating-the-time-cepstrum-of-a-time-series.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/estimating-the-time-cepstrum-of-a-time-series.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the periodic components of a time series vary over time, you cannot use traditional cepstrum estimation methods to identify echoes and periodic components of that time series, however, you can identify time-varying periodic components of a time series by observing the time-cepstrum of the time se

### Estimating the Time-Cepstrum of a Time Series

If the periodic components of a time series vary over time, you cannot use traditional
 cepstrum estimation methods to identify echoes and periodic components of that time
 series, however, you can identify time-varying periodic components of a time series by
 observing the time-cepstrum of the time series.

A time-cepstrum is a function of time and quefrency that indicates how the cepstral content of a
 signal evolves over time. A time-cepstrum uses a sliding window to estimate each real
 cepstrum of a signal. Sliding windows, also called window functions, are functions in
 which the amplitude tapers gradually and smoothly toward zero at the edges. The
 time-cepstrum first partitions the time-domain input signal into several disjointed or
 overlapped blocks by multiplying the signal with a window function. Then, the
 time-cepstrum applies the real cepstrum to each block. Because each block occupies
 different time periods, the resulting time-cepstrum indicates the cepstral content of
 the signal at each corresponding time period.

You can observe the cepstral changes of a nonstationary bearing vibration signal in the
 Cepstrogram graph in the following figure:

Figure 100.

[IMAGE alt='image' src='GUID-5241811D-34D3-4E20-AEFF-F32BA3E7DA5B-a5.gif']

You can display the Cepstrogram on an intensity graph and observe how the
 cepstral content of the signal evolves over time. The intensity legend represents the
 time-cepstrum values in decibels. In the previous figure, the peaks in the time-cepstrum
 appear as intersecting lines. These peaks do not appear in a real cepstrum, because the
 periodic components vary over the length of the signal in the time domain.

Use the TSA Time-Cepstrum VI to compute the time-cepstrum of a time series. As
 with the real cepstrum estimation method, you can estimate the time-cepstrum by using
 the Fast Fourier Transform (FFT) or the AR model of the time series. Use the
 TSA Configure Cepstrogram Indicator VI to display the
 time-cepstrum of a time series on an intensity graph.

Parent topic:

Cepstrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=example-designing-the-fbi-wavelet.html language=enus -->
## TOPIC 00056: Example: Designing the FBI Wavelet

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `example-designing-the-fbi-wavelet.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/example-designing-the-fbi-wavelet.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can complete the following steps to design the FBI wavelet, which is linear phase and near-orthogonal.Different signal processing applications require different properties of wavelets. For image compression, you need a wavelet that is smooth, linear phase, and orthogonal. However, you cannot ach

### Example: Designing the FBI Wavelet

You can complete the following steps to design the FBI wavelet, which is linear phase and
 near-orthogonal.

Different signal processing applications require different properties of wavelets. For image
 compression, you need a wavelet that is smooth, linear phase, and orthogonal. However,
 you cannot achieve all those properties simultaneously. One thing you can do is to
 ensure smoothness (higher order) and linear phase first and then pursue
 near-orthogonality.

Using the Wavelet Design Express VI, you can design a wavelet with specific
 properties.

1. Add the Wavelet Design Express VI on the block diagram. The
 Configure Wavelet Design dialog box automatically
 launches.
2. Select Biorthogonal as the Wavelet Type because only biorthogonal wavelets have the linear-phase property.
3. In the Product of lowpass (G0*H0) section, select
 Maxflat as the P0 type and set the
 value of Zero pairs at π (P0) to
 4 . When you set parameters on the left-hand side of the
 configuration dialog box, plots of the designed wavelet and the associated filter
 banks interactively appear on the right-hand side.
4. In the Factorization (Type of G0) section, select Linear
 Phase as the Filter type and set the value of
 Zeros at π (G0) to
 4 because the wavelet must be near-orthogonal, meaning
 that G 0 ( z ) and
 H 0 ( z ) have the same or almost
 the same amount of zeros. By setting the value of Zeros at π
 (G0) to 4 , you can ensure that both
 G 0 ( z ) and
 H 0 ( z ) have the same amount of
 zeros at π. The following figure shows the zeros of
 G 0 ( z ) and
 H 0 ( z ): Figure 147.Zeros in
 H<sub>0</sub>(z) and G<sub>0</sub>(z)
 
 [IMAGE alt='image' src='GUID-1854DED8-2CD3-40DA-B9B4-6E5FE72CD061-a5.gif'] In the previous figure, notice that besides the four zeros assigned to
 H 0 ( z ) at π, the
 Zeros of G0 and H0 graph also contains six more zeros
 that belong to H 0 ( z ). Note that two
 zeros are on the negative half plane and do not appear on this graph.
5. To make the number of zeros of G 0 ( z ) close to that of H 0 ( z ), click either of the two zeros (o) of H 0 ( z ) near the bottom of the Zeros of G0 and H0 graph and switch the two zeros to those of G 0 ( z ). G 0 ( z ) now has six zeros and H 0 ( z ) has eight zeros. 
 The following figure shows the design result. Notice that the analysis and synthesis scaling functions are similar, and the analysis and synthesis wavelets also are similar, which means the designed wavelet is near-orthogonal. The symmetry of the filter banks also preserves the linear-phase property.
 Figure 148.Adjusting Zero Count in G0(z) and H0(z)
 Design[IMAGE alt='image' src='GUID-75722173-09A6-4A7C-86AD-4F79F6DC977D-a5.gif']

Because of the near-orthogonality and linear-phase properties of the FBI wavelet, you can apply
 this wavelet to many kinds of signal and image processing, for example, image
 compression in JPEG2000. The FBI wavelet is called bior4_4 because both the analysis and
 synthesis lowpass filters G<sub>0</sub>(z) and
 H<sub>0</sub>(z) have four zeros at π. This
 wavelet also is known as CDF 9, 7 because the lengths of the analysis and synthesis
 highpass filters are nine and seven, respectively.

Parent topic:

Interactively Designing Discrete Wavelets

Related concepts:

- Wavelet Signal Processing Application Areas

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=exponential-smoothing-prediction.html language=enus -->
## TOPIC 00057: Exponential Smoothing Prediction

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `exponential-smoothing-prediction.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/exponential-smoothing-prediction.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can make predictions based on exponential smoothing for univariate time series.Exponential smoothing prediction builds an exponential smoothing model for a time series and then predicts the future values of the time series based on the model. Exponential smoothing prediction is suitable for a ti

### Exponential Smoothing Prediction

You can make predictions based on exponential smoothing for univariate time
 series.

Exponential smoothing prediction builds an exponential smoothing model for a time series and then
 predicts the future values of the time series based on the model.
 Exponential smoothing prediction is suitable for a time series that contains
 trends and seasonal variations.

Use the TSA Exponential Prediction VI to predict the future values of
 univariate or multivariate time series based on exponential smoothing.

The following figure shows an example of performing exponential smoothing prediction on a
 simulated sales record:

Figure 85.

[IMAGE alt='image' src='GUID-9AED527A-F430-4F47-BDDC-1CE287835F9B-a5.gif']

The Sales Record graph contains a univariate time series of a sales record
 for a certain product. This example splits the time series into two
 parts—one part for modeling and the other part for comparison—and specifies
 the following settings for prediction:

- Sets Exponential Type to Triple because the sales record contains a systematic trend and seasonality.
- Sets Season Type to Multiplicative because the amplitude of the sales record increases over time.
- Sets Season Period to 4 because the sales record contains four points in each oscillation period.

The Prediction Result graph in the previous figure shows the
 Predicted Record plot matches the Real
 Record plot.

Parent topic:

Predict Time Series Values

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=extend-signals.html language=enus -->
## TOPIC 00058: Extend Signals

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `extend-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/extend-signals.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal extension methods pad the borders of a signal to lessen discontinuity that might exist at the beginning and end of the signal.This topic contains information that applies to the LabVIEW Time Frequency Analysis Tools and the LabVIEW Wavelet Analysis Tools.The Time Frequency Analysis Tools and

### Extend Signals

Signal extension methods pad the borders of a signal to lessen discontinuity that
 might exist at the beginning and end of the signal.

Note

The Time Frequency Analysis Tools and Wavelet Analysis Tools provide the following three
 extension methods:

Zero

Symmetric

Periodic

The following figure shows a linear chirp signal and the extended versions of this signal with
 the zero, symmetric, and periodic padding methods.

Figure 1.

[IMAGE alt='image' src='GUID-9E4B0EF4-BDB1-4A5C-8E94-DA5E6B4DAD94-a5.gif']

In the previous figure, the linear chirp signal appears from 100 s to 355 s. Notice the appearance of the extended signal when different extension methods pad the signal before 100 s and after 355 s.

Parent topic:

Fundamentals

Related concepts:

- Overview of LabVIEW Time Frequency Analysis Tools
- Overview of LabVIEW Wavelet Analysis Tools

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=filtered-gaussian-white-noise-advanced-signal.html language=enus -->
## TOPIC 00059: Filtered Gaussian White Noise

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `filtered-gaussian-white-noise-advanced-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/filtered-gaussian-white-noise-advanced-signal.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Filtered Gaussian white noise is a simple signal that can generate virtually any signal spectra in conjunction with the proper linear filtering.The theoretical crest factor C[f] for a Gaussian is infinite, but clipping the Gaussian amplitude to the input signal limit reduces the crest factor. Clippi

### Filtered Gaussian White Noise

Filtered Gaussian white noise is a simple signal that can generate virtually any
 signal spectra in conjunction with the proper linear filtering.

The theoretical crest factor C<sub>f</sub> for a Gaussian is infinite, but
 clipping the Gaussian amplitude to the input signal limit reduces the crest
 factor. Clipping the Gaussian amplitude minimally affects the generated
 spectrum. You can use the Gaussian White Noise VI to
 generate Gaussian white noise. You then can use the
 Filters VIs to generate Filtered Gaussian white
 noise from Gaussian white noise.

The following figure shows an example of Filtered Gaussian white noise:

Figure 170.

[IMAGE alt='image' src='GUID-315FCDFB-440D-4769-B192-6C4D34844184-a5.gif']

Parent topic:

Choose a Stimulus Signal

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=filtering-and-downsampling-advanced-signal-pr.html language=enus -->
## TOPIC 00060: Filtering and Downsampling

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `filtering-and-downsampling-advanced-signal-pr.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/filtering-and-downsampling-advanced-signal-pr.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You might be interested in only a specific frequency range of the frequency response for a model, in this case, you can filter and enhance the data in the frequency range to improve the fit in the regions of interest.If the sampling frequency is much higher than the bandwidth of the system, the samp

### Filtering and Downsampling

You might be interested in only a specific frequency range of the frequency response for
 a model, in this case, you can filter and enhance the data in the frequency range to
 improve the fit in the regions of interest.

If the sampling frequency is much higher than the bandwidth of the system, the sampling frequency
 might substantially increase the computation burden for complicated identification
 algorithms. You can decrease the sampling frequency by taking every n<sup>th</sup> sample to construct a new downsampled data set. Applying an anti-alias
 filter on the data before downsampling prevents corruption of the downsampled data
 set.

You can use the SI Lowpass Filter VI or the SI Bandpass
 Filter VI to apply a lowpass or bandpass filter, respectively, to the data
 from the system. You then can use the SI Down Sampling VI to reduce
 the number of samples in the data set.

After preprocessing the data you acquired from a dynamic system, the result is a data set that
 you can use to estimate a model that reflects the system dynamics.

Parent topic:

Preprocess Data from a System

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=flexible-arm-case-study-advanced-signal-proce.html language=enus -->
## TOPIC 00061: Flexible Arm Case Study

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `flexible-arm-case-study-advanced-signal-proce.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/flexible-arm-case-study-advanced-signal-proce.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This case study guides you through the system identification process by using the sample data in the SI Data Samples VI.The SI Data Samples VI includes data sets for a DC motor, a flexible robot arm, a ball and beam apparatus, an RC circuit, and so on. This case study uses the flexible arm data to d

### Flexible Arm Case Study

This case study guides you through the system identification process by using the sample
 data in the SI Data Samples VI.

The SI Data Samples VI includes data sets for a DC motor, a flexible robot
 arm, a ball and beam apparatus, an RC circuit, and so on. This case study uses the
 flexible arm data to demonstrate the system identification process and to compare
 different estimation methods.

The flexible arm is a nonlinear dynamic system. The System Identification VIs
 enable you to build models for linear systems. This case study guides you through
 obtaining a linear representation of a nonlinear system.

- [Preprocessing the Data](preprocessing-the-data-advanced-signal-proces.html)
- [Estimating an ARX Model](estimating-an-arx-model-advanced-signal-proce.html)
- [Validating the ARX Model](validating-the-arx-model-advanced-signal-proc.html)
- [Estimating and Validating a State-Space Model](estimating-and-validating-a-state-space-model.html)

Parent topic:

System Identification Case Studies

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=frequency-domain-model-estimation-case-study.html language=enus -->
## TOPIC 00062: Frequency-Domain Model Estimation Case Study

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `frequency-domain-model-estimation-case-study.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/frequency-domain-model-estimation-case-study.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This case study demonstrates how to use frequency-domain data from a flexible robotic arm to estimate and validate a transfer function model and state-space model of the robotic arm. This case study estimates the models directly from frequency-domain data. If the system you want to estimate contains

### Frequency-Domain Model Estimation Case
 Study

This case study demonstrates how to use frequency-domain data from a flexible robotic arm
 to estimate and validate a transfer function model and state-space model of the robotic
 arm. This case study estimates the models directly from frequency-domain data.

Note

SI Estimate
 FRF

In this case study, the input is voltage and the outputs are strain and position. Strain is
 proportional to the acceleration of the flexible arm. Position is the radial position of
 the arm.

Because this system contains one input and two outputs, two Single-Input Single-Output (SISO)
 FRFs or one Multiple-Input Multiple-Output (MIMO) FRF define this system. One FRF
 defines the relationship between the voltage input and the strain output. The other FRF
 defines the relationship between the voltage input and the position output. Each FRF
 contains information about the magnitude and phase of the frequency response and the
 scale of the frequency data. This information is specific to each input-output pair. To
 measure the FRFs in this case study, sine waves at different frequencies excite the
 flexible arm. This data set has a sampling time of 0.02 seconds, which is equivalent to
 a sampling rate of 50 Hz.

#### Estimating and Validating a Transfer
 Function Model

Use the SI Estimate Transfer Function Model from
 FRF VI to estimate a transfer function model from a SISO FRF. Because
 this case study involves one input and two outputs, this VI must estimate and
 validate each SISO transfer function model separately. The following figure shows
 the block diagram for estimating a transfer function model and validating the
 resulting transfer function model against the original FRF data. This block diagram
 uses the FRF describing the relationship between the voltage input and the position
 output to estimate the transfer function model.

Figure 227.

[IMAGE alt='image' src='GUID-87214A0A-ECAA-47BF-83C9-6B1A1B5348A0-a5.gif']

The FRF magnitude and the FRF phase
 inputs of the SI Estimate Transfer Function Model from FRF VI
 require that the data input is in polar form.

Note

FRF magnitude

FRF
 phase

SI Estimate Transfer Function Model
 from FRF

In this case study, the FRF
 magnitude and the FRF phase inputs contain
 data in polar form. Therefore, the FRF magnitude and the
 FRF phase inputs wire directly into the SI
 Estimate Transfer Function Model from FRF VI.

Note

FRF
 format

FRF format

Because
 a transfer function model is a type of parametric model representation, you must
 specify the model parameters before estimating the model. For a transfer function
 model, you must specify the orders of the numerator and denominator polynomial
 functions. If you do not have prior knowledge about the system, you must use trial
 and error to determine the optimal orders of the model.

One way to identify
 the optimal orders is to observe the peaks in the magnitude response of the original
 FRF. The optimal order is at least twice the number of peaks. You can plot and
 observe the magnitude by using the SI Bode Plot VI. You can
 increase the accuracy of the model by modifying the initial guess after analyzing
 the model. In the previous block diagram, 2 is the initial guess for both the
 numerator order and the denominator order.

You can validate the resulting
 model by comparing the original FRF and the FRF that the model generates. Compare
 the two FRFs on an XY graph by using the SI Bode Plot VI. By
 default, the SI Bode Plot VI unwraps the phase information and
 converts the units of the resulting phase to degrees. To compare the original FRF
 and the FRF that the SI Bode Plot VI displays more accurately,
 use the Unwrap Phase VI to unwrap the phase in the original FRF.
 This case study also uses the Mathematics VIs to convert the
 original FRF from radians to degrees.

Figure 228.

[IMAGE alt='image' src='GUID-62AD0360-07C7-48E8-B881-92D6932ABDE6-a5.gif']

Visually inspect the alignment of the Model-generated FRF
 and the Original FRF to determine whether the estimated
 transfer function model accurately describes the dynamic system. Notice that the
 Original FRF and the Model-generated
 FRF do not align. Therefore, 2 is not the most appropriate order
 value for the transfer function model.

Orders of TF

Figure 229.

[IMAGE alt='image' src='GUID-0CAAA902-5CF8-4933-9968-CDFC9D0C9BF2-a5.gif']

In this case study, setting the value of the Orders of TF
 to 6 provides a closer alignment of the Model-generated
 FRF and the Original FRF. Therefore, a
 6th-order transfer function model describes the voltage-position FRF of the dynamic
 system more accurately than a 2nd-order model.

Identify a second transfer
 function model by using the FRF of the voltage input and strain output. You must
 apply the same method when optimizing the model order.

#### Estimating and Validating a
 State-Space Model

In this case study, a single MIMO FRF also can represent
 the frequency-domain relationship of the input and outputs of the flexible arm
 system. You can use this MIMO FRF to estimate state-space models of a dynamic
 system. The SI Estimate State-Space Model from FRF VI estimates a
 state-space model for SISO and MIMO systems. This VI requires you to specify the
 number of states of the system you want to estimate. This
 value comes from prior knowledge about the system.

You also can provide an
 initial guess if you do not have prior knowledge. A guideline for identifying the
 number of states of a system is the same as the guideline for identifying the orders
 of a transfer function model. The number of states is at least twice the number of
 peaks in the magnitude of the FRF. Because a MIMO FRF is composed of more than one
 SISO FRF, you must observe the magnitude of the SISO FRF with the maximum number of
 peaks.

In this case study, the SISO FRFs that comprise the MIMO FRF both have
 one peak. Therefore, the initial guess at the number of states is 2. By increasing
 the number of states and plotting the model-generated MIMO FRF along with the
 original MIMO FRF on a Bode plot, you can observe that entering eight states
 produces an acceptable estimation for the system.

The following figure shows
 the Bode Plots of the original MIMO FRF and of the MIMO FRF that the state-space
 model generates:

Figure 230.

[IMAGE alt='image' src='GUID-CF639F19-2282-407F-8BC7-DCB22F47A725-a5.gif']

Compare the FRF Position graphs in the previous figure
 with the 6th-order transfer function FRF Position graphs.
 Both model-generated FRFs are close to the original FRF in the FRF
 Position graphs. The proximity of these FRFs indicates that the
 6th-order transfer function model and the state-space model with eight states are
 close approximations for estimating system models in this case study.

Parent topic:

System Identification Case Studies

Related concepts:

- Estimating the Frequency Response Function
- Parametric Model Estimation Methods
- Analyze, Validate, and Convert Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=frequency-domain-model-estimation-methods-adv.html language=enus -->
## TOPIC 00063: Frequency-Domain Model Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `frequency-domain-model-estimation-methods-adv.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/frequency-domain-model-estimation-methods-adv.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frequency-domain model estimation involves identifying a model of a dynamic system by using the frequency-domain representation of the dynamic system data.You acquire frequency-domain data by using a frequency analyzer. If you acquire time-domain data, you also can convert this time-domain data to f

### Frequency-Domain Model Estimation
 Methods

Frequency-domain model estimation involves identifying a model of a dynamic system by
 using the frequency-domain representation of the dynamic system data.

You acquire frequency-domain data by using a frequency analyzer. If you acquire time-domain data,
 you also can convert this time-domain data to frequency-domain data by estimating the
 Frequency Response Function (FRF) of a dynamic system. The FRF represents the
 frequency-domain relationship between the inputs and outputs of a dynamic system.

Use the System Identification VIs to obtain the FRF and estimate two
 categories of parametric models—transfer function and state-space. Use the SI
 Estimate Transfer Function Model from FRF VI to estimate continuous and
 discrete Single-Input Single-Output (SISO) transfer function models. Use the SI
 Estimate State-Space Model from FRF VI to estimate discrete SISO and
 Multiple-Input Multiple-Output (MIMO) state-space models.

#### Advantages of Frequency-Domain System Identification

Compared to time-domain model estimation methods, frequency-domain model estimation methods have the following advantages:

- You can reduce a large number of time-domain data samples to a finite number of frequency-domain data samples.
- You can reduce the effects of noise by averaging the FRF from multiple time-domain data measurements.
- You can focus on frequency bands of interest by directly weighting the frequency-domain data.

Parent topic:

Estimate Models

Related concepts:

- Parametric Model Estimation Methods
- Model Types and Representations

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=frequency-response-advanced-signal-processing.html language=enus -->
## TOPIC 00064: Frequency Response

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `frequency-response-advanced-signal-processing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/frequency-response-advanced-signal-processing.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The frequency response provides the complete frequency-domain characteristics of the system, including the passband and the natural frequency of the system.Theoretically, the results from impulse response estimation and the results from frequency response estimation are equivalent. For example, the

### Frequency Response

The frequency response provides the complete frequency-domain characteristics of the
 system, including the passband and the natural frequency of the system.

Theoretically, the results from impulse response estimation and the results from frequency
 response estimation are equivalent. For example, the Fourier transform of the impulse
 response h(n), which you can compute using impulse
 response estimation, equals the frequency response
 G(e<sup>jω</sup>). However,
 this equivalence does not hold in most real-world applications because of different
 preprocessing schemes in impulse response estimation and frequency response
 estimation.

A sinusoidal input signal has the following general form:

u(t) = sin(ω<sub>0</sub>t)

The response of a linear time-invariant system to a sinusoidal input also is a sinusoidal signal.
 However, the response to the sinusoidal input might have a different magnitude and phase
 than the sinusoidal signal, as shown in the following equation:

y(t) = bsin(ω<sub>0</sub>t + θ)

b

θ

ω

0

G

ω

G

ω

G

ω

SI
 Estimate Frequency Response

Note

SI Estimate FRF

#### Applications of the Frequency
 Response

The frequency response gives the characteristics of the system in the frequency
 domain. You can use the frequency response to obtain useful information before
 applying parametric estimation. For example, you can use the frequency response to
 determine whether you must pre-filter the signals or what the model order of the
 system is. You also can use nonparametric frequency response to verify parametric
 model estimation results by comparing the frequency response of the parametric model
 with the nonparametric frequency response.

One example of a real-world application of the frequency response is with the
 flexible arm, as shown in the following figure. The input of this system is the
 reaction torque of the structure on the ground. This input is a multi-sine wave with
 200 frequency points equally spaced over the frequency band from 0.122 Hz to 24.4
 Hz. The output of this system is the acceleration of the flexible arm. The frequency
 response of this system is not significant outside of the range of interest, which
 is the frequency band of the input signal, or 0.122 Hz to 24.4 Hz. However, notice
 that the magnitude response has a peak around 42 Hz. The peak
 around 42 Hz may be the result of noise, or nonlinearity, or another input source.
 You can use lowpass filtering to remove the 42 Hz peak before applying parametric
 estimation.

Figure 183.

[IMAGE alt='image' src='GUID-5F400AE1-7863-454F-8154-4504A22094B4-a5.gif']

- [Spectral Analysis Method](spectral-analysis-method-advanced-signal-proc.html)
- [Apply a Lag Window](apply-a-lag-window-advanced-signal-process.html)

Parent topic:

Nonparametric Model Estimation Methods

Related concepts:

- Impulse Response
- Estimating the Frequency Response Function
- Parametric Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=fundamentals.html language=enus -->
## TOPIC 00065: Fundamentals

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/fundamentals.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections describe the concepts in the LabVIEW Advanced Signal Processing Toolkit.

### Fundamentals

The following sections describe the concepts in the LabVIEW Advanced Signal
 Processing Toolkit.

- [Categorize Signals](categorize-signals.html)
- [Extend Signals](extend-signals.html)
- [Analytic Signals](analytic-signals.html)
- [Central Time and Central Frequency](central-time-and-central-frequency.html)

Parent topic:

LabVIEW Advanced Signal Processing Toolkit Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=gabor-spectrogram.html language=enus -->
## TOPIC 00066: Gabor Spectrogram

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `gabor-spectrogram.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/gabor-spectrogram.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Gabor spectrogram method to reduce the cross-term interference of the Wigner-Ville Distribution (WVD). This method decomposes a signal with the Gabor expansion and then sums the WVD of each auto-term with some cross-terms.Because you can decompose a signal as a linear combination of

### Gabor Spectrogram

You can use the Gabor spectrogram method to reduce the cross-term interference of
 the Wigner-Ville Distribution (WVD). This method decomposes a signal with
 the Gabor expansion and then sums the WVD of each auto-term with some
 cross-terms.

Because you can decompose a signal as a linear combination of a family of elementary functions,
 you can consider the WVD of a signal to be the summation of the WVD of each
 elementary function, or auto-term, and the cross-terms of each pair of
 elementary functions.

You can use the Gabor spectrogram method to reduce the cross-term interference of the WVD. This
 method decomposes a signal with the Gabor expansion and then sums the WVD of each
 auto-term with some cross-terms. Because the Gabor spectrogram method uses the Gabor
 expansion first and then the WVD, the Gabor spectrogram also is called the Gabor
 expansion-based spectrogram. The Gabor spectrogram also is called the time-frequency
 distribution series. The Gabor spectrogram is a method unique to the LabVIEW Time
 Frequency Analysis Tools.

The Gabor spectrogram has a better time-frequency resolution than the short-time Fourier
 transform (STFT) spectrogram method and less cross-term interference than the WVD
 method. The Gabor spectrogram algorithm includes simple analytic forms, and you can
 implement the Gabor spectrogram with interpolation filters. Therefore, the Gabor
 spectrogram is more efficient than the Choi-Williams Distribution (CWD) and the
 Cone-Shaped Distribution (CSD), especially with large signal lengths. However, the Gabor
 spectrogram usually requires more computation time than the STFT spectrogram or the WVD.

Use TFA Fast Gabor Spectrogram VI to compute the Gabor spectrogram.

#### Selecting an Appropriate Gabor
 Spectrogram Order and Window Length

You need to select the order of the Gabor spectrogram and the window length of the
 Gabor spectrogram properly to balance the time-frequency resolution and the
 cross-term interference. For Gabor spectrograms with a low order, the window length
 affects the time resolution, the frequency resolution, and the cross-term
 interference of the Gabor spectrogram. As in the case of the STFT, a narrow window
 length results in a coarse frequency resolution, a fine time resolution, and severe
 cross-term interference between two auto-terms with the same time center. A wide
 window length results in a fine frequency resolution, a coarse time resolution, and
 severe cross-term interference between two auto-terms with the same frequency
 center. The selection of the window length in the Gabor spectrogram is much less
 sensitive than in the STFT spectrogram. Also, regardless of the window length you
 select, the Gabor spectrogram always converges to the WVD as the order
 increases.

The order of the Gabor spectrogram balances the time-frequency resolution and the
 cross-term interference of the Gabor spectrogram. As the order increases, the
 time-frequency resolution of the Gabor spectrogram improves, but the spectrogram
 includes more cross-term interference and requires a longer computation time. When
 the order is zero, the Gabor spectrogram is non-negative and is similar to the STFT
 spectrogram. As the order increases, the Gabor spectrogram converges to the WVD. For
 most real-world applications, choose an order of two to five to balance the
 time-frequency resolution and cross-term suppression.

The following figure shows the Gabor spectrogram of the example frequency hopper
 signal when the order is 0 and the window length is 128:

Figure 35.

[IMAGE alt='image' src='GUID-88D30577-CFA3-4508-B121-90E0EFC43C3D-a5.gif']

Notice that the signal in the previous figure is similar to the STFT spectrogram in
 the example frequency hopper signal with window length of 128. The Gabor spectrogram
 of the example frequency hopper signal in the previous figure has a coarse
 time-frequency resolution and does not include cross-term interference.

The following figure shows the Gabor spectrogram of the example frequency hopper
 signal when the order is 20 and the window length is 128:

Figure 36.

[IMAGE alt='image' src='GUID-4C02E5E9-72B0-49A1-AB8C-8765A68FE5E1-a5.gif']

1

The signal in the previous figure is similar to the WVD of the example frequency
 hopper signal because the Gabor spectrogram converges to the WVD as the order
 increases. The Gabor spectrogram of the example frequency hopper signal in the
 previous figure has a fine time-frequency resolution and includes cross-term
 interference.

The following figure shows the Gabor spectrogram of the example frequency hopper
 signal when the order is 3 and the window length is 128:

Figure 37.

[IMAGE alt='image' src='GUID-1295C229-2EAA-48AF-B9F5-2EE7F36B6D64-a5.gif']

The signal in the previous figure has a higher time-frequency resolution than the
 STFT spectrogram and less cross-term interference than the WVD.

The following figure shows a signal with three Gaussian components. The composite
 Gaussian signal can be a useful test signal for testing the time-frequency
 resolution and the cross-term interference of a time-frequency analysis algorithm
 because the composite Gaussian signal has compact signal components that should be
 very narrow on the time-frequency plane.

Figure 38.

[IMAGE alt='image' src='GUID-093A4834-5FCE-4BC4-B45B-78828D648113-a5.gif']

The example signal in the previous figure contains one Gaussian-windowed linear chirp
 signal and two Gaussian-windowed sine wave signals. The linear chirp has the same
 time center as one of the sine waves and the same frequency center as the other sine
 wave, but you cannot see that in the time-domain representation in the previous
 figure.

The following figure shows the Gabor spectrogram of the composite Gaussian signal
 example when the order is 5 and the window length is 32:

Figure 39.

[IMAGE alt='image' src='GUID-00B56223-7A8C-4371-8267-1255896E436E-a5.gif']

1

The following figure shows the Gabor spectrogram of the composite Gaussian signal
 example when the order is 5 and the window length is 256:

Figure 40.

[IMAGE alt='image' src='GUID-E0172D28-0995-48F0-83B4-D263BF3F5037-a5.gif']

1

Notice in the previous two figures that the cross-term interference along the time
 axis increases with the window length and the cross-term interference along the
 frequency axis decreases with the window length.

Parent topic:

Quadratic Time Frequency Analysis Methods

Related concepts:

- Discrete Gabor Transform and Expansion

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=general-linear-model-definitions-advanced-sig.html language=enus -->
## TOPIC 00067: General-Linear Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `general-linear-model-definitions-advanced-sig.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/general-linear-model-definitions-advanced-sig.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generally, you can describe a discrete system by using the general-linear polynomial model. This model provides flexibility for both system dynamics and stochastic dynamics.Use the SI Estimate General Linear Model VI to estimate general-linear polynomial models. The following equation describes this

### General-Linear Model Definitions

Generally, you can describe a discrete system by using the general-linear polynomial
 model. This model provides flexibility for both system dynamics and stochastic
 dynamics.

Use the SI Estimate General Linear Model VI to estimate general-linear
 polynomial models. The following equation describes this model:

y

k

=

z

-

n

G

z

-

1

,

θ

u

k

+

H

z

-

1

,

θ

e

k

where

- u ( k ) is the input of the system
- y ( k ) is the output of the system
- e ( k ) is the disturbance of the system which
 usually is zero-mean white noise
- G ( z –1 , θ) is the transfer function
 of the deterministic part of the system
- H ( z –1 , θ) is the transfer function
 of the stochastic part of the system

The deterministic transfer function specifies the relationship between the output and the input
 signal. The stochastic transfer function specifies how the random disturbance affects
 the output signal. Often the deterministic and stochastic parts of a system are referred
 to as system dynamics and stochastic dynamics, respectively.

The term z<sup>–1</sup> is the backward shift operator, which is defined by the following equations:

z

-

1

x

k

=

x

k

-

1

z

-

2

x

k

=

x

k

-

2

...

z

-

n

x

k

=

x

k

-

n

z<sup>–n</sup> defines the number of delay samples between the input
 and the output.

G(z<sup>–1</sup>, θ)u(k) and
 H(z<sup>–1</sup>, θ)e(k) are rational polynomials as
 defined by the following equations:

G

z

-

1

,

θ

=

B

z

,

θ

A

z

,

θ

F

z

,

θ

H

z

-

1

,

θ

=

C

z

,

θ

A

z

,

θ

D

z

,

θ

The vector θ is the set of model parameters. The following equations do not display θ to make the equations easier to read.

The following equation shows the form of the general-linear model:

A

z

y

k

=

B

z

F

z

u

k

-

n

+

C

z

D

z

e

k

where

- y ( k ) represents the system outputs
- u ( k ) represents the system inputs
- n is the system delay
- e ( k ) is the system disturbance

A(z), B(z),
 C(z),
 D(z), and
 F(z) are polynomial with respect to the
 backward shift operator z<sup>-1</sup> and defined by the following equations:

A

z

=

1

+

a

1

z

-

1

+

.

.

.

+

a

k

a

z

-

k

a

B

z

=

b

0

+

b

1

z

-

1

+

.

.

.

+

b

k

b

z

-

k

b

-

1

C

z

=

1

+

c

1

z

-

1

+

.

.

.

+

c

k

c

z

-

k

c

D

z

=

1

+

d

1

z

-

1

+

.

.

.

+

d

k

d

z

-

k

d

F

z

=

1

+

f

1

z

-

1

+

.

.

.

+

f

k

f

z

-

k

f

The following figure depicts the signal flow of a general-linear model:

Figure 188.

[IMAGE alt='image' src='GUID-21D02722-FB2A-4214-952C-57DECD0CAFF4-a5.gif']

where

- u represents the system inputs
- y represents the system outputs
- e is the system disturbance
- both v and ω are the auxiliary variables

Setting one or more of A(z),
 C(z),
 D(z), and
 F(z) to 1 can create simpler
 models such as autoregressive with exogenous terms (ARX), autoregressive-moving average
 with exogenous terms (ARMAX), output-error, and Box-Jenkins models, which you commonly
 use in real-world applications.

#### SISO

The following are the
 time domain equations for the general-linear SISO model:

w

k

+

f

1

w

k

-

1

+

.

.

.

+

f

k

f

w

k

-

k

f

=

b

0

u

k

-

n

+

b

1

u

k

-

n

-

1

+

.

.

.

+

b

k

b

-

1

u

k

-

n

-

k

b

+

1

v

k

+

d

1

v

k

-

1

+

.

.

.

+

d

k

d

v

k

-

k

d

=

e

k

+

c

1

e

k

-

1

+

.

.

.

+

c

k

c

e

k

-

k

c

y

k

+

a

1

y

k

-

1

+

.

.

.

+

a

k

a

y

k

-

k

a

=

w

k

+

v

k

where

- k f is the F 
 order
- k b is the B 
 order
- k c is the C 
 order
- k d is the D 
 order
- k a is the A 
 order
- u ( k ) represents the system inputs
- n is the system delay
- e ( k ) is the system disturbance
- w is the auxiliary variable

- [AR Model Definitions](ar-model-definitions-advanced-signal-processi.html)
- [ARX Model Definitions](arx-model-definitions-advanced-signal-process.html)
- [ARMAX Model Definitions](armax-model-definitions-advanced-signal-proce.html)
- [Box-Jenkins Model Definitions](box-jenkins-model-definitions-advanced-signal.html)
- [Output-Error Model Definitions](output-error-model-definitions-advanced-signa.html)

Parent topic:

Parametric Model Estimation Methods

Related concepts:

- Model Types and Representations

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=get-started-with-system-identification.html language=enus -->
## TOPIC 00068: Get Started with System Identification

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `get-started-with-system-identification.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/get-started-with-system-identification.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: System identification is a series of processes for building the mathematical models of a dynamic system by using the stimulus and response data of the dynamic system.A Direct Current (DC) servomotor is a typical example of dynamic systems. A DC servomotor generates rotation motion through the magnet

### Get Started with System Identification

System identification is a series of processes for building the mathematical models of a
 dynamic system by using the stimulus and response data of the dynamic system.

A Direct Current (DC) servomotor is a typical example of dynamic systems. A DC servomotor
 generates rotation motion through the magnetic interaction between a current-carrying
 conductor and an external magnetic field.

A DC servomotor is a common actuator in a control system. To estimate the model of a DC
 servomotor, you need to create a model that contains unknown coefficients according to
 the application requirements. For example, if you plan to create a model that you can
 use with a proportional-integral-derivative controller for a DC servomotor, you can
 create the following transfer function model,
 G(s), for the measured rotational speed of the
 shaft, ω, and the driving voltage, U, of the DC
 servomotor:

G

s

=

ω

s

U

s

=

b

0

a

2

s

2

+

a

1

s

+

a

0

Perform system identification on the previous transfer function model to estimate the coefficients, b<sub>0</sub>, a<sub>0</sub>, a<sub>1</sub>, and a<sub>2</sub>, of the transfer function, on the basis of the measured rotational speed, ω, and driving voltage, U.

The following figure shows the processes of identifying a DC servomotor's model:

Figure 152.

[IMAGE alt='image' src='GUID-7C29FA48-6693-4BA1-9BF4-E2F79616FF03-a5.gif']

Read through the following topics to perform system identification on a DC servomotor by using
 the System Identification VIs:

1. Choosing a Proper Dynamic System Model by Using Physical Modeling
2. Exciting the System and Acquiring Data
3. Identifying Dynamic System Models
4. Validating and Analyzing Dynamic System Models
5. Converting Dynamic System Models to Control Design Models

Parent topic:

System Identification Concepts

Related concepts:

- Estimate Models
- Transfer Function Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=identifying-continuous-time-state-space-model.html language=enus -->
## TOPIC 00069: Identifying Continuous-Time State-Space Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `identifying-continuous-time-state-space-model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/identifying-continuous-time-state-space-model.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Advanced Signal Processing Toolkit offers a variety of methods for identifying continuous-time state-space models.After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the following differential equations:Jdωdt+bω=KiiLdidt+Ri=V-KeωSet K[i] to be equal to K

### Identifying Continuous-Time State-Space
 Models

The LabVIEW Advanced Signal Processing Toolkit offers a variety of methods for
 identifying continuous-time state-space models.

After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the
 following differential equations:

J

d

ω

d

t

+

b

ω

=

K

i

i

L

d

i

d

t

+

R

i

=

V

-

K

e

ω

Set K<sub>i</sub> to be equal to
 K<sub>e</sub> to transform these
 differential equations. If you want to design an analog state feedback controller,
 transform these differential equations to the following dynamic system model:

d

d

t

ω

i

=

-

b

J

K

J

-

K

L

-

R

L

ω

i

+

0

1

L

U

ω

=

1

0

ω

i

Transform the dynamic system model to the following continuous-time state-space model:

d

ω

,

i

d

t

=

A

ω

,

i

+

B

U

ω

=

C

ω

,

i

where

- A , B , and C are matrices of
 this continuous-time state-space model
- ω is the rotational speed of the shaft
- U is the driving voltage
- i is the armature current

You must estimate the values of the A, B, and C matrices to identify a state-space model.

#### Using the SI Model Estimation Express
 VI

Complete the following steps to identify the continuous-time
 state-space model by using the SI Model Estimation Express
 VI:

1. Add the SI Model Estimation Express VI to the block diagram
 of the VI you created. The Configure SI Model Estimation 
 dialog box appears.
2. Select the State-Space button in the Select
 Model Type section to identify state-space models. The
 Model Diagram section displays a mathematical
 equation for the selected model type and a diagram of the model.
3. Select the SISO button in the Select System
 Dims section to identify Single-Input Single-Output (SISO)
 dynamic models.
4. Select the Waveform button in the Select Data
 Type section to identify dynamic models by using waveform input
 signals.
5. Enter 2 in the Number of states text box
 because the continuous-time state-space model contains two states: rotational
 speed ω and armature current i .
6. Click the OK button to close the configuration dialog box
 and return to the block diagram.
7. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Model Estimation Express 
 VI.
8. Add the SI Convert Discrete to Continuous Model VI to the
 block diagram.
9. Wire the system model out output of the SI Model
 Estimation Express VI to the system model
 in input of the SI Convert Discrete to Continuous
 Model VI.
10. Add the SI Draw Model VI to the block diagram.
11. Wire the system model out output of the SI
 Convert Discrete to Continuous Model VI to the system
 model input of the SI Draw Model VI.
12. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block diagram: Figure 158.Block Diagram of
 Model Output Indicator for SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-18E1C161-DAFF-4C44-8FFA-4A9AFBB5D1E4-a5.gif']
13. Wire all error in and error out terminals on the block diagram.
14. Run this VI to identify the dynamic system model.

#### Using the SI Estimate State-Space
 Model VI

Complete the following steps to identify the continuous-time
 state-space model by using the SI Estimate State-Space Model
 VI:

1. Add the SI Estimate State-Space Model VI to the block diagram
 of the VI you created.
2. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Estimate State-Space Model 
 VI.
3. Create a control for the structure selector input of the
 SI Estimate State-Space Model VI.
4. Set all the Boolean controls of the structure selector 
 input to FALSE because you need to estimate the
 A , B , and C 
 matrices only.
5. Create a control for the number of states input of the
 SI Estimate State-Space Model VI.
6. Set the number of states input to 2 
 because the continuous-time state-space model contains two states: rotational
 speed ω and armature current i .
7. Switch to the front panel, right-click all controls, and
 select Data Operations»Make Current Value Default from
 the shortcut menu. LabVIEW uses the current values as the default values for
 these controls.
8. Add the SI Convert Discrete to Continuous Model VI to the
 block diagram.
9. Wire the system model out output of the SI
 Estimate State-Space Model VI to the system model
 in input of the SI Convert Discrete to Continuous
 Model VI.
10. Add the SI Draw Model VI to the block diagram.
11. Wire the system model out output of the SI
 Convert Discrete to Continuous Model VI to the system
 model input of the SI Draw Model VI.
12. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block diagram: Figure 159.Block Diagram of
 Model Output Indicator for SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-73923C48-9723-4DDD-9601-AC215EFBA257-a5.gif']
13. Wire all error in and error out terminals on the block diagram.
14. Run this VI to identify the dynamic system model.

#### Verifying Resulting Dynamic System
 Models

If you use the SI Data Samples VI to generate
 the input and output data in *Exciting the System and Acquiring Data*,
 LabVIEW returns the following system model:

d

x

d

t

=

-

15

.

7417

1

.

8577

E

-

11

3

.

20328

E

-

11

-

852

.

222

x

t

+

-

0

.

175335

-

0

.

101903

u

t

+

0

2

.

99129

E

-

10

e

t

y

t

-

0

.

0480361

-

0

.

0142187

x

t

+

e

t

where

- A matrix is -
 15
 .
 7417
 1
 .
 8577
 E
 -
 11
 3
 .
 20328
 E
 -
 11
 -
 852
 .
 222
- B matrix is -
 0
 .
 175335
 -
 0
 .
 101903
- C matrix is -
 0
 .
 0480361
 -
 0
 .
 0142187
- e ( t ) is the system noise

Parent topic:

Identifying Dynamic System Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=identifying-continuous-time-transfer-function.html language=enus -->
## TOPIC 00070: Identifying Continuous-Time Transfer Function Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `identifying-continuous-time-transfer-function.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/identifying-continuous-time-transfer-function.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Advanced Signal Processing Toolkit offers a variety of methods for identifying continuous-time transfer function models.After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the following differential equations: J d ω d t + b ω = K i i L d i d t + R i = V

### Identifying Continuous-Time Transfer Function
 Models

The LabVIEW Advanced Signal Processing Toolkit offers a variety of methods for
 identifying continuous-time transfer function models.

After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the
 following differential equations:

J

d

ω

d

t

+

b

ω

=

K

i

i

L

d

i

d

t

+

R

i

=

V

-

K

e

ω

If you want to design an analog Proportional-Integral-Derivative (PID) controller, perform the
 Laplace transform on these differential equations to obtain the following equations:

J

s

ω

s

+

b

ω

s

=

K

i

l

s

L

s

l

s

=

V

s

-

K

e

ω

s

Set K<sub>i</sub> to be equal to
 K<sub>e</sub> to transform these
 differential equations. You can transform these differential equations to the following
 continuous-time transfer function model:

ω

s

U

s

=

K

J

L

s

2

+

b

L

+

J

R

s

+

b

R

+

k

2

where

- K is the electromotive force constant
- ω is the rotational speed of the shaft
- U is the driving voltage
- J is the moment of inertia of the DC servomotor
- b is the damping ratio of the mechanical part of the DC
 servomotor
- R is the electric resistance
- L is the inductance of circuit

In this example, you need to estimate the values of K,
 JL, (bL+JR), and
 (bR+K<sup>2</sup>) to identify the
 continuous-time transfer function model.

#### Using the SI Transfer Function
 Estimation Express VI

Complete the following steps to identify the
 continuous-time transfer function model by using the SI Transfer Function
 Estimation Express VI:

1. Add the SI Transfer Function Estimation Express VI to the
 block diagram of the VI you created. The Configure SI Transfer
 Function Estimation dialog box appears.
2. Select the Waveform button to identify dynamic models by
 using waveform input signals.
3. Click the Model Settings tab.
4. Select the Continuous button to identify continuous-time
 transfer function models.
5. Enter 0 in the Numerator order text box
 because the numerator of this model is constant only.
6. Enter 2 in the Denominator order text
 box because the highest denominator order of the continuous-time transfer
 function model is s 2 .
7. Click the OK button to close the configuration dialog box
 and return to the block diagram.
8. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Transfer Function Estimation
 Express VI.
9. Add the SI Draw Model VI to the block diagram.
10. Wire the system model out output of the SI
 Transfer Function Estimation Express VI to the system
 model input of the SI Draw Model VI.
11. Create a constant for the display format for TF
 model input of the SI Draw Model VI and set
 the value to Descending .
12. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block diagram: Figure 156.Example Block
 Diagram for the SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-64923799-C0CB-4F65-B892-B8419FBB48AD-a5.gif']
13. Wire all error in and error out terminals on the block diagram.
14. Run this VI to identify the dynamic system model.

#### Using the SI Estimate Transfer
 Function Model VI

Complete the following steps to identify the
 continuous-time transfer function model by using the SI Estimate Transfer
 Function Model VI:

1. Add the SI Estimate Transfer Function Model VI to the block
 diagram of the VI you created.
2. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Estimate Transfer Function
 Model VI.
3. Create a control for the orders of transfer function
 model input of the SI Estimate Transfer Function
 Model VI.
4. Enter 0 in the num order field of this
 control because the numerator of this model is constant only.
5. Enter 2 in the den order field of this
 control because the highest denominator order of this model is
 s 2 .
6. Switch to the front panel, right-click this control, and
 select Data Operations»Make Current Value Default from
 the shortcut menu. LabVIEW uses the current value as the default value for this
 control.
7. Add the SI Draw Model VI to the block diagram.
8. Wire the system model out output of the SI
 Estimate Transfer Function Model VI to the system
 model input of the SI Draw Model VI.
9. Create a constant for the display format for TF
 model input of the SI Draw Model VI and set
 the value to Descending .
10. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block diagram: Figure 157.Example Block
 Diagram for the SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-CD7519E0-9C4B-4E71-8762-F93772B438A9-a5.gif']
11. Wire all error in and error out terminals on the block diagram.
12. Run this VI to identify the dynamic system model.

#### Verifying Resulting Dynamic System
 Models

If you use the SI Data Samples VI to generate
 the input and output data in *Exciting the system and Acquiring Data*,
 LabVIEW returns the following system model:

y

s

=

0

.

000538735

3

.

36344

E

-

8

s

2

+

0

.

0658172

s

+

1

u

s

where

- K =0.000538735
- JL =3.36326E –8
- (bL+JR) =0.0658172
- ( bR+K 2 )=1

Parent topic:

Identifying Dynamic System Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=identifying-discrete-time-state-space-models.html language=enus -->
## TOPIC 00071: Identifying Discrete-Time State-Space Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `identifying-discrete-time-state-space-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/identifying-discrete-time-state-space-models.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the SI Model Estimation Express VI and SI Estimate State-Space Model VI to identify accurate system models.After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the following differential equations:Jdωdt+bω=KiiLdidt+Ri=V-KeωSet K[i] to be equal to K[e] to transfor

### Identifying Discrete-Time State-Space
 Models

Use the SI Model Estimation Express VI and SI Estimate
 State-Space Model VI to identify accurate system models.

After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the
 following differential equations:

J

d

ω

d

t

+

b

ω

=

K

i

i

L

d

i

d

t

+

R

i

=

V

-

K

e

ω

Set K<sub>i</sub> to be equal to
 K<sub>e</sub> to transform these differential
 equations. If you want to design a digital state feedback controller, transform these
 differential equations to the following continuous-time state-space model:

d

d

t

ω

i

=

-

b

J

K

J

-

K

L

-

R

L

ω

i

+

0

1

L

U

ω

=

1

0

ω

i

You can transform the continuous-time state-space model to the following discrete-time
 state-space model:

x

0

k

+

1

x

1

k

+

1

=

a

00

a

01

a

10

a

11

x

0

k

x

1

k

+

b

0

b

1

U

k

ω

k

=

c

0

c

1

x

0

k

x

1

k

where

- a 00 ,
 a 01 ,
 a 10 ,
 a 11 ,
 b 0 ,
 b 1 ,
 c 0 ,
 c 1 are unknown
 parameters
- ω is the rotational speed of the shaft
- U is the driving voltage

You must estimate the values of the A, B, and
 C matrices to identify a state-space model. In this example, you
 must estimate the values of a<sub>00</sub>,
 a<sub>01</sub>,
 a<sub>10</sub>,
 a<sub>11</sub>,
 b<sub>0</sub>,
 b<sub>1</sub>,
 c<sub>0</sub>,
 c<sub>1</sub> to identify the
 discrete-time state-space model.

#### Using the SI Model Estimation Express
 VI

Complete the following steps to identify the discrete-time state-space
 model by using the SI Model Estimation Express VI:

1. Add the SI Model Estimation Express VI to the block diagram
 of the VI you created. The Configure SI Model
 Estimation dialog box appears.
2. Select the State-Space button in the Select
 Model Type section to identify state-space models. The
 Model Diagram section displays a mathematical
 equation for the selected model type and a diagram of the model.
3. Select the SISO button in the Select System
 Dims section to identify Single-Input Single-Output (SISO)
 dynamic models.
4. Select the Waveform button in the Select Data
 Type section to identify dynamic models by using waveform input
 signals.
5. Enter 2 in the Number of states text box
 because this model contains two states: rotational speed ω 
 and armature current i .
6. Click the OK button to close the configuration dialog box
 and return to the block diagram.
7. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Model Estimation Express 
 VI.
8. Add the SI Draw Model VI to the block diagram.
9. Wire the system model out output of the SI Model
 Estimation Express VI to the system model 
 input of the SI Draw Model VI.
10. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block diagram: Figure 162.Model Output
 Indicator for SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-9ED6EE8C-BFB1-49FC-9F46-86C5EDA53679-a5.gif']
11. Wire all error in and error out terminals on the block diagram.
12. Run this VI to identify the dynamic system model.

#### Using the SI Estimate State-Space
 Model VI

Complete the following steps to identify the discrete-time
 state-space model by using the SI Estimate State-Space Model
 VI.

1. Add the SI Estimate State-Space Model VI to the block diagram
 of the VI you created.
2. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Estimate State-Space Model 
 VI.
3. Create a control for the structure selector input of the
 SI Estimate State-Space Model VI.
4. Set all the Boolean controls of the structure selector 
 input to FALSE because you need to estimate the
 A , B , and C 
 matrices only.
5. Create a control for the number of states input of the
 SI Estimate State-Space Model VI.
6. Set the number of states input to 2 
 because the continuous-time state-space model contains two states: rotational
 speed ω and armature current i .
7. Switch to the front panel, right-click all controls, and
 select Data Operations»Make Current Value Default from
 the shortcut menu. LabVIEW uses the current values as the default values for
 these controls.
8. Add the SI Draw Model VI to the block diagram.
9. Wire the system model out output of the SI
 Estimate State-Space Model VI to the system
 model input of the SI Draw Model VI.
10. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block
 diagram. Figure 163.Model Output
 Indicator for SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-112C074A-2B3E-4ED1-A809-4FAA580C4018-a5.gif']
11. Wire all error in and error out terminals on the block diagram.
12. Run this VI to identify the system model.

#### Verifying Resulting Dynamic System
 Models

If you use the SI Data Samples VI to generate
 the input and output data in *Exciting the System and Acquiring Data*,
 LabVIEW returns the following system model:

x

k

+

1

=

0

.

984382

0

0

-

0

.

426466

x

k

+

-

2

.

17452

E

-

5

-

0

.

000170568

u

k

y

k

=

-

0

.

384289

-

0

.

0142187

x

k

f

s

=

1000

H

z

where

- a 00 = 0.984382
- a 01 = 0
- a 10 = 0
- a 11 = –0.426466
- b 0 = –2.17452E –5
- b 1 = –0.000170568
- c 0 = –0.384289
- c 1 = –0.0142187

Parent topic:

Identifying Dynamic System Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=identifying-discrete-time-transfer-function-m.html language=enus -->
## TOPIC 00072: Identifying Discrete-Time Transfer Function Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `identifying-discrete-time-transfer-function-m.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/identifying-discrete-time-transfer-function-m.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Advanced Signal Processing Toolkit offers a variety of methods for identifying disrete-time transfer function models.After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the following differential equations:Jdωdt+bω=KiiLdidt+Ri=V-KeωSet K[i] to be equal t

### Identifying Discrete-Time Transfer Function
 Models

The LabVIEW Advanced Signal Processing Toolkit offers a variety of methods for
 identifying disrete-time transfer function models.

After physical modeling, you can describe the Direct Circuit (DC) servomotor by using the
 following differential equations:

J

d

ω

d

t

+

b

ω

=

K

i

i

L

d

i

d

t

+

R

i

=

V

-

K

e

ω

Set K<sub>i</sub> to be equal to
 K<sub>e</sub> to transform these
 differential equations. If you want to design a digital proportional-integral-derivative
 (PID) controller, transform these differential equations to the following
 continuous-time transfer function model:

ω

s

U

s

=

K

J

L

s

2

+

b

L

+

J

R

s

+

b

R

+

K

2

You can transform the continuous-time transfer function model to the following discrete-time transfer function model:

ω

z

U

z

=

b

1

z

+

b

0

z

2

+

a

1

z

+

a

0

where

- a 0 ,
 a 1 ,
 b 0 , and
 b 1 are unknown parameters
- ω is the rotational speed of the shaft
- U is the driving voltage

In this tutorial, you must estimate the values of a<sub>0</sub>, a<sub>1</sub>, b<sub>0</sub>, and b<sub>1</sub> to identify the discrete-time transfer function model.

#### Using the SI Transfer Function
 Estimation Express VI

Complete the following steps to identify the
 discrete-time transfer function model by using the SI Transfer Function
 Estimation Express VI:

1. Add the SI Transfer Function Estimation Express VI to the
 block diagram of the VI you created. The Configure SI Transfer
 Function Estimation dialog box appears.
2. Select the Waveform button to identify dynamic models by
 using waveform input signals.
3. Click the Model Settings tab.
4. Select the Discrete button to identify discrete-time
 transfer function models.
5. Enter 1 in the Numerator order text box
 because the highest numerator order of this model is z .
6. Enter 2 in the Denominator order text
 box because the highest denominator order of this model is
 z 2 .
7. Click the OK button to close the configuration dialog box
 and return to the block diagram.
8. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Transfer Function Estimation
 Express VI.
9. Add the SI Draw Model VI to the block diagram.
10. Wire the system model out output of the SI
 Transfer Function Estimation Express VI to the system
 model input of the SI Draw Model VI.
11. Create a constant for the display format for TF
 model input of the SI Draw Model VI and set
 the value to Descending .
12. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block diagram: Figure 160.Block Diagram of
 Model Output Indicator for SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-9EFE4684-9778-4814-A8B9-726BF805D1D7-a5.gif']
13. Wire all error in and error out terminals on the block diagram.
14. Run this VI to identify the dynamic system model.

#### Using the SI Estimate Transfer
 Function Model VI

Complete the following steps to identify the
 discrete-time transfer function model by using the SI Estimate Transfer
 Function Model VI.

1. Add the SI Estimate Transfer Function Model VI to the block
 diagram of the VI you created.
2. Click the polymorphic VI selector and select Discrete»Direct
 Method»Waveform .
3. Wire the stimulus signal and response
 signal outputs of the SI Data Samples VI to
 the corresponding inputs of the SI Estimate Transfer Function
 Model VI.
4. Create a control for the orders of transfer function
 model input of the SI Estimate Transfer Function
 Model VI.
5. Enter 1 in the num order field of this
 control because the highest numerator order of this model is
 z .
6. Enter 2 in the den order field of this
 control because the highest denominator order of this model is
 z 2 .
7. Switch to the front panel, right-click this control, and
 select Data Operations»Make Current Value Default from the shortcut menu. LabVIEW uses the current value as the
 default value for this control.
8. Add the SI Draw Model VI to the block diagram.
9. Wire the system model out output of the SI
 Estimate Transfer Function Model VI to the system
 model input of the SI Draw Model VI.
10. Create a constant for the display format for TF
 model input of the SI Draw Model VI and set the value to
 Descending .
11. Create an indicator for the model output of the
 SI Draw Model VI. The following figure shows the block diagram: Figure 161.Block Diagram of
 Model Output Indicator for SI Draw Model VI
 
 [IMAGE alt='image' src='GUID-9D164EA9-6660-4581-8938-CE7328F0F13A-a5.gif']
12. Wire all error in and error out terminals on the block diagram.
13. Run this VI to identify the dynamic system model.

#### Verifying Resulting Dynamic System
 Models

If you use the SI Data Samples VI to generate
 the input and output data in *Exciting the System and Acquiring Data*,
 LabVIEW returns the following system model:

y

z

=

2

.

22606

E

-

5

z

-

2

.

21744

E

-

5

z

2

-

1

.

69258

z

+

0

.

695308

u

z

f

s

=

1000

H

z

where

- a 0 =0.695308
- a 1 =1.69258
- b 0 =2.21744E –5
- b 1 =2.22606E –5

Parent topic:

Identifying Dynamic System Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=impulse-response-advanced-signal-processing-t.html language=enus -->
## TOPIC 00073: Impulse Response

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `impulse-response-advanced-signal-processing-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/impulse-response-advanced-signal-processing-t.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The impulse response not only indicates the stability and causality of the system if feedback exists in the system, but also provides information on properties such as the damping, dominating time constant, and time delay.An impulse input to a dynamic system is defined differently depending on wheth

### Impulse Response

The impulse response not only indicates the stability and causality of the system if
 feedback exists in the system, but also provides information on properties such as the
 damping, dominating time constant, and time delay.

An impulse input to a dynamic system is defined differently depending on whether the system is
 discrete or continuous. For a continuous dynamic system, an impulse input, also known as
 the Dirac delta function, is a unit-area signal with an infinite amplitude and
 infinitely small duration occurring at a specified time. At all other times, the input
 signal value is zero. For a discrete system, an impulse is a physical pulse that has
 unit amplitude at the first sample period and zero amplitude for all other times.

The following figure shows an impulse input:

Figure 178.

[IMAGE alt='image' src='GUID-29F1AA75-8FE1-47FC-A4D1-0D0C9D7CD3BD-a5.gif']

where t is time andu(t) is the
 input signal

Because the impulse signal excites all frequencies and the duration of this signal is infinitely small, you can see the natural response of the system.

The following figure shows that the impulse response of a linear time-invariant system is equal to the output y(k) of the system when you apply an impulse signal to the input u(k) of the system. The impulse response provides the complete characteristic information of a system.

Figure 179.

[IMAGE alt='image' src='GUID-EB238B49-E777-45DA-9E27-D43172C1A18B-a5.gif']

If you know the impulse response h(n) and the input signal
 u(k) of a system, then you can compute the
 output y(k) of the system by using the following
 equation:

y

k

=

∑

n

=

-

∞

∞

u

k

-

n

h

n

+

e

k

where e(k) is the disturbance of the system.

According to impulse response theory, when you apply a Dirac delta function to a system, the output of the system is the impulse response. You can think of the Dirac delta function δ(x) as a function that has the value of infinity for x = 0, the value zero elsewhere, and a total integral of one. However, generating an ideal Dirac delta function is unrealistic.

If you apply an approximate impulse with a small duration to the input of a system, the output of
 the system is the approximation of the impulse response of the system. The smaller the
 duration of the impulse, the closer the output of the system is to the true impulse
 response. However, an impulse carries little energy and might not excite the system, and
 noise might corrupt the output of the system. An impulse with a large amplitude and
 duration can improve the signal-to-noise ratio of the output signal. However, a large
 amplitude impulse can damage the hardware of the system, and a long-duration impulse
 leads to inaccuracy. For these reasons, you can use the least squares and correlation
 analysis methods to estimate the impulse response.

#### Applications of the Impulse
 Response

Some of the information indicated by the impulse response, such
 as the time delay, is useful for parametric model estimation. Therefore, you can use
 nonparametric impulse response estimation before parametric model estimation to help
 estimate the parameters. You can use the SI Estimate Impulse
 Response VI to estimate the impulse response and determine the time
 delay of a system by using the correlation analysis method.

The following
 figure shows the block diagram of a VI that simulates a system defined by the
 following equation:

y(k) =
 0.2u(k – 2) +
 0.8u(k – 3) +
 0.3u(k – 4)

Figure 180.

[IMAGE alt='image' src='GUID-25A038B6-556E-43BA-9D40-39143E1A266E-a5.gif']

In the previous figure, the two initial values of the estimated
 impulse response are smaller than the confidence
 level. You can have 99.0% confidence that values less than the
 confidence level are insignificant, and you can consider
 those values to be equal to 0. Therefore, you can conclude that the time delay of
 the system is 2 because the beginning of the first two values of the impulse
 response are zero.

Another common application of the impulse response is to
 detect feedback in systems by using the least squares method. If feedback exists in
 a system, the impulse response of the system becomes significantly large at negative
 lags and the correlation between the input signal and disturbance
 e(n) is nonzero. The correlation analysis
 method assumes the input signal and the disturbance
 e(n) are independent from each other.
 Thus, this method cannot estimate accurately the impulse response of the system that
 contains feedback. Only the least squares method can provide reliable results. You
 can use the SI Detect Feedback VI to estimate the impulse
 response of a system and determine whether feedback exists in the
 system.

- [Least Squares Method](least-squares-method-advanced-signal-processi.html)
- [Correlation Analysis Method](correlation-analysis-method-advanced-signal-p.html)
- [Select an Impulse Response Length](select-an-impulse-response-length-advanced.html)

Parent topic:

Nonparametric Model Estimation Methods

Related concepts:

- Closed-Loop Systems Model Estimation Methods
- Parametric Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=indirect-identification-advanced-signal-proce.html language=enus -->
## TOPIC 00074: Indirect Identification

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `indirect-identification-advanced-signal-proce.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/indirect-identification-advanced-signal-proce.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The indirect identification approach, which estimates the transfer function model of a dynamic system in a closed-loop system, first identifies the transfer function model of the closed-loop system based on the reference signal and the response signal.This approach then retrieves the transfer functi

### Indirect Identification

The indirect identification approach, which estimates the transfer function model of a
 dynamic system in a closed-loop system, first identifies the transfer function model of
 the closed-loop system based on the reference signal and the response signal.

This approach then retrieves the transfer function model of the dynamic system from the
 identified closed-loop system. The indirect identification approach can identify the
 transfer function of the dynamic system accurately even when the Signal-to-Noise Ratio
 (SNR) of the system is low and no matter whether the output noise is white noise or
 color noise. However, this approach requires prior knowledge about the controller of the
 system and the reference signal also must be available. In addition, any inaccuracy or
 nonlinearity of the controller in the system might affect estimating the model of the
 dynamic system.

With indirect identification, you can use the following two equations to describe the
 feedback-path closed-loop system:

y

k

=

G

0

z

u

k

+

e

k

u

k

=

r

k

-

F

y

z

y

k

where

- G 0 ( z ) is the open-loop transfer
 function of the dynamic system
- F y ( z ) is the transfer function of a
 Linear, Time-Invariant (LTI) controller
- u ( k ) is the stimulus signal of the system
- y ( k ) is the response signal of the system
- r ( k ) is the reference signal of the
 system
- e ( k ) is the output noise of the system

By combining the previous two equations, you can represent the closed-loop relationship with the following equation:

y

k

=

G

0

z

1

+

G

0

z

F

y

z

r

k

+

1

1

+

G

0

z

F

y

z

e

k

If you define G<sub>cl</sub> as the closed-loop transfer function between the
 reference signal and the response signal, and let G<sub>cl</sub>
 satisfy the following equation:

G

c

l

=

G

0

z

1

+

G

0

z

F

y

z

you can estimate G<sub>cl</sub> with
 r(k) as the input and
 y(k) as the output using an open loop method,
 because r(k) and
 e(k) are uncorrelated. You then can calculate
 G<sub>0</sub>after you calculate
 G<sub>cl</sub>, as the following equation shows:

G

0

=

G

c

l

1

-

G

c

l

F

y

For feedforward-path closed-loop systems, you use the following two equations to describe the
 systems:

y

k

=

G

0

z

u

k

+

e

k

u

k

=

r

k

-

y

k

F

y

z

By combining the previous two equations, you can represent the feedforward-path closed-loop
 relationship with the following equation:

y

k

=

F

y

z

G

0

z

1

+

G

0

z

F

y

z

r

k

+

1

1

+

G

0

z

F

y

z

e

k

If you define G<sub>cl</sub> as the feedforward-path closed-loop transfer
 function and let G<sub>cl</sub> satisfy the following equation:

G

c

l

=

F

y

z

G

0

z

1

+

G

0

z

F

y

z

you can estimate G<sub>cl</sub> with
 r(k) as the input and
 y(k) as the output using an open loop method,
 because r(k) and
 e(k) are uncorrelated. You then can calculate
 G<sub>0</sub>after you calculate
 G<sub>cl</sub>, as the following equation shows:

G

0

=

G

c

l

1

-

G

c

l

F

y

With indirect identification, you calculate G<sub>cl</sub>by performing
 polynomial operations on G<sub>o</sub> and
 F<sub>y</sub>. Because of the limitations of polynomial
 operations, the orders of the numerator and denominator might change after manipulation.
 Thus, the SI Estimate Transfer Function Model VI or the SI
 Transfer Function Estimation Express VI, which you can use with the
 indirect identification approach, might return an error regarding the mismatch between
 the order you set and the order of the estimated model. In this case, you must adjust
 the tolerance setting of these two VIs so that the numerator and denominator orders
 match the orders you set. A larger tolerance facilitates zero-pole cancellations, which
 reduce the numerator and denominator polynomial orders.

Parent topic:

Closed-Loop Systems Model Estimation Methods

Related concepts:

- Transfer Function Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=integer-wavelet-transform.html language=enus -->
## TOPIC 00075: Integer Wavelet Transform

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `integer-wavelet-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/integer-wavelet-transform.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: For integer-encoded signals, an Integer Wavelet Transform (IWT) can be particularly efficient.Many signal samples you encounter in real-world applications are encoded as integers, such as the signal amplitudes encoded by Analog-to-Digital (A/D) converters and color intensities of pixels encoded in d

### Integer Wavelet Transform

For integer-encoded signals, an Integer Wavelet Transform (IWT) can be particularly
 efficient.

Many signal samples you encounter in real-world applications are encoded as integers, such as the
 signal amplitudes encoded by Analog-to-Digital (A/D) converters and color intensities of
 pixels encoded in digital images. The IWT is an invertible integer-to-integer wavelet
 analysis algorithm. You can use the IWT in the applications that you want to produce
 integer coefficients for integer-encoded signals. Compared with the Continuous Wavelet
 Transform (CWT) and the Discrete Wavelet Transform (DWT), the IWT is not only
 computationally faster and more memory-efficient but also more suitable in lossless
 data-compression applications. The IWT enables you to reconstruct an integer signal
 perfectly from the computed integer coefficients.

Use the WA Integer Wavelet Transform VI, which implements the IWT with the
 lifting scheme, to decompose an integer signal or image. Use the WA Inverse
 Integer Wavelet Transform VI, which implements the inverse IWT with the
 inverse lifting scheme, to reconstruct an integer signal or image from the IWT
 coefficients. Use the WA Get Coefficients of Integer Wavelet
 TransformVI to get the IWT coefficients you compute from the WA
 Integer Wavelet Transform VI and to return the coefficient type, such as
 the approximation coefficients or the detail coefficients, at a specific coefficient
 level. Use the WA Set Coefficients of Integer Wavelet Transform VI to
 set the coefficients you obtain from the WA Get Coefficients of Integer Wavelet
 Transform VI.

Parent topic:

Wavelet Analysis Concepts

Related concepts:

- Wavelet Signal Processing Application Areas
- Continuous Wavelet Transform
- Discrete Wavelet Transform

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=interactively-designing-discrete-wavelets.html language=enus -->
## TOPIC 00076: Interactively Designing Discrete Wavelets

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `interactively-designing-discrete-wavelets.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/interactively-designing-discrete-wavelets.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can apply the predefined wavelets directly to signal processing applications.Both the discrete wavelet transform and the inverse discrete wavelet transform are implemented using a set of cascaded two-channel Perfect Reconstruction (PR) filter banks. The WA Wavelet Filter VI already contains a co

### Interactively Designing Discrete Wavelets

You can apply the predefined wavelets directly to signal processing applications.

Both the discrete wavelet transform and the inverse discrete wavelet transform are implemented
 using a set of cascaded two-channel Perfect Reconstruction (PR) filter banks.

The WA Wavelet Filter VI already contains a collection of predefined wavelets,
 including orthogonal wavelets (Haar, Daubechies, Coiflets, Symmlets) and biorthogonal
 wavelets (Biorthogonal, including FBI). If you cannot find a wavelet that best matches
 the signal, you can use the Wavelet Design Express VI to design a
 customized discrete wavelet.

The following figure shows the wavelet design process:

Figure 140.

[IMAGE alt='image' src='GUID-60B40EC6-5CD1-40D1-8A34-A3D8B5B1971B-a5.gif']

Using the Wavelet Design Express VI, you need to complete the following steps
 to design wavelets:

1. Select the wavelet type.
2. Design the product of lowpass filters, P 0 ( z ),
 where the auxiliary function P 0 ( z )
 is the product of G 0 ( z ) and
 H 0 ( z ).
3. Select the factorization type to factorize
 P 0 ( z ) into
 G 0 ( z ) and
 H 0 ( z ).

After you create an analysis lowpass filter
 G<sub>0</sub>(z) and a synthesis lowpass filter
 H<sub>0</sub>(z), the Wavelet Design
 Express VI automatically generates the corresponding analysis highpass
 filter G<sub>1</sub>(z) and synthesis highpass
 filter H<sub>1</sub>(z).

The design of discrete wavelets is essentially the design of two-channel PR filter banks. This
 book describes the steps that you can follow when using the Wavelet Design
 Express VI to design discrete wavelets and provides an example of
 designing the FBI wavelet.

- [Selecting the Wavelet Type](select-the-wavelet-type.html)
- [Design the Product P0(z)](design-the-product-p0-z.html)
- [Select the Factorization Type for P0(z)](select-the-factorization-type-for-p0-z.html)
- [Example: Designing the FBI Wavelet](example-designing-the-fbi-wavelet.html)

Parent topic:

Wavelet Analysis Concepts

Related concepts:

- Discrete Wavelet Transform

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=introduction-to-system-identification-advance.html language=enus -->
## TOPIC 00077: Introduction to System Identification

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `introduction-to-system-identification-advance.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/introduction-to-system-identification-advance.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: System identification, the first step in the model-based control design process, involves building mathematical models of a dynamic system based on a set of measured stimulus and response data samples.You can use system identification in a wide range of applications, including mechanical engineering

### Introduction to System Identification

System identification, the first step in the model-based control design process, involves
 building mathematical models of a dynamic system based on a set of measured stimulus and
 response data samples.

You can use system identification in a wide range of applications, including mechanical
 engineering, biology, physiology, meteorology, economics, and model-based control
 design. For example, engineers use a system model of the relationship between the fuel
 flow and the shaft speed of a turbojet engine to optimize the efficiency and operational
 stability of the engine. Biologists and physiologists use system identification
 techniques in areas such as eye pupil response and heart rate control. Meteorologists
 and economists build mathematical models based on historical data for use in
 forecasting.

The LabVIEW Advanced Signal Processing Toolkit and the LabVIEW Control Design and Simulation
 Module provide the following tools.

#### System Identification
 VIs

You can use the System Identification VIs to
 preprocess raw data from a dynamic system and develop a model that reflects the
 behavior of that system. The Data Preprocessing VIs enable you to
 analyze the response of a dynamic system to a certain stimulus. After analyzing the
 data, you can use the Parametric Model Estimation,
 Nonparametric Model Estimation, Partially Known
 Model Estimation, Recursive Model Estimation, and
 Frequency-Domain Model Estimation VIs to estimate a model for
 the dynamic system. You can use the Model Validation or
 Model Analysis VIs to determine whether the model accurately
 describes the dynamics of the identified system. You also can use the Model
 Conversion VIs to convert a model from one type to another. Finally,
 you can use the SI Convert to Models of CDT VI to convert the
 model you identified to a model that you can use in the LabVIEW Control Design and
 Simulation Module.

The System Identification VIs enable you
 to customize a LabVIEW block diagram to achieve specific goals. You also can use
 other LabVIEW VIs and functions to enhance the functionality of the application.
 Creating a LabVIEW application using the System Identification
 VIs requires basic knowledge about programming in LabVIEW. Refer to the Getting
 Started with LabVIEW manual for more information about the LabVIEW programming
 environment.

The following case studies demonstrate how to use the
 System Identification VIs to estimate different model
 representations by using time-domain or frequency domain data.

Flexible Arm Case Study

Partially Known Model Estimation Case Study

Frequency-Domain Model Estimation Case Study

#### System Identification
 Assistant

If you do not have prior knowledge about programming in LabVIEW,
 you can use the System Identification Assistant to develop a
 model that reflects the behavior of a certain dynamic system. You access the
 System Identification Assistant by launching LabVIEW and
 selecting Tools»Control Design and Simulation»Launch System Identification
 Assistant.

Using the System Identification Assistant,
 you can create a project that encompasses the whole system identification process.
 In a single project, you can load or acquire raw data into the System
 Identification Assistant, preprocess the data, estimate a model that
 describes the system, and then validate the accuracy of the model. SignalExpress
 provides windows in which you can see the raw data, the response data, the estimated
 model, the validation results, and the mathematical equations that describe the
 model.

After creating a project in SignalExpress, you can convert the project
 to a LabVIEW block diagram and customize the block diagram in LabVIEW. This
 conversion enables you to enhance the capabilities of the application. Refer to the
 SignalExpress Help, available in the SignalExpress
 environment by selecting Help»SignalExpress Help, for more information about using the assistant to develop
 models.

- [Model-Based Control Design Process](model-based-control-design-process-advanced-s.html)
- [Model Types and Representations](model-types-and-representations-advanced-sign.html)

Parent topic:

System Identification Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=introduction-to-time-frequency-analysis.html language=enus -->
## TOPIC 00078: Introduction to Time Frequency Analysis

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `introduction-to-time-frequency-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/introduction-to-time-frequency-analysis.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: One way to represent a signal is the time-domain waveform, which shows how the amplitude of the signal changes over time.Examples of time-varying signals include the temperature in temperature logs, stock-index profiles, electrocardiogram signals, vibration signals, and speech signals, such as the s

### Introduction to Time Frequency Analysis

One way to represent a signal is the time-domain waveform, which shows how the
 amplitude of the signal changes over time.

Examples of time-varying signals include the temperature in temperature logs, stock-index
 profiles, electrocardiogram signals, vibration signals, and speech signals, such as the
 speech signal in the following figure:

Figure 5.

[IMAGE alt='image' src='GUID-28254F58-0635-4441-9F2F-BA36A6765BA2-a5.gif']

The time-domain speech waveform in the previous figure depicts how the sound-pressure level evolves over time. The higher the sound-pressure level at any particular time, the larger the magnitude, or the absolute value, of the signal.

An important task in most speech-enhancement applications is to find the noise characteristics and then remove the noise from the speech signal. In the previous figure, the period from 1.4 s to 2.0 s is the silence period, when no speech is present. Any signal measured during this time frame is noise. In speech-enhancement applications, you often observe the signal during the silence periods to estimate the noise characteristics.

In many speech-analysis applications, it is important to identify the spectral content of the
 speech signal. Notice that the time waveform in the previous figure does not
 provide information about the spectral content of the speech signal. To
 determine the frequency characteristics of this speech signal, you need a
 way to estimate the spectral content of the signal. One possible technique
 is to apply the Fast Fourier Transform (FFT) to the signal to convert the
 time waveform to a frequency spectrum. The following figure is an example of
 the FFT.

Figure 6.

[IMAGE alt='image' src='GUID-C91322B0-BB91-4967-8076-FC62AEAA2021-a5.gif']

Using the FFT to transform a time-domain signal to the frequency-domain representation of the
 signal can help you discover information that might be hidden in the time-domain
 waveform. The square of the magnitude of the FFT is called the power spectrum, which
 characterizes how the energy of a signal is distributed in the frequency domain.

The power spectrum of a speech signal can show the relative intensity of the energy of a signal
 at each frequency for the entire signal. However, the power spectrum of a signal for a
 shorter time scale can be more useful. For example, if a speech signal includes separate
 low-frequency utterances and high-frequency utterances, separate power spectra for each
 utterance can be useful. Even within a particular utterance, variations in signal
 characteristics might exist, so it is useful to analyze the signal with a short time
 scale. For example, it might be useful to separate unvoiced speech from voiced speech in
 a particular utterance.

You can use the STFT spectrogram to provide power spectra for short time scales. The following
 figure shows the STFT spectrogram of the speech signal in the previous two figures.

Figure 7.

[IMAGE alt='image' src='GUID-9FD39D7A-A995-432B-8035-37302E61881B-a5.gif']

1

2

3

In the previous figure, the color depicts the magnitude of the energy of the signal at time, t, and frequency, f. The spectrum from red to blue corresponds to the energy level from strongest to weakest.

From the time-frequency representation in the previous figure, you can identify the silence
 period, and you can see the change in spectral content of the signal over time. You can
 see the time onset, the end, the fundamental frequency, and the harmonic frequencies of
 the two utterances in the previous figure. These parameters are crucial in various
 speech-processing applications, such as speech recognition. Compared to the speech
 signal and FFT figures, the spectrogram in the previous figure can illuminate better the
 nature of a human speech signal.

Speech signal analysis is only one example application that benefits from methods other than the
 FFT. Time-frequency analysis is broadly useful because most signals in real-world
 applications have time-varying spectral content. Analyzing the time-dependent spectra
 enables you to better understand the signal and the associated system. The spectrogram
 in the previous figure is only one of many proven time-frequency analysis methods.

Parent topic:

Time Frequency Analysis Concepts

Related concepts:

- STFT Spectrogram

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=introduction-to-time-series-analysis.html language=enus -->
## TOPIC 00079: Introduction to Time Series Analysis

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `introduction-to-time-series-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/introduction-to-time-series-analysis.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A time series is a sequence of observed values ordered through time. Time series analysis uses a collection of systematic approaches to extract information about the characteristics of a physical system that generates time series.For example, the air temperature in meteorological science, blood pres

### Introduction to Time Series Analysis

A time series is a sequence of observed values ordered through time. Time series
 analysis uses a collection of systematic approaches to extract information
 about the characteristics of a physical system that generates time
 series.

For example, the air temperature in meteorological science, blood pressure in biomedical science,
 or vibration in mechanical engineering or civil engineering are examples of
 a time series. Approaches to time series analysis include estimating
 statistical parameters, building dynamic models, performing correlations,
 computing the Power Spectral Density (PSD), and others.

Generally, a time series contains the following information:

- The characteristics of the time series, such as amplitude, spectral content and other
 statistical characteristics.
- The native characteristics or structural parameters of a system that generates the time series,
 for example, the natural frequency and damping of a civil structure.
- The characteristics of the input or stimulus to the physical system that generates the time series.

#### Continuous Time Series and Discrete
 Time Series

In nature, physical quantities such as temperature, pressure, and light intensity
 change continuously. Observations of these values form a continuous time series.

Given a continuous time series, you can digitize the values at a specified time
 interval to obtain a discrete time series. The following figure shows the
 seismograph of the Kobe earthquake, recorded at Tasmania University, Hobart,
 Australia on January 16, 1995. In this figure, the continuous earthquake vibration
 signal is sampled at a one-second interval to form a discrete time series.

Figure 46.

[IMAGE alt='image' src='GUID-3449986E-06F5-473F-990B-299641D64062-a5.gif']

Note

#### Time-Ordered Series and Spatial-Ordered Series

Time series can be ordered not only through time but also through other physical units. For example, you can obtain a discrete time series ordered versus angular position by sampling the diameter of a spindle as a function of angle.

The following figure shows an example of the diameter error as a function of angle of a spindle during a lathe machining process. The diameter error generates a discrete time series ordered versus angular position.

Figure 47.

[IMAGE alt='image' src='GUID-7315E252-7F51-4528-92E1-6DDD9BA8DF8F-a5.gif']

#### Univariate Time Series and
 Multivariate Time Series

You can collect observed values from a single source or simultaneously from two or
 more sources. Single-source observations generate univariate time series, and
 multi-source observations form multivariate time series, or vector time series. For
 example, you can obtain a multivariate time series by recording the values of
 pressure, flow, and temperature simultaneously in an industrial process.

The following figure shows an example of the vibration signals from a
 steel-reinforced concrete beam. The signals are acquired simultaneously from seven
 acceleration sensors located at different positions on the beam.

Figure 48.

[IMAGE alt='image' src='GUID-8F2ECB31-F498-43B3-A38C-E6E329559C94-a5.gif']

#### Stationary Time Series and Nonstationary Time Series

In theory, given a behavioral model for a system, you can predict future values of a time series measured from that system, based on past observations. However, in practice, physical systems are affected by many kinds of disturbances, so the predicted values always reflect the stochastic, or statistical, characteristic of a time series.

Generally speaking, if the statistical characteristic of a time series contains no systematic change, the time series is stationary. Otherwise the time series is nonstationary.

#### Time Series Analysis
 Objectives

Time series analysis is useful when you want to
 extract information from a time series, to discover the
 characteristics of a physical system that generates the time series,
 to predict the changes of a time series, or to improve control over
 the physical system. The objectives of time series analysis are as
 follows:

Description

Explanation

Prediction

Control

Time series exist in many application areas, ranging from economics
 to engineering. The LabVIEW Time Series Analysis Tools focus more on
 the applications in engineering. Use the Time Series
 Analysis VIs to analyze or process a time
 series.

Parent topic:

Time Series Analysis Concepts

Related concepts:

- Perform Statistical Analysis
- Building Models
- Correlation Methods
- Power Spectrum Estimation Methods
- Predict Time Series Values

Related information:

- Related Documentation

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=introduction-to-wavelet-signal-processing.html language=enus -->
## TOPIC 00080: Introduction to Wavelet Signal Processing

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `introduction-to-wavelet-signal-processing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/introduction-to-wavelet-signal-processing.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wavelets are functions that you can use to decompose signals. Just as the Fourier transform decomposes a signal into a family of complex sinusoids, the wavelet transform decomposes a signal into a family of wavelets.Unlike sinusoids, which are symmetric, smooth, and regular, wavelets can be either s

### Introduction to Wavelet Signal Processing

Wavelets are functions that you can use to decompose signals. Just as the Fourier
 transform decomposes a signal into a family of complex sinusoids, the wavelet transform
 decomposes a signal into a family of wavelets.

Unlike sinusoids, which are symmetric, smooth, and regular, wavelets can be either symmetric or
 asymmetric, sharp or smooth, regular or irregular. The following figure compares a sine
 wave with the db02 wavelet and the FBI wavelet:

Figure 101.

[IMAGE alt='image' src='GUID-1BBF3A9C-A93C-4D1A-B18A-F4C3D143A360-a5.gif']

In previous figure, you can see that the Sine Wave is symmetric, smooth, and regular. The db02 Wavelet is asymmetric, sharp, and irregular. The FBI Wavelet is symmetric, smooth, and regular. You also can see that a sine wave has an infinite length, whereas a wavelet has a finite length.

For different types of signals, you can select different types of wavelets that best match the
 features of the signal you want to analyze. Therefore, you can perform wavelet signal
 processing and generate reliable results about the underlying information of a
 signal.

The family of wavelets contains the dilated and translated versions of a prototype function.
 Traditionally, the prototype function is called a mother wavelet. The scale and shift of
 wavelets determine how the mother wavelet dilates and translates along the time or space
 axis. A scale factor greater than one corresponds to a dilation of the mother wavelet
 along the horizontal axis, and a positive shift corresponds to a translation to the
 right of the scaled wavelet along the horizontal axis. The following figure shows the
 db02 mother wavelet and the associated dilated and translated wavelets with different
 scale factors and shift values:

Figure 102.

[IMAGE alt='image' src='GUID-5D44EE54-CD8D-438E-B1C7-E2CCE3036CB0-a5.gif']

#### Wavelet Transform

The wavelet transform computes the inner products of a signal with a family of
 wavelets. The wavelet transform tools are categorized into continuous wavelet tools
 and discrete wavelet tools. Usually, you use the continuous wavelet tools for signal
 analysis, such as self-similarity analysis and time-frequency analysis. You use the
 discrete wavelet tools for both signal analysis and signal processing, such as noise
 reduction, data compression, peak detection and so on.

In contrast with sinusoids, wavelets are localized in both the time and frequency
 domains, so wavelet signal processing is suitable for nonstationary signals, whose
 spectral content changes over time. The adaptive time-frequency resolution of
 wavelet signal processing enables you to perform multiresolution analysis on
 nonstationary signals. The properties of wavelets and the flexibility to select
 wavelets make wavelet signal processing a beneficial tool for feature extraction
 applications.

#### Benefits of Wavelet Signal Processing

Wavelet signal processing is different from other signal processing methods because of the unique properties of wavelets. For example, wavelets are irregular in shape and finite in length. Wavelet signal processing can represent signals sparsely, capture the transient features of signals, and enable signal analysis at multiple resolutions.

#### Sparse
 Representation

Wavelets are localized in both the time and frequency
 domains because wavelets have limited time duration and frequency bandwidth. The
 wavelet transform can represent a signal with a few coefficients because of the
 localization property of wavelets. The following figure shows the waveform of the
 Doppler signal:

Figure 103.

[IMAGE alt='image' src='GUID-A383461D-84B5-4575-A5A2-6A176F86096A-a5.gif']

The following figure shows the Discrete Wavelet Transform (DWT) coefficients of
 the Doppler signal:

Figure 104.

[IMAGE alt='image' src='GUID-77F2D648-EC65-4CAB-9B9C-B3A9D00B78C4-a5.gif']

In the previous figure, most of the DWT coefficients are zero, which indicates
 that the wavelet transform is a useful method to represent signals sparsely and
 compactly. Therefore, you usually use the DWT in some signal compression
 applications.

#### Transient Feature
 Detection

Transient features are sudden changes or discontinuities in a
 signal. A transient feature can be generated by the impulsive action of a system and
 frequently implies a causal relationship to an event. For example, heartbeats
 generate peaks in an Electrocardiogram (ECG) signal.

Transient features
 generally are not smooth and are of short duration. Because wavelets are flexible in
 shape and have short time durations, the wavelet signal processing methods can
 capture transient features precisely. The following figure shows an ECG signal and
 the peaks detected with the wavelet transform-based method. This method locates the
 peaks of the ECG signal precisely.

Figure 105.

[IMAGE alt='image' src='GUID-35C46EB2-519F-4CAD-BC7D-A48350E3BE7B-a5.gif']

The LabVIEW Wavelet Analysis Tools provide many types of wavelets, such as the
 Daubechies, Haar, and Coiflet wavelets.

#### Multiple
 Resolutions

Signals usually contain both low-frequency components and
 high-frequency components. Low-frequency components vary slowly with time and
 require fine frequency resolution but coarse time resolution. High-frequency
 components vary quickly with time and require fine time resolution but coarse
 frequency resolution. You need to use a Multiresolution Analysis (MRA) method to
 analyze a signal that contains both low- and high-frequency
 components.

Wavelet signal processing is naturally an MRA method because of
 the dilation process. The following figure shows the wavelets with different
 dilations and their corresponding power spectra:

Figure 106.

[IMAGE alt='image' src='GUID-CDB40E4B-570D-402F-AEC5-5FB71DD73613-a5.gif']

The Wavelets graph contains three wavelets with different
 scales and translations. The Power Spectra of Wavelets graph
 shows the power spectra of the three wavelets, where a and u represent the scale and
 shift of the wavelets, respectively. The previous figure shows that a wavelet with a
 small scale has a short time duration, a wide frequency bandwidth, and a high
 central frequency. This figure also shows that a wavelet with a large scale has a
 long time duration, a narrow frequency bandwidth, and a low central
 frequency.

The time duration and frequency bandwidth determine the time and
 frequency resolutions of a wavelet, respectively. A long time duration means coarse
 time resolution. A wide frequency bandwidth means coarse frequency resolution. The
 following figure shows the time and frequency resolutions of the three wavelets with
 three boxes in the time-frequency domain. The heights and widths of the boxes
 represent the frequency and time resolutions of the wavelets, respectively. This
 figure shows that a wavelet with a small scale has fine time resolution but coarse
 frequency resolution and that a wavelet with a large scale has fine frequency
 resolution but coarse time resolution:

Figure 107.

[IMAGE alt='image' src='GUID-ABF89189-65DE-411F-950E-3D3D922C741C-a5.gif']

The fine frequency resolution of large-scale wavelets enables you to measure the
 frequency of the slow variation components in a signal. The fine time resolution of
 small-scale wavelets enables you to detect the fast variation components in a
 signal. Therefore, wavelet signal processing is a useful multiresolution analysis
 tool.

Parent topic:

Wavelet Analysis Concepts

Related concepts:

- Example: Designing the FBI Wavelet
- Signal Processing with Continuous Wavelets
- Signal Processing with Discrete Wavelets
- Discrete Wavelet Transform
- Multiresolution Analysis

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=joint-input-output-identification-advanced-si.html language=enus -->
## TOPIC 00081: Joint Input-Output Identification

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `joint-input-output-identification-advanced-si.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/joint-input-output-identification-advanced-si.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you do not have any knowledge about the controller structure but the stimulus, response, and reference signals are all available, you can use the joint input-output identification approach to estimate the transfer function model of a dynamic system in a closed-loop system.This approach uses the t

### Joint Input-Output Identification

If you do not have any knowledge about the controller structure but the stimulus,
 response, and reference signals are all available, you can use the joint input-output
 identification approach to estimate the transfer function model of a dynamic system in a
 closed-loop system.

This approach uses the transfer functions from different input-output signal pairs to estimate a
 closed-loop system. The System Identification VIs implement the
 following two-stage method for the joint input-output approach:

1. Let T<sub>0</sub>(z) satisfy the following
 equation: T0z=11+G0zFyz By manipulating two equations describing the feedback-path closed-loop
 system, you can rewrite u(k) as
 follows: uk=T0zrk-FyzT0zek Any open-loop model estimation method then can estimate
 T<sub>0</sub>(z) because
 r(k) and
 e(k) are uncorrelated signals. After
 you obtain the value of T<sub>0</sub>(z),
 you can compute û(k) =
 T<sub>0</sub>(z)r(k).
 You then can represent u(k) as
 follows: uk=u^k-FyzT0zek Using the previous equation, you obtain an input signal
 û(k), which is constructed from
 r(k) and is uncorrelated with the
 measurement noise.
2. By manipulating the equation y(k) =
 G<sub>0</sub>(z)u(k)
 + e(k), you can rewrite
 y(k) as follows: yk=G0zu^k+T0zek Because û(k) is
 uncorrelated with e(k), the original
 closed-loop model estimation problem between
 u(k) and
 y(k) becomes an open-loop problem
 between û(k) and
 y(k). You use the same
 methodology to compute y(k) for a
 feedforward-path closed-loop system, where T0z=Fyz1+G0zFyz You rewrite y(k) as follows: yk=u^kG0z+1-T0zG0kek The two-stage method does not require you to know anything about the
 feedback or the controller structure and controller parameters. Also, you treat
 the closed-loop model estimation as an open-loop model estimation within each of
 the two steps. Therefore, you can use any method that works with open-loop
 models. Whether the real-world output noise is white noise or color noise, the
 two-stage method provides reliable estimations.

Parent topic:

Closed-Loop Systems Model Estimation Methods

Related concepts:

- Transfer Function Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=kalman-filter-advanced-signal-processing-tool.html language=enus -->
## TOPIC 00082: Kalman Filter

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `kalman-filter-advanced-signal-processing-tool.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/kalman-filter-advanced-signal-processing-tool.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The convergence rate of the Kalman filter is relatively fast, but the implementation is more complex than that of LMS-based algorithms.The Kalman filter is a linear optimum filter that minimizes the mean of the squared error recursively.Recall that the equation J(k) = E[e^2(k)] defines the cost func

### Kalman Filter

The convergence rate of the Kalman filter is relatively fast, but the implementation is
 more complex than that of LMS-based algorithms.

The Kalman filter is a linear optimum filter that minimizes the mean of the squared error
 recursively.

Recall that the equation
 J(k) = E[e<sup>2</sup>(k)] defines the cost function. The following procedure
 lists the steps of the Kalman filter algorithm.

1. Initialize the parametric vector w⇀k+1=w⇀k+ek·K⇀k using a small positive number ε. w⇀0=ε,ε,...,εT
2. Initialize the data vector φ⇀k . φ⇀0=0,0,...,0T
3. Initialize the k × k matrix P (0).

 P0=ε0000ε0000...0000ε
4. For k = 1, update the data vector φ⇀k based on φ⇀k-1 and the current input data
 u ( k ) and output data
 y ( k ).
5. Compute the predicted response y^k by solving the following equation: y^k=φ⇀Tk·w⇀k
6. Compute the error e ( k ) by solving the following equation: ek=yk-y^k
7. Update the Kalman gain vector K⇀k defined by the following equation: K⇀k=Pk·φ⇀kQM+φ⇀Tk·Pk·φ⇀k Q M is the measurement noise and
 P ( k ) is a
 k × k matrix whose initial value is
 defined by P (0) in step 3.
8. Update the parametric vector w⇀k . w⇀k+1=w⇀k+ek·K⇀k
9. Update the P ( k ) matrix.

 Pk+1=Pk-K⇀k·φ⇀Tk·Pk+QP Q P is the correlation matrix of the process noise.
10. Stop if the error is small enough, else set k = k + 1 and repeat steps 4–10.

Parent topic:

Recursive Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=least-mean-squares-advanced-signal-processing.html language=enus -->
## TOPIC 00083: Least Mean Squares

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `least-mean-squares-advanced-signal-processing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/least-mean-squares-advanced-signal-processing.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Least Mean Squares (LMS) algorithm is one of the most widely used and understood adaptive algorithms.The LMS method uses the following equations to define the cost function J(k) = E[e^2(k)]. The parametric vector ŷ(k) updates according to the following equation:w⇀k+1=w⇀k+μekφ⇀kk is the number of

### Least Mean Squares

The Least Mean Squares (LMS) algorithm is one of the most widely used and understood
 adaptive algorithms.

The LMS method uses the following equations to define the cost function
 J(k) =
 E[e<sup>2</sup>(k)].

The parametric vector ŷ(k) updates according to the following equation:

w

⇀

k

+

1

=

w

⇀

k

+

μ

e

k

φ

⇀

k

k is the number of iterations, μ is step-size, which is a positive constant,
 and ⃗φ(k) is the data vector from the past input data
 u(k) and output data
 y(k). ⃗φ(k) is defined by the following
 equation:

φ

k

=

-

y

t

-

1

.

.

.

-

y

t

-

k

u

t

-

1

.

.

.

u

t

-

m

T

The following procedure describes how to implement the LMS algorithm:

1. Initialize the step-size μ.
2. Initialize the parametric vector w⇀k using a small positive number ε. w⇀0=ε,ε,...,εT
3. Initialize the data vector φ⇀k=ukyk φ⇀0=0,0,...,0T
4. For k = 1, update the data vector φ⇀k based on φ⇀k-1 and the current input data
 u ( k ) and output data
 y ( k ).
5. Compute the predicted response ŷ(k) using the following equation: y^k=φ⇀Tkw⇀k
6. Compute the error e ( k ) by solving the following equation: ek=yk-y^k
7. Update the parameter vector w⇀k . w⇀k+1=w⇀k+μθkφk
8. Stop if the error is small enough, else set k = k + 1 and repeat steps 4–8.

Selecting the step-size μ is important with the LMS algorithm, because the selection of the
 step-size μ directly affects the rate of convergence and the stability of the algorithm.
 The convergence rate of the LMS algorithm is usually proportional to the step-size μ.
 The larger the step-size μ, the faster the convergence rate. However, a large step-size
 μ can cause the LMS algorithm to become unstable. The following equation describes the
 range of the step-size μ.

0 < μ < μ
 <sub>max</sub>

μ <sub>max</sub> is the maximum step-size that maintains stability in the LMS algorithm. μ
 <sub>max</sub> is related to the statistical property of the stimulus signal. A
 uniformly optimized step-size μ that achieves a fast convergence speed while maintaining
 the stability in the system does not exist, regardless of the statistical property of
 the stimulus signal. For better performance, use a self-adjustable step-size μ and the
 Normalized Least Mean Squares (NLMS) algorithm.

Parent topic:

Recursive Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=least-squares-method-advanced-signal-processi.html language=enus -->
## TOPIC 00084: Least Squares Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `least-squares-method-advanced-signal-processi.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/least-squares-method-advanced-signal-processi.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Least Squares instance of the SI Estimate Impulse Response VI implements the least squares method to obtain the value of h(k).If both the input signal u(k) and output signal y(k) of a system are available, you can obtain the value of the impulse response h(k). This method does not require a Dira

### Least Squares Method

The Least Squares instance of the SI Estimate Impulse Response VI
 implements the least squares method to obtain the value of
 h(k).

If both the input signal u(k) and output signal
 y(k) of a system are available, you can obtain
 the value of the impulse response h(k). This
 method does not require a Dirac delta function as the input signal of the system.
 Instead, you can use a common stimulus signal and the corresponding response signal from
 the system to compute the impulse response mathematically. You can obtain the impulse
 response for both positive and negative lags.

Refer to the *LabVIEW System Identification VIs Algorithm References* section for more
 information about the least squares method.

Parent topic:

Impulse Response

Related concepts:

- Choose a Stimulus Signal

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=linear-time-frequency-analysis.html language=enus -->
## TOPIC 00085: Linear Time Frequency Analysis Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `linear-time-frequency-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/linear-time-frequency-analysis.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW Time Frequency Analysis Tools allows for Short-time Fourier Transforms, Gabor Transforms, and Adaptive Transforms.In traditional spectral analysis, the discrete Fourier transform and the inverse discrete Fourier transform are complementary operations. The discrete Fourier transform computes

### Linear Time Frequency Analysis Methods

LabVIEW Time Frequency Analysis Tools allows for Short-time Fourier Transforms, Gabor
 Transforms, and Adaptive Transforms.

In traditional spectral analysis, the discrete Fourier transform and the inverse discrete Fourier
 transform are complementary operations. The discrete Fourier transform computes a
 frequency-domain representation of time-domain signals. The inverse discrete Fourier
 transform converts the frequency-domain representation back to the time-domain
 representation.

Similarly, the discrete Gabor transform is a linear time-frequency analysis method that computes
 a linear time-frequency representation of time-domain signals. The discrete Gabor
 expansion is the inverse operation and converts the linear time-frequency representation
 back to the time-domain representation.

A linear time-frequency representation of a signal reveals not only the spectral content of the
 signal but also how the spectral content evolves over time. In many real-world
 applications, the signature of a signal and associated noise might not be obvious in the
 time domain or in the frequency domain alone but might be identified easily in the
 time-frequency domain. Also, because linear time-frequency domain representations are
 invertible, you can separate signal components or reduce noise in the time-frequency
 domain and then reconstruct the time-domain signal with the modified time-frequency
 representation. The reconstructed signal contains the signal components you want or the
 signal with the noise reduced.

The linear time-frequency analysis method you select depends on the requirements of the
 application. Consider the resolution and if the method is invertible when you select a
 linear time-frequency analysis method. The following table compares these properties of
 the linear time-frequency analysis methods in the LabVIEW Time Frequency Analysis
 Tools.

| Method | Resolution | Invertible? |
| --- | --- | --- |
| Short-Time Fourier Transform (STFT) | Affected by window type, window length | No |
| Gabor transform | Affected by window type, window length | Yes, using Gabor expansion |
| Adaptive transform | Adaptable to signal | Yes, using Adaptive expansion |

- [Short-Time Fourier Transform](short-time-fourier-transform.html)
- [Discrete Gabor Transform and Expansion](discrete-gabor-transform-and-expansion.html)
- [Adaptive Transform and Expansion](adaptive-transform-and-expansion.html)

Parent topic:

Time Frequency Analysis Concepts

Related concepts:

- Overview of LabVIEW Time Frequency Analysis Tools

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=lv-advanced-signal-processing-toolkit.html language=enus -->
## TOPIC 00086: LabVIEW Advanced Signal Processing Toolkit Concepts

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `lv-advanced-signal-processing-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/lv-advanced-signal-processing-toolkit.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To extract the underlying information of a signal effectively, you need to choose an appropriate analysis tool. The following table describes the tasks you can perform by using the different advanced signal processing tools. 1 Advanced Signal Processing Tool Capabilities Signal Type Tool Task Evolut

### LabVIEW Advanced Signal Processing Toolkit
 Concepts

To extract the underlying information of a signal effectively, you need to choose an appropriate
 analysis tool. The following table describes the tasks you can perform by using the
 different advanced signal processing tools.

| Signal Type | Tool | Task |
| --- | --- | --- |
| Evolutionary | Time Frequency Analysis Tools | The Time Frequency Analysis Tools provide VIs and Express VIs for linear and quadratic time-frequency analysis methods, including the linear discrete Gabor transform and expansion, the linear adaptive transform and expansion, the quadratic Gabor spectrogram, and the quadratic adaptive spectrogram. The Time Frequency Analysis Tools also include VIs to extract features from a signal, such as the mean instantaneous frequency, the mean instantaneous bandwidth, the group delay, and the marginal integration. |
| Stationary | Time Series Analysis Tools | The Time Series Analysis Tools provide VIs for preprocessing signals, estimating the statistical parameters of signals, building models of signals, and estimating the power spectrum, the high-order power spectrum, and the cepstrum of signals. |
| Evolutionary and transient | Wavelet Analysis Tools | The Wavelet Analysis Tools provide VIs and Express VIs for continuous wavelet transform, discrete wavelet transform, undecimated wavelet transform, integer wavelet transform, and wavelet packet decomposition. The Wavelet Analysis Tools also include VIs for feature extraction applications, such as denoising, detrending, and detecting peaks and edges. |

System Identification

Note

Related concepts:

- Categorize Signals

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=model-based-control-design-process-advanced-s.html language=enus -->
## TOPIC 00087: Model-Based Control Design Process

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `model-based-control-design-process-advanced-s.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/model-based-control-design-process-advanced-s.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The model-based control design process involves building a model of a plant, analyzing and synthesizing a controller for the plant, simulating the plant and controller, and deploying the controller.NI provides a complete solution for identifying and validating a plant model, designing a controller f

### Model-Based Control Design Process

The model-based control design process involves building a model of a plant,
 analyzing and synthesizing a controller for the plant, simulating the
 plant and controller, and deploying the controller.

NI provides a complete solution for identifying and validating a plant model, designing a
 controller for the model, analyzing the controller, and prototyping and
 deploying the control system. The following figure shows this process, which
 is based on LabVIEW and National Instruments Real-Time (RT) Series
 hardware:

Figure 150.

[IMAGE alt='image' src='GUID-C1F7999C-131A-4F86-8869-F497E14AD9C2-a5.gif']

#### Analyzing Data and
 Creating a Plant Model

In the initial phase of the design
 process, you must obtain a mathematical model of the plant you want
 to control. One way to obtain a model is by using a numerical
 process known as system identification. This process involves
 acquiring data from a plant and then numerically analyzing stimulus
 and response data to estimate the parameters of the plant.

NI
 provides DAQ and modular instrumentation software and hardware that
 you can use to stimulate and measure the response of the plant. You
 then can use the System Identification VIs to
 estimate and create accurate mathematical models of the
 plant.

System identification is a process that includes
 acquiring and preprocessing raw data from a dynamic system and
 identifying mathematical models based on the raw data. You then
 validate that the resulting model accurately describes the observed
 system behavior. If the results are unsatisfactory, you revise the
 parameters and iterate through the process. The following flowchart
 shows a typical system identification process:

Figure 151.

[IMAGE alt='image' src='GUID-9CA70E39-F222-4B92-AD37-92CDD40CE0B9-a5.gif']

A real-world system seldom has one model that perfectly describes all
 the observed behaviors of the system. Because system identification
 involves many variables — such as sampling frequency, type of
 mathematical model, model order, and so on — you usually have a
 number of models you can use. Each model describes the behavior of
 the system to some extent or in a particular mode of
 operation.

Furthermore, multiple applicable algorithms might
 be available for the same model. The algorithms you select depend on
 the model structure, stochastic assumptions, and numerical
 properties of the algorithm. The System
 Identification VIs include different adaptive
 techniques for recursive system identification and different
 algorithms for model estimation.

#### Designing a
 Controller

In the second phase of the design process, you
 synthesize and analyze a controller. The LabVIEW Control Design and
 Simulation Module provides a set of VIs for classical and modern
 linear control analysis and design techniques. With these VIs you
 can design, implement, and deploy Linear Time-Invariant (LTI) system
 models.

You can use the Control Design and Simulation
 Module to analyze the plant model you identified
 with the System Identification VIs. The
 Control Design and Simulation VIs help
 you determine an appropriate controller structure. You then can
 synthesize a controller to achieve the desired performance criteria
 of the system based on the dynamic behavior of the plant and/or
 control system. Finally, you can analyze the overall system by
 combining the controller with the identified plant
 model.

#### Simulating the
 Plant

In the third phase of the design process, you
 simulate the plant. You can simulate plants in LabVIEW by using the
 Control Design and Simulation Module. You
 can use this software to perform offline simulations of a linear or
 nonlinear plant model. You can use this simulation to investigate
 the time and frequency responses of the plant due to complex,
 time-varying inputs. If you install the LabVIEW Real-Time
 Module, you also can perform Rapid Control
 Prototyping (RCP), and Hardware-In-the-Loop (HIL) simulations by
 using NI RT Series hardware.

#### Deploying the
 Controller

The last stage of the design process is to
 deploy the controller to an RT target, such as a PXI or CompactRIO
 controller. LabVIEW, the Control Design and Simulation
 Module, the Real-Time Module,
 and NI RT Series hardware provide a common platform that you can use
 to design, prototype, and deploy the embedded control system. You
 also can use the Control Design and Simulation
 Module and the Real-Time Module
 as the platform for implementing the control system.

NI also
 provides products for I/O and signal conditioning, such as NI DAQ
 and SCXI devices, that you can use to gather and process data. Using
 these tools, which are built on the LabVIEW platform, you can
 experiment with different approaches at each stage in the design
 process and quickly identify the optimal design solution for an
 embedded control system.

Parent topic:

Introduction to System Identification

Related concepts:

- Acquire Data from a System
- Preprocess Data from a System
- Estimate Models
- Validate Models
- Recursive Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=model-based-methods.html language=enus -->
## TOPIC 00088: Model-Based Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `model-based-methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/model-based-methods.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Model-based methods assume that a time series is the response from a linear system stimulated by white noise. Correspondingly, the Power Spectral Density (PSD) of the response time series is the Frequency Response Function (FRF) of the linear system.In the following figure, white noise e[t] is the s

### Model-Based Methods

Model-based methods assume that a time series is the response from a linear
 system stimulated by white noise. Correspondingly, the Power Spectral
 Density (PSD) of the response time series is the Frequency Response Function
 (FRF) of the linear system.

In the following figure, white noise e<sub>t</sub> is the stimulus, H(z) is
 the linear system, and x<sub>t</sub> is the response time series:

[IMAGE alt='image' src='GUID-40D6FC31-0550-4491-B6B7-4ED668828196-a5.gif']

In general, you can describe a linear system H(z) with an AR, MA, or ARMA
 model. To create such a model for a time series, you can estimate the model coefficients
 first and then use the estimated model coefficients to compute the PSD of the time
 series. For example, the PSD based on an ARMA model is computed by the following
 equation:

P

S

D

f

=

σ

2

F

F

T

b

k

F

F

T

a

k

×

1

∆

f

- σ 2 is the noise variance of the estimated ARMA model of a
 time series
- a k is the AR coefficients of the ARMA model that define the
 poles of the model
- b k is the MA coefficients of the ARMA model that define the
 zeros of the model
- Δ f is the frequency interval of the PSD

The AR and MA models are the subsets of the ARMA model, so you also can compute the PSD of a time
 series based on the AR or MA model from the previous equation by setting the
 corresponding model coefficients a<sub>k</sub> or b<sub>k</sub> to zero.

Use the TSA AR Spectrum VI and the TSA ARMA Spectrum VI to
 compute the PSD of a time series with model-based methods.

The PSD based on each model has specific characteristics. The following figure shows an AR
 model-based PSD for a signal from a system with two pairs of poles, which cause the
 peaks in the PSD at about 0.17 and 0.21 Hz, and one pair of zeros, which cause the
 valley in the PSD at about 0.25 Hz. In the following figure, the AR model gives a good
 estimation for peaks and a poor estimation for valleys in the PSD:

Figure 90.

[IMAGE alt='image' src='GUID-09163E1C-A83F-436E-816F-987858D0FCF1-a5.gif']

The following figure shows an MA model-based PSD, which gives a good estimation for valleys and a
 poor estimation for peaks:

Figure 91.

[IMAGE alt='image' src='GUID-5B08A042-E4F2-4B91-B18C-3F5EACE8FE7C-a5.gif']

The following figure shows an ARMA model-based PSD, which gives the best overall estimation:

Figure 92.

[IMAGE alt='image' src='GUID-F6172096-0007-4F83-AF8D-476861B08A3E-a5.gif']

In parametric modeling applications, you usually use the AR model-based method instead of the MA
 or ARMA methods to estimate the PSD of a time series, because this method
 computes the model coefficients through a linear equation. For real-valued
 time series, the AR model order is set to at least twice the number of
 frequency peaks that you want to analyze. The estimated PSD shows more
 details about the frequency peaks with a large AR model order; however, a
 much higher AR model order can lead to spurious peaks in the resulting
 PSD.

Parent topic:

Power Spectrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=model-types-and-representations-advanced-sign.html language=enus -->
## TOPIC 00089: Model Types and Representations

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `model-types-and-representations-advanced-sign.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/model-types-and-representations-advanced-sign.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can represent a dynamic system using several types of dynamic system models. Model TypesYou base the type of a dynamic system model on the properties of the dynamic system that the model represents.Linear versus Nonlinear Models Dynamic system models are either linear or nonlinear. A linear mode

### Model Types and Representations

You can represent a dynamic system using several types of dynamic system models.

#### Model Types

You base the type of a dynamic system model on the properties of the dynamic system that the model represents.

#### Linear versus Nonlinear
 Models

Dynamic system models are either linear or nonlinear. A linear
 model obeys the principles of superposition and homogeneity. The following equations
 are true for linear models:

y<sub>1</sub> =
 f(u<sub>1</sub>)

y<sub>2</sub>
 =
 f(u<sub>2</sub>)

f(u<sub>1</sub>
 + u<sub>2</sub>) =
 f(u<sub>1</sub>) +
 f(u<sub>2</sub>) =
 y<sub>1</sub> +
 y<sub>2</sub>

f(au<sub>1</sub>)
 = af(u<sub>1</sub>) =
 ay<sub>1</sub>

where

- u 1 and u 2 are the
 system inputs
- y 1 and y 2 are the
 system outputs
- a is a constant

Conversely, nonlinear models do not obey the principles of superposition or
 homogeneity. Nonlinear effects in real-world systems include saturation, dead-zone,
 friction, backlash, and quantization effects; relays; switches; and rate limiters.
 Many real-world systems are nonlinear, but you can simulate most real-world systems
 with linear models to simplify a design or analysis procedure.

#### Time-Variant versus Time-Invariant
 Models

Dynamic system models are either time-variant or time-invariant. The parameters of a
 time-variant model change with time. For example, you can use a time-variant model
 to describe an automobile. As fuel burns, the mass of the vehicle changes with
 time.

Conversely, the parameters of a time-invariant model do not change with time. For an
 example of a time-invariant model, consider a simple robot. Generally, the dynamic
 characteristics of robots do not change over short periods of time.

#### Continuous versus Discrete Models

Dynamic system models are either continuous or discrete. Both continuous and discrete system models can be linear or nonlinear and time-invariant or time-variant. Continuous models describe how the behavior of a system varies continuously with time, which means you can obtain the properties of a system at any certain moment from the continuous model. Discrete models describe the behavior of a system at separate time instants, which means you cannot obtain the behavior of the system between every two sampling points.

Continuous system models are analog. You derive continuous models of a physical system from differential equations of the system. The coefficients of continuous models have clear physical meanings. For example, you can derive the continuous transfer function of an RC circuit if you know the details of the circuit. The coefficients of the continuous transfer function are the functions of R and C in the circuit. You use continuous models if you need to match the coefficients of a model to some physical components in the system.

Discrete system models are digital. You derive discrete models of a physical system from difference equations or by converting continuous models to discrete models. In computer-based applications, signals and operations are digital. Thus, you can use discrete models to implement a digital controller or to simulate the behavior of a physical system at discrete instants. You also can use discrete models in the accurate model-based design of a discrete controller for a dynamic system.

#### SISO, SIMO, MISO, and MIMO
 Models

Dynamic system models contain different numbers of inputs and
 outputs. You can classify dynamic system models into the following types by the
 input and output numbers of the dynamic system that the model represents:

- Single-Input Single-Output (SISO) Models
- Single-Input Multiple-Output (SIMO) Models
- Multiple-Input Single-Output (MISO) Models
- Multiple-Input Single-Output (MIMO) Models

The System Identification VIs include VIs with different
 polymorphic instances of VIs for these types of models. Use the corresponding
 polymorphic instances of VIs to estimate these types of models. You can use the MIMO
 instances of System Identification VIs to estimate MISO, SIMO,
 and SISO models by adding an empty dimension to the input signals, output signals,
 or both signals of the dynamic system.

#### Model Representations

You
 can use the System Identification VIs to represent each model
 type in any of the following representations:

- Transfer function models
- Zero-pole-gain models
- State-space models

If the model is discrete, you also can use a general-linear polynomial
 model.

Parent topic:

Introduction to System Identification

Related concepts:

- Transfer Function Model Definitions
- Zero-Pole-Gain Model Definitions
- State-Space Model Definitions
- General-Linear Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=multiresolution-analysis.html language=enus -->
## TOPIC 00090: Multiresolution Analysis

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `multiresolution-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/multiresolution-analysis.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Discrete Wavelet Transform (DWT) is well-suited for multiresolution analysis.The DWT decomposes high-frequency components of a signal with fine time resolution but coarse frequency resolution and decomposes low-frequency components with fine frequency resolution but coarse time resolution.The fo

### Multiresolution Analysis

The Discrete Wavelet Transform (DWT) is well-suited for multiresolution
 analysis.

The DWT decomposes high-frequency components of a signal with fine time resolution but coarse
 frequency resolution and decomposes low-frequency components with fine
 frequency resolution but coarse time resolution.

The following figure shows the frequency bands of the DWT for the db08 wavelet:

Figure 127.

[IMAGE alt='image' src='GUID-CB7AA5AA-3136-4202-A9BB-55D859642973-a5.gif']

You can see that the central frequency and frequency bandwidth of the detail coefficients
 decrease by half when the decomposition level increases by one. For example,
 the central frequency and frequency bandwidth of
 D<sub>2</sub> are half that of
 D<sub>1</sub>. You also can see that the
 approximation at a certain resolution contains all of the information about
 the signal at any coarser resolutions. For example, the frequency band of
 A<sub>2</sub> covers the frequency bands of
 A<sub>3</sub> and
 D<sub>3</sub>.

DWT-based multiresolution analysis helps you better understand a signal and is useful in feature
 extraction applications, such as peak detection and edge detection.
 Multiresolution analysis also can help you remove unwanted components in the
 signal, such as noise and trend.

The following figure shows the multiresolution results for a signal using the DWT:

Figure 128.

[IMAGE alt='image' src='GUID-5F806728-4FFE-4563-9DEE-AC46A00BB9CA-a5.gif']

You can see that the approximation at level 1 is the summation of the approximation and detail at level 2. The approximation at level 2 is the summation of the approximation and detail at level 3. As the level increases, you obtain lower frequency components, or large-scale approximation and detail, of the signal.

Use the Multiresolution Analysis Express VI to decompose and reconstruct a
 signal at different levels and with different wavelet types.

Parent topic:

Discrete Wavelet Transform

Related concepts:

- Discrete Wavelet Transform

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=multivariate-statistical-values.html language=enus -->
## TOPIC 00091: Multivariate Statistical Values

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `multivariate-statistical-values.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/multivariate-statistical-values.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multivariate statistical analysis methods enable you to investigate statistical interdependence between variables in a multivariate time series.These methods also help you perform blind source separation or eliminate redundant or extraneous variables in a multivariate time series. You also can use t

### Multivariate Statistical Values

Multivariate statistical analysis methods enable you to investigate statistical
 interdependence between variables in a multivariate time series.

These methods also help you perform blind source separation or eliminate redundant or extraneous
 variables in a multivariate time series. You also can use these methods to transform a
 multivariate time series so that information can be concentrated in a smaller number of
 variables, which enable you to reduce the dimensionality of multivariate time
 series.

#### Understanding the Covariance
 Matrix

Covariance matrices measure the correlation between two or more
 time series acquired during the same period. In a unified covariance matrix or
 correlation-coefficient matrix, the diagonal values all have a value of one because
 all signals are correlated with themselves perfectly. Nondiagonal values close to
 one indicate that the corresponding variables are highly correlated.

Use the
 TSA Covariance VI to compute the covariance matrix and
 unified covariance matrix for multivariate time series.

#### Understanding Principal Component
 Analysis

The main purpose of Principal Components Analysis (PCA) is to
 enable you to isolate and remove extraneous or redundant variables in a multivariate
 time series. Extraneous and redundant variables increase the dimensionality of a
 time series and prevent you from finding important underlying patterns in the data.
 With the PCA method, you can reduce the dimensionality of a time series and retain
 as much information as possible. You also can make underlying patterns in the data
 more explicit and easier to find. PCA is useful in applications such as pattern
 recognition and image compression.

The following figure shows a simulated
 multivariate time series that contains two variables. These two variables are
 uncorrelated with each other.

Figure 69.

[IMAGE alt='image' src='GUID-7426244D-122C-40AE-94EE-D3DF4C00B096-a5.gif']

The following figure shows the correlation and unified covariance matrix of the
 two variables. The Correlation graph is an XY graph that uses
 Variable 1 as x-axis and Variable
 2 as y-axis. Variable 1 and
 Variable 2 are uncorrelated with each other because the
 data points spread across the XY graph irregularly. The nondiagonal elements in the
 unified Covariance Matrix are close to zero, so the two
 variables are uncorrelated.

Figure 70.

[IMAGE alt='image' src='GUID-E66A3401-6FFB-45C2-88B5-93EF664D4426-a5.gif']

The following figure shows a simulated multivariate time series that contains two
 variables. These two variables are correlated with each other.

Figure 71.

[IMAGE alt='image' src='GUID-21FE6DF9-533A-45C7-A956-70B02B54851F-a5.gif']

The following figure shows the correlation and unified covariance matrix of the
 two variables. In the Correlation graph, Variable
 1 and Variable 2 increase together. The
 nondiagonal elements in the unified Covariance Matrix are
 close to one, so the two variables are highly correlated.

Figure 72.

[IMAGE alt='image' src='GUID-93F333FC-27E7-46CD-8592-38099FA1EB6B-a5.gif']

PCA transforms correlated time series into uncorrelated time series. In the case
 of a two-variable time series, the first principal component is the line along the
 direction that has maximum variance. The second principal component is the line
 along the direction that has second largest variance and is perpendicular to the
 first principal component. In the previous figure, the red and blue lines represent
 the first principal component and the second principal component, respectively. The
 two lines form a new coordinate system. PCA rotates the original coordinate system
 to the new coordinate system and reduces the correlation between variables,
 potentially enabling you to eliminate the component with the lower variance if you
 judge the variance to be negligible in the application.

The following figure
 shows the correlation plot and unified covariance matrix of the resulting time
 series from PCA:

Figure 73.

[IMAGE alt='image' src='GUID-C7D251A4-80BC-4524-B63E-190FB177FB18-a5.gif']

PCA is not limited to two-variable time series. When the number of variables is
 greater than two, the eigenvectors of the correlation matrix are principal
 components. PCA reorders the eigenvectors based on the corresponding eigenvalues and
 projects the original time series on the eigenvectors. Principal component scores
 describe the projection results of the time series on the new coordinate system.
 Principal component scores are the linear combination of variables in the original
 time series.

The following figure is an example that uses PCA for image
 compression. The following figure shows an x-ray image. You can consider each row of
 the image as a time series and the whole image as a multivariate time series.

Figure 74.

[IMAGE alt='image' src='GUID-B8BC070C-C315-4E41-B28D-A7A301FC6B8E-a5.gif']

You can check the correlation between each row of the image by computing the
 unified covariance matrix. The following figure shows part of the unified covariance
 matrix for the image in the previous figure. The nondiagonal elements are close to
 one. Therefore, strong correlation exists among some of the rows of the image. You
 can reduce the correlation by performing PCA on the original image.

Figure 75.

[IMAGE alt='image' src='GUID-3E4437A4-2BFA-47B4-AC7F-0CC80BE3880A-a5.gif']

The following figure shows the PCA result of the image. The variance of each row
 decreases as the row index increase. The rows contain less significance as the row
 index increases. Deciding which rows are significant or useful is a matter of
 judgment, but a reasonable threshold is at row 50. If you keep only the first 50
 rows, you can reduce the data dimensionality and corresponding image size in bits
 while retaining important information in the image.

Figure 76.

[IMAGE alt='image' src='GUID-74C4EFC4-FBA9-4168-B4C0-76B6AFC58278-a5.gif']

The following figure shows the reconstructed image with the principal component
 scores of only the first 50 principal components. You can see that the reconstructed
 image properly retains the major features of the original image.

Figure 77.

[IMAGE alt='image' src='GUID-FC914FCA-B7B7-44AD-ABD9-33FDFC1BEA32-a5.gif']

Use the TSA Principal Component Analysis VI to perform PCA on
 multivariate time series.

Note

#### Understanding Independent Component
 Analysis

Independent Component Analysis (ICA) generates a multivariate
 time series with statistically-independent components from an original multivariate
 time series with statistically-dependent components. ICA is a generalization of PCA.
 ICA removes not only the second-order statistical dependency but also high-order
 statistical dependencies between the variables of a multivariate time series.
 However, PCA removes only the second-order statistical dependency between the
 variables.

One typical application of ICA is blind source separation, or
 revealing independent sources from sensor observations that are unknown linear
 mixtures of the unobserved source signals. The following figure illustrates the
 flowchart of blind source separation:

Figure 78.

[IMAGE alt='image' src='GUID-78E13017-7724-4702-A3CC-CAACB5D7350F-a5.gif']

In the previous figure, the observed signals are the linear mixtures of a set of
 unknown independent source signals. ICA estimates the source signals and the mixing
 matrix with only the observed signals. The estimated source signals are called
 independent components because they are statistically independent of each
 other.

For example, the Electroencephalogram (EEG) data are recordings of
 electrical potentials at many different locations on a human scalp. These electrical
 potentials are the mixtures of signals generated by brain activities. ICA can help
 you recover the components of brain activities and reveal underlying information
 about those activities.

Another application of ICA is removing artifacts from
 signals. For example, in biomedical signal analysis, the Magnetoencephalography
 (MEG) signals from a human brain usually contain artifacts such as eye movements,
 heartbeats, and measurement noise. You can use ICA to remove the artifacts and
 enhance the MEG signals. Using ICA to remove artifacts usually involves the
 following steps:

1. Compute the separating matrix, that is, the inverse of the mixing matrix, and
 obtain the independent components.
2. Remove undesirable independent components by setting their values to zeros.
3. Reconstruct signals from independent components with the mixing matrix.

You also can use ICA in the applications of feature extraction and data mining
 because ICA can make the features more explicit in the resulting independent
 components.

Use the TSA Independent Component Analysis VI
 to perform ICA on multivariate time series.

Parent topic:

Perform Statistical Analysis

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=nonparametric-model-estimation-methods-advanc.html language=enus -->
## TOPIC 00092: Nonparametric Model Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `nonparametric-model-estimation-methods-advanc.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/nonparametric-model-estimation-methods-advanc.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Nonparametric model estimation is more efficient, but often less accurate, than parametric estimation. However, you can use a nonparametric model estimation method to obtain useful information about a system before applying parametric model estimation.You can describe linear time-invariant models wi

### Nonparametric Model Estimation Methods

Nonparametric model estimation is more efficient, but often less accurate, than
 parametric estimation. However, you can use a nonparametric model estimation method to
 obtain useful information about a system before applying parametric model
 estimation.

You can describe linear time-invariant models with transfer functions or by using the impulse
 response or frequency response of the system. The impulse response and frequency
 response are two ways of estimating a nonparametric model. The impulse response reveals
 the time-domain properties of the system, such as time delay and damping. The frequency
 response reveals the frequency-domain properties, such as the natural frequency of the
 system.

For example, you can use nonparametric model estimation to determine whether the system requires
 preconditioning, what the time delay of the system is, what model order to select, and
 so on. You also can use nonparametric model estimation to verify parametric models. For
 example, you can compare the Bode plot of a parametric model with the frequency response
 of the nonparametric model.

You can use the least squares and correlation analysis methods to estimate the impulse response
 of a dynamic system. You can use the spectral analysis method to estimate the frequency
 response of a dynamic system.

- [Impulse Response](impulse-response-advanced-signal-processing-t.html)
- [Frequency Response](frequency-response-advanced-signal-processing.html)

Parent topic:

Estimate Models

Related concepts:

- Model Types and Representations
- Parametric Model Estimation Methods
- Analyze Models
- Spectral Analysis Method

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=normalized-least-mean-squares-advanced-signal.html language=enus -->
## TOPIC 00093: Normalized Least Mean Squares

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `normalized-least-mean-squares-advanced-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/normalized-least-mean-squares-advanced-signal.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The procedure of the Normalized Least Mean Squares (NLMS) algorithm is the same as the LMS algorithm except for the estimation of the time-varying step-size μ(k).The following equation defines a popular self-adjustable step-size μ(k) that you use in the NLMS algorithm:μk=με+φ⇀k2φ⇀k represents the da

### Normalized Least Mean Squares

The procedure of the Normalized Least Mean Squares (NLMS) algorithm is the same as the
 LMS algorithm except for the estimation of the time-varying step-size
 μ(k).

The following equation defines a popular self-adjustable step-size μ(k) that
 you use in the NLMS algorithm:

μ

k

=

μ

ε

+

φ

⇀

k

2

φ⇀k represents the data vector. ε is a very small positive
 number that prevents the denominator from equaling zero when φ⇀k2<sup>2</sup> approaches zero.

The step-size μ(k) is time-varying because the step-size changes with
 the time index k.

Substituting μ(k) into the parametric vector w⇀k equation yields the following equation:

w

⇀

k

+

1

=

w

⇀

k

+

μ

k

e

k

φ

k

Compared to the Least Mean Squares (LMS) algorithm, the NLMS algorithm is always stable if the
 step-size μ(k) is between zero and two, regardless of the statistical
 property of the stimulus signal u(k).

Parent topic:

Recursive Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=other-cohen-s-class-time-frequency-distributi.html language=enus -->
## TOPIC 00094: Other Cohen's Class Time Frequency Distributions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `other-cohen-s-class-time-frequency-distributi.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/other-cohen-s-class-time-frequency-distributi.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Time Frequency Analysis Tools also provide two other Cohen's class methods—the Choi-Williams Distribution (CWD) and the Cone-Shaped Distribution (CSD).To understand the other Cohen's class methods, you can start with the ambiguity function, which is equivalent to the 2D inverse Fourier t

### Other Cohen's Class Time Frequency Distributions

The LabVIEW Time Frequency Analysis Tools also provide two other Cohen's class
 methods—the Choi-Williams Distribution (CWD) and the Cone-Shaped
 Distribution (CSD).

To understand the other Cohen's class methods, you can start with the ambiguity function, which
 is equivalent to the 2D inverse Fourier transform of the WVD.

The following figure shows the ambiguity function of the example frequency hopper signal:

Figure 30.

[IMAGE alt='image' src='GUID-05551606-7CCD-4A4F-8DA6-E1C300C92364-a5.gif']

1

In the previous figure, the components located at the origin of the ambiguity function plane are
 associated with the auto-terms of the WVD. All the auto-terms overlap at the origin of
 the ambiguity function plane. The components located away from the origin of the
 ambiguity function plane correspond to the cross-terms of the WVD. Because the
 auto-terms and the cross-terms are separated in the ambiguity function plane, you can
 apply a mask function, also called a kernel function, to keep the auto-terms and remove
 the cross-terms. The kernel function determines how to suppress the cross-terms. By
 selecting the appropriate kernel function, you can reduce the cross-term interference
 and keep some useful properties of the WVD, such as accurate marginal time integration,
 marginal frequency integration, mean instantaneous frequency, and group delay. Lastly,
 you can apply the 2D Fourier transform to the ambiguity function to obtain the smooth
 WVD, also called the Cohen's class time-frequency representation.

The size of the ambiguity function quadratically increases with the length of the input signal. Therefore, large signals require a long computation time and more memory. If you need to analyze large signals, divide the signal into smaller segments and analyze each segment individually.

#### Choi-Williams
 Distribution

The following CWD uses an exponential kernel
 function:

Figure 31.

[IMAGE alt='image' src='GUID-077C4B64-150D-498C-95A6-0D15D929B4B4-a5.gif']

The exponential kernel function has the same dimensions as the
 ambiguity function. The exponential kernel function suppresses the
 cross-terms away from the horizontal axis and the vertical axis.
 Therefore, the CWD reduces the cross-terms generated by two
 auto-terms with different time centers and frequency centers. The
 exponential kernel function does not reduce the values of the
 ambiguity function on the horizontal axis or the vertical axis.
 Therefore, the CWD still possesses the useful properties of the WVD,
 such as accurate marginal time integration, marginal frequency
 integration, mean instantaneous frequency, and group
 delay.

The CWD has a coarser time-frequency resolution than
 the WVD because the CWD also blurs the auto-terms when the CWD
 reduces the cross-terms. Because the exponential kernel function
 does not reduce the values of the ambiguity function on the
 horizontal axis or the vertical axis, the CWD preserves the
 cross-terms on the horizontal axis and the vertical axis. In other
 words, the CWD does not suppress the cross-terms that two auto-terms
 with the same time center or frequency center generate.

Use
 the TFA Choi-Williams Distribution VI to compute
 the CWD.

The following figure shows the CWD of the example
 frequency hopper signal:

Figure 32.

[IMAGE alt='image' src='GUID-8DE33917-D0E6-459F-B0AA-4F10EB873A4C-a5.gif']

1

The exponential kernel function includes an alpha parameter to
 balance the cross-term suppression and the blurriness of auto-terms.
 The larger the value of the alpha parameter, the better the
 cross-term suppression and the more blurry auto-terms become. As
 alpha approaches zero, the CWD converges to the WVD.

#### Cone-Shaped
 Distribution

The following CSD uses the cone-shaped kernel
 function:

Figure 33.

[IMAGE alt='image' src='GUID-6C92D259-C1B5-4CFF-A1D0-0C1B455FF0B9-a5.gif']

The cone-shaped kernel function suppresses the cross-terms away from
 the vertical axis and the origin of the ambiguity function plane.
 Therefore, the CSD suppresses the cross-terms that two auto-terms
 with different time centers and frequency centers generate.
 Additionally, the CSD suppresses the cross-terms that two auto-terms
 with the same frequency center generate.

Use the TFA
 Cone-Shaped Distribution VI to compute the
 CSD.

The following figure shows the CSD of the example
 frequency hopper signal with all cross-terms suppressed:

Figure 34.

[IMAGE alt='image' src='GUID-D80E9CC5-122C-44AB-A8C2-6156154097E8-a5.gif']

The cone-shaped kernel function does not suppress the values of the
 ambiguity function on the horizontal axis. Therefore, the CSD cannot
 reduce cross-terms that two auto-terms with the same time center
 generate. The CSD provides accurate marginal time integration and
 mean instantaneous frequency but does not provide accurate marginal
 frequency integration or group delay because the cone-shaped kernel
 function is not constant on the frequency shift axis.

Similar
 to the exponential kernel function for the CWD, the cone-shaped
 kernel function includes an alpha parameter to balance the
 cross-term suppression and the blurriness of auto-terms. The larger
 the value of the alpha parameter, the better the cross-term
 suppression and the more blurry auto-terms become.

Parent topic:

Quadratic Time Frequency Analysis Methods

Related concepts:

- Overview of LabVIEW Time Frequency Analysis Tools
- Spectrogram Feature Extraction

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=output-error-model-definitions-advanced-signa.html language=enus -->
## TOPIC 00095: Output-Error Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `output-error-model-definitions-advanced-signa.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/output-error-model-definitions-advanced-signa.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When A(z), C(z), and D(z) equal 1, the general-linear polynomial model reduces to the output-error model.This model describes the system dynamics separately from the stochastic dynamics. The output-error model does not use any parameters for simulating the disturbance characteristics.Use the SI Esti

### Output-Error Model Definitions

When A(z),
 C(z), and
 D(z) equal 1, the general-linear polynomial
 model reduces to the output-error model.

This model describes the system dynamics separately from the stochastic dynamics. The
 output-error model does not use any parameters for simulating the disturbance
 characteristics.

Use the SI Estimate OE Model VI to estimate output-error models. The
 identification method of the output-error model is the prediction error method, which is
 the same as that of the ARMAX model. If the disturbance
 e(k) is white noise, all minima are global.
 However, a local minimum can exist if the disturbance is not white noise.

The following equation shows the form of the output-error model:

y

k

=

B

z

F

z

u

k

-

n

+

e

k

where

- y ( k ) represents the system outputs
- u ( k ) represents the system inputs
- n is the system delay
- e ( k ) is the system disturbance

B(z) and F(z)
 are polynomials with respect to the backward shift operator z<sup>–1</sup> and defined by the following equations:

B

z

=

b

0

+

b

1

z

-

1

+

.

.

.

+

b

k

b

z

-

k

b

-

1

F

z

=

1

+

f

1

z

-

1

+

.

.

.

+

f

k

f

z

-

k

f

The following figure depicts the signal flow of an output-error model:

Figure 193.

[IMAGE alt='image' src='GUID-851C3639-3AB6-4AFF-BB84-98EDB298D61F-a5.gif']

where

- u represents the system inputs
- y represents the system outputs
- e is the system disturbance
- ω is the auxiliary variable

#### SISO

The following are the
 time domain equations for the output-error SISO model:

w

k

+

f

1

w

k

-

1

+

.

.

.

+

f

k

f

w

k

-

k

f

=

b

o

u

k

-

n

+

b

1

u

k

-

n

-

1

+

.

.

.

+

b

k

b

-

1

u

k

-

n

-

k

b

+

1

y

k

=

w

k

+

e

k

where

- k f is the F 
 order
- k b is the B 
 order
- n is the system delay
- e ( k ) is the system disturbance
- w is the auxiliary variable

Parent topic:

General-Linear Model Definitions

Related concepts:

- Determining Parameters for the Prediction Error Method

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=overview-of-labview-time-frequency-analysis-t.html language=enus -->
## TOPIC 00096: Overview of LabVIEW Time Frequency Analysis Tools

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `overview-of-labview-time-frequency-analysis-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/overview-of-labview-time-frequency-analysis-t.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Time Frequency Analysis Tools to remove noise from corrupted signals and to analyze nonstationary signals that contain varying spectral content.The LabVIEW Time Frequency Analysis Tools are part of the LabVIEW Advanced Signal Processing Toolkit, which also contains the LabVIEW Wavelet Analys

### Overview of LabVIEW Time Frequency Analysis Tools

Use the Time Frequency Analysis Tools to remove noise from corrupted signals and to
 analyze nonstationary signals that contain varying spectral content.

The LabVIEW Time Frequency Analysis Tools are part of the LabVIEW Advanced Signal Processing
 Toolkit, which also contains the LabVIEW Wavelet Analysis Tools, the LabVIEW Time Series
 Analysis Tools, and the LabVIEW Digital Filter Design Toolkit.

The Time Frequency Analysis Tools include VIs and Express VIs for linear and
 quadratic time frequency analysis methods, including the linear discrete Gabor transform
 and expansion, the linear adaptive transform and expansion, the quadratic Gabor
 spectrogram, and the quadratic adaptive spectrogram.

The Time Frequency Analysis Tools also include VIs to extract features from a signal, such as the
 mean instantaneous frequency, the mean instantaneous bandwidth, the group delay, and the
 marginal integration.

Parent topic:

Time Frequency Analysis Concepts

Related concepts:

- Linear Time Frequency Analysis Methods
- Quadratic Time Frequency Analysis Methods
- Spectrogram Feature Extraction

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=overview-of-labview-time-series-analysis-tool.html language=enus -->
## TOPIC 00097: Overview of LabVIEW Time Series Analysis Tools

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `overview-of-labview-time-series-analysis-tool.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/overview-of-labview-time-series-analysis-tool.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Time Series Analysis Tools provide a collection of VIs that assists you in analyzing scientific and engineering time series and rapidly deploying engineering applications based on the analysis results. You can use these VIs to handle discrete univariate and multivariate (vector) time ser

### Overview of LabVIEW Time Series Analysis Tools

The LabVIEW Time Series Analysis Tools provide a collection of VIs that assists you
 in analyzing scientific and engineering time series and rapidly deploying
 engineering applications based on the analysis results. You can use these VIs to
 handle discrete univariate and multivariate (vector) time series.

#### Time Series Analysis
 Procedure

The following diagram illustrates the procedure that you can follow when using the
 Time Series Analysis Tools to analyze a time series:

Figure 49.

[IMAGE alt='image' src='GUID-26124322-4E13-40D7-9892-32B93A2808FB-a5.gif']

A typical time series analysis procedure includes the following steps:

1. Acquire a discrete time series through NI-DAQ or by loading existing data from a
 file.
2. Preprocess the time series if necessary; for example, you can resample the time
 series using a different time interval, or remove a low-frequency trend from the
 time series.
3. Obtain useful information from the preprocessed time series by selecting
 suitable time series analysis methods.

#### Time Series Analysis
 Methods

The Time Series Analysis Tools categorize time series analysis
 into the following methods:

Statistical analysis methods

Modeling and prediction methods

Correlation and spectral analysis methods

#### Choosing an Appropriate
 Method

Each of the time series analysis methods is classified as either
 time domain or frequency domain. You can select appropriate methods from these two
 classes according to the analysis objective.

All of the statistical analysis
 methods, the modeling and prediction methods, and the correlation methods discussing
 in this help are time-domain methods. You can use the statistical analysis methods
 to investigate the stochastic characteristics of a time series. Stochastic
 characteristics, for example, are helpful in quality controls in manufacturing
 production. If you have two or more related time series, you can analyze them
 jointly using a covariance matrix, PCA, or cross-correlation method to investigate
 their relatedness. ICA can separate independent signals from linearly mixed data.
 The modeling methods help you build parametric behavioral models for time series,
 which help you predict or control future values.

The spectral analysis
 methods are frequency-domain methods. You can use the nonparametric or model-based
 spectral analysis methods to investigate the vibration characteristics of physical
 systems, such as resonance frequencies and harmonic frequencies. Some of the methods
 also support multivariate time series, such as the MUSIC method, which computes the
 common spectral components existing in a multivariate vibration time
 series.

Before applying an analysis method to a time series, you need to
 preprocess the signal. For example, you need to make sure that the signal contains
 no low-frequency trends, that the frequency bandwidth is sufficiently narrow, and
 that the sampling rate is sufficiently high. Use the Preprocessing VIs to preprocess
 a time series.

The Time Series Analysis Tools also provide a group of
 Utilities VIs that you can use to generate time series
 samples, to scale to an engineering unit, to average the power spectrum, or to load
 pre-stored data from a file.

Parent topic:

Time Series Analysis Concepts

Related concepts:

- Acquire a Discrete Time Series
- Preprocess a Discrete Time Series
- Basic Statistical Values
- Multivariate Statistical Values
- Building Models
- Predict Time Series Values
- Perform Correlation and Spectral Analysis

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=overview-of-labview-wavelet-analysis-tools.html language=enus -->
## TOPIC 00098: Overview of LabVIEW Wavelet Analysis Tools

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `overview-of-labview-wavelet-analysis-tools.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/overview-of-labview-wavelet-analysis-tools.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Wavelet Analysis Tools provide a collection of Wavelet Analysis VIs that assist you in processing signals in the LabVIEW environment.You can use the Continuous Wavelet VIs, the Discrete Wavelet VIs, and the Wavelet Packet VIs to perform the continuous wavelet transform, the discrete wave

### Overview of LabVIEW Wavelet Analysis Tools

The LabVIEW Wavelet Analysis Tools provide a collection of Wavelet
 Analysis VIs that assist you in processing signals in the LabVIEW
 environment.

You can use the Continuous Wavelet VIs, the Discrete
 Wavelet VIs, and the Wavelet Packet VIs to perform the
 continuous wavelet transform, the discrete wavelet transform, the undecimated wavelet
 transform, the integer wavelet transform, and the wavelet packet decomposition. You can
 use the Feature Extraction VIs to detrend and denoise a signal. You
 also can use these VIs to detect the peaks and edges of a signal.

The Wavelet Analysis Tools provide a collection of commonly used continuous wavelets, such as
 Mexican Hat, Meyer, and Morlet, and a collection of commonly used discrete wavelets,
 such as the Daubechies, Haar, Coiflet, and biorthogonal wavelets. You also can create a
 discrete wavelet that best matches the signal you analyze by using the Wavelet
 Design Express VI.

The Wavelet Analysis Tools contain Express VIs that provide interfaces for
 signal processing and analysis. These Express VIs enable you to
 specify parameters and settings for an analysis and see the results immediately. For
 example, the Wavelet Denoise Express VI graphs both the original and
 denoised signals. You can see the denoised signal immediately as you select a wavelet,
 specify a threshold, and set other parameters. The Wavelet Analysis Tools also provide
 Express VIs for multiresolution analysis, wavelet design, and
 wavelet packet decomposition.

Parent topic:

Wavelet Analysis Concepts

Related concepts:

- Signal Processing with Discrete Wavelets
- Interactively Designing Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=overview.html language=enus -->
## TOPIC 00099: LabVIEW Advanced Signal Processing Toolkit Overview

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/overview.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Advanced Signal Processing Toolkit includes the LabVIEW Time Frequency Analysis Tools, LabVIEW Time Series Analysis Tools, and LabVIEW Wavelet Analysis Tools. These tools are a suite of high-level signal processing VIs that you can use to perform time frequency, time series, and wavelet

### LabVIEW Advanced Signal Processing
 Toolkit
 Overview

The LabVIEW Advanced Signal Processing Toolkit includes the LabVIEW Time Frequency
 Analysis Tools, LabVIEW Time Series Analysis Tools, and LabVIEW Wavelet Analysis Tools.
 These tools are a suite of high-level signal processing VIs that you can use to perform
 time frequency, time series, and wavelet analysis.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=parametric-model-estimation-methods-advanced.html language=enus -->
## TOPIC 00100: Parametric Model Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `parametric-model-estimation-methods-advanced.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/parametric-model-estimation-methods-advanced.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the representations of parametric models you can develop by using the System Identification VIs.Parametric models describe systems in terms of difference or differential equations, depending on whether a system is represented by a discrete or continuous model. Compared to n

### Parametric Model Estimation Methods

The following table lists the representations of parametric models you can develop by
 using the System Identification VIs.

Parametric models describe systems in terms of difference or differential equations, depending on
 whether a system is represented by a discrete or continuous model. Compared to
 nonparametric models, parametric models might provide a more accurate estimation if you
 have prior knowledge about the system dynamics to determine model orders, time delays,
 and so on.

Each representation supports one or more input-output configurations: Single-Input Single-Output
 (SISO), Multiple-Input Single-Output (MISO), and Multiple-Input Multiple-Output
 (MIMO).

|  | SISO | MISO | MIMO |
| --- | --- | --- | --- |
| General-Linear | X | X |  |
| Autoregressive (AR) | X |  |  |
| Autoregressive with exogenous terms (ARX) | X | X | X |
| Autoregressive moving average with exogenous terms (ARMAX) | X | X |  |
| Box-Jenkins | X | X |  |
| Output-Error | X | X |  |
| Transfer Function | X | X |  |
| Zero-Pole-Gain | X | X |  |
| State-Space | X | X | X |

- [General-Linear Model Definitions](general-linear-model-definitions-advanced-sig.html)
- [Transfer Function Model Definitions](transfer-function-model-definitions-advanced.html)
- [Zero-Pole-Gain Model Definitions](zero-pole-gain-model-definitions-advanced-sig.html)
- [State-Space Model Definitions](state-space-model-definitions-advanced-signal.html)
- [User Defined Model Definitions](user-defined-model-definitions-advanced-signa.html)
- [Compare Polynomial and State-Space Models](compare-polynomial-and-state-space-models-a.html)
- [Determining Parameters for the Prediction Error Method](determining-parameters-for-the-prediction-err.html)

Parent topic:

Estimate Models

Related concepts:

- Model Types and Representations
- Nonparametric Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=part-1-choosing-a-proper-dynamic-system-model.html language=enus -->
## TOPIC 00101: Choosing a Proper Dynamic System Model by Using Physical Modeling

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `part-1-choosing-a-proper-dynamic-system-model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/part-1-choosing-a-proper-dynamic-system-model.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Physical modeling is a common method for sketching a mathematical model that represents a real dynamic system. Physical modeling determines the nature of the model, such as the model order and the number of I/O channels. Use physical modeling to define proper models for dynamic systems.Before you es

### Choosing a Proper Dynamic System Model by
 Using Physical Modeling

Physical modeling is a common method for sketching a mathematical model that represents a
 real dynamic system. Physical modeling determines the nature of the model, such as the
 model order and the number of I/O channels. Use physical modeling to define proper
 models for dynamic systems.

Before you estimate a dynamic system, create a mathematical model that contains unknown
 coefficients. You then use system identification to estimate these coefficients.

The following figure shows an electrical circuit model of a brushed Direct Current (DC)
 servomotor:

Figure 153.

[IMAGE alt='image' src='GUID-6C957215-D062-4302-8381-05F4B2E62C0A-a5.gif']

where

- V is the source voltage of the DC power supply
- R is the resistance of the DC servomotor armature circuit
- L is the inductance of the DC servomotor armature circuit
- i is the circuit armature current
- ω is the shaft speed of the DC servomotor
- T is the torque of the DC servomotor

In this dynamic system, the source voltage, V, is the input and the DC
 servomotor shaft speed, ω, is the output.

According to Faraday's Law of electromagnetic induction, the circuit armature current
 i, motor torque T, motor shaft velocity
 ω, and motor back-EMF voltage e, have the
 following relationship:

T

=

K

t

i

e

=

K

e

ω

where

- K t is an electromotive force constant
- K e is a motor back-EMF constant

You can obtain the following equations by using Newton's Law and Kirchhoff's Law:

J

d

ω

d

t

+

b

ω

=

K

i

i

L

d

i

d

t

+

R

i

=

V

-

K

e

ω

where

- J is the moment of inertia of the rotor
- b is the damping ratio of the mechanical part of the DC
 servomotor

Perform further transforms on these equations to obtain a mathematic model of the dynamic system.
 You can choose one of the four common dynamic system models on the basis of your
 needs.

- Use the continuous-time transfer function model to create a model that you can use with an
 analog Proportional-Integral-Derivative (PID) controller.
- Use the continuous-time state-space model to create a model that you can use with an
 analog state feedback controller.
- Use the discrete-time transfer function model to create a model that you can use
 with a digital PID controller.
- Use the discrete-time state-space model to create a model that you can use with a
 digital state feedback controller.

Note

Parent topic:

Get Started with System Identification

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=part-2-exciting-the-system-and-acquiring-data.html language=enus -->
## TOPIC 00102: Exciting the System and Acquiring Data

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `part-2-exciting-the-system-and-acquiring-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/part-2-exciting-the-system-and-acquiring-data.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you choose a proper dynamic system model, you must acquire the input and output data from the Direct Current (DC) servomotor. You then preprocess and use the data to estimate unknown coefficients of the dynamic system model. You can use an encoder or a DC tachometer to measure the shaft speed

### Exciting the System and Acquiring Data

After you choose a proper dynamic system model, you must acquire the input and output
 data from the Direct Current (DC) servomotor. You then preprocess and use the data to
 estimate unknown coefficients of the dynamic system model. You can use an encoder or a
 DC tachometer to measure the shaft speed of the DC servomotor.

Set up the following experimental circuit to excite the DC servomotor and acquire response
 signals with an encoder:

Figure 154.

[IMAGE alt='image' src='GUID-2410DF0A-98BD-4CEB-A461-8FB7DA19934C-a5.gif']

Set up the following experimental circuit to excite the DC servomotor and acquire response
 signals with a DC tachometer:

Figure 155.

[IMAGE alt='image' src='GUID-F11F97FF-3FE5-4C4E-9597-26AC99057BBF-a5.gif']

Note

You can use the following types of stimulus signals:

Step signals

Swept sine signals

Chirp
 Pattern

Random signals

Periodic Random
 Noise

In this example, you can use any of these three types of stimulus signals to excite the DC
 servomotor.

Alternately, if you do not have the required hardware or a DC servomotor, use the SI
 Data Samples VI to generate the input and output data. This tutorial uses
 the SI Data Samples VI to complete the following parts. If you also
 use this VI to complete the following parts, you can get identical results as the
 results in this tutorial.

Complete the following steps to generate the input and output data by using the SI Data
 Samples VI:

1. Create a blank VI in LabVIEW.
2. Add the SI Data Samples VI to the block diagram of the VI you created. This
 VI generates single-input single-output waveform signals by default.
3. Right-click the data input of this VI and select
 Create»Constant from the shortcut menu to create a
 constant for this input.
4. Ensure the value of this constant is Motor .

You can save this VI and use this VI to complete the following parts of this tutorial.

Parent topic:

Get Started with System Identification

Related concepts:

- Preprocess Data from a System
- Choose a Stimulus Signal
- Model Types and Representations

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=part-3-identifying-dynamic-system-models-adva.html language=enus -->
## TOPIC 00103: Identifying Dynamic System Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `part-3-identifying-dynamic-system-models-adva.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/part-3-identifying-dynamic-system-models-adva.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Model identification, or parameter estimation, is a series of data and signal processing tasks to estimate unknown parameters and coefficients of the dynamic system model.Before you perform model identification, you need to preprocess the acquired raw data to ensure the data is free from external no

### Identifying Dynamic System Models

Model identification, or parameter estimation, is a series of data and signal processing
 tasks to estimate unknown parameters and coefficients of the dynamic system model.

Before you perform model identification, you need to preprocess the acquired raw data to ensure
 the data is free from external noise, scaling problems, outliers, or other corruptions.
 Use the Data Preprocessing VIs to preprocess the data and ensure the
 data accurately reflects the response of the dynamic system.

In this tutorial, the DC servomotor is a simple dynamic system. The acquired raw data is accurate
 enough for model identification. Therefore, you can skip preprocessing the raw data.

With the acquired time-domain data, you can perform model identification on any of the following
 models:

- Continuous-time transfer function model
- Continuous-time state-space model
- Discrete-time transfer function model
- Discrete-time state-space model

You also can convert the time-domain data to frequency-domain data. With the converted
 frequency-domain data, you can identify models by using the Frequency-Domain
 Model Estimation VIs.

- [Identifying Continuous-Time Transfer Function Models](identifying-continuous-time-transfer-function.html)
- [Identifying Continuous-Time State-Space Models](identifying-continuous-time-state-space-model.html)
- [Identifying Discrete-Time Transfer Function Models](identifying-discrete-time-transfer-function-m.html)
- [Identifying Discrete-Time State-Space Models](identifying-discrete-time-state-space-models.html)

Parent topic:

Get Started with System Identification

Related concepts:

- Preprocess Data from a System
- Frequency-Domain Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=part-4-validating-and-analyzing-dynamic-syste.html language=enus -->
## TOPIC 00104: Validating and Analyzing Dynamic System Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `part-4-validating-and-analyzing-dynamic-syste.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/part-4-validating-and-analyzing-dynamic-syste.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After estimating the dynamic system model, perform model validation to test the estimated system model. Model validation verifies whether the model provides an accurate description of the dynamic system.You also can perform model analysis to analyze the dynamic properties of the dynamic system model

### Validating and Analyzing Dynamic System
 Models

After estimating the dynamic system model, perform model validation to test the estimated
 system model. Model validation verifies whether the model provides an accurate
 description of the dynamic system.

You also can perform model analysis to analyze the dynamic properties of the dynamic system
 model.

#### Validating Dynamic System
 Models

Complete the following steps to validate the system model:

1. Add the SI Model Simulation VI to the block diagram of the VI you
 created.
2. Wire the system model out output of the following VIs or
 Express VIs to the system model 
 input of the SI Model Simulation VI.
  - SI Estimate State-Space Model VI
  - SI Estimate Transfer Function Model VI
  - SI Model Estimation Express VI
  - SI Transfer Function Estimation Express VI
3. Wire the stimulus signal output of the SI Data Samples 
 VI to the stimulus signal input of the SI Model
 Simulation VI.
4. Add the Build Array function to the block diagram.
5. Wire the response signal output of the SI Data Samples 
 VI to the element input of this function.
6. Add an input to this function node by resizing the node and wire the
 response output of the SI Model
 Simulation VI to the new element 
 input.
7. Add a Waveform Graph indicator to the front panel. The
 block diagram displays a node of this indicator.
8. Right-click in this Waveform Graph and select
 Properties from the shortcut menu to display the
 Graph Properties: Waveform Graph dialog box.
9. Place a checkmark in the Show graph palette checkbox in the
 Appearance page.
10. Click the OK button to close this dialog box and save the
 configuration.
11. Switch to the block diagram and wire the appended array 
 output of the Build Array function to this indicator. The following figure shows
 the block diagram: Figure 164.Appending Array
 Output to Indicator in the Block Diagram[IMAGE alt='image' src='GUID-E471A2AB-BFBF-4A3D-94A8-204FF00B26A5-a5.gif']
12. Wire all error in and error out terminals on the block diagram.
13. Run this VI to generate the simulated response signal.

To validate the system model, compare the simulated response signal and the acquired
 response signal in the waveform graph. Use the zoom button on the graph palette to
 zoom in on the signals. The following figure shows the resulting waveform graph:

Figure 165.

[IMAGE alt='image' src='GUID-C7BE8F38-6C3F-48A9-A80C-C96CA055E8B0-a5.gif']

Because of the friction of the DC servomotor in the start-up stage, the acquired
 response signals and the simulated signals deviate at the beginning of the two
 signals. The later parts of the simulated response signals and the acquired response
 signals match each other. Therefore, this dynamic system model provides an accurate
 description of the dynamic system.

#### Analyzing Dynamic System
 Models

Use model analysis to observe the model characteristics, such as
 frequency response.

Complete the following steps to analyze the system
 model:

1. Add the SI Bode Plot VI to the block diagram of the VI you
 created.
2. Wire the system model out output of the following VIs or
 Express VIs to the system model 
 input of the SI Bode Plot VI.
  - SI Estimate State-Space Model VI
  - SI Estimate Transfer Function Model VI
  - SI Model Estimation Express VI
  - SI Transfer Function Estimation Express VI
3. Add an SI Bode Plot Indicator to the front panel. The block
 diagram shows two indicators.
4. Wire the Bode magnitude plot and Bode phase
 plot outputs to the corresponding indicators. The following
 figure shows the block diagram: Figure 166.Wiring Bode
 Magnitude and Phase Plots to Indicators in the Block Diagram
 
 [IMAGE alt='image' src='GUID-4EFDE87E-54E1-499C-B248-48B17DC1BA27-a5.gif']
5. Wire all error in and error out terminals on the block diagram.
6. Run this VI to generate the bode plots of this dynamic system model.

To analyze the system model, read the magnitude and phase information from the
 bode plots. The following figure shows the resulting bode plots:

Figure 167.

[IMAGE alt='image' src='GUID-D759008D-367F-4952-A768-AE53BC2463C5-a5.gif']

In the magnitude plot, the curve remains stable in the low frequency bands and
 falls slowly in the high frequency bands. In the phase plot, the curve falls near
 –90 degrees in the low frequency bands and falls near –180 degrees in the high
 frequency bands. These two plots indicate the following characteristics of this
 dynamic system:

- The order of this dynamic system is two.
- When the frequency is below 1000 Hz, you can treat the order of this dynamic
 system as one.

Use other Model Analysis VIs to analyze other characteristics
 of the dynamic system models, such as the SI Nyquist Plot VI and
 the SI Pole-Zero Plot VI.

Parent topic:

Get Started with System Identification

Related concepts:

- Validate Models
- Analyze Models
- Frequency Response

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=part-5-converting-dynamic-system-models-to-co.html language=enus -->
## TOPIC 00105: Converting Dynamic System Models to Control Design Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `part-5-converting-dynamic-system-models-to-co.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/part-5-converting-dynamic-system-models-to-co.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to design controllers for a dynamic system, you must convert the dynamic system model you identified to a system model that you can use in the LabVIEW Control Design and Simulation Module.For example, you can use the Control Design and Simulation Module to design controllers for this DC

### Converting Dynamic System Models to Control
 Design Models

If you want to design controllers for a dynamic system, you must convert the dynamic
 system model you identified to a system model that you can use in the LabVIEW Control
 Design and Simulation Module.

For example, you can use the Control Design and Simulation Module to design
 controllers for this DC servomotor to control the behaviors of this DC servomotor.

You also can use the Control Design and Simulation Module to complete the
 following tasks:

- Construct plants and control models
- Analyze dynamic system performance
- Simulate dynamic systems with a wide option of solvers
- Deploy dynamic systems to real-time hardware

Complete the following steps to convert a dynamic system model to a control design model:

1. Add the SI Convert to Models of CDT VI to the block diagram of the VI you
 created.
2. Select a proper instance of this polymorphic VI.
3. MIMO TF —Select this instance to convert a transfer function dynamic system
 model.
4. MIMO SS —Select this instance to convert a state-space dynamic system model.
5. Create a constant for the realization type input of the SI
 Convert to Models of CDT VI.
6. Set the realization type constant to full .
7. Wire the system model out output of the following VIs or
 Express VIs to the system model input
 of the SI Convert to Models of CDT VI.
  - SI Estimate State-Space Model VI
  - SI Estimate Transfer Function Model VI
  - SI Model Estimation Express VI
  - SI Transfer Function Estimation Express VI
8. Create an indicator for the transfer function model or
 state-space model output of the SI Convert to
 Models of CDT VI. The following figure shows the block diagram: Figure 168.Indicator for Transfer
 Function or State-Space Model Output in the Block Diagram
 
 [IMAGE alt='image' src='GUID-8710F8A6-A331-458A-9220-807B0B4A5FC1-a5.gif']
9. Wire all error in and error out terminals on the block diagram.
10. Run this VI to convert the dynamic system model.
11. Save the resulting model.

The following figure shows the resulting dynamic system model:

Figure 169.

[IMAGE alt='image' src='GUID-430E11F1-3958-4B38-998D-9513927BF5F8-a5.gif']

Note

Control Design and Simulation Module

Control Design

Functions

Simulation

Parent topic:

Get Started with System Identification

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=partially-known-model-estimation-case-study-a.html language=enus -->
## TOPIC 00106: Partially Known Model Estimation Case Study

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `partially-known-model-estimation-case-study-a.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/partially-known-model-estimation-case-study-a.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This case study gives an example that uses the prior knowledge you have about a system to define and estimate state-space models. You use the same procedure when estimating continuous transfer function models. However, you apply different methods to define continuous transfer function models.The fol

### Partially Known Model Estimation Case
 Study

This case study gives an example that uses the prior knowledge you have about a system to
 define and estimate state-space models. You use the same procedure when estimating
 continuous transfer function models. However, you apply different methods to define
 continuous transfer function models.

The following figure shows an RLC circuit, where u is the input
 voltage, y is the output voltage, i<sub>L</sub> is
 the current, and u<sub>C</sub> is the capacitor voltage. In this
 example, y equals the capacitor voltage
 u<sub>C</sub>.

Figure 231.

[IMAGE alt='image' src='GUID-914F5EA4-8C33-4268-A66A-4AE2D7D1D5A6-a5.gif']

Suppose R is 1.5 Ω and L and C
 are unknown. You can complete the following steps to identify the values of
 L and C.

1. Apply a wide-band voltage to u and measure the output y 
 simultaneously. The Continuous State-Space Model of an RLC Circuit
 example VI uses a chirp signal from 0.5 Hz to 6 Hz as the stimulus
 signal. The response to the chirp signal is the response signal. This example VI
 then preprocesses the stimulus and response signals to remove the offset level in
 these signals.
2. Define a model for this circuit. Because you have information about the approximate
 values of L and C , you can build a partially
 known state-space model or a partially known transfer function model.
3. Estimate the model you defined in step 2 and then estimate L and
 C .

You can use the following first-order differential equation to represent the relationship
 between the capacitor voltage and the current of this RLC circuit:

u

˙

C

=

1

C

i

L

You can use the following first-order differential equation to represent the voltage
 relationship in this RLC circuit:

R

i

L

+

u

C

+

L

i

L

=

u

By manipulating the previous two equations, you can deduce the continuous state-space
 model for this RLC circuit using the following two equations:

u

˙

C

i

L

=

0

1

C

-

1

L

-

R

L

u

˙

C

i

L

+

0

1

L

u

y

=

u

C

=

1

0

u

C

i

L

Use the SI Create Partially Known State-Space Model VI to build the symbolic
 state-space model for this circuit, as shown in the following figure:

Figure 232.

[IMAGE alt='image' src='GUID-6965913C-B5F5-4BAF-BC6A-2E37B259797E-a5.gif']

You specify the symbolic state-space model using formula strings, such as
 1/C, -1/L, and
 -1.5/L, with L and C as
 variables. Then you define L and C with the
 variables input, as shown in the following figure. Using
 prior knowledge, you know that L is a positive value around the
 initial value of 0.1 H, and C is a value between 0 F and 0.3 F.

Figure 233.

[IMAGE alt='image' src='GUID-834E629A-246E-4ACC-AAA9-CEA586D37C8C-a5.gif']

Next, you can estimate the state-space model with the SI Estimate Partially Known
 State-Space Model VI, as shown in the following figure:

Figure 234.

[IMAGE alt='image' src='GUID-119D8073-B912-4E0C-ADE2-13727188E94A-a5.gif']

The SI Estimate Partially Known State-Space Model VI estimates each parameter
 of the model. You obtain the estimated model and optimized variables of the model after
 this VI performs an optimization. In this example, you obtain the values 0.20 H for
 L and 0.02 F for C, as shown in the following
 figure:

Figure 235.

[IMAGE alt='image' src='GUID-E582AEC3-41DF-4703-8EF4-4AFF3C17ADBE-a5.gif']

The Continuous State-Space Model of an RLC Circuit example VI uses the SI Draw
 Model VI and the values of L and C
 you obtain to display the estimated model in a 2D picture control, as shown in the
 following figure:

Figure 236.

[IMAGE alt='image' src='GUID-B347C1C2-A916-48CD-8C78-8FE1E9554DCF-a5.gif']

You then can determine how accurately this model simulates the dynamic system by validating the
 model. Refer to the *System Identification Case Studies* section for an
 example of validating a model.

Parent topic:

System Identification Case Studies

Related concepts:

- State-Space Model Definitions
- Transfer Function Model Definitions
- Validate Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=partially-known-model-estimation-methods-adva.html language=enus -->
## TOPIC 00107: Partially Known Model Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `partially-known-model-estimation-methods-adva.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/partially-known-model-estimation-methods-adva.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Black-box model estimation methods, like the nonparametric and parametric models, assume system unknowns, thus requiring parameter adjustment via trial-and-error to match model behavior to measured data.The nonparametric and parametric model estimation methods, also known as black-box estimation met

### Partially Known Model Estimation
 Methods

Black-box model estimation methods, like the nonparametric and parametric models, assume
 system unknowns, thus requiring parameter adjustment via trial-and-error to match model
 behavior to measured data.

The nonparametric and parametric model estimation methods, also known as black-box estimation
 methods, assume that systems are unknown. Because these estimation methods do not take
 prior system knowledge into account, you must use either an algorithm or trial-and-error
 to vary model parameters until the behavior of the model matches the measured
 input-output data. Although you can use the estimated parameters to reproduce the
 response of the system accurately, these parameters might not have any physical
 meanings.

However, in practice, many systems are partially known because you have information about the
 underlying dynamics or some of the physical parameters. You can use partially known
 model estimation methods, also known as grey-box estimation methods, to estimate models
 when you have this information.

Black-box methods also assume that all model parameters are adjustable. However, in many
 real-world applications, you cannot adjust all the parameters arbitrarily, because the
 parameters might have constraints. For example, in some chemical processes, water must
 flow only in one direction. When estimating the flow rate of water, you know that the
 flow rate cannot be negative. Thus, the constraint is that the flow rate must be a
 positive value. You must consider this constraint and any other constraints when you
 estimate the flow rate of water in this process. Such constraints usually follow one of
 the following guidelines:

- A parameter must be as close to a value as possible.
- A parameter must be between two values.
- Two or more parameters must correlate to each other.

These constraints reflect the knowledge you have of the physical system. This knowledge can
 result in a more realistic parameter estimation. Parameter constraints increase the
 possibility of the System Identification VIs locating the optimal
 parameters that describe the dynamic system model. Parameter constraints also improve
 the accuracy of locating these optimal parameters.

You can set parameter constraints when using grey-box estimation methods, whereas you cannot set
 parameter constraints when using black-box estimation methods. When using these methods,
 you can set only the model order that specifies the number of parameters to
 calculate.

Parent topic:

Estimate Models

Related concepts:

- Nonparametric Model Estimation Methods
- Parametric Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=perform-correlation-and-spectral-analysis.html language=enus -->
## TOPIC 00108: Perform Correlation and Spectral Analysis

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `perform-correlation-and-spectral-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/perform-correlation-and-spectral-analysis.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Time series analysis methods like correlation and spectral analysis allows for the detection of hidden periodicities or frequency characteristics in a time series at specific frequencies.By using the Time Series Analysis VIs, you can detect a periodicity of a time series in either the time domain or

### Perform Correlation and Spectral
 Analysis

Time series analysis methods like correlation and spectral analysis allows for the
 detection of hidden periodicities or frequency characteristics in a time series at
 specific frequencies.

By using the Time Series Analysis VIs, you can detect a periodicity of a time
 series in either the time domain or the frequency domain.

In the time domain, correlation analysis is a classical method that you can use to find periodic
 patterns at a specific frequency in one or more time series. You also can use the
 correlation method to identify or extract other useful features of a time series, such
 as phase.

In the frequency domain, you can use spectral analysis methods to estimate the power spectrum of
 a time series. You also can estimate the bispectrum, which is useful for detecting
 nonlinearities in a time series, and estimate the cepstrum, which is useful for
 deconvolving a time series.

- [Correlation Methods](correlation-methods.html)
- [Bispectrum Estimation Methods](bispectrum-estimation-methods.html)
- [Power Spectrum Estimation Methods](power-spectrum-estimation-methods.html)
- [Cepstrum Estimation Methods](cepstrum-estimation-methods.html)

Parent topic:

Time Series Analysis Concepts

Related concepts:

- Cepstrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=perform-statistical-analysis.html language=enus -->
## TOPIC 00109: Perform Statistical Analysis

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `perform-statistical-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/perform-statistical-analysis.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the statistical analysis methods that the LabVIEW Time Series Analysis Tools provide. You can process both univariate and multivariate time series with these methodsStatistical analysis methods enable you to investigate the stochastic characteristics of a time series. You can

### Perform Statistical Analysis

This section describes the statistical analysis methods that the LabVIEW Time Series
 Analysis Tools provide. You can process both univariate and multivariate time series
 with these methods

Statistical analysis methods enable you to investigate the stochastic characteristics of a time
 series. You can use the computed statistical values to infer some underlying information
 about the associated physical systems. For example, if a machining tolerance error is
 due to a systematic anomaly or random fluctuations. The computed statistical values for
 a time series also help you judge if other analysis techniques, such as modeling, are
 useful in analyzing that time series.

- [Basic Statistical Values](basic-statistical-values.html)
- [Multivariate Statistical Values](multivariate-statistical-values.html)

Parent topic:

Time Series Analysis Concepts

Related concepts:

- Building Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=power-spectrum-estimation-methods.html language=enus -->
## TOPIC 00110: Power Spectrum Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `power-spectrum-estimation-methods.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/power-spectrum-estimation-methods.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A power spectrum describes the energy distribution of a time series in the frequency domain. Methods for estimating power spectral density are classified as either parametric or nonparametric.Energy is a real-valued quantity, so the power spectrum does not contain phase information. Because a time s

### Power Spectrum Estimation Methods

A power spectrum describes the energy distribution of a time series in the frequency
 domain. Methods for estimating power spectral density are classified as either
 parametric or nonparametric.

Energy is a real-valued quantity, so the power spectrum does not contain phase information.
 Because a time series may contain non-periodic or asynchronously-sampled periodic signal
 components, the power spectrum of a time series typically is considered to be a
 continuous function of frequency. When you use a series of discrete frequency bins to
 represent the continuous frequency, the value at a specific frequency bin is
 proportional to the frequency interval. To remove the dependence on the size of the
 frequency interval, you can normalize the power spectrum to produce the Power Spectral
 Density (PSD), which is the power spectrum divided by the size of the frequency
 interval.

The PSD measures the signal power per unit bandwidth for a time series in V<sup>2</sup>/Hz, which
 implicitly assumes that the PSD represents a signal in volts driving a 1 ohm load. If
 the PSD is represented in a decibel (dB), the corresponding unit for the PSD is dB ref
 V/sqrt(Hz). If you want to use other units for the estimated PSD of a time series, you
 need to scale the unit of the time series into appropriate Engineering Units (EU). After
 scaling the unit of the time series, you can obtain the corresponding unit for the
 linear PSD value and the dB PSD value as EU <sup>2</sup>/Hz and dB ref EU/sqrt(Hz),
 respectively. Use the TSA Scale to EU VI to scale the unit for a time
 series to appropriate EU.

PSD estimation methods are classified as follows:

Parametric methods

Nonparametric methods

Note

TSA Average
 PSD

- [Model-Based Methods](model-based-methods.html)
- [The MUSIC Method](the-music-method.html)
- [The Periodogram Method](the-periodogram-method.html)
- [The Welch Method](the-welch-method.html)
- [The Capon Method](the-capon-method.html)

Parent topic:

Perform Correlation and Spectral Analysis

Related concepts:

- Building Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=predict-time-series-values.html language=enus -->
## TOPIC 00111: Predict Time Series Values

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `predict-time-series-values.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/predict-time-series-values.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can predict future values of a time series using the LabVIEW Time Series Analysis Tools, which provides use of either ARMA model-based prediction or exponential smoothing prediction.

### Predict Time Series Values

You can predict future values of a time series using the LabVIEW Time Series
 Analysis Tools, which provides use of either ARMA model-based prediction or
 exponential smoothing prediction.

- [ARMA Model-Based Prediction](arma-model-based-prediction.html)
- [Exponential Smoothing Prediction](exponential-smoothing-prediction.html)

Parent topic:

Time Series Analysis Concepts

Related concepts:

- Building Autoregressive-Moving Average Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=preprocess-a-discrete-time-series.html language=enus -->
## TOPIC 00112: Preprocess a Discrete Time Series

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `preprocess-a-discrete-time-series.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/preprocess-a-discrete-time-series.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Preprocessing helps you make an acquired discrete time series more suitable for further analysis.The LabVIEW Time Series Analysis Tools provide the Preprocessing VIs that enable you to smooth a time series, to resample a time series, or to remove the trend from a time series. The Preprocessing VIs i

### Preprocess a Discrete Time Series

Preprocessing helps you make an acquired discrete time series more suitable for further
 analysis.

The LabVIEW Time Series Analysis Tools provide the Preprocessing VIs that
 enable you to smooth a time series, to resample a time series, or to remove the trend
 from a time series. The Preprocessing VIs include the Time
 Series Preprocessing Express VI that you can use to select an appropriate
 method to preprocess a time series interactively.

#### Resampling a Time
 Series

When you acquire a discrete time series, to avoid frequency
 aliasing, the sampling rate must be greater than twice the highest frequency
 component of the source signal. If you want to build models for a time series, you
 usually specify a sampling rate ten times as large as the highest frequency
 component of the source signal when acquiring the time series. However, a much
 higher sampling rate substantially increases the computation burden. If the sampling
 rate is unnecessarily high, you can resample the acquired time series and generate a
 new time series with a lower sampling rate.

Sometimes the time series under
 analysis is unequally-sampled. To use time series analysis methods, you need to
 resample the time series at equal time intervals to generate an equally-sampled time
 series.

Use the TSA Resampling VI to resample a time
 series.

#### Avoiding Frequency Aliasing

Before resampling, the frequency bandwidth of the source signal must be less than the
 Nyquist frequency at the new sampling rate to avoid aliasing. If the time series
 contains frequency components whose frequency bands are greater than the new Nyquist
 frequency, you can use a lowpass filter to attenuate those frequency components that
 are greater than the new Nyquist frequency.

The following figure shows a time series that contains a frequency component from 100
 to 200 Hz and another frequency component from 300 to 400 Hz. The sampling rate of
 the time series is 1000 Hz.

Figure 60.

[IMAGE alt='image' src='GUID-96485A05-0AC9-4EAD-ABBD-3B92E0B4AE06-a5.gif']

If the frequency band of interest is from 0 to 250 Hz, you can reduce the sampling
 rate to 500 Hz. When you resample the time series using the new sampling rate,
 frequency aliasing occurs if you do not attenuate the frequency component from 300
 to 400 Hz because this frequency component is above 250 Hz, the new Nyquist
 frequency.

The following figure shows the resampled time series that was not properly filtered
 before resampling and therefore contains frequency aliasing. In the Power
 Spectrum graph, you can see that frequency aliasing distorts the
 original frequency component from 100 Hz to 200 Hz.

Figure 61.

[IMAGE alt='image' src='GUID-E57C83F8-A31E-4140-88CE-CFCF1572048D-a5.gif']

To avoid frequency aliasing in the resampling operation, you first must sufficiently
 attenuate or filter out the frequency component that is above the new Nyquist
 frequency. In this example, you need to use a lowpass filter to attenuate the
 frequency component from 300 to 400 Hz in the original time series.

The following figure shows the filtered time series and the power spectrum. Notice
 that the lowpass filter removes the frequency component from 300 to 400 Hz from the
 time series.

Figure 62.

[IMAGE alt='image' src='GUID-B80561CC-27D8-4957-854F-8C118ACF78BA-a5.gif']

After removing the frequency component that is above the new Nyquist frequency, you
 can resample the time series with the new sampling rate of 500 Hz without frequency
 aliasing. The following Power Spectrum graph shows that the
 resampled time series preserves the frequency components of interest from 0 Hz to
 250 Hz without distortion:

Figure 63.

[IMAGE alt='image' src='GUID-E57C83F8-A31E-4140-88CE-CFCF1572048D-a5.gif']

#### Converting an Unequally-Sampled Time
 Series

Time series analysis methods process only equally-sampled time
 series. To analyze an unequally-sampled time series, you need to convert the
 unequally-sampled time series into an equally-sampled time series using the
 TSA Resampling VI.

The following figure shows an
 unequally-sampled time series and the corresponding equally-sampled time series. You
 can see that the time indexes are distributed equally in the Resampled
 Time Series graph.

Figure 64.

[IMAGE alt='image' src='GUID-09D25839-46A6-4461-9608-BDDC02D3CF87-a5.gif']

#### Smoothing a Time
 Series

Using the Time Series Analysis Tools, you can smooth a time series
 with either the moving average method or the exponential average method.

The
 moving average method estimates the local averaged value based on the adjacent
 values with a Finite Impulse Response (FIR) filter. You can use this method to
 remove the noise disturbance from a time series.

Use the TSA Moving
 Average VI to perform a moving average. This VI provides two typical
 moving average filters—Spencer and Henderson. You also can customize the
 coefficients of the moving average filters. The TSA Moving
 Average VI compensates the phase shift of the smoothed time series so
 no phase delay exists between the original and the smoothed time
 series.

Exponential averaging is another common approach to producing a smooth
 time series, which helps you remove the variations that the original time series
 contains. Exponential averaging also can remove seasonality, which is low-frequency
 periodic spectral content in a time series.

Use the TSA Exponential
 Average VI to perform exponential smoothing operations on a time
 series. You can select a suitable smoothing scheme according to the characteristics
 of the time series. This VI provides the following exponential smoothing
 schemes:

Single exponential smoothing scheme

Double exponential smoothing scheme

Triple exponential smoothing scheme

The following figure shows the results of exponential smoothing with different
 schemes. This figure indicates that the triple scheme follows the time series much
 closer than the single and double schemes because the time series contains a
 systematic trend and seasonality.

Figure 65.

[IMAGE alt='image' src='GUID-A9E5DCCE-F0A9-44EE-A84C-35E921C55618-a5.gif']

When using the triple exponential smoothing scheme, you must specify the season
 type of the analyzed time series. The following figure shows two time series with
 different types of seasonality—additive and multiplicative:

Figure 66.

[IMAGE alt='image' src='GUID-CFC5EDF9-CA41-442E-8305-286A8C075439-a5.gif']

In the previous figure, the Additive Seasonality graph
 shows a time series that has a constant amplitude change in seasonality. Using the
 TSA Exponential Average VI, you can analyze this type of time
 series by specifying Additive in season
 type. The Multiplicative Seasonality graph
 shows a time series that has a seasonality with the amplitude increasing over time.
 You can analyze this type of time series by specifying
 Multiplicative in season
 type.

#### Detrending a Time Series

A
 time series usually contains some constant amplitude offset components or
 low-frequency trends. The constant-offset components and low-frequency trends do not
 affect the dynamic characteristics of the system being analyzed, and the amplitudes
 of these trends sometimes are large and corrupt the results of time series modeling.
 Therefore, you need to remove the constant-offset components or low-frequency trends
 before performing further analysis.

If a time series contains no long-term
 (low-frequency) trends but only constant-offset components, you can detrend this
 time series by subtracting the mean value.

If a time series contains long-term
 trends and constant-offset components, use the TSA Detrend VI to
 obtain a detrended time series. This VI estimates the trend of a time series with
 the curve-fitting methods.

Parent topic:

Acquire and Preprocess Time Series

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=preprocess-data-from-a-system-advanced-sig.html language=enus -->
## TOPIC 00113: Preprocess Data from a System

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `preprocess-data-from-a-system-advanced-sig.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/preprocess-data-from-a-system-advanced-sig.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After acquiring the data, you must preprocess the raw data samples. Preprocessing involves steps such as removing trends, filtering noise, and so on.You can use the Data Preprocessing VIs to analyze the raw data and determine whether that data accurately reflects the response of the system you want

### Preprocess Data from a System

After acquiring the data, you must preprocess the raw data samples. Preprocessing
 involves steps such as removing trends, filtering noise, and so on.

You can use the Data Preprocessing VIs to analyze the raw data and determine
 whether that data accurately reflects the response of the system you want to identify.
 To identify a system model in the frequency domain by using time-domain data, you must
 preprocess the time-domain data by estimating the Frequency Response Function (FRF). You
 can use the SI Estimate FRF VI to estimate the FRF from time-domain
 data.

Note

Validating the quality of the data at each step in the preprocessing procedure is important in
 ensuring that you accurately identify a model in the later steps of the system
 identification process.

You can use a number of preprocessing techniques to ensure that the incoming data samples are
 free from external noise, scaling problems, outliers, and other corruptions. The
 following sections describe the preprocessing techniques.

- [Visually Inspect the Data](visually-inspect-the-data-advanced-signal.html)
- [Remove Offsets and Trends](remove-offsets-and-trends-advanced-signal-p.html)
- [Filtering and Downsampling](filtering-and-downsampling-advanced-signal-pr.html)
- [Data Scaling](data-scaling-advanced-signal-processing-toolk.html)

Parent topic:

System Identification Concepts

Related concepts:

- Validate Models
- Estimating the Frequency Response Function

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=preprocessing-the-data-advanced-signal-proces.html language=enus -->
## TOPIC 00114: Preprocessing the Data

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `preprocessing-the-data-advanced-signal-proces.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/preprocessing-the-data-advanced-signal-proces.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you gather data, the next step in the system identification process is to preprocess the data.The input to the system in this case study is the reaction torque of the structure on the ground. This input is a swept sine wave with 200 frequency points equally spaced over the frequency band from

### Preprocessing the Data

After you gather data, the next step in the system identification process is to
 preprocess the data.

The input to the system in this case study is the reaction torque of the structure on the ground.
 This input is a swept sine wave with 200 frequency points equally spaced over the
 frequency band from 0.122 Hz to 24.4 Hz.

The output of this system is the acceleration of the flexible arm. The acceleration contains
 information about the flexible resonances and anti-resonances.

The data set contains 4096 samples at a sampling rate of 500 Hz or sampling time of 0.002
 seconds. Thus the total time of the response is 8.192 seconds.

You can preprocess the raw data by examining the time and frequency responses of the system. Based on those analyses, you can filter and downsample the data set to reduce the amount of data in the raw data set for simpler identification.

#### Examining the Time
 Response Data

Using the data in the SI Data
 Samples VI for the flexible robotic arm, you can
 view the input and output data, as shown in the following
 figure:

Figure 204.

[IMAGE alt='image' src='GUID-0A6B6FBF-6E62-46EA-94F8-26B11105D153-a5.gif']

The stimulus signal – torque output
 corresponds to the input data, or the torque, and the
 response signal – acceleration output
 corresponds to the output data, or the acceleration.

The
 following figure shows the input and output data on graphs during
 the length of the response. By looking at the graphs, you can
 inspect the data for outliers, clipped saturation, or quantization
 effects that you can remove because they are not representative of
 the system behavior.

Figure 205.

[IMAGE alt='image' src='GUID-F98085AC-7D52-412A-A1A7-316CC790E6B1-a5.gif']

The previous figure shows no obvious nominal, trend, or outlier
 values in the input or output time waveforms.

#### Examining the
 Frequency Response Data

In addition to examining the time
 response data, you also want to examine the frequency response data.
 You can use the SI Estimate Frequency Response VI
 to view the frequency response of the measured output signal, as
 shown in the following figure:

Figure 206.

[IMAGE alt='image' src='GUID-6BF5D085-7263-4334-BA6D-F7CED5F83151-a5.gif']

The input data is periodic over 4096 samples, which is the signal
 length. Notice that in the previous figure the window
 length, 4096, is the same as the signal length
 so as to obtain a smaller bias in the frequency response
 estimation.

The following figure shows the magnitude and phase
 responses of the measured output signal. The magnitude
 response graph shows three resonances and two
 anti-resonances in the frequency domain. Resonances are vibrations
 of large amplitude in a system caused by exciting the system at its
 natural frequency.

Figure 207.

[IMAGE alt='image' src='GUID-5F400AE1-7863-454F-8154-4504A22094B4-a5.gif']

Notice the resonance at approximately 42 Hz. You can deduce that this
 resonance is caused by noise or nonlinear system behavior because
 the 42 Hz falls outside the frequency range of the input data,
 0.122–24.4 Hz. At 42 Hz, there is no input energy, thus implying
 that the response at 42 Hz is not a result of the input.

By
 examining the frequency response data, you see that filtering is
 necessary to remove this resonance peak at 42 Hz. You can use the
 System Identification VIs to apply a
 filter to the flexible arm data.

#### Applying a Filter to
 the Raw Data

To eliminate the resonance peak at 42 Hz, you
 can apply a filter to the raw data. By first applying a lowpass
 filter with a cutoff frequency of 25 Hz, you eliminate the
 high-frequency noise from the raw data set. The following figure
 shows how to use the SI Lowpass Filter VI to
 apply a lowpass filter to the raw data set:

Figure 208.

[IMAGE alt='image' src='GUID-893359C9-1FC6-4BA5-B4E0-3010C430A7C4-a5.gif']

You can see the effects of the lowpass filter by comparing the
 frequency response of the filtered data set in the following figure
 to the frequency response of the non-filtered data set. By using a
 lowpass filter, you can see that the resonance at approximately
 42 Hz is no longer part of the data set you will use to estimate the
 model.

Figure 209.

[IMAGE alt='image' src='GUID-4E6EB050-71D9-40F3-B32C-90DD22AA69BD-a5.gif']

#### Downsampling the Raw
 Data

Sampling theory, in conjunction with the Nyquist
 criterion, enables you to reduce the sampling rate from 500 Hz to
 50 Hz. Applying a filter and downsampling the data set reduces the
 number of samples in and the computational complexity of the data
 set. The goal is to use as few samples as possible to evaluate the
 behavior of the system.

Sampling theory enables you to
 downsample, or decimate, the data set. Downsampling reduces the
 sampling rate, 500 Hz, by a factor of 10. Thus downsampling enables
 you to acquire the data at a sampling rate of 50 Hz. The Nyquist
 criterion states that you must sample the signal at a minimum of
 twice the highest frequency in the system.

Recall that the
 input data is equally spaced over the frequency band 0.122–24.4 Hz.
 Therefore, according to the Nyquist criterion, you must sample at a
 minimum of 50 Hz to avoid any antialiasing. The benefit of sampling
 at 50 Hz is that you still acquire all the data in the frequency
 band, yet you eliminate the resonance peak at
 42 Hz.

Therefore, in the following figure, the SI
 Lowpass Filter VI sets the cutoff
 frequency to 25. In addition to applying a
 lowpass filter to the data, you must downsample the reduced data
 set. The SI Down Sampling VI in the following
 figure uses a decimation factor of 10.

Figure 210.

[IMAGE alt='image' src='GUID-BA88E4F9-5139-4D8C-AD2C-A1F9070EE32A-a5.gif']

The SI Lowpass Filter VI applies a lowpass filter
 before downsampling the data set to avoid aliasing at the 42 Hz
 resonance. Together, the lowpass filter and downsampling remove the
 high frequency disturbance and make the process faster and more
 efficient.

Notice that the window
 length parameter of the SI Estimate
 Frequency Response VI in the previous figure is
 around 400 instead of 4096, as shown in the previous figure. You can
 reduce the window length by a factor of 10 because the number of
 samples in the reduced data set is one tenth of the number of
 samples in the raw data set.

The following figure shows the
 frequency response after applying a filter to and downsampling the
 raw data set:

Figure 211.

[IMAGE alt='image' src='GUID-9E5EF173-6FE3-4A1D-8972-490B943C4E5B-a5.gif']

Filtering and downsampling are beneficial because they eliminate the
 nonrealistic parts of the frequency response and reduce the amount
 of work required in the model estimation process.

Parent topic:

Flexible Arm Case Study

Related concepts:

- Preprocess Data from a System
- Filtering and Downsampling
- Frequency Response

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=pseudo-random-binary-sequence-advanced-signal.html language=enus -->
## TOPIC 00115: Pseudo-Random Binary Sequence

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `pseudo-random-binary-sequence-advanced-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/pseudo-random-binary-sequence-advanced-signal.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Pseudo-Random Binary Sequence, also known as Maximal Length Sequence (MLS), is a periodic, deterministic signal with properties similar to white noise.You often generate a pseudo-random binary sequence using an n-bit shift register with feedback through an exclusive or (XOR) function. While appear

### Pseudo-Random Binary Sequence

A Pseudo-Random Binary Sequence, also known as Maximal Length Sequence (MLS), is a
 periodic, deterministic signal with properties similar to white noise.

You often generate a pseudo-random binary sequence using an n-bit shift
 register with feedback through an exclusive or (XOR) function. While appearing random,
 the sequence actually repeats every 2n–1 values.

When using a whole period, the pseudo-random binary sequence has special mathematical advantages
 that make it attractive as a stimulus signal. In particular, you can attribute
 variations in response signals between two periods of the stimulus to noise due to the
 periodic nature of the signal. Also, like the white random binary noise, the
 pseudo-random binary sequence has a low crest factor C<sub>f</sub>.
 You can use the SI Generate Pseudo-Random Binary Sequence VI to
 generate a Pseudo-Random Binary Sequence.

The following figure shows an example of a pseudo-random binary sequence:

Figure 172.

[IMAGE alt='image' src='GUID-FC3C6DD8-A034-4B96-A0DE-3349488EC11F-a5.gif']

Parent topic:

Choose a Stimulus Signal

Related concepts:

- Choose a Stimulus Signal

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=random-binary-signal-advanced-signal-processi.html language=enus -->
## TOPIC 00116: Random Binary Signal

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `random-binary-signal-advanced-signal-processi.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/random-binary-signal-advanced-signal-processi.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A random binary signal is a random process that can assume one of two possible values at any time.A simple method of generating a random binary signal is to take Gaussian white noise, filter the noise for the desired spectra and then convert the noise to a binary signal by taking the sign of the fil

### Random Binary Signal

A random binary signal is a random process that can assume one of two possible values at
 any time.

A simple method of generating a random binary signal is to take Gaussian white noise, filter the
 noise for the desired spectra and then convert the noise to a binary signal by taking
 the sign of the filtered signal. The desired spectra are functions of the system time
 constraints. The appropriate scaling must provide a meaningful response to the system,
 well above the noise level.

You can scale the signal to any desired amplitude. The resulting signal has a minimum crest
 factor  C<sub>f</sub> of 1. You can expect some differences in the resulting spectra. Therefore,
 you must perform offline analysis of the signal.

Binary signals are useful for identifying linear systems. However, the dual-level signal does not
 allow for validation against nonlinearities. If a system is nonlinear, you can use an
 input interval corresponding to the desired operating point. You might need to work with
 more than two input levels in these cases. You can combine multiple binary signals of
 different levels to form the stimulus signal.

The following figure shows an example of a random binary signal:

Figure 171.

[IMAGE alt='image' src='GUID-73DF28CD-7043-489D-A14F-39E9C2209789-a5.gif']

Parent topic:

Choose a Stimulus Signal

Related concepts:

- Data Scaling
- Choose a Stimulus Signal

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=recursive-least-squares-advanced-signal-proce.html language=enus -->
## TOPIC 00117: Recursive Least Squares

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `recursive-least-squares-advanced-signal-proce.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/recursive-least-squares-advanced-signal-proce.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The corresponding convergence rate in the Recursive Least Squares (RLS) algorithm is faster, but the implementation is more complex than that of LMS-based algorithms.The (RLS algorithm uses the following equations to modify the cost function J(k) = E[e^2(k)].Jk=Ee2k≅1N∑i=0N-1θ2k-1Compare this modifi

### Recursive Least Squares

The corresponding convergence rate in the Recursive Least Squares (RLS) algorithm is
 faster, but the implementation is more complex than that of LMS-based algorithms.

The (RLS algorithm uses the following equations to modify the cost function
 J(k) =
 E[e<sup>2</sup>(k)].

Jk=Ee2k≅1N∑i=0N-1θ2k-1

Compare this modified cost function, which uses the previous N error
 terms, to the cost function, J(k) = 
 E[e<sup>2</sup>(k)], which uses only the current error information
 e(k). The modified cost function
 J(k) is more robust.

The following procedure describes how to implement the RLS algorithm:

1. Initialize the parametric vector ⃗w(k) using a small positive number ε. w⇀0=ε,ε,...,εT
2. Initialize the data vector ⃗φ(k).
3. Initialize the k × k matrix
 P (0). P0=ε0000ε0000...0000ε
4. For k = 1, update the data vector ⃗φ(k) based on ⃗φ(k-1) and the
 current input data u ( k ) and output data
 y ( k ).
5. Compute the predicted response ŷ(k) by using the following equation. y^k=φ⇀Tk·w⇀k
6. Compute the error e ( k ) by solving the
 following equation: ek=yk-y^k
7. Update the gain vector ⃗k(k) defined by the following equation: K⇀k=Pk·φ⇀kλ+φ⇀T·Pk·φ⇀k The properties of a system might vary with time, so you must ensure
 that the algorithm tracks the variations. You can use the forgetting factor λ, which
 is an adjustable parameter, to track these variations. The smaller the forgetting
 factor λ, the less previous information this algorithm uses. When you use small
 forgetting factors, the adaptive filter is able to track time-varying systems that
 vary rapidly. The range of the forgetting factor λ is between zero and one,
 typically 0.98 < λ < 1. P ( k ) is a
 k × k matrix whose initial value is
 defined by P (0) in step 3.
8. Update the parametric vector w⇀k+1 . w⇀k+1=w⇀k+ek·K⇀k
9. Update the P ( k ) matrix. Pk+1=λ-1Pk-λ-1K⇀k·φ⇀Tk·Pk
10. Stop if the error is small enough, else set
 k = k + 1 and repeat steps 4–10.

Parent topic:

Recursive Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=recursive-model-estimation-methods-advanced-s.html language=enus -->
## TOPIC 00118: Recursive Model Estimation Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `recursive-model-estimation-methods-advanced-s.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/recursive-model-estimation-methods-advanced-s.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Recursive model estimation is a system identification technique that enables you to develop a model that adjusts based on real-time data coming from the system.Recursive model estimation processes the measured input-output data recursively as the data becomes available. This technique is helpful bec

### Recursive Model Estimation Methods

Recursive model estimation is a system identification technique that enables you to
 develop a model that adjusts based on real-time data coming from the system.

Recursive model estimation processes the measured input-output data recursively as the data
 becomes available. This technique is helpful because you obtain the mathematical model
 of the system in real time. In many real-world applications such as adaptive control and
 adaptive prediction, having a model of the system update while the system is running is
 necessary or helpful.

By comparison, the nonparametric, parametric, partially known, and closed-loop systems model
 estimation methods use nonrecursive methods to estimate a model of the dynamic system.
 These nonrecursive methods identify a model for a dynamic system based on input-output
 data gathered at a time prior to the current time.

The following figure represents a general recursive system identification application. A system identification application consists of an unknown system that has an input signal, or stimulus signal u(k) and an output signal, or response signal y(k).

Figure 200.

[IMAGE alt='image' src='GUID-E0A5B2D7-9DEE-46F9-A515-B6B0736A35D6-a5.gif']

The stimulus signal u(k) is the input to both the unknown
 system and the recursive model. The response of the system
 y(k) and the predicted response of the
 adaptive model ŷ(k) are combined to determine the error of the system. The error of the
 system is defined by the following equation:

e

k

=

y

k

-

y

^

k

The adaptive model generates the predicted response ŷ(k+1) based on
 u(k + 1) after adjusting the parametric vector
 ⃗w(k) based on the error e(k).

The previous figure shows how the error information e(k) is
 sent back to the adaptive model, which adjusts the parametric vector ⃗w(k) to account
 for the error. You iterate on this process until you minimize the magnitude of the least
 mean square error e(k).

Before you apply the recursive model estimation, you must first select the parametric model
 structure that determines the parametric vector ⃗w(k). Then, you must select the method
 that automatically adjusts the parametric vector such that the error
 e(k) goes to the minimum.

Use the Recursive Model Estimation VIs to estimate the following parametric
 model representations:

- ARX
- ARMAX
- Output-Error
- Box-Jenkins
- General-Linear

The Recursive Model Estimation VIs have a recursive
 method parameter that enables you to specify which recursive estimation
 method to use. The adaptive method you use affects the performance of recursive system
 identification application. You can choose from the following four methods:

- Least mean squares (LMS)
- Normalized least mean squares (NLMS)
- Recursive least squares (RLS)
- Kalman filter (KF)

The goal of each method is to adjust the parametric vector ⃗w(k) until you minimize the cost
 function J(k). The following equation defines the
 cost function J(k).

J

k

=

E

e

2

k

where E is the expectation of the enclosed term(s).

When the cost function J(k) is sufficiently small, the
 parametric vector ⃗w(k) is considered optimal for the estimation of the actual
 system.

- [Least Mean Squares](least-mean-squares-advanced-signal-processing.html)
- [Normalized Least Mean Squares](normalized-least-mean-squares-advanced-signal.html)
- [Recursive Least Squares](recursive-least-squares-advanced-signal-proce.html)
- [Kalman Filter](kalman-filter-advanced-signal-processing-tool.html)

Parent topic:

Estimate Models

Related concepts:

- Nonparametric Model Estimation Methods
- Parametric Model Estimation Methods
- Partially Known Model Estimation Methods
- Closed-Loop Systems Model Estimation Methods
- General-Linear Model Definitions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=remove-offsets-and-trends-advanced-signal-p.html language=enus -->
## TOPIC 00119: Remove Offsets and Trends

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `remove-offsets-and-trends-advanced-signal-p.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/remove-offsets-and-trends-advanced-signal-p.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can remove offsets and trends from raw data sets by using the SI Remove Trend VI. You can specify whether to remove offsets or trends by using the trend type input of this VI. Remove Offsets An estimated system model is a linearized version of the dynamic system around the operating point. You m

### Remove Offsets and Trends

You can remove offsets and trends from raw data sets by using the SI Remove
 Trend VI. You can specify whether to remove offsets or trends by using
 the trend type input of this VI.

#### Remove Offsets

An
 estimated system model is a linearized version of the dynamic system around the
 operating point. You must subtract the operating points from the raw data samples
 because linearization is done with respect to the signal values relative to the
 operating point, which is the offset level of the signal.

The following figure
 shows an example of removing the offset level of a signal. The goal of the water
 tank is to keep the water level at six meters. The Water level
 record graph shows that the water level changes in the vicinity of
 the operating point of six meters. If you use the water level record for system
 identification, you must remove the six meter operating point value.

Figure 176.

[IMAGE alt='image' src='GUID-4828F42F-69A9-4184-A5ED-26E848DC4BFC-a5.gif']

The SI Remove Trend VI enables you to remove the offset from
 the raw data set. You must set the trend typeto
 mean to use this preprocessing technique.

#### Remove Trends

External
 influences might add some low frequency or periodic components to the data. These
 additional components are not relevant to the specific modeling problem. Examples of
 external influences include variations due to the 24-hour day cycle in power plants,
 seasonal influences in biological and economical systems, thermal expansion in
 rolling mills, 50 or 60 Hz interference in power lines, and so on. The amplitude of
 these trends can be large and can corrupt the results of signal analysis and
 parametric identification algorithms.

The SI Remove Trend
 VI provides a way for you to remove these external influences, or trends, from the
 raw data set. You must set the trend type to
 linear to use this preprocessing technique.

Parent topic:

Preprocess Data from a System

Related concepts:

- Parametric Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=select-a-sampling-rate-advanced-signal-pro.html language=enus -->
## TOPIC 00120: Select a Sampling Rate

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `select-a-sampling-rate-advanced-signal-pro.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/select-a-sampling-rate-advanced-signal-pro.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The time constants of a system influence the selection of a sampling rate.Sampling at rates substantially greater than the system bandwidth leads to data redundancy, numerical issues, and modeling of high frequency artifacts likely due to noise. Sampling at rates slower than system dynamics leads to

### Select a Sampling Rate

The time constants of a system influence the selection of a sampling rate.

Sampling at rates substantially greater than the system bandwidth leads to data redundancy,
 numerical issues, and modeling of high frequency artifacts likely due to noise. Sampling
 at rates slower than system dynamics leads to difficulties determining an accurate
 system model and problems introduced by aliasing. You can use an anti-aliasing filter to
 counter the effects of aliasing.

A common rule of thumb is to sample signals at 10 times the bandwidth of the system or the
 bandwidth of interest for the model. If uncertainty exists in the system bandwidth and a
 fast data acquisition environment is available, you can sample as fast as possible, then
 use a digital filter and decimation to reduce the sampling rate to the desired value.
 Decimation is a form of downsampling the data set. You must ensure the sampling rate is
 constant to estimate the system model. If you sample data without a constant sampling
 rate, you must sample the data again with a constant sampling rate.

Parent topic:

Acquire Data from a System

Related concepts:

- Filtering and Downsampling

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=select-an-impulse-response-length-advanced.html language=enus -->
## TOPIC 00121: Select an Impulse Response Length

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `select-an-impulse-response-length-advanced.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/select-an-impulse-response-length-advanced.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SI Estimate Impulse Response VI has inputs to specify how many points of the impulse response to observe.Theoretically, the length of the impulse response might be infinite. For some systems, the impulse response quickly reaches zero, and the number of nonzero points is finite. For other systems

### Select an Impulse Response Length

The SI Estimate Impulse Response VI has inputs to specify how many points
 of the impulse response to observe.

Theoretically, the length of the impulse response might be infinite. For some systems, the
 impulse response quickly reaches zero, and the number of nonzero points is finite. For other
 systems, the impulse response never reaches zero. Realistically, you can obtain only the first
 N points of the impulse response due to limited signal length and limited
 memory size. Therefore, use the SI Estimate Impulse Response VI to specify
 how many points of the impulse response you want to observe. With the least squares method,
 you must ensure the sum of num of points (t<0) and num of
 points (t>=0) is no larger than the signal length. With the correlation
 analysis method, you can set num of points to be as large as the signal
 length.

Parent topic:

Impulse Response

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=select-the-factorization-type-for-p0-z.html language=enus -->
## TOPIC 00122: Select the Factorization Type for P0(z)

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `select-the-factorization-type-for-p0-z.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/select-the-factorization-type-for-p0-z.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Wavelet Design Express VI, use the Factorization (Type of G0) control to specify the factorization type.After you determine P[0](z), the next step is to specify how P[0](z) is factorized into the analysis lowpass filter G[0](z) and the synthesis lowpass filter H[0](z), respectively. The facto

### Select the Factorization Type for
 P0(z)

In the Wavelet Design Express VI, use the Factorization
 (Type of G0) control to specify the factorization type.

After you determine P<sub>0</sub>(z), the next step is to
 specify how P<sub>0</sub>(z) is factorized into
 the analysis lowpass filter G<sub>0</sub>(z) and
 the synthesis lowpass filter H<sub>0</sub>(z),
 respectively. The factorizing process is not unique. For a given
 P<sub>0</sub>(z), you have the following four
 options for creating G<sub>0</sub>(z) and
 H<sub>0</sub>(z).

- Arbitrary —No specific constraints are associated with this filter. The following figure shows an example of arbitrary factorization. The blue crosses represent the zeros of G 0 ( z ), and the red circles represent the zeros of H 0 ( z ). Click on the zero you want to select to switch the zero from that of G 0 ( z ) to that of H 0 ( z ) and vice versa.
 Figure 143.Arbitrary Factorization Example[IMAGE alt='image' src='GUID-CAA1C2EB-BEAC-45D5-9829-C34FB1325394-a5.gif']
- Minimum Phase —All of the zeros of
 G 0 ( z ) are contained inside the
 unit circle, as shown in the following figure. All the zeros of
 H 0 ( z ) are the reciprocal of the
 zeros of G 0 ( z ). The
 Wavelet Design Express VI automatically generates the zeros
 for H 0 ( z ) and
 G 0 ( z ). You cannot switch the
 zeros between G 0 ( z ) and
 H 0 ( z ). The minimum phase filter
 possesses minimum phase-lag. When
 P 0 ( z ) is maximally-flat and
 G 0 ( z ) is minimum phase, the
 resulting wavelets are the Daubechies wavelets. Figure 144.Zeros Analysis for
 G<sub>0</sub>(z) and H<sub>0</sub>(z) in Wavelet Design Express
 VI
 
 [IMAGE alt='image' src='GUID-B940065F-F2B2-4221-9BBE-3B2ABDAAFB69-a5.gif']
- Linear Phase —Any zero and its reciprocal must belong to the same filter, as shown in the following figure. When you switch a zero of G 0 ( z ) to that of H 0 ( z ), the reciprocal of the zero also switches to H 0 ( z ). When you switch a zero of H 0 ( z ) to that of G 0 ( z ), the reciprocal of the zero also switches to G 0 ( z ). This option is available only if the filter is biorthogonal. 
 Figure 145.Reciprocal Zeros Relationship in Filter
 Design[IMAGE alt='image' src='GUID-A5606826-2CBB-43A8-87EE-4733DDB9917D-a5.gif'] 
In the time domain, a linear phase implies that the coefficients of the filter are symmetric or antisymmetric. Linear phase filters have a constant group delay for all frequencies. This property is required in many signal and image feature-extraction applications, such as peak detection and image edge detection.
- B-Spline —This option is available only if Wavelet
 Type is Biorthogonal and P0
 type is Maxflat . In this case, the analysis
 lowpass filter G 0 ( z ) and the
 synthesis lowpass filter H 0 ( z ) are
 defined by the following equations, respectively:
 G 0 ( z ) = (1 +
 z –1 ) k H 0 ( z )
 = (1 +
 z –1 ) 2p–k Q ) z )
 where k is specified with the Zeros at
 π ( P0 ) control, and p is
 determined by the Zero pairs at π ( P0 )
 control. The Wavelet Design Express VI automatically generates
 the zeros of G 0 ( z ) and
 H 0 ( z ) based on the settings for
 k and p . You cannot switch the zeros
 between G 0 ( z ) and
 H 0 ( z ). The following figure
 shows an example of B-Spline factorization: Figure 146.B-Spline Factorization
 Example
 
 [IMAGE alt='image' src='GUID-B4E99441-8DB6-40CD-81F6-F8CB3355A9F3-a5.gif']

Parent topic:

Interactively Designing Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=select-the-wavelet-type.html language=enus -->
## TOPIC 00123: Selecting the Wavelet Type

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `select-the-wavelet-type.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/select-the-wavelet-type.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Wavelet Design Express VI, use the Wavelet Type control on the Configure Wavelet Design dialog box to select the wavelet type.You can choose from the following two wavelet types, Orthogonal (default) and Biorthogonal.The wavelet transform with orthogonal wavelets is energy conserving, meaning

### Selecting the Wavelet Type

In the Wavelet Design Express VI, use the Wavelet
 Type control on the Configure Wavelet Design
 dialog box to select the wavelet type.

You can choose from the following two wavelet types, Orthogonal (default)
 and Biorthogonal.

The wavelet transform with orthogonal wavelets is energy conserving, meaning that the total
 energy contained in the resulting coefficients and the energy in the original time
 samples are the same. This property is helpful for signal and image compression and
 denoising. But the filters associated with orthogonal wavelets are not linear phase.
 Linear phase is a helpful property for feature-extraction applications. The filters
 associated with biorthogonal wavelets can be linear phase.

Parent topic:

Interactively Designing Discrete Wavelets

Related concepts:

- Introduction to Wavelet Signal Processing

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=setting-parameter-constraints-with-a-range-ad.html language=enus -->
## TOPIC 00124: Setting Parameter Constraints with a Range

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `setting-parameter-constraints-with-a-range-ad.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/setting-parameter-constraints-with-a-range-ad.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have prior knowledge of a parameter, you can set constraints by providing upper and lower limits for the parameter.With the limit range, the SI Estimate Partially Known State-Space Model VI randomly selects a value within the range as an initial guess of the parameter. From this initial value

### Setting Parameter Constraints with a
 Range

If you have prior knowledge of a parameter, you can set constraints by providing upper
 and lower limits for the parameter.

With the limit range, the SI Estimate Partially Known State-Space Model VI
 randomly selects a value within the range as an initial guess of the parameter. From
 this initial value, the VI then performs optimization to minimize the difference between
 the estimated output and the measured real output. The goal of constraint optimization
 is to find a global optimum, or the smallest difference between the estimated output and
 the real output, with parameters of physical meaning. Successfully finding the global
 optimum depends on the limit range you set and the random initial value the SI
 Estimate Partially Known State-Space Model VI selects.

To increase the possibility of finding the global optimum, complete the following steps:

1. Use prior knowledge to set the range as narrow as possible.
2. Perform multiple estimates with the range you set. You might get different optimization results
 because the SI Estimate Partially Known State-Space Model VI
 randomly selects an initial value within the range each time you run the VI. If you
 repeatedly obtain the same result, this result might be the optimum you want to
 find. If you obtain inconsistent results, either choose the result that best meets
 the system requirements, or continue with step 3 to adjust the limit range.
3. Select one of the previous results you got in step 2 according to the prior knowledge you have
 of the system. Narrow the range in which the result falls. Run the SI
 Estimate Partially Known State-Space Model VI multiple times. A
 consistent result you get might be the optimum you want to find. Otherwise, repeat
 this step until you find a consistent result.

You set limits in the SI Estimate Partially Known Continuous Transfer Function
 Model VI the same way you do in the SI Estimate Partially Known
 State-Space Model VI.

Parent topic:

Define and Estimate Partially Known Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=setting-parameter-constraints-with-an-initial.html language=enus -->
## TOPIC 00125: Setting Parameter Constraints with an Initial Guess

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `setting-parameter-constraints-with-an-initial.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/setting-parameter-constraints-with-an-initial.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have information about a certain parameter and can estimate a value for that parameter, you can refine estimation by using that value as an initial guess.The SI Estimate Partially Known State-Space Model VI and the SI Estimate Partially Known Continuous Transfer Function Model VI perform opti

### Setting Parameter Constraints with an Initial
 Guess

If you have information about a certain parameter and can estimate a value for that
 parameter, you can refine estimation by using that value as an initial guess.

The SI Estimate Partially Known State-Space Model VI and the SI
 Estimate Partially Known Continuous Transfer Function Model VI perform
 optimization using the initial guess you provide. These two VIs then use the upper and
 lower limit settings you specify as boundary constraints during the optimization
 process.

The initial guess you provide greatly affects the performance of any optimization technique.
 Whether an optimization process reaches a global optimum depends on the initial guess.
 With some initial guesses, optimization processes might locate only a local optimum,
 which is the smallest difference between the estimated output and the real output within
 a certain smaller range rather than in the whole range of interest. Therefore, to
 decrease the risk of locating a local optimum instead of the global optimum, try
 different initial guesses. The following figure shows an example of different
 estimations resulting from different initial guesses and illustrates the importance of
 setting different initial guesses to find the global optimum.

Figure 195.

[IMAGE alt='image' src='GUID-B3D1250E-8459-43CB-A22D-34074AA41674-a5.gif']

As the previous figure shows, if you set C to an initial guess of 0.1, you
 obtain an optimized value of 0.02. You can see the Estimated response
 (global) plot and the Measured response plot
 match in the Response graph. This response from the estimated
 model is close to the real-world response. However, if you set the initial guess of
 C to 1.5, you get an optimized value of 1.41. The
 Estimated response (local) plot does not match the
 Measured response plot in the Response
 graph. Thus, with this initial guess, the estimated model response does
 not represent the real-world response accurately.

Parent topic:

Define and Estimate Partially Known Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=short-time-fourier-transform.html language=enus -->
## TOPIC 00126: Short-Time Fourier Transform

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `short-time-fourier-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/short-time-fourier-transform.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Short-Time Fourier Transform (STFT), also called the windowed Fourier transform or the sliding Fourier transform, partitions the time-domain input signal into several disjointed or overlapped blocks by multiplying the signal with a window function and then applies the discrete Fourier transform

### Short-Time Fourier Transform

The Short-Time Fourier Transform (STFT), also called the windowed Fourier transform or
 the sliding Fourier transform, partitions the time-domain input signal into several
 disjointed or overlapped blocks by multiplying the signal with a window function and
 then applies the discrete Fourier transform to each block.

The discrete Fourier transform expresses a signal as a sum of sinusoids. Because the time
 duration of the sinusoids is infinite, the discrete Fourier transform of the signal
 reflects the spectral content of an entire signal over time but does not indicate when
 the spectral content occurs. However, in some cases, evaluating the spectral content of
 a signal over a short time scale can be useful. You can use the STFT to evaluate
 spectral content over short time scales.

Window functions, also called sliding windows, are functions in which the amplitude tapers
 gradually and smoothly toward zero at the edges. Because each block occupies different
 time periods, the resulting STFT indicates the spectral content of the signal at each
 corresponding time period. When you move the sliding window, you obtain the spectral
 content of the signal over different time intervals. Therefore, the STFT is a function
 of time and frequency that indicates how the spectral content of a signal evolves over
 time. A complex-valued, 2-D array called the STFT coefficients stores the results of
 windowed Fourier transforms. The magnitudes of the STFT coefficients form a magnitude
 time-frequency spectrum, and the phases of the STFT coefficients form a phase
 time-frequency spectrum.

The STFT is one of the most straightforward approaches for performing time-frequency analysis and
 can help you easily understand the concept of time-frequency analysis. The STFT is
 computationally efficient because it uses the Fast Fourier Transform (FFT).

Without taking special care, however, the STFT is not invertible, meaning you cannot reconstruct
 the time-domain waveform from the STFT of a signal. For example, if you step the sliding
 window of the STFT without overlap, you cannot reconstruct the signal in the time domain
 from the STFT. The discrete Gabor transform is a special case of the STFT and is a kind
 of invertible algorithm. The inverse of the discrete Gabor transform is called the
 discrete Gabor expansion.

You can use the linear STFT method when you need the phase spectrum or when you do not need
 signal reconstruction. For example, the phase spectrum might be helpful in automatic
 speech-recognition applications. If you need only the magnitude spectrum in an
 application, use the quadratic STFT spectrogram method, which is the square of the
 linear STFT. The STFT spectrogram is one of the most popular quadratic time-frequency
 analysis methods because of its simplicity.

Use the TFA STFT VI to compute the STFT.

#### Window Type and Window Length

The time-frequency resolution of the STFT usually is defined as the product of the
 time resolution and the frequency resolution. The type of window you use affects the
 time-frequency resolution of the STFT. The Gaussian window has the optimal
 time-frequency resolution.

The window length also affects the time resolution
 and the frequency resolution of the STFT. A narrow window results in a fine time
 resolution but a coarse frequency resolution because narrow windows have a short
 time duration but a wide bandwidth. A wide window results in a fine frequency
 resolution but a coarse time resolution because wide windows have a long time
 duration but a narrow frequency bandwidth. This phenomenon is called the window
 effect. You cannot obtain a fine time resolution and a fine frequency resolution
 simultaneously using the STFT. With a time-invariant window, the STFT has the same
 time resolution and frequency resolution across the entire time-frequency
 plane.

If you need an adaptive time resolution and frequency resolution, use
 the adaptive transform or wavelet transform in the LabVIEW Wavelet Analysis
 Tools.

The best window length depends on the characteristics of the signal you
 want to analyze. The window length should be small enough so that the windowed
 signal block is essentially stationary over the window interval and large enough so
 that the Fourier transform of the windowed signal block provides a reasonable
 frequency resolution. If the spectral content of the signal evolves over time
 slowly, which does not require a fine time resolution, set the window length large.
 If the spectral content of the signal changes relatively quickly, which requires a
 fine time resolution, set the window length small. For example, in speech signal
 processing, a time-domain window length of 25 ms is common.

The step size of
 the sliding window determines if overlap exists. If the step size is smaller than
 the window length, overlap exists. If the step size is greater than the window
 length, no overlap exists. Overlap of the sliding window makes the STFT smoother
 along the time axis. However, overlap requires more computation time and memory. If
 the signal length is large and the spectral content evolves slowly, it is not
 necessary to overlap the sliding window. If the signal length is small, overlap the
 sliding window to obtain a smoother STFT.

Parent topic:

Linear Time Frequency Analysis Methods

Related concepts:

- STFT Spectrogram
- Quadratic Time Frequency Analysis Methods
- Adaptive Transform and Expansion
- Introduction to Wavelet Signal Processing

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=signal-processing-with-continuous-wavelets.html language=enus -->
## TOPIC 00127: Signal Processing with Continuous Wavelets

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `signal-processing-with-continuous-wavelets.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/signal-processing-with-continuous-wavelets.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use continuous wavelet tools to perform wavelet transforms on signals that are defined in continuous time.Unlike discrete wavelet tools, which operate on sampled-data signals, continuous wavelet tools operate on signals that are defined for all time over a time region of interest, though the

### Signal Processing with Continuous Wavelets

You can use continuous wavelet tools to perform wavelet transforms on signals that are
 defined in continuous time.

Unlike discrete wavelet tools, which operate on sampled-data signals, continuous wavelet tools
 operate on signals that are defined for all time over a time region of interest, though
 the computations are done numerically in discrete time.

The LabVIEW Wavelet Analysis Tools provide two continuous wavelet tools: the Continuous Wavelet
 Transform (CWT) and the Analytic Wavelet Transform (AWT). The AWT retains both the
 magnitude and phase information of signals in the time-scale or time-frequency domain,
 whereas the CWT retains only the magnitude information. The CWT is simpler because the
 results of the CWT are real values if both the wavelet and the signal are real. The
 results of the AWT normally are complex values.

From a mathematical point of view, both the CWT and AWT add informational redundancy because the
 number of the resulting wavelet coefficients in the time-scale or time-frequency domain
 is larger than the number of time samples in the original signal. Excess redundancy
 generally is not desirable because more computations and more memory are required to
 process signals with excess redundancy. However, excess redundancy can be helpful for
 some applications, such as singularity and cusp extraction, time-frequency analysis of
 nonstationary signals, and self-similarity analysis of fractal signals.

- [Continuous Wavelet Transform](continuous-wavelet-transform.html)
- [Analytic Wavelet Transform](analytic-wavelet-transform.html)

Parent topic:

Wavelet Analysis Concepts

Related concepts:

- Introduction to Wavelet Signal Processing
- Signal Processing with Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=signal-processing-with-discrete-wavelets.html language=enus -->
## TOPIC 00128: Signal Processing with Discrete Wavelets

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `signal-processing-with-discrete-wavelets.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/signal-processing-with-discrete-wavelets.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Although you can use numerical algorithms to compute continuous wavelet coefficients to analyze a signal, the resulting wavelet coefficients are not invertible. You cannot use those wavelet coefficients to recover the original data samples. For applications that require signal reconstruction, the La

### Signal Processing with Discrete Wavelets

Although you can use numerical algorithms to compute continuous wavelet coefficients to analyze a
 signal, the resulting wavelet coefficients are not invertible. You cannot use those
 wavelet coefficients to recover the original data samples. For applications that require
 signal reconstruction, the LabVIEW Wavelet Analysis Tools provide the following discrete
 wavelet tools:

- Discrete Wavelet Transform (DWT)
- Wavelet packet decomposition and arbitrary path decomposition
- Undecimated Wavelet Transform (UWT)

You can use the discrete wavelet tools to perform signal analysis and signal processing,
 including multiresolution analysis, denoising, compression, edge detection, peak
 detection and others.

#### Selecting an Appropriate Discrete
 Wavelet

The Wavelet Analysis Tools provide the following commonly used
 discrete wavelets:

- Orthogonal wavelets— Haar , Daubechies
 ( db xx ),
 Coiflets
 ( coif x ), and
 Symmlets
 ( sym x )
- Biorthogonal wavelets—Biorthogonal
 ( bior x_x ),
 including FBI ( bior4_4 (FBI) )

x indicates the order of the wavelet. The higher the order,
 the smoother the wavelet.

Orthogonal wavelets are suitable for applications
 such as signal and image compression and denoising, because the wavelet transform
 with orthogonal wavelets possesses the same amount of energy as that contained in
 the original data samples. The energy-conservative property ensures that the inverse
 wavelet transform does not enlarge the energy of noise suppressed in the wavelet
 domain. However, the filters associated with orthogonal wavelets are not
 linear-phase filters. Linear-phase filters maintain a constant time delay for
 different frequencies and are necessary in many signal and image feature extraction
 applications, such as peak detection and image edge detection. Biorthogonal wavelets
 can be linear phase and are suitable for applications that require linear-phase
 filters.

You also can use the Wavelet Design Express VI to
 design a customized wavelet.

#### Filter Banks

The discrete wavelet transform, the undecimated wavelet transform, and wavelet packet analysis use filter banks, as shown in the following illustration:

Figure 123.

[IMAGE alt='image' src='GUID-1C35415F-A7DE-4EBD-AC31-FC9E1C3761E8-a5.gif']

G
 <sub>1</sub>(z) is the analysis highpass filter. G<sub>0</sub>(z) is the analysis lowpass filter. G<sub>1</sub>(z) and G<sub>0</sub>(z) form the analysis filter bank. The output of the analysis highpass filter are the detail coefficients. The output of the analysis lowpass filter are the approximation coefficients. H<sub>1</sub>(z) is the synthesis highpass filter. H<sub>0</sub>(z) is the synthesis lowpass filter. H<sub>1</sub>(z) and H<sub>0</sub>(z) form the synthesis filter bank.

- [Discrete Wavelet Transform](discrete-wavelet-transform.html)
- [Wavelet Packet Decomposition](wavelet-packet-decomposition.html)
- [Undecimated Wavelet Transform](undecimated-wavelet-transform.html)

Parent topic:

Wavelet Analysis Concepts

Related concepts:

- Continuous Wavelet Transform
- Multiresolution Analysis
- Interactively Designing Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=spectral-analysis-method-advanced-signal-proc.html language=enus -->
## TOPIC 00129: Spectral Analysis Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `spectral-analysis-method-advanced-signal-proc.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/spectral-analysis-method-advanced-signal-proc.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the spectral analysis method with any input signal. However, the frequency bandwidth of the input signal must cover the range of interest.Because the frequency response is the Fourier transform of the impulse response, applying the Fourier transform to both sides of the cross-correlation

### Spectral Analysis Method

You can use the spectral analysis method with any input signal. However, the frequency
 bandwidth of the input signal must cover the range of interest.

Because the frequency response is the Fourier transform of the impulse response, applying the
 Fourier transform to both sides of the cross-correlation function yields the following
 equation:

ϕ

u

y

e

j

ω

=

ϕ

u

u

e

j

ω

G

e

j

ω

where

- G ( e jω ) is the
 frequency response of the system
- Φ uu ( e jω )
 is the auto-spectral density of the stimulus signal
- Φ uy ( e jω )
 is the cross-spectral density between the stimulus signal
 u ( k ) and the response signal
 y ( k )

You then can use the following equation to compute the frequency response
 G(e<sup>jω</sup>):

G

e

j

ω

=

ϕ

u

y

e

j

ω

ϕ

u

u

e

j

ω

You can compute
 Φ<sub>uu</sub>(e<sup>jω</sup>)
 and
 Φ<sub>uy</sub>(e<sup>jω</sup>)
 by applying a Fast Fourier Transform (FFT) to the autocorrelation function
 R<sub>uu</sub> and the cross-correlation
 function R<sub>uy</sub>, respectively. The number
 of data points you need to compute R<sub>uu</sub>
 and R<sub>uy</sub> decreases as the lag
 τ increases. Therefore,
 R<sub>uu</sub> and
 R<sub>uy</sub> become inaccurate for a
 large lag τ. In this situation, you can apply a lag window to counter
 the effects of a large lag τ and improve the accuracy of the
 frequency response estimation.

Parent topic:

Frequency Response

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=spectrogram-feature-extraction.html language=enus -->
## TOPIC 00130: Spectrogram Feature Extraction

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `spectrogram-feature-extraction.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/spectrogram-feature-extraction.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the LabVIEW Time Frequency Analysis Tools to apply post-processing techniques to extract useful 1D information from spectrograms and compute the Mean Instantaneous Frequency (MIF), the Mean Instantaneous Bandwidth (MIB), the group delay, and the marginal integration from spectrograms.Results fro

### Spectrogram Feature Extraction

Use the LabVIEW Time Frequency Analysis Tools to apply post-processing techniques to
 extract useful 1D information from spectrograms and compute the Mean Instantaneous
 Frequency (MIF), the Mean Instantaneous Bandwidth (MIB), the group delay, and the
 marginal integration from spectrograms.

Results from these post-processing techniques can be used to characterize spectrograms and to
 help with further feature extraction and pattern recognition in real-world applications.
 For example, you can use the MIF of ground echo signals to detect the liquefaction that
 might be associated with an earthquake, and you can use the MIF and MIB of Doppler
 ultrasound signals for noninvasive blood flow measurements.

#### Mean Instantaneous
 Frequency

The mean frequency of a signal describes the center of gravity
 of the power spectrum of the signal. The power spectrum of nonstationary signals is
 time dependent, and therefore the mean frequency of nonstationary signals is time
 dependent. The time-dependent mean frequency is called the mean instantaneous
 frequency. For nonstationary signals with a single frequency component or a single
 frequency band, the MIF describes the central frequency evolution over time.

Use the TFA Mean Instantaneous Frequency VI to compute the
 statistical first moment of the spectrogram along the frequency axis as an
 estimation of the MIF. The first moment of the Wigner-Ville Distribution (WVD) or
 the first moment of the Choi-Williams Distribution (CWD) is the MIF. The first
 moments of other quadratic time-frequency representations can provide only an
 approximation of the MIF.

#### Mean Instantaneous
 Bandwidth

The mean bandwidth of a signal describes the spread of the power
 spectrum of the signal around the mean frequency. The power spectrum of
 nonstationary signals is time dependent, and therefore the mean bandwidth of
 nonstationary signals is time dependent. The time-dependent mean bandwidth is called
 the mean instantaneous bandwidth.

Use the TFA Mean Instantaneous
 Bandwidth VI to compute the second moment of the spectrogram along the
 frequency axis as an estimation of the MIB.

#### Group Delay

The time delay
 of a single-tone signal describes the localization of the signal in the time domain.
 If signal A has a larger time delay than signal B, signal A follows signal B in the
 time domain. The group delay is the time delay of a nonstationary signal as a
 function of frequency. The group delay describes the time lags among different
 frequencies. You also can use the group delay to measure the propagation time
 through a system as a function of frequency.

Use the TFA Group
 Delay VI to compute the first moment of the spectrogram along the time
 axis as an estimation of the group delay.

#### Marginal Integration

The
 marginal integration is the integration of the spectrogram along the time axis or
 the frequency axis. If the integration along the time axis equals the power spectrum
 of the signal, the spectrogram satisfies the marginal frequency condition. If the
 integration along the frequency axis equals the instantaneous power of the signal,
 the spectrogram satisfies the marginal time condition. The WVD and the CWD satisfy
 both marginal conditions. For other quadratic time-frequency analysis methods, you
 can consider the marginal time integration as the mean instantaneous power and the
 marginal frequency integration as the mean power spectrum.

Use the
 TFA Marginal Integration VI to compute the marginal
 integration.

Parent topic:

Quadratic Time Frequency Analysis Methods

Related concepts:

- Overview of LabVIEW Time Frequency Analysis Tools
- Wigner-Ville Distribution
- Other Cohen's Class Time Frequency Distributions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=state-space-model-definitions-advanced-signal.html language=enus -->
## TOPIC 00131: State-Space Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `state-space-model-definitions-advanced-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/state-space-model-definitions-advanced-signal.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The state-space model is the most convenient model for describing Multiple-Input Multiple-Output (MIMO) systems. State-space models often are preferable to polynomial models, especially in modern control applications that focus on multivariable systems.You can estimate both continuous and discrete s

### State-Space Model Definitions

The state-space model is the most convenient model for describing Multiple-Input
 Multiple-Output (MIMO) systems. State-space models often are preferable to polynomial
 models, especially in modern control applications that focus on multivariable
 systems.

You can estimate both continuous and discrete state-space models.

#### Continuous

Use partially
 known model estimation methods to estimate continuous state-space models. You must
 provide an initial guess for each parameter before conducting estimation. The
 following equations show the form of the continuous state-space model:

x

=

A

x

+

B

u

+

K

e

y

=

C

x

+

D

u

+

e

where

- A is an n × n state
 matrix of the given system
- B is an n × m input matrix of the given
 system
- C is an r × n output matrix of the given
 system
- D is an r × m direct transmission matrix
 of the given system
- K is the Kalman gain matrix
- e is the system disturbance

#### Discrete

Use the
 SI Estimate State-Space Model and SI Estimate
 State-Space Model from FRF VIs to estimate discrete state-space
 models. The SI Estimate State-Space Model VI supports the
 following two estimation methods:

Deterministic-stochastic subspace method

Realization method

The following equations show the form of the discrete state-space model:

x

k

+

1

=

A

x

k

+

B

u

k

+

K

e

k

y

k

=

C

x

k

+

D

u

k

+

e

k

Note

K

e

k

e

k

where

- k is the model sampling time multiplied by the discrete time
 step, where the discrete time step equals 0, 1, 2, …
- n is the number of model states
- m is the number of model inputs
- r is the number of model outputs
- x is the model state vector
- u is the model input vector
- y is the model output vector
- e ( k ) is the system disturbance

The state-space transfer matrices A, B,
 C, and D often reflect physical
 characteristics of a system. The dimension of the state vector x
 is the only setting you must provide for the state-space model.

Parent topic:

Parametric Model Estimation Methods

Related concepts:

- Model Types and Representations
- Partially Known Model Estimation Methods
- Kalman Filter
- Impulse Response

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=step-signals-and-step-responses-advanced-sign.html language=enus -->
## TOPIC 00132: Step Signals and Step Responses

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `step-signals-and-step-responses-advanced-sign.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/step-signals-and-step-responses-advanced-sign.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A step signal is a signal that switches from an initial value a to another value b in a very short time.You can generate this signal by creating an array that begins with a series of a and then shifts to a series of b. For example, if you use zero as a and one as b, you can create an array that begi

### Step Signals and Step Responses

A step signal is a signal that switches from an initial value
 a to another value b in a very
 short time.

You can generate this signal by creating an array that begins with a series of
 a and then shifts to a series of b. For
 example, if you use zero as a and one as b, you
 can create an array that begins with a series of zeros and then shifts to a series of
 ones, such as "0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1". Use the Build Waveform
 (Analog Waveform) function to convert this array to a waveform signal.

Use step signals as stimulus signals to estimate dynamic systems from step responses. The
 following figure shows an example of a step stimulus signal and the corresponding step
 response:

Figure 174.

[IMAGE alt='image' src='GUID-861DD63C-EF08-41CD-9D30-2F39310C7909-a5.gif']

A step stimulus signal and the corresponding step response contain the following phases:

Initial Condition

0

Delay

Steady State

Parent topic:

Choose a Stimulus Signal

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=stft-spectrogram.html language=enus -->
## TOPIC 00133: STFT Spectrogram

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `stft-spectrogram.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/stft-spectrogram.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Short-Time Fourier Transform (STFT) spectrogram is the normalized, squared magnitude of the STFT coefficients produced by the STFT. Normalization makes the STFT spectrogram obey Parseval's energy-conservation property, meaning that the energy in the STFT spectrogram equals the energy in the orig

### STFT Spectrogram

The Short-Time Fourier Transform (STFT) spectrogram is the normalized, squared magnitude
 of the STFT coefficients produced by the STFT.

Normalization makes the STFT spectrogram obey Parseval's energy-conservation property, meaning
 that the energy in the STFT spectrogram equals the energy in the original time-domain
 signal. All the quadratic time-frequency analysis methods in the LabVIEW Time Frequency
 Analysis Tools adhere to Parseval's energy-conservation property.

The STFT spectrogram, a Cohen's class method, can be a good first choice for a quadratic
 time-frequency analysis method because this method is simple and fast. With the STFT
 spectrogram, you can infer if a signal is reasonably oversampled by looking for a low
 energy density at high frequencies in the STFT spectrogram. You also can estimate the
 spectral content of a signal and how the spectral content evolves over time by seeing
 where the energy is concentrated in the STFT spectrogram. However, other quadratic
 time-frequency analysis methods can provide superior time-frequency resolution. You can
 experiment with other methods in the Time Frequency Spectrogram
 Express VI to see if the STFT spectrogram unacceptably blurs the signal
 components you want to analyze.

When you have large data sets or when you do not need special features of the spectrogram, such
 as a fine time-frequency resolution, consider using the STFT spectrogram because it is
 fast and easy to use.

Use the TFA STFT Spectrogram VI to compute the STFT spectrogram.

#### Window Type and Window Length

The STFT spectrogram usually is sufficient for most applications, but it typically provides a coarse time-frequency resolution as a result of window effects that the window type and the window length determine. A narrow window results in a fine time resolution but a coarse frequency resolution because narrow windows have a short time duration but a wide bandwidth. A wide window results in a fine frequency resolution but a coarse time resolution because wide windows have a long time duration but a narrow frequency bandwidth. You cannot obtain a fine time resolution and a fine frequency resolution simultaneously by using the STFT spectrogram.

#### Selecting an Appropriate STFT
 Spectrogram Window Length

The following figure shows a frequency hopper signal, commonly used in
 spread-spectrum communication systems, such as CDMA cell phones:

Figure 22.

[IMAGE alt='image' src='GUID-D4875D12-E376-4A40-A308-C08E4839987D-a5.gif']

The following figure shows the ideal quadratic time-frequency representation of the
 example frequency hopper signal in the previous figure:

Figure 23.

[IMAGE alt='image' src='GUID-7939E17A-7F78-42C4-9107-233300B95C09-a5.gif']

In the previous figure, the ideal representation of the frequency of the signal
 remains constant and then immediately switches to another frequency. The following
 figure shows the STFT spectrogram of the example frequency hopper signal with a
 window length of 128:

Figure 24.

[IMAGE alt='image' src='GUID-4A80B850-A4BD-4A7C-BFA3-612A08390BC9-a5.gif']

Compared to the ideal time-frequency representation, the energy distribution of the
 signal in the previous figure is not confined to narrow lines. The STFT spectrogram
 in the previous figure is blurry as a result of the window effects of the STFT. This
 blurriness is a manifestation of the coarse time-frequency resolution of the STFT
 spectrogram. The window length and the window type determine how the energy blurs
 across time and frequency and thus determine the time resolution and the frequency
 resolution of the STFT spectrogram. For example, a wider window length can reduce
 energy blurring across frequencies at the expense of increased blurring across time.
 A narrower window length can reduce blurring across time at the expense of increased
 blurring across frequencies. The following figure shows the STFT spectrogram of the
 example frequency hopper signal with a window length of 32:

Figure 25.

[IMAGE alt='image' src='GUID-9C916D23-D331-4E68-B94A-15433539E546-a5.gif']

Relative to the STFT spectrogram of the frequency hopper signal with a window length
 of 128, the energy distribution of the signal in the previous figure is more spread
 out along the frequency axis and is more compact along the time axis, which means
 that the STFT spectrogram has a coarser frequency resolution but a finer time
 resolution when the window length is narrow.

The following figure shows the STFT spectrogram of the example frequency hopper
 signal with a window length of 256:

Figure 26.

[IMAGE alt='image' src='GUID-FE97CE11-E0CD-4EF5-94BD-F84647C6CD8D-a5.gif']

Relative to the spectrogram of the frequency hopper signal with a window length of
 128, the energy distribution of the signal in the previous figure is more spread out
 along the time axis and is more compact along the frequency axis, which means that
 the STFT spectrogram has a coarser time resolution but a finer frequency resolution
 when the window length is wide.

#### Reassignment Method

You can use the reassignment method to improve the time-frequency resolution of the
 STFT spectrogram artificially. The reassignment method automatically compresses the
 energy in the quadratic time-frequency representation toward the centers of gravity
 of the signal components to make the signal components more concentrated. The
 reassignment method uses the assumption that the energy of the signal components in
 the time-frequency representation is tightly concentrated. Using the reassignment
 method can help improve the time-frequency resolution of time-frequency concentrated
 components. However, the reassignment method also can bias the location of spectral
 peaks, merge distinct spectral components, falsely split compact signal components,
 or excessively sharpen naturally blurry signal components in the resulting
 time-frequency representation. The following figure shows the reassigned STFT
 spectrogram of the example frequency hopper signal:

Figure 27.

[IMAGE alt='image' src='GUID-8B56B283-2CCA-4BBA-9934-DCC9760BE559-a5.gif']

Notice that the signal components in the reassigned STFT spectrogram in the previous
 figure are less blurry in time and frequency than the STFT spectrograms in the
 figures of the frequency hopper signal with a window length of 128, 32, and 256.
 Thus, this reassigned STFT spectrogram has a better time-frequency resolution.

Parent topic:

Quadratic Time Frequency Analysis Methods

Related concepts:

- Short-Time Fourier Transform
- Overview of LabVIEW Time Frequency Analysis Tools

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=system-identification-case-studies-advanced-s.html language=enus -->
## TOPIC 00134: System Identification Case Studies

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `system-identification-case-studies-advanced-s.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/system-identification-case-studies-advanced-s.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The System Identification VIs provide the following case studies to guide you through processes of system identification: the Flexible Arm Case Study, the Frequency-Domain Model Estimation Case Study, and the Partially Known Model Estimation Case Study.

### System Identification Case Studies

The System Identification VIs provide the following case studies to
 guide you through processes of system identification: the Flexible Arm Case Study, the
 Frequency-Domain Model Estimation Case Study, and the Partially Known Model Estimation
 Case Study.

- [Flexible Arm Case Study](flexible-arm-case-study-advanced-signal-proce.html)
- [Frequency-Domain Model Estimation Case Study](frequency-domain-model-estimation-case-study.html)
- [Partially Known Model Estimation Case Study](partially-known-model-estimation-case-study-a.html)

Parent topic:

System Identification Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=system-identification-concepts-advanced-signa.html language=enus -->
## TOPIC 00135: System Identification Concepts

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `system-identification-concepts-advanced-signa.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/system-identification-concepts-advanced-signa.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections describe concepts in the System Identification VIs.

### System Identification Concepts

The following sections describe concepts in the System
 Identification VIs.

- [Introduction to System Identification](introduction-to-system-identification-advance.html)
- [Get Started with System Identification](get-started-with-system-identification.html)
- [Acquire Data from a System](acquire-data-from-a-system-advanced-signal.html)
- [Preprocess Data from a System](preprocess-data-from-a-system-advanced-sig.html)
- [Estimate Models](estimate-models-advanced-signal-processing.html)
- [Analyze, Validate, and Convert Models](analyze-validate-and-convert-models-ad.html)
- [System Identification Case Studies](system-identification-case-studies-advanced-s.html)

Parent topic:

LabVIEW Advanced Signal Processing Toolkit Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=the-capon-method.html language=enus -->
## TOPIC 00136: The Capon Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `the-capon-method.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/the-capon-method.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Capon method estimates the Power Spectral Density (PSD) of a time series, X [t], by using the output power of a Finite Impulse Response (FIR) bandpass filter.The Capon method designs an FIR filter that suppresses all frequencies of an input signal except the frequency components at frequency ω.

### The Capon Method

The Capon method estimates the Power Spectral Density (PSD) of a time series, X
 <sub>t</sub>, by using the output power of a Finite Impulse Response (FIR) bandpass
 filter.

The Capon method designs an FIR filter that suppresses all frequencies of an input signal except
 the frequency components at frequency ω. The following figure shows the Capon estimation
 method:

Figure 94.

[IMAGE alt='image' src='GUID-019A69A2-94E4-4008-8CEA-E83C7C686965-a5.gif']

The Capon method has a higher frequency resolution than the periodogram and Welch methods.
 Therefore, you can identify peaks more accurately with the Capon method than with these
 methods.

The following figure shows the PSDs based on the periodogram, Welch, and Capon methods:

Figure 95.

[IMAGE alt='image' src='GUID-49B733DB-E4F7-4BA8-B1D2-EE253966CCF6-a5.gif']

The PSD in green uses the Capon method. The PSDs in white and red use the Welch and periodogram
 methods, respectively. Notice that the peaks of the Capon method PSD are sharper.

The Capon method does not require prior knowledge about the input signal. Therefore, this method
 is less restrictive than model-based methods, such as the AR and ARMA methods, which
 require you to determine the model order before estimating the PSD.

You also can use the Capon method to determine the leading frequency and corresponding power
 magnitudes of an input signal. The following figure shows an example of a VI that uses
 the Capon method to estimate the leading frequency in a synthesized time series
 consisting of exponentially-damped sinusoids:

Figure 96.

[IMAGE alt='image' src='GUID-8A855047-8789-4E9E-BF58-71ABD138CDD7-a5.gif']

In the Estimated Parameters section of the previous figure, notice that the Power at 120.0 Hz is greater than the Power at 130.0 Hz. Therefore, the leading frequency of this time series is 120.0 Hz.

Use the TSA Capon Spectrum VI to compute the PSD of a time series by using the
 Capon method. Use the TSA Capon Frequency Estimator VI to determine
 the leading frequency of a time series by using the Capon method.

Parent topic:

Power Spectrum Estimation Methods

Related concepts:

- Model-Based Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=the-music-method.html language=enus -->
## TOPIC 00137: The MUSIC Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `the-music-method.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/the-music-method.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The MUSIC method, a model-based spectral estimation technique with high frequency resolution, computes a pseudo PSD that is not generally proportional to the true PSD.The Multiple Signal Classification (MUSIC) method is a model-based spectral estimation method. The MUSIC method offers higher frequen

### The MUSIC Method

The MUSIC method, a model-based spectral estimation technique with high frequency
 resolution, computes a pseudo PSD that is not generally proportional to the true
 PSD.

The Multiple Signal Classification (MUSIC) method is a model-based spectral estimation method.
 The MUSIC method offers higher frequency resolution in the resulting Power Spectral
 Density (PSD) than the Fast Fourier Transform (FFT)-based methods. However, the MUSIC
 method computes PSD magnitudes that generally are not proportional to the true PSD.
 Therefore, the PSD that the MUSIC method computes traditionally is known as the pseudo
 PSD.

Assuming that a time series can be represented by a series of complex sinusoids with
 additive white noise, the MUSIC method first computes the correlation matrix
 R<sub>p</sub> of the time series and obtains the eigenvectors
 V<sub>1</sub>, V<sub>2</sub>, ...,
 V<sub>p</sub> and eigenvalues λ<sub>1</sub>, λ<sub>2</sub>, ..., λ<sub>p</sub>. The
 eigenvectors V<sub>1</sub>, V<sub>2</sub>, ...,
 V<sub>M</sub> with large eigenvalues form the signal subspace. The remaining
 eigenvectors V<sub>M</sub><sub>+1</sub>,
 V<sub>M</sub><sub>+2</sub>, ..., V<sub>p</sub>
 form the noise subspace. The signal subspace also can be represented by group vectors of
 complex sinusoids e(f<sub>1</sub>),
 e(f<sub>2</sub>), ...,
 e(f<sub>M</sub>). The vector of a complex sinusoid is defined as
 follows:

e

f

i

=

1

,

e

j

2

πf

i

,

.

.

.

,

e

j

2

πf

i

M

If a time series contains a frequency component at f<sub>i</sub>, the vector
 e(f<sub>i</sub>) is uncorrelated with
 V<sub>M</sub><sub>+1</sub>,
 V<sub>M</sub><sub>+2</sub>, ..., V<sub>p</sub>. Accordingly, the
 following equation generates a peak value at f<sub>i</sub>:

P

S

D

f

i

=

1

∑

k

=

M

+

1

P

e

T

f

i

V

k

2

×

1

∆

f

Note

A modified MUSIC method uses the eigenvalues λ<sub>1</sub>, λ<sub>2</sub>, ...,
 λ<sub>p</sub> as a weighting vector to compute the PSD as follows:

P

S

D

f

i

=

1

∑

k

=

M

+

1

P

1

λ

k

e

T

f

i

V

k

2

×

1

∆

f

The modified MUSIC method, which also is called the Eigenvector method, can reduce the
 variance in the estimated PSD.

When using the MUSIC method, you must specify the size of the noise subspace, which is defined as
 p–M. In general, you can specify a rough
 percentage of the whole space for the size of the noise subspace. With a large size of
 the noise subspace, you can obtain a smooth PSD but the resulting PSD may miss weak
 spectral peaks in the signal. With a small size of the noise subspace, you can obtain a
 detailed PSD that reveals weak spectral peaks. However, a too small size for the noise
 subspace leads to spurious peaks in the resulting PSD. Refer to the *Discrete
 Random Signals and Statistical Signal Processing*section for more information
 about using the MUSIC method.

Use the TSA MUSIC VI to compute the PSD of a time series with the MUSIC
 method.

Parent topic:

Power Spectrum Estimation Methods

Related information:

- Related Documentation

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=the-periodogram-method.html language=enus -->
## TOPIC 00138: The Periodogram Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `the-periodogram-method.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/the-periodogram-method.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The periodogram method is the most common nonparametric method for computing the Power Spectral Density (PSD) of a time series.This method computes the PSD with the Fast Fourier Transform (FFT) according to the following equation:PSDf=FFTWt×Xt, f2L×1∆f where X[t] is a time series L is the number of

### The Periodogram Method

The periodogram method is the most common nonparametric method for computing the Power
 Spectral Density (PSD) of a time series.

This method computes the PSD with the Fast Fourier Transform (FFT) according to the following
 equation:

P

S

D

f

=

F

F

T

W

t

×

X

t

,

f

2

L

×

1

∆

f

where

- X t is a time series
- L is the number of samples in the time series
- W t is the applied window function
- Δ f is the frequency interval

The applied window function reduces spectral leakage in the estimation, but the window function
 also decreases the frequency resolution at the same time.

Use the TSA Periodogram VI to compute the PSD of a time series. If a time
 series contains non-periodic signal components or periodic components that are not
 sampled synchronously, the value of the resulting PSD computed by this VI may have a
 large variance at each frequency.

Parent topic:

Power Spectrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=the-welch-method.html language=enus -->
## TOPIC 00139: The Welch Method

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `the-welch-method.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/the-welch-method.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Welch method reduces the variance of the periodogram method by averaging by first dividing a time series into overlapping subsequences then applying a window to each subsequence and averaging the periodogram of each subsequence.The length of the applied window controls the trade-off between bias

### The Welch Method

The Welch method reduces the variance of the periodogram method by averaging by
 first dividing a time series into overlapping subsequences then applying a
 window to each subsequence and averaging the periodogram of each
 subsequence.

The length of the applied window controls the trade-off between bias and variance of the
 resulting Power Spectral Density (PSD). The following figure shows the
 resulting PSD for a signal from a system with two pairs of poles at about
 0.17 and 0.21 Hz, when the window length is 2048 and 128 for the top and
 bottom plots, respectively:

Figure 93.

[IMAGE alt='image' src='GUID-489B22E6-6CAE-4461-9BC1-E0E81D10326A-a5.gif']

In the PSD (Window = 2048) graph, a large window generates a PSD with
 small bias in the locations of the two peaks, as you can see that the
 magnitudes of the peaks in the Estimated PSD plot
 almost equal the magnitudes of the peaks in the Ideal
 PSD plot. However, a large window results in a coarse
 PSD plot, as shown by the general fuzziness in the Estimated
 PSD plot.

In the PSD (Window = 128) graph, you can see that a small window generates
 a smooth Estimated PSD plot. However, a small window
 can lead to large bias, as you can see that the magnitudes of the peaks in
 the Estimated PSD plot are different from the
 magnitudes of the peaks in the Ideal PSD plot.

Use the TSA Welch VI to compute the PSD of a time series.

Parent topic:

Power Spectrum Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=time-frequency-analysis-application-areas.html language=enus -->
## TOPIC 00140: Time Frequency Analysis Application Areas

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `time-frequency-analysis-application-areas.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/time-frequency-analysis-application-areas.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many real-world signals contain time-varying spectra, which means that the potential application areas of time-frequency analysis are numerous.In general, you can categorize time-frequency analysis methods into two classes: linear methods and quadratic methods. You usually use quadratic methods to a

### Time Frequency Analysis Application Areas

Many real-world signals contain time-varying spectra, which means that the potential
 application areas of time-frequency analysis are numerous.

In general, you can categorize time-frequency analysis methods into two classes: linear methods
 and quadratic methods. You usually use quadratic methods to analyze, classify, and
 detect latent features in a signal, and you usually use linear methods to reduce noise
 and extract signal components.

One major benefit of applying a time-frequency transform to a signal is discovering the pattern
 of frequency changes, which often clarifies the nature of the signal. Once you identify
 a pattern, you can analyze and classify the pattern. For example, a pattern of harmonic
 drift associated with rotating machinery can indicate the working condition of a system,
 and a pattern of frequency changes in medical signals can indicate a patient's health
 condition.

Another important use of time-frequency analysis is to reduce random noise in noise-corrupted
 signals. For example, random noise might spread evenly across the entire time-frequency
 domain. The useful information, however, usually is concentrated in a relatively small
 region in the time-frequency domain. If you convert such a noise-corrupted signal to the
 time-frequency domain using a linear time-frequency transform, you might be able to
 extract those components in the time-frequency domain and then reconstruct the
 time-domain signal, which has a higher signal-to-noise ratio.

You also can use time-frequency analysis to determine if a signal has distinct time-frequency
 components and isolate those components for further analysis. In the time domain, you
 can separate the components of signals that do not overlap, such as musical notes. You
 cannot use the Fourier transform to separate signal components that overlap in the time
 domain. In the frequency domain, you can use the Fast Fourier Transform (FFT) to
 separate signals, such as vibration harmonics caused by a steady-state shaft imbalance.
 However, the different components can overlap in the frequency domain if the spectral
 content varies over time. With such overlapping signal components, you cannot
 distinguish the components in either the time domain or in the frequency domain alone.
 In this situation, you usually can use a linear time-frequency method to distinguish the
 overlapping signal components.

The following list highlights a few successful application areas of time-frequency analysis:

- Order analysis, such as for rotating machinery analysis

Note

- Machine condition monitoring for systems associated with rotational machinery, such as power-generator systems
- Audio equipment testing and characterization, such as for speakers
- Speech processing, such as speech enhancement and speech recognition
- Radar and sonar image enhancement
- Biomedical signal processing, such as signal feature extraction
- Seismological signal processing, such as detection of soil liquefaction

Parent topic:

Time Frequency Analysis Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=time-frequency-analysis-concepts.html language=enus -->
## TOPIC 00141: Time Frequency Analysis Concepts

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `time-frequency-analysis-concepts.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/time-frequency-analysis-concepts.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections describe the concepts in the LabVIEW Time Frequency Analysis Tools.

### Time Frequency Analysis Concepts

The following sections describe the concepts in the LabVIEW Time Frequency
 Analysis Tools.

- [Introduction to Time Frequency Analysis](introduction-to-time-frequency-analysis.html)
- [Overview of LabVIEW Time Frequency Analysis Tools](overview-of-labview-time-frequency-analysis-t.html)
- [Time Frequency Analysis Application Areas](time-frequency-analysis-application-areas.html)
- [Linear Time Frequency Analysis Methods](linear-time-frequency-analysis.html)
- [Quadratic Time Frequency Analysis Methods](understanding-quadratic-time-frequency-analys.html)

Parent topic:

LabVIEW Advanced Signal Processing Toolkit Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=time-series-analysis-application-areas.html language=enus -->
## TOPIC 00142: Time Series Analysis Application Areas

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `time-series-analysis-application-areas.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/time-series-analysis-application-areas.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Time series occur in many fields. This topic discusses time series analysis applications in the industrial and engineering fields using the LabVIEW Time Series Analysis Tools. Fault and Failure DiagnosisFault diagnostics are important industrial tools to assess the health of industrial equipment and

### Time Series Analysis Application Areas

Time series occur in many fields. This topic discusses time series analysis
 applications in the industrial and engineering fields using the LabVIEW Time Series
 Analysis Tools.

#### Fault and Failure
 Diagnosis

Fault diagnostics are important industrial tools to assess the
 health of industrial equipment and ensure that the equipment is in proper working
 condition. Failure or damage detection ensures the integrity of machine elements and
 structures. Using the time series analysis methods such as dynamic modeling,
 cepstrum analysis, or bispectrum analysis, you can perform fault and failure
 diagnosis by analyzing the vibration or acoustic signals from the
 equipment.

The following figure shows an example of performing fault diagnosis
 by building an autoregressive-moving average (ARMA) model for a vibration time
 series from a running engine.

Figure 50.

[IMAGE alt='image' src='GUID-0C4002BD-5950-4681-A2B3-046705CD9299-a5.gif']

Under normal conditions, the vibration signal from the engine is a stationary
 time series. If you build an ARMA model for this stationary time series, the
 modeling errors are usually small. However, if the engine is not running properly
 due to imbalance or cracks, the vibration signal becomes a nonstationary time
 series. If you build an ARMA model for this nonstationary time series, the modeling
 errors increase. In the previous figure, the peaks in the Noise
 Variance graph show the large variances of the modeling errors and
 indicate that this engine is not running properly.

If you want to detect a
 structural failure or damage in a mechanical system, you usually compute and examine
 the Power Spectral Density (PSD) of the time series that the analyzed system
 generates. However, in some cases, you cannot get a satisfactory result by computing
 the PSD. The following figure shows the PSD of the vibration time series from a
 normal concrete beam and a cracked concrete beam. The differences are subtle, and
 they do not suggest the presence of a defect in the beam.

Figure 51.

[IMAGE alt='image' src='GUID-440C729F-F1B6-4372-A7C9-A5F523EE4796-a5.gif']

Using the Time Series Analysis Tools, you can compute the bispectra of the two
 time series. Bispectrum analysis is related to the third moment (skewness) of a
 vibration time series and outperforms traditional PSD analysis in detecting the
 asymmetric nonlinearity due to structural cracks.

The following figure
 displays the bispectra of the vibration time series from the cracked beam and the
 normal beam.

Figure 52.

[IMAGE alt='image' src='GUID-D5696CF0-5C4D-44E5-BF5E-0DCBEC537999-a5.gif']

The magnitudes of the peaks in the two bispectra are different. In the
 Bispectrum of a Normal Beam graph, the magnitudes are
 small. In the Bispectrum of a Cracked Beam graph, the
 magnitudes are large. A large magnitude indicates large coupling between frequencies
 in a time series. In the previous figure, you can see that the bispectrum of the
 cracked beam contains significant coupling between frequencies due to system
 non-linearities.

#### Structural Testing

Structural testing extracts key resonance features of a physical system by estimating
 the modal parameters of a time series that the system generates. Modal parameters
 include natural frequencies, damping factors, magnitudes, and phases.

Modal parameters contain information that describes the inherent dynamic properties
 of a structure. Understanding the vibration behavior of a structure is important in
 creating robust prototypes and validating structural systems such as cars, aircraft,
 bridges, and buildings. You can obtain the modal parameters of a structure by
 performing modal analysis using the time series modeling method.

The following figure illustrates a structural testing experiment that obtains the
 modal parameters of a steel-reinforced concrete beam. A hammer impacts the beam, and
 seven acceleration sensors located in different positions on the beam acquire the
 resulting vibration signals.

Figure 53.

[IMAGE alt='image' src='GUID-E8D1BC33-FF9F-4B8C-985D-30ECD35AF441-a5.gif']

Using the Time Series Analysis Tools, you can compute the resonance components, or
 modes, of the steel-reinforced concrete beam. The following table lists the detected
 natural frequencies f and damping factors a of
 each mode of the beam.

|  | First Mode | Second Mode | Third Mode | Fourth Mode |
| --- | --- | --- | --- | --- |
| f(Hz) | 78.2886 | 249.407 | 457.382 | 579.891 |
| α | 0.17 | 0.16 | 0.17 | 0.49 |

Besides the natural frequency and damping factor, a mode also includes the magnitude
 and phase information. The following figure shows the modal shapes of the beam
 computed with the estimated magnitudes and phases of each mode.

Figure 54.

[IMAGE alt='image' src='GUID-C679CBED-D1B0-4C38-8F36-D8751B07FDFA-a5.gif']

#### Data Mining

Data mining
 extracts important features from data and helps you find interesting patterns,
 rules, or models. Data mining involves a variety of computational methods and
 techniques. For example, Independent Component Analysis (ICA) is an effective data
 mining method in the biomedical, mechanical, and seismological fields. You can use
 ICA to separate informative signals from noise in signals such as
 Electroencephalogram (EEG) signals and Magnetoencephalogram (MEG) signals.

MEG
 signals are the magnetic signals generated from electric dipoles around a human
 brain. The following figure shows some MEG signals acquired at a human scalp by 148
 sensors. These signals indicate brain activities.

Figure 55.

[IMAGE alt='image' src='GUID-8CFB826D-5692-4E94-AE67-BF7CE9B7A225-a5.gif']

All cognitive activities in the human brain generate magnetic signals. Besides
 those cognitive activities, heartbeats, eye blinking, and breathing also generate
 magnetic signals. These signals are superimposed on the measured brain signal in the
 previous figure. To distinguish the brain signal from other signals, you can perform
 ICA on the MEG signals to remove the unwanted signals not originating in the brain
 activities. The following figure shows the result of ICA:

Figure 56.

[IMAGE alt='image' src='GUID-A349DD10-8E98-4018-B564-236C1844723F-a5.gif']

You can see that the Independent Components graph contains
 a red line, which clearly indicates the signal generated from heartbeats. You can
 remove the heartbeat signal from the MEG signals and perform further analysis on the
 residual signals.

#### Industrial Measurement

Industrial measurements involve measuring a variety of physical attributes such as
 position, speed, and force. In general, you can measure the physical attributes
 directly with appropriate sensors. However, in some special industrial applications
 where you cannot apply measuring directly, you have to obtain the physical values
 using some time series analysis methods, such as correlation.

The following figure illustrates a speed measurement system for a steel rolling mill.
 The reflected light from the surface of the steel belt is focused onto two
 photoelectric cells by lens. The two photoelectric cells, located at different
 positions with a separation of d, convert the waveform signals of
 the reflected light into voltage signals. The voltage values from the photoelectric
 cells form two time series X<sub>t</sub> and
 Y<sub>t</sub>. The two series are acquired on the same
 position track with a separation of d.

Figure 57.

[IMAGE alt='image' src='GUID-67798E9B-D006-4C24-B797-7E99D41F9F2E-a5.gif']

To measure the moving speed of the steel belt, you can perform cross-correlation on
 X<sub>t</sub> and Y<sub>t</sub> and
 generate the correlogram, as shown in the following figure:

Figure 58.

t

t

[IMAGE alt='image' src='GUID-6F50DCA5-1A7F-4821-B737-248A68CEBBC7-a5.gif']

The correlogram of the two time series contains a maximum point at a lag of
 τ<sub>d</sub>. To compute the speed v of the steel belt, you
 can use the following equation: v =
 d/τ<sub>d</sub>.

#### Model Predictive Control

Model predictive control is an important application of time series analysis in engineering. The model predictive control process includes the following steps:

1. Build models of a time series
2. Use the models to predict the future values of the time series
3. Make necessary adjustments to the system that generates the time series to make the predicted
 values align better with target values

The following section provides an example of controlling shaft axes positions based on predicted results.

First, you acquire the positions of the rotating shaft axes to form a time series. You then make a prediction for the next position of the moving shaft by building models of the time series. Using the predicted position, you can take actions to reduce the future position error. The following figure shows two time series plots of the shaft axes position with prediction control and without prediction control. The Shaft Axes Position with Control graph shows a smaller variance.

Figure 59.

[IMAGE alt='image' src='GUID-48FC0132-7B2A-45E1-A5CE-AB1CEB48AEA1-a5.gif']

Parent topic:

Time Series Analysis Concepts

Related concepts:

- Cepstrum Estimation Methods
- Bispectrum Estimation Methods
- Building Autoregressive-Moving Average Models
- Power Spectrum Estimation Methods
- Building Modal Parametric Models
- Multivariate Statistical Values
- Correlation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=time-series-analysis-concepts.html language=enus -->
## TOPIC 00143: Time Series Analysis Concepts

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `time-series-analysis-concepts.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/time-series-analysis-concepts.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections describe the concepts in the LabVIEW Time Series Analysis Tools.

### Time Series Analysis Concepts

The following sections describe the concepts in the LabVIEW Time Series Analysis
 Tools.

- [Introduction to Time Series Analysis](introduction-to-time-series-analysis.html)
- [Overview of LabVIEW Time Series Analysis Tools](overview-of-labview-time-series-analysis-tool.html)
- [Time Series Analysis Application Areas](time-series-analysis-application-areas.html)
- [Acquire and Preprocess Time Series](acquire-and-preprocess-time-series.html)
- [Perform Statistical Analysis](perform-statistical-analysis.html)
- [Building Models](building-models.html)
- [Predict Time Series Values](predict-time-series-values.html)
- [Perform Correlation and Spectral Analysis](perform-correlation-and-spectral-analysis.html)

Parent topic:

LabVIEW Advanced Signal Processing Toolkit Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=transfer-function-model-definitions-advanced.html language=enus -->
## TOPIC 00144: Transfer Function Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `transfer-function-model-definitions-advanced.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/transfer-function-model-definitions-advanced.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a transfer function to define either a continuous system or a discrete system.The following equations describe a continuous system and a discrete system, respectively, from which the transfer function is derived:yt=Gsut+etyk=Gzuk+ek where y(t) and y(k) are the system outputs G(s) and G(z

### Transfer Function Model Definitions

You can use a transfer function to define either a continuous system or a discrete
 system.

The following equations describe a continuous system and a discrete system, respectively, from
 which the transfer function is derived:

y

t

=

G

s

u

t

+

e

t

y

k

=

G

z

u

k

+

e

k

where

- y ( t ) and
 y ( k ) are the system outputs
- G ( s ) and
 G ( z ) is the transfer function between the
 stimulus and the response
- u ( t ) and
 u ( k ) are the system inputs
- e ( t ) and
 e ( k ) are the system disturbance

Note

s

z

#### SISO

The following is the
 equation for the continuous transfer function SISO model:

G

s

=

b

0

+

b

1

s

+

.

.

.

+

b

m

-

1

s

m

-

1

+

b

m

s

m

a

0

+

a

1

s

+

.

.

.

+

a

n

-

1

s

n

-

1

+

a

n

s

n

e

-

s

T

d

where

- s is the Laplace variable and continuous time
- m is the order of the numerator polynomial function
- n is the order of the denominator polynomial function
- b m are the coefficients of the
 numerator polynomial function
- a n are the coefficients of the
 numerator polynomial function
- T d is the system delay

Note

T

d

The following is the
 equation for the discrete-time transfer function SISO model:

G

z

=

b

0

+

b

1

z

+

.

.

.

+

b

m

-

1

z

m

-

1

+

b

m

z

m

a

0

+

a

1

z

+

.

.

.

+

a

n

-

1

z

n

-

1

+

a

n

z

n

where

- z is discrete time
- m is the order of the numerator polynomial function
- n is the order of the denominator polynomial function
- b m are the coefficients of the
 numerator polynomial function
- a n are the coefficients of the
 numerator polynomial function

#### MISO

The following is the
 equation for the continuous transfer function MISO model:

y

f

∑

f

=

1

n

G

i

f

s

u

j

where

- G ij are the transfer functions
 between the stimulus and the response
- i is the input number of the system
- j is the output number of the system

The following is the equation for the discrete-time transfer function MISO
 model:

v

i

∑

f

=

1

n

G

i

f

z

u

j

You can use the SI Estimate Transfer Function Model VI to
 estimate both continuous and discrete models. For discrete models, this VI
 implements the prediction error method. For continuous models, this VI internally
 performs the following three consecutive steps to estimate the model:

1. Calculates a discrete model with the prediction error method.
2. Applies the Zero-Order-Hold method to convert the discrete model to a continuous
 model.
3. Uses the Gauss-Newton method to optimize the continuous model this VI converted
 in step 2.

You can use the SI Estimate Transfer Function Model from FRF
 VI to estimate both continuous and discrete SISO models in the frequency
 domain.

Transfer function models describe only the deterministic part of the
 system. For stochastic control, general-linear polynomial models commonly are used
 because these models separately describe the deterministic and stochastic parts of a
 system. However, in classical control engineering, the deterministic part of the
 system is more important than the stochastic part. Therefore, you can take advantage
 of the relationship between input and output signals of the transfer function model
 to describe the deterministic part of the system.

Parent topic:

Parametric Model Estimation Methods

Related concepts:

- Model Types and Representations
- Determining Parameters for the Prediction Error Method
- Frequency-Domain Model Estimation Case Study

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=undecimated-wavelet-transform.html language=enus -->
## TOPIC 00145: Undecimated Wavelet Transform

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `undecimated-wavelet-transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/undecimated-wavelet-transform.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the WA Undecimated Wavelet Transform VI and the WA Inverse Undecimated Wavelet Transform VI to decompose and reconstruct 1D or 2D signals.Unlike the Discrete Wavelet Transform (DWT), which downsamples the approximation coefficients and detail coefficients at each decomposition level, the Undecim

### Undecimated Wavelet Transform

Use the WA Undecimated Wavelet Transform VI and the WA
 Inverse Undecimated Wavelet Transform VI to decompose and reconstruct 1D
 or 2D signals.

Unlike the Discrete Wavelet Transform (DWT), which downsamples the approximation coefficients and
 detail coefficients at each decomposition level, the Undecimated Wavelet Transform (UWT)
 does not incorporate the downsampling operations. Thus, the approximation coefficients
 and detail coefficients at each level are the same length as the original signal. The
 UWT upsamples the coefficients of the lowpass and highpass filters at each level. The
 upsampling operation is equivalent to dilating wavelets. The resolution of the UWT
 coefficients decreases with increasing levels of decomposition.

#### Translation-Invariant
 Property

Unlike the DWT, the UWT has the translation-invariant, or
 shift-invariant, property. If two signals are shifted versions of each other, the
 UWT results for the two signals also are shifted versions of each other. The
 translation-invariant property is important in feature-extraction
 applications.

The following figure shows an example that detects
 discontinuities in the HeaviSine signal with both the DWT and the UWT:

Figure 137.

[IMAGE alt='image' src='GUID-2FB97E80-ED98-4B74-8F52-263CB664758E-a5.gif']

You can use the first-level detail coefficients of either the DWT or the UWT to
 detect the discontinuities in the HeaviSine signal by locating the peaks in the
 coefficients. However, if the HeaviSine signal is shifted by 21 samples, all of the
 first-level DWT detail coefficients become very small. Therefore, you cannot use the
 first-level DWT detail coefficients to detect the discontinuities in the shifted
 HeaviSine signal. Because of the translation-invariant property of the UWT, you can
 use the first-level UWT detail coefficients to detect the discontinuities of the
 shifted HeaviSine Signal. The first-level UWT detail coefficients of the shifted
 HeaviSine Signal are simply the shifted version of the first-level UWT detail
 coefficients of the original HeaviSine signal.

Use the WA Get
 Coefficients of Undecimated Wavelet Transform VI to get the UWT
 coefficients you compute from the WA Undecimated Wavelet
 Transform VI and to return the coefficient type, such as the
 approximation coefficients or the detail coefficients, at a specific coefficient
 level. Use the WA Set Coefficients of Undecimated Wavelet
 Transform VI to set the coefficients you obtain from the WA
 Get Coefficients of Undecimated Wavelet Transform VI.

#### Better Denoising
 Capability

Denoising with the UWT also is shift-invariant. The denoising
 result of the UWT has a better balance between smoothness and accuracy than the DWT.
 The DWT-based method is more computationally efficient than the UWT-based method.
 However, you cannot achieve both smoothness and accuracy with the DWT-based
 denoising method.

Use the Wavelet Denoise Express VI or the
 WA Denoise VI to reduce noise in 1D signals with both the
 UWT-based and DWT-based methods. The UWT-based method supports both real and complex
 signals. The DWT-based method supports only real signals. You also can use the
 WA Denoise VI to reduce noise in 2D signals with the
 UWT-based method.

The denoising procedure in the Wavelet Denoise
 Express VI and the WA Denoise VI involves the
 following steps:

1. Applies the DWT or the UWT to noise-contaminated signals to obtain the DWT
 coefficients or the UWT coefficients. The noise in signals usually corresponds
 to the coefficients with small values.
2. Selects an appropriate threshold for the DWT coefficients or the UWT
 coefficients to set the coefficients with small values to zero. The
 Wavelet Denoise Express VI and the WA
 Denoise VI provide methods that automatically select the
 thresholds. The bound of noise reduction with these methods is 3 dB. To achieve
 better denoising performance for a signal, you can select an appropriate
 threshold manually by specifying the user defined thresholds parameter of the WA Denoise VI.
3. Reconstructs the signal with the inverse DWT or the inverse UWT.

The following figure shows the denoising results of a noisy Doppler signal with
 both the DWT-based method and the UWT-based method. Both methods use the level-5
 wavelet transform and the soft threshold.

Figure 138.

[IMAGE alt='image' src='GUID-E9DEE6A2-EA10-4889-A7B6-31AC9A7772F9-a5.gif']

In the previous figure, you can see that the UWT outperforms the DWT in signal
 denoising because the denoised signal in the Denoising with
 UWT graph is smoother.

#### Better Peak Detection
 Capability

Peaks often imply important information about a signal. You can
 use the UWT to identify the peaks in a noise-contaminated signal.

The
 UWT-based peak detection method is more robust and less sensitive to noise than the
 DWT-based method, because the UWT-based method involves finding zero-crossings in
 the multiscale UWT coefficients. The UWT-based method first finds zero-crossings
 among the coefficients with coarse resolution and then finds zero-crossings among
 the coefficients with finer resolution. Finding zero-crossings among the
 coefficients with coarse resolution enables you to remove noise from a signal
 efficiently. Finding zero-crossings among the coefficients with finer resolution
 improves the precision with which you can find peak locations.

The WA
 Multiscale Peak Detection VI and the WA Online Multiscale
 Peak Detection VI use the UWT-based method. These VIs detect peaks in
 offline and online signals. You can use these VIs in the following ways:

- Use the WA Multiscale Peak Detection VI once for an offline
 signal
- Use the WA Online Multiscale Peak Detection VI continuously
 for a block of signals
- Use the WA Online Multiscale Peak Detection VI continuously
 for signals from streaming data sources

The following figure shows an example that uses the WA Online
 Multiscale Peak Detection VI to detect peaks in an Electrocardiogram
 (ECG) signal. The UWT-based method locates the peaks of the ECG signal accurately,
 regardless of whether the peaks are sharp or rounded.

Figure 139.

[IMAGE alt='image' src='GUID-35C46EB2-519F-4CAD-BC7D-A48350E3BE7B-a5.gif']

Parent topic:

Signal Processing with Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=understanding-quadratic-time-frequency-analys.html language=enus -->
## TOPIC 00146: Quadratic Time Frequency Analysis Methods

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `understanding-quadratic-time-frequency-analys.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/understanding-quadratic-time-frequency-analys.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The discrete Fourier transform computes a frequency-domain representation of time-domain signals. The inverse discrete Fourier transform converts the frequency-domain representation back to the time-domain representation.In traditional spectral analysis, the discrete Fourier transform and the invers

### Quadratic Time Frequency Analysis
 Methods

The discrete Fourier transform computes a frequency-domain representation of time-domain
 signals. The inverse discrete Fourier transform converts the frequency-domain
 representation back to the time-domain representation.

In traditional spectral analysis, the discrete Fourier transform and the inverse discrete Fourier
 transform are complementary operations. One important application of the Fourier
 transform is computing the power spectrum of a signal. The power spectrum presents the
 energy of a signal as a function of frequency. You can use the power spectrum to detect
 harmonics of a signal and to examine the frequency response of a system when the
 spectral content does not change over time. Because the power spectrum usually is
 estimated by the square of the Fourier transform, the power spectrum is considered a
 quadratic frequency analysis method.

Note

Use the TFA Configure Spectrogram Indicator VI to display a spectrogram on an
 intensity graph as a color map, from which you can determine the spectral content of a
 signal and how the spectral content evolves over time. You also can save the
 time-dependent 2D array to a text file for use in another software environment. The
 resulting text file contains only Z values and does not retain the time axis information
 or the frequency axis information. Use the TFA Get Time and Freq Scale
 Info VI to compute the time scale information and the frequency scale
 information of the time-frequency representation.

From a spectrogram, you also can extract features from a signal, such as the Mean Instantaneous
 Frequency (MIF) and the group delay. You can use the information in these extracted
 features in signal analysis, detection, estimation, and classification.

Unlike the linear time-frequency analysis methods, the quadratic time-frequency analysis methods
 are not invertible, meaning you cannot reconstruct time-domain signals from
 spectrograms. If you need to reconstruct signals, use the linear time-frequency analysis
 methods instead.

The quadratic time-frequency analysis method you select depends on the requirements of the
 application. Consider the resolution, the negative values, the cross-term interference,
 and computation speed when you select a quadratic time-frequency analysis method.

The following table compares these properties of the quadratic time-frequency analysis methods in
 the Time Frequency Analysis Tools. In general, most applications use the STFT
 spectrogram and the Gabor spectrogram.

| Method | Resolution | Includes Negative Values? | Includes Cross-Term Interference? | Speed |
| --- | --- | --- | --- | --- |
| Short-Time Fourier Transform (STFT) spectrogram, including the STFT-based reassignment method | Coarse | No | No | Fast |
| Wigner-Ville Distribution (WVD) | Fine | Yes | Yes, strong | Fast |
| Choi-Williams Distribution (CWD) | Moderate | Yes | Suppresses cross-terms that two auto-terms with different time centers and frequency centers generate but does not suppress cross-terms that two auto-terms with the same time center or frequency center generate | Very slow |
| Cone-Shaped Distribution (CSD) | Moderate | Yes | Suppresses cross-terms that two auto-terms with different time centers and frequency centers generate but does not reduce cross-terms that two auto-terms with the same time center generate | Very slow |
| Gabor spectrogram | Fine | Yes | Minor when order is small | Moderate |
| Adaptive spectrogram | Best for signal of chirplets | No | No | Depends on signal length, number of components to extract |

The following figure shows the typical steps for creating applications for signal analysis,
 detection, and classification using the quadratic time-frequency analysis method
 VIs:

Figure 21.

[IMAGE alt='image' src='GUID-B57082D8-61A4-4565-AF3F-5FC41C7FB456-a5.gif']

You can use the Time Frequency Analysis VIs to compute the spectrogram of a
 signal, analyze the spectrogram directly, and then decide what step to take next. You
 also can use the spectrogram to compute other indexes, such as the MIF, the Mean
 Instantaneous Bandwidth (MIB), the group delay, and the marginal integration before
 deciding what step to take next.

- [STFT Spectrogram](stft-spectrogram.html)
- [Wigner-Ville Distribution](wigner-ville-distribution.html)
- [Other Cohen's Class Time Frequency Distributions](other-cohen-s-class-time-frequency-distributi.html)
- [Gabor Spectrogram](gabor-spectrogram.html)
- [Adaptive Spectrogram](adaptive-spectrogram.html)
- [Spectrogram Feature Extraction](spectrogram-feature-extraction.html)
- [Calculate the Energy of a Signal at Each Time Frequency Instant](calculate-the-energy-of-a-signal-at-each-ti.html)

Parent topic:

Time Frequency Analysis Concepts

Related concepts:

- Linear Time Frequency Analysis Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=user-defined-model-definitions-advanced-signa.html language=enus -->
## TOPIC 00147: User Defined Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `user-defined-model-definitions-advanced-signa.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/user-defined-model-definitions-advanced-signa.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If a general-linear polynomial, transfer function, zero-pole-gain, or state-space model cannot represent the model you want to estimate, you can define a model by revising a template VI.You can find template VIs in the \vi.lib\addons\System Identification\User-Defined Model Templates.llb. You then c

### User Defined Model Definitions

If a general-linear polynomial, transfer function, zero-pole-gain, or state-space model
 cannot represent the model you want to estimate, you can define a model by revising a
 template VI.

You can find template VIs in the \vi.lib\addons\System Identification\User-Defined
 Model Templates.llb. You then can estimate the model you define by using
 the SI Estimate User-Defined Model VI. This VI enables you to
 estimate some other model representations in addition to the general-linear, transfer
 function, zero-pole-gain, and state-space models that the System
 Identification VIs directly support. For example, you can use this VI to
 estimate nonlinear models. With this VI, you also can estimate linear models that you
 define early.

Parent topic:

Parametric Model Estimation Methods

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00148: LabVIEW Advanced Signal Processing Toolkit User Manual

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Advanced Signal Processing Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Re

### LabVIEW Advanced Signal Processing
 Toolkit
 User Manual

The LabVIEW Advanced Signal Processing
 Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=using-system-identification-vis-for-model-est.html language=enus -->
## TOPIC 00149: Using System Identification VIs for Model Estimation

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `using-system-identification-vis-for-model-est.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/using-system-identification-vis-for-model-est.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To apply the direct identification approach, you can use the System Identification VIs to estimate a dynamic system in a closed-loop system with general-linear polynomial, transfer function, and zero-pole-gain models.To apply the indirect or joint input-output approach to identify a dynamic system,

### Using System Identification VIs for Model
 Estimation

To apply the direct identification approach, you can use the System
 Identification VIs to estimate a dynamic system in a closed-loop system
 with general-linear polynomial, transfer function, and zero-pole-gain models.

To apply the indirect or joint input-output approach to identify a dynamic system, you can use
 this toolkit with transfer function models. Use the following guidelines when you
 estimate a dynamic system by using the System Identification VIs:

- Use the Parametric Model Estimation VIs to estimate ARX, ARMAX, output-error,
 Box-Jenkins, and general-linear models. For ARX models, the System
 Identification VIs use the least squares method, which is a special
 case of the prediction error method. For all other models, this toolkit uses the
 prediction error method. This method can accurately identify a dynamic system model
 in a closed-loop system. Hence, you can use the Parametric Model
 Estimation VIs to estimate the model of a dynamic system in a
 closed-loop system.
- Use the SI Estimate Transfer Function VI or the SI Transfer Function
 Estimation Express VI to estimate a transfer function model of the
 dynamic system in a closed-loop system. You can apply direct, indirect, and joint
 input-output identification to compute transfer function models.
- To identify zero-pole-gain models for a dynamic system, you first must identify the dynamic
 system by using other model representations. You then can convert other model
 representations to zero-pole-gain models using the Model
 Conversion VIs.

Parent topic:

Closed-Loop Systems Model Estimation Methods

Related concepts:

- Closed-Loop Systems Model Estimation Methods
- Parametric Model Estimation Methods
- Least Squares Method

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=validate-models-advanced-signal-processing.html language=enus -->
## TOPIC 00150: Validate Models

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `validate-models-advanced-signal-processing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/validate-models-advanced-signal-processing.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The best way to validate a model is to experiment with the model under real-world conditions.Model estimation determines the best model of the system within the chosen model structure. Model estimation does not determine if the model provides the most accurate description of the system. After you ob

### Validate Models

The best way to validate a model is to experiment with the model under real-world
 conditions.

Note

If the model works as you expect, the model estimation is successful. However, experimenting with
 the model under real-world conditions might be dangerous. For example, introducing
 arbitrary perturbations to the input of a chemical plant might lead to a harmful
 explosion. Therefore, before you incorporate the model into real-world applications,
 validate the model by using plots and common sense or by using statistical tests on the
 prediction error.

The System Identification VIs provide three of the most common validation
 methods—model simulation, model prediction, and model residual analysis. You can use any
 or all of these methods to validate the model. The method(s) you use depend on the
 purpose for which you created the model.

#### Model Simulation

Use model
 simulation to understand the underlying dynamic relationship between the model
 inputs and outputs. The SI Model Simulation VI determines the
 outputs of a system for given inputs. After you build a model for the system using
 the input and output data you measured, you can use the model to simulate the
 response of the system by using the model equations. You then can evaluate the
 behavior of the system. You also can use simulation to validate the model by
 comparing the simulated response with the measured response.

#### Model Prediction

Use model
 prediction to test the ability of the model to predict the response of the system
 using past input and output data. The SI Model Prediction VI
 determines the response of a system at time t based on the output
 information available at time t – k and all
 the inputs applied from time t – k to time
 t. k represents the size of the prediction
 window. Therefore, model prediction can determine how useful a model is in
 estimating future responses of the system, given all information at
 time t and an expected input profile in the future. Some
 control techniques take advantage of model prediction to improve control
 performance. For example, model predictive control uses some of the prediction
 properties of a model to determine if a particular limitation or constraint is
 active in the future. This method allows the controller to take preventive actions
 before such constraints become active.

If you have the measured input and
 output of a system, you also can validate the model of the system by comparing the
 predicted output and the measured output. If the prediction error is small, the
 model is acceptable.

#### Model Residual Analysis

Use
 model residual analysis to analyze the prediction error, which is the difference
 between the response that an estimated model predicts and the actual response from
 the system. The following equation defines the prediction error, also known as the
 residual e(k):

e

k

=

y

k

-

y

'

k

y(k) is the measured output and
 y'( k) is the output from the
 one-step-ahead prediction. If the model is capable of describing the dynamic system,
 the residual is zero-mean white noise and independent of the input signal. You can
 use autocorrelation analysis to test if the residual is zero-mean white noise. You
 can use cross-correlation analysis to test if the residual is independent of the
 input signal. The SI Model Residual Analysis VI calculates both
 the autocorrelation and the cross-correlation values.

#### Autocorrelation

The
 following equation defines the autocorrelation of the residuals:

R

e

N

τ

=

1

N

∑

k

-

1

N

e

k

e

k

-

τ

Ideally, the residual is white noise, and therefore the
 autocorrelation function
 R<sub>e</sub><sup>N</sup>(τ)
 is zero when τ is nonzero. A large autocorrelation when τ is nonzero indicates that
 the residual is not zero-mean white noise and also implies that the model structure
 is not relevant to the system or that you might need to increase the model
 order.

In real-world applications, the autocorrelation function
 R<sub>e</sub><sup>N</sup>(τ)
 cannot be zero when τ is nonzero because of the limited length of data points.
 However, the SI Model Residual Analysis VI assesses if the
 autocorrelation value is sufficiently small to be ignored. If the value of
 autocorrelation falls within the confidence range, the autocorrelation value is
 insignificant and you can consider this value to be equal to zero.

#### Cross Correlation

The
 following equation defines the cross correlation between residuals and past
 inputs:

R

e

u

N

τ

=

1

N

∑

k

-

1

N

e

k

u

k

-

τ

If the residual is independent of the input, the cross correlation is zero
 for all τ. If the residual correlates with the input, the cross correlation is
 nonzero, suggesting that the model did not capture all deterministic variations from
 the data. Therefore, you must revise the model variation.

The SI
 Model Residual Analysis VI assesses if the value of cross correlation
 is sufficiently small. If the value of cross correlation falls within the confidence
 range, the value is insignificant and you can consider this value to be equal to
 zero.

Parent topic:

Analyze, Validate, and Convert Models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=validating-the-arx-model-advanced-signal-proc.html language=enus -->
## TOPIC 00151: Validating the ARX Model

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `validating-the-arx-model-advanced-signal-proc.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/validating-the-arx-model-advanced-signal-proc.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the model orders found in the User-Defined Criterion section, you can simulate and predict the response of the system to determine whether or not the estimated model accurately reflects the actual system.You can compare these responses to the actual response and determine the accuracy of the e

### Validating the ARX Model

Using the model orders found in the User-Defined Criterion section, you can simulate and
 predict the response of the system to determine whether or not the estimated model
 accurately reflects the actual system.

You can compare these responses to the actual response and determine the accuracy of the
 estimated model. You also can analyze the residuals to determine the accuracy of the
 estimated model.

#### Simulation and
 Prediction

You can use the SI Model Simulation VI and
 SI Model Prediction VI to determine the accuracy of the
 estimated model. The SI Model Simulation VI simulates the system
 model and the SI Model Prediction VI performs a prediction of the
 system model. The results of the SI Model Prediction VI might
 differ from the SI Model Simulation VI because the SI
 Model Prediction VI periodically makes corrections to the estimated
 response based on the actual response of the system.

The following figure
 shows how you use these VIs to verify the ARX model created in the User-Defined
 Criterion section:

Figure 218.

[IMAGE alt='image' src='GUID-96CF749C-5965-488C-8C56-08E10597CC13-a5.gif']

The simulation and 1-step ahead
 prediction graphs enable you to visually determine how accurate the
 model is. The following figure shows the results of the simulation and prediction as
 well as the actual response of the system:

Figure 219.

[IMAGE alt='image' src='GUID-16E34976-0E28-4E1C-BCB0-DA03A922279B-a5.gif']

Notice how the actual response, or the measured response,
 is different from the simulated response in the
 simulation graph. The SI Model
 Simulation VI simulates the response of the system without considering
 the actual response of and the noise dynamics in the system.

#### Residual Analysis

In
 addition to simulation and prediction, you can perform a residual analysis to
 validate the system model. Residual analysis tests whether the prediction error
 correlates to the stimulus signal. Prediction errors are usually uncorrelated with
 all stimulus signals in an open-loop system.

The following block diagram shows
 how you can use the SI Model Residual Analysis VI with the ARX
 model identified in the User-Defined Criterion section to analyze the residuals:

Figure 220.

[IMAGE alt='image' src='GUID-CE27A281-20D9-459D-8D4A-31897F3FFA6A-a5.gif']

The following figure shows an example of ideal results where both autocorrelation
 and cross correlation are inside the confidence region except those in the vicinity
 of τ = 0. This result indicates that the estimated model accurately describes the
 system.

Figure 221.

[IMAGE alt='image' src='GUID-21862D3C-B191-42D5-A4B7-C6B64EF08CBF-a5.gif']

When you verify and validate the identified model, you must use multiple analysis
 techniques to determine if the estimated model accurately represents the system.
 Some analysis techniques can be misleading. For example, if you performed a residual
 analysis on the model identified in the Minimum Description Length Criterion
 section, you might conclude that this model is an accurate representation of the
 system. The following figure shows the autocorrelation and cross-correlation
 residual analysis for the model in the Minimum Description Length Criterion section.
 Recall that this model has the following orders:

- A order = 6
- B order = 6
- delay = 0

Figure 222.

[IMAGE alt='image' src='GUID-1D2991F7-3022-4B17-B63D-C9B20E76611D-a5.gif']

The previous figure shows that both the autocorrelation and cross correlation are
 inside the confidence region. Therefore, without performing any other analyses, you
 might conclude that this model is an accurate representation of the system. However,
 the pole-zero analysis in the Minimum Description Length Criterion section showed
 poles outside of the unit circle. So you already determined that this model is
 unstable. Thus, despite acceptable autocorrelation and cross-correlation values,
 concluding that this model is accurate is incorrect.

Thus, if you only
 performed a residual analysis, you might not discover that this model is actually
 unstable. When validating a model, perform multiple analyses to ensure the accuracy
 of the model.

Parent topic:

Flexible Arm Case Study

Related concepts:

- Validate Models
- ARX Model Definitions
- Determining Parameters for the Prediction Error Method

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=visually-inspect-the-data-advanced-signal.html language=enus -->
## TOPIC 00152: Visually Inspect the Data

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `visually-inspect-the-data-advanced-signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/visually-inspect-the-data-advanced-signal.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Visually inspecting the data is the best way to detect disturbances such as an abnormal pulse, a temporary sensor failure, or a transmitter failure.Unexpected events like these can corrupt the raw data samples. These disturbances can result in outliers, clipped saturation, and/or quantization effect

### Visually Inspect the Data

Visually inspecting the data is the best way to detect disturbances such as an abnormal
 pulse, a temporary sensor failure, or a transmitter failure.

Unexpected events like these can corrupt the raw data samples. These disturbances can result in
 outliers, clipped saturation, and/or quantization effects that severely distort the
 resulting model estimation.

In the following figure, you can recognize outliers by visually inspecting the data:

Figure 175.

[IMAGE alt='image' src='GUID-9043D08A-4104-4192-A622-D8C093F65650-a5.gif']

Note

Traditionally, you examine data samples either in the time domain or the frequency domain. An
 effective approach is to display the data in the joint time-frequency domain, which
 provides a better understanding about the measured signals. You must have the LabVIEW
 Advanced Signal Processing Toolkit installed to use the joint time-frequency domain.

Parent topic:

Preprocess Data from a System

Related concepts:

- Time Frequency Analysis Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=wavelet-analysis-concepts.html language=enus -->
## TOPIC 00153: Wavelet Analysis Concepts

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `wavelet-analysis-concepts.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/wavelet-analysis-concepts.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections describe the concepts in the LabVIEW Wavelet Analysis Tools.

### Wavelet Analysis Concepts

The following sections describe the concepts in the LabVIEW Wavelet Analysis
 Tools.

- [Introduction to Wavelet Signal Processing](introduction-to-wavelet-signal-processing.html)
- [Overview of LabVIEW Wavelet Analysis Tools](overview-of-labview-wavelet-analysis-tools.html)
- [Wavelet Signal Processing Application Areas](wavelet-signal-processing-application-areas.html)
- [Signal Processing with Continuous Wavelets](signal-processing-with-continuous-wavelets.html)
- [Signal Processing with Discrete Wavelets](signal-processing-with-discrete-wavelets.html)
- [Interactively Designing Discrete Wavelets](interactively-designing-discrete-wavelets.html)
- [Integer Wavelet Transform](integer-wavelet-transform.html)

Parent topic:

LabVIEW Advanced Signal Processing Toolkit Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=wavelet-packet-decomposition.html language=enus -->
## TOPIC 00154: Wavelet Packet Decomposition

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `wavelet-packet-decomposition.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/wavelet-packet-decomposition.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can approximate the Discrete Wavelet Transform (DWT) using filter banks. When the decomposition is applied to both the approximation coefficients and the detail coefficients, the operation is called wavelet packet decomposition.The following figure shows the wavelet packet decomposition tree:132

### Wavelet Packet Decomposition

You can approximate the Discrete Wavelet Transform (DWT) using filter banks. When the
 decomposition is applied to both the approximation coefficients and the detail
 coefficients, the operation is called wavelet packet decomposition.

The following figure shows the wavelet packet decomposition tree:

Figure 132.

[IMAGE alt='image' src='GUID-F7BBA390-2675-4A4D-A4E3-8A2654EE6FA5-a5.gif']

The numbers indicate the path of each node. The path is a combination of the characters
 0 and 1, where 0 represents
 lowpass filtering followed by a decimation with a factor of two, and
 1 represents highpass filtering followed by a decimation with a
 factor of two.

Based on the previous figure, you can represent a signal with different sets of sequences, or
 different decomposition schemes, such as (1, 01, 001, 000), (
 1, 00, 010, 011), or ( 000, 001, 010, 011, 100, 101,
 110, 111). As the decomposition level increases, the number of different
 decomposition schemes also increases.

The DWT is useful in compressing signals in some applications. The wavelet packet decomposition
 also can compress signals and provide more compression for a given level of distortion
 than the DWT does for some signals, such as signals composed of chirps.

For example, the wavelet packet decomposition and the DWT with the sym8 wavelet, decomposition
 level 4, and periodic extension are applied to the Piece Polynomial signal and the
 Chirps signal. The following figure shows the decomposition of the Piece Polynomial
 signal. The resulting histogram of the wavelet packet coefficients is similar to the
 histogram of the discrete wavelet coefficients, meaning that the DWT and the wavelet
 packet decomposition have similar compression performance for the Piece Polynomial
 signal.

Figure 133.

[IMAGE alt='image' src='GUID-7A9C00B0-81B8-4382-926B-1666C525D8FB-a5.gif']

The following figure shows the decomposition of the Chirps signal. The resulting histogram of the
 wavelet packet coefficients is more compact than the histogram of the DWT coefficients.
 Therefore, the wavelet packet decomposition can achieve a higher ratio for signals like
 the Chirps signal.

Figure 134.

[IMAGE alt='image' src='GUID-EBBA15C0-4F36-4F8F-AADF-2F4167542359-a5.gif']

#### Arbitrary Path
 Decomposition

Traditional wavelet packet decomposition iteratively applies
 the lowpass and highpass filters to both the approximation and the detail
 coefficients. The arbitrary path decomposition, as a special case of the wavelet
 packet decomposition, iteratively applies the lowpass and highpass filters to either
 the approximation or the detail coefficients at each level. You can consider
 arbitrary path decomposition as a band-pass filter, which you can implement by
 cascading filter banks. The following figure shows an example arbitrary path
 decomposition:

Figure 135.

[IMAGE alt='image' src='GUID-DD2CAE3B-CBB4-4F34-9D40-B7CA7CE0343D-a5.gif']

In this example, the decomposition path is 011, because the
 signal first enters a lowpass filter 0, then a highpass filter
 1, and finally a highpass filter 1 again.
 The results on the paths 1, 00, and
 010 also can be saved for reconstruction purpose. The paths
 1, 00, and 010 define
 residual paths.

Use the WA Arbitrary Path Decomposition VI
 and the WA Arbitrary Path Reconstruction VI to decompose and
 reconstruct a signal according to different paths and wavelet types.

The
 following figure shows an application of the arbitrary path decomposition in
 detecting engine knocking due to an ignition-system malfunction:

Figure 136.

[IMAGE alt='image' src='GUID-E4ECBBB0-225A-47E1-B922-DD2E80CB3E81-a5.gif']

This example applies the bior3_7 wavelet and the path 11 to the
 decomposition of the signal that the Engine Knocking Sound
 graph contains. The Enhanced Sound graph shows the signal
 reconstructed from the path 11. The high-amplitude components
 around 0.6, 0.8, and 1.0 in the Enhanced Sound graph indicate
 where the ignition malfunction of the engine occurs.

Parent topic:

Signal Processing with Discrete Wavelets

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=wavelet-signal-processing-application-areas.html language=enus -->
## TOPIC 00155: Wavelet Signal Processing Application Areas

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `wavelet-signal-processing-application-areas.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/wavelet-signal-processing-application-areas.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use wavelets in a variety of signal processing applications, such as analyzing signals at different scales, reducing noise, compressing data, and extracting features of signals.This section discusses these application areas by analyzing signals and images with the LabVIEW Wavelet Analysis To

### Wavelet Signal Processing Application Areas

You can use wavelets in a variety of signal processing applications, such as analyzing
 signals at different scales, reducing noise, compressing data, and extracting features
 of signals.

This section discusses these application areas by analyzing signals and images with the LabVIEW
 Wavelet Analysis Tools.

#### Multiscale Analysis

Multiscale analysis involves looking at a signal at different time and frequency
 scales. Wavelet transform-based multiscale analysis helps you understand both the
 long-term trends and the short-term variations of a signal simultaneously.

The following figure shows a multiscale analysis of a Standard & Poor's (S&P)
 500 stock index during the years 1947 through 1993. The S&P 500
 Index graph displays the monthly S&P 500 indexes. The other
 three graphs are the results of wavelet analysis. The Long-Term
 Trend graph is the result with a large time scale, which describes
 the long-term trend of the stock movement. The Short-Term
 Variation and Medium-Term Variation graphs
 describe the magnitudes of the short-term variation and medium-term variation,
 respectively.

Figure 108.

[IMAGE alt='image' src='GUID-3671F097-2163-434C-BD35-CE4C7E9C9B8A-a5.gif']

#### Noise Reduction

One of the most effective applications of wavelets in signal processing is denoising,
 or reducing noise in a signal. The wavelet transform-based method can produce much
 higher denoising quality than conventional methods. Furthermore, the wavelet
 transform-based method retains the details of a signal after denoising.

The following figure shows a signal with noise and the denoised signal using the
 wavelet transform-based method:

Figure 109.

[IMAGE alt='image' src='GUID-2D3CB76B-9E39-43B7-80B2-9005CA53F97C-a5.gif']

With the wavelet transform, you can reduce the noise in the signal in the
 Noisy Signal graph. The resulting signal in the
 Denoised Signal graph contains less noise and retains the
 details of the original signal.

#### Compression

In many applications, storage and transmission resources limit performance. Thus,
 data compression has become an important topic in information theory. Usually, you
 can achieve compression by converting a source signal into a sparse representation,
 which includes a small number of nonzero values, and then encoding the sparse
 representation with a low bit rate. The wavelet transform, as a time-scale
 representation method, generates large coefficients only around discontinuities. So
 the wavelet transform is a useful tool to convert signals to sparse
 representations.

#### Feature Extraction

Extracting relevant features is a key step when you analyze and interpret signals and
 images. Signals and images are characterized by local features, such as peaks,
 edges, and breakdown points. The wavelet transform-based methods are typically
 useful when the target features consist of rapid changes, such as the sound caused
 by engine knocking. Wavelet signal processing is suitable for extracting the local
 features of signals because wavelets are localized in both the time and frequency
 domains.

The following figure shows an image and the associated edge maps detected at
 different levels of resolutions using the wavelet transform-based method.
 Conventional methods process an image at a single resolution and return a binary
 edge map. The wavelet transform-based method processes an image at multiple levels
 of resolution and returns a series of grey-level edge maps at different
 resolutions.

Figure 110.

[IMAGE alt='image' src='GUID-789DA1E4-6FAE-4F06-AE86-E74EC1A0F534-a5.gif']

A large level value corresponds to an edge map with low resolution. You can obtain
 the global profile of the image in a low-resolution edge map and the detailed
 texture of the image in a high-resolution edge map. You also can form a
 multiresolution edge detection method by examining the edge maps from the low
 resolution to the high resolution. With the multiresolution edge detection method,
 you can locate an object of interest in the image reliably and accurately, even
 under noisy conditions.

Parent topic:

Wavelet Analysis Concepts

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=wigner-ville-distribution.html language=enus -->
## TOPIC 00156: Wigner-Ville Distribution

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `wigner-ville-distribution.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/wigner-ville-distribution.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Wigner-Ville Distribution (WVD) returns many useful signal properties for signal analysis, such as marginal properties, the mean instantaneous frequency, and the group delay. With the WVD is a quadratic time-frequency analysis method, you do not need to specify a window type like you do with the

### Wigner-Ville Distribution

The Wigner-Ville Distribution (WVD) returns many useful signal properties for
 signal analysis, such as marginal properties, the mean instantaneous
 frequency, and the group delay.

With the WVD is a quadratic time-frequency analysis method, you do not need to specify a window
 type like you do with the STFT spectrogram method. The WVD also has time and
 frequency shift invariance, which means that the components of two signals
 that are the time-shifted versions of each other look the same regardless of
 location in the time-frequency plane. The WVD is a Cohen's class method.

You can use the WVD on signals that have simple, widely separated signal components for which you
 require a fine time-frequency resolution for the corresponding time-frequency
 representation. The WVD also is a good choice when you want to extract signal features
 from a signal that contains only a single component.

Use the TFA Wigner-Ville Distribution VI to compute the WVD.

#### Cross-Term Interference

One serious disadvantage of the WVD is cross-term interference. Cross-terms are
 artifacts that appear in the WVD representation between auto-terms, which correspond
 to physically existing signal components. These cross-terms falsely indicate the
 existence of signal components between auto-terms.

The following figure shows the WVD of the example frequency hopper signal. This
 signal has four auto-terms. Each component has a different time center and a
 different frequency center.

Figure 28.

[IMAGE alt='image' src='GUID-1B380D21-8EC4-4CA0-83BF-1B81BCC5D881-a5.gif']

1

Compared to the ideal time-frequency representation of the hopper signal, the
 previous figure includes many signal components that do not correspond to the four
 auto-terms. These artifacts are the cross-terms. Notice that the cross-terms are
 strongest at the midpoints between the auto-terms and that the cross-terms have a
 higher peak magnitude than the auto-terms. The cross-terms also oscillate, or form
 bands in the time-frequency domain, with the band spacing proportional to the
 distance between the auto-terms. In general, as the number of auto-terms increases,
 the auto-terms and the cross-terms overlap. Consequently, distinguishing the
 auto-terms from cross-terms can be challenging.

The time-frequency plane includes positive frequencies and negative frequencies.
 Signal components present at positive frequencies in real-valued signals, such as
 the example frequency hopper signal, have mirrored, symmetric components at negative
 frequencies. The example frequency hopper signal contains four signal components at
 positive frequencies and four corresponding signal components at negative
 frequencies, which are not shown. The cross-terms appear between auto-terms at
 positive frequencies, between auto-terms at negative frequencies, and between
 auto-terms at positive and negative frequencies.

In the previous example frequency hopper signal, if you convert this real-valued
 signal into a complex-valued analytic signal by removing the auto-terms at negative
 frequencies before you apply the WVD, you can reduce the number of cross-terms in
 the WVD, as shown in the following figure.

Figure 29.

[IMAGE alt='image' src='GUID-ACFA2233-EF0B-4BCF-A6A5-C543EDAF2C41-a5.gif']

1

Notice that in contrast to the figure of the WVD of the hopper signal, no cross-terms
 appear near the horizontal axis in the previous figure. The analytic frequency
 hopper signal example has the same spectral content at positive frequencies as the
 original, real-valued signal but has no spectral content at negative frequencies. By
 converting the real-valued signal to an analytic signal, you remove the cross-terms
 between auto-terms at negative frequencies and the cross-terms between auto-terms at
 positive frequencies and negative frequencies.

In addition to converting real-valued signals to analytic signals to reduce
 cross-terms in the WVD, you can use other Cohen's class methods and the Gabor
 expansion-based spectrogram, also called the Gabor spectrogram, to reduce cross-term
 interference. The Gabor spectrogram is a method unique to the LabVIEW Time Frequency
 Analysis Tools.

Parent topic:

Quadratic Time Frequency Analysis Methods

Related concepts:

- Overview of LabVIEW Time Frequency Analysis Tools
- Short-Time Fourier Transform
- Spectrogram Feature Extraction
- Gabor Spectrogram

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit path=zero-pole-gain-model-definitions-advanced-sig.html language=enus -->
## TOPIC 00157: Zero-Pole-Gain Model Definitions

- bundle_id: `labview-advanced-signal-processing-toolkit`
- source_path: `zero-pole-gain-model-definitions-advanced-sig.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit/raw/resource/enus/zero-pole-gain-model-definitions-advanced-sig.html
- document_id: `labview-advanced-signal-processing-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you rewrite the equations for the transfer function model to show the locations of the zeros and poles of the dynamic system, you obtain the zero-pole-gain model. SISOThe following is the equation for the continuous zero-pole-gain SISO model: G s = k s - Z 1 s - Z 2 . . . s - Z m s - P 1 s - P 1

### Zero-Pole-Gain Model Definitions

If you rewrite the equations for the transfer function model to show the locations of
 the zeros and poles of the dynamic system, you obtain the zero-pole-gain model.

#### SISO

The following is the
 equation for the continuous zero-pole-gain SISO model:

G

s

=

k

s

-

Z

1

s

-

Z

2

.

.

.

s

-

Z

m

s

-

P

1

s

-

P

1

.

.

.

s

-

P

n

where

- s is the Laplace variable and continuous time
- k is the transfer function gain
- Z i are the zeros
- P j are the poles

The following is the equation for the discrete-time zero-pole-gain SISO
 model:

G

z

=

k

z

-

Z

1

z

-

Z

2

.

.

.

z

-

Z

m

z

-

P

1

z

-

P

1

.

.

.

z

-

P

n

where z is discrete time

When s
 or z equals 0, you can calculate the static gain from the two
 equations.

s

t

a

t

i

c

g

a

i

n

=

-

1

m

-

n

k

z

1

z

2

.

.

.

z

m

P

1

P

2

.

.

.

P

n

#### MISO

The following is the
 equation for the continuous zero-pole-gain MISO model:

y

i

=

∑

f

=

1

n

G

i

f

s

u

j

where

- G ij are the transfer functions
 between the stimulus and the response
- i is the input number of the system
- j is the output number of the system

The following is the equation for the discrete-time zero-pole-gain MISO
 model:

y

i

=

∑

j

=

1

n

G

i

j

s

u

j

The System Identification VIs do not include a VI to
 estimate zero-pole-gain models directly because you can use the SI Model
 Conversion VI to convert another model representation to a
 zero-pole-gain model.

Parent topic:

Parametric Model Estimation Methods

Related concepts:

- Converting Models
