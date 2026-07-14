# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5001 ordinal=5001 -->
## Functions

Functions

MedianMedian FilterFilter PtByPtPtByPt

Applies a median filter of rank to x.

This VI is similar to the Median Filter VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is the input signal to filter.

   •      rank —

    rank is the number of elements used to compute the median. rank must be greater than or
    equal to 0. The default is 2.

       If rank is less than 0, this VI sets Filtered x to 0 and returns an error. If rank is 0, this VI does not
    apply a median filter to x.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 5001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5002 ordinal=5002 -->
## Functions

Functions

       FIRFIR FilterFilter PtByPtPtByPt

        Filters x using the FIR filter specified by Forward Coefficients.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is the input signal to filter.

               •      Forward Coefficients —

           Forward Coefficients is the IIR filter specification.

               •       Filtered x —

             Filtered x contains the result of filtering the input sequence x by convolution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If Y represents the set of Filtered x, the elements of Y are obtained using


      where xi–j is an array of input data and bj is the Forward Coefficients array.


5002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5003 ordinal=5003 -->
## Functions

Functions

IIRIIR FilterFilter PtByPtPtByPt

Filters x using the direct form IIR filter specified by Reverse Coefficients and Forward
Coefficients.

This VI is similar to the IIR Filter VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is the input signal to filter.

   •      Reverse Coefficients —

    Reverse Coefficients is the reverse coefficients of the filter design.

    This VI does not place any restrictions on the coefficient arrays. If both coefficient arrays are
    empty, the VI performs no filtering and sets Filtered X to the value of X.

   •      Forward Coefficients —

    Forward Coefficients is the forward coefficients of the filter design.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —


                                                    © National Instruments 5003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5004 ordinal=5004 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The IIR Filter PtByPt VI obtains the elements of Filtered X using the following equation.


                                                         ,

      where Yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
       Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.

           Note You can use the IIR Filter PtByPt VI to perform FIR filtering by passing
            an empty array into Reverse Coefficients.

        IIRIIR FilterFilter withwith I.C.I.C. PtByPtPtByPt

        Filters x using the IIR filter specified by Reverse Coefficients and Forward Coefficients.

       This VI is similar to the IIR Filter with I.C. VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

5004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5005 ordinal=5005 -->
## Functions

Functions


  x is the input signal to filter.

•      Reverse Coefficients —

  Reverse Coefficients is the reverse coefficients of the filter design.

  This VI does not place any restrictions on the coefficient arrays. If both coefficient arrays are
  empty, the VI performs no filtering and sets Filtered X to the value of X.

•      Forward Coefficients —

  Forward Coefficients is the forward coefficients of the filter design.

•        Initial X Conditions —

   Initial X Conditions contains the most recent inputs.

  The most recent prior input should be the last element in the array. The number of elements in
   this array should be one less than the number of elements in the Forward Coefficients array.

•        Initial Y Conditions —

   Initial Y Conditions contains the most recent outputs.

  The most recent output should be the last element in the array. The number of elements in this
  array should be one less than the number of elements in the Reverse Coefficients array.

•       Filtered x —

  Filtered x contains the result of filtering the input sequence x by convolution.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
  Code VI to convert the error code or warning into an error cluster.

•       Final X Conditions —

  Final X Conditions contains the most recent inputs. You can use Final X Conditions as Initial X
  Conditions on the next call to this VI.

•       Final Y Conditions —

  Final Y Conditions contains the most recent outputs. You can use Final Y Conditions as Initial Y


                                                   © National Instruments 5005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5006 ordinal=5006 -->
## Functions

Functions


            Conditions on the next call to this VI.


      The IIR Filter with I.C. PtByPt VI obtains the elements of Filtered X using the following
       equation.


      where yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
       Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.

      The filter initialization uses the following equations.

        y[i] = yic[Na + i– 1] for i< 0 x[i] = xic[Nb + i– 1] for i< 0

      where yic is the array of Initial Y Conditions and xic is the array of Initial X Conditions.

           Note You can use the IIR Filter PtByPt VI to perform FIR filtering by passing
            an empty array into Reverse Coefficients or by leaving Reverse Coefficients
              unwired.

        IIRIIR CascadeCascade FilterFilter PtByPtPtByPt

        Filters x using the cascade form of the IIR filter specified by the IIR Filter Cluster.

       This VI is similar to the IIR Cascade Filter VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5007 ordinal=5007 -->
## Functions

Functions

Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is the input signal to filter.

   •       IIR Filter Cluster —

     IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

    This cluster is the output from one of the IIR coefficient design VIs: Butterworth Coefficients,
    Bessel Coefficients, Chebyshev Coefficients, Elliptic Coefficients, or Inv Chebyshev Coefficients.

         •        filter structure —

           filter structure selects IIR second-order or fourth-order filter stages.

        0        IIR 2nd Order
        1        IIR 4th Order

         •      Reverse Coefficients —

        Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

         •      Forward Coefficients —

       Forward Coefficients is the forward coefficients of the IIR cascade filter.


   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 5007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5008 ordinal=5008 -->
## Functions

Functions

        IIRIIR CascadeCascade FilterFilter withwith I.C.I.C. PtByPtPtByPt

        Filters x using the cascade form of the IIR filter specified by the IIR Filter Cluster.

       This VI is similar to the IIR Cascade Filter with I.C. VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is the input signal to filter.

               •       IIR Filter Cluster —

              IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

             This cluster is the output from one of the IIR coefficient design VIs: Butterworth Coefficients,
            Bessel Coefficients, Chebyshev Coefficients, Elliptic Coefficients, or Inv Chebyshev Coefficients.

                     •        filter structure —

                     filter structure selects IIR second-order or fourth-order filter stages.

               0        IIR 2nd Order
               1        IIR 4th Order

                     •      Reverse Coefficients —


5008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5009 ordinal=5009 -->
## Functions

Functions


        Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

         •      Forward Coefficients —

       Forward Coefficients is the forward coefficients of the IIR cascade filter.


   •        Initial Condition —

     Initial Condition contains the initial internal filter state. The Initial Condition array should be
    the same size as the Reverse Coefficients array in the IIR Filter Cluster.

       If this array is not the correct size, such as if the array is empty, the array resizes internally and
     initializes to zero before the IIR filtering operation.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       Final Condition —

    Final Condition contains the final, internal filter states, which Initial Condition can pass to the
    next call to the IIR Cascade Filter with I.C. PtByPt VI to filter samples continuously.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


SavitzkySavitzky GolayGolay FilterFilter PtByPtPtByPt

Performs fitting based on a polynomial of a given order and then smooths the curve
instead of returning raw data.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 5009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5010 ordinal=5010 -->
## Functions

Functions


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •       side points —

            side points specifies the number of data points to each side of the current data point to use for
            the least squares minimization.

            side points*2 + 1 is the length of the moving window, which must be greater than the order
            polynomial. This number determines the amount of data used to fit the curve. For example, the
             default value 6 for side points generates a history length 2*(6) + 1, or 13. The VI uses 13 points to
                   fit the curve.

               •      order polynomial —

            order polynomial specifies the order of the polynomial. The default is 3.

              In the case of the Savitzky Golay Filter PtByPt VI, the order is a polynomial. For example, when
           you set order polynomial to 2, the VI uses quadratic fitting.

               •       Filtered x —

             Filtered x is the fitted and smoothed data point.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      You can use the Savitzky Golay Filter PtByPt VI in real-time operation.


5010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5011 ordinal=5011 -->
## Functions

Functions

SpectralSpectral AnalysisAnalysis PtByPtPtByPt

Use the Spectral Analysis PtByPt VIs to implement common transforms used in
mathematics and signal processing.

The VIs on this palette can return point by point error codes.


 Palette Object      Description

 Auto Power       Computes the single-sided, scaled, auto power spectrum of a time-domain
 Spectrum PtByPt    signal.


 Power Spectrum   Computes the Power Spectrum, Sxx, of the set of input data points specified
 PtByPt            by sample length.


 Amplitude and
                 Computes the single-sided, scaled amplitude spectrum of a real-valued time- Phase Spectrum                 domain signal and returns the amplitude spectrum as magnitude and phase. PtByPt


 Cross Power       Computes the single-sided, scaled, cross power spectrum of two real-time
 Spectrum PtByPt    signals.


 Cross Power       Computes the cross power spectrum, Sxy, of the set of input data points
 PtByPt              specified by sample length.


 STFT Spectrogram  Computes the signal energy distribution in the joint time-frequency domain
 PtByPt             using the short-time Fourier transform (STFT) algorithm.


 WVD Spectrogram  Computes the signal energy distribution in the joint time-frequency domain
 PtByPt             using the Wigner-Ville distribution algorithm.


                                                    © National Instruments 5011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5012 ordinal=5012 -->
## Functions

Functions


         Palette Object      Description

       Buneman                            Estimates the frequency of a given sine wave of unknown frequency using the
        Frequency                      Buneman formula.         Estimator PtByPt

      AutoAuto PowerPower SpectrumSpectrum PtByPtPtByPt

      Computes the single-sided, scaled, auto power spectrum of a time-domain signal.

       This VI is similar to the Auto Power Spectrum VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •       signal —

             signal specifies the input time-domain signal, usually in volts.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •      dt —

            dt is the sample period of the time-domain signal, usually in seconds.


5012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5013 ordinal=5013 -->
## Functions

Functions


    Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal. The default is 1.

   •     Power Spectrum (V^2 rms) —

   Power Spectrum returns the single-sided power spectrum.

       If the input Signal is in volts (V), Power Spectrum has units of volts-rms squared (Vrms²). If the
    input Signal is not in volts, Power Spectrum has units of the input signal unit-rms squared.

   •       df —

    df is the frequency interval of the power spectrum in hertz, if dt is in seconds.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


PowerPower SpectrumSpectrum PtByPtPtByPt

Computes the Power Spectrum, Sxx, of the set of input data points specified by
sample length.

This VI is similar to the Power Spectrum VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —


                                                    © National Instruments 5013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5014 ordinal=5014 -->
## Functions

Functions


           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •     Power Spectrum —

          Power Spectrum returns the double-sided power spectrum of x.

                    If the set of input data points that sample length specifies is in volts (V), Power Spectrum has
             units of volts-rms squared (Vrms²). If the input signal is not in volts, Power Spectrum has units of
            the input signal unit-rms squared.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      AmplitudeAmplitude andand PhasePhase SpectrumSpectrum PtByPtPtByPt

      Computes the single-sided, scaled amplitude spectrum of a real-valued time-domain
       signal and returns the amplitude spectrum as magnitude and phase.

       This VI is similar to the Amplitude and Phase Spectrum VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5015 ordinal=5015 -->
## Functions

Functions

Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •       signal —

    signal specifies the input time-domain signal, usually in volts.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.

    sample length must be greater than 0.

   •      dt —

    dt is the sample period of the time-domain signal, usually in seconds.

    Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal. The default is 1.

   •     unwrap phase (T) —

   unwrap phase, when TRUE, enables phase unwrapping on the output Amp Spectrum Phase.
    The default is TRUE.

       If unwrap phase is FALSE, this VI does not unwrap the output phase.

   •    Amp Spectrum Mag (Vrms) —

   Amp Spectrum Mag returns the magnitude of the single-sided power spectrum.

       If the input signal is in volts (V), Amp Spectrum Mag has units of volts-rms (Vrms). If the input
    signal is not in volts, Amp Spectrum Mag has units of the input signal unit-rms.

   •    Amp Spectrum Phase (radians) —

   Amp Spectrum Phase is the single-sided amplitude spectrum phase in radians.

   •       df —

    df is the frequency interval of the power spectrum in hertz, if dt is in seconds.


                                                    © National Instruments 5015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5016 ordinal=5016 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      CrossCross PowerPower SpectrumSpectrum PtByPtPtByPt

      Computes the single-sided, scaled, cross power spectrum of two real-time signals.

       This VI is similar to the Cross Power Spectrum VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •       signal x —

             signal x is the input, time-domain signal x, usually in volts.

               •       signal y —

             signal y is the input, time-domain signal y, usually in volts.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •      dt —

5016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5017 ordinal=5017 -->
## Functions

Functions


    dt is the sample period of the time-domain signal, usually in seconds.

    Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal. The default is 1.

   •      Cross Power XY Spectrum Mag (V^2rms) —

    Cross Power XY Spectrum Mag is the single-sided cross power spectrum between signals X and
      Y.

       If the input signals are in volts (V), Cross Power XY Spectrum Mag has units of volts-rms squared
     (Vrms²). If the input signals are not in volts, Cross Power XY Spectrum Mag has units of the input
     signal unit-rms squared.

   •      Cross Power XY Spectrum Phase (radians) —

    Cross Power XY Spectrum Phase is the phase spectrum in radians showing the difference
    between the phases of signal Y and signal X.

   •       df —

    df is the frequency interval of the power spectrum in hertz, if dt is in seconds.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The cross power spectrum gives the product of the amplitude of the signals x and y
and the difference between their phases, phase of signal y minus phase of signal x.

CrossCross PowerPower PtByPtPtByPt

Computes the cross power spectrum, Sxy, of the set of input data points specified by
sample length.

This VI is similar to the Cross Power VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 5017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5018 ordinal=5018 -->
## Functions

Functions


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •      y —

           y is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •      Sxy —

           Sxy is the cross power spectrum of the set of input data points specified by sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     STFTSTFT SpectrogramSpectrogram PtByPtPtByPt

      Computes the signal energy distribution in the joint time-frequency domain using the
       short-time Fourier transform (STFT) algorithm.

       This VI performs a sliding FFT. This VI is similar to the STFT Spectrograms VI.


5018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5019 ordinal=5019 -->
## Functions

Functions

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is the time waveform.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.

    sample length must be greater than 0.

   •      time increment —

    time increment is the number of samples needed to shift the sliding window. The default is 1.

   When you increase time increment, you decrease computation time and reduce memory
    requirements, but you reduce time-domain resolution. When you decrease time increment, you
    improve time-domain resolution, but you increase computation time and memory
    requirements.

   •     window length —

   window length is the actual length of the selected window. The default is 50.

      It corresponds to the number of samples used in calculating the Fourier transform.

   •     window selector —


                                                    © National Instruments 5019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5020 ordinal=5020 -->
## Functions

Functions


          window selector determines the type of analysis window the VI uses to compute the
            spectrogram.

           0    Hanning (default)
           1    Hamming
           2    Blackman
           3     Exact Blackman
           4    Blackman Harris

               •     STFT Spectrogram {X} —

          STFT Spectrogram {X} is a 2D array that describes the time waveform energy distribution in the
              joint time-frequency domain.

          The number of rows, time axis, in STFT Spectrogram {X} is equal to the number of elements in
            the time waveform divided by time increment and then rounded up. The number of columns,
            frequency axis, in STFT Spectrogram {X} is equal to (window length/2) + 1.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Point by Point\Moving
        STFT PtByPt.vi

    WVDWVD SpectrogramSpectrogram PtByPtPtByPt

      Computes the signal energy distribution in the joint time-frequency domain using the
       Wigner-Ville distribution algorithm.

       This VI is similar to the WVD Spectrogram VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.

5020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5021 ordinal=5021 -->
## Functions

Functions


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.

    sample length must be greater than 0.

   •      time increment —

    time increment controls the time intervals of the Wigner-Ville Distribution. You express time
    increment in units of samples. The default is 1.

    For example, if you sample the time waveform at fsHz, the spacing between the rows of WVD
    Spectrogram {X} is time increment/fsseconds.

    Increasing time increment decreases the computation time and reduces memory requirements
    but also reduces time-domain resolution. Decreasing time increment improves time-domain
    resolution but increases the computation time and memory requirements.

   •    WVD Spectrogram {X} —

   WVD Spectrogram {X} is a 2D array that describes the energy distribution of x in the joint time-
    frequency domain.

    The number of rows, time axis, in WVD Spectrogram {X} is equal to the number of elements in
    the time waveform divided by time increment and then rounded up.

   •       error —


                                                    © National Instruments 5021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5022 ordinal=5022 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     BunemanBuneman FrequencyFrequency EstimatorEstimator PtByPtPtByPt

       Estimates the frequency of a given sine wave of unknown frequency using the
     Buneman formula.

       This VI is similar to the Buneman Frequency Estimator VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is the sampled signal.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •      beta —

           beta is the estimation of the frequency of the sine wave that x represents. beta is the index of the
         maximum frequency and can be a noninteger.


5022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5023 ordinal=5023 -->
## Functions

Functions


    The following equation describes the actual frequency: beta * df = beta * fs/number of samples

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

TransformsTransforms PtByPtPtByPt

Use the Transforms PtByPt VIs to compute transforms.

The VIs on this palette can return point by point error codes.


 Palette Object  Description

             Computes the Fourier transform of x. This VI is similar to the FFT VI. Wire data to
 FFT PtByPt     the x input to determine the polymorphic instance to use or manually select the
                 instance.


 Fast Hilbert
             Computes the fast Hilbert transform of the set of input data points specified by Transform              sample length using fast Fourier transform (FFT) identities. PtByPt


             Computes the fast Hartley transform (FHT) of the set of input data points specified
 FHT PtByPt
              by sample length.

 Walsh
 Hadamard     Performs the real Walsh Hadamard transform.
 PtByPt

 Wavelet
 Transform
               Performs the wavelet transform based on the Daubechies4 function.
 Daubechies4
 PtByPt


                                                    © National Instruments 5023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5024 ordinal=5024 -->
## Functions

Functions


         Palette Object  Description

       Windowed    Computes the windowed fast Fourier transform of the set of input data points
        FFT PtByPt     specified by sample length.


                    Computes the inverse discrete Fourier transform (IDFT) of the set of input data
         Inverse FFT     points specified by sample length. This VI is similar to the Inverse FFT VI. Wire data
        PtByPt         to the x input to determine the polymorphic instance to use or manually select the
                          instance.

         Inverse Fast
          Hilbert       Computes the inverse fast Hilbert transform of the set of input data points
        Transform      specified by sample length using Fourier transform identities.
        PtByPt

         Inverse FHT   Computes the inverse fast Hartley transform of the set of input data points
        PtByPt         specified by sample length.

        Walsh
       Hadamard     Performs the inverse of the real Walsh Hadamard transform.
         Inverse PtByPt

        Wavelet
        Transform                       Performs the inverse of the wavelet transform based on the Daubechies4 function.        Daubechies4
         Inverse PtByPt

         Transfer      Computes the single-sided transfer function, also known as the frequency
         Function       response, from the time-domain Stimulus Signal and Response Signal from a
        PtByPt        network under test.

        Impulse
        Response     Computes the impulse response of a network based on the set of real signals x,
         Function       stimulus signal x, and y, response signal y.
        PtByPt

      FFTFFT PtByPtPtByPt

      Computes the Fourier transform of x. This VI is similar to the FFT VI. Wire data to the x

5024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5025 ordinal=5025 -->
## Functions

Functions

input to determine the polymorphic instance to use or manually select the instance.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


  • Real FFT PtByPt VI
  • Complex FFT PtByPt VI
RealReal FFTFFT PtByPtPtByPt VIVI

Computes the Fourier transform of x. This VI is similar to the FFT VI. Wire data to the x
input to determine the polymorphic instance to use or manually select the instance.

This VI is similar to the Real FFT instance of the FFT VI.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.

    sample length must be greater than 0.

   •      FFT{X} —

                                                    © National Instruments 5025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5026 ordinal=5026 -->
## Functions

Functions


            FFT{X} is the real FFT of the set of input data points specified by sample length.

                    If the input signal is in volts (V), FFT {X} has units of volts. If the input signal is not in volts, FFT {X}
           has units of the input signal unit. This VI returns the phase in radians.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   ComplexComplex FFTFFT PtByPtPtByPt VIVI

      Computes the Fourier transform of x. This VI is similar to the FFT VI. Wire data to the x
       input to determine the polymorphic instance to use or manually select the instance.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is a complex-valued data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.


5026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5027 ordinal=5027 -->
## Functions

Functions

   •      FFT{X} —

    FFT{X} is the complex FFT of the set of input data points specified by sample length.

       If the input signal is in volts (V), FFT {X} has units of volts. If the input signal is not in volts, FFT {X}
    has units of the input signal unit. This VI returns the phase in radians.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


FastFast HilbertHilbert TransformTransform PtByPtPtByPt

Computes the fast Hilbert transform of the set of input data points specified by sample
length using fast Fourier transform (FFT) identities.

This VI is similar to the Fast Hilbert Transform VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.


                                                    © National Instruments 5027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5028 ordinal=5028 -->
## Functions

Functions


           sample length must be greater than 0.

               •       Hilbert{X} —

             Hilbert{X} is the fast Hilbert transform of the set of input data points specified by sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let h(t) be the Hilbert transform of x(t) and let


      be the Fourier transform pairs, then H(f) can be written in terms of X(f) as

        H(f) = –j sgn(f) X(f),

      where

        sgn(f) = 1 for f > 0 sgn(f) = –1 for f < 0.
     FHTFHT PtByPtPtByPt

      Computes the fast Hartley transform (FHT) of the set of input data points specified by
      sample length.

       This VI is similar to the FHT VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5029 ordinal=5029 -->
## Functions

Functions

Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.

    sample length must be greater than 0.

   •       Hartley{X} —

    Hartley{X} is the Hartley transform of the set of input data points specified by sample length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


WalshWalsh HadamardHadamard PtByPtPtByPt

Performs the real Walsh Hadamard transform.

This VI is similar to the Walsh Hadamard VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 5029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5030 ordinal=5030 -->
## Functions

Functions

      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 128.

           sample length must be greater than zero and a power of 2.

               •      Walsh Hadamard {X} —

           Walsh Hadamard {X} returns the Walsh Hadamard transform of the set of input data points
             specified by sample length.

              In the case of an error, the VI returns an empty array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      WaveletWavelet TransformTransform Daubechies4Daubechies4 PtByPtPtByPt

      Performs the wavelet transform based on the Daubechies4 function.

       This VI is similar to the Wavelet Transform Daubechies4 VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5031 ordinal=5031 -->
## Functions

Functions

Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 128.

    sample length must be greater than zero and a power of 2.

   •      Wavelet Daubechies4 {X} —

    Wavelet Daubechies4 {X} returns the calculated wavelet Daubechies4 transform of the set of
    input data points specified by sample length.

     In the case of an error, the VI returns an empty array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


WindowedWindowed FFTFFT PtByPtPtByPt

Computes the windowed fast Fourier transform of the set of input data points
specified by sample length.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 5031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5032 ordinal=5032 -->
## Functions

Functions

      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •     window selector —

          window selector determines the type of analysis window the VI uses to compute the windowed
             FFT.

           0     Hanning
           1    Hamming
           2     Blackman
           3     Exact Blackman
           4     Blackman Harris

               •     Windowed FFT —

          Windowed FFT is the Windowed fast Fourier transform of the set of input data points specified
           by sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       InverseInverse FFTFFT PtByPtPtByPt

      Computes the inverse discrete Fourier transform (IDFT) of the set of input data points
       specified by sample length. This VI is similar to the Inverse FFT VI. Wire data to the x

5032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5033 ordinal=5033 -->
## Functions

Functions

input to determine the polymorphic instance to use or manually select the instance.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


  • Inverse Real FFT PtByPt VI
  • Inverse Complex FFT PtByPt VI
InverseInverse RealReal FFTFFT PtByPtPtByPt VIVI

Computes the inverse discrete Fourier transform (IDFT) of the set of input data points
specified by sample length. This VI is similar to the Inverse FFT VI. Wire data to the x
input to determine the polymorphic instance to use or manually select the instance.

This VI is similar to the Inverse Real FFT instance of the Inverse FFT VI.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is a complex-valued data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.


                                                    © National Instruments 5033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5034 ordinal=5034 -->
## Functions

Functions


           sample length must be greater than 0.

               •      Inverse FFT{X} —

            Inverse FFT{X} is the inverse real FFT of the set of input data points specified by sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

    InverseInverse ComplexComplex FFTFFT PtByPtPtByPt VIVI

      Computes the inverse discrete Fourier transform (IDFT) of the set of input data points
       specified by sample length. This VI is similar to the Inverse FFT VI. Wire data to the x
       input to determine the polymorphic instance to use or manually select the instance.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is a complex-valued data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.


5034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5035 ordinal=5035 -->
## Functions

Functions


    sample length must be greater than 0.

   •      Inverse Complex FFT{X} —

    Inverse Complex FFT{X} is the inverse complex FFT of the set of input data points specified by
    sample length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


InverseInverse FastFast HilbertHilbert TransformTransform PtByPtPtByPt

Computes the inverse fast Hilbert transform of the set of input data points specified by
sample length using Fourier transform identities.

This VI is similar to the Inverse Fast Hilbert Transform VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each


                                                    © National Instruments 5035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5036 ordinal=5036 -->
## Functions

Functions


             set of data. The default is 100.

           sample length must be greater than 0.

               •      Inverse Hilbert{X} —

            Inverse Hilbert{X} is the inverse Hilbert transform of the set of input data points specified by
           sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The inverse Hilbert transform of a function h(t) is defined as


       Using the definition of the Hilbert transform


      you can obtain the inverse Hilbert transform by negating the forward Hilbert transform

         x(t) = H–1{h(t)} = –H{h(t)}

       Therefore, the VI performs the discrete implementation of the inverse Hilbert
       transform with the aid of the Hilbert transform by first performing the Hilbert
       transform of the input sequence X,

      Y = H{X},

      and then negating Y to obtain the inverse Hilbert transform,

       H–1{X} = –Y.

      The Hilbert transform works best with AC coupled, band-limited signals.

5036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5037 ordinal=5037 -->
## Functions

Functions

InverseInverse FHTFHT PtByPtPtByPt

Computes the inverse fast Hartley transform of the set of input data points specified by
sample length.

This VI is similar to the Inverse FHT VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 100.

    sample length must be greater than 0.

   •      Inverse Hartley{X} —

    Inverse Hartley{X} is the inverse Hartley transform of the set of input data points specified by
    sample length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 5037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5038 ordinal=5038 -->
## Functions

Functions

      WalshWalsh HadamardHadamard InverseInverse PtByPtPtByPt

      Performs the inverse of the real Walsh Hadamard transform.

          It is WHI{X}=WH{X}/n, where n is the signal length of X. This VI is similar to the Walsh
      Hadamard Inverse VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 128.

           sample length must be greater than zero and a power of 2.

               •      Walsh Hadamard Inverse {X} —

           Walsh Hadamard Inverse {X} returns the inverse Walsh Hadamard transform of the set of input
            data points specified by sample length.

              In the case of an error, the VI returns an empty array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


5038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5039 ordinal=5039 -->
## Functions

Functions

WaveletWavelet TransformTransform Daubechies4Daubechies4 InverseInverse PtByPtPtByPt

Performs the inverse of the wavelet transform based on the Daubechies4 function.

This VI is similar to the Wavelet Transform Daubechies4 Inverse VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation on each
     set of data. The default is 128.

    sample length must be greater than zero and a power of 2.

   •      Wavelet Daubechies4 Inv {X} —

    Wavelet Daubechies4 Inv {X} returns the calculated inverse wavelet Daubechies4 transform of
    the set of input data points specified by sample length.

     In the case of an error, the VI returns an empty array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 5039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5040 ordinal=5040 -->
## Functions

Functions

       TransferTransfer FunctionFunction PtByPtPtByPt

      Computes the single-sided transfer function, also known as the frequency response,
      from the time-domain Stimulus Signal and Response Signal from a network under
        test.

       This VI is similar to the Frequency Response Function (Mag-Phase) and the Frequency
      Response Function (Real-Im) VIs.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      stimulus signal x —

            stimulus signal x is a time-domain signal, usually the network stimulus.

               •      response signal y —

           response signal y is a time-domain signal, usually the network response.

               •      dt —

            dt is the sample period of the time-domain signal, usually in seconds.

            dt is also 1/ fs, where fs is the sampling frequency of the time-domain signal.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.


5040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5041 ordinal=5041 -->
## Functions

Functions


    sample length must be greater than 0.

   •      Frequency Response Mag (gain) —

    Frequency Response Mag is the single-sided frequency response spectrum of the network.

    This is the amplitude gain of the network.

   •      Frequency Response Phase (radians) —

    Frequency Response Phase is the single-sided phase response spectrum of the network.

    This is the network phase in radians.

   •       df —

    df is the line frequency interval of the frequency response spectra, in hertz, when dt is in
    seconds.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


ImpulseImpulse ResponseResponse FunctionFunction PtByPtPtByPt

Computes the impulse response of a network based on the set of real signals x,
stimulus signal x, and y, response signal y.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —


                                                    © National Instruments 5041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5042 ordinal=5042 -->
## Functions

Functions


               initialize, when TRUE, initializes the internal state of the VI.

               •      stimulus signal x —

            stimulus signal x is a time-domain signal, usually the network stimulus.

               •      response signal y —

           response signal y is a time-domain signal, usually the network response.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •      Impulse Response —

           Impulse Response is the impulse response function versus time. This parameter has no units.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

      LinearLinear AlgebraAlgebra PtByPtPtByPt

      Use the Linear Algebra PtByPt VIs to perform matrix- and vector-related computations
      and analysis.

      The VIs on this palette can return point by point error codes.


         Palette Object                  Description

        Dot Product PtByPt           Computes the dot product, X*Y, of y and x.


5042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5043 ordinal=5043 -->
## Functions

Functions


 Palette Object                  Description

 Outer Product PtByPt          Computes the Outer Product of y and x.


 Complex Dot Product PtByPt    Computes the dot product, X*Y, of the complex values y and x.


 Complex Outer Product PtByPt   Computes the Outer Product of the complex values y and x.


DotDot ProductProduct PtByPtPtByPt

Computes the dot product, X*Y, of y and x.

This VI is similar to the Dot Product VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      y —

    y is an input data point.

   •      x —

    x is an input data point.

   •     sample length —


                                                    © National Instruments 5043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5044 ordinal=5044 -->
## Functions

Functions


           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

         When you set sample length to zero, the VI calculates a cumulative solution for the input data
           from the time that you called or initialized the VI. When the sample length setting is greater than
              zero, the VI calculates the solution for only the newest set of input data.

               •      X*Y —

           X*Y is the dot product.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      OuterOuter ProductProduct PtByPtPtByPt

      Computes the Outer Product of y and x.

       This VI is similar to the Outer Product VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      y —

           y is an input data point.


5044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5045 ordinal=5045 -->
## Functions

Functions

   •     sample length y —

    sample length y is the length of each set of incoming data. The VI performs computation for
    each set of data. The default is 10.

    sample length y must be greater than zero.

   •      x —

    x is an input data point.

   •     sample length x —

    sample length x is the length of each set of incoming data. The VI performs computation for
    each set of data. The default is 10.

    sample length x must be greater than zero.

   •      Outer Product —

    Outer Product is the outer product computed from the input values.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


ComplexComplex DotDot ProductProduct PtByPtPtByPt

Computes the dot product, X*Y, of the complex values y and x.

This VI is similar to the Dot Product VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 5045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5046 ordinal=5046 -->
## Functions

Functions

      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      y —

           y is a complex-valued data point.

               •      x —

           x is a complex-valued data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

         When you set sample length to zero, the VI calculates a cumulative solution for the input data
           from the time that you called or initialized the VI. When the sample length setting is greater than
              zero, the VI calculates the solution for only the newest set of input data.

               •      X*Y —

           X*Y is the dot product.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     ComplexComplex OuterOuter ProductProduct PtByPtPtByPt

      Computes the Outer Product of the complex values y and x.

       This VI is similar to the Outer Product VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5047 ordinal=5047 -->
## Functions

Functions


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      y —

    y is a complex-valued data point.

   •     sample length y —

    sample length y is the length of each set of incoming data. The VI performs computation for
    each set of data. The default is 10.

    sample length y must be greater than zero.

   •      x —

    x is a complex-valued data point.

   •     sample length x —

    sample length x is the length of each set of incoming data. The VI performs computation for
    each set of data. The default is 10.

    sample length x must be greater than zero.

   •      Outer Product —

    Outer Product is the outer product computed from the complex values.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 5047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5048 ordinal=5048 -->
## Functions

Functions

       FittingFitting PtByPtPtByPt

      Use the Fitting PtByPt VIs to fit data to a model and perform interpolation and
       extrapolation.

      The VIs on this palette can return point by point error codes.


         Palette                     Description        Object

                     Finds the line values and the coefficients slope and intercept, using the least-squares
         Linear Fit                       solution, that describe the line that best represents the set of input data points        PtByPt                       specified by sample length.


         Linear Fit
                     Finds the coefficients slope and intercept, using the least-squares solution, which          Coefficients                     describe the line that best represents the set of input data points.        PtByPt


                     Finds the exponential curve values and the exponential coefficients amplitude and         Exponential                   damping, using the least-squares solution, which describe the exponential curve that           Fit PtByPt
                     best represents the input set of data points defined by sample length.


         Exponential
                     Finds the exponential coefficients amplitude and damping, using the least-squares
           Fit
                       solution, which describe the exponential curve that best represents the set of input
          Coefficients
                     data points specified by sample length.
        PtByPt


        General     Finds the polynomial curve values and the set of Polynomial Fit Coefficients which
        Polynomial  describe the polynomial curve that best represents the set of input data points
           Fit PtByPt    specified by sample length.

        General LS
         Linear Fit    Finds the Best Fit k-dimensional plane and the set of linear coefficients for the set of
        PtByPt

5048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5049 ordinal=5049 -->
## Functions

Functions


 Palette             Description
 Object

             input data points specified by sample length.


LinearLinear FitFit PtByPtPtByPt

Finds the line values and the coefficients slope and intercept, using the least-squares
solution, that describe the line that best represents the set of input data points
specified by sample length.

This VI is similar to the Linear Fit VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      y —

    y is an input data point.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each


                                                    © National Instruments 5049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5050 ordinal=5050 -->
## Functions

Functions


             set of data. The default is 100.

         When you set sample length to zero, the VI calculates a cumulative solution for the input data
           from the time that you called or initialized the VI. When the sample length setting is greater than
              zero, the VI calculates the solution for only the newest set of input data.

               •      Best Linear Fit —

            Best Linear Fit returns the y-values of the fitted model.

               •      slope —

            slope returns the slope of the fitted model.

               •       intercept —

             intercept returns the intercept of the fitted model.

               •     mse —

         mse is the mean square error.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The general form of the output is

      F = mX + b,

      where F is the set of output data Best Linear Fit, X is x, m is the slope, b is the
       intercept.

      The MSE between the output Best Linear Fit and y is computed using the MSE PtByPt
        VI and returned in mse, as shown in the following equation.


      where n is the number of elements in the set of input data, f is Best Linear Fit, and y is

5050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5051 ordinal=5051 -->
## Functions

Functions

y.

LinearLinear FitFit CoefficientsCoefficients PtByPtPtByPt

Finds the coefficients slope and intercept, using the least-squares solution, which
describe the line that best represents the set of input data points.

This VI is a subVI of the Linear Fit PtByPt VI. The Linear Fit Coefficients PtByPt VI is
similar to the Linear Fit Coefficients VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      y —

    y is an input data point.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.


                                                    © National Instruments 5051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5052 ordinal=5052 -->
## Functions

Functions

               •      History of x —

            History of x is the set of input data points used to compute slope and intercept.

               •      slope —

            slope returns the slope of the fitted model.

               •       intercept —

             intercept returns the intercept of the fitted model.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      History of y —

            History of y is the set of input data points used to compute slope and intercept.


      ExponentialExponential FitFit PtByPtPtByPt

       Finds the exponential curve values and the exponential coefficients amplitude and
      damping, using the least-squares solution, which describe the exponential curve that
       best represents the input set of data points defined by sample length.

       This VI is similar to the Exponential Fit VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

5052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5053 ordinal=5053 -->
## Functions

Functions


   initialize, when TRUE, initializes the internal state of the VI.

•      y —

  y is an input data point.

•      x —

  x is an input data point.

•     sample length —

  sample length is the length of each set of incoming data. The VI performs computation for each
  set of data. The default is 100.

  When you set sample length to zero, the VI calculates a cumulative solution for the input data
  from the time that you called or initialized the VI. When the sample length setting is greater than
  zero, the VI calculates the solution for only the newest set of input data.

•      Best Exponential Fit —

  Best Exponential Fit returns the y-values of the fitted model.

•      amplitude —

  amplitude is the exponential curve amplitude value that best describes the curve.

        Note You must call this VI at least twice to obtain a valid result for amplitude.

•     damping —

  damping is the exponential curve damping value that best describes the curve.

        Note You must call this VI at least twice to obtain a valid result for damping.

•     mse —

  mse is the mean square error.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                   © National Instruments 5053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5054 ordinal=5054 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


      The general form of the exponential fit is given by

      F = a*exp(d*X),

      where

      F is the set of output data Best Exponential Fit.

      X is x.

      a is amplitude.

      d is damping.

      The mean square error (MSE) between the Best Exponential Fit and the set of input
       data yi is determined using the MSE PtByPt VI and returned in the output mse. mse =
       1/n* sum[f(i)-y(i)]². Here n is the number of elements in the set of input data.

           Note The Exponential Fit PtByPt VI performs an exponential fit even when
              the set of y-values is negative. The Exponential Fit PtByPt VI performs the fit
             under the assumption that the amplitude coefficient is also negative and
               returns a negative amplitude. The set of y-values cannot contain both
                positive and negative elements.

      ExponentialExponential FitFit CoefficientsCoefficients PtByPtPtByPt

       Finds the exponential coefficients amplitude and damping, using the least-squares
       solution, which describe the exponential curve that best represents the set of input
       data points specified by sample length.

       This VI is similar to the Exponential Fit Coefficients VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5055 ordinal=5055 -->
## Functions

Functions


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      y —

    y is an input data point.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.

   •      History of x —

    History of x is the set of x-values and considerations. The size of the array is sample length.

   •      amplitude —

    amplitude is the exponential curve amplitude value that best describes the curve.

          Note You must call this VI at least twice to obtain a valid result for amplitude.

   •     damping —

   damping is the exponential curve damping value that best describes the curve.


                                                    © National Instruments 5055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5056 ordinal=5056 -->
## Functions

Functions


               Note You must call this VI at least twice to obtain a valid result for damping.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      History of y —

            History of y is the set of y-values and considerations. The size of the array is sample length.


           Note The Exponential Fit Coefficients PtByPt VI performs an exponential fit
             even when the set of y-values is negative. The Exponential Fit Coefficients
              PtByPt VI performs the fit under the assumption that the amplitude
                coefficient is also negative and returns a negative amplitude. The set of y-
              values cannot contain a mixture of positive and negative elements.

      GeneralGeneral PolynomialPolynomial FitFit PtByPtPtByPt

       Finds the polynomial curve values and the set of Polynomial Fit Coefficients which
       describe the polynomial curve that best represents the set of input data points
       specified by sample length.

       This VI is similar to the General Polynomial Fit VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

5056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5057 ordinal=5057 -->
## Functions

Functions


   initialize, when TRUE, initializes the internal state of the VI.

•      y —

  y is an input data point.

•      x —

  x is an input data point.

•      polynomial order —

  polynomial order specifies the order of the polynomial to fit to the data set.

  polynomial order must be greater than or equal to zero. If polynomial order is less than zero,
   this VI sets Polynomial Coefficients to an empty array and returns an error. The default is 2.

•      algorithm —

  algorithm specifies the algorithm to use to compute the Best Polynomial Fit.

       SVD
  0         (default)
  1     Givens
  2     Givens2
  3    Householder
  4    LU Decomposition
  5     Cholesky

•     sample length —

  sample length is the length of each set of incoming data. The VI performs computation for each
  set of data. The default is 100.

  sample length must be greater than zero.

•      Best Polynomial Fit —

  Best Polynomial Fit returns the y-values of the polynomial curve that best fits the input values.

•      Polynomial Fit Coefficients —

  Polynomial Fit Coefficients returns the coefficients of the fitted model in ascending order of


                                                   © National Instruments 5057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5058 ordinal=5058 -->
## Functions

Functions


            power. The total number of elements in Polynomial Fit Coefficients is m+ 1, where mis the
            polynomial order.

               •     mse —

         mse is the mean square error.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      GeneralGeneral LSLS LinearLinear FitFit PtByPtPtByPt

       Finds the Best Fit k-dimensional plane and the set of linear coefficients for the set of
       input data points specified by sample length.

       This VI is similar to the General Linear Fit VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •    H —

        H is the matrix that represents the formula you use to fit the data set {X,Y}. H[i][j] are the function
            values of X[i].


5058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5059 ordinal=5059 -->
## Functions

Functions

•      y —

  y is an input data point.

•      Standard Deviation —

  Standard Deviation is the standard deviation for data point (xi, yi). The default is 1.0.

   If xi and yi are equal or you do not know their values, leave Standard Deviation empty.

•      covariance selector —

  covariance selector indicates whether the VI computes the covariance matrix.

  0  do not compute Covariance
  1  compute Covariance

•      algorithm —

  algorithm specifies the algorithm this VI uses to compute Best Fit.

       SVD
  0         (default)
  1     Givens
  2     Givens2
  3    Householder
  4    LU Decomposition
  5     Cholesky

•     sample length —

  sample length is the length of each set of incoming data. The VI performs computation for each
  set of data. The default is 100. sample length must be greater than 0 and equal to the number of
  rows in H.

•       Coefficients —

  Coefficients is the set of coefficients that minimize chi squared.

  The following equation defines χ², where    is equal to the i-th element in Weight:


                                                   © National Instruments 5059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5060 ordinal=5060 -->
## Functions

Functions


               •      Best Fit —

            Best Fit is the fitted data computed by using Coefficients.

               •      Covariance —

            Covariance is the matrix of covariance Cwith k-by-kelements.

               cjk is the covariance between ai and ak. cjj is the variance of aj. This VI uses the following
            equation to compute the covariance matrix C: C= (H0TH0)–1

               •     mse —

         mse is the mean square error.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The General LS Linear Fit PtByPt VI uses the least-chi-square method for observation
       data sets where i= 0, 1, …, n– 1, where nis the number of your observation data sets.

      The General LS Linear Fit PtByPt VI finds the k-dimensional linear curve values and the
       set of k-dimensional linear fit coefficients, which describe the k-dimensional linear
       curve that best represents the input data set using the least-squares solution. The
       general form of the k-dimensional linear fit is

        z[i] = b[0] + Sum{b[j] H(X[i], j)} for j= 1, 2, …, k– 1; i= 0, 1, …, n– 1,

      where H is the input matrix which represents the formula you use to fit the data set{X,
         Y},


5060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5061 ordinal=5061 -->
## Functions

Functions

H[i][j] are the function values of X[i],

bis the set of Coefficients,

kis the number of elements in Coefficients,

nis the number of elements in data set{X,Y},

zis the output Best Fit.

InterpolationInterpolation PtByPtPtByPt

Use the Interpolation PtByPt VIs to perform interpolation and extrapolation.

The VIs on this palette can return point by point error codes.


 Palette Object               Description

 Polynomial Interpolation                               Interpolates or extrapolates the function f at x. PtByPt


 Rational Interpolation        Interpolates or extrapolates the function f at x using a rational
 PtByPt                        function.


 Spline Interpolant PtByPt     Returns an array, Interpolant, of length n.


                            Performs a cubic spline interpolation of f at x, given a set of
 Spline Interpolation PtByPt
                             tabulated values.


                                                    © National Instruments 5061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5062 ordinal=5062 -->
## Functions

Functions

      PolynomialPolynomial InterpolationInterpolation PtByPtPtByPt

       Interpolates or extrapolates the function f at x.

       This VI is similar to the Polynomial Interpolation VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      y —

           y is an input data point.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

           sample length must be greater than zero.

               •      x value —

           x value specifies the point at which the VI performs interpolation or extrapolation.

          The VI retains a history of values used for x and y since the last reset. If x value is in the range of
            the history of x values, the VI performs interpolation. Otherwise, the VI performs extrapolation. If


5062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5063 ordinal=5063 -->
## Functions

Functions


    x value is too far from the range of the history of x values, the interpolation error may be large.

   •       interpolation value —

    interpolation value is the interpolation of the function f at x value.

   •       interpolation error —

    interpolation error is an estimate of the error in the interpolation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The VI interpolates or extrapolates the function f at x, given a set of n points (xiyi),
where f(xi) = yi, f is any function, and given a number, x.

The VI calculates output interpolation value Pn – 1(x), where Pn – 1 is the unique
polynomial of degree n – 1 that passes through the n points (xiyi).

RationalRational InterpolationInterpolation PtByPtPtByPt

Interpolates or extrapolates the function f at x using a rational function.

The rational function passes through all the points formed by y and x. This VI is similar
to the Rational Interpolation VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 5063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5064 ordinal=5064 -->
## Functions

Functions

      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      y —

           y is an input data point.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

           sample length must be greater than zero.

               •      x value —

           x value specifies the point at which the VI performs interpolation or extrapolation.

          The VI retains a history of values used for x and y since the last reset. If x value is in the range of
            the history of x values, the VI performs interpolation. Otherwise, the VI performs extrapolation. If
           x value is too far from the range of the history of x values, the interpolation error may be large.

               •       interpolation value —

             interpolation value is the interpolation of the function f at x value.

               •       interpolation error —

             interpolation error is an estimate of the error in the interpolation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


5064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5065 ordinal=5065 -->
## Functions

Functions

SplineSpline InterpolantInterpolant PtByPtPtByPt

Returns an array, Interpolant, of length n.

The array contains the second derivatives of the spline interpolating function g(x) at
the tabulated points ξ, where i = 0, 1, …, n – 1.

      Note By default, reentrant execution is enabled in all Point By Point VIs.

This VI is similar to the Spline Interpolant VI.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      y —

    y is an input data point.

   •      x —

    x is an input data point.

   •        initial boundary —

     initial boundary is the first derivative of interpolating function g(x) at x[0], g'(x[0]). The default is
    1.0E+30, which causes this VI to set the initial boundary condition for a natural spline.

   •       final boundary —

     final boundary is the first derivative of interpolating function g(x) at x[n – 1], g'(x[n – 1]). The
     default is 1.0E+30, which causes this VI to set the final boundary condition for a natural spline.


                                                    © National Instruments 5065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5066 ordinal=5066 -->
## Functions

Functions

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

           sample length must be greater than zero.

               •      Interpolant —

            Interpolant is the second derivative of interpolating function g(x) at points x[i], i = 0, 1, …, n – 1.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The sets of input data x and y have length n and contain a tabulated function, f(xi) = yi,
       with x0 < x1 <…xn – 1. initial boundary and final boundary are the first derivatives of
       the interpolating function g(x) at points 0 and n – 1, respectively.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Point by Point\Spline
        Interpolation PtbyPt.vi

      SplineSpline InterpolationInterpolation PtByPtPtByPt

      Performs a cubic spline interpolation of f at x, given a set of tabulated values.

       This VI is similar to the Spline Interpolation VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5067 ordinal=5067 -->
## Functions

Functions


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      y —

    y is an input data point.

   •      x —

    x is an input data point.

   •      x value —

    x value is a single value.

    x value should fall within the range [x0, xn – 1].

   •      Interpolant —

    Interpolant is the second derivative of the cubic spline interpolating function.

    The number of elements in Interpolant must equal sample length. Otherwise, the VI sets the
    output interpolation value to zero.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

    sample length must be greater than zero.

   •       interpolation value —

    interpolation value is the cubic spline interpolation of f at x value.

   •       error —


                                                    © National Instruments 5067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5068 ordinal=5068 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The set of given tabulated values of f at x is in the form of yi = f(xi) for i = 0, 1, …, n – 1.
      The given second derivatives is Interpolant, which the VI obtains from the Spline
       Interpolant PtByPt VI. The points are formed by the set of input data points specified
      by sample length, and n is the total number of points.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Point by Point\Spline
        Interpolation PtbyPt.vi

      IntegralIntegral && DifferentialDifferential PtByPtPtByPt

      Use the Integral & Differential PtByPt VIs to perform integration and differentiation.

      The VIs on this palette can return point by point error codes.


         Palette Object       Description

                           Performs the discrete integration on x. You must sample x at regular intervals
          Integral x(t) PtByPt
                               of dt.


         Derivative x(t)
                           Performs a discrete differentiation on x.
        PtByPt

       IntegralIntegral x(t)x(t) PtByPtPtByPt

      Performs the discrete integration on x. You must sample x at regular intervals of dt.

5068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5069 ordinal=5069 -->
## Functions

Functions

This VI is similar to the Integral x(t) VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •        initial condition —

     initial condition is the value used to calculate the integral for the first and second time.

   •      dt —

    dt is the sampling interval and must be greater than 0. The default is 1.0.

       If dt is less than or equal to 0, the VI sets integral x(t) to 0 and returns an error.

   •       integral x(t) —

     integral x(t) is the discrete integration of x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Integral x(t) PtByPt VI calculates a definite integral. The value of integral x(t) is the
area under the curve of the set of input data points between 0 and (n– 1)(dt).


                                                    © National Instruments 5069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5070 ordinal=5070 -->
## Functions

Functions

           Note You must pass the same value to initial condition on every call to this
                 VI between one initialization of the VI and the next. The VI is not designed to
               integrate a curve of sample data points taken at irregular intervals. The VI
               returns erroneous values if you change initial condition on successive calls in
            an attempt to integrate a curve of sample data points taken at irregular
                 intervals.

       DerivativeDerivative x(t)x(t) PtByPtPtByPt

      Performs a discrete differentiation on x.

       This VI is similar to the Derivative x(t) VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •        initial condition —

               initial condition is the value used to calculate the derivative for the first and second point. The
             default is 0.

               •      dt —

            dt is the sampling interval and must be greater than zero. The default is 1.0.


5070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5071 ordinal=5071 -->
## Functions

Functions


       If dt is less than or equal to zero, the VI returns an error.

   •      dx/dt —

    dx/dt is the differentiated data point.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI uses the 2nd Order Central method to calculate the differentiation. Let y
represent the output dx/dt. yis given by the following equations:

y0 = (x0 – initial condition)/2dt y1 = (x1 – initial condition)/2dt yj = (xj+1 – xj–1) / 2dt,
for j= 2, 3, 4, …

where yj is the output dx/dt of the (j+1)th call of this VI and xj is the input x of the
(j+1)th call of this VI.

ProbabilityProbability && StatisticsStatistics PtByPtPtByPt

Use the Probability & Statistics PtByPt VIs to perform probability, descriptive statistics,
and analysis of variance operations.

The VIs on this palette can return point by point error codes.


 Palette
            Description
 Object

 Mean     Computes the mean, or average, of the values in the set of input data points specified
 PtByPt    by sample length. If the number of values is less than the sample length, the VI uses


                                                    © National Instruments 5071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5072 ordinal=5072 -->
## Functions

Functions


         Palette                    Description
        Object

                    the number of values to compute the mean.


        Standard                 Computes the mean and the standard deviation of the values in the set of input data         Deviation                     points specified by sample length.        PtByPt


         Variance   Computes the variance and mean of the set of input data points specified by sample
        PtByPt     length.


       Sample
                 Computes the mean and sample variance of the values in the set of input data points         Variance                      specified by sample length.        PtByPt


      RMS      Computes the root mean square (rms) of the set of input data points specified by
        PtByPt    sample length.


       MSE                 Computes the mean square error (mse) of x and y.
        PtByPt

       Moment
        about     Computes the moment about the mean using the specified order, m, for the set of
       Mean      input data points specified by sample length.
        PtByPt

                    Finds the median value of the set of input data points specified by sample length by
        Median
                     sorting the values of the newest set of input data points and selecting the middle
        PtByPt
                    element(s) of the sorted set of data points.


                    Finds the mode of the set of input data points specified by sample length by
       Mode
                  computing the histogram of the input values and selecting the largest bin. The mode is
        PtByPt
                    the center value of the bin with the largest count.


5072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5073 ordinal=5073 -->
## Functions

Functions


 Palette            Description
 Object

            Finds the discrete histogram of the set of input data points specified by sample length. Histogram          The histogram is a frequency count of the number of times that a specified interval PtByPt            occurs in the set of input data points.


 General            Finds the discrete histogram of the set of input data points specified by sample length
 Histogram           based on the given bin specifications. PtByPt

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Point by Point\Moving
   Histogram PtByPt.vi

MeanMean PtByPtPtByPt

Computes the mean, or average, of the values in the set of input data points specified
by sample length. If the number of values is less than the sample length, the VI uses
the number of values to compute the mean.

This VI is similar to the Mean VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —


                                                    © National Instruments 5073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5074 ordinal=5074 -->
## Functions

Functions


               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

         When you set sample length to zero, the VI calculates a cumulative solution for the input data
           from the time that you called or initialized the VI. When the sample length setting is greater than
              zero, the VI calculates the solution for only the newest set of input data.

               •     mean —

         mean is the mean, or average, of the values in the set of input data points specified by sample
             length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      StandardStandard DeviationDeviation PtByPtPtByPt

      Computes the mean and the standard deviation of the values in the set of input data
       points specified by sample length.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

5074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5075 ordinal=5075 -->
## Functions

Functions


     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.

   •      standard deviation —

    standard deviation is the standard deviation calculated from the set of input data points
     specified by sample length.

   •     mean —

   mean is the mean of the values in the set of input data points specified by sample length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


VarianceVariance PtByPtPtByPt

Computes the variance and mean of the set of input data points specified by sample
length.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 5075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5076 ordinal=5076 -->
## Functions

Functions

      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

         When you set sample length to zero, the VI calculates a cumulative solution for the input data
           from the time that you called or initialized the VI. When the sample length setting is greater than
              zero, the VI calculates the solution for only the newest set of input data.

               •     mean —

         mean is the mean of the values in the set of input data points specified by sample length.

               •      variance —

            variance is the variance computed from the set of input data points specified by sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     SampleSample VarianceVariance PtByPtPtByPt

      Computes the mean and sample variance of the values in the set of input data points
       specified by sample length.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


5076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5077 ordinal=5077 -->
## Functions

Functions


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.

   •     mean —

   mean is the mean of the values in the set of input data points specified by sample length.

   •     sample variance —

    sample variance is the sample variance of the values in the set of input data points specified by
    sample length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


      Note To compute the sample standard deviation of X, take the square root of
      sample variance.


                                                    © National Instruments 5077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5078 ordinal=5078 -->
## Functions

Functions

     RMSRMS PtByPtPtByPt

      Computes the root mean square (rms) of the set of input data points specified by
      sample length.

      The rms is shown as (ψx). This VI is similar to the RMS VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

         When you set sample length to zero, the VI calculates a cumulative solution for the input data
           from the time that you called or initialized the VI. When the sample length setting is greater than
              zero, the VI calculates the solution for only the newest set of input data.

               •     rms value —

          rms value is the root mean square computed from the set of input data points specified by
           sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


5078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5079 ordinal=5079 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.


MSEMSE PtByPtPtByPt

Computes the mean square error (mse) of x and y.

This VI is similar to the MSE VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •      y —

    y is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.

   •     mse —


                                                    © National Instruments 5079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5080 ordinal=5080 -->
## Functions

Functions


         mse is the mean square error.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     MomentMoment aboutabout MeanMean PtByPtPtByPt

      Computes the moment about the mean using the specified order, m, for the set of
       input data points specified by sample length.

       This VI is similar to the Moment about Mean VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •      order —

            order must be greater than 0. If order is less than or equal to 0, the VI sets moment to 0 and
             returns an error. The default is 2.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each


5080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5081 ordinal=5081 -->
## Functions

Functions


     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.

   •     moment —

   moment is the moment about the mean computed from the set of input data points specified by
    sample length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


MedianMedian PtByPtPtByPt

Finds the median value of the set of input data points specified by sample length by
sorting the values of the newest set of input data points and selecting the middle
element(s) of the sorted set of data points.

This VI is similar to the Median VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —


                                                    © National Instruments 5081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5082 ordinal=5082 -->
## Functions

Functions


           x is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

           sample length must be greater than zero.

               •     median —

          median is the calculated median value of the set of input data specified by sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     ModeMode PtByPtPtByPt

       Finds the mode of the set of input data points specified by sample length by
      computing the histogram of the input values and selecting the largest bin. The mode is
       the center value of the bin with the largest count.

       This VI is similar to the Mode VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.


5082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5083 ordinal=5083 -->
## Functions

Functions

   •      x —

    x is an input data point.

   •       intervals —

     intervals must be greater than 0. The default is 1.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

    sample length must be greater than zero.

   •     mode —

   mode is the value that occurs most often in a set of input values.

    For example, if the input sequence is {0, 1, 3, 3, 4, 4, 4, 5, 5, 7}, then the mode is 4 because 4
    occurs most often in the sequence.

    The Mode PtByPt VI finds mode with the aid of a histogram and according to the equation
    h(mode) = max[h(x)]. The Mode PtByPt VI generates a discrete histogram, h(x), with the specified
   number of intervals of the set of input data points specified by sample length. The Mode PtByPt
     VI scans h(x) for the interval Δi that has the maximum count. After the Mode PtByPt VI identifies
    the interval, it selects the center value of the interval as the mode of the set of input data. Refer
    to the Histogram PtByPt VI for more information about point-by-point histograms.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


HistogramHistogram PtByPtPtByPt

Finds the discrete histogram of the set of input data points specified by sample length.
The histogram is a frequency count of the number of times that a specified interval
occurs in the set of input data points.

This VI is similar to the Histogram VI.


                                                    © National Instruments 5083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5084 ordinal=5084 -->
## Functions

Functions

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •      x —

           x is an input data point.

               •       intervals —

             intervals specifies the number of intervals, or bins, to use in the histogram and must be greater
           than 0. If intervals is less than or equal to 0, the histogram is undefined, and the VI sets
            Histogram: h(X) and X Values to empty arrays and returns an error. The default is 10.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

           sample length must be greater than zero.

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      Histogram Graph —

           Histogram Graph displays the bar graph of the histogram of the input sequence x. The y-axis is
            the histogram count, and the x-axis is the histogram center values of the intervals (bins) of the
            histogram.

               •      Histogram: h(x) —

            Histogram: h(x) is the discrete histogram computed from the set of input data points specified
           by sample length.

               •     X Values —


5084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5085 ordinal=5085 -->
## Functions

Functions


    X Values is an array of the center values of the interval (bin) of the histogram.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Point by Point\Moving
   Histogram PtByPt.vi

GeneralGeneral HistogramHistogram PtByPtPtByPt

Finds the discrete histogram of the set of input data points specified by sample length
based on the given bin specifications.

This VI is similar to the General Histogram VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •     max —

                                                    © National Instruments 5085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5086 ordinal=5086 -->
## Functions

Functions


         max specifies the maximum value to include in the histogram. LabVIEW ignores this control if
            the Bins input array is not empty.

               •      x —

           x is an input data point.

               •      Bins —

            Bins specifies the boundaries of each bin of the histogram.

          The input Bins is an array of clusters where each cluster defines the range of values for a bin.

          The default behavior is to determine the number of bins according to Sturges' Rule, number of
            bins = 1 + 3.3log(size of(X)).

                     •      lower —

               lower specifies the lower boundaries of the bin.

                     •      upper —

              upper specifies the upper boundaries of the bin.

                     •       inclusion —

                 inclusion specifies how to handle the boundaries of each bin.

                           If no bin specifications are provided in the input Bins, the inputs max, min, # bins, and
                 inclusion are used to specify a set of uniformly spaced bins.

               0 Lower—Lower boundary is part of the bin but not the upper boundary.
               1 Upper—Upper boundary is part of the bin but not the lower boundary.
               2 Both—Both boundaries are part of the bin.
               3 Neither—Excludes both boundaries from the bin.


               •       inclusion —

             inclusion specifies how to treat the boundaries of each bin.

                    If array Bins is not empty, LabVIEW ignores the max, min, # bins, and inclusion inputs.


5086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5087 ordinal=5087 -->
## Functions

Functions


  0  lower—Includes the lower boundary.
  1  upper—Includes the upper boundary.

•     sample length —

  sample length is the length of each set of incoming data. The VI processes each set of data. The
  default is 100. sample length must be greater than zero.

•     min —

  min specifies the minimum value to include in the histogram. LabVIEW ignores this control if the
  Bins input array is not empty.

•      # bins —

  # bins specifies the number of bins in the histogram. # bins is ignored if the Bins input array is
  not empty.

•      Histogram Graph —

  Histogram Graph displays the bar graph of the histogram of the input sequence x. The y-axis is
  the histogram count, and the x-axis is the histogram center values of the intervals (bins) of the
  histogram.

•      Histogram —

  Histogram specifies the resulting histogram.

•       Axis —

  Axis specifies the center values for each bin of Histogram.

  The centers of each bin are set according to the following equation and returned in the output
  array Axis. center[i] = (lower + upper)/2, where lower is the lower boundary of bin i, and upper is
  the upper boundary of bin i.

•      # outside —

  # outside contains information about points not falling in any bin upon successful execution of
  the VI.

        Note The elements above and below have meaning only if you specify Bins such


                                                   © National Instruments 5087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5088 ordinal=5088 -->
## Functions

Functions


                      that Bins[0].upper ≤ Bins[1].lower < Bins[1].upper, …– < Bins[k– 1].lower, and <
                   Bins[k– 1].upper, where kis the number of elements in Bins.

                     •       total —

                  total contains the total number of values in the set of input data points specified by sample
                length not falling in any bin upon successful execution.

                     •     above —

              above represents the number of values in the set of input data points specified by sample
                length above the last bin on the upper boundary.

              The last bin on the upper boundary is Bins[size of(Bins) – 1].upper.

                     •     below —

              below represents the number of values in the set of input data points specified by sample
                length below the first bin on the lower boundary.

              The first bin on the lower boundary is Bins[0].lower.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

     GeometryGeometry PtByPtPtByPt

      Use the Geometry PtByPt VIs to perform geometry operations.

      The VIs on this palette can return point by point error codes.


5088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5089 ordinal=5089 -->
## Functions

Functions


 Palette Object       Description

 1D Polar to          Converts the polar representation of a complex number into the rectangular
 Rectangular PtByPt  representation of the complex number.


 1D Rectangular to    Converts the rectangular representation of a complex number into the polar
 Polar PtByPt         representation of the complex number.


1D1D PolarPolar toto RectangularRectangular PtByPtPtByPt

Converts the polar representation of a complex number into the rectangular
representation of the complex number.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •      magnitude —

    magnitude is the magnitude of a complex number.

   •      phase —

    phase is the angle of a complex number. You must express phase in radians.

   •      x —

    x is the x coordinate of the complex number.

   •      y —

    y is the y coordinate of the complex number.


                                                    © National Instruments 5089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5090 ordinal=5090 -->
## Functions

Functions

       This VI converts the data according to the following equations.

      x = magnitude cos(phase) y = magnitude sin(phase)
     1D1D RectangularRectangular toto PolarPolar PtByPtPtByPt

       Converts the rectangular representation of a complex number into the polar
       representation of the complex number.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •      x —

           x is the x coordinate of a complex number.

               •      y —

           y is the y coordinate of a complex number.

               •      magnitude —

           magnitude is the magnitude of the complex number.

               •      phase —

           phase is the angle of the complex number. phase is expressed in radians.


       This VI converts the data according to the following equations.


5090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5091 ordinal=5091 -->
## Functions

Functions

PolynomialPolynomial PtByPtPtByPt

Use the Polynomial PtByPt VIs to perform calculations and evaluations with
polynomials.

The VIs on this palette can return point by point error codes.


 Palette Object                    Description

 1D Polynomial Evaluation PtByPt   Performs a polynomial evaluation of x using Coefficients: a.


 1D Linear Evaluation PtByPt        Performs a linear evaluation of x.


1D1D PolynomialPolynomial EvaluationEvaluation PtByPtPtByPt

Performs a polynomial evaluation of x using Coefficients: a.

This VI is similar to the Polynomial Evaluation VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •      x —

    x is an input data point.

   •       Coefficients: a —


                                                    © National Instruments 5091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5092 ordinal=5092 -->
## Functions

Functions


             Coefficients: a contains the polynomial coefficients in ascending order of power.

          The number of elements in Coefficients: a is the polynomial order plus one.

               •      y —

           y is the polynomial evaluation of x.


      y is given by the following equation.


      where mdenotes the polynomial order.

     1D1D LinearLinear EvaluationEvaluation PtByPtPtByPt

      Performs a linear evaluation of x.

       This VI is similar to the Linear Evaluation VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •      x —

           x is an input data point.

               •       scale —

             scale is the multiplicative constant.

               •       offset —


5092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5093 ordinal=5093 -->
## Functions

Functions


     offset is the additive constant.

   •       y[i]=x[i]*a+b —

     y[i]=x[i]*a+b is the output.

OtherOther FunctionsFunctions PtByPtPtByPt

Use the Other Functions PtByPt VIs to perform miscellaneous point-by-point
operations.

The VIs on this palette can return point by point error codes.


 Palette             Description Object

 Search 1D
 Array       Searches for an element in the set of input data points specified by sample length.
 PtByPt

 Sort 1D
 Array       Sorts the set of input data points specified by sample length in ascending order.
 PtByPt

 Array Max   Searches for the maximum and minimum values in the set of input data points
 &amp; Min  specified by sample length where the region of interest is determined by the last
 PtByPt     sample length data. The indexes are between 0 and sample length.

 Add Array
 Elements   Returns the sum of all elements determined by sample length.
 PtByPt

 Increment
            Increments counter by one each time the VI is called when activate is set to TRUE.
 PtByPt


                                                    © National Instruments 5093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5094 ordinal=5094 -->
## Functions

Functions


         Palette                     Description
        Object

        Decrement Begins at start and decrements counter by one each time the VI is called when
        PtByPt      activate is set to TRUE.

        Data
       Queue      Creates a data queue of real numbers.
        PtByPt

       Complex
       Queue      Creates a data queue of complex numbers.
        PtByPt

        Boolean                     Detects transitions of input. You can choose one of the following directions: either,
         Crossing                       false-true, or true-false.        PtByPt

        Zero                     Detects zero crossings of input data point. crossing becomes TRUE immediately after
         Crossing                    the transition occurs.        PtByPt

         Zero-Order                   Holds input data point for the hold time in cycles that you define. In other words,        Hold
                   output data point is a delayed instance of input data point.        PtByPt

         Value Has                     Detects changes of input data point between the current call and the previous call to       Changed
                    the Value Has Changed PtByPt VI.
        PtByPt

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Point by Point\Train
        Wheel PtByPt.vi


5094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5095 ordinal=5095 -->
## Functions

Functions

SearchSearch 1D1D ArrayArray PtByPtPtByPt

Searches for an element in the set of input data points specified by sample length.

This VI is similar to the Search 1D Array function.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      input data point —

    input data point is an input data point.

   •      element —

    element is the value to search for in the set of input data points specified by sample length.

   •     sample length —

    sample length is the length of each set of incoming data. The VI processes each set of data. The
     default is 100. sample length must be greater than zero.

   •      index —

    index is the index where element is found. If the VI does not find element, index is –1.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 5095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5096 ordinal=5096 -->
## Functions

Functions

       SortSort 1D1D ArrayArray PtByPtPtByPt

       Sorts the set of input data points specified by sample length in ascending order.

       This VI is similar to the Sort 1D Array function.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      input data point —

            input data point is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI processes each set of data. The
             default is 100. sample length must be greater than zero.

               •      sorted array —

            sorted array is the output array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       ArrayArray MaxMax &amp;&amp; MinMin PtByPtPtByPt

      Searches for the maximum and minimum values in the set of input data points


5096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5097 ordinal=5097 -->
## Functions

Functions

specified by sample length where the region of interest is determined by the last
sample length data. The indexes are between 0 and sample length.

This VI is similar to the Array Max & Min function.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      input data point —

    input data point is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.

   •     max index —

   max index is the index for the first max value.

      It is 0 ≤ max index < sample length.

   •     max value —

   max value is the maximum value contained in the set of input data points specified by sample


                                                    © National Instruments 5097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5098 ordinal=5098 -->
## Functions

Functions


             length.

               •     min index —

          min index is the index for the first min value.

                  It is 0 ≤ min index < sample length.

               •     min value —

          min value is the minimum value contained in the set of input data points specified by sample
             length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     AddAdd ArrayArray ElementsElements PtByPtPtByPt

       Returns the sum of all elements determined by sample length.

       This VI is similar to the Add Array Elements function.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      input data point —


5098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5099 ordinal=5099 -->
## Functions

Functions


    input data point is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

   When you set sample length to zero, the VI calculates a cumulative solution for the input data
    from the time that you called or initialized the VI. When the sample length setting is greater than
     zero, the VI calculates the solution for only the newest set of input data.

   •     sum —

   sum is the sum of the input data points. The history length is determined by the last sample
    length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


IncrementIncrement PtByPtPtByPt

Increments counter by one each time the VI is called when activate is set to TRUE.

This VI is similar to the Increment function.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •       activate —

     activate, when TRUE, initiates an incremental count. When FALSE, the VI does not count.

   •        initialize —

                                                    © National Instruments 5099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5100 ordinal=5100 -->
## Functions

Functions


               initialize, when TRUE, initializes the internal state of the VI.

               •      counter —

            counter is the incremental value where counter = (previous counter + 1). The default is 1. The
            value of counter changes only after you set activate to TRUE.

               •      overflow —

            overflow is FALSE by default. If counter reaches overflow, overflow becomes TRUE and causes
            the value of counter to become 1 again.


      DecrementDecrement PtByPtPtByPt

       Begins at start and decrements counter by one each time the VI is called when
       activate is set to TRUE.

       This VI is similar to the Decrement function.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •       start —

              start is the initial value of counter if you set activate to TRUE.

               •       activate —

             activate, when TRUE, initiates a countdown beginning at the start value. When FALSE, the VI
           does not count down.

               •        initialize —


5100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5101 ordinal=5101 -->
## Functions

Functions


     initialize, when TRUE, initializes the internal state of the VI.

   •      counter —

    counter is the decremental value where counter = (previous counter – 1). The value of counter
    changes only after you set activate to TRUE.

   •      zero crossing —

    zero crossing is FALSE by default. If counter reaches zero, zero crossing becomes TRUE and
    causes the value of counter to become start again.


DataData QueueQueue PtByPtPtByPt

Creates a data queue of real numbers.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      input data point —

    input data point is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI processes each set of data. The
     default is 100. sample length must be greater than zero.


                                                    © National Instruments 5101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5102 ordinal=5102 -->
## Functions

Functions

               •        initial queue element —

               initial queue element specifies the initial element value in the data queues.

               •      eliminated element —

            eliminated element is the first point eliminated from the queue.

               •      Current Queue —

            Current Queue is the new array created by eliminating the first point and appending the new
             point.

               •      Previous Queue —

            Previous Queue is the set of data before any operation in this call.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      current length —

            current length is the size of the current queue.


      The data queue begins as a set defined by the initial queue element that matches the
        size of sample length.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Point by Point\
        Threshold Detector Comparison.vi

     ComplexComplex QueueQueue PtByPtPtByPt

       Creates a data queue of complex numbers.


5102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5103 ordinal=5103 -->
## Functions

Functions

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      input data point —

    input data point is a complex-valued data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI processes each set of data. The
     default is 100. sample length must be greater than zero.

   •        initial queue element —

     initial queue element specifies the initial element value in the data queues.

   •      eliminated element —

    eliminated element is the first point eliminated from the queue.

   •      Current Queue —

    Current Queue is the new array created by eliminating the first point and appending the new
     point.

   •      Previous Queue —

    Previous Queue is the set of data before any operation in this call.

   •       error —


                                                    © National Instruments 5103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5104 ordinal=5104 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      current length —

            current length is the size of the current queue.


      The data queue begins as a set defined by the initial queue element that matches the
        size of sample length.

      BooleanBoolean CrossingCrossing PtByPtPtByPt

       Detects transitions of input. You can choose one of the following directions: either,
        false-true, or true-false.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      input —

            input is a Boolean input value.

               •       direction —

             direction is the kind of Boolean crossing.

           0          either
           1           false-true


5104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5105 ordinal=5105 -->
## Functions

Functions


    2           true-false

   •      crossing —

    crossing is TRUE if a Boolean crossing occurred.


ZeroZero CrossingCrossing PtByPtPtByPt

Detects zero crossings of input data point. crossing becomes TRUE immediately after
the transition occurs.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      input data point —

    input data point is an input data point. If you wire a waveform value or a dynamic data type
    value to input data point, this VI evaluates only the first value of the input data.

   •       direction —

    direction is the kind of zero crossing.

    0         either
    1        minus-plus
    2        plus-minus

   •      crossing —


                                                    © National Instruments 5105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5106 ordinal=5106 -->
## Functions

Functions


            crossing is TRUE if a zero crossing occurred.


      Zero-OrderZero-Order HoldHold PtByPtPtByPt

      Holds input data point for the hold time in cycles that you define. In other words,
      output data point is a delayed instance of input data point.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      input data point —

            input data point is an input data point.

               •      hold time in cycles —

           hold time in cycles is the length of the hold phase of the zero-order hold element.

               •      output data point —

           output data point is the calculated output value.


      ValueValue HasHas ChangedChanged PtByPtPtByPt

       Detects changes of input data point between the current call and the previous call to
       the Value Has Changed PtByPt VI.


5106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5107 ordinal=5107 -->
## Functions

Functions

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      input data point —

    input data point is an input data point.

   •      has changed —

    has changed becomes TRUE when the value changes.

   •      output data point —

    output data point is a copy of input data point.


You can use the Value Has Changed PtByPt VI to trigger events when a user changes an
input parameter. The Boolean indicator has changed becomes TRUE when the change
of input data point occurs.

The following programming sequence describes how to use the Value Has Changed
PtByPt VI to build a point-by-point error checking mechanism for Point By Point VIs
that have an error parameter.

 1. Choose a parameter that you want to monitor closely for errors.
 2. Wire the parameter value as input data point to the Value Has Changed PtByPt VI.
 3. Transfer the output data point, which is always the unchanged input data point in
   the Value Has Changed PtByPt VI, to the target VI.
 4. Pass the TRUE event generated by the Value Has Changed PtByPt VI to the target VI
    to trigger initialization. The Value Has Changed PtByPt VI outputs a TRUE value
   whenever the input parameter value changes.

                                                    © National Instruments 5107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5108 ordinal=5108 -->
## Functions

Functions

       For the first call that follows initialization of the target VI, LabVIEW checks for errors.
        Initialization of the target VI and error checking occurs every time the input parameter
       changes.

     AdditionalAdditional InformationInformation aboutabout thethe SignalSignal ProcessingProcessing VIsVIs

       This book contains additional information about the Signal Processing VIs.

     OutputOutput UnitsUnits forfor FFT-BasedFFT-Based VIsVIs

      The following table displays the output units and scale factors that the LabVIEW FFT-
      based VIs use.


                                                            Non-DC   DC                                    Non-DC  DC                               Phase          VI                                                  Sided   Scale      Scale                                            Unit(k>0)  Unit(k=0)                             Unit
                                                                         Factor     Factor

        FFT                            V        V        Double N/2     N       radians
       Power Spectrum                   Vrms 2     V2        Double  1/2       1    —
        Auto Power Spectrum               Vrms 2     V2         Single  1         1    —

        Amplitude and Phase Spectrum      Vrms      V          Single  1         1        radians
        FFT Power Spectrum and PSD             2                                           Vrms      V2         Single  1         1    —        (power spectrum measurement)

        FFT Power Spectrum and PSD
        (power spectral density             Vrms 2/Hz  V2/Hz      Single  1         1    —
        measurement)

                                                                                                 radians/
        FFT Spectrum (Mag-Phase)          Vrms      V          Single  1         1                                                                                         degrees

                                                                                                 radians/
        FFT Spectrum (Real-Imag)           Vrms      V          Single  1         1                                                                                         degrees

      The VI column of the previous table displays the VI name. The Non-DC Unit column
       displays the output unit for non-DC components where the bin number, or array index,
         is nonzero. The DC Unit column displays the output unit for the DC or offset
      component where the bin number is zero, indicating the first element of the spectrum

5108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5109 ordinal=5109 -->
## Functions

Functions

array. k is the spectral bin number defined by the equation f/Δ f = f/(fs/n). V is Volts,
and Vrms is Volts root-mean-squared, or Volts rms. VIs with a dB On control map the
output unit onto a dB scale by computing 10*log(unit2) if the output unit is normally
squared, or 20*log(unit) for non-squared units. These VIs reference all dB values to 1.0.

The Sided column of the previous table displays whether the VI computes the double-
sided or single-sided spectrum. A double-sided spectrum has non-DC component
magnitudes that the VI halves between the positive and negative frequency bins,
corresponding to the first and second halves of the double-sided spectrum array
respectively. All double-sided VIs associate a non-unity scale factor with the results,
and the Non-DC Scale Factor and DC Scale Factor columns list these values. N is the
input time-domain signal size, or the number of samples. A single-sided spectrum
returns only the positive frequency components, or the components in the first half of
the double-sided spectrum. The single-sided spectrum also compensates for all scale
factors these VIs associate with the double-sided spectrum.

The Power Spectrum VI, Auto Power Spectrum VI, FFT Power Spectrum VI, and FFT
Power Spectral Density VI compute power as a real quantity and thus return no phase
information. The FFT VI, Amplitude and Phase Spectrum VI, FFT Spectrum (Mag-Phase)
VI, and FFT Spectrum (Real-Imag) VI compute the real and imaginary parts of the
spectrum phase. These VIs reference all phase values to a cosine so that an FFT
component at bin k with an amplitude of A volts and θ radians can be represented as
the time-domain signal:                                   where i = 0, 1, ...
N–1.The Phase Unit column of the previous table displays the resulting phase units. A
Phase Unit of radians/degrees indicates that you can use the convert to degree
control to change the phase units from radians to degrees.

Refer to the FFT and Power Spectrums Units VI in the labview\examples\Signal
Processing\Transforms for an example converting units using the FFT-based
VIs.

CharacteristicCharacteristic InputsInputs andand OutputsOutputs ofof thethe PointPoint ByBy PointPoint VIsVIs

The Point By Point VIs correspond to each array-based analysis VI that is relevant to
continuous data acquisition. However, you must account for programming differences.
You usually have fewer programming tasks when you use the Point By Point VIs. The
following table describes characteristic inputs and outputs of the Point By Point VIs.

                                                    © National Instruments 5109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5110 ordinal=5110 -->
## Functions

Functions

           Note You can use the Point By Point VIs only in the LabVIEW Full and
               Professional Development Systems.


        Parameter  Description

         input data  Incoming data

        output                    Outgoing, analyzed data        data

           initialize    Routine that resets the internal state of a VI

        sample     Setting for the data acquisition system or computation system that best represents the
         length     area of interest in the data

        InitializingInitializing thethe PointPoint ByBy PointPoint VIsVIs

       Using the initialize parameter, you can reset the internal state of Point By Point VIs
       without interrupting the continuous flow of data or computation. You can reset a VI in
      response to events such as the following:

            • A user changing the value of a parameter
            • The application generating a specific event or reaching a threshold

       For example, the Value Has Changed PtByPt VI can respond to change events such as
       the following:

            • Receiving the input data
            • Detecting the change
            • Generating a Boolean TRUE value that triggers initialization in another VI
            • Transferring the input data to another VI for processing

      The following block diagram shows the Value Has Changed PtByPt VI triggering
        initialization in another VI and transferring data to that VI. In this case, the input data is
      a parameter value for the target VI.


5110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5111 ordinal=5111 -->
## Functions

Functions


Many point-by-point applications do not require use of the initialize parameter
because initialization occurs automatically whenever an operator quits an application
and then starts again.

Error Checking and Initialization

Error codes usually identify invalid parameters and settings. For higher-level error
checking, configure the program to monitor and respond to irregularities in data
acquisition or in computation. For example, you create a form of error checking when
you range check data.

A Point By Point VI generates an error code once at the initial call to the VI or at the first
call to the VI after you initialize an application. Because Point By Point VIs generate
error codes only once, they can perform optimally in a real-time, deterministic
application.

The Point By Point VIs generate an error code to inform you of any invalid parameters
or settings when they detect an error during the first call. In subsequent calls, the Point
By Point VIs set the error code to zero and continue running, generating no error codes.
You can program an application to take one of the following actions in response to the
first error:

  • Report the error and continue running.
  • Report the error and stop.
  • Ignore the error and continue running. This is the default behavior.

You can use the Value Has Changed PtByPt VI to build a point-by-point error checking
mechanism for Point by Point VIs that have an error parameter.


                                                    © National Instruments 5111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5112 ordinal=5112 -->
## Functions

Functions

    DataData CommunicationCommunication

      Use the Data Communication VIs and functions to exchange data between
       applications.

      The VIs and functions on this palette can return SMTP email reply codes.


         Palette Object   Description

                      Use the Shared Variable node, VI, and functions to share data among VIs or        Shared Variable
                      between locations on the block diagram that you cannot connect with wires.


        Network        Use the Network Streams functions to stream data continuously between two
        Streams        LabVIEW applications.

                      Use local variables to read or write to one of the controls or indicators on the         Local Variable                            front panel of a VI.

         Global Variable  Use global variables to access and pass data among several VIs.

       Queue         Use the Queue Operations functions to create a queue for communicating data
        Operations      between sections of a block diagram or from another VI.


                      Use the Synchronization VIs and functions to synchronize tasks executing in
         Synchronization
                             parallel and to pass data between parallel tasks.


        DataSocket     Use the DataSocket VI and functions to pass data between VIs programmatically.


                      Use the Protocols VIs and functions to exchange data between applications by
         Protocols
                         using protocols such as TCP/IP, UDP, serial, IrDA, Bluetooth, and SMTP.


5112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5113 ordinal=5113 -->
## Functions

Functions


 Palette Object   Description

 Actor          Use the Actor Framework VIs to create applications based on the Actor
 Framework     Framework.

SharedShared VariableVariable

Use the Shared Variable node, VI, and functions to share data among VIs or between
locations on the block diagram that you cannot connect with wires.


 Palette
             Description Object

 Open
 Variable    Opens a connection to a shared variable.
 Connection

 Read       Reads from a network-published shared variable, I/O variable, or I/O variable
 Variable     container.

 Write             Writes to a network-published shared variable, I/O variable, or I/O variable container. Variable

 Close
 Variable
             Closes a connection to a shared variable.
 Connection
 Function

             Represents a shared variable on the block diagram. To bind a Shared Variable node to
            a shared variable from the active project, add a Shared Variable node to the block
 Shared     diagram and double-click or right-click the node and select Select Variable>>Browse
 Variable    from the shortcut menu to display the Browse for Variable dialog box. You also can
            drag a shared variable from the Project Explorer window onto the block diagram of a
               VI in the same project to create a Shared Variable node.

 Local
 Variable    Use this constant to supply a reference to one of the following items: local PSP
 Object       Variable Engine, local I/O Variable Engine, local Root PSP Variable Container, or local
 Reference

                                                    © National Instruments 5113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5114 ordinal=5114 -->
## Functions

Functions


         Palette                     Description
        Object

                   Root I/O Variable Container.


         Variable     Gets (reads) and/or sets (writes) properties of a reference. This node operates the
         Property   same way as a standard Property Node. However, this node is pre-configured for
       Node        variable references.

        Search                    Searches under a variable container and returns an array of references to variable         Variable                      objects that match your search criteria. You can use this function to find variables         Container                     programmatically.
         Function

       PSP                  Use the PSP Variable VI and functions to access PSP variables programmatically.
         Variable

         I/O
                  Use the I/O Variable functions to access I/O variables programmatically.         Variable

    OpenOpen VariableVariable ConnectionConnection

      Opens a connection to a shared variable.

      You cannot buffer data that you read or write with this function. To enable buffering,
      use the Open and Verify Variable Connection or Open Variable Connection in
      Background function instead.


      Inputs/Outputs

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.


5114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5115 ordinal=5115 -->
## Functions

Functions


  You can right-click this input terminal and select Create»Control or Create»Constant to create
   this reference. You then can click the control or constant and select Browse to display the
  Browse Variable Objects dialog box. You also can find variable references programmatically. This
  input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
  type the address into a string control and directly wire that string control to this input terminal.

•      data type —

  data type specifies the data type of the shared variable or I/O variable container. For I/O variable
  containers, you must specify an array data type.

  This input is available only if the data type has not been previously specified. You can specify a
  data type by placing a checkmark in the Specify Data Type checkbox on the Configuration page
  of the Properties dialog box for the variable refnum. If you specify the data type upon opening
  the connection, this terminal is unavailable on subsequent read and write functions.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      access —

  access specifies read access and write access settings for the shared variable connection.

      •     Read Access —

     Read Access specifies read access settings.

       Allowed—You can use the shared variable connection to read the value of the shared
      0         variable.
       Required—You must use the shared variable connection to read the value of the shared
      1 variable. If you set this option and LabVIEW cannot open the variable connection for
        reading, the function returns an error.
      None—You cannot use the shared variable connection to read the value of the shared
      2
         variable.

      •      Write Access —

      Write Access specifies write access options.


                                                   © National Instruments 5115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5116 ordinal=5116 -->
## Functions

Functions


               0 Allowed—You can use the shared variable connection to write to the shared variable.
                Required—You must use the shared variable connection to write to the shared variable. If
               1 you set this option and LabVIEW cannot open the variable connection for write, the
                  function returns an error.
               2 None—You cannot use the shared variable connection to write to the shared variable.


               •      shared variable refnum out —

           shared variable refnum out is the reference to the shared variable or I/O variable container.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     ReadRead VariableVariable

      Reads from a network-published shared variable, I/O variable, or I/O variable
       container.

       For I/O variables and I/O variable containers, this function performs a scanned read
       operation.


      Inputs/Outputs

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.

           You can right-click this input terminal and select Create»Control or Create»Constant to create
              this reference. You then can click the control or constant and select Browse to display the
           Browse Variable Objects dialog box. You also can find variable references programmatically. This
            input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
            type the address into a string control and directly wire that string control to this input terminal.
               •      data type —


5116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5117 ordinal=5117 -->
## Functions

Functions


    data type specifies the data type of the shared variable or I/O variable container. For I/O variable
     containers, you must specify an array data type.

    This input is available only if the data type has not been previously specified. You can specify a
    data type by placing a checkmark in the Specify Data Type checkbox on the Configuration page
     of the Properties dialog box for the variable refnum. If you specify the data type upon opening
    the connection, this terminal is unavailable on subsequent read and write functions.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      shared variable refnum out —

    shared variable refnum out is the reference to the shared variable or I/O variable container.

   •      data out —

    data out is the data read from the shared variable or I/O variable container.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      timestamp —

    timestamp is the timestamp indicating when the current data was written to the shared
     variable.

    This output is available only if you place a checkmark in the Read Timestamp checkbox on the
    Configuration page of the Properties dialog box for the variable refnum. I/O variable containers
   do not support timestamps.

Use this function when you need to read the current value regardless of value changes.
If you need to read only new data values, use the Read Variable with Timeout function.

      Caution If you use this function to access a shared variable without first
       opening a connection to the variable, LabVIEW automatically opens a
       connection to the variable. However, this implicit open operation can add
          jitter to the application. Therefore, National Instruments recommends that
       you open all variable connections with the Open Variable Connection


                                                    © National Instruments 5117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5118 ordinal=5118 -->
## Functions

Functions


               function before accessing the variables.

      WriteWrite VariableVariable

       Writes to a network-published shared variable, I/O variable, or I/O variable container.

       For I/O variables and I/O variable containers, this function performs a scanned write
       operation.


      Inputs/Outputs

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.

           You can right-click this input terminal and select Create»Control or Create»Constant to create
              this reference. You then can click the control or constant and select Browse to display the
           Browse Variable Objects dialog box. You also can find variable references programmatically. This
            input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
            type the address into a string control and directly wire that string control to this input terminal.
               •      data in —

           data in contains the data you want to write to the connection.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      shared variable refnum out —

           shared variable refnum out is the reference to the shared variable or I/O variable container.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5119 ordinal=5119 -->
## Functions

Functions

      Caution If you use this function to access a shared variable without first
       opening a connection to the variable, LabVIEW automatically opens a
       connection to the variable. However, this implicit open operation can add
          jitter to the application. Therefore, National Instruments recommends that
       you open all variable connections with the Open Variable Connection
        function before accessing the variables.

CloseClose VariableVariable ConnectionConnection FunctionFunction

Closes a connection to a shared variable.


Inputs/Outputs

   •      shared variable refnum in —

    shared variable refnum in is the reference to the shared variable or I/O variable container.

    You can right-click this input terminal and select Create»Control or Create»Constant to create
     this reference. You then can click the control or constant and select Browse to display the
    Browse Variable Objects dialog box. You also can find variable references programmatically. This
    input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
    type the address into a string control and directly wire that string control to this input terminal.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5120 ordinal=5120 -->
## Functions

Functions

     SharedShared VariableVariable

       Represents a shared variable on the block diagram. To bind a Shared Variable node to
      a shared variable from the active project, add a Shared Variable node to the block
      diagram and double-click or right-click the node and select Select Variable>>Browse
      from the shortcut menu to display the Browse for Variable dialog box. You also can
      drag a shared variable from the Project Explorer window onto the block diagram of a VI
        in the same project to create a Shared Variable node.

           Note The behavior of the Shared Variable node differs when it is bound to a
               physical I/O channel. Refer to the Using I/O Variables topic for information
             about I/O variables.


      Inputs/Outputs

               •      ? —

            Variable specifies the value to write to the Shared Variable node. You must wire a value to this
            input when the Shared Variable node is configured to write data, or the VI will be broken. This
            input is available only when the Shared Variable node is configured to write data.

               •     ms timeout (0) —

         ms timeout specifies a timeout period in milliseconds for a Shared Variable node configured to
            read data. The shared variable waits the specified amount of time for updated data, and the
           timed out? indicator returns whether the shared variable received updated data in the specified
           time period or timed out. Updated data can represent a new value or an existing value that
            simply confirms a valid connection with the shared variable in the active project. To add a ms
           timeout input to the Shared Variable node, right-click the Shared Variable node and select Show
           Timeout from the shortcut menu. You only can enable a timeout period for Shared Variable
           nodes configured to read data. You cannot enable a timeout period for nodes that access I/O
             variables locally.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


5120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5121 ordinal=5121 -->
## Functions

Functions

   •      ? —

    Variable specifies the current value of the shared variable that the Shared Variable node
    represents. This output is available only when the Shared Variable node is configured to read
     data. If the Shared Variable node times out, Variable returns the value that the node last read. If
    the node times out before reading any data or if the type of data is incompatible, data returns a
    value of 0, empty, or an equivalent value.

   •      timed out? —

    timed out? displays whether a Shared Variable node read new data within the specified timeout
    period or timed out. To add a timed out? output to the Shared Variable node, right-click the
    Shared Variable node and select Show Timeout from the shortcut menu. You only can enable a
    timeout period for Shared Variable nodes configured to read data. You cannot enable a timeout
    period for nodes that access I/O variables locally.

       If the timeout expires, the Shared Variable node returns the last value written to the variable and
    does not return an error.
   •      timestamp —

    timestamp displays the timestamp data for the shared variable. To add a timestamp output to
    the Shared Variable node for a single-process shared variable or an I/O variable, you must first
    place a checkmark in the Enable timestamp checkbox on the Variable page of the Shared
    Variable Properties dialog box, and then right-click the Shared Variable node and select Show
    Timestamp from the shortcut menu. You can use this output only with shared variable nodes
    that are configured to read data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


When you drag a shared variable from the Project Explorer window to the block
diagram or place a Shared Variable node on the block diagram, LabVIEW configures
the Shared Variable node to read data. To configure the Shared Variable node to write
data, right-click the Shared Variable node and select Change to Write from the
shortcut menu.

      Note You can create, configure, and host shared variables only on Windows,
      RT targets, and certain PDA targets. You can use the DataSocket VI and
        functions to read or write shared variables from other platforms.


                                                    © National Instruments 5121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5122 ordinal=5122 -->
## Functions

Functions

      To specify how a Shared Variable node connects to a shared variable, you can set the
      node to absolute or target-relative. An absolute Shared Variable node always connects
       to the shared variable on the target on which you created the shared variable. A target-
        relative Shared Variable node always connects to the shared variable on the target on
      which you run the VI that contains the Shared Variable node. To change an absolute
      Shared Variable node to target-relative, right-click the Shared Variable node and select
      Reference Mode»Target Relative from the shortcut menu. To change a target-relative
      Shared Variable node to absolute, right-click the Shared Variable node and select
      Reference Mode»Absolute from the shortcut menu.

           Note

             Opening a VI containing a Shared Variable node in a project where the Shared
               Variable node cannot find its associated shared variable in the Project
               Explorer window causes the Shared Variable node to break. Any front panel
               controls associated with the missing shared variable also break.

             (Windows) This behavior is specific to Windows and only occurs when you
            open the VI in a project. If you open the VI in the main application instance,
            you do not receive notification of missing shared variables.


      A network-published Shared Variable node on a VI uses an .aliases file to determine
       the IP address of the computing device in the project where the Shared Variable is
       deployed. When you run a VI in a LabVIEW project, the VI finds the project's .aliases
          file and uses that to resolve aliases. The project keeps entries for each computing
       device in the project in the .aliases file, and updates the IP addresses when they
       change. When the VI runs in the main application instance, the VI uses the
     LabVIEW.aliases file in the same directory as LabVIEW.exe to find aliases. This
          file does not update automatically like the project .aliases file. When building an
       application that uses shared variables, ensure that the build specification includes the
     .aliases file.

      You must add the IP address to the .aliases file. If the VI fails to find the alias, the
      Shared Variable node uses the last known IP address. If the shared variable is no
       longer deployed at the last known IP address, the Shared Variable node will return an
        error.

5122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5123 ordinal=5123 -->
## Functions

Functions

If you publish a shared variable with less than 8 kilobytes of data, it can take up to 10
milliseconds for LabVIEW to send that data over the network. The Flush Shared
Variable Data VI allows you to flush the buffer immediately and eliminate this delay.

      Note You can right-click a Shared Variable node and select Replace with
       Programmatic Access from the shortcut menu to switch to programmatic
        access. By using programmatic shared variable access, you can create clean,
        scalable block diagrams.

LocalLocal VariableVariable ObjectObject ReferenceReference

Use this constant to supply a reference to one of the following items: local PSP Variable
Engine, local I/O Variable Engine, local Root PSP Variable Container, or local Root I/O
Variable Container.

To define the type of the constant, click inside the border of the constant and select
the type from the shortcut menu.

Use this constant when finding variables programmatically.


Inputs/Outputs

   •      Local PSP Variable Root Container —

VariableVariable PropertyProperty NodeNode

Gets (reads) and/or sets (writes) properties of a reference. This node operates the
same way as a standard Property Node. However, this node is pre-configured for
variable references.


                                                    © National Instruments 5123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5124 ordinal=5124 -->
## Functions

Functions


      Inputs/Outputs

               •      reference —
            reference is the refnum associated with the object for which you want to set or get properties.

                    If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For
            the Application class, the default is the current application instance. For the VI class, the default
                is the VI containing the Property Node.

           You also can wire a LabVIEW class to the reference input to access the private data of the
           LabVIEW class.

               •       error in (no error) —
             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.
               •      property 2 — property 2..n are examples of properties you want to set (write).
               •      reference out —
            reference out returns reference unchanged.
               •       error out —
             error out contains error information. This output provides standard error out functionality.
               •      property 1 — property 1..n are examples of properties you want to get (read).
               •      Property —

     SearchSearch VariableVariable ContainerContainer FunctionFunction

      Searches under a variable container and returns an array of references to variable
       objects that match your search criteria. You can use this function to find variables
       programmatically.

         All search criteria are optional. If you leave a search criterion input terminal unwired,
        this function does not filter based on that criterion.


5124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5125 ordinal=5125 -->
## Functions

Functions


Inputs/Outputs

   •       class —

     class specifies the class of the variable objects to search for. The default is Variable Object.

   •      container refnum in —

    container refnum in specifies the variable container under which to search. This function
    searches the full container hierarchy under the container you specify.

    This function searches the partial URLs of all variables under the container you specify. The
     partial URLs do not include the URL corresponding to this container.

   •      regular expression —

    regular expression is the pattern to search for within the variable object URLs. The default is an
    empty string.

    This function uses the same regular expression rules as the Match Regular Expression function.

   •      data type —

    data type specifies the data type of the shared variables you want to search for. The default is
     variant, which specifies that if you leave the terminal unwired, the function does not filter based
    on data type. However, if you wire a variant control or constant to this terminal, the function
    returns variables of the variant data type only.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      access type —

    access type specifies the read access and write access settings of the shared variables you want
    to search for. The default value is Allowed for both read access and write access.


                                                    © National Instruments 5125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5126 ordinal=5126 -->
## Functions

Functions


                     •     Read Access —

              Read Access specifies options for filtering shared variables based on read access.

               0 Allowed—Performs no filtering based on read access.
               1 Required—Returns only shared variables with read access enabled.
               2 Denied—Returns only shared variables with read access disabled.

                     •      Write Access —

                Write Access specifies options for filtering shared variables based on write access.

               0 Allowed—Performs no filtering based on write access.
               1 Required—Returns only shared variables with write access enabled.
               2 Denied—Returns only shared variables with write access disabled.


               •      container refnum out —

            container refnum out is the reference to the shared variable container you wire to the container
          refnum in input.

               •     refnum array out —

          refnum array out contains the variable object references that result from your search.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The search matches the regular expression you specify against the partial variable
        identifier URLs of all variable objects under the variable container you specify. The
        partial URL does not include the initial URL substring that corresponds to the URL you
       wire to the container refnum in input.

       For example, if you wire a URL of ni.var.psp://lib1 to the container refnum in
       input, the partial URL for a variable object with the URL ni.var.psp://lib1/
     lib2/var1 becomes lib2/var1.


5126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5127 ordinal=5127 -->
## Functions

Functions

PSPPSP VariableVariable

Use the PSP Variable VI and functions to access PSP variables programmatically.


 Palette              Description
 Object

 Open and
 Verify      Opens a connection to a shared variable and verifies that the connection is opened
 Variable      successfully.
 Connection

 Open
 Variable           Opens a connection to a shared variable in the background. This function does not
 Connection              wait to verify that the connection is opened successfully. in
 Background

 Read       Reads a new value from a network-published shared variable. Instead of returning the
 Variable      latest data value, which might have been read already, this function performs a
 with         blocking read, which means the function does not finish executing until a new value
 Timeout      arrives or the timeout you specify expires.

 Flush
             Flushes the buffer of all network-published shared variables immediately. LabVIEW Shared             uses an 8 kilobyte buffer for all shared variable values, and LabVIEW automatically Variable
              flushes the 8 kilobyte buffer either when the buffer fills up or after 10 ms have passed. Data

OpenOpen andand VerifyVerify VariableVariable ConnectionConnection

Opens a connection to a shared variable and verifies that the connection is opened
successfully.


Inputs/Outputs

   •       buffer size in elements —

                                                    © National Instruments 5127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5128 ordinal=5128 -->
## Functions

Functions


             buffer size in elements specifies the number of elements to include in the client-side buffer for
            the variable connection. The default is 0, which specifies no buffering.

         When you wire a value of 2 or greater to this input, the function creates a read buffer, a write
              buffer, or both, depending on the read and write access settings you specify using the access
             input. If you wire a value of 1 to this input, the function returns an error.

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.

           You can right-click this input terminal and select Create»Control or Create»Constant to create
              this reference. You then can click the control or constant and select Browse to display the
           Browse Variable Objects dialog box. You also can find variable references programmatically. This
            input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
            type the address into a string control and directly wire that string control to this input terminal.

               •      data type —

           data type specifies the data type of the shared variable or I/O variable container. For I/O variable
             containers, you must specify an array data type.

             This input is available only if the data type has not been previously specified. You can specify a
            data type by placing a checkmark in the Specify Data Type checkbox on the Configuration page
             of the Properties dialog box for the variable refnum. If you specify the data type upon opening
            the connection, this terminal is unavailable on subsequent read and write functions.

               •      timeout ms —

           timeout ms specifies the time, in milliseconds, that the function waits before timing out.

          The operation aborts if it does not complete within timeout ms. To disable timeouts, set
           timeout ms to -1.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      access —

            access specifies read access and write access settings for the shared variable connection.


5128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5129 ordinal=5129 -->
## Functions

Functions


         •     Read Access —

       Read Access specifies read access settings.

        Allowed—You can use the shared variable connection to read the value of the shared        0           variable.
         Required—You must use the shared variable connection to read the value of the shared
        1 variable. If you set this option and LabVIEW cannot open the variable connection for
          reading, the function returns an error.
        None—You cannot use the shared variable connection to read the value of the shared        2           variable.

         •      Write Access —

        Write Access specifies write access options.

        0 Allowed—You can use the shared variable connection to write to the shared variable.
         Required—You must use the shared variable connection to write to the shared variable. If
        1 you set this option and LabVIEW cannot open the variable connection for write, the
          function returns an error.
        2 None—You cannot use the shared variable connection to write to the shared variable.


   •      shared variable refnum out —

    shared variable refnum out is the reference to the shared variable or I/O variable container.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use this function when you do not want to add code to wait explicitly for the
connection to open before using the connection to read or write variables.

OpenOpen VariableVariable ConnectionConnection inin BackgroundBackground

Opens a connection to a shared variable in the background. This function does not
wait to verify that the connection is opened successfully.


                                                    © National Instruments 5129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5130 ordinal=5130 -->
## Functions

Functions


      Inputs/Outputs

               •       buffer size in elements —

             buffer size in elements specifies the number of elements to include in the client-side buffer for
            the variable connection. The default is 0, which specifies no buffering.

         When you wire a value of 2 or greater to this input, the function creates a read buffer, a write
              buffer, or both, depending on the read and write access settings you specify using the access
             input. If you wire a value of 1 to this input, the function returns an error.

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.

           You can right-click this input terminal and select Create»Control or Create»Constant to create
              this reference. You then can click the control or constant and select Browse to display the
           Browse Variable Objects dialog box. You also can find variable references programmatically. This
            input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
            type the address into a string control and directly wire that string control to this input terminal.

               •      data type —

           data type specifies the data type of the shared variable or I/O variable container. For I/O variable
             containers, you must specify an array data type.

             This input is available only if the data type has not been previously specified. You can specify a
            data type by placing a checkmark in the Specify Data Type checkbox on the Configuration page
             of the Properties dialog box for the variable refnum. If you specify the data type upon opening
            the connection, this terminal is unavailable on subsequent read and write functions.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      access —

            access specifies read access and write access settings for the shared variable connection.


5130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5131 ordinal=5131 -->
## Functions

Functions


         •     Read Access —

       Read Access specifies read access settings.

        Allowed—You can use the shared variable connection to read the value of the shared        0           variable.
         Required—You must use the shared variable connection to read the value of the shared
        1 variable. If you set this option and LabVIEW cannot open the variable connection for
          reading, the function returns an error.
        None—You cannot use the shared variable connection to read the value of the shared        2           variable.

         •      Write Access —

        Write Access specifies write access options.

        0 Allowed—You can use the shared variable connection to write to the shared variable.
         Required—You must use the shared variable connection to write to the shared variable. If
        1 you set this option and LabVIEW cannot open the variable connection for write, the
          function returns an error.
        2 None—You cannot use the shared variable connection to write to the shared variable.


   •      shared variable refnum out —

    shared variable refnum out is the reference to the shared variable or I/O variable container.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use this function when you need to open a large number of PSP Variable connections
quickly. For large quantities of PSP Variables, this function is more efficient than the
Open and Verify Variable Connection function. However, when you use this function,
you must add code to wait explicitly for the variable connection(s) to finish opening
before using the connection(s) to read or write variables. If you do not add code to wait
explicitly for the connection(s) to open, the read and write function(s) might return
errors on the first one or more iterations.


                                                    © National Instruments 5131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5132 ordinal=5132 -->
## Functions

Functions

     ReadRead VariableVariable withwith TimeoutTimeout

      Reads a new value from a network-published shared variable. Instead of returning the
        latest data value, which might have been read already, this function performs a
       blocking read, which means the function does not finish executing until a new value
        arrives or the timeout you specify expires.

      Use this function to avoid reading data values that you already have read. If you need
       to read the current value regardless of whether the value changes, use the Read
       Variable function.


      Inputs/Outputs

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.

           You can right-click this input terminal and select Create»Control or Create»Constant to create
              this reference. You then can click the control or constant and select Browse to display the
           Browse Variable Objects dialog box. You also can find variable references programmatically. This
            input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
            type the address into a string control and directly wire that string control to this input terminal.
               •      data type —

           data type specifies the data type of the shared variable or I/O variable container. For I/O variable
             containers, you must specify an array data type.

             This input is available only if the data type has not been previously specified. You can specify a
            data type by placing a checkmark in the Specify Data Type checkbox on the Configuration page
             of the Properties dialog box for the variable refnum. If you specify the data type upon opening
            the connection, this terminal is unavailable on subsequent read and write functions.
               •      timeout ms —

           timeout ms specifies the time, in milliseconds, that the function waits before timing out.

          A value of –1 specifies no timeout. The default is 0. Use the timed out? output to detect a
            timeout.
               •       error in (no error) —


5132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5133 ordinal=5133 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      shared variable refnum out —

    shared variable refnum out is the reference to the shared variable or I/O variable container.

   •      data out —

    data out is the data read from the shared variable or I/O variable container.

   •      timed out? —

    timed out? is TRUE if a new element does not become available within the timeout you specify.

       If the timeout expires, this function returns the last value written to the variable and does not
    return an error.
   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      timestamp —

    timestamp is the timestamp indicating when the current data was written to the shared
     variable.

    This output is available only if you place a checkmark in the Read Timestamp checkbox on the
    Configuration page of the Properties dialog box for the variable refnum. I/O variable containers
   do not support timestamps.

Each variable connection treats a value as new only once. If multiple Read Variable
with Timeout functions share the same variable connection, each instance of the
function returns a different value depending on the order in which the instances
execute.

      Caution If you use this function to access a shared variable without first
       opening a connection to the variable, LabVIEW automatically opens a
       connection to the variable. However, this implicit open operation can add
          jitter to the application. Therefore, National Instruments recommends that
       you open all variable connections with the Open Variable Connection
        function before accessing the variables.

                                                    © National Instruments 5133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5134 ordinal=5134 -->
## Functions

Functions

      FlushFlush SharedShared VariableVariable DataData

       Flushes the buffer of all network-published shared variables immediately. LabVIEW
       uses an 8 kilobyte buffer for all shared variable values, and LabVIEW automatically
       flushes the 8 kilobyte buffer either when the buffer fills up or after 10 ms have passed.

           If you write less than 8 kilobytes of data, it can take up to 10 milliseconds for LabVIEW
       to send that data over the network. You can use the Flush Shared Variable Data VI to
       flush the buffer immediately and eliminate this delay.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      I/OI/O VariableVariable

      Use the I/O Variable functions to access I/O variables programmatically.


         Palette Object          Description

        Scanned Variable Read  Reads from an I/O variable or I/O variable container using scanned access.

        Scanned Variable Write  Writes to an I/O variable or I/O variable container using scanned access.

         Direct Variable Read    Reads from an I/O variable or I/O variable container using direct access.

         Direct Variable Write    Writes to an I/O variable or I/O variable container using direct access.

5134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5135 ordinal=5135 -->
## Functions

Functions

ScannedScanned VariableVariable ReadRead

Reads from an I/O variable or I/O variable container using scanned access.


Inputs/Outputs

   •      shared variable refnum in —

    shared variable refnum in is the reference to the shared variable or I/O variable container.

    You can right-click this input terminal and select Create»Control or Create»Constant to create
     this reference. You then can click the control or constant and select Browse to display the
    Browse Variable Objects dialog box. You also can find variable references programmatically. This
    input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
    type the address into a string control and directly wire that string control to this input terminal.
   •      data type —

    data type specifies the data type of the shared variable or I/O variable container. For I/O variable
     containers, you must specify an array data type.

    This input is available only if the data type has not been previously specified. You can specify a
    data type by placing a checkmark in the Specify Data Type checkbox on the Configuration page
     of the Properties dialog box for the variable refnum. If you specify the data type upon opening
    the connection, this terminal is unavailable on subsequent read and write functions.
   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      shared variable refnum out —

    shared variable refnum out is the reference to the shared variable or I/O variable container.

   •      data out —

    data out is the data read from the shared variable or I/O variable container.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5136 ordinal=5136 -->
## Functions

Functions

               •      timestamp —

           timestamp is the timestamp indicating when the current data was written to the shared
              variable.

             This output is available only if you place a checkmark in the Read Timestamp checkbox on the
            Configuration page of the Properties dialog box for the variable refnum. I/O variable containers
          do not support timestamps.

     ScannedScanned VariableVariable WriteWrite

       Writes to an I/O variable or I/O variable container using scanned access.


      Inputs/Outputs

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.

           You can right-click this input terminal and select Create»Control or Create»Constant to create
              this reference. You then can click the control or constant and select Browse to display the
           Browse Variable Objects dialog box. You also can find variable references programmatically. This
            input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
            type the address into a string control and directly wire that string control to this input terminal.
               •      data in —

           data in is the data to write to the shared variable.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      shared variable refnum out —

           shared variable refnum out is the reference to the shared variable or I/O variable container.

               •       error out —


5136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5137 ordinal=5137 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


DirectDirect VariableVariable ReadRead

Reads from an I/O variable or I/O variable container using direct access.


Inputs/Outputs

   •      shared variable refnum in —

    shared variable refnum in is the reference to the shared variable or I/O variable container.

    You can right-click this input terminal and select Create»Control or Create»Constant to create
     this reference. You then can click the control or constant and select Browse to display the
    Browse Variable Objects dialog box. You also can find variable references programmatically. This
    input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
    type the address into a string control and directly wire that string control to this input terminal.

   •      data type —

    data type specifies the data type of the shared variable or I/O variable container. For I/O variable
     containers, you must specify an array data type.

    This input is available only if the data type has not been previously specified. You can specify a
    data type by placing a checkmark in the Specify Data Type checkbox on the Configuration page
     of the Properties dialog box for the variable refnum. If you specify the data type upon opening
    the connection, this terminal is unavailable on subsequent read and write functions.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      shared variable refnum out —

    shared variable refnum out is the reference to the shared variable or I/O variable container.

   •      data out —


                                                    © National Instruments 5137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5138 ordinal=5138 -->
## Functions

Functions


           data out is the data read from the shared variable or I/O variable container.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      timestamp —

           timestamp is the timestamp indicating when the current data was written to the shared
              variable.

             This output is available only if you place a checkmark in the Read Timestamp checkbox on the
            Configuration page of the Properties dialog box for the variable refnum. I/O variable containers
          do not support timestamps.


       DirectDirect VariableVariable WriteWrite

       Writes to an I/O variable or I/O variable container using direct access.


      Inputs/Outputs

               •      shared variable refnum in —

           shared variable refnum in is the reference to the shared variable or I/O variable container.

           You can right-click this input terminal and select Create»Control or Create»Constant to create
              this reference. You then can click the control or constant and select Browse to display the
           Browse Variable Objects dialog box. You also can find variable references programmatically. This
            input terminal accepts string values too. If you know the exact NI-PSP variable address, you can
            type the address into a string control and directly wire that string control to this input terminal.

               •      data in —

           data in is the data to write to the shared variable.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


5138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5139 ordinal=5139 -->
## Functions

Functions


    standard error in functionality.

   •      shared variable refnum out —

    shared variable refnum out is the reference to the shared variable or I/O variable container.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

NetworkNetwork StreamsStreams

Use the Network Streams functions to stream data continuously between two LabVIEW
applications.


 Palette           Description
 Object

           Creates the writer endpoint of a network stream. This function will not run unless you Create
           also create a reader endpoint with the Create Network Stream Reader Endpoint Network            function. You either must wire the reader url input of this function or the writer url input Stream
            of the Create Network Stream Reader Endpoint function. If you do not wire either of Writer           these inputs, your endpoints will not create a network stream. Refer to the Streaming Endpoint
          Data and Sending Commands between Applications topic for more information about Function
           using this function.

 Write
 Single
           Writes a single element to a network stream. You can call this function from the writer
 Element
          endpoint only.
 to
 Stream

 Write
 Multiple
           Writes an array of elements to a network stream. You can call this function from the
 Elements
            writer endpoint only.
 to
 Stream


                                                    © National Instruments 5139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5140 ordinal=5140 -->
## Functions

Functions


         Palette                   Description
        Object

                    Transfers all data to the reader endpoint before data flow resumes. You can call this         Flush                   function from the writer endpoint only. Use this function before using the Destroy        Stream                  Endpoint function to ensure that the writer endpoint buffer is empty before you destroy         Function
                              it.

         Destroy   Destroys the specified endpoint. To completely destroy a stream and free up the
        Stream   memory allocated to that stream, you must destroy both the reader and writer
        Endpoint  endpoints. To ensure that you do not lose any data when you destroy a stream, use the
         Function  Flush Stream function before this function on the writer endpoint.

                   Creates the reader endpoint of a network stream. This function will not run unless you         Create                    also create a writer endpoint with the Create Network Stream Writer Endpoint function.        Network                 You must wire either the writer url input of this function or the reader url input of the
        Stream                   Create Network Stream Writer Endpoint function. If you do not wire either of these        Reader
                     inputs, your endpoints will not create a network stream. Refer to the Streaming Data and        Endpoint                 Sending Commands between Applications topic for more information about using this         Function
                    function.

       Read
         Single                 Reads a single element from a network stream. You can call this function from the reader        Element
                  endpoint only.        from
        Stream

       Read
         Multiple
                 Reads an array of elements from a network stream. You can call this function from the        Elements                   reader endpoint only.        from
        Stream

        Network
        Streams
                  Gets (reads) and/or sets (writes) properties of a reference.
         Property
       Node

      CreateCreate NetworkNetwork StreamStream WriterWriter EndpointEndpoint FunctionFunction

       Creates the writer endpoint of a network stream. This function will not run unless you
       also create a reader endpoint with the Create Network Stream Reader Endpoint
       function. You either must wire the reader url input of this function or the writer url
       input of the Create Network Stream Reader Endpoint function. If you do not wire either

5140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5141 ordinal=5141 -->
## Functions

Functions

of these inputs, your endpoints will not create a network stream. Refer to the
Streaming Data and Sending Commands between Applications topic for more
information about using this function.


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms specifies the time, in milliseconds, that this endpoint waits to connect to the
    other endpoint. The default value is –1, which means this endpoint waits indefinitely. If the
    timeout expires before the endpoints connect, this function returns an error.

   •       writer buffer size —

    write buffer size is the size of the writer buffer in number of elements. The minimum size is one
    element.

   •       writer name —

    writer name specifies the name of the endpoint. You can organize multiple endpoints by adding
    segments to this name. If you specify a name that already belongs to another endpoint on the
   same computer, LabVIEW creates the first endpoint that runs and returns an error on the second.
       If this endpoint resides on a computer that runs multiple applications that use network streams,
    you must assign an endpoint URL to this endpoint instead of a name.

   •      reader url —

    reader url is where you specify the URL of the reader endpoint you want to connect to. If you do
    not wire this input, this endpoint will not attempt to connect with the reader endpoint. Instead,
       it will wait for a connection from the reader endpoint. Therefore, you either must wire this input
    or the writer url input on the Create Network Stream Reader Endpoint VI to create a valid
    network stream. Refer to the Connecting Network Stream Endpoints Together topic for more
    information about these options.

   •      data type —


                                                    © National Instruments 5141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5142 ordinal=5142 -->
## Functions

Functions


           data type is the data type of the element or elements you want to write to the stream. This data
            type must match the data type input of the Create Network Stream Reader Endpoint function.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      element allocation mode —

           element allocation mode specifies whether buffer memory is allocated when the endpoint is
             created. The default mode is allocate as needed. Specifying an allocation mode only affects the
             transfer of non-scalar data types.

             allocate                      specifies that the memory required to store each data element is allocated as elements            as                    enter the buffer.
          needed
                      specifies that buffer memory allocation occurs when the endpoint is created. The
            pre-   element wired to the data type input determines the amount of memory allocated for
             allocate each element. If a larger element is added to the buffer during run-time, additional
               memory is allocated dynamically.

               •       writer endpoint —

             writer endpoint returns the reference to the writer endpoint.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      WriteWrite SingleSingle ElementElement toto StreamStream

       Writes a single element to a network stream. You can call this function from the writer
      endpoint only.


5142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5143 ordinal=5143 -->
## Functions

Functions

Inputs/Outputs

   •      endpoint in —

    endpoint in specifies the reference to the endpoint. Obtain this reference by wiring the writer
    endpoint output on the Create Network Stream Writer Endpoint function to this input.

   •      data in —

    data in is where you wire the data that you want to write to the stream.

   •      timeout ms (-1) —

    timeout in ms is the time, in milliseconds, that this function has to write the specified data to
    the stream. The default value is –1, which means there is no time limit.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      endpoint out —

    endpoint out returns endpoint in unchanged.

   •      timed out? —

    timed out? returns TRUE if the timeout period elapses before the function writes the specified
    data to the stream.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WriteWrite MultipleMultiple ElementsElements toto StreamStream

Writes an array of elements to a network stream. You can call this function from the
writer endpoint only.


                                                    © National Instruments 5143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5144 ordinal=5144 -->
## Functions

Functions

      Inputs/Outputs

               •      endpoint in —

           endpoint in specifies the reference to the endpoint. Obtain this reference by wiring the writer
           endpoint output on the Create Network Stream Writer Endpoint function to this input.

               •      data in —

           data in is the array of elements to write to the stream.

               •      timeout ms (-1) —

           timeout in ms is the time, in milliseconds, that this function has to write the specified data to
            the stream. The default value is –1, which means there is no time limit.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      endpoint out —

           endpoint out returns endpoint in unchanged.

               •      timed out? —

           timed out? returns TRUE if the timeout period elapses before the function writes the specified
            data to the stream.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      FlushFlush StreamStream FunctionFunction

       Transfers all data to the reader endpoint before data flow resumes. You can call this
       function from the writer endpoint only. Use this function before using the Destroy
      Endpoint function to ensure that the writer endpoint buffer is empty before you
       destroy it.


5144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5145 ordinal=5145 -->
## Functions

Functions


Inputs/Outputs

   •      endpoint in —

    endpoint in specifies the reference to the writer endpoint. Obtain this reference by wiring the
    endpoint out output of the Write Single Element to Stream or Write Multiple Elements to Stream
    function to this input.

   •      wait condition —

    wait condition specifies the condition under which data flow resumes.

       All Elements Read from Stream (default)—Specifies that data flow resumes when the Network
    0 Streams Engine transfers all data to the reader endpoint and the reader endpoint finishes
      reading that data.
       All Elements Available for Reading—Specifies that data flow resumes when the Network
    1 Streams Engine transfers all data to the reader endpoint but before the reader endpoint
      finishes reading that data.

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this function waits for the wait condition to
    complete. The default is -1, which means the function waits indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      endpoint out —

    endpoint out returns endpoint in unchanged.

   •      timed out? —

    timed out? returns TRUE if the wait condition does not complete within the timeout period.

   •       error out —


                                                    © National Instruments 5145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5146 ordinal=5146 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

     DestroyDestroy StreamStream EndpointEndpoint FunctionFunction

       Destroys the specified endpoint. To completely destroy a stream and free up the
     memory allocated to that stream, you must destroy both the reader and writer
       endpoints. To ensure that you do not lose any data when you destroy a stream, use the
       Flush Stream function before this function on the writer endpoint.


      Inputs/Outputs

               •      endpoint in —

           endpoint in specifies the reference to the endpoint. Obtain this reference by wiring the endpoint
           out output terminal from another Network Streams function to this one.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      CreateCreate NetworkNetwork StreamStream ReaderReader EndpointEndpoint FunctionFunction

       Creates the reader endpoint of a network stream. This function will not run unless you
       also create a writer endpoint with the Create Network Stream Writer Endpoint
       function. You must wire either the writer url input of this function or the reader url
       input of the Create Network Stream Writer Endpoint function. If you do not wire either
       of these inputs, your endpoints will not create a network stream. Refer to the

5146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5147 ordinal=5147 -->
## Functions

Functions

Streaming Data and Sending Commands between Applications topic for more
information about using this function.


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms specifies the time, in milliseconds, that this endpoint waits to connect to the
    other endpoint. The default value is –1, which means this endpoint waits indefinitely. If the
    timeout expires before the endpoints connect, this function returns an error.

   •      reader buffer size —

    reader buffer size is the size of the reader buffer in number of elements. The minimum size is
    one element.

   •      reader name —

    reader name specifies the name of the endpoint. You can organize multiple endpoints by adding
    segments to this name. If you specify a name that already belongs to another endpoint on the
   same computer, LabVIEW creates the first endpoint that runs and returns an error on the second.
       If this endpoint resides on a computer that runs multiple applications that use network streams,
    you must assign an endpoint URL to this endpoint instead of a name.

   •       writer url —

    writer url is where you specify the URL of the endpoint you want to connect to. If you do not wire
     this input, this endpoint will not attempt to connect with the writer endpoint. Instead, it will wait
     for a connection from the writer endpoint. Therefore, you either must wire this input or the
    reader url input on the Create Network Stream Writer Endpoint function to create a valid
    network stream. Refer to the Connecting Network Stream Endpoints Together topic for more
    information about these options.

   •      data type —


                                                    © National Instruments 5147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5148 ordinal=5148 -->
## Functions

Functions


           data type specifies the data type of the stream. Wire a constant or control to this input of the
          same data type as the data type input on the Create Network Stream Writer Endpoint function.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      element allocation mode —

           element allocation mode specifies whether buffer memory is allocated when the endpoint is
             created. The default mode is allocate as needed. Specifying an allocation mode only affects the
             transfer of non-scalar data types.

             allocate                      specifies that the memory required to store each data element is allocated as elements            as                    enter the buffer.
          needed
                      specifies that buffer memory allocation occurs when the endpoint is created. The
            pre-   element wired to the data type input determines the amount of memory allocated for
             allocate each element. If a larger element is added to the buffer during run-time, additional
               memory is allocated dynamically.

               •      reader endpoint —

            reader endpoint returns the reference to the reader endpoint.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     ReadRead SingleSingle ElementElement fromfrom StreamStream

      Reads a single element from a network stream. You can call this function from the
       reader endpoint only.


5148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5149 ordinal=5149 -->
## Functions

Functions

Inputs/Outputs

   •      endpoint in —

    endpoint in specifies the reference to the endpoint. Obtain this reference by wiring the reader
    endpoint output of the Create Network Stream Reader Endpoint function to this input.

   •      data type —

    data type specifies the data type of the stream. Wire a constant or control to this input of the
   same data type as the data type input on the Create Network Stream Writer Endpoint function.

   •      timeout ms (-1) —

    timeout in ms is the time, in milliseconds, that this function waits for the data. The default is –1,
    which means the function waits indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      endpoint out —

    endpoint out returns endpoint in unchanged.

   •      data out —

    data out returns the data this function reads from the stream. If timeout in ms expires before
     this function receives data, this terminal returns the default value for the data type you
    configured with the data type terminal of this function or the Create Network Stream Reader
     function.

   •      timed out? —

    timed out? returns TRUE if the timeout period elapses before this function reads the data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5150 ordinal=5150 -->
## Functions

Functions

     ReadRead MultipleMultiple ElementsElements fromfrom StreamStream

      Reads an array of elements from a network stream. You can call this function from the
       reader endpoint only.


      Inputs/Outputs

               •      # elements —

           # elements is the number of elements you want to read from the stream. The default is –1, which
              specifies to read all available elements from the stream. If you use the default value for this
             input, this function does not time out. LabVIEW ignores the timeout in ms input, and this
             function immediately returns any data available for reading. If you use the default value for this
            input and there are no elements available for reading, this function returns an empty array. If
           you specify a number greater than the read buffer size of the Create Network Stream Reader
           Endpoint function, this function returns an error. If timeout in ms expires before the elements
            are available, this function returns an empty array. Use the Available Elements for Reading
            property to determine the number of elements in the stream.

               •      endpoint in —

           endpoint in specifies the reference to the endpoint. Obtain this reference by wiring the reader
           endpoint output of the Create Network Stream Reader Endpoint function to this input.

               •      data type —

           data type is the data type of the elements you want to read. This input is available only if you
             build an array of more than one data type or you wire more than one data type to the same
           output tunnel of a structure, such as a Case Structure. Wire the data type of the elements you are
            reading from the stream to this input.

               •      timeout ms (-1) —

           timeout in ms is the time, in milliseconds, that this function waits for the data. The default is –1,
           which means the function waits indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


5150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5151 ordinal=5151 -->
## Functions

Functions


    standard error in functionality.

   •      endpoint out —

    endpoint out returns endpoint in unchanged.

   •      data out —

    data out returns the data this function reads from the stream. This terminal returns an empty
    array if an error occurs or timeout in ms expires before the number of elements you specify in
    the # elements is available.

   •      timed out? —

    timed out? returns TRUE if the timeout period elapses before this function reads the data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

NetworkNetwork StreamsStreams PropertyProperty NodeNode

Gets (reads) and/or sets (writes) properties of a reference.

The Property Node (Network Stream Endpoint) is preconfigured to access Network
Stream Endpoint properties. The node operates in the same way as a standard
Property Node.


Inputs/Outputs

   •      reference —
    reference is the refnum associated with the object for which you want to set or get properties.

       If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For
    the Application class, the default is the current application instance. For the VI class, the default


                                                    © National Instruments 5151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5152 ordinal=5152 -->
## Functions

Functions


                is the VI containing the Property Node.

           You also can wire a LabVIEW class to the reference input to access the private data of the
           LabVIEW class.

               •       error in (no error) —
             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.
               •      property 2 — property 2..n are examples of properties you want to set (write).
               •      reference —
            reference out returns reference unchanged.
               •       error out —
             error out contains error information. This output provides standard error out functionality.
               •      Property —
            property 1..n are examples of properties you want to get (read).

     LocalLocal VariableVariable

      Use local variables to read or write to one of the controls or indicators on the front
       panel of a VI.

     When you create a local variable, a local variable icon for the object appears on the
       block diagram. Writing to a local variable is similar to passing data to any other
       terminal. However, you can write to a local variable even if it is a control or read from a
        local variable even if it is an indicator. In effect, with a local variable, you can access a
       front panel object as both an input and an output.


       Inputs/Outputs

               •    —

     GlobalGlobal VariableVariable

      Use global variables to access and pass data among several VIs.


5152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5153 ordinal=5153 -->
## Functions

Functions

When you create a global variable, LabVIEW automatically creates a special global VI,
which has a front panel but no block diagram.


Inputs/Outputs

   •    —

QueueQueue OperationsOperations

Use the Queue Operations functions to create a queue for communicating data
between sections of a block diagram or from another VI.

Unlike the Notifier Operations functions, the Queue Operations functions buffer data.


 Palette            Description
 Object

 Obtain
 Queue     Returns a reference to a queue.
 Function

 Enqueue
 Element   Adds an element to the back of a queue.
 Function

 Preview
 Queue     Returns the element at the front of the queue without removing the element from the
 Element   queue.
 Function

 Get
 Queue     Returns information about the current state of a queue, such as the number of elements
 Status     currently in the queue.
 Function


                                                    © National Instruments 5153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5154 ordinal=5154 -->
## Functions

Functions


         Palette                    Description
        Object

         Release
       Queue     Releases a reference to a queue.
         Function

                 Adds an element to a queue. If no space is available in the queue, this function removes        Lossy                 an element from the front of the queue and discards the element to make space. Unlike       Enqueue                   the Enqueue Element function, this function does not wait for room in the queue to        Element                become available. Use the Obtain Queue function to set the maximum size of the         Function
                  queue.

       Enqueue
        Element
         At
                 Adds an element to the front of a queue.        Opposite
       End
         Function

       Dequeue
        Element   Removes an element from the front of a queue and returns the element.
         Function

         Flush
       Queue    Removes all elements from a queue and returns the elements as an array.
         Function

     SynchronizationSynchronization

      Use the Synchronization VIs and functions to synchronize tasks executing in parallel
      and to pass data between parallel tasks.


         Palette
                      Description
        Object

          Notifier     Use the Notifier Operations functions to suspend the execution of a block diagram
        Operations   until you receive data from another section of the block diagram or from another VI


5154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5155 ordinal=5155 -->
## Functions

Functions


 Palette              Description
 Object

             running in the same application instance.


 Queue      Use the Queue Operations functions to create a queue for communicating data
 Operations  between sections of a block diagram or from another VI.


            Use the Semaphore VIs to limit the number of tasks that can simultaneously operate
           on a shared (protected) resource. A protected resource or critical section of code Semaphore             might include writing to global variables or communicating with external
              instruments.


            Use the Rendezvous VIs to synchronize two or more separate, parallel tasks at
                specific points of execution. Each task that reaches the rendezvous waits until the Rendezvous
               specified number of tasks are waiting, at which point all tasks proceed with
              execution.


 Occurrences Use the Occurrences functions to control separate, synchronous activities.

               Indicates that a subVI or section of a block diagram is running for the first time. The First Call?                 First Call? function returns TRUE only the first time you call it after you click the Run
 Function              button.

             Passes through the values of the input wires after the upstream code executes.
 Synchronize
 Data Flow   Use this VI to synchronize multiple parallel code paths at a single point of data flow to
             ensure a certain execution order.

DataSocketDataSocket

Use the DataSocket VI and functions to pass data between VIs programmatically.

The VI and functions on this palette can return networking error codes.

                                                    © National Instruments 5155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5156 ordinal=5156 -->
## Functions

Functions

           Note LabVIEW 64-bit does not support using DataSocket connections to an
           OPC server.


         Palette Object  Description

        DataSocket    Dequeues the next available data value from the client-side buffer associated with
       Read Function  the connection you specify in connection in and returns the data.

        DataSocket
         Write          Writes data to the connection you specify in connection in.
         Function

        DataSocket     Displays a dialog box for the user to select a data source and returns the URL to
         Select URL     that data.

        DataSocket
       Open        Opens a data connection you specify in URL.
         Function

        DataSocket
         Close          Closes a data connection you specify in connection id.
         Function

     DataSocketDataSocket ReadRead FunctionFunction

      Dequeues the next available data value from the client-side buffer associated with the
       connection you specify in connection in and returns the data.

           Note Client-side buffering also applies to other protocols, such as opc and
            file. However, in some cases these servers might lose data.


5156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5157 ordinal=5157 -->
## Functions

Functions


Inputs/Outputs

   •      connection in —

    connection in identifies the data source to read.

    connection in can be a string that describes the url, a shared variable control, a connection id
    reference parameter output from a DataSocket Open function, or a connection out parameter
    output from a DataSocket Write function.

   •      type (Variant) —

    type (Variant) specifies the type of data you want to read and defines the type of the data
    output terminal. The default type is Variant, which can be any type.

    Wire any data type to this input to define the output data type. LabVIEW ignores the value of the
    input data.

   •     ms timeout (10000) —

   ms timeout specifies how long to wait for a value update to become available in the connection
     buffer.

    The function ignores this input and does not wait if wait for updated value is FALSE and an
      initial value arrived. The default is 10,000 ms (10 seconds).

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      wait for updated value (T) —

    wait for updated value causes the function to wait for an updated value if set to TRUE.

       If the connection buffer contains unprocessed data, the function returns the next available value
    immediately. Otherwise, the function waits ms timeout milliseconds for an update. If an update


                                                    © National Instruments 5157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5158 ordinal=5158 -->
## Functions

Functions


           does not occur in the timeout period, the function returns the current value and timed out is
           TRUE. If wait for updated value is FALSE, the function returns the next available value in the
            connection buffer or the last value read if no data is available.

               •       status —

             status reports warnings or errors from a PSP server or FieldPoint controller. If the 31st bit is 1,
             status indicates an error. Otherwise, status indicates a status code.

               •       quality —

             quality is the data quality of the data read from a shared variable or an NI Publish-Subscribe
            Protocol (NI-PSP) data item. Use the value of quality for information for debugging a VI.

          The following table lists some of the possible quality values.

              Bit                      Description         Number
                   The value from this shared variable might not be the most current value from the data           1                       source.
           2        Sensor failure.
           3        General device error response.
           4        Server failure.
           5        General communications failure.
                    Unable to locate variable in the Shared Variable Engine. Deployment of this variable           6                may have failed.
           7       The shared variable has no known value.
           8       The shared variable is inactive.
           10      Low Limited.
           11       High Limited.
           12       Constant.
           13       Sensor inaccurate.
           14       Engineering unit limits exceeded.
           15       Generic OPC Error.
           16      Math error.
           17      Communications link failure.
           18       NI-PSP has not connected to the server yet.
           19     DNS lookup failed for the server.
           20      The server is not reachable.
           21        Service lookup failed for the server.
           22      The connection to the server was disconnected.


5158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5159 ordinal=5159 -->
## Functions

Functions


     Bit              Description
   Number
    23      The process was not found or is not responding.
    24        Failed to resolve URL for this shared variable.
    25      Read access is denied to the shared variable.
    26        Invalid URL for this shared variable.
    30       Point has an active alarm.
    31       Subscription failed.
    32        Quality bit greater than 32 is set, or there is an error/status reported.
    33      The shared variable client-side read buffer is full.
    34      The shared variable client-side read buffer overflowed.
    35      The shared variable server-side write buffer is full.
    36      The shared variable server-side write buffer has overflowed.

   •      connection out —

    connection out is the data source that specifies the data connection.

   •      data —

    data is the result of the read. If this function times out, data returns the value that this function
     last read. If this function times out before reading any data or if the type of data is incompatible,
    data returns a value of 0, empty, or an equivalent value.

   •      timed out —

    timed out returns TRUE if the function timed out waiting for an update or an initial value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      timestamp —

    timestamp returns the timestamp data for shared variables and NI Publish-Subscribe Protocol
    (NI-PSP) data items.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 5159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5160 ordinal=5160 -->
## Functions

Functions

            • labview\examples\Data Communication\DataSocket\Simple
        DataSocket\Simple DataSocket.lvproj

     DataSocketDataSocket WriteWrite FunctionFunction

       Writes data to the connection you specify in connection in.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      connection in —

           connection in identifies the data item to write. connection in can be a string that describes the
              url or a shared variable control.

               •      data —

           data is the data written to the connection. data can be in any format or LabVIEW data type.

               •     ms timeout (0) —

         ms timeout specifies the number of milliseconds the function waits for the pending operation to
            complete.

          The default is 0, which means the function does not wait for the operation to complete. Use a
            timeout value of –1 to make the function wait until the operation completes. Currently, only the
         opc on Windows and the dstp and file protocols on all LabVIEW-supported platforms
            support nonzero timeout values for this function. You must enable synchronous notifications to
           use a nonzero timeout value with the psp protocol. When you enable synchronous notifications,
            the function waits until the operation completes or the timeout expires. You must append
         ?sync=true to the end of the psp URL to enable synchronous notifications and allow nonzero
            timeout values for write operations. Enabling synchronous notifications can cause slower
            performance, particularly on RT targets.

               •       error in (no error) —


5160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5161 ordinal=5161 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      connection out —

    connection out is the data source that specifies the data connection.

   •      timed out —

    timed out returns FALSE if the operation completed within the timeout interval with no errors. If
   ms timeout is 0, timed out is FALSE.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\DataSocket\Simple
   DataSocket\Simple DataSocket.lvproj

DataSocketDataSocket SelectSelect URLURL

Displays a dialog box for the user to select a data source and returns the URL to that
data.

Use this VI only when you do not know the URL for an object and you want to search
for a data source or target from a dialog box.


                                                    © National Instruments 5161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5162 ordinal=5162 -->
## Functions

Functions

      Inputs/Outputs

               •      Options (0) —

           Options determines whether PSP, DataSocket, or OPC items are shown in the browser. Combine
            values to show multiple types of items. For example, an input of 3 shows PSP and DataSocket
            items and an input of 7 shows all three types. The default is 0.

           1   Show PSP items
           2   Show DataSocket items
           4   Show OPC items

               •      StartURL (empty) —

           StartURL specifies the URL to open the dialog box.

           StartURL can be blank, a protocol such as file:, or an entire URL.

               •       Title (Select URL) —

              Title is the title of the dialog box.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        Filter (empty) —

               Filter inputs the filter values the dialog box uses.

               Filter currently is enabled for files only.

               •     URL Selected —

         URL Selected is TRUE if you selected a valid data source.

               •     URL —

         URL provides the URL of the selected data source.

             This value is valid only if URL Selected is TRUE.

               •       error out —


5162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5163 ordinal=5163 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

DataSocketDataSocket OpenOpen FunctionFunction

Opens a data connection you specify in URL.


Inputs/Outputs

   •     URL —

   URL identifies the data source to read or data target to write.

    URLs begin with the name of the protocol you want to use to read or write the data, such as psp,
     dstp, opc, ftp, http, and file. You also can wire a shared variable control to this terminal.

   •     mode —

   mode specifies the operation you want to perform through the data connection.

    Buffering applies when you use the DataSocket Read function to read data a server writes.
    Buffering is not available when you use front panel DataSocket data binding to read data.
    Buffering is available for front panel data binding through the Shared Variable Engine if you bind
    controls to shared variables with buffering enabled on the Network page of the Shared Variable
    Properties dialog box.

          Note To minimize data loss, you also should buffer the data on the server.


         Read
    0
           (default)
    1     Write
    2    ReadWrite
    3    BufferedRead
    4     BufferedReadWrite


                                                    © National Instruments 5163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5164 ordinal=5164 -->
## Functions

Functions

               •     ms timeout (10000) —

         ms timeout specifies the time in milliseconds to wait until LabVIEW establishes a connection.

          The default is 10,000 ms (10 seconds). If you specify –1, the function waits indefinitely. If you
             specify 0, LabVIEW does not attempt to establish a connection and returns error 56.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      connection id —

           connection id uniquely identifies the data connection.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     DataSocketDataSocket CloseClose FunctionFunction

       Closes a data connection you specify in connection id.


      Inputs/Outputs

               •      connection id —

           connection id is a connection refnum that uniquely identifies the connection.

               •     ms timeout (0) —

         ms timeout (0) specifies the number of milliseconds the function waits for the pending
            operation to complete.

          The default is 0, which means the function does not wait for the operation to complete. Use a
            timeout value of –1 to make the function wait until the operation completes.


5164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5165 ordinal=5165 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      timed out —

    timed out returns FALSE if the operation completed within the timeout interval with no errors. If
   ms timeout is 0, timed out is FALSE.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ProtocolsProtocols

Use the Protocols VIs and functions to exchange data between applications by using
protocols such as TCP/IP, UDP, serial, IrDA, Bluetooth, and SMTP.

The VIs and functions on this palette can return serial error codes and SMTP email
reply codes.


 Palette
             Description
 Object

 TCP       Use the TCP VI and functions to interface with devices on a TCP network.


 UDP       Use the UDP VI and functions to exchange data with devices on a remote UDP socket.


           Use the Serial VIs and functions to access the VISA VIs and functions that communicate
 Serial
            with devices connected to a serial port. Additional functions are also available on the


                                                    © National Instruments 5165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5166 ordinal=5166 -->
## Functions

Functions


         Palette                     Description
        Object

                    VISA palette.


                  Use the IrDA functions to establish a wireless communication link between VIs running         IrDA                 on separate computers.


                  Use the Bluetooth VIs and functions to communicate with devices that use the         Bluetooth
                    Bluetooth communication protocol.


                  Use the SMTP Email VIs to send email, including attached data and files, using the
                   Simple Mail Transfer Protocol (SMTP). You can use Transport Layer Security (TLS) to       SMTP
                  communicate with the SMTP server with added security. You also can specify        Email                     authentication credentials for the SMTP client. However, you cannot use the SMTP
                    Email VIs to receive information.


                  Use the HTTP Client VIs to build a Web client that interacts with servers, Web pages,
       HTTP      and Web services. You can add HTTP headers, store cookies, provide authentication
          Client       credentials, and send Web requests using HTTP methods such as POST, GET, PUT,
                  HEAD, and DELETE. These VIs also can interact with LabVIEW Web services.


       FTP       Use the FTP VIs to send and retrieve raw data and files to and from an FTP server.


                  Use the WebDAV VIs to transfer files securely to and from a WebDAV server. Web
       WebDAV    Distributing Authoring and Versioning (WebDAV) allows you to store, edit, and manage
                  documents and files on a web server or web share.

        Wait for
        Configured  Waits until the system can contact the remote host.
        Network

       SFTP      Use the SFTP VIs and nodes to interact with the data and files on an SFTP server.


5166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5167 ordinal=5167 -->
## Functions

Functions

TCPTCP

Use the TCP VI and functions to interface with devices on a TCP network.

The VI and functions on this palette can return networking error codes.


 Palette             Description Object

             Creates a listener and waits for an accepted TCP network connection at the specified TCP Listen
              port.

 TCP Open
 Connection Opens a TCP network connection with the address and remote port or service name.
 Function

 TCP Read   Reads a number of bytes from a TCP network connection, returning the results in data
 Function    out.

 TCP Write             Writes data to a TCP network connection. Function

 TCP Close
 Connection  Closes a TCP network connection.
 Function

 IP To String
             Converts an IP network address to a string.
 Function

 String To IP
             Converts a string to an IP network address or an array of IP network addresses.
 Function

 Resolve
             Returns the network address of the machine, which you can use with the networking
 Machine
           and VI server functions.
 Alias

             Creates a listener for a TCP network connection. Wire 0 to the port input to
 TCP Create
             dynamically choose an available TCP port the operating system determines is valid for
 Listener
              use. Use the TCP Open Connection to query the NI Service Locator for the port
 Function
           number registered with the service name.

                                                    © National Instruments 5167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5168 ordinal=5168 -->
## Functions

Functions


         Palette                     Description
        Object

       TCP Wait
      On Listener  Waits for an accepted TCP network connection.
         Function

         Transport
         Layer      Use the Transport Layer Security (TLS) functions to implement TLS connection and
         Security     secure remote communications.
         (TLS)

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\TCP\Simple
        TCP\Simple TCP.lvproj

     TCPTCP ListenListen

       Creates a listener and waits for an accepted TCP network connection at the specified
       port.


      Inputs/Outputs

               •      net address —

            net address specifies on which network address to listen. Specifying an address is useful if you
           have more than one network card, such as two Ethernet cards, and want to listen only on the
            card with the specified address. If you do not specify a network address, LabVIEW listens on all
           network addresses.

           Use the String To IP function to obtain the IP network address of the current computer.


5168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5169 ordinal=5169 -->
## Functions

Functions

•       service name —

  service name creates a known reference for the port number. If you specify a service name,
  LabVIEW registers the service name and the port number with the NI Service Locator.

•      port —

  port is the port number on which you want to listen for a connection.

•      timeout ms (wait forever: -1) —

  timeout ms specifies the time, in milliseconds, that the VI waits for a connection. If a connection
   is not established in the specified time, the VI completes and returns an error. The default value
   is –1, which indicates to wait indefinitely.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      resolve remote address (T) —

  resolve remote address indicates whether to call the IP To String function on the remote
  address. The default is TRUE.

  Refer to IP To String for more information.

•       listener ID —

  listener ID is a network connection refnum that uniquely identifies the listener.

•      connection ID —

  connection ID is a network connection refnum that uniquely identifies the TCP connection. Use
   this value to refer to this connection in subsequent VI calls.

•      remote address —

  remote address is the address of the remote machine associated with the TCP connection. If
  resolve remote address is TRUE, this address is in the form machinename.domain.com. If
  resolve remote address is FALSE, this address is in IP dot notation format such as
  128.0.0.25.

•      remote port —


                                                   © National Instruments 5169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5170 ordinal=5170 -->
## Functions

Functions


           remote port is the port the remote system uses for the connection.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When a listen on a given port begins, you cannot use another TCP Listen VI to listen on
       the same port. For example, if a VI has two TCP Listen VIs on its block diagram and you
        start a listen on port 2222 with the first TCP Listen VI, you cannot listen on port 2222
       with the second TCP Listen VI.

        Until the top level VI containing this VI goes idle, this VI maintains a table of active
        listeners and the ports on which they listen, sorted by listener ID. Subsequent calls to
        this VI reuse these listeners depending on the service name, port, and net address you
        specify. However, if you wire a value of 0 to the port terminal and an empty string to
       the service name terminal, each call to this VI creates a new listener on an open port.
       Therefore, if you wire the VI in this manner and specify any timeout other than the
        default, this VI creates a new listener on an open port each time the VI times out, which
      consumes socket resources. To free socket resources in this situation, wire the listener
       ID terminal to the TCP Close Connection function to free the port the listener uses. Or,
       wire the listener ID terminal to the TCP Wait on Listener function to listen for a
       connection on a single port.

     TCPTCP OpenOpen ConnectionConnection FunctionFunction

      Opens a TCP network connection with the address and remote port or service name.

      Use the TCP Close Connection function to close the connection.


      Inputs/Outputs

               •      address —

5170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5171 ordinal=5171 -->
## Functions

Functions


    address is the address with which you want to establish a connection. This address can be in IP
    dot notation or it can be a hostname.

       If you do not specify an address, LabVIEW establishes a connection to the local computer.
   •      remote port or service name —

    remote port or service name can accept a numeric or a string input. remote port or service
   name is the port or name of the service with which you want to establish a connection. If you
     specify a service name, LabVIEW queries the NI Service Locator for the port number that the
    server registered. If you wire a value of 0, LabVIEW returns an error.

   •      timeout ms (60000) —

    timeout ms specifies the time, in milliseconds, that the function waits to complete and return an
     error. The default value is 60,000 ms or 1 minute. A value of –1 indicates to wait indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       local port (0) —

     local port is the local connection port. Some servers only allow connections to clients that use
    port numbers within a specific range that is dependent on the server. If the value is 0, the
    operating system selects an unused port. The default is 0.

   •      connection ID —

    connection ID is a network connection refnum that uniquely identifies the TCP connection. Use
     this value to refer to this connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


When wiring an unused IP address, you may receive an error stating the network
operation exceeded the user-specified or system time limit. This error occurs before
the default timeout of 60000 ms has occurred. To correct this error, wire an IP address
that is running and listening on the port you are trying to use.


                                                    © National Instruments 5171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5172 ordinal=5172 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\TCP\TCP
        Named Service\TCP Named Service.lvproj

     TCPTCP ReadRead FunctionFunction

      Reads a number of bytes from a TCP network connection, returning the results in data
       out.


      Inputs/Outputs

               •     mode (standard) —

         mode indicates the behavior of the read operation.

            Standard (default)—Waits until all bytes you specify in bytes to read arrive or until timeout ms
           0 runs out. Returns the number of bytes read so far. If fewer bytes than the number of bytes you
             requested arrive, returns the partial number of bytes and reports a timeout error.
             Buffered—Waits until all bytes you specify in bytes to read arrive or until timeout ms runs out.
           1 If fewer bytes than the number you requested arrive, returns no bytes and reports a timeout
                error.
            CRLF—Waits until all bytes you specify in bytes to read arrive or until the function receives a CR
               (carriage return) followed by a LF (linefeed) within the number of bytes you specify in bytes to
           2
             read or until timeout ms runs out. The function returns the bytes up to and including the CR
           and LF if it finds them in the string.
            Immediate—Waits until the function receives any bytes from those you specify in bytes to
           3 read. Waits the full timeout only if the function receives no bytes. Returns the number of bytes
             so far. Reports a timeout error if the function receives no bytes.

               •      connection ID —


5172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5173 ordinal=5173 -->
## Functions

Functions


  connection ID is a network connection refnum that uniquely identifies the TCP connection.

•      bytes to read —

  bytes to read is the number of bytes to read. You must wire a value greater than 0 in order to
  read data from a network connection. The default is 0.

  Use one of the following techniques to handle messages that might vary in size:

      • Send messages that are preceded by a fixed size header that describes the message. For
      example, it might contain a command integer that identifies what kind of message follows
     and a length integer that identifies how much more data is in the message. Both the server
     and client receive messages by issuing a read function of eight bytes (assuming each is a
       four byte integer), converting them into the two integers, and using the length integer to
      determine the number of bytes to pass to a second read function for the remainder of the
      message. Once this second read is complete, each side loops back to the read function of
      the eight byte header. This technique is the most flexible, but it requires two reads to
       receive each message. In practice, the second read usually completes immediately if the
     message is written with a single write function.
      • Make each message a fixed size. When the content of a message is smaller than the fixed
       size you specify, pad the message to the fixed size. This technique is marginally more
        efficient because only a single read is required to receive a message at the expense of
      sending unnecessary data sometimes.
      • Send messages that are strictly ASCII in content, where each message is terminated by a
       carriage return and linefeed pair of characters. The read function has a mode input that,
     when passed CRLF, causes it to read until seeing a carriage return and linefeed sequence.
       This technique becomes more complicated when message data can possibly contain CRLF
      sequences, but it is quite common among many internet protocols, including POP3, FTP,
     and HTTP.
•      timeout ms (25000) —

  timeout ms specifies the time, in milliseconds, that mode waits before reporting a timeout error.

  The default is 25,000 ms. A value of –1 indicates to wait indefinitely.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      connection ID out —

  connection ID out returns the same value as connection ID.


                                                   © National Instruments 5173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5174 ordinal=5174 -->
## Functions

Functions

               •      data out —

           data out contains the data read from the TCP connection.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\TCP\TCP
        Named Service\TCP Named Service.lvproj

     TCPTCP WriteWrite FunctionFunction

       Writes data to a TCP network connection.


      Inputs/Outputs

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the TCP connection.

               •      data in —

           data in contains the data you want to write to the connection.

           Use one of the following techniques to handle messages that might vary in size:
                     • Send messages that are preceded by a fixed size header that describes the message. For
               example, it might contain a command integer that identifies what kind of message follows
              and a length integer that identifies how much more data is in the message. Both the server
              and client receive messages by issuing a read function of eight bytes (assuming each is a
                 four byte integer), converting them into the two integers, and using the length integer to
               determine the number of bytes to pass to a second read function for the remainder of the

5174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5175 ordinal=5175 -->
## Functions

Functions

        message. Once this second read is complete, each side loops back to the read function of
        the eight byte header. This technique is the most flexible, but it requires two reads to
         receive each message. In practice, the second read usually completes immediately if the
       message is written with a single write function.
         • Make each message a fixed size. When the content of a message is smaller than the fixed
          size you specify, pad the message to the fixed size. This technique is marginally more
          efficient because only a single read is required to receive a message at the expense of
        sending unnecessary data sometimes.
         • Send messages that are strictly ASCII in content, where each message is terminated by a
         carriage return and linefeed pair of characters. The read function has a mode input that,
       when passed CRLF, causes it to read until seeing a carriage return and linefeed sequence.
         This technique becomes more complicated when message data can possibly contain CRLF
        sequences, but it is quite common among many internet protocols, including POP3, FTP,
       and HTTP.
   •      timeout ms (25000) —

    timeout ms specifies the time, in milliseconds, for the function to write bytes to a device before
    the function completes and returns an error. The default value is 25,000 ms. A value of –1
     indicates to wait indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      connection ID out —

    connection ID out returns the same value as connection ID.

   •      bytes written —

    bytes written is the number of bytes the VI writes to the connection.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\TCP\TCP


                                                    © National Instruments 5175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5176 ordinal=5176 -->
## Functions

Functions

        Named Service\TCP Named Service.lvproj

     TCPTCP CloseClose ConnectionConnection FunctionFunction

       Closes a TCP network connection.


      Inputs/Outputs

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the TCP connection you
          want to close.

               •      abort (F) —

            abort is reserved for future use.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •      connection ID out —

           connection ID out has the same value as connection ID. Do not wire this output to other TCP
             functions.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.


5176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5177 ordinal=5177 -->
## Functions

Functions

  • labview\examples\Data Communication\Protocols\TCP\TCP
   Named Service\TCP Named Service.lvproj

IPIP ToTo StringString FunctionFunction

Converts an IP network address to a string.


Inputs/Outputs

   •      net address —

    net address is the unsigned numeric representation of the dot-notation format representation of
    the IP network address you want to convert.

   •      dot notation? (F) —

    dot notation? indicates whether name is in dot-notation format. The default is FALSE, which
    returns an IP address in the form machinename.domain.com. Dot-notation format returns
    an IP address in the form 128.0.0.25.

   •     name —

   name is the string equivalent of net address.


StringString ToTo IPIP FunctionFunction

Converts a string to an IP network address or an array of IP network addresses.


Inputs/Outputs

   •     name —


                                                    © National Instruments 5177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5178 ordinal=5178 -->
## Functions

Functions


         name is the string you want to convert. If empty, net address is the IP network address of the
             current machine.

               •      net address —

            net address is the IP network address equivalent to name; it is the unsigned numeric
            representation of the dot-notation format representation of the IP network address.


      The String To IP function accepts standard decimal, octal, or a combination of both
      number systems. If you enter a leading zero into a string, the String To IP function
        interprets the string as an octal number.

           If String To IP is in single output mode, the net address is the first result returned by
       the operating system resolver. If String To IP is in multiple output mode, the result is an
       array of all IP network addresses returned by the operating system resolver. If the node
         fails to convert the string, the result is a value of zero in single output mode or an
      empty array in multiple output mode.

      To switch between single output and multiple output modes, right-click the node and
        select Multiple output from the shortcut menu.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\UDP\UDP
        Multicast\UDP Multicast.lvproj

      ResolveResolve MachineMachine AliasAlias

       Returns the network address of the machine, which you can use with the networking
      and VI server functions.


5178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5179 ordinal=5179 -->
## Functions

Functions

Inputs/Outputs

   •     App Refnum —

   App Refnum is a reference to a LabVIEW application.

   •      Machine Alias —

    Machine Alias is the alias for the computer.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     App Refnum Out —

   App Refnum Out passes the application reference specified by App Refnum.

   •     Network Identity —

    Network Identity is the network address, such as the IP address, for the machine.

       If this VI cannot resolve the machine alias, the VI returns an error and returns as the value of
    Machine Alias as the value of Network Identity.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Resolve Machine Alias VI returns the network address of the machine alias
specified in the LabVIEW project .aliases file. This .aliases file is automatically
updated with mappings that you specify in the LabVIEW project. You can extend the set
of mappings in the .aliases file. If you extend the mappings of the .aliases file
and you check the LabVIEW project into source control, then you also need to check
the .aliases file into source control.
TCPTCP CreateCreate ListenerListener FunctionFunction

Creates a listener for a TCP network connection. Wire 0 to the port input to
dynamically choose an available TCP port the operating system determines is valid for
use. Use the TCP Open Connection to query the NI Service Locator for the port number

                                                    © National Instruments 5179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5180 ordinal=5180 -->
## Functions

Functions

       registered with the service name.


      Inputs/Outputs

               •      net address —

            net address specifies on which network address to listen. Specifying an address is useful if you
           have more than one network card, such as two Ethernet cards, and want to listen only on the
            card with the specified address. If you do not specify a network address, LabVIEW listens on all
           network addresses.

           Use the String To IP function to obtain the IP network address of the current computer.
               •       service name —

             service name creates a known reference for the port number. If you specify a service name,
           LabVIEW registers the service name and the port number with the NI Service Locator.

               •      port —

            port is the port number on which you want to listen for a connection.

               •      timeout ms (25000) —

           timeout ms specifies the time, in milliseconds, that the function waits before the function
           completes and returns an error. The default value is 25,000 ms or 25 seconds. A value of -1
             indicates to wait indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       listener ID —

              listener ID is a network connection refnum that uniquely identifies the listener.

               •      port —


5180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5181 ordinal=5181 -->
## Functions

Functions


    port returns the port number the function used. If the input port is not zero, the output port
   number equals the input port number. Wire 0 to the port input to dynamically choose an
     available TCP port the operating system determines is valid for use.

    As defined by the Internet Assigned Numbers Authority (IANA), valid port numbers are between
    the range of 49152 through 65535. Well Known Ports are between the range of 0 through 1023
    and Registered Ports are between the range of 1024 through 49151. Not all operating systems
    follow the IANA standard; for example, Windows returns dynamic ports between the range of
    1024 through 5000.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\TCP\TCP
   Named Service\TCP Named Service.lvproj

TCPTCP WaitWait OnOn ListenerListener FunctionFunction

Waits for an accepted TCP network connection.


Inputs/Outputs

   •       listener ID in —

     listener ID in is a network connection refnum that uniquely identifies the listener.

   •      resolve remote address (T) —

    resolve remote address indicates whether to call the IP To String function on the remote


                                                    © National Instruments 5181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5182 ordinal=5182 -->
## Functions

Functions


            address. The default is TRUE.

             Refer to IP To String for more information.
               •      timeout ms (wait forever: -1) —

           timeout ms specifies the time, in milliseconds, that the function waits for a connection. If a
            connection is not established in the specified time, the function returns an error. The default
            value is –1, which indicates to wait indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       listener ID out —

              listener ID out has the same value as listener ID in. Use this value to refer to the listener in
           subsequent calls to this function.

               •      remote address —

           remote address is the address of the remote machine associated with the TCP connection. If
            resolve remote address is TRUE, this address is in the form machinename.domain.com. If
            resolve remote address is FALSE, this address is in IP dot notation format such as
          128.0.0.25.

               •      remote port —

           remote port is the port the remote system uses for the connection.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the TCP connection. Use
              this value to refer to this connection in subsequent VI calls.


     Examples

       Refer to the following example files included with LabVIEW.


5182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5183 ordinal=5183 -->
## Functions

Functions

  • labview\examples\Data Communication\Protocols\TCP\TCP
   Named Service\TCP Named Service.lvproj

TransportTransport LayerLayer SecuritySecurity (TLS)(TLS)

Use the Transport Layer Security (TLS) functions to implement TLS connection and
secure remote communications.


 Palette Object   Description

                 Creates a Transport Layer Security (TLS) configuration. After creating a TLS
 New TLS                   configuration, you must use the Make TLS Configuration Immutable function to Configuration              make the configuration immutable before using the configuration to start or
 Function                 accept a TLS connection.

 Make TLS
               Makes a Transport Layer Security (TLS) configuration immutable. You must make Configuration               a TLS configuration immutable before applying the TLS configuration to a TCP Immutable
                 connection using the Start TLS function or Accept TLS function. Function

 Close TLS
 Configuration    Closes a Transport Layer Security (TLS) configuration.
 Function

 TLS                  Detects whether a TCP connection is encrypted with Transport Layer Security Connection?
                    (TLS). Function

 Load
 Certificates Into
                Loads one or more X.509 certificates into the local memory.
 Memory
 Function

 Add Trusted
 Certificate To
               Adds a Certificate Authority (CA) certificate to a Transport Layer Security (TLS)
 TLS
                  configuration and marks the certificate as trusted.
 Configuration
 Function

 Start TLS        Negotiates a Transport Layer Security (TLS) connection on the specified TCP
 Function        socket as a client. If successful, the connection is transparently encrypted.


                                                    © National Instruments 5183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5184 ordinal=5184 -->
## Functions

Functions


         Palette Object   Description

                         Otherwise, the connection is closed.

        Load Private
        Key Into                       Loads an X.509 private key into the local memory.       Memory
         Function

       Add Private Key
        To TLS         Adds a signed private key to a Transport Layer Security (TLS) configuration. The
         Configuration    function is optional for clients but required for servers.
         Function

                         Negotiates a Transport Layer Security (TLS) connection on the specified TCP        Accept TLS                         socket as a server. If successful, the connection is transparently encrypted.         Function
                         Otherwise, the connection is closed.

   NewNew TLSTLS ConfigurationConfiguration FunctionFunction

       Creates a Transport Layer Security (TLS) configuration. After creating a TLS
       configuration, you must use the Make TLS Configuration Immutable function to make
       the configuration immutable before using the configuration to start or accept a TLS
       connection.


      Inputs/Outputs

               •      load OS trusted CAs? —

            load OS trusted CAs? specifies whether to load Certificate Authority (CA) certificates trusted by
            the OS into the new TLS configuration. The default is TRUE. If FALSE, no certificates are trusted
           by default. Use the Add Trusted Certificate To TLS Configuration function to explicitly trust
             individual certificates.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides


5184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5185 ordinal=5185 -->
## Functions

Functions


    standard error in functionality.

   •     TLS configuration out —

    TLS configuration out returns a reference to the new, mutable TLS configuration. Wire this
    output to the Make TLS Configuration Immutable function to make the TLS configuration
    immutable.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\TLS\Connect
   to TLS Server.vi
MakeMake TLSTLS ConfigurationConfiguration ImmutableImmutable FunctionFunction

Makes a Transport Layer Security (TLS) configuration immutable. You must make a TLS
configuration immutable before applying the TLS configuration to a TCP connection
using the Start TLS function or Accept TLS function.


Inputs/Outputs

   •     TLS configuration —

    TLS configuration specifies the reference to the TLS configuration.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 5185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5186 ordinal=5186 -->
## Functions

Functions


            standard error in functionality.

               •     TLS configuration out —

          TLS configuration out returns a reference to the new, immutable TLS configuration. Use this
           output to refer to this TLS configuration in subsequent function calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\TLS\Connect
        to TLS Server.vi
   CloseClose TLSTLS ConfigurationConfiguration FunctionFunction

       Closes a Transport Layer Security (TLS) configuration.


      Inputs/Outputs

               •     TLS configuration —

          TLS configuration specifies the reference to the TLS configuration.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —


5186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5187 ordinal=5187 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

TLSTLS Connection?Connection? FunctionFunction

Detects whether a TCP connection is encrypted with Transport Layer Security (TLS).


Inputs/Outputs

   •     TCP connection —

   TCP connection specifies the network connection reference that uniquely identifies the TCP
    connection.

   •      TLS? —

    TLS? returns TRUE when TCP connection is encrypted with TLS; returns FALSE when TCP
    connection is not encrypted with TLS.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\TLS\TLS
   Client and Server with Self-Signed Server Certificate.vi
LoadLoad CertificatesCertificates IntoInto MemoryMemory FunctionFunction

Loads one or more X.509 certificates into the local memory.


                                                    © National Instruments 5187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5188 ordinal=5188 -->
## Functions

Functions


      Inputs/Outputs

               •      path —

           path specifies the file path of the certificate(s) on disk.

               •      format —

           format specifies the format of the certificate(s). The default is X.509 (PEM).

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       certificates —

              certificates returns the loaded certificates in an array. Each certificate is a byte array in
             Distinguished Encoding Rules (DER) format. Use this output as the input to the Add Trusted
              Certificate To TLS Configuration function.

                     •       certificate —


               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\TLS\TLS
        Client and Server with Self-Signed Server Certificate.vi


5188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5189 ordinal=5189 -->
## Functions

Functions

AddAdd TrustedTrusted CertificateCertificate ToTo TLSTLS ConfigurationConfiguration
FunctionFunction

Adds a Certificate Authority (CA) certificate to a Transport Layer Security (TLS)
configuration and marks the certificate as trusted.


Inputs/Outputs

   •     TLS configuration —

    TLS configuration specifies the reference to the TLS configuration.

   •       certificate —

     certificate specifies a byte array of the Distinguished Encoding Rules (DER) certificate. If the
     certificate is not for a Certificate Authority (CA), this function returns an error.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     TLS configuration out —

    TLS configuration out returns a reference to the TLS configuration with the trusted certificate
    you specify.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 5189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5190 ordinal=5190 -->
## Functions

Functions

            • labview\examples\Data Communication\Protocols\TLS\TLS
        Client and Server with Self-Signed Server Certificate.vi
    StartStart TLSTLS FunctionFunction

       Negotiates a Transport Layer Security (TLS) connection on the specified TCP socket as
      a client. If successful, the connection is transparently encrypted. Otherwise, the
       connection is closed.


      Inputs/Outputs

               •      timeout ms —

           timeout ms specifies the time, in milliseconds, that the function waits before timing out. A value
             of –1 indicates to wait indefinitely. The default value is 25000.

               •     TCP connection —

          TCP connection specifies the network connection reference that uniquely identifies the TCP
            connection.

               •     immutable TLS configuration —

          immutable TLS configuration specifies the reference to the immutable TLS configuration.

               •      server hostname —

            server hostname specifies the hostname of the server you are connecting. This function checks
            server hostname and fails TLS negotiation if server hostname does not match the hostname
             indicated in the server certificate. This function skips the check if server hostname is
             unspecified.

               •       error in —


5190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5191 ordinal=5191 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      server certificate validation —

    server certificate validation specifies the requirements for the server certificate.

     Any Trusted CA (default)—Requires a server certificate signed by any OS-provided certificate
    0 authority (CA) or by a CA explicitly added using the Add Trusted Certificate To TLS
      Configuration function.
    None—Does not require a server certificate. When you choose this option, the TLS connection
      provides confidentiality, but not authentication.

    1       Note Choosing this option introduces a security vulnerability. Only use this option
                for debugging and development purposes. Do not use this option in deployed
              systems.


   •     TLS connection —

    TLS connection returns a network connection reference that uniquely identifies the TLS
    connection. Use this value to refer to this TLS connection in subsequent function calls.

   •      server certificate chain —

    server certificate chain returns an array of Distinguished Encoding Rules (DER) certificates
    provided by the server. The first element of the array is the certificate of the server.

         •       certificate —


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\TLS\Connect


                                                    © National Instruments 5191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5192 ordinal=5192 -->
## Functions

Functions

        to TLS Server.vi
   LoadLoad PrivatePrivate KeyKey IntoInto MemoryMemory FunctionFunction

      Loads an X.509 private key into the local memory.


      Inputs/Outputs

               •      path —

           path specifies the file path of the private key on disk.

               •      format —

           format specifies the format of the private key.

           0     PKCS#8 (PEM)
           1     PKCS#8 (DER)

               •      password —

           password specifies the password to decrypt encrypted PEM private keys. The default is an
          empty string.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       private key —
             private key returns the private key in Distinguished Encoding Rules (DER) format. Use this
           output as the input to the Add Private Key To TLS Configuration function.

                Caution Disclosure of the private key compromises the security of your application.

               •       error out —

5192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5193 ordinal=5193 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\TLS\TLS
   Client and Server with Self-Signed Server Certificate.vi
AddAdd PrivatePrivate KeyKey ToTo TLSTLS ConfigurationConfiguration
FunctionFunction

Adds a signed private key to a Transport Layer Security (TLS) configuration. The
function is optional for clients but required for servers.


Inputs/Outputs

   •     TLS configuration —

    TLS configuration specifies the reference to the TLS configuration.

   •       private key —

    private key specifies the location of the private key in the local memory.

   •       certificate chain —

     certificate chain specifies an array of Distinguished Encoding Rules (DER) certificates. The
     certificates must be supplied depth-first: the server's certificate, followed by the Certificate
    Authority (CA) that signs the certificate of the server, on up to the root CA. Use the Load
     Certificates Into Memory function to construct this array.


                                                    © National Instruments 5193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5194 ordinal=5194 -->
## Functions

Functions


                     •       certificate —


               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     TLS configuration out —

          TLS configuration out returns a reference to the TLS configuration with the private key you
              specify.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\TLS\TLS
        Client and Server with Self-Signed Server Certificate.vi
   AcceptAccept TLSTLS FunctionFunction

       Negotiates a Transport Layer Security (TLS) connection on the specified TCP socket as
      a server. If successful, the connection is transparently encrypted. Otherwise, the
       connection is closed.


      Inputs/Outputs

               •      timeout ms —


5194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5195 ordinal=5195 -->
## Functions

Functions


    timeout ms specifies the time, in milliseconds, that the function waits before timing out. A value
     of –1 indicates to wait indefinitely. The default value is 25000.

   •     TCP connection —

   TCP connection specifies the network connection reference that uniquely identifies the TCP
    connection.

   •     immutable TLS configuration —

    immutable TLS configuration specifies the reference to the immutable TLS configuration.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     TLS connection —

    TLS connection returns a network connection reference that uniquely identifies the TLS
    connection. Use this value to refer to this TLS connection in subsequent function calls.

   •       client certificate chain —

     client certificate chain returns an array of Distinguished Encoding Rules (DER) certificates
    provided by the client. The first element of the array is the certificate of the client.

         •       certificate —


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\TLS\TLS
   Client and Server with Self-Signed Server Certificate.vi


                                                    © National Instruments 5195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5196 ordinal=5196 -->
## Functions

Functions

    UDPUDP

      Use the UDP VI and functions to exchange data with devices on a remote UDP socket.

      The VI and functions on this palette can return networking error codes.


         Palette Object  Description

      UDP Open                    Opens a UDP socket on the port or service name.
         Function

      UDP Multicast  Opens a UDP multicast socket on the port. You must manually select the
       Open         polymorphic instance you want to use.

      UDP Read
                     Reads a datagram from a UDP socket, returning the results in data out.         Function

      UDP Write                        Writes to a remote UDP socket.         Function

      UDP Close                        Closes a UDP socket.         Function

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\UDP\Simple
        UDP\Simple UDP.lvproj

     UDPUDP OpenOpen FunctionFunction

      Opens a UDP socket on the port or service name.

       Close the socket with the UDP Close function. Use the UDP Multicast Open VI instead of
        this function to open connections capable of reading, writing, or reading and writing


5196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5197 ordinal=5197 -->
## Functions

Functions

data to or from UDP Multicast sockets. Use the UDP Write function to query the NI
Service Locator for the port number registered with the service name.


Inputs/Outputs

   •      net address —

    net address specifies on which network address to listen. Specifying an address is useful if you
    have more than one network card, such as two Ethernet cards, and want to listen only on the
    card with the specified address. If you do not specify a network address, LabVIEW listens on all
    network addresses. This function broadcasts only on the default network address.

    Use the String To IP function to obtain the IP network address of the current computer.

    (VxWorks) You cannot send a broadcast from a network card on a target that runs VxWorks and
    receive the broadcast on that same network card.

     (Linux, Mac, VxWorks) If you wire this terminal, you cannot receive broadcasts.

   •      port —

    port is the local port with which you want to create a UDP socket.

   •       service name —

    service name creates a known reference for the port number. If you specify a service name,
    LabVIEW registers the service name and the port number with the NI Service Locator.

   •      timeout ms (25000) —

    timeout ms specifies the time, in milliseconds, that the function waits before the function
    completes and returns an error. The default value is 25,000 ms or 25 seconds. A value of -1
     indicates to wait indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 5197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5198 ordinal=5198 -->
## Functions

Functions


            standard error in functionality.

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the UDP socket. Use this
            value to refer to this socket in subsequent VI calls.

               •      port —

            port returns the port number the function used. If the input port is not zero, the output port
          number equals the input port number. Wire 0 to the port input to dynamically choose an
             available UDP port the operating system determines is valid for use.

           As defined by the Internet Assigned Numbers Authority (IANA), valid port numbers are between
            the range of 49152 through 65535. Well Known Ports are between the range of 0 through 1023
          and Registered Ports are between the range of 1024 through 49151. Not all operating systems
             follow the IANA standard; for example, Windows returns dynamic ports between the range of
           1024 through 5000.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\UDP\Simple
        UDP\Simple UDP.lvproj
            • labview\examples\Data Communication\Protocols\UDP\UDP
        Named Service\UDP Named Service.lvproj

     UDPUDP MulticastMulticast OpenOpen

      Opens a UDP multicast socket on the port. You must manually select the polymorphic
       instance you want to use.


5198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5199 ordinal=5199 -->
## Functions

Functions

  • UDP Multicast Read-Only Open VI
  • UDP Multicast Read-Write Open VI
  • UDP Multicast Write-Only Open VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\UDP\UDP
   Multicast\UDP Multicast.lvproj
UDPUDP MulticastMulticast Read-OnlyRead-Only OpenOpen VIVI

Opens a UDP multicast socket on the port. You must manually select the polymorphic
instance you want to use.


Inputs/Outputs

   •      net address —

    net address specifies on which network address to listen. Specifying an address is useful if you
    have more than one network card, such as two Ethernet cards, and want to listen only on the
    card with the specified address. If you do not specify a network address, LabVIEW listens on all
    network addresses. This VI broadcasts only on the default network address.

    Use the String To IP function to obtain the IP network address of the current computer.

   •      port —

    port is the local port with which you want to create a UDP socket.

   •      multicast addr —

    multicast addr is the IP address of the multicast group you want to join.


                                                    © National Instruments 5199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5200 ordinal=5200 -->
## Functions

Functions


                    If you do not specify an address, you do not join a multicast group, and the connection returned
                is write only. Multicast group addresses are in the 224.0.0.0 to 239.255.255.255 range.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the UDP socket. Use this
            value to refer to this socket in subsequent VI calls.

               •      port out —

            port out returns the port number the function used. If the input port is not zero, the output port
          number equals the input port number. Wire 0 to the port input to dynamically choose an
             available UDP port the operating system determines is valid for use.

           As defined by the Internet Assigned Numbers Authority (IANA), valid port numbers are between
            the range of 49152 through 65535. Well Known Ports are between the range of 0 through 1023
          and Registered Ports are between the range of 1024 through 49151. Not all operating systems
             follow the IANA standard; for example, Windows returns dynamic ports between the range of
           1024 through 5000.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\UDP\UDP
        Multicast\UDP Multicast.lvproj
   UDPUDP MulticastMulticast Read-WriteRead-Write OpenOpen VIVI

      Opens a UDP multicast socket on the port. You must manually select the polymorphic
       instance you want to use.

5200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5201 ordinal=5201 -->
## Functions

Functions


Inputs/Outputs

   •      net address —

    net address specifies on which network address to listen. Specifying an address is useful if you
    have more than one network card, such as two Ethernet cards, and want to listen only on the
    card with the specified address. If you do not specify a network address, LabVIEW listens on all
    network addresses. This VI broadcasts only on the default network address.

    Use the String To IP function to obtain the IP network address of the current computer.

   •      port —

    port is the local port with which you want to create a UDP socket.

   •      multicast addr —

    multicast addr is the IP address of the multicast group you want to join.

       If you do not specify an address, you do not join a multicast group, and the connection returned
      is write only. Multicast group addresses are in the 224.0.0.0 to 239.255.255.255 range.

   •       time-to-live (1) —

     time-to-live specifies the number of routers, minus 1, to forward a datagram. The TTL value
    applies to all datagrams sent using this socket.

    The following table lists what action occurs to a multicast datagram when you specify a value for
    the TTL parameter. The default value is 1.

    0 Datagram is sent and routers forward it through TTL-1 layers.
    0 Datagram remains on the host computer.
     Datagram sent to every client on the same local subnet that subscribes to that IP address.
    1 Hubs/repeaters and bridges/switches forward the datagram. Routers do not forward the
     datagram if the TTL is 1.

   •       error in (no error) —


                                                    © National Instruments 5201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5202 ordinal=5202 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the UDP socket. Use this
            value to refer to this socket in subsequent VI calls.

               •      port out —

            port out returns the port number the function used. If the input port is not zero, the output port
          number equals the input port number. Wire 0 to the port input to dynamically choose an
             available UDP port the operating system determines is valid for use.

           As defined by the Internet Assigned Numbers Authority (IANA), valid port numbers are between
            the range of 49152 through 65535. Well Known Ports are between the range of 0 through 1023
          and Registered Ports are between the range of 1024 through 49151. Not all operating systems
             follow the IANA standard; for example, Windows returns dynamic ports between the range of
           1024 through 5000.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\UDP\UDP
        Multicast\UDP Multicast.lvproj
   UDPUDP MulticastMulticast Write-OnlyWrite-Only OpenOpen VIVI

      Opens a UDP multicast socket on the port. You must manually select the polymorphic
       instance you want to use.


5202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5203 ordinal=5203 -->
## Functions

Functions


Inputs/Outputs

   •      net address —

    net address specifies on which network address to listen. Specifying an address is useful if you
    have more than one network card, such as two Ethernet cards, and want to listen only on the
    card with the specified address. If you do not specify a network address, LabVIEW listens on all
    network addresses. This VI broadcasts only on the default network address.

    Use the String To IP function to obtain the IP network address of the current computer.

   •      port —

    port is the local port with which you want to create a UDP socket.

   •       time-to-live (1) —

     time-to-live specifies the number of routers, minus 1, to forward a datagram. The TTL value
    applies to all datagrams sent using this socket.

    The following table lists what action occurs to a multicast datagram when you specify a value for
    the TTL parameter. The default value is 1.

    0 Datagram is sent and routers forward it through TTL-1 layers.
    0 Datagram remains on the host computer.
     Datagram sent to every client on the same local subnet that subscribes to that IP address.
    1 Hubs/repeaters and bridges/switches forward the datagram. Routers do not forward the
     datagram if the TTL is 1.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      connection ID —

    connection ID is a network connection refnum that uniquely identifies the UDP socket. Use this
    value to refer to this socket in subsequent VI calls.

   •       error out —

                                                    © National Instruments 5203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5204 ordinal=5204 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\UDP\UDP
        Multicast\UDP Multicast.lvproj

     UDPUDP ReadRead FunctionFunction

      Reads a datagram from a UDP socket, returning the results in data out.

      The function returns data when it receives any bytes, and waits the full timeout ms
       only if it receives no bytes.


      Inputs/Outputs

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the UDP socket.

               •     max size (548) —

         max size is the maximum number of bytes to read. The default is 548.

           (Windows) If you wire a value other than 548 to this input, Windows might return an error
           because the function cannot read fewer bytes than are in a packet.
               •      timeout ms (25000) —

           timeout ms specifies the time, in milliseconds, that the function waits for bytes. If no bytes have
          been received within the specified time, the function completes and returns an error.

          The default is 25,000 ms. A value of –1 indicates to wait indefinitely.

5204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5205 ordinal=5205 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      connection ID out —

    connection ID out returns the same value as connection ID.

   •      data out —

    data out contains the data read from the UDP datagram.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      port —

    port is the port of the UDP socket that sent the datagram.

   •      address —

    address is the address of the computer where a datagram originates.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\UDP\UDP
   Multicast\UDP Multicast.lvproj
  • labview\examples\Data Communication\Protocols\UDP\Simple
   UDP\Simple UDP.lvproj

UDPUDP WriteWrite FunctionFunction

Writes to a remote UDP socket.


                                                    © National Instruments 5205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5206 ordinal=5206 -->
## Functions

Functions


      Inputs/Outputs

               •      port or service name —

            port or service name can accept a numeric or string input. port or service name identifies what
            port to write to. If you specify a service name, LabVIEW queries the NI Service Locator for the
            port number that the server registered.

               •      address —

           address is the address of the computer where you want to send a datagram.

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the UDP socket.

               •      data in —

           data in contains the data to write to another UDP socket.

              In an Ethernet environment, restrict data to 8192 bytes. In a LocalTalk environment, restrict data
             to 1458 bytes to maintain gateway performance.
               •      timeout ms (25000) —

           timeout ms specifies the time, in milliseconds, that the function waits before the function
           completes and returns an error. The default value is 25,000 ms or 25 seconds. A value of -1
             indicates to wait indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      connection ID out —

           connection ID out returns the same value as connection ID.

               •       error out —


5206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5207 ordinal=5207 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\UDP\UDP
   Multicast\UDP Multicast.lvproj
  • labview\examples\Data Communication\Protocols\UDP\Simple
   UDP\Simple UDP.lvproj
  • labview\examples\Data Communication\Protocols\UDP\UDP
   Named Service\UDP Named Service.lvproj

UDPUDP CloseClose FunctionFunction

Closes a UDP socket.


Inputs/Outputs

   •      connection ID —

    connection ID is a network connection refnum that uniquely identifies the UDP socket you want
    to close.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      connection ID out —

    connection ID out has the same value as connection ID. Do not wire this output to other UDP


                                                    © National Instruments 5207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5208 ordinal=5208 -->
## Functions

Functions


             functions.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\UDP\UDP
        Multicast\UDP Multicast.lvproj
            • labview\examples\Data Communication\Protocols\UDP\Simple
        UDP\Simple UDP.lvproj

      SerialSerial

      Use the Serial VIs and functions to access the VISA VIs and functions that communicate
       with devices connected to a serial port. Additional functions are also available on the
       VISA palette.

      The VIs and functions on this palette can return serial error codes.


         Palette
                      Description
        Object

        VISA           Initializes the serial port specified by VISA resource name to the specified settings.
         Configure    Wire data to the VISA resource name input to determine the polymorphic instance to
          Serial Port   use or manually select the instance.

        VISA Write    Writes the data from write buffer to the device or interface specified by VISA
         Function     resource name.

        VISA Read    Reads the specified number of bytes from the device or interface specified by VISA


5208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5209 ordinal=5209 -->
## Functions

Functions


 Palette              Description
 Object

 Function     resource name and returns the data in read buffer.

 VISA Close              Closes a device session or event object specified by VISA resource name. Function

 VISA Bytes
 at Serial      Returns the number of bytes in the input buffer of the specified serial port.
 Port

 VISA Serial   Sends a break on the specified output port. Wire data to the VISA resource name
 Break        input to determine the polymorphic instance to use or manually select the instance.

 VISA Set I/O              Sets the size of the I/O buffer. Run the VISA Configure Serial Port VI first if you are Buffer Size               setting the size of a serial port buffer.
 Function

 VISA Flush
 I/O Buffer    Flushes the I/O buffer specified by mask.
 Function

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Instrument IO\Serial\Serial.lvproj

IrDAIrDA

Use the IrDA functions to establish a wireless communication link between VIs running
on separate computers.


 Palette Object   Description

 IrDA Discover    Finds any IrDA-enabled devices within a detectable wireless boundary and
 Function         returns the ID and name of each device and the number of devices detected.


                                                    © National Instruments 5209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5210 ordinal=5210 -->
## Functions

Functions


         Palette Object   Description

         IrDA Open
        Connection     Opens an infrared connection to another IrDA-enabled device.
         Function

         IrDA Read       Reads the number of bytes specified in bytes to read from the IrDA connection
         Function         specified in the connection ID.

         IrDA Write                      Sends string data to the IrDA connection specified by connection ID.         Function

         IrDA Close                         Closes the open infrared connection to the IrDA device specified by connection
        Connection                              ID.         Function

         IrDA Create                          Creates a listener for an IrDA connection on a wireless network using the service
         Listener                   name and returns listener ID.         Function

         IrDA Wait On
         Listener         Waits for the designated IrDA listener to accept an IrDA network connection.
         Function

       IrDAIrDA DiscoverDiscover FunctionFunction

       Finds any IrDA-enabled devices within a detectable wireless boundary and returns the
       ID and name of each device and the number of devices detected.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     number of devices —

          number of devices indicates how many IrDA devices the function currently detects on the


5210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5211 ordinal=5211 -->
## Functions

Functions


     wireless network.

   •      device list —

    device list returns a list of devices the function detects on the wireless network.

         •      Device ID —

        device id identifies a device on the IrDA network. Use this ID to open a connection to a
          server.

         •      Device Name —

        device name indicates the name of an IrDA device detected.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


IrDAIrDA OpenOpen ConnectionConnection FunctionFunction

Opens an infrared connection to another IrDA-enabled device.

Close the connection with the IrDA Close Connection function.


Inputs/Outputs

   •       service name —

    service name specifies the IrDA service you want to connect to.

   •      remote device id —

    remote device id is the device ID of the remote IrDA device on the IrDA network. Use the IrDA


                                                    © National Instruments 5211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5212 ordinal=5212 -->
## Functions

Functions


            Discover function to locate the device ID.

               •      timeout ms (60000) —

           timeout ms specifies the time, in milliseconds, that the function waits to complete and return an
               error. The default value is 60,000 ms or 1 minute. A value of –1 indicates to wait indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      connection ID —

           connection ID is an IrDA connection refnum that uniquely identifies the IrDA connection. Use
              this value to refer to this connection in subsequent IrDA function calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\IrDA\Simple
        IrDA\Simple IrDA.lvproj

       IrDAIrDA ReadRead FunctionFunction

      Reads the number of bytes specified in bytes to read from the IrDA connection
       specified in the connection ID.


      Inputs/Outputs

               •     mode (standard) —


5212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5213 ordinal=5213 -->
## Functions

Functions


  mode indicates the behavior of the read operation.

   Standard (default)—Waits until all bytes you specify in bytes to read arrive or until timeout ms
  0 runs out. Returns the number of bytes read so far. If fewer bytes than the number of bytes you
   requested arrive, returns the partial number of bytes and reports a timeout error.
   Buffered—Waits until all bytes you specify in bytes to read arrive or until timeout ms runs out.
  1 If fewer bytes than the number you requested arrive, returns no bytes and reports a timeout
    error.
   CRLF—Waits until all bytes you specify in bytes to read arrive or until the function receives a CR
    (carriage return) followed by a LF (linefeed) within the number of bytes you specify in bytes to  2   read or until timeout ms runs out. The function returns the bytes up to and including the CR
   and LF if it finds them in the string.
   Immediate—Waits until the function receives any bytes from those you specify in bytes to
  3 read. Waits the full timeout only if the function receives no bytes. Returns the number of bytes
   so far. Reports a timeout error if the function receives no bytes.

•      connection ID —

  connection ID is an IrDA connection refnum that uniquely identifies the IrDA connection.

•      bytes to read —

  bytes to read indicates how many bytes the function reads from the IrDA device. Use one of the
  following techniques to handle messages that might vary in size:

      • Send messages that are preceded by a fixed size header that describes the message. For
      example, it might contain a command integer that identifies what kind of message follows
     and a length integer that identifies how much more data is in the message. Both the server
     and client receive messages by issuing a read function of eight bytes (assuming each is a
       four byte integer), converting them into the two integers, and using the length integer to
      determine the number of bytes to pass to a second read function for the remainder of the
      message. Once this second read is complete, each side loops back to the read function of
      the eight byte header. This technique is the most flexible, but it requires two reads to
       receive each message. In practice, the second read usually completes immediately if the
     message is written with a single write function.
      • Make each message a fixed size. When the content of a message is smaller than the fixed
       size you specify, pad the message to the fixed size. This technique is marginally more
        efficient because only a single read is required to receive a message at the expense of
      sending unnecessary data sometimes.
      • Send messages that are strictly ASCII in content, where each message is terminated by a
       carriage return and linefeed pair of characters. The read function has a mode input that,
     when passed CRLF, causes it to read until seeing a carriage return and linefeed sequence.


                                                   © National Instruments 5213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5214 ordinal=5214 -->
## Functions

Functions

                 This technique becomes more complicated when message data can possibly contain CRLF
                sequences, but it is quite common among many internet protocols, including POP3, FTP,
              and HTTP.
               •      timeout ms (25000) —

           timeout ms specifies the time, in milliseconds, that the function waits for bytes from an IrDA
            device on a wireless network before the function completes and returns an error. The default
            value is 25,000 ms. A value of –1 indicates to wait indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      connection ID out —

           connection ID out is the IrDA connection refnum that uniquely identifies the IrDA connection.
           Use this value to refer to this connection in subsequent IrDA function calls. connection ID out
            always has the same value as connection ID.

               •      data out —

           data out is the data the function reads from an IrDA device returned as a string or as a flattened
               string. Use the Unflatten From String function to convert the data to the correct data type. You
             also can use the Unflatten From XML function to convert data from XML format.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\IrDA\Simple
        IrDA\Simple IrDA.lvproj
            • labview\examples\Data Communication\Protocols\IrDA\Simple
        IrDA\Simple IrDA.lvproj


5214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5215 ordinal=5215 -->
## Functions

Functions

IrDAIrDA WriteWrite FunctionFunction

Sends string data to the IrDA connection specified by connection ID.


Inputs/Outputs

   •      connection ID —

    connection ID is an IrDA connection refnum that uniquely identifies the IrDA connection.

   •      data in —

    data in is the data the function writes to an IrDA device. The data must be a string or a flattened
     string.

    Use the Flatten To String function to convert any data that is not a string to the string format. You
    must then use the Unflatten From String function to unflatten the string on the remote
    computer. You also can use the Flatten To XML function to convert data to XML format.

    Use one of the following techniques to handle messages that might vary in size:
         • Send messages that are preceded by a fixed size header that describes the message. For
        example, it might contain a command integer that identifies what kind of message follows
       and a length integer that identifies how much more data is in the message. Both the server
       and client receive messages by issuing a read function of eight bytes (assuming each is a
         four byte integer), converting them into the two integers, and using the length integer to
        determine the number of bytes to pass to a second read function for the remainder of the
        message. Once this second read is complete, each side loops back to the read function of
        the eight byte header. This technique is the most flexible, but it requires two reads to
         receive each message. In practice, the second read usually completes immediately if the
       message is written with a single write function.
         • Make each message a fixed size. When the content of a message is smaller than the fixed
          size you specify, pad the message to the fixed size. This technique is marginally more
          efficient because only a single read is required to receive a message at the expense of
        sending unnecessary data sometimes.
         • Send messages that are strictly ASCII in content, where each message is terminated by a
         carriage return and linefeed pair of characters. The read function has a mode input that,
       when passed CRLF, causes it to read until seeing a carriage return and linefeed sequence.
         This technique becomes more complicated when message data can possibly contain CRLF
        sequences, but it is quite common among many internet protocols, including POP3, FTP,
       and HTTP.

                                                    © National Instruments 5215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5216 ordinal=5216 -->
## Functions

Functions

               •      timeout ms (25000) —

           timeout ms specifies the time, in milliseconds, for the function to write bytes to a device before
            the function completes and returns an error. The default value is 25,000 ms. A value of –1
             indicates to wait indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      connection ID out —

           connection ID out is the IrDA connection refnum that uniquely identifies the IrDA connection.
           Use this value to refer to this connection in subsequent IrDA function calls. connection ID out
            always has the same value as connection ID.

               •      bytes written —

            bytes written indicates the number of bytes the function wrote.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\IrDA\Simple
        IrDA\Simple IrDA.lvproj
            • labview\examples\Data Communication\Protocols\IrDA\Simple
        IrDA\Simple IrDA.lvproj

       IrDAIrDA CloseClose ConnectionConnection FunctionFunction

       Closes the open infrared connection to the IrDA device specified by connection ID.


5216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5217 ordinal=5217 -->
## Functions

Functions

Inputs/Outputs

   •      connection ID —

    connection ID is an IrDA connection refnum that uniquely identifies the IrDA connection.

   •      abort (F) —

    abort is reserved for future use.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      connection ID out —

    connection ID out has the same value as connection ID. Do not wire this output to other IrDA
     functions.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\IrDA\Simple
   IrDA\Simple IrDA.lvproj
  • labview\examples\Data Communication\Protocols\IrDA\Simple
   IrDA\Simple IrDA.lvproj

IrDAIrDA CreateCreate ListenerListener FunctionFunction

Creates a listener for an IrDA connection on a wireless network using the service name
and returns listener ID.

After you create the listener ID, you can use the IrDA Wait on Listener function to wait

                                                    © National Instruments 5217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5218 ordinal=5218 -->
## Functions

Functions

        for the detection of a remote computer.


      Inputs/Outputs

               •       service name —

             service name specifies the IrDA service you want to connect to.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       listener ID —

              listener ID is the IrDA connection refnum that uniquely identifies the listener.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       IrDAIrDA WaitWait OnOn ListenerListener FunctionFunction

       Waits for the designated IrDA listener to accept an IrDA network connection.

      You can communicate with only one computer at a time. Use the IrDA Create Listener
       function to create the listener ID.


      Inputs/Outputs

               •       listener ID in —

              listener ID in is an IrDA connection refnum that uniquely identifies the IrDA listener.


5218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5219 ordinal=5219 -->
## Functions

Functions

   •      timeout ms (wait forever: -1) —

    timeout ms specifies the time, in milliseconds, that the function waits for a connection. If a
    connection is not established in the specified time, the function returns an error. The default
    value is –1, which indicates to wait indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       listener ID out —

     listener ID out has the same value as listener ID in. Use this value to refer to the listener in
    subsequent calls to this function.

   •      remote LSAP-SEL —

    remote LSAP-SEL is the selector number the remote IrDA device uses for the IrDA connection.

   •      remote device ID —

    remote device ID is the ID of the remote IrDA device.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      connection ID —

    connection ID out is the IrDA connection refnum that uniquely identifies the IrDA connection.
    Use this value to refer to this connection in subsequent IrDA function calls. connection ID out
    always has the same value as connection ID.

BluetoothBluetooth

Use the Bluetooth VIs and functions to communicate with devices that use the
Bluetooth communication protocol.

      Note You must have the Microsoft Bluetooth Driver installed to use the
       Bluetooth VIs and functions.


                                                    © National Instruments 5219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5220 ordinal=5220 -->
## Functions

Functions

      The VIs and functions on this palette can return networking error codes.


         Palette Object         Description

         Bluetooth Open                             Requests a connection to a Bluetooth server.        Connection Function

         Bluetooth Read       Reads the number of bytes from a Bluetooth network connection and
         Function               returns the results in data out.

         Bluetooth Write                                Writes data to a Bluetooth network connection.         Function

         Bluetooth Close                               Closes a Bluetooth network connection.        Connection Function

         Bluetooth Create       Creates a service for a Bluetooth server and returns a Bluetooth channel the
         Listener Function      server can use to listen for inbound connections.

         Bluetooth Wait On                               Waits for the listener to accept a connection request.         Listener Function

         Bluetooth Discover    Searches for all locally installed or other Bluetooth devices within the range
         Function               of the Bluetooth network.

         Bluetooth RFCOMM                              Returns a list of services available from a Bluetooth address.         Service Discovery


         Bluetooth Set Mode    Sets the discoverable and connectable status of the local Bluetooth device.


                              Returns the discoverable and connectable status of the local Bluetooth
         Bluetooth Get Mode
                                 device.


      BluetoothBluetooth OpenOpen ConnectionConnection FunctionFunction

      Requests a connection to a Bluetooth server.


5220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5221 ordinal=5221 -->
## Functions

Functions


Inputs/Outputs

   •      address —

    address is the address of the Bluetooth server. An example of a Bluetooth address is
   00:07:E0:07:D7:50.

   •      channel (0) —

    channel is the channel number on the Bluetooth server.

       If channel is zero, this function uses the UUID to specify the service to connect to.

   •      timeout ms (60000) —

    timeout ms specifies the time, in milliseconds, that the function waits to complete and return an
     error. The default value is 60,000 ms or 1 minute. A value of –1 indicates to wait indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      uuid —

    uuid is the unique identifier for the service.

       If channel is zero, this function uses the UUID to specify the service. The UUID must be in GUID
    format. An example of a UUID in GUID format is B62C4E8D-62CC-404b-BBBF-
   BF3E3BBB1374

   •      connection ID —

    connection ID is a network connection refnum that uniquely identifies the Bluetooth
    connection.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5222 ordinal=5222 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\Bluetooth\
        Simple Bluetooth\Simple Bluetooth.lvproj

      BluetoothBluetooth ReadRead FunctionFunction

      Reads the number of bytes from a Bluetooth network connection and returns the
        results in data out.


      Inputs/Outputs

               •     mode (standard) —

         mode indicates the behavior of the read operation.

            Standard (default)—Waits until all bytes you specify in bytes to read arrive or until timeout ms
           0 runs out. Returns the number of bytes read so far. If fewer bytes than the number of bytes you
             requested arrive, returns the partial number of bytes and reports a timeout error.
             Buffered—Waits until all bytes you specify in bytes to read arrive or until timeout ms runs out.
           1 If fewer bytes than the number you requested arrive, returns no bytes and reports a timeout
                error.
            CRLF—Waits until all bytes you specify in bytes to read arrive or until the function receives a CR
               (carriage return) followed by a LF (linefeed) within the number of bytes you specify in bytes to
           2
             read or until timeout ms runs out. The function returns the bytes up to and including the CR
           and LF if it finds them in the string.
            Immediate—Waits until the function receives any bytes from those you specify in bytes to
           3 read. Waits the full timeout only if the function receives no bytes. Returns the number of bytes
             so far. Reports a timeout error if the function receives no bytes.

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the Bluetooth
            connection.

               •      bytes to read —

5222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5223 ordinal=5223 -->
## Functions

Functions


  bytes to read is the number of bytes to read. You must wire a value greater than 0 in order to
  read data from a network connection. The default is 0.

  Use one of the following techniques to handle messages that might vary in size:

      • Send messages that are preceded by a fixed size header that describes the message. For
      example, it might contain a command integer that identifies what kind of message follows
     and a length integer that identifies how much more data is in the message. Both the server
     and client receive messages by issuing a read function of eight bytes (assuming each is a
       four byte integer), converting them into the two integers, and using the length integer to
      determine the number of bytes to pass to a second read function for the remainder of the
      message. Once this second read is complete, each side loops back to the read function of
      the eight byte header. This technique is the most flexible, but it requires two reads to
       receive each message. In practice, the second read usually completes immediately if the
     message is written with a single write function.
      • Make each message a fixed size. When the content of a message is smaller than the fixed
       size you specify, pad the message to the fixed size. This technique is marginally more
        efficient because only a single read is required to receive a message at the expense of
      sending unnecessary data sometimes.
      • Send messages that are strictly ASCII in content, where each message is terminated by a
       carriage return and linefeed pair of characters. The read function has a mode input that,
     when passed CRLF, causes it to read until seeing a carriage return and linefeed sequence.
       This technique becomes more complicated when message data can possibly contain CRLF
      sequences, but it is quite common among many internet protocols, including POP3, FTP,
     and HTTP.
•      timeout ms (25000) —

  timeout ms specifies the time, in milliseconds, that the function waits for the connection. The
  default is 25,000 ms. A value of –1 indicates to wait indefinitely.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      connection ID out —

  connection ID out returns the same value as connection ID.

•      data out —

  data out contains the data the function read from the Bluetooth connection.

•       error out —

                                                   © National Instruments 5223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5224 ordinal=5224 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\Bluetooth\
        Simple Bluetooth\Simple Bluetooth.lvproj

      BluetoothBluetooth WriteWrite FunctionFunction

       Writes data to a Bluetooth network connection.


      Inputs/Outputs

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the Bluetooth
            connection.

               •      data in —

           data in contains the data you want to write to the connection.

           Use one of the following techniques to handle messages that might vary in size:
                     • Send messages that are preceded by a fixed size header that describes the message. For
               example, it might contain a command integer that identifies what kind of message follows
              and a length integer that identifies how much more data is in the message. Both the server
              and client receive messages by issuing a read function of eight bytes (assuming each is a
                 four byte integer), converting them into the two integers, and using the length integer to
               determine the number of bytes to pass to a second read function for the remainder of the
               message. Once this second read is complete, each side loops back to the read function of
                the eight byte header. This technique is the most flexible, but it requires two reads to
                 receive each message. In practice, the second read usually completes immediately if the
              message is written with a single write function.
                     • Make each message a fixed size. When the content of a message is smaller than the fixed
                   size you specify, pad the message to the fixed size. This technique is marginally more

5224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5225 ordinal=5225 -->
## Functions

Functions

          efficient because only a single read is required to receive a message at the expense of
        sending unnecessary data sometimes.
         • Send messages that are strictly ASCII in content, where each message is terminated by a
         carriage return and linefeed pair of characters. The read function has a mode input that,
       when passed CRLF, causes it to read until seeing a carriage return and linefeed sequence.
         This technique becomes more complicated when message data can possibly contain CRLF
        sequences, but it is quite common among many internet protocols, including POP3, FTP,
       and HTTP.
   •      timeout ms (25000) —

    timeout ms specifies the time, in milliseconds, that the function waits for the connection. The
     default is 25,000 ms. A value of –1 indicates to wait indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      connection ID out —

    connection ID out returns the same value as connection ID.

   •      bytes written —

    bytes written indicates the number of bytes the function wrote.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\Bluetooth\
   Simple Bluetooth\Simple Bluetooth.lvproj

BluetoothBluetooth CloseClose ConnectionConnection FunctionFunction

Closes a Bluetooth network connection.


                                                    © National Instruments 5225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5226 ordinal=5226 -->
## Functions

Functions


      Inputs/Outputs

               •      connection ID —

           connection ID is a network connection refnum that uniquely identifies the Bluetooth
            connection.

               •      abort (F) —

            abort is reserved for future use.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •      connection ID out —

           connection ID out returns the same value as connection ID.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\Bluetooth\
        Simple Bluetooth\Simple Bluetooth.lvproj

      BluetoothBluetooth CreateCreate ListenerListener FunctionFunction

       Creates a service for a Bluetooth server and returns a Bluetooth channel the server can
      use to listen for inbound connections.


5226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5227 ordinal=5227 -->
## Functions

Functions


Inputs/Outputs

   •      address —

    address is the address of the Bluetooth server. An example of a Bluetooth address is
   00:07:E0:07:D7:50.

   •      uuid —

    uuid identifies the service.

    You can assign duplicate UUIDs, but National Instruments does not recommend assigning
    duplicate UUIDs. If a Bluetooth client requests a UUID that multiple services use on a Bluetooth
     server, the server uses the first UUID it encounters. The UUID must be in GUID format. An
    example of a UUID in GUID format is B62C4E8D-62CC-404b-BBBF-BF3E3BBB1374.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       service description —

    service description contains the name and description of the service uuid indicates.

         •     name —

      name is the name of the service.

         •      description —

         description is a short description of the service.


   •       listener ID —

     listener ID is a network connection refnum that uniquely identifies the listener.

   •      channel —


                                                    © National Instruments 5227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5228 ordinal=5228 -->
## Functions

Functions


           channel returns the channel assigned to the listener.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Data Communication\Protocols\Bluetooth\
        Simple Bluetooth\Simple Bluetooth.lvproj

      BluetoothBluetooth WaitWait OnOn ListenerListener FunctionFunction

       Waits for the listener to accept a connection request.


      Inputs/Outputs

               •       listener ID in —

              listener ID in is a network connection refnum that uniquely identifies the listener.

               •      timeout ms (wait forever: -1) —

           timeout ms specifies the time, in milliseconds, that the function waits for a connection. If a
            connection is not established in the specified time, the function returns an error. The default
            value is –1, which indicates to wait indefinitely.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       listener ID out —


5228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5229 ordinal=5229 -->
## Functions

Functions


     listener ID out returns the same value as listener ID in.

   •      remote address —

    remote address is the address of the client.

   An example of a Bluetooth address is 00:07:E0:07:D7:50.
   •      remote channel —

    remote channel returns the channel of the Bluetooth client.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      connection ID —

    connection ID is a network connection refnum that uniquely identifies the Bluetooth
    connection.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\Bluetooth\
   Simple Bluetooth\Simple Bluetooth.lvproj

BluetoothBluetooth DiscoverDiscover FunctionFunction

Searches for all locally installed or other Bluetooth devices within the range of the
Bluetooth network.


Inputs/Outputs

   •      time limit ms (10000) —


                                                    © National Instruments 5229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5230 ordinal=5230 -->
## Functions

Functions


           time limit ms is the amount of time the function uses to search for Bluetooth devices. The
             default value is 10,000 ms. The maximum value is 30,000 ms.

                    If the value is less than or equal to zero, this function returns a list of local installed Bluetooth
             devices.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     number of devices —

          number of devices indicates how many Bluetooth devices the function detects on the network.

               •      device list —

            device list returns a list of devices the function detects on the network.

                     •      Address —

               Address identifies a device on the Bluetooth network. Use this ID to open a connection to a
                   server.

                     •      Device Name —

                Device Name indicates the name of the Bluetooth device.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The process of discovering Bluetooth devices can be a slow operation. If you know the
       Bluetooth address of the specific device to which you want to connect, you can skip
       the discovery process and use the Bluetooth Open Connection function to connect to
       the device directly.

      BluetoothBluetooth RFCOMMRFCOMM ServiceService DiscoveryDiscovery

       Returns a list of services available from a Bluetooth address.

5230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5231 ordinal=5231 -->
## Functions

Functions

This VI performs a Service Discovery Protocol (SDP) query to search for available
services on the local or remote Bluetooth device you specify with address in.


Inputs/Outputs

   •      address in —

    address in specifies the Bluetooth address of the device.

   An example of a Bluetooth address is 00:07:E0:07:D7:50.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      address out —

    address out returns the same address as address in.

   •     number of services —

   number of services returns the number of services available on the Bluetooth device address in
     specifies.

   •       service list —

    service list is an array of clusters that describes each service available on the Bluetooth device.

         •      channel —

        channel returns the channel of the service.

         •      uuid —

        uuid identifies the service.

         •       service name —


                                                    © National Instruments 5231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5232 ordinal=5232 -->
## Functions

Functions


                 service name returns the name of the service.

                     •       service description —

                 service description returns the description of the service.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      BluetoothBluetooth SetSet ModeMode

       Sets the discoverable and connectable status of the local Bluetooth device.


      Inputs/Outputs

               •      address in —

           address in specifies the Bluetooth address of the local device.

                    If you do not specify an address, this VI attempts to set the discoverable and connectable modes
             of all local devices.

               •      discoverable —

            discoverable determines if the device allows other Bluetooth devices to discover the device. The
             default is TRUE.

               •      connectable —

           connectable determines if the device allows other Bluetooth devices to connect to the device.
          The default is TRUE.

                    If discoverable is TRUE and connectable is FALSE, the VI returns an error.


5232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5233 ordinal=5233 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      address out —

    address out returns the same address as address in.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


BluetoothBluetooth GetGet ModeMode

Returns the discoverable and connectable status of the local Bluetooth device.


Inputs/Outputs

   •      address in —

    address in specifies the Bluetooth address of the local device.

       If you do not specify an address, this VI reads the discoverable and connectable modes of all
     local devices.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      address out —

    address out returns the same address as address in.

   •      discoverable —


                                                    © National Instruments 5233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5234 ordinal=5234 -->
## Functions

Functions


            discoverable returns TRUE if the device allows other Bluetooth devices to discover the device.

                    If you do not specify address in, this VI returns TRUE if at least one of the local devices is
            configured to be discoverable.

               •      connectable —

           connectable returns TRUE if the device allows connections.

                    If you do not specify address in, this VI returns TRUE if at least one of the local devices is
            configured to be connectable.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SMTPSMTP EmailEmail

      Use the SMTP Email VIs to send email, including attached data and files, using the
      Simple Mail Transfer Protocol (SMTP). You can use Transport Layer Security (TLS) to
      communicate with the SMTP server with added security. You also can specify
       authentication credentials for the SMTP client. However, you cannot use the SMTP
      Email VIs to receive information.

           Note The SMTP Email VIs use UTF-8 encoding to send email.

      You can use the Send Email Express VI to quickly send emails from LabVIEW to a list of
       recipients you specify. However, if you want to configure headers, set TLS settings, or
       include an attachment, you can use the standard SMTP Email VIs to configure and send
      an email with more advanced settings.

      The standard SMTP Email VIs use an SMTP client handle to maintain the SMTP client
       settings across the block diagram. You can use individual VIs to set the email
       configuration. Close the client handle using the Close Handle VI when you no longer
      need it to free system resources.

      The VIs on this palette can return SMTP email reply codes.


5234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5235 ordinal=5235 -->
## Functions

Functions

Refer to labview\examples\Data Communication\Protocols\SMTP\
Send Email using SMTP Client.vi for an example of using multiple SMTP
Email VIs in a single VI to send an email.


 Palette              Description Object

              Creates and sends an email according to the settings you specify in the configuration Send Email               dialog box.


              Creates a new SMTP client handle using the specified SMTP server. Use this VI with Open              other SMTP Email VIs to send emails according to your specifications. You must close
 Handle              the handle using the Close Handle VI.


 Close        Closes a connection to an SMTP server and disposes of the handle created by an
 Handle     Open Handle VI.


 Set          Sets the list of recipients to whom you want to send the email. This VI overwrites the
 Recipients    existing values before it executes.


              Sets the message you want to include in the body of the email. This VI overwrites any
 Set Message
            message values that you specify before this VI executes.


 Send        Sends an email using the configuration you set on the handle wired to handle in.


 Set          Sets a list of files that you want to include with the email. This VI overwrites any
 Attachments attachment values that you specify before this VI executes.


                                                    © National Instruments 5235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5236 ordinal=5236 -->
## Functions

Functions


         Palette                      Description
        Object

         Clear                  Removes all attachments you set using the Set Attachments VI.        Attachments


                      Sets a list of auxiliary headers that you want to send with the email. This VI         Set Headers                      overwrites any header values that you specify before this VI executes.


         Clear                  Removes all headers you set using the Set Headers VI.        Headers


                      Sets the SMTP client certificate, certificate authority (CA) certificates bundle, and         Config TLS
                        private key file paths for a TLS or SSL request.


     SendSend EmailEmail

       Creates and sends an email according to the settings you specify in the configuration
       dialog box.


      Dialog Box Options

        Option      Description

                     Contains the following options:

                                   • Sender's Email Address—
        User
        Information      Specifies the email address from which you want to send the email.

                                   • Outgoing Mail Server (SMTP)—


5236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5237 ordinal=5237 -->
## Functions

Functions


Option      Description

                   Specifies the hostname or IP address of the SMTP server you want to use to send
                  emails. Do not include the port number in this field.

                      • Port—

                   Specifies the port number of the SMTP server you want to use to send emails.
               The default is 25, which is standard for open connections. However, if you use a
                 secure connection, you may need to change the port number.

                      • Require Log-in—

                   Specifies whether to transmit log-in credentials to the SMTP server. Most public
             SMTP servers require log-in credentials. The default is unselected.

        ◦ Username—

                       Specifies the log-in username for the SMTP server you specify. On most
                      public servers, this is your email address.

        ◦ Password—

                       Specifies the log-in password for the SMTP server you specify.

                      • Use Secure Connection (TLS\SSL)—

                   Specifies whether to require a Transport Layer Security (TLS) and Secure Sockets
                 Layer (SSL) secured connection when LabVIEW communicates with the SMTP
                   server.

             Contains the following options:

                      • Recipients—

                   Specifies the email address(es) of the recipient(s). To send an email to multiple
                   recipients, separate each email address with a comma. You must enter at least
Email          one email address. You also can wire a recipient list to the Recipients input on
                 the block diagram.

                      • Subject—

                  (Optional) Specifies the subject of the message. You also can wire a subject line


                                                    © National Instruments 5237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5238 ordinal=5238 -->
## Functions

Functions


        Option      Description

                           to the Subject input on the block diagram.

                                   • Message—

                           (Optional) Specifies a message in plain text that you want to send to the
                              recipient(s). You also can wire a message to the Message input on the block
                         diagram.


       Send Test    Tests the configuration of the VI by sending a test email to the email address you
        Email        specify in Sender's Email Address.


      Inputs/Outputs

               •       error in —

             Specifies error conditions that occur before this node runs. This input provides standard error in
              functionality.

               •      Message —

             Specifies a message, in plain text, that you want to send to the recipient(s).

               •      Subject —

             Specifies the subject of the message.

               •      Recipients —

             Specifies the email address(es) of the recipient(s). To send an email with multiple recipients,
            separate each email address with a comma. You must enter at least one email address.

               •       error out —

            Contains error information. This output provides standard error out functionality.


5238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5239 ordinal=5239 -->
## Functions

Functions

Components

Specifies the email address(es) of the recipient(s). To send an email to multiple
recipients, separate each email address with a comma. You must enter at least one
email address. You also can wire a recipient list to the Recipients input on the block
diagram.

Tests the configuration of the VI by sending a test email to the email address you
specify in Sender's Email Address.

Specifies the email address from which you want to send the email.

(Optional) Specifies the subject of the message. You also can wire a subject line to the
Subject input on the block diagram.

(Optional) Specifies a message in plain text that you want to send to the recipient(s).
You also can wire a message to the Message input on the block diagram.

Specifies whether to require a Transport Layer Security (TLS) and Secure Sockets Layer
(SSL) secured connection when LabVIEW communicates with the SMTP server.

Specifies the log-in password for the SMTP server you specify.

Specifies the port number of the SMTP server you want to use to send emails. The
default is 25, which is standard for open connections. However, if you use a secure
connection, you may need to change the port number.

Specifies the log-in username for the SMTP server you specify. On most public servers,
this is your email address.

Specifies the hostname or IP address of the SMTP server you want to use to send
emails. Do not include the port number in this field.

Specifies whether to transmit log-in credentials to the SMTP server. Most public SMTP
servers require log-in credentials. The default is unselected.


                                                    © National Instruments 5239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5240 ordinal=5240 -->
## Functions

Functions

     OpenOpen HandleHandle

       Creates a new SMTP client handle using the specified SMTP server. Use this VI with
       other SMTP Email VIs to send emails according to your specifications. You must close
       the handle using the Close Handle VI.


      Inputs/Outputs

               •      server address —

            server address specifies the hostname or IP address of the SMTP server you want to use to send
             emails. You also can specify a port number by appending a colon and the port number to the
          hostname or IP address in the format hostname:port. By default, LabVIEW uses port 25,
           which works only for non-TLS SMTP servers.

               •      from —

           from specifies the email address from which you want to send an email.

               •     username —

          username specifies the log-in username for the SMTP server you specify. On most public
             servers, this is your email address.

               •      password —

           password specifies the log-in password for the SMTP server you specify.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      use TLS (false) —

           use TLS specifies whether to use Transport Layer Security (TLS) for added security when


5240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5241 ordinal=5241 -->
## Functions

Functions


    communicating with the SMTP server. If TRUE, the Open Handle VI uses TLS when
    communicating with the SMTP server. If FALSE, the VI does not use TLS. The default is FALSE.

   •      handle out —

    handle out returns an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
    Use the Close Handle VI to dispose of the handle and free system resources when you no longer
    need the handle.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


CloseClose HandleHandle

Closes a connection to an SMTP server and disposes of the handle created by an Open
Handle VI.


Inputs/Outputs

   •      handle in —

    handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      handle out —

    handle out returns an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
    Use the Close Handle VI to dispose of the handle and free system resources when you no longer


                                                    © National Instruments 5241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5242 ordinal=5242 -->
## Functions

Functions


          need the handle.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      SetSet RecipientsRecipients

       Sets the list of recipients to whom you want to send the email. This VI overwrites the
        existing values before it executes.


      Inputs/Outputs

               •      handle in —

           handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

               •      to —

            to specifies an array of strings where each element contains the email address of one recipient
             to whom you want to address and send the email.

               •      cc —

            cc specifies an array of strings where each element contains the email address of one recipient
         who you want to receive a copy of the email.

               •      bcc —

           bcc specifies an array of strings where each element contains the email address of one recipient
         who you want to receive a copy of the email but do not want to appear as a recipient of the
             email.

               •       error in (no error) —


5242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5243 ordinal=5243 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      handle out —

    handle out returns an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
    Use the Close Handle VI to dispose of the handle and free system resources when you no longer
    need the handle.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SetSet MessageMessage

Sets the message you want to include in the body of the email. This VI overwrites any
message values that you specify before this VI executes.


  • Set Message Text VI
  • Set Message Text Html VI
SetSet MessageMessage TextText VIVI

Sets the message you want to include in the body of the email. This VI overwrites any
message values that you specify before this VI executes.


Inputs/Outputs

   •      handle in —

                                                    © National Instruments 5243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5244 ordinal=5244 -->
## Functions

Functions


           handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

               •      subject —

            subject specifies the subject of the email.

               •       plain text message —

             plain text message specifies a message in plain text that you want to include in the body of the
             email. The email client of the recipient selects whether to display the message using HTML or
             plain text and usually gives preference to HTML.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      handle out —

           handle out returns an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
           Use the Close Handle VI to dispose of the handle and free system resources when you no longer
          need the handle.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet MessageMessage TextText HtmlHtml VIVI

       Sets the message you want to include in the body of the email. This VI overwrites any
      message values that you specify before this VI executes.

           Note You can include both a plain text version of the message and a well-
             formed HTML version that the email client of the recipient can interpret as
                text and HTML MIME types. The email client of the recipient selects which
               version to display and usually prefers HTML. If the client cannot process
            HTML, it will select the plain text version you specify in plain text message.

5244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5245 ordinal=5245 -->
## Functions

Functions


Inputs/Outputs

   •      handle in —

    handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

   •      subject —

    subject specifies the subject of the email.

   •       plain text message —

    plain text message specifies a message in plain text that you want to include in the body of the
    email. The email client of the recipient selects whether to display the message using HTML or
     plain text and usually gives preference to HTML.

   •      html message —

    html message specifies a message in well-formed HTML that you want to include in the body of
    the email. The email client of the recipient selects whether to display the message using HTML
    or plain text and usually gives preference to HTML.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      handle out —

    handle out returns an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
    Use the Close Handle VI to dispose of the handle and free system resources when you no longer
    need the handle.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5246 ordinal=5246 -->
## Functions

Functions

     SendSend

      Sends an email using the configuration you set on the handle wired to handle in.

      You must use the SMTP Email VIs to configure the handle.


      Inputs/Outputs

               •      handle in —

           handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout in ms (10000) —

           timeout in ms specifies the time, in milliseconds, that the VI to attempts to send the email
            before returning an error. The default is 10,000 ms.

               •      handle out —

           handle out returns an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
           Use the Close Handle VI to dispose of the handle and free system resources when you no longer
          need the handle.

               •       invalid recipients —

             invalid recipients lists the recipients rejected by the mail server. Any recipient that does not
           appear in this list should receive the email.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5247 ordinal=5247 -->
## Functions

Functions

SetSet AttachmentsAttachments

Sets a list of files that you want to include with the email. This VI overwrites any
attachment values that you specify before this VI executes.


Inputs/Outputs

   •      handle in —

    handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

   •      attachments —

    attachments specifies an array where each element is the path to a file you want to include with
    the email. LabVIEW opens and transmits the file when the Send Email VI executes using the
    handle that handle out returns.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      handle out —

    handle out returns an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
    Use the Close Handle VI to dispose of the handle and free system resources when you no longer
    need the handle.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ClearClear AttachmentsAttachments

Removes all attachments you set using the Set Attachments VI.


                                                    © National Instruments 5247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5248 ordinal=5248 -->
## Functions

Functions


      Inputs/Outputs

               •      handle in —

           handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      handle out —

           handle out returns an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
           Use the Close Handle VI to dispose of the handle and free system resources when you no longer
          need the handle.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      SetSet HeadersHeaders

       Sets a list of auxiliary headers that you want to send with the email. This VI overwrites
      any header values that you specify before this VI executes.


      Inputs/Outputs

               •      handle in —

           handle in specifies an SMTP client handle that references system resources that LabVIEW uses to


5248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5249 ordinal=5249 -->
## Functions

Functions


   make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

   •      headers —

    headers specifies a list of auxiliary headers, such as Reply-to, Precedence, and
   References, that you want to send with the email. The SMTP client automatically sets
    standard headers, such as To, From, Subject, CC, and BCC, so LabVIEW does not transmit
   them even if you include them in the list. Each cluster in the list specifies the following elements:

         •     Name —

      Name specifies the field name of the header that appears to the left of the colon.

         •      Value —

        Value specifies the field value(s) that appear to the right of the colon.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      handle out —

    handle out returns an SMTP client handle that references system resources that LabVIEW uses to
   make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
    Use the Close Handle VI to dispose of the handle and free system resources when you no longer
    need the handle.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ClearClear HeadersHeaders

Removes all headers you set using the Set Headers VI.


                                                    © National Instruments 5249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5250 ordinal=5250 -->
## Functions

Functions

      Inputs/Outputs

               •      handle in —

           handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      handle out —

           handle out returns an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
           Use the Close Handle VI to dispose of the handle and free system resources when you no longer
          need the handle.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      ConfigConfig TLSTLS

       Sets the SMTP client certificate, certificate authority (CA) certificates bundle, and
       private key file paths for a TLS or SSL request.

      LabVIEW opens and reads the certificate files when the Send VI executes on the same
       handle.


      Inputs/Outputs

               •       private key password —

5250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5251 ordinal=5251 -->
## Functions

Functions


  private key password specifies a password for the private key file. If the private key file is not
  encrypted, you do not have to specify a private key password.

•      handle in —

  handle in specifies an SMTP client handle that references system resources that LabVIEW uses to
  make SMTP requests. You can create an SMTP client handle using the Open Handle VI.

•     CA certificate file —

  CA certificate file specifies the path to a list of trusted certificate authority (CA) certificates. If you
  specify TRUE for the verify server control, the client verifies the server's identity against this list
  of trusted certificates.

•       client certificate file —

  client certificate file specifies the path to the client certificate file for servers that require client
  authentication. Some servers require this file to verify the identity of the client by using a trusted
  CA.

•       private key file —

  private key file specifies the path to a private key file that is part of the client certificate and
  client authentication process.

   If the server requires client authentication, you must specify a client certificate file and a private
  key file. If you need to transfer this file between client systems, especially over a network, you
  can assign a password when you create the private key file. To use password-protected private
  key files with this VI, assign the password to the private key password input.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       verify server (true) —

  verify server specifies whether to check the server's certificate against the list of trusted CA
   certificates specified by the CA certificate file control.

   If TRUE, this VI verifies the server's identity against the list of trusted CA certificates for optimal
  security. If FALSE, this VI does not verify the server's identity and does not provide optimal
  security. Specifying FALSE allows the client to accept self-signed certificates signed by the


                                                   © National Instruments 5251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5252 ordinal=5252 -->
## Functions

Functions


               certificate creator rather than a trusted CA. The default is TRUE.

               •      handle out —

           handle out returns an SMTP client handle that references system resources that LabVIEW uses to
          make SMTP requests. You can wire this output to the handle in input of other SMTP Email VIs.
           Use the Close Handle VI to dispose of the handle and free system resources when you no longer
          need the handle.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    HTTPHTTP ClientClient

      Use the HTTP Client VIs to build a Web client that interacts with servers, Web pages,
      and Web services. You can add HTTP headers, store cookies, provide authentication
        credentials, and send Web requests using HTTP methods such as POST, GET, PUT,
      HEAD, and DELETE. These VIs also can interact with LabVIEW Web services.


         Palette Object  Description

                    Opens a client handle. Use client handles to wire together multiple HTTP Client VIs
                        while preserving authentication credentials, HTTP headers, and cookies. You can
       OpenHandle    specify a username and password, if necessary, to send Web requests to a server
                         that requires authentication. You also can create a cookie file that stores data
                        across multiple Web requests.


                     Sends a Web request that returns headers and body data from a server, Web page,
       GET            or Web service. This VI uses the GET HTTP method and does not submit any data to
                       the server. You also can save the body data to an output file.


5252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5253 ordinal=5253 -->
## Functions

Functions


Palette Object  Description

             Sends a Web request that returns headers from a server, Web page, or Web service.
                This VI uses the HEAD HTTP method. This VI does not submit any data to the serverHEAD               or receive body data. The minimal data exchange makes the HEAD VI useful for
                 testing the validity of a URL.


               Closes the client handle and deletes all stored cookies, authentication credentials,
CloseHandle   and HTTP headers associated with the client handle. This VI also terminates all
            HTTP connections and logs out of any authentication, if applicable.


             Sends a Web request that submits data or a file to a server, Web page, or Web
                 service. This VI uses the PUT HTTP method. Refer to the World Wide Web
PUT              Consortium website at www.w3.org for more information about HTTP method
                 definitions, including the PUT method.


             Sends a Web request that submits data or a file to a server, Web page, or Web
                 service. This VI uses the POST HTTP method. Refer to the World Wide Web
POST         Consortium website at www.w3.org for more information about HTTP method
                 definitions, including the POST method. Use the POSTMultipart VI to send POST
               requests using the multipart/form-data MIME type.


             Sends a Web request that submits multiple sets of data or files to a server, Web
               page, or Web service. This VI uses the POST HTTP method and multipart/form-data
            MIME type.
POSTMultipart             The POSTMultipart VI submits multiple sets of data, represented by an array of
              postdata clusters. Use the postdata control descriptions to configure the
              submitted data as one of the four available combinations. For example, the VI can
               accept a buffer data string from the client and send that data as a file to the server.


             Sends a Web request to delete resources on a server, Web page, or Web service.
                This VI uses the DELETE HTTP method. The server accepting the request from the
DELETE
             DELETE VI must be setup to delete resources solely based upon receiving a DELETE
           Web request at the specified URL.


                                                    © National Instruments 5253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5254 ordinal=5254 -->
## Functions

Functions


         Palette Object  Description

                     Use the Security VIs to encrypt and decrypt data transfers. You also can use these
         Security                           VIs with the Web Services Security VIs.


                     Use the Headers VIs to manage header field lines for Web requests associated with        Headers                            client handles. These VIs also can interact with LabVIEW Web services.


     OpenHandleOpenHandle

      Opens a client handle. Use client handles to wire together multiple HTTP Client VIs
       while preserving authentication credentials, HTTP headers, and cookies. You can
       specify a username and password, if necessary, to send Web requests to a server that
       requires authentication. You also can create a cookie file that stores data across
       multiple Web requests.


      Inputs/Outputs

               •      cookie file —

            cookie file is the path to store a client-side cookie. Cookies store data across multiple Web
             requests.

               •     username —

          username specifies the log-in username for the HTTP server you created earlier.

               •      password —

           password specifies the log-in password for the HTTP server.

               •       error in (no error) —


5254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5255 ordinal=5255 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       verify server(true) —

     verify server (true) specifies whether to verify the server's identity and establish a secure
    connection. Use this control to allow HTTP Client VIs to communicate using the https://
     protocol. The default value is TRUE.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Client handles increase network efficiency by limiting the number of network sockets
and ports necessary to perform multiple Web requests. Client handles are not required
when making independent Web requests without persistent data such as headers or
credentials.

The following screenshot shows code that performs the following:

 1. The OpenHandle VI opens a client handle and a client-side cookie that can store
    persistent data.
 2. The AddHeader VI adds a new header field line that sets the preferred language for
   subsequent Web requests associated with the client handle.
 3. The GET VI performs a Web request that includes the Accept-Language header.
 4. The CloseHandle VI closes the client handle and deletes any persistent data,
    including headers.


                                                    © National Instruments 5255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5256 ordinal=5256 -->
## Functions

Functions


     GETGET

      Sends a Web request that returns headers and body data from a server, Web page, or
     Web service. This VI uses the GET HTTP method and does not submit any data to the
        server. You also can save the body data to an output file.

      You can assign a client handle to add authentication credentials, HTTP headers, or a
       cookie to Web requests made by the GET VI. Use the OpenHandle VI to open a client
      handle and establish credentials. Use the AddHeader VI to add header lines to Web
       requests made by the GET VI.


      Inputs/Outputs

               •      output file —

           output file specifies a file to save body data returned by the server. If you do not specify an
           output file, the VI does not save the body data to a file.

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       url —


5256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5257 ordinal=5257 -->
## Functions

Functions


   URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
    request.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (10000) —

    timeout specifies the amount of time in milliseconds to wait for a response from the server
    before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
    monitoring to the operating system.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      headers —

    headers returns the header fields returned by the server. Refer to the World Wide Web
    Consortium website at www.w3.org for more information about header field definitions
    including available headers, descriptions, and syntax.

   •     body —

    body returns body data returned by the server.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Refer to the World Wide Web Consortium website at www.w3.org for more
information about HTTP method definitions, including the GET method.

Using the GET VI with LabVIEW Web Services

Use this VI to interact with a LabVIEW Web service. First, you must create and publish a
Web service, including the setup of a URL map to accept the GET method. You can then

                                                    © National Instruments 5257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5258 ordinal=5258 -->
## Functions

Functions

      use the GET VI to connect to that Web service by specifying a URL that corresponds to
       the Web service.

     HEADHEAD

      Sends a Web request that returns headers from a server, Web page, or Web service.
       This VI uses the HEAD HTTP method. This VI does not submit any data to the server or
       receive body data. The minimal data exchange makes the HEAD VI useful for testing
       the validity of a URL.

      You can assign a client handle to add authentication credentials, HTTP headers, or a
       cookie to Web requests made by the HEAD VI. Use the OpenHandle VI to open a client
      handle and establish credentials. Use the AddHeader VI to add header lines to Web
       requests made by the HEAD VI.


      Inputs/Outputs

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       url —

         URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
             request.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (10000) —


5258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5259 ordinal=5259 -->
## Functions

Functions


    timeout specifies the amount of time in milliseconds to wait for a response from the server
    before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
    monitoring to the operating system.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      headers —

    headers returns the header fields returned by the server. Refer to the World Wide Web
    Consortium website at www.w3.org for more information about header field definitions
    including available headers, descriptions, and syntax.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Refer to the World Wide Web Consortium website at www.w3.org for more
information about HTTP method definitions, including the HEAD method.

CloseHandleCloseHandle

Closes the client handle and deletes all stored cookies, authentication credentials,
and HTTP headers associated with the client handle. This VI also terminates all HTTP
connections and logs out of any authentication, if applicable.


Inputs/Outputs

   •       client handle —

     client handle specifies the client handle to associate with the Web request. Use client handles to
    wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP


                                                    © National Instruments 5259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5260 ordinal=5260 -->
## Functions

Functions


            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following screenshot shows code that performs the following:

         1. The OpenHandle VI opens a client handle and a client-side cookie that can store
           persistent data.
         2. The AddHeader VI adds a new header field line that sets the preferred language for
          subsequent Web requests associated with the client handle.
         3. The GET VI performs a Web request that includes the Accept-Language header.
         4. The CloseHandle VI closes the client handle and deletes any persistent data,
           including headers.


     PUTPUT

      Sends a Web request that submits data or a file to a server, Web page, or Web service.
       This VI uses the PUT HTTP method. Refer to the World Wide Web Consortium website
       at www.w3.org for more information about HTTP method definitions, including the
     PUT method.

      You can assign a client handle to add authentication credentials, HTTP headers, or a


5260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5261 ordinal=5261 -->
## Functions

Functions

cookie to Web requests made by the PUT VI. Use the OpenHandle VI to open a client
handle and establish credentials. Use the AddHeader VI to add header lines to Web
requests made by the PUT VI.


  • PUTBuffer VI
  • PUTFile VI

Using the PUT VI with LabVIEW Web Services

Use this VI to interact with a LabVIEW Web service. First, you must create and publish a
Web service, including the setup of a URL map to accept the PUT method. You can then
use the PUT VI to connect to that Web service by specifying a URL that corresponds to
the Web service.
PUTBufferPUTBuffer VIVI

Sends a Web request that submits data or a file to a server, Web page, or Web service.
This VI uses the PUT HTTP method. Refer to the World Wide Web Consortium website
at www.w3.org for more information about HTTP method definitions, including the
PUT method.

You can assign a client handle to add authentication credentials, HTTP headers, or a
cookie to Web requests made by the PUT VI. Use the OpenHandle VI to open a client
handle and establish credentials. Use the AddHeader VI to add header lines to Web
requests made by the PUT VI.


                                                    © National Instruments 5261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5262 ordinal=5262 -->
## Functions

Functions

      Inputs/Outputs

               •      output file —

           output file specifies a file to save body data returned by the server. If you do not specify an
           output file, the VI does not save the body data to a file.

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       url —

         URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
             request.

               •       buffer —

             buffer specifies a string of data to send to the server.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (10000) —

           timeout specifies the amount of time in milliseconds to wait for a response from the server
            before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
            monitoring to the operating system.

               •       client handle out —

              client handle out returns the client handle associated with the Web request. Use client handles
             to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      headers —

           headers returns the header fields returned by the server. Refer to the World Wide Web


5262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5263 ordinal=5263 -->
## Functions

Functions


    Consortium website at www.w3.org for more information about header field definitions
    including available headers, descriptions, and syntax.

   •     body —

    body returns body data returned by the server.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Using the PUT VI with LabVIEW Web Services

Use this VI to interact with a LabVIEW Web service. First, you must create and publish a
Web service, including the setup of a URL map to accept the PUT method. You can then
use the PUT VI to connect to that Web service by specifying a URL that corresponds to
the Web service.
PUTFilePUTFile VIVI

Sends a Web request that submits data or a file to a server, Web page, or Web service.
This VI uses the PUT HTTP method. Refer to the World Wide Web Consortium website
at www.w3.org for more information about HTTP method definitions, including the
PUT method.

You can assign a client handle to add authentication credentials, HTTP headers, or a
cookie to Web requests made by the PUT VI. Use the OpenHandle VI to open a client
handle and establish credentials. Use the AddHeader VI to add header lines to Web
requests made by the PUT VI.


                                                    © National Instruments 5263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5264 ordinal=5264 -->
## Functions

Functions

      Inputs/Outputs

               •      output file —

           output file specifies a file to save body data returned by the server. If you do not specify an
           output file, the VI does not save the body data to a file.

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       url —

         URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
             request.

               •        file —

                file specifies the file path of the file to send to the server as data. This VI extracts the data from
             that file and sends the data to the server.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (10000) —

           timeout specifies the amount of time in milliseconds to wait for a response from the server
            before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
            monitoring to the operating system.

               •       client handle out —

              client handle out returns the client handle associated with the Web request. Use client handles
             to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      headers —


5264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5265 ordinal=5265 -->
## Functions

Functions


    headers returns the header fields returned by the server. Refer to the World Wide Web
    Consortium website at www.w3.org for more information about header field definitions
    including available headers, descriptions, and syntax.

   •     body —

    body returns body data returned by the server.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Using the PUT VI with LabVIEW Web Services

Use this VI to interact with a LabVIEW Web service. First, you must create and publish a
Web service, including the setup of a URL map to accept the PUT method. You can then
use the PUT VI to connect to that Web service by specifying a URL that corresponds to
the Web service.

POSTPOST

Sends a Web request that submits data or a file to a server, Web page, or Web service.
This VI uses the POST HTTP method. Refer to the World Wide Web Consortium website
at www.w3.org for more information about HTTP method definitions, including the
POST method. Use the POSTMultipart VI to send POST requests using the multipart/
form-data MIME type.

You can assign a client handle to add authentication credentials, HTTP headers, or a
cookie to Web requests made by the POST VI. Use the OpenHandle VI to open a client
handle and establish credentials. Use the AddHeader VI to add header lines to Web
requests made by the POST VI.


  • POSTBuffer VI
  • POSTFile VI


                                                    © National Instruments 5265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5266 ordinal=5266 -->
## Functions

Functions

      Using the POST VI with LabVIEW Web Services

      Use this VI to interact with a LabVIEW Web service. First, you must create and publish a
     Web service, including the setup of a URL map to accept the POST method. You can
      then use the POST VI to connect to that Web service by specifying a URL that
      corresponds to the Web service.
   POSTBufferPOSTBuffer VIVI

      Sends a Web request that submits data or a file to a server, Web page, or Web service.
       This VI uses the POST HTTP method. Refer to the World Wide Web Consortium website
       at www.w3.org for more information about HTTP method definitions, including the
     POST method. Use the POSTMultipart VI to send POST requests using the multipart/
       form-data MIME type.

      You can assign a client handle to add authentication credentials, HTTP headers, or a
       cookie to Web requests made by the POST VI. Use the OpenHandle VI to open a client
      handle and establish credentials. Use the AddHeader VI to add header lines to Web
       requests made by the POST VI.


      Inputs/Outputs

               •      output file —

           output file specifies a file to save body data returned by the server. If you do not specify an
           output file, the VI does not save the body data to a file.

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests


5266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5267 ordinal=5267 -->
## Functions

Functions


  without persistent data such as headers or credentials.

•       url —

  URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
  request.

•       buffer —

  buffer specifies a string of data to send to the server.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      timeout (10000) —

  timeout specifies the amount of time in milliseconds to wait for a response from the server
  before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
  monitoring to the operating system.

•       client handle out —

  client handle out returns the client handle associated with the Web request. Use client handles
  to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
  headers, and cookies. Client handles are not required when making independent Web requests
  without persistent data such as headers or credentials.

•      headers —

  headers returns the header fields returned by the server. Refer to the World Wide Web
  Consortium website at www.w3.org for more information about header field definitions
  including available headers, descriptions, and syntax.

•     body —

  body returns body data returned by the server.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 5267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5268 ordinal=5268 -->
## Functions

Functions

      Using the POST VI with LabVIEW Web Services

      Use this VI to interact with a LabVIEW Web service. First, you must create and publish a
     Web service, including the setup of a URL map to accept the POST method. You can
      then use the POST VI to connect to that Web service by specifying a URL that
      corresponds to the Web service.
   POSTFilePOSTFile VIVI

      Sends a Web request that submits data or a file to a server, Web page, or Web service.
       This VI uses the POST HTTP method. Refer to the World Wide Web Consortium website
       at www.w3.org for more information about HTTP method definitions, including the
     POST method. Use the POSTMultipart VI to send POST requests using the multipart/
       form-data MIME type.

      You can assign a client handle to add authentication credentials, HTTP headers, or a
       cookie to Web requests made by the POST VI. Use the OpenHandle VI to open a client
      handle and establish credentials. Use the AddHeader VI to add header lines to Web
       requests made by the POST VI.


      Inputs/Outputs

               •      output file —

           output file specifies a file to save body data returned by the server. If you do not specify an
           output file, the VI does not save the body data to a file.

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests


5268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5269 ordinal=5269 -->
## Functions

Functions


  without persistent data such as headers or credentials.

•       url —

  URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
  request.

•        file —

   file specifies the file path of the file to send to the server as data. This VI extracts the data from
  that file and sends the data to the server.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      timeout (10000) —

  timeout specifies the amount of time in milliseconds to wait for a response from the server
  before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
  monitoring to the operating system.

•       client handle out —

  client handle out returns the client handle associated with the Web request. Use client handles
  to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
  headers, and cookies. Client handles are not required when making independent Web requests
  without persistent data such as headers or credentials.

•      headers —

  headers returns the header fields returned by the server. Refer to the World Wide Web
  Consortium website at www.w3.org for more information about header field definitions
  including available headers, descriptions, and syntax.

•     body —

  body returns body data returned by the server.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 5269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5270 ordinal=5270 -->
## Functions

Functions

      Using the POST VI with LabVIEW Web Services

      Use this VI to interact with a LabVIEW Web service. First, you must create and publish a
     Web service, including the setup of a URL map to accept the POST method. You can
      then use the POST VI to connect to that Web service by specifying a URL that
      corresponds to the Web service.

      POSTMultipartPOSTMultipart

      Sends a Web request that submits multiple sets of data or files to a server, Web page,
       or Web service. This VI uses the POST HTTP method and multipart/form-data MIME
       type.

      The POSTMultipart VI submits multiple sets of data, represented by an array of
      postdata clusters. Use the postdata control descriptions to configure the submitted
       data as one of the four available combinations. For example, the VI can accept a buffer
       data string from the client and send that data as a file to the server.


      Inputs/Outputs

               •      output file —

           output file specifies a file to save body data returned by the server. If you do not specify an
           output file, the VI does not save the body data to a file.

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       url —


5270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5271 ordinal=5271 -->
## Functions

Functions


  URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
  request.

•      data —

  data is the array of clusters specifying the data attributes and values to submit to the server. The
  POSTMultipart VI determines which data format to accept from the client and which format to
  send the data to the server based upon the controls specified within data.

      •     Name —

      •      Value —

      •       File —

      •      Filename —

      •     MIME type —

     MIME Type specifies the MIME type for the Web request. The default value is
     application/octet-stream.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      timeout (10000) —

  timeout specifies the amount of time in milliseconds to wait for a response from the server
  before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
  monitoring to the operating system.

•       client handle out —

  client handle out returns the client handle associated with the Web request. Use client handles
  to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
  headers, and cookies. Client handles are not required when making independent Web requests
  without persistent data such as headers or credentials.

•      headers —


                                                   © National Instruments 5271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5272 ordinal=5272 -->
## Functions

Functions


           headers returns the header fields returned by the server. Refer to the World Wide Web
           Consortium website at www.w3.org for more information about header field definitions
             including available headers, descriptions, and syntax.

               •     body —

          body returns body data returned by the server.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The POSTMultipart VI can submit either buffer data, such as a string, or a file from the
        client. The VI can then instruct the server to save the accepted data as either server-
       side buffer data or a file. The POSTMultipart VI determines which data format to accept
      from the client and which format to send the data to the server based upon the
       controls specified within each postdata cluster. The following screenshot shows four
        clusters, each configured as one of four available client-side/server-side combinations.


       Refer to the World Wide Web Consortium website at www.w3.org for more
       information about the POST method and the multipart content type.

     DELETEDELETE

      Sends a Web request to delete resources on a server, Web page, or Web service. This VI


5272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5273 ordinal=5273 -->
## Functions

Functions

uses the DELETE HTTP method. The server accepting the request from the DELETE VI
must be setup to delete resources solely based upon receiving a DELETE Web request
at the specified URL.

You can assign a client handle to add authentication credentials, HTTP headers, or a
cookie to Web requests made by the DELETE VI. Use the OpenHandle VI to open a
client handle and establish credentials. Use the AddHeader VI to add header lines to
Web requests made by the DELETE VI.


Inputs/Outputs

   •      output file —

    output file specifies a file to save body data returned by the server. If you do not specify an
    output file, the VI does not save the body data to a file.

   •       client handle —

     client handle specifies the client handle to associate with the Web request. Use client handles to
    wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •       url —

   URL specifies the URL of the server, Web page, or Web service which this VI sends the Web
    request.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (10000) —

    timeout specifies the amount of time in milliseconds to wait for a response from the server


                                                    © National Instruments 5273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5274 ordinal=5274 -->
## Functions

Functions


            before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
            monitoring to the operating system.

               •       client handle out —

              client handle out returns the client handle associated with the Web request. Use client handles
             to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      headers —

           headers returns the header fields returned by the server. Refer to the World Wide Web
           Consortium website at www.w3.org for more information about header field definitions
             including available headers, descriptions, and syntax.

               •     body —

          body returns body data returned by the server.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Refer to the World Wide Web Consortium website at www.w3.org for more
       information about HTTP method definitions, including the DELETE method.

       SecuritySecurity

      Use the Security VIs to encrypt and decrypt data transfers. You also can use these VIs
       with the Web Services Security VIs.


         Palette
                    Description
        Object

        ConfigSSL  Provides Transport Layer Security (TLS), previously known as Secure Sockets Layer


5274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5275 ordinal=5275 -->
## Functions

Functions


 Palette            Description
 Object

             (SSL), authentication for Web requests associated with the client handle. Use TLS/SSL
            authentication with other HTTP Client VIs to send Web requests to a server, Web page,
            or Web service using TLS/SSL.


            Provides API Key authentication credentials for Web requests associated with the client
            handle. API key security is one available option to protect LabVIEW Web services. Client SetAPIKey           handles save the credentials across multiple Web requests. Use the Open Handle VI to
          open a client handle.


            Negotiates a key with the host and adds the key to the client handle. Use this key with
 ConfigKey  the Encrypt and Decrypt VIs to encrypt and decrypt data. This functionality only works
           with NI Web servers. Use the OpenHandle VI to open a client handle.


            Encrypts data using the key associated with the client handle. Associate a key with a
 Encrypt    client handle using the ConfigKey VI. This functionality only works with NI Web servers.
          Use the OpenHandle VI to open a client handle.


           Decrypts data using the key associated with the client handle. Associate a key with a
 Decrypt    client handle using the ConfigKey VI. This functionality only works with NI Web servers.
          Use the OpenHandle VI to open a client handle.

ConfigSSLConfigSSL

Provides Transport Layer Security (TLS), previously known as Secure Sockets Layer
(SSL), authentication for Web requests associated with the client handle. Use TLS/SSL
authentication with other HTTP Client VIs to send Web requests to a server, Web page,
or Web service using TLS/SSL.


                                                    © National Instruments 5275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5276 ordinal=5276 -->
## Functions

Functions


      Inputs/Outputs

               •       private key password —

             private key password specifies a password for the private key file. If the private key file is not
            encrypted, you do not have to specify a private key password.

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •     CA certificate file —

          CA certificate file specifies the path to a list of trusted certificate authority (CA) certificates. If you
             specify TRUE for the verify server control, the client verifies the server's identity against this list
             of trusted certificates.

               •       client certificate file —

               •       private key file —

             private key file specifies the path to a private key file that is part of the client certificate and
              client authentication process.

                    If the server requires client authentication, you must specify a client certificate file and a private
           key file. If you need to transfer this file between client systems, especially over a network, you
           can assign a password when you create the private key file. To use password-protected private
           key files with this VI, assign the password to the private key password input.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       verify server (true) —

5276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5277 ordinal=5277 -->
## Functions

Functions


     verify server specifies whether to check the server's certificate against the list of trusted CA
     certificates specified by the CA certificate file control.

       If TRUE, this VI verifies the server's identity against the list of trusted CA certificates for optimal
     security. If FALSE, this VI does not verify the server's identity and does not provide optimal
     security. Specifying FALSE allows the client to accept self-signed certificates signed by the
     certificate creator rather than a trusted CA. The default is TRUE.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the ConfigSSL VI to verify the server's identity against a list of trusted certificate
authority (CA) certificates, and provide client authentication, if required by the server.
Client handles save the TLS/SSL credentials across multiple Web requests. Use the
OpenHandle VI to open a client handle.

TLS/SSL encryption uses certificates to establish secure connections between a client
and a server. Certificates are binary files that contain identifying information about the
server, as well as a public key and a digital signature. The digital signature can be
added by a certificate authority (CA), a trusted third party that issues digital
certifications, or by the certificate creator, which is called a self-signed certificate.

The following screenshot shows code that performs the following:

 1. The OpenHandle VI opens a client handle and a client-side cookie that can store
    persistent data.
 2. The ConfigSSL VI establishes TLS/SSL credentials including server authentication
   and client authentication.
 3. The GET VI performs a Web request with TLS/SSL authentication.
 4. The CloseHandle VI closes the client handle and closes the TLS/SSL-protected
   connection between the client and the server.

                                                    © National Instruments 5277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5278 ordinal=5278 -->
## Functions

Functions


      Using the ConfigSSL VI with LabVIEW Web Services

      Use this VI to connect with LabVIEW Web services protected by TLS/SSL. First, you
      must build and deploy a Web service, including the setup of TLS/SSL security. You can
      then use the ConfigSSL VI to authenticate all Web requests to that Web service
       associated with the Client Handle.
   SetAPIKeySetAPIKey

       Provides API Key authentication credentials for Web requests associated with the
        client handle. API key security is one available option to protect LabVIEW Web
        services. Client handles save the credentials across multiple Web requests. Use the
     Open Handle VI to open a client handle.


      Inputs/Outputs

               •     mode —

         mode specifies the API key mode. The default value is NIWS.

               •       client handle —


5278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5279 ordinal=5279 -->
## Functions

Functions


     client handle specifies the client handle to associate with the Web request. Use client handles to
    wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      access id —

    access id specifies the public component of the API key when accessing a LabVIEW Web service.
    The access id must match the Access ID when you setup API key security on the Application Web
     Server.

   •       secret id —

    secret id specifies the private component of the API key when accessing a LabVIEW Web service.
    The secret id must match the Secret ID when you setup API key security on the Application Web
     Server.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ConfigKeyConfigKey

Negotiates a key with the host and adds the key to the client handle. Use this key with
the Encrypt and Decrypt VIs to encrypt and decrypt data. This functionality only works
with NI Web servers. Use the OpenHandle VI to open a client handle.


                                                    © National Instruments 5279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5280 ordinal=5280 -->
## Functions

Functions


      Inputs/Outputs

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      host —

            host specifies the host name associated with the key.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (10000) —

           timeout specifies the amount of time in milliseconds to wait for a response from the server
            before the Web request times out. The default value is 10000 ms. A value of -1 defers timeout
            monitoring to the operating system.

               •       client handle out —

              client handle out returns the client handle associated with the Web request. Use client handles
             to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   EncryptEncrypt

       Encrypts data using the key associated with the client handle. Associate a key with a

5280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5281 ordinal=5281 -->
## Functions

Functions

client handle using the ConfigKey VI. This functionality only works with NI Web
servers. Use the OpenHandle VI to open a client handle.


Inputs/Outputs

   •       client handle —

     client handle specifies the client handle to associate with the Web request. Use client handles to
    wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      host —

    host specifies the host name associated with the key.

   •      data —

    data specifies the data to encrypt.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      encrypted data —

    encrypted data returns the encrypted data.

   •       error out —


                                                    © National Instruments 5281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5282 ordinal=5282 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

   DecryptDecrypt

       Decrypts data using the key associated with the client handle. Associate a key with a
        client handle using the ConfigKey VI. This functionality only works with NI Web
        servers. Use the OpenHandle VI to open a client handle.


      Inputs/Outputs

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      host —

            host specifies the host name associated with the key.

               •      encrypted data —

           encrypted data specifies the data to decrypt.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       client handle out —

              client handle out returns the client handle associated with the Web request. Use client handles
             to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP


5282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5283 ordinal=5283 -->
## Functions

Functions


    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      decrypted data —

    decrypted data returns the decrypted data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


HeadersHeaders

Use the Headers VIs to manage header field lines for Web requests associated with
client handles. These VIs also can interact with LabVIEW Web services.


 Palette Object  Description

              Adds a header field line to all Web requests associated with the client handle. AddHeader               Headers define attributes of the data exchanged between the client and server.


              Removes a header field line from all Web requests associated with the client
                handle. Headers define attributes of the data exchanged between the client and
                   server. Client handles save header values across multiple Web requests. Use the
 RemoveHeader             Open Handle VI to create a client handle. Refer to the World Wide Web Consortium
                website at www.w3.org for more information about header field definitions
                 including example headers, descriptions, and syntax.


                Returns the value assigned to the header of the client handle. Headers define
                  attributes of the data exchanged between the client and server. Client handles
 GetHeader      save header values across multiple Web requests. Use the Open Handle VI to
                 create a client handle. Refer to the World Wide Web Consortium website at
            www.w3.org for more information about header field definitions including


                                                    © National Instruments 5283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5284 ordinal=5284 -->
## Functions

Functions


         Palette Object  Description

                      example headers, descriptions, and syntax.


                       Determines if the header is associated with the client handle. Headers define
                           attributes of the data exchanged between the client and server. Client handles
                       save header values across multiple Web requests. Use the Open Handle VI to
         HeaderExists                          create a client handle. Refer to the World Wide Web Consortium website at
                  www.w3.org for more information about header field definitions including
                      example headers, descriptions, and syntax.


                             Lists the headers associated with the client handle. Headers define attributes of
                        the data exchanged between the client and server. Client handles save header
                         values across multiple Web requests. Use the Open Handle VI to create a client
         ListHeaders                        handle. Refer to the World Wide Web Consortium website at www.w3.org for
                    more information about header field definitions including example headers,
                           descriptions, and syntax.

   AddHeaderAddHeader

      Adds a header field line to all Web requests associated with the client handle. Headers
       define attributes of the data exchanged between the client and server.

           If you specify a header that already exists, the specified value overwrites the header
       value. Use RemoveHeader to remove headers.


      Inputs/Outputs

               •       client handle —


5284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5285 ordinal=5285 -->
## Functions

Functions


     client handle specifies the client handle to associate with the Web request. Use client handles to
    wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      header —

    header specifies the header field to add to all Web requests associated with the client handle.
    The header control provides a pull-down menu with some available header fields.

       If you specify a header that already exists, the specified value overwrites the header value.

   •      value —

    value specifies the value to assign to the header field.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Client handles save header values across multiple Web requests. Use the Open Handle
VI to create a client handle. Refer to the World Wide Web Consortium website at
www.w3.org for more information about header field definitions including example
headers, descriptions, and syntax.

The following screenshot shows code that performs the following:

 1. The OpenHandle VI opens a client handle and a client-side cookie that can store
    persistent data.


                                                    © National Instruments 5285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5286 ordinal=5286 -->
## Functions

Functions

         2. The AddHeader VI adds a new header field line that sets the preferred language for
          subsequent Web requests associated with the client handle.
         3. The GET VI performs a Web request that includes the Accept-Language header.
         4. The CloseHandle VI closes the client handle and deletes any persistent data,
           including headers.


   RemoveHeaderRemoveHeader

      Removes a header field line from all Web requests associated with the client handle.
      Headers define attributes of the data exchanged between the client and server. Client
      handles save header values across multiple Web requests. Use the Open Handle VI to
       create a client handle. Refer to the World Wide Web Consortium website at
     www.w3.org for more information about header field definitions including example
       headers, descriptions, and syntax.


      Inputs/Outputs

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      header —


5286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5287 ordinal=5287 -->
## Functions

Functions


    header specifies a header field included in the Web requests of the client handle. The header
    control provides a pull-down menu with some available header fields.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetHeaderGetHeader

Returns the value assigned to the header of the client handle. Headers define
attributes of the data exchanged between the client and server. Client handles save
header values across multiple Web requests. Use the Open Handle VI to create a client
handle. Refer to the World Wide Web Consortium website at www.w3.org for more
information about header field definitions including example headers, descriptions,
and syntax.


Inputs/Outputs

   •       client handle —

     client handle specifies the client handle to associate with the Web request. Use client handles to
    wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP


                                                    © National Instruments 5287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5288 ordinal=5288 -->
## Functions

Functions


            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      header —

           header specifies a header field included in the Web requests of the client handle. The header
             control provides a pull-down menu with some available header fields.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       client handle out —

              client handle out returns the client handle associated with the Web request. Use client handles
             to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      value —

            value returns the value assigned to the header.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If the client handle does not include a header, this VI returns an error. Use
       HeaderExists to return header values for client handles that may not include headers.
    HeaderExistsHeaderExists

      Determines if the header is associated with the client handle. Headers define
        attributes of the data exchanged between the client and server. Client handles save
      header values across multiple Web requests. Use the Open Handle VI to create a client
       handle. Refer to the World Wide Web Consortium website at www.w3.org for more
       information about header field definitions including example headers, descriptions,
      and syntax.


5288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5289 ordinal=5289 -->
## Functions

Functions


Inputs/Outputs

   •       client handle —

     client handle specifies the client handle to associate with the Web request. Use client handles to
    wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      header —

    header specifies a header field included in the Web requests of the client handle. The header
    control provides a pull-down menu with some available header fields.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       client handle out —

     client handle out returns the client handle associated with the Web request. Use client handles
    to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
    headers, and cookies. Client handles are not required when making independent Web requests
    without persistent data such as headers or credentials.

   •      header exists? —

    header exists? returns TRUE if the specified header is associated with the client handle.

   •      value —

    value returns the value assigned to the header. If header exists? returns FALSE, this output
    returns an empty string.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5290 ordinal=5290 -->
## Functions

Functions

    ListHeadersListHeaders

        Lists the headers associated with the client handle. Headers define attributes of the
       data exchanged between the client and server. Client handles save header values
       across multiple Web requests. Use the Open Handle VI to create a client handle. Refer
       to the World Wide Web Consortium website at www.w3.org for more information
      about header field definitions including example headers, descriptions, and syntax.


      Inputs/Outputs

               •       client handle —

              client handle specifies the client handle to associate with the Web request. Use client handles to
            wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       client handle out —

              client handle out returns the client handle associated with the Web request. Use client handles
             to wire together multiple HTTP Client VIs while preserving authentication credentials, HTTP
            headers, and cookies. Client handles are not required when making independent Web requests
            without persistent data such as headers or credentials.

               •      headers —

           headers returns the headers associated with the client handle.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5291 ordinal=5291 -->
## Functions

Functions

FTPFTP

Use the FTP VIs to send and retrieve raw data and files to and from an FTP server.

The VIs on this palette can return FTP error codes.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


 Palette Object        Description

 FTP Get Buffer        Connects to an FTP server and returns the contents of a single file.


 FTP Get File          Connects to an FTP server and copies a single file to the local machine.


 FTP Get Multiple                     Connects to an FTP server and returns the contents of a list of files.
 Buffers


 FTP Get Multiple Files  Connects to an FTP server and copies a list of files to the local machine.


 FTP Get Multiple Files  Connects to an FTP server and copies a list of files, saving the files on the
 and Buffers             local machine or returning their contents.


                    Use the Intermediate FTP VIs to configure options for sending and receiving
 Intermediate FTP
                      data to and from an FTP server.


 FTP Put Buffer        Connects to an FTP server and stores the contents of a single buffer.


                                                    © National Instruments 5291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5292 ordinal=5292 -->
## Functions

Functions


         Palette Object        Description

                            Connects to an FTP server and copies the contents of a single file from the
       FTP Put File                                  local machine.


       FTP Put Multiple                            Connects to an FTP server and stores the contents of multiple buffers.         Buffers


                            Connects to an FTP server and copies the contents of multiple files from the       FTP Put Multiple Files                                  local machine.


       FTP Put Multiple Files  Connects to an FTP server and copies the contents of multiple files or
       and Buffers            buffers from the local machine.


     FTPFTP GetGet BufferBuffer

      Connects to an FTP server and returns the contents of a single file.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

5292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5293 ordinal=5293 -->
## Functions

Functions


  password is the password that authenticates the username.

  (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
  server does not accept NI-Auth credentials.

•      user —

  user is the name you want to use to log on to the FTP server.

  The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
   this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

•      host —

  host is the name or IP address of an FTP server.

•      remote path —

  remote path is a path to a file on the FTP server. The remote path input supports Windows-like
   file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-rt/
  system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input supports
  paths such as /c:/ni-rt/system/a.txt.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      binary (F) —

  binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in which
  the VI transfers data in ASCII mode.

•       active (T) —

  active specifies whether the data connection is active or passive. The default is TRUE, which
  specifies an active connection.

•        file error —

   file error lists any file-related errors, such as invalid remote path or file access permission
  denied.

•      data —


                                                   © National Instruments 5293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5294 ordinal=5294 -->
## Functions

Functions


           data contains the contents of the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     FTPFTP GetGet FileFile

      Connects to an FTP server and copies a single file to the local machine.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.


5294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5295 ordinal=5295 -->
## Functions

Functions


  The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
   this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

•      host —

  host is the name or IP address of an FTP server.

•      remote path —

  remote path is a path to a file on the FTP server. The remote path input supports Windows-like
   file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-rt/
  system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input supports
  paths such as /c:/ni-rt/system/a.txt.

•       local path —

  local path is the path to the location where you store the local file. If you do not wire local path,
  a file dialog box prompts you for a location.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      binary (F) —

  binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in which
  the VI transfers data in ASCII mode.

•       active (T) —

  active specifies whether the data connection is active or passive. The default is TRUE, which
  specifies an active connection.

•        file error —

   file error lists any file-related errors, such as invalid remote path or file access permission
  denied.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 5295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5296 ordinal=5296 -->
## Functions

Functions

     FTPFTP GetGet MultipleMultiple BuffersBuffers

      Connects to an FTP server and returns the contents of a list of files.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •        file specifications —

                file specifications contains the FTP configuration for file transfers.


5296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5297 ordinal=5297 -->
## Functions

Functions


         •      remote path —

       remote path is a path to a file on the FTP server. The remote path input supports Windows-
          like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
       rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
        supports paths such as /c:/ni-rt/system/a.txt.

         •      binary —

        binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in
        which the VI transfers data in ASCII mode.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file errors —

      file errors is an array of error clusters containing file-related errors, such as invalid remote path
    and file access permission denied.

   •      data —

    data is an array of strings that contains the contents of the files.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FTPFTP GetGet MultipleMultiple FilesFiles

Connects to an FTP server and copies a list of files to the local machine.


                                                    © National Instruments 5297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5298 ordinal=5298 -->
## Functions

Functions


      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •        file specifications —

                file specifications contains the FTP configuration for file transfers.

                     •      remote path —

              remote path is a path to a file on the FTP server. The remote path input supports Windows-
                    like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
             rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
                supports paths such as /c:/ni-rt/system/a.txt.

                     •       local path —


5298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5299 ordinal=5299 -->
## Functions

Functions


         local path is the path to the location where you store the local file. If you do not wire local
         path, a file dialog box prompts you for a location.

         •      binary —

        binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in
        which the VI transfers data in ASCII mode.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file errors —

      file errors is an array of error clusters containing file-related errors, such as invalid remote path
    and file access permission denied.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FTPFTP GetGet MultipleMultiple FilesFiles andand BuffersBuffers

Connects to an FTP server and copies a list of files, saving the files on the local
machine or returning their contents.


                                                    © National Instruments 5299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5300 ordinal=5300 -->
## Functions

Functions

      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •        file specifications —

                file specifications contains the FTP configuration for file transfers.

                     •      remote path —

              remote path is a path to a file on the FTP server. The remote path input supports Windows-
                    like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
             rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
                supports paths such as /c:/ni-rt/system/a.txt.

                     •       local path —

                  local path is the path to the location where you store the local file. If you do not wire local
                 path, a file dialog box prompts you for a location.

                     •      binary —

                binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in


5300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5301 ordinal=5301 -->
## Functions

Functions


        which the VI transfers data in ASCII mode.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file errors —

      file errors is an array of error clusters containing file-related errors, such as invalid remote path
    and file access permission denied.

   •      data —

    data is an array of strings that contains the contents of the files.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


IntermediateIntermediate FTPFTP

Use the Intermediate FTP VIs to configure options for sending and receiving data to
and from an FTP server.

The VIs on this palette can return FTP error codes.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


                                                    © National Instruments 5301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5302 ordinal=5302 -->
## Functions

Functions


         Palette                   Description
        Object

       FTP       Displays the status of an FTP transaction. Use this VI only to open or close the status
         Status    window.


       FTP                  Converts an FTP reply into a class (first digit), sub-class (second digit), and code (third        Check                        digit). The VI also determines whether the reply is within an expected class.
        Reply

       FTP
                  Returns the error if error in contains an error. Otherwise, the VI converts an FTP reply        Reply To                    into an FTP error code.         Error

       FTP
       Open    Opens an FTP connection to an FTP server.
         Session

       FTP
                 Logs on to an FTP server.        Logon

       FTP
       Rename  Renames a file on the FTP server.
           File

       FTP
         Close    Sends the QUIT command and closes the FTP connection associated with ftp session.
         Session

       FTP      Returns a list of entries for a directory on the FTP server. The VI uses the LIST command
         Directory  to interpret the list as a UNIX ls command output. If the VI fails, it uses the LIST
          Listing   command to retrieve the list of names in the directory.


       FTP Get
                  Returns information about a path on the FTP server.
        Path Info

       FTP
         Retrieve  Copies a list of files, saving them on the local machine or returning their contents.
         Multiple


5302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5303 ordinal=5303 -->
## Functions

Functions


 Palette           Description
 Object

 FTP
 Store     Copies the contents of multiple files or buffers from the local machine.
 Multiple

FTPFTP StatusStatus

Displays the status of an FTP transaction. Use this VI only to open or close the status
window.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


Inputs/Outputs

   •      action string —

    action string is the string sent to the FTP server.

   •       status string —

    status string is the first line of the reply the FTP server returns.

   •     window —

   window controls the VI panel.

   nothing assigns an action and status string, open opens the VI panel, and close closes the VI
    panel.

   •     command —

   command contains the action string in progress.


                                                    © National Instruments 5303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5304 ordinal=5304 -->
## Functions

Functions

               •       last status string —

              last status string contains the most recent status string.

   FTPFTP CheckCheck ReplyReply

       Converts an FTP reply into a class (first digit), sub-class (second digit), and code (third
         digit). The VI also determines whether the reply is within an expected class.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •       reply —

            reply is the reply code that an FTP command returns.

               •      expected class —

           expected class is the class that reply is expected to be in. The default expected class is 500 –
           Permanent.

          The expected class can be any of the following values:

           0    unknown
           1     100 + Prelim
           2     200 +
           3     300 + Intermed
           4     400 – Transient
           5     500 – Permanent

               •       class —

5304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5305 ordinal=5305 -->
## Functions

Functions


     class contains the class (first digit) of the reply.

    The class can be any of the following values:

    0    unknown
    1     100 + Prelim
    2     200 +
    3     300 + Intermed
    4     400 – Transient
    5     500 – Permanent

   •      sub class —

    sub class contains the subclass (second digit) of the reply.

    The sub class can be any of the following values:

    0      Syntax
    1      Information
    2      Connection
    3      Authentication
    4      Unspecified
    5       File System
    6     Unknown

   •      code —

    code contains the code (third digit) of the reply.

   •     match —

    match returns TRUE if class is the same as expected class.

FTPFTP ReplyReply ToTo ErrorError

Returns the error if error in contains an error. Otherwise, the VI converts an FTP reply
into an FTP error code.


                                                    © National Instruments 5305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5306 ordinal=5306 -->
## Functions

Functions

           If the FTP reply code is not successful (outside the 200–299 range), the VI sets the
       status in error out to TRUE.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •       ftp session —

              ftp session contains the refnum to an FTP session.

               •       reply code in —

            reply code in is the reply code returned from an FTP command.

               •       reply string in —

            reply string in is the reply string returned from an FTP command.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       ftp session out —

              ftp session out returns the same value as ftp session.

               •      duplicate reply code —

            duplicate reply code returns the same value as reply code in.

               •      duplicate reply string —

            duplicate reply string returns the same string as reply string in.

               •       error out —

5306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5307 ordinal=5307 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

FTPFTP OpenOpen SessionSession

Opens an FTP connection to an FTP server.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


Inputs/Outputs

   •      address —

    address is the TCP/IP address of the remote FTP server.

   •      remote port (21) —

    remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

   •      timeout ms (60000) —

    timeout ms specifies the time, in milliseconds, that the VI waits when another VI makes a
    request on the same session handle before it returns an error. The default is 60,000 ms, or 1
    minute.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       local port —


                                                    © National Instruments 5307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5308 ordinal=5308 -->
## Functions

Functions


             local port is the local TCP/IP port used by the connection.

               •       ftp session —

              ftp session is an FTP session refnum that uniquely identifies the FTP connection.

               •       reply code —

            reply code is the FTP status code in the reply string.

               •       reply string —

            reply string is the reply that the FTP server returns.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FTPFTP LogonLogon

      Logs on to an FTP server.

      Logs on using the USER, PASS, ACCT, and CWD commands.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •       ftp session —


5308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5309 ordinal=5309 -->
## Functions

Functions


  ftp session contains the refnum to an FTP session.

•      user —

  user is the name you want to use to log on to the FTP server.

  The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
   this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

•      password —

  password is the password that authenticates the username.

  (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
  server does not accept NI-Auth credentials.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      account —

  account is the account used to log on to the FTP server.

•       starting path —

  starting path is the directory to which the FTP server changes.

•       ftp session out —

  ftp session out returns the same value as ftp session.

•       reply code —

  reply code is the FTP status code in the reply string.

•       reply string —

  reply string is the reply that the FTP server returns.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 5309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5310 ordinal=5310 -->
## Functions

Functions

   FTPFTP RenameRename FileFile

      Renames a file on the FTP server.

      Renames the file using the RNFR and RNTO commands.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •       ftp session —

              ftp session contains the refnum to an FTP session.

               •      old name —

            old name is the path to the file the VI renames.

               •     new name —

         new name is the name you want to replace the old name.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       ftp session out —

              ftp session out returns the same value as ftp session.

               •       reply code —

            reply code is the FTP status code in the reply string.


5310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5311 ordinal=5311 -->
## Functions

Functions

   •       reply string —

    reply string is the reply that the FTP server returns.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

FTPFTP CloseClose SessionSession

Sends the QUIT command and closes the FTP connection associated with ftp session.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


Inputs/Outputs

   •       ftp session —

     ftp session contains the refnum to an FTP session.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       ftp session out —

     ftp session out returns the same value as ftp session.

   •       reply code —

    reply code is the FTP status code in the reply string.

   •       reply string —

                                                    © National Instruments 5311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5312 ordinal=5312 -->
## Functions

Functions


            reply string is the reply that the FTP server returns.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FTPFTP DirectoryDirectory ListingListing

       Returns a list of entries for a directory on the FTP server. The VI uses the LIST
     command to interpret the list as a UNIX ls command output. If the VI fails, it uses the
     LIST command to retrieve the list of names in the directory.

           Note Only the name in the array cluster is guaranteed to be correct.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •       active (T) —

             active specifies whether the data connection is active or passive. The default is TRUE, which
              specifies an active connection.

               •       ftp session —

              ftp session contains the refnum to an FTP session.

               •       directory path —


5312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5313 ordinal=5313 -->
## Functions

Functions


  directory path is the path to a directory on the FTP server.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       ftp session out —

  ftp session out returns the same value as ftp session.

•       reply code —

  reply code is the FTP status code in the reply string.

•       reply string —

  reply string is the reply that the FTP server returns.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•       dir list —

  dir list contains information about directory entries, such as the entry name, modification date,
   size, and type.

      •      type —

      type is the type of entry.

     unknown, file, dir, link.

      •      permissions —

      permissions contains the UNIX permissions for the entry.

      •     owner —

     owner is the UNIX owner name of the entry.

      •      group —


                                                   © National Instruments 5313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5314 ordinal=5314 -->
## Functions

Functions


              group is the UNIX group name of the entry.

                     •       size —

                  size is the size, in bytes, of the entry.

                     •      date —

               date is the modification date of the entry.

                     •     name —

            name is the name of the entry.

                     •       link name —

                  link name is the path to which this entry is linked.

   FTPFTP GetGet PathPath InfoInfo

       Returns information about a path on the FTP server.

       This VI uses the LIST command to interpret the information as a UNIX ls command
       output. If the VI fails, only the name in the path info cluster is correct.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


5314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5315 ordinal=5315 -->
## Functions

Functions

Inputs/Outputs

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •       ftp session —

     ftp session contains the refnum to an FTP session.

   •      remote path —

    remote path is a path to a file on the FTP server. The remote path input supports Windows-like
      file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-rt/
   system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input supports
    paths such as /c:/ni-rt/system/a.txt.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       ftp session out —

     ftp session out returns the same value as ftp session.

   •       reply code —

    reply code is the FTP status code in the reply string.

   •       reply string —

    reply string is the reply that the FTP server returns.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      path info —

    path info is a cluster containing information about the following directory entries.

         •      type —


                                                    © National Instruments 5315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5316 ordinal=5316 -->
## Functions

Functions


               type is the type of entry.

             unknown, file, dir, link.

                     •      permissions —

                permissions contains the UNIX permissions for the entry.

                     •     owner —

              owner is the UNIX owner name of the entry.

                     •      group —

              group is the UNIX group name of the entry.

                     •       size —

                  size is the size, in bytes, of the entry.

                     •      date —

               date is the modification date of the entry.

                     •     name —

            name is the name of the entry.

                     •       link name —

                  link name is the path to which this entry is linked.

   FTPFTP RetrieveRetrieve MultipleMultiple

      Copies a list of files, saving them on the local machine or returning their contents.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.

5316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5317 ordinal=5317 -->
## Functions

Functions


Inputs/Outputs

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •       ftp session —

     ftp session contains the refnum to an FTP session.

   •        file specifications —

      file specifications contains the FTP configuration for file transfers.

         •      remote path —

       remote path is a path to a file on the FTP server. The remote path input supports Windows-
          like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
       rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
        supports paths such as /c:/ni-rt/system/a.txt.

         •       local path —

         local path is the path to the location where you store the local file. If you do not wire local
         path, a file dialog box prompts you for a location.

         •      binary —

        binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in
        which the VI transfers data in ASCII mode.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 5317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5318 ordinal=5318 -->
## Functions

Functions

               •       ftp session out —

              ftp session out returns the same value as ftp session.

               •        file errors —

                file errors is an array of error clusters containing file-related errors, such as invalid remote path
          and file access permission denied.

               •      data —

           data is an array of strings that contains the contents of the files.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FTPFTP StoreStore MultipleMultiple

      Copies the contents of multiple files or buffers from the local machine.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •       active (T) —

             active specifies whether the data connection is active or passive. The default is TRUE, which
              specifies an active connection.

               •       ftp session —

              ftp session contains the refnum to an FTP session.


5318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5319 ordinal=5319 -->
## Functions

Functions

•        file specifications —

   file specifications contains the FTP configuration for file transfers.

      •      remote path —

      remote path is a path to a file on the FTP server. The remote path input supports Windows-
        like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
     rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
      supports paths such as /c:/ni-rt/system/a.txt.

      •       local path —

       local path is the path to the location where you store the local file. If you do not wire local
      path, a file dialog box prompts you for a location.

      •      binary —

      binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in
      which the VI transfers data in ASCII mode.

      •      data —

      data is a string that contains the data you want to transfer.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       ftp session out —

  ftp session out returns the same value as ftp session.

•        file errors —

   file errors is an array of error clusters containing file-related errors, such as invalid remote path
  and file access permission denied.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 5319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5320 ordinal=5320 -->
## Functions

Functions

     FTPFTP PutPut BufferBuffer

      Connects to an FTP server and stores the contents of a single buffer.

        (NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
       safe mode. National Instruments recommends using WebDAV as the file transfer
      mechanism for improved security.


      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •      remote path —


5320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5321 ordinal=5321 -->
## Functions

Functions


    remote path is a path to a file on the FTP server. The remote path input supports Windows-like
      file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-rt/
   system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input supports
    paths such as /c:/ni-rt/system/a.txt.

   •      data —

    data is the data to be stored.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      binary (F) —

    binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in which
    the VI transfers data in ASCII mode.

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file error —

      file error lists any file-related errors, such as invalid remote path or file access permission
    denied.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FTPFTP PutPut FileFile

Connects to an FTP server and copies the contents of a single file from the local
machine.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


                                                    © National Instruments 5321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5322 ordinal=5322 -->
## Functions

Functions


      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •      remote path —

           remote path is a path to a file on the FTP server. The remote path input supports Windows-like
                 file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-rt/
          system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input supports
            paths such as /c:/ni-rt/system/a.txt.

               •       local path —

             local path is the path to the location where you store the local file. If you do not wire local path,
           a file dialog box prompts you for a location.


5322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5323 ordinal=5323 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      binary (F) —

    binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in which
    the VI transfers data in ASCII mode.

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file error —

      file error lists any file-related errors, such as invalid remote path or file access permission
    denied.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FTPFTP PutPut MultipleMultiple BuffersBuffers

Connects to an FTP server and stores the contents of multiple buffers.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


                                                    © National Instruments 5323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5324 ordinal=5324 -->
## Functions

Functions

      Inputs/Outputs

               •      remote port (21) —

           remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •        file specifications —

                file specifications contains the FTP configuration for file transfers.

                     •      remote path —

              remote path is a path to a file on the FTP server. The remote path input supports Windows-
                    like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
             rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
                supports paths such as /c:/ni-rt/system/a.txt.

                     •      binary —

                binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in
               which the VI transfers data in ASCII mode.


               •      data —

           data contains the contents of the files.


5324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5325 ordinal=5325 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file errors —

      file errors is an array of error clusters containing file-related errors, such as invalid remote path
    and file access permission denied.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FTPFTP PutPut MultipleMultiple FilesFiles

Connects to an FTP server and copies the contents of multiple files from the local
machine.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


Inputs/Outputs

   •      remote port (21) —

    remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.


                                                    © National Instruments 5325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5326 ordinal=5326 -->
## Functions

Functions

               •      password —

           password is the password that authenticates the username.

              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •        file specifications —

                file specifications contains the FTP configuration for file transfers.

                     •      remote path —

              remote path is a path to a file on the FTP server. The remote path input supports Windows-
                    like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
             rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
                supports paths such as /c:/ni-rt/system/a.txt.

                     •       local path —

                  local path is the path to the location where you store the local file. If you do not wire local
                 path, a file dialog box prompts you for a location.

                     •      binary —

                binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in
               which the VI transfers data in ASCII mode.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


5326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5327 ordinal=5327 -->
## Functions

Functions

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file errors —

      file errors is an array of error clusters containing file-related errors, such as invalid remote path
    and file access permission denied.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FTPFTP PutPut MultipleMultiple FilesFiles andand BuffersBuffers

Connects to an FTP server and copies the contents of multiple files or buffers from the
local machine.

(NI Linux Real-Time) The FTP server is disabled by default, and you cannot use it in
safe mode. National Instruments recommends using WebDAV as the file transfer
mechanism for improved security.


Inputs/Outputs

   •      remote port (21) —

    remote port is the TCP/IP port at which the server listens. The default is 21, the FTP control port.

   •      password —

    password is the password that authenticates the username.


                                                    © National Instruments 5327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5328 ordinal=5328 -->
## Functions

Functions


              (NI Linux Real-Time) You must specify a blank password. For NI Linux Real-Time targets, the FTP
             server does not accept NI-Auth credentials.

               •      user —

            user is the name you want to use to log on to the FTP server.

          The default is anonymous. (NI Linux Real-Time) You must specify anonymous as the value for
              this input. For NI Linux Real-Time targets, the FTP server does not accept NI-Auth credentials.

               •      host —

            host is the name or IP address of an FTP server.

               •        file specifications —

                file specifications contains the FTP configuration for file transfers.

                     •      remote path —

              remote path is a path to a file on the FTP server. The remote path input supports Windows-
                    like file paths such as c:\ni-rt\system\a.txt and UNIX-like file paths such as /ni-
             rt/system/a.txt. If you need to specify a drive letter on UNIX-like paths, the input
                supports paths such as /c:/ni-rt/system/a.txt.

                     •       local path —

                  local path is the path to the location where you store the local file. If you do not wire local
                 path, a file dialog box prompts you for a location.

                     •      binary —

                binary specifies whether to transfer data in binary or ASCII mode. The default is FALSE, in
               which the VI transfers data in ASCII mode.

                     •      data —

               data is a string that contains the data you want to transfer.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


5328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5329 ordinal=5329 -->
## Functions

Functions


    standard error in functionality.

   •       active (T) —

    active specifies whether the data connection is active or passive. The default is TRUE, which
     specifies an active connection.

   •        file errors —

      file errors is an array of error clusters containing file-related errors, such as invalid remote path
    and file access permission denied.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WebDAVWebDAV

Use the WebDAV VIs to transfer files securely to and from a WebDAV server. Web
Distributing Authoring and Versioning (WebDAV) allows you to store, edit, and manage
documents and files on a web server or web share.

The WebDAV palette includes the more advanced WebDAV Synchronous and WebDAV
Asynchronous subpalettes. You can use the VIs on these advanced subpalettes to
complete processes that the basic WebDAV VIs cannot, such as copying and deleting
files and obtaining directory and path information.

Although both the synchronous and asynchronous VIs allow you to complete similar
processes, asynchronous VIs allow you to run multiple requests in parallel. However,
asynchronous VIs may be more difficult to use. Consider using synchronous VIs if you
do not need to run multiple requests in parallel.


                                                    © National Instruments 5329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5330 ordinal=5330 -->
## Functions

Functions


         Palette                       Description
        Object

                       Returns a file or multiple files or the raw binary contents of a file or multiple files
        Simple Get    from a remote WebDAV server or target. You must manually select the polymorphic
                        instance you want to use.


                     Uploads a file or multiple files to a remote WebDAV server or target. You must
        Simple Put                      manually select the polymorphic instance you want to use.


       WebDAV      Use the WebDAV Synchronous VIs to securely manage files on and transfer files to
        Synchronous  and from a target using a synchronous interface.


       WebDAV      Use the WebDAV Asynchronous VIs to securely manage files on and transfer files to
        Asynchronous and from a target using an asynchronous interface.


      SimpleSimple GetGet

       Returns a file or multiple files or the raw binary contents of a file or multiple files from
      a remote WebDAV server or target. You must manually select the polymorphic instance
      you want to use.

       This VI closes the connection to the WebDAV server after LabVIEW downloads the file
       or files. If you have many files to download or multiple file operations to complete,
       consider using the Open Session VI and the Get VI or the Asynchronous Get VI.


            • Simple Get Buffer VI
            • Simple Get File VI
            • Simple Get Multiple Buffers VI
            • Simple Get Multiple Files VI


5330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5331 ordinal=5331 -->
## Functions

Functions

SimpleSimple GetGet BufferBuffer VIVI

Returns a file or multiple files or the raw binary contents of a file or multiple files from
a remote WebDAV server or target. You must manually select the polymorphic instance
you want to use.

This VI closes the connection to the WebDAV server after LabVIEW downloads the file
or files. If you have many files to download or multiple file operations to complete,
consider using the Open Session VI and the Get VI or the Asynchronous Get VI.


Inputs/Outputs

   •      password —

    password is the password for the WebDAV server, if required. For example, when connecting to a
     real-time target, use the same password as when connecting with NI Web-based Configuration &
    Monitoring.

   •     username —

    username is the username with which to access the WebDAV server, if required. For example,
   when connecting to a real-time target, use the same username as when connecting with NI Web-
    based Configuration & Monitoring.

   •      remote file uri —

    remote file uri specifies the full uniform resource indicator (URI) of the file on the host or the
     target running the WebDAV server. A URI can be a uniform resource locator (URL), a uniform
    resource name (URN), or both. remote file uri also specifies the port and whether to use
    Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL). Format remote
      file uri as
   http[s]://hostname[:port][/files][/directory/subdirectory]/filename. Use
   https to connect using TLS/SSL, which provides added security. Use http to specify a non-
    TLS/SSL connection. If you do not specify a port number, the default is to use 80 for non-TLS/SSL
    and 443 for TLS/SSL.


                                                    © National Instruments 5331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5332 ordinal=5332 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data returns the contents of the file in raw binary data format.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SimpleSimple GetGet FileFile VIVI

       Returns a file or multiple files or the raw binary contents of a file or multiple files from
      a remote WebDAV server or target. You must manually select the polymorphic instance
      you want to use.

       This VI closes the connection to the WebDAV server after LabVIEW downloads the file
       or files. If you have many files to download or multiple file operations to complete,
       consider using the Open Session VI and the Get VI or the Asynchronous Get VI.


      Inputs/Outputs

               •      password —

           password is the password for the WebDAV server, if required. For example, when connecting to a
             real-time target, use the same password as when connecting with NI Web-based Configuration &
             Monitoring.

               •     username —


5332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5333 ordinal=5333 -->
## Functions

Functions


    username is the username with which to access the WebDAV server, if required. For example,
   when connecting to a real-time target, use the same username as when connecting with NI Web-
    based Configuration & Monitoring.

   •      remote file uri —

    remote file uri specifies the full uniform resource indicator (URI) of the file on the host or the
     target running the WebDAV server. A URI can be a uniform resource locator (URL), a uniform
    resource name (URN), or both. remote file uri also specifies the port and whether to use
    Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL). Format remote
      file uri as
   http[s]://hostname[:port][/files][/directory/subdirectory]/filename. Use
   https to connect using TLS/SSL, which provides added security. Use http to specify a non-
    TLS/SSL connection. If you do not specify a port number, the default is to use 80 for non-TLS/SSL
    and 443 for TLS/SSL.

   •       local file path —

     local file path specifies the local path to the directory where you want to save the file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       local file path out —

     local file path out returns the local path to which LabVIEW saves the file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SimpleSimple GetGet MultipleMultiple BuffersBuffers VIVI

Returns a file or multiple files or the raw binary contents of a file or multiple files from
a remote WebDAV server or target. You must manually select the polymorphic instance
you want to use.

This VI closes the connection to the WebDAV server after LabVIEW downloads the file

                                                    © National Instruments 5333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5334 ordinal=5334 -->
## Functions

Functions

       or files. If you have many files to download or multiple file operations to complete,
       consider using the Open Session VI and the Get VI or the Asynchronous Get VI.


      Inputs/Outputs

               •      password —

           password is the password for the WebDAV server, if required. For example, when connecting to a
             real-time target, use the same password as when connecting with NI Web-based Configuration &
             Monitoring.

               •     username —

          username is the username with which to access the WebDAV server, if required. For example,
          when connecting to a real-time target, use the same username as when connecting with NI Web-
           based Configuration & Monitoring.

               •      host uri —

            host uri specifies the host name or IP address of the host or target running the WebDAV server. A
           uniform resource identifier (URI) can be a uniform resource locator (URL), a uniform resource
         name (URN), or both. host uri also specifies the port and whether to use TLS/SSL. Format host
              uri as http[s]://hostname[:port]/. Use https to connect using Transport Layer
             Security (TLS), formerly known as Secure Sockets Layer (SSL), which provides added security.
           Use http to specify a non-TLS/SSL connection. If you do not specify a port number, the default
                is to use 80 for non-TLS/SSL and 443 for TLS/SSL.

               •       relative remote file uris —

             relative remote file uris is an array of URI fragments that follow the host portion of the full file
             URIs. For example, format each URI fragment as directory/subdirectory/filename.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

5334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5335 ordinal=5335 -->
## Functions

Functions


    data returns an array of strings where each element contains the raw binary contents of the files
    requested by the corresponding element in file uris.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SimpleSimple GetGet MultipleMultiple FilesFiles VIVI

Returns a file or multiple files or the raw binary contents of a file or multiple files from
a remote WebDAV server or target. You must manually select the polymorphic instance
you want to use.

This VI closes the connection to the WebDAV server after LabVIEW downloads the file
or files. If you have many files to download or multiple file operations to complete,
consider using the Open Session VI and the Get VI or the Asynchronous Get VI.


Inputs/Outputs

   •      password —

    password is the password for the WebDAV server, if required. For example, when connecting to a
     real-time target, use the same password as when connecting with NI Web-based Configuration &
    Monitoring.

   •     username —

    username is the username with which to access the WebDAV server, if required. For example,
   when connecting to a real-time target, use the same username as when connecting with NI Web-
    based Configuration & Monitoring.

   •      host uri —


                                                    © National Instruments 5335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5336 ordinal=5336 -->
## Functions

Functions


            host uri specifies the host name or IP address of the host or target running the WebDAV server. A
           uniform resource identifier (URI) can be a uniform resource locator (URL), a uniform resource
         name (URN), or both. host uri also specifies the port and whether to use TLS/SSL. Format host
              uri as http[s]://hostname[:port]/. Use https to connect using Transport Layer
             Security (TLS), formerly known as Secure Sockets Layer (SSL), which provides added security.
           Use http to specify a non-TLS/SSL connection. If you do not specify a port number, the default
                is to use 80 for non-TLS/SSL and 443 for TLS/SSL.

               •        file specifications —

                file specifications specifies the URIs of the files on the WebDAV server and local path(s) to the
             directory or directories in which you want to save the files.

                     •       relative remote file uri —

                      file uri specifies the URI fragment that follows the host portion of the full URI of the file. For
               example, format file uri as directory/subdirectory/filename.

                     •       local file path —

                  local file path specifies the local path to the directory where you want to save the file.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      SimpleSimple PutPut

      Uploads a file or multiple files to a remote WebDAV server or target. You must manually
        select the polymorphic instance you want to use.

       This VI closes the connection to the WebDAV server after LabVIEW uploads the file or
         files. If you have many files to upload or multiple file operations to complete, consider
       using the Open Session VI and the Put VI or the Asynchronous Put VI.


5336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5337 ordinal=5337 -->
## Functions

Functions


  • Simple Put Buffer VI
  • Simple Put File VI
  • Simple Put Multiple Buffers VI
  • Simple Put Multiple Files VI
SimpleSimple PutPut BufferBuffer VIVI

Uploads a file or multiple files to a remote WebDAV server or target. You must manually
select the polymorphic instance you want to use.

This VI closes the connection to the WebDAV server after LabVIEW uploads the file or
files. If you have many files to upload or multiple file operations to complete, consider
using the Open Session VI and the Put VI or the Asynchronous Put VI.


Inputs/Outputs

   •      password —

    password is the password for the WebDAV server, if required. For example, when connecting to a
     real-time target, use the same password as when connecting with NI Web-based Configuration &
    Monitoring.

   •     username —

    username is the username with which to access the WebDAV server, if required. For example,
   when connecting to a real-time target, use the same username as when connecting with NI Web-
    based Configuration & Monitoring.

   •      remote file uri —


                                                    © National Instruments 5337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5338 ordinal=5338 -->
## Functions

Functions


           remote file uri specifies the full uniform resource indicator (URI) of the file on the host or the
             target running the WebDAV server. A URI can be a uniform resource locator (URL), a uniform
            resource name (URN), or both. remote file uri also specifies the port and whether to use
            Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL). Format remote
                file uri as
          http[s]://hostname[:port][/files][/directory/subdirectory]/filename. Use
         https to connect using TLS/SSL, which provides added security. Use http to specify a non-
           TLS/SSL connection. If you do not specify a port number, the default is to use 80 for non-TLS/SSL
          and 443 for TLS/SSL.

               •      data —

           data specifies the contents of the file in raw binary data format.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SimpleSimple PutPut FileFile VIVI

      Uploads a file or multiple files to a remote WebDAV server or target. You must manually
        select the polymorphic instance you want to use.

       This VI closes the connection to the WebDAV server after LabVIEW uploads the file or
         files. If you have many files to upload or multiple file operations to complete, consider
       using the Open Session VI and the Put VI or the Asynchronous Put VI.


5338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5339 ordinal=5339 -->
## Functions

Functions

Inputs/Outputs

   •      password —

    password is the password for the WebDAV server, if required. For example, when connecting to a
     real-time target, use the same password as when connecting with NI Web-based Configuration &
    Monitoring.

   •     username —

    username is the username with which to access the WebDAV server, if required. For example,
   when connecting to a real-time target, use the same username as when connecting with NI Web-
    based Configuration & Monitoring.

   •        file uri —

      file uri specifies the full uniform resource indicator (URI) of the file on the host or the target
    running the WebDAV server. A URI can be a uniform resource locator (URL), a uniform resource
   name (URN), or both. file uri also specifies the port and whether to use TLS/SSL. Format file uri
    as http[s]://hostname[:port]/directory/subdirectory/filename. Use https to
    connect using Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL),
    which provides added security. Use http to specify a non-TLS/SSL connection. If you do not
     specify a port number, the default is to use 80 for non-TLS/SSL and 443 for TLS/SSL.

   •       local file path —

     local file path is the local path to the file you want to upload.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       local file path out —

     local file path out returns the local path to the directory where the file you upload is located.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5340 ordinal=5340 -->
## Functions

Functions

   SimpleSimple PutPut MultipleMultiple BuffersBuffers VIVI

      Uploads a file or multiple files to a remote WebDAV server or target. You must manually
        select the polymorphic instance you want to use.

       This VI closes the connection to the WebDAV server after LabVIEW uploads the file or
         files. If you have many files to upload or multiple file operations to complete, consider
       using the Open Session VI and the Put VI or the Asynchronous Put VI.


      Inputs/Outputs

               •      password —

           password is the password for the WebDAV server, if required. For example, when connecting to a
             real-time target, use the same password as when connecting with NI Web-based Configuration &
             Monitoring.

               •     username —

          username is the username with which to access the WebDAV server, if required. For example,
          when connecting to a real-time target, use the same username as when connecting with NI Web-
           based Configuration & Monitoring.

               •      host uri —

            host uri specifies the host name or IP address of the host or target running the WebDAV server. A
           uniform resource identifier (URI) can be a uniform resource locator (URL), a uniform resource
         name (URN), or both. host uri also specifies the port and whether to use TLS/SSL. Format host
              uri as http[s]://hostname[:port]/. Use https to connect using Transport Layer
             Security (TLS), formerly known as Secure Sockets Layer (SSL), which provides added security.
           Use http to specify a non-TLS/SSL connection. If you do not specify a port number, the default
                is to use 80 for non-TLS/SSL and 443 for TLS/SSL.

               •        file data specifications —


5340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5341 ordinal=5341 -->
## Functions

Functions


      file data specifications specifies the file URI and the data you want to upload.

         •       relative remote file uri —

           file uri specifies the URI fragment that follows the host portion of the full URI of the file. For
        example, format file uri as directory/subdirectory/filename.

         •      data —

        data specifies the contents of the file in raw binary data format.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SimpleSimple PutPut MultipleMultiple FilesFiles VIVI

Uploads a file or multiple files to a remote WebDAV server or target. You must manually
select the polymorphic instance you want to use.

This VI closes the connection to the WebDAV server after LabVIEW uploads the file or
files. If you have many files to upload or multiple file operations to complete, consider
using the Open Session VI and the Put VI or the Asynchronous Put VI.


Inputs/Outputs

   •      password —

                                                    © National Instruments 5341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5342 ordinal=5342 -->
## Functions

Functions


           password is the password for the WebDAV server, if required. For example, when connecting to a
             real-time target, use the same password as when connecting with NI Web-based Configuration &
             Monitoring.

               •     username —

          username is the username with which to access the WebDAV server, if required. For example,
          when connecting to a real-time target, use the same username as when connecting with NI Web-
           based Configuration & Monitoring.

               •      host uri —

            host uri specifies the host name or IP address of the host or target running the WebDAV server. A
           uniform resource identifier (URI) can be a uniform resource locator (URL), a uniform resource
         name (URN), or both. host uri also specifies the port and whether to use TLS/SSL. Format host
              uri as http[s]://hostname[:port]/. Use https to connect using Transport Layer
             Security (TLS), formerly known as Secure Sockets Layer (SSL), which provides added security.
           Use http to specify a non-TLS/SSL connection. If you do not specify a port number, the default
                is to use 80 for non-TLS/SSL and 443 for TLS/SSL.

               •        file specifications —

                file specifications specifies the file URI and the local path to the directory where the files you
          want to upload are located.

                     •       relative remote file uri —

                      file uri specifies the URI fragment that follows the host portion of the full URI of the file. For
               example, format file uri as directory/subdirectory/filename.

                     •       local file path —

                  local file path is the local path to the file you want to upload.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5343 ordinal=5343 -->
## Functions

Functions

WebDAVWebDAV SynchronousSynchronous

Use the WebDAV Synchronous VIs to securely manage files on and transfer files to and
from a target using a synchronous interface.

Although both the synchronous and asynchronous VIs allow you to complete similar
processes, asynchronous VIs allow you to run multiple requests in parallel. However,
asynchronous VIs may be more difficult to use. Consider using synchronous VIs if you
do not need to run multiple requests in parallel.

Consider using asynchronous VIs to complete the following processes:

  • Dynamically start requests in parallel. For example, you can use a single
   Asynchronous Get VI in a loop to download any number of files in parallel.
    Initiating parallel requests using synchronous VIs would require you to use
    multiple Get VIs and to branch the session wire.
  • Process requests in response to a user interface event. The WebDAV user events
    allow you to maintain a responsive user interface while a request processes.
    Creating a similar application using synchronous VIs requires much more effort.
  • View the progress of an upload or download request. This ability is unique to
   asynchronous VIs.
  • Abort individual requests before LabVIEW completes them. Aborting a request
    using synchronous VIs would require you to close the session, but doing so aborts
     all requests.


 Palette
           Description
 Object

          Opens a WebDAV session and creates an associated session handle. After calling this VI,
 Open
          you can use the WebDAV session handle to perform other operations using the same
 Session
           connection. Use the Close Session VI to dispose of the session reference.


 Configure
           Provides Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL)
 SSL


                                                    © National Instruments 5343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5344 ordinal=5344 -->
## Functions

Functions


         Palette                   Description
        Object

                    authentication for requests associated with the session handle. Use TLS/SSL
                    authentication with other WebDAV VIs to send requests to a server, Web page, or Web
                     service using TLS/SSL. Use this VI to verify the identity of the server against a list of
                    trusted certificate authority (CA) certificates and provide client authentication, if
                   required by the server. Session handles save the TLS/SSL credentials across multiple
              Web requests.


         Close      Closes a WebDAV session created by an Open Session VI. LabVIEW aborts any requests
         Session     still running when this VI executes.


                   Returns a file or the raw binary contents of a file from a remote WebDAV server or target.
        Get       You must manually select the polymorphic instance you want to use. This VI times out if
                              it exceeds the timeout value of the session that you set in the Open Session VI.


                  Uploads a file to a remote WebDAV server or target. You must manually select the
        Put       polymorphic instance you want to use. This VI times out if it exceeds the timeout value
                     of the session that you set in the Open Session VI.


         Create     Creates the specified directory on the remote WebDAV server. The full path to the parent
         Directory  directory must already exist. Otherwise, this VI returns an error.


         Directory
                   Returns a list of all directories and files within the directory you specify in relative uri.
          Listing


        Path Info  Returns information about a single file or directory on a remote WebDAV server.


                  Copies a file or directory from one location on a WebDAV server to another location on
       Copy      that WebDAV server. This VI times out if it exceeds the timeout value of the session that
                 you set in the Open Session VI.


5344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5345 ordinal=5345 -->
## Functions

Functions


 Palette           Description
 Object

          Moves a file or directory from a location on a WebDAV server to another location on that Move             server.


 Delete     Deletes a file or directory on a WebDAV server.

OpenOpen SessionSession

Opens a WebDAV session and creates an associated session handle. After calling this VI,
you can use the WebDAV session handle to perform other operations using the same
connection. Use the Close Session VI to dispose of the session reference.


Inputs/Outputs

   •      password —

    password is the password for the WebDAV server, if required. For example, when connecting to a
     real-time target, use the same password as when connecting with NI Web-based Configuration &
    Monitoring.

   •     username —

    username is the username with which to access the WebDAV server, if required. For example,
   when connecting to a real-time target, use the same username as when connecting with NI Web-
    based Configuration & Monitoring.

   •      host uri prefix —


                                                    © National Instruments 5345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5346 ordinal=5346 -->
## Functions

Functions


            host uri prefix specifies the root uniform resource indicator (URI) and an optional prefix for all
              relative URIs of the file(s) on the host or the target running the WebDAV server. A URI can be a
           uniform resource locator (URL), a uniform resource name (URN), or both. host uri prefix also
              specifies the port and whether to use TLS/SSL.

           Format host uri prefix as http[s]://hostname[:port][/files]. Use https to connect
            using Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL), which
            provides added security. Use http to specify a non-TLS/SSL connection. If you do not specify a
            port number, the default is to use 80 for non-TLS/SSL and 443 for TLS/SSL. On LabVIEW Real-
          Time targets, you must specify /files as the prefix.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout ms (60000) —

           timeout ms specifies the time, in milliseconds, that the VI waits when another VI makes a
            request on the same session handle before it returns an error. This timeout value applies to any
              VI that uses the session. The default is 60,000 ms, or 1 minute. A value of –1 indicates to wait
              indefinitely.

               •       verify server? (true) —

             verify server? specifies whether to check the certificate of the server against the list of trusted
          CA certificates specified by CA certificate file. If you do not specify a list of trusted CA certificates,
           LabVIEW checks the server's certificate against a default list of trusted CA certificates.

                    If TRUE, the VI verifies the identity of the server using the list of trusted CA certificates for
            optimal security. If FALSE, the VI does not verify the identity of the server and does not provide
            optimal security. However, this allows the client to accept self-signed certificates signed by the
               certificate creator rather than a trusted CA. The default is TRUE.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5347 ordinal=5347 -->
## Functions

Functions

ConfigureConfigure SSLSSL

Provides Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL)
authentication for requests associated with the session handle. Use TLS/SSL
authentication with other WebDAV VIs to send requests to a server, Web page, or Web
service using TLS/SSL. Use this VI to verify the identity of the server against a list of
trusted certificate authority (CA) certificates and provide client authentication, if
required by the server. Session handles save the TLS/SSL credentials across multiple
Web requests.


Inputs/Outputs

   •       private key password —

    private key password specifies a password for the private key file. If the private key file is not
    encrypted, you do not have to specify a private key password.

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •     CA certificate file —

   CA certificate file specifies the path to a list of trusted certificate authority (CA) certificates. If
     verify server? is TRUE, the client verifies the identity of the server against this list of trusted
     certificates.

   •       client certificate file —

     client certificate file specifies the path to the client certificate file for servers that require client
    authentication. Some servers require this file to verify the identity of the client by using a trusted
    CA.

   •       private key file —

                                                    © National Instruments 5347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5348 ordinal=5348 -->
## Functions

Functions


             private key file specifies the path to a private key file that is part of the client certificate and
              client authentication process.

                    If the server requires client authentication, you must specify a client certificate file and a private
           key file. If you need to transfer this file between client systems, especially over a network, you
           can assign a password when you create the private key file. To use password-protected private
           key files with this VI, assign the password to the private key password input.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       verify server? (true) —

             verify server? specifies whether to check the certificate of the server against the list of trusted
          CA certificates specified by CA certificate file. If you do not specify a list of trusted CA certificates,
           LabVIEW checks the server's certificate against a default list of trusted CA certificates.

                    If TRUE, the VI verifies the identity of the server using the list of trusted CA certificates for
            optimal security. If FALSE, the VI does not verify the identity of the server and does not provide
            optimal security. However, this allows the client to accept self-signed certificates signed by the
               certificate creator rather than a trusted CA. The default is TRUE.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   CloseClose SessionSession

       Closes a WebDAV session created by an Open Session VI. LabVIEW aborts any requests
          still running when this VI executes.


5348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5349 ordinal=5349 -->
## Functions

Functions

Inputs/Outputs

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet

Returns a file or the raw binary contents of a file from a remote WebDAV server or
target. You must manually select the polymorphic instance you want to use. This VI
times out if it exceeds the timeout value of the session that you set in the Open Session
VI.


  • Get Buffer VI
  • Get File VI
GetGet BufferBuffer VIVI

Returns a file or the raw binary contents of a file from a remote WebDAV server or
target. You must manually select the polymorphic instance you want to use. This VI
times out if it exceeds the timeout value of the session that you set in the Open Session
VI.


                                                    © National Instruments 5349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5350 ordinal=5350 -->
## Functions

Functions


      Inputs/Outputs

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      data —

           data returns the contents of the file in raw binary data format.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   GetGet FileFile VIVI

       Returns a file or the raw binary contents of a file from a remote WebDAV server or
        target. You must manually select the polymorphic instance you want to use. This VI
       times out if it exceeds the timeout value of the session that you set in the Open Session
         VI.


5350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5351 ordinal=5351 -->
## Functions

Functions

      Note This instance returns the file you specify in remote file uri.


Inputs/Outputs

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative uri —

     relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
    host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
    (URL), a uniform resource name (URN), or both. Format relative uri as
    directory/subdirectory/filename.

   •       local file path —

     local file path specifies the local path to the directory where you want to save the file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •       local file path out —

     local file path out returns the local path to which LabVIEW saves the file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5352 ordinal=5352 -->
## Functions

Functions

   PutPut

      Uploads a file to a remote WebDAV server or target. You must manually select the
      polymorphic instance you want to use. This VI times out if it exceeds the timeout value
       of the session that you set in the Open Session VI.


            • Put Buffer VI
            • Put File VI
   PutPut BufferBuffer VIVI

      Uploads a file to a remote WebDAV server or target. You must manually select the
      polymorphic instance you want to use. This VI times out if it exceeds the timeout value
       of the session that you set in the Open Session VI.


      Inputs/Outputs

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •      data —


5352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5353 ordinal=5353 -->
## Functions

Functions


    data specifies the contents of the file in raw binary data format.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

PutPut FileFile VIVI

Uploads a file to a remote WebDAV server or target. You must manually select the
polymorphic instance you want to use. This VI times out if it exceeds the timeout value
of the session that you set in the Open Session VI.

      Note This instance uploads the file you specify in local file path to the
      WebDAV server.


Inputs/Outputs

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative uri —


                                                    © National Instruments 5353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5354 ordinal=5354 -->
## Functions

Functions


             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       local file path —

             local file path is the local path to the file you want to upload.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •       local file path out —

             local file path out returns the local path to the directory where the file you upload is located.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    CreateCreate DirectoryDirectory

       Creates the specified directory on the remote WebDAV server. The full path to the
       parent directory must already exist. Otherwise, this VI returns an error.


      Inputs/Outputs

               •      session handle —


5354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5355 ordinal=5355 -->
## Functions

Functions


    session handle specifies the unique reference to the WebDAV session.

   •       relative uri —

     relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
    host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
    (URL), a uniform resource name (URN), or both. Format relative uri as
    directory/subdirectory/filename.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DirectoryDirectory ListingListing

Returns a list of all directories and files within the directory you specify in relative uri.


Inputs/Outputs

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative uri —


                                                    © National Instruments 5355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5356 ordinal=5356 -->
## Functions

Functions


             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •       directory list —

             directory list returns an array of clusters where each element contains the following information
           about the specified directory or a subdirectory within the specified directory.

                     •      type —

               type returns the Multipurpose Internet Mail Extension (MIME) type of the file or directory.
               type may return an empty value if the server does not specify a MIME type.

                     •       size —

                  size returns the size, in bytes, of the file. For directories, size returns a value of 0.

                     •       last modification —

                   last modification returns the time and date of the last time the file or directory was
                 modified.

                     •      display name —

                 display name returns the name of the file or directory on the server.

                     •       uri —

                   uri specifies the absolute uniform resource identifier (URI) of the file or directory. A URI can
              be a uniform resource locator (URL), a uniform resource name (URN), or both.


5356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5357 ordinal=5357 -->
## Functions

Functions


       The server may return either a relative or absolute URI.


   •        file list —

      file list returns an array of all files within the specified directory.

         •      type —

        type returns the Multipurpose Internet Mail Extension (MIME) type of the file or directory.
        type may return an empty value if the server does not specify a MIME type.

         •       size —

         size returns the size, in bytes, of the file. For directories, size returns a value of 0.

         •       last modification —

          last modification returns the time and date of the last time the file or directory was
         modified.

         •      display name —

         display name returns the name of the file or directory on the server.

         •       uri —

          uri specifies the absolute uniform resource identifier (URI) of the file or directory. A URI can
       be a uniform resource locator (URL), a uniform resource name (URN), or both.

       The server may return either a relative or absolute URI.


   •       error out —

    error out contains error information. This output provides standard error out functionality.

PathPath InfoInfo

Returns information about a single file or directory on a remote WebDAV server.

                                                    © National Instruments 5357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5358 ordinal=5358 -->
## Functions

Functions


      Inputs/Outputs

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      path info —

           path info returns a cluster containing information about the file or directory you specify.

                     •      type —

               type returns the Multipurpose Internet Mail Extension (MIME) type of the file or directory.
               type may return an empty value if the server does not specify a MIME type.

                     •       size —

                  size returns the size, in bytes, of the file. For directories, size returns a value of 0.

                     •       last modification —


5358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5359 ordinal=5359 -->
## Functions

Functions


          last modification returns the time and date of the last time the file or directory was
         modified.

         •      display name —

         display name returns the name of the file or directory on the server.

         •       uri —

          uri specifies the absolute uniform resource identifier (URI) of the file or directory. A URI can
       be a uniform resource locator (URL), a uniform resource name (URN), or both.

       The server may return either a relative or absolute URI.


   •        is directory? —

      is directory? returns TRUE if path uri is the path to a directory.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CopyCopy

Copies a file or directory from one location on a WebDAV server to another location on
that WebDAV server. This VI times out if it exceeds the timeout value of the session that
you set in the Open Session VI.


Inputs/Outputs

   •      session handle —


                                                    © National Instruments 5359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5360 ordinal=5360 -->
## Functions

Functions


            session handle specifies the unique reference to the WebDAV session.

               •       relative source uri —

             relative source uri specifies the location of the source file or directory. The location can be a file
            or directory of any depth.

               •       relative destination uri —

             relative destination uri specifies the new name and the location where you want to save the file
            or directory. The directory you specify must already exist. Otherwise, the operation fails.

               •      overwrite? (T) —

            overwrite? (T) specifies whether to replace any existing files with source files of the same name.
                    If TRUE, LabVIEW overwrites any existing files that conflict with source files. If FALSE, LabVIEW
             returns an error code if any existing files conflict with source files.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   MoveMove

      Moves a file or directory from a location on a WebDAV server to another location on
       that server.


5360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5361 ordinal=5361 -->
## Functions

Functions


Inputs/Outputs

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative source uri —

     relative source uri specifies the location of the source file or directory. The location can be a file
    or directory of any depth.

   •       relative destination uri —

     relative destination uri specifies the new name and the location where you want to save the file
    or directory. The directory you specify must already exist. Otherwise, the operation fails.

   •      overwrite? (T) —

    overwrite? (T) specifies whether to replace any existing files with source files of the same name.
       If TRUE, LabVIEW overwrites any existing files that conflict with source files. If FALSE, LabVIEW
    returns an error code if any existing files conflict with source files.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5362 ordinal=5362 -->
## Functions

Functions

    DeleteDelete

       Deletes a file or directory on a WebDAV server.


      Inputs/Outputs

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     WebDAVWebDAV AsynchronousAsynchronous

      Use the WebDAV Asynchronous VIs to securely manage files on and transfer files to and
      from a target using an asynchronous interface.

      Although both the synchronous and asynchronous VIs allow you to complete similar

5362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5363 ordinal=5363 -->
## Functions

Functions

processes, asynchronous VIs allow you to run multiple requests in parallel. However,
asynchronous VIs may be more difficult to use. Consider using synchronous VIs if you
do not need to run multiple requests in parallel.

Consider using asynchronous VIs to complete the following processes:

  • Dynamically start requests in parallel. For example, you can use a single
   Asynchronous Get VI in a loop to download any number of files in parallel.
    Initiating parallel requests using synchronous VIs would require you to use
    multiple Get VIs and to branch the session wire.
  • Process requests in response to a user interface event. The WebDAV user events
    allow you to maintain a responsive user interface while a request processes.
    Creating a similar application using synchronous VIs requires much more effort.
  • View the progress of an upload or download request. This ability is unique to
   asynchronous VIs.
  • Abort individual requests before LabVIEW completes them. Aborting a request
    using synchronous VIs would require you to close the session, but doing so aborts
     all requests.


 Palette                Description Object

             Opens an asynchronous WebDAV session and creates an associated session handle.
 Asynchronous  This VI also returns event clusters that indicate request progress and completion.
 Open Session  After calling this VI, you can use the WebDAV session handle to perform other
               operations using the same connection.


               Provides Transport Layer Security (TLS), formerly known as Secure Sockets Layer
                (SSL) authentication for asynchronous requests associated with the session handle.
             Use TLS/SSL authentication with other WebDAV VIs to send requests to a server,
 Asynchronous
           Web page, or Web service using TLS/SSL. Use this VI to verify the identity of the
 Configure SSL
                server against a list of trusted certificate authority (CA) certificates, and provide
                  client authentication, if required by the server. Session handles save the TLS/SSL
                credentials across multiple Web requests. The request this VI generates can run in


                                                    © National Instruments 5363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5364 ordinal=5364 -->
## Functions

Functions


         Palette                       Description
        Object

                           parallel with other asynchronous WebDAV requests.


        Asynchronous Returns an event registration reference that is identical to the event registration
         Create Event   reference the Asynchronous Open Session VI generates. This VI allows you to send
         Registration   events from the same WebDAV session handle to multiple Event structures.


        Asynchronous  Closes an asynchronous WebDAV session created by an Asynchronous Open
         Close Session  Session VI. LabVIEW aborts any requests still running when this VI executes.


                       Returns a file or directory from a remote WebDAV server or target. You must
                      manually select the polymorphic instance you want to use. The request this VI        Asynchronous                       generates can run in parallel with other asynchronous WebDAV requests. This VI        Get
                       times out if it exceeds the timeout value of the session that you set in the
                     Asynchronous Open Session VI.


                     Uploads a file or raw binary contents of a file to a remote WebDAV server or target.
                     You must manually select the polymorphic instance you want to use. The request        Asynchronous
                           this VI generates can run in parallel with other asynchronous WebDAV requests. This        Put                           VI times out if it exceeds the timeout value of the session that you set in the
                     Asynchronous Open Session VI.


                      Copies a file or directory from one location on a WebDAV server to another location
        Asynchronous on that WebDAV server. The request this VI generates can run in parallel with other
       Copy         asynchronous WebDAV requests. This VI times out if it exceeds the timeout value of
                       the session that you set in the Asynchronous Open Session VI.


                    Moves a file or directory from a location on a WebDAV server to another location on
        Asynchronous
                         that server. The request this VI generates can run in parallel with other
       Move
                      asynchronous WebDAV requests.


5364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5365 ordinal=5365 -->
## Functions

Functions


 Palette                Description
 Object

 Asynchronous  Creates the specified directory on the remote WebDAV server. The full path to the
 Create         parent directory must already exist. Otherwise, this VI returns an error. The request
 Directory       this VI generates can run in parallel with other asynchronous WebDAV requests.


               Generates a list of all directories and files within the directory you specify in
 Asynchronous                 relative uri. You can view the list of directories and files in the List Directory Directory              Complete WebDAV event that this VI triggers. The request this VI generates can run Listing                  in parallel with other asynchronous WebDAV requests.


               Generates information about the file or directory you specify in relative uri. You can
 Asynchronous view the file or directory information in the Path Info Complete WebDAV event that
 Path Info       this VI triggers. The request this VI generates can run in parallel with other
              asynchronous WebDAV requests.


 Asynchronous  Deletes a file or directory on a WebDAV server. The request this VI generates can run
 Delete          in parallel with other asynchronous WebDAV requests.

 Asynchronous
 Request       Gets the current status of an asynchronous request.
 Status

 Asynchronous Cancels a working asynchronous WebDAV request. This VI triggers a Request
 Abort Request Complete WebDAV event that lists the status as aborted.


 Asynchronous
               Closes and disposes of a request handle. If the request is not complete, this VI
 Close Request
                aborts the request.
 Handle

AsynchronousAsynchronous OpenOpen SessionSession

Opens an asynchronous WebDAV session and creates an associated session handle.


                                                    © National Instruments 5365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5366 ordinal=5366 -->
## Functions

Functions

       This VI also returns event clusters that indicate request progress and completion. After
        calling this VI, you can use the WebDAV session handle to perform other operations
       using the same connection.

      You must use this VI to open a session before you can use other VIs on the WebDAV
      Asynchronous palette.

           Note The session handles that WebDAV Asynchronous VIs use are not
              compatible with WebDAV Synchronous VIs.


      Inputs/Outputs

               •      password —

           password is the password for the WebDAV server, if required. For example, when connecting to a
             real-time target, use the same password as when connecting with NI Web-based Configuration &
             Monitoring.

               •     username —

          username is the username with which to access the WebDAV server, if required. For example,
          when connecting to a real-time target, use the same username as when connecting with NI Web-
           based Configuration & Monitoring.

               •      host uri prefix —

            host uri prefix specifies the root uniform resource indicator (URI) and an optional prefix for all
              relative URIs of the file(s) on the host or the target running the WebDAV server. A URI can be a
           uniform resource locator (URL), a uniform resource name (URN), or both. host uri prefix also
              specifies the port and whether to use TLS/SSL.

           Format host uri prefix as http[s]://hostname[:port][/files]. Use https to connect
            using Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL), which


5366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5367 ordinal=5367 -->
## Functions

Functions


    provides added security. Use http to specify a non-TLS/SSL connection. If you do not specify a
    port number, the default is to use 80 for non-TLS/SSL and 443 for TLS/SSL. On LabVIEW Real-
    Time targets, you must specify /files as the prefix.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout ms (60000) —

    timeout ms specifies the time, in milliseconds, that the VI waits when another VI makes a
    request on the same session handle before it returns an error. This timeout value applies to any
     VI that uses the session. The default is 60,000 ms, or 1 minute. A value of –1 indicates to wait
     indefinitely.

   •       verify server? (true) —

     verify server? specifies whether to check the certificate of the server against the list of trusted
   CA certificates specified by CA certificate file. If you do not specify a list of trusted CA certificates,
    LabVIEW checks the server's certificate against a default list of trusted CA certificates.

       If TRUE, the VI verifies the identity of the server using the list of trusted CA certificates for
    optimal security. If FALSE, the VI does not verify the identity of the server and does not provide
    optimal security. However, this allows the client to accept self-signed certificates signed by the
     certificate creator rather than a trusted CA. The default is TRUE.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •      Request Events —

    Request Events returns an event registration reference that refers to a cluster of user events
     called WebDAV.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If you want to combine WebDAV events with your own user events, wire the Request
Events refnum and one or more other event registration refnums to the input


                                                    © National Instruments 5367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5368 ordinal=5368 -->
## Functions

Functions

       terminals of a Bundle function and wire the resulting cluster to the dynamic event
       terminal of an Event structure. To display the dynamic event terminal, right-click the
      Event structure and select Show Dynamic Event Terminals. Both the WebDAV and user
       event data items appear in the Event Data Node on the left border of the Event
        structure.

           Note Do not wire the same event registration reference to multiple Event
                structures. Otherwise, you create a race condition between the Event
                structures, and only one of the Event structures receives any given event.
                Instead, use the Asynchronous Create Event Registration VI to create
               additional event registration refnums that you can wire to additional Event
               structures on the same WebDAV session handle.
   AsynchronousAsynchronous ConfigureConfigure SSLSSL

       Provides Transport Layer Security (TLS), formerly known as Secure Sockets Layer (SSL)
       authentication for asynchronous requests associated with the session handle. Use
      TLS/SSL authentication with other WebDAV VIs to send requests to a server, Web page,
       or Web service using TLS/SSL. Use this VI to verify the identity of the server against a
          list of trusted certificate authority (CA) certificates, and provide client authentication, if
       required by the server. Session handles save the TLS/SSL credentials across multiple
     Web requests. The request this VI generates can run in parallel with other
      asynchronous WebDAV requests.

       This VI triggers a Request Complete WebDAV event.


      Inputs/Outputs

               •       private key password —


5368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5369 ordinal=5369 -->
## Functions

Functions


  private key password specifies a password for the private key file. If the private key file is not
  encrypted, you do not have to specify a private key password.

•      session handle —

  session handle specifies the unique reference to the WebDAV session.

•     CA certificate file —

  CA certificate file specifies the path to a list of trusted certificate authority (CA) certificates. If you
  specify TRUE for the verify server control, the client verifies the server's identity against this list
  of trusted certificates.

•       client certificate file —

  client certificate file specifies the path to the client certificate file for servers that require client
  authentication. Some servers require this file to verify the identity of the client by using a trusted
  CA.

•       private key file —

  private key file specifies the path to a private key file that is part of the client certificate and
  client authentication process.

   If the server requires client authentication, you must specify a client certificate file and a private
  key file. If you need to transfer this file between client systems, especially over a network, you
  can assign a password when you create the private key file. To use password-protected private
  key files with this VI, assign the password to the private key password input.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       verify server? (true) —

  verify server? specifies whether to check the certificate of the server against the list of trusted
  CA certificates specified by CA certificate file. If you do not specify a list of trusted CA certificates,
  LabVIEW checks the server's certificate against a default list of trusted CA certificates.

   If TRUE, the VI verifies the identity of the server using the list of trusted CA certificates for
  optimal security. If FALSE, the VI does not verify the identity of the server and does not provide
  optimal security. However, this allows the client to accept self-signed certificates signed by the


                                                   © National Instruments 5369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5370 ordinal=5370 -->
## Functions

Functions


               certificate creator rather than a trusted CA. The default is TRUE.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   AsynchronousAsynchronous CreateCreate EventEvent RegistrationRegistration

       Returns an event registration reference that is identical to the event registration
       reference the Asynchronous Open Session VI generates. This VI allows you to send
       events from the same WebDAV session handle to multiple Event structures.


      Inputs/Outputs

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      Request Events —

           Request Events returns an event registration reference that refers to a cluster of user events
             called WebDAV.


5370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5371 ordinal=5371 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AsynchronousAsynchronous CloseClose SessionSession

Closes an asynchronous WebDAV session created by an Asynchronous Open Session
VI. LabVIEW aborts any requests still running when this VI executes.


Inputs/Outputs

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AsynchronousAsynchronous GetGet

Returns a file or directory from a remote WebDAV server or target. You must manually
select the polymorphic instance you want to use. The request this VI generates can run
in parallel with other asynchronous WebDAV requests. This VI times out if it exceeds
the timeout value of the session that you set in the Asynchronous Open Session VI.


                                                    © National Instruments 5371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5372 ordinal=5372 -->
## Functions

Functions

      Both instances of this VI trigger a Request Progress WebDAV event.


            • Asynchronous Get Buffer VI
            • Asynchronous Get File VI
   AsynchronousAsynchronous GetGet BufferBuffer VIVI

       Returns a file or directory from a remote WebDAV server or target. You must manually
        select the polymorphic instance you want to use. The request this VI generates can run
        in parallel with other asynchronous WebDAV requests. This VI times out if it exceeds
       the timeout value of the session that you set in the Asynchronous Open Session VI.

      Both instances of this VI trigger a Request Progress WebDAV event.


      Inputs/Outputs

               •      user data —

            user data specifies any data you want to include with the request handle. LabVIEW passes this
            data along with the request handle, but the data does not affect the request. LabVIEW returns
            user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
            data within your VI.

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator


5372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5373 ordinal=5373 -->
## Functions

Functions


    (URL), a uniform resource name (URN), or both. Format relative uri as
    directory/subdirectory/filename.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •      request handle out —

    request handle out returns the unique reference to the WebDAV request. You can wire this
    output only to other asynchronous WebDAV VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AsynchronousAsynchronous GetGet FileFile VIVI

Returns a file or directory from a remote WebDAV server or target. You must manually
select the polymorphic instance you want to use. The request this VI generates can run
in parallel with other asynchronous WebDAV requests. This VI times out if it exceeds
the timeout value of the session that you set in the Asynchronous Open Session VI.

      Note

        This instance returns the file you specify in remote file uri.

        In addition to the Request Progress WebDAV event, this instance triggers a
       Request Complete WebDAV event.


                                                    © National Instruments 5373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5374 ordinal=5374 -->
## Functions

Functions


      Inputs/Outputs

               •      user data —

            user data specifies any data you want to include with the request handle. LabVIEW passes this
            data along with the request handle, but the data does not affect the request. LabVIEW returns
            user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
            data within your VI.

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       local file path —

             local file path specifies the local path to the directory where you want to save the file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      request handle out —

            request handle out returns the unique reference to the WebDAV request. You can wire this
           output only to other asynchronous WebDAV VIs.

               •       local file path out —


5374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5375 ordinal=5375 -->
## Functions

Functions


     local file path out returns the local path to which LabVIEW saves the file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AsynchronousAsynchronous PutPut

Uploads a file or raw binary contents of a file to a remote WebDAV server or target. You
must manually select the polymorphic instance you want to use. The request this VI
generates can run in parallel with other asynchronous WebDAV requests. This VI times
out if it exceeds the timeout value of the session that you set in the Asynchronous
Open Session VI.

Both instances of this VI trigger Request Progress and a Request Complete WebDAV
events.


  • Asynchronous Put Buffer VI
  • Asynchronous Put File VI
AsynchronousAsynchronous PutPut BufferBuffer VIVI

Uploads a file or raw binary contents of a file to a remote WebDAV server or target. You
must manually select the polymorphic instance you want to use. The request this VI
generates can run in parallel with other asynchronous WebDAV requests. This VI times
out if it exceeds the timeout value of the session that you set in the Asynchronous
Open Session VI.

Both instances of this VI trigger Request Progress and a Request Complete WebDAV
events.


                                                    © National Instruments 5375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5376 ordinal=5376 -->
## Functions

Functions


      Inputs/Outputs

               •      user data —

            user data specifies any data you want to include with the request handle. LabVIEW passes this
            data along with the request handle, but the data does not affect the request. LabVIEW returns
            user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
            data within your VI.

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •      data —

           data specifies the contents of the file in raw binary data format.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      request handle out —

            request handle out returns the unique reference to the WebDAV request. You can wire this
           output only to other asynchronous WebDAV VIs.

               •       error out —


5376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5377 ordinal=5377 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

AsynchronousAsynchronous PutPut FileFile VIVI

Uploads a file or raw binary contents of a file to a remote WebDAV server or target. You
must manually select the polymorphic instance you want to use. The request this VI
generates can run in parallel with other asynchronous WebDAV requests. This VI times
out if it exceeds the timeout value of the session that you set in the Asynchronous
Open Session VI.

      Note This instance uploads the file you specify in local file path to the
      WebDAV server.


Inputs/Outputs

   •      user data —

    user data specifies any data you want to include with the request handle. LabVIEW passes this
    data along with the request handle, but the data does not affect the request. LabVIEW returns
    user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
    data within your VI.

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative uri —

     relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
    host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
    (URL), a uniform resource name (URN), or both. Format relative uri as


                                                    © National Instruments 5377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5378 ordinal=5378 -->
## Functions

Functions


          directory/subdirectory/filename.

               •       local file path —

             local file path is the local path to the file you want to upload.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      request handle out —

            request handle out returns the unique reference to the WebDAV request. You can wire this
           output only to other asynchronous WebDAV VIs.

               •       local file path out —

             local file path out returns the local path to the directory where the file you upload is located.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   AsynchronousAsynchronous CopyCopy

      Copies a file or directory from one location on a WebDAV server to another location on
       that WebDAV server. The request this VI generates can run in parallel with other
      asynchronous WebDAV requests. This VI times out if it exceeds the timeout value of the
       session that you set in the Asynchronous Open Session VI.

       This VI triggers a Request Complete WebDAV event.


5378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5379 ordinal=5379 -->
## Functions

Functions


Inputs/Outputs

   •      user data —

    user data specifies any data you want to include with the request handle. LabVIEW passes this
    data along with the request handle, but the data does not affect the request. LabVIEW returns
    user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
    data within your VI.

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative source uri —

     relative source uri specifies the location of the source file or directory. The location can be a file
    or directory of any depth.

   •       relative destination uri —

     relative destination uri specifies the new name and the location where you want to save the file
    or directory. The directory you specify must already exist. Otherwise, the operation fails.

   •      overwrite? (T) —

    overwrite? (T) specifies whether to replace any existing files with source files of the same name.
       If TRUE, LabVIEW overwrites any existing files that conflict with source files. If FALSE, LabVIEW
    returns an error code if any existing files conflict with source files.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •      request handle out —

                                                    © National Instruments 5379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5380 ordinal=5380 -->
## Functions

Functions


            request handle out returns the unique reference to the WebDAV request. You can wire this
           output only to other asynchronous WebDAV VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   AsynchronousAsynchronous MoveMove

      Moves a file or directory from a location on a WebDAV server to another location on
       that server. The request this VI generates can run in parallel with other asynchronous
     WebDAV requests.

       This VI triggers a Request Complete WebDAV event.


      Inputs/Outputs

               •      user data —

            user data specifies any data you want to include with the request handle. LabVIEW passes this
            data along with the request handle, but the data does not affect the request. LabVIEW returns
            user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
            data within your VI.

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative source uri —

             relative source uri specifies the location of the source file or directory. The location can be a file
            or directory of any depth.


5380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5381 ordinal=5381 -->
## Functions

Functions

   •       relative destination uri —

     relative destination uri specifies the new name and the location where you want to save the file
    or directory. The directory you specify must already exist. Otherwise, the operation fails.

   •      overwrite? (T) —

    overwrite? (T) specifies whether to replace any existing files with source files of the same name.
       If TRUE, LabVIEW overwrites any existing files that conflict with source files. If FALSE, LabVIEW
    returns an error code if any existing files conflict with source files.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •      request handle out —

    request handle out returns the unique reference to the WebDAV request. You can wire this
    output only to other asynchronous WebDAV VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AsynchronousAsynchronous CreateCreate DirectoryDirectory

Creates the specified directory on the remote WebDAV server. The full path to the
parent directory must already exist. Otherwise, this VI returns an error. The request
this VI generates can run in parallel with other asynchronous WebDAV requests.

This VI triggers a Request Complete WebDAV event.


                                                    © National Instruments 5381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5382 ordinal=5382 -->
## Functions

Functions

      Inputs/Outputs

               •      user data —

            user data specifies any data you want to include with the request handle. LabVIEW passes this
            data along with the request handle, but the data does not affect the request. LabVIEW returns
            user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
            data within your VI.

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the location and name of the new directory.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      request handle out —

            request handle out returns the unique reference to the WebDAV request. You can wire this
           output only to other asynchronous WebDAV VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   AsynchronousAsynchronous DirectoryDirectory ListingListing

       Generates a list of all directories and files within the directory you specify in relative
         uri. You can view the list of directories and files in the List Directory Complete WebDAV
       event that this VI triggers. The request this VI generates can run in parallel with other
      asynchronous WebDAV requests.


5382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5383 ordinal=5383 -->
## Functions

Functions

This VI triggers a List Directory Complete WebDAV event.


Inputs/Outputs

   •      user data —

    user data specifies any data you want to include with the request handle. LabVIEW passes this
    data along with the request handle, but the data does not affect the request. LabVIEW returns
    user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
    data within your VI.

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative uri —

     relative uri specifies the location and name of the new directory.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •      request handle out —

    request handle out returns the unique reference to the WebDAV request. You can wire this
    output only to other asynchronous WebDAV VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5384 ordinal=5384 -->
## Functions

Functions

   AsynchronousAsynchronous PathPath InfoInfo

       Generates information about the file or directory you specify in relative uri. You can
      view the file or directory information in the Path Info Complete WebDAV event that this
        VI triggers. The request this VI generates can run in parallel with other asynchronous
     WebDAV requests.

       This VI triggers a Path Info Complete WebDAV event.


      Inputs/Outputs

               •      user data —

            user data specifies any data you want to include with the request handle. LabVIEW passes this
            data along with the request handle, but the data does not affect the request. LabVIEW returns
            user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
            data within your VI.

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •       relative uri —

             relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the
            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —


5384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5385 ordinal=5385 -->
## Functions

Functions


    session handle out returns the unique reference to the WebDAV session.

   •      request handle out —

    request handle out returns the unique reference to the WebDAV request. You can wire this
    output only to other asynchronous WebDAV VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AsynchronousAsynchronous DeleteDelete

Deletes a file or directory on a WebDAV server. The request this VI generates can run in
parallel with other asynchronous WebDAV requests.

This VI triggers a Request Complete WebDAV event.


Inputs/Outputs

   •      user data —

    user data specifies any data you want to include with the request handle. LabVIEW passes this
    data along with the request handle, but the data does not affect the request. LabVIEW returns
    user data in every WebDAV request event cluster. Use this input to pass WebDAV request-specific
    data within your VI.

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •       relative uri —

     relative uri specifies the uniform resource identifier (URI) of the file or directory relative to the


                                                    © National Instruments 5385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5386 ordinal=5386 -->
## Functions

Functions


            host uri prefix that you wire to the Open Session VI. A URI can be a uniform resource locator
             (URL), a uniform resource name (URN), or both. Format relative uri as
          directory/subdirectory/filename.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      request handle out —

            request handle out returns the unique reference to the WebDAV request. You can wire this
           output only to other asynchronous WebDAV VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   AsynchronousAsynchronous RequestRequest StatusStatus

       Gets the current status of an asynchronous request.


      Inputs/Outputs

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •      request handle —


5386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5387 ordinal=5387 -->
## Functions

Functions


  request handle specifies the unique reference to the WebDAV request.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      session handle out —

  session handle out returns the unique reference to the WebDAV session.

•      request handle out —

  request handle out returns the unique reference to the WebDAV request. You can wire this
  output only to other asynchronous WebDAV VIs.

•      request status —

  request status returns the current status of the WebDAV request.

   working
  0   —LabVIEW is still processing the request.
   complete
  1   —LabVIEW has completed the request.
   aborted
  2   —LabVIEW aborted the request.
   timeout
  3   —LabVIEW could not connect to the WebDAV server within the specified timeout limit.
    error
  4 —LabVIEW encountered an error while processing the request and cannot continue completing
   the request.

•      bytes completed —

  bytes completed returns the number of bytes that LabVIEW has uploaded or downloaded since
  the WebDAV request began. If the request does not transfer any bytes, bytes completed returns
  a value of 0.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•       total bytes —

                                                   © National Instruments 5387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5388 ordinal=5388 -->
## Functions

Functions


              total bytes returns the number of bytes that LabVIEW will upload or download when the request
                is complete.

   AsynchronousAsynchronous AbortAbort RequestRequest

       Cancels a working asynchronous WebDAV request. This VI triggers a Request Complete
     WebDAV event that lists the status as aborted.


      Inputs/Outputs

               •      session handle —

            session handle specifies the unique reference to the WebDAV session.

               •      request handle —

            request handle specifies the unique reference to the WebDAV request.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session handle out —

            session handle out returns the unique reference to the WebDAV session.

               •      request handle out —

            request handle out returns the unique reference to the WebDAV request. You can wire this
           output only to other asynchronous WebDAV VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5389 ordinal=5389 -->
## Functions

Functions

AsynchronousAsynchronous CloseClose RequestRequest HandleHandle

Closes and disposes of a request handle. If the request is not complete, this VI aborts
the request.

If you attempt to obtain the status of a closed request handle, LabVIEW returns an
error.


Inputs/Outputs

   •      session handle —

    session handle specifies the unique reference to the WebDAV session.

   •      request handle —

    request handle specifies the unique reference to the WebDAV request.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      session handle out —

    session handle out returns the unique reference to the WebDAV session.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WaitWait forfor ConfiguredConfigured NetworkNetwork

Waits until the system can contact the remote host.

                                                    © National Instruments 5389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5390 ordinal=5390 -->
## Functions

Functions


      Inputs/Outputs

               •     hostname or URL in —

          hostname or URL in specifies the remote host to contact. You can specify an IPv4 address,
          domain name, or URL that contains an IPv4 address or domain name.

               •      timeout in ms —

           timeout in ms specifies the time, in milliseconds, that this VI waits to get a response from the
           remote host. The actual time to wait may be 1-2 seconds more or less than timeout in ms. If
           timeout in ms is -1, this VI chooses a value appropriate for the networking environment. If
           timeout in ms is 0, this VI queries the status for the remote host but does not wait to get a
            response if the remote host is unreachable. The default is -1.

             Refer to the Details section for more information about how this VI waits.

               •     must be directly reachable? (F) —

          must be directly reachable? specifies whether this VI waits until the remote host is directly
             accessible on a local network, without the use of a network gateway. For instance, if you connect
          an IPv4-accessible device directly to the computer over Ethernet or USB, set must be directly
            reachable? to TRUE to ensure that this VI waits until the device is online. The default is FALSE.

             This VI ignores the value of must be directly reachable? under the following circumstances:

                     •  If hostname or URL in is a link-local or multicast address, this VI always waits until the
               remote host is directly reachable.
                     •  If hostname or URL in is unwired, the remote host is never directly reachable.
               •     hostname or URL out —

          hostname or URL out returns the name or URL of the remote host.

               •      network status for remote host —

           network status for remote host returns the current status of the network to contact the remote
             host.


5390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5391 ordinal=5391 -->
## Functions

Functions


     Indeterminate—This VI does not have enough information to determine the network status,    0
     whether due to invalid inputs or internal errors.
    1 Configured—Network configuration can contact the remote host.
    2 Unconfigured—Network configuration does not support connecting to the remote host.


The Wait for Configured Network VI may use heuristics to identify whether or not the
system is sufficiently configured to contact the remote host. If these heuristics fail, the
VI may wait the duration of timeout in ms or return immediately. To avoid incorrectly
waiting, do not specify an excessively large timeout in ms value.

Use the Wait for Configured Network VI before contacting a remote host when all of the
following conditions apply:

  • Your application requires a TCP/IP network connection, which may not yet be
    configured typically due to system startup.
  • Your application has no other preferred mitigation process for connection failures.
    For example, if the application is interactive, using this VI may be inappropriate,
   because the timeout may delay user feedback, particularly if the remote host may
   be mistyped or otherwise incorrect. In this situation, you may want to report the
   connection failure immediately and allow the user to choose to retry the
    connection.
  • The connection attempt is not time-sensitive. This VI may take several hundred
    milliseconds to execute, even when not waiting. If you are making several
   connection attempts in sequence, only call this VI once, for the first connection.
  • (NI Linux Real-Time) Time-critical performance is not considered critical while this
    VI runs. On NI Linux Real-Time targets, this VI may perform system operations that
    affect determinism, even if the operations run at a lower priority. Consider running
    this VI before starting time-critical loops, or while time-critical performance is not
   a high priority during system startup.

The Wait for Configured Network VI achieves the same result that retrying a
connection request in a For Loop achieves, in addition to the following advantages:

  • This VI only queries the operating system and requires no network traffic.
  • You do not need to distinguish between network-failure errors and other errors
    inside the For Loop.

                                                    © National Instruments 5391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5392 ordinal=5392 -->
## Functions

Functions

            • In a For Loop, you must choose the duration of the connection attempts by
           estimating system conditions that may evolve over time and across deployment to
            different targets. By default, the Wait for Configured Network VI sets a timeout
          considered appropriate for the vast majority of LabVIEW application deployments.

     SFTPSFTP

      Use the SFTP VIs and nodes to interact with the data and files on an SFTP server.


         Palette                     Description        Object

                   Connects to an SFTP server using OpenSSH (ssh.exe) or PuTTY (plink.exe).
        Connect
                  You must manually select the polymorphic instance you want to use.


        Disconnect  Disconnects from an SFTP server.


                   Uploads local file(s) from disk, buffer, or stream to an SFTP server.
        Upload
                  You must manually select the polymorphic instance you want to use.


                  Downloads file(s) from an SFTP server and returns the file(s) to the disk, buffer, or
       Download  stream.
          VI
                  You must manually select the polymorphic instance you want to use.


                     Deletes a file from an SFTP server. If you want to delete an entire directory, use the
         Delete File
                     Delete Directory VI.


5392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5393 ordinal=5393 -->
## Functions

Functions


 Palette             Description
 Object

 Rename   Renames a file or directory on an SFTP server.


 Create             Creates a directory on an SFTP server. Directory

 List             Acquires information about the contents of a directory on an SFTP server. Directory


 Delete      Deletes a directory on an SFTP server. If you want to delete a single file, use the Delete
 Directory    File VI.


           Use the Advanced VIs and nodes for more advanced operations on an SFTP server,
 Advanced   such as updating file attributes, reading filesystem statistics, and configuring server
              settings.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Data Communication\Protocols\SFTP

ConnectConnect

Connects to an SFTP server using OpenSSH (ssh.exe) or PuTTY (plink.exe).

You must manually select the polymorphic instance you want to use.


  • Connect (OpenSSH) VI
  • Connect (PuTTY) VI


                                                    © National Instruments 5393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5394 ordinal=5394 -->
## Functions

Functions

            • Connect (Generic) VI
   ConnectConnect (OpenSSH)(OpenSSH) VIVI

      Connects to an SFTP server using an installed OpenSSH client.


      Inputs/Outputs

               •       client —

              client is a class instance for the specified OpenSSH client. Set property nodes on this object
            before calling the Connect VI to set advanced connection options.

               •      user@host —

           user@host specifies the destination SFTP server. This may be specified as
         <username>@<hostname>, or any other destination understood by the OpenSSH SSH client.
             This input is optional if you do not require custom configuration of the server.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session —

            session returns a session that stores the configuration and state of an SFTP server connection.
           Use this session to refer to the SFTP server connection in subsequent VI calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5395 ordinal=5395 -->
## Functions

Functions

ConnectConnect (PuTTY)(PuTTY) VIVI

Connects to an SFTP server using the Plink executable typically installed with the
PuTTY client.


Inputs/Outputs

   •       client —

     client is a class instance for the specified PuTTY client. Set property nodes on this object before
     calling the Connect VI to set advanced connection options.

   •      user@host —

    user@host specifies the destination SFTP server. This may be specified as
   <username>@<hostname>, or any other destination understood by the Plink SSH client.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session —

    session returns a session that stores the configuration and state of an SFTP server connection.
    Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5396 ordinal=5396 -->
## Functions

Functions

   ConnectConnect (Generic)(Generic) VIVI

      Connects to an SFTP server. The client determines which SSH Client to use.


      Inputs/Outputs

               •       client —

              client is a class instance for the specified SSH client. This terminal automatically determines
           which SSH client to use. Set property nodes on this object before calling the Connect VI to set
           advanced connection options

               •      user@host —

           user@host specifies the destination SFTP server. This may be specified as
         <username>@<hostname>, or any other destination understood by the SSH client. This input
                is optional if you do not require custom configuration of the server.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session —

            session returns a session that stores the configuration and state of an SFTP server connection.
           Use this session to refer to the SFTP server connection in subsequent VI calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5397 ordinal=5397 -->
## Functions

Functions

DisconnectDisconnect

Disconnects from an SFTP server.


Inputs/Outputs

   •      session in —

    session in specifies the session of the SFTP server connection.

   •       error in —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      return code —

    return code returns the exit code of the underlying SSH executable. Typically, the value of 0
    stands for success and any number from 1 to 255 stands for other conditions.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to reconnect to the SFTP server and to recover from problems
     trusting the server identity.

   •      server errors —

    server error returns sideband logging and error information sent by the SFTP server.

   •       error out —


                                                    © National Instruments 5397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5398 ordinal=5398 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      UploadUpload

      Uploads local file(s) from disk, buffer, or stream to an SFTP server.

      You must manually select the polymorphic instance you want to use.


            • Upload File
            • Upload File from Buffer
            • Upload File from Stream
            • Upload Multiple Files
   UploadUpload FileFile

       Creates a new remote file, initialized with the contents of a local file.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •       local path —

             local path specifies the path of the file you want to upload.

               •      remote path —

5398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5399 ordinal=5399 -->
## Functions

Functions


    remote path specifies the path of the directory where the file is uploaded.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •       attributes —

    attributes specifies the reference to the information, such as name, size, permissions and
    modification time, about the file you upload.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

UploadUpload FileFile fromfrom BufferBuffer

Creates a new remote file, initialized with a byte array.


Inputs/Outputs

   •      session in —


                                                    © National Instruments 5399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5400 ordinal=5400 -->
## Functions

Functions


            session in specifies the session of the SFTP server connection.

               •      data —

           data specifies the buffer, in byte array, of the file you want to upload.

               •      remote path —

           remote path specifies the path of the directory where the file is uploaded.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •       attributes —

             attributes specifies the reference to the information, such as name, size, permissions and
            modification time, about the file you upload.

               •      session out —

            session out returns a session that stores the configuration and state of an SFTP server
            connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   UploadUpload FileFile fromfrom StreamStream

       Creates a new remote file, initialized with a High-Speed Stream of byte arrays.


5400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5401 ordinal=5401 -->
## Functions

Functions


Inputs/Outputs

   •      session in —

    session in specifies the session of the SFTP server connection.

   •      channel —

    channel specifies the channel, in a High-Speed Stream of byte arrays, of the file you want to
    upload.

   •      remote path —

    remote path specifies the path of the directory where the file is uploaded.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •       attributes —

    attributes specifies the reference to the information, such as name, size, permissions and
    modification time, about the file you upload.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5402 ordinal=5402 -->
## Functions

Functions

   UploadUpload MultipleMultiple FilesFiles

       Creates multiple remote files.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •        file specifications —

                file specifications specifies the local paths of the files you want to upload and the remote paths
             of the directories where the files are uploaded.

                     •      remote path —

              remote path specifies the path of the directory where the file is uploaded.

                     •       local path —

                  local path specifies the path of the file you want to upload.


               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •       attributes —


5402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5403 ordinal=5403 -->
## Functions

Functions


    attributes specifies the reference to the information, such as name, size, permissions and
    modification time, about the file you upload.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


DownloadDownload VIVI

Downloads file(s) from an SFTP server and returns the file(s) to the disk, buffer, or
stream.

You must manually select the polymorphic instance you want to use.


  • Download File VI
  • Download File To Buffer VI
  • Download File to Stream VI
  • Download Multiple Files VI
DownloadDownload FileFile VIVI

Downloads a remote file, storing the contents in a local file.


                                                    © National Instruments 5403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5404 ordinal=5404 -->
## Functions

Functions

      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      remote path —

           remote path specifies the path of the file that you want to download from the SFTP server.

               •       local path —

             local path specifies the path where you want to store the file on your local machine.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session out —

            session out returns a session that stores the configuration and state of an SFTP server
            connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   DownloadDownload FileFile ToTo BufferBuffer VIVI

      Downloads a remote file, returning the contents as a byte array.


5404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5405 ordinal=5405 -->
## Functions

Functions

Inputs/Outputs

   •      session in —

    session in specifies the session of the SFTP server connection.

   •      remote path —

    remote path specifies the path of the file that you want to download from the SFTP server.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       buffer —

    buffer returns the contents of the file you download as a byte array.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DownloadDownload FileFile toto StreamStream VIVI

Downloads a remote file, returning the contents as a High-Speed Stream of byte
arrays.


                                                    © National Instruments 5405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5406 ordinal=5406 -->
## Functions

Functions


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      remote path —

           remote path specifies the path of the file that you want to download from the SFTP server.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session out —

            session out returns a session that stores the configuration and state of an SFTP server
            connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

               •      channel —

           channel returns the contents of the file you download as a High-Speed Stream of byte arrays.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   DownloadDownload MultipleMultiple FilesFiles VIVI

      Downloads multiple files.


5406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5407 ordinal=5407 -->
## Functions

Functions


Inputs/Outputs

   •      session in —

    session in specifies the session of the SFTP server connection.

   •        file specifications —

      file specifications specifies the remote paths of the files you want to download and the local
    paths of the folders where the files are downloaded on your local machine.

         •      remote path —

       remote path specifies the path of the file that you want to download from the SFTP server.

         •       local path —

         local path specifies the path where you want to store the file on your local machine.


   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5408 ordinal=5408 -->
## Functions

Functions

      DeleteDelete FileFile

       Deletes a file from an SFTP server. If you want to delete an entire directory, use the
       Delete Directory VI.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      path —

           path specifies the path of the file that you want to delete from the SFTP server.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session out —

            session out returns a session that stores the configuration and state of an SFTP server
            connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     RenameRename

      Renames a file or directory on an SFTP server.

5408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5409 ordinal=5409 -->
## Functions

Functions


Inputs/Outputs

   •     must be atomic —

    must be atomic specifies whether the rename action must be atomic. The default value is FALSE.

    Use this input to ensure that running processes do not temporarily see the destination file as
    missing. Atomic rename is an OpenSSH extension and may not be supported on all SFTP servers.

   •      session in —

    session in specifies the session of the SFTP server connection.

   •      old remote path —

    old remote path specifies the path of the file or directory that you want to rename on the SFTP
     server.

   •     new remote path —

   new remote path specifies the new path with the updated name of the file or directory.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

                                                    © National Instruments 5409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5410 ordinal=5410 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      CreateCreate DirectoryDirectory

       Creates a directory on an SFTP server.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      remote path —

           remote path specifies the path of the directory that you want to create on the SFTP server.

               •      create as needed —

            create as needed specifies whether to create the directory only if it does not already exist. The
             default value is FALSE.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session out —

            session out returns a session that stores the configuration and state of an SFTP server
            connection. Use this session to refer to the SFTP server connection in subsequent VI calls.


5410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5411 ordinal=5411 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ListList DirectoryDirectory

Acquires information about the contents of a directory on an SFTP server.


Inputs/Outputs

   •      session in —

    session in specifies the session of the SFTP server connection.

   •      remote path —

    remote path specifies the path of the directory that you want to inspect on the SFTP server.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •        files and directories —

     files and directories returns an array of File Attributes objects. Use the File Attributes node on
    each element of the array to identify filenames and other metadata.


                                                    © National Instruments 5411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5412 ordinal=5412 -->
## Functions

Functions


             This VI always populates the Name and Long Listing properties of each File Attributes element.
          The Name property contains the filename. The Long Listing property contains a single line
          summary of the file information.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      DeleteDelete DirectoryDirectory

       Deletes a directory on an SFTP server. If you want to delete a single file, use the Delete
        File VI.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      path —

           path specifies the path of the directory that you want to delete from the SFTP server.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session out —


5412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5413 ordinal=5413 -->
## Functions

Functions


    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AdvancedAdvanced

Use the Advanced VIs and nodes for more advanced operations on an SFTP server,
such as updating file attributes, reading filesystem statistics, and configuring server
settings.


 Palette               Description Object

 Get File       Acquires information about a file or directory on an SFTP server. Use the output
 Attributes     reference to view or modify the file attributes with the File Attributes node.

 SFTP File               Gets (reads) or sets (writes) file attributes contained in a File Attributes object. Attributes              These objects are returned by several SFTP functions, and can be used to update
 Property                     file attributes with the Set File Attributes function. Node

 Set File
              Updates mutable information about a file or directory on an SFTP server.
 Attributes


 Read          Acquires information, including total space and free space, about the disk or
 Filesystem     filesystem that contains the specified path. The server must support OpenSSH
 Statistics      extensions. Use the Filesystem Statistics node to read total and free disk space.


 SFTP
               Gets (reads) remote filesystem statistics returned by the Get Filesystem Statistics
 Filesystem
                function.
 Statistics

                                                    © National Instruments 5413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5414 ordinal=5414 -->
## Functions

Functions


         Palette                       Description
        Object

         Property
       Node

       SFTP Session                      Gets (reads) or sets (writes) properties of an SFTP Session object. Use these
         Property                        properties to configure SFTP before and during a connection to an SFTP server.       Node

         Create                       Creates a symbolic link on an SFTP server. A symbolic link is a file that points to        Symbolic                      another file or directory.         Link

       Read
        Symbolic      Resolves all symbolic links referenced in a remote path.
         Link

         Canonicalize                      Transforms a remote path into its absolute, canonical form.
        Path

   GetGet FileFile AttributesAttributes

       Acquires information about a file or directory on an SFTP server. Use the output
       reference to view or modify the file attributes with the File Attributes node.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      remote path —

           remote path specifies the path of the file or directory on the SFTP server.

               •       error in —

5414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5415 ordinal=5415 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •        file attributes —

      file attributes returns a reference to the information, such as name, size, permissions and
    modification time, about the file or directory you specify in remote path. Use this reference to
     refer to these file attributes in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SFTPSFTP FileFile AttributesAttributes PropertyProperty NodeNode

Gets (reads) or sets (writes) file attributes contained in a File Attributes object. These
objects are returned by several SFTP functions, and can be used to update file
attributes with the Set File Attributes function.

The Property Node (File Attributes) is preconfigured to access File Attributes
properties. The node operates in the same way as a standard Property Node.


                                                    © National Instruments 5415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5416 ordinal=5416 -->
## Functions

Functions

      Inputs/Outputs

               •      reference —
            reference is the refnum associated with the object for which you want to set or get properties.

                    If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For
            the Application class, the default is the current application instance. For the VI class, the default
                is the VI containing the Property Node.

           You also can wire a LabVIEW class to the reference input to access the private data of the
           LabVIEW class.

               •       error in (no error) —
             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.
               •      property 2 — property 2..n are examples of properties you want to set (write).
               •      reference out —
            reference out returns reference unchanged.
               •       error out —
             error out contains error information. This output provides standard error out functionality.
               •      Properties:Name —
            property 1..n are examples of properties you want to get (read).

    SetSet FileFile AttributesAttributes

      Updates mutable information about a file or directory on an SFTP server.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      remote path —


5416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5417 ordinal=5417 -->
## Functions

Functions


    remote path specifies the path of the file or directory that you want to update on the SFTP
     server.

   •        file attributes —

      file attributes specifies the reference to the file attributes of the file or directory that you modify
    with the File Attributes node.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReadRead FilesystemFilesystem StatisticsStatistics

Acquires information, including total space and free space, about the disk or filesystem
that contains the specified path. The server must support OpenSSH extensions. Use
the Filesystem Statistics node to read total and free disk space.

      Note Files accessible over SFTP may span more than one filesystem. For
        instance, on an NI Linux Real-Time system, the directories /home/lvuser,
      /media/sda1, and /tmp typically each resides on a different filesystem,
      and this VI might return different results for each directory.


                                                    © National Instruments 5417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5418 ordinal=5418 -->
## Functions

Functions


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      remote path —

           remote path specifies the path of the disk or filesystem on the SFTP server.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session out —

            session out returns a session that stores the configuration and state of an SFTP server
            connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

               •       filesystem statistics —

            filesystem statistics returns a reference to the statistics, including total and free space, for the
             disk or filesystem. Use this reference to refer to these statistics in subsequent VI calls.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SFTPSFTP FilesystemFilesystem StatisticsStatistics PropertyProperty NodeNode

       Gets (reads) remote filesystem statistics returned by the Get Filesystem Statistics
       function.

      The Property Node (Filesystem Statistics) is preconfigured to access Filesystem
        Statistics properties. The node operates in the same way as a standard Property Node.


5418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5419 ordinal=5419 -->
## Functions

Functions


Inputs/Outputs

   •      reference —

      Is the filesystem statistics object for which you want to get or set properties.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      reference out —

    reference out returns reference unchanged.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      Properties:Bytes Free —

    Bytes Free is an exanple of a property you want to get or set.

SFTPSFTP SessionSession PropertyProperty NodeNode

Gets (reads) or sets (writes) properties of an SFTP Session object. Use these properties
to configure SFTP before and during a connection to an SFTP server.

The Property Node (Session Node) is preconfigured to access Session Node properties.
The node operates in the same way as a standard Property Node.


                                                    © National Instruments 5419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5420 ordinal=5420 -->
## Functions

Functions

      Inputs/Outputs

               •      reference —
            reference is the refnum associated with the object for which you want to set or get properties.

                    If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For
            the Application class, the default is the current application instance. For the VI class, the default
                is the VI containing the Property Node.

           You also can wire a LabVIEW class to the reference input to access the private data of the
           LabVIEW class.

               •       error in (no error) —
             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.
               •      Synchronize Transferred Files —
            property 2..n are examples of properties you want to set (write).
               •      reference out —
            reference out returns reference unchanged.
               •       error out —
             error out contains error information. This output provides standard error out functionality.
               •      property 1 — property 1..n are examples of properties you want to get (read).

    CreateCreate SymbolicSymbolic LinkLink

       Creates a symbolic link on an SFTP server. A symbolic link is a file that points to
      another file or directory.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •       target —


5420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5421 ordinal=5421 -->
## Functions

Functions


    target specifies the path of the file or directory that you want to point to on the SFTP server.

   •      source —

    source specifies the path of the symbolic link that you want to create on the SFTP server.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReadRead SymbolicSymbolic LinkLink

Resolves all symbolic links referenced in a remote path.


Inputs/Outputs

   •      session in —

    session in specifies the session of the SFTP server connection.

   •      remote path —

                                                    © National Instruments 5421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5422 ordinal=5422 -->
## Functions

Functions


           remote path specifies the path that contains the symbolic links.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (ms) —

           timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
             indicates to wait indefinitely. The default value is 30000.

               •      session out —

            session out returns a session that stores the configuration and state of an SFTP server
            connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

               •      remote target —

           remote target returns the path of the file or directory that the symbolic links point to.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    CanonicalizeCanonicalize PathPath

       Transforms a remote path into its absolute, canonical form.


      Inputs/Outputs

               •      session in —

            session in specifies the session of the SFTP server connection.

               •      path —

5422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5423 ordinal=5423 -->
## Functions

Functions


    path specifies the remote path that you want to transform.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (ms) —

    timeout (ms) specifies the time, in milliseconds, that the VI waits before timing out. A value of –1
     indicates to wait indefinitely. The default value is 30000.

   •      session out —

    session out returns a session that stores the configuration and state of an SFTP server
    connection. Use this session to refer to the SFTP server connection in subsequent VI calls.

   •      canonicalized path —

    canonicalized path returns the absolute, canonical form of path.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ChannelChannel WireWire EndpointsEndpoints

Channel wire endpoints are nodes where a channel wire terminates.

By connecting a channel writer endpoint to a reader endpoint using a channel wire,
you build a channel. The channel wire endpoints operate on the channel in the
following way: the writer endpoints write data to the channel, and reader endpoints
read data from the channel. You can use the channel wire endpoints to write or read
data between parallel sections of code. LabVIEW provides several channel templates.
Each template expresses a different communications protocol to use between the
writers and readers. Choose which channel template to use based on your
communications needs.

Create a channel endpoint by right-clicking a terminal or a wire and selecting
Create»Channel Writer or Create»Channel Reader. When you create an endpoint from

                                                    © National Instruments 5423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5424 ordinal=5424 -->
## Functions

Functions

      a terminal, you instantiate the channel template with that data type as its transmission
       type.

    © 2005–2023 National Instruments Corporation. All rights reserved. Refer to the
     <National Instruments>\_Legal Information directory for information
      about NI copyright, patents, trademarks, warranties, product warnings, and export
       compliance.

     StreamStream

      Use the Stream channel to communicate homogeneous data from a single writer to a
       single reader. The data elements are buffered and transferred with no data loss in a
         first-in-first-out (FIFO) order.

       WriteWrite

       Writes an element to a Stream channel. The endpoint waits if the channel is full.


      Inputs/Outputs

               •      timeout in ms (-1) —

           timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to
            the channel. The default value is -1, which means there is no time limit.

               •      element valid? (T) —

           element valid? specifies whether the element is valid. If TRUE, the endpoint records the
           element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
            nothing if both element valid? and last element? are FALSE. The default is TRUE.

               •      element —

           element specifies the data to write to the channel.


5424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5425 ordinal=5425 -->
## Functions

Functions

   •       last element? (F) —

     last element? specifies whether this is the last element that the endpoint writes to the channel.
    The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
    to write. The reader endpoint can continue reading data until the last element? output of the
    reader endpoint returns TRUE.

   •       size (unlimited) —

     size specifies the maximum number of elements that can be buffered in the channel. The default
      is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
    endpoint ignores the size input.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
    endpoint writes the data specified in element to the channel.

   •      count —

    count returns the number of elements in the channel after this endpoint updates the channel.
    Use this output to monitor the relative writing and reading speed of the channel endpoints and
   make adjustments, if necessary.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.


WriteWrite MultipleMultiple

Writes an array of elements to a Stream channel, one element at a time. The endpoint
waits if the channel is full.

You can drop this endpoint on the block diagram by right-clicking a terminal or a wire
and selecting Create»Channel Writer»Stream»Write Multiple.


                                                    © National Instruments 5425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5426 ordinal=5426 -->
## Functions

Functions

      Inputs/Outputs

               •      timeout in ms (-1) —

           timeout in ms is the time, in milliseconds, that this endpoint has to write one data element in
            the specified array to the channel. The default value is -1, which means there is no time limit.

               •      elements —

           elements specifies an array of data to write to the channel.

               •       last element? (F) —

              last element? specifies whether this is the last array of data that the endpoint writes to the
            channel. The default is FALSE. If TRUE, the endpoint marks the channel as closed after writing
            the last element in the array and ignores further calls to write. The reader endpoint can continue
            reading data until the last element? output of the reader endpoint returns TRUE.

               •       size (unlimited) —

             size specifies the maximum number of elements that can be buffered in the channel. The default
                is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
           endpoint ignores the size input.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
           endpoint writes the array of data specified in elements to the channel.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •     number unwritten —

          number unwritten returns the number of elements in the array that are not written to the
            channel. This output will always be zero unless the endpoint times out before finishing writing
                all the elements in the array.


5426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5427 ordinal=5427 -->
## Functions

Functions

Related Information

Read Multiple

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Channels\Measure And Log\Channel -
   Measure And Log.lvproj
  • labview\examples\Channels\Stream String Processing\
   Channel - String Processing.lvproj

WriteWrite ScheduledScheduled

Writes an element to a Stream channel at a scheduled time. The endpoint waits until
the scheduled time and continues waiting if the channel is full at the scheduled time.


Inputs/Outputs

   •      scheduled time —

    scheduled time specifies the time when the endpoint should write data to the channel.

   •      element valid? (T) —

    element valid? specifies whether the element is valid. If TRUE, the endpoint records the
    element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
    nothing if both element valid? and last element? are FALSE. The default is TRUE.

   •      element —

    element specifies the data to write to the channel.

   •       last element? (F) —

                                                    © National Instruments 5427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5428 ordinal=5428 -->
## Functions

Functions


              last element? specifies whether this is the last element that the endpoint writes to the channel.
          The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
             to write. The reader endpoint can continue reading data until the last element? output of the
            reader endpoint returns TRUE.

               •       size (unlimited) —

             size specifies the maximum number of elements that can be buffered in the channel. The default
                is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
           endpoint ignores the size input.

               •      actual time —

            actual time returns the actual time when the endpoint wrote data to the channel.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.


       WriteWrite WithWith AbortAbort

       Writes an element to a Stream channel or signals the channel to abort. The endpoint
       waits if the channel is full. This endpoint is the same as the Write endpoint except that
          it has an abort input and an aborted? output. You can use the abort capability of the
      Stream channel to close a channel abruptly, ignoring any data left in the channel
        buffer. You must use this endpoint together with the Read With Abort endpoint.


5428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5429 ordinal=5429 -->
## Functions

Functions

Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to
    the channel. The default value is -1, which means there is no time limit.

   •      element valid? (T) —

    element valid? specifies whether the element is valid. If TRUE, the endpoint records the
    element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
    nothing if both element valid? and last element? are FALSE. The default is TRUE.

   •      element —

    element specifies the data to write to the channel.

   •       last element? (F) —

     last element? specifies whether this is the last element that the endpoint writes to the channel.
    The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
    to write. The reader endpoint can continue reading data until the last element? output of the
    reader endpoint returns TRUE.

   •      abort —

    abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
    as closed and ignores further calls to write. Meanwhile, the aborted? output returns TRUE on the
    next call of this endpoint.

   •       size (unlimited) —

     size specifies the maximum number of elements that can be buffered in the channel. The default
      is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
    endpoint ignores the size input.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
    endpoint writes the data specified in element to the channel.

   •      count —

    count returns the number of elements in the channel after this endpoint updates the channel.


                                                    © National Instruments 5429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5430 ordinal=5430 -->
## Functions

Functions


           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the reader endpoints connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.


     ReadRead

      Reads an element from a Stream channel. The endpoint waits if the channel is empty.


      Inputs/Outputs

               •      timeout in ms (-1) —

           timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
            channel. The default value is -1, which means there is no time limit.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
           endpoint reads the data specified in element from the channel. If timed out? is TRUE, element
             valid? and last element? will be FALSE.

               •      element valid? —


5430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5431 ordinal=5431 -->
## Functions

Functions


    element valid? returns TRUE if the element was read successfully. This output returns FALSE if a
    timeout occurs, if the channel closes without a valid last element, or if the channel aborts.

   •      element —

    element returns the data that this endpoint reads from the channel. This output returns the
     default value of the transmission data type if a timeout occurs, if the channel closes without a
     valid last element, or if the channel aborts.

   •       last element? —

     last element? returns whether this is the last element that the endpoint reads from the channel.
     last element? can be TRUE even if element valid? is FALSE, which means that the last element
    was already written to the channel during the previous iteration or the channel closes without a
     valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

   •      count —

    count returns the number of elements in the channel after this endpoint updates the channel.
    Use this output to monitor the relative writing and reading speed of the channel endpoints and
   make adjustments, if necessary.


ReadRead MultipleMultiple

Reads multiple elements as a block from a Stream channel. You can configure how and
when the channel waits for multiple elements.

You can drop this endpoint on the block diagram by right-clicking a Stream channel
terminal or wire and selecting Create»Channel Reader»Stream»Read Multiple.


Inputs/Outputs

   •      timeout in ms (-1) —


                                                    © National Instruments 5431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5432 ordinal=5432 -->
## Functions

Functions


           timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
            channel. The default value is -1, which means there is no time limit.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •     number to read (-1, available) —

          number to read specifies the number of elements the endpoint returns each time. The default is
                -1.

            negative The endpoint returns as many elements as there are in the channel, if any, without any
          number waiting.
                 The endpoint waits for the last element and then returns all elements. If a timeout
           0       occurs before the last element is available, the endpoint returns all the available
                   elements in the channel.
                 The endpoint waits for the specified number of elements to be available and then
             positive returns them. If the last element is transmitted or a timeout occurs before the specified
          number number of elements are available, the endpoint returns all the available elements in the
                    channel.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses. If timed out?
                is TRUE, last element? will be FALSE.

               •      elements —

           elements returns the array of data that the endpoint reads from the channel. This output returns
          an empty array if the channel aborts.

               •       last element? —

              last element? returns whether this is the last element that the endpoint reads from the channel.
              last element? can be TRUE even if element valid? is FALSE, which means that the last element
          was already written to the channel during the previous iteration or the channel closes without a
              valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.


5432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5433 ordinal=5433 -->
## Functions

Functions


    Use this output to monitor the relative writing and reading speed of the channel endpoints and
   make adjustments, if necessary.


Related Information

Write Multiple

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Channels\Stream String Processing\
   Channel - String Processing.lvproj

ReadRead ScheduledScheduled

Reads an element from a Stream channel at a scheduled time. The endpoint waits if no
element is available in the channel at the scheduled time.


Inputs/Outputs

   •      scheduled time —

    scheduled time specifies the time when the endpoint should read data from the channel.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      actual time —

    actual time returns the actual time when the endpoint read data from the channel.


                                                    © National Instruments 5433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5434 ordinal=5434 -->
## Functions

Functions

               •      element valid? —

           element valid? returns TRUE if the element was read successfully. This output returns FALSE if
            the channel closes without a valid last element or if the channel aborts.

               •      element —

           element returns the data that this endpoint reads from the channel. This output returns the
             default value of the transmission data type if a timeout occurs, if the channel closes without a
              valid last element, or if the channel aborts.

               •       last element? —

              last element? returns whether this is the last element that the endpoint reads from the channel.
              last element? can be TRUE even if element valid? is FALSE, which means that the last element
          was already written to the channel during the previous iteration or the channel closes without a
              valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.


     ReadRead WithWith AbortAbort

      Reads an element from a Stream channel or signals the channel to abort. This
      endpoint is the same as the Read endpoint except that it has an abort input and an
      aborted? output. You can use the abort capability of the Stream channel to close a
      channel abruptly, ignoring any data left in the channel buffer. You must use this
      endpoint together with the Write With Abort endpoint.


      Inputs/Outputs

               •      timeout in ms (-1) —

5434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5435 ordinal=5435 -->
## Functions

Functions


  timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
  channel. The default value is -1, which means there is no time limit.

•      channel —

  channel is the channel wire that connects this endpoint to a writer endpoint.

•      abort —

  abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
  as closed and ignores further calls to read. Meanwhile, the aborted? output returns TRUE on the
  next call of this endpoint.

•      timed out? —

  timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
  endpoint reads the data specified in element from the channel. This output returns FALSE if
  aborted? is TRUE. If timed out? is TRUE, element valid? and last element? will be FALSE.

•      element valid? —

  element valid? returns TRUE if the element was read successfully. This output returns FALSE if a
  timeout occurs, if the channel closes without a valid last element, or if the channel aborts.

•      element —

  element returns the data that this endpoint reads from the channel. This output returns the
  default value of the transmission data type if a timeout occurs, if the channel closes without a
  valid last element, or if the channel aborts.

•       last element? —

  last element? returns whether this is the last element that the endpoint reads from the channel.
  last element? can be TRUE even if element valid? is FALSE, which means that the last element
  was already written to the channel during the previous iteration or the channel closes without a
  valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

•      aborted? —

  aborted? returns TRUE if abort occurred on this endpoint or the writer endpoint connected to
  the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
  aborted? TRUE again.

•      count —


                                                   © National Instruments 5435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5436 ordinal=5436 -->
## Functions

Functions


           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.


       ReplicateReplicate

        Splits a Stream channel into two Stream channels so that each of the readers of the
       channels receives a separate copy of the data written into the original channel.


      Inputs/Outputs

               •      stream —

           stream is the channel wire that connects this endpoint to a writer endpoint and splits into two
            outgoing channels.

               •      independent aborts? (F) —

           independent aborts? specifies whether signaling one of the outgoing channels to abort only
            causes that one outgoing channel to abort. The default is FALSE, which means if one of the
            outgoing channels aborts, the other will also abort.

               •      copy 1 size (unlimited) —

           copy 1 size specifies the number of remaining elements to write to the first outgoing channel.
          The default is unlimited.

               •      copy 2 size (unlimited) —

           copy 2 size specifies the number of remaining elements to write to the second outgoing channel.
          The default is unlimited.

               •      stream copy 1 —

           stream copy 1 is the first outgoing channel wire that connects this endpoint to a reader


5436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5437 ordinal=5437 -->
## Functions

Functions


    endpoint.

   •      stream copy 2 —

    stream copy 2 is the second outgoing channel wire that connects this endpoint to a reader
    endpoint.

TagTag

Use the Tag channel to share a single value among multiple readers and/or writers.
Sharing the value is similar to sharing a global or network shared variable. Each time a
writer endpoint writes a value to the channel, the value overwrites the existing value in
the channel to ensure that the reader endpoints always read the latest value.

WriteWrite

Writes a value to a Tag channel.


Inputs/Outputs

   •      element —

    element specifies the data to write to the channel.

   •      previous element —

    previous element returns the value of the channel before this endpoint updates the channel.
    This output returns the default value of the transmission data type if the channel aborts.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.


                                                    © National Instruments 5437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5438 ordinal=5438 -->
## Functions

Functions

       WriteWrite ScheduledScheduled

       Writes a value to a Tag channel at the scheduled time.


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should write data to the channel.

               •      element —

           element specifies the data to write to the channel.

               •      actual time —

            actual time returns the actual time when the endpoint wrote data to the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •      previous element —

            previous element returns the value of the channel before this endpoint updates the channel.
             This output returns the default value of the transmission data type if the channel aborts.


       WriteWrite WithWith AbortAbort

       Writes a value to a Tag channel or signals the channel to abort. This endpoint is the
     same as the Write endpoint except that it has an abort input and an aborted? output.
      You can use the abort capability of the Tag channel to close a channel abruptly,
       ignoring any data left in the channel buffer. You must use this endpoint together with
       the Read With Abort endpoint.


5438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5439 ordinal=5439 -->
## Functions

Functions


Inputs/Outputs

   •      element —

    element specifies the data to write to the channel.

   •      abort —

    abort specifies whether to abort this channel. If abort is TRUE, this endpoint will not perform
     further write operations until the whole channel is reset. Reset occurs when the common caller
     VI of both the writer endpoint and the reader endpoint begins another iteration.

   •      previous element —

    previous element returns the value of the channel before this endpoint updates the channel.
    This output returns the default value of the transmission data type if the channel aborts.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.

   •      aborted? —

    aborted? returns TRUE if abort occurred on this endpoint or the reader endpoints connected to
    the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
    aborted? TRUE again.


ReadRead

Reads a value from a Tag channel.


                                                    © National Instruments 5439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5440 ordinal=5440 -->
## Functions

Functions

      Inputs/Outputs

               •      timeout in ms (0) —

           timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
            channel. The default is 0.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      missed —

           missed returns the number of times that the element from the channel has been overwritten.

               •      element —

           element returns the data that this endpoint reads from the channel. If a timeout occurs or the
           channel aborts, the data will be the last value that this endpoint reads from the channel.


     ReadRead ScheduledScheduled

      Reads a value from a Tag channel at a scheduled time.


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should read data from the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      actual time —


5440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5441 ordinal=5441 -->
## Functions

Functions


    actual time returns the actual time when the endpoint read data from the channel.

   •      element —

    element returns the data that this endpoint reads from the channel. If a timeout occurs or the
    channel aborts, the data will be the last value that this endpoint reads from the channel.

   •      missed —

    missed returns the number of times that the element from the channel has been overwritten.


ReadRead WithWith AbortAbort

Reads a value from a Tag channel or signals the channel to abort. This endpoint is the
same as the Read endpoint except that it has an abort input and an aborted? output.
You can use the abort capability of the Tag channel to close a channel abruptly,
ignoring any data left in the channel buffer. You must use this endpoint together with
the Write With Abort endpoint.


Inputs/Outputs

   •      timeout in ms (0) —

    timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
    channel. The default is 0.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      abort —

    abort specifies whether to abort this channel. If abort is TRUE, this endpoint will not perform
     further read operations until the whole channel is reset. Reset occurs when the common caller VI


                                                    © National Instruments 5441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5442 ordinal=5442 -->
## Functions

Functions


             of both the writer endpoint and the reader endpoint begins another iteration.

               •      missed —

           missed returns the number of times that the element from the channel has been overwritten.

               •      element —

           element returns the data that this endpoint reads from the channel. If a timeout occurs or the
           channel aborts, the data will be the last value that this endpoint reads from the channel.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the writer endpoint connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.

     MessengerMessenger

      Use the Messenger channel to transfer command-like messages among multiple
       writers and/or multiple readers. Messages can optionally be synchronous when the
       writer waits until the message is acknowledged by the reader. The Messenger channel
         is also capable of consolidating repetitive messages and disposing orphaned
      messages when the channel aborts.

       WriteWrite

       Writes an element to a Messenger channel. The endpoint waits if the channel is full.


      Inputs/Outputs

               •      timeout in ms (-1) —


5442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5443 ordinal=5443 -->
## Functions

Functions


    timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to
    the channel. The default value is -1, which means there is no time limit.

   •      wait for ack (F) —

    wait for ack specifies whether this endpoint waits until a reader endpoint acknowledges
     receiving the message before writing the next element. The default is FALSE.

   •      element —

    element specifies the data to write to the channel.

         •      MessageAckBase.lvclass —


   •       size (unlimited) —

     size specifies the maximum number of elements that can be buffered in the channel. The default
      is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
    endpoint ignores the size input.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses. This output
    returns FALSE if the channel aborts on any endpoint.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.

   •       id —

     id returns an integer that identifies this message within the channel. Other endpoints use this
     integer to cancel or acknowledge the message within the channel.


WriteWrite ScheduledScheduled

Writes an element to a Messenger channel at a scheduled time. The endpoint waits
until the scheduled time and continues waiting if the channel is full at the scheduled
time.


                                                    © National Instruments 5443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5444 ordinal=5444 -->
## Functions

Functions


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should write data to the channel.

               •      wait for ack (F) —

            wait for ack specifies whether this endpoint waits until a reader endpoint acknowledges
             receiving the message before writing the next element. The default is FALSE.

               •      element —

           element specifies the data to write to the channel.

                     •      MessageAckBase.lvclass —


               •       size (unlimited) —

             size specifies the maximum number of elements that can be buffered in the channel. The default
                is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
           endpoint ignores the size input.

               •      actual time —

            actual time returns the actual time when the endpoint wrote data to the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •       id —

             id returns an integer that identifies this message within the channel. Other endpoints use this
             integer to cancel or acknowledge the message within the channel.


5444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5445 ordinal=5445 -->
## Functions

Functions

WriteWrite WithWith AbortAbort

Writes an element to a Messenger channel or signals the channel to abort. The
endpoint waits if the channel is full. This endpoint is the same as the Write endpoint
except that it has an abort input and an aborted? output. You can use the abort
capability of the Messenger channel to close a channel abruptly, ignoring any data left
in the channel buffer. You must use this endpoint together with the Read With Abort
endpoint.


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to
    the channel. The default value is -1, which means there is no time limit.

   •      wait for ack (F) —

    wait for ack specifies whether this endpoint waits until a reader endpoint acknowledges
     receiving the message before writing the next element. The default is FALSE.

   •      element —

    element specifies the data to write to the channel.

         •      MessageAckBase.lvclass —


   •      abort (F) —

    abort specifies whether to abort this channel. The default is FALSE. If abort is TRUE, this
    endpoint marks the channel as closed and ignores further calls to read. Meanwhile, the
    aborted? output returns TRUE on the next call of this endpoint.

   •       size (unlimited) —


                                                    © National Instruments 5445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5446 ordinal=5446 -->
## Functions

Functions


             size specifies the maximum number of elements that can be buffered in the channel. The default
                is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
           endpoint ignores the size input.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •       id —

             id returns an integer that identifies this message within the channel. Other endpoints use this
             integer to cancel or acknowledge the message within the channel.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the reader endpoints connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.


       WriteWrite AckAck

       Writes an acknowledgement to a Messenger channel that the message with the given
        id has been read.

      You can drop this endpoint on the block diagram by right-clicking a terminal or a wire
      and selecting Create»Channel Writer»Messenger»Write Ack.


      Inputs/Outputs

               •       id —

             id specifies the identification information of the message.


5446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5447 ordinal=5447 -->
## Functions

Functions

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.


Related Information

Read

ReadRead

Waits to read an element from a Messenger channel.


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
    channel. The default value is -1, which means there is no time limit.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      ack id (0) —

    ack id specifies the ID number of a message to be acknowledged. This input allows the endpoint
    to acknowledge receiving the previous message. Use this input as an alternative to the Write Ack
    endpoint to enable acknowledgement in the channel. You can use Write Ack on every iteration
     after reading a message, or you can use this input so that the reader endpoint both
    acknowledges the previous message and reads the next message. The default is 0.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses.

   •      element —


                                                    © National Instruments 5447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5448 ordinal=5448 -->
## Functions

Functions


           element returns the data to read from the channel.

                     •      MessageAckBase.lvclass —


               •      remaining —

           remaining returns the number of elements that remain in the channel after this read operation.


     ReadRead ScheduledScheduled

      Reads an element from a Messenger channel at a scheduled time. The endpoint waits
           if no element is available in the channel at the scheduled time.


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should read data from the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      ack id (0) —

           ack id specifies the ID number of a message to be acknowledged. This input allows the endpoint
             to acknowledge receiving the previous message. Use this input as an alternative to the Write Ack
           endpoint to enable acknowledgement in the channel. You can use Write Ack on every iteration
              after reading a message, or you can use this input so that the reader endpoint both
           acknowledges the previous message and reads the next message. The default is 0.

               •      actual time —

            actual time returns the actual time when the endpoint read data from the channel.


5448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5449 ordinal=5449 -->
## Functions

Functions

   •      element —

    element returns the data to read from the channel.

         •      MessageAckBase.lvclass —


   •      remaining —

    remaining returns the number of elements that remain in the channel after this read operation.


ReadRead WithWith AbortAbort

Reads an element from a Messenger channel or signals the channel to abort. This
endpoint is the same as the Read endpoint except that it has an abort input and an
aborted? output. You can use the abort capability of the Messenger channel to close a
channel abruptly, ignoring any data left in the channel buffer. You must use this
endpoint together with the Write With Abort endpoint.


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
    channel. The default value is -1, which means there is no time limit.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      ack id (0) —

    ack id specifies the ID number of a message to be acknowledged. This input allows the endpoint
    to acknowledge receiving the previous message. Use this input as an alternative to the Write Ack
    endpoint to enable acknowledgement in the channel. You can use Write Ack on every iteration


                                                    © National Instruments 5449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5450 ordinal=5450 -->
## Functions

Functions


              after reading a message, or you can use this input so that the reader endpoint both
           acknowledges the previous message and reads the next message. The default is 0.

               •      abort (F) —

            abort specifies whether to abort this channel. The default is FALSE. If abort is TRUE, this
           endpoint marks the channel as closed and ignores further calls to read. Meanwhile, the
           aborted? output returns TRUE on the next call of this endpoint.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses.

               •      element —

           element returns the data to read from the channel.

                     •      MessageAckBase.lvclass —


               •      remaining —

           remaining returns the number of elements that remain in the channel after this read operation.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the writer endpoint connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.


     ReadRead AckAck

       Waits for an acknowledgement from a Messenger channel. If no acknowledgement
      from the channel, this endpoint waits until the acknowledgement is available.

      You can drop this endpoint on the block diagram by right-clicking a Messenger channel
       terminal or wire and selecting Create»Channel Reader»Messenger»Read Ack.


5450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5451 ordinal=5451 -->
## Functions

Functions


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to wait for acknowledgment
    from a message. The default value is -1, which means there is no time limit.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      ack id (0) —

    ack id specifies the ID number of a message to be acknowledged. The default is 0, which means
    the endpoint waits for any message to be acknowledged. If ack id is not 0, the endpoint waits for
    the acknowledgment from the message with the specified ID.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses.


Related Information

Write Ack

ReadRead AckAck WithWith AbortAbort

Waits for an acknowledgement from a Messenger channel or signals the channel to
abort. This endpoint is the same as the Read Ack endpoint except that it has an abort
input and an aborted? output. You can use the abort capability of the Messenger
channel to close a channel abruptly, ignoring any data left in the channel buffer. You
must use this endpoint together with the Write With Abort endpoint.

You can drop this endpoint on the block diagram by right-clicking a Messenger channel
terminal or wire and selecting Create»Channel Reader»Messenger»Read Ack With
Abort.


                                                    © National Instruments 5451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5452 ordinal=5452 -->
## Functions

Functions


      Inputs/Outputs

               •      timeout in ms (-1) —

           timeout in ms is the time, in milliseconds, that this endpoint has to wait for acknowledgment
           from a message. The default value is -1, which means there is no time limit.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      ack id (0) —

           ack id specifies the ID number of a message to be acknowledged. The default is 0, which means
            the endpoint waits for any message to be acknowledged. If ack id is not 0, the endpoint waits for
            the acknowledgment from the message with the specified ID.

               •      abort (F) —

            abort specifies whether to abort this channel. The default is FALSE. If abort is TRUE, this
           endpoint marks the channel as closed and ignores further calls to read. Meanwhile, the
           aborted? output returns TRUE on the next call of this endpoint.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the writer endpoint connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.


      Related Information

       Write Ack


5452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5453 ordinal=5453 -->
## Functions

Functions

Read Ack

AccumulatorAccumulator TagTag

Use the Accumulator Tag channel to share a single value among multiple writers and
readers. Sharing the value is similar to sharing a global or network shared variable.
Each time a writer endpoint writes a value to the channel, the channel adds the value
to the existing value. Reader endpoints can optionally clear the value when they
retrieve the current sum.

      Note Accumulator Tag channels support only numeric data types as a
        transmission data type.

WriteWrite

Adds a value to an Accumulator Tag channel.


Inputs/Outputs

   •      element —

    element specifies the data to add to the channel.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.


WriteWrite ScheduledScheduled

Adds a value to an Accumulator Tag channel at a scheduled time. The endpoint waits
until the scheduled time.


                                                    © National Instruments 5453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5454 ordinal=5454 -->
## Functions

Functions


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should write data to the channel.

               •      element —

           element specifies the data to add to the channel.

               •      actual time —

            actual time returns the actual time when the endpoint wrote data to the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.


       WriteWrite WithWith AbortAbort

      Adds a value to an Accumulator Tag channel or signals the channel to abort. This
      endpoint is the same as the Write endpoint except that it has an abort input and an
      aborted? output. You can use the abort capability of the Accumulator Tag channel to
       close a channel abruptly, ignoring any data left in the channel buffer. You must use this
      endpoint together with the Read With Abort endpoint.


      Inputs/Outputs

               •      element —

           element specifies the data to add to the channel.

               •      abort —


5454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5455 ordinal=5455 -->
## Functions

Functions


    abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
    as closed and ignores further calls to write. Meanwhile, the aborted? output returns TRUE on the
    next call of this endpoint.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.

   •      aborted? —

    aborted? returns TRUE if abort occurred on this endpoint or the reader endpoints connected to
    the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
    aborted? TRUE again.


ReadRead

Reads the sum of values from an Accumulator Tag channel and optionally clears the
value after the endpoint retrieves the current sum.


Inputs/Outputs

   •       clear (T) —

     clear specifies whether to clear the accumulator or not. The default is TRUE.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      average (F) —

    average specifies whether to read the average of the elements from the channel or not. The
     default is FALSE.

   •      element —


                                                    © National Instruments 5455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5456 ordinal=5456 -->
## Functions

Functions


           element returns the data that this endpoint reads from the channel if average is FALSE. If
           average is TRUE, this output returns the average of the data from the channel.

               •      count —

           count returns the number of times that the value of the channel has been updated since the last
           time the channel was cleared. This output returns its value even if the channel has aborted.


     ReadRead ScheduledScheduled

      Reads the sum of values from an Accumulator Tag channel at a scheduled time and
       optionally clears the value when the endpoint retrieves the current sum.


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should read data from the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      average (F) —

           average specifies whether to read the average of the elements from the channel or not. The
             default is FALSE.

               •       clear (T) —

             clear specifies whether to clear the accumulator or not. The default is TRUE.

               •      actual time —

            actual time returns the actual time when the endpoint read data from the channel.


5456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5457 ordinal=5457 -->
## Functions

Functions

   •      element —

    element returns the data that this endpoint reads from the channel if average is FALSE. If
    average is TRUE, this output returns the average of the data from the channel.

   •      count —

    count returns the number of times that the value of the channel has been updated since the last
    time the channel was cleared. This output returns its value even if the channel has aborted.


ReadRead WithWith AbortAbort

Reads the value from an Accumulator Tag channel, optionally clears the accumulator,
and optionally signals the channel to abort. This endpoint is the same as the Read
endpoint except that it has an abort input and an aborted? output. You can use the
abort capability of the Accumulator Tag channel to close a channel abruptly, ignoring
any data left in the channel buffer. You must use this endpoint together with the Write
With Abort endpoint.


Inputs/Outputs

   •       clear (T) —

     clear specifies whether to clear the accumulator or not. The default is TRUE.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      average (F) —

    average specifies whether to read the average of the elements from the channel or not. The
     default is FALSE.

   •      abort —


                                                    © National Instruments 5457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5458 ordinal=5458 -->
## Functions

Functions


            abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
            as closed and ignores further calls to read. Meanwhile, the aborted? output returns TRUE on the
            next call of this endpoint.

               •      element —

           element returns the data that this endpoint reads from the channel if average is FALSE. If
           average is TRUE, this output returns the average of the data from the channel.

               •      count —

           count returns the number of times that the value of the channel has been updated since the last
           time the channel was cleared. This output returns its value even if the channel has aborted.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the writer endpoint connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.

     EventEvent MessengerMessenger

      Use the Event Messenger channel to transfer data from multiple writers to one or more
      Event structures. Each write operation to the channel triggers an event. The Event
      Messenger channel allows the channel syntax to combine with the event syntax that
       controls your user interface events and generated events.

       WriteWrite

       Writes a value to an Event Messenger channel so that the value can be read by one or
      more Event structures. This endpoint waits if the channel is full.

      You can drop this endpoint on the block diagram by right-clicking a terminal or a wire
      and selecting Create»Channel Writer»Event Messenger»Write.


5458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5459 ordinal=5459 -->
## Functions

Functions


Inputs/Outputs

   •      element valid? (T) —

    element valid? specifies whether to record or ignore the element. If TRUE, the endpoint records
    that the element is good data. If FALSE, the endpoint ignores the value of element and records
    the default value of the transmission data type. The element valid? flag is available when the
    event is received by the Event structure. The endpoint does nothing if both element valid? and
     last element? are FALSE. The default is TRUE.

   •      element —

    element specifies the data to write to the channel. This endpoint ignores the data if element
     valid? is FALSE or if abort is TRUE.

   •       last element? (F) —

     last element? specifies whether this is the last element that the endpoint writes to the channel.
    The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
    to write. This output returns FALSE if abort is TRUE.

   •      abort (F) —

    abort specifies whether to abort this channel. The default is FALSE. If abort is TRUE, this
    endpoint marks the channel as closed, ignores further calls to write, flushes previous events,
    and fires a single additional event to notify the Event structure that the channel has been
    aborted.

   •      high priority? (F) —

    high priority? specifies whether to add the element to the front of the queue. The default is
    FALSE.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.

   •     done? —


                                                    © National Instruments 5459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5460 ordinal=5460 -->
## Functions

Functions


          done? returns TRUE if the endpoint has written the last element or if any endpoint has aborted
            the channel.


      Related Information

      Read Event Registration

      Read Multiple Event Registration

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Channels\Event Messenger\Channel - Event
        Messenger.lvproj

     ReadRead EventEvent RegistrationRegistration

      Reads an event registration refnum for an Event Messenger channel.

      You can drop this endpoint on the block diagram by right-clicking an Event Messenger
      channel terminal or wire and selecting Create»Channel Reader»Event
      Messenger»Read Event Registration.


      Inputs/Outputs

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      event registration refnum —

           event registration refnum returns the event registration refnum that this endpoint reads from
            the channel. You must wire this output to the dynamic event terminal of an Event structure to


5460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5461 ordinal=5461 -->
## Functions

Functions


    receive events from the channel.


Unlike the reader endpoints of other channel templates, this reader endpoint must be
placed outside the While Loop and can execute only once.

Use one Event structure to handle events whenever possible. Use the Build Array or
Bundle functions to combine multiple event registration refnums for a single Event
structure.

Do not fork the event registration refnums to multiple Event structures. Doing so
creates undefined behavior that may result in race conditions or deadlocks in your
application.

Related Information

Write

Caveats and Recommendations when Using Events in LabVIEW

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Channels\Event Messenger\Channel - Event
   Messenger.lvproj

ReadRead MultipleMultiple EventEvent RegistrationRegistration

Reads multiple event registration refnums for an Event Messenger channel and makes
the refnums available to one or more Event structures.

You can drop this endpoint on the block diagram by right-clicking an Event Messenger
channel terminal or wire and selecting Create»Channel Reader»Event
Messenger»Read Multiple Event Registration.


                                                    © National Instruments 5461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5462 ordinal=5462 -->
## Functions

Functions


      Inputs/Outputs

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •     number of event structures —

          number of event structures specifies the number of Event structures that read event
              registration information from this endpoint. number of event structures must match the
          number of Event structures that read from this endpoint to avoid undefined errors.

               •      event registration refnums —

           event registration refnums returns an array of event registration refnums for an Event
           Messenger channel.

          The number of elements in the array equals number of event structures. Each refnum in the
             array is a unique refnum intended for one specific Event structure that reads from this endpoint,
          and each Event structure triggers on all of the events from the channel.


       Unlike the reader endpoints of other channel templates, this reader endpoint must be
       placed outside the While Loop and can execute only once.

      Use one Event structure to handle events whenever possible. Use the Build Array or
      Bundle functions to combine multiple event registration refnums for a single Event
        structure.

      To allow multiple Event structures to read event registration refnums from this
       endpoint, you must use the Index Array function to index the event registration
      refnums and wire each refnum to the dynamic event terminal of each Event structure
      so that each Event structure receives its own copy of the events from the channel.

     Do not fork the event registration refnums to multiple Event structures. Doing so
       creates undefined behavior that may result in race conditions or deadlocks in your
       application.


5462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5463 ordinal=5463 -->
## Functions

Functions

Related Information

Write

Caveats and Recommendations when Using Events in LabVIEW

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Channels\Event Messenger\Channel - Event
   Messenger.lvproj

HighHigh SpeedSpeed StreamStream

Use the High Speed Stream channel to transfer data from a single writer to a single
reader in a fast and highly efficient manner. The High Speed Stream channels can
handle complex data transfer scenarios while managing the whole execution process
of parallel loops. The High Speed Stream channel lacks the debug capabilities of the
other Streams.

WriteWrite

Writes an element to a High Speed Stream channel. If the channel is full, this endpoint
waits until space is available or a timeout occurs. You can use this endpoint to signal a
normal stop when the last element is written to the queue or to signal an immediate
stop when abort occurs.


Inputs/Outputs

   •      timeout in ms (-1) —


                                                    © National Instruments 5463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5464 ordinal=5464 -->
## Functions

Functions


           timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to
            the channel. The default value is -1, which means there is no time limit.

               •       size (unlimited) —

             size specifies the maximum number of elements that can be buffered in the channel. The default
                is unlimited. The channel size is initialized on the first call to the writer endpoint, after which the
           endpoint ignores the size input.

               •      element —

           element specifies the data to write to the channel.

               •      element valid? (T) —

           element valid? specifies whether the element is valid. If TRUE, the endpoint records the
           element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
            nothing if both element valid? and last element? are FALSE. The default is TRUE.

               •       last element? (F) —

              last element? specifies whether this is the last element that the endpoint writes to the channel.
          The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
             to write. The reader endpoint can continue reading data until the last element? output of the
            reader endpoint returns TRUE.

               •      abort status (no abort) —

            abort status specifies the abort status of this endpoint. The default is no abort.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
           endpoint writes the data specified in element to the channel.

               •     done? —

          done? returns TRUE if the endpoint has written the last element or if the channel aborts on
             either endpoint. This output returns FALSE if a timeout occurs.


5464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5465 ordinal=5465 -->
## Functions

Functions

ReadRead

Reads an element from a High Speed Stream channel.


Inputs/Outputs

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      abort before read? (F) —

    abort before read? specifies whether to abort before reading the element from the channel. The
     default is FALSE.

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
    channel. The default value is -1, which means there is no time limit.

   •      abort signal —

    abort signal is an object for aborting a High Speed Stream channel after the read operation. You
    can use this object's Abort method to stop the channel. Right click the abort signal terminal and
     select Create Abort Node to generate the Abort function. Refer to the labview\examples\
   Channels\High Speed Stream\Channel - High Speed Stream.lvproj for
    examples of using the Abort function.

   •      element —

    element returns the data that this endpoint reads from the channel. This output returns the
     default value of the transmission data type if a timeout occurs or if the channel aborts.

   •      element valid? —

    element valid? returns TRUE if the element was read successfully. This output returns FALSE if a
    timeout occurs or if the channel aborts.


                                                    © National Instruments 5465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5466 ordinal=5466 -->
## Functions

Functions

               •     done? —

          done? returns TRUE if the endpoint has read the last element or if the channel aborts on either
            endpoint. This output returns FALSE if a timeout occurs.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses. If timed out?
                is TRUE, element valid? will be FALSE.


       ReplicateReplicate

        Splits a High Speed Stream channel into two High Speed Stream channels so that each
       of the readers of the channels receives a separate copy of the data written into the
        original channel.


      Inputs/Outputs

               •      high speed stream —

            high speed stream is the channel wire that connects this endpoint to a writer endpoint and
               splits into two outgoing channels.

               •      independent aborts? (F) —

           independent aborts? specifies whether signaling one of the outgoing channels to abort only
            causes that one outgoing channel to abort. The default is FALSE, which means if one of the
            outgoing channels aborts, the other will also abort.

               •      copy 1 size (unlimited) —

           copy 1 size specifies the number of remaining elements to write to the first outgoing channel.
          The default is unlimited.

               •      copy 2 size (unlimited) —


5466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5467 ordinal=5467 -->
## Functions

Functions


    copy 2 size specifies the number of remaining elements to write to the second outgoing channel.
    The default is unlimited.

   •      high speed stream copy 1 —

    high speed stream copy 1 is the first outgoing channel wire that connects this endpoint to a
    reader endpoint.

   •      high speed stream copy 2 —

    high speed stream copy 2 is the second outgoing channel wire that connects this endpoint to a
    reader endpoint.

LossyLossy StreamStream

Use the Lossy Stream channel to communicate homogeneous data from a single writer
to a single reader. If the channel is already full when the writer attempts to write a new
data, the writer does not wait for space to be available. Instead, the channel optionally
either drops the oldest data element in the channel to make room for this new data or
discards this new data. You can use the Lossy Stream readers to identify data gaps.

WriteWrite

Writes an element to a Lossy Stream channel. If the channel is full, this endpoint either
drops the oldest element in the channel to make room for this new element or
discards this new element.


Inputs/Outputs

   •       lossy behavior (drop oldest) —

    lossy behavior specifies how this endpoint writes data to a Lossy Stream channel when an


                                                    © National Instruments 5467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5468 ordinal=5468 -->
## Functions

Functions


           element comes in. The default is drop oldest element.

               •      element valid? (T) —

           element valid? specifies whether the element is valid. If TRUE, the endpoint records the
           element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
            nothing if both element valid? and last element? are FALSE. The default is TRUE.

               •      element —

           element specifies the data to write to the channel.

               •       last element? (F) —

              last element? specifies whether this is the last element that the endpoint writes to the channel.
          The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
             to write. The reader endpoint can continue reading data until the last element? output of the
            reader endpoint returns TRUE.

               •       size (1) —

             size specifies the number of elements that the endpoint will write to the channel. The default is
               1.

               •      data lost? —

           data lost? returns TRUE if the channel was full when the endpoint performed this write
             operation.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.


       WriteWrite ScheduledScheduled

       Writes an element to a Lossy Stream channel at a scheduled time. The endpoint waits


5468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5469 ordinal=5469 -->
## Functions

Functions

until the scheduled time and continues waiting if the channel is full at the scheduled
time.


Inputs/Outputs

   •      scheduled time —

    scheduled time specifies the time when the endpoint should write data to the channel.

   •      element valid? (T) —

    element valid? specifies whether the element is valid. If TRUE, the endpoint records the
    element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
    nothing if both element valid? and last element? are FALSE. The default is TRUE.

   •      element —

    element specifies the data to write to the channel.

   •       last element? (F) —

     last element? specifies whether this is the last element that the endpoint writes to the channel.
    The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
    to write. The reader endpoint can continue reading data until the last element? output of the
    reader endpoint returns TRUE.

   •       lossy behavior (drop oldest) —

    lossy behavior specifies how this endpoint writes data to a Lossy Stream channel when an
    element comes in. The default is drop oldest element.

   •       size (1) —

     size specifies the number of elements that the endpoint will write to the channel. The default is
     1.

   •      actual time —


                                                    © National Instruments 5469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5470 ordinal=5470 -->
## Functions

Functions


            actual time returns the actual time when the endpoint wrote data to the channel.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •      data lost? —

           data lost? returns TRUE if the channel was full when the endpoint performed this write
             operation.


       WriteWrite WithWith AbortAbort

       Writes an element to a Lossy Stream channel or signals the channel to abort. The
      endpoint waits if the channel is full. This endpoint is the same as the Write endpoint
       except that it has an abort input and an aborted? output. You can use the abort
       capability of the Lossy Stream channel to close a channel abruptly, ignoring any data
         left in the channel buffer. You must use this endpoint together with the Read With
       Abort endpoint.


      Inputs/Outputs

               •       lossy behavior (drop oldest) —

             lossy behavior specifies how this endpoint writes data to a Lossy Stream channel when an
           element comes in. The default is drop oldest element.

               •      element valid? (T) —

5470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5471 ordinal=5471 -->
## Functions

Functions


  element valid? specifies whether the element is valid. If TRUE, the endpoint records the
  element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
  nothing if both element valid? and last element? are FALSE. The default is TRUE.

•      element —

  element specifies the data to write to the channel.

•       last element? (F) —

  last element? specifies whether this is the last element that the endpoint writes to the channel.
  The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
  to write. The reader endpoint can continue reading data until the last element? output of the
  reader endpoint returns TRUE.

•      abort —

  abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
  as closed and ignores further calls to write. Meanwhile, the aborted? output returns TRUE on the
  next call of this endpoint.

•       size (1) —

  size specifies the number of elements that the endpoint will write to the channel. The default is
   1.

•      data lost? —

  data lost? returns TRUE if the channel was full when the endpoint performed this write
  operation.

•      count —

  count returns the number of elements in the channel after this endpoint updates the channel.
  Use this output to monitor the relative writing and reading speed of the channel endpoints and
  make adjustments, if necessary.

•      channel —

  channel is the channel wire that connects this endpoint to a reader endpoint.

•      aborted? —


                                                   © National Instruments 5471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5472 ordinal=5472 -->
## Functions

Functions


           aborted? returns TRUE if abort occurred on this endpoint or the reader endpoints connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.


     ReadRead

      Reads an element from a Lossy Stream channel.


      Inputs/Outputs

               •      timeout in ms (-1) —

           timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
            channel. The default value is -1, which means there is no time limit.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
           endpoint reads the data specified in element from the channel. If timed out? is TRUE, element
             valid? and last element? will be FALSE.

               •      gap? —

           gap? returns TRUE if any data was lost because an endpoint attempted to write to a full channel
           between the previous read operation and this one.

               •      element valid? —

           element valid? returns TRUE if the element was read successfully. This output returns FALSE if a
            timeout occurs, if the channel closes without a valid last element, or if the channel aborts.


5472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5473 ordinal=5473 -->
## Functions

Functions

   •      element —

    element returns the data that this endpoint reads from the channel. This output returns the
     default value of the transmission data type if a timeout occurs, if the channel closes without a
     valid last element, or if the channel aborts.

   •       last element? —

     last element? returns whether this is the last element that the endpoint reads from the channel.
     last element? can be TRUE even if element valid? is FALSE, which means that the last element
    was already written to the channel during the previous iteration or the channel closes without a
     valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

   •      count —

    count returns the number of elements in the channel after this endpoint updates the channel.
    Use this output to monitor the relative writing and reading speed of the channel endpoints and
   make adjustments, if necessary.


ReadRead ScheduledScheduled

Reads an element from a Lossy Stream channel at a scheduled time. The endpoint
waits if no element is available in the channel at the scheduled time.


Inputs/Outputs

   •      scheduled time —

    scheduled time specifies the time when the endpoint should read data from the channel.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      actual time —


                                                    © National Instruments 5473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5474 ordinal=5474 -->
## Functions

Functions


            actual time returns the actual time when the endpoint read data from the channel.

               •      element valid? —

           element valid? returns TRUE if the element was read successfully. This output returns FALSE if
            the channel closes without a valid last element or if the channel aborts.

               •      element —

           element returns the data that this endpoint reads from the channel. This output returns the
             default value of the transmission data type if a timeout occurs, if the channel closes without a
              valid last element, or if the channel aborts.

               •       last element? —

              last element? returns whether this is the last element that the endpoint reads from the channel.
              last element? can be TRUE even if element valid? is FALSE, which means that the last element
          was already written to the channel during the previous iteration or the channel closes without a
              valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

               •      gap? —

           gap? returns TRUE if any data was lost because an endpoint attempted to write to a full channel
           between the previous read operation and this one.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.


     ReadRead WithWith AbortAbort

      Reads an element from a Lossy Stream channel or signals the channel to abort. This
      endpoint is the same as the Read endpoint except that it has an abort input and an
      aborted? output. You can use the abort capability of the Lossy Stream channel to close
      a channel abruptly, ignoring any data left in the channel buffer. You must use this
      endpoint together with the Write With Abort endpoint.


5474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5475 ordinal=5475 -->
## Functions

Functions


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
    channel. The default value is -1, which means there is no time limit.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      abort —

    abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
    as closed and ignores further calls to read. Meanwhile, the aborted? output returns TRUE on the
    next call of this endpoint.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
    endpoint reads the data specified in element from the channel. This output returns FALSE if
    aborted? is TRUE. If timed out? is TRUE, element valid? and last element? will be FALSE.

   •      gap? —

    gap? returns TRUE if any data was lost because an endpoint attempted to write to a full channel
    between the previous read operation and this one.

   •      element valid? —

    element valid? returns TRUE if the element was read successfully. This output returns FALSE if a
    timeout occurs, if the channel closes without a valid last element, or if the channel aborts.

   •      element —

    element returns the data that this endpoint reads from the channel. This output returns the
     default value of the transmission data type if a timeout occurs, if the channel closes without a


                                                    © National Instruments 5475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5476 ordinal=5476 -->
## Functions

Functions


              valid last element, or if the channel aborts.

               •       last element? —

              last element? returns whether this is the last element that the endpoint reads from the channel.
              last element? can be TRUE even if element valid? is FALSE, which means that the last element
          was already written to the channel during the previous iteration or the channel closes without a
              valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the writer endpoint connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.

               •      count —

           count returns the number of elements in the channel after this endpoint updates the channel.
           Use this output to monitor the relative writing and reading speed of the channel endpoints and
          make adjustments, if necessary.

    OneOne ElementElement StreamStream

      Use the One Element Stream channel exactly the way you use a Stream channel with
        size equal to one. Allowing only one element in the buffer makes One Element Stream
       channels more optimized. They execute faster and save resources compared with
      Stream channels.

       WriteWrite

       Writes an element to a One Element Stream channel. The endpoint waits if the channel
         is full.


5476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5477 ordinal=5477 -->
## Functions

Functions

Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to
    the channel. The default value is -1, which means there is no time limit.

   •      element valid? (T) —

    element valid? specifies whether the element is valid. If TRUE, the endpoint records the
    element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
    nothing if both element valid? and last element? are FALSE. The default is TRUE.

   •      element —

    element specifies the data to write to the channel.

   •       last element? (F) —

     last element? specifies whether this is the last element that the endpoint writes to the channel.
    The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
    to write. The reader endpoint can continue reading data until the last element? output of the
    reader endpoint returns TRUE.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
    endpoint writes the data specified in element to the channel.

   •      channel —

    channel is the channel wire that connects this endpoint to a reader endpoint.


WriteWrite ScheduledScheduled

Writes an element to a One Element Stream channel at a scheduled time. The
endpoint waits until the scheduled time and continues waiting if the channel is full at
the scheduled time.

You can drop this endpoint on the block diagram by right-clicking a terminal or a wire
and selecting Create»Channel Writer»One Element Stream»Write Scheduled.


                                                    © National Instruments 5477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5478 ordinal=5478 -->
## Functions

Functions


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should write data to the channel.

               •      element valid? (T) —

           element valid? specifies whether the element is valid. If TRUE, the endpoint records the
           element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
            nothing if both element valid? and last element? are FALSE. The default is TRUE.

               •      element —

           element specifies the data to write to the channel.

               •       last element? (F) —

              last element? specifies whether this is the last element that the endpoint writes to the channel.
          The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
             to write. The reader endpoint can continue reading data until the last element? output of the
            reader endpoint returns TRUE.

               •      actual time —

            actual time returns the actual time when the endpoint wrote data to the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.


      Related Information

      Read Scheduled


5478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5479 ordinal=5479 -->
## Functions

Functions

WriteWrite WithWith AbortAbort

Writes an element to a One Element Stream channel or signals the channel to abort.
The endpoint waits if the channel is full. This endpoint is the same as the Write
endpoint except that it has an abort input and an aborted? output. You can use the
abort capability of the One Element Stream channel to close a channel abruptly,
ignoring any data left in the channel buffer. You must use this endpoint together with
the Read With Abort endpoint.

You can drop this endpoint on the block diagram by right-clicking a terminal or a wire
and selecting Create»Channel Writer»One Element Stream»Write With Abort.


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to
    the channel. The default value is -1, which means there is no time limit.

   •      element valid? (T) —

    element valid? specifies whether the element is valid. If TRUE, the endpoint records the
    element valid? flag. If FALSE, the endpoint ignores the value of element. The endpoint does
    nothing if both element valid? and last element? are FALSE. The default is TRUE.

   •      element —

    element specifies the data to write to the channel.

   •       last element? (F) —

     last element? specifies whether this is the last element that the endpoint writes to the channel.
    The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls
    to write. The reader endpoint can continue reading data until the last element? output of the
    reader endpoint returns TRUE.


                                                    © National Instruments 5479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5480 ordinal=5480 -->
## Functions

Functions

               •      abort —

            abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
            as closed and ignores further calls to write. Meanwhile, the aborted? output returns TRUE on the
            next call of this endpoint.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
           endpoint writes the data specified in element to the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a reader endpoint.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the reader endpoints connected to
            the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
           aborted? TRUE again.


      Related Information

      Read With Abort

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Channels\One Element Stream\Channel -
        One Element Stream.lvproj

     ReadRead

       Waits to read data from a One Element Stream channel.

      You can drop this endpoint on the block diagram by right-clicking a One Element
      Stream channel terminal or wire and selecting Create»Channel Reader»One Element
      Stream»Read.


5480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5481 ordinal=5481 -->
## Functions

Functions


Inputs/Outputs

   •      timeout in ms (-1) —

    timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
    channel. The default value is -1, which means there is no time limit.

   •      channel —

    channel is the channel wire that connects this endpoint to a writer endpoint.

   •      timed out? —

    timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
    endpoint reads the data specified in element from the channel. If timed out? is TRUE, element
     valid? and last element? will be FALSE.

   •      element valid? —

    element valid? returns TRUE if the element was read successfully. This output returns FALSE if a
    timeout occurs, if the channel closes without a valid last element, or if the channel aborts.

   •      element —

    element returns the data that this endpoint reads from the channel. This output returns the
     default value of the transmission data type if a timeout occurs, if the channel closes without a
     valid last element, or if the channel aborts.

   •       last element? —

     last element? returns whether this is the last element that the endpoint reads from the channel.
     last element? can be TRUE even if element valid? is FALSE, which means that the last element
    was already written to the channel during the previous iteration or the channel closes without a
     valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.


Related Information

Write

                                                    © National Instruments 5481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5482 ordinal=5482 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Channels\Basics\Channel Basics.lvproj
            • labview\examples\Channels\Replacing The Function At The
        Heart Of An Algorithm At Run Time\Replacing The Function
        At The Heart Of An Algorithm At Run Time.lvproj

     ReadRead ScheduledScheduled

       Waits to read an element from a One Element Stream channel at a scheduled time. The
      endpoint waits if no element is available in the channel at the scheduled time.

      You can drop this endpoint on the block diagram by right-clicking a One Element
      Stream channel terminal or wire and selecting Create»Channel Reader»One Element
      Stream»Read Scheduled.


      Inputs/Outputs

               •      scheduled time —

           scheduled time specifies the time when the endpoint should read data from the channel.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      actual time —

            actual time returns the actual time when the endpoint read data from the channel.

               •      element valid? —

           element valid? returns TRUE if the element was read successfully. This output returns FALSE if


5482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5483 ordinal=5483 -->
## Functions

Functions


    the channel closes without a valid last element or if the channel aborts.

   •      element —

    element returns the data that this endpoint reads from the channel. This output returns the
     default value of the transmission data type if a timeout occurs, if the channel closes without a
     valid last element, or if the channel aborts.

   •       last element? —

     last element? returns whether this is the last element that the endpoint reads from the channel.
     last element? can be TRUE even if element valid? is FALSE, which means that the last element
    was already written to the channel during the previous iteration or the channel closes without a
     valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.


Related Information

Write Scheduled

ReadRead WithWith AbortAbort

Waits to read an element from a One Element Stream channel or signals the channel to
abort. This endpoint is the same as the Read endpoint except that it has an abort input
and an aborted? output. You can use the abort capability of the One Element Stream
channel to close a channel abruptly, ignoring any data left in the channel buffer. You
must use this endpoint together with the Write With Abort endpoint.

You can drop this endpoint on the block diagram by right-clicking a One Element
Stream channel terminal or wire and selecting Create»Channel Reader»One Element
Stream»Read With Abort.


                                                    © National Instruments 5483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5484 ordinal=5484 -->
## Functions

Functions

      Inputs/Outputs

               •      timeout in ms (-1) —

           timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the
            channel. The default value is -1, which means there is no time limit.

               •      channel —

           channel is the channel wire that connects this endpoint to a writer endpoint.

               •      abort —

            abort specifies whether to abort this channel. If abort is TRUE, this endpoint marks the channel
            as closed and ignores further calls to read. Meanwhile, the aborted? output returns TRUE on the
            next call of this endpoint.

               •      timed out? —

           timed out? returns TRUE if the amount of time specified by timeout in ms elapses before the
           endpoint reads the data specified in element from the channel. This output returns FALSE if
           aborted? is TRUE. If timed out? is TRUE, element valid? and last element? will be FALSE.

               •      element valid? —

           element valid? returns TRUE if the element was read successfully. This output returns FALSE if a
            timeout occurs, if the channel closes without a valid last element, or if the channel aborts.

               •      element —

           element returns the data that this endpoint reads from the channel. This output returns the
             default value of the transmission data type if a timeout occurs, if the channel closes without a
              valid last element, or if the channel aborts.

               •       last element? —

              last element? returns whether this is the last element that the endpoint reads from the channel.
              last element? can be TRUE even if element valid? is FALSE, which means that the last element
          was already written to the channel during the previous iteration or the channel closes without a
              valid last element. This output returns FALSE if a timeout occurs or if the channel aborts.

               •      aborted? —

           aborted? returns TRUE if abort occurred on this endpoint or the writer endpoint connected to


5484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5485 ordinal=5485 -->
## Functions

Functions


    the channel. If aborted? is TRUE, further calls to this endpoint will do nothing except returning
    aborted? TRUE again.


Related Information

Write With Abort

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Channels\One Element Stream\Channel -
   One Element Stream.lvproj

ReplicateReplicate

Splits a One Element Stream channel into two One Element channels so that each of
the readers of the channels receives a separate copy of the data written into the
original channel.

You can drop this endpoint on the block diagram by right-clicking a One Element
Stream channel and selecting Insert»Replicate.


Inputs/Outputs

   •     one element stream —

    one element stream is the channel wire that connects this endpoint to a writer endpoint and
     splits into two outgoing channels.

   •      independent aborts? (F) —

    independent aborts? specifies whether signaling one of the outgoing channels to abort only
    causes that one outgoing channel to abort. The default is FALSE, which means if one of the


                                                    © National Instruments 5485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5486 ordinal=5486 -->
## Functions

Functions


            outgoing channels aborts, the other will also abort.

               •     one element stream copy 1 —

          one element stream copy 1 is the first outgoing channel wire that connects this endpoint to a
            reader endpoint.

               •     one element stream copy 2 —

          one element stream copy 2 is the second outgoing channel wire that connects this endpoint to a
            reader endpoint.


      Related Information

     One Element Stream

     ActorActor FrameworkFramework

      Use the Actor Framework VIs to create applications based on the Actor Framework.

      These VIs are a small subset of the complete Actor Framework. Most of the framework
         is not invoked by dropping a subVI. Instead, you create a new child class of
     Actor.lvclass and then override methods in the new class.


         Palette
                     Description
        Object

                    (Filename: Actor Framework.lvlib:Actor.lvclass:Launch Root Actor.vi)

        Launch     Launches an asynchronously running VI that performs tasks and handles messages for
        Root Actor  the Actor. This VI returns a reference to an enqueuer that you can use to send
          VI         messages to the newly launched actor.

                  The Launch Root Actor VI launches the Actor without a caller. Use this VI to launch the


5486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5487 ordinal=5487 -->
## Functions

Functions


Palette            Description
Object

            root actor of the actor tree. Use the Launch Nested Actor VI to launch all other actors.


            (Filename: Actor Framework.lvlib:Actor.lvclass:Launch Nested Actor.vi)

           Launches an asynchronously running VI that performs tasks and handles messages for
            the Nested Actor. Use this VI to launch actors that are dependent on one or more
Launch              calling actors. This VI returns a reference to the enqueuer that you can use to sendNested          messages to the newly launched actor.Actor VI
            This VI requires the Caller Actor in input to call the Nested Actor. This VI will return an
             error if the Caller Actor in has not already been launched itself. Use the Launch Root
            Actor VI for launching an actor without a caller.


Read
            (Filename: Actor Framework.lvlib:Actor.lvclass:Read Caller Enqueuer.vi)Caller
Enqueuer            Returns the reference the actor needs to send messages to its caller.
VI


Read Self   (Filename: Actor Framework.lvlib:Actor.lvclass:Read Self Enqueuer.vi)
Enqueuer
VI          Returns the reference needed for the actor to send messages to itself.


            (Filename: Actor Framework.lvlib:Stop Msg.lvclass:Send Normal Stop.vi)
Send
Normal    Sends a Stop message to an actor, triggering the actor to run its Stop Core method.
Stop VI      This message has normal priority, meaning the actor will process this message after
            processing high- or normal-priority messages that are in the queue already.


            (Filename: Actor Framework.lvlib:Stop Msg.lvclass:Send Emergency Stop.vi)
Send
Emergency Sends an Emergency Stop message to an actor, triggering the actor to shut down as
Stop VI      quickly as possible. This message has critical priority, meaning it will be processed
            before all messages that are already in the queue.


                                                    © National Instruments 5487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5488 ordinal=5488 -->
## Functions

Functions


         Palette                     Description
        Object

                    (Filename: Actor Framework.lvlib:Stop Msg.lvclass:Send Normal or Emergency Stop.vi)       Send
        Normal or                  Sends a Stop message to an actor. The priority of this message is determined by the
        Emergency                     value of the final error code input. If this input is 0, this VI sends the message with
        Stop VI                  normal priority; otherwise, it sends the message with critical priority.


       Read       (Filename: Actor Framework.lvlib:Actor.lvclass:Read Autostop Nested Actor Count.vi)
        Autostop
        Nested     Returns the number of auto-stop nested actors that were launched by an actor but
         Actor      have not yet sent back their Last Ack messages. Use this VI to detect whether all nested
        Count VI    actors have finished working.


                    (Filename: Actor Framework.lvlib:Last Ack.lvclass:Read Actor.vi)       Read Actor
          VI                    Returns the state the actor was in when it shut down.


       Read
                    (Filename: Actor Framework.lvlib:Last Ack.lvclass:Read Caller-To-Actor Enqueuer.vi)          Caller-To-
         Actor                    Returns the reference the caller used to send messages to the actor. Although the
        Enqueuer                     reference is invalid, you can use it to identify which actor shut down.
          VI


                    (Filename: Actor Framework.lvlib:Last Ack.lvclass:Read Error Report.vi)       Read Error
        Report VI                    Returns the error, if any, that caused an actor to shut down.


                    (Filename: Actor Framework.lvlib:Report Error Msg.lvclass:Send Error Report.vi)
       Send Error
        Report VI   Use this VI to send an error to an actor. The error will be handled by the Handle Error VI
                      of the actor. If the error is not handled there, it will cause the actor to stop running.


        Advanced  Use the Advanced VIs with the Actor Framework to implement advanced messaging


5488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5489 ordinal=5489 -->
## Functions

Functions


 Palette             Description
 Object

             techniques.


      Note Refer to the Actor Framework template, available from the Create
        Project dialog box, for a template that demonstrates the basics of the Actor
       Framework. Refer to the Feedback Evaporative Cooler sample project, also
        available from this dialog box, for a sample project that demonstrates an
        application based on the Actor Framework.

LaunchLaunch RootRoot ActorActor VIVI

(Filename: Actor Framework.lvlib:Actor.lvclass:Launch Root Actor.vi)

Launches an asynchronously running VI that performs tasks and handles messages for
the Actor. This VI returns a reference to an enqueuer that you can use to send
messages to the newly launched actor.

The Launch Root Actor VI launches the Actor without a caller. Use this VI to launch the
root actor of the actor tree. Use the Launch Nested Actor VI to launch all other actors.


Inputs/Outputs

   •      Actor —

    Actor specifies the initial state of the actor.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 5489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5490 ordinal=5490 -->
## Functions

Functions

               •     Open Actor Core front panel? (F) —

          Open Actor Core front panel? specifies whether, on launching the actor, the front panel of the
            Actor Core method opens. The default is FALSE. The TRUE setting causes this VI to return an
             error in the run-time engine.

            Set Open Actor Core front panel? to TRUE during code development so you can access the
           Abort button for the VI, which helps if you forget to stop an actor. To open the Actor Core front
            panel of an actor for purposes other than debugging, use the Front Panel:Open method. You can
             also enable Show front panel when called on the Customize Window Appearance dialog box to
             configure this VI to open the Actor Core front panel when you call the actor.

               •     Debug Alias —

          Debug Alias specifies an alias to use to identify the launched actor in trace data captured by the
           Desktop Execution Trace Toolkit.

               •       Actor's Enqueuer —

             Actor's Enqueuer returns a reference to an enqueuer. Use this reference to send messages to the
           newly launched actor.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Refer to the Actor Framework template for more information about the Actor
      Framework. To use the Actor Framework template, click Create Project from the
      LabVIEW start screen and select Actor Framework.

     LaunchLaunch NestedNested ActorActor VIVI

       (Filename: Actor Framework.lvlib:Actor.lvclass:Launch Nested Actor.vi)

      Launches an asynchronously running VI that performs tasks and handles messages for
       the Nested Actor. Use this VI to launch actors that are dependent on one or more
        calling actors. This VI returns a reference to the enqueuer that you can use to send
      messages to the newly launched actor.

       This VI requires the Caller Actor in input to call the Nested Actor. This VI will return an
       error if the Caller Actor in has not already been launched itself. Use the Launch Root

5490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5491 ordinal=5491 -->
## Functions

Functions

Actor VI for launching an actor without a caller.


Inputs/Outputs

   •       Caller Actor in —

     Caller Actor in is the actor that calls Nested Actor. Caller Actor in must already be launched
    before calling Nested Actor, or else this VI will return an error.

   •      Nested Actor —

    Nested Actor is the initial state of the actor you want to launch.

   •      Auto-stop? (T) —

    Auto-stop determines whether Nested Actor stops when the calling actor stops. The default
    value is TRUE. If you set the value of this input to FALSE, you must manually override the Stop
    Core VI on the caller actor to specify stop behavior for Nested Actor.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     Open Actor Core front panel? (F) —

   Open Actor Core front panel? specifies whether, on launching the actor, the front panel of the
    Actor Core method opens. The default is FALSE. The TRUE setting causes this VI to return an
     error in the run-time engine.

    Set Open Actor Core front panel? to TRUE during code development so you can access the
    Abort button for the VI, which helps if you forget to stop an actor. To open the Actor Core front
    panel of an actor for purposes other than debugging, use the Front Panel:Open method. You can
    also enable Show front panel when called on the Customize Window Appearance dialog box to
    configure this VI to open the Actor Core front panel when you call the actor.

   •     Debug Alias —


                                                    © National Instruments 5491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5492 ordinal=5492 -->
## Functions

Functions


          Debug Alias specifies an alias to use to identify the launched actor in trace data captured by the
           Desktop Execution Trace Toolkit.

               •       Caller Actor out —

             Caller Actor out returns the modified caller actor. The caller actor has a record of Nested Actor.
          The caller actor uses the record of Nested Actor to auto-stop the Nested Actor if Auto-stop? is
             set to true.

               •      Nested Actor's Enqueuer —

           Nested Actor's Enqueuer returns the reference to the enqueuer. Use this reference to send
           messages to the newly launched actor.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Refer to the Actor Framework template for more information about the Actor
      Framework. To use the Actor Framework template, click Create Project from the
      LabVIEW start screen and select Actor Framework.

     ReadRead CallerCaller EnqueuerEnqueuer VIVI

       (Filename: Actor Framework.lvlib:Actor.lvclass:Read Caller Enqueuer.vi)

       Returns the reference the actor needs to send messages to its caller.


      Inputs/Outputs

               •      Actor —

            Actor specifies the actor.

               •       Caller Enqueuer —


5492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5493 ordinal=5493 -->
## Functions

Functions


     Caller Enqueuer returns the reference the actor needs to send messages to its caller.

ReadRead SelfSelf EnqueuerEnqueuer VIVI

(Filename: Actor Framework.lvlib:Actor.lvclass:Read Self Enqueuer.vi)

Returns the reference needed for the actor to send messages to itself.


Inputs/Outputs

   •      Actor —

    Actor specifies the actor.

   •       Self Enqueuer —

     Self Enqueuer returns the reference needed for the actor to send messages to itself.

SendSend NormalNormal StopStop VIVI

(Filename: Actor Framework.lvlib:Stop Msg.lvclass:Send Normal Stop.vi)

Sends a Stop message to an actor, triggering the actor to run its Stop Core method.
This message has normal priority, meaning the actor will process this message after
processing high- or normal-priority messages that are in the queue already.


Inputs/Outputs

   •      Message Enqueuer —


                                                    © National Instruments 5493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5494 ordinal=5494 -->
## Functions

Functions


           Message Enqueuer specifies the reference needed to send messages to the actor.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     SendSend EmergencyEmergency StopStop VIVI

       (Filename: Actor Framework.lvlib:Stop Msg.lvclass:Send Emergency Stop.vi)

      Sends an Emergency Stop message to an actor, triggering the actor to shut down as
       quickly as possible. This message has critical priority, meaning it will be processed
       before all messages that are already in the queue.


      Inputs/Outputs

               •      Message Enqueuer —

           Message Enqueuer specifies the reference needed to send messages to the actor.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The message this VI sends is one of only two critical-priority messages in the Actor


5494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5495 ordinal=5495 -->
## Functions

Functions

Framework, the other being Last Ack. National Instruments does not provide a way to
send any other message with critical priority.

SendSend NormalNormal oror EmergencyEmergency StopStop VIVI

(Filename: Actor Framework.lvlib:Stop Msg.lvclass:Send Normal or Emergency Stop.vi)

Sends a Stop message to an actor. The priority of this message is determined by the
value of the final error code input. If this input is 0, this VI sends the message with
normal priority; otherwise, it sends the message with critical priority.


Inputs/Outputs

   •      Message Enqueuer —

    Message Enqueuer specifies the reference needed to send messages to the actor.

   •       final error code —

     final error code specifies the error code that determines whether this VI sends a normal- or
     critical-priority message. A value of 0 sends a normal-priority message. Any other value sends a
     critical-priority message.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The normal-priority message is the same as the one sent by the Send Normal Stop
method.

The critical-priority message is the same as the one sent by the Send Emergency Stop

                                                    © National Instruments 5495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5496 ordinal=5496 -->
## Functions

Functions

      method.

     ReadRead AutostopAutostop NestedNested ActorActor CountCount VIVI

       (Filename: Actor Framework.lvlib:Actor.lvclass:Read Autostop Nested Actor Count.vi)

       Returns the number of auto-stop nested actors that were launched by an actor but
      have not yet sent back their Last Ack messages. Use this VI to detect whether all nested
       actors have finished working.

           Note Nested actors launched with Auto-stop? set to FALSE will not be
              included in this count; actors are responsible for counting those actors
              themselves.


      Inputs/Outputs

               •      Actor in —

            Actor in specifies the actor.

               •      Count —

           Count returns the number of auto-stop nested actors that were launched by the specified actor
           but have not yet sent back their Last Ack messages.

     ReadRead ActorActor VIVI

       (Filename: Actor Framework.lvlib:Last Ack.lvclass:Read Actor.vi)

       Returns the state the actor was in when it shut down.


5496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5497 ordinal=5497 -->
## Functions

Functions

Inputs/Outputs

   •      Last Ack —

    Last Ack specifies the Last Ack message that an actor sent.

   •      Actor —

    Actor returns the final state of the actor.

ReadRead Caller-To-ActorCaller-To-Actor EnqueuerEnqueuer VIVI

(Filename: Actor Framework.lvlib:Last Ack.lvclass:Read Caller-To-Actor Enqueuer.vi)

Returns the reference the caller used to send messages to the actor. Although the
reference is invalid, you can use it to identify which actor shut down.


Inputs/Outputs

   •      Last Ack —

    Last Ack specifies the Last Ack message that an actor sent.

   •       Caller-to-Actor Enqueuer —

     Caller-to-Actor Enqueuer returns the reference the caller used to send messages to the actor.

ReadRead ErrorError ReportReport VIVI

(Filename: Actor Framework.lvlib:Last Ack.lvclass:Read Error Report.vi)

Returns the error, if any, that caused an actor to shut down.


                                                    © National Instruments 5497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5498 ordinal=5498 -->
## Functions

Functions


      Inputs/Outputs

               •      Last Ack —

            Last Ack specifies the Last Ack message that an actor sent.

               •       error report —

             error report returns the error the actor sent when it shut down.

     SendSend ErrorError ReportReport VIVI

       (Filename: Actor Framework.lvlib:Report Error Msg.lvclass:Send Error Report.vi)

      Use this VI to send an error to an actor. The error will be handled by the Handle Error VI
       of the actor. If the error is not handled there, it will cause the actor to stop running.


      Inputs/Outputs

               •      Message Enqueuer —

           Message Enqueuer specifies a message enqueuer to check.

               •       Error From Sender —

            Error From Sender can accept error information wired from previously called VIs. Use this
            information to decide if any functionality should be bypassed in the event of errors from other
               VIs.

              Right-click the Error From Sender control on the front panel and select Explain Error or Explain
           Warning from the shortcut menu for more information about the error.

               •      Message Priority (Normal) —


5498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5499 ordinal=5499 -->
## Functions

Functions


    Message Priority specifies the placement of the messages in the message queue, which
    determines when the actor will process the messages.

    0 Low—Specifies that the batch will be processed after messages of all other priorities.
     Normal (Default)—Specifies that the batch will be processed after critical- and high-priority    1     messages but before low-priority ones.
     High—Specifies that the batch will be processed first. High-priority messages can be
    2 superseded only by an Emergency Stop or Last Ack message, both of which have critical
       priority.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Refer to the Actor Framework template for more information about the Actor
Framework. To use the Actor Framework template, click Create Project from the
LabVIEW start screen and select Actor Framework.

AdvancedAdvanced

Use the Advanced VIs with the Actor Framework to implement advanced messaging
techniques.


 Palette
            Description
 Object

            (Filename: Actor Framework.lvlib:Batch Msg.lvclass:Send Batch.vi) Send
 Batch VI           Sends multiple messages in a batch to an actor. All messages in the batch are given the


                                                    © National Instruments 5499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5500 ordinal=5500 -->
## Functions

Functions


         Palette                    Description
        Object

                same priority. No additional messages of the same priority will be processed by the
                     actor in between the messages in the batch. However, messages with a higher priority
                   than the batch will be processed before the batch itself.

        Time-
        Delayed                    Waits for the specified amount of time and then sends a message to an actor a       Send                     specified number of times.        Message
          VI

                    (Filename: Actor Framework.lvlib:Self-Addressed Msg.lvclass:Address Message.vi)
        Address
        Message   Creates a self-addressed message by storing an enqueuer inside a message. Later,
          VI       when you send the message with the Send Self-Addressed Message method, the
                 message will be sent to the actor that uses this enqueuer.


                    (Filename: Actor Framework.lvlib:Self-Addressed Msg.lvclass:Send Self-Addressed
                     Message.vi)       Send Self-
        Addressed                  Sends a self-addressed message. You can send multiple copies to the same address by        Message
                       calling this VI multiple times with the same message.          VI
                 Use the Address Message method to create a self-addressed message.

       Send
        Message   (Filename: Actor Framework.lvlib:Reply Msg.lvclass:Send Message And Wait For
       And Wait   Response.vi)
         For
        Response  Sends a message to an actor and synchronously waits for a response from the actor.
          VI

       Send      (Filename: Actor Framework.lvlib:Actor.lvclass:Send Launch Nested Actor Msg.vi)
        Launch
        Nested     This VI sends a message containing an actor to another actor. The actor receiving the
         Actor Msg  message will launch the payload actor as a nested actor. Use this VI only to send a
          VI        message from an actor to itself.


5500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5500 -->

