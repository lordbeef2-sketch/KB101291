# NI DOCUMENT BUNDLE: labview-advanced-signal-processing-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-advanced-signal-processing-toolkit-api-ref start=1 end=146 -->
<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_complex_cepstrum.html language=enus -->
## TOPIC 00001: Estimating the Complex Cepstrum of a Time Series (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_complex_cepstrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_complex_cepstrum.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Estimating the Complex Cepstrum of a Time Series (Advanced Signal Processing Toolkit)

Unlike the [real cepstrum](aspt_real_cepstrum.html), the complex cepstrum of a time series preserves the phase information of the original time series. Therefore, you can reconstruct the original time series from the power cepstrum. The complex cepstrum is useful in noise reduction, signal separation, and cepstral filtering.

Use the [TSA Complex Cepstrum](../lvtimeseriestk/tsa_complex_cepstrum.html) VI to compute the complex cepstrum of a time series. Use the [TSA Inverse Complex Cepstrum](../lvtimeseriestk/tsa_invs_cmplx_cepstrum.html) VI to reconstruct a time series from the complex cepstrum.

The following figure shows an example of removing echoes from a time series by processing the complex cepstrum. In this example, the original signal consists of three signal components: a decaying sinusoid starting at time 0, added with two distinct echoes of that signal later in time, as shown in the **Signal with Echoes** graph.

[IMAGE alt='image' src='fp_tsa_complex_cepstrum.gif']

As the previous figure shows, you can remove echoes from a time series using the following steps:

- Compute the complex cepstrum of the original time series using the TSA Complex Cepstrum VI. The peaks appearing in the Complex Cepstrum graph indicate the echo locations.
- Remove the peaks corresponding to the echoes from the complex cepstrum by setting the peak values to zero. The Peak-Removed Complex Cepstrum graph shows that the peaks have been removed.
- Reconstruct the original time series from the modified complex cepstrum using the TSA Inverse Complex Cepstrum VI. In the Reconstructed Signal graph, you can see that the reconstructed time series does not contain echoes.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_default_page.html language=enus -->
## TOPIC 00002: Advanced Signal Processing Toolkit

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_default_page.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_default_page.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Advanced Signal Processing Toolkit

June 2014, 372656C-01

The LabVIEW Advanced Signal Processing Toolkit includes the LabVIEW Time Frequency Analysis Tools, LabVIEW Time Series Analysis Tools, and LabVIEW Wavelet Analysis Tools. These tools are a suite of high-level signal processing VIs that you can use to perform time frequency, time series, and wavelet analysis. To extract the underlying information of a signal effectively, you need to choose an appropriate analysis tool. The following table describes the tasks you can perform by using the different advanced signal processing tools.

| Signal Type | Tool | Task |
| --- | --- | --- |
| Evolutionary | Time Frequency Analysis Tools | The Time Frequency Analysis Tools provide VIs and Express VIs for linear and quadratic time-frequency analysis methods, including the linear discrete Gabor transform and expansion, the linear adaptive transform and expansion, the quadratic Gabor spectrogram, and the quadratic adaptive spectrogram. The Time Frequency Analysis Tools also include VIs to extract features from a signal, such as the mean instantaneous frequency, the mean instantaneous bandwidth, the group delay, and the marginal integration. |
| Stationary | Time Series Analysis Tools | The Time Series Analysis Tools provide VIs for preprocessing signals, estimating the statistical parameters of signals, building models of signals, and estimating the power spectrum, the high-order power spectrum, and the cepstrum of signals. |
| Evolutionary and transient | Wavelet Analysis Tools | The Wavelet Analysis Tools provide VIs and Express VIs for continuous wavelet transform, discrete wavelet transform, undecimated wavelet transform, integer wavelet transform, and wavelet packet decomposition. The Wavelet Analysis Tools also include VIs for feature extraction applications, such as denoising, detrending, and detecting peaks and edges. |

The Advanced Signal Processing Toolkit also contains the [System Identification](../lvsysid/lv_sysid_pal.html) VIs. Use these VIs to identify large, multivariable models of high-order systems from large amounts of data.

|  | Note The Advanced Signal Processing Toolkit also contains the LabVIEW Digital Filter Design Toolkit. Use the Digital Filter Design Toolkit to perform signal analysis on stationary signals. |
| --- | --- |

This help file contains:

- System Identification Concepts —An overview of the System Identification VIs and conceptual information that you need to understand before using the System Identification VIs.
- System Identification VIs —Detailed information about the System Identification VIs.
- Time Frequency Analysis Concepts —An overview of the Time Frequency Analysis Tools and conceptual information that you need to understand before using the Time Frequency Analysis Tools.
- Time Frequency Analysis Reference —Detailed information about the Time Frequency Analysis VIs.
- Time Series Analysis Concepts —An overview of the Time Series Analysis Tools and conceptual information that you need to understand before using the Time Series Analysis Tools.
- Time Series Analysis Reference —Detailed information about the Time Series Analysis VIs.
- Wavelet Analysis Concepts —An overview of the Wavelet Analysis Tools and conceptual information that you need to understand before using the Wavelet Analysis Tools.
- Wavelet Analysis Reference —Detailed information about the Wavelet Analysis VIs.

© 2009–2014 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_exponential_prediction.html language=enus -->
## TOPIC 00003: Exponential Smoothing Prediction (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_exponential_prediction.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_exponential_prediction.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Exponential Smoothing Prediction (Advanced Signal Processing Toolkit)

Exponential smoothing prediction builds an exponential smoothing model for a time series and then predicts the future values of the time series based on the model. Exponential smoothing prediction is suitable for a time series that contains trends and seasonal variations.

Use the [TSA Exponential Prediction](../lvtimeseriestk/tsa_exponential_prediction.html) VI to predict the future values of univariate or multivariate time series based on exponential smoothing.

The following figure shows an example of performing exponential smoothing prediction on a simulated sales record.

[IMAGE alt='image' src='fp_tsa_exponential_prediction.gif']

The **Sales Record** graph contains a univariate time series of a sales record for a certain product. This example splits the time series into two parts—one part for modeling and the other part for comparison—and specifies the following settings for prediction:

- Sets Exponential Type to Triple because the sales record contains a systematic trend and seasonality.
- Sets Season Type to Multiplicative because the amplitude of the sales record increases over time.
- Sets Season Period to 4 because the sales record contains four points in each oscillation period.

The **Prediction Result** graph in the previous figure shows the **Predicted Record** plot matches the **Real Record** plot.

Refer to the Exponential Prediction VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example that demonstrates how to forecast the future values of a univariate time series based on the exponential smoothing.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_extending_signals.html language=enus -->
## TOPIC 00004: Extending Signals (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_extending_signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_extending_signals.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Extending Signals (Advanced Signal Processing Toolkit)

|  | Note This topic contains information that applies to the LabVIEW Time Frequency Analysis Tools and the LabVIEW Wavelet Analysis Tools. |
| --- | --- |

Signal extension methods pad the borders of a signal to lessen discontinuity that might exist at the beginning and end of the signal. The Time Frequency Analysis Tools and Wavelet Analysis Tools provide the following three extension methods.

- Zero —Uses zeros to pad the borders of a signal.
- Symmetric —Replicates a signal to pad the borders of that signal. The symmetric extension method left-flips the signal replication at the beginning of the signal and right-flips the signal replication at the end of the signal.
- Periodic —Replicates a signal to pad the borders of that signal. The periodic extension method adds a signal replication before the signal and another signal replication after the signal.

The following figure shows a linear chirp signal and the extended versions of this signal with the zero, symmetric, and periodic padding methods.

[IMAGE alt='image' src='extensions.gif']

In the previous figure, the linear chirp signal appears from 100 s to 355 s. Notice the appearance of the extended signal when different extension methods pad the signal before 100 s and after 355 s.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_fundamentals.html language=enus -->
## TOPIC 00005: Fundamentals (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_fundamentals.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Fundamentals (Advanced Signal Processing Toolkit)

Refer to the following help topics to learn about concepts in the LabVIEW Advanced Signal Processing Toolkit.

- Categorizing Signals
- Extending Signals
- Analytic Signals
- Central Time and Central Frequency

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_music.html language=enus -->
## TOPIC 00006: Using the MUSIC Method (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_music.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_music.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using the MUSIC Method (Advanced Signal Processing Toolkit)

The multiple signal classification (MUSIC) method is a [model-based spectral estimation](tsa_model-based.html) method. The MUSIC method offers higher frequency resolution in the resulting power spectral density (PSD) than the fast Fourier transform (FFT)-based methods. However, the MUSIC method computes PSD magnitudes that generally are not proportional to the true PSD. Therefore, the PSD that the MUSIC method computes traditionally is known as the pseudo PSD.

Assuming that a time series can be represented by a series of complex sinusoids with additive white noise, the MUSIC method first computes the correlation matrix *R<sub>p</sub>* of the time series and obtains the eigenvectors *V*<sub>1</sub>, *V*<sub>2</sub>, ..., *V<sub>p</sub>* and eigenvalues λ<sub>1</sub>, λ<sub>2</sub>, ..., λ*<sub>p</sub>*. The eigenvectors *V*<sub>1</sub>, *V*<sub>2</sub>, ..., *V<sub>M</sub>* with large eigenvalues form the signal subspace. The remaining eigenvectors *V**<sub>M</sub>*<sub>+1</sub>, *V**<sub>M</sub>*<sub>+2</sub>, ..., *V**<sub>p</sub>* form the noise subspace. The signal subspace also can be represented by group vectors of complex sinusoids *e*(*f*<sub>1</sub>), *e*(*f*<sub>2</sub>), ..., *e*(*f<sub>M</sub>*). The vector of a complex sinusoid is defined as follows:

[IMAGE alt='image' src='eq_complex_sinusoid_vector.gif']

If a time series contains a frequency component at *f<sub>i</sub>*, the vector *e*(*f<sub>i</sub>*) is uncorrelated with *V**<sub>M</sub>*<sub>+1</sub>, *V**<sub>M</sub>*<sub>+2</sub>, ..., *V<sub>p</sub>*. Accordingly, the following equation generates a peak value at *f<sub>i</sub>*:

[IMAGE alt='image' src='eq_psd_peaks.gif']

|  | Note A power spectral density (PSD) normally gives a good indication of the attributes of spectral components contained in a time series. However, the peaks in the PSD computed with the MUSIC method just indicate the frequency locations of components in a time series. These peaks occur when the denominator of the previous equation reaches zero. Therefore, the magnitude of each peak does not indicate the spectral power at the corresponding frequency. |
| --- | --- |

A modified MUSIC method uses the eigenvalues λ<sub>1</sub>, λ<sub>2</sub>, ..., λ*<sub>p</sub>* as a weighting vector to compute the PSD as follows:

[IMAGE alt='image' src='eq_psd_music.gif']

The modified MUSIC method, which also is called the Eigenvector method, can reduce the variance in the estimated PSD.

When using the MUSIC method, you must specify the size of the noise subspace, which is defined as *p*–*M*. In general, you can specify a rough percentage of the whole space for the size of the noise subspace. With a large size of the noise subspace, you can obtain a smooth PSD but the resulting PSD may miss weak spectral peaks in the signal. With a small size of the noise subspace, you can obtain a detailed PSD that reveals weak spectral peaks. However, a too small size for the noise subspace leads to spurious peaks in the resulting PSD. Refer to the [Discrete Random Signals and Statistical Signal Processing](../lvasptconcepts/aspt_related_doc.html) book for more information about using the MUSIC method.

Use the [TSA MUSIC](../lvtimeseriestk/tsa_music.html) VI to compute the PSD of a time series with the MUSIC method.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_stft.html language=enus -->
## TOPIC 00007: Short-Time Fourier Transform (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_stft.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_stft.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Short-Time Fourier Transform (Advanced Signal Processing Toolkit)

The [discrete Fourier transform](/csh?topicname=lvanlsconcepts/discrete_fourier_transform.html) expresses a signal as a sum of sinusoids. Because the time duration of the sinusoids is infinite, the discrete Fourier transform of the signal reflects the spectral content of an entire signal over time but does not indicate when the spectral content occurs. However, in some cases, evaluating the spectral content of a signal over a short time scale can be useful. You can use the STFT to evaluate spectral content over short time scales.

The STFT, also called the windowed Fourier transform or the sliding Fourier transform, partitions the time-domain input signal into several disjointed or overlapped blocks by multiplying the signal with a [window function](/csh?topicname=lvanlsconcepts/windowing_signals.html) and then applies the discrete Fourier transform to each block. Window functions, also called sliding windows, are functions in which the amplitude tapers gradually and smoothly toward zero at the edges. Because each block occupies different time periods, the resulting STFT indicates the spectral content of the signal at each corresponding time period. When you move the sliding window, you obtain the spectral content of the signal over different time intervals. Therefore, the STFT is a function of time and frequency that indicates how the spectral content of a signal evolves over time. A complex-valued, 2-D array called the STFT coefficients stores the results of windowed Fourier transforms. The magnitudes of the STFT coefficients form a magnitude time-frequency spectrum, and the phases of the STFT coefficients form a phase time-frequency spectrum.

The STFT is one of the most straightforward approaches for performing time-frequency analysis and can help you easily understand the concept of time-frequency analysis. The STFT is computationally efficient because it uses the [fast Fourier transform (FFT)](/csh?topicname=lvanlsconcepts/fft_fundamentals.html).

Without taking special care, however, the STFT is not invertible, meaning you cannot reconstruct the time-domain waveform from the STFT of a signal. For example, if you step the sliding window of the STFT without overlap, you cannot reconstruct the signal in the time domain from the STFT. The [discrete Gabor transform](tfa_discrete_gabor_trans_exp.html) is a special case of the STFT and is a kind of invertible algorithm. The inverse of the discrete Gabor transform is called the [discrete Gabor expansion](tfa_discrete_gabor_trans_exp.html).

You can use the linear STFT method when you need the phase spectrum or when you do not need signal reconstruction. For example, the phase spectrum might be helpful in automatic speech-recognition applications. If you need only the magnitude spectrum in an application, use the quadratic [STFT spectrogram](aspt_stft_spectrogram.html) method, which is the square of the linear STFT. The STFT spectrogram is one of the most popular [quadratic time-frequency analysis methods](tfa_quadratic.html) because of its simplicity.

Use the [TFA STFT](../lvtimefreqtk/tfa_stft.html) VI to compute the STFT.

#### Window Type and Window Length

The time-frequency resolution of the STFT usually is defined as the product of the time resolution and the frequency resolution. The type of window you use affects the time-frequency resolution of the STFT. The [Gaussian window](/csh?topicname=lvanlsconcepts/lvac_gaussian_window.html) has the optimal time-frequency resolution.

The window length also affects the time resolution and the frequency resolution of the STFT. A narrow window results in a fine time resolution but a coarse frequency resolution because narrow windows have a short time duration but a wide bandwidth. A wide window results in a fine frequency resolution but a coarse time resolution because wide windows have a long time duration but a narrow frequency bandwidth. This phenomenon is called the window effect. You cannot obtain a fine time resolution and a fine frequency resolution simultaneously using the STFT. With a time-invariant window, the STFT has the same time resolution and frequency resolution across the entire time-frequency plane.

If you need an adaptive time resolution and frequency resolution, use the [adaptive transform](tfa_adapt_trans_exp.html) or [wavelet transform](wa_intro.html#wavelet_transform) in the LabVIEW Wavelet Analysis Tools.

The best window length depends on the characteristics of the signal you want to analyze. The window length should be small enough so that the windowed signal block is essentially stationary over the window interval and large enough so that the Fourier transform of the windowed signal block provides a reasonable frequency resolution. If the spectral content of the signal evolves over time slowly, which does not require a fine time resolution, set the window length large. If the spectral content of the signal changes relatively quickly, which requires a fine time resolution, set the window length small. For example, in speech signal processing, a time-domain window length of 25 ms is common.

The step size of the sliding window determines if overlap exists. If the step size is smaller than the window length, overlap exists. If the step size is greater than the window length, no overlap exists. Overlap of the sliding window makes the STFT smoother along the time axis. However, overlap requires more computation time and memory. If the signal length is large and the spectral content evolves slowly, it is not necessary to overlap the sliding window. If the signal length is small, overlap the sliding window to obtain a smoother STFT.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_stft_spectrogram.html language=enus -->
## TOPIC 00008: STFT Spectrogram (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_stft_spectrogram.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_stft_spectrogram.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### STFT Spectrogram (Advanced Signal Processing Toolkit)

The short-time Fourier transform (STFT) spectrogram is the normalized, squared magnitude of the STFT coefficients produced by the [STFT](aspt_stft.html). Normalization makes the STFT spectrogram obey [Parseval's energy-conservation property](/csh?topicname=lvanlsconcepts/lvac_parseval_s_theorem.html), meaning that the energy in the STFT spectrogram equals the energy in the original time-domain signal. All the quadratic time-frequency analysis methods in the [LabVIEW Time Frequency Analysis Tools](tfa_overview.html) adhere to Parseval's energy-conservation property.

The STFT spectrogram, a Cohen's class method, can be a good first choice for a quadratic time-frequency analysis method because this method is simple and fast. With the STFT spectrogram, you can infer if a signal is reasonably oversampled by looking for a low energy density at high frequencies in the STFT spectrogram. You also can estimate the spectral content of a signal and how the spectral content evolves over time by seeing where the energy is concentrated in the STFT spectrogram. However, other quadratic time-frequency analysis methods can provide superior time-frequency resolution. You can experiment with other methods in the [Time Frequency Spectrogram](../lvtimefreqtk/time_frequency_representation.html) Express VI to see if the STFT spectrogram unacceptably blurs the signal components you want to analyze.

When you have large data sets or when you do not need special features of the spectrogram, such as a fine time-frequency resolution, consider using the STFT spectrogram because it is fast and easy to use.

Use the [TFA STFT Spectrogram](../lvtimefreqtk/tfa_stft_spectrogram.html) VI to compute the STFT spectrogram.

#### Window Type and Window Length

The STFT spectrogram usually is sufficient for most applications, but it typically provides a coarse time-frequency resolution as a result of window effects that the window type and the window length determine. A narrow window results in a fine time resolution but a coarse frequency resolution because narrow windows have a short time duration but a wide bandwidth. A wide window results in a fine frequency resolution but a coarse time resolution because wide windows have a long time duration but a narrow frequency bandwidth. You cannot obtain a fine time resolution and a fine frequency resolution simultaneously by using the STFT spectrogram.

##### Selecting an Appropriate STFT Spectrogram Window Length

The following figure shows a frequency hopper signal, commonly used in spread-spectrum communication systems, such as CDMA cell phones.

[IMAGE alt='image' src='fp_tfa_freq_hopper_signal.gif']

The following figure shows the ideal quadratic time-frequency representation of the example frequency hopper signal in the previous figure.

[IMAGE alt='image' src='fp_tfa_ideal_tf_rep_hop_sig.gif']

In the previous figure, the ideal representation of the frequency of the signal remains constant and then immediately switches to another frequency. The following figure shows the STFT spectrogram of the example frequency hopper signal with a window length of 128.

[IMAGE alt='image' src='fp_tfa_stft_spec_hop_sig_wl128.gif']

Compared to the ideal time-frequency representation, the energy distribution of the signal in the previous figure is not confined to narrow lines. The STFT spectrogram in the previous figure is blurry as a result of the window effects of the STFT. This blurriness is a manifestation of the coarse time-frequency resolution of the STFT spectrogram. The window length and the window type determine how the energy blurs across time and frequency and thus determine the time resolution and the frequency resolution of the STFT spectrogram. For example, a wider window length can reduce energy blurring across frequencies at the expense of increased blurring across time. A narrower window length can reduce blurring across time at the expense of increased blurring across frequencies. The following figure shows the STFT spectrogram of the example frequency hopper signal with a window length of 32.

[IMAGE alt='image' src='fp_tfa_stft_spec_hop_sig_wl32.gif']

Relative to the STFT spectrogram of the frequency hopper signal with a window length of 128, the energy distribution of the signal in the previous figure is more spread out along the frequency axis and is more compact along the time axis, which means that the STFT spectrogram has a coarser frequency resolution but a finer time resolution when the window length is narrow.

The following figure shows the STFT spectrogram of the example frequency hopper signal with a window length of 256.

[IMAGE alt='image' src='fp_tfa_stft_spec_hop_sig_wl256.gif']

Relative to the spectrogram of the frequency hopper signal with a window length of 128, the energy distribution of the signal in the previous figure is more spread out along the time axis and is more compact along the frequency axis, which means that the STFT spectrogram has a coarser time resolution but a finer frequency resolution when the window length is wide.

Refer to the Time-Frequency Resolution VI in the labview\examples\Time Frequency Analysis\TFAGettingStarted directory for an example that demonstrates the window effects of the STFT spectrogram.

#### Reassignment Method

You can use the reassignment method to improve the time-frequency resolution of the STFT spectrogram artificially. The reassignment method automatically compresses the energy in the quadratic time-frequency representation toward the centers of gravity of the signal components to make the signal components more concentrated. The reassignment method uses the assumption that the energy of the signal components in the time-frequency representation is tightly concentrated. Using the reassignment method can help improve the time-frequency resolution of time-frequency concentrated components. However, the reassignment method also can bias the location of spectral peaks, merge distinct spectral components, falsely split compact signal components, or excessively sharpen naturally blurry signal components in the resulting time-frequency representation. The following figure shows the reassigned STFT spectrogram of the example frequency hopper signal.

[IMAGE alt='image' src='fp_tfa_reassigned_stft_spectrogram.gif']

Notice that the signal components in the reassigned STFT spectrogram in the previous figure are less blurry in time and frequency than the STFT spectrograms in the figures of the frequency hopper signal with a window length of 128, 32, and 256. Thus, this reassigned STFT spectrogram has a better time-frequency resolution.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/aspt_welch.html language=enus -->
## TOPIC 00009: Using the Welch Method (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/aspt_welch.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/aspt_welch.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using the Welch Method (Advanced Signal Processing Toolkit)

The Welch method reduces the variance of the [periodogram](aspt_periodogram.html) method by averaging. This method first divides a time series into overlapping subsequences by applying a window to each subsequence and then averaging the periodogram of each subsequence.

The length of the applied window controls the trade-off between bias and variance of the resulting power spectral density (PSD). The following figure shows the resulting PSD for a signal from a system with two pairs of poles at about 0.17 and 0.21 Hz, when the window length is 2048 and 128 for the top and bottom plots, respectively.

[IMAGE alt='image' src='fp_tsa_psd_welch.gif']

In the **PSD (Window = 2048)** graph, a large window generates a PSD with small bias in the locations of the two peaks, as you can see that the magnitudes of the peaks in the **Estimated PSD** plot almost equal the magnitudes of the peaks in the **Ideal PSD** plot. However, a large window results in a coarse PSD plot, as shown by the general fuzziness in the **Estimated PSD**plot.

In the **PSD (Window = 128)** graph, you can see that a small window generates a smooth **Estimated PSD** plot. However, a small window can lead to large bias, as you can see that the magnitudes of the peaks in the **Estimated PSD** plot are different from the magnitudes of the peaks in the **Ideal PSD** plot.

Use the [TSA Welch](../lvtimeseriestk/tsa_welch.html) VI to compute the PSD of a time series.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/categorizing_signals.html language=enus -->
## TOPIC 00010: Categorizing Signals (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/categorizing_signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/categorizing_signals.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Categorizing Signals (Advanced Signal Processing Toolkit)

In signal processing, you usually categorize signals into the following types:

- Stationary —For stationary signals, you assume that the spectral content of stationary signals does not change as a function of time, space, or some other independent variable. For example, you might work under the assumption that an engine vibration signal is stationary when an engine is running at a constant speed.
- Nonstationary —For nonstationary signals, you assume that the spectral content changes over time, space, or some other independent variable. For example, you might work under the assumption that an engine vibration signal is nonstationary when an engine is revving up or down. You can categorize nonstationary signals into the following types according to how the spectral content changes over time.
  - Evolutionary —The spectral contents of evolutionary signals change over time slowly. Evolutionary signals usually contain time-varying harmonics. The time-varying harmonics relate to the underlying periodic time-varying characteristic of the system that generates signals. Evolutionary signals also can contain time-varying broadband spectral contents.
  - Transient —Transient signals are the short-time events in a nonstationary signal, such as peaks, edges, breakdown points, and start and end of bursts. Transient signals usually vary over time and you typically cannot predict the occurrence exactly.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/cont_wavelets.html language=enus -->
## TOPIC 00011: Signal Processing with Continuous Wavelets (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/cont_wavelets.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/cont_wavelets.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Signal Processing with Continuous Wavelets (Advanced Signal Processing Toolkit)

You can use continuous wavelet tools to perform [wavelet transforms](wa_intro.html#wavelet_transform) on signals that are defined in continuous time. Unlike [discrete wavelet](wa_discrete.html) tools, which operate on sampled-data signals, continuous wavelet tools operate on signals that are defined for all time over a time region of interest, though the computations are done numerically in discrete time.

The LabVIEW Wavelet Analysis Tools provide two continuous wavelet tools: the [continuous wavelet transform (CWT)](wa_cwt.html) and the [analytic wavelet transform (AWT)](wa_awt.html). The AWT retains both the magnitude and phase information of signals in the time-scale or time-frequency domain, whereas the CWT retains only the magnitude information. The CWT is simpler because the results of the CWT are real values if both the wavelet and the signal are real. The results of the AWT normally are complex values.

From a mathematical point of view, both the CWT and AWT add informational redundancy because the number of the resulting wavelet coefficients in the time-scale or time-frequency domain is larger than the number of time samples in the original signal. Excess redundancy generally is not desirable because more computations and more memory are required to process signals with excess redundancy. However, excess redundancy can be helpful for some applications, such as singularity and cusp extraction, time-frequency analysis of nonstationary signals, and self-similarity analysis of fractal signals.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/designing_fbi_wavelet.html language=enus -->
## TOPIC 00012: Example: Designing the FBI Wavelet (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/designing_fbi_wavelet.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/designing_fbi_wavelet.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Example: Designing the FBI Wavelet (Advanced Signal Processing Toolkit)

Different [signal processing applications](wa_application.html) require different properties of wavelets. For image compression, you need a wavelet that is smooth, linear phase, and orthogonal. However, you cannot achieve all those properties simultaneously. One thing you can do is to ensure smoothness (higher order) and linear phase first and then pursue near-orthogonality.

Using the [Wavelet Design](../lvwavelettk/wavelet_design.html) Express VI, you can design a wavelet with specific properties. For example, you can complete the following steps to design the FBI wavelet, which is linear phase and near-orthogonal.

1. Add the Wavelet Design Express VI on the block diagram. The Configure Wavelet Design dialog box automatically launches.
 [IMAGE alt='image' src='add.gif'] Add
2. Select Biorthogonal as the Wavelet Type because only biorthogonal wavelets have the linear-phase property.
3. In the Product of lowpass (G0*H0) section, select Maxflat as the P0 type and set the value of Zero pairs at (P0) to 4 . 
 When you set parameters on the left-hand side of the configuration dialog box, plots of the designed wavelet and the associated filter banks interactively appear on the right-hand side.
4. In the Factorization (Type of G0) section, select Linear Phase as the Filter type and set the value of Zeros at (G0) to 4 because the wavelet must be near-orthogonal, meaning that G 0 ( z ) and H 0 ( z ) have the same or almost the same amount of zeros. By setting the value of Zeros at (G0) to 4 , you can ensure that both G 0 ( z ) and H 0 ( z ) have the same amount of zeros at . 
 The following figure shows the zeros of G 0 ( z ) and H 0 ( z ).
 [IMAGE alt='image' src='zeroes.gif'] 
 In the previous figure, notice that besides the four zeros assigned to H 0 ( z ) at π, the Zeros of G0 and H0 graph also contains six more zeros that belong to H 0 ( z ). Note that two zeros are on the negative half plane and do not appear on this graph.
5. To make the number of zeros of G 0 ( z ) close to that of H 0 ( z ), click either of the two zeros (o) of H 0 ( z ) near the bottom of the Zeros of G0 and H0 graph and switch the two zeros to those of G 0 ( z ). G 0 ( z ) now has six zeros and H 0 ( z ) has eight zeros. 
 The following figure shows the design result. Notice that the analysis and synthesis scaling functions are similar, and the analysis and synthesis wavelets also are similar, which means the designed wavelet is near-orthogonal. The symmetry of the filter banks also preserves the linear-phase property.
 [IMAGE alt='image' src='wa_designing_fbi_wavelet.gif']

Because of the near-orthogonality and linear-phase properties of the FBI wavelet, you can apply this wavelet to many kinds of signal and image processing, for example, image compression in JPEG2000. The FBI wavelet is called bior4_4 because both the analysis and synthesis lowpass filters *G*<sub>0</sub>(*z*) and *H*<sub>0</sub>(*z*) have four zeros at [IMAGE alt='image' src='pi.gif']. This wavelet also is known as CDF 9, 7 because the lengths of the analysis and synthesis highpass filters are nine and seven, respectively.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/designing_product.html language=enus -->
## TOPIC 00013: Designing the Product P0(z) (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/designing_product.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/designing_product.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing the Product P0(z) (Advanced Signal Processing Toolkit)

The auxiliary function *P*<sub>0</sub>(*z*) denotes the product of *G*<sub>0</sub>(*z*) and *H*<sub>0</sub>(*z*), as shown in the following equation:

*P*<sub>0</sub>(*z*) = *G*<sub>0</sub>(*z*) + *H*<sub>0</sub>(*z*)

You usually use one of the following three types of filters for *P*<sub>0</sub>(*z*).

- Maximally-flat
- General equiripple halfband
- Positive equiripple halfband

The maximally-flat filter is defined by the following equation:

*P*<sub>0</sub>(*z*) = (1 + *z*<sup>–1</sup>)<sup>2</sup><sup>*p*</sup>*Q*(*z*)

In the [Wavelet Design](../lvwavelettk/wavelet_design.html) Express VI, the **Zero pairs at** [IMAGE alt='image' src='pi.gif'] (**P0**) control on the **Configure Wavelet Design** dialog box specifies the value of the parameter *p*, which determines the number of zeros placed at π on the unit circle. The more the zeros at [IMAGE alt='image' src='pi.gif'], the smoother the corresponding wavelet. The value of *p* also affects the transition band of the frequency response. A large value of *p*results in a narrow transition band. In the time domain, a narrower transition band implies more oscillations in the corresponding wavelet. When you specify a value for the parameter *p*, you can review the frequency response shown on the right-hand side of the **Configure Wavelet Design** dialog box.

In a general equiripple halfband filter, halfband refers to a filter in which ω<sub>*s*</sub> + ω<sub>*p*</sub> = π, where ω<sub>*s*</sub> denotes the stopband frequency and ω<sub>*p*</sub> denotes the passband frequency, as shown in the following figure.

[IMAGE alt='image' src='halfband-filter.gif']

The positive equiripple halfband filter is a special case of general equiripple halfband filters. The [Fourier transform](/csh?topicname=lvanlsconcepts/fourier_transform.html) of this type of filter is always nonnegative. Positive equiripple halfband filter is appropriate for orthogonal wavelets because the auxiliary function *P*<sub>0</sub>(*z*) must be nonnegative.

Use the **P**<sub>0</sub>**type** control to specify the *P*<sub>0</sub>(*z*) type. When **Wavelet Type** is set to **Orthogonal**, you can set **P**<sub>0</sub>(**z**) either to **Maxflat** (default), for a maximally-flat filter, or to **Positive Equiripple**. When **Wavelet Type** is set to **Biorthogonal**, you can set **P**<sub>0</sub>(**z**) to **Maxflat** (default), **Positive Equiripple**, or **General Equiripple**.

Because all filters, including *P*<sub>0</sub>(*z*), *G*<sub>0</sub>(*z*), and *H*<sub>0</sub>(*z*), are real-valued finite impulse response (FIR) filters, the zeros of these filters are mirror-symmetric about the x-axis in the z-plane. Therefore, for any zero *z*<sub>*i*</sub>, a corresponding complex conjugate *z*<sub>*i*</sub>* always exists. If *z*<sub>*i*</sub> is complex, meaning that if *z*<sub>*i*</sub> is located off of the x-axis, you always can find a corresponding zero on the other side of the x-axis, as shown in the following figure. As a result, you only need to see the top half of the z-plane to see all of the zeros that are present. After you select *z*<sub>*i*</sub>, the Wavelet Design Express VI automatically includes the complex conjugate *z*<sub>*i*</sub>*.

[IMAGE alt='image' src='zero-dist.gif']

Two parameters are associated with equiripple filters—**# of taps** and **Passband**. Use the **# of taps** control to define the number of coefficients of *P*<sub>0</sub>(*z*). Because *P*<sub>0</sub>(*z*) is a type-I FIR filter, the length of *P*<sub>0</sub>(*z*) must be odd. Use the **Passband** control to define the normalized passband frequency, ω<sub>*p*</sub>, of *P*<sub>0</sub>(*z*). The value of ω<sub>*p*</sub> must be less than 0.5. Longer filters improve the sharpness of the transition band and the magnitude of the attenuation in the stopband at the expense of extra computation time for implementation.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/factorizing_for_product.html language=enus -->
## TOPIC 00014: Selecting the Factorization Type for P0(z) (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/factorizing_for_product.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/factorizing_for_product.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Selecting the Factorization Type for P0(z) (Advanced Signal Processing Toolkit)

After you [determine *P*<sub>0</sub>(*z*)](designing_product.html), the next step is to specify how *P*<sub>0</sub>(*z*) is factorized into the analysis lowpass filter *G*<sub>0</sub>(*z*) and the synthesis lowpass filter *H*<sub>0</sub>(*z*), respectively. In the [Wavelet Design](../lvwavelettk/wavelet_design.html) Express VI, use the **Factorization (Type of G0)** control to specify the factorization type. The factorizing process is not unique. For a given *P*<sub>0</sub>(*z*), you have the following four options for creating *G*<sub>0</sub>(*z*) and *H*<sub>0</sub>(*z*).

- Arbitrary —No specific constraints are associated with this filter. The following figure shows an example of arbitrary factorization. The blue crosses represent the zeros of G 0 ( z ), and the red circles represent the zeros of H 0 ( z ). Click on the zero you want to select to switch the zero from that of G 0 ( z ) to that of H 0 ( z ) and vice versa.
 [IMAGE alt='image' src='wa_arbitrary_phase.gif']
- Minimum Phase —All of the zeros of G 0 ( z ) are contained inside the unit circle, as shown in the following figure. All the zeros of H 0 ( z ) are the reciprocal of the zeros of G 0 ( z ). The Wavelet Design Express VI automatically generates the zeros for H 0 ( z ) and G 0 ( z ). You cannot switch the zeros between G 0 ( z ) and H 0 ( z ). The minimum phase filter possesses minimum phase-lag. When P 0 ( z ) is maximally-flat and G 0 ( z ) is minimum phase, the resulting wavelets are the Daubechies wavelets.
 [IMAGE alt='image' src='wa_minimum_phase.gif']
- Linear Phase —Any zero and its reciprocal must belong to the same filter, as shown in the following figure. When you switch a zero of G 0 ( z ) to that of H 0 ( z ), the reciprocal of the zero also switches to H 0 ( z ). When you switch a zero of H 0 ( z ) to that of G 0 ( z ), the reciprocal of the zero also switches to G 0 ( z ). This option is available only if the filter is biorthogonal. 
 [IMAGE alt='image' src='wa_linear_phase.gif'] 
 In the time domain, a linear phase implies that the coefficients of the filter are symmetric or antisymmetric. Linear phase filters have a constant group delay for all frequencies. This property is required in many signal and image feature-extraction applications, such as peak detection and image edge detection.
- B-Spline —This option is available only if Wavelet Type is Biorthogonal and P0 type is Maxflat . In this case, the analysis lowpass filter G 0 ( z ) and the synthesis lowpass filter H 0 ( z ) are defined by the following equations, respectively: 
 G 0 ( z ) = (1 + z –1 ) *k* 
 H 0 ( z ) = (1 + z –1 ) *2p–k* Q ) z ) 
 where k is specified with the Zeros at ( P0 ) control, and p is determined by the Zero pairs at ( P0 ) control. The Wavelet Design Express VI automatically generates the zeros of G 0 ( z ) and H 0 ( z ) based on the settings for k and p . You cannot switch the zeros between G 0 ( z ) and H 0 ( z ). The following figure shows an example of B-Spline factorization.
 [IMAGE alt='image' src='wa_b-spline_phase.gif']

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/predicting_ts_values.html language=enus -->
## TOPIC 00015: Predicting Time Series Values (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/predicting_ts_values.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/predicting_ts_values.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Predicting Time Series Values (Advanced Signal Processing Toolkit)

You can predict future values of a time series using the LabVIEW Time Series Analysis Tools, which provide the following two types of prediction methods:

- ARMA Model-based prediction —You can make predictions based on the estimated ARMA model for both univariate and multivariate time series.
- Exponential smoothing prediction —You can make predictions based on exponential smoothing for univariate time series.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/selecting_wavelet_type.html language=enus -->
## TOPIC 00016: Selecting the Wavelet Type (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/selecting_wavelet_type.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/selecting_wavelet_type.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Selecting the Wavelet Type (Advanced Signal Processing Toolkit)

In the [Wavelet Design](../lvwavelettk/wavelet_design.html) Express VI, use the **Wavelet Type** control on the **Configure Wavelet Design** dialog box to select the wavelet type. You can choose from the following two wavelet types, **Orthogonal** (default) and **Biorthogonal**.

The [wavelet transform](wa_intro.html#wavelet_transform) with orthogonal wavelets is energy conserving, meaning that the total energy contained in the resulting coefficients and the energy in the original time samples are the same. This property is helpful for signal and image compression and denoising. But the filters associated with orthogonal wavelets are not linear phase. Linear phase is a helpful property for feature-extraction applications. The filters associated with biorthogonal wavelets can be linear phase.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tfa_adapt_trans_exp.html language=enus -->
## TOPIC 00017: Adaptive Transform and Expansion (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tfa_adapt_trans_exp.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tfa_adapt_trans_exp.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Adaptive Transform and Expansion (Advanced Signal Processing Toolkit)

You can use the [inverse Fourier transform](/csh?topicname=lvanlsconcepts/fourier_transform.html) and the [discrete Gabor expansion](tfa_discrete_gabor_trans_exp.html) to express signals as a linear combination of a series of elementary functions. For example, the inverse discrete Fourier transform expresses a signal as the linear combination of sinusoids in which the weight of each elementary sinusoid is the corresponding discrete Fourier coefficient. The discrete Gabor expansion expresses a signal as the linear combination of windowed sinusoids with Gabor transform coefficients.

Like the [discrete Gabor transform](tfa_discrete_gabor_trans_exp.html), the adaptive expansion expresses a signal as a linear combination of Gaussian-windowed, linear-chirp functions called chirplets.

In the following equation, the adaptive expansion represents a signal, *s*(*t*), as the linear combination of a series elementary functions, *h**<sub>k</sub>*(*t*), approximately:

[IMAGE alt='image' src='eq_adaptive_expansion.gif']

where *A**<sub>k</sub>* is the corresponding complex amplitude of *h**<sub>k</sub>*(*t*), and *D* specifies the number of the elementary functions. The adaptive transform computes the complex amplitudes, *A**<sub>k</sub>*.

The adaptive transform, also called the adaptive chirplet decomposition, computes the weight for each elementary chirplet. Because the sinusoid function is a subset of the chirplet, the adaptive transform is more powerful than the Gabor transform but generally requires more computing time. The adaptive transform and the adaptive expansion are unique to the [LabVIEW Time Frequency Analysis Tools](tfa_overview.html).

Unlike the discrete Gabor expansion and discrete Gabor transform, the elementary functions of the adaptive expansion are time-varying signals themselves with spectral content that changes linearly over time. The time centers and the frequency centers of the chirplets are not limited to a grid in the time-frequency plane, and they can be any real value. Also, the window lengths of all the chirplets do not need to be the same. Therefore, the adaptive expansion can have a finer time-frequency resolution and express time-varying signals more accurately.

#### Matching Pursuit Method

The matching pursuit method is a commonly used implementation of the adaptive transform that uses a set of elementary functions called a dictionary. The dictionary size in the matching pursuit algorithm determines the speed and accuracy of the resulting analysis. A small dictionary requires less computing time but has poorer accuracy. A large dictionary results in better accuracy but requires more computing time. Refer to the book [Introduction to Time-Frequency and Wavelet Transforms](aspt_related_doc.html) for more information about the matching pursuit method.

The [TFA Adaptive Transform](../lvtimefreqtk/tfa_adaptive_transform.html) VI provides an implementation of the adaptive transform that is more efficient and accurate than the matching pursuit method. This implementation uses the matching pursuit method with a small dictionary size as a coarse estimation step and then follows with a refinement step to achieve an accurate estimation. The small dictionary size and refinement step make the adaptive transform in the Time Frequency Analysis Tools more efficient and accurate.

The adaptive transform is used widely in applications, such as radar and sonar signal processing, that need to accurately estimate parameters of signals with time-variant spectra, especially signals that contain chirplets. After you detect the adaptive chirplets in a signal, you also can use adaptive chirplets to improve the performance of some pattern-recognition applications.

#### Using the Adaptive Transform and Adaptive Expansion

The following figure shows the typical steps to create an adaptive transform and adaptive expansion application.

[IMAGE alt='image' src='using-at-and-ae.gif']

Usually, you use the adaptive transform to compute the magnitudes and parameters of chirplets, select the chirplets that you need for the application, and then apply the adaptive expansion to reconstruct the signal. In some applications, you might use the parameters of chirplets to make a decision before the expansion.

The white line in the following figure represents the real parts of a complex-valued signal from a pulse radar receiver, and the red line in this figure represents the imaginary parts of the signal.

[IMAGE alt='image' src='fp_tfa_original_pulse_radar_signal.gif']

Though not apparent in the previous figure, this signal contains three signals—the target signature signal and two instances of strong interference from sea clutter, which is the radar signal reflected off of surface sea waves. The interference signal is much stronger than the target signature signal so you cannot see the target signature in the time-domain representation in the previous figure. The goal of this application is to remove the interference signal and extract the target signature signal.

Because the target signature signal is a time-varying chirp signal, first observe the time-frequency representation of the signal before selecting a signal processing method to use. The following figure shows the STFT magnitude spectrum of the example signal.

[IMAGE alt='image' src='fp_tfa_stft_mag_pulse_radar.gif']

The color corresponds to the magnitude of the STFT coefficients. The color spectrum from red to blue corresponds to the magnitude from maximum to minimum. The red stripes close to 0 Hz are the sea clutter interference. The green stripe running diagonally across the interference signal is the target signature signal. Notice that the interference signal is stronger than the target signature signal and that the interference and the target signature overlap in the time-frequency plane. A conventional time-domain fixed filter is not sufficient for separating these components. Because the spectral peak of the target signature changes over time and the spectral bandwidths of the interference vary over time, you can use the TFA Adaptive Transform VI to decompose the signal into a linear combination of chirplets. Next, you can remove the resulting chirplets with a chirp rate close to zero and a frequency less than 0.02 Hz in this example. Then you can use the [TFA Adaptive Expansion](../lvtimefreqtk/tfa_adaptive_expansion.html) VI to reconstruct the target signature, as shown in the following figure.

[IMAGE alt='image' src='fp_tfa_recon_targ_sig_sea_clut_removed.gif']

Compared to the interference signal in the figure of the complex signal from the pulse radar receiver, the sea clutter signal in the previous figure has been suppressed up to 20 dB. The following figure shows the STFT magnitude spectrum of the extracted target signature with the interference substantially reduced.

[IMAGE alt='image' src='fp_tfa_stft_mag_reconst_targ_sig.gif']

Refer to the Chirplet TDR VI in the labview\examples\Time Frequency Analysis\TFAApplications directory for an example of using the TFA Adaptive Transform VI and the TFA Adaptive Expansion VI.

If the signal you want to analyze using any linear time-frequency method contains a large constant offset or is non-negative, a single line in the vicinity of 0 Hz dominates the resulting time-dependent spectrum. In these situations, you might not be able to identify more interesting frequency patterns. To suppress the constant offset component, you can apply certain types of preprocessing, but the detrending methods for removing the constant-offset components depend on the application. No general method works in all cases. Common techniques of detrending include lowpass [filtering](/csh?topicname=lvanlsconcepts/introduction_to_filtering.html) and [curve fitting](/csh?topicname=lvanlsconcepts/curve_fitting_overview.html). However, another technique is the [wavelet transform](wa_intro.html#wavelet_transform).

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tfa_analytic_signals.html language=enus -->
## TOPIC 00018: Analytic Signals (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tfa_analytic_signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tfa_analytic_signals.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Analytic Signals (Advanced Signal Processing Toolkit)

|  | Note This topic contains information that applies to the LabVIEW Time Frequency Analysis Tools. |
| --- | --- |

For real-valued signals, the power spectrum has symmetric components at positive frequencies and at negative frequencies. The corresponding analytic signal of the real-valued signal is a complex-valued signal. The analytic signal retains the DC component of the real-valued signal, doubles the components with positive frequency, and removes the components with negative frequency. The following illustrations show the power spectrum of a real-valued signal, *s*(*t*), and the power spectrum of the corresponding analytic signal.

[IMAGE alt='image' src='psofrealsignal.gif']

[IMAGE alt='image' src='psofanalyticsignal.gif']

Notice that the power spectrum of the real-valued signal is symmetric about 0 Hz. In comparison, the power spectrum of the analytic signal is not symmetric and contains components with positive frequency only. Furthermore, the amplitude of the power spectrum of the analytic signal with positive frequency is twice the amplitude of the power spectrum of the real-valued signal. Whereas the amplitude of the power spectrum of the real-valued signal is 40 at 300 Hz, the amplitude of the power spectrum of the corresponding analytic signal is 80 at 300 Hz.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tfa_application.html language=enus -->
## TOPIC 00019: Time Frequency Analysis Application Areas (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tfa_application.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tfa_application.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Frequency Analysis Application Areas (Advanced Signal Processing Toolkit)

In general, you can categorize time-frequency analysis methods into two classes: [linear methods](tfa_linear.html) and [quadratic methods](tfa_quadratic.html). You usually use quadratic methods to analyze, classify, and detect latent features in a signal, and you usually use linear methods to reduce noise and extract signal components.

One major benefit of applying a time-frequency transform to a signal is discovering the pattern of frequency changes, which often clarifies the nature of the signal. Once you identify a pattern, you can analyze and classify the pattern. For example, a pattern of harmonic drift associated with rotating machinery can indicate the working condition of a system, and a pattern of frequency changes in medical signals can indicate a patient's health condition.

Another important use of time-frequency analysis is to reduce random noise in noise-corrupted signals. For example, random noise might spread evenly across the entire time-frequency domain. The useful information, however, usually is concentrated in a relatively small region in the time-frequency domain. If you convert such a noise-corrupted signal to the time-frequency domain using a linear time-frequency transform, you might be able to extract those components in the time-frequency domain and then reconstruct the time-domain signal, which has a higher signal-to-noise ratio.

You also can use time-frequency analysis to determine if a signal has distinct time-frequency components and isolate those components for further analysis. In the time domain, you can separate the components of signals that do not overlap, such as musical notes. You cannot use the Fourier transform to separate signal components that overlap in the time domain. In the frequency domain, you can use the [fast Fourier transform (FFT)](/csh?topicname=lvanlsconcepts/fft_fundamentals.html) to separate signals, such as vibration harmonics caused by a steady-state shaft imbalance. However, the different components can overlap in the frequency domain if the spectral content varies over time. With such overlapping signal components, you cannot distinguish the components in either the time domain or in the frequency domain alone. In this situation, you usually can use a linear time-frequency method to distinguish the overlapping signal components.

Many real-world signals contain time-varying spectra, which means that the potential application areas of time-frequency analysis are numerous. The following list highlights a few successful application areas of time-frequency analysis.

- Order analysis, such as for rotating machinery analysis

|  | Note You can use the NI Sound and Vibration Measurement Suite to examine dynamic signals mechanical systems generate, including rotating or reciprocating components, and to create order analysis applications for order tracking, order extraction, and tachometer signal processing. |
| --- | --- |

- Machine condition monitoring for systems associated with rotational machinery, such as power-generator systems
- Audio equipment testing and characterization, such as for speakers
- Speech processing, such as speech enhancement and speech recognition
- Radar and sonar image enhancement
- Biomedical signal processing, such as signal feature extraction
- Seismological signal processing, such as detection of soil liquefaction

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tfa_calculating_energy.html language=enus -->
## TOPIC 00020: Calculating the Energy of a Signal at Each Time Frequency Instant (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tfa_calculating_energy.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tfa_calculating_energy.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Calculating the Energy of a Signal at Each Time Frequency Instant (Advanced Signal Processing Toolkit)

A main motivation for the development of various time-frequency distributions, such as the [short-time Fourier transform (STFT) spectrogram](aspt_stft_spectrogram.html), the [Wigner-Ville distribution (WVD)](tfa_wvd.html), the [Gabor spectrogram](tfa_gabor_spectrogram.html), and so on, has been to describe how the energy of a signal varies with time and frequency.

Currently, scientists do not know of an algorithm, except for a few special cases, that can compute the energy of a signal at each particular time-frequency instant (*t*, *f*). Strictly speaking, the result of all quadratic time-frequency analysis algorithms, *P*(*t*, *f* ), is nothing more than a certain type of weighted average energy in the vicinity of the point (*t*, *f*). Different weighting schemes lead to different algorithms with different time-frequency resolutions and other properties.

Without going into any detail, the following examples show the effect of different algorithms, or different weighting averages, and the resulting time-frequency distribution.

The following figure shows the STFT spectrogram of a test signal that contains ten sine cycles at 10 Hz. This example uses a [Hanning window](/csh?topicname=lvanlsconcepts/lvac_hanning.html).

[IMAGE alt='image' src='fp_tfa_stft_spectrogram.gif']

Although the signal starts at 1 s and ends at 2 s, the STFT spectrogram in the previous figure shows that energy exists before 1 s and after 2 s. You can use the Gabor spectrogram method with an order of four to suppress the energy substantially before 1 s, after 2 s, and above or below 10 Hz to achieve a better measurement, as shown in the following figure.

[IMAGE alt='image' src='fp_tfa_stft_spectrogram_gabor4.gif']

The previous figure shows that most of the energy of the signal now exists between 1 s and 2 s and within 10 Hz. As the order of the Gabor spectrogram increases, the energy concentration also increases, and you can come closer to achieving measurement between 1 s and 2 s and within 10 Hz. However, a Gabor spectrogram with a high order produces negative values, which can cause problems with the classical energy definition, which requires that the energy be non-negative.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tfa_discrete_gabor_trans_exp.html language=enus -->
## TOPIC 00021: Discrete Gabor Transform and Expansion (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tfa_discrete_gabor_trans_exp.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tfa_discrete_gabor_trans_exp.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Discrete Gabor Transform and Expansion (Advanced Signal Processing Toolkit)

The discrete Gabor transform is an invertible, linear time-frequency transform. The discrete Gabor expansion is the inverse of the discrete Gabor transform. The output of the discrete Gabor transform is called the Gabor coefficients.

Characteristics of time-varying signals that are not obvious in the time domain or in the frequency domain alone can become clear in the time-frequency domain when you apply the discrete Gabor transform. After you extract the useful features of a signal in the time-frequency domain, you can apply the discrete Gabor expansion to obtain the time waveform with the extracted features. Similarly, after you suppress the useless components, like noise, in the time-frequency domain, you can apply the discrete Gabor expansion to obtain the time waveform with the noise suppressed.

In the following equation, the Gabor expansion represents a time-domain signal, *s*(*i*), as the linear combination of elementary functions *h**<sub>m,n</sub>*(*i*):

[IMAGE alt='image' src='eq_gabor_exp.gif']

where *h**<sub>m,n</sub>*(*i*) is the time-frequency elementary function, *C**<sub>m,n</sub>* is the weight of *h**<sub>m,n</sub>*(*i*), and *C**<sub>m,n</sub>* is the Gabor coefficients.

The Gabor transform computes the Gabor coefficients *C**<sub>m,n</sub>* for the signal *s*(*i*).

#### Synthesis Window, Analysis Window, and Dual Window

Because the discrete Gabor transform is a special case of the [STFT](aspt_stft.html), you must consider the effects of the window characteristics and understand how the window length and type affect the time-frequency resolution of the time-frequency representation. The window used with the discrete Gabor transform is called the analysis window. The window used with the discrete Gabor expansion is called the synthesis window.

The following equation defines the time-shifted and frequency-modulated version, *h**<sub>m,n</sub>*(*i*), of a window function, *h*(*i*):

[IMAGE alt='image' src='eq_window.gif']

where *h*(*i*) is the synthesis window, *dM* is **time step**, and *N* is **frequency bins**. *C**<sub>m,n</sub>* reveals how the signal behaves in the joint time-frequency domain around the time and the frequency centers of *h**<sub>m,n</sub>*(*i*).

You can use the Gabor transform to obtain the Gabor coefficients *C**<sub>m,n</sub>* with the following equation:

[IMAGE alt='image' src='eq_gabor_trans.gif']

where [IMAGE alt='image' src='eq_analysis_window.gif'] is the analysis window. [IMAGE alt='image' src='eq_analysis_window.gif'] and *h*(*i*) are a pair of dual functions because you use one for the Gabor transform and the other for the Gabor expansion, respectively. Usually, you specify the synthesis window *h*(*i*) first and then use the [TFA Dual Window](../lvtimefreqtk/tfa_dual_window.html) VI to compute the corresponding analysis window ([IMAGE alt='image' src='eq_analysis_window.gif']).

To reconstruct the time-domain signal accurately from the Gabor time-frequency representation, you must use appropriate, complementary analysis and synthesis windows. You can exchange the analysis windows and the synthesis windows, meaning that you can use the synthesis windows for the Gabor transform and use the analysis windows for the Gabor expansion. Therefore, the analysis windows and the synthesis windows are called dual windows. Usually, you first specify the synthesis window, such as a Gaussian window. Given a synthesis window, you must use the TFA Dual Window VI to compute the corresponding analysis window. You also can use the [Dual Window](../lvtimefreqtk/dual_window.html) Express VI to design the dual windows for the discrete Gabor transform and the discrete Gabor expansion interactively.

#### Oversampling Rate

You can consider *h**<sub>m,n</sub>*(*i*) as the discrete atoms in the time-frequency domain as shown in the following grid:

[IMAGE alt='image' src='gaborgrid.gif']

The cross points in the grid are the time and the frequency centers of the elementary functions. The time and the frequency centers of *h**<sub>m,n</sub>*(*i*) in normalized units are *mdM* and 2[IMAGE alt='image' src='pi.gif']*n*/*N*, respectively.

You can consider the Gabor expansion as a way to resample the time-domain signal in the joint time-frequency domain. The time sampling interval in the joint time-frequency domain is *dM*. The frequency sampling interval in the joint time-frequency domain is 2[IMAGE alt='image' src='pi.gif']/*N*.

The time centers and frequency centers of the elementary functions used in a particular Gabor transform application are discrete and form an equally sampled grid in the time-frequency domain, as shown in the previous figure. If the time-frequency center of a signal component is not aligned with the time-frequency sampling grid, some spectral energy from that signal component might spread erroneously to adjacent points in the time-frequency plane. This [energy leakage](/csh?topicname=lvanlsconcepts/spectral_leakage.html) can distort the resulting time-frequency spectrum and introduce confusing artifacts in the spectrum. Therefore, the discrete Gabor transform and the discrete Gabor expansion are not always the best way to analyze time-varying signals.

The number of sampling points in the time-frequency domain is M×N. The ratio of the total sampling points in the time-frequency domain and in the time domain, that is, *MN/L*, is called the oversampling rate, where *L* is the signal length. Because *M = L/dM*, the oversampling rate equals *N/dM*. The oversampling rate must be greater than or equal to 1 to reconstruct the time-domain signal from the time-frequency domain representation.

#### Using the Discrete Gabor Transform and Discrete Gabor Expansion

The following figure shows the typical steps for creating applications using the discrete Gabor transform and the discrete Gabor expansion.

[IMAGE alt='image' src='using-dgt-and-dge.gif']

To reduce noise or separate components of a time-varying signal, you first use the discrete Gabor transform to compute the time-frequency representation of a signal, modify the time-frequency representation of the signal, and then apply the discrete Gabor expansion to reconstruct the time-domain signal with the modified time-frequency representation.

Use the [TFA Discrete Gabor Transform](../lvtimefreqtk/tfa_discrete_gabor_transform.html) VI and the [TFA Discrete Gabor Expansion](../lvtimefreqtk/tfa_discrete_gabor_expansion.html) VI to compute the Gabor transform and Gabor expansion.

Masking and thresholding are the most commonly used methods to modify a signal in the time-frequency domain. A mask defines which parts of the time-frequency representation remain and which parts to set to zero. The threshold defines which parts of the time-frequency representation with magnitudes greater than the threshold remain and which parts to set to zero. The mask and the threshold are similar to filters with time-dependent specifications. This kind of application commonly is called time-varying filtering.

Use the [TFA Time Varying Filter](../lvtimefreqtk/tfa_time_varying_filter.html) VI and the [Time Varying Filter (Thresholding)](../lvtimefreqtk/time_varying_filter_thresholding.html) Express VI to perform time-varying filtering interactively, such as in noise reduction and feature extraction applications. Many other methods exist to modify the time-frequency representation, for example, setting the phase of the time-frequency representation to zero or setting the magnitude of the time-frequency representation to unity.

The following figure shows an example of a noisy signal that contains three chirps.

[IMAGE alt='image' src='fp_tfa_noisy_chirps.gif']

The color corresponds to the magnitude of the Gabor coefficients from the discrete Gabor transform. The color spectrum from red to blue corresponds to the magnitude from maximum to minimum. The Gabor coefficients that correspond to the chirps have a higher magnitude and are concentrated in a relatively small region in the time-frequency domain. The Gabor coefficients that correspond to the noise have a lower magnitude and are spread over the entire time-frequency domain. By applying a thresholding operation, you can preserve the Gabor coefficients that correspond to the chirps and reduce to zero the Gabor coefficients that correspond to noise. The Time Varying Filter (Thresholding) Express VI reconstructs the denoised chirps from these modified Gabor coefficients by using the discrete Gabor expansion, as shown in the following figure.

[IMAGE alt='image' src='fp_tfa_denoised_chirps.gif']

Refer to the Offline Noise Reduction with Time Varying Filter VI in the labview\examples\Time Frequency Analysis\TFAApplications directory for an example of using the Time Varying Filter (Thresholding) Express VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tfa_gabor_spectrogram.html language=enus -->
## TOPIC 00022: Gabor Spectrogram (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tfa_gabor_spectrogram.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tfa_gabor_spectrogram.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Gabor Spectrogram (Advanced Signal Processing Toolkit)

Because you can decompose a signal as a linear combination of a family of elementary functions, you can consider the [Wigner-Ville Distribution (WVD)](tfa_wvd.html) of a signal to be the summation of the WVD of each elementary function, or auto-term, and the cross-terms of each pair of elementary functions.

You can use the Gabor spectrogram method to reduce the cross-term interference of the WVD. This method decomposes a signal with the [Gabor expansion](tfa_discrete_gabor_trans_exp.html) and then sums the WVD of each auto-term with some cross-terms. Because the Gabor spectrogram method uses the Gabor expansion first and then the WVD, the Gabor spectrogram also is called the Gabor expansion-based spectrogram. The Gabor spectrogram also is called the time-frequency distribution series. The Gabor spectrogram is a method unique to the [LabVIEW Time Frequency Analysis Tools](tfa_overview.html).

The Gabor spectrogram has a better time-frequency resolution than the [short-time Fourier transform (STFT) spectrogram](aspt_stft_spectrogram.html) method and less cross-term interference than the WVD method. The Gabor spectrogram algorithm includes simple analytic forms, and you can implement the Gabor spectrogram with interpolation filters. Therefore, the Gabor spectrogram is more efficient than the [Choi-Williams Distribution (CWD)](tfa_cwd_csd.html#choi-williams_distribution) and the [Cone-Shaped Distribution (CSD)](tfa_cwd_csd.html#cone-shaped_distribution), especially with large signal lengths. However, the Gabor spectrogram usually requires more computation time than the STFT spectrogram or the WVD.

Use [TFA Fast Gabor Spectrogram](../lvtimefreqtk/tfa_fast_gabor_spectrogram.html) VI to compute the Gabor spectrogram.

#### Selecting an Appropriate Gabor Spectrogram Order and Window Length

You need to select the order of the Gabor spectrogram and the window length of the Gabor spectrogram properly to balance the time-frequency resolution and the cross-term interference. For Gabor spectrograms with a low order, the window length affects the time resolution, the frequency resolution, and the cross-term interference of the Gabor spectrogram. As in the case of the STFT, a narrow window length results in a coarse frequency resolution, a fine time resolution, and severe cross-term interference between two auto-terms with the same time center. A wide window length results in a fine frequency resolution, a coarse time resolution, and severe cross-term interference between two auto-terms with the same frequency center. The selection of the window length in the Gabor spectrogram is much less sensitive than in the STFT spectrogram. Also, regardless of the window length you select, the Gabor spectrogram always converges to the WVD as the order increases.

The order of the Gabor spectrogram balances the time-frequency resolution and the cross-term interference of the Gabor spectrogram. As the order increases, the time-frequency resolution of the Gabor spectrogram improves, but the spectrogram includes more cross-term interference and requires a longer computation time. When the order is zero, the Gabor spectrogram is non-negative and is similar to the STFT spectrogram. As the order increases, the Gabor spectrogram converges to the WVD. For most real-world applications, choose an order of two to five to balance the time-frequency resolution and cross-term suppression.

The following figure shows the Gabor spectrogram of the [example frequency hopper signal](aspt_stft_spectrogram.html#frequency_hopper_signal_window_length) when the order is 0 and the window length is 128.

[IMAGE alt='image' src='fp_tfa_gabor_hop_sig_o0_wl128.gif']

Notice that the signal in the previous figure is similar to the STFT spectrogram in the example frequency hopper signal with window length of 128. The Gabor spectrogram of the example frequency hopper signal in the previous figure has a coarse time-frequency resolution and does not include cross-term interference.

The following figure shows the Gabor spectrogram of the example frequency hopper signal when the order is 20 and the window length is 128.

[IMAGE alt='image' src='fp_tfa_gabor_hop_sig_o20_wl128.gif']

| 1 | Auto-terms |
| --- | --- |

The signal in the previous figure is similar to the [WVD of the example frequency hopper signal](tfa_wvd.html#cross-term_interference) because the Gabor spectrogram converges to the WVD as the order increases. The Gabor spectrogram of the example frequency hopper signal in the previous figure has a fine time-frequency resolution and includes cross-term interference.

The following figure shows the Gabor spectrogram of the example frequency hopper signal when the order is 3 and the window length is 128.

[IMAGE alt='image' src='fp_tfa_gabor_hop_sig_o3_wl128.gif']

The signal in the previous figure has a higher time-frequency resolution than the STFT spectrogram and less cross-term interference than the WVD.

The following figure shows a signal with three Gaussian components. The composite Gaussian signal can be a useful test signal for testing the time-frequency resolution and the cross-term interference of a time-frequency analysis algorithm because the composite Gaussian signal has compact signal components that should be very narrow on the time-frequency plane.

[IMAGE alt='image' src='fp_tfa_three-gaussian.gif']

The example signal in the previous figure contains one Gaussian-windowed linear chirp signal and two Gaussian-windowed sine wave signals. The linear chirp has the same time center as one of the sine waves and the same frequency center as the other sine wave, but you cannot see that in the time-domain representation in the previous figure.

The following figure shows the Gabor spectrogram of the composite Gaussian signal example when the order is 5 and the window length is 32.

[IMAGE alt='image' src='fp_tfa_gabor_3_gaus_o5_wl32.gif']

| 1 | Auto-terms |
| --- | --- |

The following figure shows the Gabor spectrogram of the composite Gaussian signal example when the order is 5 and the window length is 256.

[IMAGE alt='image' src='fp_tfa_gabor_3_gaus_o5_wl256.gif']

| 1 | Auto-terms |
| --- | --- |

Notice in the previous two figures that the cross-term interference along the time axis increases with the window length and the cross-term interference along the frequency axis decreases with the window length.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tfa_gaussian_chirplet_pulse.html language=enus -->
## TOPIC 00023: Estimating Gaussian Chirplet and Gaussian Pulse (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tfa_gaussian_chirplet_pulse.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tfa_gaussian_chirplet_pulse.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Estimating Gaussian Chirplet and Gaussian Pulse (Advanced Signal Processing Toolkit)

You can consider the elementary functions that the discrete Gabor expansion uses, such as Gaussian-windowed, complex-sinusoid functions or complex, frequency-modulated Gaussian functions, as being a set of time-shifted and frequency-modulated versions of a single prototype function.

The following equation represents the linear Gaussian chirplet:

[IMAGE alt='image' src='eq_gaussian_chirplet.gif']

| where | is the time-frequency center of the chirplet |
| --- | --- |
|  | is the standard deviation of the Gaussian envelope |
|  | is the chirp rate |

The following figures show the time waveform and the time-frequency spectrogram of the Gaussian chirplet:

[IMAGE alt='image' src='gauschirpamp.gif']

[IMAGE alt='image' src='gauschirpfreq.gif']

Use the [TFA Adaptive Transform](../lvtimefreqtk/tfa_adaptive_transform.html) VI to select either **Gaussian chirplet** or **Gaussian pulse** as the elementary function to represent a signal. When you choose the Gaussian pulse in the elementary functions, this VI forces the chirp rate [IMAGE alt='image' src='eq_chirp_rate.gif'] to 0. The following illustrations show the waveform and the time-frequency spectrogram of the linear Gaussian pulse in this situation:

[IMAGE alt='image' src='gauspulseamp.gif']

[IMAGE alt='image' src='gauspulsefreq.gif']

Given a signal, *s*(*t*), the adaptive transform computes the parameters of each elementary function by using the [matching pursuit method](tfa_adapt_trans_exp.html#matching_pursuit_method) together with a fast refinement algorithm.

When you specify how many possible terms of Gaussian chirplet or Gaussian pulse exist for the signal, the TFA Adaptive Transform VI estimates the parameters of the Gaussian chirplets or the Gaussian pulses. The estimated Gaussian chirplets or Gaussian pulses can be distributed in the time-frequency domain arbitrarily. The time and the frequency centers of the Gaussian chirplets or Gaussian pulses are not fixed in a grid. Also, the envelopes of the Gaussian chirplets or Gaussian pulses are arbitrary. In comparison, the discrete Gabor expansion has a fixed sampling grid and a fixed envelope for all the elementary functions.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tsa_building_modal.html language=enus -->
## TOPIC 00024: Building Modal Parametric Models (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tsa_building_modal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tsa_building_modal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Building Modal Parametric Models (Advanced Signal Processing Toolkit)

A modal parametric model describes the bulk dynamic characteristics of resonant systems such as buildings and bridges. The dynamic characteristics include natural frequencies, damping factors, resonance magnitudes, and resonance phases.

You can use the impulse response function to determine the response of a linear system to stimulus. The impulse response time series for a linear system can be represented parametrically with a linear combination of damped complex sinusoids as follows:

[IMAGE alt='image' src='eq_impulse_response_ts.gif']

| where | t is the time index |
| --- | --- |
|  | n is the model order |
|  | gi is one of the complex magnitudes |
|  | si is one of the modal poles |

*s**<sub>i</sub>* contains a unified frequency *f**<sub>i</sub>* and a damping factor *alpha**<sub>i</sub>* as follows:

[IMAGE alt='image' src='eq_modal_pole_si1.gif']

The parameter *g**<sub>i</sub>* contains a magnitude *r**<sub>i</sub>* and a phase θ*<sub>i</sub>*as follows:

[IMAGE alt='image' src='eq_parameter_gi.gif']

So a discrete-time system can be defined by a series of resonance components, or modes: natural frequencies *f**<sub>i</sub>*, damping factors *alpha**<sub>i</sub>*, resonance magnitudes *r**<sub>i</sub>*, and resonance phases θ*<sub>i</sub>*.

For a multivariate impulse response time series, you can build a modal parametric model as follows:

[IMAGE alt='image' src='eq_multivariate_impulse_response_ts.gif']

where *H**<sub>t</sub>* is a (*k* × 1) vector with *k* variables that come from *k* sources. *H**<sub>t</sub>**<sup>T</sup>* = [*h*<sub>1</sub>*<sub>t</sub>*, *h*<sub>2</sub>*<sub>t</sub>*, ..., *h**<sub>kt</sub>*]. *G**<sub>i</sub>* is a (*k* × 1) complex magnitude vector with *k* variables. *G**<sub>i</sub>**<sup>T</sup>* = [*g*<sub>1</sub>*<sub>i</sub>*, *g*<sub>2</sub>*<sub>i</sub>*, ..., *g**<sub>ki</sub>*]. Each variable in the vector *G**<sub>i</sub>* is one of the complex magnitudes. *s**<sub>i</sub>* is one of the modal poles.

#### Specifying an Appropriate Model Order

The model order determines the number of modes that a modal parametric model contains. A model can contain real modes or pairs of complex conjugate modes. A real mode generates a resonance component at 0 Hz or at the Nyquist frequency. A pair of conjugate complex modes generates a resonance component with a positive frequency and discards the conjugate resonance component with the corresponding negative frequency. To search for m positive resonance components, you must specify the model order to be at least 2 × *m*. If a time series contains a large offset, you need to set the model order to at least 2 × *m* + 1 to allow for a real mode. Structural vibration time series typically do not have offsets, so you can use a model order of 2 × *m*.

|  | Note Noise and distortion in the measured time series, as well as an insufficient model order, can result in the estimated model containing spurious components. To discern which components in the estimated model are valid, you can try specifying different model orders and form a histogram for the estimated resonance components. In the histogram, the true resonance components of the dynamic system typically do not change with model orders. However, spurious resonance components may change with orders, and weak resonance components also may change with orders, especially if the measured time series is noisy or distorted. |
| --- | --- |

Refer to the Modal Analysis of a Plate VI in the labview\examples\Time Series Analysis\TSAApplications directory for an example that demonstrates the application of the Time Series Analysis VIs in operational modal analysis.

Use the [TSA Modal Parametric Modeling](../lvtimeseriestk/tsa_modal_parametric.html) VI to build modal parametric models for univariate or multivariate time series.

The following figure shows an example of computing the modes of a synthesized univariate time series consisting of two sinusoids at the frequencies of 120 Hz and 130 Hz.

[IMAGE alt='image' src='fp_tsa_estimating_modes.gif']

This example uses the **Matrix Pencil** method because this method is less sensitive to noise than the other available methods. The value of **Model Order** is 4, which equals twice the number of the sinusoids in the univariate time series.

The **Noise Subspace** value is set to 90% to compensate for additive noise in the measurements. For a fixed number of resonance components, a large dimension for the **Noise Subspace** parameter results in a large dimension for the signal subspace you use to describe a time series. A large dimension for the signal subspace helps you reduce the modeling error for the time series. However, an excessively large dimension may introduce spurious resonance components if the time series does not contain much noise. In the previous figure, the **Modes** array accurately indicates the attribute of the resonance components that the synthesized time series contains.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tsa_cepstrum_est.html language=enus -->
## TOPIC 00025: Cepstrum Estimation Methods (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tsa_cepstrum_est.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tsa_cepstrum_est.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cepstrum Estimation Methods (Advanced Signal Processing Toolkit)

A *cepstrum*, which is an anagram of the word *spectrum*, is the [Fourier transform](/csh?topicname=lvanlsconcepts/fourier_transform.html) of the natural logarithm of a spectrum. You can use the estimated cepstrum to identify echoes or periodic components in a time series. A cepstrum also is useful for separating homomorphic or convolved components in a time series by transforming the time series into a domain where the convolution becomes a simple summation operation. A cepstrum has the following four derivative forms:

- real cepstrum
- complex cepstrum
- power cepstrum
- time-cepstrum

Cepstrum estimation methods treat frequency-domain data as time-domain data. Therefore, the domain of a cepstrum is called *quefrency*, which is an anagram of the word *frequency*.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tsa_concepts_intro.html language=enus -->
## TOPIC 00026: Time Series Analysis Concepts (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tsa_concepts_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tsa_concepts_intro.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Series Analysis Concepts (Advanced Signal Processing Toolkit)

Refer to the following help topics to learn about concepts in the LabVIEW Time Series Analysis Tools.

- Introduction to Time Series Analysis
- Overview of LabVIEW Time Series Analysis Tools
- Time Series Analysis Application Areas
- Acquiring and Preprocessing Time Series
- Performing Statistical Analysis
- Building Models
- Predicting Time Series Values
- Performing Correlation and Spectral Analysis

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tsa_corr_spec_analysis.html language=enus -->
## TOPIC 00027: Performing Correlation and Spectral Analysis (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tsa_corr_spec_analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tsa_corr_spec_analysis.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Performing Correlation and Spectral Analysis (Advanced Signal Processing Toolkit)

One application of time series analysis is detecting the hidden periodicities or frequency characteristics in a time series at specific frequencies. By using the [Time Series Analysis](../lvtimeseriestk/time_series_analysis_pal.html) VIs, you can detect a periodicity of a time series in either the time domain or the frequency domain.

In the time domain, [correlation analysis](tsa_correlation_methods.html) is a classical method that you can use to find periodic patterns at a specific frequency in one or more time series. You also can use the correlation method to identify or extract other useful features of a time series, such as phase.

In the frequency domain, you can use spectral analysis methods to estimate the power spectrum of a time series. You also can [estimate the bispectrum](tsa_bispectrum_est.html), which is useful for detecting nonlinearities in a time series, and [estimate the cepstrum](tsa_cepstrum_est.html), which is useful for deconvolving a time series.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tsa_intro.html language=enus -->
## TOPIC 00028: Introduction to Time Series Analysis (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tsa_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tsa_intro.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Introduction to Time Series Analysis (Advanced Signal Processing Toolkit)

A time series is a sequence of observed values ordered through time. For example, the air temperature in meteorological science, blood pressure in biomedical science, or vibration in mechanical engineering or civil engineering are examples of a time series. Time series analysis uses a collection of systematic approaches to extract information about the characteristics of a physical system that generates time series. Approaches to time series analysis include [estimating statistical parameters](tsa_stat_analysis.html), [building dynamic models](tsa_building_models.html), [performing correlations](tsa_correlation_methods.html), [computing the power spectral density (PSD)](tsa_power_spectrum_est.html), and others.

Generally, a time series contains the following information:

- The characteristics of the time series, such as amplitude, spectral content and other statistical characteristics.
- The native characteristics or structural parameters of a system that generates the time series, for example, the natural frequency and damping of a civil structure.
- The characteristics of the input or stimulus to the physical system that generates the time series.

#### Continuous Time Series and Discrete Time Series

In nature, physical quantities such as temperature, pressure, and light intensity change continuously. Observations of these values form a continuous time series.

Given a continuous time series, you can digitize the values at a specified time interval to obtain a discrete time series. The following figure shows the seismograph of the Kobe earthquake, recorded at Tasmania University, Hobart, Australia on January 16, 1995. In this figure, the continuous earthquake vibration signal is sampled at a one-second interval to form a discrete time series.

[IMAGE alt='image' src='fp_tsa_earthquake.gif']

|  | Note The data source in the previous figure is from the Time Series Data Library. |
| --- | --- |

#### Time-Ordered Series and Spatial-Ordered Series

Time series can be ordered not only through time but also through other physical units. For example, you can obtain a discrete time series ordered versus angular position by sampling the diameter of a spindle as a function of angle.

The following figure shows an example of the diameter error as a function of angle of a spindle during a lathe machining process. The diameter error generates a discrete time series ordered versus angular position.

[IMAGE alt='image' src='fp_tsa_spindle.gif']

#### Univariate Time Series and Multivariate Time Series

You can collect observed values from a single source or simultaneously from two or more sources. Single-source observations generate univariate time series, and multi-source observations form multivariate time series, or vector time series. For example, you can obtain a multivariate time series by recording the values of pressure, flow, and temperature simultaneously in an industrial process.

The following figure shows an example of the vibration signals from a steel-reinforced concrete beam. The signals are acquired simultaneously from seven acceleration sensors located at different positions on the beam.

[IMAGE alt='image' src='fp_tsa_multivariate.gif']

#### Stationary Time Series and Nonstationary Time Series

In theory, given a behavioral model for a system, you can predict future values of a time series measured from that system, based on past observations. However, in practice, physical systems are affected by many kinds of disturbances, so the predicted values always reflect the stochastic, or statistical, characteristic of a time series.

Generally speaking, if the statistical characteristic of a time series contains no systematic change, the time series is stationary. Otherwise the time series is nonstationary.

#### Time Series Analysis Objectives

Time series analysis is useful when you want to extract information from a time series, to discover the characteristics of a physical system that generates the time series, to predict the changes of a time series, or to improve control over the physical system. The objectives of time series analysis are as follows:

- Description —You can use the time series analysis methods to obtain descriptive or statistical measures of a time series. For example, to measure the trends or periodicity, you can plot the time series. To measure the symmetry of a time-series amplitude distribution, you can examine a histogram of the amplitude of a time series.
- Explanation —You can use the observed variation of a time series to explain the variation of a related time series, which can help you understand the nature of the relationship between the two signals. For example, you can explain the dynamic properties of a physical system by analyzing the input time series to and output time series from the system.
- Prediction —You can use observed values to predict the future values of a time series . For example, you can predict the future variation of a time series in an industrial process and make sure the process is working properly.
- Control —You can use the predicted values of a time series to determine appropriate corrective actions that you take to specify optimal settings for the controller and keep a physical system or process operating properly.

Time series exist in many application areas, ranging from economics to engineering. The LabVIEW Time Series Analysis Tools focus more on the applications in engineering. Use the [Time Series Analysis](../lvtimeseriestk/time_series_analysis_pal.html) VIs to analyze or process a time series.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tsa_power_cepstrum.html language=enus -->
## TOPIC 00029: Estimating the Power Cepstrum of a Time Series (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tsa_power_cepstrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tsa_power_cepstrum.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Estimating the Power Cepstrum of a Time Series (Advanced Signal Processing Toolkit)

The power cepstrum is an efficient tool for finding different harmonic families in the power spectral density (PSD) of a time series. A power cepstrum is the inverse FFT transform of the natural logarithm of the PSD. You can compute the power cepstrum of a time series as follows:

*C*(τ) = *FFT*<sup>–1</sup>(log(*PSD*))

The power cepstrum *C*(τ) is a real-valued time series.

The following figure shows the PSD and power cepstrum of a gearbox vibration signal, respectively.

[IMAGE alt='image' src='fp_tsa_psd_power_cepstrum.gif']

The **PSD** graph suggests that the signal contains both periodic and non-periodic components. In the **Power Cepstrum** graph, you can see that the power cepstrum gives a more clear indication of harmonic peak families than the PSD.

You can modify, or lifter, the power cepstrum and then transform it back to the PSD. The word *lifter* is an anagram of the word *filter*, formed by reversing the first three letters. By liftering the unnecessary harmonic peak families, you can remove an individual peak family from the PSD. The following figure shows the PSD of the gearbox vibration signal after you lifter all the harmonic peak families. Notice that the harmonic peaks in the liftered PSD have disappeared.

[IMAGE alt='image' src='fp_tsa_liftered_psd.gif']

To lifter the harmonic families, complete the following steps:

1. Compute the power cepstrum of the vibration signal from the PSD.
2. Remove harmonic peaks of individual harmonic family that you want to discard from the power cepstrum.
3. Reconstruct the PSD from the liftered power cepstrum.

If a PSD contains several harmonic families, use the [TSA Lifter PSD](../lvtimeseriestk/tsa_lifter_psd.html) VI to separate harmonic peaks in the PSD by computing the power cepstrum and filtering the unnecessary harmonic peaks in the cepstrum.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/tsa_power_spectrum_est.html language=enus -->
## TOPIC 00030: Power Spectrum Estimation Methods (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/tsa_power_spectrum_est.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/tsa_power_spectrum_est.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Power Spectrum Estimation Methods (Advanced Signal Processing Toolkit)

A power spectrum describes the energy distribution of a time series in the frequency domain. Energy is a real-valued quantity, so the power spectrum does not contain phase information. Because a time series may contain non-periodic or asynchronously-sampled periodic signal components, the power spectrum of a time series typically is considered to be a continuous function of frequency. When you use a series of discrete frequency bins to represent the continuous frequency, the value at a specific frequency bin is proportional to the frequency interval. To remove the dependence on the size of the frequency interval, you can normalize the power spectrum to produce the power spectral density (PSD), which is the power spectrum divided by the size of the frequency interval.

The PSD measures the signal power per unit bandwidth for a time series in V<sup>2</sup>/Hz, which implicitly assumes that the PSD represents a signal in volts driving a 1 ohm load. If the PSD is represented in a decibel (dB), the corresponding unit for the PSD is dB ref V/sqrt(Hz). If you want to use other units for the estimated PSD of a time series, you need to scale the unit of the time series into appropriate engineering units (EU). After scaling the unit of the time series, you can obtain the corresponding unit for the linear PSD value and the dB PSD value as EU <sup>2</sup>/Hz and dB ref EU/sqrt(Hz), respectively. Use the [TSA Scale to EU](../lvtimeseriestk/tsa_scale_to_eu.html) VI to scale the unit for a time series to appropriate EU.

PSD estimation methods are classified as follows:

- Parametric methods —These methods are based on parametric models of a time series, such as AR models, moving average (MA) models, and autoregressive-moving average (ARMA) models. Therefore, parametric methods also are known as model-based methods . To estimate the PSD of a time series with parametric methods, you need to obtain the model parameters of the time series first. You must build an appropriate model that correctly reflects the behavior of the system that generates the time series; otherwise, the estimated PSD might not be reliable.
 The multiple signal classification (MUSIC) method also is a model-based spectral estimation method.
- Nonparametric methods —These methods, which include the periodogram method , Welch method , and Capon method , are based on the discrete Fourier transform . You do not need to obtain the parameters of the time series before using these methods.

The primary limitation of nonparametric methods is that the computation uses [data windowing](/csh?topicname=lvanlsconcepts/windowing_signals.html), resulting in distortion of the resulting PSDs due to window effects. The key benefit of nonparametric methods is the robustness—the estimated PSDs do not contain spurious frequency peaks. In contrast, parametric methods do not use data windowing. Parametric methods assume a signal fits a particular model. The estimated PSDs may contain spurious frequency peaks if the assumed model is wrong. PSDs estimated with parametric methods are less biased and possess a lower variance than PSDs estimated with nonparametric methods if the assumed model is correct. However, the magnitudes of PSDs estimated with parametric methods usually are incorrect.

|  | Note During spectral analysis, you can average successive spectrum measurements to reduce estimation variance and improve measurement accuracy. Use the TSA Average PSD VI to average the estimated spectrum continuously. |
| --- | --- |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/wa_dwt.html language=enus -->
## TOPIC 00031: Discrete Wavelet Transform (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/wa_dwt.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/wa_dwt.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Discrete Wavelet Transform (Advanced Signal Processing Toolkit)

Unlike the [discrete Fourier transform (DFT)](/csh?topicname=lvanlsconcepts/discrete_fourier_transform.html), which is a discrete version of the [Fourier transform](/csh?topicname=lvanlsconcepts/fourier_transform.html), the discrete wavelet transform (DWT) is not really a discrete version of the [continuous wavelet transform (CWT)](wa_cwt.html). Instead, the DWT is functionally different from the CWT. To implement the DWT, you use discrete filter banks to compute discrete wavelet coefficients. Two-channel perfect reconstruction (PR) filter banks are a common and efficient way to implement the DWT. The following figure shows a typical two-channel PR filter bank system.

[IMAGE alt='image' src='pr_filter_bank.gif']

The signal *X*(*z*) first is filtered by a filter bank consisting of *G*<sub>0</sub>(*z*) and *G*<sub>1</sub>(*z*). The outputs of *G*<sub>0</sub>(*z*) and *G*<sub>1</sub>(*z*) then are downsampled by a factor of 2. After some processing, the modified signals are upsampled by a factor of 2 and filtered by another filter bank consisting of *H*<sub>0</sub>(*z*) and *H*<sub>1</sub>(*z*).

If no processing takes place between the two filter banks, the sum of outputs of *H*<sub>0</sub>(*z*) and *H*<sub>1</sub>(*z*) is identical to the original signal *X*(*z*), except for the time delay. This system is a two-channel PR filter bank, where *G*<sub>0</sub>(*z*) and *G*<sub>1</sub>(*z*) form an analysis filter bank, and *H*<sub>0</sub>(*z*) and *H*<sub>1</sub>(*z*) form a synthesis filter bank.

Traditionally, *G*<sub>0</sub>(*z*) and *H*<sub>0</sub>(*z*) are lowpass filters, and *G*<sub>1</sub>(*z*) and *H*<sub>1</sub>(*z*) are highpass filters. The subscripts 0 and 1 represent lowpass and highpass filters, respectively. The operation ↓2 denotes a decimation of the signal by a factor of two. Applying decimation factors to the signal ensures that the number of output samples of the two lowpass filters equal the number of original input samples *X*(*z*). Therefore, no redundant information is added during the decomposition. Refer to the LabVIEW Digital Filter Design Toolkit documentation for more information about filters.

You can use the two-channel PR filter bank system and consecutively decompose the outputs of lowpass filters, as shown in the following figure.

[IMAGE alt='image' src='dwt.gif']

Lowpass filters remove high-frequency fluctuations from the signal and preserve slow trends. The outputs of lowpass filters provide an approximation of the signal. Highpass filters remove the slow trends from the signal and preserve high-frequency fluctuations. The outputs of highpass filters provide detail information about the signal. The outputs of lowpass filters and highpass filters define the approximation coefficients and detail coefficients, respectively. Symbols ***A*** and ***D*** in the previous figure represent the approximation and detail information, respectively.

You also can call the detail coefficients *wavelet coefficients* because detail coefficients approximate the inner products of the signal and wavelets.

|  | Note This help alternately uses the terms wavelet coefficients and detail coefficients, depending on the context. |
| --- | --- |

The LabVIEW Wavelet Analysis Tools use the subscripts 0 and 1 to describe the decomposition path, where 0 indicates lowpass filtering and 1 indicates highpass filtering. For example, *D*<sub>2</sub> in the previous figure denotes the output of two cascaded filtering operations—lowpass filtering followed by highpass filtering. Therefore, you can describe this decomposition path with the sequence 01. Similarly, *D*<sub>*L*</sub> denotes the output of the filtering operations 000...1 in which the total number of 0 is *L*–1. The impulse response of 000...1 converges asymptotically to the mother wavelet and the impulse response of 000...0 converges to the scaling function in the wavelet transform.

The DWT is invertible, meaning that you can reconstruct the signal from the DWT coefficients with the inverse DWT. The inverse DWT also is implemented with filter banks by cascading the synthesis filter banks. The following figure shows the inverse DWT using filter banks.

[IMAGE alt='image' src='inverse_dwt.gif']

Use the [WA Discrete Wavelet Transform](../lvwavelettk/wa_discrete_wavelet_transform.html) VI to compute the DWT of 1D and 2D signals. Use the [WA Inverse Discrete Wavelet Transform](../lvwavelettk/wa_inverse_1d_discrete_wavelet_transform.html) VI to compute the inverse DWT of 1D and 2D signals. Use the [WA Get Coefficients of Discrete Wavelet Transform](../lvwavelettk/wa_getdwtcoef.html) VI to get DWT coefficients you compute from the WA Discrete Wavelet Transform VI and to return the coefficient type, such as the approximation coefficients or the detail coefficients, at a specific coefficient level. Use the [WA Set Coefficients of Discrete Wavelet Transform](../lvwavelettk/wa_setdwtcoef.html) VI to set the coefficients you obtain from the WA Get Coefficients of Discrete Wavelet Transform VI.

Refer to the Get and Set Approximation Coefficients VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of how to get and set the approximation coefficients that you compute from the discrete wavelet transform.

Refer to the Get and Set Single Level Detail Coefficients VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of how to get and set the detail coefficients that you compute from the discrete wavelet transform.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/wa_intro.html language=enus -->
## TOPIC 00032: Introduction to Wavelet Signal Processing (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/wa_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/wa_intro.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Introduction to Wavelet Signal Processing (Advanced Signal Processing Toolkit)

Wavelets are functions that you can use to decompose signals. Just as the [Fourier transform](/csh?topicname=lvanlsconcepts/fourier_transform.html) decomposes a signal into a family of complex sinusoids, the [wavelet transform](wa_intro.html#wavelet_transform) decomposes a signal into a family of wavelets. Unlike sinusoids, which are symmetric, smooth, and regular, wavelets can be either symmetric or asymmetric, sharp or smooth, regular or irregular. The following figure compares a sine wave with the db02 wavelet and the [FBI wavelet](designing_fbi_wavelet.html).

[IMAGE alt='image' src='fp_wa_sine_vs_wavelet.gif']

In previous figure, you can see that the **Sine Wave** is symmetric, smooth, and regular. The **db02 Wavelet** is asymmetric, sharp, and irregular. The **FBI Wavelet** is symmetric, smooth, and regular. You also can see that a sine wave has an infinite length, whereas a wavelet has a finite length.

For different types of signals, you can select different types of wavelets that best match the features of the signal you want to analyze. Therefore, you can perform wavelet signal processing and generate reliable results about the underlying information of a signal.

The family of wavelets contains the dilated and translated versions of a prototype function. Traditionally, the prototype function is called a mother wavelet. The scale and shift of wavelets determine how the mother wavelet dilates and translates along the time or space axis. A scale factor greater than one corresponds to a dilation of the mother wavelet along the horizontal axis, and a positive shift corresponds to a translation to the right of the scaled wavelet along the horizontal axis. The following figure shows the db02 mother wavelet and the associated dilated and translated wavelets with different scale factors and shift values.

[IMAGE alt='image' src='fp_wa_scale_shift.gif']

#### Wavelet Transform

The wavelet transform computes the inner products of a signal with a family of wavelets. The wavelet transform tools are categorized into [continuous wavelet](cont_wavelets.html) tools and [discrete wavelet](wa_discrete.html) tools. Usually, you use the continuous wavelet tools for signal analysis, such as self-similarity analysis and time-frequency analysis. You use the discrete wavelet tools for both signal analysis and signal processing, such as noise reduction, data compression, peak detection and so on.

In contrast with sinusoids, wavelets are localized in both the time and frequency domains, so wavelet signal processing is suitable for nonstationary signals, whose spectral content changes over time. The adaptive time-frequency resolution of wavelet signal processing enables you to perform multiresolution analysis on nonstationary signals. The properties of wavelets and the flexibility to select wavelets make wavelet signal processing a beneficial tool for feature extraction applications.

#### Benefits of Wavelet Signal Processing

Wavelet signal processing is different from other signal processing methods because of the unique properties of wavelets. For example, wavelets are irregular in shape and finite in length. Wavelet signal processing can represent signals sparsely, capture the transient features of signals, and enable signal analysis at multiple resolutions.

##### Sparse Representation

Wavelets are localized in both the time and frequency domains because wavelets have limited time duration and frequency bandwidth. The wavelet transform can represent a signal with a few coefficients because of the localization property of wavelets. The following figure shows the waveform of the Doppler signal.

[IMAGE alt='image' src='fp_wa_doppler_signal.gif']

The following figure shows the [discrete wavelet transform (DWT)](wa_dwt.html) coefficients of the Doppler signal.

[IMAGE alt='image' src='fp_wa_doppler_dwt.gif']

In the previous figure, most of the DWT coefficients are zero, which indicates that the wavelet transform is a useful method to represent signals sparsely and compactly. Therefore, you usually use the DWT in some signal compression applications.

##### Transient Feature Detection

Transient features are sudden changes or discontinuities in a signal. A transient feature can be generated by the impulsive action of a system and frequently implies a causal relationship to an event. For example, heartbeats generate peaks in an electrocardiogram (ECG) signal.

Transient features generally are not smooth and are of short duration. Because wavelets are flexible in shape and have short time durations, the wavelet signal processing methods can capture transient features precisely. The following figure shows an ECG signal and the peaks detected with the wavelet transform-based method. This method locates the peaks of the ECG signal precisely.

[IMAGE alt='image' src='fp_wa_ecg_peak.gif']

Refer to the ECG QRS Complex Detection VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of wavelet transform-based peak detection in an ECQ signal.

The LabVIEW Wavelet Analysis Tools provide many [types of wavelets](wa_discrete.html#selecting_an_appropriate_discrete_wavelet), such as the Daubechies, Haar, and Coiflet wavelets.

##### Multiple Resolutions

Signals usually contain both low-frequency components and high-frequency components. Low-frequency components vary slowly with time and require fine frequency resolution but coarse time resolution. High-frequency components vary quickly with time and require fine time resolution but coarse frequency resolution. You need to use a multiresolution analysis (MRA) method to analyze a signal that contains both low- and high-frequency components.

Wavelet signal processing is naturally an MRA method because of the dilation process. The following figure shows the wavelets with different dilations and their corresponding power spectra.

[IMAGE alt='image' src='fp_wa_frequency_bands_wavelets.gif']

The **Wavelets** graph contains three wavelets with different scales and translations. The **Power Spectra of Wavelets** graph shows the power spectra of the three wavelets, where a and u represent the scale and shift of the wavelets, respectively. The previous figure shows that a wavelet with a small scale has a short time duration, a wide frequency bandwidth, and a high central frequency. This figure also shows that a wavelet with a large scale has a long time duration, a narrow frequency bandwidth, and a low central frequency.

The time duration and frequency bandwidth determine the time and frequency resolutions of a wavelet, respectively. A long time duration means coarse time resolution. A wide frequency bandwidth means coarse frequency resolution. The following figure shows the time and frequency resolutions of the three wavelets with three boxes in the time-frequency domain. The heights and widths of the boxes represent the frequency and time resolutions of the wavelets, respectively. This figure shows that a wavelet with a small scale has fine time resolution but coarse frequency resolution and that a wavelet with a large scale has fine frequency resolution but coarse time resolution.

[IMAGE alt='image' src='multiresolution_box.gif']

The fine frequency resolution of large-scale wavelets enables you to measure the frequency of the slow variation components in a signal. The fine time resolution of small-scale wavelets enables you to detect the fast variation components in a signal. Therefore, wavelet signal processing is a useful [multiresolution analysis](wa_dwt_mra.html) tool.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/wa_iwt.html language=enus -->
## TOPIC 00033: Integer Wavelet Transform (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/wa_iwt.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/wa_iwt.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Integer Wavelet Transform (Advanced Signal Processing Toolkit)

Many signal samples you encounter in real-world [applications](wa_application.html) are encoded as integers, such as the signal amplitudes encoded by analog-to-digital (A/D) converters and color intensities of pixels encoded in digital images. For integer-encoded signals, an integer wavelet transform (IWT) can be particularly efficient. The IWT is an invertible integer-to-integer wavelet analysis algorithm. You can use the IWT in the applications that you want to produce integer coefficients for integer-encoded signals. Compared with the [continuous wavelet transform (CWT)](wa_cwt.html) and the [discrete wavelet transform (DWT)](wa_dwt.html), the IWT is not only computationally faster and more memory-efficient but also more suitable in lossless data-compression applications. The IWT enables you to reconstruct an integer signal perfectly from the computed integer coefficients.

Use the [WA Integer Wavelet Transform](../lvwavelettk/wa_integer_wavelet_transform.html) VI, which implements the IWT with the lifting scheme, to decompose an integer signal or image. Use the [WA Inverse Integer Wavelet Transform](../lvwavelettk/wa_inverse_integer_wavelet_transform.html) VI, which implements the inverse IWT with the inverse lifting scheme, to reconstruct an integer signal or image from the IWT coefficients. Use the [WA Get Coefficients of Integer Wavelet Transform](../lvwavelettk/wa_getiwtcoef.html) VI to get the IWT coefficients you compute from the WA Integer Wavelet Transform VI and to return the coefficient type, such as the approximation coefficients or the detail coefficients, at a specific coefficient level. Use the [WA Set Coefficients of Integer Wavelet Transform](../lvwavelettk/wa_setiwtcoef.html) VI to set the coefficients you obtain from the WA Get Coefficients of Integer Wavelet Transform VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/wa_lossless_compression.html language=enus -->
## TOPIC 00034: Application Example: Lossless Compression (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/wa_lossless_compression.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/wa_lossless_compression.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Application Example: Lossless Compression (Advanced Signal Processing Toolkit)

When you apply the [discrete wavelet transform (DWT)](wa_dwt.html) to integer signal samples, you convert the original integer signal samples to floating-point wavelet coefficients. In signal compression applications, you typically further quantize these coefficients to an integer representation before entropy-based encoding. As a result, compression with the DWT is lossy, meaning that some information is lost when you compress a signal using the DWT, and that you typically cannot reconstruct the original signal perfectly from the coefficients of the DWT.

The [integer wavelet transform (IWT)](wa_iwt.html), however, provides lossless compression. You can use the IWT to convert integer signal samples into integer wavelet coefficients, and you can compress these integer coefficients by entropy-based encoding without further quantization. As a result, you can reconstruct the original signal perfectly from a compressed set of IWT coefficients. The following figure shows an example of lossless compression with the IWT.

[IMAGE alt='image' src='fp_wa_lossless_example.gif']

In the **Histogram** graph, most of the elements in the **IWT Coefficients** plot are zero, meaning that you can obtain a high compression ratio using the IWT of this image. You can reconstruct the image perfectly with the inverse IWT, as shown in the **Reconstructed Image** graph. The **Maximum Difference** value of 0 indicates that the reconstructed image retains all the information of the original image.

Refer to the Lossless Medical Image Compression VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of lossless compression.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/wa_overview.html language=enus -->
## TOPIC 00035: Overview of LabVIEW Wavelet Analysis Tools (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/wa_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/wa_overview.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Overview of LabVIEW Wavelet Analysis Tools (Advanced Signal Processing Toolkit)

The LabVIEW Wavelet Analysis Tools provide a collection of Wavelet Analysis VIs that assist you in processing signals in the LabVIEW environment. You can use the [Continuous Wavelet](../lvwavelettk/continuouswaveletpal.html) VIs, the [Discrete Wavelet](../lvwavelettk/discretewaveletpal.html) VIs, and the [Wavelet Packet](../lvwavelettk/waveletpacketpal.html) VIs to perform the continuous wavelet transform, the discrete wavelet transform, the undecimated wavelet transform, the integer wavelet transform, and the wavelet packet decomposition. You can use the [Feature Extraction](../lvwavelettk/waveletapplicationpal.html) VIs to detrend and denoise a signal. You also can use these VIs to detect the peaks and edges of a signal.

The Wavelet Analysis Tools provide a collection of commonly used continuous wavelets, such as Mexican Hat, Meyer, and Morlet, and a collection of commonly used [discrete wavelets](wa_discrete.html#selecting_an_appropriate_discrete_wavelet), such as the Daubechies, Haar, Coiflet, and biorthogonal wavelets. You also can [create a discrete wavelet](wa_design_discrete.html) that best matches the signal you analyze by using the [Wavelet Design](../lvwavelettk/wavelet_design.html) Express VI.

The Wavelet Analysis Tools contain Express VIs that provide interfaces for signal processing and analysis. These Express VIs enable you to specify parameters and settings for an analysis and see the results immediately. For example, the [Wavelet Denoise](../lvwavelettk/wavelet_denoise.html) Express VI graphs both the original and denoised signals. You can see the denoised signal immediately as you select a wavelet, specify a threshold, and set other parameters. The Wavelet Analysis Tools also provide Express VIs for multiresolution analysis, wavelet design, and wavelet packet decomposition.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvasptconcepts/wa_uwt.html language=enus -->
## TOPIC 00036: Undecimated Wavelet Transform (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvasptconcepts/wa_uwt.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvasptconcepts/wa_uwt.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Undecimated Wavelet Transform (Advanced Signal Processing Toolkit)

Unlike the [discrete wavelet transform (DWT)](wa_dwt.html), which downsamples the approximation coefficients and detail coefficients at each decomposition level, the undecimated wavelet transform (UWT) does not incorporate the downsampling operations. Thus, the approximation coefficients and detail coefficients at each level are the same length as the original signal. The UWT upsamples the coefficients of the lowpass and highpass filters at each level. The upsampling operation is equivalent to dilating wavelets. The resolution of the UWT coefficients decreases with increasing levels of decomposition.

Use the [WA Undecimated Wavelet Transform](../lvwavelettk/wa_undecimated_wavelet_transform.html) VI and the [WA Inverse Undecimated Wavelet Transform](../lvwavelettk/wa_inverse_undecimated_wavelet_transform.html) VI to decompose and reconstruct 1D or 2D signals.

By comparing the UWT with the DWT, the UWT has some unique features.

#### Translation-Invariant Property

Unlike the DWT, the UWT has the translation-invariant, or shift-invariant, property. If two signals are shifted versions of each other, the UWT results for the two signals also are shifted versions of each other. The translation-invariant property is important in feature-extraction applications.

The following figure shows an example that detects discontinuities in the HeaviSine signal with both the DWT and the UWT.

[IMAGE alt='image' src='fp_wa_uwt_dwt.gif']

You can use the first-level detail coefficients of either the DWT or the UWT to detect the discontinuities in the HeaviSine signal by locating the peaks in the coefficients. However, if the HeaviSine signal is shifted by 21 samples, all of the first-level DWT detail coefficients become very small. Therefore, you cannot use the first-level DWT detail coefficients to detect the discontinuities in the shifted HeaviSine signal. Because of the translation-invariant property of the UWT, you can use the first-level UWT detail coefficients to detect the discontinuities of the shifted HeaviSine Signal. The first-level UWT detail coefficients of the shifted HeaviSine Signal are simply the shifted version of the first-level UWT detail coefficients of the original HeaviSine signal.

Use the [WA Get Coefficients of Undecimated Wavelet Transform](../lvwavelettk/wa_getuwtcoef.html) VI to get the UWT coefficients you compute from the WA Undecimated Wavelet Transform VI and to return the coefficient type, such as the approximation coefficients or the detail coefficients, at a specific coefficient level. Use the [WA Set Coefficients of Undecimated Wavelet Transform](../lvwavelettk/wa_setuwtcoef.html) VI to set the coefficients you obtain from the WA Get Coefficients of Undecimated Wavelet Transform VI.

#### Better Denoising Capability

Denoising with the UWT also is shift-invariant. The denoising result of the UWT has a better balance between smoothness and accuracy than the DWT. The DWT-based method is more computationally efficient than the UWT-based method. However, you cannot achieve both smoothness and accuracy with the DWT-based denoising method.

Use the [Wavelet Denoise](../lvwavelettk/wavelet_denoise.html) Express VI or the [WA Denoise](../lvwavelettk/wa_de_noise.html) VI to reduce noise in 1D signals with both the UWT-based and DWT-based methods. The UWT-based method supports both real and complex signals. The DWT-based method supports only real signals. You also can use the WA Denoise VI to reduce noise in 2D signals with the UWT-based method.

The denoising procedure in the Wavelet Denoise Express VI and the WA Denoise VI involves the following steps:

1. Applies the DWT or the UWT to noise-contaminated signals to obtain the DWT coefficients or the UWT coefficients. The noise in signals usually corresponds to the coefficients with small values.
2. Selects an appropriate threshold for the DWT coefficients or the UWT coefficients to set the coefficients with small values to zero. The Wavelet Denoise Express VI and the WA Denoise VI provide methods that automatically select the thresholds. The bound of noise reduction with these methods is 3 dB. To achieve better denoising performance for a signal, you can select an appropriate threshold manually by specifying the user defined thresholds parameter of the WA Denoise VI.
3. Reconstructs the signal with the inverse DWT or the inverse UWT.

The following figure shows the denoising results of a noisy Doppler signal with both the DWT-based method and the UWT-based method. Both methods use the level-5 wavelet transform and the soft threshold.

[IMAGE alt='image' src='fp_wa_denoising_dwt_uwt.gif']

In the previous figure, you can see that the UWT outperforms the DWT in signal denoising because the denoised signal in the **Denoising with UWT** graph is smoother.

Refer to the Denoise - 1D Real Signal VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of DWT-based and UWT-based methods for denoising a 1D real signal.

Refer to the Denoise - 1D Complex Signal VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of DWT-based and UWT-based methods for denoising a 1D complex signal.

Refer to the Denoise - Image VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of DWT-based and UWT-based methods for denoising a 2D signal.

#### Better Peak Detection Capability

Peaks often imply important information about a signal. You can use the UWT to identify the peaks in a noise-contaminated signal.

The UWT-based peak detection method is more robust and less sensitive to noise than the DWT-based method, because the UWT-based method involves finding zero-crossings in the multiscale UWT coefficients. The UWT-based method first finds zero-crossings among the coefficients with coarse resolution and then finds zero-crossings among the coefficients with finer resolution. Finding zero-crossings among the coefficients with coarse resolution enables you to remove noise from a signal efficiently. Finding zero-crossings among the coefficients with finer resolution improves the precision with which you can find peak locations.

The [WA Multiscale Peak Detection](../lvwavelettk/wa_multiscale_peak_detection.html) VI and the [WA Online Multiscale Peak Detection](../lvwavelettk/wa_online_multiscale_peak_detection.html) VI use the UWT-based method. These VIs detect peaks in offline and online signals. You can use these VIs in the following ways:

- Use the WA Multiscale Peak Detection VI once for an offline signal
- Use the WA Online Multiscale Peak Detection VI continuously for a block of signals
- Use the WA Online Multiscale Peak Detection VI continuously for signals from streaming data sources

The following figure shows an example that uses the WA Online Multiscale Peak Detection VI to detect peaks in an electrocardiogram (ECG) signal. The UWT-based method locates the peaks of the ECG signal accurately, regardless of whether the peaks are sharp or rounded.

[IMAGE alt='image' src='fp_wa_ecg_peak.gif']

Refer to the ECG Heart Rate Monitor (Online) VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of how to use the WA Online Multiscale Peak Detection VI to detect peaks in an ECG signal.

Refer to the ECG QRS Complex Detection VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of wavelet-based peak detection in biomedical engineering.

Refer to the Peak Detection (Wavelet vs. Normal) VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example that compares the wavelet transform-based peak detection method with the traditional curve fitting-based method.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/check_system_model.html language=enus -->
## TOPIC 00037: SI Check System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/check_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/check_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Check System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Verifies whether the model order matches the number of coefficients in **system model**.

[IMAGE alt='image' src='si_check_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | valid returns TRUE if the data dimensions are consistent with the model parameters in system model. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/cnvrt_continuous_to_discrete.html language=enus -->
## TOPIC 00038: SI Convert Continuous to Discrete Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/cnvrt_continuous_to_discrete.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/cnvrt_continuous_to_discrete.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Convert Continuous to Discrete Model VI

**Owning Palette:** [Model Conversion VIs](../lvsysid/model_conversion_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Converts a continuous model to a discrete model using the **sampling rate** you specify. You can use this VI to convert continuous [transfer function](../lvsysidconcepts/modeldefinitionstf.html), [state-space](../lvsysidconcepts/modeldefinitionsss.html), and [zero-pole-gain](../lvsysidconcepts/modeldefinitionszpg.html) models to discrete transfer function, state-space, and zero-pole-gain models, respectively.

[Details](#details)

[IMAGE alt='image' src='si_convert_continuous_to_discrete_model.gif']

|  | system model in contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model in contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sampling rate (Hz) is the sampling frequency, in hertz, of the corresponding discrete model to which this VI converts the continuous model. |
|  | tolerance determines zero-pole cancellations. If the difference between the location of a pole and a zero is within the tolerance, this VI removes the zero-pole pair. You can visually inspect the location difference in the pole-zero plot. The default is 1E-12. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Convert Continuous to Discrete Model Details

This VI accepts only continuous transfer function, state-space, and zero-pole-gain models and converts these continuous models to their discrete equivalents. For [ARX](../lvsysidconcepts/modeldefinitionsarx.html), [ARMAX](../lvsysidconcepts/modeldefinitionsarmax.html), [output-error](../lvsysidconcepts/modeldefinitionsoe.html), [Box-Jenkins](../lvsysidconcepts/modeldefinitionsbj.html), and [general-linear](../lvsysidconcepts/modeldefinitionsgl.html) models, use the [SI Model Conversion](../lvsysid/model_conversion_vi.html) VI to convert these models to transfer function, state-space, or zero-pole-gain models.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/cnvrt_discrete_to_continuous.html language=enus -->
## TOPIC 00039: SI Convert Discrete to Continuous Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/cnvrt_discrete_to_continuous.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/cnvrt_discrete_to_continuous.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Convert Discrete to Continuous Model VI

**Owning Palette:** [Model Conversion VIs](../lvsysid/model_conversion_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Converts a discrete model to a continuous model. You can use this VI to convert discrete [transfer function](../lvsysidconcepts/modeldefinitionstf.html), [state-space](../lvsysidconcepts/modeldefinitionsss.html), and [zero-pole-gain](../lvsysidconcepts/modeldefinitionszpg.html) models to continuous transfer function, state-space, and zero-pole-gain models, respectively.

For an [ARX](../lvsysidconcepts/modeldefinitionsarx.html), [ARMAX](../lvsysidconcepts/modeldefinitionsarmax.html), [output-error](../lvsysidconcepts/modeldefinitionsoe.html), [Box-Jenkins](../lvsysidconcepts/modeldefinitionsbj.html), or [general-linear](../lvsysidconcepts/modeldefinitionsgl.html) model, this VI converts the discrete model to a continuous transfer function model.

[Example](#examples)

[IMAGE alt='image' src='si_convert_discrete_to_continuous_model.gif']

|  | system model in contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model in contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | tolerance determines zero-pole cancellations. If the difference between the location of a pole and a zero is within the tolerance, this VI removes the zero-pole pair. You can visually inspect the location difference in the pole-zero plot. The default is 1E-12. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Model Conversion VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Convert Discrete to Continuous Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/create_system_model.html language=enus -->
## TOPIC 00040: SI Create System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/create_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/create_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Create System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Creates a model for an unknown system.

[Examples](#examples)

[IMAGE alt='image' src='si_create_system_modelc.gif']

|  | model type specifies the type of model to create. Note: If you set model type to Undefined, this VI creates a model with an empty type. 0Undefined1AR2ARX (SISO) (default)3ARX (MISO)4ARX (MIMO)5ARMAX (SISO)6ARMAX (MISO)7Output-Error (SISO)8Output-Error (MISO)9Box-Jenkins (SISO)10Box-Jenkins (MISO)11General-Linear (SISO)12General-Linear (MISO)13State-Space (SISO)14State-Space (MISO)15State-Space (MIMO)16Transfer Function (SISO)17Transfer Function (MISO)18Transfer Function (MIMO)19Zero-Pole-Gain (SISO)20Zero-Pole-Gain (MISO)21Zero-Pole-Gain (MIMO) |
| --- | --- |
|  | Note: If you set model type to Undefined, this VI creates a model with an empty type. |
| 0 | Undefined |
| 1 | AR |
| 2 | ARX (SISO) (default) |
| 3 | ARX (MISO) |
| 4 | ARX (MIMO) |
| 5 | ARMAX (SISO) |
| 6 | ARMAX (MISO) |
| 7 | Output-Error (SISO) |
| 8 | Output-Error (MISO) |
| 9 | Box-Jenkins (SISO) |
| 10 | Box-Jenkins (MISO) |
| 11 | General-Linear (SISO) |
| 12 | General-Linear (MISO) |
| 13 | State-Space (SISO) |
| 14 | State-Space (MISO) |
| 15 | State-Space (MIMO) |
| 16 | Transfer Function (SISO) |
| 17 | Transfer Function (MISO) |
| 18 | Transfer Function (MIMO) |
| 19 | Zero-Pole-Gain (SISO) |
| 20 | Zero-Pole-Gain (MISO) |
| 21 | Zero-Pole-Gain (MIMO) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the SI Create System Model VI:

- Continuous Transfer Function Model of 1st order RC Circuit VI: labview\examples\System Identification\Getting Started\Continuous Model.llb
- Continuous Transfer Function Model of 2nd order RC Circuit VI: labview\examples\System Identification\Getting Started\Continuous Model.llb

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/data_preprocess_pal.html language=enus -->
## TOPIC 00041: Data Preprocessing VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/data_preprocess_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/data_preprocess_pal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Data Preprocessing VIs

**Owning Palette:** [System Identification VIs](../lvsysid/lv_sysid_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Data Preprocessing VIs to preprocess the raw data that you acquired from an unknown system.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific System Identification error codes](../lvsysid/sysid_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SI Bandpass Filter | Applies a bandpass filter to stimulus and response signals. Wire data to the signal in and stimulus signal in inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Detect Feedback | Detects if feedback exists in a system using the impulse response of the system. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Down Sampling | Reduces the sampling rate of stimulus and response signals using decimation. Wire data to the stimulus signal in and response signal in inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Lowpass Filter | Applies a lowpass filter to stimulus and response signals. Wire data to the stimulus signal in and response signal in inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Normalize | Normalizes the stimulus and response signals so that their mean and standard deviation are 0 and 1 respectively. Wire data to the stimulus signal in and response signal in inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Rebuild Missing Data | Rebuilds corrupted or missing parts of stimulus and response signals. Wire data to the stimulus signal in and response signal in inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Remove Trend | Removes mean and linear steady-state trends from stimulus and response signals. Wire data to the stimulus signal in and response signal in inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Split Signal | Splits stimulus and response signals into two parts. Use one set of signals for model estimation and one for model validation. Wire data to the stimulus signal in and response signal in inputs to determine the polymorphic instance to use or manually select the instance. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/get_continuous_tf_denominator_info.html language=enus -->
## TOPIC 00042: SI Get Continuous Transfer Function Denominator Information VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/get_continuous_tf_denominator_info.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/get_continuous_tf_denominator_info.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Get Continuous Transfer Function Denominator Information VI

**Owning Palette:** [Utilities VIs](../lvsysid/sysid_utility_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Returns the denominator from a continuous [transfer function](../lvsysidconcepts/modeldefinitionstf.html) model, including Tp, natural frequency, and damping ratio.

#### SI Get Continuous Transfer Function Denominator Information (SISO)

[IMAGE alt='image' src='si_get_continuous_transfer_function_denominator_information_(siso).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Tp returns the time constant of the continuous transfer function model. |
|  | natural freq & damping ratio returns the natural frequency and damping ratio of the continuous transfer function models. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Get Continuous Transfer Function Denominator Information (MISO)

[IMAGE alt='image' src='si_get_continuous_transfer_function_denominator_information_(miso).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Tp returns the time constants of the continuous transfer function models. |
|  | natural freq & damping ratio returns the natural frequencies and damping ratios of the continuous transfer function models. natural freq (rad/s) returns the natural frequencies of the continuous transfer function models. damping ratio returns the damping ratios of the continuous transfer function models. |
|  | natural freq (rad/s) returns the natural frequencies of the continuous transfer function models. |
|  | damping ratio returns the damping ratios of the continuous transfer function models. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Get Continuous Transfer Function Denominator Information (MIMO)

[IMAGE alt='image' src='si_get_continuous_transfer_function_denominator_information_(mimo).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Tp returns the time constants of the continuous transfer function models. |
|  | natural freq & damping ratio returns the natural frequencies and damping ratios of the continuous transfer function models. natural freq (rad/s) returns the natural frequencies of the continuous transfer function models. damping ratio returns the damping ratios of the continuous transfer function models. |
|  | natural freq (rad/s) returns the natural frequencies of the continuous transfer function models. |
|  | damping ratio returns the damping ratios of the continuous transfer function models. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/get_delays_from_system_model.html language=enus -->
## TOPIC 00043: SI Get Delays from System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/get_delays_from_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/get_delays_from_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Get Delays from System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Returns the delay of the system from the system model. You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance to use.

[Details](#details)

#### SI Get Delays from System Model (SISO)

[IMAGE alt='image' src='si_get_delays_from_system_model_(siso).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | delay returns the delay of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Get Delays from System Model (MISO)

[IMAGE alt='image' src='si_get_delays_from_system_model_(miso).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | delays returns the delays of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Get Delays from System Model (MIMO)

[IMAGE alt='image' src='si_get_delays_from_system_model_(mimo).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | delays returns the delays of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Get Delays from System Model Details

The System Identification VIs handle delays differently for discrete and continuous systems.

Discrete systems include delays in coefficients of the system model. For example, if a system has a delay of 2, the system adjusts the coefficients to 0, 0, *a*1, *a*2,…. You can use the SI Get Delays from System Model VI to determine delays, in number of samples, of discrete systems. You also can use the [SI Get Orders of System Model](../lvsysid/get_orders_sys_model.html) VI to determine the delays in discrete systems.

Continuous systems save delays separately from coefficients. For example, if a system has a delay of 2, the system saves the information of delay separately and does not modify the coefficients. You can use the SI Get Delays from System Model VI to retrieve delays in seconds for continuous systems.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/get_dimensions_sys_model.html language=enus -->
## TOPIC 00044: SI Get Dimensions of System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/get_dimensions_sys_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/get_dimensions_sys_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Get Dimensions of System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Obtains the number of inputs and outputs for a system model.

[Example](#examples)

[IMAGE alt='image' src='si_get_dimensions_of_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of inputs returns the number of stimulus signals of the system model. |
|  | number of outputs returns the number of response signals of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Read Information from Model VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Get Dimensions of System Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/get_names_system_model.html language=enus -->
## TOPIC 00045: SI Get Names from System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/get_names_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/get_names_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Get Names from System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Reads input and output names from a system model. Use the [SI Set Names to System Model](../lvsysid/set_names_system_model.html) VI to write input and output names to a system model.

[Example](#examples)

[IMAGE alt='image' src='si_get_names_from_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | input names returns the names of the system model stimulus signals. |
|  | output names returns the names of the system model response signals. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Read Information from Model VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Get Names from System Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/get_noise_covar_sys_model.html language=enus -->
## TOPIC 00046: SI Get Noise Covariance from System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/get_noise_covar_sys_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/get_noise_covar_sys_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Get Noise Covariance from System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Obtains **noise variance** and **noise covariance** from a system model. Use the [SI Set Noise Covariance to System Model](../lvsysid/set_noise_covar_sys_model.html) VI to apply noise variance and noise covariance to a system model.

[Example](#examples)

[IMAGE alt='image' src='si_get_noise_covariance_from_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | noise variance returns the variance of the disturbance for a SISO or MISO system. noise variance returns –1 if system model contains a MIMO system. |
|  | noise covariance returns the covariance of the disturbances for a MIMO system. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Read Information from Model VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Get Noise Covariance from System Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/get_static_gains_from_system_model.html language=enus -->
## TOPIC 00047: SI Get Static Gains from System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/get_static_gains_from_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/get_static_gains_from_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Get Static Gains from System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Returns the static gain from a system model. The system model you wire to the **system model** input determines the polymorphic instance to use.

#### SI Get Static Gains from System Model (SISO)

[IMAGE alt='image' src='si_get_static_gains_from_system_model_(siso).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | static gain returns the static gain of the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Get Static Gains from System Model (MISO)

[IMAGE alt='image' src='si_get_static_gains_from_system_model_(miso).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | static gains returns the static gain of the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Get Static Gains from System Model (MIMO)

[IMAGE alt='image' src='si_get_static_gains_from_system_model_(mimo).gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | static gains returns the static gain of the model. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/get_type_of_sys_mdl.html language=enus -->
## TOPIC 00048: SI Get Type of System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/get_type_of_sys_mdl.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/get_type_of_sys_mdl.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Get Type of System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Reads the model type from **system model**. The number of inputs and outputs of the model determines its system type.

[Example](#examples)

[IMAGE alt='image' src='si_get_type_of_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model type returns the model type and indicates if the system type is SISO, MISO, or MIMO. 0Undefined (default)1AR2ARX (SISO)3ARX (MISO)4ARX (MIMO)5ARMAX (SISO)6ARMAX (MISO)7Output-Error (SISO)8Output-Error (MISO)9Box-Jenkins (SISO)10Box-Jenkins (MISO)11General-Linear (SISO)12General-Linear (MISO)13State-Space (SISO)14State-Space (MISO)15State-Space (MIMO)16Transfer Function (SISO)17Transfer Function (MISO)18Transfer Function (MIMO)19Zero-Pole-Gain (SISO)20Zero-Pole-Gain (MISO)21Zero-Pole-Gain (MIMO) |
| 0 | Undefined (default) |
| 1 | AR |
| 2 | ARX (SISO) |
| 3 | ARX (MISO) |
| 4 | ARX (MIMO) |
| 5 | ARMAX (SISO) |
| 6 | ARMAX (MISO) |
| 7 | Output-Error (SISO) |
| 8 | Output-Error (MISO) |
| 9 | Box-Jenkins (SISO) |
| 10 | Box-Jenkins (MISO) |
| 11 | General-Linear (SISO) |
| 12 | General-Linear (MISO) |
| 13 | State-Space (SISO) |
| 14 | State-Space (MISO) |
| 15 | State-Space (MIMO) |
| 16 | Transfer Function (SISO) |
| 17 | Transfer Function (MISO) |
| 18 | Transfer Function (MIMO) |
| 19 | Zero-Pole-Gain (SISO) |
| 20 | Zero-Pole-Gain (MISO) |
| 21 | Zero-Pole-Gain (MIMO) |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Read Information from Model VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Get Type of System Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/load_sys_model_from_file.html language=enus -->
## TOPIC 00049: SI Load System Model from File VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/load_sys_model_from_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/load_sys_model_from_file.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Load System Model from File VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Loads a system model from a .sim file. A .sim file is a system identification model file that saves all model coefficients regardless of the model type. Use the [SI Save System Model to File](../lvsysid/save_sys_model_to_file.html) VI to save a system model to a .sim file.

[Example](#examples)

[IMAGE alt='image' src='si_load_system_model_from_filec.gif']

|  | file path specifies the path to the file from which you want to load the system model. If you specify a valid path in file path, this VI loads the model from the file whose path is file path. If file path is empty (default) or is <Not A Path>, this VI displays a dialog box from which you can select a file. You receive an error if you do not specify file path. |
| --- | --- |
|  | start path specifies the path to the initially displayed directory or folder in the Open a file containing system identification model dialog box. If you do not specify a valid path in file path, the Open a file containing system identification model dialog box opens. You can select the file from which you want to load the system model from this dialog box. The default value is <Not A Path>, which is the path to the last directory or folder shown in the Open a file containing system identification model dialog box. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | model type returns the model type and indicates if the system type is SISO, MISO, or MIMO. 0Undefined (default)1AR2ARX (SISO)3ARX (MISO)4ARX (MIMO)5ARMAX (SISO)6ARMAX (MISO)7Output-Error (SISO)8Output-Error (MISO)9Box-Jenkins (SISO)10Box-Jenkins (MISO)11General-Linear (SISO)12General-Linear (MISO)13State-Space (SISO)14State-Space (MISO)15State-Space (MIMO)16Transfer Function (SISO)17Transfer Function (MISO)18Transfer Function (MIMO)19Zero-Pole-Gain (SISO)20Zero-Pole-Gain (MISO)21Zero-Pole-Gain (MIMO) |
| 0 | Undefined (default) |
| 1 | AR |
| 2 | ARX (SISO) |
| 3 | ARX (MISO) |
| 4 | ARX (MIMO) |
| 5 | ARMAX (SISO) |
| 6 | ARMAX (MISO) |
| 7 | Output-Error (SISO) |
| 8 | Output-Error (MISO) |
| 9 | Box-Jenkins (SISO) |
| 10 | Box-Jenkins (MISO) |
| 11 | General-Linear (SISO) |
| 12 | General-Linear (MISO) |
| 13 | State-Space (SISO) |
| 14 | State-Space (MISO) |
| 15 | State-Space (MIMO) |
| 16 | Transfer Function (SISO) |
| 17 | Transfer Function (MISO) |
| 18 | Transfer Function (MIMO) |
| 19 | Zero-Pole-Gain (SISO) |
| 20 | Zero-Pole-Gain (MISO) |
| 21 | Zero-Pole-Gain (MIMO) |
|  | new file path returns the path of the file from which this VI loads the system model. You can use this output to determine the path of the file that you opened using the Open a file containing system identification model dialog box. new file path returns <Not A Path> if you click the Cancel button in the dialog box. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Load Model from File VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Load System Model from File VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/lv_sysid_pal.html language=enus -->
## TOPIC 00050: System Identification VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/lv_sysid_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/lv_sysid_pal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### System Identification VIs

June 2014, 370805H-01

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the System Identification VIs to create and estimate mathematical models of dynamic systems. You can use the VIs to estimate accurate models of systems based on observed input-output data.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific System Identification error codes](../lvsysid/sysid_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SI Convert to Models of CDT | Converts a model you created with the System Identification VIs into a transfer function, zero-pole-gain, or state-space model that you can use with the LabVIEW Control Design and Simulation Module. You must manually select the polymorphic instance to use. |

| Subpalette | Description |
| --- | --- |
| Data Preprocessing VIs | Use the Data Preprocessing VIs to preprocess the raw data that you acquired from an unknown system. |
| Frequency-Domain Model Estimation VIs | Use the Frequency-Domain Model Estimation VIs to estimate the frequency response function (FRF) and to identify a transfer function (TF) or a state-space (SS) model of an unknown system. |
| Model Analysis VIs | Use the Model Analysis VIs to perform a Bode, Nyquist, or pole-zero analysis of a system model and to compute the standard deviation of the results. |
| Model Conversion VIs | Use the Model Conversion VIs to convert an AR, ARX, ARMAX, output-error, Box-Jenkins, general-linear, or state-space model into a transfer function, zero-pole-gain, or state-space model. You also can convert a continuous model to a discrete model or convert a discrete model to a continuous model. |
| Model Management VIs | Use the Model Management VIs to access information about the system model. Model information includes properties such as the system type, sampling rate, system dimensions, noise covariance, and so on. |
| Model Validation VIs | Use the Model Validation VIs to analyze and validate a system model. |
| Nonparametric Model Estimation VIs | Use the Nonparametric Model Estimation VIs to estimate the impulse response or frequency response of an unknown, linear, time-invariant system from an input and corresponding output signal. |
| Parametric Model Estimation VIs | Use the Parametric Model Estimation VIs to estimate a parametric mathematical model for an unknown, linear, time-invariant system. |
| Partially Known Model Estimation VIs | Use the Partially Known Model Estimation VIs to create and estimate partially known models for a dynamic system. |
| Recursive Model Estimation VIs | Use the Recursive Model Estimation VIs to recursively estimate the parametric mathematical model for an unknown system. |
| Utilities VIs | Use the Utilities VIs to perform miscellaneous tasks on data or the system model, including producing data samples, displaying model equations, merging models, and so on. |

© 2004–2014 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/merge_models.html language=enus -->
## TOPIC 00051: SI Merge Models VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/merge_models.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/merge_models.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Merge Models VI

**Owning Palette:** [Utilities VIs](../lvsysid/sysid_utility_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Merges multiple models of the same representation and order to one model. This VI supports only polynomial models. Wire system models to the **system model 1** and **system model 2** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### SI Merge Models (Single with Single)

[IMAGE alt='image' src='si_merge_models_(single_with_single).gif']

|  | system model 1 contains information about the first model, including the model structure, nominal or estimated parameters, identification result, and so on. |
| --- | --- |
|  | system model 2 contains information about the second model, including the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | merged system model returns information about the merged model, including the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information the merged system model contains. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Merge Models (Single with Multiple)

[IMAGE alt='image' src='si_merge_models_(single_with_multiple).gif']

|  | system model 1 contains information about the first model, including the model structure, nominal or estimated parameters, identification result, and so on. |
| --- | --- |
|  | system model 2 specifies an array of system models. Each system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | merged system model returns information about the merged model, including the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information the merged system model contains. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Merge Models (Multiple with Single)

[IMAGE alt='image' src='si_merge_models_(multiple_with_single).gif']

|  | system model 1 is an array of system models. Each system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. |
| --- | --- |
|  | system model 2 contains information about the second model, including the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | merged system model returns information about the merged model, including the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information the merged system model contains. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Merge Models (Multiple with Multiple)

[IMAGE alt='image' src='si_merge_models_(multiple_with_multiple).gif']

|  | system model 1 is an array of system models. Each system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. |
| --- | --- |
|  | system model 2 specifies an array of system models. Each system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | merged system model returns information about the merged model, including the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information the merged system model contains. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Merge Models VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Merge Models VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/model_conversion_pal.html language=enus -->
## TOPIC 00052: Model Conversion VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/model_conversion_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/model_conversion_pal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Model Conversion VIs

**Owning Palette:** [System Identification VIs](../lvsysid/lv_sysid_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Model Conversion VIs to convert an [AR](../lvsysidconcepts/modeldefinitionsar.html), [ARX](../lvsysidconcepts/modeldefinitionsarx.html), [ARMAX](../lvsysidconcepts/modeldefinitionsarmax.html), [output-error](../lvsysidconcepts/modeldefinitionsoe.html), [Box-Jenkins](../lvsysidconcepts/modeldefinitionsbj.html), [general-linear](../lvsysidconcepts/modeldefinitionsgl.html), or [state-space](../lvsysidconcepts/modeldefinitionsss.html) model into a [transfer function](../lvsysidconcepts/modeldefinitionstf.html), [zero-pole-gain](../lvsysidconcepts/modeldefinitionszpg.html), or [state-space](../lvsysidconcepts/modeldefinitionsss.html) model. You also can convert a continuous model to a discrete model or convert a discrete model to a continuous model.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific System Identification error codes](../lvsysid/sysid_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SI Convert Continuous to Discrete Model | Converts a continuous model to a discrete model using the sampling rate you specify. You can use this VI to convert continuous transfer function, state-space, and zero-pole-gain models to discrete transfer function, state-space, and zero-pole-gain models, respectively. |
| SI Convert Discrete to Continuous Model | Converts a discrete model to a continuous model. You can use this VI to convert discrete transfer function, state-space, and zero-pole-gain models to continuous transfer function, state-space, and zero-pole-gain models, respectively. |
| SI Model Conversion | Converts a model into another type of model that you can use with the System Identification VIs. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/nyquist_plot.html language=enus -->
## TOPIC 00053: SI Nyquist Plot VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/nyquist_plot.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/nyquist_plot.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Nyquist Plot VI

**Owning Palette:** [Model Analysis VIs](../lvsysid/model_presentation_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Produces the Nyquist plot of a system model on an XY graph.

This VI computes the transfer function and frequency response function (FRF) for one input-output pair of a system model. This VI then presents the FRF as a real part versus imaginary part, or Nyquist plot. Use the [SI Nyquist Plot Indicator](../lvsysid/si_nyquist_indicator.html) to display the Nyquist plot on the front panel window.

[Examples](#examples)

[IMAGE alt='image' src='si_nyquist_plotc.gif']

|  | freq info specifies the frequency information for the data plot. start frequency specifies the start frequency of the data plot. The value of start frequency must be in a normalized frequency range of 0–0.5 times the real sampling rate. end frequency specifies the end frequency of the data plot. The value of end frequency must be in a normalized frequency range of 0–0.5 times the real sampling rate and greater than the value of start frequency. num of freq bins specifies the number of frequency bins between start frequency and end frequency for the data plot. interval type determines how the frequency points of the FRF increase from start frequency to end frequency. For a logarithmic interval type, the frequency points are the following: f0, f0*df, f0*(df)2, f0*(df)3, ..., fFinal where f0 = start frequency fFinal = end frequency df = (log10(end frequency) – log10(start frequency)) / (num of freq bins – 1) For a linear interval type, the frequency points are the following: f0, f0+df, f0+2df, f0+3df, ..., fFinal wheref0 = start frequency fFinal = end frequency df = (end frequency – start frequency) / (num of freq bins – 1) 0logarithmic (default)1linear |
| --- | --- |
|  | start frequency specifies the start frequency of the data plot. The value of start frequency must be in a normalized frequency range of 0–0.5 times the real sampling rate. |
|  | end frequency specifies the end frequency of the data plot. The value of end frequency must be in a normalized frequency range of 0–0.5 times the real sampling rate and greater than the value of start frequency. |
|  | num of freq bins specifies the number of frequency bins between start frequency and end frequency for the data plot. |
|  | interval type determines how the frequency points of the FRF increase from start frequency to end frequency. For a logarithmic interval type, the frequency points are the following: f0, f0*df, f0*(df)2, f0*(df)3, ..., fFinal where f0 = start frequency fFinal = end frequency df = (log10(end frequency) – log10(start frequency)) / (num of freq bins – 1) For a linear interval type, the frequency points are the following: f0, f0+df, f0+2df, f0+3df, ..., fFinal wheref0 = start frequency fFinal = end frequency df = (end frequency – start frequency) / (num of freq bins – 1) 0logarithmic (default)1linear |
| where | f0 = start frequency |
|  | fFinal = end frequency |
|  | df = (log10(end frequency) – log10(start frequency)) / (num of freq bins – 1) |
| where | f0 = start frequency |
|  | fFinal = end frequency |
|  | df = (end frequency – start frequency) / (num of freq bins – 1) |
| 0 | logarithmic (default) |
| 1 | linear |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | channel selects the signal pair with which to compute the transfer function. type specifies whether to compute the transfer function between a stimulus signal and a response signal or the transfer function between a noise signal and a response signal. 0stimulus (default)—Computes the transfer function between a stimulus signal and a response signal. Use input index and output index to select the stimulus and response signals to use.1noise—Computes the transfer function between a noise signal and a response signal. Use input index and output index to select the noise and response signals to use. input index specifies the index of the system input channel with which to compute the transfer function. input index applies only for MISO or MIMO system models. output index specifies the index of the system output channel with which to compute the transfer function. output index applies only for MIMO system models. |
|  | type specifies whether to compute the transfer function between a stimulus signal and a response signal or the transfer function between a noise signal and a response signal. 0stimulus (default)—Computes the transfer function between a stimulus signal and a response signal. Use input index and output index to select the stimulus and response signals to use.1noise—Computes the transfer function between a noise signal and a response signal. Use input index and output index to select the noise and response signals to use. |
| 0 | stimulus (default)—Computes the transfer function between a stimulus signal and a response signal. Use input index and output index to select the stimulus and response signals to use. |
| 1 | noise—Computes the transfer function between a noise signal and a response signal. Use input index and output index to select the noise and response signals to use. |
|  | input index specifies the index of the system input channel with which to compute the transfer function. input index applies only for MISO or MIMO system models. |
|  | output index specifies the index of the system output channel with which to compute the transfer function. output index applies only for MIMO system models. |
|  | confidence level (%) specifies the percentage confidence interval for the FRF. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | show confidence range? specifies whether to show the confidence range of the plot data. The default is TRUE. |
|  | Nyquist plot returns the Nyquist plot of the input signal. Nyquist plot returns the imaginary part of the complex frequency response of the input system plotted against its real part. Use the SI Nyquist Plot Indicator to display the Nyquist plot. real returns the real part of the frequency response of the system. imaginary returns the imaginary part of the frequency response of the system. |
|  | real returns the real part of the frequency response of the system. |
|  | imaginary returns the imaginary part of the frequency response of the system. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the SI Nyquist Plot VI:

- Model Presentation VI: labview\examples\System Identification\Getting Started\General.llb
- Flexible Arm VI: labview\examples\System Identification\Industry Applications\Mechanical Systems.llb

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/parametric_estimation_pal.html language=enus -->
## TOPIC 00054: Parametric Model Estimation VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/parametric_estimation_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/parametric_estimation_pal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Parametric Model Estimation VIs

**Owning Palette:** [System Identification VIs](../lvsysid/lv_sysid_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Parametric Model Estimation VIs to estimate a parametric mathematical model for an unknown, linear, time-invariant system.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific System Identification error codes](../lvsysid/sysid_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SI Estimate AR Model | Estimates the parameters of an AR model for an unknown system. Wire data to the response signal input to determine the polymorphic instance to use or manually select the instance. |
| SI Estimate ARMAX Model | Estimates the parameters of an ARMAX model for an unknown system. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Estimate ARX Model | Estimates the parameters of an ARX model for an unknown system. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Estimate BJ Model | Estimates the parameters of a Box-Jenkins (BJ) model for an unknown system. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Estimate General Linear Model | Estimates the parameters of a general-linear (GL) model for an unknown system. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Estimate OE Model | Estimates the parameters of an output-error (OE) model for an unknown system. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Estimate Orders of System Model | Searches the model of an unknown system for the optimal orders and delay. |
| SI Estimate State-Space Model | Estimates the parameters of a state-space model for an unknown system. You must manually select the polymorphic instance to use. |
| SI Estimate Transfer Function Model | Estimates the parameters of a continuous or discrete transfer function model for an unknown system. This VI estimates only the transfer function between the stimulus and the response. The transfer function between the noise and the response is assumed to be 1. You must manually select the polymorphic instance to use. |
| SI Estimate User-Defined Model | Estimates a user-defined model. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Model Estimation | Estimates the mathematical model for an unknown system. |
| SI Transfer Function Estimation | Estimates a discrete or continuous transfer function model for a SISO unknown system. For discrete models, this VI supports the direct, indirect, and joint input-output identification methods. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/pk_mdl_est_pal.html language=enus -->
## TOPIC 00055: Partially Known Model Estimation VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/pk_mdl_est_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/pk_mdl_est_pal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Partially Known Model Estimation VIs

**Owning Palette:** [System Identification VIs](../lvsysid/lv_sysid_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Partially Known Model Estimation VIs to create and estimate partially known models for a dynamic system.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific System Identification error codes](../lvsysid/sysid_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SI Create Partially Known Continuous Transfer Function Model | Creates a continuous transfer function model for a partially known system. Use the SI Estimate Partially Known Continuous Transfer Function Model VI to estimate the model you create with this VI. You must manually select the polymorphic instance to use. |
| SI Create Partially Known State-Space Model | Creates a state-space model for a partially known system. Use the SI Estimate Partially Known State-Space Model VI to estimate the model you create with this VI. You must manually select the polymorphic instance to use. |
| SI Estimate Partially Known Continuous Transfer Function Model | Estimates a continuous transfer function model for a partially known system. Use the SI Create Partially Known Continuous Transfer Function Model VI to create the model you want to estimate. You must manually select the polymorphic instance to use. |
| SI Estimate Partially Known State-Space Model | Estimates a state-space model for a partially known system. Use the SI Create Partially Known State-Space Model VI to create the model you want to estimate. Wire data to the stimulus signal and response signal inputs to determine the polymorphic instance to use or manually select the instance. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/read_from_file.html language=enus -->
## TOPIC 00056: SI Read from File VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/read_from_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/read_from_file.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Read from File VI

**Owning Palette:** [Utilities VIs](../lvsysid/sysid_utility_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Reads arrays or waveforms from a specified data file. Use this VI to read spreadsheet text files and waveforms data files.

[Example](#examples)

[IMAGE alt='image' src='si_read_from_file.gif']

|  | file path (dialog if empty) specifies the path to the file from which this VI reads data. |
| --- | --- |
|  | file type specifies the type of the source data file. You can specify a Spreadsheet Text File or a Waveforms Data File. |
|  | sampling rate (Hz) specifies the sampling frequency in hertz. The value of sampling rate must be greater than 0. sampling rate is ignored if the file type is a waveforms data file. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | first channel returns the data from the first waveform in the record if the file type is Waveforms Data File. If the file type is Spreadsheet Text File, this VI converts the data array to a waveform based on the sampling rate you provide. |
|  | all channels returns the data from all waveforms in the record if the file type is Waveforms Data File. If only one waveform exists in the record, this output is identical to the first channel output. If the file type is Spreadsheet Text File, this VI converts the data array to an array of waveforms based on the sampling rate you provide. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Read Data from File VI in the labview\examples\System Identification\Getting Started\General.llb for an example of using the SI Read from File VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/rebld_missng_data.html language=enus -->
## TOPIC 00057: SI Rebuild Missing Data VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/rebld_missng_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/rebld_missng_data.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Rebuild Missing Data VI

**Owning Palette:** [Data Preprocessing VIs](../lvsysid/data_preprocess_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Rebuilds corrupted or missing parts of stimulus and response signals. Wire data to the **stimulus signal in** and **response signal in** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### SI Rebuild Missing Data (SISO Waveform)

[IMAGE alt='image' src='si_rebuild_missing_data_(siso_waveform)c.gif']

|  | stimulus signal in specifies the input waveform of the stimulus signal. |
| --- | --- |
|  | response signal in specifies the input waveform of the response signal. |
|  | indexes to rebuild specifies the index of the stimulus signal and the index of the response signal. This VI rebuilds the stimulus signal and response signal values at these indexes. stimulus specifies the index of the stimulus signal to rebuild. response specifies the index of the response signal to rebuild. |
|  | stimulus specifies the index of the stimulus signal to rebuild. |
|  | response specifies the index of the response signal to rebuild. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | stimulus signal out returns the waveform of the rebuilt stimulus signal. |
|  | response signal out returns the waveform of the rebuilt response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Rebuild Missing Data (SISO Array)

[IMAGE alt='image' src='si_rebuild_missing_data_(siso_array)c.gif']

|  | stimulus signal in specifies an array that represents the stimulus signal. |
| --- | --- |
|  | response signal in specifies an array that represents the response signal. |
|  | indexes to rebuild specifies the index of the stimulus signal and the index of the response signal. This VI rebuilds the stimulus signal and response signal values at these indexes. stimulus specifies the index of the stimulus signal to rebuild. response specifies the index of the response signal to rebuild. |
|  | stimulus specifies the index of the stimulus signal to rebuild. |
|  | response specifies the index of the response signal to rebuild. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | stimulus signal out returns the array of the rebuilt stimulus signal. |
|  | response signal out returns the array of the rebuilt response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Rebuild Missing Data (MISO Waveform)

[IMAGE alt='image' src='si_rebuild_missing_data_(miso_waveform)c.gif']

|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
| --- | --- |
|  | response signal in specifies the input waveform of the response signal. |
|  | indexes to rebuild specifies the indexes of the stimulus signals and the index of the response signal to rebuild. stimulus specifies the indexes of the stimulus signals to rebuild. response specifies the index of the response signal to rebuild. |
|  | stimulus specifies the indexes of the stimulus signals to rebuild. |
|  | response specifies the index of the response signal to rebuild. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | stimulus signals out returns the waveform array of the rebuilt stimulus signals. |
|  | response signal out returns the waveform of the rebuilt response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Rebuild Missing Data (MISO Array)

[IMAGE alt='image' src='si_rebuild_missing_data_(miso_array)c.gif']

|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
| --- | --- |
|  | response signal in specifies an array that represents the response signal. |
|  | indexes to rebuild specifies the indexes of the stimulus signals and the index of the response signal to rebuild. stimulus specifies the indexes of the stimulus signals to rebuild. response specifies the index of the response signal to rebuild. |
|  | stimulus specifies the indexes of the stimulus signals to rebuild. |
|  | response specifies the index of the response signal to rebuild. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | stimulus signals out returns the array of the rebuilt stimulus signals. |
|  | response signal out returns the array of the rebuilt response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Rebuild Missing Data (MIMO Waveform)

[IMAGE alt='image' src='si_rebuild_missing_data_(mimo_waveform)c.gif']

|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
| --- | --- |
|  | response signals in specifies the input waveform array of the response signals. Each element of the waveform array is the waveform of one response signal. |
|  | indexes to rebuild specifies the indexes of the stimulus signals and the indexes of the response signals to rebuild. stimulus specifies the indexes of the stimulus signals to rebuild. response specifies the indexes of the response signals to rebuild. |
|  | stimulus specifies the indexes of the stimulus signals to rebuild. |
|  | response specifies the indexes of the response signals to rebuild. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | stimulus signals out returns the waveform array of the rebuilt stimulus signals. |
|  | response signals out returns the waveform array of the rebuilt response signals. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Rebuild Missing Data (MIMO Array)

[IMAGE alt='image' src='si_rebuild_missing_data_(mimo_array)c.gif']

|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
| --- | --- |
|  | response signals in specifies an array that represents the response signals. Each row in the array is one response signal. |
|  | indexes to rebuild specifies the indexes of the stimulus signals and the indexes of the response signals to rebuild. stimulus specifies the indexes of the stimulus signals to rebuild. response specifies the indexes of the response signals to rebuild. |
|  | stimulus specifies the indexes of the stimulus signals to rebuild. |
|  | response specifies the indexes of the response signals to rebuild. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | stimulus signals out returns the array of the rebuilt stimulus signals. |
|  | response signals out returns the array of the rebuilt response signals. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/rec_est_armax_model.html language=enus -->
## TOPIC 00058: SI Recursively Estimate ARMAX Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/rec_est_armax_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/rec_est_armax_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Recursively Estimate ARMAX Model VI

**Owning Palette:** [Recursive Model Estimation VIs](../lvsysid/recursive_model_est_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Estimates the parameters of an [ARMAX](../lvsysidconcepts/modeldefinitionsarmax.html) model using a recursive method. Wire data to the **stimulus signal** and **response signal** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### SI Recursively Estimate ARMAX Model (SISO Waveform)

[IMAGE alt='image' src='si_recursively_estimate_armax_model_(siso_array)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signal specifies the input waveform of the stimulus signal. |
|  | response signal specifies the input waveform of the response signal. |
|  | orders of ARMAX model specifies the orders and delay of the ARMAX model. A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. |
|  | B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. |
|  | C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. |
|  | delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of ARMAX model returns the coefficients of the ARMAX model. A returns the A coefficients of the system model. B returns the B coefficients of the system model. C returns the C coefficients of the system model. |
|  | A returns the A coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | C returns the C coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Recursively Estimate ARMAX Model (SISO Array)

[IMAGE alt='image' src='si_recursively_estimate_armax_model_(siso_waveform)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signal specifies an array that represents the stimulus signal. |
|  | response signal specifies an array that represents the response signal. |
|  | orders of ARMAX model specifies the orders and delay of the ARMAX model. A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. |
|  | B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. |
|  | C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. |
|  | delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sampling rate (Hz) is the signal sampling rate in hertz. The value of sampling rate must be greater than 0. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of ARMAX model returns the coefficients of the ARMAX model. A returns the A coefficients of the system model. B returns the B coefficients of the system model. C returns the C coefficients of the system model. |
|  | A returns the A coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | C returns the C coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Online Model Estimation VI in the labview\examples\System Identification\Getting Started\Recursive Estimation.llb for an example of using the SI Recursively Estimate ARMAX Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/rec_est_arx_model.html language=enus -->
## TOPIC 00059: SI Recursively Estimate ARX Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/rec_est_arx_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/rec_est_arx_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Recursively Estimate ARX Model VI

**Owning Palette:** [Recursive Model Estimation VIs](../lvsysid/recursive_model_est_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Estimates the parameters of an [ARX](../lvsysidconcepts/modeldefinitionsarx.html) model using a recursive method. Wire data to the **stimulus signal** and **response signal** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### SI Recursively Estimate ARX Model (SISO Waveform)

[IMAGE alt='image' src='si_recursively_estimate_arx_model_(siso_waveform)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signal specifies the input waveform of the stimulus signal. |
|  | response signal specifies the input waveform of the response signal. |
|  | orders of ARX model specifies the orders and delay of the ARX model. A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. |
|  | B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. |
|  | delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of ARX model returns the coefficients of the ARX model. A returns the A coefficients of the system model. B returns the B coefficients of the system model. |
|  | A returns the A coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Recursively Estimate ARX Model (SISO Array)

[IMAGE alt='image' src='si_recursively_estimate_arx_model_(siso_array)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signal specifies an array that represents the stimulus signal. |
|  | response signal specifies an array that represents the response signal. |
|  | orders of ARX model specifies the orders and delay of the ARX model. A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. |
|  | B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. |
|  | delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sampling rate (Hz) is the signal sampling rate in hertz. The value of sampling rate must be greater than 0. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of ARX model returns the coefficients of the ARX model. A returns the A coefficients of the system model. B returns the B coefficients of the system model. |
|  | A returns the A coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Recursively Estimate ARX Model (MISO Waveform)

[IMAGE alt='image' src='si_recursively_estimate_arx_model_(miso_waveform)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signals specifies the input waveform array of the stimulus signals. Each element of the array is the waveform of one stimulus signal. |
|  | response signal specifies the input waveform of the response signal. |
|  | orders of ARX model specifies the orders and delays of the ARX model. A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. B orders specifies the orders of the B coefficients of the model. The value of B orders must be greater than or equal to 1. delays specifies the delays k of the model. The value of delays should be greater than 0. |
|  | A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. |
|  | B orders specifies the orders of the B coefficients of the model. The value of B orders must be greater than or equal to 1. |
|  | delays specifies the delays k of the model. The value of delays should be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of ARX model returns the coefficients of the ARX model. A returns the A coefficients of the system model. B returns the B coefficients of the system model. |
|  | A returns the A coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Recursively Estimate ARX Model (MISO Array)

[IMAGE alt='image' src='si_recursively_estimate_arx_model_(miso_array)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signals specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
|  | response signal specifies an array that represents the response signal. Each row in the array is one response signal. |
|  | orders of ARX model specifies the orders and delays of the ARX model. A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. B orders specifies the orders of the B coefficients of the model. The value of B orders must be greater than or equal to 1. delays specifies the delays k of the model. The value of delays should be greater than 0. |
|  | A order specifies the order of the A coefficients of the system model. The value of A order must be greater than or equal to 0. |
|  | B orders specifies the orders of the B coefficients of the model. The value of B orders must be greater than or equal to 1. |
|  | delays specifies the delays k of the model. The value of delays should be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sampling rate (Hz) is the signal sampling rate in hertz. The value of sampling rate must be greater than 0. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of ARX model returns the coefficients of the ARX model. A returns the A coefficients of the system model. B returns the B coefficients of the system model. |
|  | A returns the A coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Online Model Estimation VI in the labview\examples\System Identification\Getting Started\Recursive Estimation.llb for an example of using the SI Recursively Estimate ARX Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/rec_est_bj_model.html language=enus -->
## TOPIC 00060: SI Recursively Estimate BJ Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/rec_est_bj_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/rec_est_bj_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Recursively Estimate BJ Model VI

**Owning Palette:** [Recursive Model Estimation VIs](../lvsysid/recursive_model_est_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Estimates the parameters of a [Box-Jenkins (BJ)](../lvsysidconcepts/modeldefinitionsbj.html) model using a recursive method. Wire data to the **stimulus signal** and **response signal** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### SI Recursively Estimate BJ Model (SISO Waveform)

[IMAGE alt='image' src='si_recursively_estimate_bj_model_(siso_waveform)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signal specifies the input waveform of the stimulus signal. |
|  | response signal specifies the input waveform of the response signal. |
|  | orders of BJ model specifies the orders and delay of the Box-Jenkins (BJ) model. B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. F order specifies the order of the F coefficients of the system model. The value of F order must be greater than or equal to 0. C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. D order specifies the order of the D coefficients of the model. The value of D order must be greater than or equal to 0. delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. |
|  | F order specifies the order of the F coefficients of the system model. The value of F order must be greater than or equal to 0. |
|  | C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. |
|  | D order specifies the order of the D coefficients of the model. The value of D order must be greater than or equal to 0. |
|  | delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of BJ model returns the coefficients of the Box-Jenkins (BJ) model. B returns the B coefficients of the system model. F returns the F coefficients of the system model. C returns the C coefficients of the system model. D returns the D coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | F returns the F coefficients of the system model. |
|  | C returns the C coefficients of the system model. |
|  | D returns the D coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Recursively Estimate BJ Model (SISO Array)

[IMAGE alt='image' src='si_recursively_estimate_bj_model_(siso_array)c.gif']

|  | initialize specifies whether to initialize the internal state of the VI. This VI performs calculations that are dependent on all previous data since you last ran the VI or since you set initialize to TRUE. When initialize is TRUE, this VI restarts the calculation dependency. The default is FALSE. |
| --- | --- |
|  | recursive method specifies the recursive estimation method to use. 0RLS (default)—Recursive least squares method1KF—Kalman filter method2NLMS—Normalized least mean squares method3LMS—Least mean squares method |
| 0 | RLS (default)—Recursive least squares method |
| 1 | KF—Kalman filter method |
| 2 | NLMS—Normalized least mean squares method |
| 3 | LMS—Least mean squares method |
|  | stimulus signal specifies an array that represents the stimulus signal. |
|  | response signal specifies an array that represents the response signal. |
|  | orders of BJ model specifies the orders and delay of the Box-Jenkins (BJ) model. B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. F order specifies the order of the F coefficients of the system model. The value of F order must be greater than or equal to 0. C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. D order specifies the order of the D coefficients of the model. The value of D order must be greater than or equal to 0. delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | B order specifies the order of the B coefficients of the system model. The value of B order must be greater than or equal to 1. |
|  | F order specifies the order of the F coefficients of the system model. The value of F order must be greater than or equal to 0. |
|  | C order specifies the order of the C coefficients of the system model. The value of C order must be greater than or equal to 0. |
|  | D order specifies the order of the D coefficients of the model. The value of D order must be greater than or equal to 0. |
|  | delay specifies the delay k of the system model. The value of delay must be greater than or equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sampling rate (Hz) is the signal sampling rate in hertz. The value of sampling rate must be greater than 0. |
|  | ref value specifies the reference value for the recursive estimation algorithms. When recursive method is KF, ref value is the drift matrix. This method uses the drift matrix to prevent the gradient from approaching zero in the identification process. The gradient indicates the changes of the model coefficients. When recursive method is RLS, this VI uses the value in the first row and the first column of ref value as the forgetting factor. The forgetting factor specifies the percentage of information this VI uses from previous estimation calculations. The range of the forgetting factor is between 0 and 1. For example, if you set the forgetting factor to 0.5, this VI uses 50% of information from previous estimation. If you want to estimate a time-invariant system, you can set the forgetting factor between 0.98 and less than 1. If you want to estimate a time-variant system, you can set a smaller forgetting factor. Then, this VI can have a better ability to track the changes of the system coefficients. When recursive method is NLMS or LMS, this VI uses the value in the first row and the first column of ref value as the step size. The value of the step size is proportional to the convergence rate. The larger the step size, the faster the convergence. However, the algorithm can become unstable if the step size gets too large. An appropriate step size depends on the model type, order, and input signal. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model out contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | predicted response returns the predicted response output from the current estimated system model. The difference between the values of predicted response and response signal is the measure of the recursive estimation. |
|  | coefficients of BJ model returns the coefficients of the Box-Jenkins (BJ) model. B returns the B coefficients of the system model. F returns the F coefficients of the system model. C returns the C coefficients of the system model. D returns the D coefficients of the system model. |
|  | B returns the B coefficients of the system model. |
|  | F returns the F coefficients of the system model. |
|  | C returns the C coefficients of the system model. |
|  | D returns the D coefficients of the system model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Online Model Estimation VI in the labview\examples\System Identification\Getting Started\Recursive Estimation.llb for an example of using the SI Recursively Estimate BJ Model VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/set_coeff_system_model.html language=enus -->
## TOPIC 00061: SI Set Coefficients to System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/set_coeff_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/set_coeff_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Set Coefficients to System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Applies coefficients and the standard deviation and covariance of the coefficients to **system model**. Use the [SI Get Coefficients to System Model](../lvsysid/get_coeff_from_sys_model.html) VI to return the coefficients and the standard deviation and covariance of the coefficients of **system model**. You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance to use.

#### SI Set Coefficients to AR Model

[IMAGE alt='image' src='si_set_coefficients_to_ar_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients specifies the coefficients in the AR model. |
|  | std deviations specifies the standard deviations of the coefficients. Each value in std deviations is the standard deviation of the corresponding coefficient in coefficients. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ARX Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_arx_model_(siso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of ARX model specifies the coefficients of the ARX model. A specifies the A coefficients of the system model. B specifies the B coefficients of the system model. |
|  | A specifies the A coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of ARX model. A std dev specifies the standard deviations of the A coefficients of the system model. B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | A std dev specifies the standard deviations of the A coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ARX Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_arx_model_(miso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of ARX model specifies the coefficients of the ARX model. A specifies the A coefficients of the system model. B specifies the B coefficients of the system model. |
|  | A specifies the A coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of ARX model. A std dev specifies the standard deviations of the A coefficients of the system model. B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | A std dev specifies the standard deviations of the A coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ARX Model (MIMO)

[IMAGE alt='image' src='si_set_coefficients_to_arx_model_(mimo)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of ARX model specifies the coefficients of the ARX model. A specifies the A coefficients of the system model. B specifies the B coefficients of the system model. |
|  | A specifies the A coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of ARX model. A std dev specifies the standard deviation of the A coefficients of the system model. B std dev specifies the standard deviation of the B coefficients of the system model. |
|  | A std dev specifies the standard deviation of the A coefficients of the system model. |
|  | B std dev specifies the standard deviation of the B coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ARMAX Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_armax_model_(siso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of ARMAX model specifies the coefficients of the ARMAX model. A specifies the A coefficients of the system model. B specifies the B coefficients of the system model. C specifies the C coefficients of the system model. |
|  | A specifies the A coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | C specifies the C coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of ARMAX model. A std dev specifies the standard deviations of the A coefficients of the system model. B std dev specifies the standard deviations of the B coefficients of the system model. C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | A std dev specifies the standard deviations of the A coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ARMAX Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_armax_model_(miso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of ARMAX model specifies the coefficients of the ARMAX model. A specifies the A coefficients of the system model. B specifies the B coefficients of the system model. C specifies the C coefficients of the system model. |
|  | A specifies the A coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | C specifies the C coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of ARMAX model. A std dev specifies the standard deviations of the A coefficients of the system model. B std dev specifies the standard deviations of the B coefficients of the system model. C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | A std dev specifies the standard deviations of the A coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to OE Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_oe_model_(siso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of OE model specifies the coefficients of the output-error (OE) model. B specifies the B coefficients of the system model. F specifies the F coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | F specifies the F coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of OE model. B std dev specifies the standard deviations of the B coefficients of the system model. F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to OE Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_oe_model_(miso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of OE model specifies the coefficients of the output-error (OE) model. B specifies the B coefficients of the system model. F specifies the F coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | F specifies the F coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of OE model. B std dev specifies the standard deviations of the B coefficients of the system model. F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to BJ Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_bj_model_(siso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of BJ model specifies the coefficients of the Box-Jenkins (BJ) model. B specifies the B coefficients of the system model. F specifies the F coefficients of the system model. C specifies the C coefficients of the system model. D specifies the D coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | F specifies the F coefficients of the system model. |
|  | C specifies the C coefficients of the system model. |
|  | D specifies the D coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of BJ model. B std dev specifies the standard deviations of the B coefficients of the system model. F std dev specifies the standard deviations of the F coefficients of the system model. C std dev specifies the standard deviations of the C coefficients of the system model. D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to BJ Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_bj_model_(miso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of BJ model specifies the coefficients of the Box-Jenkins (BJ) model. B specifies the B coefficients of the system model. F specifies the F coefficients of the system model. C specifies the C coefficients of the system model. D specifies the D coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | F specifies the F coefficients of the system model. |
|  | C specifies the C coefficients of the system model. |
|  | D specifies the D coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of BJ model. B std dev specifies the standard deviations of the B coefficients of the system model. F std dev specifies the standard deviations of the F coefficients of the system model. C std dev specifies the standard deviations of the C coefficients of the system model. D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to GL Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_gl_model_(siso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of GL model specifies the coefficients of the general-linear (GL) model. A specifies the A coefficients of the system model. B specifies the B coefficients of the system model. F specifies the F coefficients of the system model. C specifies the C coefficients of the system model. D specifies the D coefficients of the system model. |
|  | A specifies the A coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | F specifies the F coefficients of the system model. |
|  | C specifies the C coefficients of the system model. |
|  | D specifies the D coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of GL model. A std dev specifies the standard deviations of the A coefficients of the system model. B std dev specifies the standard deviations of the B coefficients of the system model. F std dev specifies the standard deviations of the F coefficients of the system model. C std dev specifies the standard deviations of the C coefficients of the system model. D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | A std dev specifies the standard deviations of the A coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to GL Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_gl_model_(miso)c.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of GL model specifies the coefficients of the general-linear (GL) model. A specifies the A coefficients of the system model. B specifies the B coefficients of the system model. F specifies the F coefficients of the system model. C specifies the C coefficients of the system model. D specifies the D coefficients of the system model. |
|  | A specifies the A coefficients of the system model. |
|  | B specifies the B coefficients of the system model. |
|  | F specifies the F coefficients of the system model. |
|  | C specifies the C coefficients of the system model. |
|  | D specifies the D coefficients of the system model. |
|  | std deviations specifies the standard deviations of coefficients of GL model. A std dev specifies the standard deviations of the A coefficients of the system model. B std dev specifies the standard deviations of the B coefficients of the system model. F std dev specifies the standard deviations of the F coefficients of the system model. C std dev specifies the standard deviations of the C coefficients of the system model. D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | A std dev specifies the standard deviations of the A coefficients of the system model. |
|  | B std dev specifies the standard deviations of the B coefficients of the system model. |
|  | F std dev specifies the standard deviations of the F coefficients of the system model. |
|  | C std dev specifies the standard deviations of the C coefficients of the system model. |
|  | D std dev specifies the standard deviations of the D coefficients of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | covariance specifies the covariance of the values of the system model coefficients. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to SS Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_ss_model_(siso).gif']

|  | Kalman gain specifies the Kalman gain of the state-space (SS) model. |
| --- | --- |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of state-space model specifies the coefficients of the state-space model. A specifies the state matrix of the system model. B specifies the input matrix of the system model. C specifies the output matrix of the system model. D specifies the direct transmission matrix of the system model. |
|  | A specifies the state matrix of the system model. |
|  | B specifies the input matrix of the system model. |
|  | C specifies the output matrix of the system model. |
|  | D specifies the direct transmission matrix of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | initial states specifies the initial states of the state-space (SS) model. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to SS Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_ss_model_(miso).gif']

|  | Kalman gain specifies the Kalman gain of the state-space (SS) model. |
| --- | --- |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of state-space model specifies the coefficients of the state-space model. A specifies the state matrix of the system model. B specifies the input matrix of the system model. C specifies the output matrix of the system model. D specifies the direct transmission matrix of the system model. |
|  | A specifies the state matrix of the system model. |
|  | B specifies the input matrix of the system model. |
|  | C specifies the output matrix of the system model. |
|  | D specifies the direct transmission matrix of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | initial states specifies the initial states of the state-space (SS) model. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to SS Model (MIMO)

[IMAGE alt='image' src='si_set_coefficients_to_ss_model_(mimo).gif']

|  | Kalman gain specifies the Kalman gain of the state-space (SS) model. |
| --- | --- |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of state-space model specifies the coefficients of the state-space model. A specifies the state matrix of the system model. B specifies the input matrix of the system model. C specifies the output matrix of the system model. D specifies the direct transmission matrix of the system model. |
|  | A specifies the state matrix of the system model. |
|  | B specifies the input matrix of the system model. |
|  | C specifies the output matrix of the system model. |
|  | D specifies the direct transmission matrix of the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | initial states specifies the initial states of the state-space (SS) model. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to TF Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_tf_model_(siso)c.gif']

|  | input type specifies whether to set the coefficients for the transfer function between the stimulus and the response of the system model or for the transfer function between the noise and the response of the system model. 0stimulus (default)—Sets the coefficients for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function.1noise—Sets the coefficients for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
| --- | --- |
| 0 | stimulus (default)—Sets the coefficients for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function. |
| 1 | noise—Sets the coefficients for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of transfer function model specifies the coefficients of the transfer function (TF) model. numerator specifies the numerator coefficients of the stimulus or noise transfer function. denominator specifies the denominator coefficients of the stimulus or noise transfer function. |
|  | numerator specifies the numerator coefficients of the stimulus or noise transfer function. |
|  | denominator specifies the denominator coefficients of the stimulus or noise transfer function. |
|  | std deviations specifies the standard deviations of coefficients of transfer function model. numerator std dev specifies the standard deviation of the numerator coefficients of the transfer function model. denominator std dev specifies the standard deviation of the denominator coefficients of the transfer function model. |
|  | numerator std dev specifies the standard deviation of the numerator coefficients of the transfer function model. |
|  | denominator std dev specifies the standard deviation of the denominator coefficients of the transfer function model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to TF Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_tf_model_(miso)c.gif']

|  | input type specifies whether to set the coefficients for the transfer function between the stimulus and the response of the system model or for the transfer function between the noise and the response of the system model. 0stimulus (default)—Sets the coefficients for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function.1noise—Sets the coefficients for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
| --- | --- |
| 0 | stimulus (default)—Sets the coefficients for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function. |
| 1 | noise—Sets the coefficients for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of transfer function model specifies the coefficients of the transfer function (TF) model. numerator specifies the numerator coefficients of the stimulus or noise transfer function. denominator specifies the denominator coefficients of the stimulus or noise transfer function. |
|  | numerator specifies the numerator coefficients of the stimulus or noise transfer function. |
|  | denominator specifies the denominator coefficients of the stimulus or noise transfer function. |
|  | std deviations specifies the standard deviations of coefficients of transfer function model. numerator std dev specifies the standard deviation of the numerator coefficients of the transfer function model. denominator std dev specifies the standard deviation of the denominator coefficients of the transfer function model. |
|  | numerator std dev specifies the standard deviation of the numerator coefficients of the transfer function model. |
|  | denominator std dev specifies the standard deviation of the denominator coefficients of the transfer function model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to TF Model (MIMO)

[IMAGE alt='image' src='si_set_coefficients_to_tf_model_(mimo)c.gif']

|  | input type specifies whether to set the coefficients for the transfer function between the stimulus and the response of the system model or for the transfer function between the noise and the response of the system model. 0stimulus (default)—Sets the coefficients for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function.1noise—Sets the coefficients for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
| --- | --- |
| 0 | stimulus (default)—Sets the coefficients for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function. |
| 1 | noise—Sets the coefficients for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of transfer function model specifies the coefficients of the transfer function (TF) model. numerator specifies the numerator coefficients of the stimulus or noise transfer function. denominator specifies the denominator coefficients of the stimulus or noise transfer function. |
|  | numerator specifies the numerator coefficients of the stimulus or noise transfer function. |
|  | denominator specifies the denominator coefficients of the stimulus or noise transfer function. |
|  | std deviations specifies the standard deviations of coefficients of transfer function model. numerator std dev specifies the standard deviation of the numerator coefficients of the transfer function model. denominator std dev specifies the standard deviation of the denominator coefficients of the transfer function model. |
|  | numerator std dev specifies the standard deviation of the numerator coefficients of the transfer function model. |
|  | denominator std dev specifies the standard deviation of the denominator coefficients of the transfer function model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ZPK Model (SISO)

[IMAGE alt='image' src='si_set_coefficients_to_zpk_model_(siso).gif']

|  | input type specifies whether to set the poles and zeros for the transfer function between the stimulus and the response of the system model or for the transfer function between the noise and the response of the system model. 0stimulus (default)—Sets the poles and zeros for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function.1noise—Sets the poles and zeros for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
| --- | --- |
| 0 | stimulus (default)—Sets the poles and zeros for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function. |
| 1 | noise—Sets the poles and zeros for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of zero-pole-gain model specifies the coefficients and gain of the zero-pole-gain (ZPK) model. zeros specifies the zeros of the zero-pole-gain model. poles specifies the poles of the zero-pole-gain model. gain specifies the gain of the zero-pole-gain model. |
|  | zeros specifies the zeros of the zero-pole-gain model. |
|  | poles specifies the poles of the zero-pole-gain model. |
|  | gain specifies the gain of the zero-pole-gain model. |
|  | std deviations specifies the standard deviations of coefficients of zero-pole-gain model. zeros std dev specifies the standard deviations of the zeros of the zero-pole-gain model. poles std dev specifies the standard deviations of the poles of the zero-pole-gain model. gain std dev specifies the standard deviation of the gain of the zero-pole-gain model. |
|  | zeros std dev specifies the standard deviations of the zeros of the zero-pole-gain model. |
|  | poles std dev specifies the standard deviations of the poles of the zero-pole-gain model. |
|  | gain std dev specifies the standard deviation of the gain of the zero-pole-gain model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ZPK Model (MISO)

[IMAGE alt='image' src='si_set_coefficients_to_zpk_model_(miso).gif']

|  | input type specifies whether to set the poles and zeros for the transfer function between the stimulus and the response of the system model or for the transfer function between the noise and the response of the system model. 0stimulus (default)—Sets the poles and zeros for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function.1noise—Sets the poles and zeros for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
| --- | --- |
| 0 | stimulus (default)—Sets the poles and zeros for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function. |
| 1 | noise—Sets the poles and zeros for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of zero-pole-gain model specifies the coefficients and gain of the zero-pole-gain (ZPK) model. zeros specifies the zeros of the zero-pole-gain model. poles specifies the poles of the zero-pole-gain model. gain specifies the gain of the zero-pole-gain model. |
|  | zeros specifies the zeros of the zero-pole-gain model. |
|  | poles specifies the poles of the zero-pole-gain model. |
|  | gain specifies the gain of the zero-pole-gain model. |
|  | std deviations specifies the standard deviations of coefficients of zero-pole-gain model. zeros std dev specifies the standard deviations of the zeros of the zero-pole-gain model. poles std dev specifies the standard deviations of the poles of the zero-pole-gain model. gain std dev specifies the standard deviation of the gain of the zero-pole-gain model. |
|  | zeros std dev specifies the standard deviations of the zeros of the zero-pole-gain model. |
|  | poles std dev specifies the standard deviations of the poles of the zero-pole-gain model. |
|  | gain std dev specifies the standard deviation of the gain of the zero-pole-gain model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Set Coefficients to ZPK Model (MIMO)

[IMAGE alt='image' src='si_set_coefficients_to_zpk_model_(mimo).gif']

|  | input type specifies whether to set the poles and zeros for the transfer function between the stimulus and the response of the system model or for the transfer function between the noise and the response of the system model. 0stimulus (default)—Sets the poles and zeros for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function.1noise—Sets the poles and zeros for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
| --- | --- |
| 0 | stimulus (default)—Sets the poles and zeros for G(z), the transfer function between the stimulus and the response. G(z) is defined as the stimulus transfer function. |
| 1 | noise—Sets the poles and zeros for H(z), the transfer function between the noise and the response. H(z) is defined as the noise transfer function. |
|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | coefficients of zero-pole-gain model specifies the coefficients and gain of the zero-pole-gain (ZPK) model. The elements of the ith row and jth column are the coefficients of the zero-pole-gain model from the jth input to the ith output. zeros specifies the zeros of the zero-pole-gain model. poles specifies the poles of the zero-pole-gain model. gain specifies the gain of the zero-pole-gain model. |
|  | zeros specifies the zeros of the zero-pole-gain model. |
|  | poles specifies the poles of the zero-pole-gain model. |
|  | gain specifies the gain of the zero-pole-gain model. |
|  | std deviations specifies the standard deviations of coefficients of zero-pole-gain model. zeros std dev specifies the standard deviations of the zeros of the zero-pole-gain model. poles std dev specifies the standard deviations of the poles of the zero-pole-gain model. gain std dev specifies the standard deviation of the gain of the zero-pole-gain model. |
|  | zeros std dev specifies the standard deviations of the zeros of the zero-pole-gain model. |
|  | poles std dev specifies the standard deviations of the poles of the zero-pole-gain model. |
|  | gain std dev specifies the standard deviation of the gain of the zero-pole-gain model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/set_names_system_model.html language=enus -->
## TOPIC 00062: SI Set Names to System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/set_names_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/set_names_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Set Names to System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Writes input and output names to a system model. Use the [SI Get Names from System Model](../lvsysid/get_names_system_model.html) VI to read input and output names from a system model.

[IMAGE alt='image' src='si_set_names_to_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | input names specifies the names of the stimulus signals for the system model. |
|  | output names specifies the names of the response signals for the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/set_noise_covar_sys_model.html language=enus -->
## TOPIC 00063: SI Set Noise Covariance to System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/set_noise_covar_sys_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/set_noise_covar_sys_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Set Noise Covariance to System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Applies noise variance and noise covariance to a system model. Use the [SI Get Noise Covariance from System Model](../lvsysid/get_noise_covar_sys_model.html) VI to obtain the noise variance and noise covariance from a system model.

[IMAGE alt='image' src='si_set_noise_covariance_to_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | noise variance specifies the variance of the disturbance for a SISO or MISO system model. |
|  | noise covariance specifies the covariance of the disturbances for a MIMO system. This VI ignores noise covariance if the system model is a SISO or MISO system. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/set_notes_system_model.html language=enus -->
## TOPIC 00064: SI Set Notes to System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/set_notes_system_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/set_notes_system_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Set Notes to System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Writes comments to a system model. Use the [SI Get Notes from System Model](../lvsysid/get_notes_system_model.html) VI to read comments from a system model.

[IMAGE alt='image' src='si_set_notes_to_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | notes specifies the comments you want to store with the system model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/set_samp_rate_sys_model.html language=enus -->
## TOPIC 00065: SI Set Sampling Rate to System Model VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/set_samp_rate_sys_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/set_samp_rate_sys_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Set Sampling Rate to System Model VI

**Owning Palette:** [Model Management VIs](../lvsysid/model_management_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Applies a sampling rate to a system model. Use the [SI Get Sampling Rate from System Model](../lvsysid/get_samp_rate_sys_model.html) VI to retrieve the sampling rate from a system model.

[IMAGE alt='image' src='si_set_sampling_rate_to_system_modelc.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | sampling rate (Hz) specifies the sampling rate to apply to system model. If system model is a continuous system, set sampling rate to a value less than or equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | system model out returns information about the model structure, nominal or estimated parameters, identification result, and so on. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_bandpass_filter.html language=enus -->
## TOPIC 00066: SI Bandpass Filter VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_bandpass_filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_bandpass_filter.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Bandpass Filter VI

**Owning Palette:** [Data Preprocessing VIs](../lvsysid/data_preprocess_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Applies a bandpass filter to stimulus and response signals. Wire data to the **signal in** and **stimulus signal in** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

The bandpass filter is an elliptic infinite impulse response (IIR) filter and has no phase lag.

#### SI Bandpass Filter (SISO Waveform)

[IMAGE alt='image' src='si_bandpass_filter_(siso_waveform)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signal in specifies the input waveform of the stimulus signal. |
|  | response signal in specifies the input waveform of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | low cutoff freq specifies the low cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate. |
|  | high cutoff freq specifies the high cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate and greater than the low cutoff freq. |
|  | stimulus signal out returns the filtered waveform of the stimulus signal. |
|  | response signal out returns the filtered waveform of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Bandpass Filter (SISO Array)

[IMAGE alt='image' src='si_bandpass_filter_(siso_array)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signal in specifies an array that represents the stimulus signal. |
|  | response signal in specifies an array that represents the response signal. |
|  | sampling rate (Hz) is the sampling rate of the stimulus and response signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | low cutoff freq specifies the low cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate. |
|  | high cutoff freq specifies the high cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate and greater than the low cutoff freq. |
|  | stimulus signal out returns the filtered array of the stimulus signal. |
|  | response signal out returns the filtered array of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Bandpass Filter (MISO Waveform)

[IMAGE alt='image' src='si_bandpass_filter_(miso_waveform)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
|  | response signal in specifies the input waveform of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | low cutoff freq specifies the low cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate. |
|  | high cutoff freq specifies the high cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate and greater than the low cutoff freq. |
|  | stimulus signals out returns the filtered waveform array of the stimulus signals. |
|  | response signal out returns the filtered waveform of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Bandpass Filter (MISO Array)

[IMAGE alt='image' src='si_bandpass_filter_(miso_array)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
|  | response signal in specifies an array that represents the response signal. |
|  | sampling rate (Hz) is the sampling rate of the stimulus and response signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | low cutoff freq specifies the low cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate. |
|  | high cutoff freq specifies the high cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate and greater than the low cutoff freq. |
|  | stimulus signals out returns the filtered array of the stimulus signals. |
|  | response signal out returns the filtered array of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Bandpass Filter (MIMO Waveform)

[IMAGE alt='image' src='si_bandpass_filter_(mimo_waveform)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
|  | response signals in specifies the input waveform array of the response signals. Each element of the waveform array is the waveform of one response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | low cutoff freq specifies the low cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate. |
|  | high cutoff freq specifies the high cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate and greater than the low cutoff freq. |
|  | stimulus signals out returns the filtered waveform array of the stimulus signals. |
|  | response signals out returns the filtered waveform array of the response signals. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Bandpass Filter (MIMO Array)

[IMAGE alt='image' src='si_bandpass_filter_(mimo_array)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
|  | response signals in specifies an array that represents the response signals. Each row in the array is one response signal. |
|  | sampling rate (Hz) is the sampling rate of the stimulus and response signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | low cutoff freq specifies the low cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate. |
|  | high cutoff freq specifies the high cutoff frequency of the bandpass filter. The cutoff frequency must be less than half the sampling rate and greater than the low cutoff freq. |
|  | stimulus signals out returns the filtered array of the stimulus signals. |
|  | response signals out returns the filtered array of the response signals. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_freqdomain_pal.html language=enus -->
## TOPIC 00067: Frequency-Domain Model Estimation VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_freqdomain_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_freqdomain_pal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Frequency-Domain Model Estimation VIs

**Owning Palette:** [System Identification VIs](../lvsysid/lv_sysid_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Frequency-Domain Model Estimation VIs to estimate the [frequency response function (FRF)](../lvsysidconcepts/est_frf.html) and to identify a [transfer function (TF)](../lvsysidconcepts/modeldefinitionstf.html) or a [state-space (SS)](../lvsysidconcepts/modeldefinitionsss.html) model of an unknown system.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific System Identification error codes](../lvsysid/sysid_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SI Estimate FRF | Estimates the frequency response function (FRF) of an unknown system. Use the FRF to estimate a transfer function (TF) model or a state-space (SS) model of the system. |
| SI Estimate State-Space Model from FRF | Estimates the parameters of a discrete state-space model for an unknown system by using a frequency response function (FRF). Wire data to the FRF magnitude and FRF phase inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Estimate Transfer Function Model from FRF | Estimates the parameters of a continuous or discrete transfer function (TF) model for an unknown system by using a frequency response function (FRF). You must manually select the polymorphic instance to use. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_lowpass_filter.html language=enus -->
## TOPIC 00068: SI Lowpass Filter VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_lowpass_filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_lowpass_filter.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Lowpass Filter VI

**Owning Palette:** [Data Preprocessing VIs](../lvsysid/data_preprocess_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Applies a lowpass filter to stimulus and response signals. Wire data to the **stimulus signal in** and **response signal in** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

The lowpass filter is an elliptic infinite impulse response (IIR) filter and has no phase lag.

#### SI Lowpass Filter (SISO Waveform)

[IMAGE alt='image' src='si_lowpass_filter_(siso_waveform)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signal in specifies the input waveform of the stimulus signal. |
|  | response signal in specifies the input waveform of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | cutoff frequency specifies the cutoff frequency of the lowpass filter. The cutoff frequency must be less than half the sampling rate. The default is 0.125. |
|  | stimulus signal out returns the filtered waveform of the stimulus signal. |
|  | response signal out returns the filtered waveform of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Lowpass Filter (SISO Array)

[IMAGE alt='image' src='si_lowpass_filter_(siso_array)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signal in specifies an array that represents the stimulus signal. |
|  | response signal in specifies an array that represents the response signal. |
|  | sampling rate (Hz) is the sampling rate of the stimulus and response signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | cutoff frequency specifies the cutoff frequency of the lowpass filter. The cutoff frequency must be less than half the sampling rate. The default is 0.125. |
|  | stimulus signal out returns the filtered array of the stimulus signal. |
|  | response signal out returns the filtered array of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Lowpass Filter (MISO Waveform)

[IMAGE alt='image' src='si_lowpass_filter_(miso_waveform)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
|  | response signal in specifies the input waveform of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | cutoff frequency specifies the cutoff frequency of the lowpass filter. The cutoff frequency must be less than half the sampling rate. The default is 0.125. |
|  | stimulus signals out returns the filtered waveform array of the stimulus signals. |
|  | response signal out returns the filtered waveform of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Lowpass Filter (MISO Array)

[IMAGE alt='image' src='si_lowpass_filter_(miso_array)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
|  | response signal in specifies an array that represents the response signal. |
|  | sampling rate (Hz) is the sampling rate of the stimulus and response signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | cutoff frequency specifies the cutoff frequency of the lowpass filter. The cutoff frequency must be less than half the sampling rate. The default is 0.125. |
|  | stimulus signals out returns the filtered array of the stimulus signals. |
|  | response signal out returns the filtered array of the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Lowpass Filter (MIMO Waveform)

[IMAGE alt='image' src='si_lowpass_filter_(mimo_waveform)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
|  | response signals in specifies the input waveform array of the response signals. Each element of the waveform array is the waveform of one response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | cutoff frequency specifies the cutoff frequency of the lowpass filter. The cutoff frequency must be less than half the sampling rate. The default is 0.125. |
|  | stimulus signals out returns the filtered waveform array of the stimulus signals. |
|  | response signals out returns the filtered waveform array of the response signals. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SI Lowpass Filter (MIMO Array)

[IMAGE alt='image' src='si_lowpass_filter_(mimo_array)c.gif']

|  | order specifies the filter order. The default is 6. The value of order must be greater than 0. Increasing the order value generates a sharper transition band from the filter. |
| --- | --- |
|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
|  | response signals in specifies an array that represents the response signals. Each row in the array is one response signal. |
|  | sampling rate (Hz) is the sampling rate of the stimulus and response signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | cutoff frequency specifies the cutoff frequency of the lowpass filter. The cutoff frequency must be less than half the sampling rate. The default is 0.125. |
|  | stimulus signals out returns the filtered array of the stimulus signals. |
|  | response signals out returns the filtered array of the response signals. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_model_indicator.html language=enus -->
## TOPIC 00069: SI Generic Model Indicator

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_model_indicator.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_model_indicator.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Generic Model Indicator

**Owning Palette:** [System Identification Indicators](../lvsysid/systemidentificationindicators.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Contains information about the mathematical model of a dynamic system. You can use the [Model Management](../lvsysid/model_management_pal.html) VIs to access the information of a system model.

[IMAGE alt='image' src='si_model_indicator.gif']

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_normalize.html language=enus -->
## TOPIC 00070: SI Normalize VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_normalize.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_normalize.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Normalize VI

**Owning Palette:** [Data Preprocessing VIs](../lvsysid/data_preprocess_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Normalizes the stimulus and response signals so that their mean and standard deviation are 0 and 1 respectively. Wire data to the **stimulus signal in** and **response signal in** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

If you know the mean and standard deviation of the signals, set **mean** and **std** to those values. If you do not provide values for **mean** and **std**, this VI estimates the mean and standard deviation of the signals automatically.

#### SI Normalize (SISO Waveform)

[IMAGE alt='image' src='si_normalize_(siso_waveform)c.gif']

|  | stimulus signal in specifies the input waveform of the stimulus signal. |
| --- | --- |
|  | response signal in specifies the input waveform of the response signal. |
|  | mean contains the mean values you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for mean, this VI uses the actual signal to calculate the mean to use. stimulus mean in is the mean value of the stimulus signal. response mean in is the mean value of the response signal. |
|  | stimulus mean in is the mean value of the stimulus signal. |
|  | response mean in is the mean value of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | std contains the standard deviations you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for std, this VI uses the actual signal to calculate the standard deviation to use. stimulus std in is the standard deviation of the stimulus signal. response std in is the standard deviation of the response signal. |
|  | stimulus std in is the standard deviation of the stimulus signal. |
|  | response std in is the standard deviation of the response signal. |
|  | stimulus signal out returns the normalized waveform of the stimulus signal. |
|  | response signal out returns the normalized waveform of the response signal. |
|  | mean out returns the mean values that this VI uses to normalize the stimulus and response signals. stimulus mean out returns the mean value that this VI uses to normalize the stimulus signal. response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | stimulus mean out returns the mean value that this VI uses to normalize the stimulus signal. |
|  | response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | std out returns the standard deviations that this VI uses to normalize the stimulus and response signals. stimulus std out returns the standard deviation that this VI uses to normalize the stimulus signal. response std out returns the standard deviation that this VI uses to normalize the response signal. |
|  | stimulus std out returns the standard deviation that this VI uses to normalize the stimulus signal. |
|  | response std out returns the standard deviation that this VI uses to normalize the response signal. |

#### SI Normalize (SISO Array)

[IMAGE alt='image' src='si_normalize_(siso_array)c.gif']

|  | stimulus signal in specifies an array that represents the stimulus signal. |
| --- | --- |
|  | response signal in specifies an array that represents the response signal. |
|  | mean contains the mean values you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for mean, this VI uses the actual signal to calculate the mean to use. stimulus mean in is the mean value of the stimulus signal. response mean in is the mean value of the response signal. |
|  | stimulus mean in is the mean value of the stimulus signal. |
|  | response mean in is the mean value of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | std contains the standard deviations you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for std, this VI uses the actual signal to calculate the standard deviation to use. stimulus std in is the standard deviation of the stimulus signal. response std in is the standard deviation of the response signal. |
|  | stimulus std in is the standard deviation of the stimulus signal. |
|  | response std in is the standard deviation of the response signal. |
|  | stimulus signal out returns the normalized array of the stimulus signal. |
|  | response signal out returns the normalized array of the response signal. |
|  | mean out returns the mean values that this VI uses to normalize the stimulus and response signals. stimulus mean out returns the mean value that this VI uses to normalize the stimulus signal. response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | stimulus mean out returns the mean value that this VI uses to normalize the stimulus signal. |
|  | response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | std out returns the standard deviations that this VI uses to normalize the stimulus and response signals. stimulus std out returns the standard deviation that this VI uses to normalize the stimulus signal. response std out returns the standard deviation that this VI uses to normalize the response signal. |
|  | stimulus std out returns the standard deviation that this VI uses to normalize the stimulus signal. |
|  | response std out returns the standard deviation that this VI uses to normalize the response signal. |

#### SI Normalize (MISO Waveform)

[IMAGE alt='image' src='si_normalize_(miso_waveform)c.gif']

|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
| --- | --- |
|  | response signal in specifies the input waveform of the response signal. |
|  | mean contains the mean values you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for mean, this VI uses the actual signals to calculate the mean to use. stimulus mean in is the mean values of the stimulus signals. response mean in is the mean value of the response signal. |
|  | stimulus mean in is the mean values of the stimulus signals. |
|  | response mean in is the mean value of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | std contains the standard deviations you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for std, this VI uses the actual signals to calculate the standard deviation to use. stimulus std in is the standard deviations of the stimulus signals. response std in is the standard deviation of the response signal. |
|  | stimulus std in is the standard deviations of the stimulus signals. |
|  | response std in is the standard deviation of the response signal. |
|  | stimulus signals out returns the normalized waveform array of the stimulus signals. |
|  | response signal out returns the normalized waveform of the response signal. |
|  | mean out returns the mean values that this VI uses to normalize the stimulus and response signals. stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. |
|  | response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | std out returns the standard deviations that this VI uses to normalize the stimulus and response signals. stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. response std out returns the standard deviation that this VI uses to normalize the response signal. |
|  | stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. |
|  | response std out returns the standard deviation that this VI uses to normalize the response signal. |

#### SI Normalize (MISO Array)

[IMAGE alt='image' src='si_normalize_(miso_array)c.gif']

|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
| --- | --- |
|  | response signal in specifies an array that represents the response signal. |
|  | mean contains the mean values you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for mean, this VI uses the actual signals to calculate the mean to use. stimulus mean in is the mean values of the stimulus signals. response mean in is the mean value of the response signal. |
|  | stimulus mean in is the mean values of the stimulus signals. |
|  | response mean in is the mean value of the response signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | std contains the standard deviations you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for std, this VI uses the actual signals to calculate the standard deviation to use. stimulus std in is the standard deviations of the stimulus signals. response std in is the standard deviation of the response signal. |
|  | stimulus std in is the standard deviations of the stimulus signals. |
|  | response std in is the standard deviation of the response signal. |
|  | stimulus signals out returns the normalized array of the stimulus signals. |
|  | response signal out returns the normalized array of the response signal. |
|  | mean out returns the mean values that this VI uses to normalize the stimulus and response signals. stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. |
|  | response mean out returns the mean value that this VI uses to normalize the response signal. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | std out returns the standard deviations that this VI uses to normalize the stimulus and response signals. stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. response std out returns the standard deviation that this VI uses to normalize the response signal. |
|  | stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. |
|  | response std out returns the standard deviation that this VI uses to normalize the response signal. |

#### SI Normalize (MIMO Waveform)

[IMAGE alt='image' src='si_normalize_(mimo_waveform)c.gif']

|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
| --- | --- |
|  | response signals in specifies the input waveform array of the response signals. Each element of the waveform array is the waveform of one response signal. |
|  | mean contains the mean values you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for mean, this VI uses the actual signals to calculate the mean to use. stimulus mean in is the mean values of the stimulus signals. response mean in is the mean values of the response signals. |
|  | stimulus mean in is the mean values of the stimulus signals. |
|  | response mean in is the mean values of the response signals. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | std contains the standard deviations you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for std, this VI uses the actual signals to calculate the standard deviation to use. stimulus std in is the standard deviations of the stimulus signals. response std in is the standard deviations of the response signals. |
|  | stimulus std in is the standard deviations of the stimulus signals. |
|  | response std in is the standard deviations of the response signals. |
|  | stimulus signals out returns the normalized waveform array of the stimulus signals. |
|  | response signals out returns the normalized waveform array of the response signals. |
|  | mean out returns the mean values that this VI uses to normalize the stimulus and response signals. stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. response mean out returns the mean values that this VI uses to normalize the response signals. |
|  | stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. |
|  | response mean out returns the mean values that this VI uses to normalize the response signals. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | std out returns the standard deviations that this VI uses to normalize the stimulus and response signals. stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. response std out returns the standard deviations that this VI uses to normalize the response signals. |
|  | stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. |
|  | response std out returns the standard deviations that this VI uses to normalize the response signals. |

#### SI Normalize (MIMO Array)

[IMAGE alt='image' src='si_normalize_(mimo_array)c.gif']

|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
| --- | --- |
|  | response signals in specifies an array that represents the response signals. Each row in the array is one response signal. |
|  | mean contains the mean values you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for mean, this VI uses the actual signals to calculate the mean to use. stimulus mean in is the mean values of the stimulus signals. response mean in is the mean values of the response signals. |
|  | stimulus mean in is the mean values of the stimulus signals. |
|  | response mean in is the mean values of the response signals. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | std contains the standard deviations you want this VI to use to normalize the stimulus and response signals. If you do not provide a value for std, this VI uses the actual signals to calculate the standard deviation to use. stimulus std in is the standard deviations of the stimulus signals. response std in is the standard deviations of the response signals. |
|  | stimulus std in is the standard deviations of the stimulus signals. |
|  | response std in is the standard deviations of the response signals. |
|  | stimulus signals out returns the normalized array of the stimulus signals. |
|  | response signals out returns the normalized array of the response signals. |
|  | mean out returns the mean values that this VI uses to normalize the stimulus and response signals. stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. response mean out returns the mean values that this VI uses to normalize the response signals. |
|  | stimulus mean out returns the mean values that this VI uses to normalize the stimulus signals. |
|  | response mean out returns the mean values that this VI uses to normalize the response signals. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | std out returns the standard deviations that this VI uses to normalize the stimulus and response signals. stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. response std out returns the standard deviations that this VI uses to normalize the response signals. |
|  | stimulus std out returns the standard deviations that this VI uses to normalize the stimulus signals. |
|  | response std out returns the standard deviations that this VI uses to normalize the response signals. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_nyquist_indicator.html language=enus -->
## TOPIC 00071: SI Nyquist Plot Indicator

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_nyquist_indicator.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_nyquist_indicator.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Nyquist Plot Indicator

**Owning Palette:** [System Identification Indicators](../lvsysid/systemidentificationindicators.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Displays the Nyquist plot generated from the [SI Nyquist Plot](../lvsysid/nyquist_plot.html) VI.

[IMAGE alt='image' src='nyquist_plot_indicator.gif']

The above figure shows a Nyquist plot with sample data.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_pole_zero_indicator.html language=enus -->
## TOPIC 00072: SI Pole-Zero Plot Indicator

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_pole_zero_indicator.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_pole_zero_indicator.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Pole-Zero Plot Indicator

**Owning Palette:** [System Identification Indicators](../lvsysid/systemidentificationindicators.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Displays the pole-zero plot generated from the [SI Pole-Zero Plot](../lvsysid/zeros_poles_plot.html) VI.

[IMAGE alt='image' src='pole_zero_plot_indicator.gif']

The above figure shows a pole-zero plot with sample data.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/si_split_signal.html language=enus -->
## TOPIC 00073: SI Split Signal VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/si_split_signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/si_split_signal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Split Signal VI

**Owning Palette:** [Data Preprocessing VIs](../lvsysid/data_preprocess_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Splits stimulus and response signals into two parts. Use one set of signals for model estimation and one for model validation. Wire data to the **stimulus signal in** and **response signal in** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### SI Split Signal (SISO Waveform)

[IMAGE alt='image' src='si_split_signal_(siso_waveform)c.gif']

|  | stimulus signal in specifies the input waveform of the stimulus signal. |
| --- | --- |
|  | response signal in specifies the input waveform of the response signal. |
|  | 1st portion (%) specifies the length of the first portion of the stimulus and response signals as a percentage of the length of the original signals. The default is 66. |
|  | stimulus signal 1 returns the waveform of the first portion of the stimulus signal. |
|  | response signal 1 returns the waveform of the first portion of the response signal. |
|  | stimulus signal 2 returns the waveform of the second portion of the stimulus signal. |
|  | response signal 2 returns the waveform of the second portion of the response signal. |

#### SI Split Signal (SISO Array)

[IMAGE alt='image' src='si_split_signal_(siso_array)c.gif']

|  | stimulus signal in specifies an array that represents the stimulus signal. |
| --- | --- |
|  | response signal in specifies an array that represents the response signal. |
|  | 1st portion (%) specifies the length of the first portion of the stimulus and response signals as a percentage of the length of the original signals. The default is 66. |
|  | stimulus signal 1 returns the array of the first portion of the stimulus signal. |
|  | response signal 1 returns the array of the first portion of the response signal. |
|  | stimulus signal 2 returns the array of the second portion of the stimulus signal. |
|  | response signal 2 returns the array of the second portion of the response signal. |

#### SI Split Signal (MISO Waveform)

[IMAGE alt='image' src='si_split_signal_(miso_waveform)c.gif']

|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
| --- | --- |
|  | response signal in specifies the input waveform of the response signal. |
|  | 1st portion (%) specifies the length of the first portion of the stimulus and response signals as a percentage of the length of the original signals. The default is 66. |
|  | stimulus signals 1 returns the waveform array of the first portion of the stimulus signals. |
|  | response signal 1 returns the waveform of the first portion of the response signal. |
|  | stimulus signals 2 returns the waveform array of the second portion of the stimulus signals. |
|  | response signal 2 returns the waveform of the second portion of the response signal. |

#### SI Split Signal (MISO Array)

[IMAGE alt='image' src='si_split_signal_(miso_array)c.gif']

|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
| --- | --- |
|  | response signal in specifies an array that represents the response signal. |
|  | 1st portion (%) specifies the length of the first portion of the stimulus and response signals as a percentage of the length of the original signals. The default is 66. |
|  | stimulus signals 1 returns the array of the first portion of the stimulus signals. |
|  | response signal 1 returns the array of the first portion of the response signal. |
|  | stimulus signals 2 returns the array of the second portion of the stimulus signals. |
|  | response signal 2 returns the array of the second portion of the response signal. |

#### SI Split Signal (MIMO Waveform)

[IMAGE alt='image' src='si_split_signal_(mimo_waveform)c.gif']

|  | stimulus signals in specifies the input waveform array of the stimulus signals. Each element of the waveform array is the waveform of one stimulus signal. |
| --- | --- |
|  | response signals in specifies the input waveform array of the response signals. Each element of the waveform array is the waveform of one response signal. |
|  | 1st portion (%) specifies the length of the first portion of the stimulus and response signals as a percentage of the length of the original signals. The default is 66. |
|  | stimulus signals 1 returns the waveform array of the first portion of the stimulus signals. |
|  | response signals 1 returns the waveform array of the first portion of the response signals. |
|  | stimulus signals 2 returns the waveform array of the second portion of the stimulus signals. |
|  | response signals 2 returns the waveform array of the second portion of the response signals. |

#### SI Split Signal (MIMO Array)

[IMAGE alt='image' src='si_split_signal_(mimo_array)c.gif']

|  | stimulus signals in specifies an array that represents the stimulus signals. Each row in the array is one stimulus signal. |
| --- | --- |
|  | response signals in specifies an array that represents the response signals. Each row in the array is one response signal. |
|  | 1st portion (%) specifies the length of the first portion of the stimulus and response signals as a percentage of the length of the original signals. The default is 66. |
|  | stimulus signals 1 returns the array of the first portion of the stimulus signals. |
|  | response signals 1 returns the array of the first portion of the response signals. |
|  | stimulus signals 2 returns the array of the second portion of the stimulus signals. |
|  | response signals 2 returns the array of the second portion of the response signals. |

#### Example

Refer to the Four-Stage Evaporator VI in the labview\examples\System Identification\Industry Applications\Process Industry Systems.llb for an example of using the SI Split Signal VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/sysid_utility_pal.html language=enus -->
## TOPIC 00074: Utilities VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/sysid_utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/sysid_utility_pal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Utilities VIs

**Owning Palette:** [System Identification VIs](../lvsysid/lv_sysid_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Utilities VIs to perform miscellaneous tasks on data or the system model, including producing data samples, displaying model equations, merging models, and so on.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific System Identification error codes](../lvsysid/sysid_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SI Data Samples | Produces sample stimulus and response signals. You must manually select the polymorphic instance to use. |
| SI Draw Model | Displays model equations and the sampling rate in a 2D picture control. You can use this VI to display the equations of a transfer function, state-space, zero-pole-gain, AR, ARX, ARMAX, output-error, Box-Jenkins, or general-linear model in a 2D picture control according to the model representation you wire to the system model input. |
| SI Generate Pseudo-Random Binary Sequence | Generates a Pseudo-Random Binary Sequence (PRBS). |
| SI Get Continuous Transfer Function Denominator Information | Returns the denominator from a continuous transfer function model, including Tp, natural frequency, and damping ratio. |
| SI Merge Models | Merges multiple models of the same representation and order to one model. This VI supports only polynomial models. Wire system models to the system model 1 and system model 2 inputs to determine the polymorphic instance to use or manually select the instance. |
| SI Read from File | Reads arrays or waveforms from a specified data file. Use this VI to read spreadsheet text files and waveforms data files. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/systemidentificationindicators.html language=enus -->
## TOPIC 00075: System Identification Indicators

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/systemidentificationindicators.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/systemidentificationindicators.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### System Identification Indicators

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the System Identification indicators to display Bode, Nyquist, and pole-zero plots on the front panel window of a VI you create.

You also can create these indicators from the block diagram by using the [SI Bode Plot](../lvsysid/bode_plot.html) VI, the [SI Nyquist Plot](../lvsysid/nyquist_plot.html) VI, and the [SI Pole-Zero Plot](../lvsysid/zeros_poles_plot.html) VI.

| Palette Object | Description |
| --- | --- |
| SI Bode Plot Indicator | Displays the Bode plot generated from the SI Bode Plot VI. |
| SI Generic Model Indicator | Contains information about the mathematical model of a dynamic system. You can use the Model Management VIs to access the information of a system model. |
| SI Nyquist Plot Indicator | Displays the Nyquist plot generated from the SI Nyquist Plot VI. |
| SI Pole-Zero Plot Indicator | Displays the pole-zero plot generated from the SI Pole-Zero Plot VI. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysid/zeros_poles_plot.html language=enus -->
## TOPIC 00076: SI Pole-Zero Plot VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysid/zeros_poles_plot.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysid/zeros_poles_plot.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SI Pole-Zero Plot VI

**Owning Palette:** [Model Analysis VIs](../lvsysid/model_presentation_pal.html)

**Requires:** Advanced Signal Processing Toolkit *or* Control Design and Simulation Module

Produces the pole-zero plot of a system model on an XY graph.

This VI computes the zeros and poles of the transfer function for one input-output pair of a system model. Use the [SI Pole-Zero Plot Indicator](../lvsysid/si_pole_zero_indicator.html) to display the pole-zero plot on the front panel window.

[Examples](#examples)

[IMAGE alt='image' src='si_zeros_poles_plot.gif']

|  | system model contains information about the model structure, nominal or estimated parameters, identification result, and so on. Use the Model Management VIs to retrieve the information system model contains. Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
| --- | --- |
|  | Note You can use a customized system model probe to view model information that flows through system model wires when you debug a block diagram created with the System Identification VIs. Right-click a system model wire and select Custom Probe»SI System Model from the shortcut menu to use the system model probe. |
|  | channel selects the signal pair with which to compute the transfer function. type specifies whether to compute the transfer function between a stimulus signal and a response signal or the transfer function between a noise signal and a response signal. 0stimulus (default)—Computes the transfer function between a stimulus signal and a response signal. Use input index and output index to select the stimulus and response signals to use.1noise—Computes the transfer function between a noise signal and a response signal. Use input index and output index to select the noise and response signals to use. input index specifies the index of the system input channel with which to compute the transfer function. input index applies only for MISO or MIMO system models. output index specifies the index of the system output channel with which to compute the transfer function. output index applies only for MIMO system models. |
|  | type specifies whether to compute the transfer function between a stimulus signal and a response signal or the transfer function between a noise signal and a response signal. 0stimulus (default)—Computes the transfer function between a stimulus signal and a response signal. Use input index and output index to select the stimulus and response signals to use.1noise—Computes the transfer function between a noise signal and a response signal. Use input index and output index to select the noise and response signals to use. |
| 0 | stimulus (default)—Computes the transfer function between a stimulus signal and a response signal. Use input index and output index to select the stimulus and response signals to use. |
| 1 | noise—Computes the transfer function between a noise signal and a response signal. Use input index and output index to select the noise and response signals to use. |
|  | input index specifies the index of the system input channel with which to compute the transfer function. input index applies only for MISO or MIMO system models. |
|  | output index specifies the index of the system output channel with which to compute the transfer function. output index applies only for MIMO system models. |
|  | confidence level (%) specifies the percentage confidence interval for the poles and zeros. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | show confidence range? specifies whether to show the confidence range of the plot data. The default is TRUE. |
|  | pole-zero plot returns the pole-zero plot of the input signal. pole-zero plot is a plot of the poles and zeros of the system model on the complex plane, where the real values are on the x-axis, and imaginary values are on the y-axis. Use the SI Pole-Zero Plot Indicator to display the pole-zero plot. real returns the real part of zeros and poles. imaginary returns the imaginary part of zeros and poles. |
|  | real returns the real part of zeros and poles. |
|  | imaginary returns the imaginary part of zeros and poles. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the SI Pole-Zero Plot VI:

- Model Presentation VI: labview\examples\System Identification\Getting Started\General.llb
- Flexible Arm VI: labview\examples\System Identification\Industry Applications\Mechanical Systems.llb

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/define_est_pk.html language=enus -->
## TOPIC 00077: Defining and Estimating Partially Known Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/define_est_pk.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/define_est_pk.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Defining and Estimating Partially Known Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Before estimating partially known models, you first must define those models. Using prior knowledge, you choose a model for the dynamic system and set parameter constraints for the model. You then can estimate the model to represent the dynamic system. Use the [SI Create Partially Known State-Space Model](../lvsysid/create_pk_ss_model.html) VI and the [SI Create Partially Known Continuous Transfer Function Model](../lvsysid/create_pk_continuous_tf_model.html) VI to define partially known models.

Use the SI Create Partially Known State-Space Model VI to define partially known continuous or discrete [state-space](modeldefinitionsss.html) models.

You can use the SI Create Partially Known State-Space Model VI, for example, to define a state-space model that represents an RLC circuit consisting of a resistor *R*, an inductor *L*, and a capacitor *C*. Using prior knowledge, you describe the relationship of *R*, *L*, and *C* with the following equations:

[IMAGE alt='image' src='eq_rlc_a.gif']

[IMAGE alt='image' src='eq_rlc_b.gif']

[IMAGE alt='image' src='eq_rlc_c.gif']

*D* = 0

You also can use prior knowledge to define the initial guesses and upper and lower limits of *R*, *L*, and *C*. The SI Create Partially Known State-Space Model VI uses variables rather than numerical values to construct a symbolic model. As the following figure shows, you use variable names, such as *R*, *L*, and *C*, in the **symbolic A**, **symbolic B**, **symbolic C**, and **symbolic D** inputs to define the RLC circuit. Then you specify values for *R*, *L*, and *C* in the **variables** input.

[IMAGE alt='image' src='using_variables.gif']

Use the SI Create Partially Known Continuous Transfer Function Model VI to define partially known continuous transfer function models. The following equation represents a continuous [transfer function](modeldefinitionstf.html) model.

[IMAGE alt='image' src='eq_continuoustf_model.gif']

| where | Kp is the transfer function gain |
| --- | --- |
|  | Td is the delay |
|  | Tp is the first-order time constant |
|  | w is the natural frequency |
|  | r is the damping ratio |
|  | s represents the time |

You can apply the prior knowledge you have about the parameters *K*, *T*<sub>d</sub>, *T*<sub>p</sub>, *w*, and *r* to the **static gain**, **delay(s)**, **T**<sub>p</sub>**(s)**, **natural freq (rad/s)**, and **damping ratio** inputs, respectively, of the SI Create Partially Known Continuous Transfer Function Model VI by defining the initial guesses and upper and lower limits.

With the System Identification VIs and a partially known model, you can set constraints on each parameter of a state-space or continuous transfer function model in two ways—with an upper and lower limit or with an initial guess.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/filt_gauss_white_noise.html language=enus -->
## TOPIC 00078: Filtered Gaussian White Noise (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/filt_gauss_white_noise.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/filt_gauss_white_noise.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Filtered Gaussian White Noise (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Filtered Gaussian white noise is a simple signal that can generate virtually any signal spectra in conjunction with the proper linear filtering. The theoretical [crest factor](choosing_stimulus_signal.html) *C*<sub>f</sub> for a Gaussian is infinite, but clipping the Gaussian amplitude to the input signal limit reduces the crest factor. Clipping the Gaussian amplitude minimally affects the generated spectrum. You can use the [Gaussian White Noise](/csh?topicname=lvanls/gaussian_white_noise.html) VI to generate Gaussian white noise. You then can use the [Filters](/csh?topicname=lvanls/filter_vis.html) VIs to generate Filtered Gaussian white noise from Gaussian white noise.

The following figure shows an example of Filtered Gaussian white noise.

[IMAGE alt='image' src='filtered_gaussian.gif']

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/flexarm_case_study.html language=enus -->
## TOPIC 00079: Flexible Arm Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/flexarm_case_study.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/flexarm_case_study.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Flexible Arm Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

This case study guides you through the system identification process by using the sample data in the [SI Data Samples](../lvsysid/si_data_samples.html) VI. The SI Data Samples VI includes data sets for a DC motor, a flexible robot arm, a ball and beam apparatus, an RC circuit, and so on. This case study uses the flexible arm data to demonstrate the system identification process and to compare different estimation methods.

The flexible arm is a nonlinear dynamic system. The [System Identification](../lvsysid/lv_sysid_pal.html) VIs enable you to build models for linear systems. This case study guides you through obtaining a linear representation of a nonlinear system.

Refer to the labview\examples\system identification\SICaseStudy1.llb to access the VIs in this case study.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/fr_lag_window.html language=enus -->
## TOPIC 00080: Applying a Lag Window (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/fr_lag_window.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/fr_lag_window.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Applying a Lag Window (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

When computing *Φ*<sub>*uu*</sub>(*e*<sup>*jω*</sup>) and *Φ*<sub>*uy*</sub>(*e*<sup>*jω*</sup>) to obtain the frequency response *G*(*e*<sup>*jω*</sup>), you can apply a lag window *ω*(*τ*) to the autocorrelation function *R*<sub>*uu*</sub> and the cross-correlation function *R*<sub>*uy*</sub> before performing the FFT operation. Applying a lag window improves the accuracy of the frequency response estimation, according to the following equations.

[IMAGE alt='image' src='eq_auto-spectral_density.gif']

[IMAGE alt='image' src='eq_cross-spectral_density.gif']

The lag window approaches zero when the lag *τ* is large. The window weighs out the points of *R*<sub>*uu*</sub> and *R*<sub>*uy*</sub> with large lag *τ*, thereby improving the accuracy of the frequency response estimation. The [SI Estimate Frequency Response](../lvsysid/estimate_freq_response.html) VI uses a Hanning window as the lag window.

The [frequency response](si_frequency_response.html) with the lag window, *G*'(*e*<sup>*jω*</sup>), is equivalent to the moving average version of the frequency response without the lag window, *G*(*e*<sup>*jω*</sup>). The average smooths the frequency response, but the smooth frequency response also can deviate from the true frequency response. Adjusting the length of the lag window can balance the trade-off between variance and bias of the frequency response estimation. The larger the length of the lag window, the fewer points of *G*(*e*<sup>*jω*</sup>) the SI Estimate Frequency Response VI averages to compute *G*'(*e*<sup>*jω*</sup>), and hence the larger the variance and the smaller the bias of the frequency estimation.

The following example demonstrates how the length of the lag window affects the frequency response estimation. The following figure shows the front panel of a VI that simulates a system defined by the following equation.

*y*(*k*) – 1.46*y*(*k*– 1) + 2.5*y*(*k* – 2) – 1.46*y*(*k* – 3) + *yk* – 4 = *u*(*k*) + 0.45*u*(*k* – 1) + *u*(*k* – 2)

[IMAGE alt='image' src='lagwindow_fp.gif']

The following figure shows the block diagram of this VI.

[IMAGE alt='image' src='noloc_bd_lag_window.gif']

In this example VI, the input signal *u*(*k*) is a swept sine wave whose normalized frequency is from 0 to 0.5 Hz. The number of data points in the input signal is 4096. The length of the lag window therefore must be less than or equal to 4096. The following figures show the resulting frequency responses when the window length is 4096 and 64, respectively.

[IMAGE alt='image' src='lagwindowlarge.gif']

[IMAGE alt='image' src='lagwindowsmall.gif']

The frequency response curve is smoother and the variance is smaller when the length of the lag window is small. However, when the length of the lag window is too small, you cannot distinguish between the two close peaks in the frequency response, as shown in the previous figure with window length equal to 64. When the length of the lag window is large, the SI Estimate Frequency Response VI accurately estimates the peaks, as shown in the previous figure with window length equal to 4096. The bias is small with a large lag window, but the variance of the estimated frequency response is large.

Setting the length of the lag window to 5–10% of the number of data points when estimating the frequency response often results in a good trade-off between the bias and variance. The length also depends on the signals, the properties of the system, and the purpose of application. For example, to identify the passband of a system, use a smaller lag window. To identify the dynamic properties of a system, such as its natural frequency, use a larger lag window.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/fr_spectral_analysis.html language=enus -->
## TOPIC 00081: Spectral Analysis Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/fr_spectral_analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/fr_spectral_analysis.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Spectral Analysis Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You can use the spectral analysis method with any input signal. However, the frequency bandwidth of the input signal must cover the range of interest.

Because the [frequency response](si_frequency_response.html) is the [Fourier transform](/csh?topicname=lvanlsconcepts/fourier_transform.html) of the impulse response, applying the Fourier transform to both sides of the cross-correlation function yields the following equation.

*Φ*<sub>*uy*</sub>(*e*<sup>*jω*</sup>) = *Φ*<sub>*uu*</sub>(*e*<sup>*jω*</sup>)*G*(*e*<sup>*jω*</sup>)

| where | G(ejω) is the frequency response of the system |
| --- | --- |
|  | Φuu(ejω) is the auto-spectral density of the stimulus signal |
|  | Φuy(ejω) is the cross-spectral density between the stimulus signal u(k) and the response signal y(k) |

You then can use the following equation to compute the frequency response *G*(*e*<sup>*jω*</sup>).

[IMAGE alt='image' src='eq_frequency_response.gif']

You can compute *Φ*<sub>uu</sub>(*e*<sup>*jω*</sup>) and *Φ*<sub>*uy*</sub>(*e*<sup>*jω*</sup>) by applying a fast Fourier transform (FFT) to the autocorrelation function *R*<sub>*uu*</sub> and the cross-correlation function *R*<sub>*uy*</sub>, respectively. The number of data points you need to compute *R*<sub>*uu*</sub> and *R*<sub>*uy*</sub> decreases as the lag *τ* increases. Therefore, *R*<sub>*uu*</sub> and *R*<sub>*uy*</sub> become inaccurate for a large lag *τ*. In this situation, you can apply a [lag window](fr_lag_window.html) to counter the effects of a large lag *τ* and improve the accuracy of the frequency response estimation.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/freq_sysid.html language=enus -->
## TOPIC 00082: Frequency-Domain Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/freq_sysid.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/freq_sysid.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Frequency-Domain Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Frequency-domain model estimation involves identifying a model of a dynamic system by using the frequency-domain representation of the dynamic system data. You acquire frequency-domain data by using a frequency analyzer. If you acquire time-domain data, you also can convert this time-domain data to frequency-domain data by [estimating the frequency response function](est_frf.html) (FRF) of a dynamic system. The FRF represents the frequency-domain relationship between the inputs and outputs of a dynamic system.

Use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to obtain the FRF and estimate two categories of [parametric](parametric_est.html) models—[transfer function](modeldefinitionstf.html) and [state-space](modeldefinitionsss.html). Use the [SI Estimate Transfer Function Model from FRF](../lvsysid/est_tf_from_frf.html) VI to estimate [continuous and discrete](model_types_and_reps.html) single-input single-output (SISO) transfer function models. Use the [SI Estimate State-Space Model from FRF](../lvsysid/est_ss_from_frf.html) VI to estimate discrete SISO and multiple-input multiple-output (MIMO) state-space models.

#### Advantages of Frequency-Domain System Identification

Compared to time-domain model estimation methods, frequency-domain model estimation methods have the following advantages:

- You can reduce a large number of time-domain data samples to a finite number of frequency-domain data samples.
- You can reduce the effects of noise by averaging the FRF from multiple time-domain data measurements.
- You can focus on frequency bands of interest by directly weighting the frequency-domain data.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/freqsysid_case_study.html language=enus -->
## TOPIC 00083: Frequency-Domain Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/freqsysid_case_study.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/freqsysid_case_study.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Frequency-Domain Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

This case study demonstrates how to use frequency-domain data from a flexible robotic arm to estimate and validate a [transfer function](modeldefinitionstf.html) model and [state-space](modeldefinitionsss.html) model of the robotic arm. This case study estimates the models directly from frequency-domain data.

|  | Note If the system you want to estimate contains time-domain data, you first must estimate the FRF by using the SI Estimate FRF VI. |
| --- | --- |

Refer to the Flexible Arm (Frequency Domain) VI in the labview\examples\System Identification\Industry Applications\Mechanical Systems.llb to access the VI in this case study.

In this case study, the input is voltage and the outputs are strain and position. Strain is proportional to the acceleration of the flexible arm. Position is the radial position of the arm.

Because this system contains one input and two outputs, two single-input single-output (SISO) FRFs or one multiple-input multiple-output (MIMO) FRF define this system. One FRF defines the relationship between the voltage input and the strain output. The other FRF defines the relationship between the voltage input and the position output. Each FRF contains information about the magnitude and phase of the frequency response and the scale of the frequency data. This information is specific to each input-output pair. To measure the FRFs in this case study, sine waves at different frequencies excite the flexible arm. This data set has a sampling time of 0.02 seconds, which is equivalent to a sampling rate of 50 Hz.

#### Estimating and Validating a Transfer Function Model

Use the [SI Estimate Transfer Function Model from FRF](../lvsysid/est_tf_from_frf.html) VI to estimate a transfer function model from a SISO FRF. Because this case study involves one input and two outputs, this VI must estimate and validate each SISO transfer function model separately. The following figure shows the block diagram for estimating a transfer function model and validating the resulting transfer function model against the original FRF data. This block diagram uses the FRF describing the relationship between the voltage input and the position output to estimate the transfer function model.

[IMAGE alt='image' src='bd_tf_position.gif']

The **FRF magnitude** and the **FRF phase** inputs of the SI Estimate Transfer Function Model from FRF VI require that the data input is in polar form.

|  | Note If the data input is in complex form, you can use the Re/Im To Polar Function to convert the complex data into polar form to separate the magnitude, phase, and frequency components of the complex representation. After converting the complex data into polar form, bundle the magnitude and frequency components into one cluster and bundle the phase and frequency components into another cluster. Each cluster then contains the data you wire to the FRF magnitude and the FRF phase inputs of the SI Estimate Transfer Function Model from FRF VI. |
| --- | --- |

In this case study, the **FRF magnitude** and the **FRF phase** inputs contain data in polar form. Therefore, the **FRF magnitude** and the **FRF phase** inputs wire directly into the SI Estimate Transfer Function Model from FRF VI.

|  | Note The FRF format input of this VI specifies whether the original FRF magnitude is in decibels or in a linear scale and whether the original FRF phase is wrapped and in radians or in degrees. In this case study, the original FRF data uses the default values of FRF format. The original FRF magnitude is not in decibels. The original FRF phase is wrapped and in radians. |
| --- | --- |

Because a transfer function model is a type of [parametric](parametric_est.html) model representation, you must specify the model parameters before estimating the model. For a transfer function model, you must specify the orders of the numerator and denominator polynomial functions. If you do not have prior knowledge about the system, you must use trial and error to determine the optimal orders of the model.

One way to identify the optimal orders is to observe the peaks in the magnitude response of the original FRF. The optimal order is at least twice the number of peaks. You can plot and observe the magnitude by using the [SI Bode Plot](../lvsysid/bode_plot.html) VI. You can increase the accuracy of the model by modifying the initial guess after analyzing the model. In the previous block diagram, 2 is the initial guess for both the numerator order and the denominator order.

You can [validate](validating_models.html) the resulting model by comparing the original FRF and the FRF that the model generates. Compare the two FRFs on an XY graph by using the SI Bode Plot VI. By default, the SI Bode Plot VI unwraps the phase information and converts the units of the resulting phase to degrees. To compare the original FRF and the FRF that the SI Bode Plot VI displays more accurately, use the [Unwrap Phase](/csh?topicname=lvanls/unwrap_phase.html) VI to unwrap the phase in the original FRF. This case study also uses the [Mathematics](/csh?topicname=lvwave/waveform_measurement_vis.html) VIs to convert the original FRF from radians to degrees.

The following figure shows the [Bode plot](analyzing_models.html#bode_plot) of a 2nd-order transfer function model.

[IMAGE alt='image' src='noloc_eps_fp_tf_position_order3.gif']

Visually inspect the alignment of the **Model-generated FRF** and the **Original FRF** to determine whether the estimated transfer function model accurately describes the dynamic system. Notice that the **Original FRF** and the **Model-generated FRF** do not align. Therefore, 2 is not the most appropriate order value for the transfer function model.

You can increase the accuracy of the model by specifying different values for the **Orders of TF** control. The following figure shows the Bode plots of a 6th-order transfer function model.

[IMAGE alt='image' src='noloc_eps_fp_tf_position.gif']

In this case study, setting the value of the **Orders of TF** to 6 provides a closer alignment of the **Model-generated FRF** and the **Original FRF**. Therefore, a 6th-order transfer function model describes the voltage-position FRF of the dynamic system more accurately than a 2nd-order model.

Identify a second transfer function model by using the FRF of the voltage input and strain output. You must apply the same method when optimizing the model order.

#### Estimating and Validating a State-Space Model

In this case study, a single MIMO FRF also can represent the frequency-domain relationship of the input and outputs of the flexible arm system. You can use this MIMO FRF to estimate state-space models of a dynamic system. The [SI Estimate State-Space Model from FRF](../lvsysid/est_ss_from_frf.html) VI estimates a state-space model for SISO and MIMO systems. This VI requires you to specify the **number of states** of the system you want to estimate. This value comes from prior knowledge about the system.

You also can provide an initial guess if you do not have prior knowledge. A guideline for identifying the number of states of a system is the same as the guideline for identifying the orders of a transfer function model. The number of states is at least twice the number of peaks in the magnitude of the FRF. Because a MIMO FRF is composed of more than one SISO FRF, you must observe the magnitude of the SISO FRF with the maximum number of peaks.

In this case study, the SISO FRFs that comprise the MIMO FRF both have one peak. Therefore, the initial guess at the number of states is 2. By increasing the number of states and plotting the model-generated MIMO FRF along with the original MIMO FRF on a Bode plot, you can observe that entering eight states produces an acceptable estimation for the system.

The following figure shows the Bode Plots of the original MIMO FRF and the MIMO FRF that the state-space model generates.

[IMAGE alt='image' src='fp_ss.gif']

Compare the **FRF Position** graphs in the previous figure with the 6th-order transfer function **FRF Position** graphs. Both model-generated FRFs are close to the original FRF in the **FRF Position** graphs. The proximity of these FRFs indicates that the 6th-order transfer function model and the state-space model with eight states are close approximations for estimating system models in this case study.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/indirect_id.html language=enus -->
## TOPIC 00084: Indirect Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/indirect_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/indirect_id.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Indirect Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The indirect identification approach, which estimates the [transfer function](modeldefinitionstf.html) model of a dynamic system in a closed-loop system, first identifies the transfer function model of the closed-loop system based on the reference signal and the response signal. This approach then retrieves the transfer function model of the dynamic system from the identified closed-loop system. The indirect identification approach can identify the transfer function of the dynamic system accurately even when the signal-to-noise ratio (SNR) of the system is low and no matter whether the output noise is white noise or color noise. However, this approach requires prior knowledge about the controller of the system and the reference signal also must be available. In addition, any inaccuracy or nonlinearity of the controller in the system might affect estimating the model of the dynamic system.

With indirect identification, you can use the following two equations to describe the [feedback-path closed-loop system](closed-loop_est.html).

*y*(*k*) = *G*<sub>0</sub>(*z*)*u*(*k*) + *e*(*k*)

*u*(*k*) = *r*(*k*) – *F*
 <sub>y</sub>(*z*)*y*(*k*)

| where | G0(z) is the open-loop transfer function of the dynamic system |
| --- | --- |
|  | Fy(z) is the transfer function of a linear, time-invariant (LTI) controller |
|  | u(k) is the stimulus signal of the system |
|  | y(k) is the response signal of the system |
|  | r(k) is the reference signal of the system |
|  | e(k) is the output noise of the system |

By combining the previous two equations, you can represent the closed-loop relationship with the following equation:

[IMAGE alt='image' src='eq_closed-loop1.gif']

If you define *G*<sub>cl</sub> as the closed-loop transfer function between the reference signal and the response signal, and let *G*<sub>cl</sub> satisfy the following equation:

[IMAGE alt='image' src='eq_closed-loop2.gif']

you can estimate *G*<sub>cl</sub> with *r*(*k*) as the input and *y*(*k*) as the output using an open loop method, because *r*(*k*) and *e*(*k*) are uncorrelated. You then can calculate *G*<sub>0</sub>after you calculate *G*<sub>cl</sub>, as the following equation shows:

[IMAGE alt='image' src='eq_closed-loop3.gif']

For [feedforward-path closed-loop systems](closed-loop_est.html), you use the following two equations to describe the systems.

*y*(*k*) = *G*<sub>0</sub>(*z*)*u*(*k*) + *e*(*k*)

*u*(*k*) = [*r*(*k*) – *y*(*k*)]*F*<sub>y</sub>(*z*)

By combining the previous two equations, you can represent the feedforward-path closed-loop relationship with the following equation:

[IMAGE alt='image' src='eq_closed-loop4.gif']

If you define *G*<sub>cl</sub> as the feedforward-path closed-loop transfer function and let *G*<sub>cl</sub> satisfy the following equation:

[IMAGE alt='image' src='eq_closed-loop5.gif']

you can estimate *G*<sub>cl</sub> with *r*(*k*) as the input and *y*(*k*) as the output using an open loop method, because *r*(*k*) and *e*(*k*) are uncorrelated. You then can calculate *G*<sub>0</sub>after you calculate *G*<sub>cl</sub>, as the following equation shows:

[IMAGE alt='image' src='eq_closed-loop6.gif']

With indirect identification, you calculate *G*<sub>cl</sub>by performing polynomial operations on *G*<sub>o</sub> and *F*<sub>y</sub>. Because of the limitations of polynomial operations, the orders of the numerator and denominator might change after manipulation. Thus, the [SI Estimate Transfer Function Model](../lvsysid/est_transfer_function_model.html) VI or the [SI Transfer Function Estimation](../lvsysid/est_tf_model_express.html) Express VI, which you can use with the indirect identification approach, might return an error regarding the mismatch between the order you set and the order of the estimated model. In this case, you must adjust the tolerance setting of these two VIs so that the numerator and denominator orders match the orders you set. A larger tolerance facilitates zero-pole cancellations, which reduce the numerator and denominator polynomial orders.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/influencing_factors.html language=enus -->
## TOPIC 00085: Accounting for Factors that Influence a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/influencing_factors.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/influencing_factors.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Accounting for Factors that Influence a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The key to the system identification process is having some knowledge of the system for which you want to identify a model. This knowledge provides the basis for determining which signals are outputs, which in turn determines sensor placement, and which signals are inputs that you can use to excite the system. Simple tests might be necessary to determine influences, coupling, time delays, and time constants to aid in the modeling effort.

You also must consider signals that are not directly capable of being manipulated but still affect the system. You must include those signals as inputs to the system model. For example, consider the effect of wind gusts on the pitch dynamics of an airplane. The airplane responds in pitch to the elevator angle as a direct input. A wind gust affects the pitch of an airplane, which in turn influences the dynamics of the airplane, but the wind gust is not directly adjustable. To create an accurate model of the airplane, you might want to include wind gusts as an input variable.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/least_mean_squares.html language=enus -->
## TOPIC 00086: Least Mean Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/least_mean_squares.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/least_mean_squares.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Least Mean Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The least mean squares (LMS) method uses the following equations to define the cost function *J*(*k*) = *E*[*e*
 <sup>2</sup>(*k*)].

The parametric vector [IMAGE alt='image' src='eq_predicted_response2.gif'] updates according to the following equation.

[IMAGE alt='image' src='eq_least_mean_sq1.gif']

*k* is the number of iterations, μ is step-size, which is a positive constant, and [IMAGE alt='image' src='eq_data_vector1.gif'] is the data vector from the past input data *u*(*k*) and output data *y*(*k*). [IMAGE alt='image' src='eq_data_vector1.gif'] is defined by the following equation.

[IMAGE alt='image' src='eq_least_mean_sq2.gif']

The following procedure describes how to implement the LMS algorithm.

1. Initialize the step-size μ.
2. Initialize the parametric vector using a small positive number ε. 
 
 [IMAGE alt='image' src='eq_least_mean_sq3.gif']
3. Initialize the data vector . 
 
 [IMAGE alt='image' src='eq_least_mean_sq5.gif']
4. For k = 1, update the data vector based on and the current input data u ( k ) and output data y ( k ).
5. Compute the predicted response using the following equation. 
 
 [IMAGE alt='image' src='eq_least_mean_sq6.gif']
6. Compute the error e ( k ) by solving the following equation. 
 
 [IMAGE alt='image' src='eq_system_error.gif']
7. Update the parameter vector . 
 
 [IMAGE alt='image' src='eq_least_mean_sq7.gif']
8. Stop if the error is small enough, else set k = k + 1 and repeat steps 4–8.

The LMS algorithm is one of the most widely used and understood adaptive algorithms. Selecting the step-size μ is important with the LMS algorithm, because the selection of the step-size μ directly affects the rate of convergence and the stability of the algorithm. The convergence rate of the LMS algorithm is usually proportional to the step-size μ. The larger the step-size μ, the faster the convergence rate. However, a large step-size μ can cause the LMS algorithm to become unstable. The following equation describes the range of the step-size μ.

0 < μ < μ
 <sub>max</sub>

μ
 <sub>max</sub> is the maximum step-size that maintains stability in the LMS algorithm. μ
 <sub>max</sub> is related to the statistical property of the stimulus signal. A uniformly optimized step-size μ that achieves a fast convergence speed while maintaining the stability in the system does not exist, regardless of the statistical property of the stimulus signal. For better performance, use a self-adjustable step-size μ and the [normalized least mean squares (NLMS)](normalized_lms.html) algorithm.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/model-based_cd.html language=enus -->
## TOPIC 00087: Model-Based Control Design Process (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/model-based_cd.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/model-based_cd.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Model-Based Control Design Process (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The model-based control design process involves building a model of a plant, analyzing and synthesizing a controller for the plant, simulating the plant and controller, and deploying the controller. National Instruments provides a complete solution for identifying and validating a plant model, designing a controller for the model, analyzing the controller, and prototyping and deploying the control system. The following figure shows this process, which is based on LabVIEW and National Instruments Real-Time (RT) Series hardware.

[IMAGE alt='image' src='noloc_eps_ni_tool_chain.gif']

#### Analyzing Data and Creating a Plant Model

In the initial phase of the design process, you must obtain a mathematical model of the plant you want to control. One way to obtain a model is by using a numerical process known as system identification. This process involves acquiring data from a plant and then numerically analyzing stimulus and response data to estimate the parameters of the plant.

National Instruments provides DAQ and modular instrumentation software and hardware that you can use to stimulate and measure the response of the plant. You then can use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to estimate and create accurate mathematical models of the plant.

System identification is a process that includes [acquiring](acquiring_data.html) and [preprocessing](preprocessing_data.html) raw data from a dynamic system and [identifying mathematical models](estimating_models.html) based on the raw data. You then [validate](validating_models.html) that the resulting model accurately describes the observed system behavior. If the results are unsatisfactory, you revise the parameters and iterate through the process. The following flowchart shows a typical system identification process.

[IMAGE alt='image' src='noloc_eps_system_id_app_flowchart.gif']

A real-world system seldom has one model that perfectly describes all the observed behaviors of the system. Because system identification involves many variables—such as sampling frequency, type of mathematical model, model order, and so on—you usually have a number of models you can use. Each model describes the behavior of the system to some extent or in a particular mode of operation.

Furthermore, multiple applicable algorithms might be available for the same model. The algorithms you select depend on the model structure, stochastic assumptions, and numerical properties of the algorithm. The System Identification VIs include different adaptive techniques for [recursive system identification](recursive_est.html) and different algorithms for model estimation.

#### Designing a Controller

In the second phase of the design process, you synthesize and analyze a controller. The LabVIEW Control Design and Simulation Module provides a set of VIs for classical and modern linear control analysis and design techniques. With these VIs you can design, implement, and deploy linear time-invariant (LTI) system models.

You can use the Control Design and Simulation Module to analyze the plant model you identified with the System Identification VIs. The Control Design and Simulation VIs help you determine an appropriate controller structure. You then can synthesize a controller to achieve the desired performance criteria of the system based on the dynamic behavior of the plant and/or control system. Finally, you can analyze the overall system by combining the controller with the identified plant model.

#### Simulating the Plant

In the third phase of the design process, you simulate the plant. You can simulate plants in LabVIEW by using the Control Design and Simulation Module. You can use this software to perform offline simulations of a linear or nonlinear plant model. You can use this simulation to investigate the time and frequency responses of the plant due to complex, time-varying inputs. If you install the LabVIEW Real-Time Module, you also can perform rapid control prototyping (RCP), and hardware-in-the-loop (HIL) simulations by using NI RT Series hardware.

#### Deploying the Controller

The last stage of the design process is to deploy the controller to an RT target, such as a PXI or CompactRIO controller. LabVIEW, the Control Design and Simulation Module, the Real-Time Module, and NI RT Series hardware provide a common platform that you can use to design, prototype, and deploy the embedded control system. You also can use the Control Design and Simulation Module and the Real-Time Module as the platform for implementing the control system.

National Instruments also provides products for I/O and signal conditioning, such as NI DAQ and SCXI devices, that you can use to gather and process data. Using these tools, which are built on the LabVIEW platform, you can experiment with different approaches at each stage in the design process and quickly identify the optimal design solution for an embedded control system.

Refer to the National Instruments website for more information about these National Instruments products.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/partially_known_est.html language=enus -->
## TOPIC 00088: Partially Known Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/partially_known_est.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/partially_known_est.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Partially Known Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The [nonparametric](nonparametric_est.html) and [parametric](parametric_est.html) model estimation methods, also known as black-box estimation methods, assume that systems are unknown. Because these estimation methods do not take prior system knowledge into account, you must use either an algorithm or trial-and-error to vary model parameters until the behavior of the model matches the measured input-output data. Although you can use the estimated parameters to reproduce the response of the system accurately, these parameters might not have any physical meanings.

However, in practice, many systems are partially known because you have information about the underlying dynamics or some of the physical parameters. You can use [partially known](define_est_pk.html) model estimation methods, also known as grey-box estimation methods, to estimate models when you have this information.

Black-box methods also assume that all model parameters are adjustable. However, in many real-world applications, you cannot adjust all the parameters arbitrarily, because the parameters might have constraints. For example, in some chemical processes, water must flow only in one direction. When estimating the flow rate of water, you know that the flow rate cannot be negative. Thus, the constraint is that the flow rate must be a positive value. You must consider this constraint and any other constraints when you estimate the flow rate of water in this process. Such constraints usually follow one of the following guidelines:

- A parameter must be as close to a value as possible.
- A parameter must be between two values.
- Two or more parameters must correlate to each other.

These constraints reflect the knowledge you have of the physical system. This knowledge can result in a more realistic parameter estimation. Parameter constraints increase the possibility of the [System Identification](../lvsysid/lv_sysid_pal.html) VIs locating the optimal parameters that describe the dynamic system model. Parameter constraints also improve the accuracy of locating these optimal parameters.

You can set parameter constraints when using grey-box estimation methods, whereas you cannot set parameter constraints when using black-box estimation methods. When using these methods, you can set only the model order that specifies the number of parameters to calculate.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/pk_case_study.html language=enus -->
## TOPIC 00089: Partially Known Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/pk_case_study.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/pk_case_study.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Partially Known Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

This case study gives an example that uses the prior knowledge you have about a system to define and estimate [state-space](modeldefinitionsss.html) models. You use the same procedure when estimating continuous [transfer function](modeldefinitionstf.html) models. However, you apply different methods to define continuous transfer function models.

The following figure shows an RLC circuit, where *u* is the input voltage, *y* is the output voltage, *i*<sub>L</sub> is the current, and *u*<sub>C</sub> is the capacitor voltage. In this example, *y* equals the capacitor voltage *u*<sub>C</sub>.

[IMAGE alt='image' src='noloc_eps_rlc_circuit.gif']

Suppose *R* is 1.5 Ω and *L* and *C* are unknown. You can complete the following steps to identify the values of *L* and *C*.

1. Apply a wide-band voltage to u and measure the output y simultaneously. The Continuous State-Space Model of an RLC Circuit example VI uses a chirp signal from 0.5 Hz to 6 Hz as the stimulus signal. The response to the chirp signal is the response signal. This example VI then preprocesses the stimulus and response signals to remove the offset level in these signals.
2. Define a model for this circuit. Because you have information about the approximate values of L and C , you can build a partially known state-space model or a partially known transfer function model.
3. Estimate the model you defined in step 2 and then estimate L and C .

The Continuous State-Space Model of an RLC Circuit example VI guides you through defining and estimating a state-space model for the RLC circuit.

Refer to the Continuous State-Space Model of an RLC Circuit VI in the labview\examples\System Identification\Getting Started\Grey-Box Model.llb to access the VI in this case study.

Refer to the Continuous Transfer Function Model of a DC Motor with Known Gain VI in the labview\examples\System Identification\Getting Started\Grey-Box Model.llb for an example that demonstrates how to use a partially known transfer function model to estimate the RLC circuit.

You can use the following first-order differential equation to represent the relationship between the capacitor voltage and the current of this RLC circuit.

[IMAGE alt='image' src='eq_capacitor_volt_rlc.gif']

You can use the following first-order differential equation to represent the voltage relationship in this RLC circuit.

[IMAGE alt='image' src='eq_volt_rlc.gif']

By manipulating the previous two equations, you can deduce the continuous state-space model for this RLC circuit using the following two equations:

[IMAGE alt='image' src='eq_continuousss_model_rlc1.gif']

[IMAGE alt='image' src='eq_continuousss_model_rlc2.gif']

Use the [SI Create Partially Known State-Space Model](../lvsysid/create_pk_ss_model.html) VI to build the symbolic state-space model for this circuit, as shown in the following figure.

[IMAGE alt='image' src='noloc_bd_defining_partially_known_state_space_model.gif']

You specify the symbolic state-space model using formula strings, such as 1/C, -1/L, and -1.5/L, with *L* and *C* as variables. Then you define *L* and *C* with the **variables** input, as shown in the following figure. Using prior knowledge, you know that *L* is a positive value around the initial value of 0.1 H, and *C* is a value between 0 F and 0.3 F.

[IMAGE alt='image' src='model_parameters_of_rlc_circuit.gif']

Next, you can estimate the state-space model with the [SI Estimate Partially Known State-Space Model](../lvsysid/est_pk_ss_model.html) VI, as shown in the following figure.

[IMAGE alt='image' src='noloc_bd_estimate_partially_known_state_space_model.gif']

The SI Estimate Partially Known State-Space Model VI estimates each parameter of the model. You obtain the estimated model and optimized variables of the model after this VI performs an optimization. In this example, you obtain the values 0.20 H for *L* and 0.02 F for *C*, as shown in the following figure.

[IMAGE alt='image' src='optimized_variables.gif']

The Continuous State-Space Model of an RLC Circuit example VI uses the [SI Draw Model](../lvsysid/draw_model.html) VI and the values of *L* and *C* you obtain to display the estimated model in a 2D picture control, as shown in the following figure.

[IMAGE alt='image' src='estimated_model.gif']

You then can determine how accurately this model simulates the dynamic system by [validating the model](validating_models.html). Refer to the [System Identification Case Study](sysid_case_study.html) book for an example of validating a model.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/si_impulse_response.html language=enus -->
## TOPIC 00090: Impulse Response (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/si_impulse_response.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/si_impulse_response.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Impulse Response (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

An impulse input to a dynamic system is defined differently depending on whether the system is discrete or continuous. For a continuous dynamic system, an impulse input, also known as the Dirac delta function, is a unit-area signal with an infinite amplitude and infinitely small duration occurring at a specified time. At all other times, the input signal value is zero. For a discrete system, an impulse is a physical pulse that has unit amplitude at the first sample period and zero amplitude for all other times.

The following figure shows an impulse input.

[IMAGE alt='image' src='noloc_eps_unit_impulse.gif']

| where | t is time |
| --- | --- |
|  | u(t) is the input signal |

Because the impulse signal excites all frequencies and the duration of this signal is infinitely small, you can see the natural response of the system.

The following figure shows that the impulse response of a linear time-invariant system is equal to the output *y*(*k*) of the system when you apply an impulse signal to the input *u*(*k*) of the system. The impulse response provides the complete characteristic information of a system.

[IMAGE alt='image' src='noloc_eps_impulse_response_definition.gif']

If you know the impulse response *h*(*n*) and the input signal *u*(*k*) of a system, then you can compute the output *y*(*k*) of the system by using the following equation.

[IMAGE alt='image' src='eq_ir_output.gif']

where*e*(*k*) is the disturbance of the system.

According to impulse response theory, when you apply a Dirac delta function to a system, the output of the system is the impulse response. You can think of the Dirac delta function *δ*(*x*) as a function that has the value of infinity for *x* = 0, the value zero elsewhere, and a total integral of one. However, generating an ideal Dirac delta function is unrealistic.

If you apply an approximate impulse with a small duration to the input of a system, the output of the system is the approximation of the impulse response of the system. The smaller the duration of the impulse, the closer the output of the system is to the true impulse response. However, an impulse carries little energy and might not excite the system, and noise might corrupt the output of the system. An impulse with a large amplitude and duration can improve the signal-to-noise ratio of the output signal. However, a large amplitude impulse can damage the hardware of the system, and a long-duration impulse leads to inaccuracy. For these reasons, you can use the [least squares](ir_least_squares.html) and [correlation analysis](ir_correlation_analysis.html) methods to estimate the impulse response.

#### Applications of the Impulse Response

The impulse response not only indicates the stability and causality of the system if [feedback](closed-loop_est.html#feedback_in_systems) exists in the system, but also provides information on properties such as the damping, dominating time constant, and time delay. Some of this information, such as the time delay, is useful for [parametric model estimation](parametric_est.html). Therefore, you can use nonparametric impulse response estimation before parametric model estimation to help estimate the parameters. You can use the [SI Estimate Impulse Response](../lvsysid/estimate_impulse_response.html) VI to estimate the impulse response and determine the time delay of a system by using the correlation analysis method.

The following figure shows the block diagram of a VI that simulates a system defined by the following equation.

*y*(*k*) = 0.2*u*(*k* – 2) + 0.8*u*(*k* – 3) + 0.3*u*(*k* – 4)

[IMAGE alt='image' src='timedelay_bd.gif']

In the previous figure, the two initial values of the **estimated impulse response** are smaller than the **confidence level**. You can have 99.0% confidence that values less than the **confidence level** are insignificant, and you can consider those values to be equal to 0. Therefore, you can conclude that the time delay of the system is 2 because the beginning of the first two values of the impulse response are zero.

Another common application of the impulse response is to detect feedback in systems by using the least squares method. If feedback exists in a system, the impulse response of the system becomes significantly large at negative lags and the correlation between the input signal and disturbance *e*(*k*) is nonzero. The correlation analysis method assumes the input signal and the disturbance *e*(*k*) are independent from each other. Thus, this method cannot estimate accurately the impulse response of the system that contains feedback. Only the least squares method can provide reliable results. You can use the [SI Detect Feedback](../lvsysid/detect_feedback.html) VI to estimate the impulse response of a system and determine whether feedback exists in the system.

Refer to the Feedback Detection VI in the labview\examples\System Identification\Getting Started\General.llb for an example that demonstrates how to use the SI Detect Feedback VI to detect feedback in a system.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/si_sampling_rate.html language=enus -->
## TOPIC 00091: Selecting a Sampling Rate (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/si_sampling_rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/si_sampling_rate.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Selecting a Sampling Rate (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The time constants of a system influence the selection of a sampling rate. Sampling at rates substantially greater than the system bandwidth leads to data redundancy, numerical issues, and modeling of high frequency artifacts likely due to noise. Sampling at rates slower than system dynamics leads to difficulties determining an accurate system model and problems introduced by aliasing. You can use an [anti-aliasing filter](anti-aliasing_filter.html) to counter the effects of aliasing.

A common rule of thumb is to sample signals at 10 times the bandwidth of the system or the bandwidth of interest for the model. If uncertainty exists in the system bandwidth and a fast data acquisition environment is available, you can sample as fast as possible, then use a digital filter and decimation to reduce the sampling rate to the desired value. Decimation is a form of [downsampling](filt_downsampling.html) the data set. You must ensure the sampling rate is constant to estimate the system model. If you sample data without a constant sampling rate, you must sample the data again with a constant sampling rate.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_acq_data.html language=enus -->
## TOPIC 00092: Part 2: Exciting the System and Acquiring Data (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_acq_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_acq_data.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 2: Exciting the System and Acquiring Data (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After you [choose a proper dynamic system model](sigs_phys_model.html), you must acquire the input and output data from the direct current (DC) servomotor. You then [preprocess](preprocessing_data.html) and use the data to estimate unknown coefficients of the dynamic system model. You can use an encoder or a DC tachometer to measure the shaft speed of the DC servomotor.

Set up the following experimental circuit to excite the DC servomotor and acquire response signals with an encoder.

[IMAGE alt='image' src='noloc_eps_sigs_motor_exp_encoder.gif']

Set up the following experimental circuit to excite the DC servomotor and acquire response signals with a DC tachometer.

[IMAGE alt='image' src='noloc_eps_sigs_motor_exp_tacho.gif']

Both circuits use an NI data acquisition (DAQ) card to generate digital stimulus signals. You also can use a reconfigurable I/O (RIO), CompactRIO, or Single-Board RIO device to generate the stimulus signals and acquire data. In these two circuits, a D/A output channel of the NI-DAQ card converts the stimulus signals to analog voltage signals and sends these signals to an amplifier. An A/D input on the NI-DAQ card acquires the original analog signals, converts the signals to digital signals, and records these digital signals for identification. The amplifier sends the enhanced analog signals to drive the DC servomotor. If you use an encoder to measure the shaft speed of the DC servomotor, the encoder generates pulses when the DC servomotor rotates. The encoder sends the pulses to a digital input channel of the NI-DAQ card. A counter in the NI-DAQ card counts the number of pulses and computes the rotational speed of the DC servomotor. If you use a DC tachometer to measure the shaft speed of the DC servomotor, the DC tachometer generates back-EMF voltage signals when the DC servomotor rotates. The DC tachometer sends the voltage signals to another A/D channel of the NI-DAQ card. The NI-DAQ card calculates the rotational speed by using the voltage signals.

|  | Note Ensure the NI-DAQ card acquires stimulus voltage signals and rotational speed synchronously. Ensure you acquire and save synchronous stimulus signals and response signals with constant time steps. |
| --- | --- |

You can use the following [types of stimulus signals](choosing_stimulus_signal.html):

- Step signals —Use step stimulus signals for the low frequency band of a linear dynamic system. This type of signal is easy to generate but has a low signal-to-noise ratio (SNR) in the high frequency bands. To generate a step signal, create an array that begins with a series of zeros and then shifts to a series of ones, such as "0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1". An element in this array represents a sampling point. Ensure the array contains enough elements according to the sampling rate of the device you use. You then use the Build Waveform (Analog Waveform) function to convert this array to a waveform signal.
- Swept sine signals —Use swept sine stimulus signals for the full frequency bands of a linear dynamic system. This type of stimulus signal has a high SNR in the full frequency bands of a linear dynamic system. However, if the response signals contain non-linear distortion, this type of stimulus signal cannot eliminate the distortion and leads to an inaccurate dynamic system model. Use the Chirp Pattern VI to generate an array containing a swept sine pattern. You then use the Build Waveform (Analog Waveform) function to convert this array to a waveform signal.
- Random signals —Use random stimulus signals for the full frequency band of dynamic systems. This type of stimulus signal has a high SNR in the full frequency band. You must repeat exciting the dynamic system and acquiring data for multiple times to cover the full range of the dynamic system and eliminate any non-linear distortion in the response signals. Use the Periodic Random Noise VI to generate an array of periodic random noise. You then use the Build Waveform (Analog Waveform) function to convert this array to a waveform signal.

In this example, you can use any of these three types of stimulus signals to excite the DC servomotor.

Refer to the following VIs for examples of generating stimulus signals and acquiring data from a dynamic system. You must have the required hardware, such as an NI-DAQ card, to use these examples.

- Stimulus Signal Generation (DAQmx) VI: labview\examples\System Identification\Getting Started\General.llb 
 Open example 
 Find related examples
- Stimulus and Response Data (DAQmx) VI: labview\examples\System Identification\Getting Started\General.llb 
 Open example 
 Find related examples
- Stimulus and Response Data with Encoder (DAQmx) VI: labview\examples\System Identification\Getting Started\General.llb 
 Open example 
 Find related examples

Alternately, if you do not have the required hardware or a DC servomotor, use the [SI Data Samples](../lvsysid/si_data_samples.html) VI to generate the input and output data. This tutorial uses the SI Data Samples VI to complete the following parts. If you also use this VI to complete the following parts, you can get identical results as the results in this tutorial.

Complete the following steps to generate the input and output data by using the SI Data Samples VI.

1. Create a blank VI in LabVIEW.
2. Add the SI Data Samples VI to the block diagram of the VI you created. This VI generates single-input single-output waveform signals by default.
 [IMAGE alt='image' src='add.gif'] Add
3. Right-click the data input of this VI and select Create»Constant from the shortcut menu to create a constant for this input.
4. Ensure the value of this constant is Motor .

You can save this VI and use this VI to complete the following parts of this tutorial.

| Previous: Choosing a Proper System Model by Using Physical Modeling | Next: Identifying Dynamic System Models |
| --- | --- |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_mod_convert.html language=enus -->
## TOPIC 00093: Part 5: Converting Dynamic System Models to Control Design Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_mod_convert.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_mod_convert.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 5: Converting Dynamic System Models to Control Design Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If you want to design controllers for a dynamic system, you must convert the dynamic system model you [identified](sigs_model_id.html) to a system model that you can use in the LabVIEW Control Design and Simulation Module. For example, you can use the Control Design and Simulation Module to design controllers for this DC servomotor to control the behaviors of this DC servomotor.

You also can use the Control Design and Simulation Module to complete the following tasks:

- Construct plants and control models
- Analyze dynamic system performance
- Simulate dynamic systems with a wide option of solvers
- Deploy dynamic systems to real-time hardware

Complete the following steps to convert a dynamic system model to a control design model.

1. Add the SI Convert to Models of CDT VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add
2. Select a proper instance of this polymorphic VI.
  - MIMO TF —Select this instance to convert a transfer function dynamic system model.
  - MIMO SS —Select this instance to convert a state-space dynamic system model.
3. Create a constant for the realization type input of the SI Convert to Models of CDT VI.
4. Set the realization type constant to full .
5. Wire the system model out output of the following VIs or Express VIs to the system model input of the SI Convert to Models of CDT VI.
  - SI Estimate State-Space Model VI
  - SI Estimate Transfer Function Model VI
  - SI Model Estimation Express VI
  - SI Transfer Function Estimation Express VI
6. Create an indicator for the transfer function model or state-space model output of the SI Convert to Models of CDT VI. The following figure shows the block diagram. 
 [IMAGE alt='image' src='noloc_eps_sigs_cdt_model_conv.gif']
7. Wire all error in and error out terminals on the block diagram.
8. Run this VI to convert the dynamic system model.
9. Save the resulting model.

The following figure shows the resulting dynamic system model.

[IMAGE alt='image' src='sigs_cdt_model_result.gif']

|  | Note If you have the Control Design and Simulation Module installed, you can wire the resulting model to the Control Design VIs and Functions or the Simulation VIs and Functions. |
| --- | --- |

| Previous: Validating and Analyzing Dynamic System Models |  |
| --- | --- |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_mod_id_ctss.html language=enus -->
## TOPIC 00094: Identifying Continuous-Time State-Space Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_mod_id_ctss.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_mod_id_ctss.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Identifying Continuous-Time State-Space Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After [physical modeling](sigs_phys_model.html), you can describe the direct circuit (DC) servomotor by using the following differential equations:

[IMAGE alt='image' src='eq_sigs_n_k_model.gif']

Set *K*<sub>*i*</sub> to be equal to *K*<sub>*e*</sub> to transform these differential equations. If you want to design an analog state feedback controller, transform these differential equations to the following dynamic system model:

[IMAGE alt='image' src='eq_sigs_ctss.gif']

Transform the dynamic system model to the following continuous-time state-space model.

[IMAGE alt='image' src='eq_sigs_ctss_matrix.gif']

| where | A, B, and C are matrices of this continuous-time state-space model. |
| --- | --- |
|  | ω is the rotational speed of the shaft. |
|  | U is the driving voltage. |
|  | i is the armature current. |

You must estimate the values of the *A*, *B*, and *C* matrices to identify a state-space model.

#### Using the SI Model Estimation Express VI

Complete the following steps to identify the continuous-time state-space model by using the [SI Model Estimation](../lvsysid/model_estimation_xpres.html) Express VI.

1. Add the SI Model Estimation Express VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add 
 
 The Configure SI Model Estimation dialog box appears.
2. Select the State-Space button in the Select Model Type section to identify state-space models. The Model Diagram section displays a mathematical equation for the selected model type and a diagram of the model.
3. Select the SISO button in the Select System Dims section to identify single-input single-output (SISO) dynamic models.
4. Select the Waveform button in the Select Data Type section to identify dynamic models by using waveform input signals.
5. Enter 2 in the Number of states text box because the continuous-time state-space model contains two states: rotational speed ω and armature current i .
6. Click the OK button to close the configuration dialog box and return to the block diagram.
7. Wire the stimulus signal and response signal outputs of the SI Data Samples VI to the corresponding inputs of the SI Model Estimation Express VI.
8. Add the SI Convert Discrete to Continuous Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
9. Wire the system model out output of the SI Model Estimation Express VI to the system model in input of the SI Convert Discrete to Continuous Model VI.
10. Add the SI Draw Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
11. Wire the system model out output of the SI Convert Discrete to Continuous Model VI to the system model input of the SI Draw Model VI.
12. Create an indicator for the model output of the SI Draw Model VI. The following figure shows the block diagram. 
 [IMAGE alt='image' src='noloc_bd_sigs_id_ctss_ex.gif']
13. Wire all error in and error out terminals on the block diagram.
14. Run this VI to identify the dynamic system model.

#### Using the SI Estimate State-Space Model VI

Complete the following steps to identify the continuous-time state-space model by using the [SI Estimate State-Space Model](../lvsysid/est_state_space_model.html) VI.

1. Add the SI Estimate State-Space Model VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add
2. Wire the stimulus signal and response signal outputs of the SI Data Samples VI to the corresponding inputs of the SI Estimate State-Space Model VI.
3. Create a control for the structure selector input of the SI Estimate State-Space Model VI.
4. Set all the Boolean controls of the structure selector input to FALSE because you need to estimate the A , B , and C matrices only.
5. Create a control for the number of states input of the SI Estimate State-Space Model VI.
6. Set the number of states input to 2 because the continuous-time state-space model contains two states: rotational speed ω and armature current i .
7. (Optional) Switch to the front panel, right-click all controls, and select Data Operations»Make Current Value Default from the shortcut menu. LabVIEW uses the current values as the default values for these controls.
8. Add the SI Convert Discrete to Continuous Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
9. Wire the system model out output of the SI Estimate State-Space Model VI to the system model in input of the SI Convert Discrete to Continuous Model VI.
10. Add the SI Draw Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
11. Wire the system model out output of the SI Convert Discrete to Continuous Model VI to the system model input of the SI Draw Model VI.
12. Create an indicator for the model output of the SI Draw Model VI. The following figure shows the block diagram. 
 [IMAGE alt='image' src='noloc_eps_sigs_id_ctss_bd.gif']
13. Wire all error in and error out terminals on the block diagram.
14. Run this VI to identify the dynamic system model.

#### Verifying Resulting Dynamic System Models

If you use the [SI Data Samples](../lvsysid/si_data_samples.html) VI to generate the input and output data in [Part 2](sigs_acq_data.html), LabVIEW returns the following system model:

[IMAGE alt='image' src='sigs_ctss_model.gif']

| where | A matrix is . |
| --- | --- |
|  | B matrix is . |
|  | C matrix is [–0.0480361 –0.0142187]. |
|  | e(t) is the system noise. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_mod_id_cttf.html language=enus -->
## TOPIC 00095: Identifying Continuous-Time Transfer Function Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_mod_id_cttf.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_mod_id_cttf.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Identifying Continuous-Time Transfer Function Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After [physical modeling](sigs_phys_model.html), you can describe the direct circuit (DC) servomotor by using the following differential equations:

[IMAGE alt='image' src='eq_sigs_n_k_model.gif']

If you want to design an analog proportional-integral-derivative (PID) controller, perform the [Laplace transform](/csh?topicname=lvanls/laplace_transform_real.html) on these differential equations to obtain the following equations:

[IMAGE alt='image' src='eq_sigs_ctmodel.gif']

Set *K*<sub>*i*</sub> to be equal to *K*<sub>*e*</sub> to transform these differential equations. You can transform these differential equations to the following continuous-time transfer function model:

[IMAGE alt='image' src='eq_sigs_cttf.gif']

| where | K is the electromotive force constant. |
| --- | --- |
|  | ω is the rotational speed of the shaft. |
|  | U is the driving voltage. |
|  | J is the moment of inertia of the DC servomotor. |
|  | b is the damping ratio of the mechanical part of the DC servomotor. |
|  | R is the electric resistance. |
|  | L is the inductance of circuit. |

In this example, you need to estimate the values of *K*, *JL*, (*bL+JR*), and (*bR+K*<sup>*2*</sup>) to identify the continuous-time transfer function model.

#### Using the SI Transfer Function Estimation Express VI

Complete the following steps to identify the continuous-time transfer function model by using the [SI Transfer Function Estimation](../lvsysid/est_tf_model_express.html) Express VI.

1. Add the SI Transfer Function Estimation Express VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add 
 
 The Configure SI Transfer Function Estimation dialog box appears.
2. Select the Waveform button to identify dynamic models by using waveform input signals.
3. Click the Model Settings tab.
4. Select the Continuous button to identify continuous-time transfer function models.
5. Enter 0 in the Numerator order text box because the numerator of this model is constant only.
6. Enter 2 in the Denominator order text box because the highest denominator order of the continuous-time transfer function model is s 2 .
7. Click the OK button to close the configuration dialog box and return to the block diagram.
8. Wire the stimulus signal and response signal outputs of the SI Data Samples VI to the corresponding inputs of the SI Transfer Function Estimation Express VI.
9. Add the SI Draw Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
10. Wire the system model out output of the SI Transfer Function Estimation Express VI to the system model input of the SI Draw Model VI.
11. (Optional) Create a constant for the display format for TF model input of the SI Draw Model VI and set the value to Descending .
12. Create an indicator for the model output of the SI Draw Model VI. The following figure shows the block diagram. 

 [IMAGE alt='image' src='noloc_bd_sigs_id_cttf_ex.gif']
13. Wire all error in and error out terminals on the block diagram.
14. Run this VI to identify the dynamic system model.

#### Using the SI Estimate Transfer Function Model VI

Complete the following steps to identify the continuous-time transfer function model by using the [SI Estimate Transfer Function Model](../lvsysid/est_transfer_function_model.html) VI.

1. Add the SI Estimate Transfer Function Model VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add
2. Wire the stimulus signal and response signal outputs of the SI Data Samples VI to the corresponding inputs of the SI Estimate Transfer Function Model VI.
3. Create a control for the orders of transfer function model input of the SI Estimate Transfer Function Model VI.
4. Enter 0 in the num order field of this control because the numerator of this model is constant only.
5. Enter 2 in the den order field of this control because the highest denominator order of this model is s 2 .
6. (Optional) Switch to the front panel, right-click this control, and select Data Operations»Make Current Value Default from the shortcut menu. LabVIEW uses the current value as the default value for this control.
7. Add the SI Draw Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
8. Wire the system model out output of the SI Estimate Transfer Function Model VI to the system model input of the SI Draw Model VI.
9. (Optional) Create a constant for the display format for TF model input of the SI Draw Model VI and set the value to Descending .
10. Create an indicator for the model output of the SI Draw Model VI. The following figure shows the block diagram. 
 [IMAGE alt='image' src='noloc_eps_sigs_id_cttf_bd.gif']
11. Wire all error in and error out terminals on the block diagram.
12. Run this VI to identify the dynamic system model.

#### Verifying Resulting Dynamic System Models

If you use the [SI Data Samples](../lvsysid/si_data_samples.html) VI to generate the input and output data in [Part 2](sigs_acq_data.html), LabVIEW returns the following system model:

[IMAGE alt='image' src='sigs_cttf_model.gif']

| where | K=0.000538735. |
| --- | --- |
|  | JL=3.36326E–8. |
|  | (bL+JR)=0.0658172. |
|  | (bR+K2)=1. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_mod_id_dtss.html language=enus -->
## TOPIC 00096: Identifying Discrete-Time State-Space Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_mod_id_dtss.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_mod_id_dtss.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Identifying Discrete-Time State-Space Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After [physical modeling](sigs_phys_model.html), you can describe the direct circuit (DC) servomotor by using the following differential equations:

[IMAGE alt='image' src='eq_sigs_n_k_model.gif']

Set *K*<sub>*i*</sub> to be equal to *K*<sub>*e*</sub> to transform these differential equations. If you want to design a digital state feedback controller, transform these differential equations to the following [continuous-time state-space model](sigs_mod_id_ctss.html):

[IMAGE alt='image' src='eq_sigs_ctss.gif']

You can transform the continuous-time state-space model to the following discrete-time state-space model:

[IMAGE alt='image' src='eq_sigs_dtss.gif']

| where | a00, a01, a10, a11, b0, b1, c0, c1 are unknown parameters. |
| --- | --- |
|  | ω is the rotational speed of the shaft. |
|  | U is the driving voltage. |

You must estimate the values of the *A*, *B*, and *C* matrices to identify a state-space model. In this example, you must estimate the values of *a*<sub>*00*</sub>, *a*<sub>*01*</sub>, *a*<sub>*10*</sub>, *a*<sub>*11*</sub>, *b*<sub>*0*</sub>, *b*<sub>*1*</sub>, *c*<sub>*0*</sub>, *c*<sub>*1*</sub> to identify the discrete-time state-space model.

#### Using the SI Model Estimation Express VI

Complete the following steps to identify the discrete-time state-space model by using the [SI Model Estimation](../lvsysid/model_estimation_xpres.html) Express VI.

1. Add the SI Model Estimation Express VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add 
 
 The Configure SI Model Estimation dialog box appears.
2. Select the State-Space button in the Select Model Type section to identify state-space models. The Model Diagram section displays a mathematical equation for the selected model type and a diagram of the model.
3. Select the SISO button in the Select System Dims section to identify single-input single-output (SISO) dynamic models.
4. Select the Waveform button in the Select Data Type section to identify dynamic models by using waveform input signals.
5. Enter 2 in the Number of states text box because this model contains two states: rotational speed ω and armature current i .
6. Click the OK button to close the configuration dialog box and return to the block diagram.
7. Wire the stimulus signal and response signal outputs of the SI Data Samples VI to the corresponding inputs of the SI Model Estimation Express VI.
8. Add the SI Draw Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
9. Wire the system model out output of the SI Model Estimation Express VI to the system model input of the SI Draw Model VI.
10. Create an indicator for the model output of the SI Draw Model VI. The following figure shows the block diagram. 
 [IMAGE alt='image' src='noloc_bd_sigs_id_dtss_ex.gif']
11. Wire all error in and error out terminals on the block diagram.
12. Run this VI to identify the dynamic system model.

#### Using the SI Estimate State-Space Model VI

Complete the following steps to identify the discrete-time state-space model by using the [SI Estimate State-Space Model](../lvsysid/est_state_space_model.html) VI.

1. Add the SI Estimate State-Space Model VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add
2. Wire the stimulus signal and response signal outputs of the SI Data Samples VI to the corresponding inputs of the SI Estimate State-Space Model VI.
3. Create a control for the structure selector input of the SI Estimate State-Space Model VI.
4. Set all the Boolean controls of the structure selector input to FALSE because you need to estimate the A , B , and C matrices only.
5. Create a control for the number of states input of the SI Estimate State-Space Model VI.
6. Set the number of states input to 2 because the continuous-time state-space model contains two states: rotational speed ω and armature current i .
7. (Optional) Switch to the front panel, right-click all controls, and select Data Operations»Make Current Value Default from the shortcut menu. LabVIEW uses the current values as the default values for these controls.
8. Add the SI Draw Model VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
9. Wire the system model out output of the SI Estimate State-Space Model VI to the system model input of the SI Draw Model VI.
10. Create an indicator for the model output of the SI Draw Model VI. The following figure shows the block diagram. 
 [IMAGE alt='image' src='noloc_eps_sigs_id_dtss_bd.gif']
11. Wire all error in and error out terminals on the block diagram.
12. Run this VI to identify the system model.

#### Verifying Resulting Dynamic System Models

If you use the [SI Data Samples](../lvsysid/si_data_samples.html) VI to generate the input and output data in [Part 2](sigs_acq_data.html), LabVIEW returns the following system model:

[IMAGE alt='image' src='sigs_dtss_model.gif']

| where | a00= 0.984382. |
| --- | --- |
|  | a01= 0. |
|  | a10= 0. |
|  | a11= –0.426466. |
|  | b0= –2.17452E–5. |
|  | b1= –0.000170568. |
|  | c0= –0.384289. |
|  | c1= –0.0142187. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_mod_valid.html language=enus -->
## TOPIC 00097: Part 4: Validating and Analyzing Dynamic System Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_mod_valid.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_mod_valid.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 4: Validating and Analyzing Dynamic System Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After estimating the dynamic system model, perform [model validation](validating_models.html) to test the estimated system model. Model validation verifies whether the model provides an accurate description of the dynamic system. You also can perform [model analysis](analyzing_models.html) to analyze the dynamic properties of the dynamic system model.

#### Validating Dynamic System Models

Complete the following steps to validate the system model.

1. Add the SI Model Simulation VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add
2. Wire the system model out output of the following VIs or Express VIs to the system model input of the SI Model Simulation VI.
  - SI Estimate State-Space Model VI
  - SI Estimate Transfer Function Model VI
  - SI Model Estimation Express VI
  - SI Transfer Function Estimation Express VI
3. Wire the stimulus signal output of the SI Data Samples VI to the stimulus signal input of the SI Model Simulation VI.
4. Add the Build Array function to the block diagram.
5. Wire the response signal output of the SI Data Samples VI to the element input of this function.
6. Add an input to this function node by resizing the node and wire the response output of the SI Model Simulation VI to the new element input.
7. Add a Waveform Graph indicator to the front panel. The block diagram displays a node of this indicator.
8. Right-click in this Waveform Graph and select Properties from the shortcut menu to display the Graph Properties: Waveform Graph dialog box.
9. Place a checkmark in the Show graph palette checkbox in the Appearance page.
10. Click the OK button to close this dialog box and save the configuration.
11. Switch to the block diagram and wire the appended array output of the Build Array function to this indicator. The following figure shows the block diagram.
 
 [IMAGE alt='image' src='noloc_eps_sigs_model_sim.gif']
12. Wire all error in and error out terminals on the block diagram.
13. Run this VI to generate the simulated response signal.

To validate the system model, compare the simulated response signal and the acquired response signal in the waveform graph. Use the zoom button on the graph palette to zoom in on the signals. The following figure shows the resulting waveform graph.

[IMAGE alt='image' src='sigs_model_sim_graph.gif']

Because of the friction of the DC servomotor in the start-up stage, the acquired response signals and the simulated signals deviate at the beginning of the two signals. The later parts of the simulated response signals and the acquired response signals match each other. Therefore, this dynamic system model provides an accurate description of the dynamic system.

#### Analyzing Dynamic System Models

Use model analysis to observe the model characteristics, such as [frequency response](si_frequency_response.html).

Complete the following steps to analyze the system model.

1. Add the SI Bode Plot VI to the block diagram of the VI you created . 
 [IMAGE alt='image' src='add.gif'] Add
2. Wire the system model out output of the following VIs or Express VIs to the system model input of the SI Bode Plot VI.
  - SI Estimate State-Space Model VI
  - SI Estimate Transfer Function Model VI
  - SI Model Estimation Express VI
  - SI Transfer Function Estimation Express VI
3. Add an SI Bode Plot Indicator to the front panel. The block diagram shows two indicators.
4. Wire the Bode magnitude plot and Bode phase plot outputs to the corresponding indicators. The following figure shows the block diagram.
 
 [IMAGE alt='image' src='sigs_bode_plot_bd.gif']
5. Wire all error in and error out terminals on the block diagram.
6. Run this VI to generate the bode plots of this dynamic system model.

To analyze the system model, read the magnitude and phase information from the bode plots. The following figure shows the resulting bode plots.

[IMAGE alt='image' src='sigs_bode_plot_graph.gif']

In the magnitude plot, the curve remains stable in the low frequency bands and falls slowly in the high frequency bands. In the phase plot, the curve falls near –90 degrees in the low frequency bands and falls near –180 degrees in the high frequency bands. These two plots indicate the following characteristics of this dynamic system:

- The order of this dynamic system is two.
- When the frequency is below 1000 Hz, you can treat the order of this dynamic system as one.

Use other [Model Analysis](../lvsysid/model_presentation_pal.html) VIs to analyze other characteristics of the dynamic system models, such as the [SI Nyquist Plot](../lvsysid/nyquist_plot.html) VI and the [SI Pole-Zero Plot](../lvsysid/zeros_poles_plot.html) VI.

| Previous: Identifying Dynamic System Models | Next: Converting Dynamic System Models to Control Design Models |
| --- | --- |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_model_id.html language=enus -->
## TOPIC 00098: Part 3: Identifying Dynamic System Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_model_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_model_id.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 3: Identifying Dynamic System Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Model identification, or parameter estimation, is a series of data and signal processing tasks to estimate unknown parameters and coefficients of the dynamic system model.

Before you perform model identification, you need to [preprocess](preprocessing_data.html) the acquired raw data to ensure the data is free from external noise, scaling problems, outliers, or other corruptions. Use the [Data Preprocessing](../lvsysid/data_preprocess_pal.html) VIs to preprocess the data and ensure the data accurately reflects the response of the dynamic system.

In this tutorial, the DC servomotor is a simple dynamic system. The acquired raw data is accurate enough for model identification. Therefore, you can skip preprocessing the raw data.

With the acquired time-domain data, you can perform model identification on any of the following models:

- Continuous-time transfer function model
- Continuous-time state-space model
- Discrete-time transfer function model
- Discrete-time state-space model

You also can convert the time-domain data to [frequency-domain](freq_sysid.html) data. With the converted frequency-domain data, you can identify models by using the [Frequency-Domain Model Estimation](../lvsysid/si_freqdomain_pal.html) VIs.

| Previous: Exciting the System and Acquiring Data | Next: Validating and Analyzing Dynamic System Models |
| --- | --- |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sigs_phys_model.html language=enus -->
## TOPIC 00099: Part 1: Choosing a Proper Dynamic System Model by Using Physical Modeling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sigs_phys_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sigs_phys_model.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 1: Choosing a Proper Dynamic System Model by Using Physical Modeling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Before you estimate a dynamic system, create a mathematical model that contains unknown coefficients. You then use system identification to estimate these coefficients.

Physical modeling is a common method for sketching a mathematical model that represents a real dynamic system. Physical modeling determines the nature of the model, such as the model order and the number of I/O channels. Use physical modeling to define proper models for dynamic systems.

The following figure shows an electrical circuit model of a brushed direct current (DC) servomotor.

[IMAGE alt='image' src='noloc_eps_sigs_dcmotor_graph.gif']

| where | V is the source voltage of the DC power supply. |
| --- | --- |
|  | R is the resistance of the DC servomotor armature circuit. |
|  | L is the inductance of the DC servomotor armature circuit. |
|  | i is the circuit armature current. |
|  | ω is the shaft speed of the DC servomotor. |
|  | T is the torque of the DC servomotor. |

In this dynamic system, the source voltage, *V*, is the input and the DC servomotor shaft speed, *ω*, is the output.

According to Faraday's Law of electromagnetic induction, the circuit armature current *i*, motor torque *T*, motor shaft velocity *ω*, and motor back-EMF voltage *e*, have the following relationship:

[IMAGE alt='image' src='eq_sigs_motor_te.gif']

| where | Kt is an electromotive force constant. |
| --- | --- |
|  | Ke is a motor back-EMF constant. |

You can obtain the following equations by using Newton's Law and Kirchhoff's Law.

[IMAGE alt='image' src='eq_sigs_n_k_model.gif']

| where | J is the moment of inertia of the rotor. |
| --- | --- |
|  | b is the damping ratio of the mechanical part of the DC servomotor. |

Perform further transforms on these equations to obtain a mathematic model of the dynamic system. You can choose one of the four common dynamic system models on the basis of your needs.

- Use the continuous-time transfer function model to create a model that you can use with an analog proportional-integral-derivative (PID) controller.
- Use the continuous-time state-space model to create a model that you can use with an analog state feedback controller.
- Use the discrete-time transfer function model to create a model that you can use with a digital PID controller.
- Use the discrete-time state-space model to create a model that you can use with a digital state feedback controller.

|  | Note If you perform system identification with an improper or incorrect physical model, the resulting dynamic system model may not correctly describe the behaviors of the dynamic system. |
| --- | --- |

|  | Next: Exciting the System and Acquiring Data |
| --- | --- |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sysid_concepts_intro.html language=enus -->
## TOPIC 00100: Introduction to System Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sysid_concepts_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sysid_concepts_intro.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Introduction to System Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

System identification, the first step in the [model-based control design process](model-based_cd.html), involves building mathematical models of a dynamic system based on a set of measured stimulus and response data samples. You can use system identification in a wide range of applications, including mechanical engineering, biology, physiology, meteorology, economics, and model-based control design. For example, engineers use a system model of the relationship between the fuel flow and the shaft speed of a turbojet engine to optimize the efficiency and operational stability of the engine. Biologists and physiologists use system identification techniques in areas such as eye pupil response and heart rate control. Meteorologists and economists build mathematical models based on historical data for use in forecasting.

The LabVIEW Advanced Signal Processing Toolkit and the LabVIEW Control Design and Simulation Module provide the following tools.

#### System Identification VIs

You can use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to preprocess raw data from a dynamic system and develop a model that reflects the behavior of that system. The [Data Preprocessing](../lvsysid/data_preprocess_pal.html) VIs enable you to analyze the response of a dynamic system to a certain stimulus. After analyzing the data, you can use the [Parametric Model Estimation](../lvsysid/parametric_estimation_pal.html), [Nonparametric Model Estimation](../lvsysid/nonparametric_est_pal.html), [Partially Known Model Estimation](../lvsysid/pk_mdl_est_pal.html), [Recursive Model Estimation](../lvsysid/recursive_model_est_pal.html), and/or [Frequency-Domain Model Estimation](../lvsysid/si_freqdomain_pal.html) VIs to estimate a model for the dynamic system. You can use the [Model Validation](../lvsysid/model_validation_palette.html) or [Model Analysis](../lvsysid/model_presentation_pal.html) VIs to determine whether the model accurately describes the dynamics of the identified system. You also can use the [Model Conversion](../lvsysid/model_conversion_pal.html) VIs to convert a model from one type to another. Finally, you can use the [SI Convert to Models of CDT](../lvsysid/convert_to_models_cdt.html) VI to convert the model you identified to a model that you can use in the LabVIEW Control Design and Simulation Module.

The System Identification VIs enable you to customize a LabVIEW block diagram to achieve specific goals. You also can use other LabVIEW VIs and functions to enhance the functionality of the application. Creating a LabVIEW application using the System Identification VIs requires basic knowledge about programming in LabVIEW. Refer to the Getting Started with LabVIEW manual for more information about the LabVIEW programming environment.

The following case studies demonstrate how to use the System Identification VIs to estimate different [model representations](model_types_and_reps.html#model_reps) by using time-domain or frequency domain data.

- Flexible Arm Case Study —Guides you through the entire system identification process. This case study demonstrates how to preprocess time-domain data from a dynamic system, estimate an ARX and state-space model by using the time-domain data, and validate the models to ensure they accurately reflect the dynamic system.
- Partially Known Model Estimation Case Study —Demonstrates how to estimate a state-space model by using prior knowledge about the system you want to define.
- Frequency-Domain Model Estimation Case Study —Demonstrates how to estimate and validate a state-space and transfer function model by using frequency-domain data from a dynamic system.

#### System Identification Assistant

If you do not have prior knowledge about programming in LabVIEW, you can use the System Identification Assistant to develop a model that reflects the behavior of a certain dynamic system. You access the System Identification Assistant by launching LabVIEW and selecting **Tools»Control Design and Simulation»Launch System Identification Assistant**.

Using the System Identification Assistant, you can create a project that encompasses the whole system identification process. In a single project, you can load or acquire raw data into the System Identification Assistant, preprocess the data, estimate a model that describes the system, and then validate the accuracy of the model. SignalExpress provides windows in which you can see the raw data, the response data, the estimated model, the validation results, and the mathematical equations that describe the model.

After creating a project in SignalExpress, you can convert the project to a LabVIEW block diagram and customize the block diagram in LabVIEW. This conversion enables you to enhance the capabilities of the application. Refer to the *SignalExpress Help*, available in the SignalExpress environment by selecting **Help»SignalExpress Help**, for more information about using the assistant to develop models.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvsysidconcepts/sysid_gsd.html language=enus -->
## TOPIC 00101: Getting Started with System Identification

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvsysidconcepts/sysid_gsd.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvsysidconcepts/sysid_gsd.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Getting Started with System Identification

System identification is a series of processes for building the [mathematical models](../lvsysidconcepts/estimating_models.html) of a dynamic system by using the stimulus and response data of the dynamic system. A direct current (DC) servomotor is a typical example of dynamic systems. A DC servomotor generates rotation motion through the magnetic interaction between a current-carrying conductor and an external magnetic field.

A DC servomotor is a common actuator in a control system. To estimate the model of a DC servomotor, you need to create a model that contains unknown coefficients according to the application requirements. For example, if you plan to create a model that you can use with a proportional-integral-derivative controller for a DC servomotor, you can create the following [transfer function](modeldefinitionstf.html) model, *G*(*s*), for the measured rotational speed of the shaft, *ω*, and the driving voltage, *U*, of the DC servomotor.

[IMAGE alt='image' src='eq_dcsvmotor.gif']

Perform system identification on the previous transfer function model to estimate the coefficients, *b*<sub>*0*</sub>, *a*<sub>*0*</sub>, *a*<sub>*1*</sub>, and *a*<sub>*2*</sub>, of the transfer function, on the basis of the measured rotational speed, *ω*, and driving voltage, *U*.

The following figure shows the processes of identifying the model of a DC servomotor.

[IMAGE alt='image' src='noloc_eps_sigs_diagram.gif']

Read through the following topics to perform system identification on a DC servomotor by using the [System Identification](../lvsysid/lv_sysid_pal.html) VIs.

- Choosing a proper dynamic system model by using physical modeling
- Exciting the system and acquiring data
- Identifying dynamic system models
- Validating and analyzing dynamic system models
- Converting dynamic system models to control design models

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimefreqtk/dual_window.html language=enus -->
## TOPIC 00102: Dual Window Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimefreqtk/dual_window.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimefreqtk/dual_window.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Dual Window Express VI

**Owning Palette:** [Time Frequency Transform VIs](../lvtimefreqtk/tftranspal.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the dual windows for the Gabor transform and the Gabor expansion.

[Details](#details)  [Examples](#examples)

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Dual Window | Displays the analysis window and the synthesis window. You can use the analysis window and the synthesis window for the Gabor transform and the Gabor expansion, respectively. To characterize the local time and frequency properties of a signal in the joint time-frequency domain accurately, adjust the Synthesis Window Info and the Transform Info so that the analysis window and the synthesis window match as closely as possible. |
| Synthesis Window Info | Contains the following options: Window type—Specifies the type of envelope window of the Gabor elementary functions. Options include: Gaussian (default) Low Sidelobe 7 Term B-Harris 4 Term B-Harris Flat Top Blackman Exact Blackman Blackman-Harris Hamming Hanning Optimal variance—Specifies to compute the variance of the Gaussian window automatically. When Optimal variance is TRUE, this VI sets the variance as the optimal value, which is equal to N (frequency bins)×dM (time steps)/(2). This control is available only when Window type is Gaussian. Window length—Specifies the window length, in samples, of the Gabor elementary functions. This VI sets Window length to a power of 2 automatically. Variance—Specifies the variance, in square samples, of the Gaussian window. This control is available only when Window type is Gaussian and you remove the checkmark from the Optimal variance checkbox. |
| Transform Info | Contains the following options: dM (time steps)—Specifies the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. This VI sets dM (time steps) to a power of 2 and less than or equal to N (frequency bins) automatically. You also can consider dM (time steps) as the sampling period along the time axis in the joint time-frequency domain. N (frequency bins)—Specifies the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. This VI sets N (frequency bins) to a power of 2 and greater than or equal to dM (time steps). The ratio between N (frequency bins) and dM (time steps) is called the oversampling rate. You also can consider N (frequency bins) as the number of bins to sample the signal along the frequency axis in the joint time-frequency domain. |
| Data length equals window length | Specifies if the lengths of the window function and the signal are equal. When the window length is equal to the signal length, the chance of obtaining the corresponding dual function is higher. |
| Sampling Grid | Displays the Gabor sampling lattice in the joint time-frequency domain. Zoom out—Zooms out the sampling plot grid. Zoom in—Zooms in the sampling plot grid. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| error out | Contains error information. This output provides standard error out functionality. |
| synthesis info | Returns the Gabor elementary functions for the Gabor expansion. synthesis window—Contains the window of the Gabor elementary functions. The size of synthesis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps)—Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins)—Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. For stable reconstruction, N (frequency bins) must be greater than or equal to dM (time steps). The ratio between N (frequency bins) and dM (time steps) is called the oversampling rate. |
| analysis info | Returns the analysis window for the Gabor transform. analysis window—Contains the window this VI used to compute the Gabor coefficients. analysis window is the dual window of the synthesis window, which is the envelope of the Gabor elementary functions. The size of analysis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps)—Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins)—Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. For stable reconstruction, N (frequency bins) must be greater than or equal to dM (time steps). The ratio between N (frequency bins) and dM (time steps) is called the oversampling rate. |

#### Dual Window Details

The [synthesis window](../lvasptconcepts/tfa_discrete_gabor_trans_exp.html#synthesis_window) is the envelope window of the Gabor elementary functions. The [dual window](../lvasptconcepts/tfa_discrete_gabor_trans_exp.html#synthesis_window) of the synthesis window is called the [analysis window](../lvasptconcepts/tfa_discrete_gabor_trans_exp.html#synthesis_window), which this VI uses in the Gabor transform to compute the complex weight of the Gabor elementary functions. You can use the resulting **analysis info** and **synthesis info** for the Gabor transform and the Gabor expansion, respectively.

This Express VI operates similarly to the following VIs and functions:

[TFA Dual Window](../lvtimefreqtk/tfa_dual_window.html)

#### Examples

Refer to the following VIs for examples of using the Dual Window Express VI:

- Online Noise Reduction VI: labview\examples\Time Frequency Analysis\TFAApplications
- Dual Function VI: labview\examples\Time Frequency Analysis\TFAGettingStarted
- Gabor Transform and Expansion VI: labview\examples\Time Frequency Analysis\TFAFunctions

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimefreqtk/lvtimefreqtk.html language=enus -->
## TOPIC 00103: Time Frequency Analysis VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimefreqtk/lvtimefreqtk.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimefreqtk/lvtimefreqtk.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Frequency Analysis VIs

June 2013, 371419E-01

**Requires:** Advanced Signal Processing Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Time Frequency Analysis VIs to transform a time-domain signal to a joint time-frequency domain representation. You can extract useful information from the time-frequency domain representation of a signal, or you can process a time-frequency domain representation and reconstruct a time-domain signal.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Time Frequency Analysis error codes](tfa_error_codes.html).

| Subpalette | Description |
| --- | --- |
| Feature Extraction VIs | Use the Feature Extraction VIs to extract useful information from the quadratic time-frequency representation of signals. |
| Online JTFA VIs | Use the Online JTFA VIs to perform time-frequency type calculations continuously. |
| Time Frequency Spectrogram VIs | Use the Time Frequency Spectrogram VIs to compute the quadratic energy distribution of the signal in the joint time-frequency domain. |
| Time Frequency Transform VIs | Use the Time Frequency Transform VIs to decompose signals as linear combinations of elementary functions. The elementary functions are localized in time and frequency. You also can reconstruct the signal from the elementary functions. |
| Utilities VIs | Use the Utilities VIs to generate signals for demonstration purposes or to access scale information in the time-frequency representation. |

© 2005–2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimefreqtk/tfa_adaptive_expansion.html language=enus -->
## TOPIC 00104: TFA Adaptive Expansion VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimefreqtk/tfa_adaptive_expansion.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimefreqtk/tfa_adaptive_expansion.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TFA Adaptive Expansion VI

**Owning Palette:** [Time Frequency Transform VIs](../lvtimefreqtk/tftranspal.html)

**Requires:** Advanced Signal Processing Toolkit

Reconstructs a signal from the Gaussian chirplet [elementary functions](../lvasptconcepts/tfa_gaussian_chirplet_pulse.html). Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### TFA Adaptive Expansion (Waveform)

[IMAGE alt='image' src='tfa_adaptive_expansion_(waveform)c.gif']

|  | sampling info specifies the sampling information of the reconstructed signal. sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. length specifies the length, in samples, of the reconstructed signal. The default is –1, which specifies that length equals the largest value of center + 4×standard deviation. |
| --- | --- |
|  | sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. |
|  | length specifies the length, in samples, of the reconstructed signal. The default is –1, which specifies that length equals the largest value of center + 4×standard deviation. |
|  | chirplet info specifies the parameters of each elementary function. amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. standard deviation specifies the standard deviation of the Gaussian envelope in seconds. center specifies the central time of the Gaussian envelope in seconds. frequency specifies the central frequency of the chirplet in hertz. chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |
|  | amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. |
|  | standard deviation specifies the standard deviation of the Gaussian envelope in seconds. |
|  | center specifies the central time of the Gaussian envelope in seconds. |
|  | frequency specifies the central frequency of the chirplet in hertz. |
|  | chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | signal returns the reconstructed signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Adaptive Expansion (Real)

[IMAGE alt='image' src='tfa_adaptive_expansion_(real)c.gif']

|  | sampling info specifies the sampling information of the reconstructed signal. sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. length specifies the length, in samples, of the reconstructed signal. The default is –1, which specifies that length equals the largest value of center + 4×standard deviation. |
| --- | --- |
|  | sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. |
|  | length specifies the length, in samples, of the reconstructed signal. The default is –1, which specifies that length equals the largest value of center + 4×standard deviation. |
|  | chirplet info specifies the parameters of each elementary function. amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. standard deviation specifies the standard deviation of the Gaussian envelope in seconds. center specifies the central time of the Gaussian envelope in seconds. frequency specifies the central frequency of the chirplet in hertz. chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |
|  | amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. |
|  | standard deviation specifies the standard deviation of the Gaussian envelope in seconds. |
|  | center specifies the central time of the Gaussian envelope in seconds. |
|  | frequency specifies the central frequency of the chirplet in hertz. |
|  | chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | signal returns the reconstructed signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Adaptive Expansion (Complex)

[IMAGE alt='image' src='tfa_adaptive_expansion_(complex)c.gif']

|  | sampling info specifies the sampling information of the reconstructed signal. sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. length specifies the length, in samples, of the reconstructed signal. The default is –1, which specifies that length equals the largest value of center + 4×standard deviation. |
| --- | --- |
|  | sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. |
|  | length specifies the length, in samples, of the reconstructed signal. The default is –1, which specifies that length equals the largest value of center + 4×standard deviation. |
|  | chirplet info specifies the parameters of each elementary function. amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. standard deviation specifies the standard deviation of the Gaussian envelope in seconds. center specifies the central time of the Gaussian envelope in seconds. frequency specifies the central frequency of the chirplet in hertz. chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |
|  | amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. |
|  | standard deviation specifies the standard deviation of the Gaussian envelope in seconds. |
|  | center specifies the central time of the Gaussian envelope in seconds. |
|  | frequency specifies the central frequency of the chirplet in hertz. |
|  | chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | signal returns the reconstructed signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Adaptive Transform (ADT) and Adaptive Expansion (ADE) VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Adaptive Expansion VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimefreqtk/tfa_adaptive_spectrogram.html language=enus -->
## TOPIC 00105: TFA Adaptive Spectrogram VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimefreqtk/tfa_adaptive_spectrogram.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimefreqtk/tfa_adaptive_spectrogram.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TFA Adaptive Spectrogram VI

**Owning Palette:** [Time Frequency Spectrogram VIs](../lvtimefreqtk/tfspectpal.html)

**Requires:** Advanced Signal Processing Toolkit

Decomposes the signal into a linear combination of Gaussian chirplet [elementary functions](../lvasptconcepts/tfa_adapt_trans_exp.html) and sums the [Wigner-Ville Distribution (WVD)](../lvasptconcepts/tfa_wvd.html) of all the Gaussian chirplet elementary functions to compute the quadratic time-frequency representation of **signal**. Use this VI if the signal contains Gaussian chirps. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### TFA Adaptive Spectrogram (Waveform)

[IMAGE alt='image' src='tfa_adaptive_spectrogram_(waveform)c.gif']

|  | zoom settings specifies the frequency zoom factor and the zoom range. zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. The larger the zoom factor, the more the detail in the spectrogram you can see. f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals –fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is –1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factor×frequency bins for real-valued input signals and must not be greater than zoom factor×frequency bins for complex-valued input signals. |
| --- | --- |
|  | zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. The larger the zoom factor, the more the detail in the spectrogram you can see. |
|  | f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals –fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. |
|  | number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is –1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factor×frequency bins for real-valued input signals and must not be greater than zoom factor×frequency bins for complex-valued input signals. |
|  | extension specifies the method to use to pad data at the borders of the input signal to lessen discontinuity. The extension length is half the window length. 0Zero padding (default)—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| 0 | Zero padding (default)—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the input signal. |
|  | time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. |
|  | frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | number of terms specifies the maximum number of elementary functions to use in the adaptive representation. Using more elementary functions improves the accuracy of the representation but increases computation time. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | elementary functions specifies the settings of the elementary functions. type specifies the type of elementary function to use to represent the signal. 0Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet.1Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. max window length specifies the maximum window length of the Gaussian envelopes of the elementary functions. The default is –1, which specifies that this VI sets the maximum window length as the power of 2 that is closest to but less than the signal length. The value of max window length must be a power of 2. If the value of max window length is not a power of 2, this VI sets the value to a power of 2 automatically. Use the default setting if the size of the input signal is not greater than 1,000,000. reserved is reserved for future use. |
|  | type specifies the type of elementary function to use to represent the signal. 0Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet.1Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. |
| 0 | Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet. |
| 1 | Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. |
|  | max window length specifies the maximum window length of the Gaussian envelopes of the elementary functions. The default is –1, which specifies that this VI sets the maximum window length as the power of 2 that is closest to but less than the signal length. The value of max window length must be a power of 2. If the value of max window length is not a power of 2, this VI sets the value to a power of 2 automatically. Use the default setting if the size of the input signal is not greater than 1,000,000. |
|  | reserved is reserved for future use. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | reconstructed signal returns the signal reconstructed from the detected elementary functions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Adaptive Spectrogram (Real)

[IMAGE alt='image' src='tfa_adaptive_spectrogram_(real)c.gif']

|  | zoom settings specifies the frequency zoom factor and the zoom range. zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. The larger the zoom factor, the more the detail in the spectrogram you can see. f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals –fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is –1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factor×frequency bins for real-valued input signals and must not be greater than zoom factor×frequency bins for complex-valued input signals. |
| --- | --- |
|  | zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. The larger the zoom factor, the more the detail in the spectrogram you can see. |
|  | f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals –fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. |
|  | number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is –1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factor×frequency bins for real-valued input signals and must not be greater than zoom factor×frequency bins for complex-valued input signals. |
|  | extension specifies the method to use to pad data at the borders of the input signal to lessen discontinuity. The extension length is half the window length. 0Zero padding (default)—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| 0 | Zero padding (default)—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the input signal. |
|  | time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. |
|  | frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | number of terms specifies the maximum number of elementary functions to use in the adaptive representation. Using more elementary functions improves the accuracy of the representation but increases computation time. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | elementary functions specifies the settings of the elementary functions. type specifies the type of elementary function to use to represent the signal. 0Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet.1Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. max window length specifies the maximum window length of the Gaussian envelopes of the elementary functions. The default is –1, which specifies that this VI sets the maximum window length as the power of 2 that is closest to but less than the signal length. The value of max window length must be a power of 2. If the value of max window length is not a power of 2, this VI sets the value to a power of 2 automatically. Use the default setting if the size of the input signal is not greater than 1,000,000. reserved is reserved for future use. |
|  | type specifies the type of elementary function to use to represent the signal. 0Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet.1Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. |
| 0 | Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet. |
| 1 | Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. |
|  | max window length specifies the maximum window length of the Gaussian envelopes of the elementary functions. The default is –1, which specifies that this VI sets the maximum window length as the power of 2 that is closest to but less than the signal length. The value of max window length must be a power of 2. If the value of max window length is not a power of 2, this VI sets the value to a power of 2 automatically. Use the default setting if the size of the input signal is not greater than 1,000,000. |
|  | reserved is reserved for future use. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | reconstructed signal returns the signal reconstructed from the specified elementary functions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Adaptive Spectrogram (Complex)

[IMAGE alt='image' src='tfa_adaptive_spectrogram_(complex)c.gif']

|  | zoom settings specifies the frequency zoom factor and the zoom range. zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. The larger the zoom factor, the more the detail in the spectrogram you can see. f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals –fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is –1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factor×frequency bins for real-valued input signals and must not be greater than zoom factor×frequency bins for complex-valued input signals. |
| --- | --- |
|  | zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. The larger the zoom factor, the more the detail in the spectrogram you can see. |
|  | f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals –fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. |
|  | number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is –1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factor×frequency bins for real-valued input signals and must not be greater than zoom factor×frequency bins for complex-valued input signals. |
|  | extension specifies the method to use to pad data at the borders of the input signal to lessen discontinuity. The extension length is half the window length. 0Zero padding (default)—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| 0 | Zero padding (default)—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the input signal. |
|  | time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. |
|  | frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | number of terms specifies the maximum number of elementary functions to use in the adaptive representation. Using more elementary functions improves the accuracy of the representation but increases computation time. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | elementary functions specifies the settings of the elementary functions. type specifies the type of elementary function to use to represent the signal. 0Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet.1Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. max window length specifies the maximum window length of the Gaussian envelopes of the elementary functions. The default is –1, which specifies that this VI sets the maximum window length as the power of 2 that is closest to but less than the signal length. The value of max window length must be a power of 2. If the value of max window length is not a power of 2, this VI sets the value to a power of 2 automatically. Use the default setting if the size of the input signal is not greater than 1,000,000. reserved is reserved for future use. |
|  | type specifies the type of elementary function to use to represent the signal. 0Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet.1Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. |
| 0 | Gaussian chirplet (default)—Specifies that the elementary function is the Gaussian chirplet. |
| 1 | Gaussian pulse—Specifies that the elementary function is the Gaussian pulse. |
|  | max window length specifies the maximum window length of the Gaussian envelopes of the elementary functions. The default is –1, which specifies that this VI sets the maximum window length as the power of 2 that is closest to but less than the signal length. The value of max window length must be a power of 2. If the value of max window length is not a power of 2, this VI sets the value to a power of 2 automatically. Use the default setting if the size of the input signal is not greater than 1,000,000. |
|  | reserved is reserved for future use. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | reconstructed signal returns the signal reconstructed from the specified elementary functions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Adaptive Spectrogram Details

You can [combine a series of Gaussian chirplets to approximate a signal](../lvasptconcepts/tfa_gaussian_chirplet_pulse.html), *s(t)*. The [adaptive spectrogram](../lvasptconcepts/aspt_adaptive_spectrogram.html) is the summation of the weighted WVD of each Gaussian chirplet. The adaptive spectrogram does not contain cross-term interference. Because the WVD of the Gaussian function is nonnegative, the adaptive spectrogram is also nonnegative. Use the adaptive spectrogram if a set of Gaussian chirplets can represent the signal.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimefreqtk/tfa_cohen.html language=enus -->
## TOPIC 00106: TFA Cohen VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimefreqtk/tfa_cohen.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimefreqtk/tfa_cohen.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TFA Cohen VI

**Owning Palette:** [Time Frequency Spectrogram VIs](../lvtimefreqtk/tfspectpal.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the [Cohen's class time-frequency distribution](../lvasptconcepts/tfa_cwd_csd.html) of **signal**. **kernel** controls the properties of the resulting spectrogram. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### TFA Cohen (Waveform)

[IMAGE alt='image' src='tfa_cohen_(waveform)c.gif']

|  | signal specifies the input signal. |
| --- | --- |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory. National Instruments recommends that you set time steps so that the number of rows in spectrogram does not exceed 512. If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment or downsample the signal if it is oversampled. The scale info output contains the actual sampling period in seconds along the time axis. |
|  | kernel specifies the upper half of a user-defined 2D kernel function. The number of rows in kernel determines the number of frequency bins, or the number of columns, in the resulting spectrogram. The number of rows in kernel must be a power of 2. The number of columns in kernel must be 2^(ceil(log2(Ls – 1))), where Ls is the length of signal. For a kernel function Phi(, ), is associated with the row direction of kernel, and is associated with the column direction. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analytic signal? specifies whether to convert the real input signal to the corresponding analytic signal. The default is TRUE. The analytic signal has no negative frequency components and has the same positive frequency components as the original signal. Converting the real input signal to the analytic signal can suppress the cross-term interference between the positive frequency components and the negative frequency components. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Cohen (Real)

[IMAGE alt='image' src='tfa_cohen_(real)c.gif']

|  | signal specifies the input signal. |
| --- | --- |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory. National Instruments recommends that you set time steps so that the number of rows in spectrogram does not exceed 512. If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment or downsample the signal if it is oversampled. The scale info output contains the actual sampling period in seconds along the time axis. |
|  | kernel specifies the upper half of a user-defined 2D kernel function. The number of rows in kernel determines the number of frequency bins, or the number of columns, in the resulting spectrogram. The number of rows in kernel must be a power of 2. The number of columns in kernel must be 2^(ceil(log2(Ls – 1))), where Ls is the length of signal. For a kernel function Phi(, ), is associated with the row direction of kernel, and is associated with the column direction. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analytic signal? specifies whether to convert the real input signal to the corresponding analytic signal. The default is TRUE. The analytic signal has no negative frequency components and has the same positive frequency components as the original signal. Converting the real input signal to the analytic signal can suppress the cross-term interference between the positive frequency components and the negative frequency components. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Cohen (Complex)

[IMAGE alt='image' src='tfa_cohen_(complex)c.gif']

|  | signal specifies the input signal. |
| --- | --- |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory. National Instruments recommends that you set time steps so that the number of rows in spectrogram does not exceed 512. If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment or downsample the signal if it is oversampled. The scale info output contains the actual sampling period in seconds along the time axis. |
|  | kernel specifies the upper half of a user-defined 2D kernel function. The number of rows in kernel determines the number of frequency bins, or the number of columns, in the resulting spectrogram. The number of rows in kernel must be a power of 2. The number of columns in kernel must be 2^(ceil(log2(Ls – 1))), where Ls is the length of signal. For a kernel function Phi(, ), is associated with the row direction of kernel, and is associated with the column direction. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Cohen Details

For large values of the signal length, this VI requires a long computation time and more memory. National Instruments recommends that you limit **signal** to 15,000 samples.

#### Cohen's Class Time Frequency Distribution

To suppress the cross-term interference in the [Wigner-Ville Distribution (WVD)](../lvasptconcepts/tfa_wvd.html), Leon Cohen proposed a general framework of time-frequency distributions. You can derive most of the quadratic JTFA methods from the Cohen's class time-frequency distributions. The [short-time Fourier transform (STFT) spectrogram](../lvasptconcepts/aspt_stft_spectrogram.html) and the WVD are two extreme cases in Cohen's class.

The following equations define the Cohen's class time-frequency distribution of signal *s(t)*:

[IMAGE alt='image' src='eq_cohen_1.gif']

[IMAGE alt='image' src='eq_cohen_2.gif']

where [IMAGE alt='image' src='eq_cohen_ambiguity.gif'] is the ambiguity function of the input signal, [IMAGE alt='image' src='eq_kernel.gif'] is the kernel function for smoothing the cross-term interference, and [IMAGE alt='image' src='eq_time_dep_autocorr.gif'] is the time-dependent auto-correlation function of the input signal. When [IMAGE alt='image' src='eq_cohen_w_v.gif'], the Cohen's distribution is degraded into the WVD. When the kernel is the ambiguity function of a window used in the STFT, the resulting time-frequency distribution is the STFT spectrogram.

Complete the following steps to compute the Cohen's class time-frequency distribution.

1. Apply the fast Fourier transform (FFT) to the time-dependent auto-correlation function along the t –axis to compute the ambiguity function.
2. Multiply the kernel function with the ambiguity function and perform the inverse FFT on the kernel-truncated ambiguity function along the –axis. You can consider the resulting function as the smoothed time-dependent auto-correlation function.
3. Apply the FFT to the smoothed time-dependent auto-correlation function along the –axis.

The following table outlines some general kernel functions:

| Name | Kernel | Kernel Plot |
| --- | --- | --- |
| Born-Jordan (BJD) |  |  |
| Choi-Williams (CWD) |  |  |
| Cone-shape (CSD) |  |  |

You can use the kernel plot to investigate the ability of each kernel function to suppress cross-term interference. The [IMAGE alt='image' src='eq_axis2.gif']–axis indicates the central time difference between any two signal components, and the [IMAGE alt='image' src='eq_axis1.gif']–axis indicates the central frequency difference. If the kernel function decays rapidly along the [IMAGE alt='image' src='eq_axis2.gif']–axis, the kernel function can suppress cross-term interference from signal components with a large central time difference. If the kernel function decays rapidly along the [IMAGE alt='image' src='eq_axis1.gif']–axis, the kernel function can suppress cross-term interference from signal components with different central frequencies.

The kernel function you select in real applications depends on the property of the input signals. The CSD is a common first choice for the evaluation of different time-frequency distributions in real applications.

Refer to the book [Introduction to Time-Frequency and Wavelet Transforms](../lvasptconcepts/aspt_related_doc.html) for more information about Cohen's class time-frequency distributions.

#### Example

Refer to the Pseudo Wigner-Ville Distribution VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Cohen VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimefreqtk/tfa_cone_shaped_distribution.html language=enus -->
## TOPIC 00107: TFA Cone-Shaped Distribution VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimefreqtk/tfa_cone_shaped_distribution.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimefreqtk/tfa_cone_shaped_distribution.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TFA Cone-Shaped Distribution VI

**Owning Palette:** [Time Frequency Spectrogram VIs](../lvtimefreqtk/tfspectpal.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the [Cone-Shaped Distribution (CSD)](../lvasptconcepts/tfa_cwd_csd.html#cone-shaped_distribution) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### TFA Cone-Shaped Distribution (Waveform)

[IMAGE alt='image' src='tfa_cone_shaped_distribution_(waveform)c.gif']

|  | signal specifies the input signal. |
| --- | --- |
|  | time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. |
|  | frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | alpha specifies the relationship between resolution and cross-term interference. alpha must be greater than or equal to 0. Increasing alpha better suppresses cross-term interference but reduces the time-frequency resolution. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analytic signal? specifies whether to convert the real input signal to the corresponding analytic signal. The default is TRUE. The analytic signal has no negative frequency components and has the same positive frequency components as the original signal. Converting the real input signal to the analytic signal can suppress the cross-term interference between the positive frequency components and the negative frequency components. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Cone-Shaped Distribution (Real)

[IMAGE alt='image' src='tfa_cone_shaped_distribution_(real)c.gif']

|  | signal specifies the input signal. |
| --- | --- |
|  | time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. |
|  | frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | alpha specifies the relationship between resolution and cross-term interference. alpha must be greater than or equal to 0. Increasing alpha better suppresses cross-term interference but reduces the time-frequency resolution. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analytic signal? specifies whether to convert the real input signal to the corresponding analytic signal. The default is TRUE. The analytic signal has no negative frequency components and has the same positive frequency components as the original signal. Converting the real input signal to the analytic signal can suppress the cross-term interference between the positive frequency components and the negative frequency components. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Cone-Shaped Distribution (Complex)

[IMAGE alt='image' src='tfa_cone_shaped_distribution_(complex)c.gif']

|  | signal specifies the input signal. |
| --- | --- |
|  | time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. The number of rows in spectrogram equals the signal length divided by time steps.National Instruments recommends that you set time steps such that the number of rows in spectrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large spectrogram, which requires a long computation time and more memory.If you need a small sampling period to observe more details and the signal length is large, divide the signal into smaller segments and compute the spectrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis. |
|  | frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
|  | alpha specifies the relationship between resolution and cross-term interference. alpha must be greater than or equal to 0. Increasing alpha better suppresses cross-term interference but reduces the time-frequency resolution. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. Use the TFA Spectrogram Indicator to display the spectrogram on an intensity graph. You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the TFA Get Time and Freq Scale Info VI to compute the time scale information and the frequency scale information of the time-frequency representation. |
|  | scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TFA Cone-Shaped Distribution Details

CSD is a type of [Cohen's class distribution](../lvasptconcepts/tfa_cwd_csd.html) and is the smooth version of the [Wigner-Ville Distribution (WVD)](../lvasptconcepts/tfa_wvd.html). CSD has better readability than WVD but worse time-frequency resolution, because CSD suppresses the cross-term interference between two signal components that have a large difference in [central time](../lvasptconcepts/tfa_central_time_frequency.html) or [central frequency](../lvasptconcepts/tfa_central_time_frequency.html). However, CSD does not suppress the cross-term interference between two signal components that have the same central time. Therefore, for large values of the signal length, this VI requires a long computation time and more memory. National Instruments recommends that you limit **signal** to 15,000 samples.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_error_code.html language=enus -->
## TOPIC 00108: Error Codes (Time Series Analysis Tools)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_error_code.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_error_code.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Time Series Analysis Tools)

The [Time Series Analysis](time_series_analysis_pal.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −42461 | The dimension of the scale info parameter does not match the dimension of the multivariate time series. |
| −42454 | The noise variance must be greater than zero or the noise covariance matrix is invalid. |
| −42453 | The first element of the model coefficients array must be 1, and the size of the array must be greater than or equal to 1. |
| −42452 | The number of predicted points must be greater than 0. |
| −42451 | The value of the model order is less than the value of the required order. |
| −42442 | The number of cepstrum bins must be greater than 0. |
| −42441 | The subspace dimension must be greater than 0 and less than 100 in percentage. |
| −42430 | The reference value is invalid. |
| −42429 | The number of subsequences into which to divide the input series must be greater than 0. |
| −42428 | The percentage must be greater than or equal to 0 and less than 100. |
| −42427 | The size of the time point array does not match the size of the value array in the unequally-sampled time series. |
| −42426 | The length of seasonal pattern in time series must be greater than 0. |
| −42425 | The degree of freedom defining the distribution must be greater than 0. |
| −42424 | The value of upper endpoint must be greater than the value of lower endpoint. |
| −42423 | The input parameters do not match the dimension of multivariate time series. |
| −42422 | The number of samples must be greater than 0. |
| −42421 | The input standard deviation must be greater than 0. |
| −42407 | The input time series is too large for memory. You can downsample the input time series, modify the window length, or trim the input time series to reduce memory consumption. |
| −42406 | All the values of input time series must be positive numbers. |
| −42405 | The input time series is empty or the length of the input time series must be greater than the required length. |
| −42404 | This file operation does not support the LabVIEW Real-Time Module. |
| −42403 | The number of frequency bins must be greater than 0. |
| −42402 | The sampling rate must be greater than 0. |
| −42401 | The size of the color table must equal 256. |
| 42421 | Cannot estimate more independent components than specified. |
| 42422 | The number of frequency bins has changed. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_exponential_average.html language=enus -->
## TOPIC 00109: TSA Exponential Average VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_exponential_average.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_exponential_average.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Exponential Average VI

**Owning Palette:** [Preprocessing VIs](../lvtimeseriestk/tsa_preprocess_vi.html)

**Requires:** Advanced Signal Processing Toolkit

Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a [smoothed time series](../lvasptconcepts/tsa_preprocess.html#smoothing_a_time_series). Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### TSA Exponential Average (Waveform)

[IMAGE alt='image' src='tsa_exponential_average_(waveform)c.gif']

|  | Xt specifies the univariate time series. |
| --- | --- |
|  | exponential type specifies the type of exponential average. Options include Single, Double, and Triple. The default is Single. Refer to the Details section for more information about each exponential type. |
|  | exponential factors specifies the weighting factors for exponential smoothing. level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | level specifies the weight for the level cumulant. The value must be a number between 0 and 1. |
|  | trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. |
|  | season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | season period specifies the length of the seasonal pattern in the input time series. The default is 1. This option is available only when exponential type is Triple. |
|  | season type specifies the way in which this VI models the seasonality. This option is available only when exponential type is Triple. Refer to the Details section for more information about each season type. 0Multiplicative (default)—Indicates that the time series has a seasonality with the amplitude increasing over time.1Additive—Indicates that the time series has a constant amplitude change in seasonality. |
| 0 | Multiplicative (default)—Indicates that the time series has a seasonality with the amplitude increasing over time. |
| 1 | Additive—Indicates that the time series has a constant amplitude change in seasonality. |
|  | Xt averaged returns the averaged univariate time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Exponential Average (Array)

[IMAGE alt='image' src='tsa_exponential_average_(array)c.gif']

|  | Xt specifies the univariate time series. |
| --- | --- |
|  | exponential type specifies the type of exponential average. Options include Single, Double, and Triple. The default is Single. Refer to the Details section for more information about each exponential type. |
|  | exponential factors specifies the weighting factors for exponential smoothing. level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | level specifies the weight for the level cumulant. The value must be a number between 0 and 1. |
|  | trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. |
|  | season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | season period specifies the length of the seasonal pattern in the input time series. The default is 1. This option is available only when exponential type is Triple. |
|  | season type specifies the way in which this VI models the seasonality. This option is available only when exponential type is Triple. Refer to the Details section for more information about each season type. 0Multiplicative (default)—Indicates that the time series has a seasonality with the amplitude increasing over time.1Additive—Indicates that the time series has a constant amplitude change in seasonality. |
| 0 | Multiplicative (default)—Indicates that the time series has a seasonality with the amplitude increasing over time. |
| 1 | Additive—Indicates that the time series has a constant amplitude change in seasonality. |
|  | Xt averaged returns the averaged univariate time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Exponential Average (Waveform)

[IMAGE alt='image' src='tsa_vector_exponential_average_(waveform)c.gif']

|  | Xt specifies the multivariate (vector) time series. |
| --- | --- |
|  | exponential type specifies the type of exponential average. Each element of the array is one selection for one channel. Refer to the Details section for more information about each exponential type. |
|  | exponential factors specifies the weighting factors for exponential smoothing. Each element of the array represents one selection for one channel. level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | level specifies the weight for the level cumulant. The value must be a number between 0 and 1. |
|  | trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. |
|  | season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | season period specifies the length of the seasonal pattern in the input time series. Each element of the array represents one selection for one channel. This option is available only when exponential type is Triple. |
|  | season type specifies the way in which this VI models the seasonality. Each element of the array represents one selection for one channel. This option is available only when exponential type is Triple. Refer to the Details section for more information about each season type. |
|  | Xt averaged returns the averaged multivariate (vector) time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Exponential Average (Array)

[IMAGE alt='image' src='tsa_vector_exponential_average_(array)c.gif']

|  | Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
| --- | --- |
|  | exponential type specifies the type of exponential average. Each element of the array is one selection for one channel. Refer to the Details section for more information about each exponential type. |
|  | exponential factors specifies the weighting factors for exponential smoothing. Each element of the array represents one selection for one channel. level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | level specifies the weight for the level cumulant. The value must be a number between 0 and 1. |
|  | trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. |
|  | season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | season period specifies the length of the seasonal pattern in the input time series. Each element of the array represents one selection for one channel. This option is available only when exponential type is Triple. |
|  | season type specifies the way in which this VI models the seasonality. Each element of the array represents one selection for one channel. This option is available only when exponential type is Triple. Refer to the Details section for more information about each season type. |
|  | Xt averaged returns the averaged multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Exponential Average Details

This VI uses the exponential weighting scheme to produce a smoothed time series. This VI computes the averaged values by assigning exponentially decreasing weights to the old values in the original time series according to the following equation:

*X<sub>a</sub>*(*i*) = a*X<sub>t</sub>*(*i*–1) + a(1–a)*X<sub>t</sub>*(*i*–2) + a(1–a)<sup>2</sup>*X<sub>t</sub>*(*i*–3) + …

where a is the **level** weight for level cumulant *X<sub>a</sub>*, *X<sub>a</sub>* is the averaged time series, and *X<sub>t</sub>* is the original time series.

##### Single

This average scheme begins by initializing *X<sub>a</sub>*(0) as *X<sub>t</sub>*(0), For any time period *i*, this VI computes the averaged value *X<sub>a</sub>* according to the following equation:

*X<sub>a</sub>*(*i*) = aX<sub>t</sub>(*i*) + (1–a)*X<sub>a</sub>*(*i*–1), 0<a<1, *n*≥2

##### Double

This average scheme begins by initializing *X<sub>a</sub>*(0) as *X<sub>t</sub>*(0), For any time period *i*, this VI computes the averaged value *X<sub>a</sub>* according to the following equation:

*X<sub>a</sub>*(*i*) = aX<sub>t</sub>(*i*) + (1–a)[*X<sub>a</sub>*(*i*–1) + *B*(*i*–1)], 0<a<1

*B*(*i*) = b[*X<sub>a</sub>*(*i*)–*X<sub>a</sub>*(*i*–1)]+(1–b)*B*(*i*–1), 0<b<1

where b is the trend weight for trend cumulant *B*. *B*(0) is initialized as *X<sub>t</sub>*(1)–*X<sub>t</sub>*(0).

##### Triple

This average scheme begins by initializing *X<sub>a</sub>*(0) as *X<sub>t</sub>*(0) and computes different averaged values depending on the seasonality type: **Multiplicative** or **Additive**.

- Multiplicative seasonality 

 For any time period *i*, this VI computes the averaged value *X<sub>a</sub>* according to the following equation: 

 [IMAGE alt='image' src='tsa_equ_expomulti.gif'] 

 where b is the **trend** weight for trend cumulant *B*, g is the **season** weight for season cumulant vector *I*, and *L* is **season period**.
- Additive seasonality 

 For any time period *i*, this VI computes the averaged value *X<sub>a</sub>* according to the following equation: 

 [IMAGE alt='image' src='tsa_equ_additive.gif'] 

 *B*(0) is initialized as follows: 

 [IMAGE alt='image' src='tsa_equ_initial1.gif'] 

 *I<sub>j</sub>*, *j*=–*L*, …, –1 is initialized as follows: 

 [IMAGE alt='image' src='tsa_equ_initial2.gif'] 

 *M* is approximately equal to the length of the time series divided by *L*, and *I*<sub>0</sub>=*I*<sub>-*L*</sub>

##### Reference:

*NIST/SEMATECH e-Handbook of Statistical Methods*, http://www.itl.nist.gov/div898/handbook, 2005.

#### Example

Refer to the Exponential Smoothing VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Exponential Average VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_mean.html language=enus -->
## TOPIC 00110: TSA Mean VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_mean.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_mean.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Mean VI

**Owning Palette:** [Statistical Analysis VIs](../lvtimeseriestk/tsa_statistical_analysis_vis.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the [mean](../lvasptconcepts/tsa_basic_stat_analysis.html#understanding_the_mean_and_variance_values) values of a univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### TSA Mean (Waveform)

[IMAGE alt='image' src='tsa_mean_(waveform)c.gif']

|  | trimmed percent specifies a percentage at which to discard the lowest and highest values in the time series. This option is available only when method is Trimmed. |
| --- | --- |
|  | Xt specifies the univariate time series. |
|  | method specifies the method to use in computing the mean value of the input time series. Refer to the Details section for more information about each method. 0Arithmetic (default)1Geometric2Trimmed3Median |
| 0 | Arithmetic (default) |
| 1 | Geometric |
| 2 | Trimmed |
| 3 | Median |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | mean returns the mean value of the input time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Mean (Array)

[IMAGE alt='image' src='tsa_mean_(array)c.gif']

|  | trimmed percent specifies a percentage at which to discard the lowest and highest values in the time series. This option is available only when method is Trimmed. |
| --- | --- |
|  | Xt specifies the univariate time series. |
|  | method specifies the method to use in computing the mean value of the input time series. Refer to the Details section for more information about each method. 0Arithmetic (default)1Geometric2Trimmed3Median |
| 0 | Arithmetic (default) |
| 1 | Geometric |
| 2 | Trimmed |
| 3 | Median |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | mean returns the mean value of the input time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Mean (Waveform)

[IMAGE alt='image' src='tsa_vector_mean_(waveform)c.gif']

|  | trimmed percent specifies a percentage at which to discard the lowest and highest values in the time series. This option is available only when method is Trimmed. |
| --- | --- |
|  | Xt specifies the multivariate (vector) time series. |
|  | method specifies the method to use in computing the mean value of the input time series. Refer to the Details section for more information about each method. 0Arithmetic (default)1Geometric2Trimmed3Median |
| 0 | Arithmetic (default) |
| 1 | Geometric |
| 2 | Trimmed |
| 3 | Median |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | vector mean returns the vector mean values of the multivariate (vector) time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Mean (Array)

[IMAGE alt='image' src='tsa_vector_mean_(array)c.gif']

|  | trimmed percent specifies a percentage at which to discard the lowest and highest values in the time series. This option is available only when method is Trimmed. |
| --- | --- |
|  | Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
|  | method specifies the method to use in computing the mean value of the input time series. Refer to the Details section for more information about each method. 0Arithmetic (default)1Geometric2Trimmed3Median |
| 0 | Arithmetic (default) |
| 1 | Geometric |
| 2 | Trimmed |
| 3 | Median |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | vector mean returns the vector mean values of the multivariate (vector) time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Mean Details

This VI calculates the mean values of an input time series with the method you specify for the **method** parameter.

##### Arithmetic mean

This VI calculates the arithmetic mean value according to the following equation:

[IMAGE alt='image' src='tsa_equ_meanarith.gif']

where m is the arithmetic mean value, and *n* is the number of samples of the time series *X<sub>t</sub>*.

##### Geometric mean

This VI calculates the geometric mean value according to the following equation:

[IMAGE alt='image' src='tsa_equ_meangeo.gif']

where m is the geometric mean value, and *n* is the number of samples of the time series *X<sub>t</sub>*.

##### Trimmed mean

This VI calculates the trimmed mean value by eliminating a percentage of the smallest and largest values from the time series and then calculating the arithmetic average of the remaining values. This method is useful for a time series with extreme values.

##### Median mean

This VI calculates the median mean value by sorting the values and then selecting the value in the middle. If the number of values in the sample is even, then the median is the average of the two middle values. This method generates a rough mean value but is useful in cases when a time series has large outliers.

#### Example

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Mean VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_principal_component.html language=enus -->
## TOPIC 00111: TSA Principal Component Analysis VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_principal_component.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_principal_component.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Principal Component Analysis VI

**Owning Palette:** [Statistical Analysis VIs](../lvtimeseriestk/tsa_statistical_analysis_vis.html)

**Requires:** Advanced Signal Processing Toolkit

Performs [principal component analysis (PCA)](../lvasptconcepts/tsa_multivariate_stat_analysis.html#understanding_principal_component_analysis) on a multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Examples](#examples)

#### TSA Principal Component Analysis (Waveform)

[IMAGE alt='image' src='tsa_principal_component_analysis_(waveform)c.gif']

|  | Xt specifies the multivariate (vector) time series. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | unified? specifies to remove the mean and then unify Xt before performing PCA. The default is FALSE. |
|  | Xt out returns the computed principal component scores. |
|  | variance returns the variance values of the calculated principal component scores. |
|  | weights returns the weight matrix that this VI used when computing principal component scores from multivariate time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Principal Component Analysis (Array)

[IMAGE alt='image' src='tsa_principal_component_analysis_(array)c.gif']

|  | Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | unified? specifies to remove the mean and then unify Xt before performing PCA. The default is FALSE. |
|  | Xt out returns the computed principal component scores. Each column of the 2D array represents a series of the computed principal component scores. |
|  | variance returns the variance values of the calculated principal component scores. |
|  | weights returns the weight matrix that this VI used when computing principal component scores from multivariate time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Principal Component Analysis Details

Principal component analysis (PCA) computes a new set of uncorrelated multivariate (vector) time series by a transform of coordinate rotation from original correlated multivariate time series.

This VI performs PCA according to the following steps:

1. Calculates the covariance/correlation coefficient matrix

This VI calculates the covariance matrix according to the following equation:

[IMAGE alt='image' src='tsa_equ_principal1.gif']

where *w* = *N*–1, *N* is the number of time series samples. The dimension of the covariance matrix is *m*×*m*.

This VI calculates the correlation coefficient matrix according to the following equation:

[IMAGE alt='image' src='tsa_equ_principal2.gif']

If **unified?** is TRUE, this VI calculates the correlation coefficients matrix first and then performs PCA. If **unified?** is FALSE, this VI calculates the covariance matrix first, and then performs PCA.

2. Calculates the eigenvectors and eigenvalues of the matrix

This VI obtains the *m* eigenvalues l<sub>i</sub> and eigenvectors *v<sub>i</sub>* from either covariance matrix or correlation matrix. l<sub>i</sub> and *v<sub>i</sub>* satisfy the following equation:

*AV<sub>i</sub>* = l<sub>i</sub>*V<sub>i</sub>*, *i*=1, …, *m*

where *A* is an *m*×*m* covariance matrix or correlation matrix.

3. Generates the new time series

This VI then computes a new set of uncorrelated multivariate (vector) time series according to the following equation:

*X<sub>t</sub><sup>new</sup>*=*V<sup>T</sup>X<sub>t</sub>*

where *X<sub>t</sub><sup>new</sup>* is the new uncorrelated multivariate (vector) time series, and *X<sub>t</sub>* is the original correlated multivariate (vector) time series. Both of them are *m*×*n* matrices whose row vectors represent a single channel time series. *V* is eigenvectors matrix [*v*<sub>1</sub>, *v*<sub>2</sub>,…, *v<sub>m</sub>*].

*V* also is the weight matrix. Each column of *V* is one principle component. *X<sub>t</sub><sup>new</sup>* also is the principal component scores. Each row of *X<sub>t</sub><sup>new</sup>* is the scores for one principal component. Each l<sub>i</sub> is variance of the scores for one principal component.

#### Examples

Refer to the following VIs for examples of using the TSA Principal Component Analysis VI:

- Principal Component Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted
- Image Compression with PCA VI: labview\examples\Time Series Analysis\TSAApplications

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_real_cepstrum.html language=enus -->
## TOPIC 00112: TSA Real Cepstrum VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_real_cepstrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_real_cepstrum.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Real Cepstrum VI

**Owning Palette:** [Correlation and Spectral Analysis VIs](../lvtimeseriestk/tsa_correlation_spectral_vi.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the single-sided [real cepstrum](../lvasptconcepts/aspt_real_cepstrum.html) of a univariate time series. You can use the resulting real cepstrum to detect the periodicities of the time series. The real cepstrum does not keep the phase information of the time series, so you cannot reconstruct the original time series from the real cepstrum. Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Examples](#examples)

#### TSA Real Cepstrum (Waveform)

[IMAGE alt='image' src='tsa_real_cepstrum_(waveform)c.gif']

|  | cepstrum bins specifies the number of time points. This VI computes the cepstrum for each time point. The default is –1, which specifies that the number of cepstrum bins equals the length of the input time series. |
| --- | --- |
|  | Xt specifies the univariate time series. |
|  | method specifies whether this VI uses the FFT-based or the autoregressive (AR) model-based method to compute the real cepstrum. The default is FFT. Refer to the Details section for more information about each method. |
|  | window specifies the time-domain window applied to the time series. Options include None (default), Hanning, Hamming, Blackman-Harris, Exact Blackman, Blackman, Flat Top, 4 Term B-Harris, 7 Term B-Harris, and Low Sidelobe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | AR setting specifies the settings for the autoregressive (AR) model. This option is valid only when the method is AR Model. AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
| 0 | Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions. |
| 1 | Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions. |
| 2 | Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions. |
| 3 | Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average. |
| 4 | Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
|  | AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | cepstrum returns the cepstrum information about Xt. t0 returns the lower boundary of the time range. dt returns the time increment. C(t) returns the resulting values of the complex cepstrum. |
|  | t0 returns the lower boundary of the time range. |
|  | dt returns the time increment. |
|  | C(t) returns the resulting values of the complex cepstrum. |
|  | unit returns the engineering unit of the PSD. You can specify an engineering unit for a time series by using the TSA Scale to EU VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Real Cepstrum (Array)

[IMAGE alt='image' src='tsa_real_cepstrum_(array)c.gif']

|  | sampling rate specifies the sampling rate, in hertz, of the univariate time series Xt. The default is 1. |
| --- | --- |
|  | cepstrum bins specifies the number of time points. This VI computes the cepstrum for each time point. The default is –1, which specifies that the number of cepstrum bins equals the length of the input time series. |
|  | Xt specifies the univariate time series. |
|  | method specifies whether this VI uses the FFT-based or the autoregressive (AR) model-based method to compute the real cepstrum. The default is FFT. Refer to the Details section for more information about each method. |
|  | window specifies the time-domain window applied to the time series. Options include None (default), Hanning, Hamming, Blackman-Harris, Exact Blackman, Blackman, Flat Top, 4 Term B-Harris, 7 Term B-Harris, and Low Sidelobe. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | AR setting specifies the settings for the autoregressive (AR) model. This option is valid only when the method is AR Model. AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
| 0 | Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions. |
| 1 | Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions. |
| 2 | Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions. |
| 3 | Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average. |
| 4 | Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
|  | AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | cepstrum returns the cepstrum information about Xt. t0 returns the lower boundary of the time range. dt returns the time increment. C(t) returns the resulting values of the complex cepstrum. |
|  | t0 returns the lower boundary of the time range. |
|  | dt returns the time increment. |
|  | C(t) returns the resulting values of the complex cepstrum. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Real Cepstrum Details

When **method** is **FFT**, this VI computes the real cepstrum of a univariate time series according to the following equation:

[IMAGE alt='image' src='tsa_equ_realcep1.gif']

*X<sub>t</sub>* is the univariate time series and [IMAGE alt='image' src='c_tau.gif'] is the real cepstrum of *X<sub>t</sub>*.

When **method** is **AR Model**, this VI computes the real cepstrum of a univariate time series according to the following equation:

[IMAGE alt='image' src='tsa_equ_realcep2.gif']

s is the standard deviation of estimated noise series of AR model of *X<sub>t</sub>* and *a* is the estimated coefficients of AR model. *a* = [1, *a*<sub>1</sub>, *a*<sub>2</sub>, …, *a<sub>k</sub>*].

#### Examples

Refer to the following VIs for examples of using the TSA Real Cepstrum VI:

- Bearing Monitor VI: labview\examples\Time Series Analysis\TSAApplications
- Cepstrum Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_resampling.html language=enus -->
## TOPIC 00113: TSA Resampling VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_resampling.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_resampling.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Resampling VI

**Owning Palette:** [Preprocessing VIs](../lvtimeseriestk/tsa_preprocess_vi.html)

**Requires:** Advanced Signal Processing Toolkit

[Resamples](../lvasptconcepts/tsa_preprocess.html#resampling_a_time_series) the equally- or unequally-sampled time series into a new time series with a specified time interval using the interpolation method. Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### TSA Resampling (Waveform)

[IMAGE alt='image' src='tsa_resampling_(waveform)c.gif']

|  | Xt specifies the univariate time series. |
| --- | --- |
|  | new sampling rate specifies the sampling rate for the resampled time series. The value must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt resampled returns the resampled univariate time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Resampling (Equal)

[IMAGE alt='image' src='tsa_resampling_(equal)c.gif']

|  | original sampling rate specifies the original sampling rate of the equally-sampled time series Xt. |
| --- | --- |
|  | Xt specifies the univariate time series. |
|  | new sampling rate specifies the sampling rate for the resampled time series. The value must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt resampled returns the resampled univariate time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Resampling (Unequal)

[IMAGE alt='image' src='tsa_resampling_(unequal)c.gif']

|  | Xt specifies the univariate time series. time index specifies the sampling time point of the unequally-sampled univariate time series Xt. data specifies the unequally-sampled data in the univariate time series Xt. |
| --- | --- |
|  | time index specifies the sampling time point of the unequally-sampled univariate time series Xt. |
|  | data specifies the unequally-sampled data in the univariate time series Xt. |
|  | new sampling rate specifies the sampling rate for the resampled time series. The value must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt resampled returns the resampled univariate time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Resampling (Waveform)

[IMAGE alt='image' src='tsa_vector_resampling_(waveform)c.gif']

|  | Xt specifies the multivariate (vector) time series. |
| --- | --- |
|  | new sampling rate specifies the sampling rate for the resampled time series. The value must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt resampled returns the resampled multivariate (vector) time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Resampling (Equal)

[IMAGE alt='image' src='tsa_vector_resampling_(equal)c.gif']

|  | original sampling rate specifies the original sampling rate of the equally-sampled time series Xt. |
| --- | --- |
|  | Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
|  | new sampling rate specifies the sampling rate for the resampled time series. The value must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt resampled returns the resampled multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Resampling (Unequal)

[IMAGE alt='image' src='tsa_vector_resampling_(unequal)c.gif']

|  | Xt specifies the multivariate (vector) time series. time index specifies the sampling time point of the unequally-sampled multivariate (vector) time series Xt. data specifies the unequally-sampled data in the multivariate (vector) time series Xt. Each column of the 2D array represents a vector at certain time. |
| --- | --- |
|  | time index specifies the sampling time point of the unequally-sampled multivariate (vector) time series Xt. |
|  | data specifies the unequally-sampled data in the multivariate (vector) time series Xt. Each column of the 2D array represents a vector at certain time. |
|  | new sampling rate specifies the sampling rate for the resampled time series. The value must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt resampled returns the resampled multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the TSA Resampling VI:

- Resample Time Series VI: labview\examples\Time Series Analysis\TSAGettingStarted
- Resample Unequally-Sampled Time Series VI: labview\examples\Time Series Analysis\TSAGettingStarted

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_rndm_squns_generation.html language=enus -->
## TOPIC 00114: Random Sequence Generation Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_rndm_squns_generation.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_rndm_squns_generation.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Random Sequence Generation Express VI

**Owning Palette:** [Utilities VIs](../lvtimeseriestk/tsa_utilities_vis.html)

**Requires:** Advanced Signal Processing Toolkit

Generates a random univariate time series from the normal, uniform, chi-square, *t*, or *F* distribution. This Express VI also can generate a random multivariate time series from the vector normal distribution. You can plot the histogram of the generated time series in the configuration dialog box.

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Configuration | Contains the following options: Noise type—Specifies the type of probability density function distribution of the noise. Contains the following options: Normal Distribution (default) Uniform Distribution Chi-Square Distribution T Distribution F Distribution Samples—Specifies the number of random sequence samples to generate. |
| Parameters Settings | Contains the following options: Mean—Specifies the mean value of the normal distribution. The default is 0. Available only when you select Normal Distribution from the Noise type list. Standard deviation—Specifies the standard deviation value of the normal distribution. The default is 1. Available only when you select Normal Distribution from the Noise type list. Seed—Specifies the seed of the noise sample generator. Seeds with different values greater than 0 generate different noise sequences. Values less than 0 cause reseeding each time this VI runs. The default is –1. Available only when you select Normal Distribution or Uniform Distribution from the Noise type list. Upper endpoint—Specifies the maximum value for the uniform distribution. Available only when you select Uniform Distribution from the Noise type list. Lower endpoint—Specifies the minimum value for the uniform distribution. Available only when you select Uniform Distribution from the Noise type list. Degrees of freedom—Specifies the degrees of freedom (DOF) this VI uses to define the chi-square or t distribution. Available only when you select Chi-Square Distribution or T Distribution from the Noise type list. Numerator DOF—Specifies the degrees of freedom (DOF) of the numerator to define the F distribution. Available only when you select F Distribution from the Noise type list. Denominator DOF—Specifies degrees of freedom (DOF) of the denominator to define the F distribution. Available only when you select F Distribution from the Noise type list. |
| Random Sequence and Histogram | Contains the following options: Random sequence—Displays the generated random sequence. Histogram—Displays the histogram of the generated random sequence. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| error out | Contains error information. This output provides standard error out functionality. |
| Xt | Returns the generated random sequence. |

This Express VI operates similarly to the following VIs and functions:

[TSA Normal Distribution Test](../lvtimeseriestk/tsa_normal_distribution_test.html) 

[TSA Random Sequence Generation](../lvtimeseriestk/tsa_random_squnc_generation.html)

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_scale_to_eu.html language=enus -->
## TOPIC 00115: TSA Scale to EU VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_scale_to_eu.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_scale_to_eu.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Scale to EU VI

**Owning Palette:** [Utilities VIs](../lvtimeseriestk/tsa_utilities_vis.html)

**Requires:** Advanced Signal Processing Toolkit

Converts the unit of a univariate or multivariate (vector) time series from volts to an engineering unit (EU). Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### TSA Scale to EU (Single-Channel)

[IMAGE alt='image' src='tsa_scale_to_eu_(single-channel)c.gif']

|  | Xt specifies the univariate time series. |
| --- | --- |
|  | scale info specifies information about the measurement system used before the signal reaches the data acquisition (DAQ) device. sensor sensitivity [mV/EU] specifies the sensitivity of the sensor in mV/EU. engineering unit specifies the engineering unit to which you want to scale. The default is V. custom label specifies a label for the custom engineering unit. |
|  | sensor sensitivity [mV/EU] specifies the sensitivity of the sensor in mV/EU. |
|  | engineering unit specifies the engineering unit to which you want to scale. The default is V. |
|  | custom label specifies a label for the custom engineering unit. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt out returns the scaled univariate time series expressed in specified scale information. |
|  | unit returns the name of the specified engineering unit. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Scale to EU (Multi-Channel)

[IMAGE alt='image' src='tsa_scale_to_eu_(multi-channel)c.gif']

|  | Xt specifies the multivariate (vector) time series. |
| --- | --- |
|  | scale info specifies information about the measurement system used before the signal reaches the DAQ device. Each element of the array represents one setting for one channel. scale info contains the following elements: sensor sensitivity [mV/EU] specifies the sensitivity of the sensor in mV/EU. engineering unit specifies the engineering unit to which you want to scale. The default is V. custom label specifies a label for the custom engineering unit. |
|  | sensor sensitivity [mV/EU] specifies the sensitivity of the sensor in mV/EU. |
|  | engineering unit specifies the engineering unit to which you want to scale. The default is V. |
|  | custom label specifies a label for the custom engineering unit. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Xt out returns the scaled multivariate (vector) time series expressed in specified scale information. |
|  | unit returns the name of the specified engineering units. Each element of the array represents one unit for one channel. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Scale to EU Details

Use the TSA Scale To Unit VI to analyze a time series for engineering purposes, such as vibration testing.

|  | Note If the unit of the input time series is scaled from volts to another engineering unit prior to reaching this VI, this VI does not perform any additional scaling. Therefore, this VI ignores any scaling information specified in scale info, such as sensor sensitivity [mV/EU] or engineering units and reads the engineering unit from the attributes of the input signal. |
| --- | --- |

#### Example

Refer to the Average PSD VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Scale to EU VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_stochastic_subspace_modeling.html language=enus -->
## TOPIC 00116: TSA Stochastic State-Space Modeling VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_stochastic_subspace_modeling.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_stochastic_subspace_modeling.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Stochastic State-Space Modeling VI

**Owning Palette:** [Modeling and Prediction VIs](../lvtimeseriestk/tsa_mdl_prdctn_vis.html)

**Requires:** Advanced Signal Processing Toolkit

Estimates the [stochastic state-space model](../lvasptconcepts/tsa_building_sss.html) of a multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### TSA Vector Stochastic State-Space Modeling (Waveform)

[IMAGE alt='image' src='tsa_vector_stochastic_state-space_modeling_(waveform)c.gif']

|  | Xt specifies the multivariate (vector) time series. The number of samples must be greater than two times model order. |
| --- | --- |
|  | model order specifies the model order of the state-space model. The value of model order must be at least twice the number of frequency components that you want to estimate. The default is 4. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | noise subspace specifies the percentage of the noise subspace in the whole space, which is the combination of the signal subspace and the noise subspace. The default is 10. |
|  | A returns the estimated state transition matrix of the stochastic state-space model. |
|  | C returns the estimated measurement matrix of the stochastic state-space model. |
|  | frequency components returns information about the estimated frequency components. frequency returns the estimated frequency of the frequency component. damping factor returns the estimated damping factor of the frequency component. magnitude returns the estimated magnitude of the frequency component. Each element of the array represents one channel series in Xt. phase returns the estimated phase of the frequency component. Each element of the array represents one channel series in Xt. |
|  | frequency returns the estimated frequency of the frequency component. |
|  | damping factor returns the estimated damping factor of the frequency component. |
|  | magnitude returns the estimated magnitude of the frequency component. Each element of the array represents one channel series in Xt. |
|  | phase returns the estimated phase of the frequency component. Each element of the array represents one channel series in Xt. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Vector Stochastic State-Space Modeling (Array)

[IMAGE alt='image' src='tsa_vector_stochastic_state-space_modeling_(array)c.gif']

|  | Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. |
| --- | --- |
|  | model order specifies the model order of the state-space model. The value of model order must be at least twice the number of frequency components that you want to estimate. The default is 4. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | noise subspace specifies the percentage of the noise subspace in the whole space, which is the combination of the signal subspace and the noise subspace. The default is 10. |
|  | A returns the estimated state transition matrix of the stochastic state-space model. |
|  | C returns the estimated measurement matrix of the stochastic state-space model. |
|  | frequency components returns information about the estimated frequency components. frequency returns the estimated frequency of the frequency component. damping factor returns the estimated damping factor of the frequency component. magnitude returns the estimated magnitude of the frequency component. Each element of the array represents one channel series in Xt. phase returns the estimated phase of the frequency component. Each element of the array represents one channel series in Xt. |
|  | frequency returns the estimated frequency of the frequency component. |
|  | damping factor returns the estimated damping factor of the frequency component. |
|  | magnitude returns the estimated magnitude of the frequency component. Each element of the array represents one channel series in Xt. |
|  | phase returns the estimated phase of the frequency component. Each element of the array represents one channel series in Xt. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Stochastic State-Space Modeling Details

This VI estimates the stochastic state-space model of a multivariate (vector) time series according to the following equations:

*S*<sub>*k*+1</sub> = *AS<sub>k</sub>* + *w<sub>k</sub>*

*x<sub>k</sub>* = *CS<sub>k</sub>*+*v<sub>k</sub>*

*x<sub>k</sub>* is the *m*×1 vector time series with *m* variables, *S<sub>k</sub>* is the state vector with *n* state variables, *n* is **model order**, *A* is the state transition matrix with the size *n* × *n*, *C* is the measurement matrix with the size *m* × *n*, and *w<sub>k</sub>* and *v<sub>k</sub>* are *n* × 1 and *m* × 1 noise vectors, respectively, with a mean of zero.

You can use the estimated stochastic state-space model to describe the signal subspace. The **noise subspace** parameter specifies the amount of noise subspace as a percentage in the whole space, which is the combination of the signal subspace and the noise subspace.

You can characterize the dynamic behavior of a system by converting the matrix *A* and matrix *C* into the **frequency**, **damping factor**, **magnitude** and **phase** parameters that the modal parametric model contains. Refer to the [TSA Modal Parametric Modeling](../lvtimeseriestk/tsa_modal_parametric.html) VI for the definition of modal parameters.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_time_cepstrum.html language=enus -->
## TOPIC 00117: TSA Time-Cepstrum VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_time_cepstrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_time_cepstrum.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Time-Cepstrum VI

**Owning Palette:** [Correlation and Spectral Analysis VIs](../lvtimeseriestk/tsa_correlation_spectral_vi.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the single-sided [time-cepstrum](../lvasptconcepts/tsa_time-cepstrum.html) of a univariate time series by using a [sliding window](/csh?topicname=lvanlsconcepts/windowing_signals.html). You can use the resulting time-cepstrum to detect time-varying periodic components of a time series. Wire data to the **Xt** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### TSA Time-Cepstrum (Waveform)

[IMAGE alt='image' src='tsa_time-cepstrum_(waveform)c.gif']

|  | method specifies whether this VI uses the FFT-based or the autoregressive (AR) model-based method to compute the real cepstrum. The default is FFT. |
| --- | --- |
|  | quefrency offset specifies the offset, in seconds, of the quefrency. This VI returns the real cepstrum at a certain time whose quefrency is larger than the offset value. The default is 0. |
|  | Xt specifies the univariate time series. |
|  | time-quefrency sampling info specifies information about the density and the size of the time-cepstrum. time steps specifies the sampling period, in number of samples, along the time axis in the joint time-quefrency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in the cepstrogram. National Instruments recommends that you set time steps such that the number of rows in cepstrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large cepstrogram, which requires a long computation time and more memory. If you need a small sampling period to observe more details and the signal length is long, divide the signal into smaller segments and compute the cepstrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis of the cepstrogram. quefrency bins specifies the number of bins along the quefrency axis of the cepstrogram to sample the time series in the joint time-quefrency domain. quefrency bins must be greater than 0. The scale info output contains the actual sampling period, in seconds, along the quefrency axis of the cepstrogram. The default is 512. |
|  | time steps specifies the sampling period, in number of samples, along the time axis in the joint time-quefrency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in the cepstrogram. National Instruments recommends that you set time steps such that the number of rows in cepstrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large cepstrogram, which requires a long computation time and more memory. If you need a small sampling period to observe more details and the signal length is long, divide the signal into smaller segments and compute the cepstrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis of the cepstrogram. |
|  | quefrency bins specifies the number of bins along the quefrency axis of the cepstrogram to sample the time series in the joint time-quefrency domain. quefrency bins must be greater than 0. The scale info output contains the actual sampling period, in seconds, along the quefrency axis of the cepstrogram. The default is 512. |
|  | window info specifies the information about the sliding window that divides the time series Xt into subsequences. type specifies the time-domain window that this VI applies to the time series. 0None1Hanning (default)2Hamming3Blackman-Harris4Exact Blackman5Blackman6Flat Top74-Term B-Harris87-Term B-Harris9Low Sidelobe10Gaussian length specifies the length of the window in samples. The default is –1, which indicates that the window length equals the length of the input time series. |
|  | type specifies the time-domain window that this VI applies to the time series. 0None1Hanning (default)2Hamming3Blackman-Harris4Exact Blackman5Blackman6Flat Top74-Term B-Harris87-Term B-Harris9Low Sidelobe10Gaussian |
| 0 | None |
| 1 | Hanning (default) |
| 2 | Hamming |
| 3 | Blackman-Harris |
| 4 | Exact Blackman |
| 5 | Blackman |
| 6 | Flat Top |
| 7 | 4-Term B-Harris |
| 8 | 7-Term B-Harris |
| 9 | Low Sidelobe |
| 10 | Gaussian |
|  | length specifies the length of the window in samples. The default is –1, which indicates that the window length equals the length of the input time series. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | AR setting specifies the settings for the autoregressive (AR) model. This option is valid only when the method is AR Model. AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
| 0 | Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions. |
| 1 | Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions. |
| 2 | Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions. |
| 3 | Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average. |
| 4 | Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
|  | AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | cepstrogram returns the time-quefrency representation of the time series Xt. Each row corresponds to the real cepstrum at a certain time. The number of rows in cepstrogram equals the signal length divided by time steps. You can use the TSA Get Time and Quefrency Scale Info VI to compute the time scale information and the quefrency scale information of the time-quefrency representation. |
|  | scale info returns the time scale and quefrency scale information of the time-quefrency representation, including the time offset, the time interval between every two contiguous rows, the quefrency offset, and the quefrency interval between every two contiguous columns of the cepstrogram. |
|  | overlap returns the overlap, in percentage, of the sliding window this VI applies to the time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TSA Time-Cepstrum (Array)

[IMAGE alt='image' src='tsa_time-cepstrum_(array)c.gif']

|  | method specifies whether this VI uses the FFT-based or the autoregressive (AR) model-based method to compute the real cepstrum. The default is FFT. |
| --- | --- |
|  | quefrency offset specifies the offset, in seconds, of the quefrency. This VI returns the real cepstrum at a certain time whose quefrency is larger than the offset value. The default is 0. |
|  | Xt specifies the univariate time series. |
|  | time-quefrency sampling info specifies information about the density and the size of the time-cepstrum. time steps specifies the sampling period, in number of samples, along the time axis in the joint time-quefrency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in the cepstrogram. National Instruments recommends that you set time steps such that the number of rows in cepstrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large cepstrogram, which requires a long computation time and more memory. If you need a small sampling period to observe more details and the signal length is long, divide the signal into smaller segments and compute the cepstrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis of the cepstrogram. quefrency bins specifies the number of bins along the quefrency axis of the cepstrogram to sample the time series in the joint time-quefrency domain. quefrency bins must be greater than 0. The scale info output contains the actual sampling period, in seconds, along the quefrency axis of the cepstrogram. The default is 512. |
|  | time steps specifies the sampling period, in number of samples, along the time axis in the joint time-quefrency domain. The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in the cepstrogram. National Instruments recommends that you set time steps such that the number of rows in cepstrogram does not exceed 512. If you specify a small value for time steps, this VI might return a large cepstrogram, which requires a long computation time and more memory. If you need a small sampling period to observe more details and the signal length is long, divide the signal into smaller segments and compute the cepstrogram for each segment. If the signal is oversampled, you also can downsample the signal. The scale info output contains the actual sampling period, in seconds, along the time axis of the cepstrogram. |
|  | quefrency bins specifies the number of bins along the quefrency axis of the cepstrogram to sample the time series in the joint time-quefrency domain. quefrency bins must be greater than 0. The scale info output contains the actual sampling period, in seconds, along the quefrency axis of the cepstrogram. The default is 512. |
|  | window info specifies the information about the sliding window that divides the time series Xt into subsequences. type specifies the time-domain window that this VI applies to the time series. 0None1Hanning (default)2Hamming3Blackman-Harris4Exact Blackman5Blackman6Flat Top74-Term B-Harris87-Term B-Harris9Low Sidelobe10Gaussian length specifies the length of the window in samples. The default is –1, which indicates that the window length equals the length of the input time series. |
|  | type specifies the time-domain window that this VI applies to the time series. 0None1Hanning (default)2Hamming3Blackman-Harris4Exact Blackman5Blackman6Flat Top74-Term B-Harris87-Term B-Harris9Low Sidelobe10Gaussian |
| 0 | None |
| 1 | Hanning (default) |
| 2 | Hamming |
| 3 | Blackman-Harris |
| 4 | Exact Blackman |
| 5 | Blackman |
| 6 | Flat Top |
| 7 | 4-Term B-Harris |
| 8 | 7-Term B-Harris |
| 9 | Low Sidelobe |
| 10 | Gaussian |
|  | length specifies the length of the window in samples. The default is –1, which indicates that the window length equals the length of the input time series. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | AR setting specifies the settings for the autoregressive (AR) model. This option is valid only when the method is AR Model. AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | AR method specifies the method this VI uses to estimate the autoregressive (AR) model. 0Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions.1Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions.2Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions.3Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average.4Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
| 0 | Forward-Backward (default)—Computes the AR coefficients by minimizing the least-square errors of the forward and backward predictions. |
| 1 | Least-Squares—Computes the AR coefficients by minimizing the least-square errors of the forward predictions. |
| 2 | Yule-Walker—Computes the AR coefficients by solving the Yule-Walker functions based on the forward predictions. |
| 3 | Burg-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the arithmetic average. |
| 4 | Geometric-Lattice—Computes the AR coefficients using the Levinson-Durbin recursion based on the forward and backward predictions. The Levinson-Durbin recursion uses the geometric average. |
|  | AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |
|  | sampling rate specifies the sampling rate, in hertz, of the univariate time series Xt. The default is 1. |
|  | cepstrogram returns the time-quefrency representation of the time series Xt. Each row corresponds to the real cepstrum at a certain time. The number of rows in cepstrogram equals the signal length divided by time steps. You can use the TSA Get Time and Quefrency Scale Info VI to compute the time scale information and the quefrency scale information of the time-quefrency representation. |
|  | scale info returns the time scale and quefrency scale information of the time-quefrency representation, including the time offset, the time interval between every two contiguous rows, the quefrency offset, and the quefrency interval between every two contiguous columns of the cepstrogram. |
|  | overlap returns the overlap, in percentage, of the sliding window this VI applies to the time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Bearing Time-Cepstrum Analysis VI in the labview\examples\Time Series Analysis\TSAApplications directory for an example of using the TSA Time-Cepstrum VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_time_series_bispectrum.html language=enus -->
## TOPIC 00118: Time Series Bispectrum Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_time_series_bispectrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_time_series_bispectrum.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Series Bispectrum Express VI

**Owning Palette:** [Correlation and Spectral Analysis VIs](../lvtimeseriestk/tsa_correlation_spectral_vi.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the single-sided [bispectrum](../lvasptconcepts/tsa_bispectrum_est.html) of a univariate time series.

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Data Source | Specifies whether this Express VI reads data from a block diagram input terminal or from a file. From terminal specifies that this Express VI reads data from a block diagram input terminal. From file specifies that this Express VI reads data from a file. This Express VI can read data from waveform, WAV, or TXT files. The valid format of a TXT data file is a file that contains only a 1D real array. |
| File Path Configuration | Contains the following options: File path—Specifies and displays the path to the file from which this Express VI reads data. This option is available only when you select From file in the Data Source section. Prompt to choose a file each time this VI runs—Specifies whether this Express VI displays a dialog box that prompts you to select a file each time this Express VI runs. This option is available only when you select the From file option in the Data Source section. |
| Signal and Window | Displays the signal and window. Contains the following option: Display window—Specifies to display the windows that you apply to the time series. This option is available only when you select FFT in Method. |
| Bispectrum | Contains the following options: dB—Specifies to return the results in decibels. The default is TRUE. Bispectrum—Displays the bispectrum. |
| Algorithm Settings | Contains the following options: Frequency bins—Specifies the number of frequency bins for which this VI computes the bispectrum. The resulting bispectrum is a square array. Method—Specifies the method to use in computing the bispectrum. Options include FFT (default) and AR Model. Window—Specifies the time-domain window you apply to the time series. Options include Hanning, Hamming, Blackman-Harris, Exact Blackman, Blackman, Flat Top, 4 Term B-Harris, 7 Term B-Harris, and Low Sidelobe. This option is available only when you select FFT in Method. Window length—Specifies the length of the window. A large window size leads to a small variance and a large bias of the bispectrum, and vice versa. This option is available only when you select FFT in Method. Overlap—Specifies the overlap of the moving window applied to a time series as a percentage. This option is available only when you select FFT in Method. Method of AR Model—Specifies the method to use in estimating the autoregressive model. Options include Forward-Backward (default), Least-Squares, Yule-Walker, Burg-Lattice, and Geometric-Lattice. This option is available only when you select AR Model in Method. AR order—Specifies the order of the autoregressive model. The default is 40. This option is available only when you select AR Model in Method. |
| Averaging Parameters | Specifies how this VI computes the averaging. Contains the following options: Averaging mode—Specifies the averaging mode. Options include No Averaging (default), Vector Averaging, RMS Averaging, and Peak Hold. Weighting mode—Specifies the weighting mode for RMS and vector averaging. Options include Linear and Exponential (default). Number of averages—Specifies the number of averages used for RMS and vector averaging. If Weighting mode is exponential, the averaging process is continuous. If Weighting mode is linear, the averaging process stops after this VI computes the selected Number of averages. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |
| Xt | Specifies the time series. Xt is available only when you select From terminal in Data Source. |
| File path | Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| averaging done? | Returns whether the averaging process is complete. averaging done? returns TRUE when the number of averages this VI completes is greater than or equal to the Number of averages. Otherwise, averaging done? returns FALSE. averaging done? is always TRUE if the Averaging mode is No Averaging. |
| error out | Contains error information. This output provides standard error out functionality. |
| freq bins | Returns the frequency bins at which this VI estimates the bispectrum. |
| Sxxx | Returns the magnitude of the single-sided bispectrum, S(f1, f2). |
| unit | Returns the selected engineering unit of the estimated power spectral density. |

This Express VI operates similarly to the following VIs and functions:

[TSA Bispectrum](../lvtimeseriestk/tsa_bispectrum.html)

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_time_series_cepstrum.html language=enus -->
## TOPIC 00119: Time Series Cepstrum Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_time_series_cepstrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_time_series_cepstrum.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Series Cepstrum Express VI

**Owning Palette:** [Correlation and Spectral Analysis VIs](../lvtimeseriestk/tsa_correlation_spectral_vi.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the single-sided [real cepstrum](../lvasptconcepts/aspt_real_cepstrum.html) of a univariate time series.

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Data Source | Specifies whether this Express VI reads data from a block diagram input terminal or from a file. From terminal specifies that this Express VI reads data from a block diagram input terminal. From file specifies that this Express VI reads data from a file. This Express VI can read data from waveform, WAV, or TXT files. The valid format of a TXT data file is a file that contains only a 1D real array. |
| File Path Configuration | Contains the following options: File path—Specifies and displays the path to the file from which this Express VI reads data. This option is available only when you select From file in the Data Source section. Prompt to choose a file each time this VI runs—Specifies whether this Express VI displays a dialog box that prompts you to select a file each time this Express VI runs. This option is available only when you select the From file option in the Data Source section. |
| Algorithm Settings | Contains the following options: Cepstrum bins—Specifies the number of time points for which this VI computes the cepstrum. The default is 128. Method—Specifies the method to use in computing the cepstrum. Options include AR Model (default) and FFT. AR order—Specifies the order of the autoregressive model. The default is 40. This option is available only when you select AR Model in Method. Method of AR Model—Specifies the method to use in estimating the autoregressive model. Options include Forward-Backward (default), Least-Squares, Yule-Walker, Burg-Lattice, and Geometric-Lattice. This option is available only when you select AR Model in Method. Window—Specifies the time-domain window you apply to the time series. This option is available only when you select FFT in Method. |
| Signal and Window | Displays the signal and window. Contains the following option: Display window—Specifies to display the windows that you apply to the time series. This option is available only when you select FFT in Method. |
| Cepstrum | Displays the cepstrum of a univariate time series. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |
| Xt | Specifies the time series. Xt is available only when you select From terminal in Data Source. |
| File path | Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| cepstrum | Returns information about the single-sided real cepstrum, such as the time range and time increment. |
| error out | Contains error information. This output provides standard error out functionality. |
| unit | Returns the selected engineering unit of the estimated power spectral density. |

This Express VI operates similarly to the following VIs and functions:

[TSA Real Cepstrum](../lvtimeseriestk/tsa_real_cepstrum.html)

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_time_series_modeling.html language=enus -->
## TOPIC 00120: Time Series Modeling Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_time_series_modeling.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_time_series_modeling.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Series Modeling Express VI

**Owning Palette:** [Modeling and Prediction VIs](../lvtimeseriestk/tsa_mdl_prdctn_vis.html)

**Requires:** Advanced Signal Processing Toolkit

[Builds dynamic models](../lvasptconcepts/tsa_building_models.html) of the univariate or multivariate (vector) time series. You can specify the model orders automatically or manually when building models.

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Data Source | Specifies whether this Express VI reads data from a block diagram input terminal or from a file. From terminal specifies that this Express VI reads data from a block diagram input terminal. From file specifies that this Express VI reads data from a file. This Express VI can read data from waveform, WAV, or TXT files. Waveform and TXT files can contain single-channel or multi-channel data. WAV files can contain only single-channel data. |
| File Path Configuration | Contains the following options: File path—Specifies and displays the path to the file from which this Express VI reads data. This option is available only when you select From file in the Data Source section. Prompt to choose a file each time this VI runs—Specifies whether this Express VI displays a dialog box that prompts you to select a file each time this Express VI runs. This option is available only when you select the From file option in the Data Source section. |
| Signal and Noise Auto-correlation | Displays the signal and noise auto-correlation. Channel—Specifies the channel of the time series to display. This option is available only when you select Multiple channels from the System Dimensions section. Signal—Displays the signal that you want to analyze. Noise auto-correlation—Displays the noise auto-correlation. |
| Model Settings | Specifies the settings of the model. Contains the following options: Type—Specifies the type of the model. Contains the following options: AR (default)—Specifies an autoregressive (AR) model. MA—Specifies a moving average (MA) model. ARMA—Specifies an autoregressive-moving average (ARMA) model. Settings—Specifies the settings of the model. AR order—Specifies the order of the AR model to estimate. The value of AR order must be greater than 0. The default is 10. This option is not available when you select MA in Type. MA order—Specifies the order of the MA model to estimate. The value of MA order must be greater than 0. The default is 1. This option is not available when you select AR in Type. Method of AR—Specifies the method to use in estimating the AR model. Options include Forward-Backward (default), Least-Squares, Yule-Walker, Burg-Lattice, and Geometric-Lattice. Method of AR is available only when you select AR in Type. Method of MA—Specifies the method to use in estimating the MA model. Options include Yule-Walker (default), High order AR, and Polynomial. Method of MA is available only when you select MA in Type. Method of ARMA—Specifies the method to use in estimating the ARMA model. Options include Yule-Walker (default), High order AR, and Polynomial. Method of ARMA is available only when you select ARMA in Type. Model Diagram—Displays the model diagram. |
| System Settings | Specifies the system dimensions and data type. System Dimensions—Specifies the dimensions of the system. Options include Single channel (default) and Multiple channels. System Dimensions is available only when you select From terminal in Data Source. When you select From file in Data Source, this VI determines the dimensions of the input time series automatically according to the file content. Data Type—Specifies the data type for the input signal or signals. Options include Array and Waveform (default). Data Type is available only when you select From terminal in Data Source. When you select From file in Data Source, this VI determines the data type of the input time series automatically according to the file content. |
| Order Estimation | This tab is available only when you select AR in Type and Single channel in System Dimensions. Contains the following options: Method—Specifies the method to use in estimating the optimal order. Options include FPE (default), AIC, BIC, MDL, Phi, and PCF. Maximum AR order—Specifies the upper limit of the search for the optimal order of autoregressive (AR) model. The value must be greater than Minimum AR order. The default is 20. Minimum AR order—Specifies the lower limit of the search for the optimal order of autoregressive (AR) model. The value must be greater than 0. The default is 1. Estimate—Click this button to estimate the optimal order. Criterion Function—Displays the criterion function. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |
| Xt | Specifies the time series. Xt is available only when you select From terminal in Data Source. |
| File path | Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| AR coefficients | Returns the estimated AR coefficients. This output is available only when you select AR or ARMA in Type. |
| MA coefficients | Returns the estimated MA coefficients. This output is available only when you select MA or ARMA in Type. |
| noise | Returns the estimated white noise series of the system model. |
| error out | Contains error information. This output provides standard error out functionality. |

This Express VI operates similarly to the following VIs and functions:

[TSA AR Modeling Order](../lvtimeseriestk/tsa_ar_model_order.html) 

[TSA AR Modeling](../lvtimeseriestk/tsa_ar_modeling.html) 

[TSA MA Modeling](../lvtimeseriestk/tsa_ma_modeling.html) 

[TSA ARMA Modeling](../lvtimeseriestk/tsa_arma_modeling.html)

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_time_series_preprocessing.html language=enus -->
## TOPIC 00121: Time Series Preprocessing Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_time_series_preprocessing.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_time_series_preprocessing.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Series Preprocessing Express VI

**Owning Palette:** [Preprocessing VIs](../lvtimeseriestk/tsa_preprocess_vi.html)

**Requires:** Advanced Signal Processing Toolkit

[Preprocesses](../lvasptconcepts/tsa_preprocess.html) univariate or multivariate (vector) time series by moving average, resampling, detrending, or exponential average.

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Data Source | Specifies whether this Express VI reads data from a block diagram input terminal or from a file. From terminal specifies that this Express VI reads data from a block diagram input terminal. From file specifies that this Express VI reads data from a file. This Express VI can read data from waveform, WAV, or TXT files. Waveform and TXT files can contain single-channel or multi-channel data. WAV files can contain only single-channel data. |
| File Path Configuration | Contains the following options: File path—Specifies and displays the path to the file from which this Express VI reads data. This option is available only when you select From file in the Data Source section. Prompt to choose a file each time this VI runs—Specifies whether this Express VI displays a dialog box that prompts you to select a file each time this Express VI runs. This option is available only when you select the From file option in the Data Source section. |
| System Dimensions | Specifies the dimensions of the input signal. Options include Single channel and Multiple channels. System Dimensions is available only when you select From terminal in Data Source. When you select From file in Data Source, this VI determines the dimensions of the time series automatically according to the file content. |
| Data Type | Specifies the data type for the input signal or signals. Options include Array and Waveform. Data Type is available only when you select From terminal in Data Source. When you select From file in Data Source, this VI determines the data type of the time series automatically according to the file content. |
| Configuration | Contains the following options: Method—Specifies the method to use in preprocessing a time series. Contains the following options: Moving Average (default) Resampling Detrending Exponential Average Channel—Specifies the channel of the time series and the processed time series. This option is available only when you select Multiple channels in System Dimensions. Sampling rate—Specifies the sampling rate of the time series. This option is available only when you select Array in Data Type. |
| Algorithm settings | Specifies the settings for the preprocessing algorithm. Contains the following options: Method of moving average—Specifies the filter type to use in filtering the time series. Options include Spencer (default) and Henderson. This option is available only when you select Moving Average from the Method list. New sampling rate—Specifies the sampling rate for the resampled time series. This option is available only when you select Resampling from the Method list. Method of detrend—Specifies the curve-fitting method to use in estimating the trend. Options include Linear (default), Quadratic, Cubic, N-polynomial, and Exponential. This option is available only when you select Detrending from the Method list. Polynomial order—Specifies the polynomial order to use in the N-polynomial fit. The value of this parameter must be greater than or equal to 0. This option is available only when you select N-polynomial from the Method of detrend list. View trend—Specifies whether to display the trend of the time series. The default is FALSE. This option is available only when you select Detrending from the Method list. Exponential type—Specifies the type of the exponential function. This option is available only when you select Exponential Average from the Method list. Contains the following options: Single (default) Double Triple Season period—Specifies the length of the seasonal pattern in the time series. This option is available only when Exponential type is Triple. Season type—Specifies the way in which this Express VI models the seasonality. This option is available only when Exponential type is Triple. Contains the following options: Multiplicative (default) Additive Level—Specifies the weight for the level cumulant. The value must be a number between 0 and 1. This option is available only when you select Exponential Average from the Method list. Trend—Specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when Exponential type is Double or Triple. Season—Specifies the weight for the seasonal cumulant. The value must be a number between 0 and 1. This option is available only when Exponential type is Triple. |
| Original and Processed Signal | Contains the following options: Signal—Displays the univariate or multivariate (vector) time series to preprocess. Filtered signal—Displays the processed time series. This graph displays the filtered time series. This option is available only when you select Moving Average from the Method list. Resampled signal—Displays the processed time series. This graph displays the resampled time series. This option is available only when you select Resampling from the Method list. Detrended signal—Displays the processed time series. This graph displays the detrended time series. This option is available only when you select Detrending from the Method list. Averaged signal—Displays the processed time series. This graph displays the averaged time series. This option is available only when you select Exponential Average from the Method list. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |
| Xt | Specifies the time series. Xt is available only when you select From terminal in Data Source. |
| File path | Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| error out | Contains error information. This output provides standard error out functionality. |
| Xt filtered | Returns the processed time series. This output returns the filtered time series. This output is available only when you select Moving Average from the Method list in the Time Series Preprocessing dialog box. |
| Xt resampled | Returns the processed time series. This output returns the resampled time series. This output is available only when you select Resampling from the Method list in the Time Series Preprocessing dialog box. |
| Xt detrended | Returns the processed time series. This output returns the detrended time series. This output is available only when you select Detrending from the Method list in the Time Series Preprocessing dialog box. |
| Trend | Returns the trend of the input time series. This output is available only when you select Detrending from the Method list. |
| Xt averaged | Returns the processed time series. This output returns the averaged time series. This output is available only when you select Exponential Average from the Method list in the Time Series Preprocessing dialog box. |

This Express VI operates similarly to the following VIs and functions:

[TSA Detrend](../lvtimeseriestk/tsa_de-trend.html) 

[TSA Exponential Average](../lvtimeseriestk/tsa_exponential_average.html) 

[TSA Moving Average](../lvtimeseriestk/tsa_moving_average.html) 

[TSA Resampling](../lvtimeseriestk/tsa_resampling.html)

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_timeseries_samples.html language=enus -->
## TOPIC 00122: TSA Time Series Samples VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_timeseries_samples.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_timeseries_samples.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### TSA Time Series Samples VI

**Owning Palette:** [Utilities VIs](../lvtimeseriestk/tsa_utilities_vis.html)

**Requires:** Advanced Signal Processing Toolkit

Contains the demonstration data samples for the [Time Series Analysis](../lvtimeseriestk/time_series_analysis_pal.html) VIs.

[Examples](#examples)

[IMAGE alt='image' src='tsa_time_series_samplesc.gif']

|  | data specifies the demonstration data. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | univariate time series returns the univariate time series. |
|  | multivariate time series returns the multivariate (vector) time series. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the TSA Time Series Samples VI:

- Bearing Monitor VI: labview\examples\Time Series Analysis\TSAApplications
- Echo Canceling VI: labview\examples\Time Series Analysis\TSAApplications
- Engine Knocking Monitor VI: labview\examples\Time Series Analysis\TSAApplications
- Modal Analysis of a Plate VI: labview\examples\Time Series Analysis\TSAApplications
- Power Line Monitor VI: labview\examples\Time Series Analysis\TSAApplications

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsa_utilities_vis.html language=enus -->
## TOPIC 00123: Utilities VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsa_utilities_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsa_utilities_vis.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Utilities VIs

**Owning Palette:** [Time Series Analysis VIs](../lvtimeseriestk/time_series_analysis_pal.html)

**Requires:** Advanced Signal Processing Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Utilities VIs to generate time series for demonstration purposes, to perform engineering unit scaling, and to read data files.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Time Series Analysis error codes](tsa_error_code.html).

| Palette Object | Description |
| --- | --- |
| Random Sequence Generation | Generates a random univariate time series from the normal, uniform, chi-square, t, or F distribution. This Express VI also can generate a random multivariate time series from the vector normal distribution. You can plot the histogram of the generated time series in the configuration dialog box. |
| TSA Configure Cepstrogram Indicator | Configures the time-cepstrum of a univariate time series and displays the cepstrogram of the univariate time series on an intensity graph. Wire data to the color table input to determine the polymorphic instance to use or manually select the instance. |
| TSA Get Time and Quefrency Scale Info | Gets the time scale information and the quefrency scale information of the time-quefrency representation. |
| TSA Random Sequence Generation | Generates a pseudorandom univariate or multivariate (vector) time series from different types of distribution. You must manually select the polymorphic instance to use. |
| TSA Read from File | Reads a univariate or multivariate (vector) time series from a specified data file. You can use this VI to read spreadsheet text files and WAV files. |
| TSA Scale to EU | Converts the unit of a univariate or multivariate (vector) time series from volts to an engineering unit (EU). Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. |
| TSA Set Time and Quefrency Scale Info | Sets the time scale information and the quefrency scale information for the time-quefrency representation. |
| TSA Time Series Samples | Contains the demonstration data samples for the Time Series Analysis VIs. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvtimeseriestk/tsacontrolpal.html language=enus -->
## TOPIC 00124: Controls (Advanced Signal Processing Toolkit)

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvtimeseriestk/tsacontrolpal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvtimeseriestk/tsacontrolpal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Controls (Advanced Signal Processing Toolkit)

Use the controls on the **Time Series Controls** palette to display the [cepstrogram](../lvasptconcepts/tsa_time-cepstrum.html) of a univariate time series on an intensity graph.

| Palette Object | Description |
| --- | --- |
| TSA Cepstrogram Indicator | Displays the cepstrogram of a univariate time series on an intensity graph. When you add the TSA Cepstrogram Indicator to the front panel, the TSA Configure Cepstrogram Indicator VI appears on the block diagram with the reference of cepstrogram indicator input and the cepstrogram indicator output already wired. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/discretewaveletpal.html language=enus -->
## TOPIC 00125: Discrete Wavelet VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/discretewaveletpal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/discretewaveletpal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Discrete Wavelet VIs

**Owning Palette:** [Wavelet Analysis VIs](../lvwavelettk/lvwavelettk.html)

**Requires:** Advanced Signal Processing Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Discrete Wavelet VIs to compute the [discrete wavelet transform (DWT)](../lvasptconcepts/wa_dwt.html) or the inverse DWT, to compute the [undecimated wavelet transform (UWT)](../lvasptconcepts/wa_uwt.html) or the inverse UWT, to compute the [integer wavelet transform (IWT)](../lvasptconcepts/wa_iwt.html) or the inverse IWT, to retrieve specific DWT, UWT, and IWT coefficients, and to compute the arbitrary path transform or reconstruction.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Wavelet Analysis error codes](wa_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Arbitrary Path Analysis | Decomposes a signal according to the paths you specify and reconstructs the signal from the corresponding path coefficients. |
| Multiresolution Analysis | Decomposes a signal according to the level you specify and reconstructs the signal from the frequency bands you select. |
| Multiresolution Analysis 2D | Decomposes a 2D image according to the level you specify and reconstructs the 2D image from the frequency bands you select. |
| WA Arbitrary Path Decomposition | Performs subband decomposition by cascading the lowpass analysis filters and the highpass analysis filters and applies a decimation factor of 2 after each filtering step. path specifies the subband and determines how to cascade the lowpass analysis filters and the highpass analysis filters. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. |
| WA Arbitrary Path Reconstruction | Reconstructs a signal with subband coefficients. Wire data to the path coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Discrete Wavelet Transform | Computes the multi-level discrete wavelet transform (DWT) of signal. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input. This VI returns the approximation coefficients and the detail coefficients at all levels for a 2D signal input. This VI computes the DWT at each level by using the lowpass analysis filters, the highpass analysis filters, and a decimation factor of 2. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. |
| WA Get Coefficients of Discrete Wavelet Transform | Retrieves approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT of a signal. Wire data to the DWT coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Get Coefficients of Integer Wavelet Transform | Retrieves approximation or detail integer wavelet transform (IWT) coefficients at a specific level. Use the WA Integer Wavelet Transform VI to compute the IWT of a signal. Wire data to the IWT coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Get Coefficients of Undecimated Wavelet Transform | Retrieves approximation or detail undecimated wavelet transform (UWT) coefficients at a specific level. Use the WA Undecimated Wavelet Transform VI to compute the UWT of a signal. Wire data to the UWT coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Integer Wavelet Transform | Uses the lifting scheme to compute the multi-level integer wavelet transform (IWT) of signal. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input and returns the approximation coefficients and the detail coefficients at all levels for a 2D signal input. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. |
| WA Inverse Discrete Wavelet Transform | Computes the multi-level inverse discrete wavelet transform (DWT) and returns the reconstructed signal from the approximation coefficients and the detail coefficients. An interpolator with a factor 2 and the lowpass synthesis filters and the highpass synthesis filters implement the inverse DWT at each level. Wire data to the DWT coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Inverse Integer Wavelet Transform | Computes the multi-level inverse integer wavelet transform (IWT) and returns the reconstructed signal from the approximation coefficients and the detail coefficients. Wire data to the IWT coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Inverse Undecimated Wavelet Transform | Computes the multi-level inverse undecimated wavelet transform (UWT) and returns the reconstructed signal from the approximation coefficients and the detail coefficients. Wire data to the UWT coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Set Coefficients of Discrete Wavelet Transform | Sets approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT. Use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients. |
| WA Set Coefficients of Integer Wavelet Transform | Sets approximation or detail integer wavelet transform (IWT) coefficients at a specific level. Use the WA Integer Wavelet Transform VI to compute the IWT. Use the WA Get Coefficients of Integer Wavelet Transform VI to obtain the IWT coefficients. |
| WA Set Coefficients of Undecimated Wavelet Transform | Sets approximation or detail undecimated wavelet transform (UWT) coefficients at a specific level. Use the WA Undecimated Wavelet Transform VI to compute the UWT. Use the WA Get Coefficients of Undecimated Wavelet Transform VI to obtain the UWT coefficients. |
| WA Undecimated Wavelet Transform | Computes the multi-level undecimated wavelet transform (UWT) of signal. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input and returns the approximation coefficients and the detail coefficients at all levels for a 2D signal input. The approximation coefficients and the detail coefficients at all levels are the same size as signal. The results of the UWT have the translation invariant property, which is helpful in robust feature extraction and pattern recognition. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. |
| Wavelet Design | Designs customized analysis filters and synthesis filters for discrete wavelet analysis and reconstruction, respectively. |

| Subpalette | Description |
| --- | --- |
| Filter Banks VIs | Use the Filter Banks VIs to apply a two-channel filter bank to compute single-level discrete wavelet transform or synthesis, to compute the mother wavelet function and the scaling function from the filter bank, and to get the coefficients of the analysis filters and the synthesis filters for a predefined wavelet. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/multiresolution_analysis.html language=enus -->
## TOPIC 00126: Multiresolution Analysis Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/multiresolution_analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/multiresolution_analysis.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multiresolution Analysis Express VI

**Owning Palette:** [Discrete Wavelet VIs](../lvwavelettk/discretewaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

[Decomposes a signal](../lvasptconcepts/wa_dwt_mra.html) according to the level you specify and reconstructs the signal from the frequency bands you select.

[Example](#examples)

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Data Source | Specifies whether this Express VI reads data from a block diagram input terminal or from a file. From terminal specifies that this Express VI reads data from a block diagram input terminal. From file specifies that this Express VI reads data from a file. This Express VI can read data from waveform, WAV, or TXT files. The valid format of a TXT data file is a file that contains only a 1D real array. |
| File Path Configuration | Contains the following options: File path—Specifies and displays the path to the file from which this Express VI reads data. This option is available only when you select From file in the Data Source section. Prompt to choose a file each time this VI runs—Specifies whether this Express VI displays a dialog box that prompts you to select a file each time this Express VI runs. This option is available only when you select the From file option in the Data Source section. |
| Original and Reconstructed Signal | Displays the original and reconstructed signal. |
| Wavelet Transform and Subband Selection | Contains the following options: Frequency bands—Specifies the subbands or the parts of subbands to use to reconstruct the signal. The discrete wavelet transform (DWT) decomposes a signal into a series of dyadic frequency subbands. Zoom out—Zooms out the frequency bands near DC, which is the origin of the x-scale of Frequency bands. Zoom in—Zooms in the frequency bands near DC, which is the origin of the x-scale of Frequency bands. Select all—Selects all the frequency bands. Click this button to reconstruct the image from the approximation coefficients and the detail coefficients of all the frequency bands. Levels—Specifies the number of levels in the discrete wavelet analysis. Levels must be a positive integer no greater than log2(Ls), where Ls is the length of the signal. Wavelet—Specifies the wavelet type this Express VI uses for discrete wavelet analysis. The default is db02. You can choose from the following options: Customized Wavelet Haar—Orthogonal dbxx—Orthogonal, Daubechies coifx—Orthogonal, Coiflets symx—Orthogonal, Symmlets biorx_x—Biorthogonal bior4_4 (FBI)—Biorthogonal, FBI where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. Note The orthogonal wavelets are not redundant and therefore are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and therefore are suitable for signal or image feature extraction. |
|  | Note The orthogonal wavelets are not redundant and therefore are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and therefore are suitable for signal or image feature extraction. |
| Functions | Displays the following graphs: Analysis scaling—Displays the scaling function of the analysis filter bank. Analysis wavelet—Displays the mother wavelet of the analysis filter bank. Synthesis scaling—Displays the scaling function of the synthesis filter bank. Synthesis wavelet—Displays the mother wavelet of the synthesis filter bank. |
| Filters | Displays the following graphs: Analysis lowpass (G0)—Displays the coefficients of the lowpass analysis filter G0(z). Analysis highpass (G1)—Displays the coefficients of the highpass analysis filter G1(z). Synthesis lowpass (H0)—Displays the coefficients of the lowpass synthesis filter H0(z). Synthesis highpass (H1)—Displays the coefficients of the highpass synthesis filter H1(z). |
| Parameters Settings | Contains the following options: Note The following options are available only if you select the Customized Wavelet option from the Wavelet pull-down menu. Wavelet Type—Specifies the type of wavelet this Express VI uses to design a customized wavelet for discrete wavelet analysis and reconstruction. You can select the Orthogonal or Biorthogonal option. Product of Lowpass (P0=G0*H0)—Specifies P0, which is the product of the lowpass analysis filter G0 and the lowpass synthesis filter H0. Contains the following options: P0 type—Specifies the type of P0. The default is Maxflat. You can choose from the following options: Maxflat Positive Equiripple General Equiripple Note The General Equiripple option is available only if you select the Biorthogonal option in the Wavelet Type section. Zero pairs at pi (P0)—Specifies the value of p in the Maxflat filter P0(z), where P0(z) = (1+1/z)^(2p)*Q(z). This option is available only if you select the Maxflat option in the P0 type section. # of taps—Specifies the number of coefficients of P0(z). The length of P0(z) must be 4p–1, where p = 2, 3, …. This option is available only if you select the Positive Equiripple or General Equiripple option in the P0 type section. Passband—Specifies the normalized cutoff frequency of P0(z). The value of Passband must be less than 0.5. Passband is available only if you select the Positive Equiripple or General Equiripple option in the P0 type section. Factorization (Type of G0)—Contains the following options: Filter type—Specifies how this Express VI factors P0 to G0 and H0. Contains the following options: Arbitrary—Specifies that no restriction exists on the placement of zeros. Minimum Phase—Specifies that the zeros of G0 are located inside the unit circle, except for the zeros at pi. Linear Phase—Specifies that if one zero belongs to G0(H0), the reciprocal of that zero must belong to G0(H0). B-Spline—Specifies that except for some zeros at pi, all the zeros of P0 belong to H0. Zeros at pi (G0)—Controls how many zeros at z=–1 belong to G0(z). This option is available only if you select the Maxflat option in the P0 type section. The maximum value of this option is 2p, where p = the value of the Zero pairs at pi (P0) option. |
|  | Note The following options are available only if you select the Customized Wavelet option from the Wavelet pull-down menu. |
|  | Note The General Equiripple option is available only if you select the Biorthogonal option in the Wavelet Type section. |
| Zeros of G0 and H0 | Shows the distribution of the zeros of P0(z), G0(z) and H0(z). This Express VI uses this distribution to factor the zeros of P0(z) into the zeros of G0(z) and H0(z). Because the filter coefficients of P0(z) are real, all the zeros of P0(z) are symmetrical with respect to the x-axis. Consequently, this Express VI displays only the upper half of the plane. The zeros on the x-axis represent real-valued roots. The zeros outside of the x-axis represent complex-valued roots. The blue crosses represent the zeros of G0(z), and the red circles represent the zeros of H0(z). Click on the zero you want to select to switch the zero from that of G0(z) to that of H0(z) and vice versa. All the zeros belong to G0(z) or H0(z). Selecting different values for Filter type puts different constraints on the selections of zeros. For example, if you select Linear Phase for Filter type and select a zero for one filter, the filter automatically contains the reciprocal of the zero. Note This section is available only if you select the Customized Wavelet option from the Wavelet pull-down menu. |
|  | Note This section is available only if you select the Customized Wavelet option from the Wavelet pull-down menu. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |
| Signal | Specifies the block diagram terminal of the data you want to load. This input is available only if you select the From terminal option in the Data Source section. |
| File path | Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| Reconstruction | Returns the reconstructed signal. |
| error out | Contains error information. This output provides standard error out functionality. |

This Express VI operates similarly to the following VIs and functions:

[WA Discrete Wavelet Transform](../lvwavelettk/wa_discrete_wavelet_transform.html) 

[WA Inverse Discrete Wavelet Transform](../lvwavelettk/wa_inverse_1d_discrete_wavelet_transform.html)

#### Example

Refer to the Multiresolution Analysis - 1D Signal VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the Multiresolution Analysis Express VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/multiresolution_analysis_2d.html language=enus -->
## TOPIC 00127: Multiresolution Analysis 2D Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/multiresolution_analysis_2d.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/multiresolution_analysis_2d.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multiresolution Analysis 2D Express VI

**Owning Palette:** [Discrete Wavelet VIs](../lvwavelettk/discretewaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

[Decomposes a 2D image](../lvasptconcepts/wa_dwt_2d.html) according to the level you specify and reconstructs the 2D image from the frequency bands you select.

[Example](#examples)

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Signal | Contains the following options: Data Source—Specifies whether this Express VI reads a 2D image from a block diagram input terminal or from a file. Contains the following options: From terminal—Specifies that this Express VI reads data from the Image block diagram input terminal. From file—Specifies that this Express VI reads data from a file. This Express VI can read data from BMP, JPG, and PNG files. File path—Specifies and displays the path to the file from which this Express VI reads data. This option is available only if you select From file in the Data Source section. Prompt to choose a file each time this VI runs—Specifies whether this Express VI displays a dialog box that prompts you to select a file each time this Express VI runs. This option is available only when you select the From file option in the Data Source section. Wavelet Levels and Type—Specifies the wavelet level and wavelet type this Express VI uses for discrete wavelet analysis. Contains the following options: Levels—Specifies the number of levels in the discrete wavelet analysis. Levels must be a positive integer no greater than log2(Ls), where Ls is the minimum dimensional size of the image you want to reconstruct. Wavelet—Specifies the wavelet type this Express VI uses for discrete wavelet analysis. The default is db02. You can choose from the following options: Customized Wavelet—Use the Wavelet Design page to configure a customized wavelet. Haar—Orthogonal dbxx—Orthogonal, Daubechies coifx—Orthogonal, Coiflets symx—Orthogonal, Symmlets biorx_x—Biorthogonal bior4_4 (FBI)—Biorthogonal, FBI where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. Note The orthogonal wavelets are not redundant and therefore are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and therefore are suitable for signal or image feature extraction. Original Image—Displays the original 2D image. Reconstructed Image—Displays the 2D image this Express VI reconstructs according to the Frequency Band Selection you make. If you place a checkmark in the Undecimated checkbox, this Express VI displays an image reconstructed by the wavelet coefficients from the undecimated wavelet transform (UWT). If you remove the checkmark from the Undecimated checkbox, this Express VI displays an image reconstructed by the wavelet coefficients from the discrete wavelet transform (DWT). Frequency Band Selection—Specifies the frequency band(s) this Express VI uses to reconstruct the image. The discrete wavelet transform (DWT) decomposes a signal into a series of dyadic frequency subbands in two directions. Each wavelet level produces the following four subbands: LL approximation—low-low LH detail in column direction—low-high HL detail in row direction—high-low HH detail in diagonal direction—high-high Wavelet Coefficients—Displays the wavelet coefficients of the frequency subband you select. If you place a checkmark in the Undecimated checkbox, this Express VI displays the wavelet coefficients from the undecimated wavelet transform (UWT). If you remove the checkmark from this checkbox, this Express VI displays the wavelet coefficients from the discrete wavelet transform (DWT). Note The Wavelet Coefficients indicator changes depending on the Frequency Band Selection and whether you place a checkmark in the Undecimated checkbox. Undecimated—Specifies whether this Express VI uses the undecimated wavelet transform (UWT) or discrete wavelet transform (DWT) for multiresolution analysis. If you place a checkmark in this checkbox, this Express VI applies UWT to the Original Image and reconstructs an image with the wavelet coefficients of the frequency band(s) you select by using inverse UWT. If you remove the checkmark from this checkbox, this Express VI applies DWT to the Original Image and reconstructs an image with the wavelet coefficients of the frequency band(s) you select by using inverse DWT. Zoom in—Zooms in the frequency bands at the origin of the Frequency Band Selection. Zoom out—Zooms out the frequency bands at the origin of the Frequency Band Selection. Zoom reset—Resets the zoom value of Frequency Band Selection to display all the frequency bands. Select none—Selects none of the frequency bands. If you click this button, the 2D image does not appear. Select all—Selects all the frequency bands. Click this button to reconstruct the image from the approximation coefficients and the detail coefficients of all the frequency bands. |
|  | Note The orthogonal wavelets are not redundant and therefore are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and therefore are suitable for signal or image feature extraction. |
|  | Note The Wavelet Coefficients indicator changes depending on the Frequency Band Selection and whether you place a checkmark in the Undecimated checkbox. |
| Wavelet Design | Designs customized analysis filters and synthesis filters for discrete wavelet analysis and reconstruction, respectively. Contains the following options: Note Except for the Wavelet and Filter Banks section, the following options are valid only if you select the Customized Wavelet option from the Wavelet pull-down menu. Wavelet Type—Specifies the type of wavelet this Express VI uses to design a customized wavelet for discrete wavelet analysis and reconstruction. You can select the Orthogonal or Biorthogonal option. Product of Lowpass (P0=G0*H0)—Specifies P0, which is the product of the lowpass analysis filter G0 and the lowpass synthesis filter H0. Contains the following options: P0 type—Specifies the type of P0. The default is Maxflat. You can choose from the following options: Maxflat Positive Equiripple General Equiripple Note The General Equiripple option is available only if you select the Biorthogonal option in the Wavelet Type section. Zero pairs at pi (P0)—Specifies the value of p in the Maxflat filter P0(z), where P0(z) = (1+1/z)^(2p)*Q(z). This option is available only if you select the Maxflat option in the P0 type section. # of taps—Specifies the number of coefficients of P0(z). The length of P0(z) must be 4p–1, where p = 2, 3, …. This option is available only if you select the Positive Equiripple or General Equiripple option in the P0 type section. Passband—Specifies the normalized cutoff frequency of P0(z). The value of Passband must be less than 0.5. Passband is available only if you select the Positive Equiripple or General Equiripple option in the P0 type section. Factorization (Type of G0)—Contains the following options: Filter type—Specifies how this Express VI factors P0 to G0 and H0. Contains the following options: Arbitrary—Specifies that no restriction exists on the placement of zeros. Minimum Phase—Specifies that the zeros of G0 are located inside the unit circle, except for the zeros at pi. Linear Phase—Specifies that if one zero belongs to G0(H0), the reciprocal of that zero must belong to G0(H0). B-Spline—Specifies that except for some zeros at pi, all the zeros of P0 belong to H0. Zeros at pi (G0)—Controls how many zeros at z=–1 belong to G0(z). This option is available only if you select the Maxflat option in the P0 type section. The maximum value of this option is 2p, where p = the value of the Zero pairs at pi (P0) option. Zeros of G0 and H0—Shows the distribution of the zeros of P0(z), G0(z) and H0(z). This Express VI uses this distribution to factor the zeros of P0(z) into the zeros of G0(z) and H0(z). Because the filter coefficients of P0(z) are real, all the zeros of P0(z) are symmetrical with respect to the x-axis. Consequently, this Express VI displays only the upper half of the plane. The zeros on the x-axis represent real-valued roots. The zeros outside of the x-axis represent complex-valued roots. The blue crosses represent the zeros of G0(z), and the red circles represent the zeros of H0(z). Click on the zero you want to select to switch the zero from that of G0(z) to that of H0(z) and vice versa. All the zeros belong to G0(z) or H0(z). Selecting different values for Filter type puts different constraints on the selections of zeros. For example, if you select Linear Phase for Filter type and select a zero for one filter, the filter automatically contains the reciprocal of the zero. Wavelet and Filter Banks—Displays the following graphs: Analysis scaling—Displays the scaling function of the analysis filter bank. Analysis wavelet—Displays the mother wavelet of the analysis filter bank. Analysis lowpass (G0)—Displays the coefficients of the lowpass analysis filter G0(z). Analysis highpass (G1)—Displays the coefficients of the highpass analysis filter G1(z). Synthesis scaling—Displays the scaling function of the synthesis filter bank. Synthesis wavelet—Displays the mother wavelet of the synthesis filter bank. Synthesis lowpass (H0)—Displays the coefficients of the lowpass synthesis filter H0(z). Synthesis highpass (H1)—Displays the coefficients of the highpass synthesis filter H1(z). Wavelet—Specifies the wavelet type this Express VI uses for discrete wavelet analysis. The default is db02. You can choose from the following options: Customized Wavelet—Use the Wavelet Design page to configure a customized wavelet. Haar—Orthogonal dbxx—Orthogonal, Daubechies coifx—Orthogonal, Coiflets symx—Orthogonal, Symmlets biorx_x—Biorthogonal bior4_4 (FBI)—Biorthogonal, FBI where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. Note The orthogonal wavelets are not redundant and therefore are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and therefore are suitable for signal or image feature extraction. |
|  | Note Except for the Wavelet and Filter Banks section, the following options are valid only if you select the Customized Wavelet option from the Wavelet pull-down menu. |
|  | Note The General Equiripple option is available only if you select the Biorthogonal option in the Wavelet Type section. |
|  | Note The orthogonal wavelets are not redundant and therefore are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and therefore are suitable for signal or image feature extraction. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| File path | Specifies the file path of the 2D image you want to load. This input is available only if you select the From file option in the Data Source section. |
| Image | Specifies the block diagram terminal of the 2D image you want to load. This input is available only if you select the From terminal option in the Data Source section. |
| error in (no error) | Describes error conditions that occur before this node runs. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| Reconstructed Image | Returns the reconstructed image. |
| Selected Coefficients | Returns the wavelet coefficients of the frequency band(s) you select to reconstruct the 2D image. |
| error out | Contains error information. This output provides standard error out functionality. |

This Express VI operates similarly to the following VIs and functions:

[WA Discrete Wavelet Transform](../lvwavelettk/wa_discrete_wavelet_transform.html) 

[WA Inverse Discrete Wavelet Transform](../lvwavelettk/wa_inverse_1d_discrete_wavelet_transform.html)

#### Example

Refer to the Multiresolution Analysis - Image VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the Multiresolution Analysis 2D Express VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_analysis_filter_bank.html language=enus -->
## TOPIC 00128: WA Analysis Filter Bank VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_analysis_filter_bank.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_analysis_filter_bank.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Analysis Filter Bank VI

**Owning Palette:** [Filter Banks VIs](../lvwavelettk/filterbankssubpal.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the single-level [discrete wavelet transform](../lvasptconcepts/wa_dwt.html) (DWT) using a two-channel [analysis filter bank](../lvasptconcepts/wa_discrete.html#filter_banks). This VI decomposes the signal into the low-frequency subband (**approx coef**) and the high-frequency subband (**detail coef**). Both subbands have half the sampling rate of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### WA 1D Analysis Filter Bank (Waveform)

[IMAGE alt='image' src='wa_1d_analysis_filter_bank_(waveform)c.gif']

|  | extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. 0Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| --- | --- |
| 0 | Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the input signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters. You can use the WA Wavelet Filter VI to obtain the filters of commonly used wavelets. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | shift specifies the index where decimation starts after this VI filters the signal. shift must be 0 or 1. |
|  | approx coef returns the approximation coefficients, which are the output of the lowpass analysis filter followed by a decimation factor of 2. |
|  | detail coef returns the detail coefficients, which are the output of the highpass analysis filter followed by a decimation factor of 2. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA 1D Analysis Filter Bank (Array)

[IMAGE alt='image' src='wa_1d_analysis_filter_bank_(array)c.gif']

|  | extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. 0Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| --- | --- |
| 0 | Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the input signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters. You can use the WA Wavelet Filter VI to obtain the filters of commonly used wavelets. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | shift specifies the index where decimation starts after this VI filters the signal. shift must be 0 or 1. |
|  | approx coef returns the approximation coefficients, which are the output of the lowpass analysis filter followed by a decimation factor of 2. |
|  | detail coef returns the detail coefficients, which are the output of the highpass analysis filter followed by a decimation with a factor of 2. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA 2D Analysis Filter Bank

[IMAGE alt='image' src='wa_2d_analysis_filter_bankc.gif']

|  | extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. 0Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| --- | --- |
| 0 | Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the 2D input signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters. You can use the WA Wavelet Filter VI to obtain the filters of commonly used wavelets. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | shift specifies the index where decimation starts after this VI filters the signal. shift must be 0 or 1. |
|  | DWT coef returns the approximation coefficients and the detail coefficients from the 2D single-level discrete wavelet transform (DWT). low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. |
|  | low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. |
|  | high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. |
|  | high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the WA Analysis Filter Bank VI:

- Filter Banks - 1D VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Filter Banks - 2D VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Order Selection VI: labview\examples\Wavelet Analysis\WAGettingStarted

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_analytic_wavelet_transform.html language=enus -->
## TOPIC 00129: WA Analytic Wavelet Transform VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_analytic_wavelet_transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_analytic_wavelet_transform.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Analytic Wavelet Transform VI

**Owning Palette:** [Continuous Wavelet VIs](../lvwavelettk/continuouswaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

Uses the complex-valued Morlet wavelet to compute the [continuous wavelet transform (CWT)](../lvasptconcepts/wa_cwt.html) of a 1D input signal. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

The [analytic wavelet transform (AWT)](../lvasptconcepts/wa_awt.html) also is known as the complex wavelet transform.

[Details](#details)  [Examples](#examples)

#### WA Analytic Wavelet Transform (Waveform)

[IMAGE alt='image' src='wa_analytic_wavelet_transform_(waveform)c.gif']

|  | normalization specifies how to scale the dilated wavelets. 0energy (default)—Specifies that the wavelets have a unified energy in all scales.1amplitude—Specifies that wavelets at different scales have the same maximum amplitude of frequency response. |
| --- | --- |
| 0 | energy (default)—Specifies that the wavelets have a unified energy in all scales. |
| 1 | amplitude—Specifies that wavelets at different scales have the same maximum amplitude of frequency response. |
|  | time steps specifies the number of samples to translate, or shift, the wavelet in the analytic wavelet transform (AWT). The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 coefficients exist at each scale. The number of rows in the output wavelet coefficients equals the signal length divided by time steps. National Instruments recommends that you set time steps such that the number of rows in the wavelet coefficients does not exceed 512. If you specify a small value for time steps, this VI might return a large number of wavelet coefficients, which requires a long computation time and more memory. If you need a small time step to observe more details and the signal length is large, divide the signal into smaller segments and compute the wavelet coefficients for each segment. If the signal is oversampled, you can downsample the signal. time steps must be greater than 0, or this VI sets time steps to the default value –1 automatically. |
|  | signal specifies the input signal. |
|  | scales specifies the number of scales of the dilated wavelet. |
|  | scale sampling method specifies the method to use to select the scales of the wavelets. scale sampling method affects the mapping style of the y-axis of the scalogram. Use the user defined scales input to specify a customized scale. 0even frequency (default)—This VI computes the continuous wavelet transform (CWT) such that the center frequencies of the wavelets at the analyzed scales evenly sample the frequency range from 0 to sampling rate/2. The central frequency of a wavelet is inversely proportional to the scale. The resulting scalogram is a kind of joint time-frequency representation with an adaptive time-frequency resolution.1even scale—This VI computes the CWT at positive integer scales 1, 2, 3, ..., scales. |
| 0 | even frequency (default)—This VI computes the continuous wavelet transform (CWT) such that the center frequencies of the wavelets at the analyzed scales evenly sample the frequency range from 0 to sampling rate/2. The central frequency of a wavelet is inversely proportional to the scale. The resulting scalogram is a kind of joint time-frequency representation with an adaptive time-frequency resolution. |
| 1 | even scale—This VI computes the CWT at positive integer scales 1, 2, 3, ..., scales. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | user defined scales specifies the scales to use to compute AWT coef. The scale must be positive and no greater than the length of signal. If you specify a value for user defined scales, this VI ignores the settings in the scale sampling method input and the scales input. |
|  | AWT coef returns the results of the analytic wavelet transform (AWT). The element in the ith column and the jth row is the result of the AWT at the (i+1)th scale with a translation of j×time steps. When you use user defined scales to define the scales of the AWT, the element in the ith column and the jth row is the result of the AWT, where scale (a) equals the ith element of user defined scales and shift () equals j×time steps. The squared magnitude of AWT coef is the scalogram, which jointly represents a signal in terms of time and scale. Large scales correspond to low frequencies, and small scales correspond to high frequencies. Use the WA Scalogram Indicator to display the scalogram on an intensity graph. |
|  | scale info returns the time information and the scale (frequency) information, which this VI uses in the scalogram plot. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Analytic Wavelet Transform (Array)

[IMAGE alt='image' src='wa_analytic_wavelet_transform_(array)c.gif']

|  | normalization specifies how to scale the dilated wavelets. 0energy (default)—Specifies that the wavelets have a unified energy in all scales.1amplitude—Specifies that wavelets at different scales have the same maximum amplitude of frequency response. |
| --- | --- |
| 0 | energy (default)—Specifies that the wavelets have a unified energy in all scales. |
| 1 | amplitude—Specifies that wavelets at different scales have the same maximum amplitude of frequency response. |
|  | time steps specifies the number of samples to translate, or shift, the wavelet in the analytic wavelet transform (AWT). The default is –1, which specifies that this VI adjusts time steps automatically so that no more than 512 coefficients exist at each scale. The number of rows in the output wavelet coefficients equals the signal length divided by time steps. National Instruments recommends that you set time steps such that the number of rows in the wavelet coefficients does not exceed 512. If you specify a small value for time steps, this VI might return a large number of wavelet coefficients, which requires a long computation time and more memory. If you need a small time step to observe more details and the signal length is large, divide the signal into smaller segments and compute the wavelet coefficients for each segment. If the signal is oversampled, you can downsample the signal. time steps must be greater than 0, or this VI sets time steps to the default value –1 automatically. |
|  | signal specifies the input signal. |
|  | scales specifies the number of scales of the dilated wavelet. |
|  | scale sampling method specifies the method to use to select the scales of the wavelets. scale sampling method affects the mapping style of the y-axis of the scalogram. Use the user defined scales input to specify a customized scale. 0even frequency (default)—This VI computes the continuous wavelet transform (CWT) such that the center frequencies of the wavelets at the analyzed scales evenly sample the frequency range from 0 to sampling rate/2. The central frequency of a wavelet is inversely proportional to the scale. The resulting scalogram is a kind of joint time-frequency representation with an adaptive time-frequency resolution.1even scale—This VI computes the CWT at positive integer scales 1, 2, 3, ..., scales. |
| 0 | even frequency (default)—This VI computes the continuous wavelet transform (CWT) such that the center frequencies of the wavelets at the analyzed scales evenly sample the frequency range from 0 to sampling rate/2. The central frequency of a wavelet is inversely proportional to the scale. The resulting scalogram is a kind of joint time-frequency representation with an adaptive time-frequency resolution. |
| 1 | even scale—This VI computes the CWT at positive integer scales 1, 2, 3, ..., scales. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | user defined scales specifies the scales to use to compute AWT coef. The scale must be positive and no greater than the length of signal. If you specify a value for user defined scales, this VI ignores the settings in the scale sampling method input and the scales input. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | AWT coef returns the results of the analytic wavelet transform (AWT). The element in the ith column and the jth row is the result of the AWT at the (i+1)th scale with a translation of j×time steps. When you use user defined scales to define the scales of the AWT, the element in the ith column and the jth row is the result of the AWT, where scale (a) equals the ith element of user defined scales and shift () equals j×time steps. The squared magnitude of AWT coef is the scalogram, which jointly represents a signal in terms of time and scale. Large scales correspond to low frequencies, and small scales correspond to high frequencies. Use the WA Scalogram Indicator to display the scalogram on an intensity graph. |
|  | scale info returns the time information and the scale (frequency) information, which this VI uses in the scalogram plot. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Analytic Wavelet Transform Details

The AWT is a special case of the CWT with the complex-valued Morlet wavelet, also called the Gabor wavelet. The following equation defines the complex-valued Morlet wavelet:

[IMAGE alt='image' src='eq_morlet.gif']

where [IMAGE alt='image' src='sigma.gif'] is the standard deviation of the Gaussian envelope of the mother wavelet, and [IMAGE alt='image' src='eq_central_freq.gif'] is the central frequency of the mother wavelet, which is [IMAGE alt='image' src='eq_threehalves_pi.gif'] in this VI.

#### Scale and Frequency

The following illustration shows the real parts of the complex-valued Morlet wavelet. The scales and shifts, (*a*, [IMAGE alt='image' src='eq_shift.gif']), are (16, 100), (32, 200), and (64, 300) respectively.

[IMAGE alt='image' src='awt_wavelet.gif']

The following illustration shows the Fourier transforms of the previous complex-valued Morlet wavelet:

[IMAGE alt='image' src='awt_fft.gif']

From the above illustrations, you can see that the center frequency of the scaled wavelet is inversely proportional to the scale *a*.

The Fourier transform of [IMAGE alt='image' src='eq_fourier_trans1.gif'] is [IMAGE alt='image' src='eq_fourier_trans2.gif'], where [IMAGE alt='image' src='eq_fourier_trans3.gif'] is the Fourier transform of the mother wavelet. Therefore, the center frequency of the scaled wavelet is [IMAGE alt='image' src='eq_scaled_cent_freq.gif']. You can use the AWT to analyze the frequency content of a signal by selecting a set of scales.

#### Examples

Refer to the following VIs for examples of using the WA Analytic Wavelet Transform VI:

- Scalogram with Analytic Wavelet Transform VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Spectrogram Ridge Detection VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Color Tables for Displaying the Scalogram VI: labview\examples\Wavelet Analysis\WAGettingStarted

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_discrete_wavelet_transform.html language=enus -->
## TOPIC 00130: WA Discrete Wavelet Transform VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_discrete_wavelet_transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_discrete_wavelet_transform.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Discrete Wavelet Transform VI

**Owning Palette:** [Discrete Wavelet VIs](../lvwavelettk/discretewaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the multi-level [discrete wavelet transform (DWT)](../lvasptconcepts/wa_dwt.html) of **signal**. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input. This VI returns the approximation coefficients and the detail coefficients at all levels for a 2D signal input. This VI computes the DWT at each level by using the lowpass analysis filters, the highpass analysis filters, and a decimation factor of 2. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Examples](#examples)

#### WA 1D Discrete Wavelet Transform (Waveform)

[IMAGE alt='image' src='wa_1d_discrete_wavelet_transform_(waveform)c.gif']

|  | extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. 0Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| --- | --- |
| 0 | Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the input signal. |
|  | levels specifies the number of levels in the discrete wavelet analysis. levels must be a positive integer no greater than log2(Ls), where Ls is the length of the 1D signal or the minimum dimensional size of the 2D signal. Otherwise, you can set the value to –1, which indicates that this VI sets levels as the largest integer no greater than log2(Ls). The default is –1. |
|  | wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. The orthogonal wavelets are not redundant and are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and are suitable for signal or image feature extraction. If you want to use other types of wavelets, do not wire this input. Instead, use the Wavelet Design Express VI to design the wavelet you want and wire the resulting analysis filters to the analysis filters input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. If you specify a value for analysis filters, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | DWT coef returns the approximation coefficients and the detail coefficients from the multi-level discrete wavelet decomposition. This VI concatenates the coefficients into a waveform starting with the approximation coefficients at the largest level followed by the detail coefficients at all levels in descending order. You can use the WA Get Coefficients of Discrete Wavelet Transform VI to read the approximation coefficients or detail coefficients at a specific level. Wire DWT coef to the DWT coef input of the WA Get Coefficients of Discrete Wavelet Transform VI. |
|  | length returns, in a 1D array, the number of approximation and detail coefficients at each level. At a decomposition level of N, length is equal to N+2. The first element of length always is equal to the number of approximation coefficients. The last element of length indicates the total number of raw data samples. The length of the detail coefficients is arranged in descending order. You can use the WA Get Coefficients of Discrete Wavelet Transform VI to read the approximation coefficients or detail coefficients at a specific level. Wire length to the length input of the WA Get Coefficients of Discrete Wavelet Transform VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA 1D Discrete Wavelet Transform (Array)

[IMAGE alt='image' src='wa_1d_discrete_wavelet_transform_(array)c.gif']

|  | extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. 0Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| --- | --- |
| 0 | Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the input signal. |
|  | levels specifies the number of levels in the discrete wavelet analysis. levels must be a positive integer no greater than log2(Ls), where Ls is the length of the 1D signal or the minimum dimensional size of the 2D signal. Otherwise, you can set the value to –1, which indicates that this VI sets levels as the largest integer no greater than log2(Ls). The default is –1. |
|  | wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. The orthogonal wavelets are not redundant and are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and are suitable for signal or image feature extraction. If you want to use other types of wavelets, do not wire this input. Instead, use the Wavelet Design Express VI to design the wavelet you want and wire the resulting analysis filters to the analysis filters input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. If you specify a value for analysis filters, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | DWT coef returns the approximation coefficients and the detail coefficients from the multi-level discrete wavelet decomposition. This VI concatenates the coefficients into a array starting with the approximation coefficients at the largest level followed by the detail coefficients at all levels in descending order. You can use the WA Get Coefficients of Discrete Wavelet Transform VI to read the approximation coefficients or detail coefficients at a specific level. Wire DWT coef to the DWT coef input of the WA Get Coefficients of Discrete Wavelet Transform VI. |
|  | length returns, in a 1D array, the number of approximation and detail coefficients at each level. At a decomposition level of N, length is equal to N+2. The first element of length always is equal to the number of approximation coefficients. The last element of length indicates the total number of raw data samples. The length of the detail coefficients is arranged in descending order. You can use the WA Get Coefficients of Discrete Wavelet Transform VI to read the approximation coefficients or detail coefficients at a specific level. Wire length to the length input of the WA Get Coefficients of Discrete Wavelet Transform VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA 2D Discrete Wavelet Transform

[IMAGE alt='image' src='wa_2d_discrete_wavelet_transformc.gif']

|  | extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. 0Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition.1Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end.2Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
| --- | --- |
| 0 | Zero padding—Uses zeros to pad the input data. Watch for abrupt transitions between the padded zeros and the input data, which causes large artifacts near the transition. |
| 1 | Symmetric (default)—Uses replications of the input data to pad the data, except that this VI left-flips the block at the input and right-flips the block at the end. |
| 2 | Periodic—Adds a replication of the input data block before and another replication after the input data block to pad the data. |
|  | signal specifies the 2D input signal. |
|  | levels specifies the number of levels in the discrete wavelet analysis. levels must be a positive integer no greater than log2(Ls), where Ls is the length of the 1D signal or the minimum dimensional size of the 2D signal. Otherwise, you can set the value to –1, which indicates that this VI sets levels as the largest integer no greater than log2(Ls). The default is –1. |
|  | wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. The orthogonal wavelets are not redundant and are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and are suitable for signal or image feature extraction. If you want to use other types of wavelets, do not wire this input. Instead, use the Wavelet Design Express VI to design the wavelet you want and wire the resulting analysis filters to the analysis filters input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. If you specify a value for analysis filters, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | DWT coef returns the approximation coefficients and the detail coefficients from the multi-level discrete wavelet transform (DWT). Each element of the array contains the 2D DWT results of one level. The ith element stores the approximation coefficients and the detail coefficients at level i+1. You can use the WA Get Coefficients of Discrete Wavelet Transform VI to read the approximation coefficients or detail coefficients at a specific level. Wire DWT coef to the DWT coef input of the WA Get Coefficients of Discrete Wavelet Transform VI. low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. |
|  | low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. |
|  | high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. |
|  | high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Discrete Wavelet Transform Details

The following illustration shows an example of a three-level discrete wavelet decomposition, where you set the **levels** input of this VI to 3. The length of the input signal is 16 points.

[IMAGE alt='image' src='disc_wvlet_transform.gif']

*G*<sub>1</sub>(*z*) denotes that the signal passes through a highpass filter. *G*<sub>0</sub>(*z*) denotes that the signal passes through a lowpass filter. *G*<sub>1</sub>(*z*) and *G*<sub>0</sub>(*z*) form the [analysis filter bank](../lvasptconcepts/wa_discrete.html#filter_banks). [IMAGE alt='image' src='eq_decimate_by_2.gif'] denotes a decimation on the signal with a factor of 2.

Using information in the previous illustration, you can see that the **DWT coef** output contains the approximation coefficients of the largest level and the details coefficients of each level. You also can see that the **length** output of this VI contains the following elements, where the last element is the length of the input signal:

[IMAGE alt='image' src='lengths_elements.gif']

#### 2D Discrete Wavelet Transform

You easily can extend the 1D discrete wavelet decomposition and reconstruction to 2D signal processing. At each level, this VI implements the 1D DWT on each row signal. Then, this VI applies the 1D DWT to each column of the preceding output. This VI implements the inverse transform with the reverse operation. The following illustration shows the filter bank implementation for a 2D DWT.

[IMAGE alt='image' src='2d_disc_wvlet_transform.gif']

**low_low** is the approximation of the input 2D signal at a larger scale. **low_high**, **high_low**, and **high_high** correspond to the detail information along the column, row, and diagonal directions.

The following illustrations show an image fed into the 2D DWT and the resulting **DWT coef**.

[IMAGE alt='image' src='dwt_image_new.gif']

[IMAGE alt='image' src='dwt_coef_image_new.gif']

Notice that the maxima (white points) and the minima (black points) of **low_high** are located around the column edges, the maxima and the minima of **high_low** are near the row edges, and the maxima and the minima of **high_high** are near the diagonal edges. Refer to [A Wavelet Tour of Signal Processing](../lvasptconcepts/aspt_related_doc.html) for more information about the DWT.

#### Examples

Refer to the following VIs for examples of using the WA Discrete Wavelet Transform VI:

- Image Compression VI: labview\examples\Wavelet Analysis\WAApplications
- Get and Set Single Level Detail Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Transform and Reconstruction with Image VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Piece Polynomial Function Approx and Comp VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Multiscale Analysis VI: labview\examples\Wavelet Analysis\WAApplications
- Get and Set Approximation Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- ECG Compression VI: labview\examples\Wavelet Analysis\WAApplications

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_getiwtcoef.html language=enus -->
## TOPIC 00131: WA Get Coefficients of Integer Wavelet Transform VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_getiwtcoef.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_getiwtcoef.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Get Coefficients of Integer Wavelet Transform VI

**Owning Palette:** [Discrete Wavelet VIs](../lvwavelettk/discretewaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

Retrieves approximation or [detail integer wavelet transform](../lvasptconcepts/wa_iwt.html) (IWT) coefficients at a specific level. Use the [WA Integer Wavelet Transform](../lvwavelettk/wa_integer_wavelet_transform.html) VI to compute the IWT of a signal. Wire data to the **IWT coef** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### WA Get Coefficients of 1D Integer Wavelet Transform

[IMAGE alt='image' src='wa_get_coefficients_of_1d_integer_wavelet_transformc.gif']

|  | coef type specifies whether this VI returns approximation coefficients or detail coefficients. The default is Approximation coefficients. |
| --- | --- |
|  | IWT coef specifies the approximation coefficients and the detail coefficients from the multi-level integer wavelet transform (IWT). You must organize the coefficients into a 1D integer array starting with the approximation coefficients at the largest level followed by the detail coefficients at all levels in descending order. If you use the WA Integer Wavelet Transform VI to compute the IWT, wire the IWT coef output of the WA Integer Wavelet Transform VI to the IWT coef input of this VI. |
|  | length specifies, in a 1D array, the number of approximation and detail coefficients at each level. At a decomposition level of N, length is equal to N+2. The first element of length always is equal to the number of approximation coefficients. The last element of length indicates the total number of raw data samples. You must arrange the length of the detail coefficients in descending order. If you use the WA Integer Wavelet Transform VI to compute the IWT, wire the length output of the WA Integer Wavelet Transform VI to the length input of this VI. |
|  | coef level specifies the coefficient level this VI returns. The coef level must be between 1 and the largest level of the detail coefficients. The levels in the WA Integer Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI returns the coefficients at level 1. If coef type is Approximation coefficients, this VI ignores coef level. If coef type is Detail coefficients, this VI returns the coefficients at the level you specify in coef level. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | IWT coef out returns IWT coef unchanged. |
|  | length out returns length unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | selected IWT coef returns the integer wavelet transform (IWT) coefficients at the coefficient level coef level of the coefficient type coef type. |

#### WA Get Coefficients of 2D Integer Wavelet Transform

[IMAGE alt='image' src='wa_get_coefficients_of_2d_integer_wavelet_transformc.gif']

|  | coef type specifies the coefficient type this VI returns. 0low_low (default)—Specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal.1low_high—Specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients.2high_low—Specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients.3high_high—Specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
| --- | --- |
| 0 | low_low (default)—Specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. |
| 1 | low_high—Specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. |
| 2 | high_low—Specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. |
| 3 | high_high—Specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | IWT coef specifies the approximation coefficients and the detail coefficients from the multi-level integer wavelet transform (IWT). Each element of the array contains the 2D IWT results of one level. The ith element stores the approximation coefficients and the detail coefficients at level i+1. If you use the WA Integer Wavelet Transform VI to compute the IWT, wire the IWT coef output of the WA Integer Wavelet Transform VI to the IWT coef input of this VI. low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. |
|  | low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. |
|  | high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. |
|  | high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | coef level specifies the coefficient level this VI returns. The coef level must be between 1 and the largest level of the coefficients. The levels in the WA Integer Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI returns the coefficients at level 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | IWT coef out returns IWT coef unchanged. low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. |
|  | low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. |
|  | low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. |
|  | high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. |
|  | high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | selected IWT coef returns the integer wavelet transform (IWT) coefficients at the coefficient level coef level of the coefficient type coef type. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_multiscale_peak_detection.html language=enus -->
## TOPIC 00132: WA Multiscale Peak Detection VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_multiscale_peak_detection.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_multiscale_peak_detection.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Multiscale Peak Detection VI

**Owning Palette:** [Feature Extraction VIs](../lvwavelettk/waveletapplicationpal.html)

**Requires:** Advanced Signal Processing Toolkit

Uses [multiresolution wavelet analysis](../lvasptconcepts/wa_dwt_mra.html) to detect peaks or valleys in a **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

|  | Note Use this VI for offline wavelet analysis. To detect peaks or valleys in a streaming signal, use the WA Online Multiscale Peak Detection VI. |
| --- | --- |

[Details](#details)  [Examples](#examples)

#### WA Multiscale Peak Detection (Waveform)

[IMAGE alt='image' src='wa_multiscale_peak_detection_(waveform).gif']

|  | peaks/valleys specifies whether this VI looks for peaks or valleys in the signal. The default is peaks. |
| --- | --- |
|  | signal specifies the input signal. |
|  | threshold specifies the threshold this VI uses to reject peaks or valleys of a particular size. If this VI looks for peaks, this VI ignores peaks with a peak amplitude less than threshold. If this VI looks for valleys, this VI ignores valleys with a valley amplitude greater than threshold. If detrend? is TRUE, this VI rejects peaks or valleys below the threshold in the detrended signal. If detrend? is FALSE, this VI rejects peaks or valleys below the threshold in the signal. |
|  | width specifies the width, in number of samples, of the peaks or valleys. This VI coerces the value to a power of 2. Refer to the Details section for more information about how this VI uses width to control the decomposition level. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | detrend settings specifies the settings this VI uses to remove the trend from the signal. detrend? specifies whether this VI removes the trend from the signal. The default is FALSE, which means this VI does not remove the trend. threshold frequency specifies the upper frequency limit, in hertz, of the trend that this VI removes from the signal. The threshold frequency determines the wavelet transform level. The wavelet transform level specifies the number of levels in the discrete wavelet analysis. The wavelet transform level is floor(log2[sampling rate/(2*threshold frequency)]). The floor function rounds a value to the nearest integer towards negative infinity. The default is –1, which means this VI sets the threshold frequency automatically. |
|  | detrend? specifies whether this VI removes the trend from the signal. The default is FALSE, which means this VI does not remove the trend. |
|  | threshold frequency specifies the upper frequency limit, in hertz, of the trend that this VI removes from the signal. The threshold frequency determines the wavelet transform level. The wavelet transform level specifies the number of levels in the discrete wavelet analysis. The wavelet transform level is floor(log2[sampling rate/(2*threshold frequency)]). The floor function rounds a value to the nearest integer towards negative infinity. The default is –1, which means this VI sets the threshold frequency automatically. |
|  | number of peaks returns the number of peaks or valleys this VI detects. |
|  | location returns the locations of the peaks or valleys this VI detects. |
|  | amplitude returns the amplitudes of the peaks or valleys this VI detects. |
|  | peak plot returns the signal and the peaks or valleys this VI detects. If detrend? is TRUE, peak plot also returns the trend of the input signal. You can plot this information on an XY graph. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Multiscale Peak Detection (Array)

[IMAGE alt='image' src='wa_multiscale_peak_detection_(array).gif']

|  | peaks/valleys specifies whether this VI looks for peaks or valleys in the signal. The default is peaks. |
| --- | --- |
|  | signal specifies the input signal. |
|  | threshold specifies the threshold this VI uses to reject peaks or valleys of a particular size. If this VI looks for peaks, this VI ignores peaks with a peak amplitude less than threshold. If this VI looks for valleys, this VI ignores valleys with a valley amplitude greater than threshold. If detrend? is TRUE, this VI rejects peaks or valleys below the threshold in the detrended signal. If detrend? is FALSE, this VI rejects peaks or valleys below the threshold in the signal. |
|  | width specifies the width, in number of samples, of the peaks or valleys. This VI coerces the value to a power of 2. Refer to the Details section for more information about how this VI uses width to control the decomposition level. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | detrend settings specifies the settings this VI uses to remove the trend from the signal. detrend? specifies whether this VI removes the trend from the signal. The default is FALSE, which means this VI does not remove the trend. threshold frequency specifies the upper frequency limit, in hertz, of the trend that this VI removes from the signal. The threshold frequency determines the wavelet transform level. The wavelet transform level specifies the number of levels in the discrete wavelet analysis. The wavelet transform level is floor(log2[sampling rate/(2*threshold frequency)]). The floor function rounds a value to the nearest integer towards negative infinity. The default is –1, which means this VI sets the threshold frequency automatically. |
|  | detrend? specifies whether this VI removes the trend from the signal. The default is FALSE, which means this VI does not remove the trend. |
|  | threshold frequency specifies the upper frequency limit, in hertz, of the trend that this VI removes from the signal. The threshold frequency determines the wavelet transform level. The wavelet transform level specifies the number of levels in the discrete wavelet analysis. The wavelet transform level is floor(log2[sampling rate/(2*threshold frequency)]). The floor function rounds a value to the nearest integer towards negative infinity. The default is –1, which means this VI sets the threshold frequency automatically. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | number of peaks returns the number of peaks or valleys this VI detects. |
|  | location returns the locations of the peaks or valleys this VI detects. |
|  | amplitude returns the amplitudes of the peaks or valleys this VI detects. |
|  | peak plot returns the signal and the peaks or valleys this VI detects. If detrend? is TRUE, peak plot also returns the trend of the input signal. You can plot this information on an XY graph. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Multiscale Peak Detection Details

This VI executes the following steps to detect peaks by using a wavelet-based method.

1. Calculates the undecimated wavelet transform (UWT) level based on the width and the UWT level based on the threshold frequency , separately. This VI chooses the greater UWT level from the two results to control the decomposition level.
2. Performs UWT on the input signal by using the biorthogonal wavelet bior3_1 and the greater UWT level calculated in step 1.
3. Searches for zero-crossing points in the detail coefficients at all levels.
4. Selects the zero-crossing points at the largest scale as the coarse estimation of the real peaks.
5. Searches the finer scale for the corresponding nearest zero-crossing point for each detected point.
6. Repeats step 5 until this VI reaches the finest scale, which is the first level.

#### Examples

Refer to the following VIs for examples of using the WA Multiscale Peak Detection VI:

- Breakdown Point Detection VI: labview\examples\Wavelet Analysis\WAApplications
- ECG QRS Complex Detection VI: labview\examples\Wavelet Analysis\WAApplications
- Peak Detection (Wavelet vs. Normal) VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Peak Detection in a Signal with Baseline Wandering VI: labview\examples\Wavelet Analysis\WAGettingStarted

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_multiscale_ridge_detection.html language=enus -->
## TOPIC 00133: WA Multiscale Ridge Detection VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_multiscale_ridge_detection.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_multiscale_ridge_detection.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Multiscale Ridge Detection VI

**Owning Palette:** [Feature Extraction VIs](../lvwavelettk/waveletapplicationpal.html)

**Requires:** Advanced Signal Processing Toolkit

Detects ridges by extracting peaks of each row of a **signal**.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='wa_multiscale_ridge_detectionc.gif']

|  | local threshold? specifies the method to use to choose the threshold. If local threshold? is TRUE, this VI sets the threshold for each row of the signal. If local threshold? is FALSE, this VI uses the global threshold. The default is FALSE. |
| --- | --- |
|  | signal specifies the 2D input signal. |
|  | threshold ratio specifies the threshold to reject small peaks. The threshold equals (Max–Min)×threshold ratio+Min, where Max and Min are the maximum and minimum value of the signal, respectively. threshold ratio must be between 0 and 1. |
|  | width specifies the width, in samples, of the peaks of each row of signal. This VI coerces the value to a power of 2. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | ridge returns the ridges this VI detects. ridge has the same dimensions as signal. The values in ridge are 0 or 1, where 1 indicates that a peak exists at the location along the row direction. Use an intensity graph to display the ridges. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Multiscale Ridge Detection Details

You usually can characterize the ridges of the 2D input signal by the peaks in each row. Therefore, this VI carries out the robust peak detection using the wavelet-based method on each row. All detected peaks form the ridges. For signals with ridges parallel to the row direction, you can detect the ridges from the transposed 2D signals.

#### Example

Refer to the Spectrogram Ridge Detection VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA Multiscale Ridge Detection VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_online_detrend.html language=enus -->
## TOPIC 00134: WA Online Detrend VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_online_detrend.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_online_detrend.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Online Detrend VI

**Owning Palette:** [Online Wavelet Analysis VIs](../lvwavelettk/wa_onlinewaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

Removes the trend from 1D streaming signals by setting the approximation coefficients to zeros. Wire data to the **signal** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

|  | Note Use this VI to remove the trend from streaming signals. For offline wavelet analysis, use the WA Detrend VI. |
| --- | --- |

[Example](#examples)

#### WA Online Detrend (Waveform)

[IMAGE alt='image' src='wa_online_detrend_(waveform).gif']

|  | initialize? specifies whether to initialize the internal state of the block of data to zero. The default is FALSE. When the value is TRUE, this VI initializes the internal state to zero and processes one block of data. When the value is FALSE, this VI initializes the internal states to the final states by using the previous call to this VI instance.To process consecutive blocks of data, set initialize? to TRUE for the first block and FALSE for all other blocks of data. |
| --- | --- |
|  | signal specifies the input signal. |
|  | threshold frequency specifies the upper frequency limit, in hertz, of the trend that this VI removes from the signal. The threshold frequency determines the wavelet transform level. The wavelet transform level specifies the number of levels in the discrete wavelet analysis, where more levels result in a longer delay when you run this VI. The wavelet transform level is floor(log2[sampling rate/(2*threshold frequency)]). The floor function rounds a value to the nearest integer towards negative infinity. The default is –1, which means this VI sets the threshold frequency as sampling rate/4. |
|  | wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. The orthogonal wavelets are not redundant and are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and are suitable for signal or image feature extraction. If you want to use other types of wavelets, do not wire this input. Instead, use the Wavelet Design Express VI to design the wavelet you want, bundle the resulting analysis and synthesis filters, and then wire them to the filter banks input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | filter banks specifies the analysis filter banks and the synthesis filter banks for the wavelet you specify. If you specify a value for filter banks, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
|  | lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. |
|  | highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
|  | detrended signal returns the signal without the trend. |
|  | trend signal returns the residual trend of the signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Online Detrend (Array)

[IMAGE alt='image' src='wa_online_detrend_(array).gif']

|  | initialize? specifies whether to initialize the internal state of the block of data to zero. The default is FALSE. When the value is TRUE, this VI initializes the internal state to zero and processes one block of data. When the value is FALSE, this VI initializes the internal states to the final states by using the previous call to this VI instance.To process consecutive blocks of data, set initialize? to TRUE for the first block and FALSE for all other blocks of data. |
| --- | --- |
|  | signal specifies the input signal. |
|  | threshold frequency specifies the upper frequency limit, in hertz, of the trend that this VI removes from the signal. The threshold frequency determines the wavelet transform level. The wavelet transform level specifies the number of levels in the discrete wavelet analysis, where more levels result in a longer delay when you run this VI. The wavelet transform level is floor(log2[sampling rate/(2*threshold frequency)]). The floor function rounds a value to the nearest integer towards negative infinity. The default is –1, which means this VI sets the threshold frequency as sampling rate/4. |
|  | wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. The orthogonal wavelets are not redundant and are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and are suitable for signal or image feature extraction. If you want to use other types of wavelets, do not wire this input. Instead, use the Wavelet Design Express VI to design the wavelet you want, bundle the resulting analysis and synthesis filters, and then wire them to the filter banks input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | filter banks specifies the analysis filter banks and the synthesis filter banks for the wavelet you specify. If you specify a value for filter banks, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
|  | analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. |
|  | highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
|  | synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
|  | lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. |
|  | highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
|  | sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. |
|  | detrended signal returns the signal without the trend. |
|  | trend signal returns the residual trend of the signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Online Detrend and Trend Estimation VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA Online Detrend VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_setdwtcoef.html language=enus -->
## TOPIC 00135: WA Set Coefficients of Discrete Wavelet Transform VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_setdwtcoef.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_setdwtcoef.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Set Coefficients of Discrete Wavelet Transform VI

**Owning Palette:** [Discrete Wavelet VIs](../lvwavelettk/discretewaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

discrete wavelet transform (DWT)

WA Discrete Wavelet Transform

WA Get Coefficients of Discrete Wavelet Transform

[Examples](#examples)

#### WA Set Coefficients of 1D Discrete Wavelet Transform (Waveform)

[IMAGE alt='image' src='wa_set_coefficients_of_1d_discrete_wavelet_transform_waveformc.gif']

|  | coef type specifies whether this VI sets the approximation coefficients or detail coefficients. The default is Approximation coefficients. |
| --- | --- |
|  | DWT coef specifies the approximation coefficients and the detail coefficients from the multi-level discrete wavelet transform (DWT). You must organize the coefficients into a waveform starting with the approximation coefficients at the largest level followed by the detail coefficients at all levels in descending order. If you use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients, wire the DWT coef out output of the WA Get Coefficients of Discrete Wavelet Transform VI to the DWT coef input of this VI. |
|  | length specifies, in a 1D array, the number of approximation and detail coefficients at each level. At a decomposition level of N, length is equal to N+2. The first element of length always is equal to the number of approximation coefficients. The last element of length indicates the total number of raw data samples. You must arrange the length of the detail coefficients in descending order. If you use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients, wire the length out output of the WA Get Coefficients of Discrete Wavelet Transform VI to the length input of this VI. |
|  | coef level specifies the coefficient level this VI sets. The coef level must be between 1 and the largest level of the detail coefficients. The levels in the WA Discrete Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI sets the coefficients at level 1. If coef type is Approximation coefficients, this VI ignores coef level. If coef type is Detail coefficients, this VI sets the coefficients at the level you specify in coef level. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | new DWT coef specifies the discrete wavelet transform (DWT) coefficients to set. |
|  | DWT coef out returns the discrete wavelet transform (DWT) coefficients set to new DWT coef at the coef type and coef level. |
|  | length out returns length unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Set Coefficients of 1D Discrete Wavelet Transform (Array)

[IMAGE alt='image' src='wa_set_coefficients_of_1d_discrete_wavelet_transform_arrayc.gif']

|  | coef type specifies whether this VI sets the approximation coefficients or detail coefficients. The default is Approximation coefficients. |
| --- | --- |
|  | DWT coef specifies the approximation coefficients and the detail coefficients from the multi-level discrete wavelet decomposition (DWT). You must organize the coefficients into a 1D real array starting with the approximation coefficients at the largest level followed by the detail coefficients at all levels in descending order. If you use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients, wire the DWT coef out output of the WA Get Coefficients of Discrete Wavelet Transform VI to the DWT coef input of this VI. |
|  | length specifies, in a 1D array, the number of approximation and detail coefficients at each level. At a decomposition level of N, length is equal to N+2. The first element of length always is equal to the number of approximation coefficients. The last element of length indicates the total number of raw data samples. You must arrange the length of the detail coefficients in descending order. If you use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients, wire the length out output of the WA Get Coefficients of Discrete Wavelet Transform VI to the length input of this VI. |
|  | coef level specifies the coefficient level this VI sets. The coef level must be between 1 and the largest level of the detail coefficients. The levels in the WA Discrete Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI sets the coefficients at level 1. If coef type is Approximation coefficients, this VI ignores coef level. If coef type is Detail coefficients, this VI sets the coefficients at the level you specify in coef level. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | new DWT coef specifies the discrete wavelet transform (DWT) coefficients to set. |
|  | DWT coef out returns the discrete wavelet transform (DWT) coefficients set to new DWT coef at the coef type and coef level. |
|  | length out returns length unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA Set Coefficients of 2D Discrete Wavelet Transform

[IMAGE alt='image' src='wa_set_coefficients_of_2d_discrete_wavelet_transformc.gif']

|  | coef type specifies the coefficient type this VI sets. 0low_low (default)—Specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal.1low_high—Specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients.2high_low—Specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients.3high_high—Specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
| --- | --- |
| 0 | low_low (default)—Specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. |
| 1 | low_high—Specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. |
| 2 | high_low—Specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. |
| 3 | high_high—Specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | DWT coef specifies the approximation coefficients and the detail coefficients from the multi-level discrete wavelet transform. Each element of the array contains the 2D DWT results of one level. The ith element stores the approximation coefficients and the detail coefficients at level i+1. If you use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients, wire the DWT coef out output of the WA Get Coefficients of Discrete Wavelet Transform VI to the DWT coef input of this VI. low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. |
|  | low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. |
|  | high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. |
|  | high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
|  | coef level specifies the coefficient level this VI sets. The coef level must be between 1 and the largest level of the coefficients. The levels in the WA Discrete Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI sets the coefficients at level 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | new DWT coef specifies the discrete wavelet transform (DWT) coefficients to set. |
|  | DWT coef out returns the discrete wavelet transform (DWT) coefficients set to new DWT coef at the coef type and coef level. low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. |
|  | low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. |
|  | low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. |
|  | high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. |
|  | high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the WA Set Coefficients of Discrete Wavelet Transform VI:

- Get and Set Approximation Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Get and Set Single Level Detail Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_wp_read_entropy.html language=enus -->
## TOPIC 00136: WA WP Read Entropy VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_wp_read_entropy.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_wp_read_entropy.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA WP Read Entropy VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Reads the entropy of the wavelet packet (WP) coefficients of a node that **path** specifies.

[Example](#examples)

[IMAGE alt='image' src='wa_wp_read_entropyc.gif']

|  | WP session specifies a reference to an existing wavelet packet structure. |
| --- | --- |
|  | path specifies the path associated with a node of the wavelet packet tree. path is a combination of the characters 0 and 1, where 0 represents lowpass filtering, and 1 represents highpass filtering. For example, a value of 101 indicates that this VI passes the signal through a highpass filter, through a lowpass filter, and then through a highpass filter. path can be root, which represents the original signal without any filtering operation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | WP session out returns a reference to an existing wavelet packet structure, which this VI can modify. |
|  | entropy returns the entropy of the wavelet packet coefficients at the node that path specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Wavelet Packet - Read Entropy VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA WP Read Entropy VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_wp_read_node.html language=enus -->
## TOPIC 00137: WA WP Read Node VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_wp_read_node.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_wp_read_node.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA WP Read Node VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Reads the wavelet packet (WP) coefficients of a terminal node that **path** specifies. If you want to read the coefficients of a non-terminal node, use the [WA WP Join](../lvwavelettk/wa_wp_join.html) VI to convert the node to a terminal node.

[Examples](#examples)

[IMAGE alt='image' src='wa_wp_read_nodec.gif']

|  | WP session specifies a reference to an existing wavelet packet structure. |
| --- | --- |
|  | path specifies the path associated with a node of the wavelet packet tree. For this VI, path must refer to a terminal node of the wavelet packet tree. path is a combination of the characters 0 and 1, where 0 represents lowpass filtering, and 1 represents highpass filtering. For example, a value of 101 indicates that this VI passes the signal through a highpass filter, through a lowpass filter, and then through a highpass filter. path can be root, which represents the original signal without any filtering operation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | WP session out returns a reference to an existing wavelet packet structure, which this VI can modify. |
|  | node coef returns the wavelet packet coefficients of the terminal node that path specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the WA WP Read Node VI:

- Wavelet Packet - Read and Write Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet - Read Entropy VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet Signal Compression VI: labview\examples\Wavelet Analysis\WAApplications

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_wp_read_tree_structure.html language=enus -->
## TOPIC 00138: WA WP Read Tree Structure VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_wp_read_tree_structure.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_wp_read_tree_structure.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA WP Read Tree Structure VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Reads the tree structure information of the terminal nodes in the wavelet packet (WP) tree and returns the node indexes and the associated paths of the terminal nodes.

[Example](#examples)

[IMAGE alt='image' src='wa_wp_read_tree_structurec.gif']

|  | WP session specifies a reference to an existing wavelet packet structure. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | WP session out returns a reference to an existing wavelet packet structure, which this VI can modify. |
|  | node index returns the indexes of the terminal nodes of the wavelet packet tree indexed from top to bottom and left to right. |
|  | path returns the paths associated with the terminal nodes in node index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Wavelet Packet Signal Compression VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of using the WA WP Read Tree Structure VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_wp_reconstruction.html language=enus -->
## TOPIC 00139: WA WP Reconstruction VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_wp_reconstruction.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_wp_reconstruction.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA WP Reconstruction VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Computes the 1D wavelet packet (WP) reconstruction from the wavelet packet tree and coefficients. You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance to use.

[Examples](#examples)

#### WA WP Reconstruction (Waveform)

[IMAGE alt='image' src='wa_wp_reconstruction_(waveform)c.gif']

|  | WP session specifies a reference to an existing wavelet packet structure. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | WP session out returns a reference to an existing wavelet packet structure, which this VI can modify. |
|  | signal returns the reconstructed signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### WA WP Reconstruction (Array)

[IMAGE alt='image' src='wa_wp_reconstruction_(array)c.gif']

|  | WP session specifies a reference to an existing wavelet packet structure. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | WP session out returns a reference to an existing wavelet packet structure, which this VI can modify. |
|  | signal returns the reconstructed signal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the WA WP Reconstruction VI:

- Wavelet Packet - Read and Write Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet Signal Compression VI: labview\examples\Wavelet Analysis\WAApplications

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_wp_split.html language=enus -->
## TOPIC 00140: WA WP Split VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_wp_split.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_wp_split.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA WP Split VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Splits the terminal node that **path** specifies into two children nodes.

[Example](#examples)

[IMAGE alt='image' src='wa_wp_splitc.gif']

|  | WP session specifies a reference to an existing wavelet packet structure. |
| --- | --- |
|  | path specifies the path associated with a node of the wavelet packet tree. For this VI, path must refer to a terminal node of the wavelet packet tree. path is a combination of the characters 0 and 1, where 0 represents lowpass filtering, and 1 represents highpass filtering. For example, a value of 101 indicates that this VI passes the signal through a highpass filter, through a lowpass filter, and then through a highpass filter. path can be root, which represents the original signal without any filtering operation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | WP session out returns a reference to an existing wavelet packet structure, which this VI can modify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Wavelet Packet - Split Node VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA WP Split VI.

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wa_wp_write_node.html language=enus -->
## TOPIC 00141: WA WP Write Node VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wa_wp_write_node.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wa_wp_write_node.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA WP Write Node VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Writes the wavelet packet (WP) coefficients to a terminal node that **path** specifies. If you want to write coefficients to a non-terminal node, use the [WA WP Join](../lvwavelettk/wa_wp_join.html) VI to convert the node to a terminal node.

[Examples](#examples)

[IMAGE alt='image' src='wa_wp_write_nodec.gif']

|  | WP session specifies a reference to an existing wavelet packet structure. |
| --- | --- |
|  | path specifies the path associated with a node of the wavelet packet tree. For this VI, path must refer to a terminal node of the wavelet packet tree. path is a combination of the characters 0 and 1, where 0 represents lowpass filtering, and 1 represents highpass filtering. For example, a value of 101 indicates that this VI passes the signal through a highpass filter, through a lowpass filter, and then through a highpass filter. path can be root, which represents the original signal without any filtering operation. |
|  | node coef specifies the wavelet packet coefficients to write to the terminal node path specifies. The required length of node coef depends on the signal length, the type of wavelet, and path. Use the WA WP Read Node VI to obtain the original coefficients of the node path specifies and thus the exact coefficients length acquired. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | WP session out returns a reference to an existing wavelet packet structure, which this VI can modify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the WA WP Write Node VI:

- Wavelet Packet - Read and Write Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet Signal Compression VI: labview\examples\Wavelet Analysis\WAApplications

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wavelet_design.html language=enus -->
## TOPIC 00142: Wavelet Design Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wavelet_design.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wavelet_design.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Wavelet Design Express VI

**Owning Palette:** [Discrete Wavelet VIs](../lvwavelettk/discretewaveletpal.html)

**Requires:** Advanced Signal Processing Toolkit

Designs customized analysis filters and synthesis filters for discrete wavelet analysis and reconstruction, respectively.

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Wavelet Type | Specifies the type of wavelet this Express VI uses to design a customized wavelet for discrete wavelet analysis and reconstruction. You can select the Orthogonal or Biorthogonal option. |
| Product of Lowpass (P0=G0*H0) | Specifies P0, which is the product of the lowpass analysis filter G0 and the lowpass synthesis filter H0. Contains the following options: P0 type—Specifies the type of P0. The default is Maxflat. You can choose from the following options: Maxflat Positive Equiripple General Equiripple Note The General Equiripple option is available only if you select the Biorthogonal option in the Wavelet Type section. Zero pairs at pi (P0)—Specifies the value of p in the Maxflat filter P0(z), where P0(z) = (1+1/z)^(2p)*Q(z). This option is available only if you select the Maxflat option in the P0 type section. # of taps—Specifies the number of coefficients of P0(z). The length of P0(z) must be 4p–1, where p = 2, 3, …. This option is available only if you select the Positive Equiripple or General Equiripple option in the P0 type section. Passband—Specifies the normalized cutoff frequency of P0(z). The value of Passband must be less than 0.5. Passband is available only if you select the Positive Equiripple or General Equiripple option in the P0 type section. |
|  | Note The General Equiripple option is available only if you select the Biorthogonal option in the Wavelet Type section. |
| Factorization (Type of G0) | Contains the following options: Filter type—Specifies how this Express VI factors P0 to G0 and H0. Contains the following options: Arbitrary—Specifies that no restriction exists on the placement of zeros. Minimum Phase—Specifies that the zeros of G0 are located inside the unit circle, except for the zeros at pi. Linear Phase—Specifies that if one zero belongs to G0(H0), the reciprocal of that zero must belong to G0(H0). B-Spline—Specifies that except for some zeros at pi, all the zeros of P0 belong to H0. Zeros at pi (G0)—Controls how many zeros at z=–1 belong to G0(z). This option is available only if you select the Maxflat option in the P0 type section. The maximum value of this option is 2p, where p = the value of the Zero pairs at pi (P0) option. |
| Zeros of G0 and H0 | Shows the distribution of the zeros of P0(z), G0(z) and H0(z). This Express VI uses this distribution to factor the zeros of P0(z) into the zeros of G0(z) and H0(z). Because the filter coefficients of P0(z) are real, all the zeros of P0(z) are symmetrical with respect to the x-axis. Consequently, this Express VI displays only the upper half of the plane. The zeros on the x-axis represent real-valued roots. The zeros outside of the x-axis represent complex-valued roots. The blue crosses represent the zeros of G0(z), and the red circles represent the zeros of H0(z). Click on the zero you want to select to switch the zero from that of G0(z) to that of H0(z) and vice versa. All the zeros belong to G0(z) or H0(z). Selecting different values for Filter type puts different constraints on the selections of zeros. For example, if you select Linear Phase for Filter type and select a zero for one filter, the filter automatically contains the reciprocal of the zero. |
| Wavelet and Filter Banks | Displays the following graphs: Analysis scaling—Displays the scaling function of the analysis filter bank. Analysis wavelet—Displays the mother wavelet of the analysis filter bank. Analysis lowpass (G0)—Displays the coefficients of the lowpass analysis filter G0(z). Analysis highpass (G1)—Displays the coefficients of the highpass analysis filter G1(z). Synthesis scaling—Displays the scaling function of the synthesis filter bank. Synthesis wavelet—Displays the mother wavelet of the synthesis filter bank. Synthesis lowpass (H0)—Displays the coefficients of the lowpass synthesis filter H0(z). Synthesis highpass (H1)—Displays the coefficients of the highpass synthesis filter H1(z). |
| Frequency response | Displays the magnitude of the frequency responses of the designed filters G0(z) and G1(z). G1(z) is the sign-alternated version of H0(z). In other words, G1(z) is a highpass filter if H0(z) is a lowpass filter. This VI shows the frequency response of G0(z) in blue and shows the frequency response of G1(z) in green. The units of the y-axis are in dB, and the units of the x-axis are in terms of the normalized frequency. The full scale ranges from 0.0 to 1.0 pi. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| Analysis filters | Returns the coefficients of the analysis filters. lowpass—Contains the coefficients of the analysis lowpass filter G0(z). highpass—Contains the coefficients of the analysis highpass filter G1(z). |
| Analysis scaling | Returns the scaling function of the analysis filter bank. |
| Analysis wavelet | Returns the mother wavelet of the analysis filter bank. |
| error out | Contains error information. This output provides standard error out functionality. |
| Synthesis filters | Returns the coefficients of the synthesis filters. lowpass—Contains the coefficients of the synthesis lowpass filter H0(z). highpass—Contains the coefficients of the synthesis highpass filter H1(z). |
| Synthesis scaling | Returns the scaling function of the synthesis filter bank. |
| Synthesis wavelet | Returns the mother wavelet of the synthesis filter bank. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wavelet_packet_analysis.html language=enus -->
## TOPIC 00143: Wavelet Packet Analysis Express VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wavelet_packet_analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wavelet_packet_analysis.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Wavelet Packet Analysis Express VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Decomposes the signal according to the tree structure you specify and reconstructs the signal from the nodes you specify. This VI also returns the coefficients and the entropies of the nodes you select.

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Data Source | Specifies whether this Express VI reads data from a block diagram input terminal or from a file. From terminal specifies that this Express VI reads data from a block diagram input terminal. From file specifies that this Express VI reads data from a file. This Express VI can read data from waveform, WAV, or TXT files. |
| File Path Configuration | Contains the following options: File path—Specifies and displays the path to the file from which this Express VI reads data. This option is available only when you select From file in the Data Source section. Prompt to choose a file each time this VI runs—Specifies whether this Express VI displays a dialog box that prompts you to select a file each time this Express VI runs. This option is available only when you select the From file option in the Data Source section. |
| Signals and Coefficients | Displays the following graphs: Original and reconstructed signal—Displays the original and the reconstructed signal. Nodes coefficients—Displays the coefficients of the nodes you select. If you select multiple nodes, this VI concatenates the node coefficients into one array. |
| Decomposition Settings | Contains the following options: Wavelet—Specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. The higher the order, the smoother the wavelet. The orthogonal wavelets are not redundant and are suitable for signal or image denoising and compression. The biorthogonal wavelets usually have the linear phase property and are suitable for signal or image feature extraction. Entropy type—Specifies the method to use to compute the entropy of the wavelet packet coefficients. Best tree—Specifies to decompose the signal based on the minimum entropy criterion. Levels—Specifies the number of levels in the discrete wavelet analysis. Levels must be a positive integer no greater than log2(Ls), where Ls is the length of the signal. Optional parameter—Specifies the associated parameter for the Threshold, SURE, and Norm entropy. Optional parameter is not available when you select Shannon or Energy in Entropy type. |
| Decomposition Tree | Plots the entire tree structure of the wavelet packet tree. Click a node to select it and display the coefficients of the node and the reconstruction of the signal in Signals and Coefficients. <Ctrl>–click to select multiple nodes. Double-click to split or join nodes. Zoom out—Zooms out the decomposition tree. Zoom in—Zooms in the decomposition tree. Restore—Restores the decomposition tree. Display mode—Specifies the display mode of the node strings in the decomposition tree. Contains the following options: node path—Displays the node with a string that consists of the characters 0 and 1, where 0 represents lowpass filtering, and 1 represents highpass filtering. depth, pos—Displays the node with the depth of the node in the tree and the position of the node in its level. The depth and the position start with 0. The depth ascends from the top to the bottom of the tree. The position ascends from the left to the right in a level. entropy—Displays the node with the entropy of the node. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in (no error) | Describes error conditions that occur before this node runs. |
| Signal | Specifies the block diagram terminal of the data you want to load. This input is available only if you select the From terminal option in the Data Source section. |
| File path | Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| Reconstruction | Returns the reconstructed signal. |
| node coeffs | Returns the coefficients of the nodes you select. |
| entropy | Returns the entropies of the nodes you select. |
| path out | Returns the paths of the nodes you select. |
| error out | Contains error information. This output provides standard error out functionality. |

This Express VI operates similarly to the following VIs and functions:

[WA Create WP Session](../lvwavelettk/wp_create_wp_session.html) 

[WA WP Decomposition](../lvwavelettk/wa_wp_decomposition.html) 

[WA WP Split](../lvwavelettk/wa_wp_split.html) 

[WA WP Read Node](../lvwavelettk/wa_wp_read_node.html) 

[WA WP Read Tree Structure](../lvwavelettk/wa_wp_read_tree_structure.html) 

[WA WP Read Entropy](../lvwavelettk/wa_wp_read_entropy.html) 

[WA Dispose WP Session](../lvwavelettk/wa_dispose_wp_session.html) 

[WA WP Reconstruction](../lvwavelettk/wa_wp_reconstruction.html)

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/waveletpacketpal.html language=enus -->
## TOPIC 00144: Wavelet Packet VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/waveletpacketpal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/waveletpacketpal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Wavelet Packet VIs

**Owning Palette:** [Wavelet Analysis VIs](../lvwavelettk/lvwavelettk.html)

**Requires:** Advanced Signal Processing Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Wavelet Packet VIs to compute various wavelet packet analyses, such as [wavelet packet decomposition](../lvasptconcepts/wp_decomposition.html), wavelet packet reconstruction, and various operations on the wavelet packet tree.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Wavelet Analysis error codes](wa_error_codes.html).

| Palette Object | Description |
| --- | --- |
| WA Create WP Session | Creates a new wavelet packet (WP) structure and returns a reference to it. Use this VI as the first step to perform wavelet packet analyses. Use the WA Dispose WP Session VI to dispose of the reference. |
| WA Dispose WP Session | Disposes the reference of the wavelet packet (WP) structure the WA Create WP Session VI created. |
| WA WP Best Tree | Searches for the optimal decomposition tree based on the minimum entropy criterion, which is the smallest value of the total entropy of all terminal nodes at a certain level in all the possible tree structures. |
| WA WP Decomposition | Computes the 1D wavelet packet (WP) decomposition and stores the resulting coefficients and wavelet packet tree information in the wavelet packet structure. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. |
| WA WP Join | Reconstructs the wavelet packet (WP) coefficients of the node that path specifies. The node that path specifies must not be a terminal node of the wavelet packet tree. |
| WA WP Plot Tree | Plots the whole tree structure of the wavelet packet (WP) tree in a picture control. You can show the node information of path, position, or entropy on each node of the wavelet packet tree. |
| WA WP Read Entropy | Reads the entropy of the wavelet packet (WP) coefficients of a node that path specifies. |
| WA WP Read Node | Reads the wavelet packet (WP) coefficients of a terminal node that path specifies. If you want to read the coefficients of a non-terminal node, use the WA WP Join VI to convert the node to a terminal node. |
| WA WP Read Tree Structure | Reads the tree structure information of the terminal nodes in the wavelet packet (WP) tree and returns the node indexes and the associated paths of the terminal nodes. |
| WA WP Reconstruction | Computes the 1D wavelet packet (WP) reconstruction from the wavelet packet tree and coefficients. You must manually select the polymorphic instance to use. |
| WA WP Split | Splits the terminal node that path specifies into two children nodes. |
| WA WP Write Node | Writes the wavelet packet (WP) coefficients to a terminal node that path specifies. If you want to write coefficients to a non-terminal node, use the WA WP Join VI to convert the node to a terminal node. |
| Wavelet Packet Analysis | Decomposes the signal according to the tree structure you specify and reconstructs the signal from the nodes you specify. This VI also returns the coefficients and the entropies of the nodes you select. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/waveletutilpal.html language=enus -->
## TOPIC 00145: Utilities VIs

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/waveletutilpal.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/waveletutilpal.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Utilities VIs

**Owning Palette:** [Wavelet Analysis VIs](../lvwavelettk/lvwavelettk.html)

**Requires:** Advanced Signal Processing Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Utilities VIs to read data files, to use demonstration data, and to display the squared magnitude or the phase of the wavelet coefficients of a signal on an intensity graph.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Wavelet Analysis error codes](wa_error_codes.html).

| Palette Object | Description |
| --- | --- |
| WA Configure Scalogram Indicator | Displays the square magnitude or the phase of the wavelet coefficients on an intensity graph. This VI displays the square magnitude of the real-valued wavelet coefficients from the WA Continuous Wavelet Transform VI and displays the square magnitude or the phase of the complex-valued wavelet coefficients from the WA Analytic Wavelet Transform VI. Wire data to the CWT coef input or the AWT coef input to determine the polymorphic instance to use or manually select the instance. |
| WA Data Samples | Contains the demonstration data samples for the Wavelet Analysis VIs. |
| WA Read from File | Reads data from a spreadsheet text file that contains a 1D array, a 2D array, a byte stream file of single-precision numbers, a byte stream file of 16-bit signed integers, a file created with the Write Waveforms to File VI, a WAV file, a JPG file, a BMP file, or a PNG file. |

<!--NI_TOPIC bundle=labview-advanced-signal-processing-toolkit-api-ref path=lvwavelettk/wp_create_wp_session.html language=enus -->
## TOPIC 00146: WA Create WP Session VI

- bundle_id: `labview-advanced-signal-processing-toolkit-api-ref`
- source_path: `lvwavelettk/wp_create_wp_session.html`
- source_url: https://docs-be.ni.com/bundle/labview-advanced-signal-processing-toolkit-api-ref/raw/resource/enus/lvwavelettk/wp_create_wp_session.html
- document_id: `labview-advanced-signal-processing-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### WA Create WP Session VI

**Owning Palette:** [Wavelet Packet VIs](../lvwavelettk/waveletpacketpal.html)

**Requires:** Advanced Signal Processing Toolkit

Creates a new wavelet packet (WP) structure and returns a reference to it. Use this VI as the first step to perform wavelet packet analyses. Use the [WA Dispose WP Session](../lvwavelettk/wa_dispose_wp_session.html) VI to dispose of the reference.

[Examples](#examples)

[IMAGE alt='image' src='wa_create_wp_sessionc.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | WP session out returns the reference of a new wavelet packet structure. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the WA Create WP Session VI:

- Wavelet Packet - Entropy Selection VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet - Read and Write Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet - Join Node VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet - Split Node VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Packet Signal Compression VI: labview\examples\Wavelet Analysis\WAApplications
