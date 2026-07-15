# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4501 ordinal=4501 -->
## Functions

Functions


The normalization factor, s, is equal to N-k.

If method is Modified Covariance, Ris a matrix of size 2(N-k)-by-(k+1) defined as
follows.


     *where xi is the complex conjugate of xi. The normalization factor, s, is equal to 2*(N-
k).

This VI supports both single shot and continuous mode. The following figure illustrates
how to use the AutoCorrelation Matrix VI in single shot and continuous mode. The two
outputs, AutoCorrelation Matrix 1 and AutoCorrelation Matrix 2, always produce the
same results.


Autocorrelation matrix is widely used in the field of spectrum analysis to estimate the
spectral components within the input signal. In general, Covariance and Modified
Covariance methods give better results in spectral estimation processing than the
AutoCorrelation, Pre-Windowed and Post-Windowed methods. National Instruments

                                                    © National Instruments 4501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4502 ordinal=4502 -->
## Functions

Functions

      recommends that you use the Covariance or the Modified Covariance method to
       estimate the autocorrelation matrix when performing spectrum analysis.

      AutoCorrelationAutoCorrelation MatrixMatrix (CDB)(CDB) VIVI

      Computes the autocorrelation matrix of the input sequence X. Wire data to the X input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •        initial? —

               initial? controls the initialization of the internal buffer. The default is FALSE.

          The first time this VI runs or if initial? is TRUE, LabVIEW initializes the internal buffer to empty. If
                initial? is FALSE, LabVIEW initializes the internal buffer to the final data points from the previous
               call to this instance. To process a large data sequence that consists of smaller blocks, set this
            input to TRUE for the first block and to FALSE for continuous processing of all remaining blocks.

               •     X —

          X is the input sequence.

               •      order —

            order specifies the order of the AutoCorrelation Matrix. If the order is smaller than zero, this VI
             returns an error. The default is 0.

               •     method —

          method specifies the method used to compute the autocorrelation matrix.

           0   AutoCorrelation (default)
           1   Pre-Windowed
           2   Post-Windowed
           3   Covariance


4502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4503 ordinal=4503 -->
## Functions

Functions


    4   Modified Covariance

   •      AutoCorrelation Matrix —

    AutoCorrelation Matrix returns the autocorrelation matrix of X of the size of (order+1) multiplied
    by (order+1).

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI uses the following equation to calculate the autocorrelation matrix.


where Mis AutoCorrelation Matrix, Ris data matrix, sis normalization factor. RH is
the conjugate transpose of matrix R.

If method is AutoCorrelation, Ris a matrix of size (N+k)-by-(k+1) defined as follows.


where xi is the i-th element in X, Nis the length of X , and kis the order. The
normalization factor, s, is equal to N.

If method is Pre-Windowed, Ris a matrix of size N-by-(k+1) defined as follows.


                                                    © National Instruments 4503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4504 ordinal=4504 -->
## Functions

Functions

      The normalization factor, s, is equal to N.

           If method is Post-Windowed, Ris a matrix of size N-by-(k+1) defined as follows.


      The normalization factor, s, is equal to N.

           If method is Covariance, Ris a matrix of size (N-k)-by-(k+1) defined as follows.


      The normalization factor, s, is equal to N-k.

           If method is Modified Covariance, Ris a matrix of size 2(N-k)-by-(k+1) defined as
        follows.


          *      where xi is the complex conjugate of xi. The normalization factor, s, is equal to 2*(N-
         k).

       This VI supports both single shot and continuous mode. The following figure illustrates
     how to use the AutoCorrelation Matrix VI in single shot and continuous mode. The two
       outputs, AutoCorrelation Matrix 1 and AutoCorrelation Matrix 2, always produce the
     same results.


4504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4505 ordinal=4505 -->
## Functions

Functions


Autocorrelation matrix is widely used in the field of spectrum analysis to estimate the
spectral components within the input signal. In general, Covariance and Modified
Covariance methods give better results in spectral estimation processing than the
AutoCorrelation, Pre-Windowed and Post-Windowed methods. National Instruments
recommends that you use the Covariance or the Modified Covariance method to
estimate the autocorrelation matrix when performing spectrum analysis.

Y[i]=X[i-n]Y[i]=X[i-n]

Shifts the elements in the Input Array by the specified number of shifts: n.


Inputs/Outputs

   •      Input Array —

    Input Array is the input array to be shifted.

   •        shifts: n —

     shifts: n specifies the direction and number of shifts applied to Input Array. The VI shifts Input
    Array to the right if shifts: n is positive and to the left if shifts: n is negative. The default is 0.

    To properly shift Input Array without setting the output sequence Shifted Array to 0, the
    absolute value of shifts: n must be less than the number of elements in Input Array:

     |shifts: n| < n.


                                                    © National Instruments 4505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4506 ordinal=4506 -->
## Functions

Functions


                    If the absolute value of shifts: n is greater than or equal to the number of samples in Input Array,
            the VI sets Shifted Array to 0 and returns an error.

               •       Shifted Array —

             Shifted Array returns the output sequence.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let the sequence Yrepresent the output sequence Shifted Array. Then the elements of
   Yare related to the elements of Xby


        for i= 0, 1, n– 1,

      where nis the number of elements in Input Array.

           Note The Y[i]=X[i-n] VI does not rotate the elements in the array. The Y[i]=X[i-
               n] VI disposes of the elements of the input sequence shifted outside the
               range. You cannot recover those elements by shifting the array in the
              opposite direction.

     ZeroZero PadderPadder

       Resizes the input sequence Input Array to the next higher valid power of 2, sets the
     new trailing elements of the sequence to zero, and leaves the first n elements
      unchanged, where n is the number of samples in the input sequence. Wire data to the
       Input Array input to determine the polymorphic instance to use or manually select the
       instance.


4506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4507 ordinal=4507 -->
## Functions

Functions

  • Zero Padder (DBL) VI
  • Zero Padder (CDB) VI

ZeroZero PadderPadder (DBL)(DBL) VIVI

Resizes the input sequence Input Array to the next higher valid power of 2, sets the
new trailing elements of the sequence to zero, and leaves the first n elements
unchanged, where n is the number of samples in the input sequence. Wire data to the
Input Array input to determine the polymorphic instance to use or manually select the
instance.


Inputs/Outputs

   •      Input Array —

    Input Array is the input sequence. If Input Array is empty, Zero Padded Array is also empty.

   •      only non-power of 2? —

    only non-power of 2? specifies when to zero pad the Input Array.

   When only non-power of 2? is TRUE, this VI zero pads Input Array only if the array size is not a
     valid power of 2. For example, if Input Array contains 500 elements, the size of the zero padded
    output sequence is 512. When only non-power of 2? is FALSE, this VI resizes Input Array to the
    next valid power of 2 even if the array size already is a valid power of 2. For example, if Input
    Array contains 1,024 elements, the size of the zero padded output sequence is 2,048. The default
      is FALSE.

   •      Zero Padded Array —

    Zero Padded Array is the Input Array padded up to the next power of 2 elements.

    Zero Padded Array is useful when the size of the acquired data buffers is not a power of 2, and
    you want to take advantage of fast processing algorithms in the analysis VIs. These algorithms
    include Fourier transforms, Power Spectrum, and fast Hartley transforms, which are extremely
     efficient for buffer sizes that are a power of 2.


                                                    © National Instruments 4507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4508 ordinal=4508 -->
## Functions

Functions

      ZeroZero PadderPadder (CDB)(CDB) VIVI

       Resizes the input sequence Input Array to the next higher valid power of 2, sets the
     new trailing elements of the sequence to zero, and leaves the first n elements
      unchanged, where n is the number of samples in the input sequence. Wire data to the
       Input Array input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •      Input Array —

            Input Array is the input sequence. If Input Array is empty, Zero Padded Array is also empty.

               •      only non-power of 2? —

            only non-power of 2? specifies when to zero pad the Input Array.

         When only non-power of 2? is TRUE, this VI zero pads Input Array only if the array size is not a
              valid power of 2. For example, if Input Array contains 500 elements, the size of the zero padded
           output sequence is 512. When only non-power of 2? is FALSE, this VI resizes Input Array to the
            next valid power of 2 even if the array size already is a valid power of 2. For example, if Input
            Array contains 1,024 elements, the size of the zero padded output sequence is 2,048. The default
                is FALSE.

               •      Zero Padded Array —

           Zero Padded Array is the Input Array padded up to the next power of 2 elements.

           Zero Padded Array is useful when the size of the acquired data buffers is not a power of 2, and
           you want to take advantage of fast processing algorithms in the analysis VIs. These algorithms
            include Fourier transforms, Power Spectrum, and fast Hartley transforms, which are extremely
               efficient for buffer sizes that are a power of 2.

     UnwrapUnwrap PhasePhase

      Unwraps the Phase array by eliminating discontinuities whose absolute values exceed

4508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4509 ordinal=4509 -->
## Functions

Functions

either pi or 180, depending on the units you specify in phase unit.


Inputs/Outputs

   •      Phase —

    Phase is the input array of phases to unwrap. Use the phase unit input to specify the units.

   •      phase unit —

    phase unit specifies the units for Phase and Unwrapped Phase.

    0  Radian in, radian out (default)
    1  Radian in, degree out
    2  Degree in, degree out
    3  Degree in, radian out

   •     Unwrapped Phase —

   Unwrapped Phase returns Phase unwrapped. Use the phase unit input to specify the units.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Unwrap Phase VI unwraps the Phase array by eliminating discontinuities. When
the difference between two adjacent values in Phase exceeds pi, and phase unit is
Radian in, radian out, this VI uses the following equation to calculate
Unwrapped Phase:


where P_outis the Unwrapped Phase, Pis the Phase, Nis the length of Phase, and

                                                    © National Instruments 4509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4510 ordinal=4510 -->
## Functions

Functions

             is the floor operation.

       This VI uses similar equations to calculate Unwrapped Phase for the other units you
       specify in phase unit.

      The following two graphs show the effects of unwrapping the phase. The first graph
      shows the original phase before you unwrap it, and the second graph shows the phase
        after you unwrap it.


      You can apply the Unwrap Phase VI to the computed phase response of a linear time-
       invariant system. The phase response is defined as the complex angle of the frequency
      response of a system. You compute the phase response as angles within [–pi, pi], or, in
       other words, as angles within one circle of 2*pi radians. Because multiples of 2*pi wrap
     when you compute the phase response, often there are discontinuities in the phase
      response from one frequency bin to the next.

       DigitalDigital ReversedReversed OrderOrder

       Modifies the input array according to the digital-reversed order of the index.

       Wire data to the X input to determine the polymorphic instance to use or manually
        select the instance.


            • Digital Reversed Order (DBL) VI


4510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4511 ordinal=4511 -->
## Functions

Functions

  • Digital Reversed Order (CDB) VI
  • Digital Reversed Order (I32) VI

When the index of a sequence has the radix-base digits (a0a1…an), the VI modifies the
sequence Xinto the digital-reversed sequence Yaccording to the following equation.


For examples of radix-base digits, 2-base is binary and 16-base is hexadecimal.

The following illustration shows the 2-base reversed order (bit-reversed order) of 8
elements.


DigitalDigital ReversedReversed OrderOrder (DBL)(DBL) VIVI

Modifies the input array according to the digital-reversed order of the index.

Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


                                                    © National Instruments 4511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4512 ordinal=4512 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is the real input array the VI modifies. The length of X must be an integer power of radix.

               •       radix —

             radix is the base of the exponent. radix must be greater than or equal to 2. The default value is 2.

               •      Reversed {X} —

           Reversed {X} returns X with permuted elements.

               •      Reversed Index —

           Reversed Index returns the corresponding index of X for each element in Reversed {X}.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When the index of a sequence has the radix-base digits (a0a1…an), the VI modifies the
      sequence Xinto the digital-reversed sequence Yaccording to the following equation.


       For examples of radix-base digits, 2-base is binary and 16-base is hexadecimal.

      The following illustration shows the 2-base reversed order (bit-reversed order) of 8
       elements.


4512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4513 ordinal=4513 -->
## Functions

Functions


DigitalDigital ReversedReversed OrderOrder (CDB)(CDB) VIVI

Modifies the input array according to the digital-reversed order of the index.

Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •     X —

    X is the complex input array the VI modifies. The length of X must be an integer power of radix.

   •       radix —

    radix is the base of the exponent. radix must be greater than or equal to 2. The default value is 2.

   •      Reversed {X} —

    Reversed {X} returns X with modified elements.

   •      Reversed Index —


                                                    © National Instruments 4513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4514 ordinal=4514 -->
## Functions

Functions


           Reversed Index returns the corresponding index of X for each element in Reversed {X}.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When the index of a sequence has the radix-base digits (a0a1…an), the VI modifies the
      sequence Xinto the digital-reversed sequence Yaccording to the following equation.


       For examples of radix-base digits, 2-base is binary and 16-base is hexadecimal.

      The following illustration shows the 2-base reversed order (bit-reversed order) of 8
       elements.


       DigitalDigital ReversedReversed OrderOrder (I32)(I32) VIVI

       Modifies the input array according to the digital-reversed order of the index.

       Wire data to the X input to determine the polymorphic instance to use or manually
        select the instance.


4514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4515 ordinal=4515 -->
## Functions

Functions


Inputs/Outputs

   •     X —

    X is the integer input array the VI modifies. The length of X must be an integer power of radix.

   •       radix —

    radix is the base of the exponent. radix must be greater than or equal to 2. The default value is 2.

   •      Reversed {X} —

    Reversed {X} returns X with modified elements.

   •      Reversed Index —

    Reversed Index returns the corresponding index of X for each element in Reversed {X}.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When the index of a sequence has the radix-base digits (a0a1…an), the VI modifies the
sequence Xinto the digital-reversed sequence Yaccording to the following equation.


For examples of radix-base digits, 2-base is binary and 16-base is hexadecimal.

The following illustration shows the 2-base reversed order (bit-reversed order) of 8
elements.


                                                    © National Instruments 4515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4516 ordinal=4516 -->
## Functions

Functions


     DecimateDecimate (single(single shot)shot)

      Decimates the input sequence X by the decimating factor and the averaging Boolean
        control. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


            • Decimate (single shot, DBL) VI
            • Decimate (single shot, CDB) VI

           If Yrepresents the output sequence Decimated Array, the Decimate (single shot) VI
       obtains the elements of the sequence Yusing the following equation:


        for i = 0, 1, 2, …, size– 1,


4516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4517 ordinal=4517 -->
## Functions

Functions

where nis the number of elements in X, mis the decimating factor, sizeis the
number of elements in the output sequence Decimated Array, and  gives the largest
integer less than or equal to the number.

DecimateDecimate (single(single shot,shot, DBL)DBL) VIVI

Decimates the input sequence X by the decimating factor and the averaging Boolean
control. Wire data to the X input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     X —

    X is the input sequence. The number of elements in X must be greater than or equal to the
    decimating factor.

   •      decimating factor —

    decimating factor is the factor by which the VI decimates input sequence X. decimating factor
    must be greater than zero. The default is 1.

       If decimating factor is greater than the number of elements in X or less than or equal to zero,
     this VI sets Decimated Array to an empty array and returns an error.

   •      averaging —

    averaging specifies how the VI handles the data points in X.

       If averaging is FALSE (default), this VI keeps every decimating factor point from X. If averaging is
    TRUE, each output point in Decimated Array is the mean of the decimating factor input points.

   •      Decimated Array —

    Decimated Array returns the decimated sequence of X.

   •       error —


                                                    © National Instruments 4517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4518 ordinal=4518 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If Yrepresents the output sequence Decimated Array, the Decimate (single shot) VI
       obtains the elements of the sequence Yusing the following equation:


        for i = 0, 1, 2, …, size– 1,


      where nis the number of elements in X, mis the decimating factor, sizeis the
      number of elements in the output sequence Decimated Array, and  gives the largest
       integer less than or equal to the number.

      DecimateDecimate (single(single shot,shot, CDB)CDB) VIVI

      Decimates the input sequence X by the decimating factor and the averaging Boolean
        control. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex input sequence for decimation. The number of elements in X must be greater
           than or equal to the decimating factor.

               •      decimating factor —


4518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4519 ordinal=4519 -->
## Functions

Functions


    decimating factor is the factor by which the VI decimates input sequence X. decimating factor
    must be greater than zero. The default is 1.

       If decimating factor is greater than the number of elements in X or less than or equal to zero,
     this VI sets Decimated Array to an empty array and returns an error.

   •      averaging —

    averaging specifies how the VI handles the data points in X.

       If averaging is FALSE (default), this VI keeps every decimating factor point from X. If averaging is
    TRUE, each output point in Decimated Array is the mean of the decimating factor input points.

   •      Decimated Array —

    Decimated Array returns the decimated sequence of X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If Yrepresents the output sequence Decimated Array, the Decimate (single shot) VI
obtains the elements of the sequence Yusing the following equation:


for i = 0, 1, 2, …, size– 1,


where nis the number of elements in X, mis the decimating factor, sizeis the
number of elements in the output sequence Decimated Array, and  gives the largest
integer less than or equal to the number.


                                                    © National Instruments 4519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4520 ordinal=4520 -->
## Functions

Functions

     DecimateDecimate (continuous)(continuous)

       Continuously decimates the input sequence X by the decimating factor and the
       averaging Boolean control. Wire data to the X input to determine the polymorphic
       instance to use or manually select the instance.


            • Decimate (continuous, DBL) VI
            • Decimate (continuous, CDB) VI

           If Yrepresents the output sequence Decimated Array, the Decimate (continuous) VI
       obtains the elements of the sequence Yusing the following equation.

           If averaging is FALSE:

      Yi=xi*m+s

        for i= 0, 1, 2,…, size–1,


           If averaging is TRUE:


        for i= 0, 1, 2,…, size–1,


      where nis the number of elements in X, mis the decimating factor, sis the start
       index, sizeis the number of elements in the output sequence Decimated Array,
       gives the smallest integer greater than or equal to the number, and  gives the largest
       integer less than or equal to the number.

4520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4521 ordinal=4521 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\
   Continuous Decimating.vi

DecimateDecimate (continuous,(continuous, DBL)DBL) VIVI

Continuously decimates the input sequence X by the decimating factor and the
averaging Boolean control. Wire data to the X input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •       reset —

    reset controls the initialization of the decimation. The default is FALSE.

       If reset is TRUE or if the VI runs for the first time, LabVIEW initializes the decimation from the
    sample of X specified by start index. When the VI runs again with reset set to FALSE, LabVIEW
     initializes the decimation from the final states of the previous call to the VI.

    To process a large data sequence that consists of smaller blocks, set reset to TRUE for the first
    block and to FALSE for all remaining blocks. You also can set reset to TRUE at regular intervals of
    blocks to periodically reset the sample from which the decimation begins.

   •     X —

    X is the first input sequence.

   •      decimating factor —

    decimating factor is the factor by which the VI decimates input sequence X. decimating factor


                                                    © National Instruments 4521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4522 ordinal=4522 -->
## Functions

Functions


          must be greater than zero. The default is 1.

                    If decimating factor is greater than the number of elements in X or less than or equal to zero,
              this VI sets Decimated Array to an empty array and returns an error.

               •      averaging —

            averaging specifies how the VI handles the data points in X.

                    If averaging is FALSE (default), this VI keeps every decimating factor point from X. If averaging is
           TRUE, each output point in Decimated Array is the mean of the decimating factor input points.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       start index —

              start index determines from which sample in X the decimation starts if LabVIEW calls the VI for
            the first time or reset is TRUE. start index must be greater than or equal to zero. The default is 0.

               •      Decimated Array —

           Decimated Array returns the decimated sequence of X.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If Yrepresents the output sequence Decimated Array, the Decimate (continuous) VI
       obtains the elements of the sequence Yusing the following equation.

           If averaging is FALSE:

      Yi=xi*m+s

        for i= 0, 1, 2,…, size–1,


4522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4523 ordinal=4523 -->
## Functions

Functions

If averaging is TRUE:


for i= 0, 1, 2,…, size–1,


where nis the number of elements in X, mis the decimating factor, sis the start
index, sizeis the number of elements in the output sequence Decimated Array,
gives the smallest integer greater than or equal to the number, and  gives the largest
integer less than or equal to the number.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\
   Continuous Decimating.vi

DecimateDecimate (continuous,(continuous, CDB)CDB) VIVI

Continuously decimates the input sequence X by the decimating factor and the
averaging Boolean control. Wire data to the X input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •       reset —


                                                    © National Instruments 4523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4524 ordinal=4524 -->
## Functions

Functions


             reset controls the initialization of the decimation. The default is FALSE.

                    If reset is TRUE or if the VI runs for the first time, LabVIEW initializes the decimation from the
           sample of X specified by start index. When the VI runs again with reset set to FALSE, LabVIEW
               initializes the decimation from the final states of the previous call to the VI.

           To process a large data sequence that consists of smaller blocks, set reset to TRUE for the first
            block and to FALSE for all remaining blocks. You also can set reset to TRUE at regular intervals of
            blocks to periodically reset the sample from which the decimation begins.

               •     X —

          X is the complex input sequence for decimation. The number of elements in X must be greater
           than or equal to the decimating factor.

               •      decimating factor —

           decimating factor is the factor by which the VI decimates input sequence X. decimating factor
          must be greater than zero. The default is 1.

                    If decimating factor is greater than the number of elements in X or less than or equal to zero,
              this VI sets Decimated Array to an empty array and returns an error.

               •      averaging —

            averaging specifies how the VI handles the data points in X.

                    If averaging is FALSE (default), this VI keeps every decimating factor point from X. If averaging is
           TRUE, each output point in Decimated Array is the mean of the decimating factor input points.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       start index —

              start index determines from which sample in X the decimation starts if LabVIEW calls the VI for
            the first time or reset is TRUE. start index must be greater than or equal to zero. The default is 0.

               •      Decimated Array —

           Decimated Array returns the decimated sequence of X.


4524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4525 ordinal=4525 -->
## Functions

Functions

   •       error out —

     error out contains error information. This output provides standard error out functionality.


If Yrepresents the output sequence Decimated Array, the Decimate (continuous) VI
obtains the elements of the sequence Yusing the following equation.

If averaging is FALSE:

Yi=xi*m+s

for i= 0, 1, 2,…, size–1,


If averaging is TRUE:


for i= 0, 1, 2,…, size–1,


where nis the number of elements in X, mis the decimating factor, sis the start
index, sizeis the number of elements in the output sequence Decimated Array,
gives the smallest integer greater than or equal to the number, and  gives the largest
integer less than or equal to the number.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Signal Operation\
   Continuous Decimating.vi


                                                    © National Instruments 4525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4526 ordinal=4526 -->
## Functions

Functions

     UpsampleUpsample

        Inserts zeros in input sequence X by upsampling factor. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • Upsample (DBL) VI
            • Upsample (CDB) VI

           If Yrepresents the output sequence Upsampled Array, the Upsample VI obtains the
      elements of the sequence Yusing the following equation.


        for i= 0, 1, 2, …, size–1,

      size= n*m,

      where nis the number of elements in X, mis the upsampling factor, kis leading
       zeros, and sizeis the number of elements in the output sequence Upsampled Array.

     UpsampleUpsample (DBL)(DBL) VIVI

        Inserts zeros in input sequence X by upsampling factor. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —


4526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4527 ordinal=4527 -->
## Functions

Functions


    X is a real vector.

   •      upsampling factor —

    upsampling factor determines the number of zeros between two adjacent samples. The VI
     inserts upsampling factor – 1 zeros into every two elements in X. upsampling factor must be
     greater than zero. The default is 1.

   •      leading zeros —

    leading zeros specifies the number of leading zeros in Upsampled Array. leading zeros must be
     greater than or equal to zero and less than upsampling factor. The default is 0.

   •     Upsampled Array —

    Upsampled Array returns the upsampled sequence. The length of Upsampled Array is the
    upsampling factor times the length of X.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If Yrepresents the output sequence Upsampled Array, the Upsample VI obtains the
elements of the sequence Yusing the following equation.


for i= 0, 1, 2, …, size–1,

size= n*m,

where nis the number of elements in X, mis the upsampling factor, kis leading
zeros, and sizeis the number of elements in the output sequence Upsampled Array.

UpsampleUpsample (CDB)(CDB) VIVI

Inserts zeros in input sequence X by upsampling factor. Wire data to the X input to

                                                    © National Instruments 4527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4528 ordinal=4528 -->
## Functions

Functions

      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •      upsampling factor —

           upsampling factor determines the number of zeros between two adjacent samples. The VI
              inserts upsampling factor – 1 zeros into every two elements in X. upsampling factor must be
             greater than zero. The default is 1.

               •      leading zeros —

            leading zeros specifies the number of leading zeros in Upsampled Array. leading zeros must be
             greater than or equal to zero and less than upsampling factor. The default is 0.

               •     Upsampled Array —

          Upsampled Array returns the upsampled sequence. The length of Upsampled Array is the
           upsampling factor times the length of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If Yrepresents the output sequence Upsampled Array, the Upsample VI obtains the
      elements of the sequence Yusing the following equation.


        for i= 0, 1, 2, …, size–1,


4528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4529 ordinal=4529 -->
## Functions

Functions

size= n*m,

where nis the number of elements in X, mis the upsampling factor, kis leading
zeros, and sizeis the number of elements in the output sequence Upsampled Array.

RationalRational ResampleResample

Resamples the input signal X by interpolating X, passing the interpolated signal
through an FIR filter, and decimating the filtered signal. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


   • Rational Resample (single channel, DBL) VI
   • Rational Resample (single channel, CDB) VI
   • Rational Resample (multi-channel, DBL) VI
   • Rational Resample (multi-channel, CDB) VI

The following steps describe the rational resampling process. Each step corresponds
to a numbered section of the following image.


                                                    © National Instruments 4529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4530 ordinal=4530 -->
## Functions

Functions


         1. Input signal X for resampling. The time interval between two adjacent samples is 1.
         2. Insert zeros between every two adjacent samples to upsample X by the
           interpolation factor. Let X1 represent the interpolated signal.
         3. Using a FIR filter, filter X1at the start index to obtain the first output sample. The
          elements outside the range of the interpolated signal equal zero.
         4. Move the filter to the position start index + decimation and filter again to obtain
          the second output sample.
         5. Repeat step 4, adding each new decimation value until there are not enough
         samples in X1 for filtering. Store the final samples to internal states and wait for the
          next signal block. The time interval between two adjacent samples in an output
           signal is equal to decimation / interpolation. t0 specifies the time of the first

4530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4531 ordinal=4531 -->
## Functions

Functions

   output sample.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\
   Rational Resampling.vi

RationalRational ResampleResample (single(single channel,channel, DBL)DBL) VIVI

Resamples the input signal X by interpolating X, passing the interpolated signal
through an FIR filter, and decimating the filtered signal. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       anti-aliasing? —

     anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
    downsamples the signal.

       If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
    the computation requirements increase during resampling.

   •       reset —

    reset controls the initialization of resampling. The default is FALSE.

    The first time this VI runs or when reset is TRUE, LabVIEW initializes the internal states of the VI
    to zero and uses start index to determine when the resampling starts. The next time this VI runs
    and reset is FALSE, LabVIEW initializes the internal states to the final states from the previous call
    to this VI.


                                                    © National Instruments 4531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4532 ordinal=4532 -->
## Functions

Functions


           To process a large data sequence that consists of smaller blocks, set reset to TRUE for the first
            block and to FALSE for all the remaining blocks in continuous resampling.

               •     X —

          X is the input real signal for resampling. The sampling interval of X is 1.

               •       start index —

              start index determines where the resampling starts for the first call to the VI or if reset is TRUE.
            Set the start index according to the signal after X is interpolated. start index must be greater
           than or equal to 0. The default is 0.

               •      resample factor —

           resample factor contains the interpolation factor and the decimation factor for resampling.

                     •       interpolation —

                 interpolation is the interpolation factor for resampling. The default is 1.

                     •      decimation —

               decimation is the decimation factor for resampling. The default is 1.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —


4532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4533 ordinal=4533 -->
## Functions

Functions


        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the resampled signal. The sampling interval of Y is decimation/interpolation.

   •       t0 —

    t0 returns the time instance for the first sample of each signal in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following steps describe the rational resampling process. Each step corresponds
to a numbered section of the following image.


                                                    © National Instruments 4533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4534 ordinal=4534 -->
## Functions

Functions


         1. Input signal X for resampling. The time interval between two adjacent samples is 1.
         2. Insert zeros between every two adjacent samples to upsample X by the
           interpolation factor. Let X1 represent the interpolated signal.
         3. Using a FIR filter, filter X1at the start index to obtain the first output sample. The
          elements outside the range of the interpolated signal equal zero.
         4. Move the filter to the position start index + decimation and filter again to obtain
          the second output sample.
         5. Repeat step 4, adding each new decimation value until there are not enough
         samples in X1 for filtering. Store the final samples to internal states and wait for the
          next signal block. The time interval between two adjacent samples in an output
           signal is equal to decimation / interpolation. t0 specifies the time of the first

4534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4535 ordinal=4535 -->
## Functions

Functions

   output sample.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\
   Rational Resampling.vi

RationalRational ResampleResample (single(single channel,channel, CDB)CDB) VIVI

Resamples the input signal X by interpolating X, passing the interpolated signal
through an FIR filter, and decimating the filtered signal. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       anti-aliasing? —

     anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
    downsamples the signal.

       If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
    the computation requirements increase during resampling.

   •       reset —

    reset controls the initialization of resampling. The default is FALSE.

    The first time this VI runs or when reset is TRUE, LabVIEW initializes the internal states of the VI
    to zero and uses start index to determine when the resampling starts. The next time this VI runs
    and reset is FALSE, LabVIEW initializes the internal states to the final states from the previous call
    to this VI.


                                                    © National Instruments 4535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4536 ordinal=4536 -->
## Functions

Functions


           To process a large data sequence that consists of smaller blocks, set reset to TRUE for the first
            block and to FALSE for all the remaining blocks in continuous resampling.

               •     X —

          X is the input complex signal for resampling. The sampling interval of X is 1.

               •       start index —

              start index determines where the resampling starts for the first call to the VI or if reset is TRUE.
            Set the start index according to the signal after X is interpolated. start index must be greater
           than or equal to 0. The default is 0.

               •      resample factor —

           resample factor contains the interpolation factor and the decimation factor for resampling.

                     •       interpolation —

                 interpolation is the interpolation factor for resampling. The default is 1.

                     •      decimation —

               decimation is the decimation factor for resampling. The default is 1.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —


4536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4537 ordinal=4537 -->
## Functions

Functions


        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the resampled signal. The sampling interval of Y is decimation/interpolation.

   •       t0 —

    t0 returns the time instance for the first sample of each signal in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following steps describe the rational resampling process. Each step corresponds
to a numbered section of the following image.


                                                    © National Instruments 4537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4538 ordinal=4538 -->
## Functions

Functions


         1. Input signal X for resampling. The time interval between two adjacent samples is 1.
         2. Insert zeros between every two adjacent samples to upsample X by the
           interpolation factor. Let X1 represent the interpolated signal.
         3. Using a FIR filter, filter X1at the start index to obtain the first output sample. The
          elements outside the range of the interpolated signal equal zero.
         4. Move the filter to the position start index + decimation and filter again to obtain
          the second output sample.
         5. Repeat step 4, adding each new decimation value until there are not enough
         samples in X1 for filtering. Store the final samples to internal states and wait for the
          next signal block. The time interval between two adjacent samples in an output
           signal is equal to decimation / interpolation. t0 specifies the time of the first

4538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4539 ordinal=4539 -->
## Functions

Functions

   output sample.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\
   Rational Resampling.vi

RationalRational ResampleResample (multi-channel,(multi-channel, DBL)DBL) VIVI

Resamples the input signal X by interpolating X, passing the interpolated signal
through an FIR filter, and decimating the filtered signal. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       anti-aliasing? —

     anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
    downsamples the signal.

       If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
    the computation requirements increase during resampling.

   •       reset —

    reset controls the initialization of resampling. The default is FALSE.

    The first time this VI runs or when reset is TRUE, LabVIEW initializes the internal states of the VI
    to zero and uses start index to determine when the resampling starts. The next time this VI runs
    and reset is FALSE, LabVIEW initializes the internal states to the final states from the previous call
    to this VI.


                                                    © National Instruments 4539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4540 ordinal=4540 -->
## Functions

Functions


           To process a large data sequence that consists of smaller blocks, set reset to TRUE for the first
            block and to FALSE for all the remaining blocks in continuous resampling.

               •     X —

          X contains the input real signals for resampling. Each row of X contains an input signal. All the
             signals have the same length. The sampling interval of each signal in X is 1.

               •       start index —

              start index determines where the resampling starts for the first call to the VI or if reset is TRUE.
            Set the start index according to the signal after X is interpolated. start index must be greater
           than or equal to 0. The default is 0.

               •      resample factor —

           resample factor contains the interpolation factor and the decimation factor for resampling.

                     •       interpolation —

                 interpolation is the interpolation factor for resampling. The default is 1.

                     •      decimation —

               decimation is the decimation factor for resampling. The default is 1.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —


4540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4541 ordinal=4541 -->
## Functions

Functions


        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the resampled signals. Each row of Y contains a resampled signal that corresponds to
    the input signal in the same row of X. All the resampled signals have the same length. The
    sampling interval of each signal is decimation/interpolation.

   •       t0 —

    t0 returns the time instance for the first sample of each signal in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following steps describe the rational resampling process. Each step corresponds
to a numbered section of the following image.


                                                    © National Instruments 4541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4542 ordinal=4542 -->
## Functions

Functions


         1. Input signal X for resampling. The time interval between two adjacent samples is 1.
         2. Insert zeros between every two adjacent samples to upsample X by the
           interpolation factor. Let X1 represent the interpolated signal.
         3. Using a FIR filter, filter X1at the start index to obtain the first output sample. The
          elements outside the range of the interpolated signal equal zero.
         4. Move the filter to the position start index + decimation and filter again to obtain
          the second output sample.
         5. Repeat step 4, adding each new decimation value until there are not enough
         samples in X1 for filtering. Store the final samples to internal states and wait for the
          next signal block. The time interval between two adjacent samples in an output
           signal is equal to decimation / interpolation. t0 specifies the time of the first

4542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4543 ordinal=4543 -->
## Functions

Functions

   output sample.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\
   Rational Resampling.vi

RationalRational ResampleResample (multi-channel,(multi-channel, CDB)CDB) VIVI

Resamples the input signal X by interpolating X, passing the interpolated signal
through an FIR filter, and decimating the filtered signal. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       anti-aliasing? —

     anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
    downsamples the signal.

       If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
    the computation requirements increase during resampling.

   •       reset —

    reset controls the initialization of resampling. The default is FALSE.

    The first time this VI runs or when reset is TRUE, LabVIEW initializes the internal states of the VI
    to zero and uses start index to determine when the resampling starts. The next time this VI runs
    and reset is FALSE, LabVIEW initializes the internal states to the final states from the previous call
    to this VI.


                                                    © National Instruments 4543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4544 ordinal=4544 -->
## Functions

Functions


           To process a large data sequence that consists of smaller blocks, set reset to TRUE for the first
            block and to FALSE for all the remaining blocks in continuous resampling.

               •     X —

          X contains the input complex signals for resampling. Each row of X contains an input signal. All
            the signals have the same length. The sampling interval of each signal is 1.

               •       start index —

              start index determines where the resampling starts for the first call to the VI or if reset is TRUE.
            Set the start index according to the signal after X is interpolated. start index must be greater
           than or equal to 0. The default is 0.

               •      resample factor —

           resample factor contains the interpolation factor and the decimation factor for resampling.

                     •       interpolation —

                 interpolation is the interpolation factor for resampling. The default is 1.

                     •      decimation —

               decimation is the decimation factor for resampling. The default is 1.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —


4544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4545 ordinal=4545 -->
## Functions

Functions


        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the resampled signals. Each row of Y contains a resampled signal that corresponds to
    the input signal in the same row of X. All the resampled signals have the same length. The
    sampling interval of each signal is decimation/interpolation.

   •       t0 —

    t0 returns the time instance for the first sample of each signal in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following steps describe the rational resampling process. Each step corresponds
to a numbered section of the following image.


                                                    © National Instruments 4545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4546 ordinal=4546 -->
## Functions

Functions


         1. Input signal X for resampling. The time interval between two adjacent samples is 1.
         2. Insert zeros between every two adjacent samples to upsample X by the
           interpolation factor. Let X1 represent the interpolated signal.
         3. Using a FIR filter, filter X1at the start index to obtain the first output sample. The
          elements outside the range of the interpolated signal equal zero.
         4. Move the filter to the position start index + decimation and filter again to obtain
          the second output sample.
         5. Repeat step 4, adding each new decimation value until there are not enough
         samples in X1 for filtering. Store the final samples to internal states and wait for the
          next signal block. The time interval between two adjacent samples in an output
           signal is equal to decimation / interpolation. t0 specifies the time of the first

4546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4547 ordinal=4547 -->
## Functions

Functions

   output sample.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\
   Rational Resampling.vi

ResampleResample (constant(constant toto constant)constant)

Resamples input signal X according to delay and dt using an FIR filter implementation.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


  • Resample (constant to constant,single -channel) VI
  • Resample (constant to constant,multi-channel) VI
  • Resample (constant to constant, complex single-channel) VI
  • Resample (constant to constant, complex multi-channel) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Constant-to-Constant Resampling.vi

ResampleResample (constant(constant toto constant,singleconstant,single -channel)-channel) VIVI

Resamples input signal X according to delay and dt using an FIR filter implementation.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


                                                    © National Instruments 4547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4548 ordinal=4548 -->
## Functions

Functions


      Inputs/Outputs

               •       anti-aliasing? —

             anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
          downsamples the signal.

                    If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
            the computation requirements increase during resampling.

               •       reset? —

             reset? controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
         When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
               call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
              this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
             blocks.

               •     X —

          X contains the input signal for resampling. The sampling interval of X is 1.

               •      delay —

            delay specifies the timestamp for Y.

               •      dt —

            dt specifies the sampling interval for Y.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —


4548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4549 ordinal=4549 -->
## Functions

Functions


    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
         instead. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the resampled signal.

   •       t0 —

    t0 returns the time instance for the first sample in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Constant-to-Constant Resampling.vi

ResampleResample (constant(constant toto constant,multi-channel)constant,multi-channel) VIVI

Resamples input signal X according to delay and dt using an FIR filter implementation.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


                                                    © National Instruments 4549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4550 ordinal=4550 -->
## Functions

Functions


      Inputs/Outputs

               •       anti-aliasing? —

             anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
          downsamples the signal.

                    If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
            the computation requirements increase during resampling.

               •       reset? —

             reset? controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
         When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
               call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
              this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
             blocks.

               •     X —

          X contains the input signals for resampling. Each row of X contains an input signal. All the signals
           have the same length. The sampling interval of each signal in X is 1.

               •      delay —

            delay specifies the timestamp for Y.

               •      dt —

            dt specifies the sampling interval for Y.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


4550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4551 ordinal=4551 -->
## Functions

Functions

   •      FIR filter specifications —

    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
         instead. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the resampled signals. Each row of Y contains a resampled signal that corresponds to
    the input signal in the same row of X. All the signals have the same length.

   •       t0 —

    t0 returns the time instance for the first sample in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Constant-to-Constant Resampling.vi

ResampleResample (constant(constant toto constant,constant, complexcomplex single-channel)single-channel) VIVI

Resamples input signal X according to delay and dt using an FIR filter implementation.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.

                                                    © National Instruments 4551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4552 ordinal=4552 -->
## Functions

Functions


      Inputs/Outputs

               •       anti-aliasing? —

             anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
          downsamples the signal.

                    If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
            the computation requirements increase during resampling.

               •       reset? —

             reset? controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
         When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
               call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
              this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
             blocks.

               •     X —

          X contains the complex input signal for resampling. The sampling interval of X is 1.

               •      delay —

            delay specifies the timestamp for Y.

               •      dt —

            dt specifies the sampling interval for Y.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


4552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4553 ordinal=4553 -->
## Functions

Functions

   •      FIR filter specifications —

    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
         instead. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the complex resampled signal.

   •       t0 —

    t0 returns the time instance for the first sample in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Constant-to-Constant Resampling.vi

ResampleResample (constant(constant toto constant,constant, complexcomplex multi-channel)multi-channel) VIVI

Resamples input signal X according to delay and dt using an FIR filter implementation.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


                                                    © National Instruments 4553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4554 ordinal=4554 -->
## Functions

Functions


      Inputs/Outputs

               •       anti-aliasing? —

             anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
          downsamples the signal.

                    If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
            the computation requirements increase during resampling.

               •       reset? —

             reset? controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
         When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
               call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
              this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
             blocks.

               •     X —

          X contains the input real signals for resampling. Each row of X contains an input signal. All the
             signals have the same length. The sampling interval of each signal in X is 1.

               •      delay —

            delay specifies the timestamp for Y.

               •      dt —

            dt specifies the sampling interval for Y.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


4554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4555 ordinal=4555 -->
## Functions

Functions


    standard error in functionality.

   •      FIR filter specifications —

    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
         instead. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      Y —

    Y returns the resampled signals. Each row of Y contains a resampled signal that corresponds to
    the input signal in the same row of X. All the signals have the same length.

   •       t0 —

    t0 returns the time instance for the first sample in Y.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Constant-to-Constant Resampling.vi

ResampleResample (constant(constant toto variable)variable)

Resamples input signal X according to Time using an FIR filter implementation. Wire

                                                    © National Instruments 4555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4556 ordinal=4556 -->
## Functions

Functions

       data to the X input to determine the polymorphic instance to use or manually select
       the instance.


            • Resample (constant to variable,single-channel) VI
            • Resample (constant to variable, multi-channel) VI
            • Resample (constant to variable, complex single-channel) VI
            • Resample (constant to variable, complex multi-channel) VI

      To calculate a resampled signal at time t, this VI needs several pieces of original signal
       data both before and after t. The FIR filter specifications determine the number of
       pieces of signal data before and after tthat this VI needs. If tis close to the end of the
       input signal, this VI might not have enough data after tto calculate the resampled
        signal. However, if you use this VI in online applications in which you continuously
       acquire data, this VI can calculate the resampled signal at twhen the next input signal
       block is available. Therefore, in the first input signal block, Time Stamps loses data for
    tat the end of the array. In the next input signal block, Time Stamps has tas
       additional data at the beginning of the array.

      ResampleResample (constant(constant toto variable,single-channel)variable,single-channel) VIVI

      Resamples input signal X according to Time using an FIR filter implementation. Wire
       data to the X input to determine the polymorphic instance to use or manually select
       the instance.


      Inputs/Outputs

               •       anti-aliasing? —


4556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4557 ordinal=4557 -->
## Functions

Functions


  anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
  downsamples the signal.

   If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
  the computation requirements increase during resampling.

•       reset? —

  reset? controls the initialization of the internal states. The default is FALSE.

  The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
  When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
   call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
   this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
  blocks.

•     X —

  X contains the input signal for resampling. The sampling interval of X is 1.

•     Time —

  Time specifies the time instances for resampling in ascending order.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      FIR filter specifications —

  FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

      •       alias rejection (dB) —

       alias rejection (dB) specifies the minimum attenuation level of signal components aliased
       after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
       instead. The default is 120.

      •      normalized bandwidth —

      normalized bandwidth specifies the fraction of the new sampling rate that is not


                                                   © National Instruments 4557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4558 ordinal=4558 -->
## Functions

Functions


                 attenuated. The default is 0.4536.


               •      Y —

           Y returns the resampled signal.

               •     Time Stamps —

          Time Stamps returns the time instance for each sample of every resampled signal in Y. The
          number of elements in Time Stamps is equal to the number of columns in Y. The contents of the
          Time input determine the contents of Time Stamps. As a result of the internal state of the
            resampling filter, Time Stamps might have additional data at the beginning of the array and
           might lose some data at the end of the array.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      To calculate a resampled signal at time t, this VI needs several pieces of original signal
       data both before and after t. The FIR filter specifications determine the number of
       pieces of signal data before and after tthat this VI needs. If tis close to the end of the
       input signal, this VI might not have enough data after tto calculate the resampled
        signal. However, if you use this VI in online applications in which you continuously
       acquire data, this VI can calculate the resampled signal at twhen the next input signal
       block is available. Therefore, in the first input signal block, Time Stamps loses data for
    tat the end of the array. In the next input signal block, Time Stamps has tas
       additional data at the beginning of the array.

      ResampleResample (constant(constant toto variable,variable, multi-channel)multi-channel) VIVI

      Resamples input signal X according to Time using an FIR filter implementation. Wire
       data to the X input to determine the polymorphic instance to use or manually select
       the instance.


4558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4559 ordinal=4559 -->
## Functions

Functions


Inputs/Outputs

   •       anti-aliasing? —

     anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
    downsamples the signal.

       If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
    the computation requirements increase during resampling.

   •       reset? —

    reset? controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
   When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
     call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
     this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
    blocks.

   •     X —

    X contains the input signals for resampling. Each row of X contains an input signal. All the signals
    have the same length. The sampling interval of each signal in X is 1.

   •     Time —

    Time specifies the time instances for resampling in ascending order.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      FIR filter specifications —

    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.


                                                    © National Instruments 4559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4560 ordinal=4560 -->
## Functions

Functions


                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
                  instead. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •      Y —

           Y returns the resampled signals. Each row of Y contains a resampled signal that corresponds to
            the input signal in the same row of X. All the signals have the same length.

               •     Time Stamps —

          Time Stamps returns the time instance for each sample of every resampled signal in Y. The
          number of elements in Time Stamps is equal to the number of columns in Y. The contents of the
          Time input determine the contents of Time Stamps. As a result of the internal state of the
            resampling filter, Time Stamps might have additional data at the beginning of the array and
           might lose some data at the end of the array.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      To calculate a resampled signal at time t, this VI needs several pieces of original signal
       data both before and after t. The FIR filter specifications determine the number of
       pieces of signal data before and after tthat this VI needs. If tis close to the end of the
       input signal, this VI might not have enough data after tto calculate the resampled
        signal. However, if you use this VI in online applications in which you continuously
       acquire data, this VI can calculate the resampled signal at twhen the next input signal
       block is available. Therefore, in the first input signal block, Time Stamps loses data for
    tat the end of the array. In the next input signal block, Time Stamps has tas
       additional data at the beginning of the array.


4560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4561 ordinal=4561 -->
## Functions

Functions

ResampleResample (constant(constant toto variable,variable, complexcomplex single-channel)single-channel) VIVI

Resamples input signal X according to Time using an FIR filter implementation. Wire
data to the X input to determine the polymorphic instance to use or manually select
the instance.


Inputs/Outputs

   •       anti-aliasing? —

     anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
    downsamples the signal.

       If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
    the computation requirements increase during resampling.

   •       reset? —

    reset? controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
   When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
     call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
     this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
    blocks.

   •     X —

    X contains the complex input signal for resampling. The sampling interval of X is 1.

   •     Time —

    Time specifies the time instances for resampling in ascending order.

   •       error in (no error) —


                                                    © National Instruments 4561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4562 ordinal=4562 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
                  instead. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •      Y —

           Y returns the complex resampled signal.

               •     Time Stamps —

          Time Stamps returns the time instance for each sample of every resampled signal in Y. The
          number of elements in Time Stamps is equal to the number of columns in Y. The contents of the
          Time input determine the contents of Time Stamps. As a result of the internal state of the
            resampling filter, Time Stamps might have additional data at the beginning of the array and
           might lose some data at the end of the array.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      To calculate a resampled signal at time t, this VI needs several pieces of original signal
       data both before and after t. The FIR filter specifications determine the number of
       pieces of signal data before and after tthat this VI needs. If tis close to the end of the
       input signal, this VI might not have enough data after tto calculate the resampled
        signal. However, if you use this VI in online applications in which you continuously


4562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4563 ordinal=4563 -->
## Functions

Functions

acquire data, this VI can calculate the resampled signal at twhen the next input signal
block is available. Therefore, in the first input signal block, Time Stamps loses data for
tat the end of the array. In the next input signal block, Time Stamps has tas
additional data at the beginning of the array.

ResampleResample (constant(constant toto variable,variable, complexcomplex multi-channel)multi-channel) VIVI

Resamples input signal X according to Time using an FIR filter implementation. Wire
data to the X input to determine the polymorphic instance to use or manually select
the instance.


Inputs/Outputs

   •       anti-aliasing? —

     anti-aliasing? specifies whether the input signal undergoes lowpass filtering when LabVIEW
    downsamples the signal.

       If anti-aliasing? is TRUE (default), this VI protects the resampled signal from aliasing. However,
    the computation requirements increase during resampling.

   •       reset? —

     reset? controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or when reset? is TRUE, LabVIEW initializes the internal states to zero.
   When reset? is FALSE, LabVIEW initializes the internal states to the final states from the previous
     call to this instance of this VI. To process a large data sequence consisting of smaller blocks, set
     this control to TRUE for the first block and to FALSE for continuous filtering of all remaining
     blocks.

   •     X —

    X contains the input real signals for resampling. Each row of X contains an input signal. All the


                                                    © National Instruments 4563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4564 ordinal=4564 -->
## Functions

Functions


             signals have the same length. The sampling interval of each signal in X is 1.

               •     Time —

          Time specifies the time instances for resampling in ascending order.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. If alias rejection (dB) is less than 48, this VI will use 48
                  instead. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •      Y —

           Y returns the resampled signals. Each row of Y contains a resampled signal that corresponds to
            the input signal in the same row of X. All the signals have the same length.

               •     Time Stamps —

          Time Stamps returns the time instance for each sample of every resampled signal in Y. The
          number of elements in Time Stamps is equal to the number of columns in Y. The contents of the
          Time input determine the contents of Time Stamps. As a result of the internal state of the
            resampling filter, Time Stamps might have additional data at the beginning of the array and
           might lose some data at the end of the array.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


4564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4565 ordinal=4565 -->
## Functions

Functions

To calculate a resampled signal at time t, this VI needs several pieces of original signal
data both before and after t. The FIR filter specifications determine the number of
pieces of signal data before and after tthat this VI needs. If tis close to the end of the
input signal, this VI might not have enough data after tto calculate the resampled
signal. However, if you use this VI in online applications in which you continuously
acquire data, this VI can calculate the resampled signal at twhen the next input signal
block is available. Therefore, in the first input signal block, Time Stamps loses data for
tat the end of the array. In the next input signal block, Time Stamps has tas
additional data at the beginning of the array.

UnitUnit VectorVector

Finds the norm of the Input Vector and obtains its corresponding Unit Vector by
normalizing the original Input Vector with its norm.


   • Unit Vector (DBL) VI
   • Unit Vector (CDB) VI

This VI calculates norm using the following equations.

 1-norm                           ||X|| = |x0| + |x1| + … + |xn– 1|
 2-norm                           ||X|| = √(|x0|² + |x1|² + … + |xn– 1|²)
 Inf-norm                         ||X|| = maxi(|xi|)
 –Inf-norm                        ||X|| = mini(|xi|)
 User Defined                    ||X|| = ||x0|y + |x1|y + … + |xn– 1|y|1/y

where Xis Input Vector, yis user defined norm, and ||X|| is norm.

This VI calculates Unit Vector using the following equation:


                                                    © National Instruments 4565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4566 ordinal=4566 -->
## Functions

Functions


      where Uis Unit Vector.

      UnitUnit VectorVector (DBL)(DBL) VIVI

       Finds the norm of the Input Vector and obtains its corresponding Unit Vector by
       normalizing the original Input Vector with its norm.


      Inputs/Outputs

               •      Input Vector —

            Input Vector is the input vector. If Input Vector is an empty array, Unit Vector is also an empty
              array, and norm is NaN.

               •     norm type —

         norm type indicates what type of norm you use to compute the norm. The default is 2-norm. If
         norm type is User Defined, this VI uses user defined norm as the norm type.

           1     1-norm
           2     2-norm (default)
           3     Inf-norm
           4     –Inf-norm
           5     User Defined

               •      user defined norm —

            user defined norm is the user defined norm type. The default is –1. This VI uses user defined
         norm as the norm type only if you set norm type to User Defined.

            user defined norm must be nonzero.

               •      Unit Vector —


4566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4567 ordinal=4567 -->
## Functions

Functions


    Unit Vector is the output, normalized vector.

   •     norm —

   norm is the norm of Input Vector.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI calculates norm using the following equations.

 1-norm                           ||X|| = |x0| + |x1| + … + |xn– 1|
 2-norm                           ||X|| = √(|x0|² + |x1|² + … + |xn– 1|²)
 Inf-norm                         ||X|| = maxi(|xi|)
 –Inf-norm                        ||X|| = mini(|xi|)
 User Defined                    ||X|| = ||x0|y + |x1|y + … + |xn– 1|y|1/y

where Xis Input Vector, yis user defined norm, and ||X|| is norm.

This VI calculates Unit Vector using the following equation:


where Uis Unit Vector.

UnitUnit VectorVector (CDB)(CDB) VIVI

Finds the norm of the Input Vector and obtains its corresponding Unit Vector by
normalizing the original Input Vector with its norm.


                                                    © National Instruments 4567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4568 ordinal=4568 -->
## Functions

Functions


      Inputs/Outputs

               •      Input Vector —

            Input Vector is the input vector. If Input Vector is an empty array, Unit Vector is also an empty
              array, and norm is NaN.

               •     norm type —

         norm type indicates what type of norm you use to compute the norm. The default is 2-norm. If
         norm type is User Defined, this VI uses user defined norm as the norm type.

           1     1-norm
           2     2-norm (default)
           3     Inf-norm
           4     –Inf-norm
           5     User Defined

               •      user defined norm —

            user defined norm is the user defined norm type. The default is –1. This VI uses user defined
         norm as the norm type only if you set norm type to User Defined.

            user defined norm must be nonzero.

               •      Unit Vector —

            Unit Vector is the output, normalized vector.

               •     norm —

         norm is the norm of Input Vector.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI calculates norm using the following equations.

4568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4569 ordinal=4569 -->
## Functions

Functions


 1-norm                           ||X|| = |x0| + |x1| + … + |xn– 1|
 2-norm                           ||X|| = √(|x0|² + |x1|² + … + |xn– 1|²)
 Inf-norm                         ||X|| = maxi(|xi|)
 –Inf-norm                        ||X|| = mini(|xi|)
 User Defined                    ||X|| = ||x0|y + |x1|y + … + |xn– 1|y|1/y

where Xis Input Vector, yis user defined norm, and ||X|| is norm.

This VI calculates Unit Vector using the following equation:


where Uis Unit Vector.

ScaleScale

Removes the offset of an input signal X and then scales the result so that the output
sequence is in the range [–1:1].


  • Scale 1D VI
  • Scale 2D VI

You can use this VI to normalize any numerical sequence with the assurance that the
range of the output sequence is [–1:1].

If X is an array of zeros, this VI returns scale as 1, offset as 0, and Y=(X–offset)/scale as
an array of zeros.

Scale 1D

This VI calculates Y=(X–offset)/scale using the following equations:

                                                    © National Instruments 4569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4570 ordinal=4570 -->
## Functions

Functions

                   scale = 0.5(max – min) offset = min + scale

      where max denotes the maximum value in X and min denotes the minimum value in X.

      The following equation defines each element of Y.

         Y[i] = (X[i] – offset)/scale
      Scale 2D

       This VI calculates Y=(X-offset)/scale using the following equations:

                   scale = 0.5(max - min) offset = min + 0.5 scale

      where max denotes the maximum value in X and min denotes the minimum value in X.

      The following equation defines each element of Y.

          Y[i,j] = (X[i,j] – offset)/scale.
      ScaleScale 1D1D VIVI

      Removes the offset of an input signal X and then scales the result so that the output
      sequence is in the range [–1:1].


      Inputs/Outputs

               •     X —

          X is the input array.

               •       Y=(X-offset)/scale —

             Y=(X-offset)/scale is the output array of the same size as X.

               •       scale —

4570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4571 ordinal=4571 -->
## Functions

Functions


    scale is the scaling factor.

   •       offset —

     offset is the offset factor.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI calculates Y=(X-offset)/scale using the following equations:

            scale = 0.5(max – min) offset = min + scale

where max denotes the maximum value in X and min denotes the minimum value in X.

The following equation defines each element of Y.

Y[i] = (X[i] – offset)/scale

You can use this VI to normalize any numerical sequence with the assurance that the
range of the output sequence is [–1:1].

ScaleScale 2D2D VIVI

Removes the offset of an input signal X and then scales the result so that the output
sequence is in the range [–1:1].


Inputs/Outputs

   •     X —


                                                    © National Instruments 4571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4572 ordinal=4572 -->
## Functions

Functions


          X is the 2D input array.

               •       Y=(X-offset)/scale —

             Y=(X-offset)/scale is the output array of the same size as X.

               •       scale —

             scale is the scaling factor.

               •       offset —

             offset is the offset factor.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      You can use this VI to normalize any numerical sequence with the assurance that the
      range of the output sequence is [–1:1].

           If X is an array of zeros, this VI returns scale as 1, offset as 0, and Y=(X–offset)/scale as
      an array of zeros.

      Scale 1D

       This VI calculates Y=(X–offset)/scale using the following equations:

                   scale = 0.5(max – min) offset = min + scale

      where max denotes the maximum value in X and min denotes the minimum value in X.

      The following equation defines each element of Y.

         Y[i] = (X[i] – offset)/scale
      Scale 2D

       This VI calculates Y=(X-offset)/scale using the following equations:

4572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4573 ordinal=4573 -->
## Functions

Functions

            scale = 0.5(max - min) offset = min + 0.5 scale

where max denotes the maximum value in X and min denotes the minimum value in X.

The following equation defines each element of Y.

Y[i,j] = (X[i,j] – offset)/scale.
QuickQuick ScaleScale

Determines the maximum absolute value of the input X and then scales X using this
value.


  • Quick Scale 1D VI
  • Quick Scale 2D VI

You can use this VI to normalize sequences within the range [–1:1]. This VI is
particularly useful if the sequence is a zero mean sequence.

Quick Scale 1D

This VI calculates Y[i]=X[i]/Max|X| using the following equation:


where sis the maximum absolute value in X.

If X is an array of zeros, this VI returns max|X| as 0 and Y[i]=X[i]/Max|X| as an array of
zeros.

Quick Scale 2D

This VI calculates Yij=Xij/Max|X| using the following equation:


                                                    © National Instruments 4573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4574 ordinal=4574 -->
## Functions

Functions

      where sdenotes the maximum absolute value in X.

           If X is an array of zeros, this VI returns max|X| as 0 and Yij=Xij/Max|X| as an array of
       zeros.

      QuickQuick ScaleScale 1D1D VIVI

      Determines the maximum absolute value of the input X and then scales X using this
       value.


      Inputs/Outputs

               •     X —

          X is the input array.

               •       Y[i]=X[i]/Max|X| —

             Y[i]=X[i]/Max|X| is the output array of the same size as X.

               •      max|X| —

           max|X| is the maximum absolute value in the input array X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI calculates Y[i]=X[i]/Max|X| using the following equation:


      where sis the maximum absolute value in X.

      You can use this VI to normalize sequences within the range [–1:1]. This VI is

4574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4575 ordinal=4575 -->
## Functions

Functions

particularly useful if the sequence is a zero mean sequence.

QuickQuick ScaleScale 2D2D VIVI

Determines the maximum absolute value of the input X and then scales X using this
value.


Inputs/Outputs

   •     X —

    X is the 2D input array.

   •       Yij=Xij/Max|X| —

     Yij=Xij/Max|X| is the 2D output array of the same size as X.

   •      max|X| —

    max|X| is the maximum absolute value in the input array X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


You can use this VI to normalize sequences within the range [–1:1]. This VI is
particularly useful if the sequence is a zero mean sequence.

Quick Scale 1D

This VI calculates Y[i]=X[i]/Max|X| using the following equation:


where sis the maximum absolute value in X.

                                                    © National Instruments 4575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4576 ordinal=4576 -->
## Functions

Functions

           If X is an array of zeros, this VI returns max|X| as 0 and Y[i]=X[i]/Max|X| as an array of
       zeros.

     Quick Scale 2D

       This VI calculates Yij=Xij/Max|X| using the following equation:


      where sdenotes the maximum absolute value in X.

           If X is an array of zeros, this VI returns max|X| as 0 and Yij=Xij/Max|X| as an array of
       zeros.

     NormalizeNormalize

       Normalizes the input vector or matrix using its statistical profile (µ,s), where µ is the
     mean and sis the standard deviation, to obtain a Normalized Vector or Normalized
       Matrix whose statistical profile is (0,1).


            • Normalize Vector VI
            • Normalize Matrix VI

     Normalize Vector

       This VI calculates Normalized Vector using the following equation:


      where Yrepresents the output sequence Normalized Vector, Xrepresents the input
      sequence Vector of length n, and xi is the ith element of X.

4576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4577 ordinal=4577 -->
## Functions

Functions

Normalize Matrix

This VI calculates Normalized Matrix using the following equation:


where Brepresents the 2D output sequence Normalized Matrix, Arepresents the 2D
input sequence Matrix with nrows and mcolumns, and aij is the element of Aon the
ith row and jth column.

NormalizeNormalize VectorVector VIVI

Normalizes the input vector or matrix using its statistical profile (µ,s), where µ is the
mean and sis the standard deviation, to obtain a Normalized Vector or Normalized
Matrix whose statistical profile is (0,1).


Inputs/Outputs

   •      Vector —

    Vector is the input vector. If Vector is an empty array, Normalized Vector is also an empty array,
    and mean and standard deviation are NaN.

   •      Normalized Vector —

    Normalized Vector is the output normalized vector.

   •      standard deviation —

    standard deviation is the standard deviation of Vector.

   •     mean —

                                                    © National Instruments 4577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4578 ordinal=4578 -->
## Functions

Functions


         mean is the mean of Vector.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI calculates Normalized Vector using the following equation:


      where Yrepresents the output sequence Normalized Vector, Xrepresents the input
      sequence Vector of length n, and xi is the ith element of X.

      NormalizeNormalize MatrixMatrix VIVI

       Normalizes the input vector or matrix using its statistical profile (µ,s), where µ is the
     mean and sis the standard deviation, to obtain a Normalized Vector or Normalized
       Matrix whose statistical profile is (0,1).


      Inputs/Outputs

               •      Matrix —

            Matrix is the 2D input matrix. If Matrix is an empty array, Normalized Matrix is also an empty
              array, and mean and standard deviation are NaN.

               •      Normalized Matrix —

           Normalized Matrix is the output normalized matrix.


4578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4579 ordinal=4579 -->
## Functions

Functions

   •      standard deviation —

    standard deviation is the standard deviation of Matrix.

   •     mean —

   mean is the mean of Matrix.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Normalize Vector

This VI calculates Normalized Vector using the following equation:


where Yrepresents the output sequence Normalized Vector, Xrepresents the input
sequence Vector of length n, and xi is the ith element of X.

Normalize Matrix

This VI calculates Normalized Matrix using the following equation:


where Brepresents the 2D output sequence Normalized Matrix, Arepresents the 2D
input sequence Matrix with nrows and mcolumns, and aij is the element of Aon the
ith row and jth column.


                                                    © National Instruments 4579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4580 ordinal=4580 -->
## Functions

Functions

       Y[i]=Clip{X[i]}Y[i]=Clip{X[i]}

       Clips the elements of Input Array to within the bounds specified by upper limit and
      lower limit.


      Inputs/Outputs

               •      Input Array —

            Input Array is the input array to be clipped.

               •      upper limit —

           upper limit must be greater than or equal to lower limit. The default is 1.0.

                    If upper limit is less than lower limit, the VI sets the sequence Clipped Array to an empty array
          and returns an error.

               •      lower limit —

           lower limit must be less than or equal to upper limit. The default is 0.0.

               •      Clipped Array —

            Clipped Array is the Input Array subjected to upper limit and lower limit.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let the sequence Yrepresent the output sequence Clipped Array. Then the elements
       of Yare related to the elements of Input Array by


4580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4581 ordinal=4581 -->
## Functions

Functions

for i= 0, 1, 2, …, n– 1,

where nis the number of elements in Input Array, ais the upper limit, and bis the
lower limit.

RiffleRiffle

Riffles the elements in the input array X. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


  •  Riffle Array (DBL) VI
  •  Riffle Array (CDB) VI
  •  Riffle Array (I32) VI

This VI riffles the input array by randomly selecting two elements in X, swapping those
elements, and then repeating this process ntimes, where nis the length of X.

RiffleRiffle ArrayArray (DBL)(DBL) VIVI

Riffles the elements in the input array X. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the real input array to riffle.

   •      seed —

    seed is the seed value at which to riffle X. The default is –1.


                                                    © National Instruments 4581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4582 ordinal=4582 -->
## Functions

Functions

               •       Riffled {X} —

              Riffled {X} returns X with riffled elements.

               •       Riffled Index —

              Riffled Index returns the corresponding index in X for each element in Riffled {X}.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI riffles the input array by randomly selecting two elements in X, swapping those
       elements, and then repeating this process ntimes, where nis the length of X.

        RiffleRiffle ArrayArray (CDB)(CDB) VIVI

        Riffles the elements in the input array X. Wire data to the X input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex input array to riffle.

               •      seed —

           seed is the seed value at which to riffle X. The default is –1.

               •       Riffled {X} —

              Riffled {X} returns X with riffled elements.

               •       Riffled Index —


4582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4583 ordinal=4583 -->
## Functions

Functions


     Riffled Index returns the corresponding index in X for each element in Riffled {X}.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI riffles the input array by randomly selecting two elements in X, swapping those
elements, and then repeating this process ntimes, where nis the length of X.

RiffleRiffle ArrayArray (I32)(I32) VIVI

Riffles the elements in the input array X. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the integer input array to riffle.

   •      seed —

    seed is the seed value at which to riffle X. The default is –1.

   •       Riffled {X} —

     Riffled {X} returns X with riffled elements.

   •       Riffled Index —

     Riffled Index returns the corresponding index in X for each element in Riffled {X}.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 4583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4584 ordinal=4584 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


       This VI riffles the input array by randomly selecting two elements in X, swapping those
       elements, and then repeating this process ntimes, where nis the length of X.

    ACAC &amp;&amp; DCDC EstimatorEstimator

       Estimates the AC and DC levels of the input Signal.

       This VI performs spectral analysis by separating DC (bin 0) from AC (the rms sum of the
        rest of the bins).


      Inputs/Outputs

               •      Signal (V) —

            Signal specifies the input time-domain signal, usually in volts.

          The time-domain record must contain at least three cycles of the signal for a valid estimate.

               •     AC estimate (Vrms) —

          AC estimate returns the estimate of the input signal AC level in volts rms when the input Signal
                is in volts.

               •     DC estimate (V) —

         DC estimate returns the estimate of the input signal DC level in volts if the input Signal is in
               volts.


      You often need to measure the AC and DC content of signals you digitize. This VI
       applies the Hanning window, which is sufficient for separating most of the AC energy
      from the DC bin. If you have a periodic signal and you do not have an integral number
       of periods in the acquisition, spectral spreading occurs regardless of whether you


4584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4585 ordinal=4585 -->
## Functions

Functions

perform an FFT later. The coherent gain and equivalent noise bandwidth constants for
the Hanning window that this VI uses compensate for windowing effects on the gain
and bandwidth.

LabVIEW uses the efficient mean and variance computations instead of Fourier
analysis to determine the total AC energy and the true DC level.

PeakPeak DetectorDetector VIVI

Finds the location, amplitude, and second derivative of peaks or valleys in the input
signal.


Inputs/Outputs

   •     X —

    X is the array of input values that represents the signal to be analyzed.

    The data can be a single array or consecutive blocks of data. Consecutive blocks of data are
    useful for large data arrays or for real time processing. Notice that in real time processing, peaks/
    valleys are not detected until approximately width/2 data points past the peak or valley.

   •      threshold —

    threshold instructs the VI to ignore peaks and valleys that are too small. The VI ignores peaks if
    the fitted amplitude is less than threshold. The VI ignores valleys if the fitted trough is greater
    than threshold.

   •      width —

    width specifies the number of consecutive data points to use in the quadratic least squares fit.
    width is coerced to a value greater than or equal to 3.

    The value should be no more than about 1/2 of the width of the peaks above threshold or


                                                    © National Instruments 4585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4586 ordinal=4586 -->
## Functions

Functions


             valleys below threshold and can be much smaller (but > 2) for noise-free data. Large widths can
           reduce the apparent amplitude of peaks and shift the apparent location. For noisy data, this
            modification is unimportant since the noise obscures the actual peak. Ideally, width should be
            as small as possible but must be balanced against the possibility of false peak detection due to
             noise.

               •      peaks/valleys —

            peaks/valleys specifies whether the VI looks for peaks or valleys in the input signal.

           0            Peaks
           1              Valleys

               •        initialize (T) —

               initialize, when set to TRUE, specifies processing the first block of data.

          The VI requires some internal setup at the beginning for proper operation. If you only want to
            process one block of data, leave initialize unwired, or set its default state to TRUE. If you want to
            process consecutive blocks of data, set initialize to TRUE for the first block and FALSE for all
            other blocks of data.

               •     end of data (T) —

          end of data, when set to TRUE, specifies processing the last block of data.

              After processing the last block of data, the VI manages internal data. If you only want to process
          one block of data, leave end of data unwired, or set its default state to TRUE. If you want to
            process consecutive blocks of data, set end of data to FALSE for all but the last block of data.

               •      # found —

           # found is the number of peaks/valleys found in the current block of data. # found is the size of
            the arrays Locations, Amplitudes, and 2nd Derivatives.

               •      Locations —

            Locations contains the index locations of all peaks or valleys detected in the current block of
             data.

           Because the peak detection algorithm uses a quadratic fit to find the peaks, it actually
             interpolates between the data points. Therefore, the indexes are not integers. In other words,


4586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4587 ordinal=4587 -->
## Functions

Functions


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

   2nd Derivatives gives an approximate measure of the sharpness of each peak or valley. If you are
    detecting peaks, these values are all negative. If you are detecting valleys, the values are all
     positive.

          Note It is assumed that dt, the time difference between samples, is equal to 1.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The data set can be passed to the Peak Detector VI as a single array or as consecutive
blocks of data.

This Peak Detector VI is based on an algorithm that fits a quadratic polynomial to
sequential groups of data points. The number of data points used in the fit is specified
by width.

For each peak or valley, the quadratic fit is tested against the threshold. Peaks with
heights lower than the threshold or valleys with troughs higher than the threshold are
ignored. Peaks and valleys are detected only after the VI processes approximately


                                                    © National Instruments 4587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4588 ordinal=4588 -->
## Functions

Functions

      width/2 data points beyond the location of the peak or valley. This delay has
       implications only for real-time processing.

      The Peak Detector VI must be notified when the first and last blocks are passed into the
         VI, so that the VI can initialize and then release data internal to the peak detection
       algorithm.

       Refer to the following support document at ni.com for more information about peak
       detection using LabVIEW.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Signal Operation\Peak
        Detection and Display.vi

     ThresholdThreshold DetectorDetector VIVI

       Analyzes the input sequence X for valid peaks and keeps a count of the number of
      peaks encountered and a record of Indices, which locates the points that exceed the
       threshold in a valid peak.


      Inputs/Outputs

               •     X —

          X is the input sequence. The number of samples in X must be greater than the specified width.

                    If X is less than or equal to width, the VI sets count to zero and returns an error.

               •      threshold —

            threshold is the level that all valid peaks must equal or exceed for the duration of width
            samples. The default is 0.0.


4588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4589 ordinal=4589 -->
## Functions

Functions

   •      width —

    width determines the minimum width, in number of samples, that the input sequence X must
    remain at or above the threshold value for the candidate peak to be considered valid. width
    must be greater than zero. If width is less than or equal to zero, the VI sets count to zero and
    returns an error. The default is 1.

   •       Indices —

    Indices contains the beginning index of all valid peaks.

   •      count —

    count is the number of valid peaks.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


A peak is valid where the consecutive elements of X exceed the threshold, and the
number of elements that exceed the threshold is equal to at least width. The
Threshold Detector VI detects the peak when the number of consecutive elements that
exceed the threshold is greater than or equal to width.

The following figure shows the threshold detector result of a sinusoid waveform,
where the threshold is 0.1 and the width is 4. The green cross represents the
beginning index of a detected peak.


                                                    © National Instruments 4589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4590 ordinal=4590 -->
## Functions

Functions


      The following figure also shows a valid peak. Here the input waveform is a step signal.
      The threshold is 0.5 and the width is 5. Since thirteen consecutive elements exceed
       the threshold, the beginning index of the peak is 8.


       Refer to the following support document at ni.com for more information about peak
       detection using LabVIEW.

     ConvolutionConvolution andand CorrelationCorrelation

      Performs convolution, deconvolution, or correlation on the input signals.

4590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4591 ordinal=4591 -->
## Functions

Functions


Dialog Box Options

 Option     Description

            Contains the following options:

                      • Convolution—

              Computes the convolution of the input signals.

                      • Deconvolution—

              Computes the deconvolution of the input signals.

                      • Autocorrelation—

              Computes the autocorrelation of the input signal.
 Signal
 Processing     • Cross correlation—

              Computes the cross correlation of the input signals.

                      • Ignore time stamp—

                  Specifies to ignore the time stamp of the input signals. This option is available
                 only when you place a checkmark in the Convolution or Deconvolution checkbox.

                           If you place a checkmark in the Ignore time stamp checkbox, the resulting signal
               has the delay you expect with classic convolution. If you do not place a checkmark
                   in the checkbox, LabVIEW shifts the resulting signal negatively in time to
               compensate for the filter length.


             Displays sample input signals you can use as a reference to determine how the
             configuration options you select affect the actual input signals.
 Sample
 Input Data   If you wire data to the Express VI and run it, Sample Input Data displays real data. If
           you close and reopen the Express VI, Sample Input Data displays sample data until
           you run the VI again.


                                                    © National Instruments 4591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4592 ordinal=4592 -->
## Functions

Functions


        Option     Description

                     Displays a preview of the measurement. The Result Preview plot indicates the value of
                    the selected measurement with a dotted line.
         Result                                 If you wire data to the Express VI and run the VI, Result Preview displays real data. If
        Preview                  you close and reopen the Express VI, Result Preview displays sample data until you
                   run the VI again. If the cutoff frequency values are invalid, Result Preview does not
                      display valid data.


      Inputs/Outputs

               •      Input1 —

            Contains the input signal X.

               •      Y —

            Contains the input signal Y.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      output signals —

            Returns the convolution of X and Y.

               •       error out —

            Contains error information. This output provides standard error out functionality.


     Components

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.

       Displays sample input signals you can use as a reference to determine how the
       configuration options you select affect the actual input signals.


4592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4593 ordinal=4593 -->
## Functions

Functions

Computes the cross correlation of the input signals.

Computes the autocorrelation of the input signal.

Computes the deconvolution of the input signals.

Computes the convolution of the input signals.

Specifies to ignore the time stamp of the input signals. This option is available only
when you place a checkmark in the Convolution or Deconvolution checkbox.

Computes the cross correlation of the input signals.

Computes the autocorrelation of the input signal.

Computes the deconvolution of the input signals.

Computes the convolution of the input signals.

ScalingScaling andand MappingMapping

Changes the amplitude of a signal by scaling or mapping the signal.


Dialog Box Options

 Option        Description

               Contains the following options:

                          • Normalize—
 Scaling or
 Mapping          Determines the scale and offset necessary to transform the signal so that its
 Type           maximum is Highest peak and its minimum is Lowest peak.

         ◦ Lowest peak—


                                                    © National Instruments 4593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4594 ordinal=4594 -->
## Functions

Functions


        Option        Description

                                   Specifies the minimum value used to normalize the signal. The default is
                                  0.

             ◦ Highest peak—

                                   Specifies the maximum value used to normalize the signal. The default is
                                  1.

                                      • Linear (Y=mX+b)—

                            Sets the scale mapping mode to be linear, which scales the signal based on a
                               straight line.

             ◦ Slope (m)—

                              Slope used for Linear (Y=mX+b) scaling. The default is 1.

             ◦ Y intercept (b)—

                                  Intercept used for Linear (Y=mX+b) scaling. The default is 0.

                                      • Logarithmic—

                            Sets the scale mapping mode to be logarithmic, which scales the signal based
                       on a decibel reference.

                        LabVIEW scales the signal using the following equation: y= 20log10(x/db
                             reference)

             ◦ db reference—

                               Reference for the Logarithmic scaling. The default is 1.

                                      • Interpolated—

                            Scales the signals based on a table of values that are interpolated linearly onto
                         a scaling factor.

             ◦ Define Table—

                                 Displays the Define Signal dialog box, which you use to define a table of


4594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4595 ordinal=4595 -->
## Functions

Functions


 Option        Description

                        values for Interpolated scaling.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Scaled Signals —

    Returns the scaled signals.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Scaling and
   Mapping.vi

Components

Displays the Define Signal dialog box, which you use to define a table of values for
Interpolated scaling.

Specifies the maximum value used to normalize the signal. The default is 1.

Specifies the minimum value used to normalize the signal. The default is 0.


                                                    © National Instruments 4595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4596 ordinal=4596 -->
## Functions

Functions

       Intercept used for Linear (Y=mX+b) scaling. The default is 0.

      Slope used for Linear (Y=mX+b) scaling. The default is 1.

      Determines the scale and offset necessary to transform the signal so that its maximum
         is Highest peak and its minimum is Lowest peak.

       Reference for the Logarithmic scaling. The default is 1.

       Sets the scale mapping mode to be logarithmic, which scales the signal based on a
       decibel reference.

       Scales the signals based on a table of values that are interpolated linearly onto a
       scaling factor.

       Sets the scale mapping mode to be linear, which scales the signal based on a straight
         line.

     Z-TransformZ-Transform DelayDelay NodeNode

       Stores data from one VI execution or loop iteration to the next. This node is the
      Feedback Node in z-transform view.


    WindowsWindows

      Use the Windows VIs to implement smoothing windows and to perform data
      windowing.

      The VIs on this palette can return signal processing error codes.


4596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4597 ordinal=4597 -->
## Functions

Functions


Palette Object  Description

Scaled Time                Applies a scaled window to the input sequence X. Wire data to the X input to
Domain               determine the polymorphic instance to use or manually select the instance.Window


Symmetric      Applies a symmetric window to the input sequence X. Wire data to the X input to
Window        determine the polymorphic instance to use or manually select the instance.


Window       Computes the coherent gain and equivalent noise bandwidth of a window. You
Properties     must manually select the polymorphic instance you want to use.


Hanning        Applies a Hanning window to the input signal X. Wire data to the X input to
Window        determine the polymorphic instance to use or manually select the instance.


Hamming       Applies a Hamming window to the input signal X. Wire data to the X input to
Window        determine the polymorphic instance to use or manually select the instance.


Blackman       Applies a Blackman window to the input signal X. Wire data to the X input to
Window        determine the polymorphic instance to use or manually select the instance.


                Applies a three-term, Blackman-Harris window to the input signal X. Wire data toBlackman-               the X input to determine the polymorphic instance to use or manually select the
Harris Window
                 instance.


Blackman-      Applies a Blackman-Nuttall window to the input sequence X. Wire data to the X
Nuttall          input to determine the polymorphic instance to use or manually select the
Window         instance.


Exact
                Applies an Exact Blackman window to the input signal X. Wire data to the X input
Blackman
                to determine the polymorphic instance to use or manually select the instance.
Window


                                                    © National Instruments 4597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4598 ordinal=4598 -->
## Functions

Functions


         Palette Object  Description

          Flat Top         Applies a flat top window to the input sequence X. Wire data to the X input to
       Window        determine the polymorphic instance to use or manually select the instance.


        General Cosine  Applies a general cosine window to the input signal X. Wire data to the X input to
       Window        determine the polymorphic instance to use or manually select the instance.


        Cosine                         Applies a cosine tapered window to the input sequence X. Wire data to the X input        Tapered
                         to determine the polymorphic instance to use or manually select the instance.       Window


                         Applies a triangular window (Bartlett Window) to the input signal X. Wire data to         Triangle                        the X input to determine the polymorphic instance to use or manually select the       Window
                          instance.


         Kaiser-Bessel    Applies a Kaiser-Bessel window to the input sequence X. Wire data to the X input
       Window         to determine the polymorphic instance to use or manually select the instance.


                         Applies an asymmetrical Gaussian window to the input sequence X. Wire data to        Gaussian                        the X input to determine the polymorphic instance to use or manually select the
       Window                          instance.


                         Applies an asymmetrical Dolph-Chebyshev window to the input sequence X. Wire
        Chebyshev
                        data to the X input to determine the polymorphic instance to use or manually
       Window
                           select the instance.


                         Applies a force window to the input signal X. Wire data to the X input to determine
         Force Window
                        the polymorphic instance to use or manually select the instance.


         Exponential     Applies an exponential window to the input signal X. Wire data to the X input to
       Window        determine the polymorphic instance to use or manually select the instance.


4598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4599 ordinal=4599 -->
## Functions

Functions


 Palette Object  Description

 Modified                 Applies a modified Bartlett-Hanning window to the input signal X. Wire data to the
 Bartlett-              X input to determine the polymorphic instance to use or manually select the Hanning                  instance. Window


 Bohman        Applies a Bohman window to the input signal X. Wire data to the X input to
 Window        determine the polymorphic instance to use or manually select the instance.


 Parzen          Applies a Parzen window to the input signal X. Wire data to the X input to
 Window        determine the polymorphic instance to use or manually select the instance.


                 Applies a Welch window to the input signal X. Wire data to the X input to Welch Window
               determine the polymorphic instance to use or manually select the instance.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Windows
   (Signal Processing).lvproj

ScaledScaled TimeTime DomainDomain WindowWindow

Applies a scaled window to the input sequence X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


  • Scaled Time Domain Window (DBL) VI
  • Scaled Time Domain Window (CDB) VI

The Scaled Time Domain Window VI scales the result so that when the power or


                                                    © National Instruments 4599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4600 ordinal=4600 -->
## Functions

Functions

      amplitude spectrum of the windowed waveform is computed, all windows provide the
     same level within the accuracy constraints of the window. The Scaled Time Domain
     Window VI also returns important window properties for the selected window. These
       properties are useful when you use VIs that perform computations on the power
       spectrum, such as the Power & Frequency Estimate VI and the Spectrum Unit
      Conversion VI.

           If yrepresents the output sequence Windowed X, the Scaled Time Domain Window VI
       obtains the elements of yfrom:

                for i= 0, 1, 2, …

      where wi and cgare the coefficients and coherent gain of the window without scaling,
        respectively.

       This VI also returns the coherent gain (CG) and equivalent noise bandwidth (ENBW) of
       the selected window. For cosine windows, these two properties are constants, as listed
        in the following table.


       Window Type             CG                        ENBW

         Rectangle                      1.0                                     1.0

        Hanning                       0.5                                     1.5

       Hamming                     0.54                                1.362826

        Blackman-Harris             0.42323                            1.708538

         Exact Blackman              0.42659071367                      1.693699

        Blackman                     0.42                                1.726757

          Flat Top                     0.215578948                        3.770246506303

        4 Term B-Harris               0.35875                            2.004353

        7 Term B-Harris              0.27105140069342415                2.631905

       Low Sidelobe                0.323215218                        2.215350782519

        Blackman Nuttall             0.3635819                          1.9761117

           If X is an empty input array and the selected window is a cosine window, this VI returns

4600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4601 ordinal=4601 -->
## Functions

Functions

the window properties. If X is an empty input array and the selected window is not a
cosine window, this VI sets the window properties to NaN and returns an error. For
Triangle, Kaiser, Dolph-Chebyshev, and Gaussian windows, the window properties
depend on the window length and the window parameters.

ScaledScaled TimeTime DomainDomain WindowWindow (DBL)(DBL) VIVI

Applies a scaled window to the input sequence X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •     window —

   window is the window to apply to X.

    0         Rectangle (default)
    1        Hanning
    2       Hamming
    3         Blackman-Harris
    4         Exact Blackman
    5        Blackman
    6           Flat Top
    7        4 Term B-Harris
    8        7 Term B-Harris
    9       Low Sidelobe
    11       Blackman Nuttall
    30         Triangle
    31        Bartlett-Hanning
    32      Bohman
    33        Parzen


                                                    © National Instruments 4601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4602 ordinal=4602 -->
## Functions

Functions


           34       Welch
           60        Kaiser
           61       Dolph-Chebyshev
           62        Gaussian

               •     window parameter —

          window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
           a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •     window properties —

          window properties returns the coherent gain and equivalent noise bandwidth of the window.

                     •     eq noise BW —

              eq noise BW returns the equivalent noise bandwidth of the window. You can use eq noise
           BW to divide a sum of individual power spectra or to compute the power in a given
                frequency span.

                     •      coherent gain —

               coherent gain returns the inverse of the scaling factor this VI applies to the window.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Scaled Time Domain Window VI scales the result so that when the power or
      amplitude spectrum of the windowed waveform is computed, all windows provide the
     same level within the accuracy constraints of the window. The Scaled Time Domain

4602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4603 ordinal=4603 -->
## Functions

Functions

Window VI also returns important window properties for the selected window. These
properties are useful when you use VIs that perform computations on the power
spectrum, such as the Power & Frequency Estimate VI and the Spectrum Unit
Conversion VI.

If yrepresents the output sequence Windowed X, the Scaled Time Domain Window VI
obtains the elements of yfrom:

        for i= 0, 1, 2, …

where wi and cgare the coefficients and coherent gain of the window without scaling,
respectively.

This VI also returns the coherent gain (CG) and equivalent noise bandwidth (ENBW) of
the selected window. For cosine windows, these two properties are constants, as listed
in the following table.


 Window Type             CG                        ENBW

 Rectangle                      1.0                                     1.0

 Hanning                       0.5                                     1.5

 Hamming                     0.54                                1.362826

 Blackman-Harris             0.42323                            1.708538

 Exact Blackman              0.42659071367                      1.693699

 Blackman                     0.42                                1.726757

 Flat Top                     0.215578948                        3.770246506303

 4 Term B-Harris               0.35875                            2.004353

 7 Term B-Harris              0.27105140069342415                2.631905

 Low Sidelobe                0.323215218                        2.215350782519

 Blackman Nuttall             0.3635819                          1.9761117

If X is an empty input array and the selected window is a cosine window, this VI returns
the window properties. If X is an empty input array and the selected window is not a
cosine window, this VI sets the window properties to NaN and returns an error. For

                                                    © National Instruments 4603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4604 ordinal=4604 -->
## Functions

Functions

       Triangle, Kaiser, Dolph-Chebyshev, and Gaussian windows, the window properties
      depend on the window length and the window parameters.

      ScaledScaled TimeTime DomainDomain WindowWindow (CDB)(CDB) VIVI

       Applies a scaled window to the input sequence X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •     window —

          window is the window to apply to X.

           0         Rectangle (default)
           1        Hanning
           2       Hamming
           3         Blackman-Harris
           4         Exact Blackman
           5        Blackman
           6           Flat Top
           7        4 Term B-Harris
           8        7 Term B-Harris
           9       Low Sidelobe
           11       Blackman Nuttall
           30         Triangle
           31        Bartlett-Hanning
           32      Bohman
           33        Parzen
           34       Welch
           60        Kaiser
           61       Dolph-Chebyshev


4604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4605 ordinal=4605 -->
## Functions

Functions


    62        Gaussian

   •     window parameter —

   window parameter specifies the beta parameter for a Kaiser window, the standard deviation for
    a Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •     window properties —

   window properties returns the coherent gain and equivalent noise bandwidth of the window.

         •     eq noise BW —

       eq noise BW returns the equivalent noise bandwidth of the window. You can use eq noise
     BW to divide a sum of individual power spectra or to compute the power in a given
        frequency span.

         •      coherent gain —

        coherent gain returns the inverse of the scaling factor this VI applies to the window.


   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Scaled Time Domain Window VI scales the result so that when the power or
amplitude spectrum of the windowed waveform is computed, all windows provide the
same level within the accuracy constraints of the window. The Scaled Time Domain
Window VI also returns important window properties for the selected window. These
properties are useful when you use VIs that perform computations on the power
spectrum, such as the Power & Frequency Estimate VI and the Spectrum Unit

                                                    © National Instruments 4605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4606 ordinal=4606 -->
## Functions

Functions

      Conversion VI.

           If yrepresents the output sequence Windowed X, the Scaled Time Domain Window VI
       obtains the elements of yfrom:

                for i= 0, 1, 2, …

      where wi and cgare the coefficients and coherent gain of the window without scaling,
        respectively.

       This VI also returns the coherent gain (CG) and equivalent noise bandwidth (ENBW) of
       the selected window. For cosine windows, these two properties are constants, as listed
        in the following table.


       Window Type             CG                        ENBW

         Rectangle                      1.0                                     1.0

        Hanning                       0.5                                     1.5

       Hamming                     0.54                                1.362826

        Blackman-Harris             0.42323                            1.708538

         Exact Blackman              0.42659071367                      1.693699

        Blackman                     0.42                                1.726757

          Flat Top                     0.215578948                        3.770246506303

        4 Term B-Harris               0.35875                            2.004353

        7 Term B-Harris              0.27105140069342415                2.631905

       Low Sidelobe                0.323215218                        2.215350782519

        Blackman Nuttall             0.3635819                          1.9761117

           If X is an empty input array and the selected window is a cosine window, this VI returns
       the window properties. If X is an empty input array and the selected window is not a
       cosine window, this VI sets the window properties to NaN and returns an error. For
       Triangle, Kaiser, Dolph-Chebyshev, and Gaussian windows, the window properties
      depend on the window length and the window parameters.


4606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4607 ordinal=4607 -->
## Functions

Functions

SymmetricSymmetric WindowWindow

Applies a symmetric window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


   • Symmetric Window (DBL) VI
   • Symmetric Window (CDB) VI

Symmetric windows often are used in digital filter design, while asymmetric windows
often are used in spectrum estimation. For a given window type, the coefficients of an
n-point asymmetric window are the same as the first ncoefficients of the (n+1)-point
symmetric window, as shown in the following illustration:


SymmetricSymmetric WindowWindow (DBL)(DBL) VIVI

Applies a symmetric window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4608 ordinal=4608 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is a real vector.

               •     window —

          window is the window to apply to X.

           0         Rectangle (default)
           1        Hanning
           2       Hamming
           3         Blackman-Harris
           4         Exact Blackman
           5        Blackman
           6           Flat Top
           7        4 Term B-Harris
           8        7 Term B-Harris
           9       Low Sidelobe
           11       Blackman Nuttall
           30         Triangle
           31        Bartlett-Hanning
           32      Bohman
           33        Parzen
           34       Welch
           60        Kaiser
           61       Dolph-Chebyshev
           62        Gaussian

               •     window parameter —

          window parameter is the beta parameter for a Kaiser window, the standard deviation for a
            Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •     Windowed X —

          Windowed X is the input signal with the window applied.


4608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4609 ordinal=4609 -->
## Functions

Functions

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Symmetric windows often are used in digital filter design, while asymmetric windows
often are used in spectrum estimation. For a given window type, the coefficients of an
n-point asymmetric window are the same as the first ncoefficients of the (n+1)-point
symmetric window, as shown in the following illustration:


SymmetricSymmetric WindowWindow (CDB)(CDB) VIVI

Applies a symmetric window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •     window —


                                                    © National Instruments 4609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4610 ordinal=4610 -->
## Functions

Functions


          window is the window to apply to X.

           0         Rectangle (default)
           1        Hanning
           2       Hamming
           3         Blackman-Harris
           4         Exact Blackman
           5        Blackman
           6           Flat Top
           7        4 Term B-Harris
           8        7 Term B-Harris
           9       Low Sidelobe
           11       Blackman Nuttall
           30         Triangle
           31        Bartlett-Hanning
           32      Bohman
           33        Parzen
           34       Welch
           60        Kaiser
           61       Dolph-Chebyshev
           62        Gaussian

               •     window parameter —

          window parameter is the beta parameter for a Kaiser window, the standard deviation for a
            Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4611 ordinal=4611 -->
## Functions

Functions

Symmetric windows often are used in digital filter design, while asymmetric windows
often are used in spectrum estimation. For a given window type, the coefficients of an
n-point asymmetric window are the same as the first ncoefficients of the (n+1)-point
symmetric window, as shown in the following illustration:


WindowWindow PropertiesProperties

Computes the coherent gain and equivalent noise bandwidth of a window. You must
manually select the polymorphic instance you want to use.


   • Window Properties by Coef VI
   • Window Properties by Name VI

The coherent gain (CG) and equivalent noise bandwidth (ENBW) of a given window are
defined as follows:


where wi are the window coefficients and nis the number of coefficients.


                                                    © National Instruments 4611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4612 ordinal=4612 -->
## Functions

Functions

     WindowWindow PropertiesProperties byby CoefCoef VIVI

      Computes the coherent gain and equivalent noise bandwidth of a window. You must
      manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •     Window Coefficients —

         Window Coefficients specifies the window coefficients.

               •     eq noise BW —

          eq noise BW returns the equivalent noise bandwidth of the window defined by Window
             Coefficients.

               •      coherent gain —

           coherent gain returns the coherent gain of the window defined by Window Coefficients.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The coherent gain (CG) and equivalent noise bandwidth (ENBW) of a given window are
       defined as follows:


      where wi are the window coefficients and nis the number of coefficients.


4612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4613 ordinal=4613 -->
## Functions

Functions

WindowWindow PropertiesProperties byby NameName VIVI

Computes the coherent gain and equivalent noise bandwidth of a window. You must
manually select the polymorphic instance you want to use.


Inputs/Outputs

   •       size —

     size specifies the window size. size must be greater than 0.

   •     window —

   window specifies the window type for calculating the properties.

   •     window parameter —

   window parameter is the beta parameter for a Kaiser window, the standard deviation for a
    Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •     eq noise BW —

    eq noise BW returns the equivalent noise bandwidth of the window defined by window.

   •      coherent gain —

    coherent gain returns the coherent gain of the window defined by window.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The coherent gain (CG) and equivalent noise bandwidth (ENBW) of a given window are

                                                    © National Instruments 4613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4614 ordinal=4614 -->
## Functions

Functions

       defined as follows:


      where wi are the window coefficients and nis the number of coefficients.

     HanningHanning WindowWindow

       Applies a Hanning window to the input signal X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


            • Hanning Window (DBL) VI
            • Hanning Window (CDB) VI

           If yrepresents the output sequence Windowed X, the Hanning Window VI obtains the
      elements of yusing

      yi = 0.5xi[1 – cos(w)]

        for i= 0, 1, 2, …, n– 1,

      where nis the number of elements in X.

      A Hanning window is also called a Hann window.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

4614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4615 ordinal=4615 -->
## Functions

Functions

HanningHanning WindowWindow (DBL)(DBL) VIVI

Applies a Hanning window to the input signal X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Hanning Window VI obtains the
elements of yusing

yi = 0.5xi[1 – cos(w)]

for i= 0, 1, 2, …, n– 1,

where nis the number of elements in X.

A Hanning window is also called a Hann window.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 4615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4616 ordinal=4616 -->
## Functions

Functions

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      HanningHanning WindowWindow (CDB)(CDB) VIVI

       Applies a Hanning window to the input signal X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Hanning Window VI obtains the
      elements of yusing

      yi = 0.5xi[1 – cos(w)]

        for i= 0, 1, 2, …, n– 1,

      where nis the number of elements in X.

      A Hanning window is also called a Hann window.


4616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4617 ordinal=4617 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

HammingHamming WindowWindow

Applies a Hamming window to the input signal X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


   • Hamming Window (DBL) VI
   • Hamming Window (CDB) VI

If yrepresents the output sequence Windowed X, the Hamming Window VI obtains the
elements of yfrom

yi = xi[0.54 – 0.46cos(w)]

for i= 0, 1, 2, …, n– 1,

where nis the number of elements in the input sequence X.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

HammingHamming WindowWindow (DBL)(DBL) VIVI

Applies a Hamming window to the input signal X. Wire data to the X input to determine

                                                    © National Instruments 4617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4618 ordinal=4618 -->
## Functions

Functions

       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Hamming Window VI obtains the
      elements of yfrom

      yi = xi[0.54 – 0.46cos(w)]

        for i= 0, 1, 2, …, n– 1,

      where nis the number of elements in the input sequence X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi


4618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4619 ordinal=4619 -->
## Functions

Functions

HammingHamming WindowWindow (CDB)(CDB) VIVI

Applies a Hamming window to the input signal X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Hamming Window VI obtains the
elements of yfrom

yi = xi[0.54 – 0.46cos(w)]

for i= 0, 1, 2, …, n– 1,

where nis the number of elements in the input sequence X.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

                                                    © National Instruments 4619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4620 ordinal=4620 -->
## Functions

Functions

     BlackmanBlackman WindowWindow

       Applies a Blackman window to the input signal X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


            • Blackman Window (DBL) VI
            • Blackman Window (CDB) VI

           If Yrepresents the output sequence Windowed X, the Blackman Window VI obtains the
      elements of Yusing the following formula:

      yi = xi[0.42 – 0.50cos(w) + 0.08cos(2w)]

        for i= 0, 1, 2, …, n– 1

      where nis the number of elements in X and          .

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

     BlackmanBlackman WindowWindow (DBL)(DBL) VIVI

       Applies a Blackman window to the input signal X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


4620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4621 ordinal=4621 -->
## Functions

Functions

Inputs/Outputs

   •     X —

    X is a real vector.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If Yrepresents the output sequence Windowed X, the Blackman Window VI obtains the
elements of Yusing the following formula:

yi = xi[0.42 – 0.50cos(w) + 0.08cos(2w)]

for i= 0, 1, 2, …, n– 1

where nis the number of elements in X and          .

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

BlackmanBlackman WindowWindow (CDB)(CDB) VIVI

Applies a Blackman window to the input signal X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4622 ordinal=4622 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If Yrepresents the output sequence Windowed X, the Blackman Window VI obtains the
      elements of Yusing the following formula:

      yi = xi[0.42 – 0.50cos(w) + 0.08cos(2w)]

        for i= 0, 1, 2, …, n– 1

      where nis the number of elements in X and          .

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

     Blackman-HarrisBlackman-Harris WindowWindow

       Applies a three-term, Blackman-Harris window to the input signal X. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


4622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4623 ordinal=4623 -->
## Functions

Functions

   • Blackman-Harris Window (DBL) VI
   • Blackman-Harris Window (CDB) VI

If Yrepresents the output sequence Windowed X, the Blackman-Harris Window VI
obtains the elements of Yusing the following formula:

yi = xi[0.42323 – 0.49755cos(w) + 0.07922cos(2w)]

for i= 0, 1, 2, …, n– 1

where nis the number of elements in X and

          .

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

Blackman-HarrisBlackman-Harris WindowWindow (DBL)(DBL) VIVI

Applies a three-term, Blackman-Harris window to the input signal X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •     Windowed X —

   Windowed X is the input signal with the window applied.


                                                    © National Instruments 4623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4624 ordinal=4624 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If Yrepresents the output sequence Windowed X, the Blackman-Harris Window VI
       obtains the elements of Yusing the following formula:

      yi = xi[0.42323 – 0.49755cos(w) + 0.07922cos(2w)]

        for i= 0, 1, 2, …, n– 1

      where nis the number of elements in X and

                      .

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      Blackman-HarrisBlackman-Harris WindowWindow (CDB)(CDB) VIVI

       Applies a three-term, Blackman-Harris window to the input signal X. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •     Windowed X —

4624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4625 ordinal=4625 -->
## Functions

Functions


   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If Yrepresents the output sequence Windowed X, the Blackman-Harris Window VI
obtains the elements of Yusing the following formula:

yi = xi[0.42323 – 0.49755cos(w) + 0.07922cos(2w)]

for i= 0, 1, 2, …, n– 1

where nis the number of elements in X and

          .

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

Blackman-NuttallBlackman-Nuttall WindowWindow

Applies a Blackman-Nuttall window to the input sequence X. Wire data to the X input
to determine the polymorphic instance to use or manually select the instance.


   • Blackman-Nuttall Window (DBL) VI
   • Blackman-Nuttall Window (CDB) VI


                                                    © National Instruments 4625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4626 ordinal=4626 -->
## Functions

Functions

           If yrepresents the output sequence Windowed X, the Blackman-Nuttall Window VI
       obtains the elements of yusing the following formula:

      yi = xi [0.3635819 – 0.4891775cos(w) + 0.1365995cos(2w) – 0.0106411cos(3w)]

        for i= 0, 1, 2, … , n–1

      where nis the number of elements in X and w =     .

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      Blackman-NuttallBlackman-Nuttall WindowWindow (DBL)(DBL) VIVI

       Applies a Blackman-Nuttall window to the input sequence X. Wire data to the X input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4627 ordinal=4627 -->
## Functions

Functions

If yrepresents the output sequence Windowed X, the Blackman-Nuttall Window VI
obtains the elements of yusing the following formula:

yi = xi [0.3635819 – 0.4891775cos(w) + 0.1365995cos(2w) – 0.0106411cos(3w)]

for i= 0, 1, 2, … , n–1

where nis the number of elements in X and w =     .

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

Blackman-NuttallBlackman-Nuttall WindowWindow (CDB)(CDB) VIVI

Applies a Blackman-Nuttall window to the input sequence X. Wire data to the X input
to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 4627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4628 ordinal=4628 -->
## Functions

Functions

           If yrepresents the output sequence Windowed X, the Blackman-Nuttall Window VI
       obtains the elements of yusing the following formula:

      yi = xi [0.3635819 – 0.4891775cos(w) + 0.1365995cos(2w) – 0.0106411cos(3w)]

        for i= 0, 1, 2, … , n–1

      where nis the number of elements in X and w =     .

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      ExactExact BlackmanBlackman WindowWindow

       Applies an Exact Blackman window to the input signal X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • Exact Blackman Window (DBL) VI
            • Exact Blackman Window (CDB) VI

           If yrepresents the output sequence Windowed X, the Exact Blackman Window VI
       obtains the elements of yfrom

      yi = xi[a0 – a1cos(w) + a2cos(2w)]

        for i= 0, 1, 2, …, n– 1

                      ,


4628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4629 ordinal=4629 -->
## Functions

Functions

where nis the number of elements in X,

a0 = 7938/18608, a1 = 9240/18608, and a2 = 1430/18608.
Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ExactExact BlackmanBlackman WindowWindow (DBL)(DBL) VIVI

Applies an Exact Blackman window to the input signal X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Exact Blackman Window VI
obtains the elements of yfrom

yi = xi[a0 – a1cos(w) + a2cos(2w)]


                                                    © National Instruments 4629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4630 ordinal=4630 -->
## Functions

Functions

        for i= 0, 1, 2, …, n– 1

                      ,

      where nis the number of elements in X,

      a0 = 7938/18608, a1 = 9240/18608, and a2 = 1430/18608.
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      ExactExact BlackmanBlackman WindowWindow (CDB)(CDB) VIVI

       Applies an Exact Blackman window to the input signal X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Exact Blackman Window VI

4630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4631 ordinal=4631 -->
## Functions

Functions

obtains the elements of yfrom

yi = xi[a0 – a1cos(w) + a2cos(2w)]

for i= 0, 1, 2, …, n– 1

          ,

where nis the number of elements in X,

a0 = 7938/18608, a1 = 9240/18608, and a2 = 1430/18608.
Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

FlatFlat TopTop WindowWindow

Applies a flat top window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


   • Flat Top Window (DBL) VI
   • Flat Top Window (CDB) VI

If yrepresents the output sequence Windowed X, the Flat Top Window VI obtains the
elements of yfrom

yi = xi[0.21557895 – 0.41663158cos(w) + 0.277263158cos(2w) – 0.083578947cos(3w) +
0.006947368cos(4w)]

for i= 0, 1, 2, …, n– 1

                                                    © National Instruments 4631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4632 ordinal=4632 -->
## Functions

Functions

                      ,

      where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

       FlatFlat TopTop WindowWindow (DBL)(DBL) VIVI

       Applies a flat top window to the input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Flat Top Window VI obtains the
      elements of yfrom

      yi = xi[0.21557895 – 0.41663158cos(w) + 0.277263158cos(2w) – 0.083578947cos(3w) +


4632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4633 ordinal=4633 -->
## Functions

Functions

0.006947368cos(4w)]

for i= 0, 1, 2, …, n– 1

          ,

where nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

FlatFlat TopTop WindowWindow (CDB)(CDB) VIVI

Applies a flat top window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 4633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4634 ordinal=4634 -->
## Functions

Functions

           If yrepresents the output sequence Windowed X, the Flat Top Window VI obtains the
      elements of yfrom

      yi = xi[0.21557895 – 0.41663158cos(w) + 0.277263158cos(2w) – 0.083578947cos(3w) +
       0.006947368cos(4w)]

        for i= 0, 1, 2, …, n– 1

                      ,

      where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

     GeneralGeneral CosineCosine WindowWindow

       Applies a general cosine window to the input signal X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • General Cosine Window (DBL) VI
            • General Cosine Window (CDB) VI

           If arepresents the Cosine Coefficients input sequence and yrepresents the output
      sequence Windowed X, the General Cosine Window VI obtains the elements of yfrom


        for i= 0, 1, 2, …, n– 1

4634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4635 ordinal=4635 -->
## Functions

Functions

          ,

where nis the number of elements in X, and mis the number of Cosine Coefficients.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

GeneralGeneral CosineCosine WindowWindow (DBL)(DBL) VIVI

Applies a general cosine window to the input signal X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •      Cosine Coefficients —

    Cosine Coefficients is the coefficients that define the general cosine window.

          Note If Cosine Coefficients is an empty array, the VI sets Windowed X to an empty
               array, even if X is not empty.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 4635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4636 ordinal=4636 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


           If arepresents the Cosine Coefficients input sequence and yrepresents the output
      sequence Windowed X, the General Cosine Window VI obtains the elements of yfrom


        for i= 0, 1, 2, …, n– 1

                      ,

      where nis the number of elements in X, and mis the number of Cosine Coefficients.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      GeneralGeneral CosineCosine WindowWindow (CDB)(CDB) VIVI

       Applies a general cosine window to the input signal X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •      Cosine Coefficients —


4636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4637 ordinal=4637 -->
## Functions

Functions


    Cosine Coefficients is the coefficients that define the general cosine window.

          Note If Cosine Coefficients is an empty array, the VI sets Windowed X to an empty
               array, even if X is not empty.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If arepresents the Cosine Coefficients input sequence and yrepresents the output
sequence Windowed X, the General Cosine Window VI obtains the elements of yfrom


for i= 0, 1, 2, …, n– 1

          ,

where nis the number of elements in X, and mis the number of Cosine Coefficients.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

CosineCosine TaperedTapered WindowWindow

Applies a cosine tapered window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.

                                                    © National Instruments 4637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4638 ordinal=4638 -->
## Functions

Functions


            • Cosine Tapered Window (DBL) VI
            • Cosine Tapered Window (CDB) VI

           If yrepresents the output sequence Windowed X, the Cosine Tapered Window VI
       obtains the elements of yusing the following equation:


      where              ,

   nis the number of elements in X, ris the ratio of the total length of the tapered section
       to the whole signal length as shown below:


           If r≤ 0, the window is equivalent to a rectangular window. If r≥ 1, the window is
       equivalent to a Hanning window.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi


4638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4639 ordinal=4639 -->
## Functions

Functions

CosineCosine TaperedTapered WindowWindow (DBL)(DBL) VIVI

Applies a cosine tapered window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •       ratio —

     ratio is the ratio of the length of the tapered section to the length of the entire signal. The
     default is 0.2.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Cosine Tapered Window VI
obtains the elements of yusing the following equation:


where              ,


                                                    © National Instruments 4639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4640 ordinal=4640 -->
## Functions

Functions

   nis the number of elements in X, ris the ratio of the total length of the tapered section
       to the whole signal length as shown below:


           If r≤ 0, the window is equivalent to a rectangular window. If r≥ 1, the window is
       equivalent to a Hanning window.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      CosineCosine TaperedTapered WindowWindow (CDB)(CDB) VIVI

       Applies a cosine tapered window to the input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •       ratio —

              ratio is the ratio of the length of the tapered section to the length of the entire signal. The


4640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4641 ordinal=4641 -->
## Functions

Functions


     default is 0.2.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Cosine Tapered Window VI
obtains the elements of yusing the following equation:


where              ,

nis the number of elements in X, ris the ratio of the total length of the tapered section
to the whole signal length as shown below:


If r≤ 0, the window is equivalent to a rectangular window. If r≥ 1, the window is
equivalent to a Hanning window.


                                                    © National Instruments 4641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4642 ordinal=4642 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      TriangleTriangle WindowWindow

       Applies a triangular window (Bartlett Window) to the input signal X. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


            • Triangle Window (DBL) VI
            • Triangle Window (CDB) VI

           If yrepresents the output sequence Windowed X, the Triangle Window VI obtains the
      elements of yfrom

      yi = xitri(w)

        for i= 0, 1, 2, …, n– 1

                         ,

      where tri(w) = 1 – |w|, and nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi


4642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4643 ordinal=4643 -->
## Functions

Functions

TriangleTriangle WindowWindow (DBL)(DBL) VIVI

Applies a triangular window (Bartlett Window) to the input signal X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Triangle Window VI obtains the
elements of yfrom

yi = xitri(w)

for i= 0, 1, 2, …, n– 1

            ,

where tri(w) = 1 – |w|, and nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 4643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4644 ordinal=4644 -->
## Functions

Functions

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

       TriangleTriangle WindowWindow (CDB)(CDB) VIVI

       Applies a triangular window (Bartlett Window) to the input signal X. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Triangle Window VI obtains the
      elements of yfrom

      yi = xitri(w)

        for i= 0, 1, 2, …, n– 1

                         ,

      where tri(w) = 1 – |w|, and nis the number of elements in X.


4644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4645 ordinal=4645 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

Kaiser-BesselKaiser-Bessel WindowWindow

Applies a Kaiser-Bessel window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


  • Kaiser-Bessel Window (DBL) VI
  • Kaiser-Bessel Window (CDB) VI

If yrepresents the output sequence Windowed X, the Kaiser-Bessel Window VI obtains
the elements of yfrom


for i= 0, 1, 2, …, n– 1


where nis the number of elements in X, and Io(·) is the zero-order modified Bessel
function.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 4645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4646 ordinal=4646 -->
## Functions

Functions

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

       Kaiser-BesselKaiser-Bessel WindowWindow (DBL)(DBL) VIVI

       Applies a Kaiser-Bessel window to the input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •      beta —

           beta is proportional to the side lobe attenuation. That is, the larger beta is, the greater the side
            lobe attenuation. The default is 0.0.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Kaiser-Bessel Window VI obtains
       the elements of yfrom


        for i= 0, 1, 2, …, n– 1


4646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4647 ordinal=4647 -->
## Functions

Functions


where nis the number of elements in X, and Io(·) is the zero-order modified Bessel
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

Kaiser-BesselKaiser-Bessel WindowWindow (CDB)(CDB) VIVI

Applies a Kaiser-Bessel window to the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •      beta —

    beta is proportional to the side lobe attenuation. That is, the larger beta is, the greater the side
    lobe attenuation. The default is 0.0.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 4647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4648 ordinal=4648 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Kaiser-Bessel Window VI obtains
       the elements of yfrom


        for i= 0, 1, 2, …, n– 1


      where nis the number of elements in X, and Io(·) is the zero-order modified Bessel
       function.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

     GaussianGaussian WindowWindow

       Applies an asymmetrical Gaussian window to the input sequence X. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


            • Gaussian Window (DBL) VI
            • Gaussian Window (CDB) VI


4648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4649 ordinal=4649 -->
## Functions

Functions

If yrepresents the output sequence Windowed X, the Gaussian Window VI obtains the
elements of yfrom:

                   for i= 0, 1, … , n–1

where nis the number of elements in X, m= (n–1)/2.0, and σ is the standard deviation
of the Gaussian window.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

GaussianGaussian WindowWindow (DBL)(DBL) VIVI

Applies an asymmetrical Gaussian window to the input sequence X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •      standard deviation —

    standard deviation is the standard deviation of the Gaussian window normalized to the length
     of X. The default is 0.2.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —


                                                    © National Instruments 4649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4650 ordinal=4650 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Gaussian Window VI obtains the
      elements of yfrom:

                           for i= 0, 1, … , n–1

      where nis the number of elements in X, m= (n–1)/2.0, and σ is the standard deviation
       of the Gaussian window.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      GaussianGaussian WindowWindow (CDB)(CDB) VIVI

       Applies an asymmetrical Gaussian window to the input sequence X. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •      standard deviation —

           standard deviation is the standard deviation of the Gaussian window normalized to the length
             of X. The default is 0.2.


4650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4651 ordinal=4651 -->
## Functions

Functions

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Gaussian Window VI obtains the
elements of yfrom:

                   for i= 0, 1, … , n–1

where nis the number of elements in X, m= (n–1)/2.0, and σ is the standard deviation
of the Gaussian window.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ChebyshevChebyshev WindowWindow

Applies an asymmetrical Dolph-Chebyshev window to the input sequence X. Wire data
to the X input to determine the polymorphic instance to use or manually select the
instance.


  • Chebyshev Window (DBL) VI
  • Chebyshev Window (CDB) VI

If yrepresents the output sequence Windowed X, the Chebyshev Window VI obtains


                                                    © National Instruments 4651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4652 ordinal=4652 -->
## Functions

Functions

       the elements of yusing the following equation:


        for i= 0, 1, … , n–1

      where nis the number of elements in X,

    sis the height ratio of the mainlobe to the sidelobe in dB,                                 is

       the m-th order Chebyshev polynomial,                               .

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      ChebyshevChebyshev WindowWindow (DBL)(DBL) VIVI

       Applies an asymmetrical Dolph-Chebyshev window to the input sequence X. Wire data
       to the X input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •      lobe ratio (dB) —


4652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4653 ordinal=4653 -->
## Functions

Functions


    lobe ratio (dB) is the ratio of the mainlobe to the sidelobe in dB. The default is 60.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Chebyshev Window VI obtains
the elements of yusing the following equation:


for i= 0, 1, … , n–1

where nis the number of elements in X,

sis the height ratio of the mainlobe to the sidelobe in dB,                                 is

the m-th order Chebyshev polynomial,                               .

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ChebyshevChebyshev WindowWindow (CDB)(CDB) VIVI

Applies an asymmetrical Dolph-Chebyshev window to the input sequence X. Wire data
to the X input to determine the polymorphic instance to use or manually select the
instance.

                                                    © National Instruments 4653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4654 ordinal=4654 -->
## Functions

Functions


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •      lobe ratio (dB) —

            lobe ratio (dB) is the ratio of the mainlobe to the sidelobe in dB. The default is 60.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Chebyshev Window VI obtains
       the elements of yusing the following equation:


        for i= 0, 1, … , n–1

      where nis the number of elements in X,

    sis the height ratio of the mainlobe to the sidelobe in dB,                                 is

       the m-th order Chebyshev polynomial,                               .


4654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4655 ordinal=4655 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ForceForce WindowWindow

Applies a force window to the input signal X. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


   • Force Window (DBL) VI
   • Force Window (CDB) VI

If yrepresents the output sequence Windowed X, the Force Window VI obtains the
elements of yfrom


d= (0.01)(n)(duty cycle), where nis the number of elements in X.

You can use the Force Window VI to analyze transients.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ForceForce WindowWindow (DBL)(DBL) VIVI

Applies a force window to the input signal X. Wire data to the X input to determine the

                                                    © National Instruments 4655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4656 ordinal=4656 -->
## Functions

Functions

      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •      duty cycle(%) —

           duty cycle must be a percentage.

                    If your duty cycle is expressed as a fraction of a completed record, you must convert the duty
             cycle to a percentage, as shown in the following illustration, before using the Force Window VI.


               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Force Window VI obtains the
      elements of yfrom


   d= (0.01)(n)(duty cycle), where nis the number of elements in X.

      You can use the Force Window VI to analyze transients.

4656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4657 ordinal=4657 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ForceForce WindowWindow (CDB)(CDB) VIVI

Applies a force window to the input signal X. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •      duty cycle(%) —

    duty cycle must be a percentage.

       If your duty cycle is expressed as a fraction of a completed record, you must convert the duty
    cycle to a percentage, as shown in the following illustration, before using the Force Window VI.


   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 4657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4658 ordinal=4658 -->
## Functions

Functions

           If yrepresents the output sequence Windowed X, the Force Window VI obtains the
      elements of yfrom


   d= (0.01)(n)(duty cycle), where nis the number of elements in X.

      You can use the Force Window VI to analyze transients.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      ExponentialExponential WindowWindow

       Applies an exponential window to the input signal X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • Exponential Window (DBL) VI
            • Exponential Window (CDB) VI

           If yrepresents the output sequence Windowed X, the Exponential Window VI obtains
       the elements of yfrom

      yi = xiexp(a*i)

        for i= 0, 1, 2, …, n– 1,

      where fis the final value, and nis the number of samples in X.


4658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4659 ordinal=4659 -->
## Functions

Functions

You can use the Exponential Window VI to analyze transients.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ExponentialExponential WindowWindow (DBL)(DBL) VIVI

Applies an exponential window to the input signal X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •       final value —

     final value specifies the coefficient of the last point of the window.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Exponential Window VI obtains
the elements of yfrom


                                                    © National Instruments 4659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4660 ordinal=4660 -->
## Functions

Functions

      yi = xiexp(a*i)

        for i= 0, 1, 2, …, n– 1,

      where fis the final value, and nis the number of samples in X.

      You can use the Exponential Window VI to analyze transients.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      ExponentialExponential WindowWindow (CDB)(CDB) VIVI

       Applies an exponential window to the input signal X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •       final value —

              final value specifies the coefficient of the last point of the window.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —


4660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4661 ordinal=4661 -->
## Functions

Functions


     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Exponential Window VI obtains
the elements of yfrom

yi = xiexp(a*i)

for i= 0, 1, 2, …, n– 1,

where fis the final value, and nis the number of samples in X.

You can use the Exponential Window VI to analyze transients.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ModifiedModified Bartlett-HanningBartlett-Hanning WindowWindow

Applies a modified Bartlett-Hanning window to the input signal X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


   • Modified Bartlett-Hanning Window (DBL) VI
   • Modified Bartlett-Hanning Window (CDB) VI

If yrepresents the output sequence Windowed X, the Modified Bartlett-Hanning
Window VI obtains the elements of yusing the following equation.


                                                    © National Instruments 4661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4662 ordinal=4662 -->
## Functions

Functions


        for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      ModifiedModified Bartlett-HanningBartlett-Hanning WindowWindow (DBL)(DBL) VIVI

       Applies a modified Bartlett-Hanning window to the input signal X. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Modified Bartlett-Hanning
     Window VI obtains the elements of yusing the following equation.


4662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4663 ordinal=4663 -->
## Functions

Functions


for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ModifiedModified Bartlett-HanningBartlett-Hanning WindowWindow (CDB)(CDB) VIVI

Applies a modified Bartlett-Hanning window to the input signal X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Modified Bartlett-Hanning
Window VI obtains the elements of yusing the following equation.


                                                    © National Instruments 4663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4664 ordinal=4664 -->
## Functions

Functions


        for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

    BohmanBohman WindowWindow

       Applies a Bohman window to the input signal X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


            • Bohman Window (DBL) VI
            • Bohman Window (CDB) VI

           If yrepresents the output sequence Windowed X, the Bohman Window VI obtains the
      elements of yusing the following equation.


        for i= 0, 1, 2,…, n–1, where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi


4664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4665 ordinal=4665 -->
## Functions

Functions

BohmanBohman WindowWindow (DBL)(DBL) VIVI

Applies a Bohman window to the input signal X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Bohman Window VI obtains the
elements of yusing the following equation.


for i= 0, 1, 2,…, n–1, where nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi


                                                    © National Instruments 4665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4666 ordinal=4666 -->
## Functions

Functions

     BohmanBohman WindowWindow (CDB)(CDB) VIVI

       Applies a Bohman window to the input signal X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Bohman Window VI obtains the
      elements of yusing the following equation.


        for i= 0, 1, 2,…, n–1, where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi


4666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4667 ordinal=4667 -->
## Functions

Functions

ParzenParzen WindowWindow

Applies a Parzen window to the input signal X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


  • Parzen Window (DBL) VI
  • Parzen Window (CDB) VI

If yrepresents the output sequence Windowed X, the Parzen Window VI obtains the
elements of yusing the following equation.


for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

ParzenParzen WindowWindow (DBL)(DBL) VIVI

Applies a Parzen window to the input signal X. Wire data to the X input to determine
the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4668 ordinal=4668 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is a real vector.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Parzen Window VI obtains the
      elements of yusing the following equation.


        for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      ParzenParzen WindowWindow (CDB)(CDB) VIVI

       Applies a Parzen window to the input signal X. Wire data to the X input to determine
       the polymorphic instance to use or manually select the instance.


4668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4669 ordinal=4669 -->
## Functions

Functions

Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Parzen Window VI obtains the
elements of yusing the following equation.


for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

WelchWelch WindowWindow

Applies a Welch window to the input signal X. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4670 ordinal=4670 -->
## Functions

Functions

            • Welch Window (DBL) VI
            • Welch Window (CDB) VI

           If yrepresents the output sequence Windowed X, the Welch Window VI obtains the
      elements of yusing the following equation.


        for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      WelchWelch WindowWindow (DBL)(DBL) VIVI

       Applies a Welch window to the input signal X. Wire data to the X input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •     Windowed X —

          Windowed X is the input signal with the window applied.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


4670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4671 ordinal=4671 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.


If yrepresents the output sequence Windowed X, the Welch Window VI obtains the
elements of yusing the following equation.


for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Windows\Window
   Comparison.vi

WelchWelch WindowWindow (CDB)(CDB) VIVI

Applies a Welch window to the input signal X. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •     Windowed X —

   Windowed X is the input signal with the window applied.

   •       error —


                                                    © National Instruments 4671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4672 ordinal=4672 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If yrepresents the output sequence Windowed X, the Welch Window VI obtains the
      elements of yusing the following equation.


        for i= 0, 1, 2, …, n– 1, where nis the number of elements in X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Windows\Window
        Comparison.vi

      FiltersFilters

      Use the Filters VIs to implement IIR, FIR, and nonlinear filters.

      The VIs on this palette can return signal processing error codes.


         Palette
                        Description
        Object

                       Generates a digital Butterworth filter by calling the Butterworth Coefficients VI.
        Butterworth
                       Wire data to the X input to determine the polymorphic instance to use or manually
           Filter
                          select the instance.


        Chebyshev
                       Generates a digital Chebyshev filter by calling the Chebyshev Coefficients VI. Wire
           Filter


4672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4673 ordinal=4673 -->
## Functions

Functions


Palette               Description
Object

              data to the X input to determine the polymorphic instance to use or manually
                select the instance.


Inverse        Generates a digital Chebyshev II filter by calling the Inv Chebyshev Coefficients VI.
Chebyshev     Wire data to the X input to determine the polymorphic instance to use or manually
Filter           select the instance.


              Generates a digital elliptic filter by calling the Elliptic Coefficients VI. Wire data to
Elliptic Filter   the X input to determine the polymorphic instance to use or manually select the
                instance.


              Generates a digital Bessel filter by calling the Bessel Coefficients VI. Wire data to the
Bessel Filter   X input to determine the polymorphic instance to use or manually select the
                instance.


              Generates a lowpass FIR filter with equi-ripple characteristics using the Parks-
               McClellan algorithm and the # of taps, pass freq, stop freq, and sampling freq: fs.Equi-Ripple
             The Equi-Ripple LowPass VI then applies a linear-phase, lowpass filter to the inputLowPass             sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
              determine the polymorphic instance to use or manually select the instance.


              Generates a highpass FIR filter with equi-ripple characteristics using the Parks-
               McClellan algorithm and the # of taps, stop freq, high freq, and sampling freq: fs.
Equi-Ripple
             The Equi-Ripple HighPass VI then applies a linear-phase, highpass filter to the input
HighPass
             sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
              determine the polymorphic instance to use or manually select the instance.


              Generates a bandpass FIR filter with equi-ripple characteristics using the Parks-
Equi-Ripple    McClellan algorithm and the higher pass freq, lower pass freq, # of taps, lower
BandPass      stop freq, higher stop freq, and sampling freq: fs. The Equi-Ripple BandPass VI
              then applies a linear-phase, bandpass filter to the input sequence X using the


                                                    © National Instruments 4673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4674 ordinal=4674 -->
## Functions

Functions


         Palette                        Description
        Object

                       Convolution VI to obtain Filtered X. Wire data to the X input to determine the
                      polymorphic instance to use or manually select the instance.


                       Generates a bandstop FIR digital filter with equi-ripple characteristics using the
                        Parks-McClellan algorithm and higher pass freq, lower pass freq, # of taps, lower
         Equi-Ripple    stop freq, higher stop freq, and sampling freq: fs. The Equi-Ripple BandStop VI
        BandStop     then applies a linear-phase, bandstop filter to the input sequence X using the
                       Convolution VI to obtain Filtered X. Wire data to the X input to determine the
                      polymorphic instance to use or manually select the instance.


                       Designs and implements an IIR filter whose magnitude-squared response is
                          inversely proportional to frequency over a specified frequency range. This inverse-f
         Inverse f Filter  filter is typically used to colorize spectrally flat, or white, noise. Wire data to the X
                        input to determine the polymorphic instance to use or manually select the
                          instance.


        Zero Phase     Applies a zero phase filter to an input sequence X. Wire data to the X input to
           Filter         determine the polymorphic instance to use or manually select the instance.


                             Filters the input data sequence, X, using the set of windowed FIR filter coefficients
         FIR Windowed  specified by the sampling freq: fs, low cutoff freq: fl, high cutoff freq: fh, and
           Filter        number of taps. Wire data to the X input to determine the polymorphic instance to
                      use or manually select the instance.


        Median Filter   Applies a median filter of rank to the input sequence X.


                             Filters the input data sequence X using a Savitzky-Golay FIR smoothing filter. Wire
         Savitzky-
                       data to the X input to determine the polymorphic instance to use or manually
        Golay Filter
                          select the instance.


4674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4675 ordinal=4675 -->
## Functions

Functions


 Palette                Description
 Object

 Mathematical                   Filters the input data sequence X with Structure Element using a mathematical Morphological               morphological filter. Filter

 Advanced IIR              Use the Advanced IIR Filtering VIs to implement advanced IIR filters. Filtering

 Advanced FIR              Use the Advanced FIR Filtering VIs to implement advanced FIR filters. Filtering


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\Filters.lvproj

ButterworthButterworth FilterFilter

Generates a digital Butterworth filter by calling the Butterworth Coefficients VI. Wire
data to the X input to determine the polymorphic instance to use or manually select
the instance.


  • Butterworth Filter (DBL) VI
  • Butterworth Filter (CDB) VI

After calling the Butterworth Coefficients VI, the Butterworth Filter VI calls the IIR
Cascade Filter VI to obtain a Butterworth Filtered X sequence.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

                                                    © National Instruments 4675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4676 ordinal=4676 -->
## Functions

Functions

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Extract the
        Sine Wave.vi

      ButterworthButterworth FilterFilter (DBL)(DBL) VIVI

       Generates a digital Butterworth filter by calling the Butterworth Coefficients VI. Wire
       data to the X input to determine the polymorphic instance to use or manually select
       the instance.


      Inputs/Outputs

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —


4676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4677 ordinal=4677 -->
## Functions

Functions


  sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
   0. The default is 1.0 Hz.

   If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
  an error.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
  the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
  (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

•      order —

  order specifies the filter order and must be greater than 0. The default is 2.

   If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

•       init/cont (init:F) —

  init/cont controls the initialization of the internal states. The default is FALSE.

  The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
  init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
  to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
   this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

•       Filtered X —

  Filtered X is the output array of filtered samples.

•       error —


                                                   © National Instruments 4677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4678 ordinal=4678 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        After calling the Butterworth Coefficients VI, the Butterworth Filter VI calls the IIR
      Cascade Filter VI to obtain a Butterworth Filtered X sequence.

      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Extract the
        Sine Wave.vi

      ButterworthButterworth FilterFilter (CDB)(CDB) VIVI

       Generates a digital Butterworth filter by calling the Butterworth Coefficients VI. Wire
       data to the X input to determine the polymorphic instance to use or manually select
       the instance.


      Inputs/Outputs

               •        filter type —


4678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4679 ordinal=4679 -->
## Functions

Functions


   filter type specifies the passband of the filter.

  0        Lowpass
  1         Highpass
  2        Bandpass
  3        Bandstop

•     X —

  X is the input signal to filter.

•      sampling freq: fs —

  sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
   0. The default is 1.0 Hz.

   If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
  an error.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
  the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
  (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

•      order —

  order specifies the filter order and must be greater than 0. The default is 2.

   If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

•       init/cont (init:F) —


                                                   © National Instruments 4679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4680 ordinal=4680 -->
## Functions

Functions


             init/cont controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
             init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
             to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
              this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        After calling the Butterworth Coefficients VI, the Butterworth Filter VI calls the IIR
      Cascade Filter VI to obtain a Butterworth Filtered X sequence.

      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Extract the
        Sine Wave.vi

     ChebyshevChebyshev FilterFilter

       Generates a digital Chebyshev filter by calling the Chebyshev Coefficients VI. Wire data
       to the X input to determine the polymorphic instance to use or manually select the
       instance.

4680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4681 ordinal=4681 -->
## Functions

Functions


  • Chebyshev Filter (DBL) VI
  • Chebyshev Filter (CDB) VI

After calling the Chebyshev Coefficients VI, the Chebyshev Filter VI obtains a
Chebyshev Filtered X sequence by calling the IIR Cascade Filter VI.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\IIR Filter
   Design.vi

ChebyshevChebyshev FilterFilter (DBL)(DBL) VIVI

Generates a digital Chebyshev filter by calling the Chebyshev Coefficients VI. Wire data
to the X input to determine the polymorphic instance to use or manually select the
instance.


                                                    © National Instruments 4681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4682 ordinal=4682 -->
## Functions

Functions

      Inputs/Outputs

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
          an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

                    If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
            the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
            (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

               •       ripple(dB) —

             ripple is the ripple in the passband. ripple must be greater than zero and expressed in decibels.


4682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4683 ordinal=4683 -->
## Functions

Functions


    The default is 0.1.

       If ripple is less than or equal to zero, the VI sets Filtered X to an empty array and returns an error.

   •      order —

    order specifies the filter order and must be greater than 0. The default is 2.

       If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

   •       init/cont (init:F) —

     init/cont controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
     init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
    to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
     this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

   •       Filtered X —

     Filtered X is the output array of filtered samples.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


After calling the Chebyshev Coefficients VI, the Chebyshev Filter VI obtains a
Chebyshev Filtered X sequence by calling the IIR Cascade Filter VI.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.


                                                    © National Instruments 4683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4684 ordinal=4684 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\IIR Filter
        Design.vi

      ChebyshevChebyshev FilterFilter (CDB)(CDB) VIVI

       Generates a digital Chebyshev filter by calling the Chebyshev Coefficients VI. Wire data
       to the X input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.


4684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4685 ordinal=4685 -->
## Functions

Functions


   If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
  an error.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
  the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
  (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

•       ripple(dB) —

  ripple is the ripple in the passband. ripple must be greater than zero and expressed in decibels.
  The default is 0.1.

   If ripple is less than or equal to zero, the VI sets Filtered X to an empty array and returns an error.

•      order —

  order specifies the filter order and must be greater than 0. The default is 2.

   If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

•       init/cont (init:F) —

  init/cont controls the initialization of the internal states. The default is FALSE.

  The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
  init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
  to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
   this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

•       Filtered X —


                                                   © National Instruments 4685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4686 ordinal=4686 -->
## Functions

Functions


             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        After calling the Chebyshev Coefficients VI, the Chebyshev Filter VI obtains a
      Chebyshev Filtered X sequence by calling the IIR Cascade Filter VI.

      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\IIR Filter
        Design.vi

      InverseInverse ChebyshevChebyshev FilterFilter

       Generates a digital Chebyshev II filter by calling the Inv Chebyshev Coefficients VI. Wire
       data to the X input to determine the polymorphic instance to use or manually select
       the instance.


            • Inverse Chebyshev Filter (DBL) VI
            • Inverse Chebyshev Filter (CDB) VI

        After calling the Inv Chebyshev Coefficients VI, the Inverse Chebyshev Filter VI obtains a

4686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4687 ordinal=4687 -->
## Functions

Functions

Chebyshev II Filtered X sequence by calling the IIR Cascade Filter VI.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\IIR Filter
   Design.vi

InverseInverse ChebyshevChebyshev FilterFilter (DBL)(DBL) VIVI

Generates a digital Chebyshev II filter by calling the Inv Chebyshev Coefficients VI. Wire
data to the X input to determine the polymorphic instance to use or manually select
the instance.


Inputs/Outputs

   •        filter type —

      filter type specifies the passband of the filter.

    0        Lowpass
    1         Highpass


                                                    © National Instruments 4687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4688 ordinal=4688 -->
## Functions

Functions


           2        Bandpass
           3        Bandstop

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
          an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

                    If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
            the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
            (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

               •      attenuation (dB) —

            attenuation is the attenuation in the stopband. attenuation must be greater than 0 and
            expressed in decibels. The default is 60.0.

                    If attenuation is less than or equal to 0, the VI sets the output to 0 and returns an error.

               •      order —

            order specifies the filter order and must be greater than 0. The default is 2.


4688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4689 ordinal=4689 -->
## Functions

Functions


       If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

   •       init/cont (init:F) —

     init/cont controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
     init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
    to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
     this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

   •       Filtered X —

     Filtered X is the output array of filtered samples.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


After calling the Inv Chebyshev Coefficients VI, the Inverse Chebyshev Filter VI obtains a
Chebyshev II Filtered X sequence by calling the IIR Cascade Filter VI.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\IIR Filter
   Design.vi


                                                    © National Instruments 4689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4690 ordinal=4690 -->
## Functions

Functions

       InverseInverse ChebyshevChebyshev FilterFilter (CDB)(CDB) VIVI

       Generates a digital Chebyshev II filter by calling the Inv Chebyshev Coefficients VI. Wire
       data to the X input to determine the polymorphic instance to use or manually select
       the instance.


      Inputs/Outputs

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
          an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.


4690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4691 ordinal=4691 -->
## Functions

Functions


  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
  the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
  (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

•      attenuation (dB) —

  attenuation is the attenuation in the stopband. attenuation must be greater than 0 and
  expressed in decibels. The default is 60.0.

   If attenuation is less than or equal to 0, the VI sets the output to 0 and returns an error.

•      order —

  order specifies the filter order and must be greater than 0. The default is 2.

   If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

•       init/cont (init:F) —

  init/cont controls the initialization of the internal states. The default is FALSE.

  The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
  init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
  to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
   this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

•       Filtered X —

  Filtered X is the output array of filtered samples.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
  Code VI to convert the error code or warning into an error cluster.


                                                   © National Instruments 4691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4692 ordinal=4692 -->
## Functions

Functions

        After calling the Inv Chebyshev Coefficients VI, the Inverse Chebyshev Filter VI obtains a
      Chebyshev II Filtered X sequence by calling the IIR Cascade Filter VI.

      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\IIR Filter
        Design.vi

       EllipticElliptic FilterFilter

       Generates a digital elliptic filter by calling the Elliptic Coefficients VI. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


            •  Elliptic Filter (DBL) VI
            •  Elliptic Filter (CDB) VI

        After calling the Elliptic Coefficients VI, the Elliptic Filter VI calls the IIR Cascade Filter VI
       to obtain an elliptic Filtered X sequence.

      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

4692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4693 ordinal=4693 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\IIR Filter
   Design.vi

EllipticElliptic FilterFilter (DBL)(DBL) VIVI

Generates a digital elliptic filter by calling the Elliptic Coefficients VI. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •        filter type —

      filter type specifies the passband of the filter.

    0        Lowpass
    1         Highpass
    2        Bandpass
    3        Bandstop

   •      passband ripple (dB) —

    passband ripple is the ripple in the passband. passband ripple must be greater than 0 and
    expressed in decibels. The default is 1.0.

       If passband ripple is less than or equal to 0, the VI sets the output filter data to an empty array
    and returns an error.

   •     X —

                                                    © National Instruments 4693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4694 ordinal=4694 -->
## Functions

Functions


          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
          an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

                    If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
            the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
            (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

               •      stopband attenuation (dB) —

           stopband attenuation is the attenuation in the stopband. stopband attenuation must be greater
           than 0 and expressed in decibels. The default is 60.0.

                    If stopband attenuation is less than or equal to 0, the VI sets Filtered X to an empty array and
             returns an error.

               Note If the filter order is high, this VI uses a higher attenuation than the value of
                   stopband attenuation to design the filter.

               •      order —

            order is the order of the IIR filter and must be greater than 0. The default is 2.0.

                    If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.


4694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4695 ordinal=4695 -->
## Functions

Functions

   •       init/cont (init:F) —

     init/cont controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
     init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
    to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
     this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

   •       Filtered X —

     Filtered X is the output array of filtered samples.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


After calling the Elliptic Coefficients VI, the Elliptic Filter VI calls the IIR Cascade Filter VI
to obtain an elliptic Filtered X sequence.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\IIR Filter
   Design.vi

EllipticElliptic FilterFilter (CDB)(CDB) VIVI

Generates a digital elliptic filter by calling the Elliptic Coefficients VI. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4696 ordinal=4696 -->
## Functions

Functions


      Inputs/Outputs

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •      passband ripple (dB) —

           passband ripple is the ripple in the passband. passband ripple must be greater than 0 and
            expressed in decibels. The default is 1.0.

                    If passband ripple is less than or equal to 0, the VI sets the output filter data to an empty array
          and returns an error.

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
          an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.


4696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4697 ordinal=4697 -->
## Functions

Functions


  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
  the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
  (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

•      stopband attenuation (dB) —

  stopband attenuation is the attenuation in the stopband. stopband attenuation must be greater
  than 0 and expressed in decibels. The default is 60.0.

   If stopband attenuation is less than or equal to 0, the VI sets Filtered X to an empty array and
  returns an error.

        Note If the filter order is high, this VI uses a higher attenuation than the value of
          stopband attenuation to design the filter.

•      order —

  order is the order of the IIR filter and must be greater than 0. The default is 2.0.

   If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

•       init/cont (init:F) —

  init/cont controls the initialization of the internal states. The default is FALSE.

  The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
  init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
  to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
   this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

•       Filtered X —

  Filtered X is the output array of filtered samples.

•       error —

                                                   © National Instruments 4697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4698 ordinal=4698 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        After calling the Elliptic Coefficients VI, the Elliptic Filter VI calls the IIR Cascade Filter VI
       to obtain an elliptic Filtered X sequence.

      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\IIR Filter
        Design.vi

      BesselBessel FilterFilter

       Generates a digital Bessel filter by calling the Bessel Coefficients VI. Wire data to the X
       input to determine the polymorphic instance to use or manually select the instance.


            • Bessel Filter (DBL) VI
            • Bessel Filter (CDB) VI

        After calling the Bessel Coefficients VI, the Bessel Filter VI calls the IIR Cascade Filter VI
       to obtain a Bessel Filtered X sequence.

      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

4698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4699 ordinal=4699 -->
## Functions

Functions

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

You can use the Filter Express VI to view the transfer functions used for the Bessel Filter
VI. Select Bessel in the Topology pull-down menu and select Transfer function in the
View Mode section of the Filter Express VI configuration dialog box.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\IIR Filter
   Design.vi

BesselBessel FilterFilter (DBL)(DBL) VIVI

Generates a digital Bessel filter by calling the Bessel Coefficients VI. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •        filter type —

      filter type specifies the passband of the filter.

    0        Lowpass
    1         Highpass
    2        Bandpass
    3        Bandstop

   •     X —

                                                    © National Instruments 4699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4700 ordinal=4700 -->
## Functions

Functions


          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
          an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

                    If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
            the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
            (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

               •      order —

            order specifies the filter order and must be greater than 0. The default is 2.

                    If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

               •       init/cont (init:F) —

             init/cont controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
             init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
             to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
              this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

               •       Filtered X —


4700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4701 ordinal=4701 -->
## Functions

Functions


     Filtered X is the output array of filtered samples.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


After calling the Bessel Coefficients VI, the Bessel Filter VI calls the IIR Cascade Filter VI
to obtain a Bessel Filtered X sequence.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

You can use the Filter Express VI to view the transfer functions used for the Bessel Filter
VI. Select Bessel in the Topology pull-down menu and select Transfer function in the
View Mode section of the Filter Express VI configuration dialog box.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\IIR Filter
   Design.vi

BesselBessel FilterFilter (CDB)(CDB) VIVI

Generates a digital Bessel filter by calling the Bessel Coefficients VI. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4702 ordinal=4702 -->
## Functions

Functions


      Inputs/Outputs

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered X to an empty array and returns
          an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.


4702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4703 ordinal=4703 -->
## Functions

Functions


       If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
    the VI sets Filtered X to an empty array and returns an error. When filter type is 2 (Bandpass) or 3
    (Bandstop), low cutoff freq: fl must be less than high cutoff freq: fh.

   •      order —

    order specifies the filter order and must be greater than 0. The default is 2.

       If order is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error.

   •       init/cont (init:F) —

     init/cont controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
     init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
    to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
     this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

   •       Filtered X —

     Filtered X is the output array of filtered samples.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


After calling the Bessel Coefficients VI, the Bessel Filter VI calls the IIR Cascade Filter VI
to obtain a Bessel Filtered X sequence.

The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

You can use the Filter Express VI to view the transfer functions used for the Bessel Filter
VI. Select Bessel in the Topology pull-down menu and select Transfer function in the


                                                    © National Instruments 4703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4704 ordinal=4704 -->
## Functions

Functions

      View Mode section of the Filter Express VI configuration dialog box.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\IIR Filter
        Design.vi

      Equi-RippleEqui-Ripple LowPassLowPass

       Generates a lowpass FIR filter with equi-ripple characteristics using the Parks-
       McClellan algorithm and the # of taps, pass freq, stop freq, and sampling freq: fs. The
       Equi-Ripple LowPass VI then applies a linear-phase, lowpass filter to the input
      sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • Equi-Ripple LowPass (DBL) VI
            • Equi-Ripple LowPass (CDB) VI

      The passband of the filter goes from zero (DC) to pass freq. The transition band goes
      from pass freq to stop freq. The stopband goes from stop freq to the Nyquist
       frequency.

      The values for pass freq and stop freq must observe the following relationship.

      0 < f0 < f1 < 0.5fs

      where f0 is pass freq, f1 is stop freq, and fs is sampling freq: fs. If you violate any of
       these conditions, this VI sets Filtered X to an empty array and returns an error through
       the Parks-McClellan VI.


4704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4705 ordinal=4705 -->
## Functions

Functions

Equi-RippleEqui-Ripple LowPassLowPass (DBL)(DBL) VIVI

Generates a lowpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and the # of taps, pass freq, stop freq, and sampling freq: fs. The
Equi-Ripple LowPass VI then applies a linear-phase, lowpass filter to the input
sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the input signal to filter.

   •      # of taps —

    # of taps must be greater than 2. The default is 32.

       If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
    through the Parks-McClellan VI.

   •      pass freq —

    pass freq must be greater than zero and observe the Nyquist criterion. The default is 0.2 Hz.

       If pass freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
     Filtered X to an empty array and returns an error through the Parks-McClellan VI.

   •      stop freq —

    stop freq must be greater than the pass freq and observe the Nyquist criterion. The default is 0.3
    Hz.

       If stop freq is less than or equal to pass freq or does not meet the Nyquist criterion, the VI sets
     Filtered X to an empty array and returns an error through the Parks-McClellan VI.

   •      sampling freq: fs —

                                                    © National Instruments 4705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4706 ordinal=4706 -->
## Functions

Functions


           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

               •       Filtered X —

             Filtered X contains the result of filtering the input sequence X by convolution.

             This VI calculates the number of elements, k, in Filtered X using the following equation: k= n+
    m– 1, where nis the number of elements in X and mis the number of taps.

             This VI also calculates the delay associated with the output sequence using the following
            equation:

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The passband of the filter goes from zero (DC) to pass freq. The transition band goes
      from pass freq to stop freq. The stopband goes from stop freq to the Nyquist
       frequency.

      The values for pass freq and stop freq must observe the following relationship.

      0 < f0 < f1 < 0.5fs

      where f0 is pass freq, f1 is stop freq, and fs is sampling freq: fs. If you violate any of
       these conditions, this VI sets Filtered X to an empty array and returns an error through
       the Parks-McClellan VI.

      Equi-RippleEqui-Ripple LowPassLowPass (CDB)(CDB) VIVI

       Generates a lowpass FIR filter with equi-ripple characteristics using the Parks-
       McClellan algorithm and the # of taps, pass freq, stop freq, and sampling freq: fs. The
       Equi-Ripple LowPass VI then applies a linear-phase, lowpass filter to the input
      sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


4706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4707 ordinal=4707 -->
## Functions

Functions


Inputs/Outputs

   •     X —

    X is the input signal to filter.

   •      # of taps —

    # of taps must be greater than 2. The default is 32.

       If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
    through the Parks-McClellan VI.

   •      pass freq —

    pass freq must be greater than zero and observe the Nyquist criterion. The default is 0.2 Hz.

       If pass freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
     Filtered X to an empty array and returns an error through the Parks-McClellan VI.

   •      stop freq —

    stop freq must be greater than the pass freq and observe the Nyquist criterion. The default is 0.3
    Hz.

       If stop freq is less than or equal to pass freq or does not meet the Nyquist criterion, the VI sets
     Filtered X to an empty array and returns an error through the Parks-McClellan VI.

   •      sampling freq: fs —

    sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
     0. The default is 1.0 Hz.

   •       Filtered X —

     Filtered X contains the result of filtering the input sequence X by convolution.

    The number of elements, k, in Filtered X is given by the following equation. k= n+ m– 1, where


                                                    © National Instruments 4707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4708 ordinal=4708 -->
## Functions

Functions


      nis the number of elements in X and mis the number of taps.

          A delay is also associated with the output sequence, as given by the following equation.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The passband of the filter goes from zero (DC) to pass freq. The transition band goes
      from pass freq to stop freq. The stopband goes from stop freq to the Nyquist
       frequency.

      The values for pass freq and stop freq must observe the following relationship.

      0 < f0 < f1 < 0.5fs

      where f0 is pass freq, f1 is stop freq, and fs is sampling freq: fs. If you violate any of
       these conditions, this VI sets Filtered X to an empty array and returns an error through
       the Parks-McClellan VI.

      Equi-RippleEqui-Ripple HighPassHighPass

       Generates a highpass FIR filter with equi-ripple characteristics using the Parks-
       McClellan algorithm and the # of taps, stop freq, high freq, and sampling freq: fs. The
       Equi-Ripple HighPass VI then applies a linear-phase, highpass filter to the input
      sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • Equi-Ripple HighPass (DBL) VI
            • Equi-Ripple HighPass (CDB) VI

      The stopband of the filter goes from zero (DC) to the stop freq. The transition band

4708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4709 ordinal=4709 -->
## Functions

Functions

goes from the stop freq to the high freq. The passband goes from the high freq to the
Nyquist frequency.

The values for stop freq and high freq must observe the following relationship.

0 < f0 < f1 < 0.5fs

where f0 is stop freq, f1 is high freq, and fs is sampling freq: fs. If you violate any of
these conditions, this VI sets Filtered X to an empty array and returns an error through
the Parks-McClellan VI.

Equi-RippleEqui-Ripple HighPassHighPass (DBL)(DBL) VIVI

Generates a highpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and the # of taps, stop freq, high freq, and sampling freq: fs. The
Equi-Ripple HighPass VI then applies a linear-phase, highpass filter to the input
sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the input signal to filter.

   •      # of taps —

    # of taps must be greater than 2. The default is 33.

       If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
    through the Parks-McClellan VI.

          Note The Parks-McClellan algorithm introduces a large error when designing a


                                                    © National Instruments 4709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4710 ordinal=4710 -->
## Functions

Functions


                    highpass filter for an even number of taps. To avoid this error, the Equi-Ripple
                    HighPass VI adjusts the number of taps to the next higher odd value if # of taps is
                     even.

               •      stop freq —

            stop freq must be greater than zero and observe the Nyquist criterion. The default is 0.2 Hz.

                    If stop freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
             Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      high freq —

            high freq must be greater than stop freq and observe the Nyquist criterion. The default is 0.3 Hz.

                    If high freq is less than or equal to stop freq or does not meet the Nyquist criterion, the VI sets
             Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

               •       Filtered X —

             Filtered X contains the result of filtering the input sequence X by convolution.

             This VI calculates the number of elements, k, in Filtered X using the following equation: k= n+
    m– 1, where nis the number of elements in X and mis the number of taps.

             This VI also calculates the delay associated with the output sequence using the following
            equation:

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The stopband of the filter goes from zero (DC) to the stop freq. The transition band
      goes from the stop freq to the high freq. The passband goes from the high freq to the
       Nyquist frequency.


4710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4711 ordinal=4711 -->
## Functions

Functions

The values for stop freq and high freq must observe the following relationship.

0 < f0 < f1 < 0.5fs

where f0 is stop freq, f1 is high freq, and fs is sampling freq: fs. If you violate any of
these conditions, this VI sets Filtered X to an empty array and returns an error through
the Parks-McClellan VI.

Equi-RippleEqui-Ripple HighPassHighPass (CDB)(CDB) VIVI

Generates a highpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and the # of taps, stop freq, high freq, and sampling freq: fs. The
Equi-Ripple HighPass VI then applies a linear-phase, highpass filter to the input
sequence X using the Convolution VI to obtain Filtered X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the input signal to filter.

   •      # of taps —

    # of taps must be greater than 2. The default is 33.

       If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
    through the Parks-McClellan VI.

          Note The Parks-McClellan algorithm introduces a large error when designing a
             highpass filter for an even number of taps. To avoid this error, the Equi-Ripple
            HighPass VI adjusts the number of taps to the next higher odd value if # of taps is
             even.

   •      stop freq —

                                                    © National Instruments 4711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4712 ordinal=4712 -->
## Functions

Functions


            stop freq must be greater than zero and observe the Nyquist criterion. The default is 0.2 Hz.

                    If stop freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
             Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      high freq —

            high freq must be greater than stop freq and observe the Nyquist criterion. The default is 0.3 Hz.

                    If high freq is less than or equal to stop freq or does not meet the Nyquist criterion, the VI sets
             Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.

               •       Filtered X —

             Filtered X contains the result of filtering the input sequence X by convolution.

          The number of elements, k, in Filtered X is given by the following equation. k= n+ m– 1, where
      nis the number of elements in X and mis the number of taps.

          A delay is also associated with the output sequence, as given by the following equation.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The stopband of the filter goes from zero (DC) to the stop freq. The transition band
      goes from the stop freq to the high freq. The passband goes from the high freq to the
       Nyquist frequency.

      The values for stop freq and high freq must observe the following relationship.

      0 < f0 < f1 < 0.5fs


4712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4713 ordinal=4713 -->
## Functions

Functions

where f0 is stop freq, f1 is high freq, and fs is sampling freq: fs. If you violate any of
these conditions, this VI sets Filtered X to an empty array and returns an error through
the Parks-McClellan VI.

Equi-RippleEqui-Ripple BandPassBandPass

Generates a bandpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and the higher pass freq, lower pass freq, # of taps, lower stop
freq, higher stop freq, and sampling freq: fs. The Equi-Ripple BandPass VI then
applies a linear-phase, bandpass filter to the input sequence X using the Convolution
VI to obtain Filtered X. Wire data to the X input to determine the polymorphic instance
to use or manually select the instance.


  • Equi-Ripple BandPass (DBL) VI
  • Equi-Ripple BandPass (CDB) VI

The first stopband of the filter region goes from zero (DC) to the lower stop frequency.
The passband region goes from the lower pass frequency to the higher pass frequency.
The second stopband region goes from the higher stop frequency to the Nyquist
frequency.

The values for the stop and pass frequencies must observe the following relationship.

0 < f0 < f1 < f2 < f3 < 0.5fs

where f0 is lower stop freq, f1 is lower pass freq, f2 is higher pass freq, f3 is higher
stop freq, and fs is sampling frequency: fs. If you violate any of these conditions, this
VI sets Filtered X to an empty array and returns an error through the Parks-McClellan
VI.

Equi-RippleEqui-Ripple BandPassBandPass (DBL)(DBL) VIVI

Generates a bandpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and the higher pass freq, lower pass freq, # of taps, lower stop

                                                    © National Instruments 4713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4714 ordinal=4714 -->
## Functions

Functions

        freq, higher stop freq, and sampling freq: fs. The Equi-Ripple BandPass VI then
       applies a linear-phase, bandpass filter to the input sequence X using the Convolution
        VI to obtain Filtered X. Wire data to the X input to determine the polymorphic instance
       to use or manually select the instance.


      Inputs/Outputs

               •      higher pass freq —

            higher pass freq must be greater than lower pass freq frequency and observe the Nyquist
              criterion. The default is 0.35 Hz.

                    If higher pass freq is less than or equal to lower pass freq or does not meet the Nyquist criterion,
            the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      lower pass freq —

           lower pass freq must be greater than the lower stop freq and observe the Nyquist criterion. The
             default is 0.25 Hz.

                    If lower pass freq is less than or equal to lower stop freq or does not meet the Nyquist criterion,
            the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •     X —

          X is the input signal to filter.

               •      # of taps —

           # of taps must be greater than 2. The default is 32.

                    If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
           through the Parks-McClellan VI.

               •      lower stop freq —


4714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4715 ordinal=4715 -->
## Functions

Functions


    lower stop freq must be greater than zero and observe the Nyquist criterion. The default is 0.20
    Hz.

       If lower stop freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
     Filtered X to an empty array and returns an error through the Parks-McClellan VI.

   •      higher stop freq —

    higher stop freq must be greater than higher pass freq and observe the Nyquist criterion. The
     default is 0.4 Hz.

       If higher stop freq is less than or equal to higher pass freq or does not meet the Nyquist
     criterion, the VI sets Filtered X to an empty array and returns an error through the Parks-
    McClellan VI.

   •      sampling freq: fs —

    sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
     0. The default is 1.0 Hz.

   •       Filtered X —

     Filtered X contains the result of filtering the input sequence X by convolution.

    This VI calculates the number of elements, k, in Filtered X using the following equation: k= n+
 m– 1, where nis the number of elements in X and mis the number of taps.

    This VI also calculates the delay associated with the output sequence using the following
    equation:

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The first stopband of the filter region goes from zero (DC) to the lower stop frequency.
The passband region goes from the lower pass frequency to the higher pass frequency.
The second stopband region goes from the higher stop frequency to the Nyquist
frequency.

The values for the stop and pass frequencies must observe the following relationship.

                                                    © National Instruments 4715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4716 ordinal=4716 -->
## Functions

Functions

      0 < f0 < f1 < f2 < f3 < 0.5fs

      where f0 is lower stop freq, f1 is lower pass freq, f2 is higher pass freq, f3 is higher
       stop freq, and fs is sampling frequency: fs. If you violate any of these conditions, this
        VI sets Filtered X to an empty array and returns an error through the Parks-McClellan
         VI.

      Equi-RippleEqui-Ripple BandPassBandPass (CDB)(CDB) VIVI

       Generates a bandpass FIR filter with equi-ripple characteristics using the Parks-
       McClellan algorithm and the higher pass freq, lower pass freq, # of taps, lower stop
        freq, higher stop freq, and sampling freq: fs. The Equi-Ripple BandPass VI then
       applies a linear-phase, bandpass filter to the input sequence X using the Convolution
        VI to obtain Filtered X. Wire data to the X input to determine the polymorphic instance
       to use or manually select the instance.


      Inputs/Outputs

               •      higher pass freq —

            higher pass freq must be greater than lower pass freq frequency and observe the Nyquist
              criterion. The default is 0.35 Hz.

                    If higher pass freq is less than or equal to lower pass freq or does not meet the Nyquist criterion,
            the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      lower pass freq —

           lower pass freq must be greater than the lower stop freq and observe the Nyquist criterion. The
             default is 0.25 Hz.

                    If lower pass freq is less than or equal to lower stop freq or does not meet the Nyquist criterion,


4716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4717 ordinal=4717 -->
## Functions

Functions


  the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

•     X —

  X is the input signal to filter.

•      # of taps —

  # of taps must be greater than 2. The default is 32.

   If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
  through the Parks-McClellan VI.

•      lower stop freq —

  lower stop freq must be greater than zero and observe the Nyquist criterion. The default is 0.20
  Hz.

   If lower stop freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
  Filtered X to an empty array and returns an error through the Parks-McClellan VI.

•      higher stop freq —

  higher stop freq must be greater than higher pass freq and observe the Nyquist criterion. The
  default is 0.4 Hz.

   If higher stop freq is less than or equal to higher pass freq or does not meet the Nyquist
   criterion, the VI sets Filtered X to an empty array and returns an error through the Parks-
  McClellan VI.

•      sampling freq: fs —

  sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
   0. The default is 1.0 Hz.

•       Filtered X —

  Filtered X contains the result of filtering the input sequence X by convolution.

  The number of elements, k, in Filtered X is given by the following equation. k= n+ m– 1, where
 nis the number of elements in X and mis the number of taps.

  A delay is also associated with the output sequence, as given by the following equation.


                                                   © National Instruments 4717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4718 ordinal=4718 -->
## Functions

Functions


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The first stopband of the filter region goes from zero (DC) to the lower stop frequency.
      The passband region goes from the lower pass frequency to the higher pass frequency.
      The second stopband region goes from the higher stop frequency to the Nyquist
       frequency.

      The values for the stop and pass frequencies must observe the following relationship.

      0 < f0 < f1 < f2 < f3 < 0.5fs

      where f0 is lower stop freq, f1 is lower pass freq, f2 is higher pass freq, f3 is higher
       stop freq, and fs is sampling frequency: fs. If you violate any of these conditions, this
        VI sets Filtered X to an empty array and returns an error through the Parks-McClellan
         VI.

      Equi-RippleEqui-Ripple BandStopBandStop

       Generates a bandstop FIR digital filter with equi-ripple characteristics using the Parks-
       McClellan algorithm and higher pass freq, lower pass freq, # of taps, lower stop freq,
       higher stop freq, and sampling freq: fs. The Equi-Ripple BandStop VI then applies a
       linear-phase, bandstop filter to the input sequence X using the Convolution VI to
       obtain Filtered X. Wire data to the X input to determine the polymorphic instance to
      use or manually select the instance.


            • Equi-Ripple BandStop (DBL) VI
            • Equi-Ripple BandStop (CDB) VI


4718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4719 ordinal=4719 -->
## Functions

Functions

The first passband region of the filter goes from zero (DC) to the lower pass freq. The
stopband region goes from the lower stop freq to the higher stop freq. The second
passband region goes from the higher pass freq to the Nyquist frequency.

The values of the stop and pass frequencies must observe the following relationship.

0 < f0 < f1 < f2 < f3 < 0.5fs

where f0 is lower pass freq, f1 is lower stop freq, f2 is higher stop freq, f3 is higher
pass freq, and fs is sampling freq: fs. If you violate any of these conditions, this VI sets
Filtered X to an empty array and returns an error through the Parks-McClellan VI.

Equi-RippleEqui-Ripple BandStopBandStop (DBL)(DBL) VIVI

Generates a bandstop FIR digital filter with equi-ripple characteristics using the Parks-
McClellan algorithm and higher pass freq, lower pass freq, # of taps, lower stop freq,
higher stop freq, and sampling freq: fs. The Equi-Ripple BandStop VI then applies a
linear-phase, bandstop filter to the input sequence X using the Convolution VI to
obtain Filtered X. Wire data to the X input to determine the polymorphic instance to
use or manually select the instance.


Inputs/Outputs

   •      higher pass freq —

    higher pass freq must be greater than higher stop freq and observe the Nyquist criterion. The
     default is 0.4 Hz.

       If higher pass freq is less than or equal to higher stop freq or does not meet the Nyquist
     criterion, the VI sets Filtered X to an empty array and returns an error through the Parks-
    McClellan VI.


                                                    © National Instruments 4719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4720 ordinal=4720 -->
## Functions

Functions

               •      lower pass freq —

           lower pass freq must be greater than zero and observe the Nyquist criterion. The default is 0.2
            Hz.

                    If lower pass freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
             Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •     X —

          X is the input signal to filter.

               •      # of taps —

           # of taps must be greater than 2. The default is 33.

                    If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
           through the Parks-McClellan VI.

               Note The Parks-McClellan algorithm introduces a large error when you design a
                   bandstop filter for an even number of taps. To avoid this error, the Equi-Ripple
                  BandStop VI adjusts the number of taps to the next higher odd value if # of taps is
                     even.

               •      lower stop freq —

           lower stop freq must be greater than lower pass freq and observe the Nyquist criterion. The
             default is 0.25 Hz.

                    If lower stop freq is less than or equal to lower pass freq or does not meet the Nyquist criterion,
            the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      higher stop freq —

            higher stop freq must be greater than lower stop freq and observe the Nyquist criterion. The
             default is 0.35 Hz.

                    If higher stop freq is less than or equal to lower stop freq or does not meet the Nyquist criterion,
            the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
               0. The default is 1.0 Hz.


4720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4721 ordinal=4721 -->
## Functions

Functions

   •       Filtered X —

     Filtered X contains the result of filtering the input sequence X by convolution.

    This VI calculates the number of elements, k, in Filtered X using the following equation: k= n+
 m– 1, where nis the number of elements in X and mis the number of taps.

    This VI also calculates the delay associated with the output sequence using the following
    equation:

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The first passband region of the filter goes from zero (DC) to the lower pass freq. The
stopband region goes from the lower stop freq to the higher stop freq. The second
passband region goes from the higher pass freq to the Nyquist frequency.

The values of the stop and pass frequencies must observe the following relationship.

0 < f0 < f1 < f2 < f3 < 0.5fs

where f0 is lower pass freq, f1 is lower stop freq, f2 is higher stop freq, f3 is higher
pass freq, and fs is sampling freq: fs. If you violate any of these conditions, this VI sets
Filtered X to an empty array and returns an error through the Parks-McClellan VI.

Equi-RippleEqui-Ripple BandStopBandStop (CDB)(CDB) VIVI

Generates a bandstop FIR digital filter with equi-ripple characteristics using the Parks-
McClellan algorithm and higher pass freq, lower pass freq, # of taps, lower stop freq,
higher stop freq, and sampling freq: fs. The Equi-Ripple BandStop VI then applies a
linear-phase, bandstop filter to the input sequence X using the Convolution VI to
obtain Filtered X. Wire data to the X input to determine the polymorphic instance to
use or manually select the instance.


                                                    © National Instruments 4721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4722 ordinal=4722 -->
## Functions

Functions


      Inputs/Outputs

               •      higher pass freq —

            higher pass freq must be greater than higher stop freq and observe the Nyquist criterion. The
             default is 0.4 Hz.

                    If higher pass freq is less than or equal to higher stop freq or does not meet the Nyquist
              criterion, the VI sets Filtered X to an empty array and returns an error through the Parks-
            McClellan VI.

               •      lower pass freq —

           lower pass freq must be greater than zero and observe the Nyquist criterion. The default is 0.2
            Hz.

                    If lower pass freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
             Filtered X to an empty array and returns an error through the Parks-McClellan VI.

               •     X —

          X is the input signal to filter.

               •      # of taps —

           # of taps must be greater than 2. The default is 33.

                    If # of taps is less than or equal to 2, the VI sets Filtered X to an empty array and returns an error
           through the Parks-McClellan VI.

               Note The Parks-McClellan algorithm introduces a large error when you design a
                   bandstop filter for an even number of taps. To avoid this error, the Equi-Ripple
                  BandStop VI adjusts the number of taps to the next higher odd value if # of taps is
                     even.

               •      lower stop freq —


4722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4723 ordinal=4723 -->
## Functions

Functions


    lower stop freq must be greater than lower pass freq and observe the Nyquist criterion. The
     default is 0.25 Hz.

       If lower stop freq is less than or equal to lower pass freq or does not meet the Nyquist criterion,
    the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

   •      higher stop freq —

    higher stop freq must be greater than lower stop freq and observe the Nyquist criterion. The
     default is 0.35 Hz.

       If higher stop freq is less than or equal to lower stop freq or does not meet the Nyquist criterion,
    the VI sets Filtered X to an empty array and returns an error through the Parks-McClellan VI.

   •      sampling freq: fs —

    sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
     0. The default is 1.0 Hz.

   •       Filtered X —

     Filtered X contains the result of filtering the input sequence X by convolution.

    The number of elements, k, in Filtered X is given by the following equation. k= n+ m– 1, where
  nis the number of elements in X and mis the number of taps.

    A delay is also associated with the output sequence, as given by the following equation.


   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The first passband region of the filter goes from zero (DC) to the lower pass freq. The
stopband region goes from the lower stop freq to the higher stop freq. The second
passband region goes from the higher pass freq to the Nyquist frequency.

The values of the stop and pass frequencies must observe the following relationship.

0 < f0 < f1 < f2 < f3 < 0.5fs

                                                    © National Instruments 4723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4724 ordinal=4724 -->
## Functions

Functions

      where f0 is lower pass freq, f1 is lower stop freq, f2 is higher stop freq, f3 is higher
      pass freq, and fs is sampling freq: fs. If you violate any of these conditions, this VI sets
       Filtered X to an empty array and returns an error through the Parks-McClellan VI.

      InverseInverse ff FilterFilter

       Designs and implements an IIR filter whose magnitude-squared response is inversely
       proportional to frequency over a specified frequency range. This inverse-f filter is
        typically used to colorize spectrally flat, or white, noise. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • Inverse f Filter (DBL) VI
            • Inverse f Filter (CDB) VI

       InverseInverse ff FilterFilter (DBL)(DBL) VIVI

       Designs and implements an IIR filter whose magnitude-squared response is inversely
       proportional to frequency over a specified frequency range. This inverse-f filter is
        typically used to colorize spectrally flat, or white, noise. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       reset —

             reset forces the filter coefficients to be redesigned and the internal filter states to be reset to
            zero when it is TRUE. The default is FALSE.

               •     X —

4724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4725 ordinal=4725 -->
## Functions

Functions


  X is the input array of samples to filter.

•        fs —

   fs specifies the design sample rate in samples/second.

•      exponent —

  exponent specifies the exponent of the desired inverse-f spectral shape.

  This VI designs a digital filter with the desired magnitude-squared response of 1/
  frequencyexponent.

•        filter specifications —

   filter specifications specifies the operating frequency range and the filter order of the filter.

      •      lower cutoff freq —

      lower cutoff freq specifies the lower frequency edge of the operating frequency range of the
         filter.

      •      higher cutoff freq —

      higher cutoff freq specifies the higher frequency edge of the operating frequency range of
      the filter.

      •      order —

      order specifies the number of first order stages of the inverse-f filter. Increasing order
      improves the inverse-f spectral shape but requires more computation time during filter
       operation.


•      unity gain freq (rad/s) —

  unity gain freq specifies the frequency in radians per second at which the ideal inverse-f filter
  response has unity gain.

  The actual inverse-f filter is designed to approximate the ideal filter over the frequency range
  defined by filter specifications. Therefore, the actual gain of the filter at unity gain freq is near
  unity only if unity gain freq is within the design frequency range specified in filter
  specifications.


                                                   © National Instruments 4725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4726 ordinal=4726 -->
## Functions

Functions

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •        filter information —

                filter information returns the magnitude and phase of the frequency response of the designed
              inverse-f filter.

                     •      magnitude (dB) —

              magnitude returns the magnitude of the frequency response of the designed inverse-f filter
                   in dB.

                           •      frequency (Hz) —

                   frequency returns the frequencies of the frequency response of the designed inverse-f
                            filter in Hz.

                           •      magnitude (dB) —

                  magnitude returns the magnitudes of the frequency response of the designed inverse-f
                            filter in dB.


                     •      phase (deg) —

              phase returns the phase of the frequency response of the designed inverse-f filter in
                 degrees.

                           •      frequency (Hz) —

                   frequency returns the frequencies of the frequency response of the designed inverse-f
                            filter in Hz.

                           •      phase (deg) —

                  phase returns the phases of the frequency response of the designed inverse-f filter in
                     degrees.


               •      magnitude error (dB) —


4726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4727 ordinal=4727 -->
## Functions

Functions


    magnitude error returns the magnitude of the deviation of the actual inverse-f filter in dB when
    measured against the ideal inverse-f filter.

                                                                         exponent    The ideal filter has a magnitude-squared response proportional to 1/f        over the
    frequency range specified by filter specifications.

         •      frequency (Hz) —

        frequency returns the frequencies of the magnitude error in Hz.

         •      magnitude (dB) —

       magnitude returns the magnitudes of the magnitude error in dB.


   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •      noise bandwidth —

    noise bandwidth returns the expected noise bandwidth of the designed inverse-f filter.


InverseInverse ff FilterFilter (CDB)(CDB) VIVI

Designs and implements an IIR filter whose magnitude-squared response is inversely
proportional to frequency over a specified frequency range. This inverse-f filter is
typically used to colorize spectrally flat, or white, noise. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       reset —

                                                    © National Instruments 4727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4728 ordinal=4728 -->
## Functions

Functions


             reset forces the filter coefficients to be redesigned and the internal filter states to be reset to
            zero when it is TRUE. The default is FALSE.

               •     X —

          X is the input array of samples to filter.

               •        fs —

               fs specifies the design sample rate in samples/second.

               •      exponent —

           exponent specifies the exponent of the desired inverse-f spectral shape.

             This VI designs a digital filter with the desired magnitude-squared response of 1/
             frequencyexponent.

               •        filter specifications —

                filter specifications specifies the operating frequency range and the filter order of the filter.

                     •      lower cutoff freq —

               lower cutoff freq specifies the lower frequency edge of the operating frequency range of the
                        filter.

                     •      higher cutoff freq —

                higher cutoff freq specifies the higher frequency edge of the operating frequency range of
                the filter.

                     •      order —

                order specifies the number of first order stages of the inverse-f filter. Increasing order
               improves the inverse-f spectral shape but requires more computation time during filter
                 operation.


               •      unity gain freq (rad/s) —

            unity gain freq specifies the frequency in radians per second at which the ideal inverse-f filter
            response has unity gain.


4728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4729 ordinal=4729 -->
## Functions

Functions


  The actual inverse-f filter is designed to approximate the ideal filter over the frequency range
  defined by filter specifications. Therefore, the actual gain of the filter at unity gain freq is near
  unity only if unity gain freq is within the design frequency range specified in filter
  specifications.

•       Filtered X —

  Filtered X is the output array of filtered samples.

•        filter information —

   filter information returns the magnitude and phase of the frequency response of the designed
  inverse-f filter.

      •      magnitude (dB) —

      magnitude returns the magnitude of the frequency response of the designed inverse-f filter
       in dB.

             •      frequency (Hz) —

          frequency returns the frequencies of the frequency response of the designed inverse-f
               filter in Hz.

             •      magnitude (dB) —

         magnitude returns the magnitudes of the frequency response of the designed inverse-f
               filter in dB.


      •      phase (deg) —

      phase returns the phase of the frequency response of the designed inverse-f filter in
      degrees.

             •      frequency (Hz) —

          frequency returns the frequencies of the frequency response of the designed inverse-f
               filter in Hz.

             •      phase (deg) —


                                                   © National Instruments 4729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4730 ordinal=4730 -->
## Functions

Functions


                  phase returns the phases of the frequency response of the designed inverse-f filter in
                     degrees.


               •      magnitude error (dB) —

           magnitude error returns the magnitude of the deviation of the actual inverse-f filter in dB when
           measured against the ideal inverse-f filter.

                                                                                 exponent          The ideal filter has a magnitude-squared response proportional to 1/f        over the
            frequency range specified by filter specifications.

                     •      frequency (Hz) —

               frequency returns the frequencies of the magnitude error in Hz.

                     •      magnitude (dB) —

              magnitude returns the magnitudes of the magnitude error in dB.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      noise bandwidth —

            noise bandwidth returns the expected noise bandwidth of the designed inverse-f filter.

     ZeroZero PhasePhase FilterFilter

       Applies a zero phase filter to an input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


4730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4731 ordinal=4731 -->
## Functions

Functions

   • Zero Phase Filter (DBL) VI
   • Zero Phase Filter (CDB) VI
   • Zero Phase Filter (Cascade, DBL) VI
   • Zero Phase Filter (Cascade, CDB) VI

This VI filters the input sequence X as shown in the following illustration:


g–n is the reverted sequence of gn. H(z) is an IIR filter whose coefficients are specified
by Reverse Coefficients and Forward Coefficients.

You must specify the Reverse Coefficients and Forward Coefficients in direct form.
Use the IIR coefficient design VIs on the Advanced IIR Filtering palette to get cascade
form IIR filter coefficients. Then use the Cascade to Direct Coefficients VI to convert the
resulting IIR Filter Cluster to direct form.

With a zero phase filter, the output sequence Filtered X has no phase distortion.
Although the zero phase filter is non-causal, it is useful in offline applications such as
filtering a sound file saved on disk.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Filters\Zero Phase
   Filtering.vi

ZeroZero PhasePhase FilterFilter (DBL)(DBL) VIVI

Applies a zero phase filter to an input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4732 ordinal=4732 -->
## Functions

Functions


      Inputs/Outputs

               •     X —

          X is a real vector.

               •      Reverse Coefficients —

           Reverse Coefficients specifies the reverse coefficients of the zero phase filter.

               •      Forward Coefficients —

           Forward Coefficients specifies the forward coefficients of the zero phase filter.

               •       Filtered X —

             Filtered X returns the filtered signal.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI filters the input sequence X as shown in the following illustration:


     g–n is the reverted sequence of gn. H(z) is an IIR filter whose coefficients are specified
      by Reverse Coefficients and Forward Coefficients.

      You must specify the Reverse Coefficients and Forward Coefficients in direct form.
      Use the IIR coefficient design VIs on the Advanced IIR Filtering palette to get cascade
      form IIR filter coefficients. Then use the Cascade to Direct Coefficients VI to convert the
       resulting IIR Filter Cluster to direct form.

4732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4733 ordinal=4733 -->
## Functions

Functions

With a zero phase filter, the output sequence Filtered X has no phase distortion.
Although the zero phase filter is non-causal, it is useful in offline applications such as
filtering a sound file saved on disk.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\Zero Phase
   Filtering.vi

ZeroZero PhasePhase FilterFilter (CDB)(CDB) VIVI

Applies a zero phase filter to an input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the complex valued input sequence.

   •      Reverse Coefficients —

    Reverse Coefficients specifies the reverse coefficients of the zero phase filter.

   •      Forward Coefficients —

    Forward Coefficients specifies the forward coefficients of the zero phase filter.

   •       Filtered X —

     Filtered X returns the filtered signal.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 4733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4734 ordinal=4734 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


       This VI filters the input sequence X as shown in the following illustration:


     g–n is the reverted sequence of gn. H(z) is an IIR filter whose coefficients are specified
      by Reverse Coefficients and Forward Coefficients.

      You must specify the Reverse Coefficients and Forward Coefficients in direct form.
      Use the IIR coefficient design VIs on the Advanced IIR Filtering palette to get cascade
      form IIR filter coefficients. Then use the Cascade to Direct Coefficients VI to convert the
       resulting IIR Filter Cluster to direct form.

      With a zero phase filter, the output sequence Filtered X has no phase distortion.
      Although the zero phase filter is non-causal, it is useful in offline applications such as
        filtering a sound file saved on disk.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Zero Phase
        Filtering.vi

      ZeroZero PhasePhase FilterFilter (Cascade,(Cascade, DBL)DBL) VIVI

       Applies a zero phase filter to an input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


4734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4735 ordinal=4735 -->
## Functions

Functions

Inputs/Outputs

   •     X —

    X is a real input signal.

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


   •       Filtered X —

     Filtered X returns the filtered signal.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI filters the input sequence X as shown in the following illustration:


                                                    © National Instruments 4735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4736 ordinal=4736 -->
## Functions

Functions


     g–n is the reverted sequence of gn. H(z) is an IIR filter whose coefficients are specified
      by Reverse Coefficients and Forward Coefficients.

      You must specify the Reverse Coefficients and Forward Coefficients in direct form.
      Use the IIR coefficient design VIs on the Advanced IIR Filtering palette to get cascade
      form IIR filter coefficients. Then use the Cascade to Direct Coefficients VI to convert the
       resulting IIR Filter Cluster to direct form.

      With a zero phase filter, the output sequence Filtered X has no phase distortion.
      Although the zero phase filter is non-causal, it is useful in offline applications such as
        filtering a sound file saved on disk.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Zero Phase
        Filtering.vi

      ZeroZero PhasePhase FilterFilter (Cascade,(Cascade, CDB)CDB) VIVI

       Applies a zero phase filter to an input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —


4736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4737 ordinal=4737 -->
## Functions

Functions


    X is a complex valued input signal.

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


   •       Filtered X —

     Filtered X returns the filtered signal.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI filters the input sequence X as shown in the following illustration:


                                                    © National Instruments 4737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4738 ordinal=4738 -->
## Functions

Functions

     g–n is the reverted sequence of gn. H(z) is an IIR filter whose coefficients are specified
      by Reverse Coefficients and Forward Coefficients.

      You must specify the Reverse Coefficients and Forward Coefficients in direct form.
      Use the IIR coefficient design VIs on the Advanced IIR Filtering palette to get cascade
      form IIR filter coefficients. Then use the Cascade to Direct Coefficients VI to convert the
       resulting IIR Filter Cluster to direct form.

      With a zero phase filter, the output sequence Filtered X has no phase distortion.
      Although the zero phase filter is non-causal, it is useful in offline applications such as
        filtering a sound file saved on disk.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Zero Phase
        Filtering.vi

      FIRFIR WindowedWindowed FilterFilter

        Filters the input data sequence, X, using the set of windowed FIR filter coefficients
       specified by the sampling freq: fs, low cutoff freq: fl, high cutoff freq: fh, and number
       of taps. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


            • FIR Windowed Filter (DBL) VI
            • FIR Windowed Filter (CDB) VI

      The values for low cutoff freq: fl and high cutoff freq: fh must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs


4738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4739 ordinal=4739 -->
## Functions

Functions

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\FIR Windowed
   Filter Design.vi

FIRFIR WindowedWindowed FilterFilter (DBL)(DBL) VIVI

Filters the input data sequence, X, using the set of windowed FIR filter coefficients
specified by the sampling freq: fs, low cutoff freq: fl, high cutoff freq: fh, and number
of taps. Wire data to the X input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     window parameter —

   window parameter is the beta parameter for a Kaiser window, the standard deviation for a
    Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •        filter type —

      filter type specifies the passband of the filter.


                                                    © National Instruments 4739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4740 ordinal=4740 -->
## Functions

Functions


           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •     X —

          X is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
              zero. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to zero, the VI sets Filtered X to an empty array and
             returns an error.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

                    If low cutoff freq : fl is less than zero or does not meet the Nyquist criterion, the VI sets Filtered X
             to an empty array and returns an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      taps —

            taps determines the total number of FIR coefficients and must be greater than zero. The default
                is 25.

                    If taps is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error. taps
          must be odd for highpass and bandstop filters.

               •     window —


4740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4741 ordinal=4741 -->
## Functions

Functions


   window specifies the type of smoothing window.

    Smoothing windows decrease ripple in the filter passband and improve the ability of the filter to
    attenuate frequency components in the filter stopband.

    0         Rectangle (default)
    1        Hanning
    2       Hamming
    3         Blackman-Harris
    4         Exact Blackman
    5        Blackman
    6           Flat Top
    7        4 Term B-Harris
    8        7 Term B-Harris
    9       Low Sidelobe
    11       Blackman Nuttall
    30         Triangle
    31        Bartlett-Hanning
    32      Bohman
    33        Parzen
    34       Welch
    60        Kaiser
    61       Dolph-Chebyshev
    62        Gaussian

   •       Filtered X —

     Filtered X is the output array of filtered samples. Filtered X has an associated index delay caused
    by the convolution operation.

    This VI calculates the delay using the following equation:

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The values for low cutoff freq: fl and high cutoff freq: fh must observe the following
relationship:


                                                    © National Instruments 4741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4742 ordinal=4742 -->
## Functions

Functions

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\FIR Windowed
        Filter Design.vi

       FIRFIR WindowedWindowed FilterFilter (CDB)(CDB) VIVI

        Filters the input data sequence, X, using the set of windowed FIR filter coefficients
       specified by the sampling freq: fs, low cutoff freq: fl, high cutoff freq: fh, and number
       of taps. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •     window parameter —

          window parameter is the beta parameter for a Kaiser window, the standard deviation for a
            Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •        filter type —


4742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4743 ordinal=4743 -->
## Functions

Functions


   filter type specifies the passband of the filter.

  0        Lowpass
  1         Highpass
  2        Bandpass
  3        Bandstop

•     X —

  X is the input signal to filter.

•      sampling freq: fs —

  sampling freq: fs is the frequency in Hz at which you want to sample X and must be greater than
  zero. The default is 1.0 Hz.

   If sampling freq: fs is less than or equal to zero, the VI sets Filtered X to an empty array and
  returns an error.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq : fl is less than zero or does not meet the Nyquist criterion, the VI sets Filtered X
  to an empty array and returns an error.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      taps —

  taps determines the total number of FIR coefficients and must be greater than zero. The default
   is 25.

   If taps is less than or equal to 0, the VI sets Filtered X to an empty array and returns an error. taps
  must be odd for highpass and bandstop filters.


                                                   © National Instruments 4743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4744 ordinal=4744 -->
## Functions

Functions

               •     window —

          window specifies the type of smoothing window.

           Smoothing windows decrease ripple in the filter passband and improve the ability of the filter to
            attenuate frequency components in the filter stopband.

           0         Rectangle (default)
           1        Hanning
           2       Hamming
           3         Blackman-Harris
           4         Exact Blackman
           5        Blackman
           6           Flat Top
           7        4 Term B-Harris
           8        7 Term B-Harris
           9       Low Sidelobe
           11       Blackman Nuttall
           30         Triangle
           31        Bartlett-Hanning
           32      Bohman
           33        Parzen
           34       Welch
           60        Kaiser
           61       Dolph-Chebyshev
           62        Gaussian

               •       Filtered X —

             Filtered X is the output array of filtered samples. Filtered X has an associated index delay caused
           by the convolution operation.

          The delay is given by the following equation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The values for low cutoff freq: fl and high cutoff freq: fh must observe the following
        relationship:

4744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4745 ordinal=4745 -->
## Functions

Functions

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\FIR Windowed
   Filter Design.vi

MedianMedian FilterFilter

Applies a median filter of rank to the input sequence X.


Inputs/Outputs

   •     X —

    X is the input signal to filter.

    The number of elements, n, in X must be greater than right rank. If the number of elements in X
      is less than or equal to right rank, the VI sets Filtered X to an empty array and returns an error.

   •        left rank —

     left rank is the number of elements used to compute the median filter to the left side. left rank
    must be greater than or equal to 0. The default is 2.

   •       right rank —

     right rank is the number of elements used to compute the median filter to the right side. If right
    rank is less than 0, the VI assumes right rank is equal to left rank. right rank must be less than
    the number of elements in X. The default is -1.

   •       Filtered X —


                                                    © National Instruments 4745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4746 ordinal=4746 -->
## Functions

Functions


             Filtered X is the output array of filtered samples. The size of this array is the same as the input
             array X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Median Filter VI obtains the elements of Filtered X using the following equation.

      yi = Median(Ji) for i= 0, 1, 2, …, n– 1,

      where Yrepresents the output sequence Filtered X, nis the number of elements in the
       input sequence X, Ji is a subset of the input sequence X centered about the ith element
       of X, and the indexed elements outside the range of X equal zero. The following
       equation describes Ji.

      Ji = {xi– rl, xi– rl+ 1, K, xi– 1, xi, xi+ 1, K, xi+ rr– 1, xi+ rr},

      where rlis the filter left rank, and rris the filter right rank.

      The following illustration shows the computation of yi.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Median
        Filtering.vi


4746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4747 ordinal=4747 -->
## Functions

Functions

Savitzky-GolaySavitzky-Golay FilterFilter

Filters the input data sequence X using a Savitzky-Golay FIR smoothing filter. Wire data
to the X input to determine the polymorphic instance to use or manually select the
instance.


  • Savitzky-Golay Filter (DBL) VI
  • Savitzky-Golay Filter (CDB) VI

The Savitzky-Golay filter smoothes a noisy signal by the piece-by-piece fitting of a
polynomial function to the signal. The VI performs the fitting by least squares
minimization. Refer to the Savitzky-Golay Filter Coefficients VI for a detailed
description of how LabVIEW applies a Savitzky-Golay filter to a signal.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\Savitzky-Golay
   Filtering.vi

Savitzky-GolaySavitzky-Golay FilterFilter (DBL)(DBL) VIVI

Filters the input data sequence X using a Savitzky-Golay FIR smoothing filter. Wire data
to the X input to determine the polymorphic instance to use or manually select the
instance.


Inputs/Outputs

   •     X —

                                                    © National Instruments 4747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4748 ordinal=4748 -->
## Functions

Functions


          X is the input array of samples to filter.

               •       side points —

            side points specifies the number of data points to each side of the current data point to use for
            the least squares minimization. side points*2 + 1 is the length of the moving window, which
          must be greater than the polynomial order.

               •      polynomial order —

           polynomial order specifies the order of the polynomial.

               •      Weight —

           Weight specifies a weighting vector to use in the least squares minimization. This array must be
          empty or have a length of side points*2+1.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Savitzky-Golay filter smoothes a noisy signal by the piece-by-piece fitting of a
      polynomial function to the signal. The VI performs the fitting by least squares
       minimization. Refer to the Savitzky-Golay Filter Coefficients VI for a detailed
       description of how LabVIEW applies a Savitzky-Golay filter to a signal.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Savitzky-Golay
        Filtering.vi


4748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4749 ordinal=4749 -->
## Functions

Functions

Savitzky-GolaySavitzky-Golay FilterFilter (CDB)(CDB) VIVI

Filters the input data sequence X using a Savitzky-Golay FIR smoothing filter. Wire data
to the X input to determine the polymorphic instance to use or manually select the
instance.


Inputs/Outputs

   •     X —

    X is the input array of samples to filter.

   •       side points —

    side points specifies the number of data points to each side of the current data point to use for
    the least squares minimization. side points*2 + 1 is the length of the moving window, which
    must be greater than the polynomial order.

   •      polynomial order —

    polynomial order specifies the order of the polynomial.

   •      Weight —

    Weight specifies a weighting vector to use in the least squares minimization. This array must be
    empty or have a length of side points*2+1.

   •       Filtered X —

     Filtered X is the output array of filtered samples.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Savitzky-Golay filter smoothes a noisy signal by the piece-by-piece fitting of a

                                                    © National Instruments 4749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4750 ordinal=4750 -->
## Functions

Functions

      polynomial function to the signal. The VI performs the fitting by least squares
       minimization. Refer to the Savitzky-Golay Filter Coefficients VI for a detailed
       description of how LabVIEW applies a Savitzky-Golay filter to a signal.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Savitzky-Golay
        Filtering.vi

     MathematicalMathematical MorphologicalMorphological FilterFilter

        Filters the input data sequence X with Structure Element using a mathematical
       morphological filter.


      Inputs/Outputs

               •     X extension type —

          X extension type specifies the method by which to extend the input X at both ends of the
            sequence.

           0 Zero padding (default)—Extends X by padding zeros to both ends of the original X.
           1 Symmetric—Extends X to form a new sequence that is symmetric at both ends of the original X.
           2 Periodic—Extends X to form a new sequence that is periodic at both ends of the original X.

               •     X —

          X is the input signal to filter.

               •      Structure Element —

            Structure Element specifies the structure element to use in the filtering process.


4750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4751 ordinal=4751 -->
## Functions

Functions

   •      operation type —

    operation type specifies the fundamental operation of the morphological filter.

    0 Dilation (default)—Specifies to perform dilation on the input sequence X.
    1 Erosion—Specifies to perform erosion on the input sequence X.

   •      zero phase? —

    zero phase? specifies whether to perform zero-phase filtering of the signal. The default is TRUE.

   •       Filtered X —

     Filtered X returns the filtered signal.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI concatenates the input signal X with a sequence of length kat both ends before
filtering according to X extension type, where kis the length of Structure Element.

The following illustration represents the new sequence when X extension type is Zero
padding.


The following illustration represents the new sequence when X extension type is
Symmetric.


If k> n, this VI pads X with k– nzeros at both ends of the new sequence, where nis


                                                    © National Instruments 4751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4752 ordinal=4752 -->
## Functions

Functions

       the length of X.

      The following illustration represents the new sequence when X extension type is
     Periodic.


           If k> n, this VI periodically repeats X more than once at both ends of the sequence.

      The Mathematical Morphological Filter VI can perform two basic operations, dilation
      and erosion.

      Dilation

      The dilation of a 1D signal fis defined as follows:

       D(i) = max{x(i– j) + s(j)}, 0 ≤ i≤ n– 1, 0 ≤ j≤ k– 1

      where x(i) is the i-th element in X and s(j) is the j-th element in Structure Element.

      The following front panel shows an example of the dilation effect. The original signal
       consists of two pulses with widths of 20 and the Structure Element is an array of ten
       zeros. The filtered signal expands the pulses in the original signal.


4752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4753 ordinal=4753 -->
## Functions

Functions

Erosion

The erosion of a 1D signal fis defined as follows:

E(i) = min{x(i+ j) – s(j)}, 0 ≤ i≤ n– 1, 0 ≤ j≤ k– 1

where x(i) is the i-th element in X and s(j) is the j-th element in Structure Element.

The following front panel shows an example of the erosion effect. The original signal
consists of two pulses with widths of 20 and the Structure Element is an array of ten
zeros. The filtered signal shrinks the pulses in the original signal.


You can use mathematical morphological filters to reduce various types of noise in an
input signal while preserving the compatibility of those shapes with the size of the
structure element. The following front panel shows the result of using a mathematical
morphological filter to remove the baseline and suppress the noise in an ECG signal.


                                                    © National Instruments 4753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4754 ordinal=4754 -->
## Functions

Functions


       Refer to the Mathematical Morphological Filters document on the NI Community Web
        site for more information about using mathematical morphological filters in LabVIEW.

     AdvancedAdvanced IIRIIR FilteringFiltering

      Use the Advanced IIR Filtering VIs to implement advanced IIR filters.

      The VIs on this palette can return signal processing error codes.


         Palette
                      Description
        Object

        Butterworth Generates the set of filter coefficients to implement an IIR filter as specified by the
          Coefficients  Butterworth filter model.


4754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4755 ordinal=4755 -->
## Functions

Functions


Palette             Description
Object

Chebyshev   Generates the set of filter coefficients to implement an IIR filter as specified by the
Coefficients  Chebyshev filter model.


Inv            Generates the set of filter coefficients to implement an IIR filter as specified by theChebyshev           Chebyshev II Filter model.
Coefficients

Elliptic
            Generates the set of filter coefficients to implement a digital elliptic IIR filter.Coefficients


Bessel       Generates the set of filter coefficients to implement an IIR filter as specified by the
Coefficients  Bessel filter model.

Butterworth
Order        Estimates the Butterworth filter order.
Estimation

Chebyshev
Order        Estimates the Chebyshev I filter order.
Estimation

Inverse
Chebyshev             Estimates the Inverse Chebyshev filter order.
Order
Estimation

Elliptic
Order        Estimates the Elliptic filter order.
Estimation

Smoothing
             Designs filter coefficients for a smoothing filter. You can use this VI to design a
Filter
            moving-average FIR filter or an exponentially-averaging IIR filter.
Coefficients


Inverse f     Designs an IIR filter whose magnitude-squared response is inversely proportional to
Filter        frequency over a specified frequency range. This inverse-f filter is typically used to
Coefficients  colorize spectrally flat, or white, noise.


                                                    © National Instruments 4755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4756 ordinal=4756 -->
## Functions

Functions


         Palette                      Description
        Object

                          Filters the input sequence X using the cascade form of the IIR filter specified by the IIR           IIR Cascade                          Filter Cluster. Wire data to the X input to determine the polymorphic instance to use           Filter                      or manually select the instance.


                          Filters the input sequence X using the cascade form of the IIR filter specified by the IIR
           IIR Cascade                          Filter Cluster. This VI is similar to the IIR Cascade Filter VI except that you specify the           Filter with                             initial conditions for this VI. Wire data to the X input to determine the polymorphic            I.C.                      instance to use or manually select the instance.


                          Filters the input sequence X using the direct form IIR filter specified by Reverse
           IIR Filter      Coefficients and Forward Coefficients. Wire data to the X input to determine the
                    polymorphic instance to use or manually select the instance.


                          Filters the input sequence X using the direct form IIR filter specified by Reverse
                       Coefficients and Forward Coefficients. You can use this VI to process blocks of           IIR Filter                     continuous data. This VI is similar to the IIR Filter VI except that you specify the initial        with I.C.
                      conditions for this VI. Wire data to the X input to determine the polymorphic instance
                      to use or manually select the instance.

        Cascade To
         Direct       Converts IIR filter coefficients from the cascade form to the direct form.
          Coefficients

      ButterworthButterworth CoefficientsCoefficients

       Generates the set of filter coefficients to implement an IIR filter as specified by the
       Butterworth filter model.

      You can pass these filter coefficients, IIR Filter Cluster, to the IIR Cascade Filter VI to
         filter a sequence of data.


4756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4757 ordinal=4757 -->
## Functions

Functions


Inputs/Outputs

   •        filter structure option —

      filter structure option specifies the order of the IIR cascade filter in IIR Filter Cluster.

    0 IIR 2nd Order—Returns IIR second-order filter stages.
    1 IIR 4th Order—Returns IIR fourth-order filter stages.
     Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
     according to the filter type. If filter type is Lowpass or Highpass, this VI returns IIR second-
    2
     order filter stages. If filter type is Bandpass or Bandstop, this VI returns IIR fourth-order
        filter stages.

   •        filter type —

      filter type specifies the passband of the filter.

    0        Lowpass
    1         Highpass
    2        Bandpass
    3        Bandstop

   •      sampling freq: fs —

    sampling freq: fs is the sampling frequency in Hz and must be greater than zero. The default is
     1.0 Hz.

       If sampling freq: fs is less than or equal to zero, the VI sets Reverse Coefficients and Forward
     Coefficients to empty arrays and returns an error.

   •      high cutoff freq: fh —

    high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

    The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
    2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and


                                                    © National Instruments 4757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4758 ordinal=4758 -->
## Functions

Functions


           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion.

                    If low cutoff freq: fl is less than zero or greater than half the sampling frequency, this VI sets
           Reverse Coefficients and Forward Coefficients to empty arrays and returns an error.

               Note All cutoff frequencies must be less than half the sampling frequency.

               •      order —

            order is the order of the IIR filter and must be greater than zero. If order is less than or equal to
              zero, the VI sets Reverse Coefficients and Forward Coefficients to empty arrays and returns an
               error.

               •       IIR Filter Cluster —

              IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

                     •        filter structure —

                     filter structure indicates either IIR second-order or IIR fourth-order filter stages.

                     •      Reverse Coefficients —

               Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

                     •      Forward Coefficients —

              Forward Coefficients is the forward coefficients of the IIR cascade filter.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Butterworth Coefficients VI is a subVI of the Butterworth Filter VI.


4758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4759 ordinal=4759 -->
## Functions

Functions

ChebyshevChebyshev CoefficientsCoefficients

Generates the set of filter coefficients to implement an IIR filter as specified by the
Chebyshev filter model.

You can pass these coefficients to the IIR Cascade Filter VI to filter a sequence of data.


Inputs/Outputs

   •        filter structure option —

      filter structure option specifies the order of the IIR cascade filter in IIR Filter Cluster.

    0 IIR 2nd Order—Returns IIR second-order filter stages.
    1 IIR 4th Order—Returns IIR fourth-order filter stages.
     Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
     according to the filter type. If filter type is Lowpass or Highpass, this VI returns IIR second-
    2
     order filter stages. If filter type is Bandpass or Bandstop, this VI returns IIR fourth-order
        filter stages.

   •        filter type —

      filter type specifies the passband of the filter.

    0        Lowpass
    1         Highpass
    2        Bandpass
    3        Bandstop

   •      sampling freq: fs —

    sampling freq: fs is the sampling frequency in Hz and must be greater than zero. The default is
     1.0 Hz.


                                                    © National Instruments 4759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4760 ordinal=4760 -->
## Functions

Functions


                    If sampling freq: fs is less than or equal to zero, the VI sets IIR Filter Cluster to an empty array
          and returns an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

         When filter type is 2 (Bandpass) or 3 (Bandstop), low cutoff freq: fl must be less than high cutoff
              freq: fh.

               •       ripple(dB) —

             ripple is the ripple in the passband. ripple must be greater than zero and must be expressed in
             decibels. The default is 0.1.

               •      order —

            order is the order of the IIR filter and must be greater than zero.

               •       IIR Filter Cluster —

              IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

                     •        filter structure —

                     filter structure indicates either IIR second-order or IIR fourth-order filter stages.

                     •      Reverse Coefficients —

               Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

                     •      Forward Coefficients —


4760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4761 ordinal=4761 -->
## Functions

Functions


       Forward Coefficients is the forward coefficients of the IIR cascade filter.


   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The values for low cutoff freq: fl and high cutoff freq: fh must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs. If
you violate any of these conditions, this VI sets Reverse Coefficients and Forward
Coefficients to empty arrays and returns an error.

The Chebyshev Coefficients VI is a subVI of the Chebyshev Filter VI.

InvInv ChebyshevChebyshev CoefficientsCoefficients

Generates the set of filter coefficients to implement an IIR filter as specified by the
Chebyshev II Filter model.

You can pass these coefficients to the IIR Cascade Filter VI to filter a sequence of data.


Inputs/Outputs

   •        filter structure option —


                                                    © National Instruments 4761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4762 ordinal=4762 -->
## Functions

Functions


                filter structure option specifies the order of the IIR cascade filter in IIR Filter Cluster.

           0 IIR 2nd Order—Returns IIR second-order filter stages.
           1 IIR 4th Order—Returns IIR fourth-order filter stages.
            Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
             according to the filter type. If filter type is Lowpass or Highpass, this VI returns IIR second-
           2
             order filter stages. If filter type is Bandpass or Bandstop, this VI returns IIR fourth-order
                   filter stages.

               •        filter type —

                filter type specifies the passband of the filter.

                    Lowpass           0                          (default)
           1         Highpass
           2        Bandpass
           3        Bandstop

               •      sampling freq: fs —

           sampling freq: fs is the sampling frequency in Hz and must be greater than zero. The default is
             1.0 Hz.

                    If sampling freq: fs is less than or equal to zero, the VI sets IIR Filter Cluster to an empty array
          and returns an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

         When filter type is 2 (Bandpass) or 3 (Bandstop), low cutoff freq: fl must be less than high cutoff


4762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4763 ordinal=4763 -->
## Functions

Functions


     freq: fh.

   •      attenuation (dB) —

    attenuation is the attenuation in the stopband. attenuation must be greater than 0 and
    expressed in decibels. The default is 60.0.

       If attenuation is less than or equal to 0, the VI sets the output to 0 and returns an error.

   •      order —

    order is the order of the IIR filter and must be greater than zero.

   •       IIR Filter Cluster —

     IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

         •        filter structure —

           filter structure indicates either IIR second-order or IIR fourth-order filter stages.

         •      Reverse Coefficients —

        Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

         •      Forward Coefficients —

       Forward Coefficients is the forward coefficients of the IIR cascade filter.


   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The values for low cutoff freq: fl and high cutoff freq: fh must observe the following
relationship.

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs. If


                                                    © National Instruments 4763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4764 ordinal=4764 -->
## Functions

Functions

      any of these conditions are violated, the VI sets Reverse Coefficients and Forward
       Coefficients to empty arrays and returns an error.

      The Inv Chebyshev Coefficients VI is a subVI of the Inverse Chebyshev Filter VI.

        EllipticElliptic CoefficientsCoefficients

       Generates the set of filter coefficients to implement a digital elliptic IIR filter.

      You can pass these coefficients to the IIR Cascade Filter VI.


      Inputs/Outputs

               •        filter structure option —

                filter structure option specifies the order of the IIR cascade filter in IIR Filter Cluster.

           0 IIR 2nd Order—Returns IIR second-order filter stages.
           1 IIR 4th Order—Returns IIR fourth-order filter stages.
            Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
             according to the filter type. If filter type is Lowpass or Highpass, this VI returns IIR second-
           2
             order filter stages. If filter type is Bandpass or Bandstop, this VI returns IIR fourth-order
                   filter stages.

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass


4764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4765 ordinal=4765 -->
## Functions

Functions


  3        Bandstop

•      sampling freq: fs —

  sampling freq: fs is the sampling frequency in Hz and must be greater than zero. The default is
  1.0 Hz.

   If sampling freq: fs is less than or equal to zero, the VI sets IIR Filter Cluster to an empty array
  and returns an error.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion.

  0 ≤ f1< 0.5fs where f1 is the cutoff frequency, and fs is the sampling frequency. If low cutoff freq :
   fl is less than zero or greater than half the sampling frequency, the VI sets IIR Filter Cluster to an
  empty array and returns an error. The default is 0.125 Hz.

        Note All cutoff frequencies must be less than half fs.

•      passband ripple (dB) —

  passband ripple is the ripple in the passband. passband ripple must be greater than 0 and
  expressed in decibels. The default is 1.0.

   If passband ripple is less than or equal to 0, the VI sets the output filter data to 0 and returns an
   error.

•      order —

  order is the order of the IIR filter and must be greater than zero.

•      stopband attenuation (dB) —

  stopband attenuation is the attenuation in the stopband. stopband attenuation must be greater


                                                   © National Instruments 4765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4766 ordinal=4766 -->
## Functions

Functions


           than zero and you must express it in decibels. The default is 60.0.

                    If stopband attenuation is less than or equal to zero, the VI sets IIR Filter Cluster to an empty
             array and returns an error.

               Note If the filter order is high, this VI uses a higher attenuation than the value of
                   stopband attenuation to design the filter.

               •       IIR Filter Cluster —

              IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

                     •        filter structure —

                     filter structure indicates either IIR second-order or IIR fourth-order filter stages.

                     •      Reverse Coefficients —

               Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

                     •      Forward Coefficients —

              Forward Coefficients is the forward coefficients of the IIR cascade filter.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Elliptic Coefficients VI is a subVI of the Elliptic Filter VI.

      BesselBessel CoefficientsCoefficients

       Generates the set of filter coefficients to implement an IIR filter as specified by the
       Bessel filter model.

      You then can pass these coefficients to the IIR Cascade Filter VI.


4766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4767 ordinal=4767 -->
## Functions

Functions


Inputs/Outputs

   •        filter structure option —

      filter structure option specifies the order of the IIR cascade filter in IIR Filter Cluster.

    0 IIR 2nd Order—Returns IIR second-order filter stages.
    1 IIR 4th Order—Returns IIR fourth-order filter stages.
     Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
     according to the filter type. If filter type is Lowpass or Highpass, this VI returns IIR second-
    2
     order filter stages. If filter type is Bandpass or Bandstop, this VI returns IIR fourth-order
        filter stages.

   •        filter type —

      filter type specifies the passband of the filter.

    0        Lowpass
    1         Highpass
    2        Bandpass
    3        Bandstop

   •      sampling freq: fs —

    sampling freq: fs is the sampling frequency in Hz and must be greater than zero. The default is
     1.0 Hz.

       If sampling freq: fs is less than or equal to zero, the VI sets Reverse Coefficients and Forward
     Coefficients to empty arrays and returns an error.

   •      high cutoff freq: fh —

    high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

    The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
    2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and


                                                    © National Instruments 4767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4768 ordinal=4768 -->
## Functions

Functions


           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

         When filter type is 2 (Bandpass) or 3 (Bandstop), low cutoff freq: fl must be less than high cutoff
              freq: fh.

               •      order —

            order is the order of the IIR filter and must be greater than zero.

               •       IIR Filter Cluster —

              IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

                     •        filter structure —

                     filter structure indicates either IIR second-order or IIR fourth-order filter stages.

                     •      Reverse Coefficients —

               Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

                     •      Forward Coefficients —

              Forward Coefficients is the forward coefficients of the IIR cascade filter.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The values for low cutoff freq: fl and high cutoff freq: fh must observe the following
        relationship.

      0 < f1 < f2 < 0.5fs


4768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4769 ordinal=4769 -->
## Functions

Functions

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs. If
you violate any of these conditions, this VI sets Reverse Coefficients and Forward
Coefficients to empty arrays and returns an error.

The Bessel Coefficients VI is a subVI of the Bessel Filter VI.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\Online
   Filtering.vi

ButterworthButterworth OrderOrder EstimationEstimation

Estimates the Butterworth filter order.


Inputs/Outputs

   •        filter type —

      filter type specifies the type of filter that this VI creates.

            Lowpass
    0
                (default)
    1        Highpass
    2        Bandpass
    3        Bandstop

   •      sampling freq: fs —

    sampling freq: fs is the sampling frequency in hertz. The value must be greater than zero. The
     default is 1.0 Hz, which is the normalized sampling frequency.


                                                    © National Instruments 4769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4770 ordinal=4770 -->
## Functions

Functions

               •       freq specs —

             freq specs specifies the band edge frequencies of the filter in hertz.

                     •      lower pass freq —

               lower pass freq specifies the first passband edge frequency in hertz.

                     •      lower stop freq —

               lower stop freq specifies the first stopband edge frequency in hertz.

                     •      higher pass freq —

                higher pass freq specifies the second passband edge frequency in hertz. The VI ignores this
                 input for lowpass and highpass filters.

                     •      higher stop freq —

                higher stop freq specifies the second stopband edge frequency in hertz. The VI ignores this
                 input for lowpass and highpass filters.


               •       ripple specs —

             ripple specs specifies the ripple level in the passband and stopband of the filter.

                     •      passband —

              passband specifies the ripple level in the passband. The default is 0.1.

                     •      stopband —

               stopband specifies the ripple level in the stopband. The default is 60.

                     •      dB/linear? (T: dB) —

                 dB/linear? specifies whether this VI applies a decibel scale or a linear scale to the ripple
                    levels. If the value is TRUE, this VI applies a decibel scale to the ripple level. If the value is
                FALSE, this VI applies a linear scale to the ripple level. The default is TRUE.


               •       error in (no error) —


4770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4771 ordinal=4771 -->
## Functions

Functions


     error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      estimated order —

    estimated order returns the minimum order value that the filter requires to meet the
     specifications you set.

   •      high cutoff freq —

    high cutoff freq returns the high cutoff frequency. The cutoff frequency corresponds to the half-
    power frequency or the 3 dB frequency.

   •      low cutoff freq —

    low cutoff freq returns the low cutoff frequency. The cutoff frequency corresponds to the half-
    power frequency or the 3 dB frequency.

   •       error out —

     error out contains error information. This output provides standard error out functionality.


The Butterworth Order Estimation VI uses the formula below to estimate the order of a
Butterworth filter:


where Nis the estimated order

Ap the passband ripple in dB

As is the stopband ripple in dB

[ ] means Round Toward +Infinity


                                                    © National Instruments 4771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4772 ordinal=4772 -->
## Functions

Functions

     Ωp and Ωs are calculated as:

      Lowpass filter:


      Highpass filter:


      Bandpass filter:


      Bandstop filter:


      where the various Ω values equal as follows:


      ChebyshevChebyshev OrderOrder EstimationEstimation

       Estimates the Chebyshev I filter order.


4772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4773 ordinal=4773 -->
## Functions

Functions


Inputs/Outputs

   •        filter type —

      filter type specifies the type of filter that this VI creates.

            Lowpass    0                (default)
    1        Highpass
    2        Bandpass
    3        Bandstop

   •      sampling freq: fs —

    sampling freq: fs is the sampling frequency in hertz. The value must be greater than zero. The
     default is 1.0 Hz, which is the normalized sampling frequency.

   •       freq specs —

    freq specs specifies the band edge frequencies of the filter in hertz.

         •      lower pass freq —

        lower pass freq specifies the first passband edge frequency in hertz.

         •      lower stop freq —

        lower stop freq specifies the first stopband edge frequency in hertz.

         •      higher pass freq —

        higher pass freq specifies the second passband edge frequency in hertz. The VI ignores this
         input for lowpass and highpass filters.

         •      higher stop freq —


                                                    © National Instruments 4773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4774 ordinal=4774 -->
## Functions

Functions


                higher stop freq specifies the second stopband edge frequency in hertz. The VI ignores this
                 input for lowpass and highpass filters.


               •       ripple specs —

             ripple specs specifies the ripple level in the passband and stopband of the filter.

                     •      passband —

              passband specifies the ripple level in the passband. The default is 0.1.

                     •      stopband —

               stopband specifies the ripple level in the stopband. The default is 60.

                     •      dB/linear? (T: dB) —

                 dB/linear? specifies whether this VI applies a decibel scale or a linear scale to the ripple
                    levels. If the value is TRUE, this VI applies a decibel scale to the ripple level. If the value is
                FALSE, this VI applies a linear scale to the ripple level. The default is TRUE.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      estimated order —

           estimated order returns the minimum order value that the filter requires to meet the
             specifications you set.

               •      high cutoff freq —

            high cutoff freq returns the high cutoff frequency. The cutoff frequency corresponds to the edge
            frequency of the passband.

               •      low cutoff freq —

           low cutoff freq returns the low cutoff frequency. The cutoff frequency corresponds to the edge
            frequency of the passband.


4774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4775 ordinal=4775 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      passband ripple [dB] —

    passband ripple [dB] returns the ripple level in the passband in decibels.


The Chebyshev Order Estimation VI uses the formula below to estimate the order of a
Chebyshev I filter:


where Nis the estimated order, Ap the passband ripple in dB, As is the stopband
ripple in dB, [ ] means Round Toward +Infinity. Refer to the Butterworth Order
Estimation VI for the definition of Ωp and Ωs.

Related Information

Butterworth Order Estimation

InverseInverse ChebyshevChebyshev OrderOrder EstimationEstimation

Estimates the Inverse Chebyshev filter order.


Inputs/Outputs

   •        filter type —

                                                    © National Instruments 4775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4776 ordinal=4776 -->
## Functions

Functions


                filter type specifies the type of filter that this VI creates.

                   Lowpass
           0                         (default)
           1        Highpass
           2        Bandpass
           3        Bandstop

               •      sampling freq: fs —

           sampling freq: fs is the sampling frequency in hertz. The value must be greater than zero. The
             default is 1.0 Hz, which is the normalized sampling frequency.

               •       freq specs —

             freq specs specifies the band edge frequencies of the filter in hertz.

                     •      lower pass freq —

               lower pass freq specifies the first passband edge frequency in hertz.

                     •      lower stop freq —

               lower stop freq specifies the first stopband edge frequency in hertz.

                     •      higher pass freq —

                higher pass freq specifies the second passband edge frequency in hertz. The VI ignores this
                 input for lowpass and highpass filters.

                     •      higher stop freq —

                higher stop freq specifies the second stopband edge frequency in hertz. The VI ignores this
                 input for lowpass and highpass filters.


               •       ripple specs —

             ripple specs specifies the ripple level in the passband and stopband of the filter.

                     •      passband —


4776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4777 ordinal=4777 -->
## Functions

Functions


       passband specifies the ripple level in the passband. The default is 0.1.

         •      stopband —

        stopband specifies the ripple level in the stopband. The default is 60.

         •      dB/linear? (T: dB) —

         dB/linear? specifies whether this VI applies a decibel scale or a linear scale to the ripple
          levels. If the value is TRUE, this VI applies a decibel scale to the ripple level. If the value is
        FALSE, this VI applies a linear scale to the ripple level. The default is TRUE.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      estimated order —

    estimated order returns the minimum order value that the filter requires to meet the
     specifications you set.

   •      high cutoff freq —

    high cutoff freq returns the high cutoff frequency. The cutoff frequency corresponds to the edge
    frequency of the stopband.

   •      low cutoff freq —

    low cutoff freq returns the low cutoff frequency. The cutoff frequency corresponds to the edge
    frequency of the stopband.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      stopband atten [dB] —

    stopband atten [dB] returns the stopband attenuation in decibels.


The Inverse Chebyshev Order Estimation VI uses the formula below to estimate the

                                                    © National Instruments 4777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4778 ordinal=4778 -->
## Functions

Functions

       order of an Inverse Chebyshev filter:


      where Nis the estimated order, Ap the passband ripple in dB, As is the stopband
       ripple in dB, [ ] means Round Toward +Infinity. Refer to the Butterworth Order
       Estimation VI for the definition of Ωp and Ωs.

        EllipticElliptic OrderOrder EstimationEstimation

       Estimates the Elliptic filter order.


      Inputs/Outputs

               •        filter type —

                filter type specifies the type of filter that this VI creates.

                   Lowpass
           0
                         (default)
           1        Highpass
           2        Bandpass
           3        Bandstop

               •      sampling freq: fs —

           sampling freq: fs is the sampling frequency in hertz. The value must be greater than zero. The
             default is 1.0 Hz, which is the normalized sampling frequency.


4778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4779 ordinal=4779 -->
## Functions

Functions

•       freq specs —

  freq specs specifies the band edge frequencies of the filter in hertz.

      •      lower pass freq —

      lower pass freq specifies the first passband edge frequency in hertz.

      •      lower stop freq —

      lower stop freq specifies the first stopband edge frequency in hertz.

      •      higher pass freq —

      higher pass freq specifies the second passband edge frequency in hertz. The VI ignores this
      input for lowpass and highpass filters.

      •      higher stop freq —

      higher stop freq specifies the second stopband edge frequency in hertz. The VI ignores this
      input for lowpass and highpass filters.


•       ripple specs —

  ripple specs specifies the ripple level in the passband and stopband of the filter.

      •      passband —

      passband specifies the ripple level in the passband. The default is 0.1.

      •      stopband —

      stopband specifies the ripple level in the stopband. The default is 60.

      •      dB/linear? (T: dB) —

       dB/linear? specifies whether this VI applies a decibel scale or a linear scale to the ripple
        levels. If the value is TRUE, this VI applies a decibel scale to the ripple level. If the value is
      FALSE, this VI applies a linear scale to the ripple level. The default is TRUE.


•       error in (no error) —


                                                   © National Instruments 4779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4780 ordinal=4780 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      estimated order —

           estimated order returns the minimum order value that the filter requires to meet the
             specifications you set.

               •      high cutoff freq —

            high cutoff freq returns the high cutoff frequency. The cutoff frequency corresponds to the edge
            frequency of the passband.

               •      low cutoff freq —

           low cutoff freq returns the low cutoff frequency. The cutoff frequency corresponds to the edge
            frequency of the passband.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       ripples [dB] —

             ripples [dB] returns the passband ripple and stopband attenuation of the filter in decibels.

                     •      passband ripple —

              passband ripple returns the ripple level in the passband in decibels.

                     •      stopband atten —

               stopband atten returns the stopband attenuation in decibels.


      The Elliptic Order Estimation VI uses the formula below to estimate the order of an
         Elliptic filter:


4780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4781 ordinal=4781 -->
## Functions

Functions


where N is the estimated order, and F(x)is the complete elliptic integral of the first
kind, which is defined as:


Ap is the passband ripple in dB, As is the stopband ripple in dB, [ ] means Round
Toward +Infinity. Refer to the Butterworth Order Estimation VI for the definition of Ωp
and Ωs.

Related Information

Formula Node and Expression Node Functions

SmoothingSmoothing FilterFilter CoefficientsCoefficients

Designs filter coefficients for a smoothing filter. You can use this VI to design a moving-
average FIR filter or an exponentially-averaging IIR filter.

The VI returns reverse coefficients and forward coefficients for direct connection to
the IIR Filter VI, which is used to implement both FIR and IIR filters.


                                                    © National Instruments 4781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4782 ordinal=4782 -->
## Functions

Functions

      Inputs/Outputs

               •      type —

           type specifies the type of smoothing filter.

           0 moving average (default)—Yields forward-only (FIR) coefficients.
           1 exponential—Yields first-order IIR coefficients.

               •      half-width —

            half-width specifies the half-width of the moving-average filter in samples.

            For a half-width of M, the full width of the moving-average filter is N= 1 + 2Msamples.
             Therefore, the full width Nis always an odd number of samples.

               •      shape —

           shape specifies the shape of the moving-average filter.

             rectangular (default)—All samples in the moving-average window are weighted equally in           0            computing each smoothed output sample.
             triangular—The moving weighting window applied to the samples is triangular with its peak
           1 centered in the middle of the window, ramping down symmetrically on both sides of the center
             sample.

               •      time constant —

           time constant specifies the time constant of the exponential-weighting filter in seconds.

               •        fs —

               fs specifies the sampling frequency in samples per second.

               •      reverse coefficients —

            reverse coefficients contains the reverse, or feedback, coefficients of an IIR filter.

               •      forward coefficients —

           forward coefficients contains the forward coefficients of an IIR filter.

               •       error —


4782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4783 ordinal=4783 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


InverseInverse ff FilterFilter CoefficientsCoefficients

Designs an IIR filter whose magnitude-squared response is inversely proportional to
frequency over a specified frequency range. This inverse-f filter is typically used to
colorize spectrally flat, or white, noise.


Inputs/Outputs

   •      exponent —

    exponent specifies the exponent of the desired inverse-f spectral shape.

    This VI designs a digital filter with the desired magnitude-squared response of 1/
    frequencyexponent.

   •        fs —

     fs specifies the design sample rate in samples/second.

   •        filter specifications —

      filter specifications specifies the operating frequency range and the filter order of the filter.

         •      lower cutoff freq —

        lower cutoff freq specifies the lower frequency edge of the operating frequency range of the
            filter.

         •      higher cutoff freq —


                                                    © National Instruments 4783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4784 ordinal=4784 -->
## Functions

Functions


                higher cutoff freq specifies the higher frequency edge of the operating frequency range of
                the filter.

                     •      order —

                order specifies the number of first order stages of the inverse-f filter. Increasing order
               improves the inverse-f spectral shape but requires more computation time during filter
                 operation.


               •      unity gain freq (rad/s) —

            unity gain freq specifies the frequency in radians per second at which the ideal inverse-f filter
            response has unity gain.

          The actual inverse-f filter is designed to approximate the ideal filter over the frequency range
            defined by filter specifications. Therefore, the actual gain of the filter at unity gain freq is near
             unity only if unity gain freq is within the design frequency range specified in filter
             specifications.

               •       IIR Filter Cluster —

              IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

                     •        filter structure —

                     filter structure indicates either IIR second-order or IIR fourth-order filter stages.

                     •      Reverse Coefficients —

               Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

                     •      Forward Coefficients —

              Forward Coefficients is the forward coefficients of the IIR cascade filter.


               •        filter information —

                filter information returns the magnitude and phase of the frequency response of the designed
              inverse-f filter.


4784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4785 ordinal=4785 -->
## Functions

Functions


      •      magnitude (dB) —

      magnitude returns the magnitude of the frequency response of the designed inverse-f filter
       in dB.

             •      frequency (Hz) —

          frequency returns the frequencies of the frequency response of the designed inverse-f
               filter in Hz.

             •      magnitude (dB) —

         magnitude returns the magnitudes of the frequency response of the designed inverse-f
               filter in dB.


      •      phase (deg) —

      phase returns the phase of the frequency response of the designed inverse-f filter in
      degrees.

             •      frequency (Hz) —

          frequency returns the frequencies of the frequency response of the designed inverse-f
               filter in Hz.

             •      phase (deg) —

         phase returns the phases of the frequency response of the designed inverse-f filter in
           degrees.


•      magnitude error (dB) —

  magnitude error returns the magnitude of the deviation of the actual inverse-f filter in dB when
  measured against the ideal inverse-f filter.

                                                                       exponent  The ideal filter has a magnitude-squared response proportional to 1/f        over the
  frequency range specified by filter specifications.

      •      frequency (Hz) —


                                                   © National Instruments 4785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4786 ordinal=4786 -->
## Functions

Functions


               frequency returns the frequencies of the magnitude error in Hz.

                     •      magnitude (dB) —

              magnitude returns the magnitudes of the magnitude error in dB.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      noise bandwidth —

            noise bandwidth returns the expected noise bandwidth of the designed inverse-f filter.


        IIRIIR CascadeCascade FilterFilter

        Filters the input sequence X using the cascade form of the IIR filter specified by the IIR
        Filter Cluster. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


            •  IIR Cascade Filter (DBL) VI
            •  IIR Cascade Filter (CDB) VI

       This IIR implementation is called cascade because it is a cascade of second- or fourth-
       order filter stages. The output of one filter stage is the input to the next filter stage for
         all Ns filter stages.


4786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4787 ordinal=4787 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\Online
   Filtering.vi
IIRIIR CascadeCascade FilterFilter (DBL)(DBL) VIVI

Filters the input sequence X using the cascade form of the IIR filter specified by the IIR
Filter Cluster. Wire data to the X input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     X —

    X is the input array of samples to filter.

   •       IIR Filter Cluster —

     IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

    This cluster is the output from one of the IIR coefficient design VIs: Butterworth Coefficients,
    Bessel Coefficients, Chebyshev Coefficients, Elliptic Coefficients, or Inv Chebyshev Coefficients.

         •        filter structure —

           filter structure selects IIR second-order or fourth-order filter stages.

        0        IIR 2nd Order
        1        IIR 4th Order

         •      Reverse Coefficients —


                                                    © National Instruments 4787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4788 ordinal=4788 -->
## Functions

Functions


               Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

                     •      Forward Coefficients —

              Forward Coefficients is the forward coefficients of the IIR cascade filter.


               •       init/cont (init:F) —

             init/cont controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
             init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
             to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
              this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This IIR implementation is called cascade because it is a cascade of second- or fourth-
       order filter stages. The output of one filter stage is the input to the next filter stage for
         all Ns filter stages.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Online
        Filtering.vi


4788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4789 ordinal=4789 -->
## Functions

Functions

IIRIIR CascadeCascade FilterFilter (CDB)(CDB) VIVI

Filters the input sequence X using the cascade form of the IIR filter specified by the IIR
Filter Cluster. Wire data to the X input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     X —

    X is the input array of samples to filter.

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


   •       init/cont (init:F) —


                                                    © National Instruments 4789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4790 ordinal=4790 -->
## Functions

Functions


             init/cont controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
             init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
             to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
              this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This IIR implementation is called cascade because it is a cascade of second- or fourth-
       order filter stages. The output of one filter stage is the input to the next filter stage for
         all Ns filter stages.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Online
        Filtering.vi

        IIRIIR CascadeCascade FilterFilter withwith I.C.I.C.

        Filters the input sequence X using the cascade form of the IIR filter specified by the IIR
        Filter Cluster. This VI is similar to the IIR Cascade Filter VI except that you specify the
         initial conditions for this VI. Wire data to the X input to determine the polymorphic
       instance to use or manually select the instance.


4790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4791 ordinal=4791 -->
## Functions

Functions


  •  IIR Cascade Filter with I.C. (DBL) VI
  •  IIR Cascade Filter with I.C. (CDB) VI
IIRIIR CascadeCascade FilterFilter withwith I.C.I.C. (DBL)(DBL) VIVI

Filters the input sequence X using the cascade form of the IIR filter specified by the IIR
Filter Cluster. This VI is similar to the IIR Cascade Filter VI except that you specify the
initial conditions for this VI. Wire data to the X input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the input array of samples to filter.

   •       IIR Filter Cluster —

     IIR Filter Cluster contains the cascaded form of IIR filter coefficients.

    This cluster is the output from one of the IIR coefficient design VIs: Butterworth Coefficients,
    Bessel Coefficients, Chebyshev Coefficients, Elliptic Coefficients, or Inv Chebyshev Coefficients.

         •        filter structure —

           filter structure selects IIR second-order or fourth-order filter stages.

        0        IIR 2nd Order
        1        IIR 4th Order

         •      Reverse Coefficients —


                                                    © National Instruments 4791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4792 ordinal=4792 -->
## Functions

Functions


               Reverse Coefficients is the reverse coefficients of the IIR cascade filter.

                     •      Forward Coefficients —

              Forward Coefficients is the forward coefficients of the IIR cascade filter.


               •        Initial Filter State —

               Initial Filter State contains the initial internal filter state. The Initial Filter State array should be
            the same size as the Reverse Coefficients array in the IIR Filter Cluster.

                    If this array is not the correct size, such as if the array is empty, the array resizes internally and
               initializes to zero before the IIR filtering operation.

          The filtering occurs internally and the filter state is maintained until all samples in array X have
          been passed through the filter. The final filter state array is then passed to the array indicator,
             Final Filter State.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       Final Filter State —

             Final Filter State contains the final, internal filter states, which Initial Filter State can pass to the
            next call to the IIR Cascade Filter with I.C. VI to filter samples continuously.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

    IIRIIR CascadeCascade FilterFilter withwith I.C.I.C. (CDB)(CDB) VIVI

        Filters the input sequence X using the cascade form of the IIR filter specified by the IIR
        Filter Cluster. This VI is similar to the IIR Cascade Filter VI except that you specify the
         initial conditions for this VI. Wire data to the X input to determine the polymorphic
       instance to use or manually select the instance.


4792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4793 ordinal=4793 -->
## Functions

Functions


Inputs/Outputs

   •     X —

    X is the input array of samples to filter.

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


   •        Initial Filter State —

     Initial Filter State contains the initial internal filter state. The Initial Filter State array should be
    the same size as the Reverse Coefficients array in the IIR Filter Cluster.

       If this array is not the correct size, for example empty, the array is resized internally and is
     initialized to zero before the IIR filtering operation.

    The filtering occurs internally and the filter state is maintained until all samples in array X have


                                                    © National Instruments 4793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4794 ordinal=4794 -->
## Functions

Functions


          been passed through the filter. The final filter state array is then passed to the array indicator,
             Final Filter State.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       Final Filter State —

             Final Filter State contains the final, internal filter states, which can be passed as the Initial Filter
            State to the next call to the IIR Cascade Filter with I.C. to filter samples continuously.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        IIRIIR FilterFilter

        Filters the input sequence X using the direct form IIR filter specified by Reverse
       Coefficients and Forward Coefficients. Wire data to the X input to determine the
      polymorphic instance to use or manually select the instance.


            •  IIR Filter (DBL) VI
            •  IIR Filter (CDB) VI

      The IIR Filter VI obtains the elements of Filtered X using the following equation.


                                                         ,

      where Yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
       Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.


4794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4795 ordinal=4795 -->
## Functions

Functions

      Note You can use the IIR Filter VI to implement the FIR filtering operation by
        leaving Reverse Coefficients unwired and by wiring the FIR filter coefficients
        to Forward Coefficients.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\Zero Phase
   Filtering.vi
IIRIIR FilterFilter (DBL)(DBL) VIVI

Filters the input sequence X using the direct form IIR filter specified by Reverse
Coefficients and Forward Coefficients. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       init/cont (init:F) —

     init/cont controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
     init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
    to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
     this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

   •     X —

    X is the input array of samples to filter.

   •      Reverse Coefficients —


                                                    © National Instruments 4795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4796 ordinal=4796 -->
## Functions

Functions


           Reverse Coefficients is the reverse coefficients of the filter design.

             This VI does not place any restrictions on the coefficient arrays. If both coefficient arrays are
           empty, the VI performs no filtering and sets Filtered X to the value of X.

               •      Forward Coefficients —

           Forward Coefficients is the forward coefficients of the filter design.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The IIR Filter VI obtains the elements of Filtered X using the following equation.


                                                         ,

      where Yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
       Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.

           Note You can use the IIR Filter VI to implement the FIR filtering operation by
               leaving Reverse Coefficients unwired and by wiring the FIR filter coefficients
               to Forward Coefficients.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Zero Phase
        Filtering.vi


4796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4797 ordinal=4797 -->
## Functions

Functions

IIRIIR FilterFilter (CDB)(CDB) VIVI

Filters the input sequence X using the direct form IIR filter specified by Reverse
Coefficients and Forward Coefficients. Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       init/cont (init:F) —

     init/cont controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
     init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
    to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
     this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

   •     X —

    X is the input array of samples to filter.

   •      Reverse Coefficients —

    Reverse Coefficients is the reverse coefficients of the filter design.

    This VI does not place any restrictions on the coefficient arrays. If both coefficient arrays are
    empty, the VI performs no filtering and sets Filtered X to the value of X.

   •      Forward Coefficients —

    Forward Coefficients is the forward coefficients of the filter design.

   •       Filtered X —

     Filtered X is the output array of filtered samples.

   •       error —


                                                    © National Instruments 4797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4798 ordinal=4798 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The IIR Filter VI obtains the elements of Filtered X using the following equation.


                                                         ,

      where Yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
       Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.

           Note You can use the IIR Filter VI to implement the FIR filtering operation by
               leaving Reverse Coefficients unwired and by wiring the FIR filter coefficients
               to Forward Coefficients.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Filters\Zero Phase
        Filtering.vi

        IIRIIR FilterFilter withwith I.C.I.C.

        Filters the input sequence X using the direct form IIR filter specified by Reverse
       Coefficients and Forward Coefficients. You can use this VI to process blocks of
       continuous data. This VI is similar to the IIR Filter VI except that you specify the initial
       conditions for this VI. Wire data to the X input to determine the polymorphic instance
       to use or manually select the instance.


            •  IIR Filter with I.C. (DBL) VI
            •  IIR Filter with I.C. (CDB) VI

4798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4799 ordinal=4799 -->
## Functions

Functions

The IIR Filter with I.C. VI obtains the elements of Filtered X using the following
equation.


where yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.

The filter initialization uses the following equations.

yi = yic[Na + i– 1]  for i< 0 xi = xic[Nb + i– 1]  for i< 0,

where yic is the array of Initial Y Conditions and xic is the array of Initial X Conditions.

      Note You can use the IIR Filter with I.C. VI to implement the FIR filtering
        operation by leaving Reverse Coefficients unwired and by wiring the FIR
           filter coefficients to Forward Coefficients.
IIRIIR FilterFilter withwith I.C.I.C. (DBL)(DBL) VIVI

Filters the input sequence X using the direct form IIR filter specified by Reverse
Coefficients and Forward Coefficients. You can use this VI to process blocks of
continuous data. This VI is similar to the IIR Filter VI except that you specify the initial
conditions for this VI. Wire data to the X input to determine the polymorphic instance
to use or manually select the instance.


Inputs/Outputs

   •     X —


                                                    © National Instruments 4799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4800 ordinal=4800 -->
## Functions

Functions


          X is the input array of samples to filter.

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

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       Final X Conditions —

             Final X Conditions contains the most recent inputs. You can use Final X Conditions as Initial X
            Conditions on the next call to this VI.

               •       Final Y Conditions —

             Final Y Conditions contains the most recent outputs. You can use Final Y Conditions as Initial Y


4800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4801 ordinal=4801 -->
## Functions

Functions


    Conditions on the next call to this VI.


The IIR Filter with I.C. VI obtains the elements of Filtered X using the following
equation.


where yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.

The filter initialization uses the following equations.

yi = yic[Na + i– 1]  for i< 0 xi = xic[Nb + i– 1]  for i< 0,

where yic is the array of Initial Y Conditions and xic is the array of Initial X Conditions.

      Note You can use the IIR Filter with I.C. VI to implement the FIR filtering
        operation by leaving Reverse Coefficients unwired and by wiring the FIR
           filter coefficients to Forward Coefficients.
IIRIIR FilterFilter withwith I.C.I.C. (CDB)(CDB) VIVI

Filters the input sequence X using the direct form IIR filter specified by Reverse
Coefficients and Forward Coefficients. You can use this VI to process blocks of
continuous data. This VI is similar to the IIR Filter VI except that you specify the initial
conditions for this VI. Wire data to the X input to determine the polymorphic instance
to use or manually select the instance.


                                                    © National Instruments 4801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4802 ordinal=4802 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is the input array of samples to filter.

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

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       Final X Conditions —

             Final X Conditions contains the most recent inputs. You can use Final X Conditions as Initial X
            Conditions on the next call to this VI.

               •       Final Y Conditions —

4802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4803 ordinal=4803 -->
## Functions

Functions


     Final Y Conditions contains the most recent outputs. You can use Final Y Conditions as Initial Y
    Conditions on the next call to this VI.


The IIR Filter with I.C. VI obtains the elements of Filtered X using the following
equation.


where yis Filtered X, Nb is the number of Forward Coefficients, bj is Forward
Coefficients, Na is the number of Reverse Coefficients, and ak is Reverse Coefficients.

The filter initialization uses the following equations.

yi = yic[Na + i– 1]  for i< 0 xi = xic[Nb + i– 1]  for i< 0,

where yic is the array of Initial Y Conditions and xic is the array of Initial X Conditions.

      Note You can use the IIR Filter with I.C. VI to implement the FIR filtering
        operation by leaving Reverse Coefficients unwired and by wiring the FIR
           filter coefficients to Forward Coefficients.

CascadeCascade ToTo DirectDirect CoefficientsCoefficients

Converts IIR filter coefficients from the cascade form to the direct form.


Inputs/Outputs

   •       IIR Filter Cluster —

     IIR Filter Cluster contains the cascaded form of IIR filter coefficients.


                                                    © National Instruments 4803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4804 ordinal=4804 -->
## Functions

Functions


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


               •      Reverse Coefficients —

           Reverse Coefficients contains the direct-form, reverse coefficients.

               •      Forward Coefficients —

           Forward Coefficients contains the direct-form, forward coefficients.


      As an example, you can convert a cascade filter, composed of two second-order stages,
       to a direct-form filter as follows.

       Reverse Coefficients

        {a11, a12, a21, a22} → {1.0, a1, a2, a3, a4}

      Forward Coefficients

        {b01, b11, b02, b12, b22} → {b0, b1, b2, b3, b4}

       Refer to the IIR Cascade Filter VI for more information about cascade-form filtering and


4804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4805 ordinal=4805 -->
## Functions

Functions

the IIR Filter VI for more information about direct-form filtering.

AdvancedAdvanced FIRFIR FilteringFiltering

Use the Advanced FIR Filtering VIs to implement advanced FIR filters.

      Note The Convolution VI is available on both the Advanced FIR Filtering
        palette and the Signal Operation palette because you can use the VI for both
         filtering and signal manipulation.

The VIs on this palette can return signal processing error codes.


 Palette              Description Object

 FIR
 Windowed   Generates the set of filter coefficients you need to implement an FIR windowed filter.
 Coefficients

 Parks-       Generates a set of linear-phase FIR multiband digital filter coefficients using the # of
 McClellan    taps, sampling frequency: fs, Band Parameters, and filter type.


 Savitzky-              Designs a Savitzky-Golay FIR smoothing filter. This VI returns the designed Savitzky-
 Golay Filter
             Golay filter coefficients and the differentiation filter coefficients.
 Coefficients

 FIR
             Generates a set of filter coefficients to implement a digital interpolated FIR (IFIR)
 Narrowband
                    filter.
 Coefficients


            Computes the convolution of the input sequences X and Y. Wire data to the X and Y
 Convolution
              inputs to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4806 ordinal=4806 -->
## Functions

Functions


         Palette                      Description
        Object

                           Filters the input sequence X using the direct-form FIR filter specified by FIR
         FIR Filter     Coefficients. Wire data to the X input to determine the polymorphic instance to use
                      or manually select the instance.


                           Filters the input sequence X using the direct-form FIR filter specified by FIR
         FIR Filter     Coefficients. You can use this VI to process blocks of continuous data. Wire data to
        with I.C.      the X input to determine the polymorphic instance to use or manually select the
                        instance.


         FIR
                           Filters the input sequence X using the interpolated FIR (IFIR) filter specified by IFIR       Narrowband                        Coefficients.
           Filter

       FIRFIR WindowedWindowed CoefficientsCoefficients

       Generates the set of filter coefficients you need to implement an FIR windowed filter.


      Inputs/Outputs

               •     window parameter —

          window parameter is the beta parameter for a Kaiser window, the standard deviation for a
            Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the


4806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4807 ordinal=4807 -->
## Functions

Functions


  standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•        filter type —

   filter type specifies the passband of the filter.

           Lowpass
  0              (default)
  1         Highpass
  2        Bandpass
  3        Bandstop

•      sampling freq: fs —

  sampling freq: fs is the sampling frequency in Hz and must be greater than zero. The default is
  1.0 Hz.

   If it is less than or equal to zero, the VI sets FIR Windowed Coefficients to an empty array and
  returns an error.

•      taps —

  taps determines the total number of FIR coefficients and must be greater than zero. The default
   is 25.

   If taps is less than or equal to 0, the VI sets FIR Windowed Coefficients to an empty array and
  returns an error. taps must be odd for highpass and bandstop filters.

•     window —

  window specifies the type of smoothing window.

  Smoothing windows decrease ripple in the filter passband and improve the ability of the filter to
  attenuate frequency components in the filter stopband.


                                                   © National Instruments 4807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4808 ordinal=4808 -->
## Functions

Functions


           0         Rectangle (default)
           1        Hanning
           2       Hamming
           3         Blackman-Harris
           4         Exact Blackman
           5        Blackman
           6           Flat Top
           7        4 Term B-Harris
           8        7 Term B-Harris
           9       Low Sidelobe
           11       Blackman Nuttall
           30         Triangle
           31        Bartlett-Hanning
           32      Bohman
           33        Parzen
           34       Welch
           60        Kaiser
           61       Dolph-Chebyshev
           62        Gaussian

               •      option —

            option specifies whether to scale the FIR Windowed Coefficients. The default is 0.

           0 not scaled—Does not scale the FIR Windowed Coefficients.
           1 scaled—Scales the FIR Windowed Coefficients.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must be greater than zero and observe
            the Nyquist criterion. The default is 0.125 Hz.

                    If low cutoff freq : fl is less than or equal to zero or does not meet the Nyquist criterion, the VI
             sets FIR Windowed Coefficients to an empty array and returns an error.

               •      FIR Windowed Coefficients —

            FIR Windowed Coefficients returns the filter coefficients.

               •       error —


4808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4809 ordinal=4809 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship.

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs. If
any of these conditions are not met, the VI sets FIR Windowed Coefficients to an
empty array and returns an error.

Parks-McClellanParks-McClellan

Generates a set of linear-phase FIR multiband digital filter coefficients using the # of
taps, sampling frequency: fs, Band Parameters, and filter type.


Inputs/Outputs

   •      # of taps —

    # of taps contains the total number of coefficients in h. The default is 32.

    A tap corresponds to a multiplication and an addition. If there are ntaps, every filtered sample
    requires nmultiplications and nadditions. # of taps must be greater than 2. If # of taps is less
    than or equal to 2, the VI sets h to an empty array, sets ripple to NaN, and returns an error.

   •      sampling freq: fs —

    sampling freq: fs is the sampling frequency in Hz and must be greater than zero. The default is
     1.0 Hz.

       If sampling freq: fs is less than or equal to zero, the VI sets h to an empty array and returns an


                                                    © National Instruments 4809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4810 ordinal=4810 -->
## Functions

Functions


               error.

               •     Band Parameters —

          Band Parameters is an array of clusters. Each cluster element contains the necessary
            information associated with each band for the FIR design. The Band Parameters cluster array
          must contain at least one element, that is, one band. The default is an empty array.

                    If Band Parameters does not contain any elements, the VI sets h to an empty array, sets ripple to
           NaN, and returns an error.

                     •      Amplitude —

               Amplitude is the appropriate magnitude response, or gain, of the filter between Lower Freq
              and Higher Freq. A value of 1.0 corresponds to a passband, and a value of 0.0 corresponds
                 to a stopband. If you set filter type to Differentiator, the Amplitude of a band is the slope of
                the frequency response in that band.

                     •     Lower Freq —

              Lower Freq is the frequency at which the band begins.

                     •      Higher Freq —

               Higher Freq is the frequency at which the band ends.

                     •      Weighted Ripple —

               Weighted Ripple is the weighted ripple error that this VI minimizes. The higher the weight,
                the smaller the error in the band.

                For each band, Higher Freq must be greater than Lower Freq, as shown by the following
                  relationship. fhi > fli for i= 0, 1, 2, …, m–1

              where fhi is the Higher Freq in the ith band, fli is the Lower Freq in the ith band, and mis
                the number of bands.

                For adjacent bands, the Lower Freq in the higher band must be greater than the Higher
               Freq in the adjacent lower band, as shown by the following relationship. fli > fhi– 1 for i= 1,
                    2, …, m–1


4810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4811 ordinal=4811 -->
## Functions

Functions


      where fli is the Lower Freq in the higher of the adjacent bands, fhi– 1 is the Higher Freq in
      the lower of the adjacent bands, and mis the number of bands.

     The Higher Freq in the last band must be equal to or less than half of sampling freq: fs.

          If any of the preceding frequency conditions are violated, the VI sets h to an empty array,
       sets ripple to NaN, and returns an error.


•        filter type —

   filter type can be the following values.

   Multiband (default)—Specifies a multiband filter. If # of taps is an odd number, this VI does not
  0 place restrictions on the value of the Amplitude. If # of taps is an even number, the Amplitude
    of the last band at half of sampling freq: fs must be 0.
    Differentiator—Specifies a differentiator. If # of taps is an even number, this VI does not place
    restrictions on the last band. If # of taps is an odd number, the value of Higher Freq in the last  1   band must be less than half of sampling freq: fs. For example, a typical normalized band {0,
    0.49} leaves a 0.01 transitional band at half of the sampling frequency, 0.5.
    Hilbert—Specifies a Hilbert transformer. The value of Lower Freq in the first band must be
    greater than 0. A typical normalized Lower Freq in the first band is 0.03. If # of taps is an even
  2 number, this VI does not place restrictions on the last band. If # of taps is an odd number, the
   value of Higher Freq in the last band must be less than half of sampling freq: fs. A typical
   normalized Higher Freq in the last band is 0.49.

•     h —

  h is an array of FIR filter coefficients, which the VI computes using the Parks-McClellan algorithm
  with the Remes exchange technique.

•       ripple —

  ripple is the optimal ripple the VI computes and is a measure of deviation from the ideal filter
  specifications.

•       error —

  error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
  Code VI to convert the error code or warning into an error cluster.


                                                   © National Instruments 4811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4812 ordinal=4812 -->
## Functions

Functions

           Note The Parks-McClellan VI finds the coefficients using iterative techniques
             based upon an error criterion. Although you specify valid filter parameters,
              the algorithm may fail to converge.

      The Parks-McClellan VI generates only the filter coefficients. It does not perform the
        filtering function. To filter a sequence X using the set of FIR filter coefficients h, use the
       Convolution VI with X and h as the input sequences, as shown in the following
        illustration.


      The equi-ripple filters use a similar technique to filter the data.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Optimal FIR
        Filter.vi

       Savitzky-GolaySavitzky-Golay FilterFilter CoefficientsCoefficients

       Designs a Savitzky-Golay FIR smoothing filter. This VI returns the designed Savitzky-
      Golay filter coefficients and the differentiation filter coefficients.


      Inputs/Outputs

               •     compute differentiation filters? —


4812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4813 ordinal=4813 -->
## Functions

Functions


    compute differentiation filters? specifies whether the VI calculates the Differentiation Filters.

    The default is TRUE.

   •       side points —

    side points specifies the number of data points to each side of the current data point to use for
    the least squares minimization. side points*2 + 1 is the length of the moving window, which
    must be greater than the polynomial order.

   •      polynomial order —

    polynomial order specifies the order of the polynomial.

   •      Weight —

    Weight specifies a weighting vector to use in the least squares minimization. This array must be
    empty or have a length of side points*2+1.

   •      Savitzky-Golay Filters —

    Savitzky-Golay Filters is an n-by-nmatrix with rows representing the FIR filter coefficients
    where nis side points*2+1.

   •       Differentiation Filters —

     Differentiation Filters is an m-by-nmatrix where the p-th row is the differentiation filter for the
    p-th order derivative, where mis polynomial order+1, and nis side points*2+1.

    This VI computes Differentiation Filters only if compute differentiation filters? is TRUE.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Savitzky-Golay filter smoothes a noisy signal by the piece-by-piece fitting of a
polynomial function to the signal. This VI performs the fitting by least squares
minimization. The following equation shows the length of the moving polynomial
fitting window.


                                                    © National Instruments 4813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4814 ordinal=4814 -->
## Functions

Functions

       2k+1, where kis side points,

       including the current point and kpoints on each side of the current point.

      The central row of Savitzky-Golay Filters estimates the middle point of the moving
      window. The other rows of Savitzky-Golay Filters smooth the endpoints of the signal,
      where the window length exceeds the number of remaining data points.

      To smooth a signal, apply the first krows of Savitzky-Golay Filters to the first 2k+1
       points of the signal to get the first ksmoothed points. Apply the last krows of
       Savitzky-Golay Filters to the last 2k+1 points of the signal to get the last ksmoothed
       points. Apply the central row of Savitzky-Golay Filters for all other points.

      The following block diagram illustrates how to apply the designed Savitzky-Golay filter
       to a signal.


      The VI also generates the differentiation filters if compute differentiation filters? is
      TRUE. The p-th row of Differentiation Filters is the differentiation filter of the p-th
       order derivative. Given a signal of length 2k+1, you can find an estimate of the p-th
       order derivative of its middle point using the following block diagram.


4814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4815 ordinal=4815 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Filters\Design and
   Apply Savitzky-Golay Filter.vi

FIRFIR NarrowbandNarrowband CoefficientsCoefficients

Generates a set of filter coefficients to implement a digital interpolated FIR (IFIR) filter.


Inputs/Outputs

   •       ripple: rp —

     ripple: rp is the ripple in the passband of the filter. The default is 0.01.

   •      sampling freq: fs —

    sampling freq: fs is the sampling frequency and must be greater than zero. The default is 1.0.

       If sampling freq: fs is less than or equal to zero, the VI sets IFIR Coefficients to an empty cluster
    and returns an error.

   •      passband: fpass —


                                                    © National Instruments 4815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4816 ordinal=4816 -->
## Functions

Functions


           passband: fpass is the passband bandwidth. The default is 0.01.

               •      stopband: fstop —

           stopband: fstop is the stopband bandwidth. The default is 0.02.

               •      center freq: fc —

            center freq: fc is the center frequency of the filter. The default is 0.1.

               •      attenuation (db): Ar —

            attenuation (db): Ar is the attenuation in the stopband of the filter. The default is 60 decibels.

               •        filter type —

                filter type specifies the passband of the filter.

                    Lowpass
           0                          (default)
           1         Highpass
           2        Bandpass
           3        Bandstop

               •       IFIR Coefficients —

             IFIR Coefficients is a cluster that contains IFIR filter coefficients.

                     •        filter type —

                     filter type is the filter type that you use to determine how to filter the data.

               0 Lowpass
               1 Highpass
               2 Bandpass
               3 Bandstop
               4 Wideband-Lowpass—For cutoff frequencies near Nyquist
               5 Wideband-Highpass—For cutoff frequencies near zero

                     •       interpolation —


4816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4817 ordinal=4817 -->
## Functions

Functions


         interpolation is the interpolation factor M. The model filter is stretched by interpolation
         times.

         •     Model Filter —

       Model Filter contains the coefficients of the model filter.

         •     Image Suppressor —

       Image Suppressor contains the coefficients of the filter image suppressor.


   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The inputs to this VI cannot have negative values, and they cannot violate the
Sampling Theorem.

The overall filter is a linear-phase FIR filter. This VI calculates the delay for the filter
using the following equation:


where NG is the number of elements in the array Model Filter, NI is the number of
elements in the array Image Suppressor, and Mis the value of interpolation.

You can design narrowband FIR filters using the FIR Narrowband Coefficients VI, and
then implement the filtering using the FIR Narrowband Filter VI. The design and
implementation are separate operations, because many narrowband filters require
long design times, whereas the actual filtering is very fast and efficient. Keep this in
mind when creating your narrowband filtering diagrams.

Related Information

FIR Narrowband Filter VI


                                                    © National Instruments 4817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4818 ordinal=4818 -->
## Functions

Functions

      ConvolutionConvolution

      Computes the convolution of the input sequences X and Y. Wire data to the X and Y
       inputs to determine the polymorphic instance to use or manually select the instance.


            • 1D Convolution (DBL) VI
            • 1D Convolution (CDB) VI
            • 2D Convolution (DBL) VI
            • 2D Convolution (CDB) VI

     1D Convolution

      The linear convolution of the signals x(t) and y(t) is defined as:


      where the symbol * denotes linear convolution.

     When algorithm is direct, this VI uses the following equation to perform the discrete
      implementation of the linear convolution and obtain the elements of X * Y.


        for i= 0, 1, 2, … , M+N–2

      where his X * Y

   Nis the number of elements in X, Mis the number of elements in Y, the indexed
      elements outside the ranges of X and Y are equal to zero, as shown in the following
        relationships:

      xj = 0, j< 0, or j≥ N


4818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4819 ordinal=4819 -->
## Functions

Functions

and

yj = 0, j< 0, or j≥ M.

When algorithm is frequency domain, this VI completes the following steps, in
order, to compute the linear convolution:

   •  First, this VI pads the end of X and Y with zeros to make their lengths M+ N– 1, as
   shown in the following equations.


   • Second, this VI calculates the Fourier transform of X' and Y' according to the
    following equations.

X'(f) = FFT(x') Y'(f) = FFT(y')

   • Third, this VI multiplies X'(f) by Y'(f) and calculates the inverse Fourier transform of
    the product. The result is the linear convolution of X and Y, as shown in the
    following equation.

X * Y = IFFT(X'(f) · Y'(f))

Thus, this VI computes the linear convolution, not the circular convolution. However,
because x(t) * y(t)N ⇔ X(f)Y(f) is a Fourier transform pair, where x(t) * y(t)N is the
circular convolution of x(t) and y(t), you can create a circular version of the
convolution. To compute the circular convolution, you can use a block diagram similar
to the block diagram shown in the following illustration.


                                                    © National Instruments 4819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4820 ordinal=4820 -->
## Functions

Functions


     2D Convolution

     When algorithm is direct, this VI uses the following equation to compute the two-
      dimensional convolution of the input matrices X and Y.


        for i= 0, 1, 2, … , M1+M2–2 and j= 0, 1, 2, … , N1+N2–2

      where his X * Y,

     M1 is the number of rows of matrix X, N1 is the number of columns of matrix X, M2 is
       the number of rows of matrix Y, N2 is the number of columns of matrix Y, The indexed
      elements outside the ranges of X and Y are equal to zero, as shown in the following
        relationships:

      x(m,n), m< 0 or m≥ M1 or n< 0 or n≥ N1

      and

      y(m,n) , m< 0 or m≥ M2 or n< 0 or n≥ N2.

     When algorithm is frequency domain, this VI completes the following steps, in
       order, to compute the two-dimensional convolution:

            •  First, this VI pads the end of X and Y with zeros to make their sizes (M1 + M2 – 1)-by-
          (N1 + N2 – 2), as shown in the following equations.


4820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4821 ordinal=4821 -->
## Functions

Functions


  • Second, this VI calculates the Fourier transform of X' and Y' according to the
    following equations.

X'(f) = FFT(x') Y'(f) = FFT(y')

  • Third, this VI multiplies X'(f) by Y'(f) and calculates the inverse Fourier transform of
   the product. The result is the two-dimensional convolution of X and Y, as shown in
   the following equation.

X * Y = IFFT(X'(f) · Y'(f))

The output size determines the size of the output matrix X * Y as shown in the
following illustration.


 1.  full

   The output matrix X * Y is (M1+M2–1)-by-(N1+N2–1).

 2. size X

    This is useful in image processing. If Xis the image you want to filter, Yis a small


                                                    © National Instruments 4821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4822 ordinal=4822 -->
## Functions

Functions

          matrix called the convolution kernel. X * Y is the filtered image whose size is the
        same as that of image X. The output M1-by-N1 matrix is the central part of the
          output matrix when the output size is full.

         3. compact

         Computing the edge elements of X * Y requires zero-padding if the output size is
             full or size X. LabVIEW removes these edge elements if the output size is compact.
         The output (M1–M2+1)-by-(N1–N2+1) matrix is the central part of the output
          matrix when the output size is size X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Signal Operation\Edge
        Detection with 2D Convolution.vi

       FIRFIR FilterFilter

        Filters the input sequence X using the direct-form FIR filter specified by FIR
       Coefficients. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


            • FIR Filter (DBL) VI
            • FIR Filter (CDB) VI

      The FIR Filter VI obtains the elements of Filtered X using the following equation.


      where yis Filtered X, Nb is the number of FIR Coefficients, and bj is FIR Coefficients.


4822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4823 ordinal=4823 -->
## Functions

Functions

FIRFIR FilterFilter (DBL)(DBL) VIVI

Filters the input sequence X using the direct-form FIR filter specified by FIR
Coefficients. Wire data to the X input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •       init/cont (init:F) —

     init/cont controls the initialization of the internal states. The default is FALSE.

    The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
     init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
    to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
     this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

   •     X —

    X is the input array of samples to filter.

   •      FIR Coefficients —

    FIR Coefficients is the coefficients of the FIR filter. If FIR Coefficients is unwired, the VI sets
     Filtered X to the value of X and does not perform filtering.

   •       Filtered X —

     Filtered X is the output array of filtered samples.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The FIR Filter VI obtains the elements of Filtered X using the following equation.


                                                    © National Instruments 4823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4824 ordinal=4824 -->
## Functions

Functions


      where yis Filtered X, Nb is the number of FIR Coefficients, and bj is FIR Coefficients.
    FIRFIR FilterFilter (CDB)(CDB) VIVI

        Filters the input sequence X using the direct-form FIR filter specified by FIR
       Coefficients. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •       init/cont (init:F) —

             init/cont controls the initialization of the internal states. The default is FALSE.

          The first time this VI runs or if init/cont is FALSE, LabVIEW initializes the internal states to 0. If
             init/cont is TRUE, LabVIEW initializes the internal states to the final states from the previous call
             to this instance of this VI. To process a large data sequence that consists of smaller blocks, set
              this input to FALSE for the first block and to TRUE for continuous filtering of all remaining blocks.

               •     X —

          X is the input array of samples to filter.

               •      FIR Coefficients —

            FIR Coefficients is the coefficients of the FIR filter. If FIR Coefficients is unwired, the VI sets
             Filtered X to the value of X and does not perform filtering.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —


4824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4825 ordinal=4825 -->
## Functions

Functions


     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The FIR Filter VI obtains the elements of Filtered X using the following equation.


where yis Filtered X, Nb is the number of FIR Coefficients, and bj is FIR Coefficients.

FIRFIR FilterFilter withwith I.C.I.C.

Filters the input sequence X using the direct-form FIR filter specified by FIR
Coefficients. You can use this VI to process blocks of continuous data. Wire data to the
X input to determine the polymorphic instance to use or manually select the instance.


   • FIR Filter with I.C. (DBL) VI
   • FIR Filter with I.C. (CDB) VI

The FIR Filter with I.C. VI obtains the elements of Filtered X using the following
equation.

              for (i≥0)

where yis Filtered X, Nb is the number of FIR Coefficients, and bj is FIR Coefficients.

The filter initialization uses the following equation.

xi = xic[Nb + i– 1] for i< 0

where xic is the array of Initial X Conditions.


                                                    © National Instruments 4825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4826 ordinal=4826 -->
## Functions

Functions

    FIRFIR FilterFilter withwith I.C.I.C. (DBL)(DBL) VIVI

        Filters the input sequence X using the direct-form FIR filter specified by FIR
       Coefficients. You can use this VI to process blocks of continuous data. Wire data to the
      X input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the input array of samples to filter.

               •      FIR Coefficients —

            FIR Coefficients is the coefficients of the FIR filter. If FIR Coefficients is unwired, the VI sets
             Filtered X to the value of X and does not perform filtering.

               •        Initial X Conditions —

               Initial X Conditions contains the most recent inputs.

          The most recent prior input should be the last element in the array. The number of elements in
              this array should be one less than the number of elements in the FIR Coefficients array.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       Final X Conditions —

             Final X Conditions contains the most recent inputs. You can use Final X Conditions as Initial X
            Conditions on the next call to this VI.


4826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4827 ordinal=4827 -->
## Functions

Functions

The FIR Filter with I.C. VI obtains the elements of Filtered X using the following
equation.

              for (i≥0)

where yis Filtered X, Nb is the number of FIR Coefficients, and bj is FIR Coefficients.

The filter initialization uses the following equation.

xi = xic[Nb + i– 1] for i< 0

where xic is the array of Initial X Conditions.
FIRFIR FilterFilter withwith I.C.I.C. (CDB)(CDB) VIVI

Filters the input sequence X using the direct-form FIR filter specified by FIR
Coefficients. You can use this VI to process blocks of continuous data. Wire data to the
X input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the input array of samples to filter.

   •      FIR Coefficients —

    FIR Coefficients is the coefficients of the FIR filter. If FIR Coefficients is unwired, the VI sets
     Filtered X to the value of X and does not perform filtering.

   •        Initial X Conditions —

     Initial X Conditions contains the most recent inputs.


                                                    © National Instruments 4827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4828 ordinal=4828 -->
## Functions

Functions


          The most recent prior input should be the last element in the array. The number of elements in
              this array should be one less than the number of elements in the FIR Coefficients array.

               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       Final X Conditions —

             Final X Conditions contains the most recent inputs. You can use Final X Conditions as Initial X
            Conditions on the next call to this VI.


      The FIR Filter with I.C. VI obtains the elements of Filtered X using the following
       equation.

                      for (i≥0)

      where yis Filtered X, Nb is the number of FIR Coefficients, and bj is FIR Coefficients.

      The filter initialization uses the following equation.

      xi = xic[Nb + i– 1] for i< 0

      where xic is the array of Initial X Conditions.

       FIRFIR NarrowbandNarrowband FilterFilter

        Filters the input sequence X using the interpolated FIR (IFIR) filter specified by IFIR
       Coefficients.


4828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4829 ordinal=4829 -->
## Functions

Functions

  • FIR Narrowband Filter (DBL) VI
  • FIR Narrowband Filter (CDB) VI

The overall filter is a linear-phase FIR filter. This VI calculates the delay for the filter
using the following equation:


where NG is the number of elements in the array Model Filter, NI is the number of
elements in the array Image Suppressor, and Mis the value of interpolation.

You can design narrowband FIR filters using the FIR Narrowband Coefficients VI, and
then implement the filtering using the FIR Narrowband Filter VI. The design and
implementation are separate operations, because many narrowband filters require
long design times, whereas the actual filtering is very fast and efficient. Keep this in
mind when creating your narrowband filtering diagrams.
FIRFIR NarrowbandNarrowband FilterFilter (DBL)(DBL) VIVI

Filters the input sequence X using the interpolated FIR (IFIR) filter specified by IFIR
Coefficients.


Inputs/Outputs

   •     X —

    X is the input signal to filter.

   •       IFIR Coefficients —

     IFIR Coefficients is a cluster that contains IFIR filter coefficients.

    You can use the FIR Narrowband Coefficients VI to generate the IFIR Coefficients to use.


                                                    © National Instruments 4829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4830 ordinal=4830 -->
## Functions

Functions


                     •        filter type —

                     filter type is the filter type that you use to determine how to filter the data.

               0  Lowpass
               1  Highpass
               2  Bandpass
               3  Bandstop
                 Wideband-Lowpass               4                       (cutoff frequencies near Nyquist)
                  Wideband-Highpass               5                       (cutoff frequencies near zero)

                     •       interpolation —

                 interpolation is the interpolation factor M. The model filter is stretched by interpolation
                 times.

                     •     Model Filter —

              Model Filter contains the coefficients of the model filter.

                     •     Image Suppressor —

              Image Suppressor contains the coefficients of the filter image suppressor.


               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The overall filter is a linear-phase FIR filter. This VI calculates the delay for the filter
       using the following equation:


4830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4831 ordinal=4831 -->
## Functions

Functions

where NG is the number of elements in the array Model Filter, NI is the number of
elements in the array Image Suppressor, and Mis the value of interpolation.

You can design narrowband FIR filters using the FIR Narrowband Coefficients VI, and
then implement the filtering using the FIR Narrowband Filter VI. The design and
implementation are separate operations, because many narrowband filters require
long design times, whereas the actual filtering is very fast and efficient. Keep this in
mind when creating your narrowband filtering diagrams.
FIRFIR NarrowbandNarrowband FilterFilter (CDB)(CDB) VIVI

Filters the input sequence X using the interpolated FIR (IFIR) filter specified by IFIR
Coefficients.


Inputs/Outputs

   •     X —

    X is the input signal to filter.

   •       IFIR Coefficients —

     IFIR Coefficients is a cluster that contains IFIR filter coefficients.

    You can use the FIR Narrowband Coefficients VI to generate the IFIR Coefficients to use.

         •        filter type —

           filter type is the filter type that you use to determine how to filter the data.

        0  Lowpass
        1  Highpass
        2  Bandpass
        3  Bandstop


                                                    © National Instruments 4831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4832 ordinal=4832 -->
## Functions

Functions


                 Wideband-Lowpass               4
                       (cutoff frequencies near Nyquist)
                  Wideband-Highpass               5                       (cutoff frequencies near zero)

                     •       interpolation —

                 interpolation is the interpolation factor M. The model filter is stretched by interpolation
                 times.

                     •     Model Filter —

              Model Filter contains the coefficients of the model filter.

                     •     Image Suppressor —

              Image Suppressor contains the coefficients of the filter image suppressor.


               •       Filtered X —

             Filtered X is the output array of filtered samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The overall filter is a linear-phase FIR filter. This VI calculates the delay for the filter
       using the following equation:


      where NG is the number of elements in the array Model Filter, NI is the number of
      elements in the array Image Suppressor, and Mis the value of interpolation.

      You can design narrowband FIR filters using the FIR Narrowband Coefficients VI, and
      then implement the filtering using the FIR Narrowband Filter VI. The design and
      implementation are separate operations, because many narrowband filters require

4832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4833 ordinal=4833 -->
## Functions

Functions

long design times, whereas the actual filtering is very fast and efficient. Keep this in
mind when creating your narrowband filtering diagrams.

SpectralSpectral AnalysisAnalysis

Use the Spectral Analysis VIs to perform array-based analysis on a spectrum.

The VIs on this palette can return signal processing error codes.


 Palette Object   Description

 Auto Power     Computes the single-sided, scaled, auto power spectrum of a time-domain
 Spectrum         signal.


               Computes the Power Spectrum, Sxx, of the input sequence X. Wire data to the X
 Power                  input to determine the polymorphic instance to use or manually select the Spectrum                   instance.


 Cross Power    Computes the single-sided, scaled, cross power spectrum of two real-time
 Spectrum         signals.

 Unevenly
 Sampled Signal  Calculates the power spectrum of a signal that is unevenly spaced in time.
 Spectrum

 Amplitude and
               Computes the single-sided, scaled amplitude spectrum of a real-valued time-
 Phase
               domain signal and returns the amplitude spectrum as magnitude and phase.
 Spectrum


 Spectrum Unit   Converts either the power, amplitude, or gain (amplitude ratio) spectrum to
 Conversion       alternate formats including Log (decibel and dbm) and spectral density.


                                                    © National Instruments 4833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4834 ordinal=4834 -->
## Functions

Functions


         Palette Object   Description

        STFT          Computes the signal energy distribution in the joint time-frequency domain,
        Spectrograms    using the short-time Fourier transform (STFT) algorithm.


      WVD          Computes the energy distribution of the input signal in the joint time-frequency
        Spectrogram    domain using the Wigner-Ville distribution (WVD) algorithm.


                     Computes the cross power spectrum, Sxy, of the input signals X and Y. Wire data
         Cross Power     to the X input to determine the polymorphic instance to use or manually select
                         the instance.


       Power &amp;                     Computes the estimated power and frequency around the peak frequency in the        Frequency
                     power spectrum of a time-domain signal.         Estimate

       Buneman                         Estimates the frequency of a given sine wave of unknown frequency using the        Frequency                    Buneman formula.
         Estimator

     AutoAuto PowerPower SpectrumSpectrum

      Computes the single-sided, scaled, auto power spectrum of a time-domain signal.


      Inputs/Outputs

               •      Signal (V) —

            Signal specifies the input time-domain signal, usually in volts.

          The time-domain record must contain at least three cycles of the signal for a valid estimate.

               •      dt —


4834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4835 ordinal=4835 -->
## Functions

Functions


    dt is the sample period of the time-domain signal, usually in seconds.

    Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal. The default is 1.

   •     Power Spectrum (V^2 rms) —

   Power Spectrum returns the single-sided power spectrum.

       If the input Signal is in volts (V), Power Spectrum has units of volts-rms squared (Vrms²). If the
    input Signal is not in volts, Power Spectrum has units of the input signal unit-rms squared.

   •       df —

    df is the frequency interval of the power spectrum in hertz, if dt is in seconds.


This VI computes the power spectrum using the following equation.


where nis the number of points in the Signal and * denotes the complex conjugate.
This VI then converts the power spectrum into a single-sided power spectrum.

Related Information

Output Units for FFT-Based VIs

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

PowerPower SpectrumSpectrum

Computes the Power Spectrum, Sxx, of the input sequence X. Wire data to the X input
to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4836 ordinal=4836 -->
## Functions

Functions


            • Power Spectrum (DBL) VI
            • Power Spectrum (CDB) VI

      The Power Spectrum Sxx(f) of a function x(t) is defined as

       Sxx(f) = X*(f)X(f) = |X(f)|²,

      where X(f) = F{x(t)}, and X* (f) is the complex conjugate of X(f).

      The Power Spectrum VI uses the FFT and DFT routines to compute the power
       spectrum, which is given by


      where Sxx represents the output sequence Power Spectrum, and nis the number of
      samples in the input sequence X.

     When the number of samples, n, in the input sequence X is a valid power of 2

   n= 2m

        for m= 1, 2, 3, …, 23,

       the Power Spectrum VI computes the fast Fourier transform of a real-valued sequence
       using the a fast radix-2 FFT algorithm and efficiently scales the magnitude square. The
        largest Power Spectrum the VI can compute using the FFT is 223 (8,388,608 or 8M).

     When the number of samples in the input sequence X is not a valid power of 2 but is
       factorable as the product of small prime numbers, the Power Spectrum VI computes
       the discrete Fourier transform of a real-valued sequence using an efficient DFT
       algorithm and scales the magnitude square. The largest Power Spectrum the VI can
      compute using the fast DFT is 222 – 1(4,194,303 or 4M – 1).


4836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4837 ordinal=4837 -->
## Functions

Functions

Let Ybe the Fourier transform of the input sequence X and nbe the number of
samples in it. You can show that

|Yn–i|² = |Y–i²|.

You can interpret the power in the (n– 1)th element of Yas the power in the –ith
element of the sequence, which represents the power in the –ith harmonic. You can
find the total power for the ith harmonic (DC and Nyquist component not included)
using

Power in the ith harmonic = 2|Yi|² = |Yi|² + |Yn– 1|² 0 < i< n/2

The total power in the DC and Nyquist components are |Y0|² and |Yn/2|² respectively.

If nis even, let        . The following table shows the format of the output sequence Sxx
corresponding to the Power Spectrum.


 Array Element                               Interpretation
 Sxx0                                 Power in DC component
 Sxx1 = Sxx(n– 1)                       Power at frequency Δf
 Sxx2 = Sxx(n– 2)                       Power at frequency 2Δf
 Sxx3 = Sxx(n– 3)                       Power at frequency 3Δf

 ⋮                                      ⋮

 Sxx(k– 2) = Sxxn– (k– 2)                  Power at frequency (k– 2)Δf
 Sxx(k– 1) = Sxxn– (k– 1)                  Power at frequency (k– 1)Δf
Sxxk                                Power in Nyquist harmonic

The following illustration represents the preceding table information.


                                                    © National Instruments 4837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4838 ordinal=4838 -->
## Functions

Functions


       Notice that the power spectrum is symmetric about the Nyquist frequency as the
       following illustration shows.


           If nis odd, let            . The following table shows the format of the output sequence
     Sxx corresponding to the Power Spectrum.


         Array Element                               Interpretation
       Sxx0                                 Power in DC component
       Sxx1 = Sxx(n– 1)                       Power at frequency Δf
       Sxx2 = Sxx(n– 2)                       Power at frequency 2Δf
       Sxx3 = Sxx(n– 3)                       Power at frequency 3Δf

        ⋮                                      ⋮


4838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4839 ordinal=4839 -->
## Functions

Functions


 Array Element                               Interpretation
 Sxx(k– 2) = Sxxn– (k– 2)                  Power at frequency (k– 2)Δf
 Sxx(k– 1) = Sxxn– (k– 1)                  Power at frequency (k– 1)Δf
Sxxk = Sxxn– k                        Power at frequency kΔf

The following illustration shows that when nis odd, the power spectrum is symmetric
about the Nyquist frequency, but the Nyquist frequency does not fall on a frequency
bin.


The format described in the preceding tables is an accepted standard in digital signal
processing applications.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Spectral Analysis\DC
   Centered Spectrum.vi
  • labview\examples\Signal Processing\Transforms\Generalized
   Fourier Spectrum.vi
  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi


                                                    © National Instruments 4839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4840 ordinal=4840 -->
## Functions

Functions

     PowerPower SpectrumSpectrum (DBL)(DBL) VIVI

      Computes the Power Spectrum, Sxx, of the input sequence X. Wire data to the X input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the input sequence.

               •     Power Spectrum —

          Power Spectrum returns the double-sided power spectrum of X.

                    If the input signal is in volts (V), Power Spectrum has units of volts-rms squared (Vrms²). If the
            input signal is not in volts, Power Spectrum has units of the input signal unit-rms squared.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Power Spectrum Sxx(f) of a function x(t) is defined as

       Sxx(f) = X*(f)X(f) = |X(f)|²,

      where X(f) = F{x(t)}, and X* (f) is the complex conjugate of X(f).

      The Power Spectrum VI uses the FFT and DFT routines to compute the power
       spectrum, which is given by


      where Sxx represents the output sequence Power Spectrum, and nis the number of


4840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4841 ordinal=4841 -->
## Functions

Functions

samples in the input sequence X.

When the number of samples, n, in the input sequence X is a valid power of 2

n= 2m

for m= 1, 2, 3, …, 23,

the Power Spectrum VI computes the fast Fourier transform of a real-valued sequence
using the a fast radix-2 FFT algorithm and efficiently scales the magnitude square. The
largest Power Spectrum the VI can compute using the FFT is 223 (8,388,608 or 8M).

When the number of samples in the input sequence X is not a valid power of 2 but is
factorable as the product of small prime numbers, the Power Spectrum VI computes
the discrete Fourier transform of a real-valued sequence using an efficient DFT
algorithm and scales the magnitude square. The largest Power Spectrum the VI can
compute using the fast DFT is 222 – 1(4,194,303 or 4M – 1).

Let Ybe the Fourier transform of the input sequence X and nbe the number of
samples in it. You can show that

|Yn–i|² = |Y–i²|.

You can interpret the power in the (n– 1)th element of Yas the power in the –ith
element of the sequence, which represents the power in the –ith harmonic. You can
find the total power for the ith harmonic (DC and Nyquist component not included)
using

Power in the ith harmonic = 2|Yi|² = |Yi|² + |Yn– 1|² 0 < i< n/2

The total power in the DC and Nyquist components are |Y0|² and |Yn/2|² respectively.

If nis even, let        . The following table shows the format of the output sequence Sxx
corresponding to the Power Spectrum.


                                                    © National Instruments 4841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4842 ordinal=4842 -->
## Functions

Functions


         Array Element                               Interpretation
       Sxx0                                 Power in DC component
       Sxx1 = Sxx(n– 1)                       Power at frequency Δf
       Sxx2 = Sxx(n– 2)                       Power at frequency 2Δf
       Sxx3 = Sxx(n– 3)                       Power at frequency 3Δf

        ⋮                                      ⋮

       Sxx(k– 2) = Sxxn– (k– 2)                  Power at frequency (k– 2)Δf
       Sxx(k– 1) = Sxxn– (k– 1)                  Power at frequency (k– 1)Δf
      Sxxk                                Power in Nyquist harmonic

      The following illustration represents the preceding table information.


       Notice that the power spectrum is symmetric about the Nyquist frequency as the
       following illustration shows.


4842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4843 ordinal=4843 -->
## Functions

Functions


If nis odd, let            . The following table shows the format of the output sequence
Sxx corresponding to the Power Spectrum.


 Array Element                               Interpretation
 Sxx0                                 Power in DC component
 Sxx1 = Sxx(n– 1)                       Power at frequency Δf
 Sxx2 = Sxx(n– 2)                       Power at frequency 2Δf
 Sxx3 = Sxx(n– 3)                       Power at frequency 3Δf

 ⋮                                      ⋮

 Sxx(k– 2) = Sxxn– (k– 2)                  Power at frequency (k– 2)Δf
 Sxx(k– 1) = Sxxn– (k– 1)                  Power at frequency (k– 1)Δf
 Sxxk = Sxxn– k                        Power at frequency kΔf

The following illustration shows that when nis odd, the power spectrum is symmetric
about the Nyquist frequency, but the Nyquist frequency does not fall on a frequency
bin.


                                                    © National Instruments 4843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4844 ordinal=4844 -->
## Functions

Functions


      The format described in the preceding tables is an accepted standard in digital signal
       processing applications.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Spectral Analysis\DC
        Centered Spectrum.vi
            • labview\examples\Signal Processing\Transforms\Generalized
        Fourier Spectrum.vi
            • labview\examples\Signal Processing\Transforms\FFT and
        Power Spectrum Units.vi

     PowerPower SpectrumSpectrum (CDB)(CDB) VIVI

      Computes the Power Spectrum, Sxx, of the input sequence X. Wire data to the X input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.


4844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4845 ordinal=4845 -->
## Functions

Functions

   •     Power Spectrum —

    Power Spectrum returns the double-sided power spectrum of X.

       If the input signal is in volts (V), Power Spectrum has units of volts-rms squared (Vrms²). If the
    input signal is not in volts, Power Spectrum has units of the input signal unit-rms squared.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Power Spectrum Sxx(f) of a function x(t) is defined as

Sxx(f) = X*(f)X(f) = |X(f)|²,

where X(f) = F{x(t)}, and X* (f) is the complex conjugate of X(f).

The Power Spectrum VI uses the FFT and DFT routines to compute the power
spectrum, which is given by


where Sxx represents the output sequence Power Spectrum, and nis the number of
samples in the input sequence X.

When the number of samples, n, in the input sequence X is a valid power of 2

n= 2m

for m= 1, 2, 3, …, 23,

the Power Spectrum VI computes the fast Fourier transform of a real-valued sequence
using the a fast radix-2 FFT algorithm and efficiently scales the magnitude square. The
largest Power Spectrum the VI can compute using the FFT is 223 (8,388,608 or 8M).

When the number of samples in the input sequence X is not a valid power of 2 but is

                                                    © National Instruments 4845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4846 ordinal=4846 -->
## Functions

Functions

       factorable as the product of small prime numbers, the Power Spectrum VI computes
       the discrete Fourier transform of a real-valued sequence using an efficient DFT
       algorithm and scales the magnitude square. The largest Power Spectrum the VI can
      compute using the fast DFT is 222 – 1(4,194,303 or 4M – 1).

       Let Ybe the Fourier transform of the input sequence X and nbe the number of
      samples in it. You can show that

      |Yn–i|² = |Y–i²|.

      You can interpret the power in the (n– 1)th element of Yas the power in the –ith
      element of the sequence, which represents the power in the –ith harmonic. You can
       find the total power for the ith harmonic (DC and Nyquist component not included)
       using

      Power in the ith harmonic = 2|Yi|² = |Yi|² + |Yn– 1|² 0 < i< n/2

      The total power in the DC and Nyquist components are |Y0|² and |Yn/2|² respectively.

           If nis even, let        . The following table shows the format of the output sequence Sxx
       corresponding to the Power Spectrum.


         Array Element                               Interpretation
       Sxx0                                 Power in DC component
       Sxx1 = Sxx(n– 1)                       Power at frequency Δf
       Sxx2 = Sxx(n– 2)                       Power at frequency 2Δf
       Sxx3 = Sxx(n– 3)                       Power at frequency 3Δf

        ⋮                                      ⋮

       Sxx(k– 2) = Sxxn– (k– 2)                  Power at frequency (k– 2)Δf
       Sxx(k– 1) = Sxxn– (k– 1)                  Power at frequency (k– 1)Δf
      Sxxk                                Power in Nyquist harmonic


4846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4847 ordinal=4847 -->
## Functions

Functions

The following illustration represents the preceding table information.


Notice that the power spectrum is symmetric about the Nyquist frequency as the
following illustration shows.


If nis odd, let            . The following table shows the format of the output sequence
Sxx corresponding to the Power Spectrum.


 Array Element                               Interpretation
 Sxx0                                 Power in DC component
 Sxx1 = Sxx(n– 1)                       Power at frequency Δf
 Sxx2 = Sxx(n– 2)                       Power at frequency 2Δf


                                                    © National Instruments 4847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4848 ordinal=4848 -->
## Functions

Functions


         Array Element                               Interpretation
       Sxx3 = Sxx(n– 3)                       Power at frequency 3Δf

        ⋮                                      ⋮

       Sxx(k– 2) = Sxxn– (k– 2)                  Power at frequency (k– 2)Δf
       Sxx(k– 1) = Sxxn– (k– 1)                  Power at frequency (k– 1)Δf
      Sxxk = Sxxn– k                        Power at frequency kΔf

      The following illustration shows that when nis odd, the power spectrum is symmetric
      about the Nyquist frequency, but the Nyquist frequency does not fall on a frequency
        bin.


      The format described in the preceding tables is an accepted standard in digital signal
       processing applications.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Spectral Analysis\DC
        Centered Spectrum.vi
            • labview\examples\Signal Processing\Transforms\Generalized
        Fourier Spectrum.vi
            • labview\examples\Signal Processing\Transforms\FFT and
        Power Spectrum Units.vi

4848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4849 ordinal=4849 -->
## Functions

Functions

CrossCross PowerPower SpectrumSpectrum

Computes the single-sided, scaled, cross power spectrum of two real-time signals.


Inputs/Outputs

   •      Signal X (V) —

    Signal X is the input, time-domain signal X, usually in volts.

    The time-domain record must contain at least three cycles of the signal for a valid estimate.

   •      Signal Y (V) —

    Signal Y is the input, time-domain signal Y, usually in volts.

    The time-domain record must contain at least three cycles of the signal for a valid estimate.

   •      dt —

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

                                                    © National Instruments 4849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4850 ordinal=4850 -->
## Functions

Functions


            df is the frequency interval of the power spectrum in hertz, if dt is in seconds.


      The Cross Power Spectrum VI computes the single-sided cross power spectrum of
       Signal X and Signal Y. If Signal X and Signal Y have different lengths, the VI first pads
       the end of the shorter input signal with zeros to make the signals the same length. The
        VI then uses the following equation to compute the two-sided cross power spectrum:


      where Nrepresents the common length of the two input signals after the VI pads the
      end of the shorter input signal with zeros.

      To compute the single-sided cross power spectrum, the VI converts the two-sided
       cross power spectrum to the single-sided form.

       df returns the frequency interval, which typically is used as the multiplier of the
       frequency axis in order to display the frequency domain.

      The cross power spectrum is an important concept for measurements. Refer to the
       Cross Power Spectrum conceptual topic for more information about the power
       spectrum.

           Note One difference between the Cross Power Spectrum VI and the Cross
            Power VI is that this VI returns the single-sided spectrum with the amplitude
            and phase as separate outputs, but the Cross Power VI returns the two-sided
             spectrum with the amplitude and phase as one complex output.

     UnevenlyUnevenly SampledSampled SignalSignal SpectrumSpectrum

       Calculates the power spectrum of a signal that is unevenly spaced in time.


4850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4851 ordinal=4851 -->
## Functions

Functions

Inputs/Outputs

   •     XTime —

    XTime is the discrete- and unevenly-spaced times.

   •     X —

    X represents the data material at times XTime.

    There is a one-to-one relation between XTime and X.

   •     Power Spectrum FFT {X} Frequency —

   Power Spectrum FFT {X} Frequency are the frequency points at which the power spectrum is
     calculated.

   •     Power Spectrum FFT {X} —

   Power Spectrum FFT {X} is the power spectrum, in the sense of the Lomb normalized
    periodogram.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The algorithm used is based on the Lomb normalized periodogram. Let the data Xk be
given at the time points tk. In other words,

X = {x0, x1, …, xn– 1}

and

XTime = {t0, t1, …, tn– 1}.

Furthermore,


                                                    © National Instruments 4851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4852 ordinal=4852 -->
## Functions

Functions

      and

                                        .


      Then the Lomb normalized periodogram is defined as


                                                                                                  ,


       with


      The following diagram shows the Fourier transform of length 256 of a signal that has
      been sampled at unequal intervals of time. The signal is a combination of sine waves
       of frequencies 20, 40, 60, and 80 Hz. The duration of the signal is 1 sec. The sampling
       frequency was chosen as 256 Hz, giving the frequency resolution of 1 Hz.


     Examples

       Refer to the following example files included with LabVIEW.


4852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4853 ordinal=4853 -->
## Functions

Functions

  • labview\examples\Signal Processing\Transforms\Generalized
   Fourier Spectrum.vi
  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

AmplitudeAmplitude andand PhasePhase SpectrumSpectrum

Computes the single-sided, scaled amplitude spectrum of a real-valued time-domain
signal and returns the amplitude spectrum as magnitude and phase.


Inputs/Outputs

   •      Signal (V) —

    Signal specifies the input time-domain signal, usually in volts.

    The time-domain record must contain at least three cycles of the signal for a valid estimate.

   •     unwrap phase (T) —

   unwrap phase, when TRUE, enables phase unwrapping on the output Amp Spectrum Phase.
    The default is TRUE.

       If unwrap phase is FALSE, this VI does not unwrap the output phase.

   •      dt —

    dt is the sample period of the time-domain signal, usually in seconds.

    Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal. The default is 1.

   •    Amp Spectrum Mag (Vrms) —

   Amp Spectrum Mag returns the magnitude of the single-sided power spectrum.

       If the input signal is in volts (V), Amp Spectrum Mag has units of volts-rms (Vrms). If the input
    signal is not in volts, Amp Spectrum Mag has units of the input signal unit-rms.


                                                    © National Instruments 4853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4854 ordinal=4854 -->
## Functions

Functions

               •    Amp Spectrum Phase (radians) —

        Amp Spectrum Phase is the single-sided amplitude spectrum phase in radians.

               •       df —

            df is the frequency interval of the power spectrum in hertz, if dt is in seconds.


      The Amplitude and Phase Spectrum VI uses two steps to compute the single-sided,
       scaled amplitude spectrum.

         First, this VI uses the following equation to compute the two-sided amplitude
       spectrum:


      where Ais the two-sided amplitude spectrum, Xis the discrete Fourier transform of
       Signal, and Nis the number of points in Signal.

      Second, this VI uses the following equation to convert the two-sided amplitude
      spectrum to the single-sided amplitude spectrum:


      where Bis the single-sided amplitude spectrum, and    is the floor operation.

     Amp Spectrum Mag is the magnitude of the single-sided amplitude spectrum B, as
      shown in the following equation:

     Amp Spectrum Mag = |B|

     Amp Spectrum Phase is the corresponding phase in radians, as shown in the following
       equation:

     Amp Spectrum Phase = phase(B)


4854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4855 ordinal=4855 -->
## Functions

Functions

df returns the frequency interval, which typically is used as the multiplier of the
frequency axis in order to display the frequency domain.

      Note If you specify the same inputs for this VI and the Auto Power Spectrum
          VI, Amp Spectrum Mag equals the square root of the Power Spectrum that
       the Auto Power Spectrum VI returns.

Related Information

Output Units for FFT-Based VIs

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Point by Point\
   Amplitude Spectrum PtbyPt.vi
  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

SpectrumSpectrum UnitUnit ConversionConversion

Converts either the power, amplitude, or gain (amplitude ratio) spectrum to alternate
formats including Log (decibel and dbm) and spectral density.


Inputs/Outputs

   •       signal unit (V) —

    signal unit is a string containing the unit of the input time domain signal. The default setting is


                                                    © National Instruments 4855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4856 ordinal=4856 -->
## Functions

Functions


              in volts.

                    If the original signal unit was in volts, then this input should contain the letter V for volts.

               •     Spectrum in —

          Spectrum in, on input, contains the spectrum of a time domain signal. It can be of type specified
           by the spectrum type selector.

               •      spectrum type —

           spectrum type specifies the type of spectrum wired to Spectrum. The default is 0.

           0   Power (Vrms²)
           1    Amplitude (Vrms)
           2    Gain (amplitude ratio)

               •       log/linear —

             log/linear specifies linear or log spectrum output. The default is 1.

           0               Linear
           1           DB
           2         DBm

               •      display unit —

            display unit is the output unit for the spectrum.

           You can set display unit to one of the values listed in the following table. The last four selections
            are amplitude spectral density (4,5) and power spectral density (6,7). The control cluster window
            constants contains constants for the selected window (from the Scaled Time Domain Window
                VI). You need this input only when you use the spectral density output formats (the last four
           output unit selections).

                 Vrms           0
                    (volts rms)
                 Vpk           1
                    (volts peak)
           2    Vrms² volts


4856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4857 ordinal=4857 -->
## Functions

Functions


       (squared rms)
       Vpk² volts  3
       (squared peak)
        Vrms/sqrt(Hz) volts  4
       (rms per root Hz)
        Vpk/sqrt(Hz) volts  5
       (peak per root Hz)
       Vrms²/Hz volts  6
       (squared rms per Hz)
       Vpk²/Hz volts  7
       (squared peak per Hz)

•       df —

  df is the line frequency interval of the input spectrum. The default is 1.0.

  You need this input only when you use the spectral density output formats (the last four display
  unit selections).

•     window constants —

  window constants contains the window constants for the selected window. You obtain window
  constants from the Scaled Time Domain Window VI.

  You need this input only when you use the spectral density output formats, the last four display
  unit selections. The default values are set to those of the rectangular window (no window).

      •     eq noise BW —

     eq noise BW is the equivalent noise bandwidth (ENBW) of the window that was used. The
       default is 1.0.

      You can use this value to divide a sum of individual power spectra of the power spectrum or
       to compute the power in a given frequency span.

      •      coherent gain —

      coherent gain is the inverse of the scaling factor applied to the window. The default is 1.0.


•     Spectrum out —


                                                   © National Instruments 4857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4858 ordinal=4858 -->
## Functions

Functions


          Spectrum out, on output, contains the spectrum in the form specified by log/linear and display
              units.

               •      spectrum unit —

           spectrum unit is a string containing the unit of the output spectrum.

                    If the output spectrum is in decibels form, the unit is prepended by dB.

     STFTSTFT SpectrogramsSpectrograms

      Computes the signal energy distribution in the joint time-frequency domain, using the
       short-time Fourier transform (STFT) algorithm.


      Inputs/Outputs

               •      time-freq config —

            time-freq config specifies the configuration of the frequency bins. time-freq config also
            determines the number of columns in STFT Spectrogram {X}.

                     •       force freq bins to power of 2? —

                 force freq bins to power of 2? specifies whether to coerce the frequency bins to a power of
                    2. If force freq bins to power of 2? is TRUE and frequency bins is not a power of 2, this VI
                  sets frequency bins to the nearest power of 2. The default is TRUE.

                     •      exclude Nyquist frequency? —

                exclude Nyquist frequency? specifies whether to exclude the energy at the Nyquist
                frequency from STFT Spectrogram {X}.


4858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4859 ordinal=4859 -->
## Functions

Functions


          If frequency bins is even and exclude Nyquist frequency? is TRUE, STFT Spectrogram {X}
      does not include the energy at the Nyquist frequency. If frequency bins is odd, LabVIEW
       ignores exclude Nyquist frequency?. The default is TRUE.


•     X —

  X specifies the input time-domain signal.

•      time-freq sampling info —

  time-freq sampling info specifies the density to use to sample the signal in the joint time-
  frequency domain and defines the size of the resulting 2D time-frequency array.

      •      time steps —

      time steps specifies the number of samples to shift the sliding window.

     When time steps is less than or equal to zero, this VI adjusts time steps automatically so
       that no more than 512 rows exist in STFT Spectrogram {X}. The default is –1

      •      frequency bins —

      frequency bins specifies the FFT size of the STFT. If frequency bins is less than or equal to
       zero, this VI sets frequency bins to 512. If frequency bins is 1, this VI coerces frequency bins
       to 2. The default is 512.


•     window info —

  window info specifies information about the window you want to use to compute the STFT.

      •      type —

      type specifies the type of window to use to compute the STFT. The default is Hanning.

      0         Rectangle
      1        Hanning
      2       Hamming


                                                   © National Instruments 4859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4860 ordinal=4860 -->
## Functions

Functions


               3         Blackman-Harris
               4         Exact Blackman
               5        Blackman
               6           Flat Top
               7        4 Term B-Harris
               8        7 Term B-Harris
               9       Low Sidelobe
               11       Blackman Nuttall
               30         Triangle
               31        Bartlett-Hanning
               32      Bohman
               33        Parzen
               34       Welch
               60         Kaiser
               61        Dolph-Chebyshev
               62        Gaussian

                     •      length —

                length specifies the length of the window in samples. If length is less than or equal to zero,
                   this VI sets length to 64. The default is 64.


               •     window parameter —

          window parameter is the beta parameter for a Kaiser window; the ratio, s, of the mainlobe to
            the sidelobe for a Dolph-Chebyshev window; and the standard deviation for a Gaussian window.
                    If the window type is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, sto 60
              for a Dolph-Chebyshev window, and the standard deviation to     for a Gaussian window,
           where Lis the window length.

               •      energy conservation? —

           energy conservation? specifies whether to scale STFT Spectrogram {X} so that the energy in the
              joint time-frequency domain equals the energy in the time domain. The default is TRUE.

               •     STFT Spectrogram {X} —


4860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4861 ordinal=4861 -->
## Functions

Functions


    STFT Spectrogram {X} is a 2D array that describes the time waveform energy distribution in the
     joint time-frequency domain.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


To compute STFT Spectrogram {X}, this VI first computes the STFT of X. To compute
the STFT of X, this VI uses a sliding window to divide the signal into several blocks of
data. The VI then applies an N-points fast Fourier transform to each block of data to
obtain the frequency contents of each block of data, where Nis frequency bins. The
STFT aligns the center of the first sliding window with the first sample of the signal X
and extends the beginning of the signal by adding zeros. The sliding window moves
time steps samples to the next block of data. If the window moves out of X, this VI pads
X with zeros.

The following illustration shows the procedure this VI uses to compute the STFT.


If force freq bins to power of 2? is TRUE, and frequency bins is not a power of 2, then
the following equation also is true:

K= 2[log2(frequency bins)]


                                                    © National Instruments 4861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4862 ordinal=4862 -->
## Functions

Functions

      where [ ] is the nearest operation.

       Otherwise, K= frequency bins.

           If the result of the STFT is the matrix STFT{X}, then the size of STFT{X} is M-by-K,
      where the following are true:


            •

            • Lis the number of elements in X
            •     is the round down operation

      You can use STFT{X} to approximate the energy in the joint time-frequency domain
       using the following expression:


       This result almost equals the energy in the time domain, as shown in the following
       expression:


        After computing the STFT of X, this VI computes the STFT spectrogram of X. This VI
       calculates STFT spectrogram as the magnitude square of the elements in STFT{X}.
      Because the FFT returns symmetric results, this VI calculates the STFT Spectrogram
        {X} only on the left half of STFT{X}, as shown in the following equation:


      where the following are true:

            • i= 0, 1, …, M–1
            • j= 0, 1, …, N–1

4862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4863 ordinal=4863 -->
## Functions

Functions


  •


  •     is the round up operation.

If you specify a small value for time steps, the VI might return a large spectrogram,
which requires a long computation time and more memory. National Instruments
recommends you set time steps so that the number of rows in spectrogram does not
exceed 512. If you need a small sampling rate to observe more details and the signal
length is large, divide the signal into smaller segments and compute the spectrogram
for each segment.

The window length affects the time resolution and the frequency resolution of the
STFT. A narrow window results in a fine time resolution but a coarse frequency
resolution because narrow windows have a short time duration but a wide bandwidth.
A wide window results in a fine frequency resolution but a coarse time resolution
because wide windows have a long time duration but a narrow frequency bandwidth.

This VI returns the same result as the TFA STFT Spectrogram VI in the LabVIEW
Advanced Signal Processing Toolkit if you set force freq bins to power of 2?, exclude
Nyquist frequency?, and energy conservation? to TRUE.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\STFT
   Spectrogram Demo.vi

WVDWVD SpectrogramSpectrogram

Computes the energy distribution of the input signal in the joint time-frequency
domain using the Wigner-Ville distribution (WVD) algorithm.


                                                    © National Instruments 4863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4864 ordinal=4864 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is the time-domain signal.

               •      time increment —

           time increment controls the time intervals of the Wigner-Ville Distribution. You express time
           increment in units of samples. The default is 1.

            For example, if you sample the time waveform at fsHz, the spacing between the rows of WVD
           Spectrogram {X} is time increment/fsseconds.

             Increasing time increment decreases the computation time and reduces memory requirements
           but also reduces time-domain resolution. Decreasing time increment improves time-domain
             resolution but increases the computation time and memory requirements.

               •    WVD Spectrogram {X} —

        WVD Spectrogram {X} is a 2D array that describes the energy distribution of X in the joint time-
            frequency domain.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       For a discrete signal X, with an analytic associate of Z, the following equation defines
       the Wigner-Ville distribution of the analytic associate, WVDZ(n, f):


      where nis the index in the time domain, fis the index in the frequency domain, and
       the analytic associate Zis X + i*H[X], where H[X] is the Hilbert Transform of X.

      The following front panel shows the WVD spectrogram and the power spectrum of a
       128-point Gaussian-modulated sine pattern. The time increment is 1.


4864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4865 ordinal=4865 -->
## Functions

Functions


A smaller time increment uses more computation time and more memory, and
consequently leads to a finer time-domain resolution. Thus, you can use the time
increment to balance between the cost and the resolution.

The WVD has many properties you can use for signal analysis, such as marginal
properties, the time marginal condition, the frequency marginal condition, the mean
instantaneous frequency, the group delay property, and the time and frequency shift
invariance.

The WVD has the best joint time-frequency resolution of all the quadratic joint time-
frequency analysis methods. However, the cross-term artifacts from a multi-
component signal degrade the readability of the time-frequency representation and
limits the usefulness of the WVD. The following graph shows a signal composed of two
Gaussian-modulated sine patterns. The frequency of the first sine wave is 250 Hz, and
the frequency of the second sine wave is 125 Hz. The time centers of the first and
second sine waves are 0.075 s and 0.18 s, respectively.


                                                    © National Instruments 4865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4866 ordinal=4866 -->
## Functions

Functions


        Ideally, the signal has only two atoms in the time-frequency domain. However, as a
        result of the WVD algorithm, the WVD of the signal contains cross-term artifacts, as
      shown in the following graph.


      Use the LabVIEW Advanced Signal Processing Toolkit for more joint-time frequency
       analysis methods such as, STFT, Gabor Spectrogram, Cohen, Choi-Williams
        Distribution, and Cone-Shape Distribution.

     CrossCross PowerPower

      Computes the cross power spectrum, Sxy, of the input signals X and Y. Wire data to the
      X input to determine the polymorphic instance to use or manually select the instance.


            • Cross Power (DBL) VI
            • Cross Power (CDB) VI


4866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4867 ordinal=4867 -->
## Functions

Functions

The cross power, Sxy(f) of the signals x(t) and y(t) is defined as

Sxy(f) = X*(f)Y(f)

where X*(f) is the complex conjugate of X(f),

X(f) = F{x(t)}, Y(f) = F{y(t)}.

This VI uses the FFT or DFT routine to compute the cross power spectrum, which is
given by

                          ,

where Sxy represents the complex sequence Sxy, and nis the number of samples that
can accommodate both input sequences X and Y.

The largest cross power that the Cross Power VI can compute by the FFT is 223
(8,388,608 or 8M).

      Note Some textbooks define the cross power spectrum as S'xy(f) =
         X(f)Y*(f). If you prefer this definition of cross power to the one specified in
       the Cross Power VI, take the complex conjugate of the output sequence Sxy.
       Because the Cross Power VI operates on the real and imaginary portions
        separately, you can use the following block diagram to obtain the results for
        S'xy(f).


When the number of samples in X and Y are equal and are a valid power of 2,

n= m= 2k

for k= 1, 2, 3,…, 23,

                                                    © National Instruments 4867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4868 ordinal=4868 -->
## Functions

Functions

      where nis the number of samples in X, and mis the number of samples in Y, the Cross
      Power VI makes direct calls to the FFT routine to compute the complex cross power
       sequence. This technique is efficient in both execution time and memory management
      because the Cross Power VI performs the operations in place.

     When the number of samples in X and Y are not equal,

   n≠ m

      where nis the number of samples in X, and mis the number of samples in Y, the Cross
      Power VI first resizes the smaller sequence by padding it with zeros to match the size of
       the larger sequence. If this size is a valid power of 2,

     max(n,m) = 2k

        for k= 1, 2, 3, …, 23,

       the Cross Power VI computes the cross power spectrum using the FFT. Otherwise, the
       Cross Power VI uses the slower DFT to compute the cross power spectrum. Thus, the
        size of the complex output sequence is

      size= max(n,m)
      CrossCross PowerPower (DBL)(DBL) VIVI

      Computes the cross power spectrum, Sxy, of the input signals X and Y. Wire data to the
      X input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the first input sequence.

               •      Y —


4868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4869 ordinal=4869 -->
## Functions

Functions


    Y is the second input sequence.

   •      Sxy —

    Sxy is the cross power spectrum of input signals X and Y.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The cross power, Sxy(f) of the signals x(t) and y(t) is defined as

Sxy(f) = X*(f)Y(f)

where X*(f) is the complex conjugate of X(f),

X(f) = F{x(t)}, Y(f) = F{y(t)}.

This VI uses the FFT or DFT routine to compute the cross power spectrum, which is
given by

                          ,

where Sxy represents the complex sequence Sxy, and nis the number of samples that
can accommodate both input sequences X and Y.

The largest cross power that the Cross Power VI can compute by the FFT is 223
(8,388,608 or 8M).

      Note Some textbooks define the cross power spectrum as S'xy(f) =
         X(f)Y*(f). If you prefer this definition of cross power to the one specified in
       the Cross Power VI, take the complex conjugate of the output sequence Sxy.
       Because the Cross Power VI operates on the real and imaginary portions
        separately, you can use the following block diagram to obtain the results for


                                                    © National Instruments 4869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4870 ordinal=4870 -->
## Functions

Functions

                S'xy(f).


     When the number of samples in X and Y are equal and are a valid power of 2,

   n= m= 2k

        for k= 1, 2, 3,…, 23,

      where nis the number of samples in X, and mis the number of samples in Y, the Cross
      Power VI makes direct calls to the FFT routine to compute the complex cross power
       sequence. This technique is efficient in both execution time and memory management
      because the Cross Power VI performs the operations in place.

     When the number of samples in X and Y are not equal,

   n≠ m

      where nis the number of samples in X, and mis the number of samples in Y, the Cross
      Power VI first resizes the smaller sequence by padding it with zeros to match the size of
       the larger sequence. If this size is a valid power of 2,

     max(n,m) = 2k

        for k= 1, 2, 3, …, 23,

       the Cross Power VI computes the cross power spectrum using the FFT. Otherwise, the
       Cross Power VI uses the slower DFT to compute the cross power spectrum. Thus, the
        size of the complex output sequence is

      size= max(n,m)


4870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4871 ordinal=4871 -->
## Functions

Functions

CrossCross PowerPower (CDB)(CDB) VIVI

Computes the cross power spectrum, Sxy, of the input signals X and Y. Wire data to the
X input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the first complex valued input sequence.

   •      Y —

    Y is the second complex valued input sequence.

   •      Sxy —

    Sxy is the cross power spectrum of input signals X and Y.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The cross power, Sxy(f) of the signals x(t) and y(t) is defined as

Sxy(f) = X*(f)Y(f)

where X*(f) is the complex conjugate of X(f),

X(f) = F{x(t)}, Y(f) = F{y(t)}.

This VI uses the FFT or DFT routine to compute the cross power spectrum, which is
given by

                          ,

                                                    © National Instruments 4871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4872 ordinal=4872 -->
## Functions

Functions

      where Sxy represents the complex sequence Sxy, and nis the number of samples that
      can accommodate both input sequences X and Y.

      The largest cross power that the Cross Power VI can compute by the FFT is 223
       (8,388,608 or 8M).

           Note Some textbooks define the cross power spectrum as S'xy(f) =
                X(f)Y*(f). If you prefer this definition of cross power to the one specified in
              the Cross Power VI, take the complex conjugate of the output sequence Sxy.
             Because the Cross Power VI operates on the real and imaginary portions
                separately, you can use the following block diagram to obtain the results for
                S'xy(f).


     When the number of samples in X and Y are equal and are a valid power of 2,

   n= m= 2k

        for k= 1, 2, 3,…, 23,

      where nis the number of samples in X, and mis the number of samples in Y, the Cross
      Power VI makes direct calls to the FFT routine to compute the complex cross power
       sequence. This technique is efficient in both execution time and memory management
      because the Cross Power VI performs the operations in place.

     When the number of samples in X and Y are not equal,

   n≠ m

      where nis the number of samples in X, and mis the number of samples in Y, the Cross
      Power VI first resizes the smaller sequence by padding it with zeros to match the size of
       the larger sequence. If this size is a valid power of 2,

4872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4873 ordinal=4873 -->
## Functions

Functions

max(n,m) = 2k

for k= 1, 2, 3, …, 23,

the Cross Power VI computes the cross power spectrum using the FFT. Otherwise, the
Cross Power VI uses the slower DFT to compute the cross power spectrum. Thus, the
size of the complex output sequence is

size= max(n,m)
PowerPower &amp;&amp; FrequencyFrequency EstimateEstimate

Computes the estimated power and frequency around the peak frequency in the
power spectrum of a time-domain signal.


Inputs/Outputs

   •     Power Spectrum (V^2 rms) —

    Power Spectrum is the power spectrum of a time domain signal. Power Spectrum is the output
     of the Auto Power Spectrum VI.

   •     peak frequency (max) —

    peak frequency is the frequency, usually in hertz, of the frequency peak around which you want
     to estimate the frequency and power. The default is –1.

       If you do not wire this parameter, the VI automatically searches for the maximum peak in the
    power spectrum array and estimates the frequency and power around it.

   •     window constants —

   window constants specifies the property constants of a window. If you apply a window to a
    time-domain signal to avoid spectral leakage when you compute the power spectrum of the
     signal, you can use window constants to compensate for the effect of the window you apply.


                                                    © National Instruments 4873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4874 ordinal=4874 -->
## Functions

Functions


          The default values are set to those of the rectangular window (no window).

          window constants is usually the output of the Scaled Time Domain Window VI.

                     •     eq noise BW —

              eq noise BW is the equivalent noise bandwidth (ENBW) of the window that was used. The
                 default is 1.0.

               You can use this value to divide a sum of individual power spectra of the power spectrum or
                 to compute the power in a given frequency span.

                     •      coherent gain —

               coherent gain is the inverse of the scaling factor applied to the window. The default is 1.0.


               •       df —

            df is the frequency interval of the power spectrum. The default is 1.0.

               •      span —

           span is the number of frequency lines (bins) around the peak to be included in the peak
            frequency and power estimation.

          The default is 7, which means that the power in three frequency lines before the peak frequency
               line, the peak frequency line itself, and three frequency lines after the peak are included in the
             estimation. This is adequate for most windows.

               •       est frequency peak —

             est frequency peak is the estimated frequency of the peak in the input Power Spectrum.

             est frequency peak is computed as                                       for j= i– span/2, …i+
            span/2,

           where i= peak index, Power Spectrum (j) = power in bin j, and df = frequency bin width.

               •       est power peak —

             est power peak is the estimated power of the peak in the input Power Spectrum.


4874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4875 ordinal=4875 -->
## Functions

Functions


    est power peak is computed as                                 for j= i– span/2, …i+ span/2,

    where i= peak index, Power Spectrum (j) = power in bin j, and ENBW = equivalent noise
    bandwidth of the window.


With the Power & Frequency Estimate VI, you can achieve good frequency estimates for
measured frequencies that lie between frequency lines on the spectrum. The Power &
Frequency Estimate VI also makes corrections for the window function you use.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Spectral Analysis\
   Power & Frequency Estimator.vi

BunemanBuneman FrequencyFrequency EstimatorEstimator

Estimates the frequency of a given sine wave of unknown frequency using the
Buneman formula.


Inputs/Outputs

   •     X —

    X is the sampled signal at consecutive times.

   •      beta —

    beta is the estimation of the frequency of the sine wave that X represents. beta is the index of
    the maximum frequency and can be a noninteger.

    The following equation describes the actual frequency: beta * df = beta * fs/number of samples

   •       error —

                                                    © National Instruments 4875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4876 ordinal=4876 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If an underlying time signal is not exactly periodic with period n, where ndenotes the
        size of the data array, you can use the Buneman algorithm to calculate the unknown
       frequency

      0 ≤ f0 ≤ f1 ≤ f2 ≤ f3< 0.5fs.

      The following formula describes the Buneman algorithm:


      where Fb denotes the value of the Fourier transform of the signal X at the frequency b.
      You can determine the value of busing the greatest value of |Fb(X)|.

      The formula for β is exact for pure sine waves and a good estimation in all other cases.

     TransformsTransforms

      Use the Transforms VIs to implement common transforms used in signal processing.
      The LabVIEW FFT-based VIs use different output units and scale factors.

      The VIs on this palette can return signal processing error codes.


         Palette Object   Description

                     Computes the fast Fourier transform (FFT) of the input sequence X. Wire data to
        FFT
                         the X input to determine the polymorphic instance to use or manually select the


4876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4877 ordinal=4877 -->
## Functions

Functions


Palette Object   Description

                  instance.


Fast Hilbert              Computes the fast Hilbert transform of the input sequence X.Transform


FHT           Computes the fast Hartley transform (FHT) of the input sequence X.


Wavelet              Computes the wavelet transform based on the Daubechies4 function of the inputTransform               sequence X.Daubechies4

Walsh              Computes the real Walsh Hadamard transform of the input sequence X.Hadamard


              Computes the Discrete Cosine Transform (DCT) of the input sequence X. Wire data
DCT             to the X input to determine the polymorphic instance to use or manually select
                the instance.


              Computes the Discrete Sine Transform (DST) of the input sequence X. Wire data to
DST            the X input to determine the polymorphic instance to use or manually select the
                  instance.


Chirp Z        Computes the Chirp-Z transform of the input sequence X. Wire data to the X input
Transform       to determine the polymorphic instance to use or manually select the instance.


Laplace
              Computes the real Laplace transform of the input sequence X.
Transform Real


              Computes the inverse discrete Fourier transform (IDFT) of the input sequence FFT
Inverse FFT
                     {X}. You must manually select the polymorphic instance you want to use.


                                                    © National Instruments 4877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4878 ordinal=4878 -->
## Functions

Functions


         Palette Object   Description

         Inverse Fast                     Computes the inverse fast Hilbert transform of the input sequence X using Fourier
          Hilbert                              identities.        Transform


         Inverse FHT     Computes the inverse fast Hartley transform of the input sequence X.

        Wavelet
        Transform      Computes the inverse of the wavelet transform based on the Daubechies4
        Daubechies4     function of the input sequence X.
         Inverse

        Walsh                     Computes the inverse of the real Walsh Hadamard transform of the input       Hadamard
                       sequence X.         Inverse


                     Computes the inverse Discrete Cosine Transform (DCT) of the input sequence DCT
         Inverse DCT       {X}. Wire data to the DCT {X} input to determine the polymorphic instance to use
                         or manually select the instance.


                     Computes the inverse Discrete Sine Transform (DST) of the input sequence DST
         Inverse DST       {X}. Wire data to the DST {X} input to determine the polymorphic instance to use
                         or manually select the instance.


         Inverse Chirp Z                     Computes the inverse Chirp-Z transform of the input sequence Chirp-Z {X}.
        Transform


      Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Transforms\
        Transforms.lvproj


4878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4879 ordinal=4879 -->
## Functions

Functions

FFTFFT

Computes the fast Fourier transform (FFT) of the input sequence X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


  • Real FFT VI
  • Complex FFT VI
  • 2D Real FFT VI
  • 2D Complex FFT VI

1D FFT

For 1D signals, the FFT VI computes the discrete Fourier transform (DFT) of the input
sequence with a fast Fourier transform algorithm. The 1D DFT is defined as:

                   for n= 0, 1, 2, …, N–1

where xis the input sequence, Nis the number of elements of x, and Yis the
transform result.

The frequency resolution, or the frequency spacing between the components of Y, is:


where fs is the sampling frequency.

The following table illustrates the pattern of the elements of FFT {X} for various FFT
size and shift values, where Yis FFT {X} and nis the FFT size:


                                                    © National Instruments 4879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4880 ordinal=4880 -->
## Functions

Functions


    nis even (k= n/2)                 nis odd (k= (n-1)/2)

          Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency

        FALSE
                Y0          DC component           Y0          DC component
          (default)


        FALSE
                Y1          Δf                    Y1          Δf
          (default)


        FALSE
                Y2          2Δf                   Y2          2Δf
          (default)


        FALSE
                Y3          3Δf                   Y3          3Δf
          (default)


        ⋮        ⋮             ⋮                       ⋮             ⋮


        FALSE
                 Yk–2          (k–2)Δf                 Yk–2          (k–2)Δf
          (default)


        FALSE
                 Yk–1          (k–1)Δf                 Yk–1          (k–1)Δf
          (default)


        FALSE
            Yk            Nyquist Frequency      Yk         kΔf
          (default)


4880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4881 ordinal=4881 -->
## Functions

Functions

nis even (k= n/2)                 nis odd (k= (n-1)/2)

Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency

FALSE
         Yk+1          –(k–1)Δf                Yk+1         –kΔf
(default)


FALSE
         Yk+2          –(k–2)Δf                Yk+2          –(k–1)Δf
(default)


⋮        ⋮             ⋮                       ⋮             ⋮


FALSE
         Yn–3         –3Δf                    Yn–3         –3Δf
(default)


FALSE
         Yn–2         –2Δf                    Yn–2         –2Δf
(default)


FALSE
         Yn–1         –Δf                     Yn–1         –Δf
(default)

TRUE    Y0             –(Nyquist Frequency)      Y0          –kΔf
TRUE    Y1            –(k–1)Δf               Y1            –(k–1)Δf
TRUE    Y2            –(k–2)Δf               Y2            –(k–2)Δf
TRUE    Y3            –(k–3)Δf               Y3            –(k–3)Δf

⋮        ⋮             ⋮                       ⋮             ⋮

TRUE    Yk–2         –2Δf                    Yk–2         –2Δf
TRUE    Yk–1         –Δf                     Yk–1         –Δf


                                                    © National Instruments 4881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4882 ordinal=4882 -->
## Functions

Functions

    nis even (k= n/2)                 nis odd (k= (n-1)/2)

          Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency
       TRUE   Yk         DC component         Yk         DC component
       TRUE    Yk+1        Δf                      Yk+1        Δf
       TRUE    Yk+2         2Δf                     Yk+2         2Δf

        ⋮        ⋮             ⋮                       ⋮             ⋮

       TRUE    Yn–3          (k–3)Δf                 Yn–3          (k–2)Δf
       TRUE    Yn–2          (k–2)Δf                 Yn–2          (k–1)Δf
       TRUE    Yn–1          (k–1)Δf                 Yn–1        kΔf

     2D FFT

       For 2D signals, the FFT VI computes the discrete Fourier transform (DFT) of the input
       matrix. This VI performs a 1D FFT on the rows of the input matrix and then performs a
      1D FFT on the columns of the output of the preceding step. The DFT of an M-by-N
       matrix is defined as:

                                             for u= 0, 1, …, M–1, v=0, 1, …, N–1

      where xis the input matrix and Yis the transform result.

      The illustration below shows the effect of shift? on the 2D FFT result:


4882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4883 ordinal=4883 -->
## Functions

Functions


 2D input signals                FFT without shift               FFT with shift


Related Information

Output Units for FFT-Based Vis

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

RealReal FFTFFT VIVI

Computes the fast Fourier transform (FFT) of the input sequence X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is a real vector.

   •       shift? —


                                                    © National Instruments 4883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4884 ordinal=4884 -->
## Functions

Functions


              shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

               •     FFT size —

           FFT size is the length of the FFT you want to perform.

                    If FFT size is greater than the number of elements in X, this VI adds zeros to the end of X to match
            the size of FFT size. If FFT size is less than the number of elements in X, this VI uses only the first
      nelements in X to perform the FFT, where nis FFT size. If FFT size is less than or equal to 0, this
              VI uses the length of X as the FFT size.

               •     FFT {X} —

           FFT {X} is the FFT of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D FFT

       For 1D signals, the FFT VI computes the discrete Fourier transform (DFT) of the input
      sequence with a fast Fourier transform algorithm. The 1D DFT is defined as:

                          for n= 0, 1, 2, …, N–1

      where xis the input sequence, Nis the number of elements of x, and Yis the
       transform result.

      The frequency resolution, or the frequency spacing between the components of Y, is:


      where fs is the sampling frequency.

      The following table illustrates the pattern of the elements of FFT {X} for various FFT
        size and shift values, where Yis FFT {X} and nis the FFT size:

4884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4885 ordinal=4885 -->
## Functions

Functions


nis even (k= n/2)                 nis odd (k= (n-1)/2)

Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency

FALSE
        Y0          DC component           Y0          DC component
(default)


FALSE
        Y1          Δf                    Y1          Δf
(default)


FALSE
        Y2          2Δf                   Y2          2Δf
(default)


FALSE
        Y3          3Δf                   Y3          3Δf
(default)


⋮        ⋮             ⋮                       ⋮             ⋮


FALSE
         Yk–2          (k–2)Δf                 Yk–2          (k–2)Δf
(default)


FALSE
         Yk–1          (k–1)Δf                 Yk–1          (k–1)Δf
(default)


FALSE
      Yk            Nyquist Frequency      Yk         kΔf
(default)


                                                    © National Instruments 4885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4886 ordinal=4886 -->
## Functions

Functions

    nis even (k= n/2)                 nis odd (k= (n-1)/2)

          Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency

        FALSE
                 Yk+1          –(k–1)Δf                Yk+1         –kΔf
          (default)


        FALSE
                 Yk+2          –(k–2)Δf                Yk+2          –(k–1)Δf
          (default)


        ⋮        ⋮             ⋮                       ⋮             ⋮


        FALSE
                 Yn–3         –3Δf                    Yn–3         –3Δf
          (default)


        FALSE
                 Yn–2         –2Δf                    Yn–2         –2Δf
          (default)


        FALSE
                 Yn–1         –Δf                     Yn–1         –Δf
          (default)

       TRUE    Y0             –(Nyquist Frequency)      Y0          –kΔf
       TRUE    Y1            –(k–1)Δf               Y1            –(k–1)Δf
       TRUE    Y2            –(k–2)Δf               Y2            –(k–2)Δf
       TRUE    Y3            –(k–3)Δf               Y3            –(k–3)Δf

        ⋮        ⋮             ⋮                       ⋮             ⋮

       TRUE    Yk–2         –2Δf                    Yk–2         –2Δf
       TRUE    Yk–1         –Δf                     Yk–1         –Δf


4886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4887 ordinal=4887 -->
## Functions

Functions

nis even (k= n/2)                 nis odd (k= (n-1)/2)

 Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency
 TRUE   Yk         DC component         Yk         DC component
 TRUE    Yk+1        Δf                      Yk+1        Δf
 TRUE    Yk+2         2Δf                     Yk+2         2Δf

 ⋮        ⋮             ⋮                       ⋮             ⋮

 TRUE    Yn–3          (k–3)Δf                 Yn–3          (k–2)Δf
 TRUE    Yn–2          (k–2)Δf                 Yn–2          (k–1)Δf
 TRUE    Yn–1          (k–1)Δf                 Yn–1        kΔf

Related Information

Output Units for FFT-Based Vis

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

ComplexComplex FFTFFT VIVI

Computes the fast Fourier transform (FFT) of the input sequence X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —


                                                    © National Instruments 4887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4888 ordinal=4888 -->
## Functions

Functions


          X is the complex valued input sequence.

               •       shift? —

              shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

               •     FFT size —

           FFT size is the length of the FFT you want to perform.

                    If FFT size is greater than the number of elements in X, this VI adds zeros to the end of X to match
            the size of FFT size. If FFT size is less than the number of elements in X, this VI uses only the first
      nelements in X to perform the FFT, where nis FFT size. If FFT size is less than or equal to 0, this
              VI uses the length of X as the FFT size.

               •     FFT {X} —

           FFT {X} is the FFT of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D FFT

       For 1D signals, the FFT VI computes the discrete Fourier transform (DFT) of the input
      sequence with a fast Fourier transform algorithm. The 1D DFT is defined as:

                          for n= 0, 1, 2, …, N–1

      where xis the input sequence, Nis the number of elements of x, and Yis the
       transform result.

      The frequency resolution, or the frequency spacing between the components of Y, is:


      where fs is the sampling frequency.

4888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4889 ordinal=4889 -->
## Functions

Functions

The following table illustrates the pattern of the elements of FFT {X} for various FFT
size and shift values, where Yis FFT {X} and nis the FFT size:

nis even (k= n/2)                 nis odd (k= (n-1)/2)

 Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency

 FALSE
         Y0          DC component           Y0          DC component
 (default)


 FALSE
         Y1          Δf                    Y1          Δf
 (default)


 FALSE
         Y2          2Δf                   Y2          2Δf
 (default)


 FALSE
         Y3          3Δf                   Y3          3Δf
 (default)


 ⋮        ⋮             ⋮                       ⋮             ⋮


 FALSE
         Yk–2          (k–2)Δf                 Yk–2          (k–2)Δf
 (default)


 FALSE
         Yk–1          (k–1)Δf                 Yk–1          (k–1)Δf
 (default)


 FALSE   Yk            Nyquist Frequency      Yk         kΔf


                                                    © National Instruments 4889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4890 ordinal=4890 -->
## Functions

Functions

    nis even (k= n/2)                 nis odd (k= (n-1)/2)

          Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency

          (default)


        FALSE
                 Yk+1          –(k–1)Δf                Yk+1         –kΔf
          (default)


        FALSE
                 Yk+2          –(k–2)Δf                Yk+2          –(k–1)Δf
          (default)


        ⋮        ⋮             ⋮                       ⋮             ⋮


        FALSE
                 Yn–3         –3Δf                    Yn–3         –3Δf
          (default)


        FALSE
                 Yn–2         –2Δf                    Yn–2         –2Δf
          (default)


        FALSE
                 Yn–1         –Δf                     Yn–1         –Δf
          (default)

       TRUE    Y0             –(Nyquist Frequency)      Y0          –kΔf
       TRUE    Y1            –(k–1)Δf               Y1            –(k–1)Δf
       TRUE    Y2            –(k–2)Δf               Y2            –(k–2)Δf
       TRUE    Y3            –(k–3)Δf               Y3            –(k–3)Δf

        ⋮        ⋮             ⋮                       ⋮             ⋮


4890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4891 ordinal=4891 -->
## Functions

Functions

nis even (k= n/2)                 nis odd (k= (n-1)/2)

 Shift     Array Element  Corresponding Frequency  Array Element  Corresponding Frequency
 TRUE    Yk–2         –2Δf                    Yk–2         –2Δf
 TRUE    Yk–1         –Δf                     Yk–1         –Δf
 TRUE   Yk         DC component         Yk         DC component
 TRUE    Yk+1        Δf                      Yk+1        Δf
 TRUE    Yk+2         2Δf                     Yk+2         2Δf

 ⋮        ⋮             ⋮                       ⋮             ⋮

 TRUE    Yn–3          (k–3)Δf                 Yn–3          (k–2)Δf
 TRUE    Yn–2          (k–2)Δf                 Yn–2          (k–1)Δf
 TRUE    Yn–1          (k–1)Δf                 Yn–1        kΔf

Related Information

Output Units for FFT-Based Vis

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

2D2D RealReal FFTFFT VIVI

Computes the fast Fourier transform (FFT) of the input sequence X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4892 ordinal=4892 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is the real input sequence.

               •       shift? —

              shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

               •   m —

       m specifies the number of rows of the 2D FFT. This VI truncates or zero-pads X to an m-by-n array
            before performing the FFT.

               •     n —

          n specifies the number of columns of the 2D FFT. This VI truncates or zero-pads X to an m-by-n
             array before performing the FFT.

               •     FFT {X} —

           FFT {X} is the 2D FFT of X.

                    If the input signal is in volts (V), FFT {X} has units of volts. If the input signal is not in volts, FFT {X}
           has units of the input signal unit. This VI returns the phase in radians.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D FFT

       For 2D signals, the FFT VI computes the discrete Fourier transform (DFT) of the input
       matrix. This VI performs a 1D FFT on the rows of the input matrix and then performs a
      1D FFT on the columns of the output of the preceding step. The DFT of an M-by-N
       matrix is defined as:

                                             for u= 0, 1, …, M–1, v=0, 1, …, N–1


4892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4893 ordinal=4893 -->
## Functions

Functions

where xis the input matrix and Yis the transform result.

The illustration below shows the effect of shift? on the 2D FFT result:


 2D input signals                FFT without shift               FFT with shift


Related Information

Output Units for FFT-Based Vis

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

2D2D ComplexComplex FFTFFT VIVI

Computes the fast Fourier transform (FFT) of the input sequence X. Wire data to the X
input to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4894 ordinal=4894 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •       shift? —

              shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

               •   m —

       m specifies the number of rows of the 2D FFT. This VI truncates or zero-pads X to an m-by-n array
            before performing the FFT.

               •     n —

          n specifies the number of columns of the 2D FFT. This VI truncates or zero-pads X to an m-by-n
             array before performing the FFT.

               •     FFT {X} —

           FFT {X} is the 2D FFT of X.

                    If the input signal is in volts (V), FFT {X} has units of volts. If the input signal is not in volts, FFT {X}
           has units of the input signal unit. This VI returns the phase in radians.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D FFT

       For 2D signals, the FFT VI computes the discrete Fourier transform (DFT) of the input
       matrix. This VI performs a 1D FFT on the rows of the input matrix and then performs a
      1D FFT on the columns of the output of the preceding step. The DFT of an M-by-N
       matrix is defined as:

                                             for u= 0, 1, …, M–1, v=0, 1, …, N–1


4894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4895 ordinal=4895 -->
## Functions

Functions

where xis the input matrix and Yis the transform result.

The illustration below shows the effect of shift? on the 2D FFT result:


 2D input signals                FFT without shift               FFT with shift


Related Information

Output Units for FFT-Based Vis

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\FFT and
   Power Spectrum Units.vi

FastFast HilbertHilbert TransformTransform

Computes the fast Hilbert transform of the input sequence X.


Inputs/Outputs

   •     X —


                                                    © National Instruments 4895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4896 ordinal=4896 -->
## Functions

Functions


          X specifies the number of elements in the data array.

               •       Hilbert{X} —

             Hilbert{X} is the fast Hilbert transform of the input sequence.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Hilbert transform of a function x(t) is defined as

                                              .

       Using Fourier identities, you can show the Fourier transform of the Hilbert transform of
       x(t) is

       h(t) ⇔ H(f) = - jsgn(f) X(f),

      where x(t) ⇔ X(f) is a Fourier transform pair and


      The Fast Hilbert Transform VI performs the discrete implementation of the Hilbert
       transform with the aid of the FFT routines based upon the h(t) ⇔ H(f) Fourier
       transform pair by taking the following steps.

         1. Fourier transform the input sequence X

     Y= F{X}

         2. Set the DC component to zero

         Y0 = 0.0


4896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4897 ordinal=4897 -->
## Functions

Functions

 3.  If the sequence Yis an even size, set the Nyquist component to zero

   YNyq = 0

 4. Multiply the positive harmonics by -j.

 5. Multiply the negative harmonics by j. Call the new sequence H, which is of the
   form

  Hk = –jsgn(k)Yk

 6. Inverse Fourier transform Hto obtain the Hilbert transform of X.

Refer to the output format of the Complex FFT instance of the FFT VI for more
information.

You use the Hilbert transform to extract instantaneous phase information and obtain
the single-sideband spectra, obtain the envelope of an oscillating signal, detect
echoes, and reduce sampling rates.

The output sequence Y= InverseFFT[X] is complex and it is returned in one
complex array: Y= (Yre,Yim).

      Note Because the Fast Hilbert Transform VI sets the DC and Nyquist
      components to zero when the number of elements in the input sequence is
       even, you cannot always recover the original signal with an inverse Hilbert
        transform. The Hilbert transform works well with bandpass limited signals,
       which exclude the DC and the Nyquist components.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\Echo
   Detector.vi


                                                    © National Instruments 4897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4898 ordinal=4898 -->
## Functions

Functions

    FHTFHT

      Computes the fast Hartley transform (FHT) of the input sequence X.

      The number of elements in the input sequence X must be a valid power of two.


      Inputs/Outputs

               •     X —

          X is the input sequence and must be a valid power of 2.

           To properly compute the FHT of X, the number of elements, n, in the sequence must be a valid
          power of 2. n = 2m for m = 1, 2, 3, …, 23

                    If the number of elements in X is not a valid power of 2, the VI sets Hartley{X} to an empty array
          and returns an error.

               •      Hartley {X} —

            Hartley {X} is the Hartley transform of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Hartley transform of a function x(t) is defined as

                                          ,

      where cas(x) = cos(x) + sin(x).

           If Yrepresents the output sequence Hartley{X} obtained by the FHT, then Yis obtained
      through the discrete implementation of the Hartley integral


4898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4899 ordinal=4899 -->
## Functions

Functions


for k= 1, 2, …, n-1,

where nis the number of elements in X.

The Hartley transform maps real-valued sequences into real-valued frequency domain
sequences. You can use it instead of the Fourier transform to convolve signals,
deconvolve signals, correlate signals, and find the power spectrum. You also can
derive the Fourier transform from the Hartley transform.

When the sequences to be processed are real-valued sequences, the Fourier transform
produces complex-valued sequences in which half of the information is redundant.
The advantage of using the Hartley transform instead of the Fourier transform is that
the Hartley transform uses half the memory to produce the same information the FFT
produces. Further, the FHT is calculated in place and is as efficient as the Fourier
transform. The disadvantage of the FHT is that the size of the input sequence must be
a valid power of 2.

WaveletWavelet TransformTransform Daubechies4Daubechies4

Computes the wavelet transform based on the Daubechies4 function of the input
sequence X.


Inputs/Outputs

   •     X —

    X is the samples of the input signal.

    The length of the signal has to be a power of 2, otherwise an error code is given.

   •      Wavelet Daubechies4 {X} —


                                                    © National Instruments 4899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4900 ordinal=4900 -->
## Functions

Functions


           Wavelet Daubechies4 {X} returns the calculated wavelet Daubechies4 transform.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Wavelet Transform Daubechies4 transform can be defined using the
       transformation matrix


                                                                             .


      Here blank entries signify zeros. The numbers c0, c1, c2, and c3 have to fulfill certain
       orthogonal properties

       c0² + c1² + c2² + c3² = 1 c2c0 + c3c1 = 0 c3 – c2 + c1 – c0 = 0 0c3 – 1c2 + 2c1 – 3c0 = 0

       with the unique solution


                            .


           Note You can solve the previous system of nonlinear equations in c0, c1, c2,
            and c3 directly with the nD Nonlinear System Single Solution VI of this
              package.


4900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4901 ordinal=4901 -->
## Functions

Functions

The Wavelet Daubechies4 transform of the array X is defined by

Wavelet Daubechies4{X} = C* X

WalshWalsh HadamardHadamard

Computes the real Walsh Hadamard transform of the input sequence X.


Inputs/Outputs

   •     X —

    X is an array of power of two length.

   •      Walsh Hadamard {X} —

    Walsh Hadamard {X} returns the Walsh Hadamard transform of X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


      Note The Walsh Hadamard transform has similar properties to the more
       well-known Fourier transform, but the computational effort is considerably
        smaller.

The Walsh Hadamard transform is based on an orthogonal system consisting of
functions of only two elements –1 and 1. For the special case of n= 4, the Walsh
Hadamard transform of the signal

X = {x0, x1, x2, x3}

can be noted in the following matrix form


                                                    © National Instruments 4901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4902 ordinal=4902 -->
## Functions

Functions


                                                .


                                                                                           + 1           If WHn and WHn+ 1 denote the Walsh Hadamard matrices of dimension 2n and 2n
        respectively, the rule is

                                           ,

      where –WHn is meant in the element wise sense.

           Note The Walsh Hadamard transform fulfills the Convolution Theorem:
           WH{X*Y} = WH{X}WH{Y}.

      The following diagram shows the Walsh Hadamard transform of a pulse pattern signal
       of length 256, delay 32, and width 64.


    DCTDCT

      Computes the Discrete Cosine Transform (DCT) of the input sequence X. Wire data to
       the X input to determine the polymorphic instance to use or manually select the
       instance.


4902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4903 ordinal=4903 -->
## Functions

Functions

   • 1D DCT VI
   • 2D DCT VI

1D DCT

The one-dimensional Discrete Cosine Transform DCT {X} of a sequence X is defined by
the following equations:


and


where Nis the length of X,

xn is the nth element of X, yk is the kth element of DCT {X}.

This VI applies a fast DCT algorithm instead of calculating the Discrete Cosine
Transform directly. LabVIEW implements this fast DCT algorithm using an FFT
technique.

2D DCT

The two-dimensional Discrete Cosine Transform DCT {X} of a matrix X is defined by the
following equation:


where Mand Nare the number of rows and columns, respectively, of the input matrix
X,

x(m,n)is the element of X with row number mand column number n, y(u,v)is the
element of DCT {X} with row number uand column number v.


                                                    © National Instruments 4903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4904 ordinal=4904 -->
## Functions

Functions

       This VI performs a two-dimensional DCT using the following two steps:

         1. Perform a one-dimensional DCT row-by-row on the input matrix X. The output is
           Y'.
         2. Perform a one-dimensional DCT column-by-column on Y'. The output is DCT {X}.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Transforms\Image
        Compression with DCT.vi

     1D1D DCTDCT VIVI

      Computes the Discrete Cosine Transform (DCT) of the input sequence X. Wire data to
       the X input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •     DCT size —

         DCT size is the length of the DCT you want to perform.

                    If DCT size is greater than the number of elements in X, this VI adds zeros to the end of X to
          match the size of DCT size. If DCT size is less than the number of elements in X, this VI uses only
            the leading DCT size elements in X to perform the DCT. If DCT size is less than or equal to zero,
              this VI uses the length of X as the DCT size.

               •     DCT {X} —


4904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4905 ordinal=4905 -->
## Functions

Functions


   DCT {X} is the DCT of X.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D DCT

The one-dimensional Discrete Cosine Transform DCT {X} of a sequence X is defined by
the following equations:


and


where Nis the length of X,

xn is the nth element of X, yk is the kth element of DCT {X}.

This VI applies a fast DCT algorithm instead of calculating the Discrete Cosine
Transform directly. LabVIEW implements this fast DCT algorithm using an FFT
technique.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Transforms\Image
   Compression with DCT.vi


                                                    © National Instruments 4905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4906 ordinal=4906 -->
## Functions

Functions

     2D2D DCTDCT VIVI

      Computes the Discrete Cosine Transform (DCT) of the input sequence X. Wire data to
       the X input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •     X —

          X is the real input sequence.

               •     DCT {X} —

         DCT {X} is the DCT of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D DCT

      The two-dimensional Discrete Cosine Transform DCT {X} of a matrix X is defined by the
       following equation:


      where Mand Nare the number of rows and columns, respectively, of the input matrix
        X,

     x(m,n)is the element of X with row number mand column number n, y(u,v)is the
      element of DCT {X} with row number uand column number v.


4906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4907 ordinal=4907 -->
## Functions

Functions

This VI performs a two-dimensional DCT using the following two steps:

 1. Perform a one-dimensional DCT row-by-row on the input matrix X. The output is
    Y'.
 2. Perform a one-dimensional DCT column-by-column on Y'. The output is DCT {X}.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\Image
   Compression with DCT.vi

DSTDST

Computes the Discrete Sine Transform (DST) of the input sequence X. Wire data to the
X input to determine the polymorphic instance to use or manually select the instance.


  • 1D DST VI
  • 2D DST VI

1D DST

The one-dimensional Discrete Sine Transform DST {X} of a sequence X is defined as:

                                   , k=0, 1, 2, …, N–1

where Nis the length of the input sequence X, xn is the nth element of the input
sequence X, and yk is the kth element of the output sequence DST {X}. This VI applies a
fast DST algorithm instead of calculating the Discrete Sine Transform directly. LabVIEW
implements this fast DST algorithm using an FFT-based technique.


                                                    © National Instruments 4907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4908 ordinal=4908 -->
## Functions

Functions

     2D DST

      The two-dimensional Discrete Sine Transform DST {X} of a matrix X is defined as:


      where Mand Nare the number of rows and columns, respectively, of the input matrix
        X. x(m,n) is the element of the input matrix X with row number mand column number
      n. y(u,v) is the element of the output matrix DST {X} with row number uand column
      number v. This VI performs a two-dimensional DST using the following two steps:

         1. Perform a one-dimensional DST row-by-row on the input matrix X. The output is
           Y'.
         2. Perform a one-dimensional DST column-by-column on Y'. The output is DST {X}.

     1D1D DSTDST VIVI

      Computes the Discrete Sine Transform (DST) of the input sequence X. Wire data to the
      X input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is a real vector.

               •     DST size —

          DST size is the length of the DST you want to perform.

                    If DST size is greater than the number of elements in X, this VI adds zeros to the end of X to
          match the size of DST size. If DST size is less than the number of elements in X, this VI uses only
            the leading DST size elements in X to perform the DST. If DST size is less than or equal to zero,
              this VI uses the length of X as the DST size.


4908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4909 ordinal=4909 -->
## Functions

Functions

   •     DST {X} —

   DST {X} is the DST of X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D DST

The one-dimensional Discrete Sine Transform DST {X} of a sequence X is defined as:

                                   , k=0, 1, 2, …, N–1

where Nis the length of the input sequence X, xn is the nth element of the input
sequence X, and yk is the kth element of the output sequence DST {X}. This VI applies a
fast DST algorithm instead of calculating the Discrete Sine Transform directly. LabVIEW
implements this fast DST algorithm using an FFT-based technique.

2D2D DSTDST VIVI

Computes the Discrete Sine Transform (DST) of the input sequence X. Wire data to the
X input to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the real input sequence.

   •     DST {X} —

   DST {X} is the DST of X.


                                                    © National Instruments 4909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4910 ordinal=4910 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D DST

      The two-dimensional Discrete Sine Transform DST {X} of a matrix X is defined as:


      where Mand Nare the number of rows and columns, respectively, of the input matrix
        X. x(m,n) is the element of the input matrix X with row number mand column number
      n. y(u,v) is the element of the output matrix DST {X} with row number uand column
      number v. This VI performs a two-dimensional DST using the following two steps:

         1. Perform a one-dimensional DST row-by-row on the input matrix X. The output is
           Y'.
         2. Perform a one-dimensional DST column-by-column on Y'. The output is DST {X}.

      ChirpChirp ZZ TransformTransform

      Computes the Chirp-Z transform of the input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.

      The Chirp-Z transform algorithm is also known as Bluestein's FFT algorithm.


            • Chirp Z Transform (DBL) VI
            • Chirp Z Transform (CDB) VI

      The Chirp Z Transform VI evaluates the z transform along a spiral in the z-plane at the
       following points:


4910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4911 ordinal=4911 -->
## Functions

Functions

zk=AW-k

for k= 0, 1, …, M–1

where Mis the # of bins, Ais the starting point, and Wis the increment.

The following illustration shows samples in the z-plane.


Set Aand Was follows:

A= 1 W=

where Nis the length of X. Let Mequal N. When Msamples are evenly distributed on
the unit circle, as shown in the following front panel, the Chirp-Z transform is the same
as the fast Fourier transform (FFT).


                                                    © National Instruments 4911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4912 ordinal=4912 -->
## Functions

Functions


      You also can use the Chirp-Z transform to calculate the partial FFT result. Set Aand W
       as follows:

   A=  W=

      where sis the start bin and Nis the length of X. This is useful when you are interested
        in only a small portion of a spectrum of a very long signal, as shown in the following
       front panel.


      You can use either the direct form method or the frequency domain method to
       calculate the Chirp-Z transform.

      Direct Form Method

      The direct form method computes the Chirp-Z transform as follows:


4912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4913 ordinal=4913 -->
## Functions

Functions


for k= 0, 1, …, M–1

where Nis the length of X.

Frequency Domain Method

The direct form can be reformulated with the convolution between gi and W-i²/2 as
follows:


where gi=xiA-iW-i²/2. You can perform the convolution operation using an FFT-based
technique.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\Spectrum
   using Chirp Z Transform.vi

ChirpChirp ZZ TransformTransform (DBL)(DBL) VIVI

Computes the Chirp-Z transform of the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.

The Chirp-Z transform algorithm is also known as Bluestein's FFT algorithm.


                                                    © National Instruments 4913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4914 ordinal=4914 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is a real vector.

               •      # of bins —

           # of bins determines the length of Chirp-Z {X}. If # of bins is less than or equal to 0, this VI sets #
             of bins to the length of X.

               •       starting point —

             starting point is the point at which to begin evaluating the Chirp-Z transform and is best
            described by the equation in the details section. If starting point is 0, the VI returns an error.

               •      increment —

           increment is the increment between each point to evaluate for the Chirp-Z transform.
           increment cannot be 0.

               •      algorithm —

            algorithm specifies the transform method to use. When algorithm is direct, this VI computes the
            Chirp-Z transform using the direct form method. When algorithm is frequency domain, this VI
           computes the Chirp-Z transform using an FFT-based technique.

                    If the size of X or the # of bins is small, the direct method is faster. If the size of X or the # of bins
                is large, the frequency domain method is faster.

               •      Chirp-Z {X} —

            Chirp-Z {X} is the Chirp-Z transform of the input sequence X. # of bins determines the length of
            Chirp-Z {X}. If # of bins is less than or equal to 0, Chirp-Z {X} has the same length as X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Chirp Z Transform VI evaluates the z transform along a spiral in the z-plane at the
       following points:


4914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4915 ordinal=4915 -->
## Functions

Functions

zk=AW-k

for k= 0, 1, …, M–1

where Mis the # of bins, Ais the starting point, and Wis the increment.

The following illustration shows samples in the z-plane.


Set Aand Was follows:

A= 1 W=

where Nis the length of X. Let Mequal N. When Msamples are evenly distributed on
the unit circle, as shown in the following front panel, the Chirp-Z transform is the same
as the fast Fourier transform (FFT).


                                                    © National Instruments 4915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4916 ordinal=4916 -->
## Functions

Functions


      You also can use the Chirp-Z transform to calculate the partial FFT result. Set Aand W
       as follows:

   A=  W=

      where sis the start bin and Nis the length of X. This is useful when you are interested
        in only a small portion of a spectrum of a very long signal, as shown in the following
       front panel.


      You can use either the direct form method or the frequency domain method to
       calculate the Chirp-Z transform.

      Direct Form Method

      The direct form method computes the Chirp-Z transform as follows:


4916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4917 ordinal=4917 -->
## Functions

Functions


for k= 0, 1, …, M–1

where Nis the length of X.

Frequency Domain Method

The direct form can be reformulated with the convolution between gi and W-i²/2 as
follows:


where gi=xiA-iW-i²/2. You can perform the convolution operation using an FFT-based
technique.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\Spectrum
   using Chirp Z Transform.vi

ChirpChirp ZZ TransformTransform (CDB)(CDB) VIVI

Computes the Chirp-Z transform of the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.

The Chirp-Z transform algorithm is also known as Bluestein's FFT algorithm.


                                                    © National Instruments 4917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4918 ordinal=4918 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •      # of bins —

           # of bins determines the length of Chirp-Z {X}. If # of bins is less than or equal to 0, this VI sets #
             of bins to the length of X.

               •       starting point —

             starting point is the point at which to begin evaluating the Chirp-Z transform and is best
            described by the equation in the details section. If starting point is 0, the VI returns an error.

               •      increment —

           increment is the increment between each point to evaluate for the Chirp-Z transform.
           increment cannot be 0.

               •      algorithm —

            algorithm specifies the transform method to use. When algorithm is direct, this VI computes the
            Chirp-Z transform using the direct form method. When algorithm is frequency domain, this VI
           computes the Chirp-Z transform using an FFT-based technique.

                    If the size of X or the # of bins is small, the direct method is faster. If the size of X or the # of bins
                is large, the frequency domain method is faster.

               •      Chirp-Z {X} —

            Chirp-Z {X} is the Chirp-Z transform of the input sequence X. # of bins determines the length of
            Chirp-Z {X}. If # of bins is less than or equal to 0, Chirp-Z {X} has the same length as X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Chirp Z Transform VI evaluates the z transform along a spiral in the z-plane at the
       following points:


4918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4919 ordinal=4919 -->
## Functions

Functions

zk=AW-k

for k= 0, 1, …, M–1

where Mis the # of bins, Ais the starting point, and Wis the increment.

The following illustration shows samples in the z-plane.


Set Aand Was follows:

A= 1 W=

where Nis the length of X. Let Mequal N. When Msamples are evenly distributed on
the unit circle, as shown in the following front panel, the Chirp-Z transform is the same
as the fast Fourier transform (FFT).


                                                    © National Instruments 4919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4920 ordinal=4920 -->
## Functions

Functions


      You also can use the Chirp-Z transform to calculate the partial FFT result. Set Aand W
       as follows:

   A=  W=

      where sis the start bin and Nis the length of X. This is useful when you are interested
        in only a small portion of a spectrum of a very long signal, as shown in the following
       front panel.


      You can use either the direct form method or the frequency domain method to
       calculate the Chirp-Z transform.

      Direct Form Method

      The direct form method computes the Chirp-Z transform as follows:


4920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4921 ordinal=4921 -->
## Functions

Functions


for k= 0, 1, …, M–1

where Nis the length of X.

Frequency Domain Method

The direct form can be reformulated with the convolution between gi and W-i²/2 as
follows:


where gi=xiA-iW-i²/2. You can perform the convolution operation using an FFT-based
technique.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Transforms\Spectrum
   using Chirp Z Transform.vi

LaplaceLaplace TransformTransform RealReal

Computes the real Laplace transform of the input sequence X.


Inputs/Outputs

   •     X —

    X is the array describing the evenly sampled time signal.


                                                    © National Instruments 4921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4922 ordinal=4922 -->
## Functions

Functions


          The first element of this array belongs to t= 0, the last to t= end.

               •     end —

          end is the instant in time of the last sample.

          The entire sample interval is between 0 and end.

               •      Laplace {X} —

            Laplace {X} is the result of the Laplace transform as an array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The real Laplace transform of a real signal x(s)is defined by


        for s≥ 0 and sreal.

      Here x(t) is defined for all: t≥ 0.

      The discrete version of the Laplace transform of a discretely and evenly-sampled
       signal is a generation of the above continuous version.

      The definition of the Laplace transform is not of much use if the time signal increases
       rapidly with the time. The discrete version of the Laplace transform cannot fully detect
       the convergence behavior of the original definition.

      The discrete version of the Laplace transform is computationally expensive. An
        efficient strategy for the discrete Laplace transform is based on the fast fractional
       Fourier transform (FFFT). The definition of the FFFT is


4922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4923 ordinal=4923 -->
## Functions

Functions

with an arbitrarily chosen complex α.

The following diagram shows the real Laplace transform of the function f(t) = sin(t) in
the interval (0, 6). This is entered on the front panel as end 6.00 and X values of sin(t)
for 0 ≤ t≤ 6.


InverseInverse FFTFFT

Computes the inverse discrete Fourier transform (IDFT) of the input sequence FFT {X}.
You must manually select the polymorphic instance you want to use.


  • Inverse Real FFT VI
  • Inverse Complex FFT VI
  • 2D Inverse Real FFT VI
  • 2D Inverse Complex FFT VI

Use the Inverse Real FFT and the 2D Inverse Real FFT instances of this VI only if FFT {X}
is the Fourier transform of a real time-domain signal. Otherwise, use the Inverse
Complex FFT and the 2D Inverse Complex FFT instances. When FFT {X} is the Fourier
transform of a real time-domain signal, FFT {X} is conjugated centrosymmetric, and
the Inverse Real FFT and the 2D Inverse Real FFT instances use only the anterior part of
FFT{X}.

The following formulas show the conjugated centrosymmetric property of FFT {X}

                                                    © National Instruments 4923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4924 ordinal=4924 -->
## Functions

Functions

     when FFT {X} is the Fourier transform of a real time-domain signal and shift? is false.

         1. When FFT {X} is the Fourier transform of a 1D real time-domain signal with length
         N, the posterior half part of FFT {X} can be constructed by the anterior half part.
         The centrosymmetric relationship between the anterior and posterior half part of
         FFT {X} can be written as

                                                   ,

         where fi is the element in FFT {X}.

         The Inverse Real FFT instance VI uses only the anterior half part, from f0 to f_   to
          perform the inverse real FFT, where  means the floor operation.

         2. When FFT {X} is the Fourier transform of a 2D real time-domain signal with Mrows
         and Ncolumns, the lower half part of FFT {X} can be constructed by the upper half
            part. The centrosymmetric relationship between the upper and lower half part of
         FFT {X} can be written as


         where fi,j is the element in FFT {X}.

         The 2D Inverse Real FFT instance uses only the upper half part, from f0,0 to f_
           to perform the 2D inverse real FFT, where  means the floor operation.

       This VI computes the inverse discrete Fourier transform (IDFT) of a vector or matrix FFT
        {X} with a fast Fourier transform algorithm. The shift? input specifies whether the input
      FFT {X} is a DC-centered FFT.

       For a 1D, N-sample, frequency domain sequence Y, the IDFT is defined as:


4924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4925 ordinal=4925 -->
## Functions

Functions

for n= 0, 1, 2, …, N–1.

For a 2D, M-by-Nfrequency domain array Y, the IDFT is defined as:


for m= 0, 1, …, M–1, n=0, 1, …, N–1.

InverseInverse RealReal FFTFFT VIVI

Computes the inverse discrete Fourier transform (IDFT) of the input sequence FFT {X}.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •     FFT {X} —

    FFT {X} is the complex valued input sequence, which should be conjugated centrosymmetric
    except for the first element. This instance uses only the anterior half of FFT {X}.

   •       shift? —

     shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

   •     X —

    X is the inverse real FFT of FFT{X}.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Use the Inverse Real FFT and the 2D Inverse Real FFT instances of this VI only if FFT {X}
is the Fourier transform of a real time-domain signal. Otherwise, use the Inverse

                                                    © National Instruments 4925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4926 ordinal=4926 -->
## Functions

Functions

      Complex FFT and the 2D Inverse Complex FFT instances. When FFT {X} is the Fourier
       transform of a real time-domain signal, FFT {X} is conjugated centrosymmetric, and
       the Inverse Real FFT and the 2D Inverse Real FFT instances use only the anterior part of
       FFT{X}.

      The following formulas show the conjugated centrosymmetric property of FFT {X}
     when FFT {X} is the Fourier transform of a real time-domain signal and shift? is false.

         1. When FFT {X} is the Fourier transform of a 1D real time-domain signal with length
         N, the posterior half part of FFT {X} can be constructed by the anterior half part.
         The centrosymmetric relationship between the anterior and posterior half part of
         FFT {X} can be written as

                                                   ,

         where fi is the element in FFT {X}.

         The Inverse Real FFT instance VI uses only the anterior half part, from f0 to f_   to
          perform the inverse real FFT, where  means the floor operation.

         2. When FFT {X} is the Fourier transform of a 2D real time-domain signal with Mrows
         and Ncolumns, the lower half part of FFT {X} can be constructed by the upper half
            part. The centrosymmetric relationship between the upper and lower half part of
         FFT {X} can be written as


         where fi,j is the element in FFT {X}.

         The 2D Inverse Real FFT instance uses only the upper half part, from f0,0 to f_
           to perform the 2D inverse real FFT, where  means the floor operation.

       This VI computes the inverse discrete Fourier transform (IDFT) of a vector or matrix FFT
        {X} with a fast Fourier transform algorithm. The shift? input specifies whether the input


4926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4927 ordinal=4927 -->
## Functions

Functions

FFT {X} is a DC-centered FFT.

For a 1D, N-sample, frequency domain sequence Y, the IDFT is defined as:


for n= 0, 1, 2, …, N–1.

For a 2D, M-by-Nfrequency domain array Y, the IDFT is defined as:


for m= 0, 1, …, M–1, n=0, 1, …, N–1.

InverseInverse ComplexComplex FFTFFT VIVI

Computes the inverse discrete Fourier transform (IDFT) of the input sequence FFT {X}.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •     FFT {X} —

    FFT {X} is the complex valued input sequence.

   •       shift? —

     shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

   •     X —

    X is the inverse complex FFT of FFT{X}.

   •       error —


                                                    © National Instruments 4927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4928 ordinal=4928 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Use the Inverse Real FFT and the 2D Inverse Real FFT instances of this VI only if FFT {X}
         is the Fourier transform of a real time-domain signal. Otherwise, use the Inverse
      Complex FFT and the 2D Inverse Complex FFT instances. When FFT {X} is the Fourier
       transform of a real time-domain signal, FFT {X} is conjugated centrosymmetric, and
       the Inverse Real FFT and the 2D Inverse Real FFT instances use only the anterior part of
       FFT{X}.

      The following formulas show the conjugated centrosymmetric property of FFT {X}
     when FFT {X} is the Fourier transform of a real time-domain signal and shift? is false.

         1. When FFT {X} is the Fourier transform of a 1D real time-domain signal with length
         N, the posterior half part of FFT {X} can be constructed by the anterior half part.
         The centrosymmetric relationship between the anterior and posterior half part of
         FFT {X} can be written as

                                                   ,

         where fi is the element in FFT {X}.

         The Inverse Real FFT instance VI uses only the anterior half part, from f0 to f_   to
          perform the inverse real FFT, where  means the floor operation.

         2. When FFT {X} is the Fourier transform of a 2D real time-domain signal with Mrows
         and Ncolumns, the lower half part of FFT {X} can be constructed by the upper half
            part. The centrosymmetric relationship between the upper and lower half part of
         FFT {X} can be written as


         where fi,j is the element in FFT {X}.

4928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4929 ordinal=4929 -->
## Functions

Functions

   The 2D Inverse Real FFT instance uses only the upper half part, from f0,0 to f_
    to perform the 2D inverse real FFT, where  means the floor operation.

This VI computes the inverse discrete Fourier transform (IDFT) of a vector or matrix FFT
{X} with a fast Fourier transform algorithm. The shift? input specifies whether the input
FFT {X} is a DC-centered FFT.

For a 1D, N-sample, frequency domain sequence Y, the IDFT is defined as:


for n= 0, 1, 2, …, N–1.

For a 2D, M-by-Nfrequency domain array Y, the IDFT is defined as:


for m= 0, 1, …, M–1, n=0, 1, …, N–1.

2D2D InverseInverse RealReal FFTFFT VIVI

Computes the inverse discrete Fourier transform (IDFT) of the input sequence FFT {X}.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •     FFT {X} —

    FFT {X} is the complex valued input sequence, which should be conjugated centrosymmetric
    except for the first row and column. This instance uses only the upper half of FFT {X}.

   •       shift? —


                                                    © National Instruments 4929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4930 ordinal=4930 -->
## Functions

Functions


              shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

               •     X —

          X is the inverse real FFT of FFT{X}.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Use the Inverse Real FFT and the 2D Inverse Real FFT instances of this VI only if FFT {X}
         is the Fourier transform of a real time-domain signal. Otherwise, use the Inverse
      Complex FFT and the 2D Inverse Complex FFT instances. When FFT {X} is the Fourier
       transform of a real time-domain signal, FFT {X} is conjugated centrosymmetric, and
       the Inverse Real FFT and the 2D Inverse Real FFT instances use only the anterior part of
       FFT{X}.

      The following formulas show the conjugated centrosymmetric property of FFT {X}
     when FFT {X} is the Fourier transform of a real time-domain signal and shift? is false.

         1. When FFT {X} is the Fourier transform of a 1D real time-domain signal with length
         N, the posterior half part of FFT {X} can be constructed by the anterior half part.
         The centrosymmetric relationship between the anterior and posterior half part of
         FFT {X} can be written as

                                                   ,

         where fi is the element in FFT {X}.

         The Inverse Real FFT instance VI uses only the anterior half part, from f0 to f_   to
          perform the inverse real FFT, where  means the floor operation.

         2. When FFT {X} is the Fourier transform of a 2D real time-domain signal with Mrows
         and Ncolumns, the lower half part of FFT {X} can be constructed by the upper half
            part. The centrosymmetric relationship between the upper and lower half part of
         FFT {X} can be written as

4930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4931 ordinal=4931 -->
## Functions

Functions


   where fi,j is the element in FFT {X}.

   The 2D Inverse Real FFT instance uses only the upper half part, from f0,0 to f_
    to perform the 2D inverse real FFT, where  means the floor operation.

This VI computes the inverse discrete Fourier transform (IDFT) of a vector or matrix FFT
{X} with a fast Fourier transform algorithm. The shift? input specifies whether the input
FFT {X} is a DC-centered FFT.

For a 1D, N-sample, frequency domain sequence Y, the IDFT is defined as:


for n= 0, 1, 2, …, N–1.

For a 2D, M-by-Nfrequency domain array Y, the IDFT is defined as:


for m= 0, 1, …, M–1, n=0, 1, …, N–1.

2D2D InverseInverse ComplexComplex FFTFFT VIVI

Computes the inverse discrete Fourier transform (IDFT) of the input sequence FFT {X}.
You must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •     FFT {x} —

                                                    © National Instruments 4931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4932 ordinal=4932 -->
## Functions

Functions


           FFT {X} is the complex valued input sequence.

               •       shift? —

              shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE.

               •     X —

          X is the inverse complex FFT of FFT {X}.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Use the Inverse Real FFT and the 2D Inverse Real FFT instances of this VI only if FFT {X}
         is the Fourier transform of a real time-domain signal. Otherwise, use the Inverse
      Complex FFT and the 2D Inverse Complex FFT instances. When FFT {X} is the Fourier
       transform of a real time-domain signal, FFT {X} is conjugated centrosymmetric, and
       the Inverse Real FFT and the 2D Inverse Real FFT instances use only the anterior part of
       FFT{X}.

      The following formulas show the conjugated centrosymmetric property of FFT {X}
     when FFT {X} is the Fourier transform of a real time-domain signal and shift? is false.

         1. When FFT {X} is the Fourier transform of a 1D real time-domain signal with length
         N, the posterior half part of FFT {X} can be constructed by the anterior half part.
         The centrosymmetric relationship between the anterior and posterior half part of
         FFT {X} can be written as

                                                   ,

         where fi is the element in FFT {X}.

         The Inverse Real FFT instance VI uses only the anterior half part, from f0 to f_   to
          perform the inverse real FFT, where  means the floor operation.

         2. When FFT {X} is the Fourier transform of a 2D real time-domain signal with Mrows

4932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4933 ordinal=4933 -->
## Functions

Functions

   and Ncolumns, the lower half part of FFT {X} can be constructed by the upper half
    part. The centrosymmetric relationship between the upper and lower half part of
   FFT {X} can be written as


   where fi,j is the element in FFT {X}.

   The 2D Inverse Real FFT instance uses only the upper half part, from f0,0 to f_
    to perform the 2D inverse real FFT, where  means the floor operation.

This VI computes the inverse discrete Fourier transform (IDFT) of a vector or matrix FFT
{X} with a fast Fourier transform algorithm. The shift? input specifies whether the input
FFT {X} is a DC-centered FFT.

For a 1D, N-sample, frequency domain sequence Y, the IDFT is defined as:


for n= 0, 1, 2, …, N–1.

For a 2D, M-by-Nfrequency domain array Y, the IDFT is defined as:


for m= 0, 1, …, M–1, n=0, 1, …, N–1.

InverseInverse FastFast HilbertHilbert TransformTransform

Computes the inverse fast Hilbert transform of the input sequence X using Fourier
identities.


                                                    © National Instruments 4933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4934 ordinal=4934 -->
## Functions

Functions


      Inputs/Outputs

               •     X —

          X is the first input sequence.

               •      Inv Hilbert {X} —

            Inv Hilbert {X} is the inverse Hilbert Transform of the input signal X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The inverse Hilbert transform of a function h(t) is defined as


       Using the definition of the Hilbert transform


      you can obtain the inverse Hilbert transform by negating the forward Hilbert transform

       x(t) = H–1{h(t)} = –H{h(t)}

       Therefore, the Inverse Fast Hilbert Transform VI performs the discrete implementation
       of the inverse Hilbert transform with the aid of the Hilbert transform by taking the
       following steps.

         1. Hilbert transform the input sequence X

     Y= H{X}.


4934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4935 ordinal=4935 -->
## Functions

Functions

 2. Negate Yto obtain the inverse Hilbert transform

   H–1{X} = –Y.

The Hilbert transform works best with AC coupled, band-limited signals.

InverseInverse FHTFHT

Computes the inverse fast Hartley transform of the input sequence X.

The number of elements in the real input sequence X must be a valid power of two.


Inputs/Outputs

   •     X —

    X is the input sequence. To properly compute the inverse FHT of X, the number of elements, n, in
    the sequence must be a valid power of 2.

  n= 2m for m= 1, 2, 3,…,23

       If the number of elements in X is not a valid power of 2, the VI sets Inv FHT{X} to an empty array
    and returns an error.

   •      Inv FHT {X} —

    Inv FHT {X} is the inverse Hartley transform of X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The inverse Hartley transform of a function X(f) is defined as


                                                    © National Instruments 4935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4936 ordinal=4936 -->
## Functions

Functions


                                          ,

      where cas(x) = cos(x) + sin(x).

           If Yrepresents the output sequence Inv FHT{X}, the Inverse FHT VI calculates Y
      through the discrete implementation of the inverse Hartley integral


        for k= 1, 2, …n– 1,

      where nis the number of elements in X.

      The inverse Hartley transform maps real-valued frequency sequences into real-valued
       sequences. You can use it instead of the inverse Fourier transform to convolve,
       deconvolve, and correlate signals. You also can derive the Fourier transform from the
       Hartley transform.

       Refer to the FHT VI for a comparison of the Fourier and Hartley transforms.

     WaveletWavelet TransformTransform Daubechies4Daubechies4 InverseInverse

      Computes the inverse of the wavelet transform based on the Daubechies4 function of
       the input sequence X.


      Inputs/Outputs

               •     X —

          X is the samples of the input signal.

          The length of the signal has to be a power of 2, otherwise an error code is given.

               •      Wavelet Daubechies4 Inv {X} —

4936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4937 ordinal=4937 -->
## Functions

Functions


    Wavelet Daubechies4 Inv {X} returns the calculated inverse wavelet Daubechies4 transform.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Wavelet Transform Daubechies4 Inverse transform can be defined with the help of
the transformation matrix


                                                                 .


Here blank entries signify zeros. The numbers c0, c1, c2, and c3 have to fulfill certain
orthogonal properties, namely

c0² + c1² + c2² + c3² = 1 c2c0 + c3c1 = 0 c3 – c2 + c1 – c0 = 0 0c3 – 1c2 + 2c1 – 3c0 = 0

with the unique solution


                .


The inverse Wavelet Daubechies4 transform of the array X is defined by

Wavelet Daubechies4 Inv {X} = C–1*X.


                                                    © National Instruments 4937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4938 ordinal=4938 -->
## Functions

Functions

          It is

      CC–1 = C–1C= I.

       Refer to the definition of the Wavelet Transform Daubechies4 VI for more information
      about the Wavelet Transform Daubechies4 transform.

      The following diagram shows the Wavelet Transform Daubechies4 Inverse of a function
       with two spikes at the points 13 and 69. The signal length is 1024.


     WalshWalsh HadamardHadamard InverseInverse

      Computes the inverse of the real Walsh Hadamard transform of the input sequence X.


      Inputs/Outputs

               •     X —

          X is an array of power of 2 length.

               •      Walsh Hadamard Inverse {X} —

           Walsh Hadamard Inverse {X} returns the inverse Walsh Hadamard transform of X.

               •       error —


4938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4939 ordinal=4939 -->
## Functions

Functions


     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If WH{X} denotes the Walsh Hadamard transform of X and WHI{X} denotes the inverse
Walsh Hadamard transform, then it is

WHI{WH{X}} = WH{WHI{X}} = X.

Furthermore, the following equation is valid

                           ,

where nis the length of the signal X.

InverseInverse DCTDCT

Computes the inverse Discrete Cosine Transform (DCT) of the input sequence DCT {X}.
Wire data to the DCT {X} input to determine the polymorphic instance to use or
manually select the instance.


   • 1D Inverse DCT VI
   • 2D Inverse DCT VI

1D Inverse DCT

If yrepresents the input sequence DCT {X}, the one-dimensional inverse DCT of yis
defined as:


and


                                                    © National Instruments 4939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4940 ordinal=4940 -->
## Functions

Functions


      where Nis the length of the input sequence DCT {X}, y(k)is the k-th element of DCT
         {X}, and x(n)is the n-th element of the output sequence X. This VI applies a fast
       inverse DCT algorithm instead of calculating the inverse DCT directly. LabVIEW
      implements this fast inverse DCT algorithm using an FFT technique.

     2D Inverse DCT

           If yrepresents the input matrix DCT {X}, the two-dimensional inverse DCT of yis
       defined as:


      where Mand Nare the number of rows and columns, respectively, of DCT {X}. x(m,n)
         is the element of the output matrix X with row number mand column number n.
      y(u,v)is the element of the input matrix DCT {X} with row number uand column
      number v. This VI performs a two-dimensional inverse DCT using the following two
        steps:

         1. Perform a one-dimensional inverse DCT row-by-row on the input matrix DCT {X}.
         The output is Y'.
         2. Perform a one-dimensional inverse DCT column-by-column on Y'. The output is X.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Transforms\Image
        Compression with DCT.vi

     1D1D InverseInverse DCTDCT VIVI

      Computes the inverse Discrete Cosine Transform (DCT) of the input sequence DCT {X}.
       Wire data to the DCT {X} input to determine the polymorphic instance to use or

4940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4941 ordinal=4941 -->
## Functions

Functions

manually select the instance.


Inputs/Outputs

   •     DCT {X} —

   DCT {X} is the real input sequence.

   •     X —

    X is the inverse DCT of DCT {X}.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D Inverse DCT

If yrepresents the input sequence DCT {X}, the one-dimensional inverse DCT of yis
defined as:


and


where Nis the length of the input sequence DCT {X}, y(k)is the k-th element of DCT
{X}, and x(n)is the n-th element of the output sequence X. This VI applies a fast
inverse DCT algorithm instead of calculating the inverse DCT directly. LabVIEW
implements this fast inverse DCT algorithm using an FFT technique.


                                                    © National Instruments 4941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4942 ordinal=4942 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Transforms\Image
        Compression with DCT.vi

     2D2D InverseInverse DCTDCT VIVI

      Computes the inverse Discrete Cosine Transform (DCT) of the input sequence DCT {X}.
       Wire data to the DCT {X} input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •     DCT {X} —

         DCT {X} is the real input sequence.

               •     X —

          X is the inverse DCT of DCT {X}.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D Inverse DCT

           If yrepresents the input matrix DCT {X}, the two-dimensional inverse DCT of yis
       defined as:


4942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4943 ordinal=4943 -->
## Functions

Functions

where Mand Nare the number of rows and columns, respectively, of DCT {X}. x(m,n)
is the element of the output matrix X with row number mand column number n.
y(u,v)is the element of the input matrix DCT {X} with row number uand column
number v. This VI performs a two-dimensional inverse DCT using the following two
steps:

 1. Perform a one-dimensional inverse DCT row-by-row on the input matrix DCT {X}.
   The output is Y'.
 2. Perform a one-dimensional inverse DCT column-by-column on Y'. The output is X.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Transforms\Image
   Compression with DCT.vi

InverseInverse DSTDST

Computes the inverse Discrete Sine Transform (DST) of the input sequence DST {X}.
Wire data to the DST {X} input to determine the polymorphic instance to use or
manually select the instance.


   • 1D Inverse DST VI
   • 2D Inverse DST VI

1D Inverse DST

If yrepresents the input sequence DST {X}, the one-dimensional inverse Discrete Sine
Transform of yis defined as:


                                                    © National Instruments 4943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4944 ordinal=4944 -->
## Functions

Functions

      where Nis the length of DST {X}, yk is the kth element of DST {X}, and xn is the nth
      element of the output sequence X. This VI applies a fast inverse DST algorithm instead
       of calculating the inverse Discrete Sine Transform directly. LabVIEW implements the
        fast inverse DST algorithm using an FFT-based technique.

     2D Inverse DST

           If yrepresents the input matrix DST {X}, the two-dimensional inverse Discrete Sine
      Transform of yis defined as:


      where Mand Nare the number of rows and columns, respectively, of DST {X}. x(m,n)
         is the element of the output matrix X with row number mand column number n.
       y(u,v) is the element of DST {X} with row number uand column number v. This VI
      performs a two-dimensional inverse DST using the following two steps:

         1. Perform a one-dimensional inverse DST row-by-row on DST {X}. The output is Y'.
         2. Perform a one-dimensional inverse DST column-by-column on Y'. The output is X.

     1D1D InverseInverse DSTDST VIVI

      Computes the inverse Discrete Sine Transform (DST) of the input sequence DST {X}.
       Wire data to the DST {X} input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •     DST {X} —

          DST {X} is the real input sequence.

               •     X —

4944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4945 ordinal=4945 -->
## Functions

Functions


    X is the inverse DST of DST {X}.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D Inverse DST

If yrepresents the input sequence DST {X}, the one-dimensional inverse Discrete Sine
Transform of yis defined as:


where Nis the length of DST {X}, yk is the kth element of DST {X}, and xn is the nth
element of the output sequence X. This VI applies a fast inverse DST algorithm instead
of calculating the inverse Discrete Sine Transform directly. LabVIEW implements the
fast inverse DST algorithm using an FFT-based technique.

2D2D InverseInverse DSTDST VIVI

Computes the inverse Discrete Sine Transform (DST) of the input sequence DST {X}.
Wire data to the DST {X} input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •     DST {X} —

   DST {X} is the real input sequence.

   •     X —


                                                    © National Instruments 4945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4946 ordinal=4946 -->
## Functions

Functions


          X is the inverse DST of DST {X}.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D Inverse DST

           If yrepresents the input matrix DST {X}, the two-dimensional inverse Discrete Sine
      Transform of yis defined as:


      where Mand Nare the number of rows and columns, respectively, of DST {X}. x(m,n)
         is the element of the output matrix X with row number mand column number n.
       y(u,v) is the element of DST {X} with row number uand column number v. This VI
      performs a two-dimensional inverse DST using the following two steps:

         1. Perform a one-dimensional inverse DST row-by-row on DST {X}. The output is Y'.
         2. Perform a one-dimensional inverse DST column-by-column on Y'. The output is X.

      InverseInverse ChirpChirp ZZ TransformTransform

      Computes the inverse Chirp-Z transform of the input sequence Chirp-Z {X}.


      Inputs/Outputs

               •      Chirp-Z {X} —


4946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4947 ordinal=4947 -->
## Functions

Functions


    Chirp-Z {X} is the complex valued input sequence. The length of Chirp-Z {x} must be greater than
    or equal to # of samples.

   •      # of samples —

    # of samples specifies the length of X. # of samples must be less than or equal to the length of
    Chirp-Z {X}. If # of samples is less than or equal to 0, the VI sets # of samples to the length of
    Chirp-Z {X}. The default is –1.

   •       starting point —

     starting point is the point at which to begin evaluating the Chirp-Z transform and is best
    described by the equation in the details section. If starting point is 0, the VI returns an error.

   •      increment —

    increment is the increment between each point to evaluate for the Chirp-Z transform.
    increment cannot be 0.

    To avoid singular cases of the inverse Chirp-Z transform, increment must be different from
    e2π*j*k/L where k= 0, 1, …,L–1 L= 1, 2,…,N–1 and Nis # of samples.

   •     X —

    X is the inverse Chirp-Z transform of Chirp-Z {X}.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If Yrepresents the sequence Chirp-Z {X}, the following equation shows how the VI
performs the Chirp-Z transform to obtain the sequence X.


for k= 0, 1, …, M—1, where Nis the length of X (# of samples), Mis the length of
Chirp-Z {X}, Ais the starting point, Wis the increment, Xn is the nth element of X, and


                                                    © National Instruments 4947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4948 ordinal=4948 -->
## Functions

Functions

     yk is the kth element of Chirp-Z {X}.

      The inverse Chirp-Z transform computes the sequence X from Chirp-Z {X}. This VI
      employs a convolution-based method to implement this transform according to the
       following equations.

     xn=hn*mn

       with


      where


      and

      zk=0, 1, …, N—1

   mn can be obtained from its z-transform M(z):


      The following block diagram illustrates using the Inverse Chirp-Z Transform VI to
      compute the inverse Chirp-Z transform of some Chirp Z transformed signal.


4948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4949 ordinal=4949 -->
## Functions

Functions


PointPoint ByBy PointPoint

Use the Point By Point VIs to conveniently and efficiently process data a point at a
time. Point By Point VIs are included in the LabVIEW Full Development and
Professional Development Systems.

The Point By Point VIs are point-by-point versions of traditional LabVIEW analysis VIs.
The PtByPt suffix in the names of these VIs denotes that they are designed to analyze
data continuously a point at a time rather than blocks of data.


 Palette Object      Description

 Signal Generation  Use the Signal Generation PtByPt VIs to generate one-dimensional arrays with
 PtByPt              specific waveform patterns.


 Signal Operation   Use the Signal Operation PtByPt VIs to perform common one- and two-
 PtByPt            dimensional numerical analysis.


 Filters PtByPt      Use the Filters PtByPt VIs to implement IIR, FIR, and nonlinear filters.


 Spectral Analysis   Use the Spectral Analysis PtByPt VIs to implement common transforms used in
 PtByPt           mathematics and signal processing.


                                                    © National Instruments 4949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4950 ordinal=4950 -->
## Functions

Functions


         Palette Object      Description

        Transforms PtByPt Use the Transforms PtByPt VIs to compute transforms.


         Linear Algebra     Use the Linear Algebra PtByPt VIs to perform matrix- and vector-related
        PtByPt            computations and analysis.


                        Use the Fitting PtByPt VIs to fit data to a model and perform interpolation and          Fitting PtByPt                              extrapolation.


         Interpolation
                        Use the Interpolation PtByPt VIs to perform interpolation and extrapolation.        PtByPt


          Integral &         Use the Integral & Differential PtByPt VIs to perform integration and
          Differential PtByPt  differentiation.


         Probability &      Use the Probability & Statistics PtByPt VIs to perform probability, descriptive
          Statistics PtByPt     statistics, and analysis of variance operations.


        Geometry PtByPt   Use the Geometry PtByPt VIs to perform geometry operations.


                        Use the Polynomial PtByPt VIs to perform calculations and evaluations with
        Polynomial PtByPt
                            polynomials.


        Other Functions    Use the Other Functions PtByPt VIs to perform miscellaneous point-by-point
        PtByPt             operations.


      SignalSignal GenerationGeneration PtByPtPtByPt

      Use the Signal Generation PtByPt VIs to generate one-dimensional arrays with specific
      waveform patterns.

4950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4951 ordinal=4951 -->
## Functions

Functions

The VIs on this palette can return point by point error codes.


 Palette Object    Description

 Sine Wave                  Generates a sine wave point by point. PtByPt

 Triangle Wave                  Generates a triangle wave point by point. PtByPt

 Square Wave                  Generates a square wave point by point.
 PtByPt

 Sawtooth Wave                  Generates a sawtooth wave point by point. PtByPt


 Uniform White    Generates a uniformly distributed, pseudorandom pattern whose values are in
 Noise PtByPt     the range [–a:a], where a is the absolute value of amplitude.


 Gaussian White   Generates a Gaussian-distributed, pseudorandom pattern whose statistical
 Noise PtByPt      profile is (mu, sigma) = (0, s), where sis standard deviation.


 Periodic Random
                  Generates a set of output data that contains periodic random noise (PRN).
 Noise PtByPt

SineSine WaveWave PtByPtPtByPt

Generates a sine wave point by point.

This VI is similar to the Sine Wave VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 4951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4952 ordinal=4952 -->
## Functions

Functions


      Inputs/Outputs

               •      amplitude —

           amplitude is the amplitude of sine wave. The default is 1.0.

               •      frequency —

           frequency is the frequency of sine wave in Hz. The default is 1.

               •      phase —

           phase is the shift of the waveform, in degrees.

               •      time —

           time is the independent variable. Set time to increment at a constant, positive rate.

           samples per period = 1/(frequency · time). sine wave(time) = amplitude*sin(frequency · time +
           phase)

               •       sine wave —

            sine wave is the output sine wave.


       TriangleTriangle WaveWave PtByPtPtByPt

       Generates a triangle wave point by point.

       This VI is similar to the Triangle Wave VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


4952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4953 ordinal=4953 -->
## Functions

Functions


Inputs/Outputs

   •      amplitude —

    amplitude is the amplitude of triangle wave. The default is 1.0.

   •      frequency —

    frequency is the frequency of triangle wave in Hz. The default is 1.

   •      phase —

    phase is the shift of the waveform, in degrees.

   •      time —

    time is the independent variable. Set time to increment at a constant, positive rate.

    samples per period = 1/(frequency · time).

   •       triangle wave —

     triangle wave is the output triangle wave.


triangle wave = amplitude × triangle (q)

where


and

q= (360 · frequency · time + phase) mod (360), phase in degrees.


                                                    © National Instruments 4953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4954 ordinal=4954 -->
## Functions

Functions

      SquareSquare WaveWave PtByPtPtByPt

       Generates a square wave point by point.

       This VI is similar to the Square Wave VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •      duty cycle (%) —

           duty cycle is the percentage of time a square wave remains high versus low over one period. The
             default is 50.

               •      amplitude —

           amplitude is the amplitude of square wave. The default is 1.0.

               •      frequency —

           frequency is the frequency of square wave in Hz. The default is 1.

               •      phase —

           phase is the shift of the waveform, in phase.

               •      time —

           time is the independent variable. Set time to increment at a constant, positive rate.

           samples per period = 1/(frequency · time).

               •      square wave —


4954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4955 ordinal=4955 -->
## Functions

Functions


    square wave is the output square wave.


square wave = amplitude × square (p)

where


SawtoothSawtooth WaveWave PtByPtPtByPt

Generates a sawtooth wave point by point.

This VI is similar to the Sawtooth Wave VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •      amplitude —

    amplitude is the amplitude of sawtooth wave. The default is 1.0.

   •      frequency —

    frequency is the frequency of sawtooth wave in Hz. The default is 1.

   •      phase —

    phase is the shift of the waveform, in degrees.

   •      time —


                                                    © National Instruments 4955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4956 ordinal=4956 -->
## Functions

Functions


           time is the independent variable. Set time to increment at a constant, positive rate.

           samples per period = 1/(frequency · time).

               •      sawtooth wave —

           sawtooth wave is the output sawtooth wave.


      sawtooth wave = amplitude × sawtooth(q)

      where


      and

      q =(360 · frequency · time) + phase) mod (360), phase in degrees.
      UniformUniform WhiteWhite NoiseNoise PtByPtPtByPt

       Generates a uniformly distributed, pseudorandom pattern whose values are in the
      range [–a:a], where a is the absolute value of amplitude.

       This VI is similar to the Uniform White Noise VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —


4956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4957 ordinal=4957 -->
## Functions

Functions


     initialize, when TRUE, initializes the internal state of the VI.

   •      amplitude —

    amplitude is the amplitude of uniform white noise. The default is 1.0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

    LabVIEW maintains the internal seed state independently for each instance of this VI. For a
     specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the noise
    generator, and the noise generator resumes producing noise samples as a continuation of the
    previous noise sequence.

   •      uniform white noise —

    uniform white noise contains the uniformly distributed, pseudorandom pattern.


GaussianGaussian WhiteWhite NoiseNoise PtByPtPtByPt

Generates a Gaussian-distributed, pseudorandom pattern whose statistical profile is
(mu, sigma) = (0, s), where sis standard deviation.

This VI is similar to the Gaussian White Noise VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      standard deviation —

                                                    © National Instruments 4957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4958 ordinal=4958 -->
## Functions

Functions


           standard deviation is the standard deviation of the Gaussian probability density function. The
             default is 1.0.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

           LabVIEW maintains the internal seed state independently for each instance of this VI. For a
              specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the noise
             generator, and the noise generator resumes producing noise samples as a continuation of the
            previous noise sequence.

               •      Gaussian white noise —

           Gaussian white noise is the set of points that contains Gaussian white noise.


      The statistical profile of the Gaussian-distributed, pseudorandom pattern is
       (µ,standard deviation) = (0,s), where sis the absolute value of the specified standard
       deviation.

       PeriodicPeriodic RandomRandom NoiseNoise PtByPtPtByPt

       Generates a set of output data that contains periodic random noise (PRN).

       This VI is similar to the Periodic Random Noise VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.


4958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4959 ordinal=4959 -->
## Functions

Functions

   •     sample length —

    sample length is the number of random points to be delivered periodically. The default is 100.

    sample length must be greater than zero.

   •       spectral amplitude —

    spectral amplitude is the magnitude of the frequency domain components of the periodic
   random noise.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

    LabVIEW maintains the internal seed state independently for each instance of this VI. For a
     specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the noise
    generator, and the noise generator resumes producing noise samples as a continuation of the
    previous noise sequence.

   •      periodic random noise —

    periodic random noise is the set of points that contain periodic random noise.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

SignalSignal OperationOperation PtByPtPtByPt

Use the Signal Operation PtByPt VIs to perform common one- and two-dimensional
numerical analysis.

The VIs on this palette can return point by point error codes.


                                                    © National Instruments 4959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4960 ordinal=4960 -->
## Functions

Functions


         Palette Object    Description

        Convolution                      Computes the convolution of x and y.
        PtByPt

        Deconvolution                      Computes the deconvolution of x*y and y.        PtByPt


         AutoCorrelation  Computes the autocorrelation of the set of input data points specified by sample
        PtByPt          length x.


         CrossCorrelation                      Computes the cross correlation of x and y.
        PtByPt

           Y[i]=X[i-n]                              Shifts x by shifts: n samples.        PtByPt


       Unwrap Phase   Unwraps phase by eliminating discontinuities whose absolute values exceed half
        PtByPt            of wrap base.


                          Finds the norm of the set of input data points specified by sample length and         Unit Vector
                          obtains its corresponding Unit Vector by normalizing the original set of input        PtByPt                         data points with its norm.


                        Determines scale and offset and scales the set of input data specified by sample
         Scale 1D PtByPt
                         length using these values.


                        Determines the maximum absolute value contained in the set of input data
        Quick Scale 1D
                          points specified by sample length and then scales the set of input data points
        PtByPt
                          using the absolute value.


        Normalize       Normalizes input data point using the statistical profile (mean,standard
         Vector PtByPt     deviation) to obtain a Normalized Vector whose statistical profile is (0,1).


4960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4961 ordinal=4961 -->
## Functions

Functions


 Palette Object    Description

 Y[i]=Clip{X[i]}                    Clips x to within the bounds specified by upper limit and lower limit.
 PtByPt

 AC &amp; DC
 Estimator       Computes an estimation of the AC and DC levels of the input signal.
 PtByPt

 Peak Detector    Finds the location of peaks or valleys in the set of input data points specified by
 PtByPt           width.


 Threshold        Analyzes the set of input data points specified by width for valid peaks and
 Detector PtByPt  detects the set of points that exceed the threshold in a valid peak.


ConvolutionConvolution PtByPtPtByPt

Computes the convolution of x and y.

This VI is similar to the Convolution VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —


                                                    © National Instruments 4961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4962 ordinal=4962 -->
## Functions

Functions


           x is an input data point.

               •     sample length x —

           sample length x is the length of each set of incoming x-data. The VI performs computation for
           each set of data. The default is 100.

           sample length x must be greater than zero.

               •      y —

           y is an input data point.

               •     sample length y —

           sample length y is the length of each set of incoming y-data. The VI performs computation for
           each set of data. The default is 100.

           sample length must be greater than zero.

               •      X*Y —

           X*Y is the convolution of x and y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      DeconvolutionDeconvolution PtByPtPtByPt

      Computes the deconvolution of x*y and y.

      The deconvolution operation is performed using Fourier transform pairs. This VI is
        similar to the Deconvolution VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


4962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4963 ordinal=4963 -->
## Functions

Functions


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x*y —

    x*y is the set of input data.

   •     sample length x*y —

    sample length x*y is the length of each set of incoming x*y data. The VI performs computation
     for each set of data. The default is 100.

       If sample length x*y is not greater than or equal to sample length y, the VI returns an empty
     array.

   •      y —

    y is the set of input data.

   •     sample length y —

    sample length y is the length of each set of incoming y data. The VI performs computation for
    each set of data. The default is 100.

    sample length must be greater than zero.

   •     X —

    X is an array of signal samples.

    The number of elements in X is size = sample length x*y – sample length y + 1.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 4963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4964 ordinal=4964 -->
## Functions

Functions

      AutoCorrelationAutoCorrelation PtByPtPtByPt

      Computes the autocorrelation of the set of input data points specified by sample
       length x.

       This VI is similar to the AutoCorrelation VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length x —

           sample length x is the length of each set of incoming x-data. The VI performs computation for
           each set of data. The default is 100.

           sample length x must be greater than zero.

               •      Rxx —

           Rxx is the autocorrelation of x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4965 ordinal=4965 -->
## Functions

Functions

CrossCorrelationCrossCorrelation PtByPtPtByPt

Computes the cross correlation of x and y.

This VI is similar to the CrossCorrelation VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length x —

    sample length x is the length of each set of incoming x-data. The VI performs computation for
    each set of data. The default is 100.

    sample length x must be greater than zero.

   •      y —

    y is an input data point.

   •     sample length y —

    sample length y is the length of each set of incoming y-data. The VI performs computation for
    each set of data. The default is 100.

    sample length must be greater than zero.


                                                    © National Instruments 4965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4966 ordinal=4966 -->
## Functions

Functions

               •      Rxy —

           Rxy is the cross correlation of x and y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        Y[i]=X[i-n]Y[i]=X[i-n] PtByPtPtByPt

        Shifts x by shifts: n samples.

       This VI is similar to the Y[i]=X[i-n] VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •        shifts: n —

               shifts: n is the number of samples the VI shifts x to the right. shifts: n must be non-negative.

               •       shifted x —

             shifted x returns the shifted value of x.

               •       error —


4966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4967 ordinal=4967 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


UnwrapUnwrap PhasePhase PtByPtPtByPt

Unwraps phase by eliminating discontinuities whose absolute values exceed half of
wrap base.

This VI is similar to the Unwrap Phase VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      phase —

    phase is the input phase to unwrap, in radians.

   •     wrap base —

    wrap base controls the discontinuity in unwrapped phase. The discontinuities in unwrapped
    phase are less than or equal to half of wrap base. The default is 2pi.

   •     unwrapped phase —

   unwrapped phase returns phase unwrapped and expressed in radians.


                                                    © National Instruments 4967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4968 ordinal=4968 -->
## Functions

Functions

      UnitUnit VectorVector PtByPtPtByPt

       Finds the norm of the set of input data points specified by sample length and obtains
         its corresponding Unit Vector by normalizing the original set of input data points with
         its norm.

       This VI is similar to the Unit Vector VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      input data point —

            input data point is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

           sample length must be greater than zero.

               •      Unit Vector —

            Unit Vector is the output, normalized vector.

               •     norm —

         norm is the norm of the set of input data points specified by sample length.

               •       error —


4968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4969 ordinal=4969 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


ScaleScale 1D1D PtByPtPtByPt

Determines scale and offset and scales the set of input data specified by sample
length using these values.

This VI is similar to the Scale VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •     sample length —

    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

    sample length must be greater than zero.

   •       Y=(X-offset)/scale —

     Y=(X-offset)/scale is the output array.

   •       scale —

                                                    © National Instruments 4969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4970 ordinal=4970 -->
## Functions

Functions


             scale is the scaling factor.

               •       offset —

             offset is the offset factor.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      QuickQuick ScaleScale 1D1D PtByPtPtByPt

      Determines the maximum absolute value contained in the set of input data points
       specified by sample length and then scales the set of input data points using the
       absolute value.

       This VI is similar to the Quick Scale VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •     sample length —


4970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4971 ordinal=4971 -->
## Functions

Functions


    sample length is the length of each set of incoming data. The VI performs computation for each
     set of data. The default is 100.

    sample length must be greater than zero.

   •       Y[i]=X[i]/Max|X| —

     Y[i]=X[i]/Max|X| is the output array.

   •      max|X| —

    max|X| is the maximum absolute value contained in the set of input data points specified by
    sample length.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


NormalizeNormalize VectorVector PtByPtPtByPt

Normalizes input data point using the statistical profile (mean,standard deviation) to
obtain a Normalized Vector whose statistical profile is (0,1).

This VI is similar to the Normalize VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.


                                                    © National Instruments 4971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4972 ordinal=4972 -->
## Functions

Functions

               •      input data point —

            input data point is an input data point.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation for each
             set of data. The default is 100.

           sample length must be greater than zero.

               •      Normalized Vector —

           Normalized Vector is the output normalized vector.

               •      standard deviation —

           standard deviation is the standard deviation of the set of input data specified by sample length.

               •     mean —

         mean is the mean value of the set of input data specified by sample length.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        Y[i]=Clip{X[i]}Y[i]=Clip{X[i]} PtByPtPtByPt

       Clips x to within the bounds specified by upper limit and lower limit.

       This VI is similar to the Y[i]=Clip{X[i]} VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


4972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4973 ordinal=4973 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x is an input data point.

   •      upper limit —

    upper limit must be greater than or equal to lower limit. The default is 1.0.

       If upper limit is less than lower limit, the VI returns an error.

   •      lower limit —

    lower limit must be less than or equal to upper limit. The default is 0.0.

   •      clipped x —

    clipped x returns the clipped value of x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


ACAC &amp;&amp; DCDC EstimatorEstimator PtByPtPtByPt

Computes an estimation of the AC and DC levels of the input signal.

This VI is similar to the AC & DC Estimator VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

                                                    © National Instruments 4973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4974 ordinal=4974 -->
## Functions

Functions


               initialize, when TRUE, initializes the internal state of the VI.

               •       signal —

             signal specifies the input time-domain signal, usually in volts.

               •     sample length —

           sample length is the length of each set of incoming data. The VI performs computation on each
             set of data. The default is 100.

           sample length must be greater than 0.

               •     AC estimate (Vrms) —

          AC estimate returns the estimate of the input signal AC level in volts rms when the input Signal
                is in volts.

               •     DC estimate (V) —

         DC estimate returns the estimate of the input signal DC level in volts if the input Signal is in
               volts.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The AC & DC Estimator PtByPt VI routine performs spectral analysis to the extent that it
       separates DC, bin 0, from AC, the rms sum of the rest of the bins.

      PeakPeak DetectorDetector PtByPtPtByPt

       Finds the location of peaks or valleys in the set of input data points specified by width.

       This VI is similar to the Peak Detector VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


4974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4975 ordinal=4975 -->
## Functions

Functions


Inputs/Outputs

   •        initialize —

     initialize, when TRUE, initializes the internal state of the VI.

   •      x —

    x is an input data point.

   •      threshold peak —

    threshold peak tells the VI to ignore peaks that have an amplitude that is less than the
    threshold peak value.

   •      threshold valley —

    threshold valley tells the VI to ignore valleys that have an amplitude that is less than the
    threshold valley value.

   •      width —

    width is the size of the region of interest. The default is 3.

       If width is an odd number, the VI can find a peak or valley only at the position (width + 1)/2. If
    width is even, the VI can find a peak or valley only at the position width/2. Peaks or valleys
    represent local maximums, peaks, or local minimums, valleys, where width describes the region
     of interest.

   •     peak —

    peak identifies a peak within the region width.

   •       valley —

     valley identifies a valley within the region width.

   •       error —


                                                    © National Instruments 4975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4976 ordinal=4976 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      ThresholdThreshold DetectorDetector PtByPtPtByPt

       Analyzes the set of input data points specified by width for valid peaks and detects the
       set of points that exceed the threshold in a valid peak.

       This VI is similar to the Threshold Detector VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      x —

           x is an input data point.

               •      threshold —

            threshold is the level that all valid peaks must equal or exceed for the duration of width
            samples. The default is 0.0.

               •      width —

           width determines the minimum width, in number of samples, for the set of input data points.
            detected becomes TRUE when width remains at or above the threshold value. The default of
           width is 1.

               •      detected —


4976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4977 ordinal=4977 -->
## Functions

Functions


    detected is TRUE when the set of samples in width exceeds the threshold.

   •      index —

    index indicates the beginning index of the most recent peak when detected is TRUE.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


A peak is valid where the consecutive elements of X exceed the threshold and the
number of elements that exceed the threshold is equal to at least width.

See Threshold Detector VI help for more information.

FiltersFilters PtByPtPtByPt

Use the Filters PtByPt VIs to implement IIR, FIR, and nonlinear filters.

The VIs on this palette can return point by point error codes.


 Palette Object        Description

 Butterworth Filter     Generates a digital Butterworth filter by calling the Butterworth Coefficients
 PtByPt                    VI.


 Chebyshev Filter
                      Generates a digital Chebyshev filter by calling the Chebyshev Coefficients VI.
 PtByPt


 Inverse Chebyshev    Generates a digital Chebyshev II filter using the Inv Chebyshev Coefficients
 Filter PtByPt          algorithm.


                                                    © National Instruments 4977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4978 ordinal=4978 -->
## Functions

Functions


         Palette Object        Description

           Elliptic Filter PtByPt   Generates a digital elliptic filter by calling the Elliptic Coefficients VI.


         Bessel Filter PtByPt    Generates a digital Bessel filter using the Bessel Coefficients algorithm.


         Equi-Ripple LowPass                                     Filters x using an equi-ripple lowpass FIR filter model.        PtByPt

         Equi-Ripple HighPass                                     Filters x using an equi-ripple highpass FIR filter model.        PtByPt

         Equi-Ripple                                     Filters x using an equi-ripple bandpass FIR filter model.
        BandPass PtByPt

         Equi-Ripple
                                     Filters x using an equi-ripple bandstop FIR filter model.        BandStop PtByPt

         FIR Windowed Filter                                     Filters x using an FIR filter model.        PtByPt


        Median Filter PtByPt   Applies a median filter of rank to x.


         FIR Filter PtByPt        Filters x using the FIR filter specified by Forward Coefficients.


                                     Filters x using the direct form IIR filter specified by Reverse Coefficients and
           IIR Filter PtByPt
                           Forward Coefficients.


           IIR Filter with I.C.       Filters x using the IIR filter specified by Reverse Coefficients and Forward
        PtByPt                 Coefficients.


           IIR Cascade Filter
                                     Filters x using the cascade form of the IIR filter specified by the IIR Filter
        PtByPt


4978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4979 ordinal=4979 -->
## Functions

Functions


 Palette Object        Description

                         Cluster.


 IIR Cascade Filter       Filters x using the cascade form of the IIR filter specified by the IIR Filter
 with I.C. PtByPt        Cluster.


 Savitzky Golay Filter   Performs fitting based on a polynomial of a given order and then smooths
 PtByPt               the curve instead of returning raw data.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Point by Point\PtByPt
   and Array Based Filter.vi

ButterworthButterworth FilterFilter PtByPtPtByPt

Generates a digital Butterworth filter by calling the Butterworth Coefficients VI.

This VI is similar to the Butterworth Filter VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


Inputs/Outputs

   •        initialize —

                                                    © National Instruments 4979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4980 ordinal=4980 -->
## Functions

Functions


               initialize, when TRUE, initializes the internal state of the VI.

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •      x —

           x is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered x to 0 and returns an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

                    If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
            the VI sets Filtered x to 0 and returns an error. When filter type is 2 (Bandpass) or 3 (Bandstop),
           low cutoff freq: fl must be less than high cutoff freq: fh.

               •      order —

            order specifies the filter order and must be greater than 0. The default is 2.


4980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4981 ordinal=4981 -->
## Functions

Functions


       If order is less than or equal to 0, the VI sets Filtered x to 0 and returns an error.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Point by Point\PtByPt
   and Array Based Filter.vi

ChebyshevChebyshev FilterFilter PtByPtPtByPt

Generates a digital Chebyshev filter by calling the Chebyshev Coefficients VI.

The Chebyshev Filter PtByPt VI is similar to the Chebyshev Filter VI.

      Note By default, reentrant execution is enabled in all Point By Point VIs.


                                                    © National Instruments 4981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4982 ordinal=4982 -->
## Functions

Functions


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •      x —

           x is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered x to 0 and returns an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •      low cutoff freq: fl —


4982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4983 ordinal=4983 -->
## Functions

Functions


    low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
     default is 0.125 Hz.

       If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
    the VI sets Filtered x to 0 and returns an error. When filter type is 2 (Bandpass) or 3 (Bandstop),
    low cutoff freq: fl must be less than high cutoff freq: fh.

   •       ripple(dB) —

     ripple is the ripple in the passband. ripple must be greater than zero and must be expressed in
     decibels. The default is 0.1.

   •      order —

    order specifies the filter order and must be greater than 0. The default is 2.

       If order is less than or equal to 0, the VI sets Filtered x to 0 and returns an error.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

InverseInverse ChebyshevChebyshev FilterFilter PtByPtPtByPt

Generates a digital Chebyshev II filter using the Inv Chebyshev Coefficients algorithm.

This VI is similar to the Inverse Chebyshev Filter VI.


                                                    © National Instruments 4983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4984 ordinal=4984 -->
## Functions

Functions

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •      x —

           x is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
               0. The default is 1.0 Hz.

                    If sampling freq: fs is less than or equal to 0, this VI sets Filtered x to 0 and returns an error.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is


4984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4985 ordinal=4985 -->
## Functions

Functions


    2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
    observe the Nyquist criterion.

   •      low cutoff freq: fl —

    low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
     default is 0.125 Hz.

       If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
    the VI sets Filtered x to 0 and returns an error. When filter type is 2 (Bandpass) or 3 (Bandstop),
    low cutoff freq: fl must be less than high cutoff freq: fh.

   •      attenuation (dB) —

    attenuation is the attenuation in the stopband. attenuation must be greater than 0 and
    expressed in decibels. The default is 60.0.

       If attenuation is less than or equal to 0, the VI sets the output to 0 and returns an error.

   •      order —

    order specifies the filter order and must be greater than 0. The default is 2.

       If order is less than or equal to 0, the VI sets Filtered x to 0 and returns an error.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
relationship:

0 < f1 < f2 < 0.5fs

where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.


                                                    © National Instruments 4985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4986 ordinal=4986 -->
## Functions

Functions

        EllipticElliptic FilterFilter PtByPtPtByPt

       Generates a digital elliptic filter by calling the Elliptic Coefficients VI.

      The Elliptic Filter PtByPt VI is similar to the Elliptic Filter VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •        filter type —

                filter type specifies the passband of the filter.

           0        Lowpass
           1         Highpass
           2        Bandpass
           3        Bandstop

               •      passband ripple (dB) —

           passband ripple is the ripple in the passband. passband ripple must be greater than 0 and
            expressed in decibels. The default is 1.0.

                    If passband ripple is less than or equal to 0, the VI sets the output filter data to 0 and returns an
               error.

               •      x —

4986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4987 ordinal=4987 -->
## Functions

Functions


  x is the input signal to filter.

•      sampling freq: fs —

  sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
   0. The default is 1.0 Hz.

   If sampling freq: fs is less than or equal to 0, this VI sets Filtered x to 0 and returns an error.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
  the VI sets Filtered x to 0 and returns an error. When filter type is 2 (Bandpass) or 3 (Bandstop),
  low cutoff freq: fl must be less than high cutoff freq: fh.

•      stopband attenuation(dB) —

  stopband attenuation must be greater than 0. stopband attenuation must be expressed in
  decibels. The default is 60.0.

   If stopband attenuation is less than or equal to 0, the VI sets Filtered x to 0 and returns an error.

        Note If the filter order is high, this VI uses a higher attenuation than the value of
          stopband attenuation to design the filter.

•      order —

  order specifies the filter order and must be greater than 0. The default is 2.

   If order is less than or equal to 0, the VI sets Filtered x to 0 and returns an error.

•       Filtered x —


                                                   © National Instruments 4987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4988 ordinal=4988 -->
## Functions

Functions


             Filtered x contains the result of filtering the input sequence x by convolution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

      BesselBessel FilterFilter PtByPtPtByPt

       Generates a digital Bessel filter using the Bessel Coefficients algorithm.

       This VI is similar to the Bessel Filter VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •        filter type —


4988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4989 ordinal=4989 -->
## Functions

Functions


   filter type specifies the passband of the filter.

  0        Lowpass
  1         Highpass
  2        Bandpass
  3        Bandstop

•      x —

  x is the input signal to filter.

•      sampling freq: fs —

  sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
   0. The default is 1.0 Hz.

   If sampling freq: fs is less than or equal to 0, this VI sets Filtered x to 0 and returns an error.

•      high cutoff freq: fh —

  high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

  The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
  2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
  observe the Nyquist criterion.

•      low cutoff freq: fl —

  low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
  default is 0.125 Hz.

   If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
  the VI sets Filtered x to 0 and returns an error. When filter type is 2 (Bandpass) or 3 (Bandstop),
  low cutoff freq: fl must be less than high cutoff freq: fh.

•      order —

  order specifies the filter order and must be greater than 0. The default is 2.

   If order is less than or equal to 0, the VI sets Filtered x to 0 and returns an error.

•       Filtered x —


                                                   © National Instruments 4989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4990 ordinal=4990 -->
## Functions

Functions


             Filtered x contains the result of filtering the input sequence x by convolution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The values for high cutoff freq: fh and low cutoff freq: fl must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.

      Equi-RippleEqui-Ripple LowPassLowPass PtByPtPtByPt

        Filters x using an equi-ripple lowpass FIR filter model.

       This VI is similar to the Equi-Ripple LowPass VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      pass freq —


4990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4991 ordinal=4991 -->
## Functions

Functions


    pass freq must be greater than zero and observe the Nyquist criterion. The default is 0.2 Hz.

       If pass freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
     Filtered x to zero and returns an error through the Parks-McClellan VI.

   •      x —

    x is the input signal to filter.

   •      sampling freq: fs —

    sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
     zero. The default is 1.0 Hz.

   •      # of taps —

    # of taps must be greater than 2. The default is 32.

       If # of taps is less than or equal to 2, the VI sets Filtered x to 0 and returns an error through the
    Parks-McClellan VI.

   •      stop freq —

    stop freq must be greater than the pass freq and observe the Nyquist criterion. The default is 0.3
    Hz.

       If stop freq is less than or equal to pass freq or does not meet the Nyquist criterion, the VI sets
     Filtered x to zero and returns an error through the Parks-McClellan VI.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Generates a lowpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and # of taps, pass freq, stop freq, and sampling freq. The Equi-
Ripple LowPass PtByPt VI then applies a linear-phase, lowpass filter to x to obtain
Filtered x.


                                                    © National Instruments 4991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4992 ordinal=4992 -->
## Functions

Functions

      The passband of the filter goes from zero (DC) to pass freq. The transition band goes
      from pass freq to stop freq. The stopband goes from stop freq to the Nyquist
       frequency.

      Equi-RippleEqui-Ripple HighPassHighPass PtByPtPtByPt

        Filters x using an equi-ripple highpass FIR filter model.

       This VI is similar to the Equi-Ripple HighPass VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      high freq —

            high freq must be greater than stop freq and observe the Nyquist criterion. The default is 0.3 Hz.

                    If high freq is less than or equal to stop freq or does not meet the Nyquist criterion, the VI sets
             Filtered x to zero and returns an error through the Parks-McClellan VI.

               •      x —

           x is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
              zero. The default is 1.0 Hz.

               •      # of taps —

4992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4993 ordinal=4993 -->
## Functions

Functions


    # of taps must be greater than 2. The default is 31.

       If # of taps is less than or equal to 2, the VI sets Filtered x to zero and returns an error through
    the Parks-McClellan VI.

          Note The Parks-McClellan algorithm introduces a large error when designing a
             highpass filter for an even number of taps. To avoid this error, the Equi-Ripple
            HighPass PtByPt VI adjusts the number of taps to the next higher odd value if # of
             taps is even.

   •      stop freq —

    stop freq must be greater than zero and observe the Nyquist criterion. The default is 0.2 Hz.

       If stop freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
     Filtered x to zero and returns an error through the Parks-McClellan VI.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Generates a highpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and # of taps, stop freq, high freq, and sampling freq. The Equi-
Ripple HighPass PtByPt VI then applies a linear-phase, highpass filter to x to obtain
Filtered x.

The stopband of the filter goes from zero (DC) to the stop freq. The transition band
goes from the stop freq to the high freq. The passband goes from the high freq to the
Nyquist frequency.

Equi-RippleEqui-Ripple BandPassBandPass PtByPtPtByPt

Filters x using an equi-ripple bandpass FIR filter model.

This VI is similar to the Equi-Ripple BandPass VI.

                                                    © National Instruments 4993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4994 ordinal=4994 -->
## Functions

Functions

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      higher pass freq —

            higher pass freq must be greater than lower pass freq frequency and observe the Nyquist
              criterion. The default is 0.35 Hz.

                    If higher pass freq is less than or equal to lower pass freq or does not meet the Nyquist criterion,
            the VI sets Filtered x to 0 and returns an error through the Parks-McClellan VI.

               •      lower pass freq —

           lower pass freq must be greater than the lower stop freq and observe the Nyquist criterion. The
             default is 0.25 Hz.

                    If lower pass freq is less than or equal to lower stop freq or does not meet the Nyquist criterion,
            the VI sets Filtered x to an empty array and returns an error through the Parks-McClellan VI.

               •      x —

           x is the input signal to filter.

               •      sampling freq: fs —

           sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
              zero. The default is 1.0 Hz.

               •      # of taps —


4994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4995 ordinal=4995 -->
## Functions

Functions


    # of taps must be greater than 2. The default is 32.

       If # of taps is less than or equal to 2, the VI sets Filtered x to 0 and returns an error through the
    Parks-McClellan VI.

   •      lower stop freq —

    lower stop freq must be greater than zero and observe the Nyquist criterion. The default is 0.20
    Hz.

       If lower stop freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
     Filtered x to zero and returns an error through the Parks-McClellan VI.

   •      higher stop freq —

    higher stop freq must be greater than higher pass freq and observe the Nyquist criterion. The
     default is 0.4 Hz.

       If higher stop freq is less than or equal to higher pass freq or does not meet the Nyquist
     criterion, the VI sets Filtered x to zero and returns an error through the Parks-McClellan VI.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Generates a bandpass FIR filter with equi-ripple characteristics using the Parks-
McClellan algorithm and higher pass freq, lower pass freq, # of taps, lower stop freq,
higher stop freq, and sampling freq: fs. The Equi-Ripple BandPass PtByPt VI then
applies a linear-phase, bandpass filter to x to obtain Filtered x.

The first stopband of the filter region goes from zero (DC) to the lower stop frequency.
The passband region goes from the lower pass frequency to the higher pass frequency.
The second stopband region goes from the higher stop frequency to the Nyquist
frequency.


                                                    © National Instruments 4995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4996 ordinal=4996 -->
## Functions

Functions

      Equi-RippleEqui-Ripple BandStopBandStop PtByPtPtByPt

        Filters x using an equi-ripple bandstop FIR filter model.

       This VI is similar to the Equi-Ripple BandStop VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      higher pass freq —

            higher pass freq must be greater than higher stop freq and observe the Nyquist criterion. The
             default is 0.4 Hz.

                    If higher pass freq is less than or equal to higher stop freq or does not meet the Nyquist
              criterion, the VI sets Filtered x to zero and returns an error through the Parks-McClellan VI.

               •      lower pass freq —

           lower pass freq must be greater than zero and observe the Nyquist criterion. The default is 0.2
            Hz.

                    If lower pass freq is less than or equal to zero or does not meet the Nyquist criterion, the VI sets
             Filtered x to zero and returns an error through the Parks-McClellan VI.

               •      x —

           x is the input signal to filter.


4996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4997 ordinal=4997 -->
## Functions

Functions

   •      sampling freq: fs —

    sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
     zero. The default is 1.0 Hz.

   •      # of taps —

    # of taps must be greater than 2. The default is 31.

       If # of taps is less than or equal to 2, the VI sets Filtered x to 0 and returns an error through the
    Parks-McClellan VI.

          Note The Parks-McClellan algorithm introduces a large error when you design a
            bandstop filter for an even number of taps. To avoid this error, the Equi-Ripple
           BandStop PtByPt VI adjusts the number of taps to the next higher odd value if # of
             taps is even.

   •      lower stop freq —

    lower stop freq must be greater than lower pass freq and observe the Nyquist criterion. The
     default is 0.25 Hz.

       If lower stop freq is less than or equal to lower pass freq or does not meet the Nyquist criterion,
    the VI sets Filtered x to zero and returns an error through the Parks-McClellan VI.

   •      higher stop freq —

    higher stop freq must be greater than lower stop freq and observe the Nyquist criterion. The
     default is 0.35 Hz.

       If higher stop freq is less than or equal to lower stop freq or does not meet the Nyquist criterion,
    the VI sets Filtered x to zero and returns an error through the Parks-McClellan VI.

   •       Filtered x —

     Filtered x contains the result of filtering the input sequence x by convolution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Generates a bandstop FIR digital filter with equi-ripple characteristics using the Parks-


                                                    © National Instruments 4997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4998 ordinal=4998 -->
## Functions

Functions

       McClellan algorithm and higher pass freq, lower pass freq, # of taps, lower stop
       frequency, higher stop freq, and sampling freq. The Equi-Ripple BandStop PtByPt VI
      then applies a linear-phase, bandstop filter to x to obtain Filtered x.

      The first passband region of the filter goes from zero (DC) to the lower pass freq. The
      stopband region goes from the lower stop freq to the higher stop freq. The second
      passband region goes from the higher pass freq to the Nyquist frequency.

       FIRFIR WindowedWindowed FilterFilter PtByPtPtByPt

        Filters x using an FIR filter model.

       This VI is similar to the FIR Windowed Filter VI.

           Note By default, reentrant execution is enabled in all Point By Point VIs.


      Inputs/Outputs

               •        initialize —

               initialize, when TRUE, initializes the internal state of the VI.

               •      high cutoff freq: fh —

            high cutoff freq: fh is the high cutoff frequency in Hz. The default is 0.45 Hz.

          The VI ignores this parameter when filter type is 0 (Lowpass) or 1 (Highpass). When filter type is
           2 (Bandpass) or 3 (Bandstop), high cutoff freq: fh must be greater than low cutoff freq: fl and
           observe the Nyquist criterion.

               •        filter type —


4998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4999 ordinal=4999 -->
## Functions

Functions


   filter type specifies the passband of the filter.

  0        Lowpass
  1         Highpass
  2        Bandpass
  3        Bandstop

•      x —

  x is the input signal to filter.

•      sampling freq: fs —

  sampling freq: fs is the frequency in Hz at which you want to sample x and must be greater than
   0. The default is 1.0 Hz.

   If sampling freq: fs is less than or equal to 0, this VI sets Filtered x to 0 and returns an error.

•     window —

  window specifies the type of smoothing window.

  Smoothing windows decrease ripple in the filter passband and improve the ability of the filter to
  attenuate frequency components in the filter stopband.

  0         Rectangle (default)
  1        Hanning
  2       Hamming
  3         Blackman-Harris
  4         Exact Blackman
  5        Blackman
  6           Flat Top
  7        4 Term B-Harris
  8        7 Term B-Harris
  9       Low Sidelobe
  11       Blackman Nuttall
  30         Triangle
  31        Bartlett-Hanning
  32      Bohman
  33        Parzen


                                                   © National Instruments 4999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5000 ordinal=5000 -->
## Functions

Functions


           34       Welch
           60        Kaiser
           61       Dolph-Chebyshev
           62        Gaussian

               •      taps —

            taps determines the total number of FIR coefficients and must be greater than 0. The default is
             25.

                    If taps is less than or equal to 0, the VI sets Filtered x to 0 and returns an error. taps must be odd
              for highpass and bandstop filters.

               •      low cutoff freq: fl —

           low cutoff freq: fl is the low cutoff frequency in Hz and must observe the Nyquist criterion. The
             default is 0.125 Hz.

                    If low cutoff freq: fl is less than or equal to 0 or greater than half the value of sampling freq: fs,
            the VI sets Filtered x to 0 and returns an error. When filter type is 2 (Bandpass) or 3 (Bandstop),
           low cutoff freq: fl must be less than high cutoff freq: fh.

               •       Filtered x —

             Filtered x contains the result of filtering the input sequence x by convolution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The values for low cutoff freq: fl and high cutoff freq: fh must observe the following
        relationship:

      0 < f1 < f2 < 0.5fs

      where f1 is low cutoff freq: fl, f2 is high cutoff freq: fh, and fs is sampling freq: fs.


5000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5000 -->

