# NI DOCUMENT BUNDLE: labview-nxg-ansi-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-ansi-c-api-ref start=1 end=3 -->
<!--NI_TOPIC bundle=labview-nxg-ansi-c-api-ref path=analysis-lib.html language=enus -->
## TOPIC 00001: Analysis Library C Function Reference

- bundle_id: `labview-nxg-ansi-c-api-ref`
- source_path: `analysis-lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ansi-c-api-ref/raw/resource/enus/analysis-lib.html
- document_id: `labview-nxg-ansi-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists Analysis Library functions. Clicking a link in this table opens a topic in the LabWindows/CVI Help in a new browser tab. Function Description Abs1D Finds the absolute values of the array elements. Add1D Adds two 1D arrays, element by element. Add2D Adds two 2D arrays, eleme

Analysis Library C Function Reference

The following table lists Analysis Library functions. Clicking a link in this table opens a topic in the LabWindows/CVI Help in a new browser tab.

| Function | Description |
| --- | --- |
| Abs1D | Finds the absolute values of the array elements. |
| Add1D | Adds two 1D arrays, element by element. |
| Add2D | Adds two 2D arrays, element by element. |
| AllocCxIIRFilterStatePtr | Allocates and initializes the filterInformation structure. |
| AllocIIRFilterPtr | Allocates and initializes the filterInformation structure. |
| ArbitraryWave | Generates an array that contains an arbitrary wave, with each cycle described by an interpolated version of the waveTable you specify. |
| AutoCorrelate | Finds the autocorrelation of the input array. |
| AutoCorrelate2D | Finds the 2D autocorrelation of the input array. |
| BernoulliNoise | Generates an array containing a pseudorandom pattern of ones and zeros. |
| Bessel_CascadeCoef | Generates the set of cascade form filter coefficients to implement an IIR filter as specified by the Bessel filter model (this function has been superseded by Bessel_CascadeCoefEx). |
| Bessel_CascadeCoefEx | Generates the set of cascade form filter coefficients to implement an IIR filter as specified by the Bessel filter model. |
| Bessel_Coef | Generates the set of filter coefficients to implement an IIR filter as specified by the Bessel filter model. |
| BinomialNoise | Generates an array containing a Binomially-distributed pseudorandom pattern of values that are the number of occurrences of an event, given the probability of that event occurring and the number of trials. |
| Bssl_BPF | Filters the input array using a Bessel bandpass digital filter. |
| Bssl_BSF | Filters the input array using a Bessel bandstop digital filter. |
| Bssl_HPF | Filters the input array using a Bessel highpass digital filter. |
| Bssl_LPF | Filters the input array using a Bessel lowpass digital filter. |
| Bw_BPF | Filters the input array using a Butterworth bandpass digital filter. |
| Bw_BSF | Filters the input array using a Butterworth bandstop digital filter. |
| Bw_CascadeCoef | Generates the set of cascade form filter coefficients to implement an IIR filter as specified by the Butterworth filter model. |
| Bw_Coef | Generates the set of filter coefficients to implement an IIR filter as specified by the Butterworth filter model. |
| Bw_HPF | Filters the input array using a Butterworth highpass digital filter. |
| Bw_LPF | Filters the input array using a Butterworth lowpass digital filter. |
| CascadeToDirectCoef | Converts from the cascade IIR coefficients contained by the filterInformation structure to direct-form IIR coefficients in arrays aCoefficientArray and bCoefficientArray. |
| Ch_BPF | Filters the input array using a Chebyshev bandpass digital filter. |
| Ch_BSF | Filters the input array using a Chebyshev bandstop digital filter. |
| Ch_CascadeCoef | Generates the set of cascade form filter coefficients to implement an IIR filter as specified by the Chebyshev filter model. |
| Ch_Coef | Generates the set of filter coefficients to implement an IIR filter as specified by the Chebyshev filter model. |
| Ch_HPF | Filters the input array using a Chebyshev highpass digital filter. |
| Ch_LPF | Filters the input array using a Chebyshev lowpass digital filter. |
| Chirp | Generates an array that contains a chirp pattern. |
| ChirpZT | The Chirp-Z Transform calculates the z transform along a spiral in the z-plane. |
| Clear1D | Sets the elements of an array to zero. |
| Clip | Clips each element of the array between the specified upper and lower limits. |
| Convolve | Finds the convolution of the input arrays (this function has been superseded by ConvolveEx). |
| Convolve2D | Finds the 2D convolution of the complex input arrays. |
| ConvolveEx | Finds the convolution of the input arrays. |
| Copy1D | Copies the elements from one array to another array. |
| Correlate | Finds the correlation of the input arrays (this function has been superseded by CorrelateEx). |
| Correlate2D | Finds the 2D correlation of the input arrays. |
| CorrelateEx | Finds the correlation of the input arrays. |
| CreateFFTTable | Creates a reusable FFT table. |
| CrossSpectrum | Calculates the double-sided cross power spectrum, Sxy, of the input sequences xArray and yArray. |
| CxAdd | Adds two complex numbers, x and y. |
| CxAdd1D | Adds two complex 1D arrays. |
| CxAutoCorrelate | Finds the autocorrelation of the complex input array. |
| CxAutoCorrelate2D | Finds the 2D autocorrelation of the complex input array. |
| CxBssl_BPF | Filters the complex input array using a Bessel bandpass digital filter. |
| CxBssl_BSF | Filters the complex input array using a Bessel bandstop digital filter. |
| CxBssl_HPF | Filters the complex input array using a Bessel highpass digital filter. |
| CxBssl_LPF | Filters the complex input array using a Bessel lowpass digital filter. |
| CxBw_BPF | Filters the complex input array using a Butterworth bandpass digital filter. |
| CxBw_BSF | Filters the complex input array using a Butterworth bandstop digital filter. |
| CxBw_HPF | Filters the complex input array using a Butterworth highpass digital filter. |
| CxBw_LPF | Filters the complex input array using a Butterworth lowpass digital filter. |
| CxCh_BPF | Filters the complex input array using a Chebyshev bandpass digital filter. |
| CxCh_BSF | Filters the complex input array using a Chebyshev bandstop digital filter. |
| CxCh_HPF | Filters the complex input array using a Chebyshev highpass digital filter. |
| CxCh_LPF | Filters the complex input array using a Chebyshev lowpass digital filter. |
| CxChirpZT | The Chirp-Z Transform calculates the z transform along a spiral in the z-plane. |
| CxConvolve | Finds the convolution of the complex input arrays arrayX and arrayY. |
| CxConvolve2D | Finds the 2D convolution of the complex input arrays. |
| CxCorrelate | Finds the correlation of the complex input arrays. |
| CxCorrelate2D | Finds the 2D correlation of the complex input arrays. |
| CxCrossSpectrum | Calculates the double-sided cross power spectrum, Sxy, of the complex input sequences xArray and yArray. |
| CxDecimate | Decimates the input sequence inputArray. |
| CxDecimateContinuous | Continuously decimates the complex input sequence inputArray by the decimatingFactor and the averaging values that you specify. |
| CxDiv | Divides two complex numbers, x and y. |
| CxDiv1D | Divides two complex 1D arrays. |
| CxElp_BPF | Filters the complex input array using an elliptic bandpass digital filter. |
| CxElp_BSF | Filters the complex input array using an elliptic bandstop digital filter. |
| CxElp_HPF | Filters the complex input array using an elliptic highpass digital filter. |
| CxElp_LPF | Filters the complex input array using an elliptic lowpass digital filter. |
| CxExp | Calculates the exponential of a complex number. |
| CxFFT2D | Computes the 2D fast Fourier transform (FFT) of a complex time-domain signal. |
| CxFFTEx | Calculates the 1D fast Fourier transform (FFT) of a complex time-domain signal. |
| CxIIRCascadeFiltering | Filters the complex input sequence using the cascade IIR filter specified by the filterInformation structure. |
| CxInvCh_BPF | Filters the complex input array using an inverse Chebyshev bandpass digital filter. |
| CxInvCh_BSF | Filters the complex input array using an inverse Chebyshev bandstop digital filter. |
| CxInvCh_HPF | Filters the complex input array using an inverse Chebyshev highpass digital filter. |
| CxInvCh_LPF | Filters the complex input array using an inverse Chebyshev lowpass digital filter. |
| CxInvFFT2D | Computes the complex 2D inverse fast Fourier transform (inverse FFT) of a signal. |
| CxInvFFTEx | Computes the complex inverse fast Fourier transform (inverse FFT) of an input sequence. |
| CxLinEv1D | Performs a linear evaluation of a complex 1D array. |
| CxLn | Calculates the natural logarithm of a complex number. |
| CxLog | Calculates the logarithm (base 10) of a complex number. |
| CxMul | Multiplies two complex numbers, x and y. |
| CxMul1D | Multiplies two complex 1D arrays. |
| CxNormalizedCorrelate | Finds the correlation of the complex input arrays. |
| CxPow | Calculates the power of a complex number. |
| CxRecip | Finds the reciprocal of a complex number, x. |
| CxRiffleArray | Riffles the input array of NIComplexNumber elements by randomly selecting two elements in inputArray, swapping those elements, and then repeating this process numberOfElements times, where numberOfElements is the size of inputArray. |
| CxSpectrum | Calculates the power spectrum of the complex input array. |
| CxSqrt | Calculates the square root of a complex number. |
| CxSub | Subtracts two complex numbers, x and y. |
| CxSub1D | Subtracts two complex 1D arrays. |
| DCT | Computes the one-dimensional Discrete Cosine Transform (DCT) of the input sequence inputArray. |
| DCT2D | Computes the two-dimensional Discrete Cosine Transform (DCT) of a matrix inputArray. |
| DST | Computes the one-dimensional Discrete Sine Transform (DST) of a sequence inputArray. |
| DST2D | Computes the two-dimensional Discrete Sine Transform (DST) of a matrix inputArray. |
| Decimate | Decimates the input sequence inputArray by the decimatingFactor and the averaging you specify. |
| DecimateContinuous | Continuously decimates the input sequence inputArray by the decimatingFactor and the averaging values that you specify. |
| Deconvolve | Calculates the deconvolution of YArray with XArray. |
| DestroyFFTTable | Frees the resources used by an FFT table created with CreateFFTTable. |
| Difference | Finds the discrete difference of the input array (this function has been superseded by DifferenceEx). |
| DifferenceEx | Differentiates the input signal inputArray using the second order central, fourth order central, forward, or backward differentiation method. |
| Div1D | Divides two 1D arrays, element by element. |
| Div2D | Divides two 2D arrays, element by element. |
| Elp_BPF | Filters the input array using an elliptic bandpass digital filter. |
| Elp_BSF | Filters the input array using an elliptic bandstop digital filter. |
| Elp_CascadeCoef | Generates the set of cascade form filter coefficients to implement an IIR filter as specified by the elliptic (or Cauer) filter model. |
| Elp_HPF | Filters the input array using an elliptic highpass digital filter. |
| Elp_LPF | Filters the input array using an elliptic lowpass digital filter. |
| FFT | Calculates the fast Fourier transform (FFT) of the complex data. |
| FFT2D | Computes the fast Fourier transform (FFT) of a 2D time-domain signal. |
| FFTEx | Computes the fast Fourier transform (FFT) of a real time-domain signal. |
| FHT | Calculates the fast Hartley transform (FHT). |
| FastHilbertTransform | Computes the fast Hilbert transform of the input sequence x. |
| FreeCxIIRFilterStatePtr | Frees the FIR filter structure and all internal arrays. |
| FreeIIRFilterPtr | Frees the IIR cascade filter structure and all internal arrays. |
| GammaNoise | Generates an array containing a Gamma-distributed pseudorandom pattern of values that are the waiting times that correspond to order. |
| GaussModSinePattern | Generates an array containing a Gaussian modulated sinusoidal pulse. |
| GaussMonopulse | Generates a Gaussian monopulse array. |
| GaussNoise | Generates an array of random Gaussian numbers distributed with expected zero mean value and the standard deviation you specify. |
| HaltonSeq | Generates an array containing a quasi-random Halton sequence, which is a low-discrepancy number sequence that uniformly distributes in the interval [0, 1]. |
| IIRCascadeFiltering | Filters the input sequence using the cascade IIR filter specified by the filterInformation structure. |
| Impulse | Generates an array that has the pattern of an impulse waveform. |
| IntRiffleArray | Riffles the input array of integer elements by randomly selecting two elements in inputArray, swapping those elements, and then repeating this process numberOfElements times, where numberOfElements is the size of inputArray. |
| Integrate | Calculates the discrete integral of the input array Simpson's Rule for discrete evaluation. |
| InvCh_BPF | Filters the input array using an inverse Chebyshev bandpass digital filter. |
| InvCh_BSF | Filters the input array using an inverse Chebyshev bandstop digital filter. |
| InvCh_CascadeCoef | Generates the set of cascade form filter coefficients to implement an IIR filter as specified by the inverse Chebyshev filter model. |
| InvCh_Coef | Generates the set of filter coefficients to implement an IIR filter as specified by the inverse Chebyshev filter model. |
| InvCh_HPF | Filters the input array using an inverse Chebyshev highpass digital filter. |
| InvCh_LPF | Filters the input array using an inverse Chebyshev lowpass digital filter. |
| InvChirpZT | Calculates the inverse Chirp Z transform of an input sequence. |
| InvDCT | Computes the one-dimensional inverse Discrete Cosine Transform (DCT) of the input sequence. |
| InvDCT2D | Computes the two-dimensional inverse Discrete Cosine Transform (DCT) of the input signal. |
| InvDST | Computes the one-dimensional inverse Discrete Sine Transform (DST) of the input signal inputArray. |
| InvDST2D | Computes the two-dimensional inverse Discrete Sine Transform (DST) of the input signal. |
| InvFFT | Calculates the inverse fast Fourier transform (inverse FFT) of the complex data. |
| InvFFT2D | Computes the real two-dimensional inverse fast Fourier transform (inverse FFT) of the input signal. |
| InvFFTEx | Computes the real inverse fast Fourier transform (inverse FFT) of an input sequence. |
| InvFHT | Calculates the inverse fast Hartley transform (FHT). |
| InvFastHilbertTransform | Computes the inverse fast Hilbert transform of the input sequence. |
| LinEv1D | Performs a linear evaluation of a 1D array. |
| LinEv2D | Performs a linear evaluation of a 2D array. |
| MaxMin1D | Finds the maximum and minimum values in the input array and their locations in the array. |
| MaxMin2D | Finds the maximum and the minimum values in the 2D input array and their locations in the array. |
| MedianFilter | Filters the input array using a median filter. |
| Mul1D | Multiplies two 1D arrays, element by element. |
| Mul2D | Multiplies two 2D arrays, element by element. |
| Neg1D | Negates the elements of the input array. |
| Normal1D | Normalizes a 1D input vector. |
| Normal2D | Normalizes a 2D input matrix. |
| NormalizedCorrelate | Finds the correlation of the input arrays. |
| PeriodNoise | Generates an array containing periodic pseudorandom noise. |
| PeriodicSinc | Generates a periodic sinc pattern. |
| PoissonNoise | Generates an array containing a Poisson-distributed pseudorandom pattern of values that are the number of discrete events that occur in the interval specified by the mean of a unit rate Poisson process. |
| PolyEv1D | Performs a polynomial evaluation on the input array. |
| PolyEv2D | Performs a polynomial evaluation on a 2D input array. |
| Prod1D | Finds the product of the elements of the input array. |
| Pulse | Generates an array that represents the pattern of a pulse waveform. |
| QScale1D | Finds the maximum absolute value in the array and produces a scaled array. |
| QScale2D | Scales a 2D input array by its maximum absolute value. |
| Ramp | Generates an output array that represents a ramp pattern. |
| ReFFT | Calculates the fast Fourier transform (FFT) of a real input array. |
| ReInvFFT | Calculates the inverse fast Fourier transform (inverse FFT) of a complex sequence that results in a real output array. |
| ResetIIRFilter | Sets the reset flag in the filterInfo filter structure so that the internal filter state information is reset to zero before the next cascade IIR filtering operation. |
| Reverse | Reverses the order of the elements of the input array. |
| RichtmeyerSeq | Generates an array containing a quasi-random Richtmeyer sequence, which is a low-discrepancy number sequence that uniformly distributes in the interval [0, 1]. |
| RiffleArray | Riffles an input array of double-precision elements by randomly selecting two elements in inputArray, swapping those elements, and then repeating this process numberOfElements times, where numberOfElements is the size of inputArray. |
| SawtoothWave | Generates an array that contains a sawtooth wave. |
| Scale1D | Scales the input array and returns the scale and offset constants. |
| Scale2D | Scales the input array and returns the scale and offset constants. |
| Set1D | Sets the elements of an array to a specified constant value. |
| Shift | Shifts the elements of the input array a specified number of places. |
| Sinc | Generates an array that contains a sinc pattern. |
| SinePattern | Generates an array with a sinusoidal pattern. |
| SineWave | Generates an array that contains a sine wave. |
| Sort | Sorts the input array in ascending or descending order. |
| Spectrum | Calculates the power spectrum of the input array. |
| SquareWave | Generates an array that contains a square wave. |
| Sub1D | Subtracts two 1D arrays, element by element. |
| Sub2D | Subtracts two 2D arrays, element by element. |
| Subset1D | Extracts a subset of the input array containing the number of elements specified by length and starting at index element. |
| Sum1D | Finds the sum of the elements of the input array. |
| Sum2D | Finds the sum of the elements in the input 2D array. |
| ToPolar | Converts the rectangular coordinates (xReal, xImg) to polar coordinates (magnitude, phase). |
| ToPolar1D | Converts the set of rectangular coordinate points (arrayXReal, arrayXImaginary) to a set of polar coordinate points (magnitude, phaseRadians). |
| ToRect | Converts the polar coordinates (magnitude, phase) to rectangular coordinates (xReal, xImg). |
| ToRect1D | Converts the set of polar coordinate points (magnitude, phase) to a set of rectangular coordinate points (outputReal, outputImg). |
| Triangle | Generates an output array that has a triangular pattern. |
| TriangleWave | Generates an array that contains a triangle wave. |
| TriggerDetection | Finds the first level-crossing location in a waveform. |
| TriggerDetection2D | Finds the first level-crossing location in multiple channel waveforms. |
| UnWrap1D | Unwraps phase information obtained from ToPolar1D so that the phase information exhibits a linear and continuous curve when plotted. |
| UnWrap1DByUnit | Unwraps phase by eliminating discontinuities whose absolute values exceed either pi or 180. |
| Uniform | Generates an array of random numbers that are distributed uniformly between zero and one. |
| UnsymmetricTriangle | Generates an unsymmetric triangle array. |
| WhiteNoise | Generates an array of random numbers that are uniformly distributed between -amplitude and amplitude. |
| ZeroPhaseFiltering | Filters the input sequence using a zero-phase filter. |
| ACDCEstimator | Calculates an estimation of the AC and DC contents of the input signal. |
| ANOVA1Way | Takes an array of experimental observations you make at various levels of some factor, with at least one observation per factor, and performs a one-way analysis of variance (ANOVA) in the fixed effect model. |
| ANOVA2Way | Takes an array of experimental observations made at various levels of two factors and performs a two-way analysis of variance in Model 1, Model 2, Model 3, or Model 4. |
| ANOVA3Way | Takes an array of experimental observations made at various levels of three factors and performs a three-way analysis of variance in Model 1, Model 2, or Model 3. |
| Airy | Computes the Airy functions. |
| AllocFIRFilterPtr | Allocates and initializes the FIR filterInformation structure. |
| AmpPhaseSpectrum | Calculates the single-sided, scaled amplitude and phase spectra of a time-domain signal, x. |
| AutoCorrMtrx | Computes the autocorrelation matrix of the input array inputArray. |
| AutoPowerSpectrum | Calculates the single-sided, scaled auto power spectrum of a time-domain signal. |
| BackSub | Solves linear equations AX=Y using backward substitution. |
| BartHannWin | Applies a modified Bartlett-Hann window to a real signal. |
| Bessel1st | Computes the Bessel function Jr(x) of the first kind of fractional order r. |
| Bessel2nd | Computes the Bessel function Yr(x) of the second kind of fractional order r, also known as the Neumann function. |
| Beta | Computes the beta or incomplete beta function. |
| BkmanWin | Applies a Blackman window to a real signal. |
| BlkHarrisWin | Applies a 3-term Blackman-Harris window to a real signal. |
| BlkmanNuttallWin | Applies a Blackman-Nuttall window to a real signal. |
| BohmanWin | Applies a Bohman window to a real signal. |
| ChebWin | Applies an unsymmetrical Dolph-Chebyshev window to a real signal. |
| CheckPosDef | Checks the positive definiteness of the real square input matrix. |
| Cholesky | Calculates the Cholesky factorization of a real, symmetric positive definite input matrix. |
| ConditionNumber | Calculates the condition number of a real input matrix. |
| Contingency_Table | Creates a contingency table in which to classify and tally objects of experimentation according to two schemes of categorization. |
| CosIntegral | Computes the cosine integral. |
| CosTaperedWin | Applies a cosine-tapered window to the input signal. |
| CosTaperedWinEx | Applies a cosine tapered window to a real signal. |
| CoshIntegral | Computes the hyperbolic cosine integral. |
| CrossPowerSpectrum | Calculates the single-sided, scaled cross power spectrum of two time-domain signals. |
| CubicSplineFit | Uses cubic spline fitting to fit the data set (x, y). |
| CxAutoCorrMtrx | Computes the autocorrelation matrix of the complex input array inputArray. |
| CxBartHannWin | Applies a modified Bartlett-Hann window to a complex signal. |
| CxBkmanWin | Applies a Blackman window to the complex input signal. |
| CxBlkHarrisWin | Applies a 3-term Blackman-Harris window to the complex input signal. |
| CxBlkmanNuttallWin | Applies a Blackman-Nuttall window to a complex signal. |
| CxBohmanWin | Applies a Bohman window to a complex signal. |
| CxChebWin | Applies an unsymmetrical Dolph-Chebyshev window to a complex signal. |
| CxCheckPosDef | Checks if the complex, square input matrix is positive definite. |
| CxCholesky | Calculates the Cholesky factorization of a complex, symmetric positive definite input matrix. |
| CxConditionNumber | Calculates the condition number of a complex input matrix. |
| CxCosTaperedWin | Applies a cosine tapered window to a complex signal. |
| CxDeterminant | Calculates the complex determinant of a square, complex input matrix. |
| CxDotProduct | Calculates the dot product of the complex input arrays. |
| CxEigenVBack | Transforms the complex eigenvectors of a balanced matrix to those of the original matrix. |
| CxEigenValueVector | Calculates the eigenvalues λ and the corresponding eigenvectors x of a complex, square input matrix A. |
| CxEquiRpl_BPFiltering | Filters the complex array using an optimal bandpass FIR linear phase filter with equi-ripple characteristics. |
| CxEquiRpl_BSFiltering | Filters the complex array using an optimal bandstop FIR linear phase filter with equi-ripple characteristics. |
| CxEquiRpl_HPFiltering | Filters the complex array using an optimal highpass FIR linear phase filter with equi-ripple characteristics. |
| CxEquiRpl_LPFiltering | Filters the complex array using an optimal lowpass FIR linear phase filter with equi-ripple characteristics. |
| CxExBkmanWin | Applies an exact Blackman window to the complex input signal. |
| CxExpWin | Applies an exponential window to the complex input signal. |
| CxFIRNarrowBandFilter | Filters the complex input sequence using the FIR narrowband filter specified by the filterInformation structure. |
| CxFlatTopWin | Applies a flat top window to the complex input signal. |
| CxForceWin | Applies a force window to the complex input signal. |
| CxGaussWin | Applies a Gaussian window to a complex input signal. |
| CxGenCosWin | Applies a general cosine window to the complex input signal. |
| CxGenEigenAB | Computes the generalized eigenvalues, and optionally the left and/or right generalized eigenvectors, for a pair of complex matrices (A,B). |
| CxGenInvMatrix | Calculates the inverse of a complex, square input matrix. |
| CxGenLinEqs | Solves for the unknown vector x in the linear system of equations. |
| CxHamWin | Applies a Hamming window to the complex input signal. |
| CxHanWin | Applies a Hanning window to the complex input signal. |
| CxHess | Calculates the Hessenberg decomposition for a complex matrix A. |
| CxKroneckerProd | Computes the Kronecker product result matrix. |
| CxKsrWin | Applies a Kaiser window to the complex input signal. |
| CxLU | Performs an LU decomposition on the complex, square matrix A. |
| CxMatrixBalance | Balances a general complex matrix so that its eigenvectors can be computed more accurately. |
| CxMatrixMul | Multiplies two complex matrices. |
| CxMatrixNorm | Calculates the norm of the complex input matrix A. |
| CxMatrixRank | Calculates the rank of the complex input matrix. |
| CxMatrixVectorMul | Multiplies a complex matrix and a complex vector. |
| CxMultipleToneInfo | Returns the frequency, amplitude, and phase for each signal tone whose amplitude exceeds a specified threshold. |
| CxMultipleToneSignal | Returns the frequency, amplitude, and phase for each signal tone whose amplitude exceeds a specified threshold. |
| CxOuterProduct | Calculates the outer product of the complex input vectors x and y. |
| CxParzenWin | Applies a Parzen window to a complex signal. |
| CxPolyRoots | Calculates the roots of a real polynomial. |
| CxPolyRootsEx | Calculates the roots of a complex polynomial with high precision. |
| CxPseudoInverse | Calculates the generalized inverse of the complex input matrix A. |
| CxQR | Calculates the QR factorization of the complex input matrix. |
| CxQREx | Performs the QR factorization for a complex matrix. |
| CxQZ | Performs the QZ decomposition of a pair of complex matrices (A,B). |
| CxRMS | Computes the root mean square of the input sequence inputArray. |
| CxSVD | Calculates the Singular Value Decomposition (SVD) factorization of the complex input matrix. |
| CxSVDEx | Calculates the Singular Value Decomposition (SVD) factorization for a complex matrix. |
| CxSVDS | Calculates only the singular values that result from the Singular Value Decomposition (SVD) factorization of the complex input matrix. |
| CxScaledWindow | Applies a scaled window to a complex signal. |
| CxSchur | Performs the Schur decomposition of a complex matrix A. |
| CxSingleToneInfo | Takes a complex signal, finds the single tone with the highest amplitude or searches a specified frequency range, and returns the single tone frequency, amplitude, and phase. |
| CxSingleToneSignal | Takes a complex signal, finds the single tone with the highest amplitude or searches a specified frequency range, and returns the single tone frequency, amplitude, and phase. |
| CxSolveEqs | Solves complex linear equations of the format AX = B. |
| CxSpecialMatrix | Generates a special type of complex matrix depending on the value of matrixType. |
| CxSymWin | Applies a symmetric window to a complex signal. |
| CxTrace | Calculates the trace of a complex matrix. |
| CxTranspose | Calculates the complex conjugate transpose of a 2D, complex input matrix. |
| CxTriWin | Applies a triangular window (Bartlett window) to the complex input signal. |
| CxUnitVector | Finds the norm of the complex input array and obtains its corresponding unit vector by normalizing the input array with the norm. |
| CxWelchWin | Applies a Welch window to a complex input signal. |
| CxWindFIR_Filtering | Filters the complex array using the set of windowed FIR filter coefficients. |
| CxWind_BPFiltering | Filters the complex array using the set of windowed FIR bandpass filter coefficients. |
| CxWind_BSFiltering | Filters the complex array using the set of windowed FIR bandstop filter coefficients. |
| CxWind_HPFiltering | Filters the complex array using the set of windowed FIR highpass filter coefficients. |
| CxWind_LPFiltering | Filters the complex array using the set of windowed FIR lowpass filter coefficients. |
| CycleRMSAverage | Returns the average and RMS levels of a waveform in one user-defined cycle. |
| Dawson | Computes Dawson's integral. |
| Determinant | Finds the determinant of an n-by-n 2D input matrix. |
| Dilogarithm | Computes the dilogarithm function, also known as Spence's Integral. |
| DotProduct | Calculates the dot product of the real input vectors. |
| EigenVBack | Transforms the eigenvectors of a balanced matrix to those of the original matrix. |
| Elliptic1st | Computes the elliptic integral or the incomplete elliptic integral of the first kind. |
| Elliptic2nd | Computes the elliptic or incomplete elliptic integral of the second kind. |
| Elp_Coef | Generates the set of filter coefficients to implement an IIR filter as specified by the elliptic (or Cauer) filter model. |
| EquiRpl_BPF | Designs an optimal bandpass FIR linear phase filter using the Parks-McClellan algorithm. |
| EquiRpl_BPFiltering | Filters the real array using a optimal bandpass FIR linear phase filter with equi-ripple characteristics. |
| EquiRpl_BSF | Designs a bandstop FIR linear phase filter using the Parks-McClellan algorithm. |
| EquiRpl_BSFiltering | Filters the real array using a optimal bandstop FIR linear phase filter with equi-ripple characteristics. |
| EquiRpl_HPF | Designs an optimal highpass FIR linear phase filter using the Parks-McClellan algorithm. |
| EquiRpl_HPFiltering | Filters the real array using a optimal highpass FIR linear phase filter with equi-ripple characteristics. |
| EquiRpl_LPF | Designs an optimal lowpass FIR linear phase filter using the Parks-McClellan algorithm. |
| EquiRpl_LPFiltering | Filters the real array using a optimal lowpass FIR linear phase filter with equi-ripple characteristics. |
| Equi_Ripple | Designs a multiband FIR linear phase filter, a differentiator, or a Hilbert Transform using the Parks-McClellan algorithm that you can adjust by a weighting factor. |
| Erf | Evaluates the error function at the input value. |
| Erfc | Evaluates the complementary error function, Erfc(x), where Erfc(x) = 1.0 - Erf(x) and Erf(x) is the error function evaluated at x. |
| ExBkmanWin | Applies an exact Blackman window to a real signal. |
| ExpFit | Finds the coefficient values that best represent the exponential fit of the data points (x, y) using the Least Square method. |
| ExpFitEx | Fits the data set (x, y) to the exponential model using the Least Square, Least Absolute Residual, or Bisquare method. |
| ExpFitInterval | Calculates the confidence interval for the best exponential fitting function or the prediction interval for the observations. |
| ExpIntegral | Computes the exponential integral function. |
| ExpWin | Applies an exponential window to a real signal. |
| FIRFiltering | Filters the input sequence using the direct-form FIR filter. |
| FIRFiltering_CxInput | Filters the complex input signal using the direct-form FIR filter. |
| FIRNarrowBandCoef | Designs a set of filter coefficients to implement a digital interpolated FIR (IFIR) filter. |
| FIRNarrowBandFilter | Filters the real input sequence using the FIR narrowband filter specified by the coefinfo structure. |
| FIR_Coef | Generates a set of FIR filter coefficients based on the window design method. |
| F_Dist | Calculates the one-sided probability. |
| Fact | Computes the factorial of n. |
| FlatTopWin | Applies a flat top window to a real signal. |
| ForceWin | Applies a force window to a real signal. |
| ForwSub | Solves linear equations AX=Y using forward substitution. |
| FreeAnalysisMem | Frees the memory that PeakDetector allocated internally for the output arguments. |
| FreeFIRFilterPtr | Frees the FIR interpolated filter structure and all internal arrays. |
| FresnelIntegrals | Computes the Fresnel sine and cosine integrals. |
| Gamma | Evaluates the gamma function or the incomplete gamma function, depending on the value of a. |
| GammaC | Computes the complementary incomplete gamma function. |
| GaussFit | Fits the data set (x, y) to the Gaussian model using the Least Square, Least Absolute Residual, or Bisquare method. |
| GaussFitInterval | Calculates the confidence interval for the best Gaussian fitting function or the prediction interval for the observations. |
| GaussHG | Computes the Gauss hypergeometric function. |
| GaussHypergeometric | Computes the Gauss hypergeometric function. |
| GaussWin | Applies a Gaussian window to a real signal. |
| GenCosWin | Applies a general cosine window to a real signal. |
| GenDeterminant | Calculates the determinant of the real, square input matrix A. |
| GenEigenAB | Computes the generalized eigenvalues and, optionally, the left and/or right generalized eigenvectors for a pair of real matrices (A, B). |
| GenEigenValueVector | Calculates the eigenvalues λ and the corresponding eigenvectors x of a real, square input matrix. |
| GenInvMatrix | Calculates the inverse of the real, square input matrix. |
| GenLSFit | Finds the best fit k-dimensional plane and the set of linear coefficients using the least chi-squares method for observation data sets. |
| GenLSFitCoef | Finds the set of linear fit coefficients, which describe the linear curve that best represents the input data that GenLSFitCoef uses to obtain the least squares solution technique. |
| GenLinEqs | Solves for the unknown vector x in the linear system of equations. |
| GetAnalysisErrorString | Returns the error message associated with the Analysis Library error code specified in the errorNumber parameter. |
| GetWinProperties | Gets the properties, including equivalent noise bandwidth (ENBW) and coherent gain, of the selected window. |
| GoodnessOfFit | Calculates three parameters, sse, rSquare, and rmse, which describe how well a fitted model matches the original data set. |
| HamWin | Applies a Hamming window to a real signal. |
| HanWin | Applies a Hanning window to a real signal. |
| HarmonicAnalyzer | Finds the amplitude and frequency of the fundamental and harmonic components present in autoPowerSpectrum. |
| HarmonicAnalyzerUsingSignal | Finds the amplitude levels and frequency tones of the fundamental and harmonic components and calculates the percent of total harmonic distortion and the total harmonic distortion plus noise. |
| Hess | Performs a Hessenberg decomposition of a real matrix A such that A = QHQH, where Q is the orthogonal matrix, H is the Hessenberg matrix, and QH is the transpose of Q. |
| Histogram | Calculates the histogram of the inputArray. |
| IIRFiltering | Filters the input sequence using the IIR filter specified by reverse coefficients aCoefficientArray and forward coefficients bCoefficientArray. |
| IIRFiltering_CxInput | Filters the complex input signal using the direct-form IIR filter, which supports in-place operations. |
| ImpulseResponse | Calculates the impulse response of a network based on time-domain signals stimulus and response. |
| InvF_Dist | Calculates f, given a probability (0 ≤ p < 1), such that: prob(F < f) = p, where f is a random variable from an F-distribution with the specified degrees of freedom. |
| InvMatrix | Finds the inverse matrix of a square matrix. |
| InvN_Dist | Calculates x, given a probability (0 < p < 1), such that: prob(X < x) = p, where x is a random variable from a standard normal distribution. |
| InvT_Dist | Calculates t, given a probability (0 < p < 1), such that: prob(T < t) = p, where t is a random variable from a T-distribution with the specified degrees of freedom. |
| InvXX_Dist | Calculates xx, given a probability (0 ≤ p < 1), such that: prob(chi < x) = p, where chi is a random variable from a chi-square distribution with the specified degrees of freedom. |
| JacobiEllipticI | Determines the Jacobian elliptic functions cn, dn, and sn. |
| Kelvin1st | Computes the complex Kelvin function of the first kind. |
| Kelvin2nd | Computes the complex Kelvin function of the second kind. |
| KroneckerProd | Computes the Kronecker product result matrix. |
| KsrWin | Applies a Kaiser window to a real signal. |
| Ksr_BPF | Designs a digital bandpass FIR linear phase filter using a Kaiser window. |
| Ksr_BSF | Designs a digital bandstop FIR linear phase filter using a Kaiser window. |
| Ksr_HPF | Designs a digital highpass FIR linear phase filter using a Kaiser window. |
| Ksr_LPF | Designs a digital lowpass FIR linear phase filter using a Kaiser window. |
| Kummer | Computes the Kummer function, also known as the confluent hypergeometric M function. |
| LU | Performs an LU matrix decomposition. |
| LinEqs | Solves the linear system of equations |
| LinFit | Finds the slope and intercept values that best represent the linear fit of the data points (x, y) using the Least Square method. |
| LinearFitEx | Fits the data set (x, y) to the linear model using the Least Square, Least Absolute Residual, or Bisquare method. |
| LinearFitInterval | Calculates the confidence interval for the best linear fitting function or the prediction interval for the observations. |
| LnFact | Computes the natural logarithm of n!. |
| LnGamma | Computes the natural logarithm of the gamma function. |
| LogFit | Fits the data set (x, y) to the logarithm model using the Least Square, Least Absolute Residual, or Bisquare method. |
| LogFitInterval | Calculates the confidence interval for the best logarithm fitting function or the prediction interval for the observations. |
| MatrixBalance | Balances a general matrix so that its eigenvectors can be computed more accurately. |
| MatrixMul | Multiplies two 2D input matrices, X and Y. |
| MatrixNorm | Calculates the norm of a real input matrix A. |
| MatrixRank | Calculates the rank of the real input matrix. |
| MatrixVectorMul | Multiplies a real matrix and a real vector: A*x=y. |
| Mean | Calculates the mean, or average, value of the input array. |
| Median | Finds the median value of the input array. |
| ModBessel1st | Computes the modified Bessel function of the first kind of order r. |
| ModBessel2nd | Computes the modified Bessel function Kr = K(r,x) of the second kind of integer order r. |
| Mode | Finds the mode of the input array. |
| ModeEx | Finds the mode(s) of a list of numbers. |
| Moment | Calculates the moment about the mean of the input array with the specified order. |
| MultipleToneInfo | Returns the frequency, amplitude, and phase for each signal tone whose amplitude exceeds a specified threshold. |
| MultipleToneSignal | Returns the frequency, amplitude, and phase for each signal tone whose amplitude exceeds a specified threshold. |
| N_Dist | Calculates the one-sided probability. |
| NameWinProperties | Computes the coherent gain and equivalent noise bandwidth of a window by window type. |
| NetworkFunctions | Calculates the single-sided coherence function along with the averaged single-sided cross power spectrum, averaged single-sided frequency response, or transfer function, and impulse response, from a 2D array of stimulus signals and a 2D array of response signals. |
| NonLinearFit | Uses the Levenberg-Marquardt algorithm to determine the least squares set of coefficients that best fit the set of input data points (x, y) as expressed by a nonlinear function y = f(x, a) where a is the set of coefficients. |
| NonLinearFitWithMaxIters | Uses the Levenberg-Marquardt algorithm to determine the least squares set of coefficients that best fit the set of input data points (x, y) as expressed by a nonlinear function y = f(x, a) where a is the set of coefficients. |
| NonLinearFitWithWeight | Uses the Levenberg-Marquardt algorithm to determine the least squares set of coefficients that best fit the set of input data points (x, y) as expressed by a nonlinear function y = f(x, a) where a is the set of coefficients. |
| NumericIntegration | Performs numeric integration on the data the input array contains. |
| NumericWinProperties | Computes the coherent gain and equivalent noise bandwidth of a window numerically. |
| OuterProduct | Calculates the outer product of the real input vectors x and y. |
| ParabolicCylinder | Computes the parabolic cylinder function, Dv(x). |
| Parks_McClellanCoef | Designs a set of linear-phase FIR multiband digital filter coefficients. |
| ParzenWin | Applies a Parzen window to a real signal. |
| PeakDetector | Finds the location, amplitude, and second derivatives of peaks or valleys in the input array. |
| PolyFit | Finds the coefficients that best represent the polynomial fit of the data points (x, y) using the Least Square method. |
| PolyFitEx | Fits the data set (x, y) to a polynomial model using the Least Square method. |
| PolyFitWithWeight | Fits the data set (x, y) to a polynomial model using the Least Square method. |
| PolyInterp | Calculates the value of the unique polynomial P of degree (numberOfElements - 1) passing through the numberOfElements points (xi, f(xi)) at x_value and returns an estimate of the error in the interpolation, given a set of numberOfElements points (xi, f(xi)) in the plane where f is some function and given a value x_value at which f is interpolated or extrapolated. |
| PolyRootsEx | Calculates the roots of a real polynomial with high precision. |
| PowerFit | Fits the data set (x, y) to the power model using the Least Square, Least Absolute Residual, or Bisquare method. |
| PowerFitInterval | Calculates the confidence interval for the best power fitting function or the prediction interval for the observations. |
| PowerFrequencyEstimate | Calculates the estimated power and frequency around a peak in the power spectrum of a time-domain signal. |
| PseudoInverse | Calculates the generalized inverse of the real input matrix A. |
| Psi | Computes the digamma (Psi) function. |
| PulseMeas | Calculates the period, pulseDuration (pulse width), pulseCenter, and dutyCycle (duty factor) of a waveform in user-defined cycle. |
| QR | Calculates the QR factorization of the real input matrix. |
| QREx | Calculates the QR factorization for a real matrix. |
| QZ | Performs the QZ decomposition of a pair of real matrices (A, B). |
| RMS | Calculates the root-mean-square (rms) value of the input array. |
| RatInterp | Returns the value of a particular rational function P(x)/Q(x) passing through the numberOfElements points (xi, f(xi)) at x_value, given a set of numberOfElements points (xi, f(xi)) in the plane where f is some function, and a value x_value at which f is to be interpolated. |
| RemoveOutlierByIndex | Removes the outliers specified by indices. |
| RemoveOutlierByRange | Removes the outliers according to the input range. |
| SVD | Calculates the singular value decomposition (SVD) factorization of the real input matrix. |
| SVDEx | Computes the singular value decomposition (SVD) of a real matrix. |
| SVDS | Calculates only the singular values that result from the singular value decomposition factorization of the real input matrix. |
| SavitzkyGolayCoef | Designs a Savitzky-Golay smoothing FIR filter. |
| SavitzkyGolayFiltering | Applies a Savitzky-Golay smoothing FIR filter to the sequence inputSequence. |
| SavitzkyGolayFiltering_CxInput | Applies a Savitzky-Golay smoothing FIR filter to the complex sequence inputSequence. |
| ScaledWindow | Applies a scaled window to the time-domain signal and returns window constants for further analysis. |
| ScaledWindowEx | Applies a scaled window to a real signal. |
| Schur | Computes the Schur decomposition of a real matrix A. |
| SinIntegral | Computes the sine integral. |
| SingleToneInfo | Takes a real signal, finds the single tone with the highest amplitude or searches a specified frequency range, and returns the single tone frequency, amplitude, and phase. |
| SingleToneSignal | Takes a signal, finds the single tone with the highest amplitude or searches a specified frequency range, and returns the single tone frequency, amplitude, and phase. |
| SinhIntegral | Computes the hyperbolic sine integral. |
| SolveEqs | Solves real linear equations as follows: AX = B. |
| SpInterp | Performs a cubic spline interpolation of the function f at a value x_value, where x_value is in the same range as xi, given a tabulated function of the form yi = f(xi) for i = 0, 1, . . ., numberOfElements - 1, with x < xi + 1, and given the second derivatives that specify the interpolant at the numberOfElements nodes of arrayX. |
| SpecialMatrix | Generates a special type of real matrix depending on the value of matrixType. |
| SpectrumUnitConversion | Converts the input spectrum, which is the power, amplitude, or gain, to alternate formats such as log, decibels or dBm, and spectral density. |
| SphBessel1st | Computes the spherical Bessel function of the first kind of order n. |
| SphBessel2nd | Computes the spherical Bessel function of the second kind of order n. |
| Spline | Calculates the second derivatives used by the cubic spline interpolant, given a tabulated function of the form yi = f(xi) for i = 0, 1, . . ., numberOfElements - 1, with xi < xi + 1, and given the boundary conditions firstBoundary and secondBoundary such that the interpolant's second derivative matches the specified values at x0 and xn - 1. |
| StateLevels | Calculates the high state level, low state level, and amplitude of a waveform. |
| StdDev | Calculates the standard deviation and the mean, or average, values of the input array. |
| Stirling | Computes the Stirling approximation to the gamma function. |
| Struve | Computes the Struve function. |
| SymEigenValueVector | Calculates the eigenvalues λ and the corresponding eigenvectors x of a real, symmetric square input matrix A. |
| SymWin | Applies a symmetric window to a real signal. |
| T_Dist | Calculates the one-sided probability. |
| ThresholdPeakDetector | Analyzes the input sequence for valid peaks. |
| Trace | Computes the trace of a real matrix. |
| TransMeas | Calculates the slope, transition duration, undershoot, and overshoot at pre-transition and over-transition region in one user-defined cycle. |
| TransferFunction | Calculates the single-sided transfer function, also known as the frequency response, from the time-domain stimulus signal and the time-domain response signal of a network under test. |
| Transpose | Computes the transpose of a real matrix. |
| TriWin | Applies a triangular window (Bartlett window) to a real signal. |
| Tricomi | Computes the Tricomi function, which is also known as the associated confluent hypergeometric U function. |
| UnitVector | Finds the norm of the input array and obtains its corresponding unit vector by normalizing the input array with the norm. |
| Variance | Calculates the variance and the mean, or average, values of the input array. |
| WelchWin | Applies a Welch window to a real signal. |
| WindFIR_Filter | Generates windowed FIR filter coefficients, which compute only FIR coefficients. |
| WindFIR_Filtering | Filters the real array using the set of windowed FIR filter coefficients. |
| Wind_BPF | Designs a digital bandpass FIR linear phase filter using a windowing technique. |
| Wind_BPFiltering | Filters the real array using the set of windowed FIR bandpass filter coefficients. |
| Wind_BSF | Designs a digital bandstop FIR linear phase filter using a windowing technique. Five windows are available. Wind_BSF generates only the filter coefficients; it does not actually perform data filtering. |
| Wind_BSFiltering | Filters the real array using the set of windowed FIR bandstop filter coefficients. |
| Wind_HPF | This function, superseded by WindFIR_Filter, designs a digital highpass FIR linear phase filter using a windowing technique. |
| Wind_HPFiltering | Filters the real array using the set of windowed FIR highpass filter coefficients. |
| Wind_LPF | Designs a digital lowpass FIR linear phase filter using a windowing technique. Five windows are available. |
| Wind_LPFiltering | Filters the real array using the set of windowed m lowpass filter coefficients. |
| XX_Dist | Approximates the one-sided probability. |
| Zeta | Computes the Riemann Zeta function. |

Parent topic:

C Node Overview

<!--NI_TOPIC bundle=labview-nxg-ansi-c-api-ref path=ansi-c-lib.html language=enus -->
## TOPIC 00002: ANSI C Library Function Reference

- bundle_id: `labview-nxg-ansi-c-api-ref`
- source_path: `ansi-c-lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ansi-c-api-ref/raw/resource/enus/ansi-c-lib.html
- document_id: `labview-nxg-ansi-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists available ANSI C Library functions. Clicking a link in this table opens a topic in the LabWindows/CVI Help in a new browser tab. Function Description _getmbcp Returns the code page currently used by the operating system. _ismbblead Returns TRUE if its input byte is a valid

ANSI C Library Function Reference

The following table lists available ANSI C Library functions. Clicking a link in this table opens a topic in the LabWindows/CVI Help in a new browser tab.

| Function | Description |
| --- | --- |
| _getmbcp | Returns the code page currently used by the operating system. |
| _ismbblead | Returns TRUE if its input byte is a valid lead byte in the current code page. |
| _mbsbtype | Determines the type of the byte in the context string at the given offset. |
| _mbscat | Appends a copy of a source string to the end of a target string. |
| _mbschr | Locates the first occurrence of the specified character in a string. |
| _mbscmp | Compares two NUL-terminated strings. |
| _mbscpy | Copies a source string, including the terminating ASCII NUL byte, into a target string. |
| _mbscspn | Locates the first occurrence in a string of any character from the specified character set. |
| _mbsdec | Moves a character pointer to the previous character in a multibyte character string. |
| _mbsicmp | Compares two NUL-terminated strings. |
| _mbsinc | Moves a character pointer in a multibyte character string to the next character. |
| _mbslen | Returns the length of the specified string up to, but not including, the terminating ASCII NUL byte. |
| _mbsnbcat | Appends a specified number of bytes from a source string to the end of a target string. |
| _mbsnbcmp | Compares a specified number of bytes from two NUL-terminated strings. |
| _mbsnbcpy | Copies a specified number of bytes from a source string to a target string. |
| _mbsnbicmp | Compares not more than a specified amount of bytes of two NUL-terminated strings. |
| _mbspbrk | Locates the first occurrence in a string of any character from the specified character set. |
| _mbsrchr | Locates the last occurrence of the specified character in a given string. |
| _mbsspn | Returns the length in bytes of the initial segment of a string that contains only characters from the specified set of characters. |
| _mbsstr | Locates the first occurrence of a sequence of characters, excluding the terminating ASCII NUL byte, in a string. |
| _mbstok | Breaks a string into tokens, which are separated by one or more characters from the specified set of delimiters. |
| _putenv | Adds or replaces an entry in the environment list of the host environment. |
| abs | Computes the absolute value of the specified integer input value. |
| acos | Computes the principal value of the arc cosine of the specified argument. |
| alloca | Allocates space on the stack for an object of specified size. |
| asctime | Takes a date and time stored in a struct tm and converts it into a string. |
| asin | Computes the principal value of the arc sine of the specified argument. |
| atan | Returns the arc tangent of the specified argument. |
| atan2 | Computes the principal value of the arc tangent of (yValue/xValue) using the signs of both arguments to determine the quadrant of the return value. |
| atof | Converts the initial portion of a string to a double representation. |
| atoi | Converts the initial portion of a string to an int representation. |
| atol | Converts the initial portion of a string to a long int representation. |
| atoll | Converts the initial portion of a string to a long long int representation. |
| bsearch | Searches an array of objects for an element that matches a specified key. |
| calloc | Allocates memory space for an array of elements in which an element's size is specified by elementSize and total number of elements is specified by number_ofElements. |
| ceil | Computes the smallest integer value not less than the specified argument by rounding the input value up to the next highest integer. |
| clearerr | Clears the end-of-file and error indicators for the specified stream. |
| clock | Returns the number of system clock cycles that have occurred since the program started executing. |
| close | Flushes the system buffers for the specified file handle and closes the associated file. |
| cos | Computes the cosine of the specified argument. |
| cosh | Computes the hyperbolic cosine of the specified argument. |
| ctime | Converts the current time to a human-readable string. |
| difftime | Computes the difference between two calendar times. |
| div | Divides numerator by denominator. |
| eof | Tests the end-of-file indicator for the specified handle. |
| exp | Computes the exponential function of the specified argument. |
| fabs | Computes the absolute value of a double. |
| fclose | Flushes the specified I/O stream and closes the associated file. |
| fdopen | Obtains a pointer to a buffered I/O stream from a file handle returned by the open or sopen (Windows only) functions. |
| feof | Tests the end-of-file indicator for the specified stream. |
| ferror | Tests the error indicator for the specified stream. |
| fflush | Flushes the I/O buffer of the specified stream. |
| fgetc | Reads the next character from the specified input stream and advances the associated file position indicator. |
| fgetpos | Obtains the current value of the file position indicator for the specified stream. |
| fgets | Reads characters from the specified input stream into a lineBuffer until end-of-file is encountered, a newline character is read, or (number_ofChars - 1) characters are read. |
| floor | Computes the largest integer value not greater than the specified argument by rounding the input value down to the next lowest integer. |
| fmod | Computes the floating-point remainder of the division of two double values and returns the result. |
| fopen | Opens the specified file according to the designated mode. |
| fprintf | Writes output to the specified stream according to format specifiers in formatString. |
| fputc | Writes the specified character to an output stream and advances the file position indicator. |
| fputs | Writes a string (not including a terminating ASCII NUL byte) to the specified output stream. |
| fread | Reads a block of data from the specified input stream then stores it in the specified buffer. |
| free | Causes the space pointed to by memBlockPointer to be deallocated. |
| freopen | Attempts to close the file that is associated with oldStream, opens a file and associates it with the I/O stream that is pointed to by oldStream, and clears error and end-of-file indicators for the I/O stream. |
| frexp | Splits a floating-point value into two parts: the mantissa (a normalized fraction with magnitude in the interval [0.5,1) or zero) and the exponent (an integral power of two). |
| fscanf | Reads input from the specified stream and converts it into a series of values according to the specifications of the formatting string. |
| fseek | Sets the file position indicator for the specified stream. |
| fsetpos | Sets the file position indicator for the specified stream according to the value obtained from an earlier call to fgetpos. |
| ftell | Returns the current value of the file position indicator for the specified stream. |
| fwrite | Writes a block of data to the specified output stream. |
| getc | Reads the next character from the specified input stream and advances the file position indicator. |
| getenv | Searches for the environment string that matches the specified environment name and returns the associated value to the string. |
| gmtime | Takes a calendar time, breaks it into its component parts, and stores the result in a struct tm. |
| isalnum | Tests to see if a character is alphanumeric (a-z, A-Z, 0-9). |
| isalpha | Tests to see if a character is alphabetic (a-z, A-Z). |
| iscntrl | Tests to see if a character is a control character (any character whose value is from 0 to 31). |
| isdigit | Tests to see if a character is a decimal digit (0-9). |
| isgraph | Tests to see if a character is a printable, non-whitespace character. |
| islower | Tests to see if a character is a lowercase alphabetic character (a - z). |
| isprint | Tests to see if a character is among printable characters, including whitespace. |
| ispunct | Tests to see if a character is a punctuation character, which is any printable character that is neither whitespace nor alphanumeric. |
| isspace | Tests to see if a character is one of the standard whitespace characters. |
| isupper | Tests to see if a character is an uppercase alphabetic character (A - Z). |
| isxdigit | Tests to see if a character is a hexadecimal digit (0-9, A - F, a - f). |
| labs | Computes the absolute value of the specified long integer input value. |
| ldexp | Multiplies a floating-point number by an integral power of two. |
| ldiv | Computes the integral quotient and remainder of the division of numerator by denominator. |
| llabs | Computes the absolute value of the specified long long integer input value. |
| lldiv | Computes the integral quotient and remainder of the division of numerator by denominator. |
| localeconv | Queries the current locale for format parameters for numeric quantities. |
| localtime | Takes a calendar time, breaks it into its component parts, adjusts it to the local time zone, and stores the result in a struct tm. |
| log | Computes the natural logarithm of the specified argument. |
| log10 | Computes the base-ten logarithm of the specified argument. |
| longjmp | Restores the environment saved by the most recent calling of setjmp. |
| lseek | Sets the file position indicator for the specified file handle. |
| malloc | Allocates space for an object of specified size. |
| mblen | Determines the number of bytes contained in the specified multibyte character. |
| mbstowcs | Converts a sequence of multibyte characters into their corresponding wide character codes, storing only a specified number of codes. |
| mbtowc | Determines the number of bytes that are contained in the specified multibyte character and the code that corresponds to that multibyte character. |
| memchr | Locates the first occurrence of the specified character in a given memory block. |
| memcmp | Compares two blocks of memory. |
| memcpy | Copies a specified number of bytes from a source buffer to a target buffer. |
| memmove | Copies a specified number of bytes from a source buffer to a target buffer. |
| memset | Copies a specified value into a memory block. |
| mktime | Converts a local date and time represented in a struct tm into a calendar time value. |
| modf | Breaks a double value into its integral and fractional parts, each of which will have the same sign as the argument. |
| open | Opens a file with the specified name according to the operation flags and returns a handle to the opened file. |
| pow | Raises the input value to the designated power and returns the result. |
| putc | Writes the specified character to an output stream at the position of the associated file position indicator. |
| qsort | Sorts an array of elements into ascending order according to a comparison function written by the user. |
| raise | Sends the specified signal to the executing program. |
| rand | Computes a pseudorandom integer in the range 0 to RAND_MAX. |
| read | Reads a block of data from the specified file handle and stores this data in the specified buffer. |
| realloc | Changes the size of a memory block that has been previously allocated while preserving the contents. |
| remove | Causes the specified file or empty directory to be made inaccessible by that name. |
| rename | Causes the file or directory specified by oldFileName to be known by the name given in newFileName. |
| rewind | Sets the file position indicator for the specified stream to the beginning of the file. |
| setbuf | Specifies how to buffer the I/O stream. |
| setjmp | Stores the current calling environment for later use by longjmp. |
| setlocale | Modifies the specified category of the program's locale. |
| setvbuf | Specifies how to buffer the I/O stream. |
| sin | Computes the sine of the specified argument. |
| sinh | Computes the hyperbolic sine of the specified argument. |
| snprintf | Writes output to the specified string according to format specifiers in formatString; a null character is written at the end of the characters written. |
| sopen | Opens a file with the specified name according to the operation and share flags. |
| sprintf | Writes output to the specified string according to format specifiers in formatString; a null character is written at the end of the characters written. |
| sqrt | Computes the nonnegative square root of the specified argument. |
| srand | Uses the argument as a seed for a new sequence of pseudorandom numbers to be returned by subsequent calls to rand. |
| sscanf | Converts input from the specified source string into a series of values according to the specifiers in formatString. |
| strcat | Appends a copy of a source string to the end of a target string, including the terminating ASCII NUL byte. |
| strchr | Locates the first occurrence of the specified character in a string. |
| strcmp | Compares two NUL-terminated strings. |
| strcoll | Compares two NUL-terminated strings, both interpreted as appropriate to the LC_COLLATE category of the current locale. |
| strcpy | Copies a source string including the terminating ASCII NUL byte into a target string. |
| strcspn | Locates the position of the first character in a string that is in a specified set of characters. |
| strerror | Maps the specified error ID number from the errno global variable to an error message string. |
| strftime | Takes a date and time stored in a time struct and generates a NUL-terminated ASCII string that contains the time and date information in a format specified by a format string. |
| stricmp | Compares two NUL-terminated strings, based on the value of the characters interpreted as an unsigned char. |
| strlen | Computes the length of the specified string, up to but not including the terminating null character. |
| strncat | Appends a specified number of characters from a source string to the end of a target string. |
| strncmp | Compares a specified number of characters of two NUL-terminated strings. |
| strncpy | Copies characters from a source string to a target string until it reaches the specified number of characters or an ASCII NUL byte. |
| strnicmp | Compares a specified number of characters of two NUL-terminated strings based upon the value of the characters in the strings interpreted as unsigned chars. |
| strpbrk | Locates the first occurrence in a string of any character in the specified character set. |
| strrchr | Locates the last occurrence of the specified character in a string. |
| strspn | Locates the position of the first character in a string that is not in a specified set of characters. |
| strstr | Locates the first occurrence of a sequence of characters excluding the terminating ASCII NUL byte in a string. |
| strtod | Converts the initial portion of a string to double representation. |
| strtok | Breaks a string into tokens, which are sequences of contiguous characters separated by one or more characters from the specified set of delimiters. |
| strtol | Converts the initial portion of a string to a long int representation with a specified base. |
| strtoll | Converts the initial portion of a string to a long long integer representation with a specified base. |
| strtoul | Converts the initial portion of a string to an unsigned long int representation with a specified base. |
| strtoull | Converts the initial portion of a string to an unsigned long long integer representation with a specified base. |
| strxfrm | Transforms the specified number of characters, including the terminating ASCII NUL byte, from a source string to a target string. |
| system | Starts running a program and waits for it to exit. |
| tan | Computes the tangent of the specified argument. |
| tanh | Computes the hyperbolic tangent of the specified argument. |
| time | Determines the current calendar time (the number of seconds since January 1, 1900 Coordinated Universal Time (UTC)). |
| tmpfile | Creates a temporary binary file that will be automatically deleted when the user closes the file or terminates the program. |
| tmpnam | Generates a string that is a valid filename and that is not the same as the name of an existing file. This function will generate a different string each time it is called, up to TMP_MAX times. |
| tolower | Converts an uppercase letter to a lowercase letter and returns the converted character. |
| toupper | Converts a lowercase letter to an uppercase letter and returns the converted character. |
| ungetc | Will push a single character back into the specified input stream; subsequent reads on that stream will return pushed-back characters in the reverse order of their pushing. |
| vfprintf | Writes output to the specified stream according to format specifiers in formatString. |
| vfscanf | Reads input from the specified stream and converts it into a series of values according to the specifications of the formatting string. |
| vsnprintf | Writes output to the specified string according to format specifiers in formatString. |
| vsprintf | Writes output to the specified string according to format specifiers in formatString. |
| vsscanf | Converts input from the specified source string into a series of values according to the specifiers in formatString. |
| wcslen | Returns the length of the specified string up to, but not including, the terminating ASCII NUL byte. |
| wcstombs | Converts a sequence of wide character codes into a sequence of the corresponding multibyte characters. |
| wctomb | Determines the number of bytes needed to represent the multibyte character corresponding to the specified wide character code. |
| write | A data block stored in the specified buffer is written to the specified file handle. |

<!--NI_TOPIC bundle=labview-nxg-ansi-c-api-ref path=c-node-lib.html language=enus -->
## TOPIC 00003: C Node Function Reference

- bundle_id: `labview-nxg-ansi-c-api-ref`
- source_path: `c-node-lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ansi-c-api-ref/raw/resource/enus/c-node-lib.html
- document_id: `labview-nxg-ansi-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists functions, macros, and variables specific to the C Node. Function Description cnode_error_check Macro that checks the input expression for error. If the result is negative, then this macro sets it to the C node error and jumps to the Error label. You must define an Error la

C Node Function Reference

The following table lists functions, macros, and variables specific to the C Node.

| Function | Description |
| --- | --- |
| cnode_error_check | Macro that checks the input expression for error. If the result is negative, then this macro sets it to the C node error and jumps to the Error label. You must define an Error label to use this macro. |
| cnode_error_code | An integer variable representing the error code in the error in and error out cluster terminals. This variable is automatically set by cnode_error_check and cnode_null_check. |
| cnode_error_set | Macro that sets the C node error code and status. Pass the integer error code in the first parameter and the Boolean error status (1 or 0) in the second parameter. A non-zero status indicates that an error has occurred, and zero indicates otherwise. |
| cnode_error_source | A string variable representing the source of error in the error in and error out cluster terminals. This variable is automatically set by cnode_error_check and cnode_null_check. |
| cnode_error_status | A Boolean variable representing the status of error in the error in and error out cluster terminals. An error is set if this variable is TRUE and not set if this variable is FALSE. This variable is automatically set by cnode_error_check and cnode_null_check. |
| cnode_get_array_length | Returns the number of elements in the array C node array terminal. |
| cnode_null_check | Macro that checks the if the input expression is NULL (zero). If the expression is NULL, then this macro sets the C node error to indicate that memory allocation failed and jumps to the Error label. You must define an Error label to use this macro. |
| cnode_printf | Prints to the Output window. |
| cnode_size_array | Resizes the array C node array terminal to hold length number of elements. Returns non-zero on success and zero on failure. |
| cnode_size_string | Resizes the string C node string terminal to hold size bytes including the terminating NUL byte. Returns non-zero on success and zero on failure. |
