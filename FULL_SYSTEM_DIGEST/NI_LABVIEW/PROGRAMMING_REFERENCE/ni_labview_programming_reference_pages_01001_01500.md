# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1001 ordinal=1001 -->
## Functions

Functions


 Palette Object  Description

 Dual Channel   Measures the frequency response of the input signals and the coherence based on
 Spectral       the current and previous input signals. This Express VI returns results such as
 Measurement  Magnitude, Phase, Coherence, Real, and Imaginary.


 Distortion      Performs distortion measurements on a signal, such as tone analysis, total
 Measurements harmonic distortion (THD), and signal in noise and distortion (SINAD).


                Finds the single tone with the highest amplitude or searches a specified frequency Tone               range to find the single tone with the highest amplitude. You also can find the Measurements               frequency and phase for a single tone.


 Timing and
               Performs timing and transition measurements, such as frequency, period, or duty Transition                  cycle, on a signal, usually a pulse. Measurements

 Amplitude
 and Level      Performs voltage measurements on a signal.
 Measurements

BasicBasic AveragedAveraged DC-RMSDC-RMS

Calculates the DC and RMS values of an input waveform or array of waveforms. This VI
is similar to the Averaged DC-RMS VI, but this VI returns only one DC value and one
RMS value per input waveform.

Wire data to the signal in input to determine the polymorphic instance to use or
manually select the instance.


  • Basic Averaged DC-RMS for 1 Chan VI
  • Basic Averaged DC-RMS for N Chan VI


                                                    © National Instruments 1001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1002 ordinal=1002 -->
## Functions

Functions

       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

           Note The Basic Averaged DC-RMS VI assumes that consecutive data blocks
              are continuous. If they are not, the VI returns a warning.
    BasicBasic AveragedAveraged DC-RMSDC-RMS forfor 11 ChanChan VIVI

       Calculates the DC and RMS values of an input waveform or array of waveforms. This VI
         is similar to the Averaged DC-RMS VI, but this VI returns only one DC value and one
     RMS value per input waveform.

       Wire data to the signal in input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •       reset —

             reset resets the history of your time signal. You typically use reset to reset the exponentially
           averaged measurement.

               •       signal in —

             signal in is the input waveform.

               •      averaging type —

            averaging type is the type of averaging used during the measurement. Because this VI computes
          one DC and one RMS value per input waveform, the input record length selects the averaging
             time. If averaging type is exponential, this VI calculates the DC and RMS values using an
             exponentially weighted averaging measurement starting from the previous DC and RMS values.


1002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1003 ordinal=1003 -->
## Functions

Functions


  0 Linear—Averaging time is equal to the record length.
  1 Exponential—Time constant is half the record length.

•     window —

  window is the window to be applied to the time record before DC/RMS computation. LabVIEW
  ignores this input if averaging type is exponential.

          Rectangular
  0          (no window)
  1      Hanning
  2     Low side lobe

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     DC value —

  DC value is the measured DC value in volts if the signal is in volts.

•     RMS value —

  RMS value is the measured RMS value in volts if the signal is in volts.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•     measurement info —

  measurement info returns information about your measurement, mainly warnings for
  inconsistencies in your input signal.

      •      uncertainty —

      uncertainty is reserved for future use.

      •      Warning —


                                                   © National Instruments 1003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1004 ordinal=1004 -->
## Functions

Functions


              Warning is TRUE if a warning is generated during processing.

                     •     comments —

             comments contains a warning message when Warning is TRUE.


       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

           Note The Basic Averaged DC-RMS VI assumes that consecutive data blocks
              are continuous. If they are not, the VI returns a warning.
    BasicBasic AveragedAveraged DC-RMSDC-RMS forfor NN ChanChan VIVI

       Calculates the DC and RMS values of an input waveform or array of waveforms. This VI
         is similar to the Averaged DC-RMS VI, but this VI returns only one DC value and one
     RMS value per input waveform.

           Note

            The multichannel waveform array input should be the result of a
              multichannel acquisition where each element of the array of waveforms is a
                 distinct and separate channel of data.


      Inputs/Outputs

               •       reset —

1004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1005 ordinal=1005 -->
## Functions

Functions


  reset resets the history of your time signal. You typically use reset to reset the exponentially
  averaged measurement.

•       signals in —

  signals in is the array of input waveforms.

•      averaging type —

  averaging type is the type of averaging used during the measurement. Because this VI computes
  one DC and one RMS value per input waveform, the input record length selects the averaging
  time. If averaging type is exponential, this VI calculates the DC and RMS values using an
  exponentially weighted averaging measurement starting from the previous DC and RMS values.

  0 Linear—Averaging time is equal to the record length.
  1 Exponential—Time constant is half the record length.

•     window —

  window is the window to be applied to the time record before DC/RMS computation. LabVIEW
  ignores this input if averaging type is exponential.

          Rectangular  0
          (no window)
  1      Hanning
  2     Low side lobe

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     DC values —

  DC values is an array of the measured DC values.

•     RMS values —

  RMS values is an array of the measured RMS values.

•       error out —


                                                   © National Instruments 1005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1006 ordinal=1006 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

               •     measurements info —

          measurements info is an array that returns information about your measurement, mainly
           warnings for inconsistencies in your input signal.

                     •      uncertainty —

                uncertainty is reserved for future use.

                     •      Warning —

              Warning is TRUE if a warning is generated during processing.

                     •     comments —

             comments contains a warning message when Warning is TRUE.


       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

           Note The Basic Averaged DC-RMS VI assumes that consecutive data blocks
              are continuous. If they are not, the VI returns a warning.
   AveragedAveraged DC-RMSDC-RMS

       Calculates the DC and RMS values of an input waveform or array of waveforms. This VI
         is similar to the Basic Averaged DC-RMS VI, but this VI gives more precise control over
       the individual DC and RMS calculations.

       Wire data to the signal in input to determine the polymorphic instance to use or
      manually select the instance.


1006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1007 ordinal=1007 -->
## Functions

Functions

  • Averaged DC-RMS for 1 Chan VI
  • Averaged DC-RMS for N Chan VI

This VI is designed to process a single channel or multiple channels continuously,
typically from within a For Loop or a While Loop.

      Note The Averaged DC-RMS VI assumes that consecutive data blocks are
       continuous. If they are not, the VI returns a warning in measurement info,
        unless Ignore input start time is enabled.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Advanced DC-RMS Measurement.vi
AveragedAveraged DC-RMSDC-RMS forfor 11 ChanChan VIVI

Calculates the DC and RMS values of an input waveform or array of waveforms. This VI
is similar to the Basic Averaged DC-RMS VI, but this VI gives more precise control over
the individual DC and RMS calculations.

Wire data to the signal in input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •       reset —


                                                    © National Instruments 1007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1008 ordinal=1008 -->
## Functions

Functions


             reset resets the history of your time signal. You typically use reset to reset the exponentially
           averaged measurement.

               •       signal in —

             signal in is the input waveform.

               •      averaging type —

            averaging type is the type of averaging used during the measurement. If averaging type is
             exponential, this VI calculates the DC and RMS values using an exponentially weighted averaging
          measurement starting from the previous DC and RMS values.

           0 Linear—Averaging time is equal to the record length.
           1 Exponential—Time constant is half the record length.

               •      averaging time —

            averaging time defines dt of DC value waveform and RMS value waveform in seconds. The
             default is –1.00, which corresponds to average time = input block duration.

            For linear averaging, each output data point results from performing the averaging process for
            the time period specified by averaging time. For exponential averaging, each output data point
              results from exponential integration performed for the time period specified by averaging time
            using exp. time constant.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging control —

            averaging control contains the advanced parameters used to completely control the DC or RMS
           measurement.

                     •     window for DC —

             window for DC is the window to be applied to the time record before DC computation.
              LabVIEW ignores this input if averaging type is exponential.


1008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1009 ordinal=1009 -->
## Functions

Functions


              Rectangular      0
             (no window)
      1      Hanning
      2     Low side lobe

      •      output function —

      output function selects the type of measurements to be performed.

          If you need only DC or RMS measurements, selecting these components separately
       increases the processing speed.

      0     DC only
      1     RMS only
      2     DC and RMS

      •     window for RMS —

     window for RMS is the window to be applied to the time record before RMS computation.
      LabVIEW ignores this input if averaging type is exponential.

              Rectangular
      0             (no window)
      1      Hanning
      2     Low side lobe

      •      exp. time constant —

      exp. time constant specifies the time constant (RC) of your DC or RMS measurement.

      exp. time constant equals –1.00, which corresponds to a value of input block duration/2.

      •      Ignore input start time —

      Set Ignore input start time to TRUE when you do not want the VI to check for continuity
      using t0 values.


•      data ready —


                                                   © National Instruments 1009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1010 ordinal=1010 -->
## Functions

Functions


           data ready indicates the DC value waveform and RMS value waveform contain data. A value of
           FALSE means the waveforms do not contain data.

               •     DC value waveform —

         DC value waveform indicates DC values of signal in computed over averaging time seconds and
           time stamped continuously from the last reset.

               •     RMS value waveform —

         RMS value waveform indicates RMS values of signal in computed over averaging time seconds
          and time stamped continuously from the last reset.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurement info —

          measurement info returns information about your measurement, mainly warnings for
             inconsistencies in your input signal.

                     •      uncertainty —

                uncertainty is reserved for future use.

                     •      Warning —

              Warning is TRUE if a warning is generated during processing.

                     •     comments —

             comments contains a warning message when Warning is TRUE.


       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

           Note The Averaged DC-RMS VI assumes that consecutive data blocks are
              continuous. If they are not, the VI returns a warning in measurement info,


1010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1011 ordinal=1011 -->
## Functions

Functions


        unless Ignore input start time is enabled.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Advanced DC-RMS Measurement.vi
AveragedAveraged DC-RMSDC-RMS forfor NN ChanChan VIVI

Calculates the DC and RMS values of an input waveform or array of waveforms. This VI
is similar to the Basic Averaged DC-RMS VI, but this VI gives more precise control over
the individual DC and RMS calculations.

      Note

           It is assumed that the array of input waveforms is the result of a multichannel
        acquisition where each element in the array of waveforms is a distinct and
        separate channel of data.


Inputs/Outputs

   •       reset —

    reset resets the history of your time signal. You typically use reset to reset the exponentially
    averaged measurement.

   •       signals in —


                                                    © National Instruments 1011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1012 ordinal=1012 -->
## Functions

Functions


             signals in is the array of input waveforms.

               •      averaging type —

            averaging type is the type of averaging used during the measurement. If averaging type is
             exponential, this VI calculates the DC and RMS values using an exponentially weighted averaging
          measurement starting from the previous DC and RMS values.

           0 Linear—Averaging time is equal to the record length.
           1 Exponential—Time constant is half the record length.

               •      averaging time —

            averaging time defines dt of DC value waveform and RMS value waveform in seconds. The
             default is –1.00, which corresponds to average time = input block duration.

            For linear averaging, each output data point results from performing the averaging process for
            the time period specified by averaging time. For exponential averaging, each output data point
              results from exponential integration performed for the time period specified by averaging time
            using exp. time constant.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging control —

            averaging control contains the advanced parameters used to completely control the DC or RMS
           measurement.

                     •     window for DC —

             window for DC is the window to be applied to the time record before DC computation.
              LabVIEW ignores this input if averaging type is exponential.

                        Rectangular
               0
                       (no window)
               1      Hanning
               2     Low side lobe


1012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1013 ordinal=1013 -->
## Functions

Functions


      •      output function —

      output function selects the type of measurements to be performed.

          If you need only DC or RMS measurements, selecting these components separately
       increases the processing speed.

      0     DC only
      1     RMS only
      2     DC and RMS

      •     window for RMS —

     window for RMS is the window to be applied to the time record before RMS computation.
      LabVIEW ignores this input if averaging type is exponential.

              Rectangular
      0             (no window)
      1      Hanning
      2     Low side lobe

      •      exp. time constant —

      exp. time constant specifies the time constant (RC) of your DC or RMS measurement.

      exp. time constant equals –1.00, which corresponds to a value of input block duration/2.

      •      Ignore input start time —

      Set Ignore input start time to TRUE when you do not want the VI to check for continuity
      using t0 values.


•      data ready —

  data ready indicates the DC value waveform and RMS value waveform contain data. A value of
  FALSE means the waveforms do not contain data.

•     DC value waveforms —

  DC value waveforms is an array of waveforms containing DC values.


                                                   © National Instruments 1013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1014 ordinal=1014 -->
## Functions

Functions

               •     RMS value waveforms —

         RMS value waveforms is an array of waveforms containing RMS values.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurements info —

          measurements info is an array that returns information about your measurement, mainly
           warnings for inconsistencies in your input signal.

                     •      uncertainty —

                uncertainty is reserved for future use.

                     •      Warning —

              Warning is TRUE if a warning is generated during processing.

                     •     comments —

             comments contains a warning message when Warning is TRUE.


       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

           Note The Averaged DC-RMS VI assumes that consecutive data blocks are
              continuous. If they are not, the VI returns a warning in measurement info,
              unless Ignore input start time is enabled.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Advanced DC-RMS Measurement.vi


1014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1015 ordinal=1015 -->
## Functions

Functions

CycleCycle AverageAverage andand RMSRMS

Returns the average and RMS levels of a selected cycle of a periodic waveform or an
array of periodic waveforms. Wire data to the signal in input to determine the
polymorphic instance to use or manually select the instance.

      Note The terminology and measurement definitions for this VI comply with
     IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
     andRelatedWaveforms.


  • Cycle Average and RMS 1 chan VI
  • Cycle Average and RMS N chan VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Pulse and Transition Measurements.vi
  • labview\examples\Signal Processing\Waveform
   Measurements\N channel Pulse and Transition
   Measurements.vi
CycleCycle AverageAverage andand RMSRMS 11 chanchan VIVI

Returns the average and RMS levels of a selected cycle of a periodic waveform or an
array of periodic waveforms. Wire data to the signal in input to determine the
polymorphic instance to use or manually select the instance.

      Note The terminology and measurement definitions for this VI comply with


                                                    © National Instruments 1015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1016 ordinal=1016 -->
## Functions

Functions

          IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
         andRelatedWaveforms.


      Inputs/Outputs

               •       cycle number (1) —

            cycle number specifies the cycle, or period, of the periodic signal on which to perform the
           measurement.

               •       signal in —

             signal in is the waveform to measure. Each waveform is required to contain at least cycle
          number complete cycles, where a cycle is defined as the interval between two consecutive rising
          mid ref level crossings.

               •      reference levels —

            reference levels specifies the high, middle, and low reference levels of a waveform.

           LabVIEW uses the reference levels to define the measurement interval of one complete cycle.
          The distance between the mid ref level and the high ref level must equal the distance between
            the low ref level and the mid ref level. If the two distances are not equal, LabVIEW adjusts either
            the high ref level or the low ref level to match the smaller of the two distances. For example, if
           you specify a high ref level of 90%, a mid ref level of 50%, and a low ref level of 20%, LabVIEW
            uses 80% instead of 90% for the high ref level.

                     •      high ref level —

                high ref level specifies the high reference level of the waveform in percent (default) or
                absolute units.

                   After the signal crosses the mid ref level in the rising direction, it must cross the high ref
                  level before the next falling mid ref level crossing can be counted.


1016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1017 ordinal=1017 -->
## Functions

Functions


      •     mid ref level —

     mid ref level specifies the middle reference level in percent (default) or absolute units.

     The interval between consecutive rising mid ref level crossings defines one cycle, or period,
       of the waveform. At least one high/low reference level crossing must separate each mid ref
       level crossing.

      •      low ref level —

      low ref level specifies the low reference level of the waveform in percent (default) or
      absolute units.

       After the signal crosses the mid ref level in the falling direction, it must cross the low ref
       level before the next rising mid ref level crossing can be counted.

      •       ref units —

       ref units specifies whether the high ref level, mid ref level, and low ref level inputs are
       interpreted as a percentage (default) of the full range of the waveform or as absolute levels.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      percent level settings —

  percent level settings specifies the method LabVIEW uses to determine the high and low state
  levels of a waveform.

   If you select percent ref units, percent level settings determines the reference levels. Otherwise,
  LabVIEW ignores this input.

      •     method —

     method specifies how LabVIEW computes the high and low state levels of the waveform.

       Histogram—Returns the levels of the histogram bins with the maximum number of hits in
      0
        the upper and lower regions of the waveform. The upper and lower regions of the


                                                   © National Instruments 1017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1018 ordinal=1018 -->
## Functions

Functions


               waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
                waveform.
               1 Peak—Searches the entire waveform for its maximum and minimum levels.
                Auto select (default)—Determines whether the histogram bins that correspond to the high
               and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
               2 results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
                   either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
                 histogram fails).

                     •      histogram size —

               histogram size specifies the number of bins in the histogram LabVIEW uses to determine
                the high and low state levels of the waveform.

                     •      histogram method —

               histogram method specifies how LabVIEW computes the high and low state levels of the
               waveform. Currently, mode is the only available histogram method.

               0           mode

                     •      reserved —

                reserved is reserved for future use.


               •       cycle average —

            cycle average is the mean level of one complete period of a periodic input waveform.

          The average is computed by the following equation.                           where i
             indicates the waveform samples that fall in the single period specified by cycle number and
         numPointsis given by the following equation. numPoints= int(period/dt+ .5) where dtis
            the time between two samples and int( ) is a function that returns the integer portion of a
             floating-point number.

          The cycle average of a perfect sine wave is zero, while the average level of the entire waveform
           can be nonzero due to partial periods at the boundaries of the waveform.

               •       cycle RMS —


1018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1019 ordinal=1019 -->
## Functions

Functions


  cycle RMS is the root mean square value of one complete period of a periodic input waveform.

  The RMS value is computed by the following equation.

  where iindicates the waveform samples that fall in the single period specified by cycle number
  and numPointsis given by the following equation. numPoints= int(period/dt+ .5) where
 dtis the time between two points and int( ) is a function that returns the integer portion of a
  floating-point number.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•     measurement info —

  measurement info returns the measurement cycle interval endpoints and the absolute
  reference levels used to define the measurement cycle.

      •       start time —

       start time specifies the time of the rising mid ref level crossing that defines the start of the
     measurement interval.

      •     end time —

     end time specifies the time of the rising mid ref level crossing that defines the end of the
     measurement interval.

      •       ref levels —

       ref levels returns the three user-defined reference levels of the waveform in absolute units.

      LabVIEW uses the reference levels to define the interval of one cycle measurement.

             •      high ref level —

          high ref level returns the high reference level.

             •     mid ref level —


                                                   © National Instruments 1019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1020 ordinal=1020 -->
## Functions

Functions


                 mid ref level returns the middle reference level.

                           •      low ref level —

                  low ref level returns the low reference level.

                           •       ref units —

                        ref units is always absolute in measurement info.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Pulse and Transition Measurements.vi
            • labview\examples\Signal Processing\Waveform
        Measurements\N channel Pulse and Transition
        Measurements.vi
    CycleCycle AverageAverage andand RMSRMS NN chanchan VIVI

       Returns the average and RMS levels of a selected cycle of a periodic waveform or an
       array of periodic waveforms. Wire data to the signal in input to determine the
      polymorphic instance to use or manually select the instance.

           Note The terminology and measurement definitions for this VI comply with
          IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
         andRelatedWaveforms.


1020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1021 ordinal=1021 -->
## Functions

Functions


Inputs/Outputs

   •       cycle number (1) —

    cycle number specifies the cycle, or period, of the periodic signal on which to perform the
    measurement.

   •       signal(s) in —

     signal(s) in is an array of waveforms containing the signals to measure. Each waveform is
    required to contain at least cycle number complete cycles, where a cycle is defined as the
     interval between two consecutive rising mid ref level crossings.

   •      reference levels —

    reference levels specifies the high, middle, and low reference levels of a waveform.

    LabVIEW uses the reference levels to define the measurement interval of one complete cycle.
    The distance between the mid ref level and the high ref level must equal the distance between
    the low ref level and the mid ref level. If the two distances are not equal, LabVIEW adjusts either
    the high ref level or the low ref level to match the smaller of the two distances. For example, if
    you specify a high ref level of 90%, a mid ref level of 50%, and a low ref level of 20%, LabVIEW
    uses 80% instead of 90% for the high ref level.

         •      high ref level —

        high ref level specifies the high reference level of the waveform in percent (default) or
        absolute units.

          After the signal crosses the mid ref level in the rising direction, it must cross the high ref
         level before the next falling mid ref level crossing can be counted.

         •     mid ref level —

       mid ref level specifies the middle reference level in percent (default) or absolute units.

       The interval between consecutive rising mid ref level crossings defines one cycle, or period,


                                                    © National Instruments 1021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1022 ordinal=1022 -->
## Functions

Functions


                  of the waveform. At least one high/low reference level crossing must separate each mid ref
                  level crossing.

                     •      low ref level —

              low ref level specifies the low reference level of the waveform in percent (default) or
                absolute units.

                   After the signal crosses the mid ref level in the falling direction, it must cross the low ref
                  level before the next rising mid ref level crossing can be counted.

                     •       ref units —

                   ref units specifies whether the high ref level, mid ref level, and low ref level inputs are
                 interpreted as a percentage (default) of the full range of the waveform or as absolute levels.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      percent level settings —

            percent level settings specifies the method LabVIEW uses to determine the high and low state
              levels of a waveform.

                    If you select percent ref units, percent level settings determines the reference levels. Otherwise,
           LabVIEW ignores this input.

                     •     method —

             method specifies how LabVIEW computes the high and low state levels of the waveform.

                Histogram—Returns the levels of the histogram bins with the maximum number of hits in
                 the upper and lower regions of the waveform. The upper and lower regions of the
               0
               waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
                waveform.
               1 Peak—Searches the entire waveform for its maximum and minimum levels.
               2 Auto select (default)—Determines whether the histogram bins that correspond to the high


1022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1023 ordinal=1023 -->
## Functions

Functions


      and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
         results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
        either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
       histogram fails).

      •      histogram size —

      histogram size specifies the number of bins in the histogram LabVIEW uses to determine
      the high and low state levels of the waveform.

      •      histogram method —

      histogram method specifies how LabVIEW computes the high and low state levels of the
      waveform. Currently, mode is the only available histogram method.

      0           mode

      •      reserved —

      reserved is reserved for future use.


•       cycle average —

  cycle average is an array containing the cycle average of each waveform in signal(s) in. cycle
  average is the mean level of one complete period of a periodic input waveform.

  The average is computed by the following equation.                           where i
  indicates the waveform samples that fall in the single period specified by cycle number and
 numPointsis given by the following equation. numPoints= int(period/dt+ .5) where dtis
  the time between two samples and int( ) is a function that returns the integer portion of a
  floating-point number.

  The cycle average of a perfect sine wave is zero, while the average level of the entire waveform
  can be nonzero due to partial periods at the boundaries of the waveform.

•       cycle RMS —

  cycle RMS is an array containing the cycle RMS value for each waveform in signal(s) in. cycle
  RMS is the root mean square value of one complete period of a periodic input waveform.


                                                   © National Instruments 1023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1024 ordinal=1024 -->
## Functions

Functions


          The RMS value is computed by the following equation.

           where iindicates the waveform samples that fall in the single period specified by cycle number
          and numPointsis given by the following equation. numPoints= int(period/dt+ .5) where
        dtis the time between two points and int( ) is a function that returns the integer portion of a
             floating-point number.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurement info —

          measurement info is an array of clusters containing measurement information for each input
           waveform.

                     •       start time —

                  start time specifies the time of the rising mid ref level crossing that defines the start of the
              measurement interval.

                     •     end time —

              end time specifies the time of the rising mid ref level crossing that defines the end of the
              measurement interval.

                     •       ref levels —

                   ref levels returns the three user-defined reference levels of the waveform in absolute units.

              LabVIEW uses the reference levels to define the interval of one cycle measurement.

                           •      high ref level —

                    high ref level returns the high reference level.

                           •     mid ref level —

                 mid ref level returns the middle reference level.

                           •      low ref level —


1024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1025 ordinal=1025 -->
## Functions

Functions


           low ref level returns the low reference level.

                •       ref units —

               ref units is always absolute in measurement info.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Pulse and Transition Measurements.vi
  • labview\examples\Signal Processing\Waveform
   Measurements\N channel Pulse and Transition
   Measurements.vi
WaveformWaveform MonitoringMonitoring

Use the Waveform Monitoring VIs to analyze the waveforms for trigger points, to search
for peaks, and to perform limit mask testing.

      Note The VIs on this palette return an error if an input waveform has a dt
        less than or equal to zero.

      Note The Waveform Monitoring VIs presently do not accept waveforms that
        contain complex data.

The VIs on this palette can return waveform error codes.


                                                    © National Instruments 1025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1026 ordinal=1026 -->
## Functions

Functions


         Palette                      Description
        Object

                     Performs limit testing on waveform or cluster input data. The VI compares signal in
                      with upper limit and lower limit and ignores any limit input that is not wired. You
         Limit Testing  can wire output values to a graph to view the limits, signal, and failures. Wire data to
                      the signal in input to determine the polymorphic instance to use or manually select
                      the instance.


                       Creates continuous or segmented masks in the time domain or in the frequency
         Limit        domain. You can use different instances of this VI to create multiple limits. Wire data
         Specification  to the Specification Cluster input to determine the polymorphic instance to use or
                     manually select the instance.


                       Creates a continuous or segmented mask in the time domain or in the frequency         Limit                    domain. You can use different instances of this VI to create multiple limits. Wire data
         Specification                       to the Specification Cluster input to determine the polymorphic instance to use or        By Formula                     manually select the instance.


       Waveform    Finds the locations, amplitudes, and second derivatives of peaks and valleys in
        Peak         Signal In. Wire data to the Signal In input to determine the polymorphic instance to
         Detection    use or manually select the instance.


                      Finds the first level-crossing location in a waveform. You can retrieve the trigger
         Basic Level
                        location as an index or as a time. The trigger conditions are specified in terms of
         Trigger
                      threshold level, slope, and hysteresis. Wire data to the signal in input to determine
         Detection
                      the polymorphic instance to use or manually select the instance.


       Mask and
                     Performs limit testing on Signals.
         Limit Testing

         Trigger and
                    Uses triggering to extract a segment out of a signal. The trigger conditions can be
        Gate


1026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1027 ordinal=1027 -->
## Functions

Functions


 Palette              Description
 Object

             based on a start or stop trigger threshold or can be static. When a trigger condition is
                  static, the trigger occurs immediately and this Express VI returns a predefined
            number of samples.

LimitLimit TestingTesting

Performs limit testing on waveform or cluster input data. The VI compares signal in
with upper limit and lower limit and ignores any limit input that is not wired. You can
wire output values to a graph to view the limits, signal, and failures. Wire data to the
signal in input to determine the polymorphic instance to use or manually select the
instance.


  • Limit Testing Time VI
  • Limit Testing Frequency VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Limit Testing Measurement.vi
  • labview\examples\Signal Processing\Waveform Measurements\
   Limit Testing for Unevenly Sampled Data.vi
LimitLimit TestingTesting TimeTime VIVI

Performs limit testing on waveform or cluster input data. The VI compares signal in
with upper limit and lower limit and ignores any limit input that is not wired. You can
wire output values to a graph to view the limits, signal, and failures. Wire data to the

                                                    © National Instruments 1027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1028 ordinal=1028 -->
## Functions

Functions

       signal in input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •      output t0 —

           output t0 determines the source of start time, t0, of the waveforms for output values.

              t0 = limit x0 (default)—Starts with upper limit start time if you define the upper and lower
           0                 limits.
           1 t0 = signal in t0—Starts with signal in start time.

               •       signal in —

             signal in specifies the waveform to test to make sure it lies in the envelope bounded by the
           upper and lower limits.

               •      upper limit —

           upper limit specifies the upper boundary of the envelope. The default is Inf.

                     •      x0 —

               x0 specifies the minimum value of the x-axis.

                     •     dx —

              dx specifies the x-axis interval between points in the input data.

                     •      Y —

               Y specifies the y-axis values for the limit.


               •      lower limit —


1028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1029 ordinal=1029 -->
## Functions

Functions


  lower limit specifies the lower boundary of the envelope. The default is –Inf.

      •      x0 —

      x0 specifies the minimum value of the x-axis.

      •     dx —

      dx specifies the x-axis interval between points in the input data.

      •      Y —

      Y specifies the y-axis values for the limit.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       limit test config —

  limit test config specifies the limit-test pass region and whether the limit values are included.

      •      pass region —

      pass region specifies whether you want the test to pass where the signal points fall inside
      the limits or outside the limits.

      0 Inside limits—lower limit < signal in < upper limit.
       Outside limits—signal in does not fall within the area defined by lower limit and upper
      1
         limit.

      •      include UL —

      include UL specifies whether you want the test to pass where the signal points fall on upper
        limit. The default is TRUE.

      •      include LL —

      include LL specifies whether you want the test to pass where the signal points fall on lower


                                                   © National Instruments 1029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1030 ordinal=1030 -->
## Functions

Functions


                    limit. The default is TRUE.


               •       failures —

              failures returns the locations of failed test points.

                     •      x values —

               x values returns the x-value locations of failed test points.

                     •      y values —

               y values returns the y-value locations of failed test points.


               •       test passed? —

              test passed? indicates the result of limit mask testing. If TRUE, the signal is less than or equal to
           upper limit and greater than or equal to lower limit and the limit testing passed. If FALSE, the
              limit testing did not pass.

               •       test results —

              test results returns the results of the limit testing at each data point. The VI returns TRUE if the
            data point is less than or equal to upper limit and greater than or equal to lower limit.

               •      output values —

           output values contains the upper limit and lower limit, the signal, and the failures. You can wire
              this output to a graph to view the values.

          The first element in the array is the input signal. The x0 and dx values in this waveform are
           changed so that it can be easily plotted with the upper and lower limits. The second element in
            the array is the failure waveform. The failure waveform contains NaN at points where the limit
              test passes and contains the input signal where the limit test fails. The third and fourth elements
             of the array are the upper and lower boundaries, respectively.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      clearance —

1030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1031 ordinal=1031 -->
## Functions

Functions


    clearance returns distance measures between signal in and upper limit and lower limit.

         •      clearance UL —

        clearance UL is the minimum distance between signal in and upper limit (UL). If the signal
         points fail at any point along upper limit, clearance UL is set to zero. When clearance UL
         returns Inf, upper limit was not defined, so the signal was not tested against it. You can
         interpret Inf as passing upper limit with maximum clearance.

         •      clearance LL —

        clearance LL is the minimum distance between signal in and lower limit (LL). If the signal
         points fail at any point along lower limit, clearance LL is set to zero. When clearance LL
         returns Inf, lower limit was not defined, so the signal was not tested against it. You can
         interpret Inf as passing lower limit with maximum clearance.

         •     min clearance —

       min clearance is the minimum, overall distance between signal in and the limits. min
        clearance is the minimum of clearance UL and clearance LL. If the signal fails the limit test
         at any point, min clearance is set to zero. When min clearance returns Inf, neither upper
          limit nor lower limit were defined, so the signal was not tested against them. You can
         interpret Inf as passing both upper limit and lower limit with maximum clearance.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Limit Testing Measurement.vi
  • labview\examples\Signal Processing\Waveform Measurements\
   Limit Testing for Unevenly Sampled Data.vi
LimitLimit TestingTesting FrequencyFrequency VIVI

Performs limit testing on waveform or cluster input data. The VI compares signal in
with upper limit and lower limit and ignores any limit input that is not wired. You can


                                                    © National Instruments 1031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1032 ordinal=1032 -->
## Functions

Functions

       wire output values to a graph to view the limits, signal, and failures. Wire data to the
       signal in input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •       signal in —

             signal in contains the signal to test to make sure it lies in the envelope bounded by the upper
          and lower limits.

                     •       f0 —

                  f0 specifies the start frequency, in hertz, of the spectrum.

                     •       df —

                 df specifies the frequency resolution, in hertz, of the spectrum.

                     •      spectrum —

              spectrum is the spectrum of the input signal.


               •      upper limit —

           upper limit specifies the upper boundary of the envelope. The default is Inf.

                     •      x0 —

               x0 specifies the minimum value of the x-axis.

                     •     dx —

              dx specifies the x-axis interval between points in the input data.


1032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1033 ordinal=1033 -->
## Functions

Functions


      •      Y —

      Y specifies the y-axis values for the limit.


•      lower limit —

  lower limit specifies the lower boundary of the envelope. The default is –Inf.

      •      x0 —

      x0 specifies the minimum value of the x-axis.

      •     dx —

      dx specifies the x-axis interval between points in the input data.

      •      Y —

      Y specifies the y-axis values for the limit.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       limit test config —

  limit test config specifies the limit-test pass region and whether the limit values are included.

      •      pass region —

      pass region specifies whether you want the test to pass where the signal points fall inside
      the limits or outside the limits.

      0 Inside limits—lower limit < signal in < upper limit.
       Outside limits—signal in does not fall within the area defined by lower limit and upper
      1
         limit.

      •      include UL —


                                                   © National Instruments 1033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1034 ordinal=1034 -->
## Functions

Functions


                include UL specifies whether you want the test to pass where the signal points fall on upper
                    limit. The default is TRUE.

                     •      include LL —

                include LL specifies whether you want the test to pass where the signal points fall on lower
                    limit. The default is TRUE.


               •       failures —

              failures returns the locations of failed test points.

                     •      x values —

               x values returns the x-value locations of failed test points.

                     •      y values —

               y values returns the y-value locations of failed test points.


               •       test passed? —

              test passed? indicates the result of limit mask testing. If TRUE, the signal is less than or equal to
           upper limit and greater than or equal to lower limit and the limit testing passed. If FALSE, the
              limit testing did not pass.

               •       test results —

              test results returns the results of the limit testing at each data point. The VI returns TRUE if the
            data point is less than or equal to upper limit and greater than or equal to lower limit.

               •      output values —

           output values contains the upper limit and lower limit, the signal, and the failures. You can wire
              this output to a graph to view the values.

          The first element in the array is the input signal. The x0 and dx values in this waveform are
           changed so that it can be easily plotted with the upper and lower limits. The second element in
            the array is the failure waveform. The failure waveform contains NaN at points where the limit
              test passes and contains the input signal where the limit test fails. The third and fourth elements


1034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1035 ordinal=1035 -->
## Functions

Functions


  of the array are the upper and lower boundaries, respectively.

      •      x0 —

      x0 is the minimum value of the x-axis.

      •     dx —

      dx is the x-axis interval between points in the input data.

      •      Y —

      Y contains the y-axis values for the limit.


•       error out —

  error out contains error information. This output provides standard error out functionality.

•      clearance —

  clearance returns distance measures between signal in and upper limit and lower limit.

      •      clearance UL —

      clearance UL is the minimum distance between signal in and upper limit (UL). If the signal
       points fail at any point along upper limit, clearance UL is set to zero. When clearance UL
       returns Inf, upper limit was not defined, so the signal was not tested against it. You can
       interpret Inf as passing upper limit with maximum clearance.

      •      clearance LL —

      clearance LL is the minimum distance between signal in and lower limit (LL). If the signal
       points fail at any point along lower limit, clearance LL is set to zero. When clearance LL
       returns Inf, lower limit was not defined, so the signal was not tested against it. You can
       interpret Inf as passing lower limit with maximum clearance.

      •     min clearance —

     min clearance is the minimum, overall distance between signal in and the limits. min
      clearance is the minimum of clearance UL and clearance LL. If the signal fails the limit test
       at any point, min clearance is set to zero. When min clearance returns Inf, neither upper


                                                   © National Instruments 1035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1036 ordinal=1036 -->
## Functions

Functions


                  limit nor lower limit were defined, so the signal was not tested against them. You can
                  interpret Inf as passing both upper limit and lower limit with maximum clearance.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Limit Testing Measurement.vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Limit Testing for Unevenly Sampled Data.vi
    LimitLimit SpecificationSpecification

       Creates continuous or segmented masks in the time domain or in the frequency
      domain. You can use different instances of this VI to create multiple limits. Wire data to
       the Specification Cluster input to determine the polymorphic instance to use or
      manually select the instance.


            • Create Continuous Mask VI
            • Create Segmented Mask VI

      You specify the y-axis values in terms of numeric values and use this VI with the Limit
       Testing VI to do limit testing. Wire the Limit Specification VI and the Limit Testing VI in
       either a For Loop or a While Loop. Set Reset to FALSE, unless you want to change the
        limit. The following illustration shows the Limit Specification VI and the Limit Testing
        VI wired together in a While Loop.


1036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1037 ordinal=1037 -->
## Functions

Functions


CreateCreate ContinuousContinuous MaskMask VIVI

Creates continuous or segmented masks in the time domain or in the frequency
domain. You can use different instances of this VI to create multiple limits. Wire data to
the Specification Cluster input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      Reset —

    Reset indicates if the VI computes Limit. If TRUE, the VI computes Limit using the values in the
    Specification Cluster. If FALSE (default), the VI does not compute Limit. The VI always computes
    Limit the first time LabVIEW runs this VI.

   •       Specification Cluster —

    Specification Cluster is a cluster that contains the x-axis and y-axis values at which the limit is
     specified.

         •     X —

       X contains the x-axis values for the limit.

         •      Y —


                                                    © National Instruments 1037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1038 ordinal=1038 -->
## Functions

Functions


               Y contains the numerical y-axis values for the limit.

               To specify y-axis values using formulas, use the Limit Specification By Formula VI.


               •     dx —

          dx is the x-axis interval between points in the input data to compare against the limits. The VI
            uses this value to interpolate the y-axis data for the limit.

               •      x0 —

           x0 is the starting x-axis value of the input data to compare against the limits. The limit is
            undefined for values of xthat are smaller than the first element in the input array X.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Limit —

            Limit contains a continuous mask, as defined by Specification Cluster, dx, and x0.

                     •      x0 —

               x0 is the starting x-axis value of the limit.

                     •     dx —

              dx is the x-axis interval between points in the limit.

                     •      Y —

               Y contains the numerical y-axis values for the limit.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


1038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1039 ordinal=1039 -->
## Functions

Functions

You specify the y-axis values in terms of numeric values and use this VI with the Limit
Testing VI to do limit testing. Wire the Limit Specification VI and the Limit Testing VI in
either a For Loop or a While Loop. Set Reset to FALSE, unless you want to change the
limit. The following illustration shows the Limit Specification VI and the Limit Testing
VI wired together in a While Loop.


CreateCreate SegmentedSegmented MaskMask VIVI

Creates continuous or segmented masks in the time domain or in the frequency
domain. You can use different instances of this VI to create multiple limits. Wire data to
the Specification Cluster input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      Reset —

    Reset indicates if the VI computes Limit. If TRUE, the VI computes Limit using the values in the
    Specification Cluster. If FALSE (default), the VI does not compute Limit. The VI always computes
    Limit the first time LabVIEW runs this VI.

   •       Specification Cluster —

    Specification Cluster is an array of clusters that contains the x-axis and y-axis values at which
    the limit is specified. The ith element in the array defines the ith segment in the segmented
    mask.


                                                    © National Instruments 1039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1040 ordinal=1040 -->
## Functions

Functions


                     •     X —

              X contains the x-axis values for the limit.

                     •      Y —

               Y contains the numerical y-axis values for the limit.

               To specify y-axis values using formulas, use the Limit Specification By Formula VI.


               •     dx —

          dx is the x-axis interval between points in the input data to compare against the limits. The VI
            uses this value to interpolate the y-axis data for the limit.

               •      x0 —

           x0 is the starting x-axis value of the input data to compare against the limits. The limit is
            undefined for values of xthat are smaller than the first element in the input array X.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Limit —

            Limit contains a segmented mask, as defined by Specification Cluster, dx, and x0.

                     •      x0 —

               x0 is the starting x-axis value of the limit.

                     •     dx —

              dx is the x-axis interval between points in the limit.

                     •      Y —

               Y contains the numerical y-axis values for the limit.


               •       error out —

1040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1041 ordinal=1041 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


You specify the y-axis values in terms of numeric values and use this VI with the Limit
Testing VI to do limit testing. Wire the Limit Specification VI and the Limit Testing VI in
either a For Loop or a While Loop. Set Reset to FALSE, unless you want to change the
limit. The following illustration shows the Limit Specification VI and the Limit Testing
VI wired together in a While Loop.


LimitLimit SpecificationSpecification ByBy FormulaFormula

Creates a continuous or segmented mask in the time domain or in the frequency
domain. You can use different instances of this VI to create multiple limits. Wire data to
the Specification Cluster input to determine the polymorphic instance to use or
manually select the instance.


  • Create Continuous Mask using Formula VI
  • Create Segmented Mask using Formula VI

You specify the y-axis values in terms of formulas and use this VI with the Limit Testing
VI to do limit testing. Wire the Limit Specification by Formula VI and the Limit Testing VI
in either a For Loop or a While Loop. Set Reset to FALSE, unless you want to change the
limit. The following illustration shows the Limit Specification by Formula VI and the
Limit Testing VI wired together in a While Loop.


                                                    © National Instruments 1041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1042 ordinal=1042 -->
## Functions

Functions


    CreateCreate ContinuousContinuous MaskMask usingusing FormulaFormula VIVI

       Creates a continuous or segmented mask in the time domain or in the frequency
      domain. You can use different instances of this VI to create multiple limits. Wire data to
       the Specification Cluster input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      Reset —

            Reset indicates if the VI computes Limit. If TRUE, the VI computes Limit using the values in the
             Specification Cluster. If FALSE (default), the VI does not compute Limit. The VI always computes
            Limit the first time LabVIEW runs this VI.

               •       Specification Cluster —

             Specification Cluster is a cluster that contains the x-axis and y-axis values at which the limit is
              specified.

                     •     X —

              X contains the x-axis values for the limit.

                     •      Y —


1042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1043 ordinal=1043 -->
## Functions

Functions


      Y contains the y-axis values described by formulas, such as -92.5+21.5*log2(x) where xis
      the x-axis value. You can enter only single-variable formulas. You also can use constants,
      such as -95.0, for the y-axis values.


•     dx —

  dx is the x-axis interval between points in the input data to compare against the limits. The VI
  uses this value to interpolate the y-axis data for the limit.

•      x0 —

  x0 is the starting x-axis value of the input data to compare against the limits. The limit is
  undefined for values of xthat are smaller than the first element in the input array X.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Limit —

  Limit contains a continuous mask, as defined by Specification Cluster, dx, and x0.

      •      x0 —

      x0 is the starting x-axis value of the limit.

      •     dx —

      dx is the x-axis interval between points in the limit.

      •      Y —

      Y contains the numerical y-axis values for the limit.


•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 1043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1044 ordinal=1044 -->
## Functions

Functions

      You specify the y-axis values in terms of formulas and use this VI with the Limit Testing
        VI to do limit testing. Wire the Limit Specification by Formula VI and the Limit Testing VI
        in either a For Loop or a While Loop. Set Reset to FALSE, unless you want to change the
        limit. The following illustration shows the Limit Specification by Formula VI and the
       Limit Testing VI wired together in a While Loop.


    CreateCreate SegmentedSegmented MaskMask usingusing FormulaFormula VIVI

       Creates a continuous or segmented mask in the time domain or in the frequency
      domain. You can use different instances of this VI to create multiple limits. Wire data to
       the Specification Cluster input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      Reset —

            Reset indicates if the VI computes Limit. If TRUE, the VI computes Limit using the values in the
             Specification Cluster. If FALSE (default), the VI does not compute Limit. The VI always computes
            Limit the first time LabVIEW runs this VI.

               •       Specification Cluster —

             Specification Cluster is an array of clusters that contains the x-axis and y-axis values at which
            the limit is specified. The ith element in the array defines the ith segment in the segmented
           mask.


1044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1045 ordinal=1045 -->
## Functions

Functions


      •     X —

     X contains the x-axis values for the limit.

      •      Y —

      Y contains the y-axis values described by formulas, such as -92.5+21.5*log2(x) where xis
      the x-axis value. You can enter only single-variable formulas. You also can use constants,
      such as -95.0, for the y-axis values.


•     dx —

  dx is the x-axis interval between points in the input data to compare against the limits. The VI
  uses this value to interpolate the y-axis data for the limit.

•      x0 —

  x0 is the starting x-axis value of the input data to compare against the limits. The limit is
  undefined for values of xthat are smaller than the first element in the input array X.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Limit —

  Limit contains a segmented mask, as defined by Specification Cluster, dx, and x0.

      •      x0 —

      x0 is the starting x-axis value of the limit.

      •     dx —

      dx is the x-axis interval between points in the limit.

      •      Y —

      Y contains the numerical y-axis values for the limit.


•       error out —

                                                   © National Instruments 1045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1046 ordinal=1046 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      You specify the y-axis values in terms of formulas and use this VI with the Limit Testing
        VI to do limit testing. Wire the Limit Specification by Formula VI and the Limit Testing VI
        in either a For Loop or a While Loop. Set Reset to FALSE, unless you want to change the
        limit. The following illustration shows the Limit Specification by Formula VI and the
       Limit Testing VI wired together in a While Loop.


   WaveformWaveform PeakPeak DetectionDetection

       Finds the locations, amplitudes, and second derivatives of peaks and valleys in Signal
        In. Wire data to the Signal In input to determine the polymorphic instance to use or
      manually select the instance.

       This VI is similar to the Peak Detector VI.


            • Waveform Peak Detection for 1 Chan VI
            • Waveform Peak Detection for N Chan VI

       Refer to the support document at ni.com for more information about peak detection
       using LabVIEW.
   WaveformWaveform PeakPeak DetectionDetection forfor 11 ChanChan VIVI

       Finds the locations, amplitudes, and second derivatives of peaks and valleys in Signal

1046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1047 ordinal=1047 -->
## Functions

Functions

In. Wire data to the Signal In input to determine the polymorphic instance to use or
manually select the instance.

This VI is similar to the Peak Detector VI.


Inputs/Outputs

   •      peaks/valleys —

    peaks/valleys indicates whether to find peaks or valleys.

    0            Peaks
    1              Valleys

   •      Signal In —

    Signal In contains the waveform in which to find peaks or valleys.

   •      threshold —

    threshold instructs the VI to ignore peaks and valleys that are too small. The VI ignores peaks if
    the fitted amplitude is less than threshold. The VI ignores valleys if the fitted trough is greater
    than threshold.

   •      width —

    width specifies the number of consecutive data points to use in the quadratic least squares fit.
    The value should be no more than about 1/2 of the half-width of the peak/valley and can be
   much smaller (but > 2) for noise-free data. Large widths can reduce the apparent amplitude of
    peaks and shift the apparent location. For noisy data, this modification is not important because
    the noise obscures the actual peak.

   •       error in —


                                                    © National Instruments 1047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1048 ordinal=1048 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        initialize (T) —

               initialize, when TRUE (default), causes the VI to process the first block of data. The VI requires
          some internal setup that must be done at the start for proper operation.

               •     end of data (T) —

          end of data (T), when TRUE (default), causes the VI to process the last block of data. The VI
            cleans up internal data after the last block has been processed.

               •      # found —

           # found is the number of peaks/valleys found in the current block of data. # found is the size of
            the arrays Locations, Amplitudes, and 2nd Derivatives.

               •      Locations —

            Locations contains the index locations of all peaks or valleys detected in the current block of
             data.

           Because the peak detection algorithm uses a quadratic fit to find the peaks, it actually
             interpolates between the data points. Therefore, the indexes are not integers. In other words,
            the peaks found are not necessarily actual points in the input data but may be at fractions of an
            index and at amplitudes not found in the input array.

           To view the locations in terms of time, use the following equation. Time Locations[i] = t0+
             dt*Locations[i]

               •      Amplitudes —

           Amplitudes contains the amplitudes of peaks or valleys found in the current block of data.

               Note The Locations and Amplitudes might deviate from actual peaks or valleys for
                     noisy signals with large dynamic ranges.

               •     2nd Derivatives —

          2nd Derivatives gives measurements of the second derivative of the amplitude at each of the
           peaks or valleys found in the current block of data.


1048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1049 ordinal=1049 -->
## Functions

Functions

   2nd Derivatives gives an approximate measure of the sharpness of each peak or valley. If you are
    detecting peaks, these values are all negative. If you are detecting valleys, the values are all
     positive.

          Note It is assumed that dt, the time difference between samples, is equal to 1.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Refer to the support document at ni.com for more information about peak detection
using LabVIEW.
WaveformWaveform PeakPeak DetectionDetection forfor NN ChanChan VIVI

Finds the locations, amplitudes, and second derivatives of peaks and valleys in Signal
In. Wire data to the Signal In input to determine the polymorphic instance to use or
manually select the instance.

This VI is similar to the Peak Detector VI.


Inputs/Outputs

   •      peaks/valleys —

    peaks/valleys indicates whether to find peaks or valleys.

    0            Peaks
    1              Valleys

   •      Signals In —

                                                    © National Instruments 1049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1050 ordinal=1050 -->
## Functions

Functions


            Signals In contains the waveforms in which to find peaks or valleys.

               •      threshold —

            threshold instructs the VI to ignore peaks and valleys that are too small. The VI ignores peaks if
            the fitted amplitude is less than threshold. The VI ignores valleys if the fitted trough is greater
           than threshold.

               •      width —

           width specifies the number of consecutive data points to use in the quadratic least squares fit.
          The value should be no more than about 1/2 of the half-width of the peak/valley and can be
         much smaller (but > 2) for noise-free data. Large widths can reduce the apparent amplitude of
           peaks and shift the apparent location. For noisy data, this modification is not important because
            the noise obscures the actual peak.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        initialize (T) —

               initialize, when TRUE (default), causes the VI to process the first block of data. The VI requires
          some internal setup that must be done at the start for proper operation.

               •     end of data (T) —

          end of data (T), when TRUE (default), causes the VI to process the last block of data. The VI
            cleans up internal data after the last block has been processed.

               •      # found —

           # found is the number of peaks/valleys found in the current block of data. # found is the size of
            the arrays Locations, Amplitudes, and 2nd Derivatives.

               •      Locations —

            Locations contains the index locations of all peaks or valleys detected in the current block of
            data for each waveform.

                     •      Locations —


1050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1051 ordinal=1051 -->
## Functions

Functions


      Locations contains the index locations of all peaks or valleys detected in the current block
       of data.

      Because the peak detection algorithm uses a quadratic fit to find the peaks, it actually
       interpolates between the data points. Therefore, the indexes are not integers. In other
      words, the peaks found are not necessarily actual points in the input data but may be at
       fractions of an index and at amplitudes not found in the input array.

      To view the locations in terms of time, use the following equation. Time Locations[i] = t0+
       dt*Locations[i]


•      Amplitudes —

  Amplitudes contains the amplitudes of peaks or valleys found in the current block of data for
  each waveform.

      •      Amplitudes —

      Amplitudes contains the amplitudes of peaks or valleys found in the current block of data.

           Note The Locations and Amplitudes might deviate from actual peaks or valleys
                 for noisy signals with large dynamic ranges.


•     2nd Derivatives —

  2nd Derivatives gives measurements of the second derivative of the amplitude at each of the
  peaks or valleys found in the current block of data for each waveform.

      •     2nd Derivatives —

     2nd Derivatives gives measurements of the second derivative of the amplitude at each of
      the peaks or valleys found in the current block of data.

     2nd Derivatives gives an approximate measure of the sharpness of each peak or valley. If
      you are detecting peaks, these values are all negative. If you are detecting valleys, the
      values are all positive.


                                                   © National Instruments 1051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1052 ordinal=1052 -->
## Functions

Functions


                   Note It is assumed that dt, the time difference between samples, is equal to 1.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Refer to the support document at ni.com for more information about peak detection
       using LabVIEW.
    BasicBasic LevelLevel TriggerTrigger DetectionDetection

       Finds the first level-crossing location in a waveform. You can retrieve the trigger
       location as an index or as a time. The trigger conditions are specified in terms of
       threshold level, slope, and hysteresis. Wire data to the signal in input to determine
       the polymorphic instance to use or manually select the instance.

           Note Do not use the single-channel version of this VI for continuous
              multiple-channel processing.


            • Trigger Detection for 1 Channel VI
            • Trigger Detection for N Channel VI

       This VI can perform single-channel measurements in both one-shot mode (single call)
      and continuous mode (multiple calls with history). It also can perform multichannel
      measurements in both one-shot mode and continuous mode. If you want to make
       multiple-channel measurements in continuous mode, you either must use the
       multichannel version of this VI or use one instance of this VI per channel. This VI
       detects only the first trigger for each channel.

      The single-channel version of this VI is intended primarily for continuous processing of

1052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1053 ordinal=1053 -->
## Functions

Functions

a single channel. Generalizing this behavior to the multichannel case, typically by
using this single-channel VI in a For Loop to continuously process multiple channels by
indexing an array of waveforms, is a misuse of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history,
using reset or restart averaging, results in an unexpected behavior of this VI because
the internal state information is passed from one channel to another.

LabVIEW uses the hysteresis to prevent noise from causing a false trigger. For a rising
edge slope, the signal must pass below level – hysteresis before a trigger level
crossing is detected. For a falling edge slope, the signal must pass above level +
hysteresis before a trigger level crossing is detected. The following graph shows how
LabVIEW uses the hysteresis.


In the previous graph, the white line is the input signal. If the level is 0.5, and the
hysteresis is 0.0, LabVIEW returns the green line that represents the false trigger
caused by the noise. If the hysteresis is 0.15, LabVIEW returns the red line at
approximately 0.125s that represents the valid trigger.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Basic Level Triggering of Waveforms.vi


                                                    © National Instruments 1053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1054 ordinal=1054 -->
## Functions

Functions

    TriggerTrigger DetectionDetection forfor 11 ChannelChannel VIVI

       Finds the first level-crossing location in a waveform. You can retrieve the trigger
       location as an index or as a time. The trigger conditions are specified in terms of
       threshold level, slope, and hysteresis. Wire data to the signal in input to determine
       the polymorphic instance to use or manually select the instance.

           Note Do not use the single-channel version of this VI for continuous
              multiple-channel processing.


      Inputs/Outputs

               •       reset —

             reset specifies whether the history, or internal state, of the VI has to be reset. The default is
            FALSE. The internal state contains the final state of the input signal. The VI uses this as the initial
              state the next time LabVIEW calls the VI.

               •       signal in —

             signal in contains the signal in which to detect a trigger.

               •       level —

             level specifies the threshold value signal in must cross before a trigger is detected. The default is
               0.

               •       hysteresis —

             hysteresis specifies the amount above or below level through which signal in must pass before
           a trigger level crossing is detected. The default is 0.


1054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1055 ordinal=1055 -->
## Functions

Functions


  Trigger hysteresis is used to prevent noise from causing a false trigger. For a rising edge trigger
  slope, the signal must pass below level – hysteresis before a trigger level crossing is detected.
  For a falling edge trigger slope, the signal must pass above level + hysteresis before a trigger
  level crossing is detected.

•       location mode —

  location mode specifies whether you want to retrieve the trigger location as an index into the Y-
  array of the waveform or as a point in time in seconds.

  0 Index (default)—Retrieves the trigger location in terms of an array index.
   Time—Retrieves the trigger location in terms of time in seconds. Time is computed by the
    following equation: time = t0 + (index*dt), where t0 and dt are contained in signal in. Use the
  1   To Time Stamp Function to convert this number to a time stamp data type with a time and date
    format.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       trigger slope —

  trigger slope specifies whether a trigger is detected as signal in crosses level on a rising edge or
  a falling edge

  0 Falling Edge—The VI detects a trigger on the falling edge, or negative slope.
  1 Rising Edge (default)—The VI detects a trigger on the rising edge, or positive slope.

•       trigger location —

  trigger location contains the index or time, depending on the location mode setting, of the
  detected trigger. If the location mode is in Time mode and you do not want the trigger location
  value to appear in seconds on the front panel, wire the trigger location to a time stamp.

•       trigger detected? —

  trigger detected? indicates whether the VI detects a valid trigger. If trigger detected? is TRUE,
  the VI detects a valid trigger.

•       error out —


                                                   © National Instruments 1055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1056 ordinal=1056 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


       This VI can perform single-channel measurements in both one-shot mode (single call)
      and continuous mode (multiple calls with history). It also can perform multichannel
      measurements in both one-shot mode and continuous mode. If you want to make
       multiple-channel measurements in continuous mode, you either must use the
       multichannel version of this VI or use one instance of this VI per channel. This VI
       detects only the first trigger for each channel.

      The single-channel version of this VI is intended primarily for continuous processing of
      a single channel. Generalizing this behavior to the multichannel case, typically by
       using this single-channel VI in a For Loop to continuously process multiple channels by
       indexing an array of waveforms, is a misuse of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history,
       using reset or restart averaging, results in an unexpected behavior of this VI because
       the internal state information is passed from one channel to another.

      LabVIEW uses the hysteresis to prevent noise from causing a false trigger. For a rising
      edge slope, the signal must pass below level – hysteresis before a trigger level
       crossing is detected. For a falling edge slope, the signal must pass above level +
       hysteresis before a trigger level crossing is detected. The following graph shows how
      LabVIEW uses the hysteresis.


        In the previous graph, the white line is the input signal. If the level is 0.5, and the
       hysteresis is 0.0, LabVIEW returns the green line that represents the false trigger

1056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1057 ordinal=1057 -->
## Functions

Functions

caused by the noise. If the hysteresis is 0.15, LabVIEW returns the red line at
approximately 0.125s that represents the valid trigger.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Basic Level Triggering of Waveforms.vi
TriggerTrigger DetectionDetection forfor NN ChannelChannel VIVI

Finds the first level-crossing location in a waveform. You can retrieve the trigger
location as an index or as a time. The trigger conditions are specified in terms of
threshold level, slope, and hysteresis. Wire data to the signal in input to determine
the polymorphic instance to use or manually select the instance.

      Note Do not use the single-channel version of this VI for continuous
        multiple-channel processing.


Inputs/Outputs

   •       reset —

    reset specifies whether the history, or internal state, of the VI has to be reset. The default is
    FALSE. The internal state contains the final state of the input signal. The VI uses this as the initial
     state the next time LabVIEW calls the VI.

   •       signal in —


                                                    © National Instruments 1057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1058 ordinal=1058 -->
## Functions

Functions


             signal in contains the signals in which to detect triggers.

               •       level —

             level specifies the threshold value that each signal contained in signal in must cross before a
              trigger is detected. The default is 0.

               •       hysteresis —

             hysteresis specifies the amount above or below level through which each signal contained in
             signal in must pass before a trigger level crossing is detected. The default is 0.

             Trigger hysteresis is used to prevent noise from causing a false trigger. For a rising edge slope,
            the signal must pass below level – hysteresis before a trigger level crossing is detected. For a
               falling edge slope, the signal must pass above level + hysteresis before a trigger level crossing is
             detected.

               •       location mode —

             location mode specifies whether you want to retrieve the trigger location as an index into the Y-
             array of the waveform or as a point in time in seconds.

           0 Index (default)—Retrieves the trigger location in terms of an array index.
            Time—Retrieves the trigger location in terms of time in seconds. Time is computed by the
              following equation: time = t0 + (index*dt), where t0 and dt are contained in signal in. Use the           1
            To Time Stamp Function to convert this number to a time stamp data type with a time and date
              format.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       trigger slope —

             trigger slope specifies whether a trigger is detected on a rising edge or a falling edge as each
             signal contained in signal in crosses level.

           0 Falling Edge—The VI detects a trigger on the falling edge, or negative slope.
           1 Rising Edge (default)—The VI detects a trigger on the rising edge, or positive slope.

               •       trigger locations —


1058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1059 ordinal=1059 -->
## Functions

Functions


     trigger locations contain the index or time value, depending on the location mode setting, of
    the detected trigger for each waveform.

   •       trigger detected? —

     trigger detected? indicates whether the VI detects a valid trigger for each signal.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI can perform single-channel measurements in both one-shot mode (single call)
and continuous mode (multiple calls with history). It also can perform multichannel
measurements in both one-shot mode and continuous mode. If you want to make
multiple-channel measurements in continuous mode, you either must use the
multichannel version of this VI or use one instance of this VI per channel. This VI
detects only the first trigger for each channel.

The single-channel version of this VI is intended primarily for continuous processing of
a single channel. Generalizing this behavior to the multichannel case, typically by
using this single-channel VI in a For Loop to continuously process multiple channels by
indexing an array of waveforms, is a misuse of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history,
using reset or restart averaging, results in an unexpected behavior of this VI because
the internal state information is passed from one channel to another.

LabVIEW uses the hysteresis to prevent noise from causing a false trigger. For a rising
edge slope, the signal must pass below level – hysteresis before a trigger level
crossing is detected. For a falling edge slope, the signal must pass above level +
hysteresis before a trigger level crossing is detected. The following graph shows how
LabVIEW uses the hysteresis.


                                                    © National Instruments 1059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1060 ordinal=1060 -->
## Functions

Functions


        In the previous graph, the white line is the input signal. If the level is 0.5, and the
       hysteresis is 0.0, LabVIEW returns the green line that represents the false trigger
      caused by the noise. If the hysteresis is 0.15, LabVIEW returns the red line at
       approximately 0.125s that represents the valid trigger.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Basic Level Triggering of Waveforms.vi
   MaskMask andand LimitLimit TestingTesting

      Performs limit testing on Signals.


      Dialog Box Options

        Option   Description

                 Contains the following options:
       Upper
         Limit         • Upper constant—


1060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1061 ordinal=1061 -->
## Functions

Functions


Option   Description

           Compares Signals to the value in Upper limit constant. This option is available only
          when you place a checkmark in the Upper Limit checkbox.

      ◦ Upper limit constant—

                   Specifies the value of the Upper constant. The default is 0. This option is
                   available only when you place a checkmark in the Upper Limit checkbox and
                   select the Upper constant option.

                 • Upper mask—

           Compares Signals to the upper limit of a signal from a file or a signal you define. This
             option is available only when you place a checkmark in the Upper Limit checkbox.

      ◦ Define—

                  Displays the Define Signal dialog box, which you use to set the values for the
                   signal you want to use for the limit test. This button is available only when you
                   select Upper Limit and Upper mask or Lower Limit and Lower mask.

                 • Upper inclusive—

               Specifies if you want Pass to return TRUE when points in Signals fall on Upper Limit.
             Place a checkmark in the Upper inclusive checkbox to include points falling on
           Upper Limit in the points that pass the limit test. This option is available only when
            you place a checkmark in the Upper Limit checkbox.

         Contains the following options:

                 • Lower constant—

           Compares Signals to the value in Lower limit constant. This option is available only
          when you place a checkmark in the Lower Limit checkbox.
Lower      ◦ Lower limit constant—Limit
                   Specifies the value of the Lower constant. The default is 0. This option is
                   available only when you place a checkmark in the Lower Limit checkbox and
                   select the Lower constant option.

                 • Lower mask—


                                                    © National Instruments 1061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1062 ordinal=1062 -->
## Functions

Functions


        Option   Description

                   Compares Signals to the lower limit of a signal from a file or a signal you define. This
                      option is available only when you place a checkmark in the Lower Limit checkbox.

          ◦ Define—

                           Displays the Define Signal dialog box, which you use to set the values for the
                             signal you want to use for the limit test. This button is available only when you
                             select Upper Limit and Upper mask or Lower Limit and Lower mask.

                              • Lower inclusive—

                        Specifies if you want Pass to return TRUE when points in Signals fall on Lower Limit.
                      Place a checkmark in the Lower inclusive checkbox to include points falling on
                   Lower Limit in the points that pass the limit test. This option is available only when
                   you place a checkmark in the Lower Limit checkbox.

                   Displays a preview of the measurement. The Result Preview plot indicates the value of
                  the selected measurement with a dotted line.

         Result     If you wire data to the Express VI and run the VI, Result Preview displays real data. If you
        Preview  close and reopen the Express VI, Result Preview displays sample data until you run the VI
                   again. If the cutoff frequency values are invalid, Result Preview does not display valid
                   data.


      Inputs/Outputs

               •       error in —

            Describes error conditions that occur before this node runs.

               •      Signals —

            Contains the input signal or signals.

               •     Lower Limit —

             Specifies the lower limit for mask and limit testing. The value you wire to this input overrides the
            value you set in the configuration dialog box.

               •     Upper Constant —

1062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1063 ordinal=1063 -->
## Functions

Functions


    Compares Signals to the value in Upper Constant. The value you wire to this input overrides the
    value you set in the configuration dialog box.

   •     Lower Constant —

    Compares Signals to the value in Lower Constant. The value you wire to this input overrides the
    value you set in the configuration dialog box.

   •     Upper Limit —

     Specifies the upper limit for mask and limit testing. The value you wire to this input overrides
    the value you set in the configuration dialog box.

   •      Point Evaluation —

    Returns the results of the limit testing at each data point. If Point Evaluation is TRUE, the data
    point is less than or equal to the upper limit and greater than or equal to the lower limit.

   •      Tested Signals —

    Returns the upper and lower limits, the input signal, and the failures.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Passed —

     Indicates the result of limit testing. If Passed is TRUE, the signal is less than or equal to the upper
     limit and greater than or equal to the lower limit.


The Express VI compares Signals with the upper and lower limits you set and returns
the result of the comparison at each data point. The Express VI also returns an array of
waveforms that contains the upper limit and lower limit, the signal, and the failures.

Components

Uses an upper limit for mask and limit testing.

Uses a lower limit for mask and limit testing.


                                                    © National Instruments 1063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1064 ordinal=1064 -->
## Functions

Functions

       Specifies if you want Pass to return TRUE when points in Signals fall on Upper Limit.
       Place a checkmark in the Upper inclusive checkbox to include points falling on Upper
       Limit in the points that pass the limit test. This option is available only when you place
      a checkmark in the Upper Limit checkbox.

       Specifies if you want Pass to return TRUE when points in Signals fall on Lower Limit.
       Place a checkmark in the Lower inclusive checkbox to include points falling on Lower
       Limit in the points that pass the limit test. This option is available only when you place
      a checkmark in the Lower Limit checkbox.

      Uses a lower limit for mask and limit testing. Contains the following options:

      Uses a upper limit for mask and limit testing. Contains the following options:

       Specifies the value of the Upper constant. The default is 0. This option is available only
     when you place a checkmark in the Upper Limit checkbox and select the Upper
       constant option.

       Specifies the value of the Lower constant. The default is 0. This option is available only
     when you place a checkmark in the Lower Limit checkbox and select the Lower
       constant option.

      Compares Signals to the value in Upper limit constant. This option is available only
     when you place a checkmark in the Upper Limit checkbox.

      Compares Signals to the value in Lower limit constant. This option is available only
     when you place a checkmark in the Lower Limit checkbox.

       Displays the Define Signal dialog box, which you use to set the values for the signal you
      want to use for the limit test. This button is available only when you select Upper Limit
      and Upper mask or Lower Limit and Lower mask.

      Compares Signals to the lower limit of a signal from a file or a signal you define. This
       option is available only when you place a checkmark in the Lower Limit checkbox.

      Compares Signals to the upper limit of a signal from a file or a signal you define. This
       option is available only when you place a checkmark in the Upper Limit checkbox.

       Displays a preview of the measurement. The Result Preview plot indicates the value of

1064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1065 ordinal=1065 -->
## Functions

Functions

the selected measurement with a dotted line.
TriggerTrigger andand GateGate

Uses triggering to extract a segment out of a signal. The trigger conditions can be
based on a start or stop trigger threshold or can be static. When a trigger condition is
static, the trigger occurs immediately and this Express VI returns a predefined number
of samples.


Dialog Box Options

 Option   Description

          Contains the following options:

                   • Threshold—

             Uses a threshold to indicate when to start triggering.

       ◦  Start sense—

                    Specifies on what edge of the signal to start taking samples. The options are
                   Rising edge, Rising or Falling edge, or Falling edge. This option is available only
               when you select Threshold. Start
 Trigger       ◦  Start level—

                  Amplitude that the signal must cross in the Start sense direction before the
                   Express VI starts taking samples. The default is 0. This option is available only
               when you select Threshold.

       ◦ Pre samples—

                    Specifies the number of samples that occur before the start trigger to return.
                The default is 0. This option is available only when you select Threshold.


                                                    © National Instruments 1065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1066 ordinal=1066 -->
## Functions

Functions


        Option   Description

                              • Immediate—

                      Begins the triggering immediately. The start of the signal is the start trigger.

                  Contains the following options:

                              • Number of samples—

                    Ends the triggering when the Express VI collects Samples.

          ◦ Samples—

                             Specifies the number of samples to collect before stopping the trigger. The
                             default is 1000.

                              • Threshold—
        Stop                     Uses a threshold to indicate when to start triggering.
         Trigger
          ◦ Stop sense—

                             Specifies on what edge of the signal to stop taking samples. The options are
                            Rising edge, Rising or Falling edge, or Falling edge. This option is available only
                     when you select Threshold.

          ◦ Stop level—

                         Amplitude that the signal must cross in the Stop sense direction before the
                           Express VI stops taking samples. The default is 0. This option is available only
                     when you select Threshold.

                  Contains the following options:

                              •  Trigger channel—

        General       Specifies the channel to use if the dynamic data type input contains multiple
                          signals. The default is 0.

                              • Reset after each trigger found—


1066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1067 ordinal=1067 -->
## Functions

Functions


Option   Description

              Resets the trigger conditions after finding each trigger. When you select this option,
              the Trigger and Gate Express VI does not buffer data with each iteration of a loop.
               Select this checkbox when you have a new data set for each iteration and you want
               to find data related only to the first trigger point. Deselect this checkbox when you
            want to pass only one set of data into a loop and then call the Trigger and Gate
              Express VI in a loop to get all the triggers in the data.

                 Note When you do not select this option, the Trigger and Gate Express VI
                        buffers data. In this case, if the Trigger and Gate Express VI is called in a
                        loop, it can start a backlog of data if there is new data for each loop
                      (because one set of data can contain several trigger points). Because
                       there is no reset, it buffers all the data from each loop so that it can find
                              all the triggers, but all the triggers might not be found.

                 • Remain triggered after trigger found—

            Remains triggered after finding a trigger. This option is available only when you
               select the Threshold option in the Start Trigger section.

                 • Hysteresis—

               Specifies the amount above and below Start level or Stop level through which
              Signals must pass before a trigger level crossing is detected. The default is 0.

            Use trigger hysteresis to prevent noise from causing a false trigger. For a rising edge
               Start sense or Stop sense, the signal must pass below Start level or Stop level
            minus Hysteresis before detecting a trigger level crossing. For a falling edge Start
             sense or Stop sense, the signal must pass above Start level or Stop level plus
              Hysteresis before detecting a trigger level crossing.

          Contains the following options:

                 • Automatic number of samples—

Output        Specifies that the Express VI returns the portion of the signal that matches the
segment      trigger criteria.
size
                 • Number of output samples—

               Specifies the number of samples to include in each output segment. This option is


                                                    © National Instruments 1067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1068 ordinal=1068 -->
## Functions

Functions


        Option   Description

                        available only if the Automatic number of samples checkbox does not contain a
                     checkmark.


                   Displays the input signal.

                              If you wire data to the Express VI and run it, Input Signal displays real data. If you close
                and reopen the Express VI, Input Signal displays sample data until you run the Express VI        Input
                    again.         Signal
                              • Number of points in the data—

                         Specifies the number of points in the data. The default is 4400.


                   Displays a preview of the measurement. The Results Preview plot indicates the value of
                  the selected measurement with a dotted line.
         Results                              If you wire data to the Express VI and run the VI, Results Preview displays real data. If you
        Preview                   close and reopen the Express VI, Results Preview displays sample data until you run the
                     VI again. If the cutoff frequency values are invalid, Results Preview does not display valid
                    data.


      Inputs/Outputs

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Signals —

            Contains the input signal or signals.

               •      Reset —

            Controls the initialization of the internal state of the VI. The default is FALSE.

               •      Data Index —


1068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1069 ordinal=1069 -->
## Functions

Functions


    Contains the index of the detected trigger. If this Express VI is in a loop, wire Data Index to the
     iteration terminal of the loop.

   •     Manual Trigger —

     Starts the trigger immediately and overrides the Start Trigger settings you configure. The default
      is FALSE.

   •      Data Available —

     Indicates if data is available that meets the requirements of the trigger.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Previous Signals —

    Contains the last triggered output data. If no data meets the requirements of the trigger, this
    output contains the most recent segment that meet the requirements of the trigger.

   •      Triggered Signals —

    Returns the resulting segment between Start Trigger and Stop Trigger. If no data meets the
    requirements of the trigger, this output returns an empty signal.


Components

Specifies that the Express VI returns the portion of the signal that matches the trigger
criteria.

Resets the trigger conditions after finding each trigger. When you select this option, the
Trigger and Gate Express VI does not buffer data with each iteration of a loop. Select
this checkbox when you have a new data set for each iteration and you want to find
data related only to the first trigger point. Deselect this checkbox when you want to
pass only one set of data into a loop and then call the Trigger and Gate Express VI in a
loop to get all the triggers in the data.

Specifies the number of points in the data. The default is 4400.


                                                    © National Instruments 1069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1070 ordinal=1070 -->
## Functions

Functions

       Displays a preview of the measurement. The Results Preview plot indicates the value
       of the selected measurement with a dotted line.

       Displays the input signal.

      Amplitude that the signal must cross in the Stop sense direction before the Express VI
       stops taking samples. The default is 0. This option is available only when you select
       Threshold.

       Specifies on what edge of the signal to stop taking samples. The options are Rising
       edge, Rising or Falling edge, or Falling edge. This option is available only when you
        select Threshold.

      Uses a threshold to indicate when to start triggering.

      Ends the triggering when the Express VI collects Samples.

       Specifies the amount above and below Start level or Stop level through which Signals
      must pass before a trigger level crossing is detected. The default is 0.

       Specifies on what edge of the signal to start taking samples. The options are Rising
       edge, Rising or Falling edge, or Falling edge. This option is available only when you
        select Threshold.

      Uses a threshold to indicate when to stop triggering.

      Amplitude that the signal must cross in the Start sense direction before the Express VI
        starts taking samples. The default is 0. This option is available only when you select
       Threshold.

       Begins the triggering immediately. The start of the signal is the start trigger.

      Remains triggered after finding a trigger. This option is available only when you select
       the Threshold option in the Start Trigger section.

       Specifies the number of samples to include in each output segment. This option is
       available only if the Automatic number of samples checkbox does not contain a
      checkmark.


1070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1071 ordinal=1071 -->
## Functions

Functions

Specifies the channel to use if the dynamic data type input contains multiple signals.
The default is 0.

Specifies the number of samples to collect before stopping the trigger. The default is
1000.

Specifies the number of samples that occur before the start trigger to return. The
default is 0. This option is available only when you select Threshold.

Contains the following options:

Contains the following options:
TransitionTransition MeasurementsMeasurements

Accepts an input signal of a single waveform or an array of waveforms and measures
the transition duration (rise or fall time), slew rate, undershoot, and overshoot of a
selected positive or negative transition in each waveform. Wire data to the signal in
input to determine the polymorphic instance to use or manually select the instance.

      Note The terminology and measurement definitions for this VI comply with
     IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
     andRelatedWaveforms.


  • Transition Measurements 1 chan VI
  • Transition Measurements N chan VI

The following information applies to the pre-transition and post-transition outputs of
both instances of this VI.
pre-transition

To calculate the pre-transition undershoot and overshoot, LabVIEW searches for a

                                                    © National Instruments 1071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1072 ordinal=1072 -->
## Functions

Functions

        local minimum and maximum in the pre-transition aberration region immediately
       preceding the beginning of the transition specified by edge number and polarity. The
       pre-transition aberration region is defined as the minimum of 3*(end time – start time)
      and (current transition start time – previous transition end time) / 2. If the transition to
      measure is the first in the waveform, the interval is defined as the minimum of 3*(end
      time – start time) and (start time – beginning of the waveform).

           If polarity is falling, LabVIEW calculates the pre-transition undershoot using the
       following equation:


           If polarity is rising, LabVIEW calculates the pre-transition undershoot using the
       following equation:


           If polarity is falling, LabVIEW calculates the pre-transition overshoot using the
       following equation:


           If polarity is rising, LabVIEW calculates the pre-transition overshoot using the
       following equation:


           Note LabVIEW uses the Histogram method to calculate the state levels and
              amplitude, regardless of the method specified by percent level settings.

      post-transition

      To calculate the post-transition undershoot and overshoot, LabVIEW searches for a
        local minimum and maximum in the post-transition aberration region immediately
       following the end of the transition specified by edge number and polarity. The post-
        transition aberration region is defined as the minimum of 3*(end time – start time) and

1072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1073 ordinal=1073 -->
## Functions

Functions

(next transition start time – current transition end time) / 2. If the transition to measure
is the last in the waveform, the interval is defined as the minimum of 3*(end time –
start time) and (end of the waveform – end time).

If polarity is falling, LabVIEW calculates the post-transition undershoot using the
following equation:


If polarity is rising, LabVIEW calculates the post-transition undershoot using the
following equation:


If polarity is falling, LabVIEW calculates the post-transition overshoot using the
following equation:


If polarity is rising, LabVIEW calculates the post-transition overshoot using the
following equation:


      Note LabVIEW uses the Histogram method to calculate the state levels and
       amplitude, regardless of the method specified by percent level settings.

Example Illustrations

The following illustration shows the undershoot and overshoot in a negative single
transition.


                                                    © National Instruments 1073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1074 ordinal=1074 -->
## Functions

Functions


      The following illustration shows the undershoot and overshoot in a positive single
        transition.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Pulse and Transition Measurements.vi
            • labview\examples\Signal Processing\Waveform
        Measurements\N channel Pulse and Transition
        Measurements.vi


1074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1075 ordinal=1075 -->
## Functions

Functions

TransitionTransition MeasurementsMeasurements 11 chanchan VIVI

Accepts an input signal of a single waveform or an array of waveforms and measures
the transition duration (rise or fall time), slew rate, undershoot, and overshoot of a
selected positive or negative transition in each waveform. Wire data to the signal in
input to determine the polymorphic instance to use or manually select the instance.

      Note The terminology and measurement definitions for this VI comply with
     IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
     andRelatedWaveforms.


Inputs/Outputs

   •      edge number (1) —

    edge number specifies the transition to measure.

   An edge number of nwith rising polarity selected indicates that the VI measures the nth rising
     transition it detects in the input waveform.

   •       signal in —

    signal in is the waveform to measure. The waveform is required to contain at least edge number
     transitions in the direction specified by polarity.

    A rising transition is the interval between adjacent rising low ref level and high ref level
     crossings. A falling transition is the interval between adjacent falling high ref level and low ref
     level crossings.

   •       polarity (rising) —

    polarity specifies the direction of the transition to measure as rising (default) or falling.


                                                    © National Instruments 1075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1076 ordinal=1076 -->
## Functions

Functions

               •      reference levels —

            reference levels specifies the high and low reference levels required to determine the transition
              interval. mid ref level is not used in transition measurements.

            Reference levels provide a means to identify the position in time of the waveform feature
           measured.

                     •      high ref level —

                high ref level specifies the high reference level of the waveform in percent (default) or
                absolute units.

              A rising high ref level crossing defines the end of a rising transition and a falling high ref
                  level crossing defines the beginning of a falling transition.

                     •     mid ref level —

             mid ref level specifies the middle reference level in percent (default) or absolute units. mid
                   ref level is not used in transition measurements.

                     •      low ref level —

              low ref level specifies the low reference level of the waveform in percent (default) or
                absolute units.

              A rising low ref level crossing defines the beginning of a rising transition and a falling low
                   ref level crossing defines the end of a falling transition.

                     •       ref units —

                   ref units specifies whether the high ref level, mid ref level, and low ref level inputs are
                 interpreted as a percentage (default) of the full range of the waveform or as absolute levels.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      percent level settings —

            percent level settings specifies the method LabVIEW uses to determine the high and low state
              levels of a waveform.


1076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1077 ordinal=1077 -->
## Functions

Functions


   If you select percent ref units, percent level settings determines the reference levels. Otherwise,
  LabVIEW ignores this input.

      •     method —

     method specifies how LabVIEW computes the high and low state levels of the waveform.

       Histogram—Returns the levels of the histogram bins with the maximum number of hits in
        the upper and lower regions of the waveform. The upper and lower regions of the
      0       waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
       waveform.
      1 Peak—Searches the entire waveform for its maximum and minimum levels.
       Auto select (default)—Determines whether the histogram bins that correspond to the high
      and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
      2 results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
        either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
       histogram fails).

      •      histogram size —

      histogram size specifies the number of bins in the histogram LabVIEW uses to determine
      the high and low state levels of the waveform.

      •      histogram method —

      histogram method specifies how LabVIEW computes the high and low state levels of the
      waveform. Currently, mode is the only available histogram method.

      0           mode

      •      reserved —

      reserved is reserved for future use.


•      slope —

  slope is a measure of the rate of change of the signal in a transition region between high ref
  level and low ref level.


                                                   © National Instruments 1077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1078 ordinal=1078 -->
## Functions

Functions


            slope is given by the following equation.                              where transition
            duration is the transition duration for either rising or falling transition polarity and high ref level
          and low ref level are in absolute units.

               •       transition duration —

             transition duration is the time span from when the waveform crosses the low ref level until it
            crosses the high ref level in seconds for a rising transition polarity.

          The measurement starts at the left edge of the waveform and finds all low ref level crossings
            preceding the first high ref level crossing. The final low ref level crossing is used in the
              calculation. A rising polarity transition duration is known as rise time, and a falling polarity
              transition duration is known as fall time, as shown in the following example:


               •       pre-transition —

             pre-transition contains the undershoot and overshoot for the waveform in signal in.

             Refer to the Details section for more information about the pre-transition output.

                     •      undershoot (%) —

               undershoot measures the height of the local minimum preceding a rising or falling
                   transition, which depends on the polarity you specify. Undershoot measures the height as a
                percentage of the histogram-based amplitude of the signal.

                     •      overshoot (%) —

               overshoot measures the height of the local maximum preceding a rising or falling


1078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1079 ordinal=1079 -->
## Functions

Functions


       transition, which depends on the polarity you specify. Overshoot measures the height as a
      percentage of the histogram-based amplitude of the signal.


•       post-transition —

  post-transition contains the undershoot and overshoot for the waveform in signal in.

  Refer to the Details section for more information about the post-transition output.

      •      undershoot (%) —

      undershoot measures the height of the local minimum following a rising or falling, as set by
       polarity, transition as a percentage of the histogram-based amplitude of the signal.

      •      overshoot (%) —

      overshoot measures the height of the local maximum following a rising or falling, as set by
       polarity, transition as a percentage of the histogram-based amplitude of the signal.


•       error out —

  error out contains error information. This output provides standard error out functionality.

•     measurement info —

  measurement info returns the transition interval end points and the absolute reference levels
  used to define the transition.

      •       start time —

       start time specifies the time of the rising (falling) low (high) ref level crossing that defines
      the start of the transition to be measured.

      •     end time —

     end time specifies the time of the rising (falling) high (low) ref level crossing that defines the
     end of the transition to be measured.

      •       ref levels —


                                                   © National Instruments 1079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1080 ordinal=1080 -->
## Functions

Functions


                   ref levels returns the three user-defined reference levels of the waveform in absolute units.

              LabVIEW uses the reference levels to define the interval of one cycle measurement.

                           •      high ref level —

                    high ref level returns the high reference level.

                           •     mid ref level —

                 mid ref level returns the middle reference level.

                           •      low ref level —

                  low ref level returns the low reference level.

                           •       ref units —

                        ref units is always absolute in measurement info.


      The following information applies to the pre-transition and post-transition outputs of
      both instances of this VI.
      pre-transition

      To calculate the pre-transition undershoot and overshoot, LabVIEW searches for a
        local minimum and maximum in the pre-transition aberration region immediately
       preceding the beginning of the transition specified by edge number and polarity. The
       pre-transition aberration region is defined as the minimum of 3*(end time – start time)
      and (current transition start time – previous transition end time) / 2. If the transition to
      measure is the first in the waveform, the interval is defined as the minimum of 3*(end
      time – start time) and (start time – beginning of the waveform).

           If polarity is falling, LabVIEW calculates the pre-transition undershoot using the
       following equation:


1080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1081 ordinal=1081 -->
## Functions

Functions


If polarity is rising, LabVIEW calculates the pre-transition undershoot using the
following equation:


If polarity is falling, LabVIEW calculates the pre-transition overshoot using the
following equation:


If polarity is rising, LabVIEW calculates the pre-transition overshoot using the
following equation:


      Note LabVIEW uses the Histogram method to calculate the state levels and
       amplitude, regardless of the method specified by percent level settings.

post-transition

To calculate the post-transition undershoot and overshoot, LabVIEW searches for a
local minimum and maximum in the post-transition aberration region immediately
following the end of the transition specified by edge number and polarity. The post-
transition aberration region is defined as the minimum of 3*(end time – start time) and
(next transition start time – current transition end time) / 2. If the transition to measure
is the last in the waveform, the interval is defined as the minimum of 3*(end time –
start time) and (end of the waveform – end time).

If polarity is falling, LabVIEW calculates the post-transition undershoot using the
following equation:


If polarity is rising, LabVIEW calculates the post-transition undershoot using the

                                                    © National Instruments 1081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1082 ordinal=1082 -->
## Functions

Functions

       following equation:


           If polarity is falling, LabVIEW calculates the post-transition overshoot using the
       following equation:


           If polarity is rising, LabVIEW calculates the post-transition overshoot using the
       following equation:


           Note LabVIEW uses the Histogram method to calculate the state levels and
              amplitude, regardless of the method specified by percent level settings.

     Example Illustrations

      The following illustration shows the undershoot and overshoot in a negative single
        transition.


      The following illustration shows the undershoot and overshoot in a positive single
        transition.


1082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1083 ordinal=1083 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Pulse and Transition Measurements.vi
  • labview\examples\Signal Processing\Waveform
   Measurements\N channel Pulse and Transition
   Measurements.vi
TransitionTransition MeasurementsMeasurements NN chanchan VIVI

Accepts an input signal of a single waveform or an array of waveforms and measures
the transition duration (rise or fall time), slew rate, undershoot, and overshoot of a
selected positive or negative transition in each waveform. Wire data to the signal in
input to determine the polymorphic instance to use or manually select the instance.

      Note The terminology and measurement definitions for this VI comply with
     IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
     andRelatedWaveforms.


                                                    © National Instruments 1083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1084 ordinal=1084 -->
## Functions

Functions


      Inputs/Outputs

               •      edge number (1) —

           edge number specifies the transition to measure.

          An edge number of nwith rising polarity selected indicates that the VI measures the nth rising
              transition it detects in the input waveform.

               •       signal(s) in —

              signal(s) in is the array of waveforms to measure. The waveform is required to contain at least
           edge number transitions in the direction specified by polarity.

          A rising transition is the interval between adjacent rising low ref level and high ref level
             crossings. A falling transition is the interval between adjacent falling high ref level and low ref
             level crossings.

               •       polarity (rising) —

             polarity specifies the direction of the transition to measure as rising (default) or falling.

               •      reference levels —

            reference levels specifies the high and low reference levels required to determine the transition
              interval. mid ref level is not used in transition measurements.

            Reference levels provide a means to identify the position in time of the waveform feature
           measured.

                     •      high ref level —

                high ref level specifies the high reference level of the waveform in percent (default) or
                absolute units.

              A rising high ref level crossing defines the end of a rising transition and a falling high ref
                  level crossing defines the beginning of a falling transition.


1084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1085 ordinal=1085 -->
## Functions

Functions


      •     mid ref level —

     mid ref level specifies the middle reference level in percent (default) or absolute units. mid
       ref level is not used in transition measurements.

      •      low ref level —

      low ref level specifies the low reference level of the waveform in percent (default) or
      absolute units.

     A rising low ref level crossing defines the beginning of a rising transition and a falling low
       ref level crossing defines the end of a falling transition.

      •       ref units —

       ref units specifies whether the high ref level, mid ref level, and low ref level inputs are
       interpreted as a percentage (default) of the full range of the waveform or as absolute levels.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      percent level settings —

  percent level settings specifies the method LabVIEW uses to determine the high and low state
  levels of a waveform.

   If you select percent ref units, percent level settings determines the reference levels. Otherwise,
  LabVIEW ignores this input.

      •     method —

     method specifies how LabVIEW computes the high and low state levels of the waveform.

       Histogram—Returns the levels of the histogram bins with the maximum number of hits in
        the upper and lower regions of the waveform. The upper and lower regions of the
      0
       waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
       waveform.
      1 Peak—Searches the entire waveform for its maximum and minimum levels.


                                                   © National Instruments 1085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1086 ordinal=1086 -->
## Functions

Functions


                Auto select (default)—Determines whether the histogram bins that correspond to the high
               and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
               2 results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
                   either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
                 histogram fails).

                     •      histogram size —

               histogram size specifies the number of bins in the histogram LabVIEW uses to determine
                the high and low state levels of the waveform.

                     •      histogram method —

               histogram method specifies how LabVIEW computes the high and low state levels of the
               waveform. Currently, mode is the only available histogram method.

               0           mode

                     •      reserved —

                reserved is reserved for future use.


               •      slope —

            slope is an array containing the slew rate for each waveform in signal(s) in. slope is a measure of
            the rate of change of the signal in a transition region between high ref level and low ref level.

            slope is given by the following equation.                              where transition
            duration is the transition duration for either rising or falling transition polarity and high ref level
          and low ref level are in absolute units.

               •       transition duration —

             transition duration is an array of the time spans from when each waveform crosses the low ref
             level until it crosses the high ref level in seconds for a rising transition polarity.

          The measurement starts at the left edge of the waveform and finds all low ref level crossings
            preceding the first high ref level crossing. The final low ref level crossing is used in the
              calculation. A rising polarity transition duration is known as rise time, and a falling polarity


1086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1087 ordinal=1087 -->
## Functions

Functions


  transition duration is known as fall time, as shown in the following example:


•       pre-transition —

  pre-transition contains the undershoot and overshoot for each waveform in signal(s) in.

  Refer to the Details section for more information about the pre-transition output.

      •      undershoot (%) —

      undershoot measures the height of the local minimum preceding a rising or falling
       transition, which depends on the polarity you specify. Undershoot measures the height as a
      percentage of the histogram-based amplitude of the signal.

      •      overshoot (%) —

      overshoot measures the height of the local maximum preceding a rising or falling
       transition, which depends on the polarity you specify. Overshoot measures the height as a
      percentage of the histogram-based amplitude of the signal.


•       post-transition —

  post-transition contains the undershoot and overshoot for each waveform in signal(s) in.

  Refer to the Details section for more information about the post-transition output.

      •      undershoot (%) —

      undershoot measures the height of the local minimum following a rising or falling, as set by


                                                   © National Instruments 1087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1088 ordinal=1088 -->
## Functions

Functions


                  polarity, transition as a percentage of the histogram-based amplitude of the signal.

                     •      overshoot (%) —

               overshoot measures the height of the local maximum following a rising or falling, as set by
                  polarity, transition as a percentage of the histogram-based amplitude of the signal.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurement info —

          measurement info is an array of clusters containing measurement information for each input
           waveform.

                     •       start time —

                  start time specifies the time of the rising (falling) low (high) ref level crossing that defines
                the start of the transition to be measured.

                     •     end time —

              end time specifies the time of the rising (falling) high (low) ref level crossing that defines the
              end of the transition to be measured.

                     •       ref levels —

                   ref levels returns the three user-defined reference levels of the waveform in absolute units.

              LabVIEW uses the reference levels to define the interval of one cycle measurement.

                           •      high ref level —

                    high ref level returns the high reference level.

                           •     mid ref level —

                 mid ref level returns the middle reference level.


1088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1089 ordinal=1089 -->
## Functions

Functions


                •      low ref level —

           low ref level returns the low reference level.

                •       ref units —

               ref units is always absolute in measurement info.


The following information applies to the pre-transition and post-transition outputs of
both instances of this VI.
pre-transition

To calculate the pre-transition undershoot and overshoot, LabVIEW searches for a
local minimum and maximum in the pre-transition aberration region immediately
preceding the beginning of the transition specified by edge number and polarity. The
pre-transition aberration region is defined as the minimum of 3*(end time – start time)
and (current transition start time – previous transition end time) / 2. If the transition to
measure is the first in the waveform, the interval is defined as the minimum of 3*(end
time – start time) and (start time – beginning of the waveform).

If polarity is falling, LabVIEW calculates the pre-transition undershoot using the
following equation:


If polarity is rising, LabVIEW calculates the pre-transition undershoot using the
following equation:


If polarity is falling, LabVIEW calculates the pre-transition overshoot using the
following equation:


                                                    © National Instruments 1089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1090 ordinal=1090 -->
## Functions

Functions


           If polarity is rising, LabVIEW calculates the pre-transition overshoot using the
       following equation:


           Note LabVIEW uses the Histogram method to calculate the state levels and
              amplitude, regardless of the method specified by percent level settings.

      post-transition

      To calculate the post-transition undershoot and overshoot, LabVIEW searches for a
        local minimum and maximum in the post-transition aberration region immediately
       following the end of the transition specified by edge number and polarity. The post-
        transition aberration region is defined as the minimum of 3*(end time – start time) and
       (next transition start time – current transition end time) / 2. If the transition to measure
         is the last in the waveform, the interval is defined as the minimum of 3*(end time –
        start time) and (end of the waveform – end time).

           If polarity is falling, LabVIEW calculates the post-transition undershoot using the
       following equation:


           If polarity is rising, LabVIEW calculates the post-transition undershoot using the
       following equation:


           If polarity is falling, LabVIEW calculates the post-transition overshoot using the
       following equation:


           If polarity is rising, LabVIEW calculates the post-transition overshoot using the

1090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1091 ordinal=1091 -->
## Functions

Functions

following equation:


      Note LabVIEW uses the Histogram method to calculate the state levels and
       amplitude, regardless of the method specified by percent level settings.

Example Illustrations

The following illustration shows the undershoot and overshoot in a negative single
transition.


The following illustration shows the undershoot and overshoot in a positive single
transition.


                                                    © National Instruments 1091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1092 ordinal=1092 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Pulse and Transition Measurements.vi
            • labview\examples\Signal Processing\Waveform
        Measurements\N channel Pulse and Transition
        Measurements.vi
   PulsePulse MeasurementsMeasurements

       Accepts a periodic waveform or an array of periodic waveforms and returns the period,
       pulse duration (pulse width), duty cycle (duty factor), and pulse center of a selected
       pulse and period. Wire data to the signal in input to determine the polymorphic
       instance to use or manually select the instance.

           Note The terminology and measurement definitions for this VI comply with
          IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
         andRelatedWaveforms.


            • Pulse Measurements 1 chan VI
            • Pulse Measurements N chan VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Pulse and Transition Measurements.vi
            • labview\examples\Signal Processing\Waveform
        Measurements\N channel Pulse and Transition

1092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1093 ordinal=1093 -->
## Functions

Functions

   Measurements.vi
PulsePulse MeasurementsMeasurements 11 chanchan VIVI

Accepts a periodic waveform or an array of periodic waveforms and returns the period,
pulse duration (pulse width), duty cycle (duty factor), and pulse center of a selected
pulse and period. Wire data to the signal in input to determine the polymorphic
instance to use or manually select the instance.

      Note The terminology and measurement definitions for this VI comply with
     IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
     andRelatedWaveforms.


Inputs/Outputs

   •      export mode —

    export mode specifies whether this VI returns the period or duty cycle outputs.

    0 all (default)–Returns period, pulse duration, duty cycle, and measurement info.
     no period and duty cycle–Returns pulse duration and measurement info but does not return
    1
     period or duty cycle.

   •      pulse number (1) —

    pulse number specifies which pulse of polarity, high or low, LabVIEW measures.

    For pulse number nwith polarity low, the VI measures the pulse duration and center of the nth
    low pulse. The VI measures the period and duty cycle of the period that begins with the (2n–


                                                    © National Instruments 1093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1094 ordinal=1094 -->
## Functions

Functions


              1)th mid ref level crossing.

               •       signal in —

             signal in is the waveform to measure. The waveform must contain at least pulse number
           complete cycles, where a cycle is the interval between two consecutive mid ref level crossings in
            the same direction.

               •       polarity (high) —

             polarity defines a pulse as high (default) or low. A high pulse consists of the interval between a
              rising mid ref level crossing and the next falling mid ref level crossing.

               •      reference levels —

            reference levels specifies the high, middle, and low reference levels of a waveform.

           LabVIEW uses the reference levels to define the measurement interval of one complete cycle.
          The distance between the mid ref level and the high ref level must equal the distance between
            the low ref level and the mid ref level. If the two distances are not equal, LabVIEW adjusts either
            the high ref level or the low ref level to match the smaller of the two distances. For example, if
           you specify a high ref level of 90%, a mid ref level of 50%, and a low ref level of 20%, LabVIEW
            uses 80% instead of 90% for the high ref level.

                     •      high ref level —

                high ref level specifies the high reference level of the waveform in percent (default) or
                absolute units.

                   After the signal crosses the mid ref level in the rising direction, it must cross the high ref
                  level before the next falling mid ref level crossing can be counted.

                     •     mid ref level —

             mid ref level specifies the middle reference level in percent (default) or absolute units.

              The interval between consecutive rising mid ref level crossings defines one cycle, or period,
                  of the waveform. At least one high/low reference level crossing must separate each mid ref
                  level crossing.

                     •      low ref level —


1094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1095 ordinal=1095 -->
## Functions

Functions


      low ref level specifies the low reference level of the waveform in percent (default) or
      absolute units.

       After the signal crosses the mid ref level in the falling direction, it must cross the low ref
       level before the next rising mid ref level crossing can be counted.

      •       ref units —

       ref units specifies whether the high ref level, mid ref level, and low ref level inputs are
       interpreted as a percentage (default) of the full range of the waveform or as absolute levels.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      percent level settings —

  percent level settings specifies the method LabVIEW uses to determine the high and low state
  levels of a waveform.

   If you select percent ref units, percent level settings determines the reference levels. Otherwise,
  LabVIEW ignores this input.

      •     method —

     method specifies how LabVIEW computes the high and low state levels of the waveform.

       Histogram—Returns the levels of the histogram bins with the maximum number of hits in
        the upper and lower regions of the waveform. The upper and lower regions of the
      0
       waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
       waveform.
      1 Peak—Searches the entire waveform for its maximum and minimum levels.
       Auto select (default)—Determines whether the histogram bins that correspond to the high
      and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
      2 results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
        either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
       histogram fails).

      •      histogram size —


                                                   © National Instruments 1095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1096 ordinal=1096 -->
## Functions

Functions


               histogram size specifies the number of bins in the histogram LabVIEW uses to determine
                the high and low state levels of the waveform.

                     •      histogram method —

               histogram method specifies how LabVIEW computes the high and low state levels of the
               waveform. Currently, mode is the only available histogram method.

               0           mode

                     •      reserved —

                reserved is reserved for future use.


               •      period —

            period returns the time between adjacent mid ref level crossings in the same direction in
            seconds.

          The reciprocal of this value is the signal frequency. The measurement interval includes the pulse
           you specify in pulse number.

               •      pulse duration —

            pulse duration is the time difference in seconds between the first two mid ref level crossings of
            the pulse number. pulse duration is also known as pulse width.

               •      duty cycle —

           duty cycle is a fraction of a period.

           duty cycle is also known as duty factor. LabVIEW uses the following equation to calculate duty
             cycle:                                  In this equation, pulse duration can refer to the high or
           low portion of the period, depending on whether polarity is high pulse or low pulse.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurement info —


1096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1097 ordinal=1097 -->
## Functions

Functions


    measurement info returns the pulse-center time of the selected pulse and the absolute
    reference levels LabVIEW uses to define the measurement cycle.

         •      pulse center —

        pulse center specifies the time instant of the midpoint of the pulse number.


        pulse center for a polarity of high pulse is given by the following equation:

       where tc is the pulse center time, tf is the time instant of the falling mid ref level crossing,
       and tr is the time instant of the preceding rising mid ref level crossing.

         •       ref levels —

          ref levels returns the three user-defined reference levels of the waveform in absolute units.

       LabVIEW uses the reference levels to define the interval of one cycle measurement.

                •      high ref level —

            high ref level returns the high reference level.

                •     mid ref level —

          mid ref level returns the middle reference level.

                •      low ref level —

           low ref level returns the low reference level.

                •       ref units —

               ref units is always absolute in measurement info.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\

                                                    © National Instruments 1097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1098 ordinal=1098 -->
## Functions

Functions

        Pulse and Transition Measurements.vi
            • labview\examples\Signal Processing\Waveform
        Measurements\N channel Pulse and Transition
        Measurements.vi
   PulsePulse MeasurementsMeasurements NN chanchan VIVI

       Accepts a periodic waveform or an array of periodic waveforms and returns the period,
       pulse duration (pulse width), duty cycle (duty factor), and pulse center of a selected
       pulse and period. Wire data to the signal in input to determine the polymorphic
       instance to use or manually select the instance.

           Note The terminology and measurement definitions for this VI comply with
          IEEEStandard181-2003, IEEEStandardonTransitions,Pulses,
         andRelatedWaveforms.


      Inputs/Outputs

               •      export mode —

            export mode specifies whether this VI returns the period or duty cycle outputs.

           0 all (default)–Returns period, pulse duration, duty cycle, and measurement info.
           no period and duty cycle–Returns pulse duration and measurement info but does not return
           1
             period or duty cycle.

               •      pulse number (1) —

            pulse number specifies which pulse of polarity, high or low, LabVIEW measures.


1098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1099 ordinal=1099 -->
## Functions

Functions


  For pulse number nwith polarity low, the VI measures the pulse duration and center of the nth
  low pulse. The VI measures the period and duty cycle of the period that begins with the (2n–
   1)th mid ref level crossing.

•       signal(s) in —

  signal(s) in is the array of waveforms to measure. The waveform must contain at least pulse
  number complete cycles, where a cycle is the interval between two consecutive mid ref level
  crossings in the same direction.

•       polarity (high) —

  polarity defines a pulse as high (default) or low. A high pulse consists of the interval between a
   rising mid ref level crossing and the next falling mid ref level crossing.

•      reference levels —

  reference levels specifies the high, middle, and low reference levels of a waveform.

  LabVIEW uses the reference levels to define the measurement interval of one complete cycle.
  The distance between the mid ref level and the high ref level must equal the distance between
  the low ref level and the mid ref level. If the two distances are not equal, LabVIEW adjusts either
  the high ref level or the low ref level to match the smaller of the two distances. For example, if
  you specify a high ref level of 90%, a mid ref level of 50%, and a low ref level of 20%, LabVIEW
  uses 80% instead of 90% for the high ref level.

      •      high ref level —

      high ref level specifies the high reference level of the waveform in percent (default) or
      absolute units.

       After the signal crosses the mid ref level in the rising direction, it must cross the high ref
       level before the next falling mid ref level crossing can be counted.

      •     mid ref level —

     mid ref level specifies the middle reference level in percent (default) or absolute units.

     The interval between consecutive rising mid ref level crossings defines one cycle, or period,
       of the waveform. At least one high/low reference level crossing must separate each mid ref
       level crossing.


                                                   © National Instruments 1099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1100 ordinal=1100 -->
## Functions

Functions


                     •      low ref level —

              low ref level specifies the low reference level of the waveform in percent (default) or
                absolute units.

                   After the signal crosses the mid ref level in the falling direction, it must cross the low ref
                  level before the next rising mid ref level crossing can be counted.

                     •       ref units —

                   ref units specifies whether the high ref level, mid ref level, and low ref level inputs are
                 interpreted as a percentage (default) of the full range of the waveform or as absolute levels.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      percent level settings —

            percent level settings specifies the method LabVIEW uses to determine the high and low state
              levels of a waveform.

                    If you select percent ref units, percent level settings determines the reference levels. Otherwise,
           LabVIEW ignores this input.

                     •     method —

             method specifies how LabVIEW computes the high and low state levels of the waveform.

                Histogram—Returns the levels of the histogram bins with the maximum number of hits in
                 the upper and lower regions of the waveform. The upper and lower regions of the
               0
               waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
                waveform.
               1 Peak—Searches the entire waveform for its maximum and minimum levels.
                Auto select (default)—Determines whether the histogram bins that correspond to the high
               and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
               2 results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
                   either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
                 histogram fails).


1100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1101 ordinal=1101 -->
## Functions

Functions


      •      histogram size —

      histogram size specifies the number of bins in the histogram LabVIEW uses to determine
      the high and low state levels of the waveform.

      •      histogram method —

      histogram method specifies how LabVIEW computes the high and low state levels of the
      waveform. Currently, mode is the only available histogram method.

      0           mode

      •      reserved —

      reserved is reserved for future use.


•      period —

  period is an array that contains the period for each waveform in signal(s) in. period returns the
  time between adjacent mid ref level crossings in the same direction in seconds.

  The reciprocal of this value is the signal frequency. The measurement interval includes the pulse
  you specify in pulse number.

•      pulse duration —

  pulse duration is an array that contains the pulse duration for each waveform in signal(s) in.
  pulse duration is the time difference in seconds between the first two mid ref level crossings of
  the pulse number. pulse duration is also known as pulse width.

•      duty cycle —

  duty cycle is an array that contains the duty cycle for each waveform in signal(s) in.

  duty cycle is also known as duty factor. LabVIEW uses the following equation to calculate duty
  cycle:                                  In this equation, pulse duration can refer to the high or
  low portion of the period, depending on whether polarity is high pulse or low pulse.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 1101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1102 ordinal=1102 -->
## Functions

Functions

               •     measurement info —

          measurement info is an array of clusters that returns the pulse center time of the selected pulse
          and the absolute reference levels LabVIEW uses to define the measurement cycle for each input
           waveform.

                     •      pulse center —

                pulse center specifies the time instant of the midpoint of the pulse number.


                pulse center for a polarity of high pulse is given by the following equation:

              where tc is the pulse center time, tf is the time instant of the falling mid ref level crossing,
              and tr is the time instant of the preceding rising mid ref level crossing.

                     •       ref levels —

                   ref levels returns the three user-defined reference levels of the waveform in absolute units.

              LabVIEW uses the reference levels to define the interval of one cycle measurement.

                           •      high ref level —

                    high ref level returns the high reference level.

                           •     mid ref level —

                 mid ref level returns the middle reference level.

                           •      low ref level —

                  low ref level returns the low reference level.

                           •       ref units —

                        ref units is always absolute in measurement info.


     Examples

       Refer to the following example files included with LabVIEW.

1102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1103 ordinal=1103 -->
## Functions

Functions

  • labview\examples\Signal Processing\Waveform Measurements\
   Pulse and Transition Measurements.vi
  • labview\examples\Signal Processing\Waveform
   Measurements\N channel Pulse and Transition
   Measurements.vi
ReferenceReference andand StateState LevelsLevels

Pulse and transition waveform measurements require a means of identifying the
position in time of the waveform feature to be measured. State and reference levels
provide a means of accomplishing this identification, resulting in a measurement time
interval that you can use as a basis for various time-domain measurements.

State Levels

Pulses or transitions involve changes in the waveform level between various
conditions, or states. The most common case is a two-state waveform with a high state
and a low state. For example, an ideal digital signal might be defined as in the high
state at 5 volts and in the low state at 0 volts.

Reference Levels

Reference levels allow you to extract information from the waveform by identifying
reference level crossings. Two adjacent waveform samples separated in magnitude by
a reference level constitute a reference level crossing. Linear interpolation gives an
approximation to the exact time instant of a reference level crossing, as shown in the
following illustration.


                                                    © National Instruments 1103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1104 ordinal=1104 -->
## Functions

Functions

      You can specify reference levels as a percentage of the state levels, with the low state
      and high state corresponding to 0 and 100%, respectively. The most common low, mid,
      and high reference levels are 10, 50, and 90%. The following illustration shows a typical
       selection of state and reference levels for a pulse waveform.


      The histogram method was used to determine the state levels. The histogram method
      has the advantage of excluding the undershoot and overshoot peaks.
   AmplitudeAmplitude andand LevelsLevels

       Returns the amplitude, high state level, and low state level of a waveform or an array
       of waveforms. Wire data to the signal in input to determine the polymorphic instance
       to use or manually select the instance.


            • Amplitude and Levels 1 chan VI
            • Amplitude and Levels N chan VI

      The terminology and measurement definitions for this VI comply with IEEEStandard
      181-2003, IEEEStandardonTransitions,Pulses,andRelatedWaveforms.

     Examples

       Refer to the following example files included with LabVIEW.


1104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1105 ordinal=1105 -->
## Functions

Functions

  • labview\examples\Signal Processing\Waveform
   Measurements\N channel Pulse and Transition
   Measurements.vi
AmplitudeAmplitude andand LevelsLevels 11 chanchan VIVI

Returns the amplitude, high state level, and low state level of a waveform or an array
of waveforms. Wire data to the signal in input to determine the polymorphic instance
to use or manually select the instance.


Inputs/Outputs

   •       signal in —

    signal in is the waveform to measure.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       state settings —

     state settings specifies the method used to determine the high and low state levels of a
    waveform.

    For pulse and transition waveform measurements, state levels provide a means to identify the
    position in time of the waveform feature to be measured.

         •     method —

       method specifies how LabVIEW computes the high and low state levels of the waveform.


                                                    © National Instruments 1105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1106 ordinal=1106 -->
## Functions

Functions


                Histogram—Returns the levels of the histogram bins with the maximum number of hits in
                 the upper and lower regions of the waveform. The upper and lower regions of the               0               waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
                waveform.
               1 Peak—Searches the entire waveform for its maximum and minimum levels.
                Auto select (default)—Determines whether the histogram bins that correspond to the high
               and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
               2 results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
                   either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
                 histogram fails).

                     •      histogram size —

               histogram size specifies the number of bins in the histogram LabVIEW uses to determine
                the high and low state levels of the waveform.

                     •      histogram method —

               histogram method specifies how LabVIEW computes the high and low state levels of the
               waveform. Currently, mode is the only available histogram method.

               0           mode

                     •      reserved —

                reserved is reserved for future use.


               •      amplitude —

           amplitude is the difference between high state level and low state level.

               •      high state level —

            high state level returns the level at which a pulse or transition waveform is defined to be in its
            highest state.

               •      low state level —

           low state level returns the level at which a pulse or transition waveform is defined to be in its
            lowest state


1106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1107 ordinal=1107 -->
## Functions

Functions

   •       error out —

     error out contains error information. This output provides standard error out functionality.


The terminology and measurement definitions for this VI comply with IEEEStandard
181-2003, IEEEStandardonTransitions,Pulses,andRelatedWaveforms.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform
   Measurements\N channel Pulse and Transition
   Measurements.vi
AmplitudeAmplitude andand LevelsLevels NN chanchan VIVI

Returns the amplitude, high state level, and low state level of a waveform or an array
of waveforms. Wire data to the signal in input to determine the polymorphic instance
to use or manually select the instance.


Inputs/Outputs

   •       signal(s) in —

     signal(s) in is an array of waveforms containing the signals to measure.

   •       error in (no error) —

     error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       state settings —


                                                    © National Instruments 1107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1108 ordinal=1108 -->
## Functions

Functions


             state settings specifies the method used to determine the high and low state levels of a
           waveform.

            For pulse and transition waveform measurements, state levels provide a means to identify the
             position in time of the waveform feature to be measured.

                     •     method —

             method specifies how LabVIEW computes the high and low state levels of the waveform.

                Histogram—Returns the levels of the histogram bins with the maximum number of hits in
                 the upper and lower regions of the waveform. The upper and lower regions of the               0               waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the
                waveform.
               1 Peak—Searches the entire waveform for its maximum and minimum levels.
                Auto select (default)—Determines whether the histogram bins that correspond to the high
               and low state levels each have over 5% of the total hits. If so, LabVIEW returns those
               2 results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for
                   either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a
                 histogram fails).

                     •      histogram size —

               histogram size specifies the number of bins in the histogram LabVIEW uses to determine
                the high and low state levels of the waveform.

                     •      histogram method —

               histogram method specifies how LabVIEW computes the high and low state levels of the
               waveform. Currently, mode is the only available histogram method.

               0           mode

                     •      reserved —

                reserved is reserved for future use.


               •      amplitude —

           amplitude is an array containing the amplitude of each waveform in signal(s) in.


1108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1109 ordinal=1109 -->
## Functions

Functions

   •      high state level —

    high state level is an array containing the high state level of each waveform in signal(s) in.

   •      low state level —

    low state level is an array containing the low state level of each waveform in signal(s) in.

   •       error out —

     error out contains error information. This output provides standard error out functionality.


The terminology and measurement definitions for this VI comply with IEEEStandard
181-2003, IEEEStandardonTransitions,Pulses,andRelatedWaveforms.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform
   Measurements\N channel Pulse and Transition
   Measurements.vi
ExtractExtract SingleSingle ToneTone InformationInformation

Takes a signal in, finds the single tone with the highest amplitude or searches a
specified frequency range, and returns the single tone frequency, amplitude, and
phase. The input signal can be real or complex and single-channel or multichannel.
Wire data to the time signal in input to determine the polymorphic instance to use or
manually select the instance.


   • Extract Single Tone Information 1 Chan VI
   • Extract Single Tone Information 1 Chan (CDB) VI
   • Extract Single Tone Information N Chan VI


                                                    © National Instruments 1109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1110 ordinal=1110 -->
## Functions

Functions

            • Extract Single Tone Information N Chan (CDB) VI

      A real tone signal can be expressed as shown in the following equation:


      where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

      A complex tone signal can be expressed as shown in the following equation:


      where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
      a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
       Fs/2).

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Correct for MIO inter-channel delay (continuous).vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Single Tone Measurements.vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Complex Single Tone Measurements.vi

1110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1111 ordinal=1111 -->
## Functions

Functions

ExtractExtract SingleSingle ToneTone InformationInformation 11 ChanChan VIVI

Takes a signal in, finds the single tone with the highest amplitude or searches a
specified frequency range, and returns the single tone frequency, amplitude, and
phase. The input signal can be real or complex and single-channel or multichannel.
Wire data to the time signal in input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      time signal in —

    time signal in is the time-domain waveform.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only
    2  detected signal—Single tone
    3  residual signal—Signal minus tone

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      advanced search —

    advanced search controls the frequency domain search area, center frequency, and width. You
    use advanced search for narrowing the single tone search range.


                                                    © National Instruments 1111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1112 ordinal=1112 -->
## Functions

Functions


                     •      approx freq. (optional) —

               approx freq. is the center frequency used of the frequency domain search for the single
                 tone. The default is –1.0, which means the VI searches the tone in the full frequency range of
                     (0, Fs/2).

                     •      search (+/- % of Fsampl.) —

                search is the frequency width, as a percentage of the sampling rate, for the frequency
              domain search for the single tone frequency.


               •      exported signals —

           exported signals contains the signals specified by export mode.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —

                      f0 returns the start frequency, in hertz, of the spectrum.

                           •       df —

                     df returns the frequency resolution, in hertz, of the spectrum.

                           •     dB Spectrum (Hann) —

                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      detected frequency —


1112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1113 ordinal=1113 -->
## Functions

Functions


    detected frequency is the frequency of the detected single tone in Hz.

   •      detected amplitude —

    detected amplitude is the peak amplitude of the detected single tone.

   •      detected phase (deg) —

    detected phase is the phase of the detected single tone in degrees.

    Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to the angle
     in input on the Wrap Angle VI, and select degree in, degree out or degree in,
   radians out for the angle units input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     measurement info —

    measurement info returns information about your measurement, mainly warnings for
    inconsistencies in your input signal.

         •      uncertainty —

        uncertainty is reserved for future use.

         •      Warning —

       Warning is TRUE if a warning is generated during processing.

         •     comments —

       comments contains a warning message when Warning is TRUE.


A real tone signal can be expressed as shown in the following equation:


where A, f, and φ are the amplitude, frequency, and phase of the tone signal,

                                                    © National Instruments 1113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1114 ordinal=1114 -->
## Functions

Functions

        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

      A complex tone signal can be expressed as shown in the following equation:


      where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
      a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
       Fs/2).

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Correct for MIO inter-channel delay (continuous).vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Single Tone Measurements.vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Complex Single Tone Measurements.vi
    ExtractExtract SingleSingle ToneTone InformationInformation 11 ChanChan
   (CDB)(CDB) VIVI

      Takes a signal in, finds the single tone with the highest amplitude or searches a
       specified frequency range, and returns the single tone frequency, amplitude, and

1114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1115 ordinal=1115 -->
## Functions

Functions

phase. The input signal can be real or complex and single-channel or multichannel.
Wire data to the time signal in input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      time signal in —

    time signal in is the time-domain waveform.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only
    2  detected signal—Single tone
    3  residual signal—Signal minus tone

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      advanced search —

    advanced search controls the frequency domain search area, center frequency, and width. You
    use advanced search for narrowing the single tone search range.

         •      approx freq. (optional) —

        approx freq. is the center frequency used of the frequency domain search for the single
         tone. The default is NaN, which means the VI searches the tone in the full frequency range of
          (–Fs/2, Fs/2).


                                                    © National Instruments 1115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1116 ordinal=1116 -->
## Functions

Functions


                     •      search (+/- % of Fsampl.) —

                search is the frequency width, as a percentage of the sampling rate, for the frequency
              domain search for the single tone frequency.


               •      exported signals —

           exported signals contains the signals specified by export mode.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —

                      f0 returns the start frequency, in hertz, of the spectrum.

                           •       df —

                     df returns the frequency resolution, in hertz, of the spectrum.

                           •     dB Spectrum (Hann) —

                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      detected frequency —

            detected frequency is the frequency of the detected single tone in Hz.

               •      detected amplitude —

            detected amplitude is the peak amplitude of the detected single tone.

               •      detected phase (deg) —

1116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1117 ordinal=1117 -->
## Functions

Functions


    detected phase is the phase of the detected single tone in degrees.

    Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to the angle
     in input on the Wrap Angle VI, and select degree in, degree out or degree in,
   radians out for the angle units input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     measurement info —

    measurement info returns information about your measurement, mainly warnings for
    inconsistencies in your input signal.

         •      uncertainty —

        uncertainty is reserved for future use.

         •      Warning —

       Warning is TRUE if a warning is generated during processing.

         •     comments —

       comments contains a warning message when Warning is TRUE.


A real tone signal can be expressed as shown in the following equation:


where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
respectively, and Fs is the sample rate in samples per second of the input waveform
signal.

A complex tone signal can be expressed as shown in the following equation:


                                                    © National Instruments 1117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1118 ordinal=1118 -->
## Functions

Functions


      where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
      a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
       Fs/2).

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Correct for MIO inter-channel delay (continuous).vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Single Tone Measurements.vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Complex Single Tone Measurements.vi
    ExtractExtract SingleSingle ToneTone InformationInformation NN ChanChan VIVI

      Takes a signal in, finds the single tone with the highest amplitude or searches a
       specified frequency range, and returns the single tone frequency, amplitude, and
       phase. The input signal can be real or complex and single-channel or multichannel.
       Wire data to the time signal in input to determine the polymorphic instance to use or
      manually select the instance.

           Note


1118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1119 ordinal=1119 -->
## Functions

Functions


      The waveform array input should be the result of a multichannel acquisition
       where each element of the array of waveforms is a distinct and separate
       channel of data.


Inputs/Outputs

   •      time signals in —

    time signals in is an array of time-domain waveforms.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only
    2  detected signal—Single tone
    3  residual signal—Signal minus tone

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      advanced search —

    advanced search controls the frequency domain search area, center frequency, and width. You
    use advanced search for narrowing the single tone search range.

         •      approx freq. (optional) —


                                                    © National Instruments 1119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1120 ordinal=1120 -->
## Functions

Functions


               approx freq. is the center frequency used of the frequency domain search for the single
                 tone. The default is –1.0, which means the VI searches the tone in the full frequency range of
                     (0, Fs/2).

                     •      search (+/- % of Fsampl.) —

                search is the frequency width, as a percentage of the sampling rate, for the frequency
              domain search for the single tone frequency.


               •      exported signals —

           exported signals is an array of exported signals.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —

                      f0 returns the start frequency, in hertz, of the spectrum.

                           •       df —

                     df returns the frequency resolution, in hertz, of the spectrum.

                           •     dB Spectrum (Hann) —

                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      detected frequencies —

            detected frequencies is an array of frequencies of the detected single tone in Hz for each


1120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1121 ordinal=1121 -->
## Functions

Functions


    waveform.

   •      detected amplitudes —

    detected amplitudes is an array of peak amplitudes of the detected single tone for each
    waveform.

   •      detected phases (deg) —

    detected phases is an array of phases of the detected single tone in degrees for each waveform.

    Use the Wrap Angle VI to change the units of detected phases. Wire detected phases to the
    angle in input on the Wrap Angle VI, and select degree in, degree out or degree in,
   radians out for the angle units input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     measurements info —

    measurements info is an array that returns information about your measurement, mainly
    warnings for inconsistencies in your input signal.

         •      uncertainty —

        uncertainty is reserved for future use.

         •      Warning —

       Warning is TRUE if a warning is generated during processing.

         •     comments —

       comments contains a warning message when Warning is TRUE.


A real tone signal can be expressed as shown in the following equation:


                                                    © National Instruments 1121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1122 ordinal=1122 -->
## Functions

Functions

      where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

      A complex tone signal can be expressed as shown in the following equation:


      where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
      a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
       Fs/2).

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Correct for MIO inter-channel delay (continuous).vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Single Tone Measurements.vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Complex Single Tone Measurements.vi
    ExtractExtract SingleSingle ToneTone InformationInformation NN ChanChan
   (CDB)(CDB) VIVI

      Takes a signal in, finds the single tone with the highest amplitude or searches a

1122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1123 ordinal=1123 -->
## Functions

Functions

specified frequency range, and returns the single tone frequency, amplitude, and
phase. The input signal can be real or complex and single-channel or multichannel.
Wire data to the time signal in input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      time signals in —

    time signals in is an array of time-domain waveforms.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only
    2  detected signal—Single tone
    3  residual signal—Signal minus tone

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      advanced search —

    advanced search controls the frequency domain search area, center frequency, and width. You
    use advanced search for narrowing the single tone search range.

         •      approx freq. (optional) —

        approx freq. is the center frequency used of the frequency domain search for the single
         tone. The default is NaN, which means the VI searches the tone in the full frequency range of


                                                    © National Instruments 1123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1124 ordinal=1124 -->
## Functions

Functions


                   (–Fs/2, Fs/2).

                     •      search (+/- % of Fsampl.) —

                search is the frequency width, as a percentage of the sampling rate, for the frequency
              domain search for the single tone frequency.


               •      exported signals —

           exported signals is an array of exported signals.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —

                      f0 returns the start frequency, in hertz, of the spectrum.

                           •       df —

                     df returns the frequency resolution, in hertz, of the spectrum.

                           •     dB Spectrum (Hann) —

                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      detected frequencies —

            detected frequencies is an array of frequencies of the detected single tone in Hz for each
           waveform.

               •      detected amplitudes —

1124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1125 ordinal=1125 -->
## Functions

Functions


    detected amplitudes is an array of peak amplitudes of the detected single tone for each
    waveform.

   •      detected phases (deg) —

    detected phases is an array of phases of the detected single tone in degrees for each waveform.

    Use the Wrap Angle VI to change the units of detected phases. Wire detected phases to the
    angle in input on the Wrap Angle VI, and select degree in, degree out or degree in,
   radians out for the angle units input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     measurements info —

    measurements info is an array that returns information about your measurement, mainly
    warnings for inconsistencies in your input signal.

         •      uncertainty —

        uncertainty is reserved for future use.

         •      Warning —

       Warning is TRUE if a warning is generated during processing.

         •     comments —

       comments contains a warning message when Warning is TRUE.


A real tone signal can be expressed as shown in the following equation:


where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
respectively, and Fs is the sample rate in samples per second of the input waveform
signal.

                                                    © National Instruments 1125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1126 ordinal=1126 -->
## Functions

Functions

      A complex tone signal can be expressed as shown in the following equation:


      where A, f, and φ are the amplitude, frequency, and phase of the tone signal,
        respectively, and Fs is the sample rate in samples per second of the input waveform
        signal.

       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
      a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
       Fs/2).

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Correct for MIO inter-channel delay (continuous).vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Single Tone Measurements.vi
            • labview\examples\Signal Processing\Waveform Measurements\
        Complex Single Tone Measurements.vi
    ExtractExtract MultipleMultiple ToneTone InformationInformation

       Returns the frequency, amplitude, and phase for each signal tone whose amplitude
      exceeds a specified threshold. Wire data to the time signal in input to determine the
      polymorphic instance to use or manually select the instance.


1126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1127 ordinal=1127 -->
## Functions

Functions

   • Extract Multiple Tone Information 1 Chan VI
   • Extract Multiple Tone Information 1 Chan (CDB) VI
   • Extract Multiple Tone Information N Chan VI
   • Extract Multiple Tone Information N Chan - N Specs VI
   • Extract Multiple Tone Information N Chan (CDB) VI
   • Extract Multiple Tone Information N Chan - N Specs (CDB) VI

The input signal can be real or complex and single-channel, in the form of a waveform,
or multichannel, in the form of an array of waveforms. If you wire an array of real
waveforms to time signal in, LabVIEW selects the Extract Multiple Tone Information N
Chan instance by default. If you wire an array of complex waveforms to time signal in,
LabVIEW selects the Extract Multiple Tone Information N Chan (CDB) instance by
default.

A real multiple tone signal can be expressed as shown in the following equation:


where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
second of the input waveform signal.

A complex multiple tone signal can be expressed as shown in the following equation:


where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
second of the input waveform signal.

For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
Fs/2).


                                                    © National Instruments 1127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1128 ordinal=1128 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Complex Multi-Tone Measurements.vi
    ExtractExtract MultipleMultiple ToneTone InformationInformation 11 ChanChan VIVI

       Returns the frequency, amplitude, and phase for each signal tone whose amplitude
      exceeds a specified threshold. Wire data to the time signal in input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      time signal in —

           time signal in is the time-domain waveform.

               •      export mode —

            export mode selects the source of the signal and spectrum to export to exported signals.

           0  none—Fastest computation
           1  input signal—Input signal only
           2  detected signal—Multiple tone
           3  residual signal—Signal minus tone

               •      threshold —

            threshold specifies the minimum amplitude that each tone must exceed for this VI to extract it
           from time signal in.


1128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1129 ordinal=1129 -->
## Functions

Functions

•     max num tones —

  max num tones specifies the maximum number of tones that this VI extracts. If you set max num
  tones to –1, this VI extracts all tones whose amplitude exceeds threshold.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      output sorting —

  output sorting specifies the sorting order of the tones that this VI extracts.

  0    increasing frequency
  1    decreasing amplitude

•      exported signals —

  exported signals contains the signals specified by export mode.

      •      exported time signal —

      exported time signal is the waveform containing the exported time signal as selected by
      export mode.

      •      exported spectrum (dB) —

      exported spectrum (dB) is the spectrum of the exported time signal as selected by export
     mode.

             •       f0 —

            f0 returns the start frequency, in hertz, of the spectrum.

             •       df —

           df returns the frequency resolution, in hertz, of the spectrum.

             •     dB Spectrum (Hann) —


                                                   © National Instruments 1129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1130 ordinal=1130 -->
## Functions

Functions


                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      multiple tone information —

            multiple tone information returns the frequency, amplitude, and phase of each tone that this VI
              extracts. Each element of the array is one single tone.

                     •      detected frequency —

                detected frequency is the frequency of the detected single tone in Hz.

                     •      detected amplitude —

                detected amplitude is the peak amplitude of the detected single tone.

                     •      detected phase (deg) —

                detected phase is the phase of the detected single tone in degrees.

              Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to the
                angle in input on the Wrap Angle VI, and select degree in, degree out or degree
            in, radians out for the angle units input.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The input signal can be real or complex and single-channel, in the form of a waveform,
       or multichannel, in the form of an array of waveforms. If you wire an array of real
      waveforms to time signal in, LabVIEW selects the Extract Multiple Tone Information N
      Chan instance by default. If you wire an array of complex waveforms to time signal in,
      LabVIEW selects the Extract Multiple Tone Information N Chan (CDB) instance by
        default.

      A real multiple tone signal can be expressed as shown in the following equation:

1130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1131 ordinal=1131 -->
## Functions

Functions


where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
second of the input waveform signal.

A complex multiple tone signal can be expressed as shown in the following equation:


where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
second of the input waveform signal.

For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
Fs/2).

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform Measurements\
   Complex Multi-Tone Measurements.vi
ExtractExtract MultipleMultiple ToneTone InformationInformation 11 ChanChan
(CDB)(CDB) VIVI

Returns the frequency, amplitude, and phase for each signal tone whose amplitude
exceeds a specified threshold. Wire data to the time signal in input to determine the
polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1132 ordinal=1132 -->
## Functions

Functions


      Inputs/Outputs

               •      time signal in —

           time signal in is the time-domain waveform.

               •      export mode —

            export mode selects the source of the signal and spectrum to export to exported signals.

           0  none—Fastest computation
           1  input signal—Input signal only
           2  detected signal—Multiple tone
           3  residual signal—Signal minus tone

               •      threshold —

            threshold specifies the minimum amplitude that each tone must exceed for this VI to extract it
           from time signal in.

               •     max num tones —

         max num tones specifies the maximum number of tones that this VI extracts. If you set max num
           tones to –1, this VI extracts all tones whose amplitude exceeds threshold.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      output sorting —

           output sorting specifies the sorting order of the tones that this VI extracts.

           0    increasing frequency
           1    decreasing amplitude


1132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1133 ordinal=1133 -->
## Functions

Functions

•      exported signals —

  exported signals contains the signals specified by export mode.

      •      exported time signal —

      exported time signal is the waveform containing the exported time signal as selected by
      export mode.

      •      exported spectrum (dB) —

      exported spectrum (dB) is the spectrum of the exported time signal as selected by export
     mode.

             •       f0 —

            f0 returns the start frequency, in hertz, of the spectrum.

             •       df —

           df returns the frequency resolution, in hertz, of the spectrum.

             •     dB Spectrum (Hann) —

        dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
            signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


•      multiple tone information —

  multiple tone information returns the frequency, amplitude, and phase of each tone that this VI
  extracts. Each element of the array is one single tone.

      •      detected frequency —

      detected frequency is the frequency of the detected single tone in Hz.

      •      detected amplitude —

      detected amplitude is the peak amplitude of the detected single tone.

      •      detected phase (deg) —


                                                   © National Instruments 1133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1134 ordinal=1134 -->
## Functions

Functions


                detected phase is the phase of the detected single tone in degrees.

              Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to the
                angle in input on the Wrap Angle VI, and select degree in, degree out or degree
            in, radians out for the angle units input.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The input signal can be real or complex and single-channel, in the form of a waveform,
       or multichannel, in the form of an array of waveforms. If you wire an array of real
      waveforms to time signal in, LabVIEW selects the Extract Multiple Tone Information N
      Chan instance by default. If you wire an array of complex waveforms to time signal in,
      LabVIEW selects the Extract Multiple Tone Information N Chan (CDB) instance by
        default.

      A real multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

      A complex multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.


1134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1135 ordinal=1135 -->
## Functions

Functions

For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For
a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
Fs/2).

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform Measurements\
   Complex Multi-Tone Measurements.vi
ExtractExtract MultipleMultiple ToneTone InformationInformation NN ChanChan VIVI

Returns the frequency, amplitude, and phase for each signal tone whose amplitude
exceeds a specified threshold. Wire data to the time signal in input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      time signals in —

    time signals in is an array of time-domain waveforms.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only
    2  detected signal—Multiple tone


                                                    © National Instruments 1135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1136 ordinal=1136 -->
## Functions

Functions


           3  residual signal—Signal minus tone

               •      threshold —

            threshold specifies the minimum amplitude that each tone must exceed for this VI to extract it
           from time signals in.

               •     max num tones —

         max num tones specifies the maximum number of tones that this VI extracts. If you set max num
           tones to –1, this VI extracts all tones whose amplitude exceeds threshold.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      output sorting —

           output sorting specifies the sorting order of the tones that this VI extracts.

           0    increasing frequency
           1    decreasing amplitude

               •      exported signals —

           exported signals is an array of exported signals.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —


1136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1137 ordinal=1137 -->
## Functions

Functions


            f0 returns the start frequency, in hertz, of the spectrum.

             •       df —

           df returns the frequency resolution, in hertz, of the spectrum.

             •     dB Spectrum (Hann) —

        dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
            signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


•      multiple tone information —

  multiple tone information returns the frequency, amplitude, and phase of each tone that this VI
  extracts. Each element of the array is the multiple tone information for one signal in time signals
   in.

      •      multiple tone information —

      multiple tone information returns the frequency, amplitude, and phase of each sine tone
       that this VI extracts. Each element of the array is the multiple tone information for one
       signal in time signals in.

             •      detected frequency —

          detected frequency is the frequency of the detected single tone in Hz.

             •      detected amplitude —

          detected amplitude is the peak amplitude of the detected single tone.

             •      detected phase (deg) —

          detected phase is the phase of the detected single tone in degrees.

         Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to


                                                   © National Instruments 1137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1138 ordinal=1138 -->
## Functions

Functions


                    the angle in input on the Wrap Angle VI, and select degree in, degree out or
               degree in, radians out for the angle units input.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The input signal can be real or complex and single-channel, in the form of a waveform,
       or multichannel, in the form of an array of waveforms. If you wire an array of real
      waveforms to time signal in, LabVIEW selects the Extract Multiple Tone Information N
      Chan instance by default. If you wire an array of complex waveforms to time signal in,
      LabVIEW selects the Extract Multiple Tone Information N Chan (CDB) instance by
        default.

      A real multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

      A complex multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For

1138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1139 ordinal=1139 -->
## Functions

Functions

a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
Fs/2).

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform Measurements\
   Complex Multi-Tone Measurements.vi
ExtractExtract MultipleMultiple ToneTone InformationInformation NN ChanChan -- NN
SpecsSpecs VIVI

Returns the frequency, amplitude, and phase for each signal tone whose amplitude
exceeds a specified threshold. Wire data to the time signal in input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      time signals in —

    time signals in is an array of time-domain waveforms.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only


                                                    © National Instruments 1139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1140 ordinal=1140 -->
## Functions

Functions


           2  detected signal—Multiple tone
           3  residual signal—Signal minus tone

               •      threshold —

            threshold specifies the minimum amplitude that each tone must exceed for this VI to extract it
           from time signals in. Each element of the array is the threshold for one signal in time signals in.

               •     max num tones —

         max num tones specifies the maximum number of tones that this VI extracts from each signal. If
           you set max num tones to –1, this VI extracts all tones whose amplitude exceeds threshold.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      output sorting —

           output sorting specifies the sorting order of the tones that this VI extracts.

           0    increasing frequency
           1    decreasing amplitude

               •      exported signals —

           exported signals is an array of exported signals.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —


1140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1141 ordinal=1141 -->
## Functions

Functions


            f0 returns the start frequency, in hertz, of the spectrum.

             •       df —

           df returns the frequency resolution, in hertz, of the spectrum.

             •     dB Spectrum (Hann) —

        dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
            signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


•      multiple tone information —

  multiple tone information returns the frequency, amplitude, and phase of each tone that this VI
  extracts. Each element of the array is the multiple tone information for one signal in time signals
   in.

      •      multiple tone information —

      multiple tone information returns the frequency, amplitude, and phase of each sine tone
       that this VI extracts. Each element of the array is the multiple tone information for one
       signal in time signals in.

             •      detected frequency —

          detected frequency is the frequency of the detected single tone in Hz.

             •      detected amplitude —

          detected amplitude is the peak amplitude of the detected single tone.

             •      detected phase (deg) —

          detected phase is the phase of the detected single tone in degrees.

         Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to


                                                   © National Instruments 1141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1142 ordinal=1142 -->
## Functions

Functions


                    the angle in input on the Wrap Angle VI, and select degree in, degree out or
               degree in, radians out for the angle units input.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The input signal can be real or complex and single-channel, in the form of a waveform,
       or multichannel, in the form of an array of waveforms. If you wire an array of real
      waveforms to time signal in, LabVIEW selects the Extract Multiple Tone Information N
      Chan instance by default. If you wire an array of complex waveforms to time signal in,
      LabVIEW selects the Extract Multiple Tone Information N Chan (CDB) instance by
        default.

      A real multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

      A complex multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For

1142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1143 ordinal=1143 -->
## Functions

Functions

a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
Fs/2).

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform Measurements\
   Complex Multi-Tone Measurements.vi
ExtractExtract MultipleMultiple ToneTone InformationInformation NN ChanChan
(CDB)(CDB) VIVI

Returns the frequency, amplitude, and phase for each signal tone whose amplitude
exceeds a specified threshold. Wire data to the time signal in input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      time signals in —

    time signals in is an array of time-domain waveforms.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only


                                                    © National Instruments 1143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1144 ordinal=1144 -->
## Functions

Functions


           2  detected signal—Multiple tone
           3  residual signal—Signal minus tone

               •      threshold —

            threshold specifies the minimum amplitude that each tone must exceed for this VI to extract it
           from time signals in.

               •     max num tones —

         max num tones specifies the maximum number of tones that this VI extracts. If you set max num
           tones to –1, this VI extracts all tones whose amplitude exceeds threshold.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      output sorting —

           output sorting specifies the sorting order of the tones that this VI extracts.

           0    increasing frequency
           1    decreasing amplitude

               •      exported signals —

           exported signals is an array of exported signals.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —


1144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1145 ordinal=1145 -->
## Functions

Functions


            f0 returns the start frequency, in hertz, of the spectrum.

             •       df —

           df returns the frequency resolution, in hertz, of the spectrum.

             •     dB Spectrum (Hann) —

        dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
            signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


•      multiple tone information —

  multiple tone information returns the frequency, amplitude, and phase of each tone that this VI
  extracts. Each element of the array is the multiple tone information for one signal in time signals
   in.

      •      multiple tone information —

      multiple tone information returns the frequency, amplitude, and phase of each sine tone
       that this VI extracts. Each element of the array is the multiple tone information for one
       signal in time signals in.

             •      detected frequency —

          detected frequency is the frequency of the detected single tone in Hz.

             •      detected amplitude —

          detected amplitude is the peak amplitude of the detected single tone.

             •      detected phase (deg) —

          detected phase is the phase of the detected single tone in degrees.

         Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to


                                                   © National Instruments 1145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1146 ordinal=1146 -->
## Functions

Functions


                    the angle in input on the Wrap Angle VI, and select degree in, degree out or
               degree in, radians out for the angle units input.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The input signal can be real or complex and single-channel, in the form of a waveform,
       or multichannel, in the form of an array of waveforms. If you wire an array of real
      waveforms to time signal in, LabVIEW selects the Extract Multiple Tone Information N
      Chan instance by default. If you wire an array of complex waveforms to time signal in,
      LabVIEW selects the Extract Multiple Tone Information N Chan (CDB) instance by
        default.

      A real multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

      A complex multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For

1146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1147 ordinal=1147 -->
## Functions

Functions

a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
Fs/2).

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform Measurements\
   Complex Multi-Tone Measurements.vi
ExtractExtract MultipleMultiple ToneTone InformationInformation NN ChanChan -- NN
SpecsSpecs (CDB)(CDB) VIVI

Returns the frequency, amplitude, and phase for each signal tone whose amplitude
exceeds a specified threshold. Wire data to the time signal in input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      time signals in —

    time signals in is an array of time-domain waveforms.

   •      export mode —

    export mode selects the source of the signal and spectrum to export to exported signals.

    0  none—Fastest computation
    1  input signal—Input signal only


                                                    © National Instruments 1147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1148 ordinal=1148 -->
## Functions

Functions


           2  detected signal—Multiple tone
           3  residual signal—Signal minus tone

               •      threshold —

            threshold specifies the minimum amplitude that each tone must exceed for this VI to extract it
           from time signals in. Each element of the array is the threshold for one signal in time signals in.

               •     max num tones —

         max num tones specifies the maximum number of tones that this VI extracts from each signal. If
           you set max num tones to –1, this VI extracts all tones whose amplitude exceeds threshold.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      output sorting —

           output sorting specifies the sorting order of the tones that this VI extracts.

           0    increasing frequency
           1    decreasing amplitude

               •      exported signals —

           exported signals is an array of exported signals.

                     •      exported time signal —

               exported time signal is the waveform containing the exported time signal as selected by
                export mode.

                     •      exported spectrum (dB) —

               exported spectrum (dB) is the spectrum of the exported time signal as selected by export
              mode.

                           •       f0 —


1148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1149 ordinal=1149 -->
## Functions

Functions


            f0 returns the start frequency, in hertz, of the spectrum.

             •       df —

           df returns the frequency resolution, in hertz, of the spectrum.

             •     dB Spectrum (Hann) —

        dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
            signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


•      multiple tone information —

  multiple tone information returns the frequency, amplitude, and phase of each tone that this VI
  extracts. Each element of the array is the multiple tone information for one signal in time signals
   in.

      •      multiple tone information —

      multiple tone information returns the frequency, amplitude, and phase of each sine tone
       that this VI extracts. Each element of the array is the multiple tone information for one
       signal in time signals in.

             •      detected frequency —

          detected frequency is the frequency of the detected single tone in Hz.

             •      detected amplitude —

          detected amplitude is the peak amplitude of the detected single tone.

             •      detected phase (deg) —

          detected phase is the phase of the detected single tone in degrees.

         Use the Wrap Angle VI to change the units of detected phase. Wire detected phase to


                                                   © National Instruments 1149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1150 ordinal=1150 -->
## Functions

Functions


                    the angle in input on the Wrap Angle VI, and select degree in, degree out or
               degree in, radians out for the angle units input.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The input signal can be real or complex and single-channel, in the form of a waveform,
       or multichannel, in the form of an array of waveforms. If you wire an array of real
      waveforms to time signal in, LabVIEW selects the Extract Multiple Tone Information N
      Chan instance by default. If you wire an array of complex waveforms to time signal in,
      LabVIEW selects the Extract Multiple Tone Information N Chan (CDB) instance by
        default.

      A real multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

      A complex multiple tone signal can be expressed as shown in the following equation:


      where Ai, fi, and φi are the amplitude, frequency, and phase, respectively, of the ith
      tone of a multiple tone signal with Ntones and Fs is the sample rate in samples per
      second of the input waveform signal.

       For a real signal, the frequency range is (min frequency, max frequency) = (0, Fs/2). For

1150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1151 ordinal=1151 -->
## Functions

Functions

a complex signal, the frequency range is (min frequency, max frequency) = (–Fs/2,
Fs/2).

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform Measurements\
   Complex Multi-Tone Measurements.vi
HarmonicHarmonic DistortionDistortion AnalyzerAnalyzer

Takes a signal in and performs a full harmonic analysis, including measuring the
fundamental frequency tone and harmonics, and returning the fundamental
frequency, all harmonic amplitude levels, and the total harmonic distortion (THD).
Wire data to the signal in input to determine the polymorphic instance to use or
manually select the instance.


   • Harmonic Distortion Analyzer 1 Chan VI
   • Harmonic Distortion Analyzer N Chan VI

This VI is designed to process a single channel or multiple channels continuously,
typically from within a For Loop or a While Loop.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Waveform Measurements\
   Multitone with Amplitudes and Phases.vi


                                                    © National Instruments 1151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1152 ordinal=1152 -->
## Functions

Functions

   HarmonicHarmonic DistortionDistortion AnalyzerAnalyzer 11 ChanChan VIVI

      Takes a signal in and performs a full harmonic analysis, including measuring the
      fundamental frequency tone and harmonics, and returning the fundamental
       frequency, all harmonic amplitude levels, and the total harmonic distortion (THD).
       Wire data to the signal in input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      stop search at Nyquist —

            stop search at Nyquist should be set to TRUE (default) to include only frequencies less than the
            Nyquist frequency, or half the sampling rate, in the harmonic search.

         When set to FALSE, this VI continues searching the frequency domain beyond Nyquist by
           assuming that these higher frequency components have aliased according to the following
            equation. aliased f = Fs – (f modulo Fs) where Fs = 1/dt = sampling rate.

               •       signal in —

             signal in is the input time-domain signal.

               •      export mode —

            export mode selects the source of the signal and spectrum to export to exported signals.

           0 none—Fastest computation
           1 input signal—Input signal only
           2 fundamental signal—Single sine tone
           3 residual signal—Signal minus tone
           4 harmonics only—Detected harmonics
           5 noise and spurs—Signal minus tone and harmonics


1152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1153 ordinal=1153 -->
## Functions

Functions

•      highest harmonic —

  highest harmonic controls the highest harmonic, including the fundamental tone, used for the
  harmonic analysis. For example, for 3rd harmonic analysis, this control should be set to 3 to
  measure the fundamental, second, and third harmonic.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      advanced search —

  advanced search controls the frequency domain search area, which is the center frequency and
  width, used for finding the fundamental frequency tone of the signal.

      •      approx freq. (optional) —

      approx freq. is the center frequency used in the frequency domain search for the
      fundamental tone frequency. If set to the default value of –1.0, the tone with the highest
      amplitude is used as the fundamental tone.

      •      search (+/- % of Fsampl.) —

      search is the frequency width, as a percentage of the sampling rate, for the frequency
     domain search for the fundamental tone frequency.


•      exported signals —

  exported signals contains the signals specified by export mode.

      •      exported time signal —

      exported time signal is the waveform containing the exported time signal as selected by
      export mode.

      •      exported spectrum (dB) —

      exported spectrum (dB) is the spectrum of the exported time signal as selected by export
     mode.


                                                   © National Instruments 1153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1154 ordinal=1154 -->
## Functions

Functions


                           •       f0 —

                      f0 returns the start frequency, in hertz, of the spectrum.

                           •       df —

                     df returns the frequency resolution, in hertz, of the spectrum.

                           •     dB Spectrum (Hann) —

                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      detected fundamental frequency —

            detected fundamental frequency contains the detected fundamental frequency resulting from
            searching the frequency domain. Use advanced search to set the frequency search range. All
           harmonics are measured at integer multiples of this fundamental frequency.

               •     THD —

         THD contains the measured total harmonic distortion up to and including the highest harmonic.
         THD is defined as the ratio of the RMS sum of the harmonics to the amplitude of the
           fundamental tone. To compute THD as a percentage, you must multiply it by 100.

               •     components level —

          components level contains the array of amplitudes of the measured harmonics in volts if the
             signal in is in volts. The array index is the harmonic number including 0 (DC), 1 (fundamental), 2
            (second harmonic),... n (nth harmonic), up to and including the highest harmonic.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurement info —

          measurement info returns information about your measurement, mainly warnings for
             inconsistencies in your input signal.


1154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1155 ordinal=1155 -->
## Functions

Functions


         •      uncertainty —

        uncertainty is reserved for future use.

         •      Warning —

       Warning is TRUE if a warning is generated during processing.

         •     comments —

       comments contains a warning message when Warning is TRUE.


This VI is designed to process a single channel or multiple channels continuously,
typically from within a For Loop or a While Loop.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Multitone with Amplitudes and Phases.vi
HarmonicHarmonic DistortionDistortion AnalyzerAnalyzer NN ChanChan VIVI

Takes a signal in and performs a full harmonic analysis, including measuring the
fundamental frequency tone and harmonics, and returning the fundamental
frequency, all harmonic amplitude levels, and the total harmonic distortion (THD).
Wire data to the signal in input to determine the polymorphic instance to use or
manually select the instance.

      Note

      The multichannel waveform array input should be the result of a
       multichannel acquisition where each element of the array of waveforms is a


                                                    © National Instruments 1155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1156 ordinal=1156 -->
## Functions

Functions


                 distinct and separate channel of data.


      Inputs/Outputs

               •      stop search at Nyquist —

            stop search at Nyquist should be set to TRUE (default) to include only frequencies less than the
            Nyquist frequency, or half the sampling rate, in the harmonic search.

         When set to FALSE, this VI continues searching the frequency domain beyond Nyquist by
           assuming that these higher frequency components have aliased according to the following
            equation. aliased f = Fs – (f modulo Fs) where Fs = 1/dt = sampling rate.

               •       signals in —

             signals in is the array of input time-domain signals.

               •      export mode —

            export mode selects the source of the signal and spectrum to export to exported signals.

           0 none—Fastest computation
           1 input signal—Input signal only
           2 fundamental signal—Single sine tone
           3 residual signal—Signal minus tone
           4 harmonics only—Detected harmonics
           5 noise and spurs—Signal minus tone and harmonics

               •      highest harmonic —

            highest harmonic controls the highest harmonic, including the fundamental tone, used for the
           harmonic analysis. For example, for 3rd harmonic analysis, this control should be set to 3 to


1156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1157 ordinal=1157 -->
## Functions

Functions


  measure the fundamental, second, and third harmonic.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      advanced search —

  advanced search controls the frequency domain search area, which is the center frequency and
  width, used for finding the fundamental frequency tone of the signal.

      •      approx freq. (optional) —

      approx freq. is the center frequency used in the frequency domain search for the
      fundamental tone frequency. If set to the default value of –1.0, the tone with the highest
      amplitude is used as the fundamental tone.

      •      search (+/- % of Fsampl.) —

      search is the frequency width, as a percentage of the sampling rate, for the frequency
     domain search for the fundamental tone frequency.


•      exported signals —

  exported signals is an array of exported signals.

      •      exported time signal —

      exported time signal is the waveform containing the exported time signal as selected by
      export mode.

      •      exported spectrum (dB) —

      exported spectrum (dB) is the spectrum of the exported time signal as selected by export
     mode.

             •       f0 —


                                                   © National Instruments 1157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1158 ordinal=1158 -->
## Functions

Functions


                      f0 returns the start frequency, in hertz, of the spectrum.

                           •       df —

                     df returns the frequency resolution, in hertz, of the spectrum.

                           •     dB Spectrum (Hann) —

                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      detected fundamental frequencies —

            detected fundamental frequencies is an array containing the detected fundamental frequency
             resulting from searching the frequency domain for each waveform.

               •     THD —

         THD returns an array containing the measured total harmonic distortion for each waveform.

               •     components levels —

          components levels is a cluster containing an array of amplitudes of the measured harmonics for
           each waveform.

                     •     components level —

              components level contains the array of amplitudes of the measured harmonics in volts if
                the signal in is in volts. The array index is the harmonic number including 0 (DC), 1
                 (fundamental), 2 (second harmonic),... n (nth harmonic), up to and including the highest
               harmonic.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurements info —


1158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1159 ordinal=1159 -->
## Functions

Functions


    measurements info is an array that returns information about your measurement, mainly
    warnings for inconsistencies in your input signal.

         •      uncertainty —

        uncertainty is reserved for future use.

         •      Warning —

       Warning is TRUE if a warning is generated during processing.

         •     comments —

       comments contains a warning message when Warning is TRUE.


This VI is designed to process a single channel or multiple channels continuously,
typically from within a For Loop or a While Loop.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Multitone with Amplitudes and Phases.vi
SINADSINAD AnalyzerAnalyzer

Takes a signal in and performs a full Signal in Noise and Distortion (SINAD) analysis,
including measuring the fundamental frequency tone and returning the fundamental
frequency and SINAD level in dB. Wire data to the signal in input to determine the
polymorphic instance to use or manually select the instance.


  • SINAD Analyzer 1 Chan VI

                                                    © National Instruments 1159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1160 ordinal=1160 -->
## Functions

Functions

            • SINAD Analyzer N Chan VI

       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

     THD Plus Noise in dB is the negative of the SINAD in dB.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        SINAD Measurement.vi
   SINADSINAD AnalyzerAnalyzer 11 ChanChan VIVI

      Takes a signal in and performs a full Signal in Noise and Distortion (SINAD) analysis,
       including measuring the fundamental frequency tone and returning the fundamental
       frequency and SINAD level in dB. Wire data to the signal in input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       signal in —

             signal in is the input time-domain signal.

               •      export mode —

            export mode selects the source of the signal and spectrum to export to exported signals.


1160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1161 ordinal=1161 -->
## Functions

Functions


  0  none—Fastest computation
  1  input signal—Input signal only
  2  detected signal—Single tone
  3  residual signal—Signal minus tone

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      advanced search —

  advanced search controls the frequency domain search area, which is the center frequency and
  width, used for finding the fundamental frequency tone of the signal.

      •      approx freq. (optional) —

      approx freq. is the center frequency used in the frequency domain search for the
      fundamental tone frequency. If set to the default value of –1.0, the tone with the highest
      amplitude is used as the fundamental tone.

      •      search (+/- % of Fsampl.) —

      search is the frequency width, as a percentage of the sampling rate, for the frequency
     domain search for the fundamental tone frequency.


•      exported signals —

  exported signals contains the signals specified by export mode.

      •      exported time signal —

      exported time signal is the waveform containing the exported time signal as selected by
      export mode.

      •      exported spectrum (dB) —

      exported spectrum (dB) is the spectrum of the exported time signal as selected by export
     mode.


                                                   © National Instruments 1161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1162 ordinal=1162 -->
## Functions

Functions


                           •       f0 —

                      f0 returns the start frequency, in hertz, of the spectrum.

                           •       df —

                     df returns the frequency resolution, in hertz, of the spectrum.

                           •     dB Spectrum (Hann) —

                dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
                        signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


               •      detected fundamental frequency —

            detected fundamental frequency contains the detected fundamental frequency resulting from
            searching the frequency domain. Use advanced search to set the frequency search range.

               •     SINAD (dB) —

          SINAD contains the measured Signal in Noise and Distortion (SINAD) expressed in dB. SINAD is
            defined as the ratio of the RMS energy of signal in to the RMS energy of signal in less the energy
              in the fundamental. To compute the THD Plus Noise in dB, simply negate the SINAD in dB.

               •     THD Plus Noise —

         THD Plus Noise contains the measured total harmonic distortion plus noise. THD Plus Noise is
            defined as the ratio of the RMS energy of signal in less the energy in the fundamental to the RMS
           energy of signal in. To compute THD Plus Noise as a percentage, you must multiply it by 100.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurement info —

          measurement info returns information about your measurement, mainly warnings for
             inconsistencies in your input signal.

                     •      uncertainty —


1162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1163 ordinal=1163 -->
## Functions

Functions


        uncertainty is reserved for future use.

         •      Warning —

       Warning is TRUE if a warning is generated during processing.

         •     comments —

       comments contains a warning message when Warning is TRUE.


This VI is designed to process a single channel or multiple channels continuously,
typically from within a For Loop or a While Loop.

THD Plus Noise in dB is the negative of the SINAD in dB.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   SINAD Measurement.vi
SINADSINAD AnalyzerAnalyzer NN ChanChan VIVI

Takes a signal in and performs a full Signal in Noise and Distortion (SINAD) analysis,
including measuring the fundamental frequency tone and returning the fundamental
frequency and SINAD level in dB. Wire data to the signal in input to determine the
polymorphic instance to use or manually select the instance.

      Note

      The multichannel waveform array input should be the result of a
       multichannel acquisition where each element of the array of waveforms is a


                                                    © National Instruments 1163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1164 ordinal=1164 -->
## Functions

Functions


                 distinct and separate channel of data.


      Inputs/Outputs

               •       signals in —

             signals in is the array of input time-domain signals.

               •      export mode —

            export mode selects the source of the signal and spectrum to export to exported signals.

           0  none—Fastest computation
           1  input signal—Input signal only
           2  detected signal—Single tone
           3  residual signal—Signal minus tone

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      advanced search —

           advanced search controls the frequency domain search area, which is the center frequency and
            width, used for finding the fundamental frequency tone of the signal.

                     •      approx freq. (optional) —

               approx freq. is the center frequency used in the frequency domain search for the
               fundamental tone frequency. If set to the default value of –1.0, the tone with the highest


1164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1165 ordinal=1165 -->
## Functions

Functions


      amplitude is used as the fundamental tone.

      •      search (+/- % of Fsampl.) —

      search is the frequency width, as a percentage of the sampling rate, for the frequency
     domain search for the fundamental tone frequency.


•      exported signals —

  exported signals is an array of exported signals.

      •      exported time signal —

      exported time signal is the waveform containing the exported time signal as selected by
      export mode.

      •      exported spectrum (dB) —

      exported spectrum (dB) is the spectrum of the exported time signal as selected by export
     mode.

             •       f0 —

            f0 returns the start frequency, in hertz, of the spectrum.

             •       df —

           df returns the frequency resolution, in hertz, of the spectrum.

             •     dB Spectrum (Hann) —

        dB Spectrum (Hann) is the magnitude spectrum of the (Hanning) windowed input
            signal, expressed in dB relative to 1.0 Vrms^2 for input signals in units of volts (V).


•      detected fundamental frequencies —

  detected fundamental frequencies is an array containing the detected fundamental frequency
  resulting from searching the frequency domain for each waveform.

•     SINAD (dB) —

                                                   © National Instruments 1165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1166 ordinal=1166 -->
## Functions

Functions


          SINAD is an array containing the measured Signal in Noise and Distortion (SINAD) for each
           waveform expressed in dB. SINAD is defined as the ratio of the RMS energy of the input signal to
            the RMS energy of the input signal less the energy in the fundamental. To compute the THD Plus
            Noise in dB, simply negate the SINAD in dB.

               •     THD Plus Noise —

         THD Plus Noise is an array containing the measured total harmonic distortion plus noise for
           each waveform.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     measurements info —

          measurements info is an array that returns information about your measurement, mainly
           warnings for inconsistencies in your input signal.

                     •      uncertainty —

                uncertainty is reserved for future use.

                     •      Warning —

              Warning is TRUE if a warning is generated during processing.

                     •     comments —

             comments contains a warning message when Warning is TRUE.


       This VI is designed to process a single channel or multiple channels continuously,
        typically from within a For Loop or a While Loop.

     THD Plus Noise in dB is the negative of the SINAD in dB.

     Examples

       Refer to the following example files included with LabVIEW.


1166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1167 ordinal=1167 -->
## Functions

Functions

  • labview\examples\Signal Processing\Waveform Measurements\
   SINAD Measurement.vi
FFTFFT PowerPower SpectrumSpectrum andand PSDPSD

Computes the averaged auto power spectrum of time signal. Wire data to the time
signal input to determine the polymorphic instance to use or manually select the
instance.


  • FFT Power Spectrum and PSD for 1 Chan VI
  • FFT Power Spectrum and PSD for N Chan VI
  • FFT Power Spectrum and PSD for 1 Chan (CDB) VI
  • FFT Power Spectrum and PSD for N Chan (CDB) VI

The FFT Power Spectrum VI completes the following steps to compute power
spectrum or power spectral density:

 1. Computes the FFT of time signal.
 2. Forms the power spectrum or power spectral density of time signal.
 3. Averages the current power spectrum/power spectral density with the power
   spectra/power spectral densities computed in previous calls to the VI since the last
   time the averaging process was restarted.
 4. Returns the averaged power spectrum or power spectral densities in Power
   Spectrum/PSD.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without
using the restart averaging control to clear the history results in an unexpected

                                                    © National Instruments 1167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1168 ordinal=1168 -->
## Functions

Functions

       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to
              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.
   FFTFFT PowerPower SpectrumSpectrum andand PSDPSD forfor 11 ChanChan VIVI

      Computes the averaged auto power spectrum of time signal. Wire data to the time
       signal input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •      export mode —

            export mode selects the output to export to Power Spectrum / PSD.

           0 Power Spectrum–exports the power spectrum of the input signal.
           1 Power Spectral Density–exports the power spectral density of the input signal.

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical


1168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1169 ordinal=1169 -->
## Functions

Functions


  case when you should restart averaging is when a major input change occurs in the middle of
  the averaging process.

•      time signal —

  time signal is the input time-domain waveform.

•     window —

  window (Hanning) is the time-domain window to apply to the time signal. The default window
   is Hanning.

  0          Rectangle
  1         Hanning (default)
  2        Hamming
  3          Blackman-Harris
  4          Exact Blackman
  5         Blackman
  6           Flat Top
  7         4 Term B-Harris
  8         7 Term B-Harris
  9        Low Sidelobe
  11        Blackman Nutall
  30         Triangle
  31         Bartlett-Hanning
  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•     dB On (F) —

  dB On specifies whether the results are expressed in decibels. The default is FALSE.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

                                                   © National Instruments 1169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1170 ordinal=1170 -->
## Functions

Functions


            averaging parameters is a cluster that defines how this VI computes the averaging. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.

                 No averaging
               0                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential               1                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •     Power Spectrum / PSD —

          Power Spectrum / PSD returns the averaged power spectrum or power spectral density and the


1170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1171 ordinal=1171 -->
## Functions

Functions


    frequency scale, according to export mode.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      magnitude —

       magnitude is the magnitude of the averaged power spectrum or power spectral density.

              If the input signal is in volts (V), magnitude has units of volts-rms squared (Vrms²) for power
        spectrum and volts-rms squared per hertz (Vrms²/Hz) for power spectral density. If the input
         signal is not in volts, magnitude has units of the input signal unit-rms squared for power
        spectrum, and input signal unit-rms squared per hertz for power spectral density. If dB On is
       TRUE and the input signal is in volts, magnitude has units of dBV for power spectrum and
        dBV/Hz for power spectral density.


   •      averaging done —

    averaging done returns TRUE when averages completed is greater than or equal to the number
    of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
    averaging done is always TRUE if the selected averaging mode is No averaging.

   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The FFT Power Spectrum VI completes the following steps to compute power
spectrum or power spectral density:

 1. Computes the FFT of time signal.
 2. Forms the power spectrum or power spectral density of time signal.


                                                    © National Instruments 1171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1172 ordinal=1172 -->
## Functions

Functions

         3. Averages the current power spectrum/power spectral density with the power
          spectra/power spectral densities computed in previous calls to the VI since the last
          time the averaging process was restarted.
         4. Returns the averaged power spectrum or power spectral densities in Power
         Spectrum/PSD.

      The single-channel version of this VI can perform single-channel measurements in
      both one-shot mode, meaning a single call, and continuous mode, meaning multiple
        calls with history. The single-channel version can perform multichannel
      measurements only in one-shot mode. If you want to make multichannel
      measurements in continuous mode, use the multichannel version of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling the single-channel version to process another channel without
       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to
              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.
   FFTFFT PowerPower SpectrumSpectrum andand PSDPSD forfor NN ChanChan VIVI

      Computes the averaged auto power spectrum of time signal. Wire data to the time
       signal input to determine the polymorphic instance to use or manually select the
       instance.


1172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1173 ordinal=1173 -->
## Functions

Functions

Inputs/Outputs

   •      export mode —

    export mode selects the output to export to Power Spectrum / PSD.

    0 Power Spectrum–exports the power spectrum of the input signal.
    1 Power Spectral Density–exports the power spectral density of the input signal.

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signals —

    time signals is the input array of time-domain waveforms.

   •     window —

   window (Hanning) is the time-domain window to apply to the time signal. The default window
      is Hanning.

    0          Rectangle
    1         Hanning (default)
    2        Hamming
    3          Blackman-Harris
    4          Exact Blackman
    5         Blackman
    6           Flat Top
    7         4 Term B-Harris
    8         7 Term B-Harris
    9        Low Sidelobe
    11        Blackman Nutall
    30         Triangle
    31         Bartlett-Hanning


                                                    © National Instruments 1173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1174 ordinal=1174 -->
## Functions

Functions


           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •     dB On (F) —

         dB On specifies whether the results are expressed in decibels. The default is FALSE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how this VI computes the averaging. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.

                 No averaging               0                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential
               1
                            (default)


1174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1175 ordinal=1175 -->
## Functions

Functions


      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     window parameter —

  window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
  a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
  window. If window is any other window, this VI ignores this input.

  The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•     Power Spectrum / PSD —

  Power Spectrum / PSD returns the averaged power spectrum or power spectral density and the
  frequency scale, according to export mode.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •      magnitude —

      magnitude is the magnitude of the averaged power spectrum or power spectral density.

          If the input signal is in volts (V), magnitude has units of volts-rms squared (Vrms²) for power
      spectrum and volts-rms squared per hertz (Vrms²/Hz) for power spectral density. If the input
       signal is not in volts, magnitude has units of the input signal unit-rms squared for power
      spectrum, and input signal unit-rms squared per hertz for power spectral density. If dB On is
     TRUE and the input signal is in volts, magnitude has units of dBV for power spectrum and
      dBV/Hz for power spectral density.


•      averaging done —


                                                   © National Instruments 1175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1176 ordinal=1176 -->
## Functions

Functions


            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The FFT Power Spectrum VI completes the following steps to compute power
      spectrum or power spectral density:

         1. Computes the FFT of time signal.
         2. Forms the power spectrum or power spectral density of time signal.
         3. Averages the current power spectrum/power spectral density with the power
          spectra/power spectral densities computed in previous calls to the VI since the last
          time the averaging process was restarted.
         4. Returns the averaged power spectrum or power spectral densities in Power
         Spectrum/PSD.

      The single-channel version of this VI can perform single-channel measurements in
      both one-shot mode, meaning a single call, and continuous mode, meaning multiple
        calls with history. The single-channel version can perform multichannel
      measurements only in one-shot mode. If you want to make multichannel
      measurements in continuous mode, use the multichannel version of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling the single-channel version to process another channel without
       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to


1176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1177 ordinal=1177 -->
## Functions

Functions


       the multichannel case and use the single-channel version in a For Loop to
       continuously process multiple channels by indexing an array of waveforms.
FFTFFT PowerPower SpectrumSpectrum andand PSDPSD forfor 11 ChanChan
(CDB)(CDB) VIVI

Computes the averaged auto power spectrum of time signal. Wire data to the time
signal input to determine the polymorphic instance to use or manually select the
instance.


Inputs/Outputs

   •      export mode —

    export mode selects the output to export to Power Spectrum / PSD.

    0 Power Spectrum–exports the power spectrum of the input signal.
    1 Power Spectral Density–exports the power spectral density of the input signal.

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signal —


                                                    © National Instruments 1177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1178 ordinal=1178 -->
## Functions

Functions


           time signal is the input time-domain waveform.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •     dB On (F) —

         dB On specifies whether the results are expressed in decibels. The default is FALSE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how this VI computes the averaging. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.


1178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1179 ordinal=1179 -->
## Functions

Functions


      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential
      1                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     window parameter —

  window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
  a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
  window. If window is any other window, this VI ignores this input.

  The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•     Power Spectrum / PSD —

  Power Spectrum / PSD returns the averaged power spectrum or power spectral density and the
  frequency scale, according to export mode.

      •       f0 —


                                                   © National Instruments 1179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1180 ordinal=1180 -->
## Functions

Functions


                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged power spectrum or power spectral density.

                           If the input signal is in volts (V), magnitude has units of volts-rms squared (Vrms²) for power
               spectrum and volts-rms squared per hertz (Vrms²/Hz) for power spectral density. If the input
                  signal is not in volts, magnitude has units of the input signal unit-rms squared for power
                spectrum, and input signal unit-rms squared per hertz for power spectral density. If dB On is
             TRUE and the input signal is in volts, magnitude has units of dBV for power spectrum and
               dBV/Hz for power spectral density.


               •      averaging done —

            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The FFT Power Spectrum VI completes the following steps to compute power
      spectrum or power spectral density:

         1. Computes the FFT of time signal.
         2. Forms the power spectrum or power spectral density of time signal.
         3. Averages the current power spectrum/power spectral density with the power
          spectra/power spectral densities computed in previous calls to the VI since the last
          time the averaging process was restarted.

1180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1181 ordinal=1181 -->
## Functions

Functions

 4. Returns the averaged power spectrum or power spectral densities in Power
   Spectrum/PSD.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without
using the restart averaging control to clear the history results in an unexpected
behavior of this VI. The unexpected behavior results from the VI passing the internal
state information from one channel to another.

      Note The single-channel version of this VI is intended primarily for
       continuous processing of a single channel. Do not generalize this behavior to
       the multichannel case and use the single-channel version in a For Loop to
       continuously process multiple channels by indexing an array of waveforms.
FFTFFT PowerPower SpectrumSpectrum andand PSDPSD forfor NN ChanChan
(CDB)(CDB) VIVI

Computes the averaged auto power spectrum of time signal. Wire data to the time
signal input to determine the polymorphic instance to use or manually select the
instance.


                                                    © National Instruments 1181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1182 ordinal=1182 -->
## Functions

Functions

      Inputs/Outputs

               •      export mode —

            export mode selects the output to export to Power Spectrum / PSD.

           0 Power Spectrum–exports the power spectrum of the input signal.
           1 Power Spectral Density–exports the power spectral density of the input signal.

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signals —

           time signals is the input array of time-domain waveforms.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning


1182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1183 ordinal=1183 -->
## Functions

Functions


  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•     dB On (F) —

  dB On specifies whether the results are expressed in decibels. The default is FALSE.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters is a cluster that defines how this VI computes the averaging. The
  specifications of the parameters include the type of averaging, the type of weighting, and the
  number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential
      1
                 (default)


                                                   © National Instruments 1183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1184 ordinal=1184 -->
## Functions

Functions


                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •     Power Spectrum / PSD —

          Power Spectrum / PSD returns the averaged power spectrum or power spectral density and the
            frequency scale, according to export mode.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged power spectrum or power spectral density.

                           If the input signal is in volts (V), magnitude has units of volts-rms squared (Vrms²) for power
               spectrum and volts-rms squared per hertz (Vrms²/Hz) for power spectral density. If the input
                  signal is not in volts, magnitude has units of the input signal unit-rms squared for power
                spectrum, and input signal unit-rms squared per hertz for power spectral density. If dB On is
             TRUE and the input signal is in volts, magnitude has units of dBV for power spectrum and
               dBV/Hz for power spectral density.


               •      averaging done —


1184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1185 ordinal=1185 -->
## Functions

Functions


    averaging done returns TRUE when averages completed is greater than or equal to the number
    of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
    averaging done is always TRUE if the selected averaging mode is No averaging.

   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The FFT Power Spectrum VI completes the following steps to compute power
spectrum or power spectral density:

 1. Computes the FFT of time signal.
 2. Forms the power spectrum or power spectral density of time signal.
 3. Averages the current power spectrum/power spectral density with the power
   spectra/power spectral densities computed in previous calls to the VI since the last
   time the averaging process was restarted.
 4. Returns the averaged power spectrum or power spectral densities in Power
   Spectrum/PSD.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without
using the restart averaging control to clear the history results in an unexpected
behavior of this VI. The unexpected behavior results from the VI passing the internal
state information from one channel to another.

      Note The single-channel version of this VI is intended primarily for
       continuous processing of a single channel. Do not generalize this behavior to


                                                    © National Instruments 1185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1186 ordinal=1186 -->
## Functions

Functions


              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.
   FFTFFT SpectrumSpectrum (Mag-Phase)(Mag-Phase)

      Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
      magnitude and phase. Wire data to the time signal input to determine the
      polymorphic instance to use or manually select the instance.


            • FFT Spectrum (Mag-Phase) for 1 Chan VI
            • FFT Spectrum (Mag-Phase) for N Chan VI
            • FFT Spectrum (Mag-Phase) for 1 Chan (CDB) VI
            • FFT Spectrum (Mag-Phase) for N Chan (CDB) VI

      The FFT Spectrum (Mag-Phase) VI completes the following steps to compute
      magnitude and phase:

         1. Computes the FFT of time signal.
         2. Averages the current FFT spectrum of time signal with the FFT spectra computed
         by the VI since the last time the averaging process was reset.
         3. Returns the magnitude and phase of the averaged spectrum.

      The single-channel version of this VI can perform single-channel measurements in
      both one-shot mode, meaning a single call, and continuous mode, meaning multiple
        calls with history. The single-channel version can perform multichannel
      measurements only in one-shot mode. If you want to make multichannel
      measurements in continuous mode, use the multichannel version of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling the single-channel version to process another channel without
       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.


1186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1187 ordinal=1187 -->
## Functions

Functions

      Note The single-channel version of this VI is intended primarily for
       continuous processing of a single channel. Do not generalize this behavior to
       the multichannel case and use the single-channel version in a For Loop to
       continuously process multiple channels by indexing an array of waveforms.

        Refer to the following LabVIEW project for examples of using a multichannel
        version of a VI like the FFT Spectrum (Mag-Phase) VI in a loop:

      labview\examples\Signal Processing\Waveform
      Measurements\Waveform Measurements.lvproj


Related Information

Output Units for FFT-Based Vis
FFTFFT SpectrumSpectrum (Mag-Phase)(Mag-Phase) forfor 11 ChanChan VIVI

Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
magnitude and phase. Wire data to the time signal input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.


                                                    © National Instruments 1187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1188 ordinal=1188 -->
## Functions

Functions


         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signal —

           time signal is the input time-domain waveform.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •      view —

           view defines how the different results from this VI are returned.

                     •     dB On (F) —

             dB On specifies whether the results are expressed in decibels. The default is FALSE.


1188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1189 ordinal=1189 -->
## Functions

Functions


      •     unwrap phase (F) —

     unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
       discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
      the phase is not unwrapped.

     When unwrap phase is TRUE, the phase is unwrapped.

      •      convert to degree (F) —

      convert to degree specifies whether the phase results are converted from radians to
      degrees. The default is FALSE, which means that results are expressed in radians.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters is a cluster that defines how this VI computes the averaging. The
  specifications of the parameters include the type of averaging, the type of weighting, and the
  number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging
      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear


                                                   © National Instruments 1189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1190 ordinal=1190 -->
## Functions

Functions


                         Exponential               1
                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •      averaging done —

            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •      magnitude —

           magnitude returns the magnitude of the averaged FFT spectrum and the frequency scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged FFT spectrum.


1190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1191 ordinal=1191 -->
## Functions

Functions


              If the input signal is in volts (V), magnitude has units of volts-rms (Vrms). If the input signal is
        not in volts, magnitude has units of the input signal unit-rms. If dB On is TRUE and the
         input signal is in volts, magnitude has units of dBV.


   •      phase —

    phase returns the phase of the averaged FFT spectrum and the frequency scale.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      phase —

       phase is the phase, in radians, of the averaged FFT spectrum.


   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The FFT Spectrum (Mag-Phase) VI completes the following steps to compute
magnitude and phase:

 1. Computes the FFT of time signal.
 2. Averages the current FFT spectrum of time signal with the FFT spectra computed
   by the VI since the last time the averaging process was reset.
 3. Returns the magnitude and phase of the averaged spectrum.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple

                                                    © National Instruments 1191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1192 ordinal=1192 -->
## Functions

Functions

        calls with history. The single-channel version can perform multichannel
      measurements only in one-shot mode. If you want to make multichannel
      measurements in continuous mode, use the multichannel version of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling the single-channel version to process another channel without
       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to
              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.

               Refer to the following LabVIEW project for examples of using a multichannel
               version of a VI like the FFT Spectrum (Mag-Phase) VI in a loop:

           labview\examples\Signal Processing\Waveform
           Measurements\Waveform Measurements.lvproj


      Related Information

      Output Units for FFT-Based Vis
   FFTFFT SpectrumSpectrum (Mag-Phase)(Mag-Phase) forfor NN ChanChan VIVI

      Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
      magnitude and phase. Wire data to the time signal input to determine the
      polymorphic instance to use or manually select the instance.

           Note

               This VI applies the same averaging parameters settings to each waveform in


1192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1193 ordinal=1193 -->
## Functions

Functions


       time signals.


Inputs/Outputs

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signals —

    time signals is the input array of time-domain waveforms.

   •     window —

   window (Hanning) is the time-domain window to apply to the time signal. The default window
      is Hanning.

    0          Rectangle
    1         Hanning (default)
    2        Hamming
    3          Blackman-Harris
    4          Exact Blackman
    5         Blackman
    6           Flat Top
    7         4 Term B-Harris


                                                    © National Instruments 1193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1194 ordinal=1194 -->
## Functions

Functions


           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •      view —

           view defines how the different results from this VI are returned.

                     •     dB On (F) —

             dB On specifies whether the results are expressed in decibels. The default is FALSE.

                     •     unwrap phase (F) —

             unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
                  discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
                the phase is not unwrapped.

            When unwrap phase is TRUE, the phase is unwrapped.

                     •      convert to degree (F) —

                convert to degree specifies whether the phase results are converted from radians to
                 degrees. The default is FALSE, which means that results are expressed in radians.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how this VI computes the averaging. The


1194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1195 ordinal=1195 -->
## Functions

Functions


  specifications of the parameters include the type of averaging, the type of weighting, and the
  number of averages.

      •      averaging mode —

      averaging mode specifies the averaging modes.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential      1
                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     window parameter —

  window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
  a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
  window. If window is any other window, this VI ignores this input.

  The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.


                                                   © National Instruments 1195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1196 ordinal=1196 -->
## Functions

Functions


            averaging done is always TRUE if the selected averaging mode is No averaging.

               •      magnitudes —

           magnitudes is an array of magnitudes of the averaged FFT spectra, one per input waveform.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged FFT spectrum.

                           If the input signal is in volts (V), magnitude has units of volts-rms (Vrms). If the input signal is
                not in volts, magnitude has units of the input signal unit-rms. If dB On is TRUE and the
                 input signal is in volts, magnitude has units of dBV.


               •      phases —

           phases is an array of phases of the averaged FFT spectra, one per input waveform.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      phase —

              phase is the phase, in radians, of the averaged FFT spectrum.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.


1196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1197 ordinal=1197 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The FFT Spectrum (Mag-Phase) VI completes the following steps to compute
magnitude and phase:

 1. Computes the FFT of time signal.
 2. Averages the current FFT spectrum of time signal with the FFT spectra computed
   by the VI since the last time the averaging process was reset.
 3. Returns the magnitude and phase of the averaged spectrum.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without
using the restart averaging control to clear the history results in an unexpected
behavior of this VI. The unexpected behavior results from the VI passing the internal
state information from one channel to another.

      Note The single-channel version of this VI is intended primarily for
       continuous processing of a single channel. Do not generalize this behavior to
       the multichannel case and use the single-channel version in a For Loop to
       continuously process multiple channels by indexing an array of waveforms.

        Refer to the following LabVIEW project for examples of using a multichannel
        version of a VI like the FFT Spectrum (Mag-Phase) VI in a loop:

      labview\examples\Signal Processing\Waveform
      Measurements\Waveform Measurements.lvproj


                                                    © National Instruments 1197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1198 ordinal=1198 -->
## Functions

Functions

      Related Information

      Output Units for FFT-Based Vis
   FFTFFT SpectrumSpectrum (Mag-Phase)(Mag-Phase) forfor 11 ChanChan (CDB)(CDB)
    VIVI

      Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
      magnitude and phase. Wire data to the time signal input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signal —

           time signal is the input time-domain waveform.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.


1198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1199 ordinal=1199 -->
## Functions

Functions


  0          Rectangle
  1         Hanning (default)
  2        Hamming
  3          Blackman-Harris
  4          Exact Blackman
  5         Blackman
  6           Flat Top
  7         4 Term B-Harris
  8         7 Term B-Harris
  9        Low Sidelobe
  11        Blackman Nutall
  30         Triangle
  31         Bartlett-Hanning
  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•      view —

  view defines how the different results from this VI are returned.

      •     dB On (F) —

     dB On specifies whether the results are expressed in decibels. The default is FALSE.

      •     unwrap phase (F) —

     unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
       discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
      the phase is not unwrapped.

     When unwrap phase is TRUE, the phase is unwrapped.

      •      convert to degree (F) —

      convert to degree specifies whether the phase results are converted from radians to
      degrees. The default is FALSE, which means that results are expressed in radians.


                                                   © National Instruments 1199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1200 ordinal=1200 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how this VI computes the averaging. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.

                 No averaging               0                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential               1                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.


1200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1201 ordinal=1201 -->
## Functions

Functions


  The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•      magnitude —

  magnitude returns the magnitude of the averaged FFT spectrum and the frequency scale.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •      magnitude —

      magnitude is the magnitude of the averaged FFT spectrum.

          If the input signal is in volts (V), magnitude has units of volts-rms (Vrms). If the input signal is
      not in volts, magnitude has units of the input signal unit-rms. If dB On is TRUE and the
      input signal is in volts, magnitude has units of dBV.


•      phase —

  phase returns the phase of the averaged FFT spectrum and the frequency scale.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •      phase —


                                                   © National Instruments 1201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1202 ordinal=1202 -->
## Functions

Functions


              phase is the phase, in radians, of the averaged FFT spectrum.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The FFT Spectrum (Mag-Phase) VI completes the following steps to compute
      magnitude and phase:

         1. Computes the FFT of time signal.
         2. Averages the current FFT spectrum of time signal with the FFT spectra computed
         by the VI since the last time the averaging process was reset.
         3. Returns the magnitude and phase of the averaged spectrum.

      The single-channel version of this VI can perform single-channel measurements in
      both one-shot mode, meaning a single call, and continuous mode, meaning multiple
        calls with history. The single-channel version can perform multichannel
      measurements only in one-shot mode. If you want to make multichannel
      measurements in continuous mode, use the multichannel version of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling the single-channel version to process another channel without
       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to
              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.


1202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1203 ordinal=1203 -->
## Functions

Functions


        Refer to the following LabVIEW project for examples of using a multichannel
        version of a VI like the FFT Spectrum (Mag-Phase) VI in a loop:

      labview\examples\Signal Processing\Waveform
      Measurements\Waveform Measurements.lvproj


Related Information

Output Units for FFT-Based Vis
FFTFFT SpectrumSpectrum (Mag-Phase)(Mag-Phase) forfor NN ChanChan (CDB)(CDB)
VIVI

Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
magnitude and phase. Wire data to the time signal input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.


                                                    © National Instruments 1203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1204 ordinal=1204 -->
## Functions

Functions

               •      time signals —

           time signals is the input array of time-domain waveforms.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •      view —

           view defines how the different results from this VI are returned.

                     •     dB On (F) —

             dB On specifies whether the results are expressed in decibels. The default is FALSE.

                     •     unwrap phase (F) —

             unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
                  discontinuities that have an absolute value greater than pi. The default is FALSE, meaning


1204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1205 ordinal=1205 -->
## Functions

Functions


      the phase is not unwrapped.

     When unwrap phase is TRUE, the phase is unwrapped.

      •      convert to degree (F) —

      convert to degree specifies whether the phase results are converted from radians to
      degrees. The default is FALSE, which means that results are expressed in radians.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters is a cluster that defines how this VI computes the averaging. The
  specifications of the parameters include the type of averaging, the type of weighting, and the
  number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential
      1
                 (default)

      •     number of averages —


                                                   © National Instruments 1205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1206 ordinal=1206 -->
## Functions

Functions


             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •      averaging done —

            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •      magnitudes —

           magnitudes is an array of magnitudes of the averaged FFT spectra, one per input waveform.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged FFT spectrum.

                           If the input signal is in volts (V), magnitude has units of volts-rms (Vrms). If the input signal is
                not in volts, magnitude has units of the input signal unit-rms. If dB On is TRUE and the
                 input signal is in volts, magnitude has units of dBV.


               •      phases —


1206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1207 ordinal=1207 -->
## Functions

Functions


    phases is an array of phases of the averaged FFT spectra, one per input waveform.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      phase —

       phase is the phase of the averaged FFT spectrum.


   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The FFT Spectrum (Mag-Phase) VI completes the following steps to compute
magnitude and phase:

 1. Computes the FFT of time signal.
 2. Averages the current FFT spectrum of time signal with the FFT spectra computed
   by the VI since the last time the averaging process was reset.
 3. Returns the magnitude and phase of the averaged spectrum.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without
using the restart averaging control to clear the history results in an unexpected

                                                    © National Instruments 1207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1208 ordinal=1208 -->
## Functions

Functions

       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to
              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.

               Refer to the following LabVIEW project for examples of using a multichannel
               version of a VI like the FFT Spectrum (Mag-Phase) VI in a loop:

           labview\examples\Signal Processing\Waveform
           Measurements\Waveform Measurements.lvproj


      Related Information

      Output Units for FFT-Based Vis
   FFTFFT SpectrumSpectrum (Real-Im)(Real-Im)

      Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
        real and imaginary parts. Wire data to the time signal input to determine the
      polymorphic instance to use or manually select the instance.


            • FFT Spectrum (Real-Im) for 1 Chan VI
            • FFT Spectrum (Real-Im) for N Chan VI
            • FFT Spectrum (Real-Im) for 1 Chan (CDB) VI
            • FFT Spectrum (Real-Im) for N Chan (CDB) VI

      The FFT Spectrum (Real-IM) VI completes the following steps to compute real part and
      imaginary part:


1208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1209 ordinal=1209 -->
## Functions

Functions

 1. Computes the FFT of time signal.
 2. Averages the current FFT spectrum of time signal with the FFT spectra computed
   by the VI since the last time the averaging process was reset.
 3. Returns the real and imaginary parts of the averaged spectrum.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without
using the restart averaging control to clear the history results in an unexpected
behavior of this VI. The unexpected behavior results from the VI passing the internal
state information from one channel to another.

      Note The single-channel version of this VI is intended primarily for
       continuous processing of a single channel. Do not generalize this behavior to
       the multichannel case and use the single-channel version in a For Loop to
       continuously process multiple channels by indexing an array of waveforms.

        Refer to the following LabVIEW project for examples of using a multichannel
        version of a VI like the FFT Spectrum (Real-IM) VI in a loop:

                • labview\examples\Signal Processing\Waveform
          Measurements\Waveform Measurements.lvproj


Related Information

Output Units for FFT-Based VIs
FFTFFT SpectrumSpectrum (Real-Im)(Real-Im) forfor 11 ChanChan VIVI

Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as


                                                    © National Instruments 1209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1210 ordinal=1210 -->
## Functions

Functions

        real and imaginary parts. Wire data to the time signal input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signal —

           time signal is the input time-domain waveform.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall


1210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1211 ordinal=1211 -->
## Functions

Functions


  30         Triangle
  31         Bartlett-Hanning
  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters is a cluster that defines how this VI computes the averaging. The
  specifications of the parameters include the type of averaging, the type of weighting, and the
  number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential
      1
                 (default)

      •     number of averages —


                                                   © National Instruments 1211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1212 ordinal=1212 -->
## Functions

Functions


             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •      averaging done —

            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •       real part —

             real part returns the real part of the averaged FFT spectrum and the frequency scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •       real part —

                  real part is the real part of the averaged FFT spectrum.

                           If the input signal is in volts (V), real part has units of volts-rms (Vrms). If the input signal is
                not in volts, real part has units of the input signal unit-rms.


               •      imaginary part —


1212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1213 ordinal=1213 -->
## Functions

Functions


    imaginary part returns the imaginary part of the averaged FFT spectrum and the frequency
     scale.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      imaginary part —

        imaginary part is the imaginary part of the averaged FFT spectrum.


   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The FFT Spectrum (Real-IM) VI completes the following steps to compute real part and
imaginary part:

 1. Computes the FFT of time signal.
 2. Averages the current FFT spectrum of time signal with the FFT spectra computed
   by the VI since the last time the averaging process was reset.
 3. Returns the real and imaginary parts of the averaged spectrum.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without

                                                    © National Instruments 1213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1214 ordinal=1214 -->
## Functions

Functions

       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to
              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.

               Refer to the following LabVIEW project for examples of using a multichannel
               version of a VI like the FFT Spectrum (Real-IM) VI in a loop:

                          • labview\examples\Signal Processing\Waveform
               Measurements\Waveform Measurements.lvproj


      Related Information

      Output Units for FFT-Based VIs
   FFTFFT SpectrumSpectrum (Real-Im)(Real-Im) forfor NN ChanChan VIVI

      Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
        real and imaginary parts. Wire data to the time signal input to determine the
      polymorphic instance to use or manually select the instance.

           Note

               This VI applies the same averaging parameters settings to each waveform in
             time signals.


1214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1215 ordinal=1215 -->
## Functions

Functions


Inputs/Outputs

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signals —

    time signals is the input array of time-domain waveforms.

   •     window —

   window (Hanning) is the time-domain window to apply to the time signal. The default window
      is Hanning.

    0          Rectangle
    1         Hanning (default)
    2        Hamming
    3          Blackman-Harris
    4          Exact Blackman
    5         Blackman
    6           Flat Top
    7         4 Term B-Harris
    8         7 Term B-Harris
    9        Low Sidelobe
    11        Blackman Nutall
    30         Triangle
    31         Bartlett-Hanning
    32       Bohman
    33        Parzen


                                                    © National Instruments 1215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1216 ordinal=1216 -->
## Functions

Functions


           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how this VI computes the averaging. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.

                 No averaging               0                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential
               1
                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


1216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1217 ordinal=1217 -->
## Functions

Functions

•     window parameter —

  window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
  a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
  window. If window is any other window, this VI ignores this input.

  The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•       real parts —

  real parts returns an array of the real part of the averaged FFT spectra, one per input waveform.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •       real part —

       real part is the real part of the averaged FFT spectrum.

          If the input signal is in volts (V), real part has units of volts-rms (Vrms). If the input signal is
      not in volts, real part has units of the input signal unit-rms.


•      imaginary parts —

  imaginary parts returns the imaginary part of the averaged FFT spectra and the frequency scale.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.


                                                   © National Instruments 1217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1218 ordinal=1218 -->
## Functions

Functions


                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      imaginary part —

               imaginary part is the imaginary part of the averaged FFT spectrum.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The FFT Spectrum (Real-IM) VI completes the following steps to compute real part and
      imaginary part:

         1. Computes the FFT of time signal.
         2. Averages the current FFT spectrum of time signal with the FFT spectra computed
         by the VI since the last time the averaging process was reset.
         3. Returns the real and imaginary parts of the averaged spectrum.

      The single-channel version of this VI can perform single-channel measurements in
      both one-shot mode, meaning a single call, and continuous mode, meaning multiple
        calls with history. The single-channel version can perform multichannel
      measurements only in one-shot mode. If you want to make multichannel
      measurements in continuous mode, use the multichannel version of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling the single-channel version to process another channel without
       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for


1218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1219 ordinal=1219 -->
## Functions

Functions


       continuous processing of a single channel. Do not generalize this behavior to
       the multichannel case and use the single-channel version in a For Loop to
       continuously process multiple channels by indexing an array of waveforms.

        Refer to the following LabVIEW project for examples of using a multichannel
        version of a VI like the FFT Spectrum (Real-IM) VI in a loop:

                • labview\examples\Signal Processing\Waveform
          Measurements\Waveform Measurements.lvproj


Related Information

Output Units for FFT-Based VIs
FFTFFT SpectrumSpectrum (Real-Im)(Real-Im) forfor 11 ChanChan (CDB)(CDB) VIVI

Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
real and imaginary parts. Wire data to the time signal input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of


                                                    © National Instruments 1219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1220 ordinal=1220 -->
## Functions

Functions


            the averaging process.

               •      time signal —

           time signal is the input time-domain waveform.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how this VI computes the averaging. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.


1220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1221 ordinal=1221 -->
## Functions

Functions


      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential
      1                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     window parameter —

  window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
  a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
  window. If window is any other window, this VI ignores this input.

  The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•       real part —


                                                   © National Instruments 1221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1222 ordinal=1222 -->
## Functions

Functions


             real part returns the real part of the averaged FFT spectrum and the frequency scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •       real part —

                  real part is the real part of the averaged FFT spectrum.

                           If the input signal is in volts (V), real part has units of volts-rms (Vrms). If the input signal is
                not in volts, real part has units of the input signal unit-rms.


               •      imaginary part —

           imaginary part returns the imaginary part of the averaged FFT spectrum and the frequency
              scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      imaginary part —

               imaginary part is the imaginary part of the averaged FFT spectrum.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1223 ordinal=1223 -->
## Functions

Functions

The FFT Spectrum (Real-IM) VI completes the following steps to compute real part and
imaginary part:

 1. Computes the FFT of time signal.
 2. Averages the current FFT spectrum of time signal with the FFT spectra computed
   by the VI since the last time the averaging process was reset.
 3. Returns the real and imaginary parts of the averaged spectrum.

The single-channel version of this VI can perform single-channel measurements in
both one-shot mode, meaning a single call, and continuous mode, meaning multiple
calls with history. The single-channel version can perform multichannel
measurements only in one-shot mode. If you want to make multichannel
measurements in continuous mode, use the multichannel version of this VI.

The single-channel version of this VI maintains internal state information for a single
channel only. Calling the single-channel version to process another channel without
using the restart averaging control to clear the history results in an unexpected
behavior of this VI. The unexpected behavior results from the VI passing the internal
state information from one channel to another.

      Note The single-channel version of this VI is intended primarily for
       continuous processing of a single channel. Do not generalize this behavior to
       the multichannel case and use the single-channel version in a For Loop to
       continuously process multiple channels by indexing an array of waveforms.

        Refer to the following LabVIEW project for examples of using a multichannel
        version of a VI like the FFT Spectrum (Real-IM) VI in a loop:

                • labview\examples\Signal Processing\Waveform
          Measurements\Waveform Measurements.lvproj


Related Information

Output Units for FFT-Based VIs


                                                    © National Instruments 1223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1224 ordinal=1224 -->
## Functions

Functions

   FFTFFT SpectrumSpectrum (Real-Im)(Real-Im) forfor NN ChanChan (CDB)(CDB) VIVI

      Computes the averaged FFT spectrum of time signal. This VI returns the FFT results as
        real and imaginary parts. Wire data to the time signal input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signals —

           time signals is the input array of time-domain waveforms.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman


1224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1225 ordinal=1225 -->
## Functions

Functions


  6           Flat Top
  7         4 Term B-Harris
  8         7 Term B-Harris
  9        Low Sidelobe
  11        Blackman Nutall
  30         Triangle
  31         Bartlett-Hanning
  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters is a cluster that defines how this VI computes the averaging. The
  specifications of the parameters include the type of averaging, the type of weighting, and the
  number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging
      0
              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.


                                                   © National Instruments 1225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1226 ordinal=1226 -->
## Functions

Functions


               0       Linear
                         Exponential               1                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •      averaging done —

            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •       real parts —

             real parts returns an array of the real part of the averaged FFT spectra, one per input waveform.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •       real part —


1226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1227 ordinal=1227 -->
## Functions

Functions


         real part is the real part of the averaged FFT spectrum.

              If the input signal is in volts (V), real part has units of volts-rms (Vrms). If the input signal is
        not in volts, real part has units of the input signal unit-rms.


   •      imaginary parts —

    imaginary parts returns the imaginary part of the averaged FFT spectra and the frequency scale.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      imaginary part —

        imaginary part is the imaginary part of the averaged FFT spectrum.


   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The FFT Spectrum (Real-IM) VI completes the following steps to compute real part and
imaginary part:

 1. Computes the FFT of time signal.
 2. Averages the current FFT spectrum of time signal with the FFT spectra computed
   by the VI since the last time the averaging process was reset.
 3. Returns the real and imaginary parts of the averaged spectrum.

The single-channel version of this VI can perform single-channel measurements in

                                                    © National Instruments 1227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1228 ordinal=1228 -->
## Functions

Functions

      both one-shot mode, meaning a single call, and continuous mode, meaning multiple
        calls with history. The single-channel version can perform multichannel
      measurements only in one-shot mode. If you want to make multichannel
      measurements in continuous mode, use the multichannel version of this VI.

      The single-channel version of this VI maintains internal state information for a single
      channel only. Calling the single-channel version to process another channel without
       using the restart averaging control to clear the history results in an unexpected
       behavior of this VI. The unexpected behavior results from the VI passing the internal
        state information from one channel to another.

           Note The single-channel version of this VI is intended primarily for
              continuous processing of a single channel. Do not generalize this behavior to
              the multichannel case and use the single-channel version in a For Loop to
              continuously process multiple channels by indexing an array of waveforms.

               Refer to the following LabVIEW project for examples of using a multichannel
               version of a VI like the FFT Spectrum (Real-IM) VI in a loop:

                          • labview\examples\Signal Processing\Waveform
               Measurements\Waveform Measurements.lvproj


      Related Information

      Output Units for FFT-Based VIs
   FrequencyFrequency ResponseResponse FunctionFunction (Mag-Phase)(Mag-Phase)

      Computes the frequency response and the coherence based on the input signals.
       Results are returned as magnitude, phase, and coherence.


            • Frequency Response Function (Mag-Phase) 1-1 VI


1228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1229 ordinal=1229 -->
## Functions

Functions

  • Frequency Response Function (Mag-Phase) 1-N VI
  • Frequency Response Function (Mag-Phase) N-1 VI
  • Frequency Response Function (Mag-Phase) N-M VI

Typically, time signal X is the stimulus, and time signal Y is the response of the system.
Each time waveform corresponds to a single FFT block. You have to pass each time
waveform individually to this VI.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Frequency Analysis of a Filter Design.vi
FrequencyFrequency ResponseResponse FunctionFunction (Mag-Phase)(Mag-Phase)
1-11-1 VIVI

Computes the frequency response and the coherence based on the input signals.
Results are returned as magnitude, phase, and coherence.


Inputs/Outputs

   •     window parameter —

   window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
    a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.


                                                    © National Instruments 1229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1230 ordinal=1230 -->
## Functions

Functions


          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signal X —

           time signal X is the time waveform X.

               •      time signal Y —

           time signal Y is the time waveform Y.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen


1230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1231 ordinal=1231 -->
## Functions

Functions


  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•      view —

  view defines how the different results from this VI are returned.

      •     dB On (F) —

     dB On specifies whether the results are expressed in decibels. The default is FALSE.

      •     unwrap phase (F) —

     unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
       discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
      the phase is not unwrapped.

     When unwrap phase is TRUE, the phase is unwrapped.

      •      convert to degree (F) —

      convert to degree specifies whether the phase results are converted from radians to
      degrees. The default is FALSE, which means that results are expressed in radians.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters defines how the averaging is computed. The specifications of the
  parameters include the type of averaging, the type of weighting, and the number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.


                                                   © National Instruments 1231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1232 ordinal=1232 -->
## Functions

Functions


                 No averaging               0
                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential               1
                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     FRF Mode —

          FRF mode specifies how to compute the frequency response function (FRF).

                    If you know that noise, which does not propagate through the system under test, infiltrates the
            input or output signals, you can select the method used for computing the frequency response
             function (H1, H2, H3) to minimize the measurement error.

          H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates
           0
             the output signal.
            H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input
           1
                signal.
          H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
           2 and upper bounds of the true frequency response of the system. In this case, select H3, the
             average of H1 and H2.

               •      averaging done —


1232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1233 ordinal=1233 -->
## Functions

Functions


  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•      magnitude —

  magnitude returns the magnitude of the averaged frequency response and the frequency scale.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •      magnitude —

      magnitude is the magnitude of the averaged frequency response.


•      phase —

  phase returns the phase of the averaged frequency response and the frequency scale.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •      phase —

      phase is the phase of the averaged frequency response.


•      coherence —

  coherence returns the coherence and the frequency scale.


                                                   © National Instruments 1233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1234 ordinal=1234 -->
## Functions

Functions


                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      coherence —

               coherence returns the coherence.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


        Typically, time signal X is the stimulus, and time signal Y is the response of the system.
      Each time waveform corresponds to a single FFT block. You have to pass each time
      waveform individually to this VI.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Frequency Analysis of a Filter Design.vi
   FrequencyFrequency ResponseResponse FunctionFunction (Mag-Phase)(Mag-Phase)
   1-N1-N VIVI

      Computes the frequency response and the coherence based on the input signals.
       Results are returned as magnitude, phase, and coherence.


1234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1235 ordinal=1235 -->
## Functions

Functions


Inputs/Outputs

   •     window parameter —

   window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
    a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signal X —

    time signal X is the time waveform X.

   •      time signals Y —

    time signals Y is the array of time waveforms Y.

   •     window —

   window (Hanning) is the time-domain window to apply to the time signal. The default window
      is Hanning.


                                                    © National Instruments 1235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1236 ordinal=1236 -->
## Functions

Functions


           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •      view —

           view defines how the different results from this VI are returned.

                     •     dB On (F) —

             dB On specifies whether the results are expressed in decibels. The default is FALSE.

                     •     unwrap phase (F) —

             unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
                  discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
                the phase is not unwrapped.

            When unwrap phase is TRUE, the phase is unwrapped.

                     •      convert to degree (F) —

                convert to degree specifies whether the phase results are converted from radians to
                 degrees. The default is FALSE, which means that results are expressed in radians.


1236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1237 ordinal=1237 -->
## Functions

Functions

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters defines how the averaging is computed. The specifications of the
  parameters include the type of averaging, the type of weighting, and the number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0
              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential      1
                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     FRF Mode —

  FRF mode specifies how to compute the frequency response function (FRF).

   If you know that noise, which does not propagate through the system under test, infiltrates the
  input or output signals, you can select the method used for computing the frequency response
  function (H1, H2, H3) to minimize the measurement error.


                                                   © National Instruments 1237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1238 ordinal=1238 -->
## Functions

Functions


          H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates           0
             the output signal.
            H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input           1                signal.
          H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
           2 and upper bounds of the true frequency response of the system. In this case, select H3, the
             average of H1 and H2.

               •      averaging done —

            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •      magnitudes —

           magnitudes returns an array of the magnitudes of the averaged frequency responses and the
            frequency scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged frequency response.


               •      phases —

           phases returns an array of the phases of the averaged frequency responses and the frequency
              scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —


1238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1239 ordinal=1239 -->
## Functions

Functions


         df returns the frequency resolution, in hertz, of the spectrum.

         •      phase —

       phase is the phase of the averaged frequency response.


   •      coherences —

    coherences returns an array of the coherence functions of the averaged frequency responses
    and the frequency scales.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      coherence —

        coherence returns the coherence.


   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Typically, time signal X is the stimulus, and time signal Y is the response of the system.
Each time waveform corresponds to a single FFT block. You have to pass each time
waveform individually to this VI.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 1239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1240 ordinal=1240 -->
## Functions

Functions

            • labview\examples\Signal Processing\Waveform Measurements\
        Frequency Analysis of a Filter Design.vi
   FrequencyFrequency ResponseResponse FunctionFunction (Mag-Phase)(Mag-Phase)
   N-1N-1 VIVI

      Computes the frequency response and the coherence based on the input signals.
       Results are returned as magnitude, phase, and coherence.


      Inputs/Outputs

               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signals X —

1240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1241 ordinal=1241 -->
## Functions

Functions


  time signals X is the array of time waveforms X.

•      time signal Y —

  time signal Y is the time waveform Y.

•     window —

  window (Hanning) is the time-domain window to apply to the time signal. The default window
   is Hanning.

  0          Rectangle
  1         Hanning (default)
  2        Hamming
  3          Blackman-Harris
  4          Exact Blackman
  5         Blackman
  6           Flat Top
  7         4 Term B-Harris
  8         7 Term B-Harris
  9        Low Sidelobe
  11        Blackman Nutall
  30         Triangle
  31         Bartlett-Hanning
  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•      view —

  view defines how the different results from this VI are returned.

      •     dB On (F) —

     dB On specifies whether the results are expressed in decibels. The default is FALSE.

      •     unwrap phase (F) —


                                                   © National Instruments 1241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1242 ordinal=1242 -->
## Functions

Functions


             unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
                  discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
                the phase is not unwrapped.

            When unwrap phase is TRUE, the phase is unwrapped.

                     •      convert to degree (F) —

                convert to degree specifies whether the phase results are converted from radians to
                 degrees. The default is FALSE, which means that results are expressed in radians.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters defines how the averaging is computed. The specifications of the
           parameters include the type of averaging, the type of weighting, and the number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.

                 No averaging
               0                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential
               1
                            (default)


1242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1243 ordinal=1243 -->
## Functions

Functions


      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     FRF Mode —

  FRF mode specifies how to compute the frequency response function (FRF).

   If you know that noise, which does not propagate through the system under test, infiltrates the
  input or output signals, you can select the method used for computing the frequency response
  function (H1, H2, H3) to minimize the measurement error.

   H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates  0   the output signal.
   H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input  1    signal.
   H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
  2 and upper bounds of the true frequency response of the system. In this case, select H3, the
   average of H1 and H2.

•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•      magnitudes —

  magnitudes returns an array of the magnitudes of the averaged frequency responses and the
  frequency scales.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.


                                                   © National Instruments 1243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1244 ordinal=1244 -->
## Functions

Functions


                     •      magnitude —

              magnitude is the magnitude of the averaged frequency response.


               •      phases —

           phases returns an array of the phases of the averaged frequency responses and the frequency
              scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      phase —

              phase is the phase of the averaged frequency response.


               •      coherences —

           coherences returns an array of the coherence functions of the averaged frequency responses
          and the frequency scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      coherence —

               coherence returns the coherence.


               •      averages completed —


1244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1245 ordinal=1245 -->
## Functions

Functions


    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Typically, time signal X is the stimulus, and time signal Y is the response of the system.
Each time waveform corresponds to a single FFT block. You have to pass each time
waveform individually to this VI.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Frequency Analysis of a Filter Design.vi
FrequencyFrequency ResponseResponse FunctionFunction (Mag-Phase)(Mag-Phase)
N-MN-M VIVI

Computes the frequency response and the coherence based on the input signals.
Results are returned as magnitude, phase, and coherence.


Inputs/Outputs

   •     window parameter —


                                                    © National Instruments 1245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1246 ordinal=1246 -->
## Functions

Functions


          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signals X —

           time signals X is the array of time waveforms X.

               •      time signals Y —

           time signals Y is the array of time waveforms Y.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall


1246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1247 ordinal=1247 -->
## Functions

Functions


  30         Triangle
  31         Bartlett-Hanning
  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•      view —

  view defines how the different results from this VI are returned.

      •     dB On (F) —

     dB On specifies whether the results are expressed in decibels. The default is FALSE.

      •     unwrap phase (F) —

     unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
       discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
      the phase is not unwrapped.

     When unwrap phase is TRUE, the phase is unwrapped.

      •      convert to degree (F) —

      convert to degree specifies whether the phase results are converted from radians to
      degrees. The default is FALSE, which means that results are expressed in radians.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters defines how the averaging is computed. The specifications of the
  parameters include the type of averaging, the type of weighting, and the number of averages.

      •      averaging mode —


                                                   © National Instruments 1247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1248 ordinal=1248 -->
## Functions

Functions


                averaging mode specifies the averaging mode.

                 No averaging
               0                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential               1                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     FRF Mode —

          FRF mode specifies how to compute the frequency response function (FRF).

                    If you know that noise, which does not propagate through the system under test, infiltrates the
            input or output signals, you can select the method used for computing the frequency response
             function (H1, H2, H3) to minimize the measurement error.

          H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates
           0
             the output signal.
            H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input
           1
                signal.
          H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
           2 and upper bounds of the true frequency response of the system. In this case, select H3, the
             average of H1 and H2.

               •      X-Y pairing —

1248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1249 ordinal=1249 -->
## Functions

Functions


  X-Y pairing specifies how to handle multiple signals in each input.

   ordered pairs (default)—Calculates the frequency response of the first channel in time signals
   X against the first channel in time signals Y, then the second channel in time signals X against
   the second channel in time signals Y, and so on.
        •  If there is one channel in time signals X and one channel in time signals Y, the result is one
        output.
        •  If there are multiple channels in time signals X and one channel in time signals Y, the
        analysis result is the first channel in time signals X against the single channel in time
        signals Y. LabVIEW ignores the rest of the channels in time signals X, and the VI returns a
        warning.
  0   •  If there is one channel in time signals X and multiple channels in time signals Y, the
        analysis result is the single channel in time signals X against the first channel in time
        signals Y. LabVIEW ignores the rest of the channels in time signals Y, and the VI returns a
        warning.
        •  If there are multiple channels in both time signals X and time signals Y, the analysis result
          is the first channel in time signals X against the first channel in time signals Y, the second
       channel in time signals X against the second channel in time signals Y, and so on. If there
          is a mismatched number of channels, the VI ignores unmatched channels and returns a
        warning.
        •  If either input signal is empty, the result is empty, and the VI returns an error.
    all cross pairs—Calculates the frequency response of the first channel in time signals X against
   each channel in time signals Y, then the second channel in time signals X against each channel
    in time signals Y, and so on.
        •  If there is one channel in time signals X and one channel in time signals Y, the result is one
        output.
        •  If there are multiple channels in time signals X and one channel in time signals Y, the
        analysis result is the first channel in time signals X against the single channel in time
        signals Y, then the second channel in time signals X against the single channel in time
  1     signals Y, and so on. The output contains the same number of signals as time signals X.
        •  If there is one channel in time signals X and multiple channels in time signals Y, the
        analysis result is the single channel in time signals X against the first channel in time
        signals Y, then the single channel in time signals X against the second channel in time
        signals Y, and so on. The output contains the same number of signals as time signals Y.
        •  If there are Nchannels in time signals X and Mchannels in time signals Y, the analysis
         result is the matrix set of time signals X versus time signals Y. LabVIEW returns the signals
         in the order 1 – 1, ..., 1 – M, 2 – 1, ..., 2 – M, ..., N– M.
        •  If either input signal is empty, the result is empty, and the VI returns an error.

•      averaging done —


                                                   © National Instruments 1249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1250 ordinal=1250 -->
## Functions

Functions


            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •      magnitudes —

           magnitudes returns an array of the magnitudes of the averaged frequency responses and the
            frequency scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged frequency response.


               •      phases —

           phases returns an array of the phases of the averaged frequency responses and the frequency
              scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      phase —

              phase is the phase of the averaged frequency response.


               •      coherences —

           coherences returns an array of the coherence functions of the averaged frequency responses


1250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1251 ordinal=1251 -->
## Functions

Functions


    and the frequency scales.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      coherence —

        coherence returns the coherence.


   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Typically, time signal X is the stimulus, and time signal Y is the response of the system.
Each time waveform corresponds to a single FFT block. You have to pass each time
waveform individually to this VI.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Frequency Analysis of a Filter Design.vi
FrequencyFrequency ResponseResponse FunctionFunction (Real-Im)(Real-Im)

Computes the frequency response and the coherence based on the input signals.
Results are returned as real part, imaginary part, and coherence.


                                                    © National Instruments 1251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1252 ordinal=1252 -->
## Functions

Functions


            • Frequency Response Function (Real-Im) 1-1 VI
            • Frequency Response Function (Real-Im) 1-N VI
            • Frequency Response Function (Real-Im) N-1 VI
            • Frequency Response Function (Real-Im) N-M VI

        Typically, time signal X is the stimulus, and time signal Y is the response of the system.
      Each time waveform corresponds to a single FFT block. You have to pass each time
      waveform individually to this VI.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Nyquist Plot of a Filter.vi
   FrequencyFrequency ResponseResponse FunctionFunction (Real-Im)(Real-Im) 1-11-1
    VIVI

      Computes the frequency response and the coherence based on the input signals.
       Results are returned as real part, imaginary part, and coherence.


      Inputs/Outputs

               •     window parameter —


1252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1253 ordinal=1253 -->
## Functions

Functions


  window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
  a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
  window. If window is any other window, this VI ignores this input.

  The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•       restart averaging (F) —

  restart averaging specifies whether the VI restarts the selected averaging process. If restart
  averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
  the VI does not restart the selected averaging process. The default is FALSE.

  When you call this VI for the first time, the averaging process restarts automatically. A typical
  case when you should restart averaging is when a major input change occurs in the middle of
  the averaging process.

•      time signal X —

  time signal X is the time waveform X.

•      time signal Y —

  time signal Y is the time waveform Y.

•     window —

  window (Hanning) is the time-domain window to apply to the time signal. The default window
   is Hanning.

  0          Rectangle
  1         Hanning (default)
  2        Hamming
  3          Blackman-Harris
  4          Exact Blackman
  5         Blackman
  6           Flat Top
  7         4 Term B-Harris
  8         7 Term B-Harris
  9        Low Sidelobe
  11        Blackman Nutall


                                                   © National Instruments 1253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1254 ordinal=1254 -->
## Functions

Functions


           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how the averaging is computed. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.

                 No averaging               0                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential
               1
                            (default)

                     •     number of averages —


1254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1255 ordinal=1255 -->
## Functions

Functions


     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     FRF Mode —

  FRF mode specifies how to compute the frequency response function (FRF).

   If you know that noise, which does not propagate through the system under test, infiltrates the
  input or output signals, you can select the method used for computing the frequency response
  function (H1, H2, H3) to minimize the measurement error.

   H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates  0
   the output signal.
   H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input
  1    signal.
   H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
  2 and upper bounds of the true frequency response of the system. In this case, select H3, the
   average of H1 and H2.

•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•       real part —

  real part returns the real part of the averaged frequency response and the frequency scale.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •       real part —


                                                   © National Instruments 1255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1256 ordinal=1256 -->
## Functions

Functions


                  real part is the real part of the averaged frequency response.


               •      imaginary part —

           imaginary part returns the imaginary part of the averaged frequency response and the
            frequency scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      imaginary part —

               imaginary part is the imaginary part of the averaged frequency response.


               •      coherence —

           coherence returns the coherence and the frequency scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      coherence —

               coherence returns the coherence.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

1256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1257 ordinal=1257 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Typically, time signal X is the stimulus, and time signal Y is the response of the system.
Each time waveform corresponds to a single FFT block. You have to pass each time
waveform individually to this VI.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Nyquist Plot of a Filter.vi
FrequencyFrequency ResponseResponse FunctionFunction (Real-Im)(Real-Im) 1-N1-N
VIVI

Computes the frequency response and the coherence based on the input signals.
Results are returned as real part, imaginary part, and coherence.


Inputs/Outputs

   •     window parameter —

   window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
    a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.


                                                    © National Instruments 1257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1258 ordinal=1258 -->
## Functions

Functions


          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart
            averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
            the VI does not restart the selected averaging process. The default is FALSE.

         When you call this VI for the first time, the averaging process restarts automatically. A typical
            case when you should restart averaging is when a major input change occurs in the middle of
            the averaging process.

               •      time signal X —

           time signal X is the time waveform X.

               •      time signals Y —

           time signals Y is the array of time waveforms Y.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen


1258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1259 ordinal=1259 -->
## Functions

Functions


  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters is a cluster that defines how the averaging is computed. The
  specifications of the parameters include the type of averaging, the type of weighting, and the
  number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential
      1
                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


                                                   © National Instruments 1259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1260 ordinal=1260 -->
## Functions

Functions

               •     FRF Mode —

          FRF mode specifies how to compute the frequency response function (FRF).

                    If you know that noise, which does not propagate through the system under test, infiltrates the
            input or output signals, you can select the method used for computing the frequency response
             function (H1, H2, H3) to minimize the measurement error.

          H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates
           0             the output signal.
            H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input           1                signal.
          H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
           2 and upper bounds of the true frequency response of the system. In this case, select H3, the
             average of H1 and H2.

               •      averaging done —

            averaging done returns TRUE when averages completed is greater than or equal to the number
             of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
            averaging done is always TRUE if the selected averaging mode is No averaging.

               •       real parts —

             real parts returns an array of the real parts of the averaged frequency responses and the
            frequency scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •       real part —

                  real part is the real part of the averaged frequency response.


               •      imaginary parts —

           imaginary parts returns an array of the imaginary parts of the averaged frequency responses


1260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1261 ordinal=1261 -->
## Functions

Functions


    and the frequency scales.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •     imag part —

        imaginary part is the imaginary part of the averaged frequency response.


   •      coherences —

    coherences returns an array of the coherence functions of the averaged frequency responses
    and the frequency scales.

         •       f0 —

         f0 returns the start frequency, in hertz, of the spectrum.

         •       df —

         df returns the frequency resolution, in hertz, of the spectrum.

         •      coherence —

        coherence returns the coherence.


   •      averages completed —

    averages completed returns the number of averages completed by the VI at that time.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Typically, time signal X is the stimulus, and time signal Y is the response of the system.


                                                    © National Instruments 1261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1262 ordinal=1262 -->
## Functions

Functions

      Each time waveform corresponds to a single FFT block. You have to pass each time
      waveform individually to this VI.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Nyquist Plot of a Filter.vi
   FrequencyFrequency ResponseResponse FunctionFunction (Real-Im)(Real-Im) N-1N-1
    VIVI

      Computes the frequency response and the coherence based on the input signals.
       Results are returned as real part, imaginary part, and coherence.


      Inputs/Outputs

               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •       restart averaging (F) —

             restart averaging specifies whether the VI restarts the selected averaging process. If restart


1262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1263 ordinal=1263 -->
## Functions

Functions


  averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
  the VI does not restart the selected averaging process. The default is FALSE.

  When you call this VI for the first time, the averaging process restarts automatically. A typical
  case when you should restart averaging is when a major input change occurs in the middle of
  the averaging process.

•      time signals X —

  time signals X is the array of time waveforms X.

•      time signal Y —

  time signal Y is the time waveform Y.

•     window —

  window (Hanning) is the time-domain window to apply to the time signal. The default window
   is Hanning.

  0          Rectangle
  1         Hanning (default)
  2        Hamming
  3          Blackman-Harris
  4          Exact Blackman
  5         Blackman
  6           Flat Top
  7         4 Term B-Harris
  8         7 Term B-Harris
  9        Low Sidelobe
  11        Blackman Nutall
  30         Triangle
  31         Bartlett-Hanning
  32       Bohman
  33        Parzen
  34        Welch
  60         Kaiser
  61        Dolph-Chebyshev
  62        Gaussian

•       error in (no error) —


                                                   © National Instruments 1263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1264 ordinal=1264 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how the averaging is computed. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.

                 No averaging               0
                          (default)
               1     Vector averaging
               2    RMS averaging
               3    Peak hold

                     •      weighting mode —

               weighting mode specifies the weighting mode for RMS and vector averaging.

               0       Linear
                         Exponential               1
                            (default)

                     •     number of averages —

             number of averages specifies the number of averages used for RMS and vector averaging. If
               weighting mode is exponential, the averaging process is continuous. If weighting mode is
                    linear, the averaging process stops after this VI computes the selected number of averages.


               •     FRF Mode —

          FRF mode specifies how to compute the frequency response function (FRF).

                    If you know that noise, which does not propagate through the system under test, infiltrates the
            input or output signals, you can select the method used for computing the frequency response
             function (H1, H2, H3) to minimize the measurement error.


1264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1265 ordinal=1265 -->
## Functions

Functions


   H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates  0
   the output signal.
   H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input  1    signal.
   H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
  2 and upper bounds of the true frequency response of the system. In this case, select H3, the
   average of H1 and H2.

•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•       real parts —

  real parts returns an array of the real parts of the averaged frequency responses and the
  frequency scales.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •       real part —

       real part is the real part of the averaged frequency response.


•      imaginary parts —

  imaginary parts returns an array of the imaginary parts of the averaged frequency responses
  and the frequency scales.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —


                                                   © National Instruments 1265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1266 ordinal=1266 -->
## Functions

Functions


                 df returns the frequency resolution, in hertz, of the spectrum.

                     •     imag part —

               imaginary part is the imaginary part of the averaged frequency response.


               •      coherences —

           coherences returns an array of the coherence functions of the averaged frequency responses
          and the frequency scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      coherence —

               coherence returns the coherence.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


        Typically, time signal X is the stimulus, and time signal Y is the response of the system.
      Each time waveform corresponds to a single FFT block. You have to pass each time
      waveform individually to this VI.

     Examples

       Refer to the following example files included with LabVIEW.


1266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1267 ordinal=1267 -->
## Functions

Functions

  • labview\examples\Signal Processing\Waveform Measurements\
   Nyquist Plot of a Filter.vi
FrequencyFrequency ResponseResponse FunctionFunction (Real-Im)(Real-Im) N-MN-M
VIVI

Computes the frequency response and the coherence based on the input signals.
Results are returned as real part, imaginary part, and coherence.


Inputs/Outputs

   •     window parameter —

   window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
    a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signals X —

                                                    © National Instruments 1267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1268 ordinal=1268 -->
## Functions

Functions


           time signals X is the array of time waveforms X.

               •      time signals Y —

           time signals Y is the array of time waveforms Y.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters is a cluster that defines how the averaging is computed. The
             specifications of the parameters include the type of averaging, the type of weighting, and the
          number of averages.


1268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1269 ordinal=1269 -->
## Functions

Functions


      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential
      1                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•     FRF Mode —

  FRF mode specifies how to compute the frequency response function (FRF).

   If you know that noise, which does not propagate through the system under test, infiltrates the
  input or output signals, you can select the method used for computing the frequency response
  function (H1, H2, H3) to minimize the measurement error.

   H1 (default)—Select H1 to minimize errors in the result when extraneous noise contaminates
  0
   the output signal.
   H2—Select H2 to minimize errors in the result when extraneous noise contaminates the input
  1
    signal.
   H3—When noise contaminates both the input and output signals, H1 and H2 provide the lower
  2 and upper bounds of the true frequency response of the system. In this case, select H3, the
   average of H1 and H2.


                                                   © National Instruments 1269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1270 ordinal=1270 -->
## Functions

Functions

               •      X-Y pairing —

            X-Y pairing specifies how to handle multiple signals in each input.

            ordered pairs (default)—Calculates the frequency response of the first channel in time signals
           X against the first channel in time signals Y, then the second channel in time signals X against
             the second channel in time signals Y, and so on.
                       •  If there is one channel in time signals X and one channel in time signals Y, the result is one
                  output.
                       •  If there are multiple channels in time signals X and one channel in time signals Y, the
                   analysis result is the first channel in time signals X against the single channel in time
                   signals Y. LabVIEW ignores the rest of the channels in time signals X, and the VI returns a
                 warning.
           0   •  If there is one channel in time signals X and multiple channels in time signals Y, the
                   analysis result is the single channel in time signals X against the first channel in time
                   signals Y. LabVIEW ignores the rest of the channels in time signals Y, and the VI returns a
                 warning.
                       •  If there are multiple channels in both time signals X and time signals Y, the analysis result
                        is the first channel in time signals X against the first channel in time signals Y, the second
                 channel in time signals X against the second channel in time signals Y, and so on. If there
                        is a mismatched number of channels, the VI ignores unmatched channels and returns a
                 warning.
                       •  If either input signal is empty, the result is empty, and the VI returns an error.
                 all cross pairs—Calculates the frequency response of the first channel in time signals X against
            each channel in time signals Y, then the second channel in time signals X against each channel
               in time signals Y, and so on.
                       •  If there is one channel in time signals X and one channel in time signals Y, the result is one
                  output.
                       •  If there are multiple channels in time signals X and one channel in time signals Y, the
                   analysis result is the first channel in time signals X against the single channel in time
                   signals Y, then the second channel in time signals X against the single channel in time
           1     signals Y, and so on. The output contains the same number of signals as time signals X.
                       •  If there is one channel in time signals X and multiple channels in time signals Y, the
                   analysis result is the single channel in time signals X against the first channel in time
                   signals Y, then the single channel in time signals X against the second channel in time
                   signals Y, and so on. The output contains the same number of signals as time signals Y.
                       •  If there are Nchannels in time signals X and Mchannels in time signals Y, the analysis
                    result is the matrix set of time signals X versus time signals Y. LabVIEW returns the signals
                    in the order 1 – 1, ..., 1 – M, 2 – 1, ..., 2 – M, ..., N– M.
                       •  If either input signal is empty, the result is empty, and the VI returns an error.

               •      averaging done —


1270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1271 ordinal=1271 -->
## Functions

Functions


  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•       real parts —

  real parts returns an array of the real parts of the averaged frequency responses and the
  frequency scales.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •       real part —

       real part is the real part of the averaged frequency response.


•      imaginary parts —

  imaginary parts returns an array of the imaginary parts of the averaged frequency responses
  and the frequency scales.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •     imag part —

      imaginary part is the imaginary part of the averaged frequency response.


•      coherences —

  coherences returns an array of the coherence functions of the averaged frequency responses


                                                   © National Instruments 1271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1272 ordinal=1272 -->
## Functions

Functions


          and the frequency scales.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      coherence —

               coherence returns the coherence.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


        Typically, time signal X is the stimulus, and time signal Y is the response of the system.
      Each time waveform corresponds to a single FFT block. You have to pass each time
      waveform individually to this VI.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Nyquist Plot of a Filter.vi
   CrossCross SpectrumSpectrum (Mag-Phase)(Mag-Phase)

      Computes the averaged cross power spectrum of the input signals. Results are
       returned as magnitude and phase.


1272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1273 ordinal=1273 -->
## Functions

Functions


Inputs/Outputs

   •     window parameter —

   window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
    a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signal X —

    time signal X is the time waveform X.

   •      time signal Y —

    time signal Y is the time waveform Y.

   •     window —

   window (Hanning) is the time-domain window to apply to the time signal. The default window
      is Hanning.


                                                    © National Instruments 1273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1274 ordinal=1274 -->
## Functions

Functions


           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •      view —

           view defines how the different results from this VI are returned.

                     •     dB On (F) —

             dB On specifies whether the results are expressed in decibels. The default is FALSE.

                     •     unwrap phase (F) —

             unwrap phase specifies whether to unwrap the phase. Unwrapping eliminates
                  discontinuities that have an absolute value greater than pi. The default is FALSE, meaning
                the phase is not unwrapped.

            When unwrap phase is TRUE, the phase is unwrapped.

                     •      convert to degree (F) —

                convert to degree specifies whether the phase results are converted from radians to
                 degrees. The default is FALSE, which means that results are expressed in radians.


1274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1275 ordinal=1275 -->
## Functions

Functions

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      averaging parameters —

  averaging parameters defines how the averaging is computed. The specifications of the
  parameters include the type of averaging, the type of weighting, and the number of averages.

      •      averaging mode —

      averaging mode specifies the averaging mode.

          No averaging      0
              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential      1
                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•      magnitude —


                                                   © National Instruments 1275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1276 ordinal=1276 -->
## Functions

Functions


           magnitude returns the magnitude of the averaged cross power spectrum and the frequency
              scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      magnitude —

              magnitude is the magnitude of the averaged cross power spectrum.


               •      phase —

           phase returns the phase of the averaged cross power spectrum and the frequency scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      phase —

              phase returns the phase of the averaged cross power spectrum.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


        Typically, time signal X is the stimulus, and time signal Y is the response of the system.


1276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1277 ordinal=1277 -->
## Functions

Functions

Each time waveform corresponds to a single FFT block. You have to pass each time
waveform individually to this VI.
CrossCross SpectrumSpectrum (Real-Im)(Real-Im)

Computes the averaged cross power spectrum of the input signals. Results are
returned as real and imaginary parts.


Inputs/Outputs

   •     window parameter —

   window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
    a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •       restart averaging (F) —

     restart averaging specifies whether the VI restarts the selected averaging process. If restart
    averaging is TRUE, the VI restarts the selected averaging process. If restart averaging is FALSE,
    the VI does not restart the selected averaging process. The default is FALSE.

   When you call this VI for the first time, the averaging process restarts automatically. A typical
    case when you should restart averaging is when a major input change occurs in the middle of
    the averaging process.

   •      time signal X —

    time signal X is the time waveform X.

   •      time signal Y —

                                                    © National Instruments 1277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1278 ordinal=1278 -->
## Functions

Functions


           time signal Y is the time waveform Y.

               •     window —

          window (Hanning) is the time-domain window to apply to the time signal. The default window
                is Hanning.

           0          Rectangle
           1         Hanning (default)
           2        Hamming
           3          Blackman-Harris
           4          Exact Blackman
           5         Blackman
           6           Flat Top
           7         4 Term B-Harris
           8         7 Term B-Harris
           9        Low Sidelobe
           11        Blackman Nutall
           30         Triangle
           31         Bartlett-Hanning
           32       Bohman
           33        Parzen
           34        Welch
           60         Kaiser
           61        Dolph-Chebyshev
           62        Gaussian

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      averaging parameters —

            averaging parameters defines how the averaging is computed. The specifications of the
           parameters include the type of averaging, the type of weighting, and the number of averages.

                     •      averaging mode —

                averaging mode specifies the averaging mode.


1278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1279 ordinal=1279 -->
## Functions

Functions


          No averaging      0
              (default)
      1     Vector averaging
      2    RMS averaging
      3    Peak hold

      •      weighting mode —

      weighting mode specifies the weighting mode for RMS and vector averaging.

      0       Linear
               Exponential      1
                 (default)

      •     number of averages —

     number of averages specifies the number of averages used for RMS and vector averaging. If
      weighting mode is exponential, the averaging process is continuous. If weighting mode is
        linear, the averaging process stops after this VI computes the selected number of averages.


•      averaging done —

  averaging done returns TRUE when averages completed is greater than or equal to the number
  of averages specified in averaging parameters. Otherwise, averaging done returns FALSE.
  averaging done is always TRUE if the selected averaging mode is No averaging.

•       real part —

  real part returns the real part of the averaged cross power spectrum and the frequency scale.

      •       f0 —

       f0 returns the start frequency, in hertz, of the spectrum.

      •       df —

       df returns the frequency resolution, in hertz, of the spectrum.

      •       real part —


                                                   © National Instruments 1279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1280 ordinal=1280 -->
## Functions

Functions


                  real part is the real part of the averaged cross power spectrum.


               •      imaginary part —

           imaginary part returns the imaginary part of the averaged cross power spectrum and the
            frequency scale.

                     •       f0 —

                  f0 returns the start frequency, in hertz, of the spectrum.

                     •       df —

                 df returns the frequency resolution, in hertz, of the spectrum.

                     •      imaginary part —

               imaginary part is the imaginary part of the averaged cross power spectrum.


               •      averages completed —

           averages completed returns the number of averages completed by the VI at that time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


        Typically, time signal X is the stimulus, and time signal Y is the response of the system.
      Each time waveform corresponds to a single FFT block. You have to pass each time
      waveform individually to this VI.
    SpectralSpectral MeasurementsMeasurements

      Performs FFT-based spectral measurements, such as the averaged magnitude
       spectrum, power spectrum, and phase spectrum on a signal.


1280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1281 ordinal=1281 -->
## Functions

Functions


Dialog Box Options

 Option        Description

               Contains the following options:

                          • Magnitude (peak)—

                  Measures the spectrum and displays the results in terms of peak amplitude.

                 You typically use this measurement with more advanced measurements that
                    require magnitude and phase information. The magnitude of the spectrum is
                 measured in peak values. For example, a sine tone of amplitude A yields a
                 magnitude spectral value of A at the sine tone frequency. You can unwrap the
                 phase spectrum or convert it from radians to degrees by setting Phase to
                Unwrap phase or Convert to degree, respectively. If you place a checkmark in
                   the Averaging checkbox, the phase of the spectrum is zero for averaging.

                          • Magnitude (RMS)—
 Selected                  Measures the spectrum and displays the results in terms of root-mean-square
 Measurement                    (RMS).

                 You typically use this measurement with more advanced measurements that
                    require magnitude and phase information. The magnitude of the spectrum is
                 measured in RMS values. For example, a sine tone of amplitude A yields a
                 magnitude spectral value of 0.707*A at the sine tone frequency. You can
                 unwrap the phase spectrum or convert it from radians to degrees by setting
                 Phase to Unwrap phase or Convert to degree, respectively. If you place a
                 checkmark in the Averaging checkbox, the phase of the spectrum is zero for
                    averaging.

                          • Power spectrum—

                  Measures the spectrum and displays the results in terms of power. All phase
                    information is lost in the computation.


                                                    © National Instruments 1281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1282 ordinal=1282 -->
## Functions

Functions


        Option        Description

                        You typically use this measurement to examine the various frequency
                        components of a signal. While averaging to compute a power spectrum does
                          not reduce the unwanted noise in a system, averaging is useful because it
                           provides a reliable statistical estimate of the level of random signals measured.

                                     • Power spectral density—

                         Measures the spectrum and displays the results in terms of power spectral
                            density (PSD).

                       Power spectral density is a scaled version of Power spectrum, where the
                       power present within each spectral bin is normalized by the frequency bin
                            width. You typically use this measurement to examine the noise floor of a
                              signal or the power in a specific frequency range. Normalizing the power
                         spectrum by the bin width makes this measurement independent of the signal
                             duration, or number of samples.

                       Contains the following options:

                                     • Linear—

                           Returns the results in terms of the original units.         Result
                                     • dB—

                           Returns the results in terms of decibels (dB).


                         Specifies the window to apply to the signal.

                                     • None does not apply a window to Signals.
                                     • Hanning applies a Hanning window to Signals.
                                     • Hamming applies a Hamming window to Signals.
                                     • Blackman-Harris applies a Blackman-Harris window to Signals.
       Window                                     • Exact Blackman applies an exact Blackman window to Signals.
                                     • Blackman applies a Blackman window to Signals.
                                     •  Flat Top applies a Flat Top window to Signals.
                                     • 4 Term B-Harris applies a Four Term Blackman-Harris window to Signals.
                                     • 7 Term B-Harris applies a Seven Term Blackman-Harris window to Signals.
                                     • Low Sidelobe applies a Low Sidelobe window to Signals.


1282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1283 ordinal=1283 -->
## Functions

Functions


Option        Description

               Refer to the Scaled Time Domain Window VI for information about coefficients and
            window parameters for each window type.

Averaging      Specifies whether the Express VI performs averaging.

              Contains the following options:

                         • Peak hold—

                  Performs averaging at each frequency line separately, retaining peak levels
                 from one FFT record to the next.

                         • Vector—Mode
                Computes the average of complex FFT spectrum quantities directly. Vector
                   averaging eliminates noise from synchronous signals.

                         • RMS—

                  Averages the energy, or power, of the FFT spectrum of the signal.

              Contains the following options:

                         • Linear—

                  Returns the results in terms of the original units.

Weighting          • Exponential—

                    Specifies exponential averaging, which averages over the number of packets
                you specify in Number of Averages in a weighted manner. Exponential
                   averaging gives the most recent packets more weighting in the average than
                   older packets.


Number of
                Specifies the number of packets to average. The default is 10.
Averages

              Contains the following options:
Produce
Spectrum           • Every iteration—


                                                    © National Instruments 1283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1284 ordinal=1284 -->
## Functions

Functions


        Option        Description

                           Returns the spectrum after every iteration of the Express VI.

                                     • Only when averaging complete—

                           Returns the spectrum only after the Express VI gathers the number of packets
                        you specify in Number of Averages.

                       Contains the following options:

                                     • Unwrap phase—

                          Enables phase unwrapping on the output phase.        Phase
                                     • Convert to degree—

                           Returns the phase in degrees.


                        Displays the first channel of Signals. This graph displays the incoming signal with
                    windowing applied.
       Windowed
        Input Signal     If you wire data to the Express VI and run it, Windowed Input Signal displays real
                         data. If you close and reopen the Express VI, Windowed Input Signal displays
                     sample data until you run the VI again.


                        Displays a preview of the magnitude measurement of the signal.
        Magnitude
         Result              If you wire data to the Express VI and run it, Magnitude Result Preview displays real
        Preview       data. If you close and reopen the Express VI, Magnitude Result Preview displays
                     sample data until you run the VI again.


                       Contains the following options:
        Phase Result                                      If you wire data to the Express VI and run it, Phase Result Preview displays real
        Preview                         data. If you close and reopen the Express VI, Phase Result Preview displays sample
                      data until you run the VI again.


1284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1285 ordinal=1285 -->
## Functions

Functions

Inputs/Outputs

   •      Restart Averaging — Specifies whether to restart the selected averaging process. The
     default is FALSE. When you call this Express VI for the first time, the averaging process starts
    automatically.

    This input appears only if you place a checkmark in the Averaging checkbox.

   •       error in (no error) —
    Describes error conditions that occur before this node runs.
   •      Signals —
    Contains the input signal or signals.
   •       error out —
    Contains error information. This output provides standard error out functionality.
   •     FFT - (RMS) — Returns the FFT magnitude spectrum and displays the results in RMS units.
   •     Power Spectrum — Returns the FFT power spectrum and displays the results in RMS-
    squared units.

    To compute the FFT power spectrum, LabVIEW converts the two-sided power spectrum to the
     single-sided power spectrum.

   •     PSD — Returns the FFT power spectral density and displays the results in RMS-squared per
    Hz units.
   •     FFT - (Peak) — Returns the FFT magnitude spectrum and displays the results in peak units.
   •      averaging done — Returns TRUE when the number of averages completed equals or
    exceeds Number of Averages.
   •      Phase —
    Returns the FFT phase spectrum and displays the results in degrees or radians.

         •       f0 —

         •       df —

         •      phase —


FFT-based spectral computations assume that the finite block of signal data represents
one period of a periodic signal. The computed spectrum of this effective periodically
extended signal shows energy spreading into frequencies that were not present in the
original signal. To reduce this spectral leakage, use smoothing windows to taper the
sharp transitions in the effective signal. You do not typically use windows if you can
acquire an integer number of cycles of each frequency component measured or if you

                                                    © National Instruments 1285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1286 ordinal=1286 -->
## Functions

Functions

       are analyzing noise spectra.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Spectral
        Measurements.vi
            • labview\examples\Express VIs\Express VI - Filter.vi

     Components

       Returns TRUE when the number of averages completed equals or exceeds Number of
       Averages.

       Describes error conditions that occur before this node runs.

       Specifies whether to restart the selected averaging process. The default is FALSE. When
      you call this Express VI for the first time, the averaging process starts automatically.

      Measures the spectrum and displays the results in terms of power spectral density
       (PSD).

      Measures the spectrum and displays the results in terms of power. All phase
       information is lost in the computation.

      Measures the spectrum and displays the results in terms of root-mean-square (RMS).

      Measures the spectrum and displays the results in terms of peak amplitude.

       Specifies whether the Express VI performs averaging.

       Contains the following options:

      Enables phase unwrapping on the output phase.

       Returns the phase in degrees.

       Specifies the number of packets to average. The default is 10.

1286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1287 ordinal=1287 -->
## Functions

Functions

Specifies the number of packets to average. The default is 10.

Specifies the window to apply to the signal.

Displays the first channel of Signals. This graph displays the incoming signal with
windowing applied.

Contains the input signal or signals.

Contains error information. This output provides standard error out functionality.

Displays a preview of the magnitude measurement of the signal.

Contains the following options:

Returns the results in terms of the original units.

Returns the results in terms of decibels (dB).

Contains the following options:

Specifies linear averaging, which averages over the number of packets you specify in
Number of Averages in a non-weighted manner.

Specifies exponential averaging, which averages over the number of packets you
specify in Number of Averages in a weighted manner. Exponential averaging gives the
most recent packets more weighting in the average than older packets.

Contains the following options:

Returns the spectrum after every iteration of the Express VI.

Returns the spectrum only after the Express VI gathers the number of packets you
specify in Number of Averages.

Contains the following options:

Computes the average of complex FFT spectrum quantities directly. Vector averaging
eliminates noise from synchronous signals.

                                                    © National Instruments 1287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1288 ordinal=1288 -->
## Functions

Functions

       Averages the energy, or power, of the FFT spectrum of the signal.

      Performs averaging at each frequency line separately, retaining peak levels from one
      FFT record to the next.
   DualDual ChannelChannel SpectralSpectral MeasurementMeasurement

      Measures the frequency response of the input signals and the coherence based on the
       current and previous input signals. This Express VI returns results such as Magnitude,
      Phase, Coherence, Real, and Imaginary.


      Dialog Box Options

        Option       Description

                        Specifies how to handle multiple signals in each input.

                                   • Ordered pairs—

                           Calculates the frequency response of the first channel in Input Signal A against
                         the first channel in Input Signal B, then the second channel in Input Signal A
                           against the second channel in Input Signal B, and so on.

            ◦  If there is one channel on Input Signal A and one channel on Input Signal B,
                              the result is one output.
        Input            ◦  If there are multiple channels on Input Signal A and one channel on Input
        Comparison                              Signal B, the analysis result is the first channel in Input Signal A against the
                                 single channel in Input Signal B. The rest of the channels in Input Signal A
                              are ignored and the VI returns a warning.
            ◦  If there is one channel on Input Signal A and multiple channels on Input
                              Signal B, the analysis result is the single channel in Input Signal A against
                              the first channel in Input Signal B. The rest of the channels in Input Signal B
                              are ignored and the VI returns a warning.
            ◦  If there are multiple channels on both Input Signal A and Input Signal B, the
                                analysis result is the first channel in Input Signal A against the first channel


1288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1289 ordinal=1289 -->
## Functions

Functions


Option       Description

                        in Input Signal B, the second channel in Input Signal A against the second
                    channel in Input Signal B, and so on. If there is a mismatched number of
                      channels, the VI ignores unmatched channels and returns a warning.
        ◦  If either Input Signal is empty, the result is empty and the VI returns an error.
                      •  All cross pairs—

                  Calculates the frequency response of the first channel in Input Signal A against
                each channel in Input Signal B, then the second channel in Input Signal A
                  against each channel in Input Signal B, and so on.

        ◦  If there is one channel on Input Signal A and one channel on Input Signal B,
                     the result is one output.
        ◦  If there are multiple channels on Input Signal A and one channel on Input
                      Signal B, the analysis result is the first channel in Input Signal A against the
                       single channel in Input Signal B, then the second channel in Input Signal A
                      against the single channel in Input Signal B, and so on. The output contains
                     the same number of signals as Input Signal A.
        ◦  If there is one channel on Input Signal A and multiple channels on Input
                      Signal B, the analysis result is the single channel in Input Signal A against
                     the first channel in Input Signal B, then the single channel in Input Signal A
                      against the second channel in Input Signal B, and so on. The output
                      contains the same number of signals as Input Signal B.
        ◦  If there are Mchannels on Input Signal A and Nchannels on Input Signal B,
                     the analysis result is the matrix set of Input Signal A versus Input Signal B.
                  The signals are returned in the order 1-1, ... 1-N, 2-1, ... M-N.
        ◦  If either Input Signal is empty, the result is empty and the VI returns an error.

             Contains the following options:

                      • Magnitude—

                  Select to include magnitude results in the output.
Frequency
Response    ◦ dB—
Function
                       Select to return the magnitude results in decibels. Remove the checkmark
                   from this checkbox to return the magnitude results in the original units.

                      • Phase—


                                                    © National Instruments 1289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1290 ordinal=1290 -->
## Functions

Functions


        Option       Description

                           Select to include phase results in the output. Select Unwrap phase to return the
                       phase results in radians. Select Convert to degree to return the phase results in
                          degrees.

            ◦ Unwrap phase—

                                Select to return the phase results in radians.

            ◦ Convert to degree—

                                Select to return the phase results in degrees.

                                   • Real—

                           Select to include real results in the output.

                                   • Imaginary—

                           Select to include imaginary results in the output.

                                   • Coherence—

                           Select to include coherence results in the output.


                        Specifies the window to apply to the signal.

                                   • None does not apply a window to Signals.
                                   • Hanning applies a Hanning window to Signals.
                                   • Hamming applies a Hamming window to Signals.
                                   • Blackman-Harris applies a Blackman-Harris window to Signals.
                                   • Exact Blackman applies an exact Blackman window to Signals.
       Window                                   • Blackman applies a Blackman window to Signals.
                                   •  Flat Top applies a Flat Top window to Signals.
                                   • 4 Term B-Harris applies a Four Term Blackman-Harris window to Signals.
                                   • 7 Term B-Harris applies a Seven Term Blackman-Harris window to Signals.
                                   • Low Sidelobe applies a Low Sidelobe window to Signals.

                       Refer to the Scaled Time Domain Window VI for information about coefficients and
                  window parameters for each window type.


1290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1291 ordinal=1291 -->
## Functions

Functions


Option       Description

Averaging    Specifies whether the Express VI performs averaging.

             Contains the following options:

                      • Vector—

               Computes the average of complex quantities directly.Mode
                      • RMS—

                 Averages the energy, or power, of the signal.

             Contains the following options:

                      • Linear—

                   Specifies linear averaging, which averages over the number of packets you
                   specify in Number of Averages in a non-weighted manner.
Weighting
                      • Exponential—

                   Specifies exponential averaging, which averages over the number of packets you
                   specify in Number of Averages in a weighted manner. Exponential averaging
                  gives the most recent packets more weighting in the average than older packets.


Number of              Specifies the number of packets to average. The default is 10.Averages

             Contains the following options:

                      • Every iteration—

                 Returns the spectrum after every iteration of the Express VI.Produce
Spectrum                      • Only when averaging complete—

                 Returns the spectrum only after the Express VI gathers the number of packets
               you specify in Number of Averages.


                                                    © National Instruments 1291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1292 ordinal=1292 -->
## Functions

Functions


        Option       Description

                       Displays the first channel of Input Signal A. This graph displays the first incoming
                        signal with windowing applied.       Windowed
        Input Signal                                   If you wire data to the Express VI and run it, Windowed Input Signal A displays real
       A                       data. If you close and reopen the Express VI, Windowed Input Signal A displays
                   sample data until you run the VI again.


                       Displays the first channel of Input Signal B. This graph displays the second incoming
                        signal with windowing applied.       Windowed
        Input Signal                                   If you wire data to the Express VI and run it, Windowed Input Signal B displays real
       B                       data. If you close and reopen the Express VI, Windowed Input Signal B displays
                   sample data until you run the VI again.


                                   If you wire data to the Express VI and run it, Results displays real data. If you close
                  and reopen the Express VI, Results displays sample data until you run the VI again.

                                   • Magnitude—

                           Select to include magnitude results in the output.

                           This page appears only if you place a checkmark in the Magnitude checkbox.

                                   • Phase—

                           Select to include phase results in the output. Select Unwrap phase to return the         Results
                       phase results in radians. Select Convert to degree to return the phase results in
                          degrees.

                           This page appears only if you place a checkmark in the Phase checkbox.

                                   • Real—

                           Select to include real results in the output.

                           This page appears only if you place a checkmark in the Real checkbox.

                                   • Imaginary—


1292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1293 ordinal=1293 -->
## Functions

Functions


 Option       Description

                   Select to include imaginary results in the output.

                   This page appears only if you place a checkmark in the Imaginary checkbox.

                        • Coherence—

                   Select to include coherence results in the output.

                   This page appears only if you place a checkmark in the Coherence checkbox.


Inputs/Outputs

   •      Input Signal A —

    Contains the first input signal or signals. This is assumed to be the excitation. The input signals
    must have the same number of data points, t0, and dt. If they do not, an error is returned.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Restart Averaging (F) —

     Specifies whether to restart the selected averaging process. The default is FALSE. When you call
     this Express VI for the first time, the averaging process starts automatically.

    This input appears only if you place a checkmark in the Averaging checkbox.

   •      Input Signal B —

    Contains the second input signal or signals. This is assumed to be the response. The input
     signals must have the same number of data points, t0, and dt. If they do not, an error is returned.

   •      Magnitude —

    The magnitude from the frequency response calculations.

    This output appears only if you place a checkmark in the Magnitude checkbox.

   •      Imaginary —


                                                    © National Instruments 1293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1294 ordinal=1294 -->
## Functions

Functions


          The imaginary part from the frequency response calculations.

             This output appears only if you place a checkmark in the Imaginary checkbox.

               •      Real —

          The real part from the frequency response calculations.

             This output appears only if you place a checkmark in the Real checkbox.

               •      Averaging Done —

            Returns TRUE when the number of averages completed equals or exceeds Number of Averages.

             This output appears only if you place a checkmark in the Averaging checkbox.

               •      Coherence —

          The coherence from the frequency response calculations.

             This output appears only if you place a checkmark in the Coherence checkbox.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Phase —

          The phase from the frequency response calculations.

             This output appears only if you place a checkmark in the Phase checkbox.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Dual Channel
        Spectral Measurement.vi

     Components

       Calculates the frequency response of the first channel in Input Signal A against each

1294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1295 ordinal=1295 -->
## Functions

Functions

channel in Input Signal B, then the second channel in Input Signal A against each
channel in Input Signal B, and so on.

Specifies the number of packets to average. The default is 10.

Select to include magnitude results in the output.

Calculates the frequency response of the first channel in Input Signal A against the
first channel in Input Signal B, then the second channel in Input Signal A against the
second channel in Input Signal B, and so on.

Select to include imaginary results in the output.

Select to include real results in the output.

Returns the spectrum after every iteration of the Express VI.

Select to include coherence results in the output.

Specifies the window to apply to the signal.

Select to return the magnitude results in decibels. Remove the checkmark from this
checkbox to return the magnitude results in the original units.

Specifies the number of packets to average. The default is 10.

Select to return the phase results in radians.

Select to return the phase results in degrees.

Displays the first channel of Input Signal A. This graph displays the first incoming
signal with windowing applied.

Specifies exponential averaging, which averages over the number of packets you
specify in Number of Averages in a weighted manner. Exponential averaging gives the
most recent packets more weighting in the average than older packets.

Specifies whether the Express VI performs averaging.


                                                    © National Instruments 1295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1296 ordinal=1296 -->
## Functions

Functions

       Select to include phase results in the output.

       Displays a preview of the phase measurement of the signals.

       Returns the spectrum only after the Express VI gathers the number of packets you
       specify in Number of Averages.

       Displays the first channel of Input Signal B. This graph displays the second incoming
       signal with windowing applied.

           If you wire data to the Express VI and run it, Results displays real data. If you close and
      reopen the Express VI, Results displays sample data until you run the VI again.

       Select to include phase results in the output. Select Unwrap phase to return the phase
        results in radians. Select Convert to degree to return the phase results in degrees.

      Computes the average of complex quantities directly.

       Averages the energy, or power, of the signal.

       Specifies linear averaging, which averages over the number of packets you specify in
     Number of Averages in a non-weighted manner.
    DistortionDistortion MeasurementsMeasurements

      Performs distortion measurements on a signal, such as tone analysis, total harmonic
       distortion (THD), and signal in noise and distortion (SINAD).


      Dialog Box Options

        Option     Description

         Distortion  Contains the following options:


1296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1297 ordinal=1297 -->
## Functions

Functions


Option     Description

                    • SINAD (dB)—

                Calculates the measured signal in noise and distortion (SINAD). SINAD is defined
               as the dB of the ratio of the RMS energy of Signals to the RMS energy of Signals
                  less the energy in the fundamental. To compute the THD Plus Noise in dB, negate
               the SINAD.

                    •  Total harmonic distortion—

             Computes the measured total harmonic distortion up to and including the highest
               harmonic. THD is defined as the ratio of the RMS sum of the harmonics to the
               amplitude of the fundamental tone. To compute THD as a percentage, multiply it
              by 100.

                    •  Specific harmonic level—

               Returns the harmonic you specify.

                    • Harmonic number (fundamental = 1)—

                 Specifies the harmonic to measure. This option is available only when you select
                 Specific harmonic level.

                    • Stop search at Nyquist—

                 Specifies to include only frequencies less than the Nyquist frequency, or half the
               sampling rate, in the harmonic search. This option is available only when you
                 select Total harmonic distortion or Specific harmonic level.

            When you remove the checkmark from the Stop search at Nyquist checkbox, this
                  VI continues searching the frequency domain beyond the Nyquist frequency by
              assuming that the higher frequency components have aliased according to the
                following equation: aliased f = Fs – (f modulo Fs) where Fs = 1/dt = sampling rate

                    • Highest harmonic—

                Controls the highest harmonic, including the fundamental tone, to use for the
              harmonic analysis. For example, for third harmonic analysis, set Highest
              harmonic to 3 to measure the fundamental, second, and third harmonic. This
               option is available only when you select Total harmonic distortion or Specific
              harmonic level.


                                                    © National Instruments 1297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1298 ordinal=1298 -->
## Functions

Functions


        Option     Description

                    Contains the following options:

                                 • Search for fundamental frequency—

                         Controls the frequency domain search area, which is the center frequency and
                         width, to use for finding the fundamental tone frequency of the signal.

           ◦ Approximate frequency—

                            Center frequency to use in the frequency domain search for the fundamental
        Search             tone frequency. The default is 0. If you set Approximate frequency to –1, this
        Frequency          Express VI uses the tone with the highest amplitude as the fundamental tone.
                             This option is available only when you place a checkmark in the Search for
                         fundamental frequency checkbox.

           ◦ Search (+/- % of approx. freq.)—

                          Frequency width, as a percentage of the sampling rate, to use for the
                            frequency domain search for the fundamental tone frequency. The default is
                                  5. This option is available only when you place a checkmark in the Search for
                         fundamental frequency checkbox.


                     Displays the measurements you configured this Express VI to perform and the
                     calculated values of those measurements. You can click any measurement listed in the         Results
                 Measurement column, and the corresponding value or plot appears in the Result
                  Preview graph.


                     Displays the input signal.
        Input                                 If you wire data to the Express VI and run it, Input Signal displays real data. If you close
         Signal                 and reopen the Express VI, Input Signal displays sample data until you run the Express
                       VI again.


                     Displays a preview of the measurement. The Result Preview plot indicates the value of
         Result     the selected measurement with a dotted line.
        Preview
                                 If you wire data to the Express VI and run the VI, Result Preview displays real data. If


1298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1299 ordinal=1299 -->
## Functions

Functions


 Option     Description

           you close and reopen the Express VI, Result Preview displays sample data until you run
            the VI again. If the cutoff frequency values are invalid, Result Preview does not display
              valid data.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •     SINAD (dB) —

    Returns the measured signal in noise and distortion (SINAD). SINAD is defined as the dB of the
     ratio of the RMS energy of Signals to the RMS energy of Signals less the energy in the
    fundamental. To compute the THD Plus Noise in dB, negate the SINAD.

   •       Specific Harmonic —

    Returns the harmonic you specify in Specific harmonic level.

   •     THD —

    Returns the measured total harmonic distortion up to and including the highest harmonic. To
    compute THD as a percentage, you must multiply it by 100.


Components

Displays the measurements you configured this Express VI to perform and the
calculated values of those measurements. You can click any measurement listed in the
Measurement column, and the corresponding value or plot appears in the Result


                                                    © National Instruments 1299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1300 ordinal=1300 -->
## Functions

Functions

      Preview graph.

       Specifies the harmonic to measure. This option is available only when you select
       Specific harmonic level.

       Controls the highest harmonic, including the fundamental tone, to use for the
      harmonic analysis. For example, for third harmonic analysis, set Highest harmonic to
     3 to measure the fundamental, second, and third harmonic. This option is available
       only when you select Total harmonic distortion or Specific harmonic level.

       Controls the frequency domain search area, which is the center frequency and width,
       to use for finding the fundamental tone frequency of the signal.

      Frequency width, as a percentage of the sampling rate, to use for the frequency
      domain search for the fundamental tone frequency. The default is 5. This option is
       available only when you place a checkmark in the Search for fundamental frequency
       checkbox.

       Center frequency to use in the frequency domain search for the fundamental tone
       frequency. The default is 0. If you set Approximate frequency to –1, this Express VI
       uses the tone with the highest amplitude as the fundamental tone. This option is
       available only when you place a checkmark in the Search for fundamental frequency
       checkbox.

       Calculates the measured signal in noise and distortion (SINAD). SINAD is defined as the
     dB of the ratio of the RMS energy of Signals to the RMS energy of Signals less the
      energy in the fundamental. To compute the THD Plus Noise in dB, negate the SINAD.

       Returns the harmonic you specify.

      Computes the measured total harmonic distortion up to and including the highest
      harmonic. THD is defined as the ratio of the RMS sum of the harmonics to the
      amplitude of the fundamental tone. To compute THD as a percentage, multiply it by
       100.

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.


1300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1301 ordinal=1301 -->
## Functions

Functions

Displays the input signal.

Specifies to include only frequencies less than the Nyquist frequency, or half the
sampling rate, in the harmonic search. This option is available only when you select
Total harmonic distortion or Specific harmonic level.
ToneTone MeasurementsMeasurements

Finds the single tone with the highest amplitude or searches a specified frequency
range to find the single tone with the highest amplitude. You also can find the
frequency and phase for a single tone.


Dialog Box Options

 Option         Description

                Contains the following options:

                           • Amplitude—

                     Calculates the amplitude of the detected single tone in volts peak (Vp).

 Single Tone          • Frequency—
 Measurements
                     Calculates the frequency of the detected single tone in Hertz.

                           • Phase—

                     Calculates the phase of the detected single tone in degrees.

                Contains the following options:
 Search for
                           • Approximate frequency (Hz)— Specific
 Frequency                    Center frequency to use in the frequency domain search for the single tone.


                                                    © National Instruments 1301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1302 ordinal=1302 -->
## Functions

Functions


        Option         Description

                        The default is 10. This option is available only when you place a checkmark in
                            the Search for Specific Frequency checkbox.

                                       • Search (+/- % of approx. freq.)—

                          Frequency width, as a percentage of the sampling rate, for the frequency
                        domain search for the single tone frequency. The default is 5. This option is
                               available only when you place a checkmark in the Search for Specific
                          Frequency checkbox.


                         Displays the measurements you configured this Express VI to perform and the
                         calculated values of those measurements. You can click any measurement listed in         Results                        the Measurement column, and the corresponding value or plot appears in the
                        Result Preview graph.


                         Displays the input signal.

        Input Signal      If you wire data to the Express VI and run it, Input Signal displays real data. If you
                         close and reopen the Express VI, Input Signal displays sample data until you run
                        the Express VI again.


                         Displays a preview of the measurement. The Result Preview plot indicates the
                        value of the selected measurement with a dotted line.
         Result                                       If you wire data to the Express VI and run the VI, Result Preview displays real data.
        Preview                                       If you close and reopen the Express VI, Result Preview displays sample data until
                     you run the VI again. If the cutoff frequency values are invalid, Result Preview does
                       not display valid data.


                        Center frequency to use in the frequency domain search for the single tone. The
        Approximate
                          default is 10. This option is available only when you place a checkmark in the
        frequency (Hz)
                      Search for Specific Frequency checkbox.


1302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1303 ordinal=1303 -->
## Functions

Functions

Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Phase —

    Returns the phase of the detected single tone in degrees.

   •      Frequency —

    Returns the frequency of the detected single tone in Hertz.

   •      Amplitude —

    Returns the amplitude of the detected single tone in volts peak (Vp).


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Filter.vi

Components

Displays the measurements you configured this Express VI to perform and the
calculated values of those measurements. You can click any measurement listed in the
Measurement column, and the corresponding value or plot appears in the Result
Preview graph.

Searches for a specific frequency in the tone.


                                                    © National Instruments 1303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1304 ordinal=1304 -->
## Functions

Functions

       Center frequency to use in the frequency domain search for the single tone. The
       default is 10. This option is available only when you place a checkmark in the Search
       for Specific Frequency checkbox.

       Calculates the phase of the detected single tone in degrees.

       Calculates the frequency of the detected single tone in Hertz.

       Calculates the amplitude of the detected single tone in volts peak (Vp).

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.

       Displays the input signal.

      Frequency width, as a percentage of the sampling rate, for the frequency domain
       search for the single tone frequency. The default is 5. This option is available only
     when you place a checkmark in the Search for Specific Frequency checkbox.
   TimingTiming andand TransitionTransition MeasurementsMeasurements

      Performs timing and transition measurements, such as frequency, period, or duty
        cycle, on a signal, usually a pulse.


      Dialog Box Options

        Option         Description

                        Contains the following options:
        Timing and
                                       • Frequency—         Transition
       Measurements                              Calculates the frequency of Signals in Hertz.


1304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1305 ordinal=1305 -->
## Functions

Functions


Option         Description

                          • Period—

                     Calculates the time in seconds between adjacent middle reference level
                     crossings in the same direction. The reciprocal of this value is the signal
                    frequency.

                          • Pulse duration—

                     Calculates the time difference in seconds between the first two middle
                    reference level crossings. Pulse duration also is known as pulse width.

                          • Duty cycle—

                     Calculates the Pulse duration as a fraction of the Period.


                          • Preshoot (%)—

                     Calculates the height of the local minimum that precedes a rising transition or
                   the local maximum that precedes a falling transition as a percentage of the
                   histogram-based amplitude of the signal.

                          • Overshoot (%)—

                     Calculates the height of the local maximum that follows a rising transition or
                   the local minimum that follows a falling transition as a percentage of the
                   histogram-based amplitude of the signal.

                          • Slew rate—

                     Calculates the ratio between (90% amplitude – 10% amplitude) and the rise
                     time.


                Displays the measurement you configured this Express VI to perform and the
                calculated value of that measurement. You can click any measurement listed in the
Results
             Measurement column, and the corresponding value or plot appears in the Result
              Preview graph.


                                                    © National Instruments 1305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1306 ordinal=1306 -->
## Functions

Functions


        Option         Description

                         Displays the input signal.

        Input Signal      If you wire data to the Express VI and run it, Input Signal displays real data. If you
                         close and reopen the Express VI, Input Signal displays sample data until you run
                        the Express VI again.


                         Displays the measurement you configured this Express VI to perform and the
                         calculated value of that measurement. You can click any measurement listed in the
                    Measurement column, and the corresponding value or plot appears in the Result
                      Preview graph.         Result
        Preview                                       If you wire data to the Express VI and run the VI, Result Preview displays real data.
                                       If you close and reopen the Express VI, Result Preview displays sample data until
                     you run the VI again. If the cutoff frequency values are invalid, Result Preview does
                       not display valid data.


      Inputs/Outputs

               •      Signals —

            Contains the input signal or signals.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Duration —

            Returns the time difference in seconds between the first two middle reference level crossings.

               •      Preshoot —

            Returns the height of the local minimum that precedes a rising transition or the local maximum
             that precedes a falling transition as a percentage of the histogram-based amplitude of the signal.


1306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1307 ordinal=1307 -->
## Functions

Functions

   •      Slew Rate —

    Returns the ratio between (90% amplitude – 10% amplitude) and the rise time.

   •      Frequency —

    Returns the frequency of Signals in Hertz.

   •      Overshoot —

    Returns the height of the local maximum that follows a rising transition or the local minimum
    that follows a falling transition as a percentage of the histogram-based amplitude of the signal.

   •      Period —

    Returns the time in seconds between adjacent middle reference level crossings in the same
     direction. The reciprocal of this value is the signal frequency.

   •      Duty Cycle —

    Calculates the Pulse duration as a fraction of the Period.


Components

Displays the measurement you configured this Express VI to perform and the
calculated value of that measurement. You can click any measurement listed in the
Measurement column, and the corresponding value or plot appears in the Result
Preview graph.

Calculates the ratio between (90% amplitude – 10% amplitude) and the rise time.

Calculates the height of the local minimum that precedes a rising transition or the
local maximum that precedes a falling transition as a percentage of the histogram-
based amplitude of the signal.

Calculates the time in seconds between adjacent middle reference level crossings in
the same direction. The reciprocal of this value is the signal frequency.


                                                    © National Instruments 1307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1308 ordinal=1308 -->
## Functions

Functions

       Calculates the height of the local maximum that follows a rising transition or the local
     minimum that follows a falling transition as a percentage of the histogram-based
      amplitude of the signal.

       Calculates the Pulse duration as a fraction of the Period.

       Calculates the time difference in seconds between the first two middle reference level
       crossings. Pulse duration also is known as pulse width.

       Calculates the frequency of Signals in Hertz.

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.

       Displays the input signal.
   AmplitudeAmplitude andand LevelLevel MeasurementsMeasurements

      Performs voltage measurements on a signal.


      Dialog Box Options

        Option         Description

                        Contains the following options:

                                       • Mean (DC)—

                             Acquires a DC measurement of Signals.
        Amplitude
       Measurements     • RMS—

                              Calculates the root mean square value of Signals.

                                       • Apply window—


1308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1309 ordinal=1309 -->
## Functions

Functions


Option         Description

                    Applies a low side lobe window to Signals. This option is available only when
                 you place a checkmark in the DC or RMS checkbox.

                 Use smoothing windows to taper the sharp transitions in the effective signal.
                 You do not typically use windows if you can acquire an integer number of
                     cycles of the signal or if you are analyzing noise spectra.

                          •  Positive peak—

                  Measures the most positive peak in Signals.

                          • Negative peak—

                  Measures the most negative peak in Signals.

                          • Peak to peak—

                  Measures the most positive peak to the most negative peak in Signals.

                          • Cycle average—

                  Measures the mean level of one complete period of a periodic input signal.

                          • Cycle RMS—

                     Calculates the root mean square value of one complete period of a periodic
                    input signal.


                Displays the measurements you configured this Express VI to perform and the
                calculated values of those measurements. You can click any measurement listed in
Results
               the Measurement column, and the corresponding value or plot appears in the
               Result Preview graph.


                Displays the input signal.

Input Signal      If you wire data to the Express VI and run it, Input Signal displays real data. If you
                close and reopen the Express VI, Input Signal displays sample data until you run
               the Express VI again.


                                                    © National Instruments 1309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1310 ordinal=1310 -->
## Functions

Functions


        Option         Description

                         Displays a preview of the measurement. The Result Preview plot indicates the
                        value of the selected measurement with a dotted line.
         Result                                       If you wire data to the Express VI and run the VI, Result Preview displays real data.
        Preview                                       If you close and reopen the Express VI, Result Preview displays sample data until
                     you run the VI again. If the cutoff frequency values are invalid, Result Preview does
                       not display valid data.


      Inputs/Outputs

               •      Restart Averaging —

             Specifies whether to restart the selected averaging process. The default is FALSE. When you call
              this Express VI for the first time, the averaging process starts automatically.

             This input appears only if you place a checkmark in the Averaging checkbox.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Signals —

            Contains the input signal or signals.

               •     Mean (DC) —

            Returns the measured DC value of Signals.

               •      Negative Peak —

            Returns a measurement of the most negative peak in Signals.

               •      Cycle Average —

            Returns the mean level of one complete period of a periodic input signal.

          The cycle average of a perfect sine wave is zero, but the average level of the entire signal can be
           nonzero as a result of partial periods at the boundaries of the signal.

               •       Positive Peak —

1310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1311 ordinal=1311 -->
## Functions

Functions


  Returns a measurement of the most positive peak in Signals.

•     RMS —

  Returns the calculated RMS of the values in Signals.

•      Cycle RMS —

  Returns the root mean square value of one complete period of a periodic input signal.

•      Cycle Average —

  Returns the mean level of one complete period of a periodic input signal. The cycle average of a
  perfect sine wave is zero, but the average level of the entire signal can be nonzero as a result of
  partial periods at the boundaries of the signal.

•      Cycle RMS —

  Returns the root mean square value of one complete period of a periodic input signal.

•     Mean (DC) —

  Returns the measured DC value of Signals.

•      Negative Peak —

  Returns a measurement of the most negative peak in Signals.

•     Peak to Peak —

  Returns a measurement from the most positive peak to the most negative peak in Signals.

•       Positive Peak —

  Returns a measurement of the most positive peak in Signals.

•     RMS —

  Returns the calculated RMS of the values in Signals.

•       error out —

  Contains error information. This output provides standard error out functionality.

•     Peak to Peak —

                                                   © National Instruments 1311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1312 ordinal=1312 -->
## Functions

Functions


            Returns a measurement from the most positive peak to the most negative peak in Signals.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Amplitude and
        Level Measurements.vi

     Components

       Applies a low side lobe window to Signals. This option is available only when you
       place a checkmark in the DC or RMS checkbox.

       Displays the measurements you configured this Express VI to perform and the
       calculated values of those measurements. You can click any measurement listed in the
      Measurement column, and the corresponding value or plot appears in the Result
      Preview graph.

       Calculates the root mean square value of one complete period of a periodic input
        signal.

      Measures the mean level of one complete period of a periodic input signal.

       Acquires a DC measurement of Signals.

      Measures the most positive peak to the most negative peak in Signals.

      Measures the most negative peak in Signals.

      Measures the most positive peak in Signals.

       Calculates the root mean square value of Signals.

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.


1312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1313 ordinal=1313 -->
## Functions

Functions

Displays the input signal.

DigitalDigital WaveformWaveform

Use the Digital Waveform VIs and functions to perform operations on digital
waveforms and digital data.

The VIs and functions on this palette can return waveform error codes.


 Palette              Description Object

 Get Digital              Returns the digital waveform components you specify. You specify components by Waveform                clicking on the center of the output terminal and selecting the component you want.
 Components

 Get Digital
              Returns the digital data components you specify. You specify components by clicking Data            on the center of the output terminal and selecting either transitions or data. Components


               Builds a digital waveform or modifies an existing waveform. If you do not wire the
 Build Digital  waveform input, the function creates a new waveform based on the components
 Waveform    you wire. If you wire the waveform input, the function modifies the waveform based
            on the components you wire.


               Builds digital data or modifies existing digital data. If you do not wire the digital data
 Build Digital  input, the function creates new digital data based on the components you wire. If
 Data        you wire the digital data input, the function modifies the digital data based on the
            components you wire.

 Set
 Waveform    Adds or replaces a waveform attribute. You can use any type of data for the value of
 Attribute     the attribute.
 Function

 Get           Retrieves the names and values of all attributes or the value of a single attribute,

                                                    © National Instruments 1313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1314 ordinal=1314 -->
## Functions

Functions


         Palette                      Description
        Object

       Waveform
          Attribute     depending on whether you wire the name parameter.
         Function

                     Generates a pattern and returns the pattern as a digital waveform. Depending on the          Digital                       instance you use, the VI can return a ramp, marching values, single value, random, or         Pattern                       toggle pattern as a waveform. You must manually select the polymorphic instance        Generator                   you want to use.


                      Returns the number of samples and signals contained in the digital input. Wire data
          Digital Size   to the digital waveform in input to determine the polymorphic instance to use or
                    manually select the instance.


          Digital       Returns a subset of the digital input so you can plot the extracted signals individually
         Signal        or in subgroups on a graph. Wire data to the digital waveform input to determine the
        Subset       polymorphic instance to use or manually select the instance.


                     Replaces a subset of the input digital waveform or digital data starting at the value        Replace                        specified in start with new digital waveform data (DWDT) or digital data (DTbl). You        Subset
                   must manually select the polymorphic instance you want to use.


                    Uncompresses the digital signals in the digital input and returns the result in the
        Uncompress
                           digital output. Wire data to the uncompressed digital waveform input to determine
          Digital
                      the polymorphic instance to use or manually select the instance.


                    Compresses the digital signals in the digital input and returns the result in the digital
        Compress
                      output. Wire data to the uncompressed digital waveform input to determine the
          Digital
                     polymorphic instance to use or manually select the instance.


          Digital      Compares a digital waveform to another digital waveform or to a specified value or
        Comparison  compares a set of digital data to another set of digital data or to a specified value.


1314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1315 ordinal=1315 -->
## Functions

Functions


Palette              Description
Object

            You must manually select the polymorphic instance you want to use.


Search for    Searches for a digital pattern in the digital input. Wire data to the digital waveform
Digital        in input to determine the polymorphic instance to use or manually select the
Pattern       instance.


            Appends the signals from digital waveform (low bits) to the LSB side of digital
Append     waveform (high bits). If the sampling rates do not match, error out returns a
Digital       warning. The start time of digital waveform (low bits) is ignored. Wire data to the
Signals        digital waveform (high bits) input to determine the polymorphic instance to use or
            manually select the instance.


            Appends all samples from digital waveform B to the end of digital waveform A. IfAppend             the sampling rates do not match, error out returns a warning. The start time ofDigital
                digital waveform B is ignored. Wire data to the digital waveform A input toSamples             determine the polymorphic instance to use or manually select the instance.


               Inverts the digital data in the digital input so that a 0 becomes a 1 and vice versa or
Invert Digital an H becomes an L and vice versa. Wire data to the digital waveform input to
             determine the polymorphic instance to use or manually select the instance.


Group
            Groups digital data into a digital data array and groups digital waveforms into a
Digital
                digital waveform array.
Signals


Digital Ring   Use the digital ring constant to set the digital bit state of a digital waveform or digital
Constant     data.


Empty
             Returns an empty digital waveform. Use this constant to initialize shift registers or
Digital
              build digital waveforms.
Waveform


                                                    © National Instruments 1315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1316 ordinal=1316 -->
## Functions

Functions


         Palette                      Description
        Object

       Empty       Returns empty digital data. Use this constant to initialize shift registers or build
          Digital Data   digital tables.


          Digital                   Use the Digital Conversion VIs and Functions to convert to and from digital data.        Conversion

      GetGet DigitalDigital WaveformWaveform ComponentsComponents

       Returns the digital waveform components you specify. You specify components by
        clicking on the center of the output terminal and selecting the component you want.


      Inputs/Outputs

               •     waveform —
          waveform is the waveform from which you want to retrieve components.
               •       t0 —
             t0 returns the trigger time of the waveform.
               •      dt —
            dt returns the time interval in seconds between data points in the waveform.
               •      Y —
           Y is the data values of a waveform.
               •       attributes —
             attributes returns the names and values of all waveform attributes.

           You also can use the Get Waveform Attribute VI to retrieve the names and values of all attributes
            or the value of a single attribute.


      GetGet DigitalDigital DataData ComponentsComponents

       Returns the digital data components you specify. You specify components by clicking
      on the center of the output terminal and selecting either transitions or data.

1316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1317 ordinal=1317 -->
## Functions

Functions


Inputs/Outputs

   •     waveform —
     digital data is the waveform from which you want to retrieve components.
   •       transitions —

   •      data —
     digital data returns the data values where each row in the 2D array represents a single binary
    value for one sample of data with the most significant bit of data in the first column and the least
     significant bit of data in the last column.

BuildBuild DigitalDigital WaveformWaveform

Builds a digital waveform or modifies an existing waveform. If you do not wire the
waveform input, the function creates a new waveform based on the components you
wire. If you wire the waveform input, the function modifies the waveform based on the
components you wire.


Inputs/Outputs

   •     waveform —
    waveform is the digital waveform you want to edit. If you do not wire an existing waveform, the
    function creates a new waveform based on the components you wire.
   •       t0 —
    t0 specifies the start time of the waveform.
   •      dt —
    dt specifies the time interval in seconds between data points in the waveform.
   •      Y —
    Y is a digital table that contains the data values of a waveform.
   •       attributes —
    attributes sets the names and values of all waveform attributes.

    You also can use the Set Waveform Attribute function to set the name and value of a single


                                                    © National Instruments 1317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1318 ordinal=1318 -->
## Functions

Functions


              attribute.

               •      output waveform —
           output waveform is the resulting waveform. If you did not wire an existing waveform, this is a
         new waveform. If you wired an existing waveform, this is the edited waveform.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Digital Waveform Graph\Create Digital Waveform.vi

      BuildBuild DigitalDigital DataData

       Builds digital data or modifies existing digital data. If you do not wire the digital data
       input, the function creates new digital data based on the components you wire. If you
       wire the digital data input, the function modifies the digital data based on the
      components you wire.

      You can use this function to build digital tables.


      Inputs/Outputs

               •     waveform —
              digital data is the digital data you want to edit. If you do not wire the digital data input, the
             function creates new digital data based on the components you wire.
               •       transitions —

               •      data —
              digital data component is a 2D array that contains the data values as 8-bit unsigned integers.
           Each row in the 2D array represents a single binary value for one sample of data with the most
              significant bit of data in the first column and the least significant bit of data in the last column.
           Each value in the 2D array corresponds to a digital value, or digital data state, represented in the
              digital data output.


1318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1319 ordinal=1319 -->
## Functions

Functions


    The following table shows the digital data state represented by each of the valid 8-bit unsigned
     integers.

           Digital    Value           Description         Data State
         0 (Drive
    0               Force logic low. Drive to the low voltage level (VOL).         Low)
         1 (Drive
    1               Force logic high. Drive to the high voltage level (VOH).          High)
        Z (Force    2               Force logic high impedance. Turn the driver off.           Off)
         L                 Compare logic low (edge). Compare for a voltage level lower than the low    3    (Compare                     voltage threshold.
         Low)
       H                 Compare logic high (edge). Compare for a voltage level higher than the high
    4    (Compare
                     voltage threshold (VOH).          High)
        X
    5    (Compare Compare logic unknown. Do not compare.
        Unknown)
        T                 Compare logic high impedance (edge). Compare for a voltage level between
    6    (Compare
                    the low voltage threshold (VOL) and the high voltage threshold (VOH).           Off)
        V                 Compare logic valid level (edge). Compare for a voltage level either lower than
    7    (Compare
                    the low voltage threshold (VOL) or higher than the high voltage threshold (VOH).           Valid)

   •      output waveform —
     digital data is the resulting digital data. If you did not wire existing digital data, this is the new
     digital data. If you wired existing digital data, this is the edited digital data.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Digital Waveform Graph\Digital Waveform
   Graph.lvproj


                                                    © National Instruments 1319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1320 ordinal=1320 -->
## Functions

Functions

      SetSet WaveformWaveform AttributeAttribute FunctionFunction

      Adds or replaces a waveform attribute. You can use any type of data for the value of
       the attribute.


      Inputs/Outputs

               •     waveform —

          waveform is the waveform for which you want to add or replace an attribute.

               •     name —

         name is the name of the attribute.

               •      value —

            value is the value of the attribute. This input is polymorphic, so you can wire any data to it.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     waveform out —

          waveform out is the waveform with the new or replaced attribute.

               •      replaced —

            replaced indicates if an attribute was overwritten.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If the attribute in name already exists, the function overwrites the attribute with the


1320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1321 ordinal=1321 -->
## Functions

Functions

new value, and replaced is TRUE. If the attribute in name does not exist already, the
function creates a new attribute. Some attributes are set by NI-DAQ and Express VIs.

The following table lists the waveform attributes set by NI-DAQ.


                            Data
 Name     Attribute                 Acceptable Values   Description                          Type

 Hardware                        Any value is        NI_DeviceNumber is the device
 Device    NI_DeviceNumber   String  acceptable for     number of the hardware producing
 Number                           NI_DeviceNumber.  the waveform.

                                 Any value is        NI_ChannelName is the name of the Name of          NI_ChannelName   String  acceptable for        virtual channel producing the Channel                                 NI_ChannelName.   waveform.

                                                   NI_LineNames is the name of the
 Name of                         Any value is           digital line in the waveform. For more
 Digital    NI_LineNames      String  acceptable for      than one digital line, the function
 Line(s)                            NI_LineNames.      returns the line names in reverse
                                                               order.

                                            Volts, PSI, and so
                                         forth are Unit for                                                   NI_UnitDescription is the units of            NI_UnitDescription  String  acceptable values
 Data                                              measure for the waveform.                                           for
                                       NI_UnitDescription.

The following table lists the waveform attributes set by Express VIs.


                                 Data
 Name       Attribute                       Acceptable Values       Description
                               Type

                                                                NI_ExpStartTimeStamp is
                                                                   the time stamp of the first
                                                             sample in the first
                                                               waveform. In Express VIs,
                                       Any value is acceptable
 Start                          Time                                 this is set once per start
            NI_ExpStartTimeStamp            for
 Timestamp                     stamp                             of the VI and does not
                                           NI_ExpStartTimeStamp.
                                                                  change, even if waveform
                                                                  data is generated in a
                                                                        loop. In Express VIs,
                                                                NI_ExpStartTimeStamp is


                                                    © National Instruments 1321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1322 ordinal=1322 -->
## Functions

Functions


                                                                                   set according to the PC
                                                                              clock unless the
                                                                  waveform originates in
                                                                          NI-DAQ. When the
                                                                  waveform originates in
                                                                          NI-DAQ, NI-DAQ sets
                                                                         NI_ExpStartTimeStamp.

                                                                    NI_ExpTimeStamp is the
                                                                        time stamp of the first
                                                                    sample in the waveform.
                                                                                     In Express VIs,
                                                                    NI_ExpTimeStamp is set
                                     Time    Any value is acceptable  according to the PC clock       Timestamp NI_ExpTimeStamp
                                      stamp    for NI_ExpTimeStamp.   unless the waveform
                                                                                   originates in NI-DAQ.
                                                          When the waveform
                                                                                   originates in NI-DAQ, NI-
                                                         DAQ sets
                                                                      NI_ExpTimeStamp.

                                                                                                                            If the value of
                                              Use a single character                                                                      NI_ExpXDimension is t, t0                                                             for the                                                                and dt are unchanged. If
                                                NI_ExpXDimension                                                                           the value of                                                         value. Currently, only t        X                                                             NI_ExpXDimension is f,
                   NI_ExpXDimension      String    for time and f for        Dimension                                                          Express VIs interpret t0                                                   frequency are                                                                and dt as f0 and df. For all
                                                    supported. The value                                                                             other values, or unknown                                                             for NI_ExpXDimension                                                                          dimension, t0 and dt are
                                                                        is case sensitive.                                                                                 interpreted as X0 and dX.

                                                                                                                            If and only if
                                          TRUE or FALSE are      NI_ExpXDimension is t,
         Relative
                     NI_ExpIsRelativeTime   Boolean  acceptable values for    Express VIs set t0 as a
        Time?
                                                      NI_ExpIsRelativeTime.   relative/absolute time
                                                                  stamp value.

           Note Express VIs also use the attributes set by NI-DAQ. If the waveform does
              not originate in NI-DAQ, Express VIs add NI_ChannelName.


1322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1323 ordinal=1323 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Create.vi

GetGet WaveformWaveform AttributeAttribute FunctionFunction

Retrieves the names and values of all attributes or the value of a single attribute,
depending on whether you wire the name parameter.

Attributes can be channel names. The connector pane displays the default data types
for this polymorphic function.


Inputs/Outputs

   •     waveform —

    waveform is the waveform for which you want to retrieve an attribute(s) and value(s).

   •     name —

   name is the name of the attribute whose value you want to retrieve.

   Do not wire this parameter if you want to retrieve all the attributes associated with the specified
    waveform. If you wire name, the names output changes to a Boolean output found, the array
    output values changes to an output called value of the same type as default value, and the
    function searches for only the specified attribute.
   •       default value (empty Variant) —

    default value is a value and data type that you specify. If the function does not find the attribute
     specified in name, it returns the default value.

       If you wire default value, you must wire name.
   •       error in (no error) —


                                                    © National Instruments 1323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1324 ordinal=1324 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      duplicate waveform —

            duplicate waveform is the waveform data you input in waveform.

               •     names —

          names returns a 1D array containing the names of all attributes associated with the waveform.

                    If you wire the name parameter, this output changes to a Boolean value found. found returns
          TRUE if the function finds the attribute that you specify in name.
               •      values —

            values returns a 1D array containing the values associated with each attribute of the specified
           waveform in variant format.

           You must unflatten each attribute value to an appropriate data type. If you wire name, this
           output changes to a single variant value. If the function does not find the attribute that you
             specify in name, it returns the value passed to default value.
               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This function has two modes of behavior depending on whether you wire the name
       parameter. By default, the function returns the names of all attributes and their
       corresponding values in 1D arrays. If you wire name, the names output changes to a
      Boolean output found, the values output changes to a variant output value, and the
       function searches for only the specified attribute. If the function does not find the
       specified attribute(s), or if it cannot convert the attribute(s) to the default value, found
         is FALSE, and value displays the contents of default value.

      The following table lists the waveform attributes set by NI-DAQ.


                                   Data
      Name     Attribute                 Acceptable Values        Description
                                 Type

        Hardware                        Any value is acceptable   NI_DeviceNumber is the device
                 NI_DeviceNumber   String
         Device                                    for NI_DeviceNumber.   number of the hardware device


1324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1325 ordinal=1325 -->
## Functions

Functions


                            Data Name     Attribute                 Acceptable Values        Description
                          Type

 Number                                                   producing the waveform.

                                                     NI_ChannelName is the name of Name of                         Any value is acceptable          NI_ChannelName   String                          the virtual channel producing Channel                                  for NI_ChannelName.
                                                             the waveform.

 Name of                                 Any value is acceptable   NI_LineNames is the name of Digital    NI_LineNames      String                                           for NI_LineNames.       the digital line in the waveform. Line(s)

                                            Volts, PSI, and so forth Unit for                                                       NI_UnitDescription is the units            NI_UnitDescription  String  are acceptable values for Data                                                              of measure for the waveform.                                       NI_UnitDescription.

The following table lists the waveform attributes set by Express VIs.


                                 Data Name       Attribute                       Acceptable Values       Description
                               Type

                                                                NI_ExpStartTimeStamp is
                                                                   the time stamp of the first
                                                             sample in the first
                                                               waveform. In Express VIs,
                                                                                this is set once per start
                                                                          of the VI and does not
                                                                  change, even if waveform
                                       Any value is acceptable  data is generated in a Start                          Time            NI_ExpStartTimeStamp            for                      loop. In Express VIs,
 Timestamp                     stamp
                                           NI_ExpStartTimeStamp. NI_ExpStartTimeStamp is
                                                                           set according to the PC
                                                                      clock unless the
                                                           waveform originates in
                                                                  NI-DAQ. When the
                                                           waveform originates in
                                                                  NI-DAQ, NI-DAQ sets
                                                                 NI_ExpStartTimeStamp.

                                                             NI_ExpTimeStamp is the
                               Time    Any value is acceptable  time stamp of the first
 Timestamp NI_ExpTimeStamp
                               stamp    for NI_ExpTimeStamp.   sample in the waveform.
                                                                            In Express VIs,


                                                    © National Instruments 1325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1326 ordinal=1326 -->
## Functions

Functions


                                        Data      Name       Attribute                       Acceptable Values       Description
                                      Type

                                                                    NI_ExpTimeStamp is set
                                                                            according to the PC clock
                                                                             unless the waveform
                                                                                   originates in NI-DAQ.
                                                          When the waveform
                                                                                   originates in NI-DAQ, NI-
                                                         DAQ sets
                                                                      NI_ExpTimeStamp.

                                                                                                                            If the value of
                                                                      NI_ExpXDimension is t, t0                                              Use a single character                                                                and dt are unchanged. If                                                             for the
                                                                           the value of                                                NI_ExpXDimension
                                                                      NI_ExpXDimension is f,                                                         value. Currently, only t        X                                                                  Express VIs interpret t0                   NI_ExpXDimension      String    for time and f for
        Dimension                                                 and dt as f0 and df. For all                                                   frequency are                                                                             other values, Express VIs
                                                    supported. The value                                                                                   generically interpret t0                                                             for NI_ExpXDimension                                                                and dt as X0 and dX, but
                                                                        is case sensitive.                                                                              there is no effect
                                                                              otherwise.

                                                                                                                            If and only if
                                          TRUE or FALSE are      NI_ExpXDimension is t,
         Relative                     NI_ExpIsRelativeTime   Boolean  acceptable values for    Express VIs set t0 as a        Time?                                                      NI_ExpIsRelativeTime.   relative/absolute time
                                                                  stamp value.

           Note Express VIs also use the attributes set by NI-DAQ. If the waveform does
              not originate in NI-DAQ, Express VIs add NI_ChannelName.

       DigitalDigital PatternPattern GeneratorGenerator

       Generates a pattern and returns the pattern as a digital waveform. Depending on the
       instance you use, the VI can return a ramp, marching values, single value, random, or
       toggle pattern as a waveform. You must manually select the polymorphic instance you
      want to use.


1326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1327 ordinal=1327 -->
## Functions

Functions


  • Digital Pattern Generator (Ramp) VI
  • Digital Pattern Generator (Marching Values) VI
  • Digital Pattern Generator (Single Value) VI
  • Digital Pattern Generator (Random) VI
  • Digital Pattern Generator (Toggle) VI

The Ramp instance generates a digital waveform that contains a binary count-up
pattern that starts at zero and counts up by one until it reaches 2n–1, where n=
number of signals.
DigitalDigital PatternPattern GeneratorGenerator (Ramp)(Ramp) VIVI

Generates a pattern and returns the pattern as a digital waveform. Depending on the
instance you use, the VI can return a ramp, marching values, single value, random, or
toggle pattern as a waveform. You must manually select the polymorphic instance you
want to use.


Inputs/Outputs

   •     number of samples —

   number of samples specifies the number of samples to include in the generated digital
    waveform.

   •     number of signals —

   number of signals specifies the number of signals to include in the generated digital waveform.

   •     sample rate —

    sample rate specifies the sample rate of the generated digital waveform. The default is 1 kHz.


                                                    © National Instruments 1327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1328 ordinal=1328 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digital waveform —

              digital waveform returns the generated digital waveform pattern.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The Ramp instance generates a digital waveform that contains a binary count-up
       pattern that starts at zero and counts up by one until it reaches 2n–1, where n=
     number of signals.
    DigitalDigital PatternPattern GeneratorGenerator (Marching(Marching Values)Values)
    VIVI

       Generates a pattern and returns the pattern as a digital waveform. Depending on the
       instance you use, the VI can return a ramp, marching values, single value, random, or
       toggle pattern as a waveform. You must manually select the polymorphic instance you
      want to use.


      Inputs/Outputs

               •      marching value —

           marching value is the binary value that marches across the signals of the generated digital


1328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1329 ordinal=1329 -->
## Functions

Functions


    waveform. The default is 1.

   •      hold value —

    hold value is the binary value of the generated digital waveform. The default is 0.

   •     number of samples —

   number of samples specifies the number of samples to include in the generated digital
    waveform.

   •     number of signals —

   number of signals specifies the number of signals to include in the generated digital waveform.

   •     sample rate —

    sample rate specifies the sample rate of the generated digital waveform. The default is 1 kHz.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digital waveform —

     digital waveform returns the generated digital waveform pattern.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Ramp instance generates a digital waveform that contains a binary count-up
pattern that starts at zero and counts up by one until it reaches 2n–1, where n=
number of signals.
DigitalDigital PatternPattern GeneratorGenerator (Single(Single Value)Value) VIVI

Generates a pattern and returns the pattern as a digital waveform. Depending on the
instance you use, the VI can return a ramp, marching values, single value, random, or

                                                    © National Instruments 1329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1330 ordinal=1330 -->
## Functions

Functions

       toggle pattern as a waveform. You must manually select the polymorphic instance you
      want to use.


      Inputs/Outputs

               •      value —

            value is the digital bit state of the generated digital waveform. The default is 0.

               •     number of samples —

          number of samples specifies the number of samples to include in the generated digital
           waveform.

               •     number of signals —

          number of signals specifies the number of signals to include in the generated digital waveform.

               •     sample rate —

           sample rate specifies the sample rate of the generated digital waveform. The default is 1 kHz.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digital waveform —

              digital waveform returns the generated digital waveform pattern.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The Ramp instance generates a digital waveform that contains a binary count-up


1330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1331 ordinal=1331 -->
## Functions

Functions

pattern that starts at zero and counts up by one until it reaches 2n–1, where n=
number of signals.
DigitalDigital PatternPattern GeneratorGenerator (Random)(Random) VIVI

Generates a pattern and returns the pattern as a digital waveform. Depending on the
instance you use, the VI can return a ramp, marching values, single value, random, or
toggle pattern as a waveform. You must manually select the polymorphic instance you
want to use.


Inputs/Outputs

   •     number of samples —

   number of samples specifies the number of samples to include in the generated digital
    waveform.

   •     number of signals —

   number of signals specifies the number of signals to include in the generated digital waveform.

   •     sample rate —

    sample rate specifies the sample rate of the generated digital waveform. The default is 1 kHz.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digital waveform —

     digital waveform returns the generated digital waveform pattern.

   •       error out —


                                                    © National Instruments 1331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1332 ordinal=1332 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      The Ramp instance generates a digital waveform that contains a binary count-up
       pattern that starts at zero and counts up by one until it reaches 2n–1, where n=
     number of signals.
    DigitalDigital PatternPattern GeneratorGenerator (Toggle)(Toggle) VIVI

       Generates a pattern and returns the pattern as a digital waveform. Depending on the
       instance you use, the VI can return a ramp, marching values, single value, random, or
       toggle pattern as a waveform. You must manually select the polymorphic instance you
      want to use.


      Inputs/Outputs

               •      value 2 —

            value 2 is the second digital bit state of the generated digital waveform. The default is 1.

               •      value 1 —

            value 1 is the first digital bit state of the generated digital waveform. The default is 0.

               •     number of samples —

          number of samples specifies the number of samples to include in the generated digital
           waveform.

               •     number of signals —

          number of signals specifies the number of signals to include in the generated digital waveform.


1332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1333 ordinal=1333 -->
## Functions

Functions

   •     sample rate —

    sample rate specifies the sample rate of the generated digital waveform. The default is 1 kHz.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digital waveform —

     digital waveform returns the generated digital waveform pattern.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Ramp instance generates a digital waveform that contains a binary count-up
pattern that starts at zero and counts up by one until it reaches 2n–1, where n=
number of signals.

DigitalDigital SizeSize

Returns the number of samples and signals contained in the digital input. Wire data to
the digital waveform in input to determine the polymorphic instance to use or
manually select the instance.


  • DWDT Digital Size VI
  • DTbl Digital Size VI
DWDTDWDT DigitalDigital SizeSize VIVI

Returns the number of samples and signals contained in the digital input. Wire data to
the digital waveform in input to determine the polymorphic instance to use or
manually select the instance.

                                                    © National Instruments 1333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1334 ordinal=1334 -->
## Functions

Functions


      Inputs/Outputs

               •       digital waveform in —

              digital waveform in is the input digital waveform.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       digital waveform out —

              digital waveform out returns digital waveform in unchanged.

               •     number of samples —

          number of samples returns the number of sample data elements of digital data contained in the
               digital input.

               •     number of signals —

          number of signals returns the number of signal elements contained in the digital input.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   DTblDTbl DigitalDigital SizeSize VIVI

       Returns the number of samples and signals contained in the digital input. Wire data to
       the digital waveform in input to determine the polymorphic instance to use or
      manually select the instance.


1334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1335 ordinal=1335 -->
## Functions

Functions


Inputs/Outputs

   •       digital data in —

     digital data in is the input set of digital data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital data out —

     digital data out returns digital data in unchanged.

   •     number of samples —

   number of samples returns the number of sample data elements of digital data contained in the
     digital input.

   •     number of signals —

   number of signals returns the number of signal elements contained in the digital input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


DigitalDigital SignalSignal SubsetSubset

Returns a subset of the digital input so you can plot the extracted signals individually
or in subgroups on a graph. Wire data to the digital waveform input to determine the
polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1336 ordinal=1336 -->
## Functions

Functions


            • DWDT Digital Signal Subset VI
            • DTbl Digital Signal Subset VI

      Use the Digital Signal Subset VI to extract individual signals from a digital waveform.
      The block diagram below shows how you can combine extracted individual signals
       with other digital data to create new digital waveforms.


      The top Digital Signal Subset VI extracts the first and second signals from the digital
      waveform. The bottom Digital Signal Subset VI extracts the fourth and fifth signals. The
      Append Digital Samples VI appends the first signal to the fourth signal, appends the
      second signal to the fifth signal, and plots the resulting two signals on a digital
      waveform graph.
  DWDTDWDT DigitalDigital SignalSignal SubsetSubset VIVI

       Returns a subset of the digital input so you can plot the extracted signals individually
       or in subgroups on a graph. Wire data to the digital waveform input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       digital waveform —


1336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1337 ordinal=1337 -->
## Functions

Functions


     digital waveform is the input digital waveform.

   •       signals —

    signals is a 1D array of numbers. Each number in the array represents a signal number. If any
    value in signals is greater than the number of signals in the digital input, the VI returns an error.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital subset —

     digital subset returns the requested subset of digital waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the Digital Signal Subset VI to extract individual signals from a digital waveform.
The block diagram below shows how you can combine extracted individual signals
with other digital data to create new digital waveforms.


The top Digital Signal Subset VI extracts the first and second signals from the digital
waveform. The bottom Digital Signal Subset VI extracts the fourth and fifth signals. The
Append Digital Samples VI appends the first signal to the fourth signal, appends the
second signal to the fifth signal, and plots the resulting two signals on a digital
waveform graph.


                                                    © National Instruments 1337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1338 ordinal=1338 -->
## Functions

Functions

   DTblDTbl DigitalDigital SignalSignal SubsetSubset VIVI

       Returns a subset of the digital input so you can plot the extracted signals individually
       or in subgroups on a graph. Wire data to the digital waveform input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       digital data —

              digital data is the set of input digital data.

               •       signals —

             signals is a 1D array of numbers. Each number in the array represents a signal number. If any
            value in signals is greater than the number of signals in the digital input, the VI returns an error.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       digital subset —

              digital subset returns the requested subset of digital data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use the Digital Signal Subset VI to extract individual signals from a digital waveform.
      The block diagram below shows how you can combine extracted individual signals
       with other digital data to create new digital waveforms.


1338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1339 ordinal=1339 -->
## Functions

Functions


The top Digital Signal Subset VI extracts the first and second signals from the digital
waveform. The bottom Digital Signal Subset VI extracts the fourth and fifth signals. The
Append Digital Samples VI appends the first signal to the fourth signal, appends the
second signal to the fifth signal, and plots the resulting two signals on a digital
waveform graph.

ReplaceReplace SubsetSubset

Replaces a subset of the input digital waveform or digital data starting at the value
specified in start with new digital waveform data (DWDT) or digital data (DTbl). You
must manually select the polymorphic instance you want to use.


  • DWDT Replace Subset VI
  • DTbl Replace Subset VI
DWDTDWDT ReplaceReplace SubsetSubset VIVI

Replaces a subset of the input digital waveform or digital data starting at the value
specified in start with new digital waveform data (DWDT) or digital data (DTbl). You
must manually select the polymorphic instance you want to use.


                                                    © National Instruments 1339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1340 ordinal=1340 -->
## Functions

Functions

      Inputs/Outputs

               •       start value format —

              start value format specifies the search method.

            Samples (default)—The subset begins from a particular element from the set of waveform data           0               in digital waveform in.
           1 Relative Time—The subset begins from the data value at a particular time.

               •       digital waveform in —

              digital waveform in is the digital waveform for which you want to replace a subset.

               •     new digital waveform —

         new digital waveform is the new digital waveform data with which you want to replace a subset
             of digital waveform in.

               •       start samples/time —

              start samples/time is the data element or time value where the subset you are replacing begins.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       signal index —

             signal index specifies the signal at which to begin replacing data. The default is 0.

               •       digital waveform out —

              digital waveform out returns digital waveform in with the replaced subset.

               •      actual start samples/time —

            actual start samples/time is the actual data element where you replaced the subset.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1341 ordinal=1341 -->
## Functions

Functions

DTblDTbl ReplaceReplace SubsetSubset VIVI

Replaces a subset of the input digital waveform or digital data starting at the value
specified in start with new digital waveform data (DWDT) or digital data (DTbl). You
must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •       digital data in —

     digital data in is the digital data for which you want to replace a subset.

   •     new digital data —

   new digital data is the new digital data with which you want to replace a subset of digital data
     in.

   •       start —

     start is the data element where you want to start replacing the digital table subset. The default is
     0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       signal index —

    signal index specifies the signal at which to begin replacing data. The default is 0.

   •       digital data out —

     digital data out returns digital data in with the replaced subset.

   •       error out —


                                                    © National Instruments 1341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1342 ordinal=1342 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     UncompressUncompress DigitalDigital

      Uncompresses the digital signals in the digital input and returns the result in the
        digital output. Wire data to the uncompressed digital waveform input to determine
       the polymorphic instance to use or manually select the instance.


            • DWDT Uncompress Digital VI
            • DTbl Uncompress Digital VI
  DWDTDWDT UncompressUncompress DigitalDigital VIVI

      Uncompresses the digital signals in the digital input and returns the result in the
        digital output. Wire data to the uncompressed digital waveform input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      compressed digital waveform —

           compressed digital waveform is the waveform you want to uncompress.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.


1342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1343 ordinal=1343 -->
## Functions

Functions

   •     uncompressed digital waveform —

    uncompressed digital waveform returns the uncompressed digital waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DTblDTbl UncompressUncompress DigitalDigital VIVI

Uncompresses the digital signals in the digital input and returns the result in the
digital output. Wire data to the uncompressed digital waveform input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       digital data in —

     digital data in is the input set of digital data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital data out —

     digital data out returns the uncompressed digital data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1344 ordinal=1344 -->
## Functions

Functions

     CompressCompress DigitalDigital

      Compresses the digital signals in the digital input and returns the result in the digital
       output. Wire data to the uncompressed digital waveform input to determine the
      polymorphic instance to use or manually select the instance.


            • DWDT Compress Digital VI
            • DTbl Compress Digital VI

      Use the Compress Digital VI to compress digital data when you want to display two or
      more serial digital signals with the same bit sets on the same row to better visualize
       the data. For example, if you acquire 10 digital waveform samples and nine waveforms
       are identical but the tenth waveform differs, compressing the digital data helps you
        easily find which waveform is different. Compressing digital data also conserves
     memory resources. Use the Uncompress Digital VI to uncompress digital data you
      compress.
  DWDTDWDT CompressCompress DigitalDigital VIVI

      Compresses the digital signals in the digital input and returns the result in the digital
       output. Wire data to the uncompressed digital waveform input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       force compression? —

             force compression? specifies whether the compression is performed even if the data already
           appears to be compressed.


1344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1345 ordinal=1345 -->
## Functions

Functions

   •     uncompressed digital waveform —

    uncompressed digital waveform is the waveform you want to compress.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      compressed digital waveform —

    compressed digital waveform returns the compressed waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the Compress Digital VI to compress digital data when you want to display two or
more serial digital signals with the same bit sets on the same row to better visualize
the data. For example, if you acquire 10 digital waveform samples and nine waveforms
are identical but the tenth waveform differs, compressing the digital data helps you
easily find which waveform is different. Compressing digital data also conserves
memory resources. Use the Uncompress Digital VI to uncompress digital data you
compress.
DTblDTbl CompressCompress DigitalDigital VIVI

Compresses the digital signals in the digital input and returns the result in the digital
output. Wire data to the uncompressed digital waveform input to determine the
polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1346 ordinal=1346 -->
## Functions

Functions

      Inputs/Outputs

               •       force compression? —

             force compression? specifies whether the compression is performed even if the data already
           appears to be compressed.

               •     uncompressed digital data —

          uncompressed digital data is the digital data you want to compress.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •      compressed digital data —

           compressed digital data returns the compressed digital data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use the Compress Digital VI to compress digital data when you want to display two or
      more serial digital signals with the same bit sets on the same row to better visualize
       the data. For example, if you acquire 10 digital waveform samples and nine waveforms
       are identical but the tenth waveform differs, compressing the digital data helps you
        easily find which waveform is different. Compressing digital data also conserves
     memory resources. Use the Uncompress Digital VI to uncompress digital data you
      compress.

       DigitalDigital ComparisonComparison

      Compares a digital waveform to another digital waveform or to a specified value or
      compares a set of digital data to another set of digital data or to a specified value. You
      must manually select the polymorphic instance you want to use.


1346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1347 ordinal=1347 -->
## Functions

Functions


  • DWDT Digital To Digital Comparison VI
  • DTbl Digital To Digital Comparison VI
  • DWDT Digital Comparison VI
  • DTbl Digital Comparison VI
DWDTDWDT DigitalDigital ToTo DigitalDigital ComparisonComparison VIVI

Compares a digital waveform to another digital waveform or to a specified value or
compares a set of digital data to another set of digital data or to a specified value. You
must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •       start sample B —

     start sample B specifies where to start the comparison within digital waveform B.

   •       start sample A —

     start sample A specifies where to start the comparison within digital waveform A.

   •       digital waveform A —

     digital waveform A is the waveform for which you want to perform a digital comparison.

   •       digital waveform B —

     digital waveform B is the waveform for which you want to perform a digital comparison.

   •       error in (no error) —


                                                    © National Instruments 1347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1348 ordinal=1348 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •     compare level —

          compare level specifies the comparison results returned by the VI.

              Pass/Fail Only (default)—Specifies that the VI returns only passed? as an output, which
           0             improves the performance of the comparison.
           1 Pass/Fail and # Errors—Specifies that the VI returns passed? and # failed samples.
               Pass/Fail, # Errors and Diff Data—Specifies that the VI returns passed?, # failed samples, and           2
                 diff data.

               •      # samples to compare (-1: all) —

           # samples to compare specifies the number of samples in digital waveform A and digital
          waveform B to compare. The default value is –1, which specifies that the VI compares all
            samples.

               •      passed? —

           passed? returns TRUE if all corresponding values in digital waveform A and digital waveform B
           match.

               •      # failed samples —

           # failed samples returns the total number of corresponding samples in digital waveform A and
              digital waveform B that do not match.

               •        diff data —

               diff data returns the waveform representing the comparison of digital waveform A and digital
          waveform B. Zeros represent corresponding samples that match. Ones represent corresponding
           samples that differ. You can use this data to determine the exact location of all differing samples.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1349 ordinal=1349 -->
## Functions

Functions

DTblDTbl DigitalDigital ToTo DigitalDigital ComparisonComparison VIVI

Compares a digital waveform to another digital waveform or to a specified value or
compares a set of digital data to another set of digital data or to a specified value. You
must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •       start position B —

     start position B specifies where to start the comparison within digital data B.

   •       start position A —

     start position A specifies where to start the comparison within digital data A.

   •       digital data A —

     digital data A is the digital data for which you want to perform a digital comparison.

   •       digital data B —

     digital data B is the digital data for which you want to perform a digital comparison.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •     compare level —

    compare level specifies the comparison results returned by the VI.


                                                    © National Instruments 1349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1350 ordinal=1350 -->
## Functions

Functions


              Pass/Fail Only (default)—Specifies that the VI returns only passed? as an output, which           0
             improves the performance of the comparison.
           1 Pass/Fail and # Errors—Specifies that the VI returns passed? and # failed samples.
               Pass/Fail, # Errors and Diff Data—Specifies that the VI returns passed?, # failed samples, and           2                 diff data.

               •      # samples to compare (-1:all) —

           # samples to compare specifies the number of samples in digital data A and digital data B to
           compare. The default value is -1, which specifies that the VI compares all samples.

               •      passed? —

           passed? returns TRUE if all corresponding values in digital data A and digital data B match.

               •      # failed samples —

           # failed samples returns the total number of corresponding samples in digital data A and digital
           data B that do not match.

               •        diff data —

               diff data returns the digital data representing the comparison of digital data A and digital data
             B. Zeros represent corresponding samples that match. Ones represent corresponding samples
             that differ. You can use this data to determine the exact location of all differing samples.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

  DWDTDWDT DigitalDigital ComparisonComparison VIVI

      Compares a digital waveform to another digital waveform or to a specified value or
      compares a set of digital data to another set of digital data or to a specified value. You
      must manually select the polymorphic instance you want to use.


1350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1351 ordinal=1351 -->
## Functions

Functions

Inputs/Outputs

   •       digital waveform —

     digital waveform is the input digital waveform.

   •      comparison —

    comparison specifies to what value the digital data contained in the digital input is compared.

    0     Equal 0 (default)—Force Down
    1     Equal 1—Force Up
    2     Equal Z—Force Z
    3     Equal L—Compare Low
    4     Equal H—Compare High
    5     Equal X—Compare Don't Care
    6     Equal T—Compare Invalid
    7     Equal V—Compare Valid
    8     Equal 0 or L
    9     Equal 1 or H
    10    Not Equal 0 or 1
    11    Not Equal 0, 1, L, or H

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      boolean array —

    boolean array is a Boolean-array representation of where the comparison value is found in the
     digital data contained in the digital input.

   •      passed? —

    passed? returns TRUE if any value in the digital data contained in the digital input matches the
    comparison request specified in comparison.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1352 ordinal=1352 -->
## Functions

Functions

   DTblDTbl DigitalDigital ComparisonComparison VIVI

      Compares a digital waveform to another digital waveform or to a specified value or
      compares a set of digital data to another set of digital data or to a specified value. You
      must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •       digital data —

              digital data is the set of input digital data.

               •      comparison —

           comparison specifies to what value the digital data contained in the digital input is compared.

           0     Equal 0 (default)—Force Down
           1     Equal 1—Force Up
           2     Equal Z—Force Z
           3     Equal L—Compare Low
           4     Equal H—Compare High
           5     Equal X—Compare Don't Care
           6     Equal T—Compare Invalid
           7     Equal V—Compare Valid
           8     Equal 0 or L
           9     Equal 1 or H
           10    Not Equal 0 or 1
           11    Not Equal 0, 1, L, or H

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.


1352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1353 ordinal=1353 -->
## Functions

Functions

   •      boolean array —

    boolean array is a Boolean-array representation of where the comparison value is found in the
     digital data contained in the digital input.

   •      Passed? —

    Passed? returns TRUE if any value in the digital data contained in the digital input matches the
    comparison request specified in comparison.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SearchSearch forfor DigitalDigital PatternPattern

Searches for a digital pattern in the digital input. Wire data to the digital waveform in
input to determine the polymorphic instance to use or manually select the instance.


  • DWDT Search for Digital Pattern VI
  • DTbl Search for Digital Pattern VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Digital Waveform Graph\Search Digital Data for
   Pattern.vi
DWDTDWDT SearchSearch forfor DigitalDigital PatternPattern VIVI

Searches for a digital pattern in the digital input. Wire data to the digital waveform in
input to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1354 ordinal=1354 -->
## Functions

Functions


      Inputs/Outputs

               •       start value format —

              start value format specifies the search method.

            Samples (default)—The subset begins from a particular element from the set of waveform data           0
               in digital waveform in.
           1 Relative Time—The subset begins from the data value at a particular time.

               •       digital waveform in —

              digital waveform in is the input digital waveform.

               •       digital pattern —

              digital pattern specifies the digital pattern for which you want to search.

            For example, if you acquire a large digital waveform and want to see if any part of the digital
           waveform matches a certain pattern, wire that pattern to the digital pattern input to discover
           any matches.

               •       start index/time —

              start index/time specifies the point in digital waveform in where the search begins. You specify
           whether this is an index or time in indexing mode. The default is 0, which is the beginning of
              digital waveform in.

         When indexing mode is set to Relative Time, this VI checks start index/time to determine if it is
          an integer multiple of dt. If start index/time is not an integer multiple of dt, this VI uses the
             closest exact multiple of dt. This VI returns an error if start index/time is out of range for digital
          waveform in.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following


1354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1355 ordinal=1355 -->
## Functions

Functions


    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •     compare mode —

    compare mode specifies how to handle values of X for the search.

    Compare X States (default)—Values of X in digital pattern match only to X states in the input    0      data.
    1 Ignore X States—Values of X in digital pattern are wildcards and match to any digital state.

   •       digital waveform out —

     digital waveform out returns digital waveform in unchanged.

   •      index/time of pattern —

    index/time of pattern is the first index or time value in digital waveform in following start
    index/time that matches the location of digital pattern.

       If indexing mode is set to Relative Time, index/time of pattern represents the time. If indexing
   mode is set to Samples, index/time of pattern represents the index.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Digital Waveform Graph\Search Digital Data for
   Pattern.vi
DTblDTbl SearchSearch forfor DigitalDigital PatternPattern VIVI

Searches for a digital pattern in the digital input. Wire data to the digital waveform in

                                                    © National Instruments 1355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1356 ordinal=1356 -->
## Functions

Functions

       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       digital data in —

              digital data in is the input set of digital data.

               •       digital pattern —

              digital pattern specifies the digital pattern for which you want to search.

            For example, if you acquire a large digital waveform and want to see if any part of the digital
           waveform matches a certain pattern, wire that pattern to the digital pattern input to discover
           any matches.

               •       start index —

              start index specifies the point in digital data in where the search begins. The default is 0, which
                is the beginning of digital data in. The VI returns an error if start index is out of range for digital
           data in.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •     compare mode —

          compare mode specifies how to handle values of X for the search.

           Compare X States (default)—Values of X in digital pattern match only to X states in the input
           0
              data.
           1 Ignore X States—Values of X in digital pattern are wildcards and match to any digital state.


1356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1357 ordinal=1357 -->
## Functions

Functions

   •       digital data out —

     digital data out returns digital data in unchanged.

   •      index of pattern —

    index of pattern returns the first index in digital data in following start index that matches the
    location of digital pattern.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Digital Waveform Graph\Search Digital Data for
   Pattern.vi

AppendAppend DigitalDigital SignalsSignals

Appends the signals from digital waveform (low bits) to the LSB side of digital
waveform (high bits). If the sampling rates do not match, error out returns a warning.
The start time of digital waveform (low bits) is ignored. Wire data to the digital
waveform (high bits) input to determine the polymorphic instance to use or manually
select the instance.


  • DWDT Append Digital Signals VI
  • DTbl Append Digital Signals VI

Use the Append Digital Signals VI to append the signals from two separate digital
waveforms into a single digital waveform. You can append signals with the same
number of samples or of different numbers of samples. For example, if you have two
digital signals that both consist of two rows of 8 bits, the resulting digital data consists

                                                    © National Instruments 1357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1358 ordinal=1358 -->
## Functions

Functions

       of two rows of 16 bits. If you combine two signals, one that consists of two rows of 8
        bits and the other that consists of one row of 8 bits, the resulting digital data consists
       of two rows of 16 bits. The Append Digital Signals VI pads the remaining columns in the
      second sample with the value you select in the default value input.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Digital Waveform Graph\Append Digital Data By
        Signal.vi
  DWDTDWDT AppendAppend DigitalDigital SignalsSignals VIVI

      Appends the signals from digital waveform (low bits) to the LSB side of digital
      waveform (high bits). If the sampling rates do not match, error out returns a warning.
      The start time of digital waveform (low bits) is ignored. Wire data to the digital
      waveform (high bits) input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •       default value —

             default value specifies the value to use to fill in the extra samples of the digital data in digital
          waveform out if digital waveform (low bits) and digital waveform (high bits) do not have the
          same number of samples.

           0   0 (default)—Force Down
           1   1—Force Up
           2   Z—Force Z


1358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1359 ordinal=1359 -->
## Functions

Functions


    3   L—Compare Low
    4   H—Compare High
    5   X—Compare Don't Care
    6   T—Compare Invalid
    7   V—Compare Valid

   •       digital waveform (high bits) —

     digital waveform (high bits) is the first set of data in the digital waveform.

   •       digital waveform (low bits) —

     digital waveform (low bits) is the set of data to append to digital waveform (high bits).

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital waveform out —

     digital waveform out returns the waveform that results from appending digital waveform (low
     bits) to digital waveform (high bits). This output matches the compression of the input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the Append Digital Signals VI to append the signals from two separate digital
waveforms into a single digital waveform. You can append signals with the same
number of samples or of different numbers of samples. For example, if you have two
digital signals that both consist of two rows of 8 bits, the resulting digital data consists
of two rows of 16 bits. If you combine two signals, one that consists of two rows of 8
bits and the other that consists of one row of 8 bits, the resulting digital data consists
of two rows of 16 bits. The Append Digital Signals VI pads the remaining columns in the
second sample with the value you select in the default value input.


                                                    © National Instruments 1359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1360 ordinal=1360 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Digital Waveform Graph\Append Digital Data By
        Signal.vi
   DTblDTbl AppendAppend DigitalDigital SignalsSignals VIVI

      Appends the signals from digital waveform (low bits) to the LSB side of digital
      waveform (high bits). If the sampling rates do not match, error out returns a warning.
      The start time of digital waveform (low bits) is ignored. Wire data to the digital
      waveform (high bits) input to determine the polymorphic instance to use or manually
        select the instance.

           Note Appends signals of digital data B to the LSB side of digital data A. If the
            number of samples do not match, error out returns a warning. The number
               of signals do not have to be the same.


      Inputs/Outputs

               •       default value —

             default value specifies the value to use to fill in the extra samples of the digital data in digital
          waveform out if digital waveform (low bits) and digital waveform (high bits) do not have the
          same number of samples.

           0   0 (default)—Force Down
           1   1—Force Up
           2   Z—Force Z


1360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1361 ordinal=1361 -->
## Functions

Functions


    3   L—Compare Low
    4   H—Compare High
    5   X—Compare Don't Care
    6   T—Compare Invalid
    7   V—Compare Valid

   •       digital data (high bits) —

     digital data (high bits) is the first set of data.

   •       digital data (low bits) —

     digital data (low bits) is the set of data to append to digital data (high bits).

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital data out —

     digital data out returns the digital data that results from appending digital data (low bits) to
     digital data (high bits).

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the Append Digital Signals VI to append the signals from two separate digital
waveforms into a single digital waveform. You can append signals with the same
number of samples or of different numbers of samples. For example, if you have two
digital signals that both consist of two rows of 8 bits, the resulting digital data consists
of two rows of 16 bits. If you combine two signals, one that consists of two rows of 8
bits and the other that consists of one row of 8 bits, the resulting digital data consists
of two rows of 16 bits. The Append Digital Signals VI pads the remaining columns in the
second sample with the value you select in the default value input.


                                                    © National Instruments 1361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1362 ordinal=1362 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Digital Waveform Graph\Append Digital Data By
        Signal.vi

     AppendAppend DigitalDigital SamplesSamples

      Appends all samples from digital waveform B to the end of digital waveform A. If the
      sampling rates do not match, error out returns a warning. The start time of digital
      waveform B is ignored. Wire data to the digital waveform A input to determine the
      polymorphic instance to use or manually select the instance.


            • DWDT Append Digital Samples VI
            • DTbl Append Digital Samples VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Digital Waveform Graph\Append Digital Data By
        Sample.vi
  DWDTDWDT AppendAppend DigitalDigital SamplesSamples VIVI

      Appends all samples from digital waveform B to the end of digital waveform A. If the
      sampling rates do not match, error out returns a warning. The start time of digital
      waveform B is ignored. Wire data to the digital waveform A input to determine the
      polymorphic instance to use or manually select the instance.


1362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1363 ordinal=1363 -->
## Functions

Functions


Inputs/Outputs

   •       default value —

    default value specifies the value to use to fill in the extra signals of the digital data in digital
    waveform out if digital waveform A and digital waveform B do not have the same number of
     signals.

    0   0 (default)—Force Down
    1   1—Force Up
    2   Z—Force Z
    3   L—Compare Low
    4   H—Compare High
    5   X—Compare Don't Care
    6   T—Compare Invalid
    7   V—Compare Valid

   •       digital waveform A —

     digital waveform A is the first set of data in the digital waveform.

   •       digital waveform B —

     digital waveform B is the set of data to append to digital waveform A.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital waveform out —

     digital waveform out returns the waveform that results from appending digital waveform (low
     bits) to digital waveform (high bits). This output matches the compression of the input.

   •       error out —


                                                    © National Instruments 1363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1364 ordinal=1364 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Digital Waveform Graph\Append Digital Data By
        Sample.vi
   DTblDTbl AppendAppend DigitalDigital SamplesSamples VIVI

      Appends all samples from digital waveform B to the end of digital waveform A. If the
      sampling rates do not match, error out returns a warning. The start time of digital
      waveform B is ignored. Wire data to the digital waveform A input to determine the
      polymorphic instance to use or manually select the instance.

           Note

            Appends all samples from digital data B to the end of digital data A. If the
            number of signals do not match, error out returns a warning. The number of
             samples do not have to be the same.


      Inputs/Outputs

               •       default value —

             default value specifies the value to fill in the extra signals of digital data out if digital data A and
              digital data B do not have the same number of signals.


1364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1365 ordinal=1365 -->
## Functions

Functions


    0   0 (default)—Force Down
    1   1—Force Up
    2   Z—Force Z
    3   L—Compare Low
    4   H—Compare High
    5   X—Compare Don't Care
    6   T—Compare Invalid
    7   V—Compare Valid

   •       digital data A —

     digital data A is the first set of data.

   •       digital data B —

     digital data B is the set of data to append to digital data A.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital data out —

     digital data out returns the digital data that results from appending digital data (low bits) to
     digital data (high bits).

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Digital Waveform Graph\Append Digital Data By
   Sample.vi


                                                    © National Instruments 1365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1366 ordinal=1366 -->
## Functions

Functions

       InvertInvert DigitalDigital

       Inverts the digital data in the digital input so that a 0 becomes a 1 and vice versa or an
     H becomes an L and vice versa. Wire data to the digital waveform input to determine
       the polymorphic instance to use or manually select the instance.


            • DWDT Invert Digital VI
            • DTbl Invert Digital VI
  DWDTDWDT InvertInvert DigitalDigital VIVI

       Inverts the digital data in the digital input so that a 0 becomes a 1 and vice versa or an
     H becomes an L and vice versa. Wire data to the digital waveform input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       digital waveform —

              digital waveform is the input digital waveform.

               •      response to invert error —

           response to invert error specifies what to do if any value in the digital input is not a 0, 1, H, or L.

           Warn but Convert (default)—Any values that are not 0, 1, H, or L are left unchanged and a           0
            warning is returned in error out.
           1 Fail—The VI returns an empty inverted digital output and returns an error in error out.

               •       error in (no error) —

1366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1367 ordinal=1367 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       signal index (0) —

    signal index specifies the signal at which to begin inverting data. The default is 0, which inverts
      all signals.

   •     number of signals (-1:all) —

   number of signals specifies the number of signals to invert, beginning with the signal at signal
    index.

   •      inverted waveform —

    inverted waveform contains the inverted waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DTblDTbl InvertInvert DigitalDigital VIVI

Inverts the digital data in the digital input so that a 0 becomes a 1 and vice versa or an
H becomes an L and vice versa. Wire data to the digital waveform input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       digital data —


                                                    © National Instruments 1367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1368 ordinal=1368 -->
## Functions

Functions


              digital data is the set of input digital data.

               •      response to invert error —

           response to invert error specifies what to do if any value in the digital input is not a 0, 1, H, or L.

           Warn but Convert (default)—Any values that are not 0, 1, H, or L are left unchanged and a           0
            warning is returned in error out.
           1 Fail—The VI returns an empty inverted digital output and returns an error in error out.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       signal index (0) —

             signal index specifies the signal at which to begin inverting data. The default is 0, which inverts
                all signals.

               •     number of signals (-1:all) —

          number of signals specifies the number of signals to invert, beginning with the signal at signal
             index.

               •      inverted digital data —

            inverted digital data contains the inverted digital data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     GroupGroup DigitalDigital SignalsSignals

      Groups digital data into a digital data array and groups digital waveforms into a digital
      waveform array.

      LabVIEW treats ungrouped signals as individual groups.

1368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1369 ordinal=1369 -->
## Functions

Functions


Dialog Box Options

 Option     Description

             Specifies the number of signals you want to wire to the Express VI. Configure this option
                 first. Number
 of signals            This number must match the number of signals you wire to Digital Data In. Otherwise,
          LabVIEW returns an error.


 Use            Allows you to retain the original names of the waveforms you wire to Digital Data In. incoming
            This checkbox contains a checkmark by default. Remove the checkmark from this waveform           checkbox to use the line and bus names you specify using the Rename button. names

 Order of            Displays the sequential order of the digital signals.
 signals


            Contains the lines and buses you configure in the configuration dialog box.

 Plot      Use this tree control to drag and drop lines into the order you want to view them in the
 Legend    output array. To put lines into groups, right-click a line and select Insert Bus and then
           drag other lines onto that bus. You cannot drag a line onto another line, a bus onto
           another bus, or a bus onto a line.


 Graph      Displays a preview of the lines and buses based on the organization you specify in the
 Preview    configuration dialog box.


 Rename   Allows you to rename the line or bus you select in the Plot Legend tree control. You also


                                                    © National Instruments 1369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1370 ordinal=1370 -->
## Functions

Functions


        Option     Description

                  can right-click a line or bus and select Rename from the shortcut menu or double-click
                  a line or bus to type a new name.

                  To rename lines or buses, you must remove the checkmark from the Use incoming
                 waveform names checkbox. Otherwise, the incoming line names take precedence over
                   the new names you specify.


                      Inserts a new bus above the line or bus you select in the Plot Legend tree control. You         Insert Bus                     also can right-click a line or bus and select Insert Bus from the shortcut menu.


                    Deletes all the buses from the Plot Legend tree control.
         Delete All                  To delete a single bus, right-click the bus and select Delete Bus from the shortcut
        Buses                 menu. You can delete only buses, not lines. LabVIEW considers lines listed under
                    deleted buses as ungrouped signals.


      Inputs/Outputs

               •       error in (no error) —
            Describes error conditions that occur before this node runs.
               •       Digital Data In —
             Specifies the input signals you want to organize into groups.
               •       error out —
            Contains error information. This output provides standard error out functionality.
               •       Digital Data Out —
            Returns a digital data array or a digital waveform array, depending on the data type of Digital
           Data In.

       DigitalDigital RingRing ConstantConstant

      Use the digital ring constant to set the digital bit state of a digital waveform or digital
       data.

      You select, add or remove, and rearrange values in ring constants much the same way
      you do for ring and enumerated controls.


1370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1371 ordinal=1371 -->
## Functions

Functions

The digital ring constant includes a predefined list of the eight digital states supported
by the digital waveform and digital data type:


 Digital             Description Data State

 0 (Force             Force logic low. Drive to the low voltage level (VIL). Down)

 1 (Force             Force logic high. Drive to the high voltage level (VIH). Up)

 Z (Force             Force logic high impedance. Turn the driver off. Off)

 L (Compare Compare logic low (edge). Compare for a voltage level lower than the low voltage
 Low)        threshold (VOL).

 H
           Compare logic high (edge). Compare for a voltage level higher than the high voltage (Compare             threshold (VOH). High)

 X (Compare           Compare logic unknown. Do not compare. Unknown)

 T           Compare logic high impedance (edge). Compare for a voltage level between the low
 (Compare             voltage threshold (VOL) and the high voltage threshold (VOH). Off)

 V (Compare Compare logic valid level (edge). Compare for a voltage level either lower than the low
 Valid)       voltage threshold (VOL) or higher than the high voltage threshold (VOH).

You can change the representation of a ring constant to any digital state you want to
use.


EmptyEmpty DigitalDigital WaveformWaveform

Returns an empty digital waveform. Use this constant to initialize shift registers or
build digital waveforms.


                                                    © National Instruments 1371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1372 ordinal=1372 -->
## Functions

Functions


      Inputs/Outputs

               •       digital waveform out —

              digital waveform out returns an empty digital waveform.


     EmptyEmpty DigitalDigital DataData

       Returns empty digital data. Use this constant to initialize shift registers or build digital
        tables.


      Inputs/Outputs

               •       digital data —

              digital data returns empty digital data.


       DigitalDigital ConversionConversion

      Use the Digital Conversion VIs and Functions to convert to and from digital data.

      The VIs on this palette can return waveform error codes.


1372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1373 ordinal=1373 -->
## Functions

Functions


 Palette              Description
 Object

 Boolean              Converts a 2D Boolean array to a digital waveform or digital data. You must manually Array to               select the polymorphic instance you want to use. Digital


 Binary to     Converts a binary array of unsigned integers to a digital waveform or set of digital
 Digital        data. You must manually select the polymorphic instance you want to use.


 Spreadsheet
              Converts a spreadsheet string to a digital waveform or set of digital data. You must String to             manually select the polymorphic instance you want to use. Digital


 Digital to     Converts the digital waveform or digital data in the digital input to a 2D Boolean
 Boolean      array. Wire data to the digital waveform input to determine the polymorphic
 Array         instance to use or manually select the instance.


 Digital to     Converts a digital waveform or set of digital data to a binary array of unsigned
 Binary        integers. You must manually select the polymorphic instance you want to use.

BooleanBoolean ArrayArray toto DigitalDigital

Converts a 2D Boolean array to a digital waveform or digital data. You must manually
select the polymorphic instance you want to use.


  • DWDT Boolean Array to Digital VI
  • DTbl Boolean Array to Digital VI


                                                    © National Instruments 1373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1374 ordinal=1374 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Digital Waveform Graph\Search Digital Data for
        Pattern.vi
  DWDTDWDT BooleanBoolean ArrayArray toto DigitalDigital VIVI

       Converts a 2D Boolean array to a digital waveform or digital data. You must manually
        select the polymorphic instance you want to use.


      Inputs/Outputs

               •      compress data (F) —

           compress data specifies whether to compress the digital output. The default is FALSE.

               •      boolean array —

           boolean array is the 2D Boolean array you want to convert to digital waveform.

               •     sample rate —

           sample rate specifies the frequency in samples per second of the output digital waveform.

               •     mode —

         mode specifies whether the conversion is performed on the data with the least significant bit
             (LSB) first or most significant bit (MSB) first. The order of the digital data in digital waveform
              reflects the selection made in mode.


1374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1375 ordinal=1375 -->
## Functions

Functions


             LSB First    0
                 (default)
    1       MSB First

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       digital waveform —

     digital waveform returns the waveform resulting from the conversion of boolean array.

    The order of the digital data in digital waveform reflects the bit direction selected in mode.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Digital Waveform Graph\Search Digital Data for
   Pattern.vi
DTblDTbl BooleanBoolean ArrayArray toto DigitalDigital VIVI

Converts a 2D Boolean array to a digital waveform or digital data. You must manually
select the polymorphic instance you want to use.


                                                    © National Instruments 1375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1376 ordinal=1376 -->
## Functions

Functions

      Inputs/Outputs

               •      compress data (F) —

           compress data specifies whether to compress the digital output. The default is FALSE.

               •      boolean array —

           boolean array is the 2D Boolean array you want to convert to digital data.

               •     mode —

         mode specifies whether the conversion is performed on the data with least significant bit (LSB)
                 first or most significant bit (MSB) first. The order of the digital data in digital data reflects the
             selection made in mode.

                    LSB First           0
                          (default)
           1       MSB First

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       digital data —

              digital data returns the digital data resulting from the conversion of boolean array.

          The order of the digital data reflects the bit direction selected in mode.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and

1376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1377 ordinal=1377 -->
## Functions

Functions

   Charts\Digital Waveform Graph\Search Digital Data for
   Pattern.vi
BinaryBinary toto DigitalDigital

Converts a binary array of unsigned integers to a digital waveform or set of digital data.
You must manually select the polymorphic instance you want to use.


  • DWDT Binary U32 to Digital VI
  • DTbl Binary U32 to Digital VI
  • DWDT Binary U16 to Digital VI
  • DTbl Binary U16 to Digital VI
  • DWDT Binary U8 to Digital VI
  • DTbl Binary U8 to Digital VI
DWDTDWDT BinaryBinary U32U32 toto DigitalDigital VIVI

Converts a binary array of unsigned integers to a digital waveform or set of digital data.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      compress data (T) —

    compress data specifies whether to compress the digital output. The default is TRUE.

   •      binary array —

    binary array is the 1D array of unsigned 32-bit integers you want to convert to a digital


                                                    © National Instruments 1377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1378 ordinal=1378 -->
## Functions

Functions


           waveform or set of digital data.

               •     sample rate —

           sample rate specifies the frequency in samples per second of the output digital waveform.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digital waveform —

              digital waveform returns the converted digital waveform.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   DTblDTbl BinaryBinary U32U32 toto DigitalDigital VIVI

       Converts a binary array of unsigned integers to a digital waveform or set of digital data.
      You must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      compress data (T) —

           compress data specifies whether to compress the digital output. The default is TRUE.

               •      binary array —

            binary array is the 1D array of unsigned 32-bit integers you want to convert to a digital
           waveform or set of digital data.

               •       error in (no error) —

1378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1379 ordinal=1379 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digital data —

     digital data returns the converted set of digital data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DWDTDWDT BinaryBinary U16U16 toto DigitalDigital VIVI

Converts a binary array of unsigned integers to a digital waveform or set of digital data.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      compress data (T) —

    compress data specifies whether to compress the digital output. The default is TRUE.

   •      binary array —

    binary array is the 1D array of unsigned 16-bit integers you want to convert to a digital
    waveform or set of digital data.

   •     sample rate —

    sample rate specifies the frequency in samples per second of the output digital waveform.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 1379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1380 ordinal=1380 -->
## Functions

Functions


            standard error in functionality.

               •       digital waveform —

              digital waveform returns the converted digital waveform.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   DTblDTbl BinaryBinary U16U16 toto DigitalDigital VIVI

       Converts a binary array of unsigned integers to a digital waveform or set of digital data.
      You must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      compress data (T) —

           compress data specifies whether to compress the digital output. The default is TRUE.

               •      binary array —

            binary array is the 1D array of unsigned 16-bit integers you want to convert to a digital
           waveform or set of digital data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digital data —

              digital data returns the converted set of digital data.

               •       error out —

1380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1381 ordinal=1381 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

DWDTDWDT BinaryBinary U8U8 toto DigitalDigital VIVI

Converts a binary array of unsigned integers to a digital waveform or set of digital data.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      compress data (T) —

    compress data specifies whether to compress the digital output. The default is TRUE.

   •      binary array —

    binary array is the 1D array of unsigned 8-bit integers you want to convert to a digital waveform
    or set of digital data.

   •     sample rate —

    sample rate specifies the frequency in samples per second of the output digital waveform.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       digital waveform —

     digital waveform returns the converted digital waveform.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1382 ordinal=1382 -->
## Functions

Functions

   DTblDTbl BinaryBinary U8U8 toto DigitalDigital VIVI

       Converts a binary array of unsigned integers to a digital waveform or set of digital data.
      You must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •      compress data (T) —

           compress data specifies whether to compress the digital output. The default is TRUE.

               •      binary array —

            binary array is the 1D array of unsigned 8-bit integers you want to convert to a digital waveform
            or set of digital data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       digital data —

              digital data returns the converted set of digital data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SpreadsheetSpreadsheet StringString toto DigitalDigital

       Converts a spreadsheet string to a digital waveform or set of digital data. You must
      manually select the polymorphic instance you want to use.


1382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1383 ordinal=1383 -->
## Functions

Functions


  • DWDT Spreadsheet String to Digital VI
  • DTbl Spreadsheet String to Digital VI
DWDTDWDT SpreadsheetSpreadsheet StringString toto DigitalDigital VIVI

Converts a spreadsheet string to a digital waveform or set of digital data. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      compress data (T) —

    compress data specifies whether to compress the digital output. The default is TRUE.

   •      spreadsheet string —

    spreadsheet string contains numeric or string values separated into columns by delimiters, such
    as tabs or commas, with an end-of-line (EOL) character separating rows. spreadsheet string
    should be a delimited list of ASCII characters representing the 8 supported digital data states,
   shown in the following table.

           Digital
    Value           Description
         Data State
         0 (Drive
    0               Force logic low. Drive to the low voltage level (VOL).         Low)
         1 (Drive
    1               Force logic high. Drive to the high voltage level (VOH).          High)
        Z (Force
    2               Force logic high impedance. Turn the driver off.
           Off)


                                                    © National Instruments 1383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1384 ordinal=1384 -->
## Functions

Functions


                    Digital            Value           Description
                Data State
                L                       Compare logic low (edge). Compare for a voltage level lower than the low           3    (Compare                             voltage threshold.                Low)
            H                       Compare logic high (edge). Compare for a voltage level higher than the high
           4    (Compare
                             voltage threshold (VOH).                  High)
               X
           5    (Compare Compare logic unknown. Do not compare.
               Unknown)
               T                       Compare logic high impedance (edge). Compare for a voltage level between
           6    (Compare
                            the low voltage threshold (VOL) and the high voltage threshold (VOH).                    Off)
               V                       Compare logic valid level (edge). Compare for a voltage level either lower than
           7    (Compare
                            the low voltage threshold (VOL) or higher than the high voltage threshold (VOH).                    Valid)

               •       delimiter (tab) —

             delimiter is the value or values used to separate fields in the spreadsheet file. The default is a
             single tab character.

               •     sample rate —

           sample rate specifies the frequency in samples per second of the output digital waveform.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      position first column —

            position first column specifies whether the first column from spreadsheet string represents the
              least significant bit (LSB) or most significant bit (MSB) of the waveform.

               •       digital waveform —

              digital waveform returns the converted digital waveform.

               •       error out —


1384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1385 ordinal=1385 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

DTblDTbl SpreadsheetSpreadsheet StringString toto DigitalDigital VIVI

Converts a spreadsheet string to a digital waveform or set of digital data. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •      compress data (T) —

    compress data specifies whether to compress the digital output. The default is TRUE.

   •      spreadsheet string —

    spreadsheet string contains numeric or string values separated into columns by delimiters, such
    as tabs or commas, with an end-of-line (EOL) character separating rows. spreadsheet string
    should be a delimited list of ASCII characters representing the 8 supported digital data states,
   shown in the following table.

           Digital
    Value           Description
         Data State
         0 (Drive
    0               Force logic low. Drive to the low voltage level (VOL).         Low)
         1 (Drive
    1               Force logic high. Drive to the high voltage level (VOH).          High)
        Z (Force
    2               Force logic high impedance. Turn the driver off.
           Off)
         L
                 Compare logic low (edge). Compare for a voltage level lower than the low
    3    (Compare
                     voltage threshold.
         Low)
    4   H        Compare logic high (edge). Compare for a voltage level higher than the high


                                                    © National Instruments 1385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1386 ordinal=1386 -->
## Functions

Functions


                    Digital            Value           Description
                Data State
               (Compare
                             voltage threshold (VOH).                  High)
               X
           5    (Compare Compare logic unknown. Do not compare.
               Unknown)
               T                       Compare logic high impedance (edge). Compare for a voltage level between
           6    (Compare
                            the low voltage threshold (VOL) and the high voltage threshold (VOH).                    Off)
               V                       Compare logic valid level (edge). Compare for a voltage level either lower than
           7    (Compare
                            the low voltage threshold (VOL) or higher than the high voltage threshold (VOH).                    Valid)

               •       delimiter (tab) —

             delimiter is the value or values used to separate fields in the spreadsheet file. The default is a
             single tab character.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      position first column —

            position first column specifies whether the first column from spreadsheet string represents the
              least significant bit (LSB) or most significant bit (MSB) of the waveform.

               •       digital data —

              digital data returns the converted set of digital data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    DigitalDigital toto BooleanBoolean ArrayArray

       Converts the digital waveform or digital data in the digital input to a 2D Boolean array.


1386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1387 ordinal=1387 -->
## Functions

Functions

Wire data to the digital waveform input to determine the polymorphic instance to use
or manually select the instance.


  • DWDT Digital to Boolean Array VI
  • DTbl Digital to Boolean Array VI
DWDTDWDT DigitalDigital toto BooleanBoolean ArrayArray VIVI

Converts the digital waveform or digital data in the digital input to a 2D Boolean array.
Wire data to the digital waveform input to determine the polymorphic instance to use
or manually select the instance.


Inputs/Outputs

   •       digital waveform —

     digital waveform is the input digital waveform.

   •      response on error —

    response on error specifies what to do if any value in the digital input is not a 0, 1, H, or L.

    Warn but Convert (default)—Any values that are not 0, 1, H, or L are converted to FALSE and a    0
     warning is returned in error out.
    1 Fail—boolean array is returned empty and an error is returned in error out.

   •     mode —

   mode specifies whether the conversion is performed on the data with the least significant bit
    (LSB) first or most significant bit (MSB) first. The order of the Boolean values in boolean array


                                                    © National Instruments 1387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1388 ordinal=1388 -->
## Functions

Functions


              reflects the selection made in mode.

                    LSB First
           0                          (default)
           1       MSB First

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •      boolean array —

           boolean array returns the converted Boolean array. The order of the Boolean values in boolean
            array reflects the bit direction selected in mode.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   DTblDTbl DigitalDigital toto BooleanBoolean ArrayArray VIVI

       Converts the digital waveform or digital data in the digital input to a 2D Boolean array.
       Wire data to the digital waveform input to determine the polymorphic instance to use
       or manually select the instance.


      Inputs/Outputs

               •       digital data —

              digital data is the set of input digital data.


1388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1389 ordinal=1389 -->
## Functions

Functions

   •      response on error —

    response on error specifies what to do if any value in the digital input is not a 0, 1, H, or L.

    Warn but Convert (default)—Any values that are not 0, 1, H, or L are converted to FALSE and a    0
     warning is returned in error out.
    1 Fail—boolean array is returned empty and an error is returned in error out.

   •     mode —

   mode specifies whether the conversion is performed on the data with the least significant bit
    (LSB) first or most significant bit (MSB) first. The order of the Boolean values in boolean array
     reflects the selection made in mode.

             LSB First    0                 (default)
    1       MSB First

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      boolean array —

    boolean array returns the converted Boolean array. The order of the Boolean values in boolean
    array reflects the bit direction selected in mode.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DigitalDigital toto BinaryBinary

Converts a digital waveform or set of digital data to a binary array of unsigned integers.
You must manually select the polymorphic instance you want to use.


                                                    © National Instruments 1389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1390 ordinal=1390 -->
## Functions

Functions


            • DWDT Digital to Binary U32 VI
            • DTbl Digital to Binary U32 VI
            • DWDT Digital to Binary U16 VI
            • DTbl Digital to Binary U16 VI
            • DWDT Digital to Binary U8 VI
            • DTbl Digital to Binary U8 VI
  DWDTDWDT DigitalDigital toto BinaryBinary U32U32 VIVI

       Converts a digital waveform or set of digital data to a binary array of unsigned integers.
      You must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •       digital waveform —

              digital waveform is the input digital waveform.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      binary array —

            binary array is the array resulting from the conversion of the digital input.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1391 ordinal=1391 -->
## Functions

Functions

DTblDTbl DigitalDigital toto BinaryBinary U32U32 VIVI

Converts a digital waveform or set of digital data to a binary array of unsigned integers.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •       digital data —

     digital data is the set of input digital data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      binary array —

    binary array is the array resulting from the conversion of the digital input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DWDTDWDT DigitalDigital toto BinaryBinary U16U16 VIVI

Converts a digital waveform or set of digital data to a binary array of unsigned integers.
You must manually select the polymorphic instance you want to use.


                                                    © National Instruments 1391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1392 ordinal=1392 -->
## Functions

Functions

      Inputs/Outputs

               •       digital waveform —

              digital waveform is the input digital waveform.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      binary array —

            binary array is the array resulting from the conversion of the digital input.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   DTblDTbl DigitalDigital toto BinaryBinary U16U16 VIVI

       Converts a digital waveform or set of digital data to a binary array of unsigned integers.
      You must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •       digital data —

              digital data is the set of input digital data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      binary array —


1392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1393 ordinal=1393 -->
## Functions

Functions


    binary array is the array resulting from the conversion of the digital input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DWDTDWDT DigitalDigital toto BinaryBinary U8U8 VIVI

Converts a digital waveform or set of digital data to a binary array of unsigned integers.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •       digital waveform —

     digital waveform is the input digital waveform.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      binary array —

    binary array is the array resulting from the conversion of the digital input.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DTblDTbl DigitalDigital toto BinaryBinary U8U8 VIVI

Converts a digital waveform or set of digital data to a binary array of unsigned integers.


                                                    © National Instruments 1393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1394 ordinal=1394 -->
## Functions

Functions

      You must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •       digital data —

              digital data is the set of input digital data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      binary array —

            binary array is the array resulting from the conversion of the digital input.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     WaveformWaveform FileFile I/OI/O

      Use the Waveform File I/O VIs to write waveform data to and read waveform data from
         files.

      The VIs on this palette can return waveform error codes.


         Palette
                      Description
        Object

         Write
        Waveforms   Creates a new file or appends to an existing file, writes the specified number of
         to File

1394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1395 ordinal=1395 -->
## Functions

Functions


 Palette              Description
 Object

              records to the file, then closes the file and checks for errors. Each record is an array of
             waveforms. Wire data to the Waveform input to determine the polymorphic instance
               to use or manually select the instance.


 Read       Opens a file created with the Write Waveforms to File VI and reads one record of the
 Waveforms    file. Each record might contain one or more separate waveforms. To retrieve all
 from File     records in the file, call this VI in a loop until the end of the file is reached.

 Export
 Waveforms   Converts a waveform to a text string and writes the string to a new byte stream file or
 to          appends the string to an existing file. Wire data to the waveforms input to determine
 Spreadsheet the polymorphic instance to use or manually select the instance.
 File

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Write Waveforms to
   File.vi

WriteWrite WaveformsWaveforms toto FileFile

Creates a new file or appends to an existing file, writes the specified number of records
to the file, then closes the file and checks for errors. Each record is an array of
waveforms. Wire data to the Waveform input to determine the polymorphic instance
to use or manually select the instance.

You can use any file extension, for example .dat or .txt, for the file you write the
waveform data to.


                                                    © National Instruments 1395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1396 ordinal=1396 -->
## Functions

Functions

            • Write Waveform to File VI
            • Write Waveforms to File (1D) VI
            • Write Waveforms to File (2D) VI
            • Write Waveform to File (Digital) VI
    WriteWrite WaveformWaveform toto FileFile VIVI

       Creates a new file or appends to an existing file, writes the specified number of records
       to the file, then closes the file and checks for errors. Each record is an array of
      waveforms. Wire data to the Waveform input to determine the polymorphic instance
       to use or manually select the instance.

      You can use any file extension, for example .dat or .txt, for the file you write the
      waveform data to.


      Inputs/Outputs

               •        file path (dialog if empty) —

                file path specifies the file where the waveform is located. If you do not wire this input, LabVIEW
             displays a non-native file dialog box instead of a native file dialog box.

               •     waveform —

          waveform is the waveform you want to write to a file.

               •     append to file? (new file:F) —

          append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
              VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


1396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1397 ordinal=1397 -->
## Functions

Functions

   •     new file path (Not A Path if cancelled) —

   new file path returns the path to the file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WriteWrite WaveformsWaveforms toto FileFile (1D)(1D) VIVI

Creates a new file or appends to an existing file, writes the specified number of records
to the file, then closes the file and checks for errors. Each record is an array of
waveforms. Wire data to the Waveform input to determine the polymorphic instance
to use or manually select the instance.

You can use any file extension, for example .dat or .txt, for the file you write the
waveform data to.


Inputs/Outputs

   •        file path (dialog if empty) —

      file path specifies the file where the waveform is located. If you do not wire this input, LabVIEW
    displays a non-native file dialog box instead of a native file dialog box.

   •     waveform array —

    waveform array is a 1D array of the waveforms you want to write to a file.

   •     append to file? (new file:F) —

   append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
     VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

   •       error in (no error) —

                                                    © National Instruments 1397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1398 ordinal=1398 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     new file path (Not A Path if cancelled) —

         new file path returns the path to the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    WriteWrite WaveformsWaveforms toto FileFile (2D)(2D) VIVI

       Creates a new file or appends to an existing file, writes the specified number of records
       to the file, then closes the file and checks for errors. Each record is an array of
      waveforms. Wire data to the Waveform input to determine the polymorphic instance
       to use or manually select the instance.

      You can use any file extension, for example .dat or .txt, for the file you write the
      waveform data to.


      Inputs/Outputs

               •        file path (dialog if empty) —

                file path specifies the file where the waveform is located. If you do not wire this input, LabVIEW
             displays a non-native file dialog box instead of a native file dialog box.

               •     waveform array —

          waveform array is a 2D array of the waveforms you want to write to a file.

               •     append to file? (new file:F) —


1398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1399 ordinal=1399 -->
## Functions

Functions


   append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
     VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     new file path (Not A Path if cancelled) —

   new file path returns the path to the file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WriteWrite WaveformWaveform toto FileFile (Digital)(Digital) VIVI

Creates a new file or appends to an existing file, writes the specified number of records
to the file, then closes the file and checks for errors. Each record is an array of
waveforms. Wire data to the Waveform input to determine the polymorphic instance
to use or manually select the instance.

You can use any file extension, for example .dat or .txt, for the file you write the
waveform data to.


Inputs/Outputs

   •        file path (dialog if empty) —

      file path specifies the file where the waveform is located. If you do not wire this input, LabVIEW
    displays a non-native file dialog box instead of a native file dialog box.

   •     waveform —

                                                    © National Instruments 1399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1400 ordinal=1400 -->
## Functions

Functions


          waveform is the digital waveform you want to write to a file.

               •     append to file? (new file:F) —

          append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
              VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     new file path (Not A Path if cancelled) —

         new file path returns the path to the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     ReadRead WaveformsWaveforms fromfrom FileFile

      Opens a file created with the Write Waveforms to File VI and reads one record of the
          file. Each record might contain one or more separate waveforms. To retrieve all records
        in the file, call this VI in a loop until the end of the file is reached.

       This VI returns an end-of-file error in the error out output.


            • Read Waveform from File VI
            • Read Waveform from File (Digital) VI
   ReadRead WaveformWaveform fromfrom FileFile VIVI

      Opens a file created with the Write Waveforms to File VI and reads one record of the
          file. Each record might contain one or more separate waveforms. To retrieve all records

1400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1401 ordinal=1401 -->
## Functions

Functions

in the file, call this VI in a loop until the end of the file is reached.

This VI returns an end-of-file error in the error out output.


Inputs/Outputs

   •        file path (dialog if empty) —

      file path specifies the file where the waveform is located. If you do not wire this input, LabVIEW
    displays a non-native file dialog box instead of a native file dialog box.

   •       offset (records:0) —

     offset specifies in records which record to read from the file. The first record is 0. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     new file path (Not A Path if cancelled) —

   new file path returns the path to the file.

   •        first waveform in record —

      first waveform in record returns the data of the first waveform in the record.

   •        all waveforms in record —

     all waveforms in record returns the data from all waveforms in the record. If there is only one
    waveform in the record, this output is identical to first waveform in record.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 1401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1402 ordinal=1402 -->
## Functions

Functions

   ReadRead WaveformWaveform fromfrom FileFile (Digital)(Digital) VIVI

      Opens a file created with the Write Waveforms to File VI and reads one record of the
          file. Each record might contain one or more separate waveforms. To retrieve all records
        in the file, call this VI in a loop until the end of the file is reached.

       This VI returns an end-of-file error in the error out output.


      Inputs/Outputs

               •        file path (dialog if empty) —

                file path specifies the file where the waveform is located. If you do not wire this input, LabVIEW
             displays a non-native file dialog box instead of a native file dialog box.

               •       offset (records:0) —

             offset specifies in records which record to read from the file. The first record is 0. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     new file path (Not A Path if cancelled) —

         new file path returns the path to the file.

               •       digital waveform —

              digital waveform returns the data of the first waveform in the record.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


1402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1403 ordinal=1403 -->
## Functions

Functions

ExportExport WaveformsWaveforms toto SpreadsheetSpreadsheet FileFile

Converts a waveform to a text string and writes the string to a new byte stream file or
appends the string to an existing file. Wire data to the waveforms input to determine
the polymorphic instance to use or manually select the instance.


  • Export Waveforms To Spreadsheet File (1D) VI
  • Export Waveforms To Spreadsheet File (2D) VI
  • Export Waveform To Spreadsheet File VI
  • Export Waveforms To Spreadsheet File (Digital) VI

This VI opens or creates the file beforehand and closes it afterwards. You can use this VI
to create a text file readable by most spreadsheet applications.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Write Waveforms to
   File.vi
ExportExport WaveformsWaveforms ToTo SpreadsheetSpreadsheet FileFile (1D)(1D)
VIVI

Converts a waveform to a text string and writes the string to a new byte stream file or
appends the string to an existing file. Wire data to the waveforms input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1404 ordinal=1404 -->
## Functions

Functions


      Inputs/Outputs

               •       delimiter (Tab) —

             delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
            For example, a value of , specifies a single comma as the delimiter, and a carriage return
              specifies a new line as the delimiter. The default specifies a single tab character as the delimiter.
           You also can use backslash ('\') codes to specify a delimiter by right-clicking the string control or
            constant and selecting '\' Codes Display from the shortcut menu.

               •     prompt —

          prompt is the prompt of the file save dialog if the file path is empty.

          The default is Choose file to write.

               •        file path (dialog if empty) —

                file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
             displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
            box.

               •     waveforms —

          waveforms contains the waveforms to export to the spreadsheet file.

               •      multiple time columns? (single:F) —

                    If multiple time columns? is TRUE, the VI writes separate time columns for each separate
           channel written to the file. If multiple time columns? is FALSE (default), a single time column
            represents the same time range for all waveforms written to the file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


1404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1405 ordinal=1405 -->
## Functions

Functions

   •     append to file? (new file:F) —

   append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
     VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

   •      header? (write header:T) —

       If header? (write header:T) is TRUE (default), the VI prints column and row headings, which
    contain time and date information and labels for the data. If header? is FALSE, the VI does not
     print column and row headings.

   •     new file path (Not A Path if cancelled) —

   new file path (Not A Path if cancelled) is the path of the file to which the VI wrote data. You can
    use this output to determine the path of a file that you opened using a dialog box. new file path
      is <Not A Path> if you cancelled the dialog box.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI opens or creates the file beforehand and closes it afterwards. You can use this VI
to create a text file readable by most spreadsheet applications.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Write Waveforms to
   File.vi
ExportExport WaveformsWaveforms ToTo SpreadsheetSpreadsheet FileFile (2D)(2D)
VIVI

Converts a waveform to a text string and writes the string to a new byte stream file or
appends the string to an existing file. Wire data to the waveforms input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1406 ordinal=1406 -->
## Functions

Functions


      Inputs/Outputs

               •       delimiter (Tab) —

             delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
            For example, a value of , specifies a single comma as the delimiter. The default specifies a single
            tab character as the delimiter.

               •     prompt —

          prompt is the prompt of the file save dialog if the file path is empty.

               •        file path (dialog if empty) —

                file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
             displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
            box.

               •     waveforms —

          waveforms contains the waveforms to export to the spreadsheet file.

               •      multiple time columns? (single:F) —

                    If multiple time columns? is TRUE, the VI writes separate time columns for each separate
           channel written to the file. If multiple time columns? is FALSE (default), a single time column
            represents the same time range for all waveforms written to the file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     append to file? (new file:F) —


1406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1407 ordinal=1407 -->
## Functions

Functions


   append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
     VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

   •      header? (write header:T) —

       If header? (write header:T) is TRUE (default), the VI prints column and row headings, which
    contain time and date information and labels for the data. If header? is FALSE, the VI does not
     print column and row headings.

   •     new file path (Not A Path if cancelled) —

   new file path (Not A Path if cancelled) is the path of the file to which the VI wrote data. You can
    use this output to determine the path of a file that you opened using a dialog box. new file path
      is <Not A Path> if you cancelled the dialog box.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI opens or creates the file beforehand and closes it afterwards. You can use this VI
to create a text file readable by most spreadsheet applications.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Write Waveforms to
   File.vi
ExportExport WaveformWaveform ToTo SpreadsheetSpreadsheet FileFile VIVI

Converts a waveform to a text string and writes the string to a new byte stream file or
appends the string to an existing file. Wire data to the waveforms input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1408 ordinal=1408 -->
## Functions

Functions


      Inputs/Outputs

               •       delimiter (Tab) —

             delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
            For example, a value of , specifies a single comma as the delimiter, and a carriage return
              specifies a new line as the delimiter. The default specifies a single tab character as the delimiter.
           You also can use backslash ('\') codes to specify a delimiter by right-clicking the string control or
            constant and selecting '\' Codes Display from the shortcut menu.

               •     prompt —

          prompt is the prompt of the file save dialog if the file path is empty.

          The default is Choose file to write.

               •        file path (dialog if empty) —

                file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
             displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
            box.

               •     waveform —

          waveform is the waveform to export to the spreadsheet file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     append to file? (new file:F) —

          append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
              VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

               •      header? (write header:T) —


1408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1409 ordinal=1409 -->
## Functions

Functions


       If header? (write header:T) is TRUE (default), the VI prints column and row headings, which
    contain time and date information and labels for the data. If header? is FALSE, the VI does not
     print column and row headings.

   •     new file path (Not A Path if cancelled) —

   new file path (Not A Path if cancelled) is the path of the file to which the VI wrote data. You can
    use this output to determine the path of a file that you opened using a dialog box. new file path
      is <Not A Path> if you cancelled the dialog box.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI opens or creates the file beforehand and closes it afterwards. You can use this VI
to create a text file readable by most spreadsheet applications.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Write Waveforms to
   File.vi
ExportExport WaveformsWaveforms ToTo SpreadsheetSpreadsheet FileFile
(Digital)(Digital) VIVI

Converts a waveform to a text string and writes the string to a new byte stream file or
appends the string to an existing file. Wire data to the waveforms input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1410 ordinal=1410 -->
## Functions

Functions


      Inputs/Outputs

               •       delimiter (Tab) —

             delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
            For example, a value of , specifies a single comma as the delimiter, and a carriage return
              specifies a new line as the delimiter. The default specifies a single tab character as the delimiter.
           You also can use backslash ('\') codes to specify a delimiter by right-clicking the string control or
            constant and selecting '\' Codes Display from the shortcut menu.

               •     prompt —

          prompt is the prompt of the file save dialog if the file path is empty.

          The default is Choose file to write.

               •        file path (dialog if empty) —

                file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
             displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
            box.

               •       Digital Waveform —

              digital waveform is the input digital waveform.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     append to file? (new file:F) —

          append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
              VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

               •      header? (write header:T) —


1410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1411 ordinal=1411 -->
## Functions

Functions


       If header? (write header:T) is TRUE (default), the VI prints column and row headings, which
    contain time and date information and labels for the data. If header? is FALSE, the VI does not
     print column and row headings.

   •     new file path (Not A Path if cancelled) —

   new file path (Not A Path if cancelled) is the path of the file to which the VI wrote data. You can
    use this output to determine the path of a file that you opened using a dialog box. new file path
      is <Not A Path> if you cancelled the dialog box.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI opens or creates the file beforehand and closes it afterwards. You can use this VI
to create a text file readable by most spreadsheet applications.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Waveform\Waveform - Write Waveforms to
   File.vi

CollectionCollection

Use the Collection VIs and functions to manipulate collection data.


 Palette Object     Description

 Map             Use the Map VIs and functions to create and manipulate maps.


 Set              Use the Set VIs and functions to create and manipulate sets.


                                                    © National Instruments 1411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1412 ordinal=1412 -->
## Functions

Functions

    MapMap

      Use the Map VIs and functions to create and manipulate maps.


         Palette                     Description
        Object

                      Creates a map from the input key-value entries. For entries with duplicate keys, this         Build Map                      function includes only the last entry in the resulting map.

          Insert Into    Inserts a key and its associated value into a map. If the key is already included in the
       Map       map, this function replaces the original value of the key with the new associated
         Function     value.

       Remove
       From Map   Removes a key and its associated value from a map.
         Function

        Look In                   Checks whether a map includes an entry with the specified key and returns the       Map                      associated value of the key.
         Function

       Read Map
       Max & Min                     Returns the maximum and minimum keys in a map.        Keys
         Function

                     Represents a map on the block diagram. You cannot modify the embedded data in a
               map interactively or programmatically. You can update map data only as a whole
       Map
                    through operations such as writing to the map front panel terminal or right-clicking
        Constant
                     the map and selecting Data Operations>>Copy Data or Data Operations>>Paste
                      Data.

         Collection
         Size         Returns the number of elements or entries in a collection.
         Function

       Empty
         Collection?  Returns TRUE if the input collection contains zero elements or entries.
         Function


1412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1413 ordinal=1413 -->
## Functions

Functions


 Palette             Description
 Object

 Convert
 Map To      Places the code that you can use to convert a map to an array.
 Array

 In Place     Places an In Place Element structure on the block diagram with the Map Get / Replace
 Map Access  Value border node added.


            Use the Registration Map VIs to create and manipulate registration maps. A Registration               registration map is a map between a key and a set of elements with operations to Map               signal when clients register or unregister for one or more services.


BuildBuild MapMap

Creates a map from the input key-value entries. For entries with duplicate keys, this
function includes only the last entry in the resulting map.


Inputs/Outputs

   •      key —

    key specifies the key of the entry. This input accepts any data type. All the keys must be unique
    and of the same data type.

   •      value —

    value specifies the value of the entry. This input accepts any data type. All the values must be of
    the same data type.

   •    map —


                                                    © National Instruments 1413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1414 ordinal=1414 -->
## Functions

Functions


         map returns the resulting map.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Collections\Map Collection - Comparing
        Test Results.vi

       InsertInsert IntoInto MapMap FunctionFunction

        Inserts a key and its associated value into a map. If the key is already included in the
      map, this function replaces the original value of the key with the new associated value.


      Inputs/Outputs

               •    map in —

         map in specifies the map in which you want to insert a key-value entry. This input accepts a map
             of any data type. The default data type is a map of 32-bit signed integers.

               •      key —

           key specifies the key of the entry to insert into the map.

          The key must be of the same data type as the existing keys in the map.

               •      value —

            value specifies the value of the entry. This input must be of the same data type as the existing
            values in the map.

               •    map out —

         map out returns the map with the inserted entry.


1414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1415 ordinal=1415 -->
## Functions

Functions

   •      key already included? —

    key already included? returns whether map in already includes key. If key already included? is
    TRUE, this function replaces the associated value of key in map in with value and returns the
     resulting map in map out.

   •      value unchanged? —

    value unchanged? returns whether any values in the input map are updated after the insertion.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Collections\Map Collection - Comparing
   Test Results.vi

RemoveRemove FromFrom MapMap FunctionFunction

Removes a key and its associated value from a map.


Inputs/Outputs

   •    map in —

   map in specifies the map from which you want to remove an entry. This input accepts a map of
    any data type. The default data type is a map of 32-bit signed integers.

   •      key —

    key specifies the key of the entry to remove. This input must be of the same data type as the
     existing keys in the map.

   •    map out —

   map out returns the map with the entry of the specified key removed.


                                                    © National Instruments 1415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1416 ordinal=1416 -->
## Functions

Functions

               •      key not found? —

           key not found? returns whether map in includes an entry with the specified key.

               •      value —

            value returns the value of the entry associated with key.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Collections\Map Collection - Word
        Counting.vi

      LookLook InIn MapMap FunctionFunction

      Checks whether a map includes an entry with the specified key and returns the
       associated value of the key.


      Inputs/Outputs

               •    map —

         map specifies the map in which you want to look for a key. This input accepts a map of any data
             type. The default data type is a map of 32-bit signed integers.

               •      key —

           key specifies the key to look for in the map. The key must be of the same data type as the
              existing keys in the map.

               •       default value —

             default value specifies the value to return in value if the specified key does not exist in the map.
             This input must be of the same data type as the existing values in the map.


1416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1417 ordinal=1417 -->
## Functions

Functions

   •      key not found? —

    key not found? returns TRUE if map does not include an entry with the specified key. Otherwise,
    key not found? returns FALSE.

   •      value —

    value returns the value of the entry with the associated key if key not found? is FALSE. If key not
    found? is TRUE, this output returns the value in default value.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Collections\Map Collection - Comparing
   Test Results.vi
  • labview\examples\Design Patterns\Registration Map\
   Registration Map Usage.lvproj

ReadRead MapMap MaxMax && MinMin KeysKeys FunctionFunction

Returns the maximum and minimum keys in a map.


Inputs/Outputs

   •    map —

   map specifies the map in which you want to look for the maximum and minimum keys. This
    input accepts a map of any data type. The default data type is a map of 32-bit signed integers.

   •     maximum —

   maximum returns the maximum key in map.

   •     minimum —


                                                    © National Instruments 1417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1418 ordinal=1418 -->
## Functions

Functions


         minimum returns the minimum key in map.


     MapMap ConstantConstant

       Represents a map on the block diagram. You cannot modify the embedded data in a
     map interactively or programmatically. You can update map data only as a whole
      through operations such as writing to the map front panel terminal or right-clicking
       the map and selecting Data Operations>>Copy Data or Data Operations>>Paste Data.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Collections\Map Collection - Word
        Counting.vi

       CollectionCollection SizeSize FunctionFunction

       Returns the number of elements or entries in a collection.


      Inputs/Outputs

               •       collection —

             collection specifies the collection. This input accepts any collection data type.

               •       size —

             size returns the number of elements or entries in collection.


1418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1419 ordinal=1419 -->
## Functions

Functions

EmptyEmpty Collection?Collection? FunctionFunction

Returns TRUE if the input collection contains zero elements or entries.


Inputs/Outputs

   •       collection —

     collection specifies the collection. This input accepts any collection data type.

   •     empty? —

    empty? returns TRUE if collection is empty. Otherwise, this output returns FALSE.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Collections\Map Collection - Comparing
   Test Results.vi
  • labview\examples\Collections\Set Collection - Word
   Counting.vi
  • labview\examples\Design Patterns\Registration Map\
   Registration Map Usage.lvproj

ConvertConvert MapMap ToTo ArrayArray

Places the code that you can use to convert a map to an array.

When you add this VI to the block diagram, a For Loop displays. Wire a map to the
tunnel input and return an array through the tunnel output.


                                                    © National Instruments 1419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1420 ordinal=1420 -->
## Functions

Functions


       InIn PlacePlace MapMap AccessAccess

       Places an In Place Element structure on the block diagram with the Map Get / Replace
       Value border node added.


       RegistrationRegistration MapMap

      Use the Registration Map VIs to create and manipulate registration maps. A registration
     map is a map between a key and a set of elements with operations to signal when
        clients register or unregister for one or more services.


         Palette Object       Description

         Registration        Adds a set element in a registration map. This VI signals the calling VI if it is
         Map:Register         the first time any set element has registered for this key.


         Registration
                           Checks if a set element is registered for a key in a registration map. This VI
        Map:Confirm
                                signals the calling VI if the set element has registered for the key.
         Registration


         Registration        Removes an entry from a registration map. This VI signals the calling VI if the
         Map:Unregister       given element is the last element registered for this key.


1420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1421 ordinal=1421 -->
## Functions

Functions

RegistrationRegistration Map:RegisterMap:Register

Adds a set element in a registration map. This VI signals the calling VI if it is the first
time any set element has registered for this key.


Inputs/Outputs

   •    map in —

   map in specifies the registration map in which you want to insert an entry. This input accepts a
   map of sets of any data type. The default data type is a map of sets of 32-bit signed integers.

   •      key —

    key specifies the key. This input must be of the same data type as the existing keys in the map.

   •       set element —

    set element specifies the set element that may be registered for the specified key. This input
    must be of the same data type as the elements of the sets in the map.

   •    map out —

   map out returns the registration map with the inserted entry.

   •      element already registered? —

    element already registered? returns whether map in already includes set element.

   •        first registration for this key? —

      first registration for this key? returns whether this is the first time that the key is registered.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 1421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1422 ordinal=1422 -->
## Functions

Functions

            • labview\examples\Design Patterns\Registration Map\
        Registration Map Usage.lvproj
    RegistrationRegistration Map:ConfirmMap:Confirm RegistrationRegistration

      Checks if a set element is registered for a key in a registration map. This VI signals the
        calling VI if the set element has registered for the key.


      Inputs/Outputs

               •    map —

         map specifies the registration map in which you want to check for the registration status of a set
            element. This input accepts a map of sets of any data type. The default data type is a map of sets
             of 32-bit signed integers.

               •      key —

           key specifies the key. This input must be of the same data type as the existing keys in the map.

               •       set element —

             set element specifies the set element that may be registered for the specified key. This input
          must be of the same data type as the elements of the sets in the map.

               •        is element registered for key? —

                is element registered for key? returns whether the set element has been registered for the key.

    RegistrationRegistration Map:UnregisterMap:Unregister

      Removes an entry from a registration map. This VI signals the calling VI if the given
      element is the last element registered for this key.


1422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1423 ordinal=1423 -->
## Functions

Functions


Inputs/Outputs

   •    map in —

   map in specifies the registration map from which you want to remove an element. This input
    accepts a map of sets of any data type. The default data type is a map of sets of 32-bit signed
     integers.

   •      key —

    key specifies the key. This input must be of the same data type as the existing keys in the map.

   •       set element —

    set element specifies the set element that may be registered for the specified key. This input
    must be of the same data type as the elements of the sets in the map.

   •    map out —

   map out returns the registration map with the specified entry removed.

   •      element not registered for this key? —

    element not registered for this key? returns whether the specified set element has been
     registered for the specified key.

   •     removed last registration for this key? —

   removed last registration for this key? returns whether the specified set of elements is the last
     set of elements registered for this key.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Design Patterns\Registration Map\
   Registration Map Usage.lvproj


                                                    © National Instruments 1423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1424 ordinal=1424 -->
## Functions

Functions

      SetSet

      Use the Set VIs and functions to create and manipulate sets.


         Palette                     Description
        Object

                      Creates a set from the input elements. Duplicate elements appear only once in the         Build Set                       resulting set.

          Insert Into
         Set           Inserts an element into a set.
         Function

       Remove
       From Set    Removes an element from a set.
         Function

        Element of
         Set?         Returns whether an element is a member of a set.
         Function

       Read Set
       Max & Min   Returns the maximum and minimum elements in a set.
         Function

                     Represents a set on the block diagram. You cannot modify the embedded data in a set
         Set           interactively or programmatically. You can update set data only as a whole through
        Constant    operations such as writing to the set front panel terminal or right-clicking the set and
                       selecting Data Operations>>Copy Data or Data Operations>>Paste Data.

         Collection
         Size         Returns the number of elements or entries in a collection.
         Function

       Empty
         Collection?  Returns TRUE if the input collection contains zero elements or entries.
         Function

        Convert Set
                      Places the code that you can use to convert a set to an array.
        To Array


1424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1425 ordinal=1425 -->
## Functions

Functions


 Palette             Description
 Object

           Computes the union of two sets. The union is all elements that belong to either of the Set Union           two sets.


 Set        Computes the intersection of two sets. The intersection is all the elements that
 Intersection belong to both sets.


 Set        Computes the Cartesian product of two sets. The Cartesian product is a set of
 Cartesian    2-element clusters which covers all possible combinations of elements from the two
 Product      sets.


 Set        Computes the difference of two sets. The difference is the elements from the first set
 Difference   that are not included in the second set.

 Set
 Symmetric  Computes the symmetric difference of two sets.
 Difference

BuildBuild SetSet

Creates a set from the input elements. Duplicate elements appear only once in the
resulting set.


Inputs/Outputs

   •      element —

    element specifies the data you want to include in the set.

    This input accepts any data type. The default data type is string. All the element inputs must be


                                                    © National Instruments 1425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1426 ordinal=1426 -->
## Functions

Functions


             of the same data type.

               •       set —

             set returns the resulting set.


       InsertInsert IntoInto SetSet FunctionFunction

        Inserts an element into a set.


      Inputs/Outputs

               •       set in —

             set in specifies the set in which you want to insert an element. This input accepts a set of any
            data type. The default data type is a set of strings.

               •      element —

           element specifies the data you want to insert into the set. This input must be of the same data
            type as the existing elements in the set.

               •       set out —

             set out returns the set with the inserted element.

               •      already included? —

            already included? returns whether set in already includes the inserted element. If already
            included? is TRUE, set out returns the same set as set in.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Collections\Set Collection - Word

1426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1427 ordinal=1427 -->
## Functions

Functions

   Counting.vi
  • labview\examples\Design Patterns\Registration Map\
   Registration Map Usage.lvproj

RemoveRemove FromFrom SetSet FunctionFunction

Removes an element from a set.


Inputs/Outputs

   •       set in —

    set in specifies the set in which you want to remove an element. This input accepts a set of any
    data type. The default data type is a set of strings.

   •      element —

    element specifies the data you want to remove from the set. This input must be of the same data
    type as the elements in the set.

   •       set out —

    set out returns the set with the specified element removed.

   •      not included? —

    not included? returns whether set in includes element. If not included? is TRUE, set out returns
    the same set as set in.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Design Patterns\Registration Map\
   Registration Map Usage.lvproj


                                                    © National Instruments 1427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1428 ordinal=1428 -->
## Functions

Functions

      ElementElement ofof Set?Set? FunctionFunction

       Returns whether an element is a member of a set.


      Inputs/Outputs

               •       set —

             set specifies the set. This input accepts a set of any data type. The default data type is a set of
              strings.

               •      element —

           element specifies the data to look for in the set. This input must be of the same data type as the
           elements in set.

               •      found? —

           found? returns TRUE if element is included in set. Otherwise, found? returns FALSE.


     ReadRead SetSet MaxMax && MinMin FunctionFunction

       Returns the maximum and minimum elements in a set.


      Inputs/Outputs

               •       set —

             set specifies the set. This input accepts a set of any data type. The default data type is a set of
              strings.

               •     maximum —


1428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1429 ordinal=1429 -->
## Functions

Functions


   maximum returns the maximum element in set.

   •     minimum —

   minimum returns the minimum element in set.


SetSet ConstantConstant

Represents a set on the block diagram. You cannot modify the embedded data in a set
interactively or programmatically. You can update set data only as a whole through
operations such as writing to the set front panel terminal or right-clicking the set and
selecting Data Operations>>Copy Data or Data Operations>>Paste Data.


CollectionCollection SizeSize FunctionFunction

Returns the number of elements or entries in a collection.


Inputs/Outputs

   •       collection —

     collection specifies the collection. This input accepts any collection data type.

   •       size —

     size returns the number of elements or entries in collection.


EmptyEmpty Collection?Collection? FunctionFunction

Returns TRUE if the input collection contains zero elements or entries.


                                                    © National Instruments 1429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1430 ordinal=1430 -->
## Functions

Functions


      Inputs/Outputs

               •       collection —

             collection specifies the collection. This input accepts any collection data type.

               •     empty? —

          empty? returns TRUE if collection is empty. Otherwise, this output returns FALSE.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Collections\Map Collection - Comparing
        Test Results.vi
            • labview\examples\Collections\Set Collection - Word
        Counting.vi
            • labview\examples\Design Patterns\Registration Map\
        Registration Map Usage.lvproj

      ConvertConvert SetSet ToTo ArrayArray

       Places the code that you can use to convert a set to an array.

     When you add this VI to the block diagram, a For Loop displays. Wire a set to the tunnel
       input and return an array through the tunnel output.


1430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1431 ordinal=1431 -->
## Functions

Functions

SetSet UnionUnion

Computes the union of two sets. The union is all elements that belong to either of the
two sets.


Inputs/Outputs

   •       set 1 —

    set 1 specifies the first set. This input accepts a set of any data type. The default data type is a set
     of strings.

   •       set 2 —

    set 2 specifies the second set. This input must be the same data type as set 1. The default data
    type is a set of strings.

   •      union —

    union returns the combined set.


The following figure illustrates how this VI computes the union of two sets. The two
circles represent the two sets. The green section is the union.


                                                    © National Instruments 1431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1432 ordinal=1432 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Collections\Set Collection - Word
        Counting.vi

      SetSet IntersectionIntersection

      Computes the intersection of two sets. The intersection is all the elements that belong
       to both sets.


      Inputs/Outputs

               •       set 1 —

             set 1 specifies the first set. This input accepts a set of any data type. The default data type is a set
             of strings.

               •       set 2 —

             set 2 specifies the second set. This input must be the same data type as set 1. The default data
            type is a set of strings.

               •       intersection —

             intersection returns a set with the duplicate elements from the two input sets.


      The following figure illustrates how this VI computes the intersection of two sets. The
      two circles represent the two sets. The green section is the intersection.


1432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1433 ordinal=1433 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Collections\Set Collection - Word
   Counting.vi

SetSet CartesianCartesian ProductProduct

Computes the Cartesian product of two sets. The Cartesian product is a set of
2-element clusters which covers all possible combinations of elements from the two
sets.


Inputs/Outputs

   •       set 1 —

    set 1 specifies the first set. This input accepts a set of any data type. The default data type is a set
     of strings.

   •       set 2 —

    set 2 specifies the second set. This input accepts a set of any data type. The default data type is a
     set of strings.

   •      Cartesian product —


                                                    © National Instruments 1433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1434 ordinal=1434 -->
## Functions

Functions


            Cartesian product returns a set of 2-element clusters which covers all possible combinations of
           elements in set 1 and set 2. For each cluster, the first element is from set 1 and the second
           element is from set 2.


      SetSet DifferenceDifference

      Computes the difference of two sets. The difference is the elements from the first set
       that are not included in the second set.


      Inputs/Outputs

               •       set 1 —

             set 1 specifies the first set. This input accepts a set of any data type. The default data type is a set
             of strings.

               •       set 2 —

             set 2 specifies the second set. This input must be the same data type as set 1. The default data
            type is a set of strings.

               •       difference —

             difference returns a set of elements from set 1 that are not included in set 2.


      The following figure illustrates how this VI computes the difference of two sets. The
      two circles represent the two sets. The green section is the difference.


1434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1435 ordinal=1435 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Collections\Set Collection - Word
   Counting.vi

SetSet SymmetricSymmetric DifferenceDifference

Computes the symmetric difference of two sets.


Inputs/Outputs

   •       set 1 —

    set 1 specifies the first set. This input accepts a set of any data type. The default data type is a set
     of strings.

   •       set 2 —

    set 2 specifies the second set. This input must be the same data type as set 1. The default data
    type is a set of strings.

   •      symmetric difference —

    symmetric difference returns a set of elements that are included in either set 1 or set 2 but not


                                                    © National Instruments 1435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1436 ordinal=1436 -->
## Functions

Functions


            both.


      The following figure illustrates how this VI computes the symmetric difference of two
        sets. The two circles represent the two sets. The green sections are the symmetric
        difference.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Collections\Set Collection - Word
        Counting.vi

      FileFile I/OI/O

      Use the File I/O VIs and functions to open and close files, read from and write to files,
       create directories and files you specify in the path control, retrieve directory
       information, and write strings, numbers, arrays, and clusters to files.

      Use the VIs and functions on this palette to perform common I/O operations and other
       types of file I/O operations. You can read or write various types of data, such as
       characters or lines in text files, numeric values in spreadsheet text files, or data in
       binary files.

      The File I/O palette and the Advanced File palette include functions to control each file
       I/O operation individually. Use these functions to create or open a file, read data from


1436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1437 ordinal=1437 -->
## Functions

Functions

or write data to the file, and close the file. You also can use the functions to create
directories; move, copy, or delete files; list directory contents; change file
characteristics; or manipulate paths.


 Palette               Description Object

               Converts a 2D or 1D array of strings, signed integers, or double-precision numbers
                to a text string and writes the string to a new byte stream file or appends the string Write
                to an existing file. Wire data to the 2D data input or 1D data input to determine the Delimited
              polymorphic instance to use or manually select the instance. Spreadsheet
             Use this VI to transpose or separate data.


             Reads a specified number of lines or rows from a numeric text file beginning at a Read
                specified character offset and converts the data to a 2D, double-precision array of Delimited              numbers, strings, or integers. You must manually select the polymorphic instance Spreadsheet
             you want to use.


 Write To                Writes data to text-based measurement files (.lvm), binary measurement files
 Measurement
             (.tdm or .tdms), or Microsoft Excel files (.xlsx). File

 Read From             Reads data from a text-based measurement file (.lvm) or binary measurement file
 Measurement
             (.tdm or .tdms). File

 Open/Create/ Opens an existing file, creates a new file, or replaces an existing file,
 Replace File   programmatically or interactively using a file dialog box. This function does not
 Function     work for files inside an LLB.

 Close File     Closes an open file specified by refnum and returns the path to the file associated
 Function      with the refnum.

              Formats string, numeric, path, or Boolean data as text and writes the text to a file. If
 Format Into
             you wire a file refnum to the file input, writing begins at the current file position. To
 File
             append to an existing file, open the file and set the file position to the end of the file

                                                    © National Instruments 1437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1438 ordinal=1438 -->
## Functions

Functions


         Palette                       Description
        Object

                    by using the Set File Position function. Otherwise, the function will open the file and
                        write to the beginning of the file. This function does not work for files inside an LLB.

                     Scans text in a file for string, numeric, path, and Boolean data, converts the text to a        Scan From
                      data type, and returns a duplicated refnum and the converted outputs in the order           File                      scanned. This function does not work for files inside an LLB.

         Write to Text   Writes a string or an array of strings as lines to a file. This function does not work for
           File Function   files inside an LLB.

       Read from                     Reads a specified number of characters or lines from a byte stream file. This         Text File                        function does not work for files inside an LLB.         Function

         Write to                        Writes binary data to a new file, appends data to an existing file, or replaces the         Binary File                       contents of a file. This function does not work for files inside an LLB.
         Function

       Read from                     Reads binary data from a file and returns it in data. How the data is read depends on
         Binary File                       the format of the specified file. This function does not work for files inside an LLB.         Function

         Build Path                       Creates a new path by appending a name or a relative path to an existing path.         Function

          Strip Path     Returns the name of the last component of a path and the stripped path that leads
         Function      to that component.

           File
                    Use the file constants with the File I/O VIs and functions.        Constants


         Configuration Use the Configuration File VIs to create, modify, and read a platform-independent
           File VIs        configuration file.


      TDM         Use the TDM Streaming VIs and functions to read and write waveforms and
        Streaming    waveform properties to binary measurement files (.tdms).


         Storage/      Use the Storage/DataPlugin VIs to read measurement data from a variety of file
         DataPlugin    formats, write data to .tdm or .tdms files, or manage DataPlugins installed on the


1438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1439 ordinal=1439 -->
## Functions

Functions


 Palette               Description
 Object

                 local computer. You must download appropriate DataPlugins and register them on
               the local computer before you can access the corresponding file formats. Refer to
               the National Instruments website at ni.com/dataplugins to download DataPlugins.


             Use the Zip VIs to create new zip files, to add files to zip files, to unzip zip files, and
 Zip                to close zip files.

 XML         Use the XML VIs and functions to manipulate XML data.

 Waveform    Use the Waveform File I/O VIs to write waveform data to and read waveform data
 File I/O       from files.

 Advanced
 File          Use the Advanced File VIs and functions to manipulate files, directories, and paths.
 Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Arrays\Array to Spreadsheet String.vi

WriteWrite DelimitedDelimited SpreadsheetSpreadsheet

Converts a 2D or 1D array of strings, signed integers, or double-precision numbers to a
text string and writes the string to a new byte stream file or appends the string to an
existing file. Wire data to the 2D data input or 1D data input to determine the
polymorphic instance to use or manually select the instance.

Use this VI to transpose or separate data.

      Note To format with Microsoft Excel, use ActiveX with LabVIEW or the Report
       Generation Toolkit for Microsoft Office.


                                                    © National Instruments 1439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1440 ordinal=1440 -->
## Functions

Functions


            • Write Delimited Spreadsheet (DBL) VI
            • Write Delimited Spreadsheet (I64) VI
            • Write Delimited Spreadsheet (string) VI

     When you use this VI to write the data, the VI opens or creates the file before writing to
          it and closes it afterwards. You can use this VI to create a text file readable by most
       spreadsheet applications. This VI calls the Array To Spreadsheet String function to
       convert the data.

       WriteWrite DelimitedDelimited SpreadsheetSpreadsheet (DBL)(DBL) VIVI

       Converts a 2D or 1D array of strings, signed integers, or double-precision numbers to a
        text string and writes the string to a new byte stream file or appends the string to an
        existing file. Wire data to the 2D data input or 1D data input to determine the
      polymorphic instance to use or manually select the instance.

      Use this VI to transpose or separate data.

           Note To format with Microsoft Excel, use ActiveX with LabVIEW or the Report
              Generation Toolkit for Microsoft Office.


      Inputs/Outputs

               •      format (%.3f) —

           format specifies how to convert the numbers to characters.


1440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1441 ordinal=1441 -->
## Functions

Functions


   If the format is %.3f (default), the VI creates a string long enough to contain the number, with
  three digits to the right of the decimal point. If format is %d, the VI converts the data to integer
  form using as many characters as necessary to contain the entire number. If format is %s, the VI
  copies the input string. Use the format string syntax.

•        file path (dialog if empty) —

   file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
  displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
  box.

•     2D data —

  2D data specifies the data to write to the file if 1D data is not wired or is empty.

•     1D data —

  1D data specifies the data to write to the file if this input is not empty.

  The VI converts the 1D array into a 2D array before proceeding.

•     append to file? (new file:F) —

  append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
  VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      transpose? (no:F) —

  transpose? specifies whether the VI transposes the data after converting it from a string.

  The default is FALSE. If transpose? is FALSE, each call to this VI creates a new line or row in the
   file.

•       delimiter (\t) —

  delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
  For example, a value of , (comma) specifies a single comma as the delimiter. The default is \t,
  which specifies a single tab character as the delimiter.


                                                   © National Instruments 1441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1442 ordinal=1442 -->
## Functions

Functions

               •     new file path (Not A Path if cancelled) —

         new file path returns the path to the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When you use this VI to write the data, the VI opens or creates the file before writing to
          it and closes it afterwards. You can use this VI to create a text file readable by most
       spreadsheet applications. This VI calls the Array To Spreadsheet String function to
       convert the data.

       WriteWrite DelimitedDelimited SpreadsheetSpreadsheet (I64)(I64) VIVI

       Converts a 2D or 1D array of strings, signed integers, or double-precision numbers to a
        text string and writes the string to a new byte stream file or appends the string to an
        existing file. Wire data to the 2D data input or 1D data input to determine the
      polymorphic instance to use or manually select the instance.

      Use this VI to transpose or separate data.

           Note To format with Microsoft Excel, use ActiveX with LabVIEW or the Report
              Generation Toolkit for Microsoft Office.


      Inputs/Outputs

               •      format (%d) —

           format specifies how to convert the numbers to characters.


1442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1443 ordinal=1443 -->
## Functions

Functions


   If format is %d (default), the VI converts the data to integer form using as many characters as
  necessary to contain the entire number. If the format is %.3f, the VI creates a string long
  enough to contain the number, with three digits to the right of the decimal point. If format is %s,
  the VI copies the input string. Use the format string syntax.

•        file path (dialog if empty) —

   file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
  displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
  box.

•     2D data —

  2D data specifies the data to write to the file if 1D data is not wired or is empty.

•     1D data —

  1D data specifies the data to write to the file if this input is not empty.

  The VI converts the 1D array into a 2D array before proceeding.

•     append to file? (new file:F) —

  append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
  VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      transpose? (no:F) —

  transpose? specifies whether the VI transposes the data after converting it from a string.

  The default is FALSE. If transpose? is FALSE, each call to this VI creates a new line or row in the
   file.

•       delimiter (\t) —

  delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
  For example, a value of , (comma) specifies a single comma as the delimiter. The default is \t,
  which specifies a single tab character as the delimiter.


                                                   © National Instruments 1443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1444 ordinal=1444 -->
## Functions

Functions

               •     new file path (Not A Path if cancelled) —

         new file path returns the path to the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When you use this VI to write the data, the VI opens or creates the file before writing to
          it and closes it afterwards. You can use this VI to create a text file readable by most
       spreadsheet applications. This VI calls the Array To Spreadsheet String function to
       convert the data.

       WriteWrite DelimitedDelimited SpreadsheetSpreadsheet (string)(string) VIVI

       Converts a 2D or 1D array of strings, signed integers, or double-precision numbers to a
        text string and writes the string to a new byte stream file or appends the string to an
        existing file. Wire data to the 2D data input or 1D data input to determine the
      polymorphic instance to use or manually select the instance.

      Use this VI to transpose or separate data.

           Note To format with Microsoft Excel, use ActiveX with LabVIEW or the Report
              Generation Toolkit for Microsoft Office.


      Inputs/Outputs

               •      format (%s) —

           format specifies how to convert the numbers to characters.


1444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1445 ordinal=1445 -->
## Functions

Functions


   If format is %s (default), the VI copies the input string. If the format is %.3f, the VI creates a
  string long enough to contain the number, with three digits to the right of the decimal point. If
  format is %d, the VI converts the data to integer form using as many characters as necessary to
  contain the entire number. Use the format string syntax.

•        file path (dialog if empty) —

   file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
  displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
  box.

•     2D data —

  2D data specifies the data to write to the file if 1D data is not wired or is empty.

•     1D data —

  1D data specifies the data to write to the file if this input is not empty.

  The VI converts the 1D array into a 2D array before proceeding.

•     append to file? (new file:F) —

  append to file? appends data to an existing file, if TRUE. If append to file? is FALSE (default), the
  VI replaces data in an existing file. If there is no existing file, the VI creates a new file.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      transpose? (no:F) —

  transpose? specifies whether the VI transposes the data after converting it from a string.

  The default is FALSE. If transpose? is FALSE, each call to this VI creates a new line or row in the
   file.

•       delimiter (\t) —

  delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
  For example, a value of , (comma) specifies a single comma as the delimiter. The default is \t,
  which specifies a single tab character as the delimiter.


                                                   © National Instruments 1445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1446 ordinal=1446 -->
## Functions

Functions

               •     new file path (Not A Path if cancelled) —

         new file path returns the path to the file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When you use this VI to write the data, the VI opens or creates the file before writing to
          it and closes it afterwards. You can use this VI to create a text file readable by most
       spreadsheet applications. This VI calls the Array To Spreadsheet String function to
       convert the data.

     ReadRead DelimitedDelimited SpreadsheetSpreadsheet

      Reads a specified number of lines or rows from a numeric text file beginning at a
       specified character offset and converts the data to a 2D, double-precision array of
      numbers, strings, or integers. You must manually select the polymorphic instance you
      want to use.

      You optionally can transpose the array. The VI opens the file before reading from it and
       closes it afterwards. You can use this VI to read a spreadsheet file saved in text format.
       This VI calls the Spreadsheet String to Array function to convert the data.


            • Read Delimited Spreadsheet (DBL) VI
            • Read Delimited Spreadsheet (I64) VI
            • Read Delimited Spreadsheet (string) VI

     ReadRead DelimitedDelimited SpreadsheetSpreadsheet (DBL)(DBL) VIVI

      Reads a specified number of lines or rows from a numeric text file beginning at a
       specified character offset and converts the data to a 2D, double-precision array of
      numbers, strings, or integers. You must manually select the polymorphic instance you
      want to use.


1446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1447 ordinal=1447 -->
## Functions

Functions

You optionally can transpose the array. The VI opens the file before reading from it and
closes it afterwards. You can use this VI to read a spreadsheet file saved in text format.
This VI calls the Spreadsheet String to Array function to convert the data.


Inputs/Outputs

   •      format (%.3f) —

    format specifies how to convert the numbers to characters.

       If the format is %.3f (default), the VI creates a string long enough to contain the number, with
    three digits to the right of the decimal point. If format is %d, the VI converts the data to integer
    form using as many characters as necessary to contain the entire number. If format is %s, the VI
    copies the input string. Use the format string syntax.

   •        file path (dialog if empty) —

      file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
    displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
    box.

   •     number of rows (all:-1) —

   number of rows is the maximum number of rows or lines the VI reads.

    For this VI, a row is a character string ending with a carriage return, linefeed, or a carriage return
    followed by a linefeed; a string ending at the end of file; or a string that has the maximum line
    length specified by the max characters per row input. If number of rows is <0, the VI reads the
     entire file. The default is –1.

   •       start of read offset (chars.:0) —

     start of read offset specifies the position in the file, in characters (bytes), at which the VI begins
    reading.


                                                    © National Instruments 1447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1448 ordinal=1448 -->
## Functions

Functions


          The offset unit is bytes rather than numbers because byte stream files can contain segments of
              different types of data. Therefore, to read an array of 100 numbers that follows a header of 57
             characters, set start of read offset to 57.

               •     max characters/row (no limit:0) —

         max characters/row is the maximum number of characters the VI reads before ending the
            search for the end of a row or line.

          The default is 0, which means that there is no limit to the number of characters the VI reads.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      transpose? (F) —

            transpose? specifies whether the VI transposes the data after converting it from a string.

          The default is FALSE.

               •       delimiter (\t) —

             delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
            For example, a value of , (comma) specifies a single comma as the delimiter. The default is \t,
           which specifies a single tab character as the delimiter.

               •     new file path (Not A Path if cancelled) —

         new file path returns the path to the file.

               •        all rows —

                all rows is the data read from the file.

               •        first row —

                first row is the first row of the all rows array.

           You can use this output when you want to read one row into a 1D array.

               •     mark after read (chars.) —


1448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1449 ordinal=1449 -->
## Functions

Functions


   mark after read returns the character (byte) in the file following the last character read.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     EOF? —

    EOF? is TRUE if you attempt to read past the end of file.


ReadRead DelimitedDelimited SpreadsheetSpreadsheet (I64)(I64) VIVI

Reads a specified number of lines or rows from a numeric text file beginning at a
specified character offset and converts the data to a 2D, double-precision array of
numbers, strings, or integers. You must manually select the polymorphic instance you
want to use.

You optionally can transpose the array. The VI opens the file before reading from it and
closes it afterwards. You can use this VI to read a spreadsheet file saved in text format.
This VI calls the Spreadsheet String to Array function to convert the data.


Inputs/Outputs

   •      format (%d) —

    format specifies how to convert the numbers to characters.

       If format is %d (default), the VI converts the data to integer form using as many characters as
    necessary to contain the entire number. If the format is %.3f, the VI creates a string long
    enough to contain the number, with three digits to the right of the decimal point. If format is %s,
    the VI copies the input string. Use the format string syntax.


                                                    © National Instruments 1449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1450 ordinal=1450 -->
## Functions

Functions

               •        file path (dialog if empty) —

                file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
             displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
            box.

               •     number of rows (all:-1) —

          number of rows is the maximum number of rows or lines the VI reads.

            For this VI, a row is a character string ending with a carriage return, linefeed, or a carriage return
            followed by a linefeed; a string ending at the end of file; or a string that has the maximum line
            length specified by the max characters per row input. If number of rows is <0, the VI reads the
             entire file. The default is –1.

               •       start of read offset (chars.:0) —

              start of read offset specifies the position in the file, in characters (bytes), at which the VI begins
             reading.

          The offset unit is bytes rather than numbers because byte stream files can contain segments of
              different types of data. Therefore, to read an array of 100 numbers that follows a header of 57
             characters, set start of read offset to 57.

               •     max characters/row (no limit:0) —

         max characters/row is the maximum number of characters the VI reads before ending the
            search for the end of a row or line.

          The default is 0, which means that there is no limit to the number of characters the VI reads.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      transpose? (F) —

            transpose? specifies whether the VI transposes the data after converting it from a string.

          The default is FALSE.

               •       delimiter (\t) —


1450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1451 ordinal=1451 -->
## Functions

Functions


    delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
    For example, a value of , (comma) specifies a single comma as the delimiter. The default is \t,
    which specifies a single tab character as the delimiter.

   •     new file path (Not A Path if cancelled) —

   new file path returns the path to the file.

   •        all rows —

     all rows is the data read from the file.

   •        first row —

      first row is the first row of the all rows array.

    You can use this output when you want to read one row into a 1D array.

   •     mark after read (chars.) —

   mark after read returns the character (byte) in the file following the last character read.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •     EOF? —

    EOF? is TRUE if you attempt to read past the end of file.


ReadRead DelimitedDelimited SpreadsheetSpreadsheet (string)(string) VIVI

Reads a specified number of lines or rows from a numeric text file beginning at a
specified character offset and converts the data to a 2D, double-precision array of
numbers, strings, or integers. You must manually select the polymorphic instance you
want to use.

You optionally can transpose the array. The VI opens the file before reading from it and
closes it afterwards. You can use this VI to read a spreadsheet file saved in text format.
This VI calls the Spreadsheet String to Array function to convert the data.


                                                    © National Instruments 1451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1452 ordinal=1452 -->
## Functions

Functions


      Inputs/Outputs

               •      format (%s) —

           format specifies how to convert the numbers to characters.

                    If format is %s (default), the VI copies the input string. If the format is %.3f, the VI creates a
              string long enough to contain the number, with three digits to the right of the decimal point. If
           format is %d, the VI converts the data to integer form using as many characters as necessary to
            contain the entire number. Use the format string syntax.

               •        file path (dialog if empty) —

                file path is the path name of the file. If file path is empty (default) or is <Not A Path>, the VI
             displays a dialog box from which you can select a file. Error 43 occurs if you cancel the dialog
            box.

               •     number of rows (all:-1) —

          number of rows is the maximum number of rows or lines the VI reads.

            For this VI, a row is a character string ending with a carriage return, linefeed, or a carriage return
            followed by a linefeed; a string ending at the end of file; or a string that has the maximum line
            length specified by the max characters per row input. If number of rows is <0, the VI reads the
             entire file. The default is –1.

               •       start of read offset (chars.:0) —

              start of read offset specifies the position in the file, in characters (bytes), at which the VI begins
             reading.

          The offset unit is bytes rather than numbers because byte stream files can contain segments of
              different types of data. Therefore, to read an array of 100 numbers that follows a header of 57
             characters, set start of read offset to 57.

               •     max characters/row (no limit:0) —

1452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1453 ordinal=1453 -->
## Functions

Functions


  max characters/row is the maximum number of characters the VI reads before ending the
  search for the end of a row or line.

  The default is 0, which means that there is no limit to the number of characters the VI reads.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      transpose? (F) —

  transpose? specifies whether the VI transposes the data after converting it from a string.

  The default is FALSE.

•       delimiter (\t) —

  delimiter is the character or string of characters to use to separate fields in the spreadsheet file.
  For example, a value of , (comma) specifies a single comma as the delimiter. The default is \t,
  which specifies a single tab character as the delimiter.

•     new file path (Not A Path if cancelled) —

  new file path returns the path to the file.

•        all rows —

   all rows is the data read from the file.

•        first row —

   first row is the first row of the all rows array.

  You can use this output when you want to read one row into a 1D array.

•     mark after read (chars.) —

  mark after read returns the character (byte) in the file following the last character read.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•     EOF? —

                                                   © National Instruments 1453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1454 ordinal=1454 -->
## Functions

Functions


          EOF? is TRUE if you attempt to read past the end of file.

      WriteWrite ToTo MeasurementMeasurement FileFile

       Writes data to text-based measurement files (.lvm), binary measurement files (.tdm
       or .tdms), or Microsoft Excel files (.xlsx).

      Use the Read From Measurement File Express VI to read data from the generated
      measurement file.


      Dialog Box Options

        Option      Description

                      Displays the full path to the file to which you want to write data. The Express VI writes
                    data to the file that this parameter specifies only if the Filename input is unwired. If        Filename
                  you wire the Filename input, the VI writes data to the file that this input specifies
                       instead.

                     Contains the following options:

                                  • Binary with XML Header (TDM)—

                       (Windows) Sets the file format to binary measurement file (.tdm) and the file
                         extension in Filename to .tdm.
          File Format
                                         If you select this option, the Delimiter section and the No headers option in the
                     Segment Headers section are not available.

                   When you select this file format, you enable the Lock file for faster access
                        checkbox. Selecting this checkbox makes reading and writing significantly faster


1454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1455 ordinal=1455 -->
## Functions

Functions


Option      Description

                    (at the expense of the ability to multitask certain activities). It is recommended
                  that you use this option in most cases.

                   Note When this option is enabled, no two Express VIs can access the
                    same file at the same time when one of them is writing a "series of
                                   files."

                     • Binary (TDMS)—

                 Sets the file format to binary measurement file (.tdms) and the file extension in
               Filename to .tdms.

                           If you select this option, the Delimiter section and the No headers option in the
              Segment Headers section are not available.

                     • Text (LVM)—

                 Sets the file format to text-based measurement file (.lvm) and the file extension
                   in Filename to .lvm.

                     •  Microsoft Excel (.xlsx)—

                 Sets the file format to Microsoft Excel (.xlsx) and the file extension in Filename
                 to .xlsx.

                           If you select this option, the Delimiter section and the Segment Headers section
                 are unavailable.

                   Note This option does not require Microsoft Excel installed on the
                             local computer.


            Contains the following options:

                     • Save to one file—
Action
                Saves all the data to one file.

                     • Ask user to choose file—


                                                    © National Instruments 1455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1456 ordinal=1456 -->
## Functions

Functions


        Option      Description

                          Displays a dialog box that prompts users to select a file. This option is available
                         only when you select the Save to one file option.

                                  • Ask only once—

                      Prompts users to select a file only once. This option is available only when you
                         place a checkmark in the Ask user to choose file checkbox.

                                  • Ask each iteration—

                      Prompts users to select a file each time the Express VI runs. This option is
                           available only when you place a checkmark in the Ask user to choose file
                        checkbox.

                                  • Save to series of files (multiple files)—

                        Saves the data to multiple files. If Reset is TRUE, the VI starts at the first file in the
                              series. For example, if test_001.lvm has been saved to test_004.lvm,
                   test_001.lvm might be renamed, overwritten, or skipped based on the value
                           of the Existing Files option in the Configure Multi-file Settings dialog box.

                                  • Settings—

                          Displays the Configure Multi-file Settings dialog box. This option is available only
                    when you select the Save to series of files (multiple files) option.

                     Contains the following options:

                                  • Rename existing file—

                     Renames the existing file if Reset is TRUE.

                                  • Use next available filename—             If a file
         already                      Appends the next sequential number to the filename if Reset is TRUE.
          exists
                         For example, if test.lvm exists, LabVIEW saves the file as test1.lvm.

                                  • Append to file—

                      Appends the data to the existing file.


1456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1457 ordinal=1457 -->
## Functions

Functions


Option      Description

              The VI ignores the value of Reset if you select the Append to file option.

                   Note When you append data to an existing Excel file, errors might
                         occur if the Excel file was not created by this Express VI. This option
                       does not support appending data to an Excel file that was created by a
                            third-party application.

                     • Overwrite file—

                Replaces data in an existing file if Reset is TRUE.

            Contains the following options:

                     • One header per segment—

                 Creates one header per segment in the file to which LabVIEW writes the data.
                  Select this option if the acquisition rate of the data changes over time, if you
                 acquire two or more signals at different acquisition rates, or if the list of signals
               you log changes over time.

                     • One header only—

Segment        Creates only one header in the file to which LabVIEW writes the data. Select this
Headers         option if you acquire the same list of signals at the same constant acquisition
                    rate.

                     • No headers—

                 Creates an empty column for the time data each channel generates. This option
               does not include the data from the x-axis.

                   Note This option is available only when you select the Text (LVM)
                         option from the File Format section.


            Contains the following options:

X Value           • One column per channel—
Columns
                 Creates a separate column for time data each channel generates. This option


                                                    © National Instruments 1457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1458 ordinal=1458 -->
## Functions

Functions


        Option      Description

                          includes a column of values from the x-axis for every column of values from the y-
                               axis. Select this option if you acquire signals of different types or at different
                           acquisition rates.

                                  • One column only—

                          Creates only one column for the time data the channels generate. This option
                          includes only one column of values from the x-axis. Select this option if you
                          acquire signals at the same acquisition rate.

                                  • Empty time column—

                      Does not create a header in the file to which LabVIEW writes the data.

                     Contains the following options:

                                  • Tab—

                       Uses tabs to delimit fields in the text file.

                                  • Comma—
         Delimiter
                       Uses commas to delimit fields in the text file.

                         Note These options are available only when you select the Text (LVM)
                                 option from the File Format section.


                     Contains the description of the measurement file. LabVIEW appends the text you
                      enter in this text box to the header of the file. This text box is unavailable when you
                       select the Microsoft Excel (.xlsx) option from the File Format section.

                                  • Advanced—
          File
         Description                          Displays the Configure User Defined Properties dialog box when you select the
                        Binary (TDMS) or Binary with XML Header (TDM) option from the File Format
                            section. Displays the Configure Advanced Excel Options dialog box when you
                            select the Microsoft Excel (.xlsx) option. This button is unavailable when you
                            select the Text (LVM) option.


1458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1459 ordinal=1459 -->
## Functions

Functions

Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •     Comment —

    Appends a comment to each data set written to the measurement file. This input is unavailable
   when you select the Microsoft Excel (.xlsx) option from the File Format section.

   •      new_file —

       If TRUE, stops writing to the current file, creates the next file in the series, and writes to that file
     instead. This input is available only when you select the Save to series of files (multiple files)
    option.

   •      Signals —

    Contains the input signal or signals.

       If you wire two or more signals with the same name to the Signals input, LabVIEW appends an
     integer to the end of the names written in the file, which enforces unique channel names. For
    example, if you wire two signals named Sine to the Signals input, LabVIEW writes the names as
   Sine and Sine 1.

          Note To change or customize how a signal name displays, use the Set Dynamic Data
              Attributes Express VI.

   •      Flush? (T) — Specifies whether LabVIEW writes data to the Microsoft Excel file each time
     after this Express VI runs. If the value is FALSE, LabVIEW does not write the data to the Microsoft
     Excel file. Instead, LabVIEW stores the data in a temporary file. If the value is TRUE, LabVIEW
    writes the data from the temporary file to the Excel file and then purges the temporary file. The
     default is TRUE.

          Note If you use this Express VI to write data iteratively, setting the Flush? input to
          TRUE at each iteration might affect the writing performance negatively. National
             Instruments recommends that you wire a FALSE value to this input until the last
               iteration of the entire writing process. For the last iteration, you can wire a TRUE
             value to this input to write all data to the Excel file.

   •      Filename —


                                                    © National Instruments 1459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1460 ordinal=1460 -->
## Functions

Functions


             Specifies the name of the file to which you want to write data. If Filename is not wired, the VI
            uses the Filename specified in the configuration dialog box.

               •     DAQmx Task —

             Specifies the DAQmx task to use to populate data on the DAQmx Properties page of the
            Configure User Defined Properties dialog box.

               •      Reset — Specifies whether you want to reset the data file when you run this Express VI
               iteratively. LabVIEW ignores this input when you run this Express VI in the first iteration. During
            the second and subsequent iterations, if the value is FALSE, this Express VI appends data to a file
                    if the file already exists. Depending on your configuration for this Express VI, if the value is TRUE,
              this Express VI renames, overwrites, or skips a file if the file already exists. The default is FALSE.
               •      Enable —

            Enables or disables the Express VI. The default is ON or TRUE.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Saving Data —

             Indicates if the Express VI is saving the data.

               •      Filename Out —

            Returns the name of the file.


           Note The behavior of this VI changes depending upon the target. If the
               current target does not or might not have a host computer connected, the
               configuration dialog box displays warnings next to options that are invalid
              without a host. If you configure this VI to prompt for input and run the VI on a
                target with no user interface, such as the Real-Time Module with no host
             computer connected, this VI returns an error.

      You can also use the Storage/DataPlugin VIs to read from and write to .tdm files, or
      you can use the TDM Streaming functions to read from and write to .tdms files.


1460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1461 ordinal=1461 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\TDMS\Express Read and Write\TDMS
   Express Write Data (Time and Frequency Domain).vi
  • labview\examples\File IO\TDMS\Express Read and Write\TDMS
   Express Write Data (Time Domain).vi
  • labview\examples\File IO\Spreadsheet\Excel\Write Excel
   File.vi

Components

Displays the Configure User Defined Properties dialog box when you select the Binary
(TDMS) or Binary with XML Header (TDM) option from the File Format section.
Displays the Configure Advanced Excel Options dialog box when you select the
Microsoft Excel (.xlsx) option. This button is unavailable when you select the Text
(LVM) option.

Creates a separate column for time data each channel generates. This option includes
a column of values from the x-axis for every column of values from the y-axis. Select
this option if you acquire signals of different types or at different acquisition rates.

Creates only one column for the time data the channels generate. This option includes
only one column of values from the x-axis. Select this option if you acquire signals at
the same acquisition rate.

Creates an empty column for the time data each channel generates. This option does
not include the data from the x-axis.

Appends the data to the existing file.

Appends the next sequential number to the filename if Reset is TRUE.

Renames the existing file if Reset is TRUE.

Replaces data in an existing file if Reset is TRUE.


                                                    © National Instruments 1461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1462 ordinal=1462 -->
## Functions

Functions

      Does not create a header in the file to which LabVIEW writes the data.

       Creates only one header in the file to which LabVIEW writes the data. Select this option
           if you acquire the same list of signals at the same constant acquisition rate.

       Creates one header per segment in the file to which LabVIEW writes the data. Select
        this option if the acquisition rate of the data changes over time, if you acquire two or
      more signals at different acquisition rates, or if the list of signals you log changes over
       time.

      Uses commas to delimit fields in the text file.

      Uses tabs to delimit fields in the text file.

      Prompts users to select a file each time the Express VI runs. This option is available
       only when you place a checkmark in the Ask user to choose file checkbox.

      Prompts users to select a file only once. This option is available only when you place a
      checkmark in the Ask user to choose file checkbox.

       Value that Number of samples uses. The default is 1.

       Displays the Configure Multi-file Settings dialog box. This option is available only when
      you select the Save to series of files (multiple files) option.

      Saves the data to multiple files. If Reset is TRUE, the VI starts at the first file in the
        series. For example, if test_001.lvm has been saved to test_004.lvm,
     test_001.lvm might be renamed, overwritten, or skipped based on the value of the
       Existing Files option in the Configure Multi-file Settings dialog box.

      Saves all the data to one file.

       Contains the description of the measurement file. LabVIEW appends the text you enter
        in this text box to the header of the file. This text box is unavailable when you select
       the Microsoft Excel (.xlsx) option from the File Format section.

       Displays a dialog box that prompts users to select a file. This option is available only
     when you select the Save to one file option.


1462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1463 ordinal=1463 -->
## Functions

Functions

Displays the full path to the file to which you want to write data. The Express VI writes
data to the file that this parameter specifies only if the Filename input is unwired. If
you wire the Filename input, the VI writes data to the file that this input specifies
instead.

(Windows) Sets the file format to binary measurement file (.tdm) and the file
extension in Filename to .tdm.

Sets the file format to binary measurement file (.tdms) and the file extension in
Filename to .tdms.

Sets the file format to text-based measurement file (.lvm) and the file extension in
Filename to .lvm.

Sets the file format to Microsoft Excel (.xlsx) and the file extension in Filename to
.xlsx.

ReadRead FromFrom MeasurementMeasurement FileFile

Reads data from a text-based measurement file (.lvm) or binary measurement file
(.tdm or .tdms).


Dialog Box Options

 Option    Description

            Displays the full path to the file from which you want to read data. The Express VI reads
           data from the file that this parameter specifies only if the Filename input is unwired. If
 Filename
          you wire the Filename input, the VI reads data from the file that this input specifies
            instead.


                                                    © National Instruments 1463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1464 ordinal=1464 -->
## Functions

Functions


        Option    Description

                   Contains the following options:

                               • Text (LVM)—

                        Sets the file format to text-based measurement file (.lvm) and the file extension in
                           File Name to .lvm.

                     To enable this VI to read data from generic text files, place a checkmark in the Read
                       generic text files checkbox.

                               • Binary (TDMS)—

                        Sets the file format to binary measurement file (.tdms) and the file extension in
                           File Name to .tdms.

                                      If you select this option, the Time Stamps and Generic Text File sections are not
                          available.          File
        Format
                               • Binary with XML Header (TDM)—

                     (Windows) Sets the file format to binary measurement file (.tdm) and the file
                       extension in File Name to .tdm.

                                      If you select this option, the Time Stamps and Generic Text File sections are not
                          available.

                  When you select this file format, you enable the Lock file for faster access
                      checkbox. Selecting this checkbox makes reading and writing significantly faster (at
                       the expense of the ability to multitask certain activities). It is recommended that
                    you use this option in most cases.

                        Note When this option is enabled, no two Express VIs can access the
                          same file at the same time when one of them is writing a "series of files."


                   Contains the following option:

                               • Ask user to choose file—         Action
                        Displays a dialog box that prompts users to select a file.

       Segment  Contains the following options:


1464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1465 ordinal=1465 -->
## Functions

Functions


Option    Description

                  • Retrieve segments of original size—

               Retrieves segments of the signal from the file in the original size.

                  • Retrieve segments of specified size—

Size           Retrieves segments of the signal using the size you specify in Samples.

       ◦ Samples—

                    Specifies the number of samples you want to include in the segment size read
                 from the file. The default is 100. This option is available only when you select
                  the Retrieve segments of specified size option.

          Contains the following options:

                  •  Relative to start of measurement—

               Displays the timestamp in terms of seconds starting from zero. For example, 100 in
                 relative time equals 1 minute and 40 seconds.

Time           • Absolute (date and time)—
Stamps
               Displays the timestamp in terms of time elapsed since 12:00 a.m., Friday, January 1,
               1904, Universal Time [01-01-1904 00:00:00].

              Note These options are available only when you select the Text (LVM) option
                 from the File Format section.


          Contains the following options:

                  •  Start row of numeric data—

                Indicates the first row of numeric data. The Express VI begins reading data from thisGeneric
               row. The default is 1.Text File
                  •  First row is channel names—

                Specifies that the channel names are in the first row of the data file.


                                                    © National Instruments 1465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1466 ordinal=1466 -->
## Functions

Functions


        Option    Description

                               •  First column is time channel—

                         Specifies that the time data for each channel are in the first column of the data file.

                               • Read File Now—

                      Imports the data from the file you specify in File Name into the Sample data table.

                               • Sample data—

                        Displays the data from the file you specify in File Name when you click the Read
                           File Now button.

                     Note These options are available only when you select the Text (LVM) option
                         from the File Format section.


                   Contains the following options:

                               • Tab—

                     Uses tabs to delimit fields in the text file.

                               • Comma—         Delimiter
                     Uses a comma as the decimal separator.

                     Note These options are available only when you select the Text (LVM) option
                         from the File Format section.


                   Contains the following options:

                               •  . (dot)—

        Decimal      Uses a period as the decimal separator.
         Point
                               •  , (comma)—

                     Uses a comma as the decimal separator.


1466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1467 ordinal=1467 -->
## Functions

Functions


 Option    Description

               Note These options are available only when you select the Text (LVM) option
                  from the File Format section.


Inputs/Outputs

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Filename —

     Specifies the name of the file from which you want to read data.

   •      Reset —

    Resets the file position such that the next read starts at the beginning of the file.

   •      Signals —

    Contains the output signal or signals.

   •      Filename Out —

    Returns the name of the file.

   •     Comment —

    Returns the appended comment of each data set in the .lvm or .tdm file.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Description —

    Returns the description in the header of the .lvm or .tdm file.


                                                    © National Instruments 1467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1468 ordinal=1468 -->
## Functions

Functions

               •     EOF? —

            Returns TRUE when the Express VI reaches the end of the file.


      You also can use this VI to read Multisim data if you have Multisim 9.0 or later installed.
      Use the Write To Measurement File Express VI to write data to a measurement file. You
       also can use the Storage/DataPlugin VIs to read from and write to .tdm files.

           Note The behavior of this VI changes depending upon the target. If the
               current target does not or might not have a host computer connected, the
               configuration dialog box displays warnings next to options that are invalid
              without a host. If you configure this VI to prompt for input and run the VI on a
                target with no user interface, such as the Real-Time Module with no host
             computer connected, this VI returns an error.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Express Read and Write\TDMS
        Express Read Data (Time Domain).vi

     Components

       Specifies the number of samples you want to include in the segment size read from the
          file. The default is 100. This option is available only when you select the Retrieve
      segments of specified size option.

       Contains the following options:

       Retrieves segments of the signal using the size you specify in Samples.

       Retrieves segments of the signal from the file in the original size.

      Reads data from generic text files.

       Displays the timestamp in terms of time elapsed since 12:00 a.m., Friday, January 1,

1468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1469 ordinal=1469 -->
## Functions

Functions

1904, Universal Time [01-01-1904 00:00:00].

Displays the timestamp in terms of seconds starting from zero. For example, 100 in
relative time equals 1 minute and 40 seconds.

Contains the following options:

Uses a comma as the decimal separator.

Uses a period as the decimal separator.

Contains the following options:

Uses commas to delimit fields in the text file.

Uses tabs to delimit fields in the text file.

Contains the following options:

(Windows) Sets the file format to binary measurement file (.tdm) and the file
extension in File Name to .tdm.

Sets the file format to binary measurement file (.tdms) and the file extension in File
Name to .tdms.

Sets the file format to text-based measurement file (.lvm) and the file extension in
File Name to .lvm.

Displays the full path to the file from which you want to read data. The Express VI reads
data from the file that this parameter specifies only if the Filename input is unwired. If
you wire the Filename input, the VI reads data from the file that this input specifies
instead.

Specifies that the time data for each channel are in the first column of the data file.

Specifies that the channel names are in the first row of the data file.

Imports the data from the file you specify in File Name into the Sample data table.


                                                    © National Instruments 1469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1470 ordinal=1470 -->
## Functions

Functions

       Displays the data from the file you specify in File Name when you click the Read File
     Now button.

       Specifies that the time data for each channel are in the first column of the data file.

       Specifies that the channel names are in the first row of the data file.

       Indicates the first row of numeric data. The Express VI begins reading data from this
       row. The default is 1.

       Retrieves segments of the signal using the size you specify in Samples.

       Displays a dialog box that prompts users to select a file.

     Open/Create/ReplaceOpen/Create/Replace FileFile FunctionFunction

      Opens an existing file, creates a new file, or replaces an existing file, programmatically
       or interactively using a file dialog box. This function does not work for files inside an
       LLB.


      Inputs/Outputs

               •     prompt —

          prompt is the message that appears above the list of files and directories or folder in the file
             dialog box.

               •        file path (use dialog) —

                file path is the absolute path to the file.

                    If you do not wire file path, the function displays a dialog box from which you can select a file. If
           you specify an empty or relative path, this function returns an error. If file path is the path to a


1470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1471 ordinal=1471 -->
## Functions

Functions


  directory that does not exist, this function returns an error. Use the Create Folder function to
  create a directory.

•      operation (0:open) —

  operation is the operation to perform. Error 43 occurs if you cancel the dialog box.

  0 open (default)—Opens an existing file. Error 7 occurs if the file cannot be found.
  1 replace—Replaces an existing file by opening the file and setting its end of file to 0.
  2 create—Creates a new file. Error 10 occurs if the file already exists.
  3 open or create—Opens an existing file or creates a new file if one does not exist.
   replace or create—Creates a new file or replaces a file if it exists. This VI replaces a file by  4   opening the file and setting its end of file to 0.
   replace or create with confirmation—Creates a new file or replaces a file if it exists and you
  5    give permission. This VI replaces a file by opening the file and setting its end of file to 0.

•      access (0:read/write) —

  access specifies how you plan to access the file.

  The default is read/write.

  0         read/write
  1         read-only
  2         write-only

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      disable buffering (F) —

  disable buffering specifies if the file opens without buffering. The default is FALSE.

   If you want to read or write a data file to a Redundant Array of Independent Disks (RAID),
  consider opening the file without buffering to speed up data transfers. To disable buffering, wire
  a TRUE value to the disable buffering input.

        Note If you have a small amount of data to transfer, you might not notice a


                                                   © National Instruments 1471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1472 ordinal=1472 -->
## Functions

Functions


                       difference if you disable buffering.

          (macOS and Linux) LabVIEW ignores this input.

               •     refnum out —

          refnum out is the reference number of the open file.

          The value is Not A Refnum if the file cannot be opened.

               •      cancelled —

            cancelled is TRUE if you cancel the file dialog box or if you do not select the replacement in an
            advisory dialog box.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      You can optionally specify a dialog prompt or default filename. Use this function with
       the intermediate Write File or Read File functions. Use the Close File function to close
       the reference to the file.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Spreadsheet\Tab-Delimited Data\
        Tab-Delimited Data.lvproj

     CloseClose FileFile FunctionFunction

       Closes an open file specified by refnum and returns the path to the file associated with
       the refnum.

       Error I/O operates uniquely in this function, which closes the file regardless of whether
      an error occurred in a preceding operation. This ensures that files are closed correctly.


1472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1473 ordinal=1473 -->
## Functions

Functions


Inputs/Outputs

   •     refnum —

    refnum is the file refnum associated with the file you want to close.

   •       error in —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      path —

    path is the corresponding path to refnum.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Datalog\Datalog File.lvproj

FormatFormat IntoInto FileFile

Formats string, numeric, path, or Boolean data as text and writes the text to a file. If
you wire a file refnum to the file input, writing begins at the current file position. To
append to an existing file, open the file and set the file position to the end of the file by
using the Set File Position function. Otherwise, the function will open the file and write
to the beginning of the file. This function does not work for files inside an LLB.


                                                    © National Instruments 1473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1474 ordinal=1474 -->
## Functions

Functions


      Inputs/Outputs

               •      format string —

           format string specifies how to convert the input arguments.

             Defaults match the data type of the input arguments. Right-click the function and select Edit
           Format String from the shortcut menu to create and edit the format string.

             This input accepts a maximum of 255 characters.

               •      input file —

            input file can be a refnum or absolute file path.

                    If it is a refnum, this node opens the file specified by the refnum. This function creates the
             specified file if it does not already exist. The default is to display a file dialog box and prompt you
             to select a file.

                    If you specify an empty or relative path, this function returns an error.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      input 1 —

            input 1..n specifies the input parameters you want the function to convert.

             This parameter accepts a string, path, enumerated type, time stamp, Boolean, or any numeric
            data type. For complex numeric data types, this function converts only the real component. You
           cannot use arrays and clusters with this function.

                    If you specify a Boolean value for this parameter and %s as the format code, the Format Into File
             function outputs the value as TRUE or FALSE. If you specify a Boolean value for this parameter
          and any numeric format code, the Format Into File function outputs the appropriate version of 1
              for TRUE and 0 for FALSE. For example, if you specify %f as the format code, the function outputs


1474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1475 ordinal=1475 -->
## Functions

Functions


    1.00000. If you specify %d, the function outputs 1.

   •      output file refnum —

    output file refnum is the refnum of the file that the VI read.

    You can wire this output to another file function, depending on what you want to do with the
      file. The default is to close the file if it is referenced by a file path or selected from the file dialog
    box. If input file is a refnum, LabVIEW assumes that the file is still in use until you close it.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


Increase the number of parameters by right-clicking the function and selecting Add
Parameter from the shortcut menu or by resizing the function.

You can use this function to determine the order in which the data appears in the file.

This function converts new lines, or \n, in the format string into the platform-specific
end-of-line character, for example, CR/LF on Windows, and LF on macOS and Linux. If
you do not want to convert new lines into the end-of-line character, use the Format
Into String function and wire the resulting string output to the text input of the Write
to Text File function. Then right-click the Write to Text File function and remove the
checkmark next to the Convert EOL shortcut menu item.

Specifying Which Input to Use within the Format String

By default, this function uses the order of the inputs to populate the format specifiers,
or percent codes, in the Format String. However, you can use a number followed by a
dollar sign ($) within a percent code to specify exactly which input to use for that
percent code. For example, the percent code %3$d uses the third input regardless of
how many percent codes appear before it in the format string.

As a further example, refer to the following block diagram:


                                                    © National Instruments 1475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1476 ordinal=1476 -->
## Functions

Functions


      The following input combinations illustrate the effects of the $ specifier:


        Input           Format    Data in                Input 2                     Comments        1                 String    Output File
                            first     Format String does notuse the $ specifier, so the       first second %s %s
                            second     function populates the percent codes in input order.

                    %2$s    second    Format String uses the $ specifier to display the
       first second
                    %1$s    first      inputs in a different order than their input order.

                    %1$s    first
                                            Format String uses the $ specifier to display the first
       first second %1$s    first
                                                   input multiple times and ignore the second input.
                    %1$s    first

      You can use other special characters besides the $ to configure how this function
       populates the percent codes in format string.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Text (ASCII)\Format Into File
        and Scan From File.vi

     ScanScan FromFrom FileFile

      Scans text in a file for string, numeric, path, and Boolean data, converts the text to a
       data type, and returns a duplicated refnum and the converted outputs in the order
       scanned. This function does not work for files inside an LLB.

      You can use this function to read all the text in the file. However, you cannot use this
       function to determine a starting point for the scan. To do so, use the Read from Text

1476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1477 ordinal=1477 -->
## Functions

Functions

File function and the Scan From String function.


Inputs/Outputs

   •      format string —

    format string specifies how to convert the input string into the output arguments.

    The default is to scan the string according to default behavior for the data types of the outputs
    wired. Right-click the function and select Edit Scan String from the shortcut menu to create and
     edit the format string.

    This input accepts a maximum of 255 characters.

   •      input file —

    input file can be a refnum or absolute file path.

       If it is a refnum, this node opens the file specified by the refnum. This function creates the
     specified file if it does not already exist. The default is to display a file dialog box and prompt you
    to select a file.

       If you specify an empty or relative path, this function returns an error.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       default value 1 —

    default 1..n specifies the type and default value for the output parameters.

       If this function cannot scan the input value from format string, the function uses the default. If
    you do not wire default 1 and you wire a constant to format string, the function uses format
     string to determine the type of the output. Otherwise, the default data type is double-precision,
     floating-point. The default value is 0 or an empty string, depending on the output data type. If


                                                    © National Instruments 1477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1478 ordinal=1478 -->
## Functions

Functions


           you wire an enumerated type to default 1, the function finds substrings matching the string
            values in the enumerated type and returns the corresponding numeric value of the enumerated
             type.

           You can scan for Boolean values if you use a string or numeric format code. If the format code is
         %s or unwired, the function reads Y, T, TRUE, ON, or YES and any lowercase versions of those
           words as TRUE Boolean values. The function reads F, FALSE, OFF, or NO and any lowercase
             versions of those words as FALSE Boolean values. If you specify a numeric format code, the
             function reads any numeric value greater than 0.5 as TRUE and any numeric value less than or
            equal to 0.5 as FALSE.

               Note This function reads negative numbers as FALSE Boolean values because the
                      function converts the number to an unsigned 8-bit integer and any number less than
                     or equal to 0.5 becomes 0 during the conversion.

               •      output file refnum —

           output file refnum is the refnum of the file that the VI read.

           You can wire this output to another file function, depending on what you want to do with the
                  file. The default is to close the file if it is referenced by a file path or selected from the file dialog
            box. If input file is a refnum, LabVIEW assumes that the file is still in use until you close it.
               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      output 1 —

           output 1..n specifies the output parameters.

           Each output can be a string, path, enumerated type, time stamp, Boolean, or any numeric data
             type. If you scan a string that does not fit into the numeric data type you specify, this function
             returns the largest number that fits into that data type. You cannot use arrays and clusters with
              this function.

       Increase the number of parameters by right-clicking the function and selecting Add
      Parameter from the shortcut menu or by resizing the function.

           Note If an error occurs, the source component of the error out cluster
              contains a string of the form ''Scan From File (arg n),'' where n
                   is the first argument for which the error occurred.

1478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1479 ordinal=1479 -->
## Functions

Functions

If you wire a block diagram constant string to format string, LabVIEW uses format
string to determine the number of outputs and the data type of each output at
compile time. If the types you wire to the outputs do not match the types determined
by format string, you must change the output types before the VI can run.

If you do not directly wire a block diagram constant to format string, LabVIEW checks
for type mismatches at run time. If you want to scan values that have data types other
than double-precision, floating point, you must wire the data types to default 1..n.

When you use the match characters not in set format specifier (%[^...]), which is
used frequently to read an entire string, the matched character(s) are left in the file
stream. %[^\n\r] matches an entire line of text, but the carriage return and new line
are left behind. To remove these characters, use %[^\n\r]\n\r.

      Note By default, this function is locale aware, which means that it uses the
       system decimal separator configured in the regional settings of the operating
       system. In some instances, such as using GPIB instruments on European
        operating systems, you may need to override the system decimal separator
       by using the localization code syntax elements.

Examples of Formatting Strings

                         format                                           remaining input string                              default(s)              output(s)                             string                                                    string

                      —                   abc
 abc, xyz                  —                      xyz                        %3s,
                                                                         00
                    %s%f%2d >12.3+56i 7200                         0+00i                   12.3+56i
                      —                    72

 Q+1.27E–3 tail          Q%f t    —                     1.27E–3             ail

                                                         12
 0123456789           %3d%3d   —                                   6789
                                                         345

                                    100 (I32)              10
 X:9.860 Z:3.450            X:%fY:%f                                                   Z: 3450
                                       100.00 (DBL)            100.00

 set49.4.2               set%d    —                    49                  .4.2

                                                    © National Instruments 1479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1480 ordinal=1480 -->
## Functions

Functions


                                format                                           remaining         input string                              default(s)              output(s)
                                      string                                                    string

                                              blue (enum {red, green,          color: red                    color: %s                           red        —                                                    blue})

                                                               abcd
                               %[a-z]%d                         12
        abcd012xyz3               —                      —
                               %[a-z]%d                            xyz
                                                                 3

                                                            welcome to
       welcome to LabVIEW,                                                              LabVIEW                                  %[^,],%s   —                                   Smith       John Smith
                                                             John

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Text (ASCII)\Format Into File
        and Scan From File.vi

      WriteWrite toto TextText FileFile FunctionFunction

       Writes a string or an array of strings as lines to a file. This function does not work for
         files inside an LLB.

      Use the Set File Position function if you need to perform random access file reads or
        writes.


      Inputs/Outputs

               •     prompt (Choose or enter file path) —


1480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1481 ordinal=1481 -->
## Functions

Functions


    prompt is the message that appears above the list of files and directories or folder in the file
    dialog box.

   •        file (use dialog) —

      file can be a refnum or absolute file path.

       If you wire a path to the file input, the function opens or creates the file before writing to it and
    replaces any previous file contents. If you wire a file refnum to the file input, writing begins at
    the current file position. To append to an existing file, set the file position to the end of the file by
    using the Set File Position function. The default is to display a file dialog box and prompt you to
     select a file.

       If you specify an empty or relative path, this function returns an error. If you specify a path to a
    hidden file, this function returns an error.

   •       text —

     text is the data the function writes to the file. text is a string or an array of strings.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the refnum of the file that the function read. You can wire this output to another
      file function, depending on what you want to do with the file. The default is to close the file if it is
    referenced by a file path or selected from the file dialog box. If file is a refnum or if you wire
    refnum out to another function, LabVIEW assumes that the file is still in use until you close it.

   •      cancelled —

    cancelled is TRUE if you cancel the file dialog box.

    Otherwise, cancelled is FALSE, even if this function returns an error.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


This function appends platform-dependent, end-of-line (EOL) characters to the
elements of an array even if you right-click the function and remove the checkmark

                                                    © National Instruments 1481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1482 ordinal=1482 -->
## Functions

Functions

       next to the Convert EOL shortcut menu item.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Text (ASCII)\Write to Text File
        and Read from Text File.vi

     ReadRead fromfrom TextText FileFile FunctionFunction

      Reads a specified number of characters or lines from a byte stream file. This function
      does not work for files inside an LLB.


      Inputs/Outputs

               •     prompt (Open existing file) —

          prompt is the message that appears above the list of files and directories, or folder, in the file
             dialog box.

               •        file (use dialog) —

                file can be a refnum or absolute file path.

                    If it is a path, this function opens the file specified by the path. The default is to display a file
             dialog box and prompt you to select a file.

                    If you specify an empty or relative path or if the file does not exist, this function returns an error.

               •      count —

           count is the maximum number of characters or lines the function reads.

          The function reads fewer characters or lines if it reaches the end of file first. If count is <0, the
             function reads the entire file starting from the current file position. The default is to read a single

1482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1483 ordinal=1483 -->
## Functions

Functions

     line if you placed a checkmark next to the Read Lines shortcut menu item and to read the entire
      file if you removed the checkmark next to the item.

          Note If you wire a file size with a data type other than a 32-bit integer to count,
           LabVIEW coerces the data type to a 32-bit integer. This means the VI may not read the
           amount of data you intend. If you wire –1 to count and the size of the file you want to
            read is too large to be represented by a 32-bit integer, LabVIEW returns an error.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the refnum of the file that the function read. You can wire this output to another
      file function, depending on what you want to do with the file. The default is to close the file if it is
    referenced by a file path or selected from the file dialog box. If file is a refnum or if you wire
    refnum out to another function, LabVIEW assumes that the file is still in use until you close it.

   •       text —

     text is the text read from the file. By default, this parameter is a string that contains the
    characters read from the first line of the file. If you wire count, this parameter is an array of
     strings that contains the lines read from the file. If you right-click the function and remove the
    checkmark next to the Read Lines shortcut menu item, this parameter is a string that contains
    the characters read from the file.

   •      cancelled —

    cancelled is TRUE if you cancel the file dialog box.

    Otherwise, cancelled is FALSE, even if this function returns an error.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


This function opens files as read-only. If you wire the refnum out output of this
function to the file input of a write function, LabVIEW returns a permissions error. Use
the Open/Create/Replace File function to open the file with the default read/write
access and wire the refnum to the read and write functions.


                                                    © National Instruments 1483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1484 ordinal=1484 -->
## Functions

Functions

      By default, this function reads all characters from the text file. Wire an integer value to
      count to specify how many individual characters you want to read starting with the
         first character. Right-click the function and place a checkmark next to the Read Lines
       option in the shortcut menu to read individual lines from the text file. When you select
       the Read Lines option in the shortcut menu, wire an integer value to the count input to
       specify how many individual lines you want to read from the file starting with the first
         line. Enter a value of -1 in count to read all characters and lines from the text file.

      Use the Set File Position function if you need to perform random access.

      The function converts all platform-dependent end-of-line characters to line feed
       characters unless you right-click the function and remove the checkmark next to the
      Convert EOL shortcut menu item. If you wire a path to file, the function opens the file
       before reading from it and closes it afterwards.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Text (ASCII)\Write to Text File
        and Read from Text File.vi

      WriteWrite toto BinaryBinary FileFile FunctionFunction

       Writes binary data to a new file, appends data to an existing file, or replaces the
       contents of a file. This function does not work for files inside an LLB.

           If you want to use the Read from Binary File function to read the array or string data
      you write to file, the prepend array or string size? parameter must indicate TRUE.
       Otherwise, LabVIEW generates an error.

       This VI truncates arrays if the total array size is over 4 GB.


1484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1485 ordinal=1485 -->
## Functions

Functions


Inputs/Outputs

   •      prepend array or string size? (T) —

    prepend array or string size? indicates whether LabVIEW includes data size information at the
    beginning of the file when data is an array or string. If prepend array or string size? is FALSE,
    LabVIEW does not include the size information.

    The default is TRUE. prepend array or string size? controls only the top-level data size
    information. Arrays and strings in hierarchical data types such as clusters always include size
    information.

   •     prompt (Choose or enter file path) —

    prompt is the message that appears above the list of files and directories, or folder, in the file
    dialog box.

   •        file (use dialog) —

      file can be a refnum or absolute file path.

       If you wire a path to the file input, the function opens or creates the file before writing to it and
    replaces any previous file contents. If you wire a file refnum to the file input, writing begins at
    the current file position. To append to an existing file, set the file position to the end of the file by
    using the Set File Position function. The default is to display a file dialog box and prompt you to
     select a file.

       If you specify an empty or relative path, this function returns an error.

   •      data —

    data contains the data to write to the file and can be any data type.

   •      byte order (0:big-endian, network order) —

    byte order sets the endian form of the resulting data. Byte order, or endian form, indicates
    whether integers are represented in memory from most-significant byte to least-significant byte
    or vice versa. The function must read the data in the same byte order that the data was written.


                                                    © National Instruments 1485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1486 ordinal=1486 -->
## Functions

Functions


              big-endian, network order (default)—The most-significant byte occupies the lowest memory
           0 address. This endian form is used on PowerPC platforms such as VxWorks. This endian-form
              also is used when reading data written on a different platform.
              native, host order—Uses the byte-ordering format of the host computer. This endian form           1              increases read and write speed.
              little-endian—The least-significant byte occupies the lowest memory address. This endian           2            form is used on Windows, macOS, and Linux.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is the refnum of the file that the function read. You can wire this output to another
                 file function, depending on what you want to do with the file. The default is to close the file if it is
            referenced by a file path or selected from the file dialog box. If file is a refnum or if you wire
          refnum out to another function, LabVIEW assumes that the file is still in use until you close it.

               •      cancelled —

            cancelled is TRUE if you cancel the file dialog box.

            Otherwise, cancelled is FALSE, even if this function returns an error.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use the Deny Access function to make sure no other users change the file while you
       write to it. Use the Set File Position function if you need to perform random access.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Binary\Simple Binary\Simple
        Binary File.lvproj
            • labview\examples\File IO\Spreadsheet\Tab-Delimited Data\

1486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1487 ordinal=1487 -->
## Functions

Functions

   Buffered Stream to Tab-Delimited Text File.vi

ReadRead fromfrom BinaryBinary FileFile FunctionFunction

Reads binary data from a file and returns it in data. How the data is read depends on
the format of the specified file. This function does not work for files inside an LLB.

Refer to the Preallocated Read from Binary File function for information about reading
binary data and placing it into a pre-allocated array without incurring a copy.


Inputs/Outputs

   •      data type —

    data type sets the type of data the function uses to read from the binary file.

    The function interprets the data starting at the current file position to be count instances of data
    type. If the type is an array, string, or cluster containing an array or string, the function assumes
    that each instance of that data type contains size information. If an instance does not include
     size information, the function misinterprets the data. If LabVIEW determines that the data does
    not match the type, it sets data to the default for the specified type and returns an error.

   •     prompt (Open existing file) —

    prompt is the message that appears above the list of files and directories, or folder, in the file
    dialog box.

   •        file (use dialog) —

      file can be a refnum or absolute file path.

       If it is a path, this function opens the file specified by the path. The default is to display a file
    dialog box and prompt you to select a file.

       If you specify an empty or relative path or if the file does not exist, this function returns an error.


                                                    © National Instruments 1487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1488 ordinal=1488 -->
## Functions

Functions

               •      count (1) —

           count is the number of data elements to read. Data elements can be bytes or instances of data
             type.

          The function returns count data elements in data, or if it reaches the end of the file, it returns all
            the complete data elements read thus far and an end-of-file error. By default, the function
             returns a single data element. If count is –1, the function reads the entire file starting from the
             current file position. If count is less than –1, the function returns an error.

                    If you wire data to count and the specified data type is an array, the function automatically
             returns a cluster of arrays or cluster array because LabVIEW does not allow arrays of arrays.

                    If you wire a file size with a data type other than a 32-bit integer to count, LabVIEW coerces the
            data type to a 32-bit integer. This means the VI may not read the amount of data you intend. If
           you wire –1 to count and the size of the file you want to read is too large to be represented by a
             32-bit integer, LabVIEW returns an error.

                    If you wire a cluster of integers to count, the function returns a multidimensional array, one
           dimension per each cluster element. For example, if you wire a cluster which contains the values
               1, 2, and 3 to count, the function returns a 3D array, in which the first dimension contains one
            element, the second dimension contains two elements, and the third dimension contains three
            elements.

               •      byte order (0:big-endian, network order) —

            byte order sets the endian form of the resulting data. Byte order, or endian form, indicates
           whether integers are represented in memory from most-significant byte to least-significant byte
            or vice versa. The function must read the data in the same byte order that the data was written.

              big-endian, network order (default)—The most-significant byte occupies the lowest memory
           0 address. This endian form is used on PowerPC platforms such as VxWorks. This endian-form
              also is used when reading data written on a different platform.
              native, host order—Uses the byte-ordering format of the host computer. This endian form
           1
              increases read and write speed.
              little-endian—The least-significant byte occupies the lowest memory address. This endian
           2
            form is used on Windows, macOS, and Linux.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

1488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1489 ordinal=1489 -->
## Functions

Functions


    refnum out is the refnum of the file that the function read. You can wire this output to another
      file function, depending on what you want to do with the file. The default is to close the file if it is
    referenced by a file path or selected from the file dialog box. If file is a refnum or if you wire
    refnum out to another function, LabVIEW assumes that the file is still in use until you close it.

   •      data —

    data contains the data read from the file in the specified data type. It can consist of a string, an
     array, a cluster of arrays, or a cluster array, depending on which data type you are reading and
   how count is set.

   •      cancelled —

    cancelled is TRUE if you cancel the file dialog box.

    Otherwise, cancelled is FALSE, even if this function returns an error.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use the Deny Access function to make sure no other users change the file while you
read from it. Use the Set File Position function if you need to perform random access.

This function opens files as read-only. If you wire the refnum out output of this
function to the file input of a write function, LabVIEW returns a permissions error. Use
the Open/Create/Replace File function to open the file with the default read/write
access and wire the refnum to the read and write functions.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\File IO\Datalog\Datalog File.lvproj
  • labview\examples\File IO\Spreadsheet\Tab-Delimited Data\
   Tab-Delimited Data.lvproj
  • labview\examples\File IO\Binary\Simple Binary\Simple
   Binary File.lvproj
  • labview\examples\File IO\Binary\Endian Considerations\


                                                    © National Instruments 1489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1490 ordinal=1490 -->
## Functions

Functions

        Endian Considerations with Binary Files.vi

      BuildBuild PathPath FunctionFunction

       Creates a new path by appending a name or a relative path to an existing path.


      Inputs/Outputs

               •      base path —

           base path specifies the path to which this function appends name or relative path.

          The default is an empty path. If base path is invalid, this function sets appended path to <Not
         A Path>.

               •     name or relative path —

         name or relative path is the new path component appended to base path.

                    If name or relative path is an empty string or an invalid path, this function sets appended path
             to <Not A Path>.

               •     appended path —

          appended path is the resulting path.


      Suppose you want to build the path c:\dir1\vis\first.vi. The following table
      shows examples of how you can specify base path and name or relative path to build
        this path.


        Operation                       base path         name or relative path

        To specify a name              c:\dir1\vis     first.vi

        To specify a relative path         c:\dir1         vis\first.vi

        To specify an absolute path      —               c:\dir1\vis\first.vi


1490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1491 ordinal=1491 -->
## Functions

Functions

StripStrip PathPath FunctionFunction

Returns the name of the last component of a path and the stripped path that leads to
that component.


Inputs/Outputs

   •      path —

    path specifies the path on which you want to operate.

       If this parameter is an empty path or is invalid, this function returns an empty string in name and
   <Not A Path> in stripped path.
   •      stripped path —

    stripped path is the resulting path obtained by removing name from the end of path.

   •     name —

   name is the last component of the specified path.


For the path C:\labview\foo.vi, stripped path returns C:\labview while
name returns foo.vi.
FileFile ConstantsConstants

Use the file constants with the File I/O VIs and functions.


 Palette Object  Description

 Path Constant  Use this constant to supply a constant path value to the block diagram.

 Current VI's    Returns the path to the file of the current VI. If the VI never has been saved, this
 Path Function  function returns <Not A Path>.

                                                    © National Instruments 1491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1492 ordinal=1492 -->
## Functions

Functions


         Palette Object  Description

        Get System                       Returns the system directory specified in the system directory type input.
         Directory

       Empty Path                       Returns an empty path.        Constant

                       Returns a path whose value is <Not A Path>. You can use this path as an output        Not A Path                     from structures and subVIs when an error occurs and you do not want to return a
        Constant                         path.

        Not a Refnum  Returns a refnum whose value is Not A Refnum. You can use this refnum as an
        Constant      output from structures and subVIs when an error occurs.

         Default
         Directory      Returns the path to the default directory.
         Function

         Default Data                       Returns the directory you configure to store the data a VI or function generates.
         Directory

          VI Library      Returns the path to the VI library directory for the current application instance on
         Function       the current computer.

         Application                       Returns the path to the directory containing the application.         Directory

        Temporary
         Directory      Returns the path to the temporary directory.
         Function

      PathPath ConstantConstant

      Use this constant to supply a constant path value to the block diagram.

        Right-click the constant and select Browse for Path from the shortcut menu to
       navigate to and select a path. You also can set the value of a path constant by using the
       Operating tool or the Labeling tool to click it and enter the path you want. To enter the
      path to a VI inside an LLB, add a backslash and the VI name to the end of the path to
       the LLB. For example, C:\example.llb\color.vi. To enter the path of a VI from
      a palette, place the VI on the block diagram and <Ctrl>-drag the VI into the path
       constant.

1492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1493 ordinal=1493 -->
## Functions

Functions

You can resize a path constant.

You cannot change the value of the path constant while the VI runs. You can assign a
label to this constant.


CurrentCurrent VI'sVI's PathPath FunctionFunction

Returns the path to the file of the current VI. If the VI never has been saved, this
function returns <Not A Path>.

This function always returns the current location of the VI. If you move the VI, the value
returned changes.

If you build the VI into an application, this function returns the path to the VI in the
application file, and treats the application file as a VI library.

      Note To obtain the path to the directory containing the application, use the
        Application Directory VI.


Inputs/Outputs

   •      path —

    path is the path to the current VI.


GetGet SystemSystem DirectoryDirectory

Returns the system directory specified in the system directory type input.

This VI returns the system directory of the current target, including My Computer.


                                                    © National Instruments 1493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1494 ordinal=1494 -->
## Functions

Functions

       (Real-Time Module) You cannot use this VI in VIs that run on RT targets.


      Inputs/Outputs

               •      system directory type —

           system directory type specifies the type of directory you want LabVIEW to retrieve.

             User Home—Directory that contains the personal files of the current user. This directory is a           0              readable and writable directory accessible to a single user of the system.
             User Desktop—Directory that contains files located on the desktop of the current user. This           1
                directory is a readable and writable directory accessible to a single user of the system.
             User Documents—Default directory for saving the documents of the current user. This           2
                directory is a readable and writable directory accessible to a single user of the system.
             User Application Data—Directory that contains data for the system applications of the current
           3 user. This directory is a readable and writable directory accessible to a single user of the
              system.
             User Preferences—Directory that contains the preferences for the current user. This directory           4                    is a readable and writable directory accessible to a single user of the system.
             User Temporary—Directory that holds temporary files for the current user. This directory is a
           5 readable and writable directory accessible to a single user of the system. You cannot change
              the path to this temporary directory.
               Public Documents—Directory that contains documents accessible to all users of the system.
           6               This directory is readable and sometimes writable.
               Public Application Data—Directory that contains data for system applications accessible to
           7                   all users of the system. This directory is readable and sometimes writable.
               Public Preferences—Directory that contains preferences common to all users of the system.
           8
               This directory is readable and sometimes writable.
             System Core Libraries—Directory that contains the libraries that come with the operating
           9
              system. This directory is typically read-only to the standard user of the system.
             System Installed Libraries—Directory that contains libraries a user installs on the system.
           10
               This directory is typically read-only to the standard user of the system.
               Application Files—Directory that contains files of applications installed on the system. This
           11
                directory is typically read-only to the standard user of the system.
             Boot Volume Root—Top-level directory used to start the system. This directory is typically
           12
               read-only to the standard user of the system.
           13 Public Cache—Directory that stores files the MathScript RT Module installs and shares among


1494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1495 ordinal=1495 -->
## Functions

Functions


         all users for the purpose of making certain operations faster. This directory is readable and
      sometimes writable.

   •      create directory if not found? (F) —

    create directory if not found? specifies whether the VI creates a new directory if the specified
     directory does not exist. If FALSE (default), the VI returns the path where the system expects to
     find the directory. If TRUE, LabVIEW creates a new directory.

   •      system directory —

    system directory returns the specified system directory of the current target.


If errors occur while accessing or creating a directory, or the current target does not
support the specified system directory type, the VI returns Not a Path.

EmptyEmpty PathPath ConstantConstant

Returns an empty path.

Unlike the not a path constant, this constant is a valid path. You can use this constant
as a starting point for building paths using the Build Path function.


NotNot AA PathPath ConstantConstant

Returns a path whose value is <Not A Path>. You can use this path as an output from
structures and subVIs when an error occurs and you do not want to return a path.

Unlike the empty path constant, this constant is an invalid path, and is generally
returned when a path operation fails.


                                                    © National Instruments 1495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1496 ordinal=1496 -->
## Functions

Functions

      NotNot aa RefnumRefnum ConstantConstant

       Returns a refnum whose value is Not A Refnum. You can use this refnum as an output
      from structures and subVIs when an error occurs.

       For example, you can use the Not a Refnum constant to verify that the refnum is valid
       before passing the refnum to the next file I/O operation. Wire the error out cluster of a
          file I/O function to the selector terminal of a Case structure. Place the Not a Refnum
       constant in the Error subdiagram and wire the constant through the output tunnel
      and to the next file I/O operation. In the No Error subdiagram, wire the refnum
      output of the file I/O function through the Case structure and to the next file I/O
       operation.

           Note Do not test whether a refnum is invalid by comparing the refnum to the
              output returned by the Not a Refnum constant. The Not a Refnum constant
               returns a unique sequence of bits that is guaranteed to be an invalid refnum.
             However, because this sequence of bits is only one possible invalid refnum
               representation, it likely will not equal another refnum to which you compare
                       it. Instead, use the Not a Number/Path/Refnum? function to test whether a
             refnum is invalid. The Not A Number/Path/Refnum? function returns a
             Boolean value that is correct for all possible invalid refnum representations.


       DefaultDefault DirectoryDirectory FunctionFunction

       Returns the path to the default directory.

      The default directory is the directory in which LabVIEW automatically stores
       information unless you specify otherwise. You can view and set the path to the default
       directory by selecting Default Directory from the pull-down menu on the Paths page of
       the Options dialog box.


1496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1497 ordinal=1497 -->
## Functions

Functions

Inputs/Outputs

   •      path —

    path is the path to the default directory.


DefaultDefault DataData DirectoryDirectory

Returns the directory you configure to store the data a VI or function generates.

You can set the default data directory in the Options dialog box.


Inputs/Outputs

   •      App:Default Data Directory —

    App:Default Data Directory is the path to the default data directory.


VIVI LibraryLibrary FunctionFunction

Returns the path to the VI library directory for the current application instance on the
current computer.

If you build the VI into an application, this function returns the path of the directory
containing the application file.


Inputs/Outputs

   •      path —

    path is the path to the VI library directory for the current application instance on the current


                                                    © National Instruments 1497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1498 ordinal=1498 -->
## Functions

Functions


            computer.


       ApplicationApplication DirectoryDirectory

       Returns the path to the directory containing the application.

           If you call this VI from a stand-alone application, this VI returns the path to the folder
       containing the stand-alone application.

           If you call this VI from the development environment and the VI is loaded in a LabVIEW
       project file (.lvproj), this VI returns the path to the folder containing the project file.
           If the project is not saved, this VI returns <Not a Path>.

           If the top-level VI is not loaded in a project, the VI returns the path to the directory
       containing the top level VI. If the VI is not saved to disk, this VI returns <Not a
      Path>.


      Inputs/Outputs

               •      Application Directory —

            Application Directory is the path to the directory where this VI is running.


      TemporaryTemporary DirectoryDirectory FunctionFunction

       Returns the path to the temporary directory.

       This temporary directory is the directory in which you want LabVIEW to store
       information that you do not want to store in the default directory. You can set this
      temporary directory in the Options dialog box. Setting this directory does not change
       the system temporary directory.


1498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1499 ordinal=1499 -->
## Functions

Functions


Inputs/Outputs

   •      path —

    path is the path to the temporary directory.

ConfigurationConfiguration FileFile VIsVIs

Use the Configuration File VIs to create, modify, and read a platform-independent
configuration file.

      Note Note

                • You cannot include comments or any other information in a key string.
                • You can use the Configuration File VIs for Windows configuration
              settings files only in the ANSI format.


 Palette          Description Object

 Open
        Opens a reference to the configuration data found in a platform-independent
 Config
          configuration file.
 Data


         Reads a value associated with a key in a specified section from the configuration data
 Read     identified by refnum. If the key does not exist, the VI returns the default value. This VI
 Key     supports multibyte characters in strings. Wire data to the default value input to
         determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 1499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1500 ordinal=1500 -->
## Functions

Functions


         Palette                  Description
        Object

                  Writes a value to a key in a specified section of the configuration data identified by
         Write    refnum. This VI modifies data in memory. To write data to disk, use the Close Config Data
        Key       VI. Wire data to the value input to determine the polymorphic instance to use or manually
                    select the instance.


       Remove               Removes a key in a specified section from the configuration data identified by refnum.        Key

       Remove               Removes a section from the configuration data identified by refnum.         Section

         Close                  Writes data to the platform-independent configuration file identified by refnum and then         Config
                   closes the reference to that file.        Data


        Get Key  Gets the names of all keys in the specified section from the configuration data identified
       Names  by refnum.

        Get
         Section  Gets the names of all sections from the configuration data identified by refnum.
       Names

        Not A
         Config                 Determines whether a configuration data refnum is valid.        Data
       Refnum

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\Configuration
        (INI)\Configuration (INI) File.lvproj


1500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:1500 -->

