# NI DOCUMENT BUNDLE: lvaspt-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvaspt-api-ref start=1 end=95 -->
<!--NI_TOPIC bundle=lvaspt-api-ref path=menus/categories/signal-processing/advanced-signal-processing/time-frequency-analysis/tfa-control-palette.html language=enus -->
## TOPIC 00001: Controls (Advanced Signal Processing Toolkit)

- bundle_id: `lvaspt-api-ref`
- source_path: `menus/categories/signal-processing/advanced-signal-processing/time-frequency-analysis/tfa-control-palette.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/menus/categories/signal-processing/advanced-signal-processing/time-frequency-analysis/tfa-control-palette.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the controls on the Time Series Controls palette to display the cepstrogram of a univariate time series on an intensity graph. Palette Object Description TFA Coefficients Indicator Displays the magnitude or phase of the linear time-frequency coefficients of a signal on an intensity graph. When y

### Controls (Advanced Signal Processing Toolkit)

Use the controls on the **Time Series Controls** palette to display the [cepstrogram](/csh?context=lvmnt_aspt_lvasptconcepts_tsa_time_cepstrum) of a univariate time series on an intensity graph.

| Palette Object | Description |
| --- | --- |
| TFA Coefficients Indicator | Displays the magnitude or phase of the linear time-frequency coefficients of a signal on an intensity graph. When you add the TFA Coefficients Indicator to the front panel, the TFA Configure Coefficients Indicator VI appears on the block diagram with the reference of TF coefficients indicator input and the TF coefficients indicator output already wired. |
| TFA Spectrogram Indicator | Displays the spectrogram of a signal on an intensity graph. When you add the TFA Spectrogram Indicator to the front panel, the TFA Configure Spectrogram Indicator VI appears on the block diagram with the reference of TF spectrogram indicator input and the TF spectrogram indicator output already wired. |
| TFA Gray Scale Image | Displays an image on an intensity graph by using the gray scale color table. The gray scale color table displays the maximum value of the color scale in white and the minimum value of the color scale in black. |

You can save the time-dependent 2D array to a text file for use in another software environment. The resulting text file contains only Z values and does not retain the time axis information or the frequency axis information. You can use the [TFA Get Time and Freq Scale Info](../../../../../vi-lib/addons/time-frequency-analysis/utilities-llb/tfa-get-time-and-freq-scale-info-vi.html) VI to compute the time scale information and the frequency scale information of the time-frequency representation.

Parent topic:

Time Frequency Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-vi.html language=enus -->
## TOPIC 00002: TFA Fast Mean Instantaneous Frequency VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the Gabor expansion-based method to compute the mean instantaneous frequency (MIF) for signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon

### TFA Fast Mean Instantaneous Frequency VI

Uses the Gabor expansion-based method to compute the mean instantaneous frequency (MIF) for **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-fast-mean-instantaneous-frequency-vi.png']

- [TFA Fast Mean Instantaneous Frequency (Waveform) VI](../../../../vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-waveform-vi.html) Uses the Gabor expansion-based method to compute the mean instantaneous frequency (MIF) for signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [TFA Fast Mean Instantaneous Frequency (Real) VI](../../../../vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-real-vi.html) Uses the Gabor expansion-based method to compute the mean instantaneous frequency (MIF) for signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [TFA Fast Mean Instantaneous Frequency (Complex) VI](../../../../vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-complex-vi.html) Uses the Gabor expansion-based method to compute the mean instantaneous frequency (MIF) for signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Feature Extraction

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-waveform-vi.html language=enus -->
## TOPIC 00003: TFA Fast Mean Instantaneous Frequency (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/application-llb/tfa-fast-mean-instantaneous-frequency-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the Gabor expansion-based method to compute the mean instantaneous frequency (MIF) for signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ci32.png order order specifies how this VI balances the bias and the var

### TFA Fast Mean Instantaneous Frequency (Waveform) VI

Uses the Gabor expansion-based method to compute the mean instantaneous frequency (MIF) for **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-fast-mean-instantaneous-frequency-waveform-vi.png']

#### Inputs/Outputs

| order — order specifies how this VI balances the bias and the variance of the MIF estimation. order must be greater than or equal to 0, or this VI sets order to 0 automatically. The default is 2. A higher order results in a large variance but less bias. signal — signal specifies the input signal. time interval — time interval specifies the time interval, in samples, to observe the MIF of the signal. The default is -1, which specifies that this VI adjusts time interval automatically so that no more than 512 time bins exist in MIF. Gaussian window length — Gaussian window length specifies the length of the Gaussian window, in samples, of the Gabor elementary functions and controls the relationship between the time resolution and the frequency resolution of the spectrogram. Gaussian window length must be a power of 2 and greater than or equal to 8. As the value of Gaussian window length increases, the frequency resolution increases, but the time resolution decreases. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MIF — MIF returns the mean instantaneous frequency of the signal at each time bin. t0 — t0 returns the lowest value of the time bins in seconds. dt — dt returns the interval between the time bins in seconds. frequency — frequency returns the resulting mean instantaneous frequencies at each time bin in hertz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 returns the lowest value of the time bins in seconds. dt — dt returns the interval between the time bins in seconds. frequency — frequency returns the resulting mean instantaneous frequencies at each time bin in hertz. |

Parent topic:

TFA Fast Mean Instantaneous Frequency VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/application-llb/tfa-group-delay-vi.html language=enus -->
## TOPIC 00004: TFA Group Delay VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/application-llb/tfa-group-delay-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/application-llb/tfa-group-delay-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the group delay of a signal from the spectrogram of the signal. icon Inputs/Outputs c2ddbl.png spectrogram spectrogram specifies the quadratic time-frequency representation of a signal. Use the Time Frequency Spectrogram VIs to compute the spectrogram of the signal. cfxdt.png scale info sca

### TFA Group Delay VI

Computes the group delay of a signal from the spectrogram of the signal.

[IMAGE alt='icon' src='tfa-group-delay-vi.png']

#### Inputs/Outputs

| spectrogram — spectrogram specifies the quadratic time-frequency representation of a signal. Use the Time Frequency Spectrogram VIs to compute the spectrogram of the signal. scale info — scale info specifies the time scale information and the frequency scale information of the time-frequency representation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. group delay — group delay returns the time delay of the signal at each frequency bin. f0 — f0 returns the lowest value of the frequency bins in hertz. df — df returns the interval between the frequency bins in hertz. delay — delay returns the time delay at each frequency bin in seconds. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| f0 — f0 returns the lowest value of the frequency bins in hertz. df — df returns the interval between the frequency bins in hertz. delay — delay returns the time delay at each frequency bin in seconds. |

#### TFA Group Delay Details

The following equation defines the group delay:

[IMAGE alt='image' src='eq_group_delay.gif']

where [IMAGE alt='image' src='eq_spectrogram.gif'] is the spectrogram of the signal. The spectrogram can result from any [Time Frequency Spectrogram](../../../../menus/categories/signal-processing/advanced-signal-processing/time-frequency-analysis/specgram-mnu.html) VI.

#### Examples

Refer to the Group Delay VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Group Delay VI.

Parent topic:

Feature Extraction

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/application-llb/tfa-marginal-integration-vi.html language=enus -->
## TOPIC 00005: TFA Marginal Integration VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/application-llb/tfa-marginal-integration-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/application-llb/tfa-marginal-integration-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the marginal integration of a signal by integrating the spectrogram of the signal along the time axis or the frequency axis. icon Inputs/Outputs c2ddbl.png spectrogram spectrogram specifies the quadratic time-frequency representation of a signal. Use the Time Frequency Spectrogram VIs to co

### TFA Marginal Integration VI

Computes the marginal integration of a signal by integrating the **spectrogram** of the signal along the time axis or the frequency axis.

[IMAGE alt='icon' src='tfa-marginal-integration-vi.png']

#### Inputs/Outputs

| spectrogram — spectrogram specifies the quadratic time-frequency representation of a signal. Use the Time Frequency Spectrogram VIs to compute the spectrogram of the signal. scale info — scale info specifies the time scale information and the frequency scale information of the time-frequency representation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. frequency marginal integral — frequency marginal integral returns the result of integrating the spectrogram along the time axis, or the integral of each column of spectrogram. frequency marginal integral is equivalent to the smoothed power spectrum of the signal. The power spectrum reveals how the power of the signal changes over frequency. The following equation defines the frequency marginal integration: where is the spectrogram of the signal. f0 — f0 returns the lowest value of the frequency bins in hertz. df — df returns the interval between the frequency bins in hertz. spectrum — spectrum returns the smoothed power spectrum at each frequency bin. time marginal integral — time marginal integral returns the result of integrating the spectrogram along the frequency axis, or the integral of each row of spectrogram. time marginal integral is equivalent to the smoothed instantaneous power of the signal. The instantaneous power reveals how the power of the signal changes over time. The following equation defines the time marginal integration: where is the spectrogram of the signal. t0 — t0 returns the lowest value of the time bins in seconds. dt — dt returns the interval between the time bins in seconds. power — power returns the smoothed instantaneous power at each time bin. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| f0 — f0 returns the lowest value of the frequency bins in hertz. df — df returns the interval between the frequency bins in hertz. spectrum — spectrum returns the smoothed power spectrum at each frequency bin. |
| t0 — t0 returns the lowest value of the time bins in seconds. dt — dt returns the interval between the time bins in seconds. power — power returns the smoothed instantaneous power at each time bin. |

#### TFA Marginal Integration Details

The spectrogram can result from any [Time Frequency Spectrogram](../../../../menus/categories/signal-processing/advanced-signal-processing/time-frequency-analysis/specgram-mnu.html) VI.

If you use the [Wigner-Ville Distribution](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_wvd) to compute the marginal integration, you can prove that

[IMAGE alt='image' src='eq_marginal_integration1.gif']

and

[IMAGE alt='image' src='eq_marginal_integration.gif']

#### Examples

Refer to the Marginal Condition VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Marginal Integration VI.

Parent topic:

Feature Extraction

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/application-llb/tfa-mean-instantaneous-frequency-vi.html language=enus -->
## TOPIC 00006: TFA Mean Instantaneous Frequency VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/application-llb/tfa-mean-instantaneous-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/application-llb/tfa-mean-instantaneous-frequency-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the mean instantaneous frequency (MIF) of a signal from its spectrogram. The MIF reveals how the central frequency of the signal changes over time. icon Inputs/Outputs cnclst.png trimmed percent trimmed percent specifies how this VI trims the spectrogram at high frequencies and at low frequ

### TFA Mean Instantaneous Frequency VI

Computes the mean instantaneous frequency (MIF) of a signal from its spectrogram. The MIF reveals how the central frequency of the signal changes over time.

[IMAGE alt='icon' src='tfa-mean-instantaneous-frequency-vi.png']

#### Inputs/Outputs

| trimmed percent — trimmed percent specifies how this VI trims the spectrogram at high frequencies and at low frequencies before computing the MIF. If obvious noise exists at high frequencies or at low frequencies, use trimmed percent to improve the accuracy of the MIF estimation. upper — upper specifies the percent of noise power at high frequencies to the total power of the spectrogram. upper must be less than 100-lower. The larger the percentage, the more bins at high frequencies this VI trims. lower — lower specifies the percent of noise power at low frequencies to the total power of the spectrogram. lower must be less than 100-upper. The larger the percentage, the more bins at low frequencies this VI trims. spectrogram — spectrogram specifies the quadratic time-frequency representation of a signal. Use the Time Frequency Spectrogram VIs to compute the spectrogram of the signal. scale info — scale info specifies the time scale information and the frequency scale information of the time-frequency representation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MIF — MIF returns the mean instantaneous frequency of the signal at each time bin. t0 — t0 returns the lowest value of the time bins in seconds. dt — dt returns the interval between the time bins in seconds. frequency — frequency returns the resulting mean instantaneous frequencies at each time bin in hertz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| upper — upper specifies the percent of noise power at high frequencies to the total power of the spectrogram. upper must be less than 100-lower. The larger the percentage, the more bins at high frequencies this VI trims. lower — lower specifies the percent of noise power at low frequencies to the total power of the spectrogram. lower must be less than 100-upper. The larger the percentage, the more bins at low frequencies this VI trims. |
| t0 — t0 returns the lowest value of the time bins in seconds. dt — dt returns the interval between the time bins in seconds. frequency — frequency returns the resulting mean instantaneous frequencies at each time bin in hertz. |

#### TFA Mean Instantaneous Frequency Details

The following equation defines the MIF of a signal:

[IMAGE alt='image' src='eq_mif.gif']

where [IMAGE alt='image' src='eq_spectrogram.gif'] is the spectrogram of the signal. The spectrogram can result from any [Time Frequency Spectrogram](../../../../menus/categories/signal-processing/advanced-signal-processing/time-frequency-analysis/specgram-mnu.html) VI.

#### Examples

Refer to the following VIs for examples of using the TFA Mean Instantaneous Frequency VI:

- Blood Flow Measurement VI: labview\examples\Time Frequency Analysis\TFAApplications
- Liquefaction Detection VI: labview\examples\Time Frequency Analysis\TFAApplications
- Mean Instantaneous Frequency or Bandwidth (MIF or MIB) VI: labview\examples\Time Frequency Analysis\TFAFunctions
- Quadratic JTFA Method VI: labview\examples\Time Frequency Analysis\TFAGettingStarted

Parent topic:

Feature Extraction

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/express/timefrequencydualwindowsource-llb/timefrequencydualwindow-source-vi.html language=enus -->
## TOPIC 00007: Dual Window

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/express/timefrequencydualwindowsource-llb/timefrequencydualwindow-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/express/timefrequencydualwindowsource-llb/timefrequencydualwindow-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the dual windows for the Gabor transform and the Gabor expansion. icon Dialog Box Options Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in functionality. icclst.png synthesis info

### Dual Window

Computes the dual windows for the Gabor transform and the Gabor expansion.

[IMAGE alt='icon' src='timefrequencydualwindow-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. synthesis info — Returns the Gabor elementary functions for the Gabor expansion. synthesis windowContains the window of the Gabor elementary functions. The size of synthesis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps)Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins)Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. For stable reconstruction, N (frequency bins) must be greater than or equal to dM (time steps). The ratio between N (frequency bins) and dM (time steps) is called the oversampling rate. synthesis window — Contains the window of the Gabor elementary functions. The size of synthesis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps) — Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins) — Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. analysis info — Returns the analysis window for the Gabor transform. analysis windowContains the window this VI used to compute the Gabor coefficients. analysis window is the dual window of the synthesis window, which is the envelope of the Gabor elementary functions. The size of analysis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps)Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins)Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. For stable reconstruction, N (frequency bins) must be greater than or equal to dM (time steps). The ratio between N (frequency bins) and dM (time steps) is called the oversampling rate. analysis window — Contains the window the VI used to compute the Gabor coefficients. dM (time steps) — Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins) — Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| synthesis window — Contains the window of the Gabor elementary functions. The size of synthesis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps) — Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins) — Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. |
| analysis window — Contains the window the VI used to compute the Gabor coefficients. dM (time steps) — Contains the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. N (frequency bins) — Contains the number of carrier frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. |

#### Dual Window Details

The [synthesis window](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_discrete_gabor_trans_exp) is the envelope window of the Gabor elementary functions. The [dual window](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_discrete_gabor_trans_exp) of the synthesis window is called the [analysis window](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_discrete_gabor_trans_exp), which this VI uses in the Gabor transform to compute the complex weight of the Gabor elementary functions. You can use the resulting **analysis info** and **synthesis info** for the Gabor transform and the Gabor expansion, respectively.

This Express VI operates similarly to the following VIs and functions:

[TFA Dual Window](../../transform-llb/tfa-dual-window-vi.html)

#### Examples

Refer to the following VIs for examples of using the Dual Window VI:

- Online Noise Reduction VI: labview\examples\Time Frequency Analysis\TFAApplications
- Dual Function VI: labview\examples\Time Frequency Analysis\TFAGettingStarted
- Gabor Transform and Expansion VI: labview\examples\Time Frequency Analysis\TFAFunctions

Parent topic:

Time Frequency Transform

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/express/timefrequencyspectrogramsource-llb/timefrequencyspectrogram-source-vi.html language=enus -->
## TOPIC 00008: Time Frequency Spectrogram

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/express/timefrequencyspectrogramsource-llb/timefrequencyspectrogram-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/express/timefrequencyspectrogramsource-llb/timefrequencyspectrogram-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the quadratic joint time-frequency representation for the input signal. You can compute the short-time Fourier transform (STFT) spectrogram, the Gabor spectrogram, the adaptive spectrogram, the Wigner-Ville distribution, the Choi-Williams distribution, and the cone-shaped distribution. icon

### Time Frequency Spectrogram

Computes the quadratic joint time-frequency representation for the input signal. You can compute the short-time Fourier transform (STFT) spectrogram, the Gabor spectrogram, the adaptive spectrogram, the Wigner-Ville distribution, the Choi-Williams distribution, and the cone-shaped distribution.

[IMAGE alt='icon' src='timefrequencyspectrogram-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| Start — Specifies the start index, in samples, of the processed part of Signal. Signal — Specifies the block diagram terminal of the signal you want to load. This input is available only if you select the From terminal option in the Data Source section. Waveform — is the input signal. Real Signal — Specifies the input signal. The signal can be a waveform, a real array, or a complex array. File path — Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. Complex Signal — Specifies the input signal. The signal can be a waveform, a real array, or a complex array. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. Length — Returns the actual length of the processed signal. Scale Info — Returns the time scale and the frequency scale information of the time-frequency representation. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. Spectrogram — Returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. dB — Specifies whether this Express VI displays the spectrogram in decibels. |
| --- |

#### Examples

Refer to the following VIs for examples of using the Time Frequency Spectrogram VI:

- The Need for JTFA VI: labview\examples\Time Frequency Analysis\TFAGettingStarted
- Quadratic JTFA Method VI: labview\examples\Time Frequency Analysis\TFAGettingStarted
- Heart Sound TFA VI: labview\examples\Time Frequency Analysis\TFAApplications
- Cross Term VI: labview\examples\Time Frequency Analysis\TFAGettingStarted

Parent topic:

Time Frequency Spectrogram

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/express/timevaryingfilterthresholdsource-llb/timevaryingfilterthreshold-source-vi.html language=enus -->
## TOPIC 00009: Time Varying Filter (Thresholding)

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/express/timevaryingfilterthresholdsource-llb/timevaryingfilterthreshold-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/express/timevaryingfilterthresholdsource-llb/timevaryingfilterthreshold-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the thresholding method to perform time-varying filtering in the joint time-frequency domain. icon Dialog Box Options Inputs/Outputs cmsdt.png Signal Specifies the block diagram terminal of the signal you want to load. This input is available only if you select the From terminal option in the D

### Time Varying Filter (Thresholding)

Uses the thresholding method to perform time-varying filtering in the joint time-frequency domain.

[IMAGE alt='icon' src='timevaryingfilterthreshold-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| Signal — Specifies the block diagram terminal of the signal you want to load. This input is available only if you select the From terminal option in the Data Source section. Waveform — is the input signal. Complex Signal — Specifies the input signal. The signal can be a waveform, a real array, or a complex array. File path — Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. Real Signal — Specifies the input signal. The signal can be a waveform, a real array, or a complex array. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. Complex Filtered — Contains the filtered signal. Filtered Signal — Returns the filtered signal. Real Filtered — Contains the filtered signal. |
| --- |

#### Examples

Refer to the Offline Noise Reduction with Time Varying Filter VI in the labview\examples\Time Frequency Analysis\TFAApplications directory for an example of using the Time Varying Filter (Thresholding) VI.

Parent topic:

Time Frequency Transform

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-complex-vi.html language=enus -->
## TOPIC 00010: TFA Choi-Williams Distribution (Complex) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-complex-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-complex-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the Choi-Williams Distribution (CWD) of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c1dcdb.png signal signal specifies the input signal. cnclst.png time-frequency sampling info time-frequency samplin

### TFA Choi-Williams Distribution (Complex) VI

Computes the Choi-Williams Distribution (CWD) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-choi-williams-distribution-complex-vi.png']

#### Inputs/Outputs

| signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. alpha — alpha specifies the relationship between resolution and cross-term interference. alpha must be greater than or equal to 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |

#### TFA Choi-Williams Distribution Details

CWD is a type of [Cohen's class distribution](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_cwd_csd) and is the smooth version of the [Wigner-Ville Distribution (WVD)](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_wvd). CWD has better readability than WVD but worse time-frequency resolution, because CWD suppresses the cross-term interference between two signal components that have a large difference in [central time](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency) or [central frequency](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency). However, CWD does not suppress the cross-term interference between two signal components that have the same central time or the same central frequency. Therefore, for large values of the signal length, this VI requires a long computation time and more memory. National instruments recommends that you limit **signal** to 15,000 samples.

#### Examples

Refer to the Marginal Condition VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Choi-Williams Distribution VI.

Parent topic:

TFA Choi-Williams Distribution VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-real-vi.html language=enus -->
## TOPIC 00011: TFA Choi-Williams Distribution (Real) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-real-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-real-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the Choi-Williams Distribution (CWD) of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c1ddbl.png signal signal specifies the input signal. cnclst.png time-frequency sampling info time-frequency samplin

### TFA Choi-Williams Distribution (Real) VI

Computes the Choi-Williams Distribution (CWD) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-choi-williams-distribution-real-vi.png']

#### Inputs/Outputs

| signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. alpha — alpha specifies the relationship between resolution and cross-term interference. alpha must be greater than or equal to 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. analytic signal? (T) — analytic signal? specifies whether to convert the real input signal to the corresponding analytic signal. The default is TRUE. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |

#### TFA Choi-Williams Distribution Details

CWD is a type of [Cohen's class distribution](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_cwd_csd) and is the smooth version of the [Wigner-Ville Distribution (WVD)](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_wvd). CWD has better readability than WVD but worse time-frequency resolution, because CWD suppresses the cross-term interference between two signal components that have a large difference in [central time](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency) or [central frequency](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency). However, CWD does not suppress the cross-term interference between two signal components that have the same central time or the same central frequency. Therefore, for large values of the signal length, this VI requires a long computation time and more memory. National instruments recommends that you limit **signal** to 15,000 samples.

#### Examples

Refer to the Marginal Condition VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Choi-Williams Distribution VI.

Parent topic:

TFA Choi-Williams Distribution VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-waveform-vi.html language=enus -->
## TOPIC 00012: TFA Choi-Williams Distribution (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-choi-williams-distribution-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the Choi-Williams Distribution (CWD) of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cmsdt.png signal signal specifies the input signal. cnclst.png time-frequency sampling info time-frequency sampling

### TFA Choi-Williams Distribution (Waveform) VI

Computes the Choi-Williams Distribution (CWD) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-choi-williams-distribution-waveform-vi.png']

#### Inputs/Outputs

| signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. alpha — alpha specifies the relationship between resolution and cross-term interference. alpha must be greater than or equal to 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. analytic signal? (T) — analytic signal? specifies whether to convert the real input signal to the corresponding analytic signal. The default is TRUE. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |

#### TFA Choi-Williams Distribution Details

CWD is a type of [Cohen's class distribution](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_cwd_csd) and is the smooth version of the [Wigner-Ville Distribution (WVD)](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_wvd). CWD has better readability than WVD but worse time-frequency resolution, because CWD suppresses the cross-term interference between two signal components that have a large difference in [central time](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency) or [central frequency](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency). However, CWD does not suppress the cross-term interference between two signal components that have the same central time or the same central frequency. Therefore, for large values of the signal length, this VI requires a long computation time and more memory. National instruments recommends that you limit **signal** to 15,000 samples.

#### Examples

Refer to the Marginal Condition VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Choi-Williams Distribution VI.

Parent topic:

TFA Choi-Williams Distribution VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-complex-vi.html language=enus -->
## TOPIC 00013: TFA Fast Gabor Spectrogram (Complex) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-complex-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-complex-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decomposes a signal as a linear combination of Gaussian Gabor elementary functions. After decomposing the signal, this VI adds the Wigner-Ville Distribution (WVD) and cross WVD of the elementary functions to compute the quadratic time-frequency representation of signal. Wire data to the signal input

### TFA Fast Gabor Spectrogram (Complex) VI

Decomposes a signal as a linear combination of Gaussian Gabor elementary functions. After decomposing the signal, this VI adds the Wigner-Ville Distribution (WVD) and cross WVD of the elementary functions to compute the quadratic time-frequency representation of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-fast-gabor-spectrogram-complex-vi.png']

#### Inputs/Outputs

| zoom settings — zoom settings specifies the frequency zoom factor and the zoom range. zoom factor — zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. f0 — f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals -fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins — number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is -1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factorxfrequency bins for real-valued input signals and must not be greater than zoom factorxfrequency bins for complex-valued input signals. order — order specifies how this VI balances the time-frequency resolution and the cross-term interference of the Gabor spectrogram. order must be greater than or equal to 0, or this VI sets order to 0 automatically. signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. Gaussian window length — Gaussian window length specifies the length of the Gaussian window, in samples, of the Gabor elementary functions and controls the relationship between the time resolution and the frequency resolution of the spectrogram. Gaussian window length must be a power of 2 and greater than or equal to 8. As the value of Gaussian window length increases, the frequency resolution increases, but the time resolution decreases. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| zoom factor — zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. f0 — f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals -fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins — number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is -1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factorxfrequency bins for real-valued input signals and must not be greater than zoom factorxfrequency bins for complex-valued input signals. |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |

#### TFA Fast Gabor Spectrogram Details

The [Gabor spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_gabor_spectrogram) has better time-frequency resolution than the [STFT spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_stft_spectrogram) method and less cross-term interference than the WVD method. The Gabor spectrogram also allows control of the tradeoff between the cross-term suppression and the joint time-frequency resolution.

The Gabor spectrogram also is called the Gabor expansion-based spectrogram. You can use the [Gabor expansion](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_discrete_gabor_trans_exp) to represent the signal as the linear combination of the time-frequency elementary functions, as shown in the following equation:

[IMAGE alt='image' src='eq_gabor_expansion.gif']

where h<sub>m,n</sub>(i) is the elementary function, and C<sub>m,n</sub> is the Gabor coefficients.

After you represent the signal as the linear combination of the time-frequency elementary function, you can use the following equation to compute the WVD of the signal:

[IMAGE alt='image' src='eq_gabor_wvd.gif']

Thus, any two elementary functions generate the cross-term interferences. Instead of computing the WVD for any pair of elementary functions, you can select a subset for the computation based on the Manhattan distance [IMAGE alt='image' src='eq_manhattan_dist.gif'] between the pair of [IMAGE alt='image' src='eq_func_1.gif'] and [IMAGE alt='image' src='eq_func_2.gif']. The resulting time-frequency distribution is the Gabor spectrogram, as defined in the following equation:

[IMAGE alt='image' src='eq_gabor_spect.gif']

where D denotes the **order**. The joint time-frequency resolution and the cross-term interference of the Gabor spectrogram increases with **order**. When **order** is 0, the Gabor spectrogram is non-negative and is similar to the STFT spectrogram. As **order** approaches infinity, the Gabor spectrogram converges to the WVD.

Refer to the book [Introduction to Time-Frequency and Wavelet Transforms](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_related_doc) for more information about the Gabor expansion and transform.

#### Examples

Refer to the Liquefaction Detection VI in the labview\examples\Time Frequency Analysis\TFAApplications directory for an example of using the TFA Fast Gabor Spectrogram VI.

Parent topic:

TFA Fast Gabor Spectrogram VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-real-vi.html language=enus -->
## TOPIC 00014: TFA Fast Gabor Spectrogram (Real) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-real-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-real-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decomposes a signal as a linear combination of Gaussian Gabor elementary functions. After decomposing the signal, this VI adds the Wigner-Ville Distribution (WVD) and cross WVD of the elementary functions to compute the quadratic time-frequency representation of signal. Wire data to the signal input

### TFA Fast Gabor Spectrogram (Real) VI

Decomposes a signal as a linear combination of Gaussian Gabor elementary functions. After decomposing the signal, this VI adds the Wigner-Ville Distribution (WVD) and cross WVD of the elementary functions to compute the quadratic time-frequency representation of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-fast-gabor-spectrogram-real-vi.png']

#### Inputs/Outputs

| zoom settings — zoom settings specifies the frequency zoom factor and the zoom range. zoom factor — zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. f0 — f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals -fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins — number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is -1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factorxfrequency bins for real-valued input signals and must not be greater than zoom factorxfrequency bins for complex-valued input signals. order — order specifies how this VI balances the time-frequency resolution and the cross-term interference of the Gabor spectrogram. order must be greater than or equal to 0, or this VI sets order to 0 automatically. signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. Gaussian window length — Gaussian window length specifies the length of the Gaussian window, in samples, of the Gabor elementary functions and controls the relationship between the time resolution and the frequency resolution of the spectrogram. Gaussian window length must be a power of 2 and greater than or equal to 8. As the value of Gaussian window length increases, the frequency resolution increases, but the time resolution decreases. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| zoom factor — zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. f0 — f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals -fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins — number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is -1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factorxfrequency bins for real-valued input signals and must not be greater than zoom factorxfrequency bins for complex-valued input signals. |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |

#### TFA Fast Gabor Spectrogram Details

The [Gabor spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_gabor_spectrogram) has better time-frequency resolution than the [STFT spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_stft_spectrogram) method and less cross-term interference than the WVD method. The Gabor spectrogram also allows control of the tradeoff between the cross-term suppression and the joint time-frequency resolution.

The Gabor spectrogram also is called the Gabor expansion-based spectrogram. You can use the [Gabor expansion](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_discrete_gabor_trans_exp) to represent the signal as the linear combination of the time-frequency elementary functions, as shown in the following equation:

[IMAGE alt='image' src='eq_gabor_expansion.gif']

where h<sub>m,n</sub>(i) is the elementary function, and C<sub>m,n</sub> is the Gabor coefficients.

After you represent the signal as the linear combination of the time-frequency elementary function, you can use the following equation to compute the WVD of the signal:

[IMAGE alt='image' src='eq_gabor_wvd.gif']

Thus, any two elementary functions generate the cross-term interferences. Instead of computing the WVD for any pair of elementary functions, you can select a subset for the computation based on the Manhattan distance [IMAGE alt='image' src='eq_manhattan_dist.gif'] between the pair of [IMAGE alt='image' src='eq_func_1.gif'] and [IMAGE alt='image' src='eq_func_2.gif']. The resulting time-frequency distribution is the Gabor spectrogram, as defined in the following equation:

[IMAGE alt='image' src='eq_gabor_spect.gif']

where D denotes the **order**. The joint time-frequency resolution and the cross-term interference of the Gabor spectrogram increases with **order**. When **order** is 0, the Gabor spectrogram is non-negative and is similar to the STFT spectrogram. As **order** approaches infinity, the Gabor spectrogram converges to the WVD.

Refer to the book [Introduction to Time-Frequency and Wavelet Transforms](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_related_doc) for more information about the Gabor expansion and transform.

#### Examples

Refer to the Liquefaction Detection VI in the labview\examples\Time Frequency Analysis\TFAApplications directory for an example of using the TFA Fast Gabor Spectrogram VI.

Parent topic:

TFA Fast Gabor Spectrogram VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-waveform-vi.html language=enus -->
## TOPIC 00015: TFA Fast Gabor Spectrogram (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-fast-gabor-spectrogram-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decomposes a signal as a linear combination of Gaussian Gabor elementary functions. After decomposing the signal, this VI adds the Wigner-Ville Distribution (WVD) and cross WVD of the elementary functions to compute the quadratic time-frequency representation of signal. Wire data to the signal input

### TFA Fast Gabor Spectrogram (Waveform) VI

Decomposes a signal as a linear combination of Gaussian Gabor elementary functions. After decomposing the signal, this VI adds the Wigner-Ville Distribution (WVD) and cross WVD of the elementary functions to compute the quadratic time-frequency representation of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-fast-gabor-spectrogram-waveform-vi.png']

#### Inputs/Outputs

| zoom settings — zoom settings specifies the frequency zoom factor and the zoom range. zoom factor — zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. f0 — f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals -fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins — number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is -1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factorxfrequency bins for real-valued input signals and must not be greater than zoom factorxfrequency bins for complex-valued input signals. order — order specifies how this VI balances the time-frequency resolution and the cross-term interference of the Gabor spectrogram. order must be greater than or equal to 0, or this VI sets order to 0 automatically. signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. Gaussian window length — Gaussian window length specifies the length of the Gaussian window, in samples, of the Gabor elementary functions and controls the relationship between the time resolution and the frequency resolution of the spectrogram. Gaussian window length must be a power of 2 and greater than or equal to 8. As the value of Gaussian window length increases, the frequency resolution increases, but the time resolution decreases. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| zoom factor — zoom factor specifies how much to zoom the spectrogram. zoom factor must be an integer greater than or equal to 1. The default is 1. f0 — f0 specifies the lowest frequency in the resulting spectrogram in hertz. The default is NaN, which indicates that the lowest frequency equals 0 for real-valued input signals and that the lowest frequency equals -fs/2 for complex-valued input signals, where fs is the sampling rate of the signal. number of bins — number of bins specifies the total number of frequency bins in the resulting spectrogram. As the value of number of bins increases, the frequency range of spectrogram increases. The default value is -1, which specifies that the frequency range of spectrogram is from f0 to fs/2, where fs is the sampling rate of the signal. number of bins must not be greater than half of zoom factorxfrequency bins for real-valued input signals and must not be greater than zoom factorxfrequency bins for complex-valued input signals. |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |

#### TFA Fast Gabor Spectrogram Details

The [Gabor spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_gabor_spectrogram) has better time-frequency resolution than the [STFT spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_stft_spectrogram) method and less cross-term interference than the WVD method. The Gabor spectrogram also allows control of the tradeoff between the cross-term suppression and the joint time-frequency resolution.

The Gabor spectrogram also is called the Gabor expansion-based spectrogram. You can use the [Gabor expansion](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_discrete_gabor_trans_exp) to represent the signal as the linear combination of the time-frequency elementary functions, as shown in the following equation:

[IMAGE alt='image' src='eq_gabor_expansion.gif']

where h<sub>m,n</sub>(i) is the elementary function, and C<sub>m,n</sub> is the Gabor coefficients.

After you represent the signal as the linear combination of the time-frequency elementary function, you can use the following equation to compute the WVD of the signal:

[IMAGE alt='image' src='eq_gabor_wvd.gif']

Thus, any two elementary functions generate the cross-term interferences. Instead of computing the WVD for any pair of elementary functions, you can select a subset for the computation based on the Manhattan distance [IMAGE alt='image' src='eq_manhattan_dist.gif'] between the pair of [IMAGE alt='image' src='eq_func_1.gif'] and [IMAGE alt='image' src='eq_func_2.gif']. The resulting time-frequency distribution is the Gabor spectrogram, as defined in the following equation:

[IMAGE alt='image' src='eq_gabor_spect.gif']

where D denotes the **order**. The joint time-frequency resolution and the cross-term interference of the Gabor spectrogram increases with **order**. When **order** is 0, the Gabor spectrogram is non-negative and is similar to the STFT spectrogram. As **order** approaches infinity, the Gabor spectrogram converges to the WVD.

Refer to the book [Introduction to Time-Frequency and Wavelet Transforms](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_related_doc) for more information about the Gabor expansion and transform.

#### Examples

Refer to the Liquefaction Detection VI in the labview\examples\Time Frequency Analysis\TFAApplications directory for an example of using the TFA Fast Gabor Spectrogram VI.

Parent topic:

TFA Fast Gabor Spectrogram VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-online-stft-spectrogram-complex-vi.html language=enus -->
## TOPIC 00016: TFA Online STFT Spectrogram (Complex) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-online-stft-spectrogram-complex-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-online-stft-spectrogram-complex-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the online short-time Fourier transform (STFT)-based spectrogram for signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cbool.png reassigned? (F) reassigned? specifies whether to reassign the spectrogram by

### TFA Online STFT Spectrogram (Complex) VI

Computes the online short-time Fourier transform (STFT)-based spectrogram for **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-online-stft-spectrogram-complex-vi.png']

#### Inputs/Outputs

| reassigned? (F) — reassigned? specifies whether to reassign the spectrogram by moving dispersed energy to the local center of gravity in the joint time-frequency domain. The reassignment can improve the readability of the spectrogram. The default is FALSE. reset? (F) — reset? specifies whether to clear the buffer for the online computation and use the new window info you specify. The default is FALSE. signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins is the FFT block size of the STFT. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. window info — window info specifies the sliding window to use to truncate the signal and defines the resolution of the resulting time-frequency representation. type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined window — user defined window specifies the sliding window to use to compute the STFT. If you specify a value for user defined window, this VI ignores the settings in the window info input. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins is the FFT block size of the STFT. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
| type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. |

#### Examples

Refer to the following VIs for examples of using the TFA Online STFT Spectrogram VI:

- Online Spectrogram Monitoring (Simulated) VI: labview\examples\Time Frequency Analysis\TFAFunctions
- Online Spectrogram Monitoring (DAQmx) VI: labview\examples\Time Frequency Analysis\TFAFunctions
- Online Spectrogram Monitoring (Sound Card) VI: labview\examples\Time Frequency Analysis\TFAFunctions

Parent topic:

TFA Online STFT Spectrogram VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-stft-spectrogram-waveform-vi.html language=enus -->
## TOPIC 00017: TFA STFT Spectrogram (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-stft-spectrogram-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-stft-spectrogram-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the short-time Fourier transform (STFT)-based spectrogram of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cbool.png reassigned? (F) reassigned? specifies whether to reassign the spectrogram by moving

### TFA STFT Spectrogram (Waveform) VI

Computes the short-time Fourier transform (STFT)-based spectrogram of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-stft-spectrogram-waveform-vi.png']

#### Inputs/Outputs

| reassigned? (F) — reassigned? specifies whether to reassign the spectrogram by moving dispersed energy to the local center of gravity in the joint time-frequency domain. The reassignment can improve the readability of the spectrogram. The default is FALSE. extension — extension specifies the method to use to pad data at the borders of the input signal to lessen discontinuity. The extension length is half the window length. signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. window info — window info specifies the sliding window to use to compute the STFT and defines the resolution of the resulting time-frequency representation. Use the user defined window input to specify a customized window. type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined window — user defined window specifies the coefficients of the sliding window to use to compute the STFT. If you specify a value for user defined window, this VI ignores the settings in the window info input. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
| type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. |

#### TFA STFT Spectrogram Details

The STFT spectrogram is the square of the magnitude of the resulting coefficients from the [STFT](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_stft). The STFT spectrogram is non-negative. All the values of the STFT spectrogram are positive. The other time-frequency representations, such as the [Wigner-Ville Distribution](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_wvd), the [Choi-Williams Distribution](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_cwd_csd), the [Cone-Shaped Distribution](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_cwd_csd), and the [Gabor spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_gabor_spectrogram), can be negative.

Refer to the book [Introduction to Time-Frequency and Wavelet Transforms](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_related_doc) for more information about reassignment.

#### Examples

Refer to the following VIs for examples of using the TFA STFT Spectrogram VI:

- Color Tables for Displaying the Spectrogram VI: labview\examples\Time Frequency Analysis\TFAGettingStarted
- Group Delay VI: labview\examples\Time Frequency Analysis\TFAFunctions
- Mean Instantaneous Frequency or Bandwidth (MIF or MIB) VI: labview\examples\Time Frequency Analysis\TFAFunctions
- Time-Frequency Resolution VI: labview\examples\Time Frequency Analysis\TFAGettingStarted

Parent topic:

TFA STFT Spectrogram VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-wigner-ville-distribution-waveform-vi.html language=enus -->
## TOPIC 00018: TFA Wigner-Ville Distribution (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-wigner-ville-distribution-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/spectrogram-llb/tfa-wigner-ville-distribution-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the discrete Wigner-Ville Distribution (WVD) of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cmsdt.png signal signal specifies the input signal. cnclst.png time-frequency sampling info time-frequency

### TFA Wigner-Ville Distribution (Waveform) VI

Computes the discrete Wigner-Ville Distribution (WVD) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-wigner-ville-distribution-waveform-vi.png']

#### Inputs/Outputs

| signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the joint time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. analytic signal? (T) — analytic signal? specifies whether to convert the real input signal to the corresponding analytic signal. The default is TRUE. spectrogram — spectrogram returns the quadratic time-frequency representation of the signal. Each row corresponds to the instantaneous power spectrum at a certain time. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of spectrogram. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins specifies the number of bins along the frequency axis to sample the signal in the joint time-frequency domain. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |

#### TFA Wigner-Ville Distribution Details

The WVD is one of the quadratic time-frequency representation methods. The WVD has better joint time-frequency resolution than the [short-time Fourier transform (STFT) spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_stft_spectrogram), whose resolution the window effect limits. You can compute the WVD by applying the fast Fourier transform (FFT) on the time-dependent autocorrelation as shown in the following equation:

[IMAGE alt='image' src='eq_wvd.gif']

where [IMAGE alt='image' src='eq_time_dep_autocorr_st.gif'] is the time-dependent autocorrelation of the signal s(t) defined by the following equation:

[IMAGE alt='image' src='eq_wvd_2.gif']

The WVD has the best joint time-frequency resolution among all known quadratic joint time-frequency analysis methods. It also preserves many useful properties, such as the time marginal condition as follows:

[IMAGE alt='image' src='eq_time_marg_cond.gif']

and the frequency marginal condition as follows:

[IMAGE alt='image' src='eq_freq_marg_cond.gif']

However, signal components with a different [central time](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency) or [central frequency](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_central_time_frequency) generate [cross-term interference](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_wvd) in the WVD. The cross-term interference reduces the readability of the time-frequency representation. Because real-valued signals have symmetric positive and negative frequency components, cross-term interference exists between the positive frequency components and the negative frequency components in the WVD of real-valued signals. If you convert real-valued signals into [analytic signals](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_analytic_signals), this VI suppresses the cross-term interference between the positive frequency components and the negative frequency components because analytic signals have only the positive frequency components of real-valued signals.

You can consider the [Cohen's class distributions](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_cwd_csd) (the Choi-Williams Distribution and the Cone-Shaped Distribution) and the STFT spectrogram as the smoothed versions of the WVD. These time-frequency distributions suppress the cross-term interference, but they also lose some useful properties of the WVD and produce a degraded time-frequency resolution. Use the WVD if you need a high time-frequency resolution and the frequency components of the signal are relatively simple. If harmonics or other types of complicated frequency components exist in the signal, use the Cohen's class distributions or [Gabor spectrogram](/csh?context=lvmnt_aspt_lvasptconcepts_tfa_gabor_spectrogram) to suppress the cross-term interference.

#### Examples

Refer to the following VIs for examples of using the TFA Wigner-Ville Distribution VI:

- Marginal Condition VI: labview\examples\Time Frequency Analysis\TFAFunctions
- Pseudo Wigner-Ville Distribution VI: labview\examples\Time Frequency Analysis\TFAFunctions

Parent topic:

TFA Wigner-Ville Distribution VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-adaptive-expansion-complex-vi.html language=enus -->
## TOPIC 00019: TFA Adaptive Expansion (Complex) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-adaptive-expansion-complex-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-adaptive-expansion-complex-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reconstructs a signal from the Gaussian chirplet elementary functions. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cnclst.png sampling info sampling info speci

### TFA Adaptive Expansion (Complex) VI

Reconstructs a signal from the Gaussian chirplet elementary functions. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='tfa-adaptive-expansion-complex-vi.png']

#### Inputs/Outputs

| sampling info — sampling info specifies the sampling information of the reconstructed signal. sampling rate — sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. length — length specifies the length, in samples, of the reconstructed signal. The default is -1, which specifies that length equals the largest value of center + 4xstandard deviation. chirplet info — chirplet info specifies the parameters of each elementary function. amplitude — amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. standard deviation — standard deviation specifies the standard deviation of the Gaussian envelope in seconds. center — center specifies the central time of the Gaussian envelope in seconds. frequency — frequency specifies the central frequency of the chirplet in hertz. chirp rate — chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. signal — signal returns the reconstructed signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| sampling rate — sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. length — length specifies the length, in samples, of the reconstructed signal. The default is -1, which specifies that length equals the largest value of center + 4xstandard deviation. |
| amplitude — amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. standard deviation — standard deviation specifies the standard deviation of the Gaussian envelope in seconds. center — center specifies the central time of the Gaussian envelope in seconds. frequency — frequency specifies the central frequency of the chirplet in hertz. chirp rate — chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |

#### Examples

Refer to the Adaptive Transform (ADT) and Adaptive Expansion (ADE) VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Adaptive Expansion VI.

Parent topic:

TFA Adaptive Expansion VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-adaptive-expansion-real-vi.html language=enus -->
## TOPIC 00020: TFA Adaptive Expansion (Real) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-adaptive-expansion-real-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-adaptive-expansion-real-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reconstructs a signal from the Gaussian chirplet elementary functions. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cnclst.png sampling info sampling info speci

### TFA Adaptive Expansion (Real) VI

Reconstructs a signal from the Gaussian chirplet elementary functions. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='tfa-adaptive-expansion-real-vi.png']

#### Inputs/Outputs

| sampling info — sampling info specifies the sampling information of the reconstructed signal. sampling rate — sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. length — length specifies the length, in samples, of the reconstructed signal. The default is -1, which specifies that length equals the largest value of center + 4xstandard deviation. chirplet info — chirplet info specifies the parameters of each elementary function. amplitude — amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. standard deviation — standard deviation specifies the standard deviation of the Gaussian envelope in seconds. center — center specifies the central time of the Gaussian envelope in seconds. frequency — frequency specifies the central frequency of the chirplet in hertz. chirp rate — chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. signal — signal returns the reconstructed signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| sampling rate — sampling rate specifies the sampling rate of the reconstructed signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. length — length specifies the length, in samples, of the reconstructed signal. The default is -1, which specifies that length equals the largest value of center + 4xstandard deviation. |
| amplitude — amplitude specifies the complex amplitude of the chirplet or Gaussian pulse. standard deviation — standard deviation specifies the standard deviation of the Gaussian envelope in seconds. center — center specifies the central time of the Gaussian envelope in seconds. frequency — frequency specifies the central frequency of the chirplet in hertz. chirp rate — chirp rate specifies the sweep rate of the carrier sine wave in hertz per second. |

#### Examples

Refer to the Adaptive Transform (ADT) and Adaptive Expansion (ADE) VI in the labview\examples\Time Frequency Analysis\TFAFunctions directory for an example of using the TFA Adaptive Expansion VI.

Parent topic:

TFA Adaptive Expansion VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-real-vi.html language=enus -->
## TOPIC 00021: TFA Online Gabor Expansion (Real) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-real-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-real-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the online Gabor expansion with Gabor coef. Wire data to the signal output to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cbool.png reset? (F) reset? specifies whether to clear the buffer for the online computation and use the new expansion

### TFA Online Gabor Expansion (Real) VI

Computes the online Gabor expansion with **Gabor coef**. Wire data to the **signal** output to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-online-gabor-expansion-real-vi.png']

#### Inputs/Outputs

| reset? (F) — reset? specifies whether to clear the buffer for the online computation and use the new expansion info you specify. The default is FALSE. Gabor coef — Gabor coef specifies the weights of the Gabor elementary functions. expansion info — expansion info specifies the Gabor elementary functions to use for the Gabor expansion. The settings of expansion info take effect the first time you run this VI or when you set reset? to TRUE. synthesis window — synthesis window specifies the window of the Gabor elementary functions. The size of synthesis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps) — dM (time steps) specifies the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. National Instruments recommends that you set dM (time steps) to a power of 2. N (frequency bins) — N (frequency bins) specifies the number of frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. signal — signal returns the reconstructed signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| synthesis window — synthesis window specifies the window of the Gabor elementary functions. The size of synthesis window must be divided evenly by dM (time steps) and N (frequency bins). dM (time steps) — dM (time steps) specifies the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. National Instruments recommends that you set dM (time steps) to a power of 2. N (frequency bins) — N (frequency bins) specifies the number of frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. |

#### Examples

Refer to the following VIs for examples of using the TFA Online Gabor Expansion VI:

- Online Noise Reduction VI: labview\examples\Time Frequency Analysis\TFAApplications
- Voice Enhancement VI: labview\examples\Time Frequency Analysis\TFAApplications
- Online Pitch Shifting VI: labview\examples\Time Frequency Analysis\TFAApplications

Parent topic:

TFA Online Gabor Expansion VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-vi.html language=enus -->
## TOPIC 00022: TFA Online Gabor Expansion VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the online Gabor expansion with Gabor coef. Wire data to the signal output to determine the polymorphic instance to use or manually select the instance. icon Examples Refer to the following VIs for examples of using the TFA Online Gabor Expansion VI:Online Noise Reduction VI: labview\exampl

### TFA Online Gabor Expansion VI

Computes the online Gabor expansion with **Gabor coef**. Wire data to the **signal** output to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-online-gabor-expansion-vi.png']

#### Examples

Refer to the following VIs for examples of using the TFA Online Gabor Expansion VI:

- Online Noise Reduction VI: labview\examples\Time Frequency Analysis\TFAApplications
- Voice Enhancement VI: labview\examples\Time Frequency Analysis\TFAApplications
- Online Pitch Shifting VI: labview\examples\Time Frequency Analysis\TFAApplications

- [TFA Online Gabor Expansion (Waveform) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-waveform-vi.html) Computes the online Gabor expansion with Gabor coef . Wire data to the signal output to determine the polymorphic instance to use or manually select the instance.
- [TFA Online Gabor Expansion (Real) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-real-vi.html) Computes the online Gabor expansion with Gabor coef . Wire data to the signal output to determine the polymorphic instance to use or manually select the instance.
- [TFA Online Gabor Expansion (Complex) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-expansion-complex-vi.html) Computes the online Gabor expansion with Gabor coef . Wire data to the signal output to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Online JTFA

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-vi.html language=enus -->
## TOPIC 00023: TFA Online Gabor Transform VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the online Gabor transform for signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Examples Refer to the following VIs for examples of using the TFA Online Gabor Transform VI:Online Noise Reduction VI: labview\examples\Tim

### TFA Online Gabor Transform VI

Computes the online Gabor transform for **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-online-gabor-transform-vi.png']

#### Examples

Refer to the following VIs for examples of using the TFA Online Gabor Transform VI:

- Online Noise Reduction VI: labview\examples\Time Frequency Analysis\TFAApplications
- Voice Enhancement VI: labview\examples\Time Frequency Analysis\TFAApplications
- Online Pitch Shifting VI: labview\examples\Time Frequency Analysis\TFAApplications

- [TFA Online Gabor Transform (Waveform) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-waveform-vi.html) Computes the online Gabor transform for signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [TFA Online Gabor Transform (Real) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-real-vi.html) Computes the online Gabor transform for signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [TFA Online Gabor Transform (Complex) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-complex-vi.html) Computes the online Gabor transform for signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Online JTFA

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-waveform-vi.html language=enus -->
## TOPIC 00024: TFA Online Gabor Transform (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-online-gabor-transform-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the online Gabor transform for signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cbool.png reset? (F) reset? specifies whether to clear the buffer for the online computation and use the new transform info

### TFA Online Gabor Transform (Waveform) VI

Computes the online Gabor transform for **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tfa-online-gabor-transform-waveform-vi.png']

#### Inputs/Outputs

| reset? (F) — reset? specifies whether to clear the buffer for the online computation and use the new transform info you specify. The default is FALSE. signal — signal specifies the input signal. transform info — transform info specifies the analysis window to use for the Gabor transform. You can use the Dual Window Express VI to design the analysis window. The settings of transform info take effect the first time you run this VI or when you set reset? to TRUE. analysis window — analysis window specifies the window to use to compute the Gabor coefficients. dM (time steps) — dM (time steps) specifies the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. National Instruments recommends that you set dM (time steps) to a power of 2. N (frequency bins) — N (frequency bins) specifies the number of frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Gabor coef — Gabor coef returns the linear time-frequency representation of the signal. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of Gabor coef. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| analysis window — analysis window specifies the window to use to compute the Gabor coefficients. dM (time steps) — dM (time steps) specifies the time shift, in samples, between elementary functions. The time sampling interval of the signal in the time-frequency domain is dM (time steps)/fs, where fs is the sampling rate of the signal. National Instruments recommends that you set dM (time steps) to a power of 2. N (frequency bins) — N (frequency bins) specifies the number of frequencies of the Gabor elementary functions. The frequency sampling interval of the signal in the time-frequency plane is fs/N (frequency bins), where fs is the sampling rate of the signal. N (frequency bins) must be a power of 2. |

#### Examples

Refer to the following VIs for examples of using the TFA Online Gabor Transform VI:

- Online Noise Reduction VI: labview\examples\Time Frequency Analysis\TFAApplications
- Voice Enhancement VI: labview\examples\Time Frequency Analysis\TFAApplications
- Online Pitch Shifting VI: labview\examples\Time Frequency Analysis\TFAApplications

Parent topic:

TFA Online Gabor Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-complex-vi.html language=enus -->
## TOPIC 00025: TFA STFT (Complex) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-complex-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-complex-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the short-time Fourier transform (STFT) of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cu16.png extension extension specifies the method to us

### TFA STFT (Complex) VI

Computes the short-time Fourier transform (STFT) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='tfa-stft-complex-vi.png']

#### Inputs/Outputs

| extension — extension specifies the method to use to pad data at the borders of the input signal to lessen discontinuity. The extension length is half the window length. signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins is the FFT block size of the STFT. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. window info — window info specifies the sliding window to use to compute the STFT and defines the resolution of the resulting time-frequency representation. Use the user defined window input to specify a customized window. type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined window — user defined window specifies the coefficients of the sliding window to use to compute the STFT. If you specify a value for user defined window, this VI ignores the settings in the window info input. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. STFT coef — STFT coef returns the linear time-frequency representation of the signal. Use the TFA Coefficients Indicator to display the magnitude of STFT coef on an intensity graph. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of STFT coef. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins is the FFT block size of the STFT. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
| type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. |

#### TFA STFT Details

The short-time Fourier transform (STFT) is the simplest method to use to analyze a time-varying signal or nonstationary signal whose frequency component varies over time. To compute the STFT of an entire signal, this VI uses a sliding window to divide the signal into several blocks and then applies the fast Fourier transform (FFT) to each data block to obtain the frequency contents. You can overlap the sliding window. The following illustration shows the computing procedure of the STFT:

[IMAGE alt='image' src='stft.gif']

The STFT aligns the center of the first sliding window with the first sample of the signal and extends the signal at the beginning with zeros or the signal itself. L is the window length, and dM is the step size to move the sliding window.

You can use the following equation to compute the STFT:

[IMAGE alt='image' src='eq_stft.gif']

where s[i] is the signal, [IMAGE alt='image' src='eq_window_func.gif'] is the window function, L is the window length, dM is **time step**, and N is **frequency bins**. The window function determines the joint time-frequency resolution of the STFT. The longer the window length, the better the frequency resolution and the worse the time resolution. When dM is greater than or equal to the window length, L, no overlap exists between sliding windows. When dM is smaller than the window length, the overlap in percent equals 100×((L-dM)/L). For example, if you set the window length to 256 and **time steps** to 64, the overlap is 75%.

Parent topic:

TFA STFT VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-real-vi.html language=enus -->
## TOPIC 00026: TFA STFT (Real) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-real-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-real-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the short-time Fourier transform (STFT) of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cu16.png extension extension specifies the method to us

### TFA STFT (Real) VI

Computes the short-time Fourier transform (STFT) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='tfa-stft-real-vi.png']

#### Inputs/Outputs

| extension — extension specifies the method to use to pad data at the borders of the input signal to lessen discontinuity. The extension length is half the window length. signal — signal specifies the input signal. time-frequency sampling info — time-frequency sampling info specifies the density to use to sample the signal in the time-frequency domain and defines the size of the resulting 2D time-frequency array. time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins is the FFT block size of the STFT. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. window info — window info specifies the sliding window to use to compute the STFT and defines the resolution of the resulting time-frequency representation. Use the user defined window input to specify a customized window. type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined window — user defined window specifies the coefficients of the sliding window to use to compute the STFT. If you specify a value for user defined window, this VI ignores the settings in the window info input. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. STFT coef — STFT coef returns the linear time-frequency representation of the signal. Use the TFA Coefficients Indicator to display the magnitude of STFT coef on an intensity graph. scale info — scale info returns the time scale and the frequency scale information of the time-frequency representation, including the time offset, the time interval between every two contiguous rows, the frequency offset, and the frequency interval between every two contiguous columns of STFT coef. Use the TFA Get Time and Freq Scale Info VI to return detailed information about the time scale and the frequency scale. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in samples, along the time axis in the joint time-frequency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in spectrogram. frequency bins — frequency bins is the FFT block size of the STFT. frequency bins must be a power of 2 and greater than 0. The scale info output contains the actual sampling period in hertz along the frequency axis. |
| type — type specifies the type of the sliding window. length — length specifies the length, in samples, of the sliding window. The default is -1, which indicates that this VI sets the window length to four times time steps. Thus, the overlap between sliding windows is 75 percent. However, this VI wraps the default window length to 64 when time steps is less than 16. |

#### TFA STFT Details

The short-time Fourier transform (STFT) is the simplest method to use to analyze a time-varying signal or nonstationary signal whose frequency component varies over time. To compute the STFT of an entire signal, this VI uses a sliding window to divide the signal into several blocks and then applies the fast Fourier transform (FFT) to each data block to obtain the frequency contents. You can overlap the sliding window. The following illustration shows the computing procedure of the STFT:

[IMAGE alt='image' src='stft.gif']

The STFT aligns the center of the first sliding window with the first sample of the signal and extends the signal at the beginning with zeros or the signal itself. L is the window length, and dM is the step size to move the sliding window.

You can use the following equation to compute the STFT:

[IMAGE alt='image' src='eq_stft.gif']

where s[i] is the signal, [IMAGE alt='image' src='eq_window_func.gif'] is the window function, L is the window length, dM is **time step**, and N is **frequency bins**. The window function determines the joint time-frequency resolution of the STFT. The longer the window length, the better the frequency resolution and the worse the time resolution. When dM is greater than or equal to the window length, L, no overlap exists between sliding windows. When dM is smaller than the window length, the overlap in percent equals 100×((L-dM)/L). For example, if you set the window length to 256 and **time steps** to 64, the overlap is 75%.

Parent topic:

TFA STFT VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-vi.html language=enus -->
## TOPIC 00027: TFA STFT VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the short-time Fourier transform (STFT) of signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. Use the pull-down menu to select an instance of this VI. icon TFA STFT Details The short-time Fourier transform (STFT) is the simple

### TFA STFT VI

Computes the short-time Fourier transform (STFT) of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='tfa-stft-vi.png']

#### TFA STFT Details

The short-time Fourier transform (STFT) is the simplest method to use to analyze a time-varying signal or nonstationary signal whose frequency component varies over time. To compute the STFT of an entire signal, this VI uses a sliding window to divide the signal into several blocks and then applies the fast Fourier transform (FFT) to each data block to obtain the frequency contents. You can overlap the sliding window. The following illustration shows the computing procedure of the STFT:

[IMAGE alt='image' src='stft.gif']

The STFT aligns the center of the first sliding window with the first sample of the signal and extends the signal at the beginning with zeros or the signal itself. L is the window length, and dM is the step size to move the sliding window.

You can use the following equation to compute the STFT:

[IMAGE alt='image' src='eq_stft.gif']

where s[i] is the signal, [IMAGE alt='image' src='eq_window_func.gif'] is the window function, L is the window length, dM is **time step**, and N is **frequency bins**. The window function determines the joint time-frequency resolution of the STFT. The longer the window length, the better the frequency resolution and the worse the time resolution. When dM is greater than or equal to the window length, L, no overlap exists between sliding windows. When dM is smaller than the window length, the overlap in percent equals 100×((L-dM)/L). For example, if you set the window length to 256 and **time steps** to 64, the overlap is 75%.

- [TFA STFT (Waveform) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-waveform-vi.html) Computes the short-time Fourier transform (STFT) of signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [TFA STFT (Real) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-real-vi.html) Computes the short-time Fourier transform (STFT) of signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [TFA STFT (Complex) VI](../../../../vi-lib/addons/time-frequency-analysis/transform-llb/tfa-stft-complex-vi.html) Computes the short-time Fourier transform (STFT) of signal . Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Time Frequency Transform

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-frequency-analysis/utilities-llb/tfa-get-time-and-freq-scale-info-vi.html language=enus -->
## TOPIC 00028: TFA Get Time and Freq Scale Info VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-frequency-analysis/utilities-llb/tfa-get-time-and-freq-scale-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-frequency-analysis/utilities-llb/tfa-get-time-and-freq-scale-info-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time scale information and the frequency scale information of the time-frequency representation. icon Inputs/Outputs cfxdt.png scale info scale info specifies the time scale information and the frequency scale information of the time frequency representation. cerrcodeclst.png error in (no e

### TFA Get Time and Freq Scale Info VI

Gets the time scale information and the frequency scale information of the time-frequency representation.

[IMAGE alt='icon' src='tfa-get-time-and-freq-scale-info-vi.png']

#### Inputs/Outputs

| scale info — scale info specifies the time scale information and the frequency scale information of the time frequency representation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. time info — time info returns the time scale information. time offset — time offset returns the offset of the time scale in seconds. time multiplier — time multiplier returns the multiplier of the time scale in seconds, for example, the time interval of the time-frequency representation. frequency info — frequency info returns the frequency scale information. frequency offset — frequency offset returns the offset of the frequency scale in hertz. frequency multiplier — frequency multiplier returns the multiplier of the frequency scale in hertz, for example, the frequency interval of the time-frequency representation. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time offset — time offset returns the offset of the time scale in seconds. time multiplier — time multiplier returns the multiplier of the time scale in seconds, for example, the time interval of the time-frequency representation. |
| frequency offset — frequency offset returns the offset of the frequency scale in hertz. frequency multiplier — frequency multiplier returns the multiplier of the frequency scale in hertz, for example, the frequency interval of the time-frequency representation. |

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-array-vi.html language=enus -->
## TOPIC 00029: TSA AR Spectrum (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive (AR) modeling. The PSD computed with this method is exempt from window effects and has a better frequency resolution than the results from using the periodogram method. icon Inputs/Outputs cdbl

### TSA AR Spectrum (Array) VI

Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive (AR) modeling. The PSD computed with this method is exempt from window effects and has a better frequency resolution than the results from using the periodogram method.

[IMAGE alt='icon' src='tsa-ar-spectrum-array-vi.png']

#### Inputs/Outputs

| sampling rate — sampling rate specifies the sampling rate, in hertz, of the univariate time series Xt. The default is 1. frequency bins — frequency bins specifies the number of frequency bins for which this VI computes the single-sided power spectral density PSD. The length of the single-sided PSD is (frequency bins/2+1). The default is 1024. Xt — Xt specifies the univariate time series. AR method — AR method specifies the method this VI uses to estimate the autoregressive (AR) model. AR order — AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. dB on? (T) — dB on? specifies whether this VI returns the PSD in decibels or in a linear scale. If dB on? is TRUE, this VI returns the PSD in decibels. If dB on? is FALSE, this VI returns the PSD in a linear scale. The default is TRUE. PSD — PSD returns information about the single-sided power spectral density (PSD). f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. |

#### TSA AR Spectrum Details

This VI computes the single-sided PSD of a univariate time series based on AR modeling according to the following equation:

[IMAGE alt='image' src='tsa_equ_arspec.gif']

where S(f) is the PSD of the time series. df is the frequency interval, which is computed as f<sub>s</sub>/N. N is the number of frequency bins, f<sub>s</sub> is the sampling rate, and s² is the noise variance of the estimated AR model of the time series. a is an array that contains the coefficients of the AR model. a=[1, a<sub>1</sub>, a<sub>2</sub>,… ,a<sub>n</sub>], where n is **AR order**. Before computing the PSD, this VI wraps a to N-point series a'.

The minimum length requirement for the input time series needs to be at least two times the **AR order**.

#### Examples

Refer to the Power Spectral Density Estimation VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA AR Spectrum VI.

Parent topic:

TSA AR Spectrum VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-vi.html language=enus -->
## TOPIC 00030: TSA AR Spectrum VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive (AR) modeling. The PSD computed with this method is exempt from window effects and has a better frequency resolution than the results from using the periodogram method. icon TSA AR Spectrum Det

### TSA AR Spectrum VI

Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive (AR) modeling. The PSD computed with this method is exempt from window effects and has a better frequency resolution than the results from using the periodogram method.

[IMAGE alt='icon' src='tsa-ar-spectrum-vi.png']

#### TSA AR Spectrum Details

This VI computes the single-sided PSD of a univariate time series based on AR modeling according to the following equation:

[IMAGE alt='image' src='tsa_equ_arspec.gif']

where S(f) is the PSD of the time series. df is the frequency interval, which is computed as f<sub>s</sub>/N. N is the number of frequency bins, f<sub>s</sub> is the sampling rate, and s² is the noise variance of the estimated AR model of the time series. a is an array that contains the coefficients of the AR model. a=[1, a<sub>1</sub>, a<sub>2</sub>,… ,a<sub>n</sub>], where n is **AR order**. Before computing the PSD, this VI wraps a to N-point series a'.

The minimum length requirement for the input time series needs to be at least two times the **AR order**.

#### Examples

Refer to the Power Spectral Density Estimation VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA AR Spectrum VI.

- [TSA AR Spectrum (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-waveform-vi.html) Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive (AR) modeling. The PSD computed with this method is exempt from window effects and has a better frequency resolution than the results from using the periodogram method.
- [TSA AR Spectrum (Array) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-ar-spectrum-array-vi.html) Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive (AR) modeling. The PSD computed with this method is exempt from window effects and has a better frequency resolution than the results from using the periodogram method.

Parent topic:

Correlation and Spectral Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-arma-spectrum-waveform-vi.html language=enus -->
## TOPIC 00031: TSA ARMA Spectrum (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-arma-spectrum-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-arma-spectrum-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive-moving average (ARMA) modeling. The PSD computed by this VI is exempt from window effects and has a better frequency resolution than the result from using the TSA Periodogram VI. This VI also m

### TSA ARMA Spectrum (Waveform) VI

Computes the single-sided power spectral density (PSD) of a univariate time series based on autoregressive-moving average (ARMA) modeling. The PSD computed by this VI is exempt from window effects and has a better frequency resolution than the result from using the TSA Periodogram VI. This VI also matches the valleys in the spectrum better than the TSA AR Spectrum VI. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-arma-spectrum-waveform-vi.png']

#### Inputs/Outputs

| frequency bins — frequency bins specifies the number of frequency bins for which this VI computes the single-sided power spectral density PSD. The length of the single-sided PSD is (frequency bins/2+1). The default is 1024. Xt — Xt specifies the univariate time series. method — method specifies the method to use in estimating the autoregressive-moving average model. ARMA order — ARMA order specifies the order of the autoregressive-moving average model. AR — AR specifies the AR order of the ARMA model. The value of AR must be greater than 0. The default is 4. MA — MA specifies the MA order of the ARMA model. The value of MA must be greater than 0. The default is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. dB on? (T) — dB on? specifies whether this VI returns the PSD in decibels or in a linear scale. If dB on? is TRUE, this VI returns the PSD in decibels. If dB on? is FALSE, this VI returns the PSD in a linear scale. The default is TRUE. PSD — PSD returns information about the single-sided power spectral density (PSD). f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. unit — unit returns the engineering unit of the PSD. You can specify an engineering unit for a time series by using the TSA Scale to EU VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| AR — AR specifies the AR order of the ARMA model. The value of AR must be greater than 0. The default is 4. MA — MA specifies the MA order of the ARMA model. The value of MA must be greater than 0. The default is 1. |
| f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. |

#### TSA ARMA Spectrum Details

This VI computes the PSD of a univariate time series based on autoregressive-moving average (ARMA) modeling according to the following equation:

[IMAGE alt='image' src='tsa_equ_armaspec.gif']

where S(f) is the PSD of the time series, df is the frequency interval, which is computed as f<sub>s</sub>/N. N is the number of frequency bins, f<sub>s</sub> is the sampling rate, and s² is the estimated noise series of the ARMA model of the time series. a is an array that contains the AR coefficients of the ARMA(m, n) model, and a=[1, a<sub>1</sub>, a<sub>2</sub>,…, a<sub>m</sub>]. b is another array that contains the MA coefficients of the ARMA(m, n) model, and b=[1, b<sub>1</sub>, b<sub>2</sub>,…, b<sub>n</sub>]. Before computing the PSD, this VI wraps a, b to N-point series a', b'.

The minimum length requirement for the input time series differs for each method you use:

- Yule-Walker method: minimum length >= AR order + MA order
- High-Order AR method: minimum length >= 5 x MA order
- Polynomial method: minimum length >= 5 x ( AR order + MA order)

#### Examples

Refer to the Power Spectral Density Estimation VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA ARMA Spectrum VI.

Parent topic:

TSA ARMA Spectrum VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-bispectrum-waveform-vi.html language=enus -->
## TOPIC 00032: TSA Bispectrum (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-bispectrum-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-bispectrum-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided bispectrum of a univariate time series using the fast Fourier transform (FFT) or the autoregressive (AR) model based method. The bispectrum is a type of third-order spectrum, which is related to the third moment (skewness) of a time series. The resulting bispectrum can dete

### TSA Bispectrum (Waveform) VI

Computes the single-sided bispectrum of a univariate time series using the fast Fourier transform (FFT) or the autoregressive (AR) model based method. The bispectrum is a type of third-order spectrum, which is related to the third moment (skewness) of a time series. The resulting bispectrum can detect the asymmetric nonlinearities in the input time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-bispectrum-waveform-vi.png']

#### Inputs/Outputs

| initialize? (F) — initialize? specifies whether the input block of data is the first block. The default is FALSE, which means the input block of data is not the first block. frequency bins — frequency bins specifies the number of frequency bins for which this VI computes the bispectrum. The resulting bispectrum S(f,f) is a square 2D array with the size (frequency bins/2+1). The default is -1, which means this VI calculates an appropriate value for the frequency bins. Refer to the Details section for information about how this VI calculates the frequency bins value. Xt — Xt specifies the univariate time series. method — method specifies to compute the bispectrum with the fast Fourier transform (FFT) based or autoregressive (AR) model based method. The default is FFT. window info — window info specifies the information of the sliding window that divides the time series into subsequences. window — window specifies the time-domain window applied to the time series. Options include None (default), Hanning, Hamming, Blackman-Harris, Exact Blackman, Blackman, Flat Top, 4 Term B-Harris, 7 Term B-Harris, and Low Sidelobe. length — length specifies the length of the window. A large window generates a power spectral density (PSD) with small bias but results in a coarse PSD plot. A small window generates a smooth PSD plot but leads to large bias. The default is -1, which indicates that the window length equals the length of the input time series. overlap (%) — overlap specifies the overlap, in percentage, of the moving window that this VI applies to the time series. This parameter determines how much data this VI reuses for the signal space matrix. A large overlap reduces the variance of the resulting power spectrum but increases computation time. The default is 50, which specifies that the overlap is half of the window length. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. dB on? (T) — dB on? specifies whether this VI returns the S(f,f) in decibels or in a linear scale. If dB on? is TRUE, this VI returns the S(f,f) in decibels. If dB on? is FALSE, this VI returns the S(f,f) in a linear scale. The default is TRUE. averaging parameters — averaging parameters specifies how this VI computes the averaging. averaging mode — averaging mode specifies the averaging mode. weighting mode — weighting mode specifies the weighting mode for RMS and vector averaging. number of averages — number of averages specifies the number of averages used for RMS and vector averaging. AR setting — AR setting specifies the settings for the autoregressive (AR) model. This option is valid only when the method is AR Model. AR method — AR method specifies the method this VI uses to estimate the autoregressive (AR) model. AR order — AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. S(f,f) — S(f,f) returns the magnitude of the single-sided bispectrum S(f1, f2). freq bins — freq bins returns the frequency bins at which this VI estimates the bispectrum. averaging done? — averaging done? returns whether the averaging process is complete. averaging done? returns TRUE when the number of averages this VI completes is greater than or equal to the number of averages specified in averaging parameters. Otherwise, averaging done? returns FALSE. averaging done? is always TRUE if the selected averaging mode is No averaging. unit — unit returns the engineering unit of the PSD. You can specify an engineering unit for a time series by using the TSA Scale to EU VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| window — window specifies the time-domain window applied to the time series. Options include None (default), Hanning, Hamming, Blackman-Harris, Exact Blackman, Blackman, Flat Top, 4 Term B-Harris, 7 Term B-Harris, and Low Sidelobe. length — length specifies the length of the window. A large window generates a power spectral density (PSD) with small bias but results in a coarse PSD plot. A small window generates a smooth PSD plot but leads to large bias. The default is -1, which indicates that the window length equals the length of the input time series. overlap (%) — overlap specifies the overlap, in percentage, of the moving window that this VI applies to the time series. This parameter determines how much data this VI reuses for the signal space matrix. A large overlap reduces the variance of the resulting power spectrum but increases computation time. The default is 50, which specifies that the overlap is half of the window length. |
| averaging mode — averaging mode specifies the averaging mode. weighting mode — weighting mode specifies the weighting mode for RMS and vector averaging. number of averages — number of averages specifies the number of averages used for RMS and vector averaging. |
| AR method — AR method specifies the method this VI uses to estimate the autoregressive (AR) model. AR order — AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |

#### TSA Bispectrum Details

This VI computes the single-sided bispectrum of a univariate time series using the FFT based method according to the following equation:

S(f<sub>1</sub>, f<sub>2</sub>) = A[X(f<sub>1</sub>)X(f<sub>2</sub>)X*(f<sub>1</sub>+f<sub>2</sub>)]

A[X] denotes the averaging value of X. X(f) is the Fourier transform of the time series X<sub>t</sub> according to the following equation.

[IMAGE alt='image' src='tsa_equ_bispe3.gif']

where N is the number of frequency bins and f<sub>s</sub> is the sampling rate. Before computing the bispectrum, this VI adjusts the value of the window length, **length**, and the value of **frequency bins** according to the following table.

| signal block size | length | adjusted length | frequency bins | adjusted frequency bins |
| --- | --- | --- | --- | --- |
| <=1024 | -1 | signal block size | -1 | signal block size |
| >1024 | -1 | 1024 | -1 | 1024 |
| arbitrary | arbitrary | no change | -1 | length |
| arbitrary | -1 | signal block size | <signal block size | signal block size |
| arbitrary | -1 | signal block size | >=signal block size | no change |
| arbitrary | arbitrary | no change | >=length | no change |
| arbitrary | arbitrary | no change | <length | length |

This VI computes the bispectrum of a univariate time series using the AR model based method according to the following equation:

S(f<sub>1</sub>, f<sub>2</sub>) = bA[X(f<sub>1</sub>)X(f<sub>2</sub>)X*(f<sub>1</sub>+f<sub>2</sub>)]

b is the third moment of estimated noise series of AR model.

[IMAGE alt='image' src='tsa_equ_bispe4.gif']

s² is the noise variance of the estimated AR model of the time series and a is an array that contains the coefficients of the AR model. a=[1, a<sub>1</sub>, a<sub>2</sub>,… ,a<sub>n</sub>], where n is **AR order**. Before computing the bispectrum, this VI wraps a to an N-point series a'.

#### Examples

Refer to the following VIs for examples of using the TSA Bispectrum VI:

- Bispectrum Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted
- Beam Crack Detection VI: labview\examples\Time Series Analysis\TSAApplications

Parent topic:

TSA Bispectrum VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-complex-cepstrum-waveform-vi.html language=enus -->
## TOPIC 00033: TSA Complex Cepstrum (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-complex-cepstrum-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-complex-cepstrum-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided complex cepstrum of a univariate time series. This VI keeps the phase information of the input time series. You can reconstruct the original time series with the computed phase information and complex cepstrum. Wire data to the Xt input to determine the polymorphic instance

### TSA Complex Cepstrum (Waveform) VI

Computes the single-sided complex cepstrum of a univariate time series. This VI keeps the phase information of the input time series. You can reconstruct the original time series with the computed phase information and complex cepstrum. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-complex-cepstrum-waveform-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. cepstrum — cepstrum returns the cepstrum information about Xt. t0 — t0 returns the lower boundary of the time range. dt — dt returns the time increment. C(t) — C(t) returns the resulting values of the complex cepstrum. phase info — phase info returns the phase information of Xt. DC — DC returns the phase information at zero frequency. Nyquist — Nyquist returns the phase information at the Nyquist frequency. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 returns the lower boundary of the time range. dt — dt returns the time increment. C(t) — C(t) returns the resulting values of the complex cepstrum. |
| DC — DC returns the phase information at zero frequency. Nyquist — Nyquist returns the phase information at the Nyquist frequency. |

#### TSA Complex Cepstrum Details

This VI computes the single-sided complex cepstrum C(t) of a univariate time series according to the following equation:

C(t) =FFT<sup>-1</sup>{ln[FFT(X<sub>t</sub>)]}

where X<sub>t</sub> is the univariate time series and FFT(X<sub>t</sub>) is a complex array. FFT(X<sub>t</sub>) = P(f)e<sup>jf(f)</sup>.

In order to make the definition unique, this VI unwraps f(f) and removes the linear phase, so the computed **cepstrum** does not contain the phase information of the original time series. This VI saves the phase values of f(f) at frequency zero and frequency p into **phase info**. You can reconstruct the original time series using the phase values and the complex cepstrum.

#### Examples

Refer to the following VIs for examples of using the TSA Complex Cepstrum VI:

- Echo Canceling VI: labview\examples\Time Series Analysis\TSAApplications
- Cepstrum Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Complex Cepstrum VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-array-vi.html language=enus -->
## TOPIC 00034: TSA Inverse Complex Cepstrum (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the Xt output to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ccclst.png cepstrum cepstrum specifies information about the cepstrum. cdbl.png t0 t0 specifies the lo

### TSA Inverse Complex Cepstrum (Array) VI

Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the **Xt** output to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-inverse-complex-cepstrum-array-vi.png']

#### Inputs/Outputs

| cepstrum — cepstrum specifies information about the cepstrum. t0 — t0 specifies the lower boundary of the time range. dt — dt specifies the time increment. C(t) — C(t) specifies the complex cepstrum. phase info — phase info specifies the phase information of the original time series. You can obtain this information when estimating the complex cepstrum. DC — DC specifies the phase information at zero frequency. Nyquist — Nyquist specifies the phase information at the Nyquist frequency. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Xt — Xt returns a univariate time series reconstructed with the information from cepstrum and phase info. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the lower boundary of the time range. dt — dt specifies the time increment. C(t) — C(t) specifies the complex cepstrum. |
| DC — DC specifies the phase information at zero frequency. Nyquist — Nyquist specifies the phase information at the Nyquist frequency. |

#### Examples

Refer to the following VIs for examples of using the TSA Inverse Complex Cepstrum VI:

- Echo Canceling VI: labview\examples\Time Series Analysis\TSAApplications
- Cepstrum Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Inverse Complex Cepstrum VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-vi.html language=enus -->
## TOPIC 00035: TSA Inverse Complex Cepstrum VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the Xt output to determine the polymorphic instance to use or manually select the instance. icon Examples Refer to the following VIs for examples of using the TSA Inverse Complex Cepstrum VI:Echo Canceling VI: labv

### TSA Inverse Complex Cepstrum VI

Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the **Xt** output to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-inverse-complex-cepstrum-vi.png']

#### Examples

Refer to the following VIs for examples of using the TSA Inverse Complex Cepstrum VI:

- Echo Canceling VI: labview\examples\Time Series Analysis\TSAApplications
- Cepstrum Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

- [TSA Inverse Complex Cepstrum (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-waveform-vi.html) Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the Xt output to determine the polymorphic instance to use or manually select the instance.
- [TSA Inverse Complex Cepstrum (Array) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-array-vi.html) Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the Xt output to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Correlation and Spectral Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-waveform-vi.html language=enus -->
## TOPIC 00036: TSA Inverse Complex Cepstrum (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-inverse-complex-cepstrum-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the Xt output to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ccclst.png cepstrum cepstrum specifies information about the cepstrum. cdbl.png t0 t0 specifies the lo

### TSA Inverse Complex Cepstrum (Waveform) VI

Reconstructs a univariate time series by inverting the complex cepstrum. Wire data to the **Xt** output to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-inverse-complex-cepstrum-waveform-vi.png']

#### Inputs/Outputs

| cepstrum — cepstrum specifies information about the cepstrum. t0 — t0 specifies the lower boundary of the time range. dt — dt specifies the time increment. C(t) — C(t) specifies the complex cepstrum. phase info — phase info specifies the phase information of the original time series. You can obtain this information when estimating the complex cepstrum. DC — DC specifies the phase information at zero frequency. Nyquist — Nyquist specifies the phase information at the Nyquist frequency. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Xt — Xt returns a univariate time series reconstructed with the information from cepstrum and phase info. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the lower boundary of the time range. dt — dt specifies the time increment. C(t) — C(t) specifies the complex cepstrum. |
| DC — DC specifies the phase information at zero frequency. Nyquist — Nyquist specifies the phase information at the Nyquist frequency. |

#### Examples

Refer to the following VIs for examples of using the TSA Inverse Complex Cepstrum VI:

- Echo Canceling VI: labview\examples\Time Series Analysis\TSAApplications
- Cepstrum Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Inverse Complex Cepstrum VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-music-waveform-vi.html language=enus -->
## TOPIC 00037: TSA MUSIC (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-music-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-music-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided power spectral density (PSD) of a univariate or multivariate (vector) time series using the multiple signal classification (MUSIC) method. The MUSIC method performs a comprehensive and accurate spectral analysis on multivariate time series. Wire data to the Xt input to dete

### TSA MUSIC (Waveform) VI

Computes the single-sided power spectral density (PSD) of a univariate or multivariate (vector) time series using the multiple signal classification (MUSIC) method. The MUSIC method performs a comprehensive and accurate spectral analysis on multivariate time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-music-waveform-vi.png']

#### Inputs/Outputs

| frequency bins — frequency bins specifies the number of frequency bins for which this VI computes the single-sided power spectral density PSD. The length of the single-sided PSD is (frequency bins/2+1). The default is 1024. Xt — Xt specifies the univariate time series. window info — window info specifies the information of the sliding window that divides the time series into subsequences. window — window specifies the time-domain window applied to the time series. Options include None (default), Hanning, Hamming, Blackman-Harris, Exact Blackman, Blackman, Flat Top, 4 Term B-Harris, 7 Term B-Harris, and Low Sidelobe. length — length specifies the length of the window. A large window generates a power spectral density (PSD) with small bias but results in a coarse PSD plot. A small window generates a smooth PSD plot but leads to large bias. The default is -1, which indicates that the window length equals the length of the input time series. overlap (%) — overlap specifies the overlap, in percentage, of the moving window that this VI applies to the time series. This parameter determines how much data this VI reuses for the signal space matrix. A large overlap reduces the variance of the resulting power spectrum but increases computation time. The default is 50, which specifies that the overlap is half of the window length. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. dB on? (T) — dB on? specifies whether this VI returns the PSD in decibels or in a linear scale. If dB on? is TRUE, this VI returns the PSD in decibels. If dB on? is FALSE, this VI returns the PSD in a linear scale. The default is TRUE. subspace settings — subspace settings specifies options for the MUSIC method. noise subspace (%) — noise subspace specifies the percentage of the noise subspace in the whole space, which is the combination of the signal subspace and the noise subspace. The default is -1, which means this VI calculates an appropriate value for the noise subspace. weighting — weighting specifies the weighting method for spectrum estimation. PSD — PSD returns information about the single-sided power spectral density (PSD). f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. unit — unit returns the engineering unit of the PSD. You can specify an engineering unit for a time series by using the TSA Scale to EU VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| window — window specifies the time-domain window applied to the time series. Options include None (default), Hanning, Hamming, Blackman-Harris, Exact Blackman, Blackman, Flat Top, 4 Term B-Harris, 7 Term B-Harris, and Low Sidelobe. length — length specifies the length of the window. A large window generates a power spectral density (PSD) with small bias but results in a coarse PSD plot. A small window generates a smooth PSD plot but leads to large bias. The default is -1, which indicates that the window length equals the length of the input time series. overlap (%) — overlap specifies the overlap, in percentage, of the moving window that this VI applies to the time series. This parameter determines how much data this VI reuses for the signal space matrix. A large overlap reduces the variance of the resulting power spectrum but increases computation time. The default is 50, which specifies that the overlap is half of the window length. |
| noise subspace (%) — noise subspace specifies the percentage of the noise subspace in the whole space, which is the combination of the signal subspace and the noise subspace. The default is -1, which means this VI calculates an appropriate value for the noise subspace. weighting — weighting specifies the weighting method for spectrum estimation. |
| f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. |

Parent topic:

TSA MUSIC VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-vi.html language=enus -->
## TOPIC 00038: TSA Time-Cepstrum VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided time-cepstrum of a univariate time series by using a sliding window. You can use the resulting time-cepstrum to detect time-varying periodic components of a time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

### TSA Time-Cepstrum VI

Computes the single-sided time-cepstrum of a univariate time series by using a sliding window. You can use the resulting time-cepstrum to detect time-varying periodic components of a time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-time-cepstrum-vi.png']

#### Examples

Refer to the Bearing Time-Cepstrum Analysis VI in the labview\examples\Time Series Analysis\TSAApplications directory for an example of using the TSA Time-Cepstrum VI.

- [TSA Time-Cepstrum (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-waveform-vi.html) Computes the single-sided time-cepstrum of a univariate time series by using a sliding window. You can use the resulting time-cepstrum to detect time-varying periodic components of a time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Time-Cepstrum (Array) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-array-vi.html) Computes the single-sided time-cepstrum of a univariate time series by using a sliding window. You can use the resulting time-cepstrum to detect time-varying periodic components of a time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Correlation and Spectral Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-waveform-vi.html language=enus -->
## TOPIC 00039: TSA Time-Cepstrum (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-time-cepstrum-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided time-cepstrum of a univariate time series by using a sliding window. You can use the resulting time-cepstrum to detect time-varying periodic components of a time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

### TSA Time-Cepstrum (Waveform) VI

Computes the single-sided time-cepstrum of a univariate time series by using a sliding window. You can use the resulting time-cepstrum to detect time-varying periodic components of a time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-time-cepstrum-waveform-vi.png']

#### Inputs/Outputs

| method — method specifies whether this VI uses the FFT-based or the autoregressive (AR) model-based method to compute the real cepstrum. The default is FFT. quefrency offset — quefrency offset specifies the offset, in seconds, of the quefrency. This VI returns the real cepstrum at a certain time whose quefrency is larger than the offset value. The default is 0. Xt — Xt specifies the univariate time series. time-quefrency sampling info — time-quefrency sampling info specifies information about the density and the size of the time-cepstrum. time steps — time steps specifies the sampling period, in number of samples, along the time axis in the joint time-quefrency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in the cepstrogram. quefrency bins — quefrency bins specifies the number of bins along the quefrency axis of the cepstrogram to sample the time series in the joint time-quefrency domain. quefrency bins must be greater than 0. The scale info output contains the actual sampling period, in seconds, along the quefrency axis of the cepstrogram. The default is 512. window info — window info specifies the information about the sliding window that divides the time series Xt into subsequences. type — type specifies the time-domain window that this VI applies to the time series. length — length specifies the length of the window in samples. The default is -1, which indicates that the window length equals the length of the input time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. AR setting — AR setting specifies the settings for the autoregressive (AR) model. This option is valid only when the method is AR Model. AR method — AR method specifies the method this VI uses to estimate the autoregressive (AR) model. AR order — AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. cepstrogram — cepstrogram returns the time-quefrency representation of the time series Xt. Each row corresponds to the real cepstrum at a certain time. The number of rows in cepstrogram equals the signal length divided by time steps. scale info — scale info returns the time scale and quefrency scale information of the time-quefrency representation, including the time offset, the time interval between every two contiguous rows, the quefrency offset, and the quefrency interval between every two contiguous columns of the cepstrogram. overlap — overlap returns the overlap, in percentage, of the sliding window this VI applies to the time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time steps — time steps specifies the sampling period, in number of samples, along the time axis in the joint time-quefrency domain. The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 rows exist in the cepstrogram. quefrency bins — quefrency bins specifies the number of bins along the quefrency axis of the cepstrogram to sample the time series in the joint time-quefrency domain. quefrency bins must be greater than 0. The scale info output contains the actual sampling period, in seconds, along the quefrency axis of the cepstrogram. The default is 512. |
| type — type specifies the time-domain window that this VI applies to the time series. length — length specifies the length of the window in samples. The default is -1, which indicates that the window length equals the length of the input time series. |
| AR method — AR method specifies the method this VI uses to estimate the autoregressive (AR) model. AR order — AR order specifies the order of the autoregressive (AR) model. The value of AR order must be greater than 0. The default is 4. |

#### Examples

Refer to the Bearing Time-Cepstrum Analysis VI in the labview\examples\Time Series Analysis\TSAApplications directory for an example of using the TSA Time-Cepstrum VI.

Parent topic:

TSA Time-Cepstrum VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-vector-music-array-vi.html language=enus -->
## TOPIC 00040: TSA Vector MUSIC (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-vector-music-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-vector-music-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided power spectral density (PSD) of a univariate or multivariate (vector) time series using the multiple signal classification (MUSIC) method. The MUSIC method performs a comprehensive and accurate spectral analysis on multivariate time series. Wire data to the Xt input to dete

### TSA Vector MUSIC (Array) VI

Computes the single-sided power spectral density (PSD) of a univariate or multivariate (vector) time series using the multiple signal classification (MUSIC) method. The MUSIC method performs a comprehensive and accurate spectral analysis on multivariate time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-music-array-vi.png']

#### Inputs/Outputs

| sampling rate — sampling rate specifies the sampling rate, in hertz, of the univariate time series Xt. The default is 1. frequency bins — frequency bins specifies the number of frequency bins for which this VI computes the single-sided power spectral density PSD. The length of the single-sided PSD is (frequency bins/2+1). The default is 1024. Xt — Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. window — window specifies the time-domain window applied on the time series in frequency computation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. dB on? (T) — dB on? specifies whether this VI returns the PSD in decibels or in a linear scale. If dB on? is TRUE, this VI returns the PSD in decibels. If dB on? is FALSE, this VI returns the PSD in a linear scale. The default is TRUE. subspace settings — subspace settings specifies options for the MUSIC method. noise subspace (%) — noise subspace specifies the percentage of the noise subspace in the whole space, which is the combination of the signal subspace and the noise subspace. The default is -1, which means this VI calculates an appropriate value for the noise subspace. weighting — weighting specifies the weighting method for spectrum estimation. PSD — PSD returns information about the single-sided power spectral density (PSD). f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| noise subspace (%) — noise subspace specifies the percentage of the noise subspace in the whole space, which is the combination of the signal subspace and the noise subspace. The default is -1, which means this VI calculates an appropriate value for the noise subspace. weighting — weighting specifies the weighting method for spectrum estimation. |
| f0 — f0 returns the lower boundary, in hertz, of the frequency range. df — df returns the frequency increment, in hertz. S(f) — S(f) returns the magnitude of the PSD at each frequency. The value of dB on? determines the unit of measurement for this parameter. |

Parent topic:

TSA MUSIC VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-welch-vi.html language=enus -->
## TOPIC 00041: TSA Welch VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-welch-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-welch-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided power spectral density (PSD) of a univariate time series using the Welch method, which is a variation of the periodogram method. This VI estimates the PSD by averaging periodograms of overlapping, windowed subsequences of the time series. Wire data to the Xt input to determ

### TSA Welch VI

Computes the single-sided power spectral density (PSD) of a univariate time series using the Welch method, which is a variation of the periodogram method. This VI estimates the PSD by averaging periodograms of overlapping, windowed subsequences of the time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-welch-vi.png']

#### TSA Welch Details

This VI estimates the PSD of a time series with the Welch method according to the following steps:

1. Divides the time series into subsequences. The size of each subsequence equals the value of the length parameter.
2. Applies a window to each subsequence and computes the PSD of each subsequence with the periodogram method.
3. Averages the PSDs of the subsequences to form the resulting PSD s(f) .

The PSD generated with the Welch method has smaller variance and is smoother than the PSD generated with the periodogram method.

#### Examples

Refer to the Power Spectral Density Estimation VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Welch VI.

- [TSA Welch (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-welch-waveform-vi.html) Computes the single-sided power spectral density (PSD) of a univariate time series using the Welch method, which is a variation of the periodogram method. This VI estimates the PSD by averaging periodograms of overlapping, windowed subsequences of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Welch (Array) VI](../../../../vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-llb/tsa-welch-array-vi.html) Computes the single-sided power spectral density (PSD) of a univariate time series using the Welch method, which is a variation of the periodogram method. This VI estimates the PSD by averaging periodograms of overlapping, windowed subsequences of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Correlation and Spectral Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-subs-llb/tsa-set-time-and-quefrency-scale-info-vi.html language=enus -->
## TOPIC 00042: TSA Set Time and Quefrency Scale Info VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-subs-llb/tsa-set-time-and-quefrency-scale-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/correlation-and-spectral-analysis-subs-llb/tsa-set-time-and-quefrency-scale-info-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time scale information and the quefrency scale information for the time-quefrency representation. icon Inputs/Outputs cnclst.png time info time info specifies the time scale information. cdbl.png time offset time offset specifies the offset of the time scale in seconds. cdbl.png time multip

### TSA Set Time and Quefrency Scale Info VI

Sets the time scale information and the quefrency scale information for the time-quefrency representation.

[IMAGE alt='icon' src='tsa-set-time-and-quefrency-scale-info-vi.png']

#### Inputs/Outputs

| time info — time info specifies the time scale information. time offset — time offset specifies the offset of the time scale in seconds. time multiplier — time multiplier specifies the multiplier of the time scale in seconds, for example, the time interval of the time-frequency representation. quefrency info — quefrency info specifies the quefrency scale information. quefrency offset — quefrency offset specifies the offset of the quefrency scale in seconds. quefrency multiplier — quefrency multiplier specifies the multiplier of the quefrency scale in seconds, for example, the quefrency interval of the time-quefrency representation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. scale info — scale info returns the time scale information and the quefrency scale information of the time-quefrency representation. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| time offset — time offset specifies the offset of the time scale in seconds. time multiplier — time multiplier specifies the multiplier of the time scale in seconds, for example, the time interval of the time-frequency representation. |
| quefrency offset — quefrency offset specifies the offset of the quefrency scale in seconds. quefrency multiplier — quefrency multiplier specifies the multiplier of the quefrency scale in seconds, for example, the quefrency interval of the time-quefrency representation. |

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/express/timeseriesbispectrumsource-llb/timeseriesbispectrum-source-vi.html language=enus -->
## TOPIC 00043: Time Series Bispectrum

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/express/timeseriesbispectrumsource-llb/timeseriesbispectrum-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/express/timeseriesbispectrumsource-llb/timeseriesbispectrum-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided bispectrum of a univariate time series. icon Dialog Box Options Inputs/Outputs cmsdt.png Xt Specifies the time series. Xt is available only when you select From terminal in Data Source. cerrcodeclst.png error in (no error) Describes error conditions that occur before this n

### Time Series Bispectrum

Computes the single-sided bispectrum of a univariate time series.

[IMAGE alt='icon' src='timeseriesbispectrum-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| Xt — Specifies the time series. Xt is available only when you select From terminal in Data Source. error in (no error) — Describes error conditions that occur before this node runs. File path — Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. error out — Contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. freq bins — Returns the frequency bins at which this VI estimates the bispectrum. averaging done? — Returns whether the averaging process is complete. averaging done? returns TRUE when the number of averages this VI completes is greater than or equal to the Number of averages. Otherwise, averaging done? returns FALSE. averaging done? is always TRUE if the Averaging mode is No Averaging. unit — Returns the selected engineering unit of the estimated power spectral density. Sxxx — Returns the magnitude of the single-sided bispectrum, S(f1, f2). |
| --- |

Parent topic:

Correlation and Spectral Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/express/timeseriescepstrumsource-llb/timeseriescepstrum-source-vi.html language=enus -->
## TOPIC 00044: Time Series Cepstrum

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/express/timeseriescepstrumsource-llb/timeseriescepstrum-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/express/timeseriescepstrumsource-llb/timeseriescepstrum-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-sided real cepstrum of a univariate time series. icon Dialog Box Options Inputs/Outputs cmsdt.png Xt Specifies the time series. Xt is available only when you select From terminal in Data Source. cpath.png File path Specifies the file path of the data you want to load. This input

### Time Series Cepstrum

Computes the single-sided real cepstrum of a univariate time series.

[IMAGE alt='icon' src='timeseriescepstrum-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| Xt — Specifies the time series. Xt is available only when you select From terminal in Data Source. File path — Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. error in (no error) — Describes error conditions that occur before this node runs. cepstrum — Returns information about the single-sided real cepstrum, such as the time range and time increment. t0 — f0 is the lower boundary of the frequency range. dt — df is the frequency increment. Cx — magnitude is the estimated power spectrum in normalized dB scale. The size of magnitude is equal to num of power spectrum bins. unit — Returns the selected engineering unit of the estimated power spectral density. error out — Contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. |
| --- |
| t0 — f0 is the lower boundary of the frequency range. dt — df is the frequency increment. Cx — magnitude is the estimated power spectrum in normalized dB scale. The size of magnitude is equal to num of power spectrum bins. |

Parent topic:

Correlation and Spectral Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/express/timeseriespreprocessingsource-llb/timeseriespreprocessing-source-vi.html language=enus -->
## TOPIC 00045: Time Series Preprocessing

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/express/timeseriespreprocessingsource-llb/timeseriespreprocessing-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/express/timeseriespreprocessingsource-llb/timeseriespreprocessing-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Preprocesses univariate or multivariate (vector) time series by moving average, resampling, detrending, or exponential average. icon Dialog Box Options Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standa

### Time Series Preprocessing

Preprocesses univariate or multivariate (vector) time series by moving average, resampling, detrending, or exponential average.

[IMAGE alt='icon' src='timeseriespreprocessing-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Xt — Specifies the time series. Xt is available only when you select From terminal in Data Source. File path — Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. Trend — Returns the trend of the input time series. This output is available only when you select Detrending from the Method list. Xt filtered — Returns the processed time series. This output returns the filtered time series. This output is available only when you select Moving Average from the Method list in the Time Series Preprocessing dialog box. error out — error out contains error information. This output provides standard error out functionality. Processed (multiple,WDT) — is the averaged multi-variable time series. Trend (multiple,WDT) — is the trend component in the input multi-variable time series. |
| --- |

Parent topic:

Preprocessing

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/express/tsarandomsequencegenerationsource-llb/tsarandomsequencegeneration-source-vi.html language=enus -->
## TOPIC 00046: Random Sequence Generation

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/express/tsarandomsequencegenerationsource-llb/tsarandomsequencegeneration-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/express/tsarandomsequencegenerationsource-llb/tsarandomsequencegeneration-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a random univariate time series from the normal, uniform, chi-square, t, or F distribution. This Express VI also can generate a random multivariate time series from the vector normal distribution. You can plot the histogram of the generated time series in the configuration dialog box. icon

### Random Sequence Generation

Generates a random univariate time series from the normal, uniform, chi-square, t, or F distribution. This Express VI also can generate a random multivariate time series from the vector normal distribution. You can plot the histogram of the generated time series in the configuration dialog box.

[IMAGE alt='icon' src='tsarandomsequencegeneration-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| error in (no error) — Describes error conditions that occur before this node runs. error out — Contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Xt — Returns the generated random sequence. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-exponential-prediction-waveform-vi.html language=enus -->
## TOPIC 00047: TSA Exponential Prediction (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-exponential-prediction-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-exponential-prediction-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Predicts the values of a univariate time series based on exponential smoothing. icon Inputs/Outputs ci32.png number of points number of points specifies the length of the predicted time series. The default is 1. cmsdt.png Xt Xt specifies the univariate time series. cu16.png exponential type exponent

### TSA Exponential Prediction (Waveform) VI

Predicts the values of a univariate time series based on exponential smoothing.

[IMAGE alt='icon' src='tsa-exponential-prediction-waveform-vi.png']

#### Inputs/Outputs

| number of points — number of points specifies the length of the predicted time series. The default is 1. Xt — Xt specifies the univariate time series. exponential type — exponential type specifies the type of exponential smoothing scheme to use in the prediction. exponential factors — exponential factors specifies the weighting factors for exponential smoothing. level — level specifies the weight for the level cumulant. The value of value must be a number between 0 and 1. trend — trend specifies the weight for the trend cumulant. The value of trend must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season — season specifies the weight for the seasonal cumulant. The value of season must be a number between 0 and 1. This option is available only when exponential type is Triple. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. season period — season period specifies the length of the seasonal pattern in the input time series. The default is 1. This option is available only when exponential type is Triple. season type — season type specifies the way in which this VI models the seasonality. This option is available only when exponential type is Triple. predicted series — predicted series returns the predicted univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| level — level specifies the weight for the level cumulant. The value of value must be a number between 0 and 1. trend — trend specifies the weight for the trend cumulant. The value of trend must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season — season specifies the weight for the seasonal cumulant. The value of season must be a number between 0 and 1. This option is available only when exponential type is Triple. |

#### TSA Exponential Prediction Details

This VI computes the future values of a time series based on one of the following exponential smoothing schemes: single, double, and triple (Holt-Winters). You can specify the type of exponential smoothing scheme using the **exponential type** parameter. Each exponential smoothing scheme has a corresponding forecasting formula that uses the computed level cumulant, trend cumulant, and season cumulant vector.

#### Examples

Refer to the Exponential Prediction VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Exponential Prediction VI.

Parent topic:

TSA Exponential Prediction VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-ma-modeling-array-vi.html language=enus -->
## TOPIC 00048: TSA MA Modeling (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-ma-modeling-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-ma-modeling-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Estimates the moving average (MA) model of a univariate time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c1ddbl.png Xt Xt specifies the univariate time series. cu16.png method method specifies the method to use i

### TSA MA Modeling (Array) VI

Estimates the moving average (MA) model of a univariate time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-ma-modeling-array-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. method — method specifies the method to use in estimating the moving average model. MA order — MA order specifies the order of the moving average model. The value of MA order must be greater than 0. The default is 4. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MA coefficients — MA coefficients returns the estimated coefficients of the moving average model. noise — noise returns the estimated white noise series of the moving average model. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA MA Modeling Details

This VI estimates the MA model according to the following equation:

X<sub>t</sub> = e<sub>t</sub> + b<sub>1</sub>e<sub>t-1</sub> + ,…, + b<sub>N</sub>e<sub>t-N</sub>

where N is the MA order, X<sub>t</sub> is a univariate time series, and e<sub>t</sub> is a Gaussian white noise series. **MA coefficients** is a 1D array of [1, b1, b2,…, b<sub>N</sub>], where each coefficient b<sub>i</sub> is a real number.

The minimum length requirement for the input time series differs for each method you use:

- Yule-Walker method: minimum length >= MA order
- High-Order AR method: minimum length >= 5 x MA order
- Polynomial method: minimum length >= 5 x MA order

Parent topic:

TSA MA Modeling VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-modal-parametric-modeling-waveform-vi.html language=enus -->
## TOPIC 00049: TSA Modal Parametric Modeling (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-modal-parametric-modeling-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-modal-parametric-modeling-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Estimates the modal parametric model of a univariate or multivariate (vector) time series. The modal parameters include magnitude, phase, damping factor, and natural frequency. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs

### TSA Modal Parametric Modeling (Waveform) VI

Estimates the modal parametric model of a univariate or multivariate (vector) time series. The modal parameters include magnitude, phase, damping factor, and natural frequency. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-modal-parametric-modeling-waveform-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. method — method specifies the method to use in estimating the frequency component of the time series. model order — model order specifies the model order. The value of model order must be at least twice the number of frequency components you want to estimate. The default is 4. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. noise subspace (%) — noise subspace specifies the percentage of frequency components due to noise in the time series. The default is 50. This option is available only when method is Matrix Pencil. frequency components — frequency components returns information about the estimated frequency components. frequency — frequency returns the estimated frequency of the frequency component. damping factor — damping factor returns the estimated damping factor of the frequency component. magnitude — magnitude returns the estimated magnitude of the frequency component. phase — phase returns the estimated phase of the frequency component. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| frequency — frequency returns the estimated frequency of the frequency component. damping factor — damping factor returns the estimated damping factor of the frequency component. magnitude — magnitude returns the estimated magnitude of the frequency component. phase — phase returns the estimated phase of the frequency component. |

#### TSA Modal Parametric Modeling Details

For a univariate impulse response time series, this VI estimates the modal parametric model according to the following equation:

[IMAGE alt='image' src='tsa_equ_modal1.gif']

where h<sub>t</sub> is the univariate impulse response series, and n is the model order.

a<sub>i</sub> denotes one of the complex amplitudes, which is defined as:

a<sub>i</sub> = r<sub>i</sub>e<sup>jq</sup>

where r is **magnitude**, and q is **phase**.

S<sub>i</sub> is one of the modal poles, which is defined as:

S<sub>i</sub> = a + j2pf

where a is **damping factor**, and f is **frequency**.

For a multivariate impulse response time series, this VI estimates the modal parametric model according to the following equation:

[IMAGE alt='image' src='tsa_equ_modal4.gif']

where H<sub>t</sub> is the multivariate impulse response series. H<sub>t</sub> is a k×1 vector with k variables that come from k sources. A<sub>i</sub> is a k×1 complex amplitude vector with k variables. A<sub>i</sub><sup>T</sup>=(a<sub>1i</sub>,…,a<sub>ki</sub>). S<sub>i</sub> is one of the modal poles. n is the model order.

Refer to the univariate modal parametric model for the descriptions of a<sub>ki</sub> in the vector A<sub>i</sub>.

#### Examples

Refer to the following VIs for examples of using the TSA Modal Parametric Modeling VI:

- Modal Analysis of a Plate VI: labview\examples\Time Series Analysis\TSAApplications
- Frequency Components VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Modal Parametric Modeling VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-vector-arma-modeling-array-vi.html language=enus -->
## TOPIC 00050: TSA Vector ARMA Modeling (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-vector-arma-modeling-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-vector-arma-modeling-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Estimates the autoregressive-moving average (ARMA) model of a univariate or multivariate (vector) time series according to the method you specify. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c2ddbl.png Xt Xt specifies th

### TSA Vector ARMA Modeling (Array) VI

Estimates the autoregressive-moving average (ARMA) model of a univariate or multivariate (vector) time series according to the method you specify. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-arma-modeling-array-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. ARMA order — ARMA order specifies the orders of the autoregressive-moving average model. AR — AR specifies the AR order of the autoregressive-moving average model. The value of AR must be equal to or greater than 0. The value of AR cannot be zero if the value of MA is zero. The default is 4. MA — MA specifies the MA order of the autoregressive-moving average model. The value of MA must be equal to or greater than 0. The value of MA cannot be zero if the value of AR is zero. The default is 3. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. AR coefficients — AR coefficients returns the estimated AR coefficients of the vector autoregressive-moving average model. — is the estimated AR coefficients of the vector ARMA model. MA coefficients — MA coefficients returns the estimated MA coefficients of the vector autoregressive-moving average model. — is the estimated MA coefficients of the vector ARMA model. noise — noise returns the estimated multivariate white noise series of the vector autoregressive-moving average model. Each column of the 2D array is a vector at certain time. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| AR — AR specifies the AR order of the autoregressive-moving average model. The value of AR must be equal to or greater than 0. The value of AR cannot be zero if the value of MA is zero. The default is 4. MA — MA specifies the MA order of the autoregressive-moving average model. The value of MA must be equal to or greater than 0. The value of MA cannot be zero if the value of AR is zero. The default is 3. |
| — is the estimated AR coefficients of the vector ARMA model. |
| — is the estimated MA coefficients of the vector ARMA model. |

#### TSA ARMA Modeling Details

This VI estimates the autoregressive (AR) model according to the following equation:

X<sub>t</sub> + a<sub>1</sub>X<sub>t-1</sub> + ,…, + a<sub>N<sub>a</sub></sub>X<sub>t-N<sub>a</sub></sub> = e<sub>t</sub> + b<sub>1</sub>e<sub>t-1</sub> + ,…, + b<sub>N<sub>b</sub></sub>e<sub>t-N<sub>b</sub></sub>

where N<sub>a</sub> is the AR order, N<sub>b</sub> is the MA order, X<sub>t</sub> is a univariate or multivariate (vector) time series, and e<sub>t</sub> is a Gaussian white noise series with a mean of zero.

For univariate time series, **AR coefficients** is a 1D array [1, a<sub>1</sub>, a<sub>2</sub>,…, a<sub>N<sub>a</sub></sub>], where each coefficient a<sub>i</sub> is a real number. **MA coefficients** is a 1D array [1, b<sub>1</sub>, b<sub>2</sub>,…, b<sub>N<sub>b</sub></sub>], where each coefficient b<sub>i</sub> also is a real number.

For multivariate time series, **AR coefficients** is a 1D array [I, a<sub>1</sub>, a<sub>2</sub>,…, a<sub>N<sub>a</sub></sub>], where each coefficient a<sub>i</sub> is a 2D array cluster. **MA coefficients** is a 1D array [I, b<sub>1</sub>, b<sub>2</sub>,…, b<sub>N<sub>b</sub></sub>], where each coefficient b<sub>i</sub> also is a 2D array cluster.

The minimum length requirement for the input time series differs for each method you use:

- Yule-Walker method: minimum length >= AR order + MA order
- High-Order AR method: minimum length >= 5 x MA order
- Polynomial method: minimum length >= 5 x ( AR order + MA order)

#### Examples

Refer to the following VIs for examples of using the TSA ARMA Modeling VI:

- Engine Knocking Monitor VI: labview\examples\Time Series Analysis\TSAApplications
- ARMA Prediction VI: labview\examples\Time Series Analysis\TSAGettingStarted
- ARMA Model Estimation VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA ARMA Modeling VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-vector-arma-modeling-waveform-vi.html language=enus -->
## TOPIC 00051: TSA Vector ARMA Modeling (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-vector-arma-modeling-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/modeling-and-prediction-llb/tsa-vector-arma-modeling-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Estimates the autoregressive-moving average (ARMA) model of a univariate or multivariate (vector) time series according to the method you specify. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c1dmsdt.png Xt Xt specifies t

### TSA Vector ARMA Modeling (Waveform) VI

Estimates the autoregressive-moving average (ARMA) model of a univariate or multivariate (vector) time series according to the method you specify. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-arma-modeling-waveform-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the multivariate (vector) time series. ARMA order — ARMA order specifies the orders of the autoregressive-moving average model. AR — AR specifies the AR order of the autoregressive-moving average model. The value of AR must be equal to or greater than 0. The value of AR cannot be zero if the value of MA is zero. The default is 4. MA — MA specifies the MA order of the autoregressive-moving average model. The value of MA must be equal to or greater than 0. The value of MA cannot be zero if the value of AR is zero. The default is 3. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. AR coefficients — AR coefficients returns the estimated AR coefficients of the vector autoregressive-moving average model. — is the estimated AR coefficients of the vector ARMA model. MA coefficients — MA coefficients returns the estimated MA coefficients of the vector autoregressive-moving average model. — is the estimated MA coefficients of the vector ARMA model. noise — noise returns the estimated multivariate white noise series of the vector autoregressive-moving average model. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| AR — AR specifies the AR order of the autoregressive-moving average model. The value of AR must be equal to or greater than 0. The value of AR cannot be zero if the value of MA is zero. The default is 4. MA — MA specifies the MA order of the autoregressive-moving average model. The value of MA must be equal to or greater than 0. The value of MA cannot be zero if the value of AR is zero. The default is 3. |
| — is the estimated AR coefficients of the vector ARMA model. |
| — is the estimated MA coefficients of the vector ARMA model. |

#### TSA ARMA Modeling Details

This VI estimates the autoregressive (AR) model according to the following equation:

X<sub>t</sub> + a<sub>1</sub>X<sub>t-1</sub> + ,…, + a<sub>N<sub>a</sub></sub>X<sub>t-N<sub>a</sub></sub> = e<sub>t</sub> + b<sub>1</sub>e<sub>t-1</sub> + ,…, + b<sub>N<sub>b</sub></sub>e<sub>t-N<sub>b</sub></sub>

where N<sub>a</sub> is the AR order, N<sub>b</sub> is the MA order, X<sub>t</sub> is a univariate or multivariate (vector) time series, and e<sub>t</sub> is a Gaussian white noise series with a mean of zero.

For univariate time series, **AR coefficients** is a 1D array [1, a<sub>1</sub>, a<sub>2</sub>,…, a<sub>N<sub>a</sub></sub>], where each coefficient a<sub>i</sub> is a real number. **MA coefficients** is a 1D array [1, b<sub>1</sub>, b<sub>2</sub>,…, b<sub>N<sub>b</sub></sub>], where each coefficient b<sub>i</sub> also is a real number.

For multivariate time series, **AR coefficients** is a 1D array [I, a<sub>1</sub>, a<sub>2</sub>,…, a<sub>N<sub>a</sub></sub>], where each coefficient a<sub>i</sub> is a 2D array cluster. **MA coefficients** is a 1D array [I, b<sub>1</sub>, b<sub>2</sub>,…, b<sub>N<sub>b</sub></sub>], where each coefficient b<sub>i</sub> also is a 2D array cluster.

The minimum length requirement for the input time series differs for each method you use:

- Yule-Walker method: minimum length >= AR order + MA order
- High-Order AR method: minimum length >= 5 x MA order
- Polynomial method: minimum length >= 5 x ( AR order + MA order)

#### Examples

Refer to the following VIs for examples of using the TSA ARMA Modeling VI:

- Engine Knocking Monitor VI: labview\examples\Time Series Analysis\TSAApplications
- ARMA Prediction VI: labview\examples\Time Series Analysis\TSAGettingStarted
- ARMA Model Estimation VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA ARMA Modeling VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-array-vi.html language=enus -->
## TOPIC 00052: TSA Detrend (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ci32.png polynomial order polynomial order spe

### TSA Detrend (Array) VI

Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-detrend-array-vi.png']

#### Inputs/Outputs

| polynomial order — polynomial order specifies the polynomial order to use in the N-polynomial fit. This option is available only when method is N-polynomial. The value must be greater than or equal to 0. The default is 2. Xt — Xt specifies the univariate time series. method — method specifies the curve-fitting method to use in estimating the trend of Xt. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Xt detrended — Xt detrended returns the detrended univariate time series. trend — trend returns the trend component of the univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the Trend Estimation (Curve Fitting) VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Detrend VI.

Parent topic:

TSA Detrend VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-vi.html language=enus -->
## TOPIC 00053: TSA Detrend VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Examples Refer to the Trend Estimation (Curve Fitting) VI in

### TSA Detrend VI

Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-detrend-vi.png']

#### Examples

Refer to the Trend Estimation (Curve Fitting) VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Detrend VI.

- [TSA Detrend (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-waveform-vi.html) Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Detrend (Array) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-array-vi.html) Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Detrend (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-vector-detrend-waveform-vi.html) Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Detrend (Array) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-vector-detrend-array-vi.html) Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Preprocessing

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-waveform-vi.html language=enus -->
## TOPIC 00054: TSA Detrend (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-detrend-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ci32.png polynomial order polynomial order spe

### TSA Detrend (Waveform) VI

Removes the trend from a univariate or multivariate (vector) time series. This VI estimates the trend with curve-fitting methods. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-detrend-waveform-vi.png']

#### Inputs/Outputs

| polynomial order — polynomial order specifies the polynomial order to use in the N-polynomial fit. This option is available only when method is N-polynomial. The value must be greater than or equal to 0. The default is 2. Xt — Xt specifies the univariate time series. method — method specifies the curve-fitting method to use in estimating the trend of Xt. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Xt detrended — Xt detrended returns the detrended univariate time series. trend — trend returns the trend component of the univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the Trend Estimation (Curve Fitting) VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Detrend VI.

Parent topic:

TSA Detrend VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-array-vi.html language=enus -->
## TOPIC 00055: TSA Exponential Average (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c1ddbl.png Xt Xt specifies the univariate time series

### TSA Exponential Average (Array) VI

Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-exponential-average-array-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. exponential type — exponential type specifies the type of exponential average. Options include Single, Double, and Triple. The default is Single. exponential factors — exponential factors specifies the weighting factors for exponential smoothing. level — level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend — trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season — season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. season period — season period specifies the length of the seasonal pattern in the input time series. The default is 1. This option is available only when exponential type is Triple. season type — season type specifies the way in which this VI models the seasonality. This option is available only when exponential type is Triple. Xt averaged — Xt averaged returns the averaged univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| level — level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend — trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season — season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |

#### TSA Exponential Average Details

This VI uses the exponential weighting scheme to produce a smoothed time series. This VI computes the averaged values by assigning exponentially decreasing weights to the old values in the original time series according to the following equation:

X<sub>a</sub>(i) = aX<sub>t</sub>(i-1) + a(1-a)X<sub>t</sub>(i-2) + a(1-a)²X<sub>t</sub>(i-3) +…

where a is the **level** weight for level cumulant X<sub>a</sub>, X<sub>a</sub> is the averaged time series, and X<sub>t</sub> is the original time series.

#### Examples

Refer to the Exponential Smoothing VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Exponential Average VI.

Parent topic:

TSA Exponential Average VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-vi.html language=enus -->
## TOPIC 00056: TSA Exponential Average VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon TSA Exponential Average Details This VI uses the exponential weighti

### TSA Exponential Average VI

Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-exponential-average-vi.png']

#### TSA Exponential Average Details

This VI uses the exponential weighting scheme to produce a smoothed time series. This VI computes the averaged values by assigning exponentially decreasing weights to the old values in the original time series according to the following equation:

X<sub>a</sub>(i) = aX<sub>t</sub>(i-1) + a(1-a)X<sub>t</sub>(i-2) + a(1-a)²X<sub>t</sub>(i-3) +…

where a is the **level** weight for level cumulant X<sub>a</sub>, X<sub>a</sub> is the averaged time series, and X<sub>t</sub> is the original time series.

#### Examples

Refer to the Exponential Smoothing VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Exponential Average VI.

- [TSA Exponential Average (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-waveform-vi.html) Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Exponential Average (Array) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-array-vi.html) Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Exponential Average (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-vector-exponential-average-waveform-vi.html) Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Exponential Average (Array) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-vector-exponential-average-array-vi.html) Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Preprocessing

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-waveform-vi.html language=enus -->
## TOPIC 00057: TSA Exponential Average (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-exponential-average-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cmsdt.png Xt Xt specifies the univariate time series.

### TSA Exponential Average (Waveform) VI

Performs exponential average on a univariate or multivariate (vector) time series. This VI returns a smoothed time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-exponential-average-waveform-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. exponential type — exponential type specifies the type of exponential average. Options include Single, Double, and Triple. The default is Single. exponential factors — exponential factors specifies the weighting factors for exponential smoothing. level — level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend — trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season — season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. season period — season period specifies the length of the seasonal pattern in the input time series. The default is 1. This option is available only when exponential type is Triple. season type — season type specifies the way in which this VI models the seasonality. This option is available only when exponential type is Triple. Xt averaged — Xt averaged returns the averaged univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| level — level specifies the weight for the level cumulant. The value must be a number between 0 and 1. trend — trend specifies the weight for the trend cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Double or Triple. season — season specifies the weight for seasonal cumulant. The value must be a number between 0 and 1. This option is available only when exponential type is Triple. |

#### TSA Exponential Average Details

This VI uses the exponential weighting scheme to produce a smoothed time series. This VI computes the averaged values by assigning exponentially decreasing weights to the old values in the original time series according to the following equation:

X<sub>a</sub>(i) = aX<sub>t</sub>(i-1) + a(1-a)X<sub>t</sub>(i-2) + a(1-a)²X<sub>t</sub>(i-3) +…

where a is the **level** weight for level cumulant X<sub>a</sub>, X<sub>a</sub> is the averaged time series, and X<sub>t</sub> is the original time series.

#### Examples

Refer to the Exponential Smoothing VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Exponential Average VI.

Parent topic:

TSA Exponential Average VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-array-vi.html language=enus -->
## TOPIC 00058: TSA Moving Average (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c1ddbl.png Xt Xt specifies

### TSA Moving Average (Array) VI

Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-moving-average-array-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. method — method specifies the filter type to use in filtering the input time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined weights — user defined weights specifies a set of weights for the moving average operation. If you specify a value for user defined weights, this VI ignores the setting for method. The number of weights must be odd, and the weight array must be symmetric so no phase distortion takes places in the moving average operation. Xt out — Xt out returns the filtered univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Moving Average Details

This VI estimates the trend of a time series by using a linear filtering operation according to the following equation:

[IMAGE alt='image' src='tsa_equ_movave1.gif']

where {a<sub>r</sub>} is a set of weights. In practice, [IMAGE alt='image' src='tsa_sumar.gif']. This operation is a moving average or finite impulse response (FIR) filter.

#### Examples

Refer to the Moving Average VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Moving Average VI.

Parent topic:

TSA Moving Average VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-vi.html language=enus -->
## TOPIC 00059: TSA Moving Average VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon TSA Moving Average Details This VI estimat

### TSA Moving Average VI

Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-moving-average-vi.png']

#### TSA Moving Average Details

This VI estimates the trend of a time series by using a linear filtering operation according to the following equation:

[IMAGE alt='image' src='tsa_equ_movave1.gif']

where {a<sub>r</sub>} is a set of weights. In practice, [IMAGE alt='image' src='tsa_sumar.gif']. This operation is a moving average or finite impulse response (FIR) filter.

#### Examples

Refer to the Moving Average VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Moving Average VI.

- [TSA Moving Average (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-waveform-vi.html) Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Moving Average (Array) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-array-vi.html) Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Moving Average (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-vector-moving-average-waveform-vi.html) Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Moving Average (Array) VI](../../../../vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-vector-moving-average-array-vi.html) Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Preprocessing

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-waveform-vi.html language=enus -->
## TOPIC 00060: TSA Moving Average (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-moving-average-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cmsdt.png Xt Xt specifies t

### TSA Moving Average (Waveform) VI

Performs moving average on a univariate or multivariate (vector) time series to smooth out fluctuations or to estimate the trend of the time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-moving-average-waveform-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. method — method specifies the filter type to use in filtering the input time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined weights — user defined weights specifies a set of weights for the moving average operation. If you specify a value for user defined weights, this VI ignores the setting for method. The number of weights must be odd, and the weight array must be symmetric so no phase distortion takes places in the moving average operation. Xt out — Xt out returns the filtered univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Moving Average Details

This VI estimates the trend of a time series by using a linear filtering operation according to the following equation:

[IMAGE alt='image' src='tsa_equ_movave1.gif']

where {a<sub>r</sub>} is a set of weights. In practice, [IMAGE alt='image' src='tsa_sumar.gif']. This operation is a moving average or finite impulse response (FIR) filter.

#### Examples

Refer to the Moving Average VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Moving Average VI.

Parent topic:

TSA Moving Average VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-resampling-equal-vi.html language=enus -->
## TOPIC 00061: TSA Resampling (Equal) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-resampling-equal-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/series-preprocess-llb/tsa-resampling-equal-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resamples the equally- or unequally-sampled time series into a new time series with a specified time interval using the interpolation method. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdbl.png original sampling rate or

### TSA Resampling (Equal) VI

Resamples the equally- or unequally-sampled time series into a new time series with a specified time interval using the interpolation method. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-resampling-equal-vi.png']

#### Inputs/Outputs

| original sampling rate — original sampling rate specifies the original sampling rate of the equally-sampled time series Xt. Xt — Xt specifies the univariate time series. new sampling rate — new sampling rate specifies the sampling rate for the resampled time series. The value must be greater than 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Xt resampled — Xt resampled returns the resampled univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following VIs for examples of using the TSA Resampling VI:

- Resample Time Series VI: labview\examples\Time Series Analysis\TSAGettingStarted
- Resample Unequally-Sampled Time Series VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Resampling VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-vi.html language=enus -->
## TOPIC 00062: TSA Confidence Limits VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon TSA Confidence Limits Details Examples Refer to the Series Statist

### TSA Confidence Limits VI

Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-confidence-limits-vi.png']

#### TSA Confidence Limits Details

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Confidence Limits VI.

- [TSA Confidence Limits (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-waveform-vi.html) Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Confidence Limits (Array) VI](../../../../vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-array-vi.html) Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Confidence Limits (Waveform) VI](../../../../vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-confidence-limits-waveform-vi.html) Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.
- [TSA Vector Confidence Limits (Array) VI](../../../../vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-confidence-limits-array-vi.html) Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Statistical Analysis

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-waveform-vi.html language=enus -->
## TOPIC 00063: TSA Confidence Limits (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-confidence-limits-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cmsdt.png Xt Xt specifies the univariate time serie

### TSA Confidence Limits (Waveform) VI

Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-confidence-limits-waveform-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the univariate time series. confidence level (%) — confidence level specifies the level of confidence, as a percentage, to use in computing the confidence limits of the mean and standard deviation values. The default is 95. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. mean limits — mean limits returns the confidence limits of the mean value at the specified confidence level. upper — upper returns the upper confidence limit of the mean value at the specified confidence level. lower — lower returns the lower confidence limit of the mean value at the specified confidence level. std deviation limits — std deviation limits returns the confidence limits of the standard deviation value at the specified confidence level. upper — upper returns the upper confidence limit of the standard deviation value at the specified confidence level. lower — lower returns the lower confidence limit of the standard deviation value at the specified confidence level. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| upper — upper returns the upper confidence limit of the mean value at the specified confidence level. lower — lower returns the lower confidence limit of the mean value at the specified confidence level. |
| upper — upper returns the upper confidence limit of the standard deviation value at the specified confidence level. lower — lower returns the lower confidence limit of the standard deviation value at the specified confidence level. |

#### TSA Confidence Limits Details

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Confidence Limits VI.

Parent topic:

TSA Confidence Limits VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-mean-waveform-vi.html language=enus -->
## TOPIC 00064: TSA Mean (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-mean-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-mean-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the mean values of a univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdbl.png trimmed percent (%) trimmed percent specifies a percentage at which to discard the lowes

### TSA Mean (Waveform) VI

Computes the mean values of a univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-mean-waveform-vi.png']

#### Inputs/Outputs

| trimmed percent (%) — trimmed percent specifies a percentage at which to discard the lowest and highest values in the time series. This option is available only when method is Trimmed. Xt — Xt specifies the univariate time series. method — method specifies the method to use in computing the mean value of the input time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. mean — mean returns the mean value of the input time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Mean Details

This VI calculates the mean values of an input time series with the method you specify for the **method** parameter.

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Mean VI.

Parent topic:

TSA Mean VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-stationarity-test-waveform-vi.html language=enus -->
## TOPIC 00065: TSA Stationarity Test (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-stationarity-test-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-stationarity-test-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Estimates the stationarity of a univariate time series by examining the mean and variance values of the subsequences. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ci32.png number of segments number of segments specifies t

### TSA Stationarity Test (Waveform) VI

Estimates the stationarity of a univariate time series by examining the mean and variance values of the subsequences. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-stationarity-test-waveform-vi.png']

#### Inputs/Outputs

| number of segments — number of segments specifies the number of subsequences into which this VI divides the input time series. The default is 100. Xt — Xt specifies the univariate time series. confidence level (%) — confidence level specifies the level of confidence as a percentage this VI uses to compute the confidence limits of specified statistics value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. stationary — stationary returns information about the stationarity of the univariate time series. mean? — mean? returns TRUE if the univariate time series is stationary based on the mean values of the subsequences. variance? — variance? returns TRUE if the univariate time series is stationary based on the variance values of the subsequences. mean of segments — mean of segments returns the mean value of each subsequence. variance of segments — variance of segments returns the variance value of each subsequence. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| mean? — mean? returns TRUE if the univariate time series is stationary based on the mean values of the subsequences. variance? — variance? returns TRUE if the univariate time series is stationary based on the variance values of the subsequences. |

#### TSA Stationarity Test Details

This VI performs stationarity estimation on a univariate time series by testing the inversion number according to the following steps:

1. Divides a time series X<sub>t</sub> into l subsequences. The mean value of each subsequence forms a time series m<sub>1</sub>, m<sub>2</sub>,…m<sub>l</sub>. The standard deviation value of each subsequence forms a time series s<sub>1</sub>, s<sub>2</sub>,…s<sub>l</sub>.

2. Computes the sum S<sub>m</sub> (S<sub>s</sub>) of inversion number for the time series m<sub>1</sub>, m<sub>2</sub>,…, m<sub>l</sub> (s<sub>1</sub>, s<sub>2</sub>,…, s<sub>l</sub>).

If X<sub>t</sub> is stationary, the statistical value e<sub>m</sub>e<sub>s</sub> satisfies the normal distribution with a mean value of 0 and a standard deviation value of 1.

[IMAGE alt='image' src='summju.gif']

and

[IMAGE alt='image' src='sumsigma.gif']

Where m<sub>A</sub> is the theoretical mean value of S<sub>m</sub> or S<sub>s</sub>, which equals [IMAGE alt='image' src='tsa_equ_stationary1.gif'], and s<sub>A</sub> is the theoretical standard deviation value of S<sub>m</sub> or S<sub>s</sub>, which equals the following equation:

[IMAGE alt='image' src='tsa_equ_stationary2.gif']

Given the confidence level a:

- If e m < N a/2 (0, 1), this time series is mean stationary.
- If e s < N a/2 (0, 1), this time series is variance stationary.

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Stationarity Test VI.

Parent topic:

TSA Stationarity Test VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-confidence-limits-array-vi.html language=enus -->
## TOPIC 00066: TSA Vector Confidence Limits (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-confidence-limits-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-confidence-limits-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c2ddbl.png Xt Xt specifies the multivariate (vector

### TSA Vector Confidence Limits (Array) VI

Computes confidence limits of the mean and standard deviation values of the univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-confidence-limits-array-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. confidence level (%) — confidence level specifies the level of confidence, as a percentage, to use in computing the confidence limits of the mean and standard deviation values. The default is 95. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. mean limits — mean limits returns the confidence limits of mean value at the specified confidence level. upper — upper returns the upper confidence limit of the mean value at the specified confidence level. lower — lower returns the lower confidence limit of the mean value at the specified confidence level. std deviation limits — std deviation limits returns the confidence limits of standard deviation value at the specified confidence level. upper — upper returns the upper confidence limit of the standard deviation value at the specified confidence level. lower — lower returns the lower confidence limit of the standard deviation value at the specified confidence level. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| upper — upper returns the upper confidence limit of the mean value at the specified confidence level. lower — lower returns the lower confidence limit of the mean value at the specified confidence level. |
| upper — upper returns the upper confidence limit of the standard deviation value at the specified confidence level. lower — lower returns the lower confidence limit of the standard deviation value at the specified confidence level. |

#### TSA Confidence Limits Details

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Confidence Limits VI.

Parent topic:

TSA Confidence Limits VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-deviation-and-variance-array-vi.html language=enus -->
## TOPIC 00067: TSA Vector Deviation and Variance (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-deviation-and-variance-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-deviation-and-variance-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the standard deviation, variance, and coefficients of variation values of a univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c2ddbl.png Xt Xt specifies the multivariat

### TSA Vector Deviation and Variance (Array) VI

Computes the standard deviation, variance, and coefficients of variation values of a univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-deviation-and-variance-array-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. weighting — weighting specifies which type of standard deviation and variance values to calculate. Options include Sample and Population. The default is Sample (N-1). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. standard deviation — standard deviation returns the vector standard deviation value of the multivariate (vector) time series. variance — variance returns the vector variance value of the multivariate (vector) time series. coefficients of variation (%) — coefficients of variation returns the vector coefficients of variation value of the multivariate (vector) time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Deviation and Variance Details

This VI calculates the standard deviation and variance values according to the following equations:

[IMAGE alt='image' src='tsa_equ_deviation1.gif']

[IMAGE alt='image' src='tsa_equ_deviation2.gif']

where m is the arithmetic mean, s² is **variance**, s is **standard deviation**, n is the number of time series X<sub>t</sub>. w = n when **weighting** is set to **Population** and w = (n-1) when **weighting** is set to **Sample**.

This VI calculates the coefficients of variation according to the following equation:

[IMAGE alt='image' src='tsa_equ_deviation3.gif']

#### Examples

Refer to the following VIs for examples of using the TSA Deviation and Variance VI:

- Engine Knocking Monitor VI: labview\examples\Time Series Analysis\TSAApplications
- Power Line Monitor VI: labview\examples\Time Series Analysis\TSAApplications
- ARMA Prediction VI: labview\examples\Time Series Analysis\TSAGettingStarted
- Series Statistical Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Deviation and Variance VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-mean-array-vi.html language=enus -->
## TOPIC 00068: TSA Vector Mean (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-mean-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-mean-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the mean values of a univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdbl.png trimmed percent (%) trimmed percent specifies a percentage at which to discard the lowes

### TSA Vector Mean (Array) VI

Computes the mean values of a univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-mean-array-vi.png']

#### Inputs/Outputs

| trimmed percent (%) — trimmed percent specifies a percentage at which to discard the lowest and highest values in the time series. This option is available only when method is Trimmed. Xt — Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. method — method specifies the method to use in computing the mean value of the input time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. vector mean — vector mean returns the vector mean values of the multivariate (vector) time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Mean Details

This VI calculates the mean values of an input time series with the method you specify for the **method** parameter.

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Mean VI.

Parent topic:

TSA Mean VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-mean-waveform-vi.html language=enus -->
## TOPIC 00069: TSA Vector Mean (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-mean-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-mean-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the mean values of a univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cdbl.png trimmed percent (%) trimmed percent specifies a percentage at which to discard the lowes

### TSA Vector Mean (Waveform) VI

Computes the mean values of a univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-mean-waveform-vi.png']

#### Inputs/Outputs

| trimmed percent (%) — trimmed percent specifies a percentage at which to discard the lowest and highest values in the time series. This option is available only when method is Trimmed. Xt — Xt specifies the multivariate (vector) time series. method — method specifies the method to use in computing the mean value of the input time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. vector mean — vector mean returns the vector mean values of the multivariate (vector) time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Mean Details

This VI calculates the mean values of an input time series with the method you specify for the **method** parameter.

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Mean VI.

Parent topic:

TSA Mean VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-skewness-and-kurtosis-array-vi.html language=enus -->
## TOPIC 00070: TSA Vector Skewness and Kurtosis (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-skewness-and-kurtosis-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-skewness-and-kurtosis-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the skewness and kurtosis values of a univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c2ddbl.png Xt Xt specifies the multivariate (vector) time series. Each column of

### TSA Vector Skewness and Kurtosis (Array) VI

Computes the skewness and kurtosis values of a univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-skewness-and-kurtosis-array-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the multivariate (vector) time series. Each column of the 2D array represents a vector at certain time. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. skewness — skewness returns the vector skewness values of the multivariate (vector) time series. kurtosis — kurtosis returns the vector kurtosis values of the multivariate (vector) time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Skewness and Kurtosis Details

This VI calculates the skewness value according to the following equation:

[IMAGE alt='image' src='tsa_equ_skewness.gif']

where n is the number of samples of the input time series X<sub>t</sub>, m is the arithmetic mean of X<sub>t</sub>, and s is the standard deviation of X<sub>t</sub>. Skewness is a symmetry measurement of the time series distribution. Negative values indicate left skewness. Positive values indicate right skewness.

This VI calculates the kurtosis value according to the following equation:

[IMAGE alt='image' src='tsa_equ_kurtosis.gif']

where n is the number of samples of the input time series X<sub>t</sub>, m is the arithmetic mean value of X<sub>t</sub>, and s is the standard deviation of X<sub>t</sub>. Kurtosis is a peakedness measurement of the time series distribution. Kurtosis values close to 3 indicate normal-peak distribution. Kurtosis values less than 3 indicate a flatter distribution than normal distribution. Kurtosis values greater than 3 indicate a sharper distribution than normal distribution.

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Skewness and Kurtosis VI.

Parent topic:

TSA Skewness and Kurtosis VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-skewness-and-kurtosis-waveform-vi.html language=enus -->
## TOPIC 00071: TSA Vector Skewness and Kurtosis (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-skewness-and-kurtosis-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/statistical-analysis-llb/tsa-vector-skewness-and-kurtosis-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the skewness and kurtosis values of a univariate or multivariate (vector) time series. Wire data to the Xt input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs c1dmsdt.png Xt Xt specifies the multivariate (vector) time series. cerrcodeclst.

### TSA Vector Skewness and Kurtosis (Waveform) VI

Computes the skewness and kurtosis values of a univariate or multivariate (vector) time series. Wire data to the **Xt** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='tsa-vector-skewness-and-kurtosis-waveform-vi.png']

#### Inputs/Outputs

| Xt — Xt specifies the multivariate (vector) time series. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. skewness — skewness returns the vector skewness values of the multivariate (vector) time series. kurtosis — kurtosis returns the vector kurtosis values of the multivariate (vector) time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Skewness and Kurtosis Details

This VI calculates the skewness value according to the following equation:

[IMAGE alt='image' src='tsa_equ_skewness.gif']

where n is the number of samples of the input time series X<sub>t</sub>, m is the arithmetic mean of X<sub>t</sub>, and s is the standard deviation of X<sub>t</sub>. Skewness is a symmetry measurement of the time series distribution. Negative values indicate left skewness. Positive values indicate right skewness.

This VI calculates the kurtosis value according to the following equation:

[IMAGE alt='image' src='tsa_equ_kurtosis.gif']

where n is the number of samples of the input time series X<sub>t</sub>, m is the arithmetic mean value of X<sub>t</sub>, and s is the standard deviation of X<sub>t</sub>. Kurtosis is a peakedness measurement of the time series distribution. Kurtosis values close to 3 indicate normal-peak distribution. Kurtosis values less than 3 indicate a flatter distribution than normal distribution. Kurtosis values greater than 3 indicate a sharper distribution than normal distribution.

#### Examples

Refer to the Series Statistical Analysis VI in the labview\examples\Time Series Analysis\TSAGettingStarted directory for an example of using the TSA Skewness and Kurtosis VI.

Parent topic:

TSA Skewness and Kurtosis VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/utilities-llb/tsa-normal-distribution-waveform-vi.html language=enus -->
## TOPIC 00072: TSA Normal Distribution (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/utilities-llb/tsa-normal-distribution-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/utilities-llb/tsa-normal-distribution-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a pseudorandom univariate or multivariate (vector) time series from different types of distribution. You must manually select the polymorphic instance to use. icon Inputs/Outputs ci32.png samples samples specifies the number of samples of the generated time series Xt. The value must be gre

### TSA Normal Distribution (Waveform) VI

Generates a pseudorandom univariate or multivariate (vector) time series from different types of distribution. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='tsa-normal-distribution-waveform-vi.png']

#### Inputs/Outputs

| samples — samples specifies the number of samples of the generated time series Xt. The value must be greater than or equal to 0. The default is 1024. mean — mean specifies the value of the center of the normal distribution. The default is 0. standard deviation — standard deviation specifies the standard deviation value of the normal distribution. The default is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. seed — seed specifies the seed of the noise sample generator. Seeds with different values greater than 0 generate different noise sequences. Values less than 0 cause reseeding each time this VI runs. The default is -1. Xt — Xt returns the random univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Random Sequence Generation Details

This VI generates a pseudorandom sequence from different distributions, such as the normal, uniform, chi-square, t, and F distributions.

#### Examples

Refer to the following VIs for examples of using the TSA Random Sequence Generation VI:

- Random Series Generate VI: labview\examples\Time Series Analysis\TSAGettingStarted
- Series Statistical Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Random Sequence Generation VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/time-series-analysis/utilities-llb/tsa-t-distribution-waveform-vi.html language=enus -->
## TOPIC 00073: TSA T Distribution (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/time-series-analysis/utilities-llb/tsa-t-distribution-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/time-series-analysis/utilities-llb/tsa-t-distribution-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a pseudorandom univariate or multivariate (vector) time series from different types of distribution. You must manually select the polymorphic instance to use. icon Inputs/Outputs ci32.png samples samples specifies the number of samples of the generated time series Xt. The value must be gre

### TSA T Distribution (Waveform) VI

Generates a pseudorandom univariate or multivariate (vector) time series from different types of distribution. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='tsa-t-distribution-waveform-vi.png']

#### Inputs/Outputs

| samples — samples specifies the number of samples of the generated time series Xt. The value must be greater than or equal to 0. The default is 1024. degrees of freedom — degrees of freedom specifies the degrees of freedom this VI uses to define the t distribution. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Xt — Xt returns the random univariate time series. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### TSA Random Sequence Generation Details

This VI generates a pseudorandom sequence from different distributions, such as the normal, uniform, chi-square, t, and F distributions.

#### Examples

Refer to the following VIs for examples of using the TSA Random Sequence Generation VI:

- Random Series Generate VI: labview\examples\Time Series Analysis\TSAGettingStarted
- Series Statistical Analysis VI: labview\examples\Time Series Analysis\TSAGettingStarted

Parent topic:

TSA Random Sequence Generation VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/application-llb/wa-detrend-array-vi.html language=enus -->
## TOPIC 00074: WA Detrend (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/application-llb/wa-detrend-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/application-llb/wa-detrend-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the trend from 1D signals by setting the approximation coefficients to zeros. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cu16.png extension extension specifies the method to use to pad data at the borders of

### WA Detrend (Array) VI

Removes the trend from 1D signals by setting the approximation coefficients to zeros. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-detrend-array-vi.png']

#### Inputs/Outputs

| extension — extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. signal — signal specifies the input signal. threshold frequency — threshold frequency specifies the upper frequency limit, in hertz, of the trend that this VI removes from the signal. The threshold frequency determines the wavelet transform level. The wavelet transform level specifies the number of levels in the discrete wavelet analysis. The wavelet transform level is floor(log2[sampling rate/(2*threshold frequency)]). The floor function rounds a value to the nearest integer towards negative infinity. The default is -1, which means this VI sets the threshold frequency automatically. wavelet — wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. filter banks — filter banks specifies the analysis filter banks and the synthesis filter banks for the wavelet you specify. If you specify a value for filter banks, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. analysis filters — analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. synthesis filters — synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. detrended signal — detrended signal returns the signal without the trend. trend signal — trend signal returns the residual trend of the signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| analysis filters — analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. synthesis filters — synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
| lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
| lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |

#### WA Detrend Details

The trend of the input signal is the slow-varying part of the signal that mainly contributes to the approximation coefficients. This VI applies the following steps to implement the detrend function.

1. Applies the discrete wavelet transform (DWT) to the input signal.
2. Sets the approximation coefficients to 0.
3. Reconstructs the signal based on all the detail coefficients.

#### Examples

Refer to the Detrend and Trend Estimation VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA Detrend VI.

Parent topic:

WA Detrend VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-vi.html language=enus -->
## TOPIC 00075: WA Probability Density Function Estimation VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Estimates the probability density function (PDF) of 1D or 2D signals from the error-reduced statistical histogram. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon WA Probability Density Function Estimation Details This VI completes the

### WA Probability Density Function Estimation VI

Estimates the probability density function (PDF) of 1D or 2D signals from the error-reduced statistical histogram. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-probability-density-function-estimation-vi.png']

#### WA Probability Density Function Estimation Details

This VI completes the following steps to implement the wavelet-based estimation of the probability density function.

1. Calculates the histogram of the input signal.
2. Performs the wavelet denoising on the histogram output.
3. Rescales the denoised function to return a unit integral.

You often estimate the PDF of a signal or image by computing the histogram for a large number of samples. However, when the realization number of a stochastic process is limited, such as with an image with a fixed size, the PDF estimation from the histogram might include a large variance. In this case, you can use smoothing methods to return a better estimate. The wavelet method can keep the smoothness of the estimated PDF and provide a solution for density functions with breakdown points.

#### Examples

Refer to the Probability Density Function Estimation VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA Probability Density Function Estimation VI.

- [WA Probability Density Function Estimation (Waveform) VI](../../../../vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-waveform-vi.html) Estimates the probability density function (PDF) of 1D or 2D signals from the error-reduced statistical histogram. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [WA Probability Density Function Estimation (1D Array) VI](../../../../vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-1d-array-vi.html) Estimates the probability density function (PDF) of 1D or 2D signals from the error-reduced statistical histogram. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [WA Probability Density Function Estimation (2D Array) VI](../../../../vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-2d-array-vi.html) Estimates the probability density function (PDF) of 1D or 2D signals from the error-reduced statistical histogram. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Feature Extraction

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-waveform-vi.html language=enus -->
## TOPIC 00076: WA Probability Density Function Estimation (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/application-llb/wa-probability-density-function-estimation-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Estimates the probability density function (PDF) of 1D or 2D signals from the error-reduced statistical histogram. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cmsdt.png signal signal specifies the input signal. ci32.

### WA Probability Density Function Estimation (Waveform) VI

Estimates the probability density function (PDF) of 1D or 2D signals from the error-reduced statistical histogram. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-probability-density-function-estimation-waveform-vi.png']

#### Inputs/Outputs

| signal — signal specifies the input signal. number of bins — number of bins specifies the number of bins to use to estimate the statistical histogram of signal. wavelet — wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. filter banks — filter banks specifies the analysis filter banks and the synthesis filter banks for the wavelet you specify. If you specify a value for filter banks, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. analysis filters — analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. synthesis filters — synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. PDF — PDF returns the estimated probability density function of signal on an XY graph. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| analysis filters — analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. synthesis filters — synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters for the wavelet you specify. lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |
| lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
| lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |

#### WA Probability Density Function Estimation Details

This VI completes the following steps to implement the wavelet-based estimation of the probability density function.

1. Calculates the histogram of the input signal.
2. Performs the wavelet denoising on the histogram output.
3. Rescales the denoised function to return a unit integral.

You often estimate the PDF of a signal or image by computing the histogram for a large number of samples. However, when the realization number of a stochastic process is limited, such as with an image with a fixed size, the PDF estimation from the histogram might include a large variance. In this case, you can use smoothing methods to return a better estimate. The wavelet method can keep the smoothness of the estimated PDF and provide a solution for density functions with breakdown points.

#### Examples

Refer to the Probability Density Function Estimation VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA Probability Density Function Estimation VI.

Parent topic:

WA Probability Density Function Estimation VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-analytic-wavelet-transform-array-vi.html language=enus -->
## TOPIC 00077: WA Analytic Wavelet Transform (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-analytic-wavelet-transform-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-analytic-wavelet-transform-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the complex-valued Morlet wavelet to compute the continuous wavelet transform (CWT) of a 1D input signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cu16.png normalization normalization specifies how to scale t

### WA Analytic Wavelet Transform (Array) VI

Uses the complex-valued Morlet wavelet to compute the continuous wavelet transform (CWT) of a 1D input signal. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-analytic-wavelet-transform-array-vi.png']

#### Inputs/Outputs

| normalization — normalization specifies how to scale the dilated wavelets. time steps — time steps specifies the number of samples to translate, or shift, the wavelet in the analytic wavelet transform (AWT). The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 coefficients exist at each scale. signal — signal specifies the input signal. scales — scales specifies the number of scales of the dilated wavelet. scale sampling method — scale sampling method specifies the method to use to select the scales of the wavelets. scale sampling method affects the mapping style of the y-axis of the scalogram. Use the user defined scales input to specify a customized scale. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined scales — user defined scales specifies the scales to use to compute AWT coef. The scale must be positive and no greater than the length of signal. If you specify a value for user defined scales, this VI ignores the settings in the scale sampling method input and the scales input. sampling rate — sampling rate specifies the sampling rate of signal in hertz. sampling rate must be greater than 0, or this VI sets sampling rate to 1 automatically. The default is 1. AWT coef — AWT coef returns the results of the analytic wavelet transform (AWT). scale info — scale info returns the time information and the scale (frequency) information, which this VI uses in the scalogram plot. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### WA Analytic Wavelet Transform Details

The AWT is a special case of the CWT with the complex-valued Morlet wavelet, also called the Gabor wavelet. The following equation defines the complex-valued Morlet wavelet:

[IMAGE alt='image' src='eq_morlet.gif']

where [IMAGE alt='image' src='sigma.gif'] is the standard deviation of the Gaussian envelope of the mother wavelet, and [IMAGE alt='image' src='eq_central_freq.gif'] is the central frequency of the mother wavelet, which is [IMAGE alt='image' src='eq_threehalves_pi.gif'] in this VI.

#### Examples

Refer to the following VIs for examples of using the WA Analytic Wavelet Transform VI:

- Scalogram with Analytic Wavelet Transform VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Spectrogram Ridge Detection VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Color Tables for Displaying the Scalogram VI: labview\examples\Wavelet Analysis\WAGettingStarted

Parent topic:

WA Analytic Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-analytic-wavelet-transform-waveform-vi.html language=enus -->
## TOPIC 00078: WA Analytic Wavelet Transform (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-analytic-wavelet-transform-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-analytic-wavelet-transform-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the complex-valued Morlet wavelet to compute the continuous wavelet transform (CWT) of a 1D input signal. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs cu16.png normalization normalization specifies how to scale t

### WA Analytic Wavelet Transform (Waveform) VI

Uses the complex-valued Morlet wavelet to compute the continuous wavelet transform (CWT) of a 1D input signal. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-analytic-wavelet-transform-waveform-vi.png']

#### Inputs/Outputs

| normalization — normalization specifies how to scale the dilated wavelets. time steps — time steps specifies the number of samples to translate, or shift, the wavelet in the analytic wavelet transform (AWT). The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 coefficients exist at each scale. signal — signal specifies the input signal. scales — scales specifies the number of scales of the dilated wavelet. scale sampling method — scale sampling method specifies the method to use to select the scales of the wavelets. scale sampling method affects the mapping style of the y-axis of the scalogram. Use the user defined scales input to specify a customized scale. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined scales — user defined scales specifies the scales to use to compute AWT coef. The scale must be positive and no greater than the length of signal. If you specify a value for user defined scales, this VI ignores the settings in the scale sampling method input and the scales input. AWT coef — AWT coef returns the results of the analytic wavelet transform (AWT). scale info — scale info returns the time information and the scale (frequency) information, which this VI uses in the scalogram plot. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### WA Analytic Wavelet Transform Details

The AWT is a special case of the CWT with the complex-valued Morlet wavelet, also called the Gabor wavelet. The following equation defines the complex-valued Morlet wavelet:

[IMAGE alt='image' src='eq_morlet.gif']

where [IMAGE alt='image' src='sigma.gif'] is the standard deviation of the Gaussian envelope of the mother wavelet, and [IMAGE alt='image' src='eq_central_freq.gif'] is the central frequency of the mother wavelet, which is [IMAGE alt='image' src='eq_threehalves_pi.gif'] in this VI.

#### Examples

Refer to the following VIs for examples of using the WA Analytic Wavelet Transform VI:

- Scalogram with Analytic Wavelet Transform VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Spectrogram Ridge Detection VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Color Tables for Displaying the Scalogram VI: labview\examples\Wavelet Analysis\WAGettingStarted

Parent topic:

WA Analytic Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-array-vi.html language=enus -->
## TOPIC 00079: WA Continuous Wavelet Transform (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the continuous wavelet transform (CWT) of the 1D input signal with real-valued wavelets. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ci32.png time steps time steps specifies the number of samples to translat

### WA Continuous Wavelet Transform (Array) VI

Computes the continuous wavelet transform (CWT) of the 1D input signal with real-valued wavelets. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-continuous-wavelet-transform-array-vi.png']

#### Inputs/Outputs

| time steps — time steps specifies the number of samples to translate, or shift, the wavelet in the continuous wavelet transform (CWT). The default is -1, which specifies that this VI adjusts time steps automatically so that no more than 512 coefficients exist at each scale. signal — signal specifies the input signal. scales — scales specifies the number of scales of the dilated wavelet. wavelet — wavelet specifies the wavelet type to use to compute the continuous wavelet coefficients. The default is db02. The options include the following types: Mexican Hat, Meyer, Morlet, orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user defined scales — user defined scales specifies the scales to use to compute CWT coef. The scale must be positive and no greater than the length of signal. If you specify a value for user defined scales, this VI ignores the settings in the scales input. user defined wavelet — user defined wavelet specifies the mother wavelet function to use to compute the continuous wavelet transform (CWT). If you specify a value for user defined wavelet, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the wavelet. t0 — t0 specifies the initial time of the mother wavelet function. dt — dt specifies the time interval of the mother wavelet function in samples. mother wavelet — mother wavelet specifies the mother wavelet function. CWT coef — CWT coef returns the results of the continuous wavelet transform (CWT). scale info — scale info returns the time information and the scale (frequency) information, which this VI uses in the scalogram plot. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the initial time of the mother wavelet function. dt — dt specifies the time interval of the mother wavelet function in samples. mother wavelet — mother wavelet specifies the mother wavelet function. |

#### WA Continuous Wavelet Transform Details

The following equation defines the CWT:

[IMAGE alt='image' src='eq_cont_wavelet_trans.gif']

where s(t) is the signal, [IMAGE alt='image' src='eq_mother_wavelet_func.gif'] is the mother wavelet function, and a and [IMAGE alt='image' src='eq_shift.gif'] are the scale and shift of the wavelet, respectively. a can be any positive real value. Use **user defined scales** to specify the scales. If you do not specify values for **user defined scales**, this VI selects the scale, a, as 1, 2, 3,…, **scales**. This VI selects the shift, [IMAGE alt='image' src='eq_shift.gif'], as 0, dt, 2dt, 3dt,…, Ndt, where dt is **time steps**, and N is approximately equal to the signal length divided by **time steps**. Refer to [A Wavelet Tour of Signal Processing](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_related_doc) for more information about the CWT.

#### Examples

Refer to the Breakdown Point Detection VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of using the WA Continuous Wavelet Transform VI.

Parent topic:

WA Continuous Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-vi.html language=enus -->
## TOPIC 00080: WA Continuous Wavelet Transform VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the continuous wavelet transform (CWT) of the 1D input signal with real-valued wavelets. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance. icon WA Continuous Wavelet Transform Details The following equation defines the CWT: where s(t

### WA Continuous Wavelet Transform VI

Computes the continuous wavelet transform (CWT) of the 1D input signal with real-valued wavelets. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-continuous-wavelet-transform-vi.png']

#### WA Continuous Wavelet Transform Details

The following equation defines the CWT:

[IMAGE alt='image' src='eq_cont_wavelet_trans.gif']

where s(t) is the signal, [IMAGE alt='image' src='eq_mother_wavelet_func.gif'] is the mother wavelet function, and a and [IMAGE alt='image' src='eq_shift.gif'] are the scale and shift of the wavelet, respectively. a can be any positive real value. Use **user defined scales** to specify the scales. If you do not specify values for **user defined scales**, this VI selects the scale, a, as 1, 2, 3,…, **scales**. This VI selects the shift, [IMAGE alt='image' src='eq_shift.gif'], as 0, dt, 2dt, 3dt,…, Ndt, where dt is **time steps**, and N is approximately equal to the signal length divided by **time steps**. Refer to [A Wavelet Tour of Signal Processing](/csh?context=lvmnt_aspt_lvasptconcepts_aspt_related_doc) for more information about the CWT.

#### Examples

Refer to the Breakdown Point Detection VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of using the WA Continuous Wavelet Transform VI.

- [WA Continuous Wavelet Transform (Waveform) VI](../../../../vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-waveform-vi.html) Computes the continuous wavelet transform (CWT) of the 1D input signal with real-valued wavelets. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [WA Continuous Wavelet Transform (Array) VI](../../../../vi-lib/addons/wavelet-analysis/continuous-wavelet-transform-llb/wa-continuous-wavelet-transform-array-vi.html) Computes the continuous wavelet transform (CWT) of the 1D input signal with real-valued wavelets. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Continuous Wavelet

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-2d-discrete-wavelet-transform-vi.html language=enus -->
## TOPIC 00081: WA 2D Discrete Wavelet Transform VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-2d-discrete-wavelet-transform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-2d-discrete-wavelet-transform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the multi-level discrete wavelet transform (DWT) of signal. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input. This VI returns the approximation coefficients and the detail coefficients at all levels for a 2D

### WA 2D Discrete Wavelet Transform VI

Computes the multi-level discrete wavelet transform (DWT) of **signal**. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input. This VI returns the approximation coefficients and the detail coefficients at all levels for a 2D signal input. This VI computes the DWT at each level by using the lowpass analysis filters, the highpass analysis filters, and a decimation factor of 2. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-2d-discrete-wavelet-transform-vi.png']

#### Inputs/Outputs

| extension — extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. signal — signal specifies the 2D input signal. levels — levels specifies the number of levels in the discrete wavelet analysis. levels must be a positive integer no greater than log2(Ls), where Ls is the length of the 1D signal or the minimum dimensional size of the 2D signal. The default is -1, which indicates that this VI sets levels as the largest integer no greater than log2(Ls). wavelet — wavelet specifies the wavelet type to use for the discrete wavelet analysis. The default is db02. The options include two types: orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx)) and biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI))), where x indicates the order of the wavelet. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. analysis filters — analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters for the wavelet you specify. If you specify a value for analysis filters, this VI ignores the settings in the wavelet input. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. DWT coef — DWT coef returns the approximation coefficients and the detail coefficients from the multi-level discrete wavelet transform (DWT). Each element of the array contains the 2D DWT results of one level. The ith element stores the approximation coefficients and the detail coefficients at level i+1. low_low — low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
| low_low — low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |

#### WA Discrete Wavelet Transform Details

The following illustration shows an example of a three-level discrete wavelet decomposition, where you set the **levels** input of this VI to 3. The length of the input signal is 16 points.

[IMAGE alt='image' src='disc_wvlet_transform.gif']

G<sub>1</sub>(z) denotes that the signal passes through a highpass filter. G<sub>0</sub>(z) denotes that the signal passes through a lowpass filter. G<sub>1</sub>(z) and G<sub>0</sub>(z) form the [analysis filter bank](/csh?context=lvmnt_aspt_lvasptconcepts_wa_discrete). [IMAGE alt='image' src='eq_decimate_by_2.gif'] denotes a decimation on the signal with a factor of 2.

Using information in the previous illustration, you can see that the **DWT coef** output contains the approximation coefficients of the largest level and the details coefficients of each level. You also can see that the **length** output of this VI contains the following elements, where the last element is the length of the input signal:

[IMAGE alt='image' src='lengths_elements.gif']

#### Examples

Refer to the following VIs for examples of using the WA Discrete Wavelet Transform VI:

- Image Compression VI: labview\examples\Wavelet Analysis\WAApplications
- Get and Set Single Level Detail Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Transform and Reconstruction with Image VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Piece Polynomial Function Approx and Comp VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Multiscale Analysis VI: labview\examples\Wavelet Analysis\WAApplications
- Get and Set Approximation Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- ECG Compression VI: labview\examples\Wavelet Analysis\WAApplications

Parent topic:

WA Discrete Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-2d-integer-wavelet-transform-vi.html language=enus -->
## TOPIC 00082: WA 2D Integer Wavelet Transform VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-2d-integer-wavelet-transform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-2d-integer-wavelet-transform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the lifting scheme to compute the multi-level integer wavelet transform (IWT) of signal. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input and returns the approximation coefficients and the detail coefficients at

### WA 2D Integer Wavelet Transform VI

Uses the lifting scheme to compute the multi-level integer wavelet transform (IWT) of **signal**. This VI returns the approximation coefficients at the largest level and the detail coefficients at all levels for a 1D signal input and returns the approximation coefficients and the detail coefficients at all levels for a 2D signal input. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-2d-integer-wavelet-transform-vi.png']

#### Inputs/Outputs

| extension — extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. signal — signal specifies the 2D input signal. levels — levels specifies the number of levels in the discrete wavelet analysis. levels must be a positive integer no greater than log2(Ls), where Ls is the length of the 1D signal or the minimum dimensional size of the 2D signal. The default is -1, which indicates that this VI sets levels as the largest integer no greater than log2(Ls). wavelet — wavelet specifies the wavelet type to use for the integer wavelet analysis. The default is Haar. Options include Haar, bior2_2, and bior4_4 (FBI). If you use another type of wavelet, this VI uses the default value automatically. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. IWT coef — IWT coef returns the approximation coefficients and the detail coefficients from the multi-level integer wavelet transform (IWT). Each element of the array includes the approximation coefficients and the detail coefficients at a level. Each element of the array contains the 2D IWT results of one level. The ith element stores the approximation coefficients and the detail coefficients at level i+1. low_low — low_low returns coefficients that are a low-resolution approximation of the original 2D signal. low_high — low_high returns the low_high coefficients. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low returns the high_low coefficients. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high returns the high_high coefficients. The high-frequency signal along the diagonal direction influences the high_high coefficients. 2D IWT plot — 2D IWT plot returns the approximation coefficients at the largest level and the detail coefficients at all levels. 2D IWT plot is the same size as signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| low_low — low_low returns coefficients that are a low-resolution approximation of the original 2D signal. low_high — low_high returns the low_high coefficients. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low returns the high_low coefficients. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high returns the high_high coefficients. The high-frequency signal along the diagonal direction influences the high_high coefficients. |

#### WA Integer Wavelet Transform Details

Similarly to the [discrete wavelet transform (DWT)](/csh?context=lvmnt_aspt_lvasptconcepts_wa_dwt), this VI applies the IWT to the signal and then to the approximation coefficients of each level recursively.

On each level, this VI implements the IWT with the lifting scheme. The following illustration shows a flowchart of a one-level IWT with the lifting scheme:

[IMAGE alt='image' src='one_level_int_wavelet_trans.gif']

a<sub>l</sub> is the approximation coefficients of level l. a<sub>l+1</sub> and d<sub>l+1</sub> are the approximation coefficients and the details coefficients of level l+1. The lifting scheme is an iterative procedure. The number of the iteration, M, depends on the wavelet type. At the first iteration, a<sub>l</sub> splits into a set of even-indexed elements and a set of odd-indexed elements. This VI uses the set of even-indexed elements of the approximation coefficients of level l, a<sub>l, 2k</sub>, as the initial approximation coefficients of level l+1, [IMAGE alt='image' src='eq_approx_coeff.gif']. This VI uses the set of odd-indexed elements of the approximation coefficients of level l, a<sub>l, 2k+1</sub>, as the initial detail coefficients of level l+1, [IMAGE alt='image' src='eq_detail_coeff.gif']. This VI then iteratively passes the initial approximation coefficients and the initial detail coefficients through the lifting filter, P<sup>(m)</sup>(z), and the dual lifting filter, U<sup>(m)</sup>(z), to obtain the approximation coefficients and the detail coefficients as shown in the following equations:

[IMAGE alt='image' src='eq_lifting1.gif']

[IMAGE alt='image' src='eq_lifting2.gif']

where m indicates the index of iteration, k is the coefficient index, n is the total number of coefficients, I is the number of taps of the lifting filters, and [IMAGE alt='image' src='eq_truncx.gif'] is the operator to truncate x to the largest integer that is no greater than x. This VI computes M, P<sup>(m)</sup>(z), and U<sup>(m)</sup>(z) automatically according to the wavelet type you select.

The inverse IWT is a reverse operation of the IWT. The following illustration shows a flowchart of a one-level inverse IWT:

[IMAGE alt='image' src='inverse_int_wavelet_trans.gif']

Because IWT coefficients are integers, you do not need to quantize the coefficients in the process of compression, and you do not encounter the quantization error. Therefore, the IWT and the inverse IWT are used widely in lossless signal or image compression applications.

#### Examples

Refer to the following VIs for examples of using the WA Integer Wavelet Transform VI:

- Lossless Medical Image Compression VI: labview\examples\Wavelet Analysis\WAApplications
- Integer Wavelet Transform on Image VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Integer Wavelet Transform on 1D Signal VI: labview\examples\Wavelet Analysis\WAGettingStarted

Parent topic:

WA Integer Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-arbitrary-path-decomposition-vi.html language=enus -->
## TOPIC 00083: WA Arbitrary Path Decomposition VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-arbitrary-path-decomposition-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-arbitrary-path-decomposition-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs subband decomposition by cascading the lowpass analysis filters and the highpass analysis filters and applies a decimation factor of 2 after each filtering step. path specifies the subband and determines how to cascade the lowpass analysis filters and the highpass analysis filters. Wire dat

### WA Arbitrary Path Decomposition VI

Performs subband decomposition by cascading the lowpass analysis filters and the highpass analysis filters and applies a decimation factor of 2 after each filtering step. **path** specifies the subband and determines how to cascade the lowpass analysis filters and the highpass analysis filters. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-arbitrary-path-decomposition-vi.png']

#### WA Arbitrary Path Decomposition Details

The following illustration shows an example of an arbitrary path decomposition with the **path** input set to 101 and the **extension** input set to **Periodic**. The length of the input signal is 16 points.

[IMAGE alt='image' src='arbpath.gif']

G<sub>1</sub>(z) denotes that the signal passes through a highpass filter. G<sub>0</sub>(z) denotes that the signal passes through a lowpass filter. G<sub>1</sub>(z) and G<sub>0</sub>(z) form the [analysis filter bank](/csh?context=lvmnt_aspt_lvasptconcepts_wa_discrete). [IMAGE alt='image' src='eq_decimate_by_2.gif'] denotes a decimation on the signal with a factor of 2. Path 101 indicates that this VI passes the signal through a highpass filter G<sub>1</sub>(z), through a lowpass filter G<sub>0</sub>(z), and then through a highpass filter G<sub>1</sub>(z).

Using information in the previous illustration, you can see that the **residual info** output contains the information about the complementary subbands at each level, and you can see that the **path coef** output of this VI contains the coefficients of the subband that **path** defines.

A discrete wavelet decomposition decomposes the lowpass filtering output, or the approximation coefficients, at each level. However, an arbitrary path decomposition does not restrict the decomposition to the lowpass filtering output. You can use the lowpass filtering output or the highpass filtering output for the further decomposition.

The **residual info** output stores the information of path 0, path 11, and path 100 in the above example for reconstruction. You can use the **source coefficients** input of the [WA Arbitrary Path Reconstruction](wa-arbitrary-path-reconstruction-vi.html) VI to select path coefficients and/or residual coefficients to reconstruct the signal.

#### Examples

Refer to the Engine Knocking Detection VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of using the WA Arbitrary Path Decomposition VI.

- [WA Arbitrary Path Decomposition (Waveform) VI](../../../../vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-arbitrary-path-decomposition-waveform-vi.html) Performs subband decomposition by cascading the lowpass analysis filters and the highpass analysis filters and applies a decimation factor of 2 after each filtering step. path specifies the subband and determines how to cascade the lowpass analysis filters and the highpass analysis filters. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.
- [WA Arbitrary Path Decomposition (Array) VI](../../../../vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-arbitrary-path-decomposition-array-vi.html) Performs subband decomposition by cascading the lowpass analysis filters and the highpass analysis filters and applies a decimation factor of 2 after each filtering step. path specifies the subband and determines how to cascade the lowpass analysis filters and the highpass analysis filters. Wire data to the signal input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Discrete Wavelet

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-get-coefficients-of-1d-discrete-wavelet-transform-array-vi.html language=enus -->
## TOPIC 00084: WA Get Coefficients of 1D Discrete Wavelet Transform (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-get-coefficients-of-1d-discrete-wavelet-transform-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-get-coefficients-of-1d-discrete-wavelet-transform-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT of a signal. Wire data to the DWT coef input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outp

### WA Get Coefficients of 1D Discrete Wavelet Transform (Array) VI

Retrieves approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT of a signal. Wire data to the **DWT coef** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-get-coefficients-of-1d-discrete-wavelet-transform-array-vi.png']

#### Inputs/Outputs

| coef type — coef type specifies whether this VI returns approximation coefficients or detail coefficients. The default is Approximation coefficients. DWT coef — DWT coef specifies the approximation coefficients and the detail coefficients from the multi-level discrete wavelet decomposition (DWT). You must organize the coefficients into a 1D real array starting with the approximation coefficients at the largest level followed by the detail coefficients at all levels in descending order. length — length specifies, in a 1D array, the number of approximation and detail coefficients at each level. At a decomposition level of N, length is equal to N+2. The first element of length always is equal to the number of approximation coefficients. The last element of length indicates the total number of raw data samples. You must arrange the length of the detail coefficients in descending order. coef level — coef level specifies the coefficient level this VI returns. The coef level must be between 1 and the largest level of the detail coefficients. The levels in the WA Discrete Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI returns the coefficients at level 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. DWT coef out — DWT coef out returns DWT coef unchanged. length out — length out returns length unchanged. error out — error out contains error information. This output provides standard error out functionality. selected DWT coef — selected DWT coef returns the discrete wavelet transform (DWT) coefficients at the coefficient level coef level of the coefficient type coef type. |
| --- |

#### Examples

Refer to the following VIs for examples of using the WA Get Coefficients of Discrete Wavelet Transform VI:

- Get and Set Approximation Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Get and Set Single Level Detail Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted

Parent topic:

WA Get Coefficients of Discrete Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-1d-undecimated-wavelet-transform-waveform-vi.html language=enus -->
## TOPIC 00085: WA Set Coefficients of 1D Undecimated Wavelet Transform (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-1d-undecimated-wavelet-transform-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-1d-undecimated-wavelet-transform-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets approximation or detail undecimated wavelet transform (UWT) coefficients at a specific level. Use the WA Undecimated Wavelet Transform VI to compute the UWT. Use the WA Get Coefficients of Undecimated Wavelet Transform VI to obtain the UWT coefficients. icon Inputs/Outputs cu16.png coef type co

### WA Set Coefficients of 1D Undecimated Wavelet Transform (Waveform) VI

Sets approximation or detail undecimated wavelet transform (UWT) coefficients at a specific level. Use the WA Undecimated Wavelet Transform VI to compute the UWT. Use the WA Get Coefficients of Undecimated Wavelet Transform VI to obtain the UWT coefficients.

[IMAGE alt='icon' src='wa-set-coefficients-of-1d-undecimated-wavelet-transform-waveform-vi.png']

#### Inputs/Outputs

| coef type — coef type specifies whether this VI sets the approximation coefficients or detail coefficients. The default is Approximation coefficients. UWT coef — UWT coef specifies the approximation coefficients and the detail coefficients from the multi-level undecimated wavelet transform (UWT). You must organize the coefficients in an array of waveforms starting with the approximation coefficients at the largest level followed by the detail coefficients at all levels in descending order. coef level — coef level specifies the coefficient level this VI sets. The coef level must be between 1 and the largest level of the coefficients. The levels in the WA Undecimated Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI sets the coefficients at level 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. new UWT coef — new UWT coef specifies the undecimated wavelet transform (UWT) coefficients to set. UWT coef out — UWT coef out returns the undecimated wavelet transform (UWT) coefficients set to new UWT coef at the coef type and coef level. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

WA Set Coefficients of Undecimated Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-2d-integer-wavelet-transform-vi.html language=enus -->
## TOPIC 00086: WA Set Coefficients of 2D Integer Wavelet Transform VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-2d-integer-wavelet-transform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-2d-integer-wavelet-transform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets approximation or detail integer wavelet transform (IWT) coefficients at a specific level. Use the WA Integer Wavelet Transform VI to compute the IWT. Use the WA Get Coefficients of Integer Wavelet Transform VI to obtain the IWT coefficients. icon Inputs/Outputs cu16.png coef type coef type spec

### WA Set Coefficients of 2D Integer Wavelet Transform VI

Sets approximation or detail integer wavelet transform (IWT) coefficients at a specific level. Use the WA Integer Wavelet Transform VI to compute the IWT. Use the WA Get Coefficients of Integer Wavelet Transform VI to obtain the IWT coefficients.

[IMAGE alt='icon' src='wa-set-coefficients-of-2d-integer-wavelet-transform-vi.png']

#### Inputs/Outputs

| coef type — coef type specifies the coefficient type this VI sets. IWT coef — IWT coef specifies the approximation coefficients and the detail coefficients from the multi-level integer wavelet transform (IWT). Each element of the array contains the 2D IWT results of one level. The ith element stores the approximation coefficients and the detail coefficients at level i+1. low_low — low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. coef level — coef level specifies the coefficient level this VI sets. The coef level must be between 1 and the largest level of the coefficients. The levels in the WA Integer Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI sets the coefficients at level 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. new IWT coef — new IWT coef specifies the integer wavelet transform (IWT) coefficients to set. IWT coef out — IWT coef out returns the integer wavelet transform (IWT) coefficients set to new IWT coef at the coef type and coef level. low_low out — low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. low_high out — low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. high_low out — high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. high_high out — high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| low_low — low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
| low_low out — low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. low_high out — low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. high_low out — high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. high_high out — high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. |

Parent topic:

WA Set Coefficients of Integer Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-2d-undecimated-wavelet-transform-vi.html language=enus -->
## TOPIC 00087: WA Set Coefficients of 2D Undecimated Wavelet Transform VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-2d-undecimated-wavelet-transform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-2d-undecimated-wavelet-transform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets approximation or detail undecimated wavelet transform (UWT) coefficients at a specific level. Use the WA Undecimated Wavelet Transform VI to compute the UWT. Use the WA Get Coefficients of Undecimated Wavelet Transform VI to obtain the UWT coefficients. icon Inputs/Outputs cu16.png coef type co

### WA Set Coefficients of 2D Undecimated Wavelet Transform VI

Sets approximation or detail undecimated wavelet transform (UWT) coefficients at a specific level. Use the WA Undecimated Wavelet Transform VI to compute the UWT. Use the WA Get Coefficients of Undecimated Wavelet Transform VI to obtain the UWT coefficients.

[IMAGE alt='icon' src='wa-set-coefficients-of-2d-undecimated-wavelet-transform-vi.png']

#### Inputs/Outputs

| coef type — coef type specifies the coefficient type this VI sets. UWT coef — UWT coef specifies the approximation coefficients and the detail coefficients from the multi-level undecimated wavelet transform (UWT). Each element of the array contains the 2D UWT results of one level. The ith element stores the approximation coefficients and the detail coefficients at level i+1. low_low — low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. coef level — coef level specifies the coefficient level this VI sets. The coef level must be between 1 and the largest level of the coefficients. The levels in the WA Undecimated Wavelet Transform VI specifies the largest level of the coefficients. The default is 1, which means this VI sets the coefficients at level 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. new UWT coef — new UWT coef specifies the undecimated wavelet transform (UWT) coefficients to set. UWT coef out — UWT coef out returns the undecimated wavelet transform (UWT) coefficients set to new UWT coef at the coef type and coef level. low_low out — low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. low_high out — low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. high_low out — high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. high_high out — high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| low_low — low_low specifies the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high specifies the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low specifies the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high specifies the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |
| low_low out — low_low out returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low out coefficients are a low-resolution approximation of the original 2D signal. low_high out — low_high out returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high out coefficients. high_low out — high_low out returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low out coefficients. high_high out — high_high out returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high out coefficients. |

Parent topic:

WA Set Coefficients of Undecimated Wavelet Transform VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-discrete-wavelet-transform-vi.html language=enus -->
## TOPIC 00088: WA Set Coefficients of Discrete Wavelet Transform VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-discrete-wavelet-transform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-discrete-wavelet-transform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT. Use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients. icon Examples Refer to the following VIs for examp

### WA Set Coefficients of Discrete Wavelet Transform VI

Sets approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT. Use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients.

[IMAGE alt='icon' src='wa-set-coefficients-of-discrete-wavelet-transform-vi.png']

#### Examples

Refer to the following VIs for examples of using the WA Set Coefficients of Discrete Wavelet Transform VI:

- Get and Set Approximation Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Get and Set Single Level Detail Coefficients VI: labview\examples\Wavelet Analysis\WAGettingStarted

- [WA Set Coefficients of 1D Discrete Wavelet Transform (Waveform) VI](../../../../vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-1d-discrete-wavelet-transform-waveform-vi.html) Sets approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT. Use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients.
- [WA Set Coefficients of 1D Discrete Wavelet Transform (Array) VI](../../../../vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-1d-discrete-wavelet-transform-array-vi.html) Sets approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT. Use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients.
- [WA Set Coefficients of 2D Discrete Wavelet Transform VI](../../../../vi-lib/addons/wavelet-analysis/discrete-wavelet-transform-llb/wa-set-coefficients-of-2d-discrete-wavelet-transform-vi.html) Sets approximation or detail discrete wavelet transform (DWT) coefficients at a specific level. Use the WA Discrete Wavelet Transform VI to compute the DWT. Use the WA Get Coefficients of Discrete Wavelet Transform VI to obtain the DWT coefficients.

Parent topic:

Discrete Wavelet

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/express/multiresolutionanalysissource-llb/multiresolutionanalysis-source-vi.html language=enus -->
## TOPIC 00089: Multiresolution Analysis

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/express/multiresolutionanalysissource-llb/multiresolutionanalysis-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/express/multiresolutionanalysissource-llb/multiresolutionanalysis-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decomposes a signal according to the level you specify and reconstructs the signal from the frequency bands you select. icon Dialog Box Options Inputs/Outputs cpath.png File path Specifies the file path of the data you want to load. This input is available only when you select the From file option i

### Multiresolution Analysis

Decomposes a signal according to the level you specify and reconstructs the signal from the frequency bands you select.

[IMAGE alt='icon' src='multiresolutionanalysis-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| File path — Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Signal — Specifies the block diagram terminal of the data you want to load. This input is available only if you select the From terminal option in the Data Source section. error out — error out contains error information. This output provides standard error out functionality. Reconstruction — Returns the reconstructed signal. |
| --- |

#### Examples

Refer to the Multiresolution Analysis - 1D Signal VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the Multiresolution Analysis VI.

Parent topic:

Discrete Wavelet

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/express/waveletdenoisesource-llb/waveletdenoise-source-vi.html language=enus -->
## TOPIC 00090: Wavelet Denoise

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/express/waveletdenoisesource-llb/waveletdenoise-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/express/waveletdenoisesource-llb/waveletdenoise-source-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs noise reduction for 1D signals by using the discrete wavelet transform (DWT) or undecimated wavelet transform (UWT). icon Dialog Box Options Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard

### Wavelet Denoise

Performs noise reduction for 1D signals by using the discrete wavelet transform (DWT) or undecimated wavelet transform (UWT).

[IMAGE alt='icon' src='waveletdenoise-source-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Signal — Specifies the block diagram terminal of the signal you want to load. This input is available only if you select the From terminal option in the Data Source section. real signal — Specifies the input signal. The signal can be a waveform, a real array, or a complex array. File path — Specifies the file path of the data you want to load. This input is available only when you select the From file option in the Data Source section. complex signal — Specifies the input signal. The signal can be a waveform, a real array, or a complex array. Denoised Signal — Returns the estimated signal after denoising. error out — error out contains error information. This output provides standard error out functionality. real denoised — Contains the estimated signal after de-noising. complex denoised — Contains the estimated signal after de-noising. |
| --- |

#### Examples

Refer to the Noise Reduction VI in the labview\examples\Wavelet Analysis\WAApplications directory for an example of using the Wavelet Denoise VI.

Parent topic:

Feature Extraction

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-array-vi.html language=enus -->
## TOPIC 00091: WA 1D Synthesis Filter Bank (Array) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-array-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband (approx coef) and the high-frequency subband (detail coef). Wire data to the approx coef or the DWT coef input to dete

### WA 1D Synthesis Filter Bank (Array) VI

Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband (**approx coef**) and the high-frequency subband (**detail coef**). Wire data to the **approx coef** or the **DWT coef** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-1d-synthesis-filter-bank-array-vi.png']

#### Inputs/Outputs

| approx coef — approx coef specifies the approximation coefficients. detail coef — detail coef specifies the detail coefficients. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. synthesis filters — synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters. You can use the WA Wavelet Filter VI to obtain the filters of commonly used wavelets. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. shift — shift specifies how many zeros to pad at the beginning of the approximation coefficients and the detail coefficients before interpolation filtering. shift must be the same value as the value you used in the WA Analysis Filter Bank VI to compute approx coef and detail coef or DWT coef. signal — signal returns the reconstructed signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |

#### Examples

Refer to the following VIs for examples of using the WA Synthesis Filter Bank VI:

- Filter Banks - 1D VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Filter Banks - 2D VI: labview\examples\Wavelet Analysis\WAGettingStarted

Parent topic:

WA Synthesis Filter Bank VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-waveform-vi.html language=enus -->
## TOPIC 00092: WA 1D Synthesis Filter Bank (Waveform) VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-waveform-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband (approx coef) and the high-frequency subband (detail coef). Wire data to the approx coef or the DWT coef input to dete

### WA 1D Synthesis Filter Bank (Waveform) VI

Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband (**approx coef**) and the high-frequency subband (**detail coef**). Wire data to the **approx coef** or the **DWT coef** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-1d-synthesis-filter-bank-waveform-vi.png']

#### Inputs/Outputs

| approx coef — approx coef specifies the approximation coefficients. detail coef — detail coef specifies the detail coefficients. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. synthesis filters — synthesis filters specifies the coefficients of the lowpass synthesis filters and the highpass synthesis filters. You can use the WA Wavelet Filter VI to obtain the filters of commonly used wavelets. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. shift — shift specifies how many zeros to pad at the beginning of the approximation coefficients and the detail coefficients before interpolation filtering. shift must be the same value as the value you used in the WA Analysis Filter Bank VI to compute approx coef and detail coef or DWT coef. signal — signal returns the reconstructed signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| lowpass — lowpass specifies the coefficients of the lowpass synthesis filter, which this VI uses to filter the interpolated approximation coefficients in the wavelet reconstruction. highpass — highpass specifies the coefficients of the highpass synthesis filter, which this VI uses to filter the interpolated detail coefficients in the wavelet reconstruction. |

#### Examples

Refer to the following VIs for examples of using the WA Synthesis Filter Bank VI:

- Filter Banks - 1D VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Filter Banks - 2D VI: labview\examples\Wavelet Analysis\WAGettingStarted

Parent topic:

WA Synthesis Filter Bank VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-2d-analysis-filter-bank-vi.html language=enus -->
## TOPIC 00093: WA 2D Analysis Filter Bank VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-2d-analysis-filter-bank-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-2d-analysis-filter-bank-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-level discrete wavelet transform (DWT) using a two-channel analysis filter bank. This VI decomposes the signal into the low-frequency subband (approx coef) and the high-frequency subband (detail coef). Both subbands have half the sampling rate of signal. Wire data to the signal i

### WA 2D Analysis Filter Bank VI

Computes the single-level discrete wavelet transform (DWT) using a two-channel analysis filter bank. This VI decomposes the signal into the low-frequency subband (**approx coef**) and the high-frequency subband (**detail coef**). Both subbands have half the sampling rate of **signal**. Wire data to the **signal** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-2d-analysis-filter-bank-vi.png']

#### Inputs/Outputs

| extension — extension specifies the method to use to pad data at the borders of the input signal. The extension length is equal to the length of the wavelet filters. When you select the extension method, make the transition between the input signal and the padded data as smooth as possible because a smooth transition generates fewer large detail coefficients and enhances the efficiency of the signal representation. signal — signal specifies the 2D input signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. analysis filters — analysis filters specifies the coefficients of the lowpass analysis filters and the highpass analysis filters. You can use the WA Wavelet Filter VI to obtain the filters of commonly used wavelets. You can use the Wavelet Design Express VI to design the analysis filters and the corresponding synthesis filters. lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. shift — shift specifies the index where decimation starts after this VI filters the signal. shift must be 0 or 1. DWT coef — DWT coef returns the approximation coefficients and the detail coefficients from the 2D single-level discrete wavelet transform (DWT). low_low — low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| lowpass — lowpass specifies the coefficients of the lowpass analysis filter, which this VI uses to compute the approximation coefficients. highpass — highpass specifies the coefficients of the highpass analysis filter, which this VI uses to compute the detail coefficients. |
| low_low — low_low returns the approximation coefficients from the lowpass analysis filtering on each row and each column. The low_low coefficients are a low-resolution approximation of the original 2D signal. low_high — low_high returns the detail coefficients from the lowpass analysis filtering on each row and the highpass analysis filtering on each column. The high-frequency signal along the column direction influences the low_high coefficients. high_low — high_low returns the detail coefficients from the highpass analysis filtering on each row and the lowpass analysis filtering on each column. The high-frequency signal along the row direction influences the high_low coefficients. high_high — high_high returns the detail coefficients from the highpass analysis filtering on each row and each column. The high-frequency signal along the diagonal direction influences the high_high coefficients. |

#### Examples

Refer to the following VIs for examples of using the WA Analysis Filter Bank VI:

- Filter Banks - 1D VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Filter Banks - 2D VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Wavelet Order Selection VI: labview\examples\Wavelet Analysis\WAGettingStarted

Parent topic:

WA Analysis Filter Bank VI

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-synthesis-filter-bank-vi.html language=enus -->
## TOPIC 00094: WA Synthesis Filter Bank VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-synthesis-filter-bank-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-synthesis-filter-bank-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband (approx coef) and the high-frequency subband (detail coef). Wire data to the approx coef or the DWT coef input to dete

### WA Synthesis Filter Bank VI

Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband (**approx coef**) and the high-frequency subband (**detail coef**). Wire data to the **approx coef** or the **DWT coef** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-synthesis-filter-bank-vi.png']

#### Examples

Refer to the following VIs for examples of using the WA Synthesis Filter Bank VI:

- Filter Banks - 1D VI: labview\examples\Wavelet Analysis\WAGettingStarted
- Filter Banks - 2D VI: labview\examples\Wavelet Analysis\WAGettingStarted

- [WA 1D Synthesis Filter Bank (Waveform) VI](../../../../vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-waveform-vi.html) Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband ( approx coef ) and the high-frequency subband ( detail coef ). Wire data to the approx coef or the DWT coef input to determine the polymorphic instance to use or manually select the instance.
- [WA 1D Synthesis Filter Bank (Array) VI](../../../../vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-1d-synthesis-filter-bank-array-vi.html) Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband ( approx coef ) and the high-frequency subband ( detail coef ). Wire data to the approx coef or the DWT coef input to determine the polymorphic instance to use or manually select the instance.
- [WA 2D Synthesis Filter Bank VI](../../../../vi-lib/addons/wavelet-analysis/filter-banks-llb/wa-2d-synthesis-filter-bank-vi.html) Computes the single-level inverse discrete wavelet transform (DWT) using a two-channel synthesis filter bank. This VI reconstructs the original signal with the low-frequency subband ( approx coef ) and the high-frequency subband ( detail coef ). Wire data to the approx coef or the DWT coef input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Filter Banks

<!--NI_TOPIC bundle=lvaspt-api-ref path=vi-lib/addons/wavelet-analysis/misc-llb/wa-configure-scalogram-indicator-vi.html language=enus -->
## TOPIC 00095: WA Configure Scalogram Indicator VI

- bundle_id: `lvaspt-api-ref`
- source_path: `vi-lib/addons/wavelet-analysis/misc-llb/wa-configure-scalogram-indicator-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvaspt-api-ref/raw/resource/enus/vi-lib/addons/wavelet-analysis/misc-llb/wa-configure-scalogram-indicator-vi.html
- document_id: `lvaspt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays the square magnitude or the phase of the wavelet coefficients on an intensity graph. This VI displays the square magnitude of the real-valued wavelet coefficients from the WA Continuous Wavelet Transform VI and displays the square magnitude or the phase of the complex-valued wavelet coeffic

### WA Configure Scalogram Indicator VI

Displays the square magnitude or the phase of the wavelet coefficients on an intensity graph. This VI displays the square magnitude of the real-valued wavelet coefficients from the WA Continuous Wavelet Transform VI and displays the square magnitude or the phase of the complex-valued wavelet coefficients from the WA Analytic Wavelet Transform VI. Wire data to the **CWT coef** input or the **AWT coef** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='wa-configure-scalogram-indicator-vi.png']

#### Examples

Refer to the Color Tables for Displaying the Scalogram VI in the labview\examples\Wavelet Analysis\WAGettingStarted directory for an example of using the WA Configure Scalogram Indicator VI.

- [WA Configure Scalogram Indicator (Predefined Color Table, Real) VI](../../../../vi-lib/addons/wavelet-analysis/misc-llb/wa-configure-scalogram-indicator-predefined-color-table-real-vi.html) Displays the square magnitude or the phase of the wavelet coefficients on an intensity graph. This VI displays the square magnitude of the real-valued wavelet coefficients from the WA Continuous Wavelet Transform VI and displays the square magnitude or the phase of the complex-valued wavelet coefficients from the WA Analytic Wavelet Transform VI. Wire data to the CWT coef input or the AWT coef input to determine the polymorphic instance to use or manually select the instance.
- [WA Configure Scalogram Indicator (Predefined Color Table, Complex) VI](../../../../vi-lib/addons/wavelet-analysis/misc-llb/wa-configure-scalogram-indicator-predefined-color-table-complex-vi.html) Displays the square magnitude or the phase of the wavelet coefficients on an intensity graph. This VI displays the square magnitude of the real-valued wavelet coefficients from the WA Continuous Wavelet Transform VI and displays the square magnitude or the phase of the complex-valued wavelet coefficients from the WA Analytic Wavelet Transform VI. Wire data to the CWT coef input or the AWT coef input to determine the polymorphic instance to use or manually select the instance.
- [WA Configure Scalogram Indicator (Customized Color Table, Real) VI](../../../../vi-lib/addons/wavelet-analysis/misc-llb/wa-configure-scalogram-indicator-customized-color-table-real-vi.html) Displays the square magnitude or the phase of the wavelet coefficients on an intensity graph. This VI displays the square magnitude of the real-valued wavelet coefficients from the WA Continuous Wavelet Transform VI and displays the square magnitude or the phase of the complex-valued wavelet coefficients from the WA Analytic Wavelet Transform VI. Wire data to the CWT coef input or the AWT coef input to determine the polymorphic instance to use or manually select the instance.
- [WA Configure Scalogram Indicator (Customized Color Table, Complex) VI](../../../../vi-lib/addons/wavelet-analysis/misc-llb/wa-configure-scalogram-indicator-customized-color-table-complex-vi.html) Displays the square magnitude or the phase of the wavelet coefficients on an intensity graph. This VI displays the square magnitude of the real-valued wavelet coefficients from the WA Continuous Wavelet Transform VI and displays the square magnitude or the phase of the complex-valued wavelet coefficients from the WA Analytic Wavelet Transform VI. Wire data to the CWT coef input or the AWT coef input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Utilities
