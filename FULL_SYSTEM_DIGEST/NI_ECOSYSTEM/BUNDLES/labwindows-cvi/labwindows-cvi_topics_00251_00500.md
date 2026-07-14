# NI DOCUMENT BUNDLE: labwindows-cvi

<!--NI_BUNDLE_CHUNK bundle=labwindows-cvi start=251 end=500 -->
<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxch_bpf.htm language=enus -->
## TOPIC 00251: CxCh_BPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxch_bpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxch_bpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCh_BPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxCh_BPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, double rippledb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Chebyshev bandpass digital filter. CxCh_BPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order bandpass Chebyshev filter. The pass band is from 200.0 to 300.0. */ 

 NIComplexNumber x[256], y[256]; 

 double input[256]; 

 double ripple, fs, fl, fh; 

 ssize_t n; 

 int status, order; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 ripple = 0.5; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){epar

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxCh_BPF (x, n, fs, fl, fh, ripple, order, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxch_bsf.htm language=enus -->
## TOPIC 00252: CxCh_BSF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxch_bsf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxch_bsf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCh_BSF

*Advanced Analysis Library Only*

AnalysisLibErrType CxCh_BSF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, double rippledb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Chebyshev bandstop digital filter. CxCh_BSF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order bandstop Chebyshev filter. The stop band is from 200.0 to 300.0. */ 

 NIComplexNumber x[256], y[256]; 

 double input[256]; 

 double ripple, fs, fl, fh; 

 ssize n; 

 int status, order; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 ripple = 0.5; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxCh_BSF (x, n, fs, fl, fh, ripple, order, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxch_hpf.htm language=enus -->
## TOPIC 00253: CxCh_HPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxch_hpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxch_hpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCh_HPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxCh_HPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, double rippledb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Chebyshev highpass digital filter. CxCh_HPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order highpass Chebyshev filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double ripple, fs, fc; 

 ssize_t n; 

 int status, order; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 ripple = 0.5; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxCh_HPF (x, n, fs, fc, ripple, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxch_lpf.htm language=enus -->
## TOPIC 00254: CxCh_LPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxch_lpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxch_lpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCh_LPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxCh_LPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, double rippledb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using a Chebyshev lowpass digital filter. CxCh_LPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order lowpass Chebyshev filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double ripple, fs, fc; 

 ssize_t n; 

 int status, order; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 ripple = 0.5; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxCh_LPF (x, n, fs, fc, ripple, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxchebwin.htm language=enus -->
## TOPIC 00255: CxChebWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxchebwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxchebwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxChebWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxChebWin (NIComplexNumber arrayX[], ssize_t numberOfElements, double ratio);

#### Purpose

Applies an unsymmetrical Dolph-Chebyshev window to a complex signal. If y represents the output sequence **arrayX**, CxChebWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='cxchebwinform_4.png']

where n is the number of elements in **arrayX**, s is the height ratio of the mainlobe to the sidelobe in dB, and the m-th order Chebyshev polynomial is

[IMAGE alt='image' src='cxchebwinform_5.png']

[IMAGE alt='image' src='cxchebwinform_6.png']

If you want to apply a symmetrical Dolph-Chebyshev window, call [SymWin](../../cvi/libref/cvisymwin.htm) instead. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in arrayX. |
| ratio | double | The height ratio of the mainlobe to the sidelobe in dB. If ratio < 0, the function uses 0 for ratio instead. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a Dolph-Chebyshev window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxcheckposdef.htm language=enus -->
## TOPIC 00256: CxCheckPosDef

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxcheckposdef.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxcheckposdef.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCheckPosDef

*Advanced Analysis Library Only*

AnalysisLibErrType CxCheckPosDef (void *inputMatrix, ssize_t matrixSize, int *positiveDefinite);

#### Purpose

Checks if the complex, square input matrix is positive definite. A complex, square matrix is positive definite if and only if it is symmetric and the quadratic form

x<sup>H</sup>Ax > 0

is true for all nonzero vectors x. For more information about positive definite matrices, refer to *Matrix Computations* by G.H. Golub and C.F. VanLoan, cited in the [Bibliography](../../cvi/libref/cvibibliography_for_advanced_analys.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Contains the input matrix that is to be tested for positive definiteness. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| matrixSize | ssize_t | Number of elements in one dimension of the matrix. |
| Output |  |  |
| Name | Type | Description |
| positiveDefinite | int | indicates if inputMatrix is symmetric and positive definite. 1 if the input matrix is positive definite; 0 otherwise. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxchirpzt.htm language=enus -->
## TOPIC 00257: CxChirpZT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxchirpzt.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxchirpzt.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxChirpZT

*Advanced Analysis Library Only*

AnalysisLibErrType CxChirpZT (NIComplexNumber inputSequence[], ssize_t numberOfElements, NIComplexNumber startingPoint, NIComplexNumber increment, int algorithm, ssize_t numberOfBins, NIComplexNumber transform[]);

#### Purpose

The Chirp-Z Transform calculates the z transform along a spiral in the z-plane at the following points:

[IMAGE alt='image' src='cxchirpztform_0.png']

for k = 0, 1, ..., M - 1, where M is **numberOfBins**, A is **startingPoint**, and W is **increment**. 

 

 The DIRECT method computes the Chirp-Z Transform as follows:

[IMAGE alt='image' src='cxchirpztform_1.png']

for k = 0, 1, ..., M - 1. 

 

 The DIRECT form can be reformulated with the convolution, as follows:

[IMAGE alt='image' src='cxchirpztform_2.png']

where [IMAGE alt='image' src='cxchirpztform_3.png'] . The convolution operation can be performed in the FREQ_DOMAIN method, which uses an FFT-based technique.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputSequence | NIComplexNumber [] | The input sequence. |
| numberOfElements | ssize_t | The length of inputSequence. |
| startingPoint | NIComplexNumber | The point at which to begin evaluating the Chirp-Z Transform. |
| increment | NIComplexNumber | The increment between each point to evaluate for the Chirp-Z Transform. |
| algorithm | int | The method to use to compute the Chirp-Z Transform. algorithm must be one of the following values: DIRECT (0): Computes the Chirp-Z transform using the direct form method. If the size of inputSequence or the numberOfBins is small, the direct method is typically faster.FREQ_DOMAIN (1): Computes the Chirp-Z transform using an FFT-based technique. If the size of inputSequence or the numberOfBins is large, the frequency domain method is typically faster. |
| numberOfBins | ssize_t | The length of transform. If numberOfBins is less than 1, this function uses numberOfElements for this parameter. |
| Output |  |  |
| Name | Type | Description |
| transform | NIComplexNumber [] | The Chirp-Z Transform of sequence inputSequence. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxcholesky.htm language=enus -->
## TOPIC 00258: CxCholesky

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxcholesky.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxcholesky.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCholesky

*Advanced Analysis Library Only*

AnalysisLibErrType CxCholesky (void *inputMatrix, ssize_t matrixSize, void *matrixR);

#### Purpose

Calculates the Cholesky factorization of a complex, symmetric positive definite input matrix. If the input matrix is not positive definite, CxCholesky returns an error.

The following formula defines the Cholesky factorization of a **matrixSize**-by-**matrixSize** symmetric positive definite matrix A:

A = R<sup>H</sup>R

| where | matrixR is an upper triangular matrix of dimensions matrixSize-by-matrixSize |
| --- | --- |
|  | RH is the complex conjugate transpose of matrixR |

Cholesky factorization is similar to LU factorization for symmetric positive definite matrices. If the matrix in your application is positive definite, use Cholesky factorization rather than LU factorization for the following reasons:

- The algorithm is well defined.
- Numerical stability does not require pivoting.
- Cholesky factorization requires about half the programming time and less memory than LU factorization.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex, square matrix. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| matrixSize | ssize_t | Number of elements in one dimension of the matrix. |
| Output |  |  |
| Name | Type | Description |
| matrixR | void * | Result matrix of the Cholesky decomposition, as an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxconditionnumber.htm language=enus -->
## TOPIC 00259: CxConditionNumber

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxconditionnumber.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxconditionnumber.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxConditionNumber

*Advanced Analysis Library Only*

AnalysisLibErrType CxConditionNumber (void *inputMatrix, ssize_t numberOfRows, ssize_t numberOfColumns, int normType, double *conditionNumber);

#### Purpose

Calculates the condition number of a complex input matrix. The **normType** parameter indicates what type of norm to use to calculate the condition number. The input matrix can be either square or rectangular when **normType** is 2-norm.

The following formula defines the condition number c of a matrix A:

[IMAGE alt='image' src='condnbr.gif'] is the p-norm of the matrix A

The **normType** value defines the p-norm behavior. For a 2-norm **normType**, c is the ratio of the largest singular value of A to the smallest singular value of A.

The condition number of a matrix indicates how near to singular the matrix is. A matrix with a large condition number is nearly singular, and a matrix with a condition number close to one is far from singular. The condition number of a matrix is always greater than or equal to one, and it can help assess the accuracy of a solution to a linear system of equations and matrix inversion.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex, square matrix. If normType is 2-norm, the matrix can be square or rectangular; otherwise, it must be square. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| numberOfRows | ssize_t | Number of rows in inputMatrix. |
| numberOfColumns | ssize_t | The number of columns in inputMatrix. |
| normType | int | Type of p-norm function to use to calculate the condition number. The following table shows valid norm type values. Norm Type Value Meaning 2-norm 0 Largest singular value of inputMatrix. 1-norm 1 Largest column sum of inputMatrix. Frobenius-norm 2 Square root of the sum of the diagonal elements of ATA, where AT is the complex conjugate transpose of A. Infinite-norm 3 Largest row sum of inputMatrix. |
| Norm Type | Value | Meaning |
| 2-norm | 0 | Largest singular value of inputMatrix. |
| 1-norm | 1 | Largest column sum of inputMatrix. |
| Frobenius-norm | 2 | Square root of the sum of the diagonal elements of ATA, where AT is the complex conjugate transpose of A. |
| Infinite-norm | 3 | Largest row sum of inputMatrix. |
| Output |  |  |
| Name | Type | Description |
| conditionNumber | double | Complex condition number of the matrix. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxconvolve.htm language=enus -->
## TOPIC 00260: CxConvolve

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxconvolve.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxconvolve.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxConvolve

*Advanced Analysis Library Only*

AnalysisLibErrType CxConvolve (NIComplexNumber arrayX[], ssize_t sizeOfX, NIComplexNumber arrayY[], ssize_t sizeOfY, int algorithm, NIComplexNumber outputArray[]);

#### Purpose

arrayX

arrayY

x

t

y

t

[IMAGE alt='image' src='cxconvolveform_9.png']

where the symbol * denotes linear convolution. 

 

 When **algorithm** is ALGORITHM_CONCOR_DIRECT, this function uses the following equation to perform the discrete implementation of the linear convolution and obtain the elements of **arrayX** * **arrayY**.

[IMAGE alt='image' src='cxconvolveform_10.png']

for i = 0, 1, 2, ..., M+N–2 

 

 where h is **arrayX** * **arrayY** 

 

 N is the number of elements in **arrayX** 

 

 M is the number of elements in **arrayY** 

 

 the indexed elements outside the ranges of **arrayX** and **arrayY** are equal to zero, as shown in the following relationships:

x<sub>j</sub> = 0, j < 0, or j ≥ N

and

y<sub>j</sub> = 0, j < 0, or j ≥ M

|  | Note This formula description assumes that M ≤ N. For M > N, exchange (x, y) and (M, N) in the previous equations. |
| --- | --- |

algorithm

ALGORITHM_CONCOR_FREQ_DOMAIN

1. First, this function pads the end of arrayX and arrayY with zeros to make their lengths M + N – 1, as shown in the following equations. 
 [IMAGE alt='image' src='cxconvolveform_11.png'] [IMAGE alt='image' src='cxconvolveform_12.png']
2. Second, this function calculates the Fourier transform of arrayX ' and arrayY ' according to the following equations. 
 
 arrayX '(f) = FFT(x') 
 
 arrayY '(f) = FFT(y')
3. Third, this function multiplies arrayX '( f ) by arrayY '( f ) and calculates the inverse Fourier transform of the product. The result is the linear convolution of arrayX and arrayY , as shown in the following equation. 
 
 arrayX * arrayY = IFFT( arrayX '(f) ⋅ arrayY '(f)) 
 
 Thus, this function computes the linear convolution, not the circular convolution. However, because x(t) * y(t) n ↔ X(f)Y(f) is a Fourier transform pair, where x(t) * y(t) n is the circular convolution of x(t) and y(t) , you can create a circular version of the convolution.

|  | Note This function temporarily allocates memory for use as a work area. If CxConvolve cannot allocate memory, the function returns an error code. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | First input array. |
| sizeOfX | ssize_t | Number of elements in arrayX. |
| arrayY | NIComplexNumber [] | Second input array. |
| sizeOfY | ssize_t | Number of elements in arrayY. |
| algorithm | int | Specifies the convolution method to use. algorithm must be one of the following values. Note that slight numerical differences can exist between the two methods. Constant Value Description ALGORITHM_CONCOR_DIRECT 0 Computes the convolution using the direct method of linear convolution. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT convolution method is typically faster. ALGORITHM_CONCOR_FREQ_DOMAIN 1 Computes the convolution using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN convolution method is typically faster. |
| Constant | Value | Description |
| ALGORITHM_CONCOR_DIRECT | 0 | Computes the convolution using the direct method of linear convolution. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT convolution method is typically faster. |
| ALGORITHM_CONCOR_FREQ_DOMAIN | 1 | Computes the convolution using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN convolution method is typically faster. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Convolution array. This array must be at least (N + M – 1) elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxconvolve2d.htm language=enus -->
## TOPIC 00261: CxConvolve2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxconvolve2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxconvolve2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxConvolve2D

*Advanced Analysis Library Only*

AnalysisLibErrType CxConvolve2D (void *arrayX, ssize_t m1, ssize_t n1, void *arrayY, ssize_t m2, ssize_t n2, int outputSize, int algorithm, void *outputArray);

#### Purpose

algorithm

ALGORITHM_CONCOR_DIRECT

arrayX

arrayY

[IMAGE alt='image' src='cxconvolve2dform_6.png']

for i = 0, 1, 2, ..., M<sub>1</sub> + M<sub>2</sub> – 2 and j = 0, 1, 2, ..., N<sub>1</sub> + N<sub>2</sub> – 2 

 

 where h is **arrayX** * **arrayY** 

 

 M<sub>1</sub> is the number of rows of matrix **arrayX** 

 N<sub>1</sub> is the number of columns of matrix **arrayX** 

 M<sub>2</sub> is the number of rows of matrix **arrayY** 

 N<sub>2</sub> is the number of columns of matrix **arrayY** 

 

 The indexed elements outside the ranges of **arrayX** and **arrayY** are equal to zero, as shown in the following relationships:

x(m,n), m < 0 or m ≥ M<sub>1</sub> or n < 0 or n ≥ N<sub>1</sub>

and

y(m,n), m < 0 or m ≥ M<sub>2</sub> or n < 0 or n ≥ N2.

algorithm

ALGORITHM_CONCOR_FREQ_DOMAIN

1. First, this function pads the end of arrayX and arrayY with zeros to make their sizes ( M 1 + M 2 – 1)-by-( N 1 + N 2 – 2), as shown in the following equations. 
 
 [IMAGE alt='image' src='cxconvolve2dform_7.png'] [IMAGE alt='image' src='cxconvolve2dform_8.png']
2. Second, this function calculates the Fourier transform of arrayX ' and arrayY ' according to the following equations. 
 
 arrayX '(f) = FFT(x') 
 arrayY '(f) = FFT(y')
3. Third, this function multiplies arrayX '(f) by arrayY '(f) and calculates the inverse Fourier transform of the product. The result is the two-dimensional convolution of arrayX and arrayY , as shown in the following equation. 
 
 arrayX * arrayY = IFFT( arrayX '(f) ⋅ arrayY '(f))

outputSize

arrayX

arrayY

[IMAGE alt='loc_eps_convol1b.gif' src='loc_eps_convol1b.gif']

1. OUTPUT_SIZE_FULL 
 
 The output matrix arrayX * arrayY is ( M 1 + M 2 – 1)-by-( N 1 + N 2 – 1).
2. OUTPUT_SIZE_SIZE_X 
 
 This is useful in image processing. If arrayX is the image you want to filter, arrayY is a small matrix called the convolution kernel. arrayX * arrayY is the filtered image whose size is the same as that of image arrayX . The output M 1 -by- N 1 matrix is the central part of the output matrix when outputSize is OUTPUT_SIZE_FULL .
3. OUTPUT_SIZE_COMPACT 
 
 Computing the edge elements of arrayX * arrayY requires zero-padding if outputSize is OUTPUT_SIZE_FULL or OUTPUT_SIZE_SIZE_X . LabWindows/CVI removes these edge elements if outputSize is OUTPUT_SIZE_COMPACT . The output ( M 1 – M 2 + 1)-by-( N 1 – N 2 + 1) matrix is the central part of the output matrix when outputSize is OUTPUT_SIZE_SIZE_X .

|  | Note This function temporarily allocates memory for use as a work area. If CxConvolve2D cannot allocate memory, the function returns an error code. |
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
| outputSize | int | The size of the output. outputSize must be one of the following values. Constant Value Description OUTPUT_SIZE_FULL 0 The size of outputArray is (M1 + M2 – 1)-by-(N1 + N2 – 1) OUTPUT_SIZE_SIZE_X 1 The size of outputArray is the same as arrayX; that is M1-by-N1. OUTPUT_SIZE_COMPACT 2 The size of outputArray (M1 – M2 + 1)-by-(N1 – N2 + 1). Note that in this mode m1 must be greater than or equal to m2 and n1 must be greater than or equal to n2. |
| Constant | Value | Description |
| OUTPUT_SIZE_FULL | 0 | The size of outputArray is (M1 + M2 – 1)-by-(N1 + N2 – 1) |
| OUTPUT_SIZE_SIZE_X | 1 | The size of outputArray is the same as arrayX; that is M1-by-N1. |
| OUTPUT_SIZE_COMPACT | 2 | The size of outputArray (M1 – M2 + 1)-by-(N1 – N2 + 1). Note that in this mode m1 must be greater than or equal to m2 and n1 must be greater than or equal to n2. |
| algorithm | int | Specifies the convolution method to use. algorithm must be one of the following values. Note that slight numerical can exist between the two methods. Constant Value Description ALGORITHM_CONCOR_DIRECT 0 Computes the convolution using the direct method of linear convolution. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT convolution method is typically faster. ALGORITHM_CONCOR_FREQ_DOMAIN 1 Computes the convolution using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN convolution method is typically faster. |
| Constant | Value | Description |
| ALGORITHM_CONCOR_DIRECT | 0 | Computes the convolution using the direct method of linear convolution. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT convolution method is typically faster. |
| ALGORITHM_CONCOR_FREQ_DOMAIN | 1 | Computes the convolution using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN convolution method is typically faster. |
| Output |  |  |
| Name | Type | Description |
| outputArray | void | Convolution array. The size of outputArray relates to outputSize. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxcorrelate.htm language=enus -->
## TOPIC 00262: CxCorrelate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxcorrelate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxcorrelate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCorrelate

*Advanced Analysis Library Only*

AnalysisLibErrType CxCorrelate (NIComplexNumber arrayX[], ssize_t sizeOfX, NIComplexNumber arrayY[], ssize_t sizeOfY, int algorithm, NIComplexNumber outputArray[]);

#### Purpose

Finds the correlation of the complex input arrays. The cross correlation Rxy(t) of the sequences x(t) and y(t) is defined by the following equation:

[IMAGE alt='image' src='cxcorrelateform_14.png']

where the symbol [IMAGE alt='image' src='cxcorrelateform_1.png'] denotes correlation. 

 

 The discrete implementation of this function is as follows. Let h represent a sequence whose indexing can be negative, let N be the number of elements in the input sequence **arrayX**, let M be the number of elements in the sequence **arrayY**, and assume that the indexed elements of **arrayX** and **arrayY** that lie outside their range are equal to zero, as shown by the following equations:

x<sub>j</sub> = 0, j < 0 or j ≥ N

and

y<sub>j</sub> = 0, j < 0 or j ≥ M.

CxCorrelate

h

[IMAGE alt='image' src='cxcorrelateform_15.png']

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

CxCorrelate

N

|  | Note This function temporarily allocates memory for use as a work area. If CxCorrelate cannot allocate memory, the function returns an error code. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | First input array. |
| sizeOfX | ssize_t | Number of elements in arrayX. |
| arrayY | NIComplexNumber [] | Second input array. |
| sizeOfY | ssize_t | Number of elements in arrayY. |
| algorithm | int | Specifies the correlation method to use. algorithm must be one of the following values. Note that slight numerical differences can exist between the two methods. Constant Value Description ALGORITHM_CONCOR_DIRECT 0 Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. ALGORITHM_CONCOR_FREQ_DOMAIN 1 Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| Constant | Value | Description |
| ALGORITHM_CONCOR_DIRECT | 0 | Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. |
| ALGORITHM_CONCOR_FREQ_DOMAIN | 1 | Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | The correlation of arrayX and arrayY. This array must be at least (n + m – 1) elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxcorrelate2d.htm language=enus -->
## TOPIC 00263: CxCorrelate2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxcorrelate2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxcorrelate2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCorrelate2D

*Advanced Analysis Library Only*

AnalysisLibErrType CxCorrelate2D (void *arrayX, ssize_t m1, ssize_t n1, void *arrayY, ssize_t m2, ssize_t n2, int algorithm, void *outputArray);

#### Purpose

CxCorrelate2D

[IMAGE alt='image' src='cxcorrelate2dform_13.png']

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

|  | Note This function temporarily allocates memory for use as a work area. If CxCorrelate2D cannot allocate memory, the function returns an error code. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxcostaperedwin.htm language=enus -->
## TOPIC 00264: CxCosTaperedWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxcostaperedwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxcostaperedwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCosTaperedWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxCosTaperedWin (NIComplexNumber arrayX[], ssize_t numberOfElements, double ratio);

#### Purpose

y

arrayX

CxCosTaperedWin

y

[IMAGE alt='image' src='cxcostaperedwinform_7.png']

where n is the number of elements in **arrayX**, [IMAGE alt='image' src='cxcostaperedwinform_8.png'], and r is the ratio of the total length of the tapered section to the whole signal length as shown in the following figure: 

 

 
[IMAGE alt='image' src='loc_fp_costapdia.gif']\n\n

If r ≤ 0, the window is equivalent to a rectangular window. If r ≥ 1, the window is equivalent to a Hanning window.

This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in arrayX. |
| ratio | double | The ratio of the total length of the tapered section to the whole signal length. The window is a cosine tapered window only if 0 < ratio < 1. If ratio <=0, the window is equivalent to a rectangular window. If ratio >=1, the window is equivalent to a Hanning window. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter turns the input signal with a cosine tapered window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxcrossspectrum.htm language=enus -->
## TOPIC 00265: CxCrossSpectrum

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxcrossspectrum.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxcrossspectrum.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxCrossSpectrum

*Advanced Analysis Library Only*

AnalysisLibErrType CxCrossSpectrum (NIComplexNumber xArray[], NIComplexNumber yArray[], ssize_t numberOfElements, NIComplexNumber crossSpectrum[]);

#### Purpose

Calculates the double-sided cross power spectrum, Sxy, of the complex input sequences X and Y according to the following formula:

[IMAGE alt='image' src='crossspec.gif']

where FFT*[X] is the complex conjugate of FFT[X].

The input sequences are copied to internal buffers and zero-padded to **n** samples before the FFTs are computed. The output arrays are the real and imaginary parts of the cross spectrum CxCrossSpectrum.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xArray | NIComplexNumber [] | Time-domain signal X. |
| yArray | NIComplexNumber [] | Time-domain signal Y. |
| numberOfElements | ssize_t | Number of elements in the input arrays. xArray and yArray must have the same length. |
| Output |  |  |
| Name | Type | Description |
| crossSpectrum | NIComplexNumber [] | Double-sided cross power spectrum between signals xArray and yArray. The size of this array must be at least numberOfElements. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxdecimate.htm language=enus -->
## TOPIC 00266: CxDecimate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxdecimate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxdecimate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxDecimate

*Advanced Analysis Library Only*

AnalysisLibErrType CxDecimate (NIComplexNumber inputArray[], ssize_t numberOfElements, ssize_t decimatingFactor, int averaging, NIComplexNumber decimatedArray[]);

#### Purpose

Decimates the input sequence **inputArray**. 

 

 This function decimates the input sequence **inputArray** as follows:

[IMAGE alt='image' src='cxdecimateform_17.png']

where k=0,1,2...D-1,i = 0, 1, 2 ... size-1, 

 

 size = truncation(n/D) is the size of the output sequence.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | The input sequence. If decimatedArray is NULL, inputArray is overwritten by the output sequence. |
| numberOfElements | ssize_t | The length of inputArray. |
| decimatingFactor | ssize_t | The decimating factor. decimatingFactor must be greater than 0 and less than numberOfElements. |
| averaging | int | Specify a nonzero value or ENABLE_OPTION or select On in the function panel to use averaging in decimating the inputArray. Specify 0 or DISABLE_OPTION or select Off in the function panel to disable averaging. This is the default value. |
| Output |  |  |
| Name | Type | Description |
| decimatedArray | NIComplexNumber [] | The decimated sequence. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxdecimatecontinuous.htm language=enus -->
## TOPIC 00267: CxDecimateContinuous

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxdecimatecontinuous.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxdecimatecontinuous.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxDecimateContinuous

*Advanced Analysis Library Only*

AnalysisLibErrType CxDecimateContinuous (NIComplexNumber inputArray[], ssize_t numberOfElements, ssize_t decimatingFactor, int averaging, ssize_t startIndex, int initialize, ssize_t *decimatedLength);

#### Purpose

Continuously decimates the complex input sequence **inputArray** by the **decimatingFactor** and the **averaging** values that you specify. If Y represents the decimated output sequence, CxDecimateContinuous obtains the elements of the sequence Y using the following equation:

averaging

[IMAGE alt='image' src='cxdecimatecontinuousform_18.png']

| for | i = 0, 1, 2, ..., size – 1 |
| --- | --- |
|  | size = ⌈(n–s/m)⌉ |

averaging

[IMAGE alt='image' src='cxdecimatecontinuousform_19.png']

| for | i = 0, 1, 2, ..., size – 1 |
| --- | --- |
|  | size = ⌊(n–s/m)⌋ |

where n is the number of elements in **inputArray**, m is the **decimatingFactor**, s is the **startIndex**, size is the number of elements in the output sequence, ⌈⋅⌉ gives the smallest integer greater than or equal to the number, and ⌊⋅⌋ gives the largest integer less than or equal to the number.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in the input array. |
| decimatingFactor | ssize_t | Factor by which to decimate inputArray. decimatingFactor must be greater than 0 and less than numberOfElements. If decimatingFactor is greater than numberOfElements or less than or equal to zero, this function sets decimatingFactor to an empty array and returns an error. |
| averaging | int | Specifies whether to use averaging in decimating inputArray. Specify a nonzero value or select On in the function panel to specify that each output element is the mean of the decimatingFactor input points. Specify 0 or select in the function panel to specify not to average the output element. |
| startIndex | ssize_t | The index from which sample in inputArray the decimation starts if you call the function for the first time or initialize is a nonzero value. startIndex must be greater than or equal to zero. The default is 0. |
| initialize | int | Specifies whether to initialize the decimation. Specify a nonzero value or select Yes in the function panel to initialize the decimation from the startIndex of the input sequence. Specify 0 or select No in the function panel to resume the decimation from the previous sequence. To process a large data sequence that consists of smaller blocks, set initialize to a nonzero value for the first block and to 0 for all remaining blocks. You also can set initialize to a nonzero value at regular intervals of blocks to periodically reset the sample from which the decimation begins. |
| Output |  |  |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | On input, the input array to decimate. On output, this parameter returns the decimated sequence of inputArray. |
| decimatedLength | ssize_t | The length of the decimated sequence. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxdeterminant.htm language=enus -->
## TOPIC 00268: CxDeterminant

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxdeterminant.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxdeterminant.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxDeterminant

*Advanced Analysis Library Only*

AnalysisLibErrType CxDeterminant (void *inputMatrix, ssize_t matrixSize, int matrixType, NIComplexNumber *determinant);

#### Purpose

Calculates the complex determinant of a square, complex input matrix.

In this function you can specify the input matrix type using **matrixType**. The input matrix can be upper or lower triangular, general, or positive definite. For an upper or lower triangular matrix, the determinant equals the product of the diagonal elements of the matrix. For a positive definite matrix, CxDeterminant first calculates the Cholesky factorization of the input matrix and then calculates the determinant as the square of the determinant of R.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex, square matrix. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| matrixSize | ssize_t | Number of elements in one dimension of the input matrix. |
| matrixType | int | Type of the input matrix. Choose the matrix type correctly because it significantly affects the speed of computation. Matrix Type Value General matrix 0 Positive definite 1 Lower triangular 2 Upper triangular 3 |
| Matrix Type | Value |  |
| General matrix | 0 |  |
| Positive definite | 1 |  |
| Lower triangular | 2 |  |
| Upper triangular | 3 |  |
| Output |  |  |
| Name | Type | Description |
| determinant | NIComplexNumber | Complex determinant of the input matrix. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxdiv.htm language=enus -->
## TOPIC 00269: CxDiv

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxdiv.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxdiv.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxDiv

AnalysisLibErrType CxDiv (double xReal, double xImaginary, double yReal, double yImaginary, double *outputReal, double *outputImaginary);

#### Purpose

Divides two complex numbers, x and y. CxDiv obtains the resulting complex number, z, using the following formulas:

[IMAGE alt='image' src='cxdiv.gif']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x_Real | double | Real part of the dividend. Default Value: 1.0. |
| x_Imaginary | double | Imaginary part of the dividend. Default Value: 0.0. |
| y_Real | double | Real part of the divisor. Default Value: 1.0. |
| y_Imaginary | double | Imaginary part of the divisor. Default Value: 0.0. |
| Output |  |  |
| Name | Type | Description |
| output_Real | double | Real part of the result of the complex division. |
| output_Imaginary | double | Imaginary part of the result of the complex division. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxdiv1d.htm language=enus -->
## TOPIC 00270: CxDiv1D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxdiv1d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxdiv1d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxDiv1D

AnalysisLibErrType CxDiv1D (double arrayXReal[], double arrayXImaginary[], double arrayYReal[], double arrayYImaginary[], ssize_t numberOfElements, double outputArrayReal[], double outputArrayImag[]);

#### Purpose

Divides two complex 1D arrays. CxDiv1D obtains the i<sup>th</sup> element of the resulting complex array using the following formulas:

[IMAGE alt='image' src='cxdiv1d.gif']

CxDiv1D can perform this operation in place; that is, the input and output arrays can be the same.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX_Real | double [] | Real part of the dividend array. |
| arrayX_Imaginary | double [] | Imaginary part of the dividend array. |
| arrayY_Real | double [] | Real part of the divisor array. |
| arrayY_Imaginary | double [] | Imaginary part of the divisor array. |
| numberOfElements | ssize_t | Number of elements to divide. |
| Output |  |  |
| Name | Type | Description |
| outputArray_Real | double [] | Real part of the result of the complex array division. |
| outputArray_Imag | double [] | Imaginary part of the result of the complex array division. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxdotproduct.htm language=enus -->
## TOPIC 00271: CxDotProduct

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxdotproduct.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxdotproduct.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxDotProduct

*Advanced Analysis Library Only*

AnalysisLibErrType CxDotProduct (NIComplexNumber vectorX[], NIComplexNumber vectorY[], ssize_t numberOfElements, NIComplexNumber *dotProduct);

#### Purpose

Calculates the dot product of the complex input arrays. Use the following formula to obtain the dot product d:

[IMAGE alt='image' src='cxdotprod.gif']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vectorX | NIComplexNumber [] | First complex input vector. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| vectorY | NIComplexNumber [] | Second complex input vector. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| numberOfElements | ssize_t | Number of elements in each vector. |
| Output |  |  |
| Name | Type | Description |
| dotProduct | NIComplexNumber | Complex dot product of the input vectors. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxeigenvaluevector.htm language=enus -->
## TOPIC 00272: CxEigenValueVector

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxeigenvaluevector.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxeigenvaluevector.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxEigenValueVector

*Advanced Analysis Library Only*

AnalysisLibErrType CxEigenValueVector (void *inputMatrix, ssize_t matrixSize, int matrixType, int outputChoice, NIComplexNumber eigenvalues[], void *eigenvectors);

#### Purpose

Calculates the eigenvalues λ and the corresponding eigenvectors x of a complex, square input matrix A. The following formula defines the eigenvalues and the corresponding eigenvectors:

Ax = λx

The **matrixType** parameter indicates the type of the input matrix. The input matrix can be a general or a Hermitian matrix.

The **outputChoice** parameter determines what CxEigenValueVector calculates. Depending on your application, you can choose to calculate just the eigenvalues or to calculate both the eigenvalues and the eigenvectors.

The **eigenValues** output parameter is a 1D array of **matrixSize** complex numbers. The **eigenVectors** output parameter is a **matrixSize**-by-**matrixSize**, complex matrix (2D array) that contains the eigenvectors of the input matrix. Each i<sup>th</sup> column of this matrix is the eigenvector that corresponds to the i<sup>th</sup> component of the **eigenValues**. Each eigenvector is normalized so that its largest component equals one.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex, square matrix. This matrix will be overwritten; you must make a copy of the input matrix if you want to use it later. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| matrixSize | ssize_t | Number of elements in one dimension of the input matrix. |
| matrixType | int | The type of the input matrix. Pass 0 for a general matrix; 1 for a Hermitian matrix. Choose the matrix type correctly because it significantly affects the speed of computation. |
| outputChoice | int | Specifies whether the function computes eigenvectors. Pass 0 to compute only eigenvalues, and pass 1 to compute both eigenvalues and eigenvectors. |
| Output |  |  |
| Name | Type | Description |
| eigenvalues | NIComplexNumber [] | Result eigenvalues of the input matrix. This matrix is an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| eigenvectors | void * | Result eigenvectors of the input matrix. You can pass NULL if outputChoice is 0. This matrix is an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxeigenvback.htm language=enus -->
## TOPIC 00273: CxEigenVBack

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxeigenvback.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxeigenvback.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxEigenVBack

*Advanced Analysis Library Only*

AnalysisLibErrType CxEigenVBack (void *inputEigenvectors, ssize_t numberOfEigenvectors, int side, int method, ssize_t indexLow, ssize_t indexHigh, double scale[], void *outputEigenvectors);

#### Purpose

Transforms the complex eigenvectors of a balanced matrix to those of the original matrix. If you want more accurate eigenvectors for an unsymmetric matrix, complete the following steps:

1. Balance the original matrix using MatrixBalance or CxMatrixBalance .
2. Call GenEigenValueVector or CxEigenValueVector to get the eigenvectors of the balanced matrix.
3. Call CxEigenVBack to back-transform the eigenvectors of the balanced matrix to the eigenvectors of the original matrix.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEigenvectors | void * | The eigenvectors of the balanced matrix. |
| numberOfEigenvectors | ssize_t | The order of inputEigenvectors. |
| side | int | Specifies whether inputEigenvectors contains right side eigenvectors or left side eigenvectors. side must be one of the following values: RIGHT_EIGEN (0): right side eigenvectorsLEFT_EIGEN (1): left side eigenvectors |
| method | int | Specifies how the original matrix is balanced. method should be the same value as passed to CxMatrixBalance or MatrixBalance when the original matrix was balanced. |
| indexLow | ssize_t | The permutation information from CxMatrixBalance or MatrixBalance. |
| indexHigh | ssize_t | The permutation information from CxMatrixBalance or MatrixBalance. |
| scale | double [] | The scale information from CxMatrixBalance or MatrixBalance. |
| Output |  |  |
| Name | Type | Description |
| outputEigenvectors | void * | The eigenvectors of the original matrix. If outputEigenvectors = NULL or outputEigenvectors = inputEigenvectors, the back-transformed eigenvectors overwrite inputEigenvectors. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxelp_bpf.htm language=enus -->
## TOPIC 00274: CxElp_BPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxelp_bpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxelp_bpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxElp_BPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxElp_BPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, double rippledb, double stopBandAttendb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using an elliptic bandpass digital filter. CxElp_BPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order bandpass elliptic filter. The pass band is from 200.0 to 300.0. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double fs, fl, fh, ripple, atten; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 order = 5; 

 ripple = 0.2; 

 atten = 60.0; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxElp_BPF (x, n, fs, fl, fh, ripple, atten, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
| stopBandAtten_db | double | Stop band attenuation in decibels. This value must be greater than 0. Default Value: 40.0 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxelp_bsf.htm language=enus -->
## TOPIC 00275: CxElp_BSF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxelp_bsf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxelp_bsf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxElp_BSF

*Advanced Analysis Library Only*

AnalysisLibErrType CxElp_BSF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, double rippledb, double stopBandAttendb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using an elliptic bandstop digital filter. CxElp_BSF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order bandstop elliptic filter. The stop band is from 200.0 to 300.0. */ 

 complexnum x[256]; 

 double input[256]; 

 double fs, fl, fh, ripple, atten; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fl = 200.0; 

 fh = 300.0; 

 order = 5; 

 ripple = 0.2; 

 atten = 60.0; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxElp_BSF (x, n, fs, fl, fh, ripple, atten, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| lowerCutoffFreq | double | Lower cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| upperCutoffFreq | double | Upper cutoff frequency in Hertz. This value must be 0 < lowerCutoffFreq < upperCutoffFreq < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
| stopBandAtten_db | double | Stop band attenuation in decibels. This value must be greater than 0. Default Value: 40.0 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxelp_hpf.htm language=enus -->
## TOPIC 00276: CxElp_HPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxelp_hpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxelp_hpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxElp_HPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxElp_HPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, double rippledb, double stopBandAttendb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using an elliptic highpass digital filter. CxElp_HPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order highpass elliptic filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double fs, fc, ripple, atten; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 order = 5; 

 ripple = 0.2; 

 atten = 60.0; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxElp_HPF (x, n, fs, fc, ripple, atten, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
| stopBandAtten_db | double | Stop band attenuation in decibels. This value must be greater than 0. Default Value: 40.0 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxelp_lpf.htm language=enus -->
## TOPIC 00277: CxElp_LPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxelp_lpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxelp_lpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxElp_LPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxElp_LPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, double rippledb, double stopBandAttendb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using an elliptic lowpass digital filter. CxElp_LPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order lowpass elliptic filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double fs, fc, ripple, atten; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 order = 5; 

 ripple = 0.2; 

 atten = 60.0; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxElp_LPF (x, n, fs, fc, ripple, atten, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| ripple_db | double | The amplitude of the stop band ripple in decibels. This value must be greater than 0. Default Value: 0.1 db. |
| stopBandAtten_db | double | Stop band attenuation in decibels. This value must be greater than 0. Default Value: 40.0 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxequirpl_bpfiltering.htm language=enus -->
## TOPIC 00278: CxEquiRpl_BPFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxequirpl_bpfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxequirpl_bpfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxEquiRpl_BPFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType CxEquiRpl_BPFiltering (NIComplexNumber inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double f1, double f2, double f3, double f4, NIComplexNumber outputArray[]);

#### Purpose

Filter the complex array using a optimal bandpass FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 51-point bandpass FIR filter and filter the complex incoming signal. */ 

 complexnum x[256], y[306];
 double input[256];
 double fs, f1, f2, f3, f4;
 int n, ncoef, i;
 
 fs = 1000.0; // sampling frequency
 f1 = 200.0; // first stop band [0, 200]
 f2 = 250.0; // pass band [250, 350]
 f3 = 350.0; 
 f4 = 400.0; // second stop band [400, fs/2]
 n = 256; // input signal length
 ncoef = 51; //filter length
 WhiteNoise (n, 1, 17, input); 
 for(i = 0; i < n; i++){
 x[i].real = input[i];
 x[i].imaginary = input[i];
 }
 
 CxEquiRpl_BPFiltering(x, n, ncoef, fs, f1, f2, f3, f4, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| highestStopFreq | double | Highest frequency of the lower stop band. The lower stop band is [0, f1]. |
| f2 | double | Lowest frequency of the pass band. The pass band is [f2, f3]. |
| f3 | double | Highest frequency of the pass band. The pass band is [f2, f3]. |
| f4 | double | Lowest frequency of the upper stop band. The upper stop band is [f4, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. This array must be at least elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxequirpl_bsfiltering.htm language=enus -->
## TOPIC 00279: CxEquiRpl_BSFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxequirpl_bsfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxequirpl_bsfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxEquiRpl_BSFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType CxEquiRpl_BSFiltering (NIComplexNumber inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double f1, double f2, double f3, double f4, NIComplexNumber outputArray[]);

#### Purpose

Filter the complex array using a optimal bandstop FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 51-point bandstop FIR filter and filter the complex incoming signal. */ 

 complexnum x[256], y[306];
 double input[256];
 double fs, f1, f2, f3, f4;
 int n, ncoef, i;
 
 fs = 1000.0; // sampling frequency
 f1 = 200.0; // first pass band [0, 200]
 f2 = 250.0; // stop band [250, 350]
 f3 = 350.0; 
 f4 = 400.0; // second pass band [400, fs/2]
 n = 256; // input signal length
 ncoef = 51; //filter length
 WhiteNoise (n, 1, 17, input); 
 for(i = 0; i < n; i++){
 x[i].real = input[i];
 x[i].imaginary = input[i];
 }
 
 CxEquiRpl_BSFiltering(x, n, ncoef, fs, f1, f2, f3, f4, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. The algorithm introduces a large error when designing a bandstop filter for an even number of ncoef. To avoid this error, the CxEquiRpl_BSFiltering adjusts the ncoef to the next higher odd value if ncoef is even. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| highestPassFreq | double | Highest frequency of the lower pass band. The lower pass band is [0, f1]. |
| f2 | double | Lowest frequency of the stop band. The stop band is [f2, f3]. |
| highestStopFreq | double | Highest frequency of the stop band. The stop band is [f2, f3]. |
| lowestPassFreq | double | Lowest frequency of the upper pass band. The upper pass band is [f4, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. This array must be at least elements long when ncoef is odd. This array must be at least elements long when ncoef is even. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxequirpl_hpfiltering.htm language=enus -->
## TOPIC 00280: CxEquiRpl_HPFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxequirpl_hpfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxequirpl_hpfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxEquiRpl_HPFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType CxEquiRpl_HPFiltering (NIComplexNumber inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double passBand, double f2, NIComplexNumber outputArray[]);

#### Purpose

Filter the complex array using a optimal highpass FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 25-point highpass FIR filter and filter the complex incoming signal. */ 

 complexnum x[256], y[280];
 double input[256];
 double fs, f1, f2;
 int n, ncoef, i;
 
 fs = 1000.0; // sampling frequency
 f1 = 300.0; // pass band [0, 300]
 f2 = 400.0; // stop band [400, fs/2]
 n = 256; // input signal length
 ncoef = 25; //filter length
 WhiteNoise (n, 1, 17, input); 
 for(i = 0; i < n; i++){
 x[i].real = input[i];
 x[i].imaginary = input[i];
 }
 
 CxEquiRpl_HPFiltering(x, n, ncoef, fs, f1, f2, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. The algorithm introduces a large error when designing a highpass filter for an even number of ncoef. To avoid this error, the CxEquiRpl_HPFiltering adjusts the ncoef to the next higher odd value if ncoef is even. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the stop band. The stop band is [0, f1]. |
| f2 | double | Lowest frequency of the pass band. The pass band is [f2, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. This array must be at least elements long when ncoef is odd. This array must be at least elements long when ncoef is even. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxequirpl_lpfiltering.htm language=enus -->
## TOPIC 00281: CxEquiRpl_LPFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxequirpl_lpfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxequirpl_lpfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxEquiRpl_LPFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType CxEquiRpl_LPFiltering (NIComplexNumber inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double f1, double f2, NIComplexNumber outputArray[]);

#### Purpose

Filter the complex array using a optimal lowpass FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 25-point lowpass FIR filter and filter the complex incoming signal. */ 

 complexnum x[256], y[280];
 double input[256];
 double fs, f1, f2;
 int n, ncoef, i;
 
 fs = 1000.0; // sampling frequency
 f1 = 300.0; // pass band [0, 300]
 f2 = 400.0; // stop band [400, fs/2]
 n = 256; // input signal length
 ncoef = 25; //filter length
 WhiteNoise (n, 1, 17, input); 
 for(i = 0; i < n; i++){
 x[i].real = input[i];
 x[i].imaginary = input[i];
 }
 
 CxEquiRpl_LPFiltering(x, n, ncoef, fs, f1, f2, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the pass band. The pass band is [0, f1]. |
| f2 | double | Lowest frequency of the stop band. The stop band is [f2, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | Filtered data. This array must be at least elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxexbkmanwin.htm language=enus -->
## TOPIC 00282: CxExBkmanWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxexbkmanwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxexbkmanwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxExBkmanWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxExBkmanWin (NIComplexNumber arrayX[], ssize_t numberOfElements);

#### Purpose

Applies an exact Blackman window to the complex input signal. If y represents the output sequence, CxExBkmanWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='exbkwin.gif']

for i = 0, 1, 2, ..., n – 1

| where |  |
| --- | --- |
|  |  |
|  |  |
|  | n is the number of elements in arrayX |

This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in arrayX. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with an exact Blackman window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxflattopwin.htm language=enus -->
## TOPIC 00283: CxFlatTopWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxflattopwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxflattopwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxFlatTopWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxFlatTopWin (NIComplexNumber arrayX[], ssize_t numberOfElements);

#### Purpose

y

CxFlatTopWin

y

y<sub>i</sub> = x<sub>i</sub> (0.215578948 - 0.416631580cos(w) + 0.277263158cos(2w) - 0.083578947cos(3w) + 0.006947368cos(4w))

i

n

[IMAGE alt='image' src='cxflattopwinform_9.png']

where n is the number of elements in **arrayX**. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in arrayX. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a flat top window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxforcewin.htm language=enus -->
## TOPIC 00284: CxForceWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxforcewin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxforcewin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxForceWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxForceWin (NIComplexNumber arrayX[], ssize_t numberOfElements, double dutyCycle);

#### Purpose

Applies a force window to the complex input signal. If y represents the output sequence **arrayX**, CxForceWin obtains the elements of y using the following equation: 

 

 [IMAGE alt='ForceWin.gif' src='forcewin.gif']
 

 

 where n is the number of elements in **arrayX**. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in arrayX. |
| dutyCycle_ | double | Duty cycle, specified as percentage, of the force window. Default Value: 50.0. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with the force window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxgausswin.htm language=enus -->
## TOPIC 00285: CxGaussWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxgausswin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxgausswin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxGaussWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxGaussWin (NIComplexNumber arrayX[], ssize_t numberOfElements, double standardDeviation);

#### Purpose

Applies a Gaussian window to a complex input signal. If y represents the output sequence **arrayX**, CxGaussWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='cxgausswinform_10.png']

where n is the number of elements in **arrayX** and σ is the standard deviation of the Gaussian window. 

 

 This function applies an unsymmetric Gaussian window on the input signal. If you want to use a symmetric Gaussian window, call [SymWin](../../cvi/libref/cvisymwin.htm) instead. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in arrayX. |
| standardDeviation | double | The standard deviation of the Gaussian window normalized to the length of arrayX. The default value is 0.2. If standardDeviation <= 0, the default value is used. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a Gaussian window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxgencoswin.htm language=enus -->
## TOPIC 00286: CxGenCosWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxgencoswin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxgencoswin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxGenCosWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxGenCosWin (NIComplexNumber arrayX[], ssize_t numberOfXElements, double aArray[], int numberOfAElements);

#### Purpose

Applies a general cosine window to the complex input signal. If a represents **aArray** and **Y** represents the output sequence, CxGenCosWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='gencoswin.gif']

for i = 0, 1, 2, ..., n – 1

where na is the number of coefficients and n is the number of elements in **arrayX**.

This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfXElements | ssize_t | Number of elements in arrayX. |
| aArray | double [] | Coefficients used in the general cosine window. |
| numberOfAElements | int | Number of elements in aArray. |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a general cosine window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxgeneigenab.htm language=enus -->
## TOPIC 00287: CxGenEigenAB

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxgeneigenab.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxgeneigenab.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxGenEigenAB

*Advanced Analysis Library Only*

AnalysisLibErrType CxGenEigenAB (void *inputMatrixA, void *inputMatrixB, ssize_t matrixSize, NIComplexNumber eigenvalues[], void *leftEigenvectors, void *rightEigenvectors);

#### Purpose

Computes the generalized eigenvalues, and optionally the left and/or right generalized eigenvectors, for a pair of complex matrices (A,B). The function computes the following generalized eigenproblems: 

 

 [IMAGE alt='image' src='cxgeneigenabform_6.png'] where*V* is the right eigenvectors matrix. 

 

 [IMAGE alt='image' src='cxgeneigenabform_7.png'] where*U* is the left eigenvectors matrix. 

 

 [IMAGE alt='image' src='cxgeneigenabform_8.png'] represents the generalized eigenvalues of (A,B).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrixA | void * | The input matrix A. |
| inputMatrixB | void * | The input matrix B. |
| matrixSize | ssize_t | The order of inputMatrixA and inputMatrixB. |
| Output |  |  |
| Name | Type | Description |
| eigenvalues | NIComplexNumber [] | The generalized eigenvalues of (inputMatrixA, inputMatrixB). |
| leftEigenvectors | void * | The left generalized eigenvectors of (inputMatrixA, inputMatrixB). If leftEigenvectors is NULL, the left generalized eigenvectors are not computed. Each column of leftEigenvectors is a left generalized eigenvector. |
| rightEigenvectors | void * | The right generalized eigenvectors of (inputMatrixA, inputMatrixB). If rightEigenvectors is NULL, the right generalized eigenvectors are not computed. Each column of rightEigenvectors is a right generalized eigenvector. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxgeninvmatrix.htm language=enus -->
## TOPIC 00288: CxGenInvMatrix

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxgeninvmatrix.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxgeninvmatrix.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxGenInvMatrix

*Advanced Analysis Library Only*

AnalysisLibErrType CxGenInvMatrix (void *inputMatrix, ssize_t matrixSize, int matrixMatrixType, void *matrixInverse);

#### Purpose

Calculates the inverse of a complex, square input matrix. If B denotes the inverse of the matrix A, then

AB = I

where **I** is the identity matrix.

The input matrix can be an upper or lower triangular matrix, a general, square matrix, or a positive definite matrix. You can save significant computation time if you properly specify the input matrix type.

|  | Note If you use this function on an ill-conditioned matrix, the result may be inaccurate due to a loss of precision from arithmetic calculations. The results could also vary between machines because National Instruments uses different optimizations based on processor type. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex, square matrix. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| matrixSize | ssize_t | Number of elements in one dimension of the matrix. |
| matrixMatrixType | int | Type of the input matrix. Choose the matrix type correctly because it significantly affects the speed of computation. The following table shows valid matrix type values. Matrix Type Value General matrix 0 Positive definite 1 Lower triangular 2 Upper triangular 3 |
| Matrix Type | Value |  |
| General matrix | 0 |  |
| Positive definite | 1 |  |
| Lower triangular | 2 |  |
| Upper triangular | 3 |  |
| Output |  |  |
| Name | Type | Description |
| matrixInverse | void * | Result complex inverse matrix, as an array of <span class"Monospace">ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxinvch_lpf.htm language=enus -->
## TOPIC 00289: CxInvCh_LPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxinvch_lpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxinvch_lpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxInvCh_LPF

*Advanced Analysis Library Only*

AnalysisLibErrType CxInvCh_LPF (NIComplexNumber inputArray[], ssize_t numberOfElements, double samplingFrequency, double cutoffFrequency, double stopBandAttendb, int order, NIComplexNumber outputArray[]);

#### Purpose

Filters the complex input array using an inverse Chebyshev lowpass digital filter. CxInvCh_LPF can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* Generate a random signal and filter it using a fifth-order lowpass inverse Chebyshev filter. */ 

 NIComplexNumber x[256]; 

 double input[256]; 

 double atten, fs, fc; 

 ssize_t n; 

 int order; 

 int status; 

 int i; 
 

 
 n = 256; 

 fs = 1000.0; 

 fc = 200.0; 

 atten = 40; 

 order = 5; 

 WhiteNoise (n, 1, 17, input); 

 for(i = 0; i < n; i++){

x[i].real = input[i]; 

 x[i].imaginary = input[i];

} 

 status = CxInvCh_LPF (x, n, fs, fc, atten, order, NULL);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in both the input and output array. |
| samplingFrequency | double | The frequency in Hertz at which you want to sample inputArray. This value must be greater than 0. |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. This value must be 0 < cutoffFrequency < 0.5 * samplingFrequency. |
| stopBandAtten_db | double | The amplitude of the stop band attenuation in decibels. This value must be greater than 0. Default Value: 40.0 db. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxinvfft2d.htm language=enus -->
## TOPIC 00290: CxInvFFT2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxinvfft2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxinvfft2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxInvFFT2D

*Advanced Analysis Library Only*

AnalysisLibErrType CxInvFFT2D (void *frequencyDomainSignal, ssize_t numberOfRows, ssize_t numberOfColumns, int shifted, void *fft);

#### Purpose

Computes the complex 2D inverse Fast Fourier Transform (FFT) of a signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| frequencyDomainSignal | void * | The frequency-domain signal. |
| numberOfRows | ssize_t | The number of rows in frequencyDomainSignal. |
| numberOfColumns | ssize_t | The number of columns in frequencyDomainSignal. |
| shifted | int | Specifies whether the DC component is shifted to the center of frequencyDomainSignal. shifted must be one of the following values: FALSE (0): Ordinary FFT. The first element of fft is the DC component.TRUE (1): DC-centered FFT. |
| Output |  |  |
| Name | Type | Description |
| FFT | void * | The complex 2D inverse FFT of the signal. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxinvfftex.htm language=enus -->
## TOPIC 00291: CxInvFFTEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxinvfftex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxinvfftex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxInvFFTEx

*Advanced Analysis Library Only*

AnalysisLibErrType CxInvFFTEx (NIComplexNumber fft[], ssize_t numberOfElements, PFFTTable fftTable, int shifted, NIComplexNumber timeDomainSignal[]);

#### Purpose

Computes the complex inverse Fast Fourier Transform (FFT) of an input sequence. National Instruments recommends you use this function instead of [InvFFT](../../cvi/libref/cviinvfft.htm). 

 

 If you must perform the same size FFT repeatedly, you can use [CreateFFTTable](../../cvi/libref/cvicreateffttable.htm) to create the FFT table and then pass the table you created to CxInvFFTEx to speed computation. If you pass NULL for **fftTable**, the function creates the table internally and frees the table when it returns. 

 

 The following code is the psuedocode for calling FFT routines:

```text
            N=1024; //Set length of signal
            tbl=CreateFFTTable(N);  //Create N-point table
            for(;;){
                Acquire_N_Point_Signal(signal); //Acquire N points
                FFT(signal,..., tbl,...);       //Perform FFT or IFFT
            }
            DestroyFFTTable(tbl);       //End, release FFT table resources
```

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FFT | NIComplexNumber [] | The input frequency domain sequence. |
| numberOfElements | ssize_t | The number of elements in fft. |
| FFTTable | PFFTTable | The FFT table created with CreateFFTTable. You can pass NULL for this parameter if you do not have a reusable FFT table. |
| shifted | int | Specifies whether fft is DC-centered. shifted must be one of the following values: FALSE (0): Not centered. The DC component is the first element of fft.TRUE (1): Centered. |
| Output |  |  |
| Name | Type | Description |
| timeDomainSignal | NIComplexNumber [] | The complex time-domain signal. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxkroneckerprod.htm language=enus -->
## TOPIC 00292: CxKroneckerProd

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxkroneckerprod.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxkroneckerprod.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxKroneckerProd

*Advanced Analysis Library Only*

AnalysisLibErrType CxKroneckerProd (void *inputMatrixX, void *inputMatrixY, ssize_t numberOfRowsInX, ssize_t numberOfColumnsInX, ssize_t numberOfRowsInY, ssize_t numberOfColumnsInY, void *kroneckerProduct);

#### Purpose

This function computes the Kronecker product result matrix z as follows:

[IMAGE alt='image' src='cxkroneckerprodform_9.png']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrixX | void * | The complex input matrix x. |
| inputMatrixY | void * | The complex input matrix y. |
| numberOfRowsInX | ssize_t | The number of the rows of inputMatrixX. |
| numberOfColumnsInX | ssize_t | The number of the columns of inputMatrixX. |
| numberOfRowsInY | ssize_t | The number of the rows of inputMatrixY. |
| numberOfColumnsInY | ssize_t | The number of the columns of inputMatrixY. |
| Output |  |  |
| Name | Type | Description |
| kroneckerProduct | void | The Kronecker product result of inputMatrixX and inputMatrixY. The size of the result is nk-by-ml. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxksrwin.htm language=enus -->
## TOPIC 00293: CxKsrWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxksrwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxksrwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxKsrWin

*Advanced Analysis Library Only*

AnalysisLibErrType CxKsrWin (NIComplexNumber arrayX[], ssize_t numberOfElements, double beta);

#### Purpose

y

arrayX

CxKsrWin

y

[IMAGE alt='image' src='cxksrwinform_11.png']

for i = 0, 1, 2, ..., n – 1

[IMAGE alt='image' src='cxksrwinform_12.png']

[IMAGE alt='image' src='cxksrwinform_13.png']

where n is the number of elements in **arrayX**, and Io(**·**) is the zero-order modified Bessel function.

This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in arrayX. |
| beta | double | Shape used in the Kaiser window function. A larger beta results a narrower window. beta Window 0.00 Rectangular 1.33 Triangle 3.86 Hanning 4.86 (Default) Hamming 7.04 Blackman For more information, refer to Discrete-Time Signal Processing by Oppenheim and Schafer, cited in the Bibliography. |
| beta | Window |  |
| 0.00 | Rectangular |  |
| 1.33 | Triangle |  |
| 3.86 | Hanning |  |
| 4.86 (Default) | Hamming |  |
| 7.04 | Blackman |  |
| Output |  |  |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | On input, the input signal. On output, this parameter returns the input signal with a Kaiser window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxlinev1d.htm language=enus -->
## TOPIC 00294: CxLinEv1D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxlinev1d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxlinev1d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxLinEv1D

AnalysisLibErrType CxLinEv1D (double arrayXReal[], double arrayXImaginary[], ssize_t numberOfElements, double aReal, double aImaginary, double bReal, double bImaginary, double outputArrayReal[], double outputArrayImag[]);

#### Purpose

Performs a linear evaluation of a complex 1D array. CxLinEv1D obtains the i<sup>th</sup> element of the resulting complex array using the following formulas:

outputReal<sub>i</sub> = aReal × arrayXReal<sub>i</sub> – aImg × arrayXImg<sub>i</sub> + bReal

outputImg<sub>i</sub> = aReal × arrayXImg<sub>i</sub> + aImg × arrayXReal<sub>i</sub> + bImg

CxLinEv1D can perform the operations in place; that is, the input and output complex arrays can be the same.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX_Real | double [] | Real part of the complex array used as the basis for the linear evaluation. |
| arrayX_Imaginary | double [] | Imaginary part of the complex array used as the basis for the linear evaluation. |
| numberOfElements | ssize_t | Number of elements to evaluate. |
| a_Real | double | Real part of the multiplicative constant used in the linear evaluation of the input array. Default Value: 1.0. |
| a_Imaginary | double | Imaginary part of the multiplicative constant used in the linear evaluation of the input array. Default Value: 1.0. |
| b_Real | double | Real part of the additive constant used in the linear evaluation of the input array. Default Value: 0.0. |
| b_Imaginary | double | Imaginary part of the additive constant used in the linear evaluation of the input array. Default Value: 0.0. |
| Output |  |  |
| Name | Type | Description |
| outputArray_Real | double [] | Real part of the result of the linear evaluation of the input array. |
| outputArray_Imag | double [] | Imaginary part of the result of the linear evaluation of the input array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxmatrixnorm.htm language=enus -->
## TOPIC 00295: CxMatrixNorm

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxmatrixnorm.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxmatrixnorm.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxMatrixNorm

*Advanced Analysis Library Only*

AnalysisLibErrType CxMatrixNorm (void *inputMatrix, ssize_t numberOfRows, ssize_t numberOfColumns, int normType, double *norm);

#### Purpose

Calculates the norm of the complex input matrix A. The input matrix can be square or rectangular. The norm of a matrix is a scalar that gives some measure of the size of the elements in the matrix. It is similar to the concept of magnitude or absolute value for scalar numbers.

There are different ways to calculate the norm of a matrix. The **normType** parameter indicates which type of norm to use to calculate the norm.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex matrix. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| numberOfRows | ssize_t | The number of rows in inputMatrix. |
| numberOfColumns | ssize_t | The number of columns ininputMatrix. |
| normType | int | Type of norm to calculate. The following table shows valid norm type values. Norm Type Value Meaning 2-norm 0 Largest singular value of inputMatrix. 1-norm 1 Largest column sum of inputMatrix. Frobenius-norm 2 Square root of the sum of the diagonal elements of ATA, where AT is the complex conjugate transpose of A. Infinite-norm 3 Largest row sum of inputMatrix. |
| Norm Type | Value | Meaning |
| 2-norm | 0 | Largest singular value of inputMatrix. |
| 1-norm | 1 | Largest column sum of inputMatrix. |
| Frobenius-norm | 2 | Square root of the sum of the diagonal elements of ATA, where AT is the complex conjugate transpose of A. |
| Infinite-norm | 3 | Largest row sum of inputMatrix. |
| Output |  |  |
| Name | Type | Description |
| norm | double | The norm of inputMatrix. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxnormalizedcorrelate.htm language=enus -->
## TOPIC 00296: CxNormalizedCorrelate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxnormalizedcorrelate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxnormalizedcorrelate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxNormalizedCorrelate

*Advanced Analysis Library Only*

AnalysisLibErrType CxNormalizedCorrelate (NIComplexNumber arrayX[], ssize_t sizeOfX, NIComplexNumber arrayY[], ssize_t sizeOfY, int algorithm, int normalization, NIComplexNumber outputArray[]);

#### Purpose

Finds the correlation of the complex input arrays. The cross correlation Rxy(t) of the sequences x(t) and y(t) is defined by the following equation:

[IMAGE alt='image' src='cxnormalizedcorrelateform_14.png']

where the symbol [IMAGE alt='image' src='cxnormalizedcorrelateform_1.png'] denotes correlation. 

 

 The discrete implementation of this function is as follows. Let h represent a sequence whose indexing can be negative, let N be the number of elements in the input sequence **arrayX**, let M be the number of elements in the sequence **arrayY**, and assume that the indexed elements of **arrayX** and **arrayY** that lie outside their range are equal to zero, as shown by the following equations:

x<sub>j</sub> = 0, j < 0 or j ≥ N

and

y<sub>j</sub> = 0, j < 0 or j ≥ M.

CxNormalizedCorrelate

h

[IMAGE alt='image' src='cxnormalizedcorrelateform_15.png']

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

CxNormalizedCorrelate

N

- Biased normalization 
 
 If normalization is ALGORITHM_CONCOR_BIASED_NORMALIZATION , LabWindows/CVI applies biased normalization as follows: [IMAGE alt='image' src='cxnormalizedcorrelateform_20.png'] for j = 0, 1, 2, ..., M+N–2 

 

 where R<sub>xy</sub> is the cross correlation between x and y with no normalization.
- Unbiased normalization 
 
 If normalization is ALGORITHM_CONCOR_UNBIASED_NORMALIZATION , LabWindows/CVI applies unbiased normalization as follows: 
 
 [IMAGE alt='image' src='cxnormalizedcorrelateform_21.png'] for j = 0, 1, 2, ..., M+N–2 

 

 where R<sub>xy</sub> is the cross correlation between x and y with no normalization. f(j) is: 

 

 [IMAGE alt='noloc_eps_croscor3.gif' src='noloc_eps_croscor3.gif']

|  | Note This function temporarily allocates memory for use as a work area. If CxNormalizedCorrelate cannot allocate memory, the function returns an error code. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | NIComplexNumber [] | First input array. |
| sizeOfX | ssize_t | Number of elements in arrayX. |
| arrayY | NIComplexNumber [] | Second input array. |
| sizeOfY | ssize_t | Number of elements in arrayY. |
| algorithm | int | Specifies the correlation method to use. algorithm must be one of the following values. Note that slight numerical differences can exist between the two methods. Constant Value Description ALGORITHM_CONCOR_DIRECT 0 Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. ALGORITHM_CONCOR_FREQ_DOMAIN 1 Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| Constant | Value | Description |
| ALGORITHM_CONCOR_DIRECT | 0 | Computes the correlation using the direct method of linear correlation. If arrayX and arrayY are small, the ALGORITHM_CONCOR_DIRECT correlation method is typically faster. |
| ALGORITHM_CONCOR_FREQ_DOMAIN | 1 | Computes the correlation using an FFT-based technique. If arrayX and arrayY are large, the ALGORITHM_CONCOR_FREQ_DOMAIN correlation method is typically faster. |
| normalization | int | Specifies the normalization method to use to compute the cross correlation between arrayX and arrayY. normalization must be one of the following values: Constant Value Description ALGORITHM_CORCOR_NO_NORMALIZATION 0 No normalization is used in correlation computation. ALGORITHM_CONCOR_UNBIASED_NORMALIZATION 1 Use max(n, m) to normalize the correlation result. ALGORITHM_CONCOR_BIASED_NORMALIZATION 2 Use the number of elements in arrayX and arrayY for computing Rxy[j] to normalize Rxy[j], j = 0, 1, ..., (n+m–2). |
| Constant | Value | Description |
| ALGORITHM_CORCOR_NO_NORMALIZATION | 0 | No normalization is used in correlation computation. |
| ALGORITHM_CONCOR_UNBIASED_NORMALIZATION | 1 | Use max(n, m) to normalize the correlation result. |
| ALGORITHM_CONCOR_BIASED_NORMALIZATION | 2 | Use the number of elements in arrayX and arrayY for computing Rxy[j] to normalize Rxy[j], j = 0, 1, ..., (n+m–2). |
| Output |  |  |
| Name | Type | Description |
| outputArray | NIComplexNumber [] | The correlation of arrayX and arrayY. This array must be at least (n + m – 1) elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxouterproduct.htm language=enus -->
## TOPIC 00297: CxOuterProduct

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxouterproduct.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxouterproduct.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxOuterProduct

*Advanced Analysis Library Only*

AnalysisLibErrType CxOuterProduct (NIComplexNumber vectorX[], ssize_t numberOfElementsInX, NIComplexNumber vectorY[], ssize_t numberOfElementsInY, void *outerProduct);

#### Purpose

Calculates the outer product of the complex input vectors x and y.

Let x<sub>i</sub> represent the elements of the **numberElementsX**-element vector x for i = 0, 1, 2, . . ., **numberElementsX** – 1.

Let y<sub>j</sub> represent the elements of the **numberElementsY**-element vector y for **j** = 0, 1, 2, . . ., **numberElementsY** – 1.

The outer product of these two vectors is a matrix O of dimensions n-by-m, where the (i, j)<sup>th</sup> element of O is given by

o<sub>i, j</sub> = x<sub>i</sub> × y<sub>j</sub>

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vectorX | NIComplexNumber [] | First vector used to compute the outer product. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| numberOfElementsInX | ssize_t | The number of elements in vectorX. |
| vectorY | NIComplexNumber [] | Second vector used to compute the outer product. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| numberOfElementsInY | ssize_t | The number of elements in vectorY. |
| Output |  |  |
| Name | Type | Description |
| outerProduct | void * | Calculated outer product matrix, as an array of ComplexNum. typedef struct { double real; double imaginary; } ComplexNum; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxpseudoinverse.htm language=enus -->
## TOPIC 00298: CxPseudoInverse

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxpseudoinverse.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxpseudoinverse.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxPseudoInverse

*Advanced Analysis Library Only*

AnalysisLibErrType CxPseudoInverse (void *inputMatrix, ssize_t numberOfRows, ssize_t numberOfColumns, double tolerance, void *matrixPseudoInverse);

#### Purpose

Calculates the generalized inverse of the complex input matrix **A**.The dimensions of the input matrix A are **numberOfRows**-by-**numberOfColumns**. The dimensions of the output matrix (inverse) are **numberOfColumns**-by-**numberOfRows**.

CxPseudoInverse uses the Singular Value Decomposition (SVD) technique. Define the pseudoinverse of a scalar s to be 1/s if s does not equal zero, and zero otherwise. Similarly, define the pseudoinverse of a diagonal matrix by transposing the matrix and then taking the scalar pseudoinverse of each entry. If A<sup>+</sup> denotes the pseudoinverse of a matrix A whose singular value decomposition is given by

A = USV<sup>T</sup>

then:

A<sup>+</sup> = US<sup>+</sup>V<sup>T</sup>

where S<sup>+</sup> is the pseudoinverse of the diagonal matrix S that contains the singular values of A

The pseudoinverse exists for both square and rectangular matrices. If the input matrix is square and nonsingular, the pseudoinverse is the same as the general matrix inverse.

|  | Note Do not use CxPseudoInverse to calculate the inverse of a square matrix because it takes more time. Use CxGenInvMatrix instead. |
| --- | --- |

The **tolerance** parameter must be a small positive number close to machine precision. CxPseudoInverse sets all singular values of the input matrix smaller than **tolerance** equal to zero.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex matrix. The input matrix can be either square or rectangular. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| numberOfRows | ssize_t | The number of rows in inputMatrix. |
| numberOfColumns | ssize_t | The number of columns in inputMatrix. |
| tolerance | double | Tolerance value. All the singular values below this tolerance value are set equal to zero. The value of tolerance determines the level of accuracy in your final solution. Set tolerance close to eps, which is the smallest possible double-precision, floating-point number. |
| Output |  |  |
| Name | Type | Description |
| matrixPseudoInverse | void * | Calculated pseudoinverse matrix, as an array of ComplexNum. This value is numberOfColumns by numberOfRows. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxqr.htm language=enus -->
## TOPIC 00299: CxQR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxqr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxqr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxQR

*Advanced Analysis Library Only*

AnalysisLibErrType CxQR (void *inputMatrix, ssize_t numberOfRows, ssize_t numberOfColumns, void *qMatrix, void *rMatrix);

#### Purpose

|  | Note This function has been superseded by CxQREx. |
| --- | --- |

Calculates the QR factorization of the complex input matrix. The input matrix can be square or rectangular.

The following formula defines the QR factorization of a n-by-m matrix A such that:

A = QR

| where | qMatrix is an orthogonal matrix of dimensions n-by-n |
| --- | --- |
|  | rMatrix is an upper triangular matrix of dimensions n-by-m |
|  | numberOfRows is the number of rows |
|  | numberOfColumns is the number of columns |

In general, QR factorization can be calculated in many different ways. In CxQR, QR factorization uses the Householder algorithm. You can use QR factorization to solve linear systems with more equations than unknowns.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input complex matrix. This matrix must be an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| numberOfRows | ssize_t | The number of rows in inputMatrix. |
| numberOfColumns | ssize_t | The number of columns in inputMatrix. |
| Output |  |  |
| Name | Type | Description |
| qMatrix | void * | Calculated orthogonal matrix of the QR factorization, as an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |
| rMatrix | void * | Calculated upper triangular matrix of the QR factorization, as an array of ComplexNum. The following C typedef statement defines the ComplexNum structure: typedef struct { double real; double imaginary; } ComplexNum; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxqrex.htm language=enus -->
## TOPIC 00300: CxQREx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxqrex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxqrex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxQREx

*Advanced Analysis Library Only*

AnalysisLibErrType CxQREx (void *inputMatrix, ssize_t numberOfRows, ssize_t numberOfColumns, int pivot, int sizeOption, void *pivotInfo, void *qMatrix, void *rMatrix);

#### Purpose

Performs the QR factorization for a complex matrix. CxQREx factorizes matrix A as AP = QR, where P is a permutation matrix, Q is a unitary matrix, and R is an upper triangular matrix. If **numberOfRows** > **numberOfColumns**, **sizeOption** is ECONOMY_SIZE and **rMatrix** is NULL or **inputMatrix**. On output, the leading **numberOfColumns** rows in **inputMatrix** are the upper triangular matrix R. 

 

 National Instruments recommends you use this function instead of [CxQR](../../cvi/libref/cvicxqr.htm). CxQREx includes additional parameters, which make it more versatile than CxQR.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | The matrix to be factorized. |
| numberOfRows | ssize_t | The number of rows of inputMatrix. |
| numberOfColumns | ssize_t | The number of columns of inputMatrix. |
| pivot | int | Specifies how to pivot inputMatrix. pivot must be one of the following values: NOT_PIVOT (0): Do not pivot inputMatrix. That is, factorize inputMatrix as inputMatrix = QR. In this case, pivotInfo is not referenced.PIVOT_VECTOR (1): Pivot inputMatrix and record the pivoting information as a vector in pivotInfo. That is, factorize inputMatrix as AP = QR, where A is inputMatrix. The size of pivotInfo must be numberOfColumns.PIVOT_MATRIX (2): Pivot inputMatrix and record the pivoting information as a matrix in pivotInfo. That is, factorize inputMatrix as AP = QR, where A is inputMatrix. The size of pivotInfo must be numberOfColumns * numberOfColumns. With pivoting, inputMatrix is pivoted so that abs(diag(rMatrix)) are in descending order. |
| sizeOption | int | The size of Q and rMatrix. sizeOption must one of the following values: FULL_SIZE (0): The size of Q is numberOfRows * numberOfRows, and the size of rMatrix is numberOfRows * numberOfColumns.ECONOMY_SIZE (1): The size of Q is numberOfRows * min(numberOfRows, numberOfColumns), and the size of R is min(numberOfRows, numberOfColumns) * numberOfColumns. |
| Output |  |  |
| Name | Type | Description |
| pivotInfo | void * | The pivoting information if pivot is PIVOT_VECTOR or PIVOT_MATRIX. If pivot = PIVOT_VECTOR, pivotInfo is a numberOfColumns element vector. The columns of AP are the columns of A in the following order: pivotInfo[0], pivotInfo[1], pivotInfo[2], . . . , pivotInfo[colA-1].If pivot = PIVOT_MATRIX, pivotInfo is directly the permutation matrix P in AP = QR. If pivot is NOT_PIVOT, you can pass NULL to pivotInfo. |
| qMatrix | void * | The unitary matrix Q. If Q = NULL, qMatrix is not generated. |
| rMatrix | void * | The upper triangular matrix R. rMatrix can be NULL. This function supports in place operation. That is, you can call the function with rMatrix = inputMatrix. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxrecip.htm language=enus -->
## TOPIC 00301: CxRecip

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxrecip.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxrecip.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxRecip

AnalysisLibErrType CxRecip (double xReal, double xImaginary, double *outputReal, double *outputImaginary);

#### Purpose

Finds the reciprocal of a complex number, x. CxRecip obtains the resulting complex number, y, using the following formulas:

[IMAGE alt='image' src='cxrecip.gif']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x_Real | double | Real part of the complex number whose reciprocal is computed. Default Value: 1.0. |
| x_Imaginary | double | Imaginary part of the complex number whose reciprocal is computed. Default Value: 0.0. |
| Output |  |  |
| Name | Type | Description |
| output_Real | double | Real part of the resulting complex reciprocal. |
| output_Imaginary | double | Imaginary part of the resulting complex reciprocal. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\smithchart\smithdem.cws for an example of using the CxRecip function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvicxrifflearray.htm language=enus -->
## TOPIC 00302: CxRiffleArray

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvicxrifflearray.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvicxrifflearray.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CxRiffleArray

*Advanced Analysis Library Only*

AnalysisLibErrType CxRiffleArray (NIComplexNumber inputArray[], ssize_t numberOfElements, int seed, ssize_t index[]);

#### Purpose

Riffles the input array of NIComplexNumber elements by randomly selecting two elements in **inputArray**, swapping those elements, and then repeating this process **numberOfElements** times, where **numberOfElements** is the size of **inputArray**.

##### Example Code

/* The following code riffles the elements in input array x. */ 

ComplexNum x[20]; 

int y[20]; 

int n = 20, i; 

for (i = 0; i < 20; i++) {

x[i].real = i + 0.5; 

 x[i].imaginary = i - 0.5;

} 

CxRiffleArray(x, n, 3, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | NIComplexNumber [] | The input array to riffle. inputArray is overwritten by the riffled array on exit. |
| numberOfElements | ssize_t | Number of elements in inputArray. |
| seed | int | The seed value at which to riffle inputArray. When seed ≥ 0, CxRiffleArray generates a new random sequence using the seed value you specify. When seed < 0, CxRiffleArray generates the sequence as a continuation of the previously generated noise sequence. |
| Output |  |  |
| Name | Type | Description |
| index | ssize_t [] | The corresponding index in the input array for each element in the riffled array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidebugprintf.htm language=enus -->
## TOPIC 00303: DebugPrintf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidebugprintf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidebugprintf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DebugPrintf

int DebugPrintf (const char formatString[], ...);

#### Purpose

Similar to the ANSI C printf function, but writes output to the LabWindows/CVI Debug Output Window, when LabWindows/CVI is debugging the program. If the program is not being debugged,
no output occurs.

(Linux) This function is not supported.

If another development environment is debugging the program, the output can appear in debugging output window of that development environments.

This function does not automatically append a newline character to the output.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| formatString | const char [] | The format string that specifies how subsequent arguments are converted for output. The format string format is identical to the format supported by the ANSI C printf function. Refer to the documentation for the ANSI C printf function for information about the format. If the format requires more arguments than the number of arguments passed to this function, the behavior is undefined. If the format is exhausted while arguments remain, the excess arguments are evaluated but are otherwise ignored. |
| source_s | ... | Specifies one or more arguments that are to be converted and written to the debug output window. You must separate multiple arguments by commas. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| CharactersWritten | int | The number of characters transmitted, or a negative value if an output error occurred. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to compiler\int64\counter.cws for an example of using the DebugPrintf function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidecrementcvitimeinterval.htm language=enus -->
## TOPIC 00304: DecrementCVITimeInterval

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidecrementcvitimeinterval.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidecrementcvitimeinterval.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DecrementCVITimeInterval

int DecrementCVITimeInterval (CVITimeInterval *interval, CVITimeInterval decrement);

#### Purpose

Decrements a time interval value by the specified time interval value.

Time interval values can be negative values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| decrement | CVITimeInterval | A time interval decrement value. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidelay.htm language=enus -->
## TOPIC 00305: Delay

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidelay.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidelay.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Delay

void Delay (double numberOfSeconds);

#### Purpose

Waits the number of seconds that **numberOfSeconds** indicates.

The resolution is normally 1 millisecond. However, if you set the useDefaultTimer configuration option to True, the resolution is 55 milliseconds.

(Linux) The resolution on Linux is 1 millisecond.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfSeconds | double | Number of seconds to wait. |

#### Return Value

None.

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the Delay function:

- networkstreams\cnsGUI.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\GraphAnnotations.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\splash.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvideletedir.htm language=enus -->
## TOPIC 00306: DeleteDir

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvideletedir.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvideletedir.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteDir

int DeleteDir (char directoryName[]);

#### Purpose

Deletes an existing directory.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| directoryName | char [] | The pathname of the directory to delete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -1 Directory not found. -3 General I/O error occurred. -4 Insufficient memory to complete operation. -6 Access denied, or directory not empty. -7 Path is a file, not a directory. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | Directory not found. |  |
| -3 | General I/O error occurred. |  |
| -4 | Insufficient memory to complete operation. |  |
| -6 | Access denied, or directory not empty. |  |
| -7 | Path is a file, not a directory. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvideletefile.htm language=enus -->
## TOPIC 00307: DeleteFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvideletefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvideletefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteFile

int DeleteFile (char fileName[]);

#### Purpose

Deletes an existing file or a group of existing files.

|  | Caution The Windows SDK also contains a function with the same name. Include windows.h before including utility.h to ensure that there are no compilation errors as a result of this naming conflict. Define the SDK_CONFLICT_PRIORITYSDK_CONFLICT_PRIORITY macro to force LabWindows/CVI to use the Windows SDK implementation of this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileName | char [] | The pathname of the file to delete. fileName can contain wildcard characters ? and *, in which case DeleteFile deletes all matching files. If you specify an empty string "", DeleteFile deletes the file found by the most recent call to GetFirstFile or GetNextFile. Note The pattern matching behavior of * is greedy and matches all subsequent characters in the pattern except the file extension. The * wildcard is useful only at the end of a filename or file extension; for example, foo*.doc*. If you use this wildcard in other locations, it matches the rest of the string; for example, *foo.txt matches bar.txt. |
|  | Note The pattern matching behavior of * is greedy and matches all subsequent characters in the pattern except the file extension. The * wildcard is useful only at the end of a filename or file extension; for example, foo*.doc*. If you use this wildcard in other locations, it matches the rest of the string; for example, *foo.txt matches bar.txt. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Result of the delete operation. Code Description 0 Success. -1 File not found or directory in path not found. -3 General I/O error occurred. -4 Insufficient memory to complete operation. -5 Invalid path; for example, c:filename. -6 Access denied. -7 Specified path is a directory, not a file. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | File not found or directory in path not found. |  |
| -3 | General I/O error occurred. |  |
| -4 | Insufficient memory to complete operation. |  |
| -5 | Invalid path; for example, c:filename. |  |
| -6 | Access denied. |  |
| -7 | Specified path is a directory, not a file. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidestroyffttable.htm language=enus -->
## TOPIC 00308: DestroyFFTTable

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidestroyffttable.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidestroyffttable.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DestroyFFTTable

*Advanced Analysis Library Only*

void DestroyFFTTable (PFFTTable fftTable);

#### Purpose

Frees the resources used by an FFT table created with [CreateFFTTable](../../cvi/libref/cvicreateffttable.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FFTTable | PFFTTable | The table whose resources to free. |

#### Return Value

None.

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvideterminant.htm language=enus -->
## TOPIC 00309: Determinant

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvideterminant.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvideterminant.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Determinant

AnalysisLibErrType Determinant (void *inputMatrix, ssize_t matrixSize, double *determinant);

#### Purpose

Finds the determinant of an **n**-by-**n** 2D input matrix.

The result is a scalar value. If the matrix is singular, the determinant is undefined.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Square real matrix whose determinant is computed. |
| matrixSize | ssize_t | Number of rows and columns in the input matrix. |
| Output |  |  |
| Name | Type | Description |
| determinant | double | Determinant of the input matrix. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidifference.htm language=enus -->
## TOPIC 00310: Difference

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidifference.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidifference.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Difference

*Advanced Analysis Library Only*

AnalysisLibErrType Difference (double inputArray[], ssize_t numberOfElements, double samplingInterval, double initialCondition, double finalCondition, double outputArray[]);

#### Purpose

|  | Note This function has been superseded by DifferenceEx. |
| --- | --- |

Finds the discrete difference of the input array. Difference obtains the [IMAGE alt='image' src='ith.gif'] element of the resulting array using the following formula:

[IMAGE alt='image' src='difference.gif']

| where | X–1 is the initial condition |
| --- | --- |
|  | Xn is the final condition |

Difference can perform the operation in place; that is, the input and output arrays can be the same.

##### Example

/* Generate an array with random numbers and differentiate it. */ 

double x[200], y[200]; 

double dt, xInit, xFinal; 

int n; 

n = 200; 

dt = 0.001; 

xInit = -0.5; 

xFinal = -0.25; 

Uniform (n, 17, x); 

Difference (x, n, dt, xInit, xFinal, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Input array to differentiate. |
| numberOfElements | ssize_t | Number of elements to include in the differentiation. |
| samplingInterval | double | Sampling interval used in the differentiation of the input array. Default Value: 1.0. |
| initialCondition | double | Initial condition. When the differentiation formula is applied to each array element, the value of the preceding array element is used. initialCondition specifies the value preceding the first element of the input array. In other words, initialCondition can be thought of as the value of X–1. Default Value: 0.0. |
| finalCondition | double | Final condition. When the differentiation formula is applied to each array element, the value of the next array element is used. finalCondition specifies the value following the last element of the input array. In other words, finalCondition can be thought of as the value of Xn. Default Value: 0.0. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Differentiated array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidifferenceex.htm language=enus -->
## TOPIC 00311: DifferenceEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidifferenceex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidifferenceex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DifferenceEx

*Advanced Analysis Library Only*

AnalysisLibErrType DifferenceEx (double inputArray[], ssize_t numberOfElements, double samplingInterval, double initialConditions[], ssize_t initialConditionsSize, double finalConditions[], ssize_t finalConditionsSize, int differenceMethod, double outputArray[]);

#### Purpose

Differentiates the input signal **inputArray** using the second order central, fourth order central, forward, or backward differentiation method. 

 

 If **differenceMethod** is SECOND_ORDER_CENTRAL_DIFF, **outputArray** is given by

[IMAGE alt='image' src='differenceexform_22.png']

for i = 0,1,2,...,n-1 where n is the length of **inputArray**, x_{-1} is the first element in **initialConditions**, and x_{n} is the first element in **finalConditions**. 

 

 If **differenceMethod** is FOURTH_ORDER_CENTRAL_DIFF, **outputArray** is given by

[IMAGE alt='image' src='differenceexform_23.png']

for i = 0,1,2,...,n-1 

 

 where n is the length of **inputArray**, x_{-2} and x_{-1} are the first and second elements in **initialConditions**, x_{n} and x_{n+1}are the first and second elements in final condition. 

 

 If **differenceMethod** is FORWARD_DIFF, **outputArray** is given by

[IMAGE alt='image' src='differenceexform_24.png']

for i = 0,1,2,...,n-1 

 

 where n is the length of **inputArray**, x_{n} is the first element in **finalConditions**. 

 

 If **differenceMethod** is BACKWARD_DIFF, **outputArray** is given by:

[IMAGE alt='image' src='differenceexform_25.png']

for i = 0,1,2,...,n-1 

 

 where n is the length of **inputArray**, x_{-1} is the first element of **initialConditions**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The length of inputArray. |
| samplingInterval | double | The sampling interval. samplingInterval must be greater than zero. |
| initialConditions | double [] | The initial condition array of inputArray. The function uses the first element in initialConditions to calculate the derivative if differenceMethod is SECOND_ORDER_CENTRAL_DIFF or BACKWARD_DIFF. The function uses the first two elements in initialConditions to calculate the derivative if differenceMethod is FOURTH_ORDER_CENTRAL_DIFF. |
| initialConditionsSize | ssize_t | The length of initialConditions. If differenceMethod is SECOND_ORDER_CENTRAL_DIFF or BACKWARD_DIFF, initialConditionsSize must be 1. If differenceMethod is FOURTH_ORDER_CENTRAL_DIFF, initialConditionsSize must be 2. |
| finalConditions | double [] | The final condition array of inputArray. The function uses the first element in finalConditions to calculate the derivative if differenceMethod is SECOND_ORDER_CENTRAL_DIFF or FORWARD_DIFF. The function uses the first two elements in finalConditions to calculate the derivative if method is FOURTH_ORDER_CENTRAL_DIFF. |
| finalConditionsSize | ssize_t | The length of finalConditions. If differenceMethod is SECOND_ORDER_CENTRAL_DIFF or FORWARD_DIFF, finalConditionsSize must be 1. If differenceMethod is FOURTH_ORDER_CENTRAL_DIFF, finalConditionsSize must be 2. |
| differenceMethod | int | The differentiation method. differenceMethod must be one of the following values: SECOND_ORDER_CENTRAL_DIFF (0)FOURTH_ORDER_CENTRAL_DIFF (1)FORWARD_DIFF (2)BACKWARD_DIFF (3) |
| Output |  |  |
| Name | Type | Description |
| inputArray | double [] | The sampled signal to perform differentiation. If outputArray is NULL, the differentiation result overwrites inputArray. |
| outputArray | double [] | The differentiation of inputArray. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidilogarithm.htm language=enus -->
## TOPIC 00312: Dilogarithm

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidilogarithm.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidilogarithm.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Dilogarithm

*Advanced Analysis Library Only*

double Dilogarithm (double x);

#### Purpose

Computes the dilogarithm function, also known as Spence's Integral, which is defined as follows:

[IMAGE alt='image' src='dilogarithmform_44.png']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | The input parameter that specifies the integral range. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | The value of the dilogarithm function. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidisablebreakonlibraryerrors.htm language=enus -->
## TOPIC 00313: DisableBreakOnLibraryErrors

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidisablebreakonlibraryerrors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidisablebreakonlibraryerrors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisableBreakOnLibraryErrors

void DisableBreakOnLibraryErrors (void);

#### Purpose

|  | Note This function has been superseded by SetBreakOnLibraryErrors. |
| --- | --- |

Directs LabWindows/CVI not to display a run-time error dialog box when a National Instruments library function reports an error.

In general, you should use the **Run»Break on»Library Errors** option in the Workspace window to disable this option. However, you can use this function in conjunction with [EnableBreakOnLibraryErrors](../../cvi/libref/cvienablebreakonlibraryerrors.htm) to temporarily suppress the **Run»Break on»Library Errors** feature around a segment of code. DisableBreakOnLibraryErrors does not affect the state of the **Run»Break on»Library Errors** option in the Workspace window.

#### Parameters

None.

#### Return Value

None.

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to networkvariable\Buffering\NVBuffering.cws for an example of using the DisableBreakOnLibraryErrors function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidisableinterrupts.htm language=enus -->
## TOPIC 00314: DisableInterrupts

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidisableinterrupts.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidisableinterrupts.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisableInterrupts

void DisableInterrupts (void);

#### Purpose

|  | Note (Windows) This function is obsolete and nonfunctional. |
| --- | --- |

(Linux) DisableInterrupts uses sigprocmask to block all unblockable signals.

#### Parameters

None.

#### Return Value

None.

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidisabletaskswitching.htm language=enus -->
## TOPIC 00315: DisableTaskSwitching

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidisabletaskswitching.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidisabletaskswitching.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisableTaskSwitching

void DisableTaskSwitching (void);

#### Purpose

|  | Note This function is obsolete. For information about alternative methods for disabling task switching on Windows 2000 and later, refer to the Alternatives on Windows 2000 and Later section in this topic. |
| --- | --- |

Prevents the user from using <Alt-Tab>, <Alt-Esc>, or <Ctrl-Esc> key combination to switch another task.

DisableTaskSwitching affects the behavior of these keys only while a LabWindows/CVI executable is the active application.

If you configure Windows 9*x* to hide the taskbar, DisableTaskSwitching also prevents the user from using the mouse to bring up the taskbar.

DisableTaskSwitching has no effect on Windows 2000 and later. Refer to the *Alternatives on Windows 2000 and Later* section in this function description for instructions on how to achieve the required effect.

|  | Note On Windows 98, DisableTaskSwitching requires the LabWindows/CVI low-level support driver. LabWindows/CVI loads the driver at startup if it is on disk. You can check whether LabWindows/CVI loaded the driver at startup by calling CVILowLevelSupportDriverLoaded. |
| --- | --- |

(Linux) This function is not supported.

**Disabling the Task List**

DisableTaskSwitching does not prevent the user from clicking on the taskbar on Windows 98. You can prevent the user from clicking on the desktop by forcing your window to cover the entire screen.

**Forcing Window to Cover Entire Screen**

You can force your window to cover the entire screen by making the following calls to functions in the User Interface Library.

SetPanelAttribute (panel, ATTR_SIZABLE, FALSE);

SetPanelAttribute (panel, ATTR_CAN_MINIMIZE, FALSE);

SetPanelAttribute (panel, ATTR_CAN_MAXIMIZE, FALSE);

SetPanelAttribute (panel, ATTR_SYSTEM_MENU_VISIBLE, FALSE);

SetPanelAttribute (panel, ATTR_MOVABLE, FALSE);

SetPanelAttribute (panel, ATTR_WINDOW_ZOOM, VAL_MAXIMIZE);

In these calls, panel is the panel handle for your top-level window.

**Alternatives on Windows 98**

On Windows 98, you can arrange for your stand-alone application to appear in place of the desktop when Windows boots.

You can do this by changing the following line in your system.ini [boot] section from:

shell = Explorer.exe

to:

shell = full-path-of-your-executable

**Alternatives on Windows 2000 and Later**

On Windows 2000 and later, you can obtain the same results as DisableTaskSwitching by specifying for your LabWindows/CVI application to appear in place of the Program Manager and by disabling the Task Manager. Complete the following changes to the registry entry for the key name:

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon

- Change the value for shell to the pathname of your application executable.
- Add a value with the name taskman . Set the data to an empty string.

**Preventing Interference with Real-Time Processing**

On Windows, many user actions can interfere with real-time processing. The following actions suspend the processing of events.

- Moving and sizing top-level windows
- Accessing the System menu
- Pressing the <Alt-Tab> key combination

You can prevent these user actions from interfering with event processing by performing the following actions:

- Call DisableTaskSwitching or use the alternative for Windows 2000 and later.
- Make all your top-level panels nonmovable and nonsizable.
- Do not use the Standard I/O Window in your final application.
- Make the following calls if you use any of the built-in pop-ups in the User Interface Library:
  - SetSystemPopupsAttribute (ATTR_MOVABLE, 0);
  - SetSystemPopupsAttribute (ATTR_SYSTEM_MENU_VISIBLE, 0);

An alternative approach is available on Windows 2000 and later. You can enable timer control callbacks while the user presses <Alt-Tab>, pulls down the **System** menu, or, in some cases, moves or sizes a window. You can do this by using the following function call:

SetSystemAttribute (ATTR_ALLOW_UNSAFE_TIMER_EVENTS, 1);

This alternative approach is incomplete and can be unsafe. Refer to the discussion on [ATTR_ALLOW_UNSAFE_TIMER_EVENTS](../../cvi/uiref/cviattrallowunsafetimerevents.htm).

#### Parameters

None.

#### Return Value

None.

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidisconnectfromddeserver.htm language=enus -->
## TOPIC 00316: DisconnectFromDDEServer

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidisconnectfromddeserver.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidisconnectfromddeserver.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisconnectFromDDEServer

int DisconnectFromDDEServer (unsigned int conversationHandle);

#### Purpose

Terminates a connection between the client and the server.

|  | Note DisconnectFromDDEServer ends only the client–server conversation that conversationHandle identifies. Multiple, concurrent conversations can exist between a client and a server. |
| --- | --- |

DisconnectFromDDEServer returns zero for success or a negative [error code](../../cvi/libref/cvidde_library_error_conditions.htm) for failure.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| conversationHandle | unsigned int | The conversation handle that uniquely represents the connection between the server and the client. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number represents the error code. For functions that read or write data (ClientDDERead, ClientDDEWrite, ServerDDEWrite, AdviseDDEDataReady, BroadcastDDEDataReady), if the function was successful, the return value is the number of bytes transferred. For other DDE Support Library functions, zero represents successful execution. The enumerated type that specifies the absolute values of the error codes is declared in ddesupp.h. For instance, if an invalid parameter is passed, –kDDE_InvalidParameter is returned. Currently, a maximum of 255 concurrent conversations are allowed at any one time. If you exceed this limit, –kDDE_TooManyConversations will be returned. Error codes from –16 to –33 are native DDEML errors, which correspond to Windows DDE error codes starting from 0x4000. |

#### Additional Information

**Library:** [DDE Support Library](../../cvi/libref/cvidde_library_function_tree.htm)

**Include file:** ddesupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidisconnectfromtcpserver.htm language=enus -->
## TOPIC 00317: DisconnectFromTCPServer

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidisconnectfromtcpserver.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidisconnectfromtcpserver.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisconnectFromTCPServer

int DisconnectFromTCPServer (unsigned int conversationHandle);

#### Purpose

Terminates a connection between the [TCP client](../../cvi/libref/cvitcp_clients_and_servers.htm) and the TCP server.

|  | Note DisconnectFromTCPServer terminates only the connection conversationHandle identifies. There can be more than one conversation between a client and a server. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| conversationHandle | unsigned int | The conversation handle that uniquely represents the connection between the server and the client. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. You can call the GetTCPSystemErrorString function to obtain a system message that describes the error. The system messages can be more descriptive than the TCP Support Library error codes. To obtain the correct system error message, you must call GetTCPSystemErrorString immediately after calling the TCP Support Library function that failed. For RegisterTCPServer and RegisterTCPServerEx, the return value is the port number assigned by the system if you passed zero for the port and the function was successful. For functions that read or write data (ClientTCPRead, ClientTCPWrite, ServerTCPRead, ServerTCPWrite), if the function was successful, the return value is the number of bytes transferred. You can have a maximum of 255 concurrent conversations and up to 1,024 connections. If you exceed this limit, -kTCP_TooManyConnections will be returned. You may not be able to open the maximum number of connections allowed by LabWindows/CVI because of limitations imposed by the operating system. |

#### Additional Information

**Library:** [TCP Support Library](../../cvi/libref/cvitcp_library_function_tree.htm)

**Include file:** tcpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the DisconnectFromTCPServer function:

- tcp\client.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- tcp\message.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- tcp\MultiThreading.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidotnet_errors_exceptions.htm language=enus -->
## TOPIC 00318: .NET Errors and Exceptions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidotnet_errors_exceptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidotnet_errors_exceptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### .NET Errors and Exceptions

If an error occurs during a call to a function in the LabWindows/CVI .NET Library, the **status** return value contains the [error code](cvidotnet_library_error.htm). You can use [CDotNetGetErrorDescription](cvicdotnetgeterrordescription.htm) to get a description of the error code. The LabWindows/CVI .NET Library error codes are defined in cvi\include\cvidotnet.h.

.NET assemblies return exceptions to indicate incorrect function behavior. Whenever an exception is caught and returned, the function in which the exception occurred returns an error code in the return value. LabWindows/CVI returns either a specific .NET Library error code that corresponds to the exception or CDotNetExceptionError.

Some generated wrapper functions and LabWindows/CVI .NET Library functions include an **exceptionHandle** parameter, which returns a handle to the thrown exception. You can pass the exception handle to [CDotNetGetExceptionInfo](cvicdotnetgetexceptioninfo.htm) to get information about the exception. If a function does not include an **exceptionHandle** parameter, only the error code is available.

|  | Note You must use CDotNetDiscardHandle to discard any exception handles the .NET assemblies return. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidotnet_sample_code.htm language=enus -->
## TOPIC 00319: Sample Code for Calling .NET Assemblies

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidotnet_sample_code.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidotnet_sample_code.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Sample Code for Calling .NET Assemblies

The following sections of code show a sample .NET assembly written in both Microsoft Visual C# and Microsoft Visual Basic .NET. The sections also include sample code for calling the .NET assembly in Visual C#, Visual Basic .NET, and LabWindows/CVI. Click the arrow next to the section heading to view the sample code.

[IMAGE alt='image' src='../arrow_close.gif'] **Sample .NET Assembly Written in Visual C#**

// Namespace 

namespace MyNamespace 

{

// Enumerations 

 public enum MyEnum1 { MyValue1, MyValue2, MyValue3 } 

 public enum MyEnum2 { MyValue1, MyValue2 } 
 


 // Class definition 

 public class MyClass1 

 {

// Constructors 

 public MyClass1() { } 
 
 public MyClass1(string s) { } 
 


 // Instance methods 

 public double MyMethod(int i) { return System.Convert.ToDouble(i); } 
 


 public string MyStringMethod(string strIn, out string strOut, ref string strRef) 

 {

string strReturnValue = strRef; 

 strRef = strIn; 

 strOut = strIn + strReturnValue; 

 return strReturnValue;

} 
 


 public double[] MyArrayMethod(string[] arrayIn, out float[] arrayOut, ref string[] arrayRef) 

 {

arrayRef = arrayIn; 

 arrayOut = new float[] { 0.0F, 1.0F }; 

 return new double [] { 0.0, 1.0 };

} 
 


 public MyStruct MyObjectMethod(MyDerivedClass objIn, out MyBaseClass objOut, ref MyInterface objRef) 

 {

objOut = objIn; 

 objRef = objIn; 

 MyStruct result = new MyStruct(); 

 result.Field1 = 1; 

 result.Field2 = 2.0; 

 result.Field3 = "abc"; 

 return result;

} 
 


 public MyEnum2 MyEnumMethod(MyEnum1 enumIn, out MyEnum1 enumOut, ref MyEnum1 enumRef) 

 {

enumOut = enumRef; 

 enumRef = enumIn; 

 return MyEnum2.MyValue2;

} 
 


 public T MyGenericMethod<T, S>(T tIn, S sIn) { return tIn; } 
 

 
 // Static method 

 public static void MyStaticMethod() { } 
 


 // Instance properties 

 public int MyReadWriteProperty 

 {

get { return MyField; } 

 set { MyField = value;}

} 
 


 public int MyReadOnlyProperty 

 {

get { return MyField; }

} 
 


 public int MyWriteOnlyProperty 

 {

set { MyField = value;}

} 
 


 // Static property 

 public static int MyStaticProperty 

 {

get { return MyStaticField; } 

 set { MyStaticField = value;}

} 
 


 // Instance field 

 public int MyField; 
 


 // Static field 

 public static int MyStaticField; 
 


 // Nested class 

 public class MyNestedClass 

 {

public MyNestedClass() { }

}

} 
 


 // Struct definition 

 public struct MyStruct 

 {

public int Field1; 

 public double Field2; 

 public string Field3;

} 
 


 // Interface definition 

 public interface MyInterface 

 {

void InterfaceFunc();

} 
 


 // Base class 

 public class MyBaseClass 

 {

public void BaseClassFunc() { }

} 
 


 // Derived class 

 public class MyDerivedClass : MyBaseClass, MyInterface 

 {

public void InterfaceFunc() { }

} 
 

 
 // Generic class 

 public class MyGenericClass<T, S> 

 {

public MyGenericClass() { } 
 


 public int MyMethod(T tIn) { return 0; } 

 public S MyGenericMethod<M>(M mIn) { return _s; } 
 


 public T Type1 

 {

get { return _t; } 

 set { _t = value; }

} 
 


 public S Type2 

 {

get { return _s; } 

 set { _s = value; }

} 
 


 private T _t; 

 private S _s;

}

}

[IMAGE alt='image' src='../arrow_close.gif'] **Sample .NET Assembly Written in Visual Basic .NET**

Namespace MyNamespace

' Enumerations 

 Public Enum MyEnum1

MyValue1 

 MyValue2 

 MyValue3

End Enum 
 


 Public Enum MyEnum2

MyValue1 

 MyValue2

End Enum 
 


 ' Class definition 

 Public Class MyClass1

' Constructors 

 Public Sub New() 

 End Sub 
 


 Public Sub New(ByVal s As String) 

 End Sub 
 


 ' Instance methods 

 Public Function MyMethod(ByVal i As Integer) As Double

Return System.Convert.ToDouble(i)

End Function 
 


 Public Function MyStringMethod(ByVal strIn As String, ByRef strOut As String, ByRef strRef As String) As String

Dim strReturnValue As String = strRef 

 strRef = strIn 

 strOut = (strIn + strReturnValue) 

 Return strReturnValue

End Function 
 


 Public Function MyArrayMethod(ByVal arrayIn() As String, ByRef arrayOut() As Single, ByRef arrayRef() As String) As Double()

arrayRef = arrayIn 

 arrayOut = New Single() {0.0!, 1.0!} 

 Return New Double() {0, 1}

End Function 
 


 Public Function MyObjectMethod(ByVal objIn As MyDerivedClass, ByRef objOut As MyBaseClass, ByRef objRef As MyInterface) As MyStruct

objOut = objIn 

 objRef = objIn 

 Dim result As MyStruct = New MyStruct 

 result.Field1 = 1 

 result.Field2 = 2 

 result.Field3 = "abc" 

 Return result

End Function 
 


 Public Function MyEnumMethod(ByVal enumIn As MyEnum1, ByRef enumOut As MyEnum1, ByRef enumRef As MyEnum1) As MyEnum2

enumOut = enumRef 

 enumRef = enumIn 

 Return MyEnum2.MyValue2

End Function 
 

 
 Public Function MyGenericMethod(Of T, S)(ByVal tIn As T, ByVal sIn As S) As T

Return tIn

End Function 
 


 ' Static method 

 Public Shared Sub MyStaticMethod() 

 End Sub 
 


 ' Instance properties 

 Public Property MyReadWriteProperty() As Integer

Get 

    Return MyField 

 End Get 

 Set(ByVal Value As Integer) 

    MyField = Value 

 End Set

End Property 
 


 Public ReadOnly Property MyReadOnlyProperty() As Integer

Get 

    Return MyField 

 End Get

End Property 
 


 Public WriteOnly Property MyWriteOnlyProperty() As Integer

Set(ByVal Value As Integer) 

    MyField = Value 

 End Set

End Property 
 


 ' Static property 

 Public Shared Property MyStaticProperty() As Integer

Get 

    Return MyStaticField 

 End Get 

 Set(ByVal Value As Integer) 

    MyStaticField = Value 

 End Set

End Property 
 


 ' Instance field 

 Public MyField As Integer 
 


 ' Static field 

 Public Shared MyStaticField As Integer 
 


 ' Nested class 

 Public Class MyNestedClass

Public Sub New() 

    MyBase.New() 

 End Sub

End Class

End Class 
 


 ' Structure definition 

 Public Structure MyStruct

Public Field1 As Integer 

 Public Field2 As Double 

 Public Field3 As String

End Structure 
 


 ' Interface definition 

 Public Interface MyInterface

Sub InterfaceFunc()

End Interface 
 


 ' Base class definition 

 Public Class MyBaseClass

Public Sub BaseClassFunc() 

 End Sub

End Class 
 


 ' Derived class definition 

 Public Class MyDerivedClass

Inherits MyBaseClass 

 Implements MyInterface 
 


 Public Sub InterfaceFunc() Implements MyInterface.InterfaceFunc 

 End Sub

End Class 
 

 
 ' Generic class 

 Public Class MyGenericClass(Of T, S)

Public Sub New() 

 End Sub 
 


 Public Function MyMethod(ByVal tIn As T) As Integer

Return 0

End Function 
 


 Public Function MyGenericMethod(Of M)(ByVal mIn As M) As S

Return _s

End Function 
 


 Public Property Type1() As T

Get

Return _t

End Get 
 


 Set(ByVal Value As T)

_t = Value

End Set

End Property 
 


 Public Property Type2() As S

Get

Return _s

End Get 
 


 Set(ByVal Value As S)

_s = Value

End Set

End Property 
 


 Private _t As T 
 


 Private _s As S

End Class

End Namespace

[IMAGE alt='image' src='../arrow_close.gif'] **Sample Code for Calling the Assembly in Visual C#**

//--------------------------------------------------------------------------------- 

// Creating objects 

MyNamespace.MyClass1 obj1 = new MyNamespace.MyClass1(); 

MyNamespace.MyClass1 obj2 = new MyNamespace.MyClass1("hello"); 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Calling instance methods 

obj1.MyMethod(0);

string strOut, strRef = "abc"; 

string strReturnValue = obj1.MyStringMethod("xyz", out strOut, ref strRef);

float[] arrayOut; 

string[] arrayRef = new string[] { "X", "Y", "Z" }; 

double[] arrayReturnValue = obj1.MyArrayMethod( 

    new string[] { "a", "b" }, out arrayOut, ref arrayRef);

MyNamespace.MyBaseClass objOut; 

MyNamespace.MyInterface objRef = null; 

MyNamespace.MyStruct objReturnValue = obj1.MyObjectMethod( 

    new MyNamespace.MyDerivedClass(), out objOut, ref objRef);

// Creating a .NET list containing strings 

System.Collections.ArrayList stringList = new System.Collections.ArrayList(arrayRef);

// Iterating through a collection using IEnumerator 

foreach (string s in stringList) 

    Console.WriteLine(s);

// Iterating through a collection using indexer 

for (int i = 0; i < stringList.Count; ++i) 

    Console.WriteLine((string) stringList[i]);

MyNamespace.MyEnum1 enumOut, enumRef = MyNamespace.MyEnum1.MyValue2; 

MyNamespace.MyEnum2 enumReturnValue = obj1.MyEnumMethod( 

    MyNamespace.MyEnum1.MyValue1, out enumOut, ref enumRef);

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Calling static method 

MyNamespace.MyClass1.MyStaticMethod(); 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Instance properties 

int property = obj1.MyReadWriteProperty; 

obj1.MyReadWriteProperty = 2;

property = obj1.MyReadOnlyProperty; 

obj1.MyWriteOnlyProperty = 3; 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Static property 

MyNamespace.MyClass1.MyStaticProperty = 4; 

property = MyNamespace.MyClass1.MyStaticProperty; 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Instance field 

int field = obj1.MyField; 

obj1.MyField = field + 1; 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Static field 

MyNamespace.MyClass1.MyStaticField = field; 

field = MyNamespace.MyClass1.MyStaticField; 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Creating structure 

MyNamespace.MyStruct structure;

// Accessing structure fields 

structure.Field1 = 1; 

structure.Field2 = 3.1415; 

structure.Field3 = "hello"; 

field = structure.Field1; 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Nested class 

MyNamespace.MyClass1.MyNestedClass obj3 = new MyNamespace.MyClass1.MyNestedClass(); 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Inheritance 

MyNamespace.MyDerivedClass derObj = new MyNamespace.MyDerivedClass(); 

derObj.BaseClassFunc(); 

derObj.InterfaceFunc(); 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Calling generic method of non-generic class 

int result = obj1.MyGenericMethod<int, string>(1, "Hi"); 

//---------------------------------------------------------------------------------

//--------------------------------------------------------------------------------- 

// Creating and using generic class 

MyNamespace.MyGenericClass<int, string> genObj = new MyNamespace.MyGenericClass<int, string>(); 

genObj.Type1 = 1; 

genObj.Type2 = "Hi"; 

int intVal = genObj.Type1; 

string strVal = genObj.Type2; 

intVal = genObj.MyMethod(2); 

strVal = genObj.MyGenericMethod<double>(1.1); 

//---------------------------------------------------------------------------------

[IMAGE alt='image' src='../arrow_close.gif'] **Sample Code for Calling the Assembly in Visual Basic .NET**

'---------------------------------------------------------------------------------- 

' Creating objects 

Dim obj1 As MyNamespace.MyClass1 = New MyNamespace.MyClass1 

Dim obj2 As MyNamespace.MyClass1 = New MyNamespace.MyClass1("hello") 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Calling instance methods 

obj1.MyMethod(0)

Dim strOut, strRef, strReturnValue As String 

strRef = "abc" 

strReturnValue = obj1.MyStringMethod("xyz", strOut, strRef)

Dim arrayOut As Single() 

Dim arrayRef As String() = New String() {"X", "Y", "Z"} 

Dim arrayReturnValue As Double() 

arrayReturnValue = obj1.MyArrayMethod(New String() {"a", "b"}, arrayOut, arrayRef)

' Creating a .NET list containing strings 

Dim stringList As System.Collections.ArrayList = New System.Collections.ArrayList(arrayRef)

' Iterating through a collection using IEnumerator 

For Each s As String In stringList 

    Console.WriteLine(s) 

Next

'Iterating through a collection using indexer 

For i As Integer = 1 To stringList.Count 

    Console.WriteLine(stringList(i - 1)) 

Next

Dim objOut As MyNamespace.MyBaseClass 

Dim objRef As MyNamespace.MyInterface = Nothing 

Dim objReturnValue As MyNamespace.MyStruct 

objReturnValue = obj1.MyObjectMethod(New MyNamespace.MyDerivedClass, objOut, objRef)

Dim enumOut, enumRef As MyNamespace.MyEnum1 

enumRef = MyNamespace.MyEnum1.MyValue2 

Dim enumReturnValue As MyNamespace.MyEnum2 

enumReturnValue = obj1.MyEnumMethod(MyNamespace.MyEnum1.MyValue1, enumOut, enumRef) 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Calling static method 

MyNamespace.MyClass1.MyStaticMethod() 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Instance properties 

Dim property1 As Integer = obj1.MyReadWriteProperty 

obj1.MyReadWriteProperty = 2

property1 = obj1.MyReadOnlyProperty 

obj1.MyWriteOnlyProperty = 3 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Static property 

MyNamespace.MyClass1.MyStaticProperty = 4 

property1 = MyNamespace.MyClass1.MyStaticProperty 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Instance field 

Dim field As Integer = obj1.MyField 

obj1.MyField = field + 1 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Static field 

MyNamespace.MyClass1.MyStaticField = field 

field = MyNamespace.MyClass1.MyStaticField 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Creating structure 

Dim structure1 As MyNamespace.MyStruct

' Accessing structure fields 

structure1.Field1 = 1 

structure1.Field2 = 3.1415 

structure1.Field3 = "hello" 

field = structure1.Field1 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Nested class 

Dim obj3 As MyNamespace.MyClass1.MyNestedClass = New MyNamespace.MyClass1.MyNestedClass 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Inheritance 

Dim derObj As MyNamespace.MyDerivedClass = New MyNamespace.MyDerivedClass 

derObj.BaseClassFunc() 

derObj.InterfaceFunc() 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Calling generic method of non-generic class 

Dim result As Integer = obj1.MyGenericMethod(Of Integer, String)(1, "Hi") 

'----------------------------------------------------------------------------------

'---------------------------------------------------------------------------------- 

' Creating and using generic class 

Dim genObj As MyNamespace.MyGenericClass(Of Integer, String) = New MyNamespace.MyGenericClass(Of Integer, String) 

genObj.Type1 = 1 

genObj.Type2 = "Hi" 

Dim intVal As Integer = genObj.Type1 

Dim strVal As String = genObj.Type2 

intVal = genObj.MyMethod(2) 

strVal = genObj.MyGenericMethod(Of Double)(1.1) 

'----------------------------------------------------------------------------------

[IMAGE alt='image' src='../arrow_close.gif'] **Sample Code for Calling the Assembly in LabWindows/CVI**

|  | Note If you generate wrappers for a generic type constructor or a generic method, LabWindows/CVI includes additional string parameters for passing the generic type arguments in the form of .NET type names. Any parameters of the specialized types are typed as void * in the generated wrapper. Always pass the values for these parameters by reference. The .NET code void Foo<T>(T t) is wrapped as Foo (..., char *T, void *t). The user must pass the value for t by reference. For example, Foo<int>(10) in .NET becomes the following code in C: int t = 10; Foo(..., "System.Int32", &t);. |
| --- | --- |

#include <ansi_c.h> 

#include <mscorlib.h>      // NOTE - for using ArrayList and IEnumerator 

#include <MyAssembly.h>

void main(void) 

{

//----------------------------------------------------------------------------- 

 // Variable declarations 

 MyNamespace_MyClass1
               
 obj1, obj2; 

 int
                   
             
 i, arrayOutLength, arrayRefLength, 

                                    
 arrayReturnValueLength, result, intVal, 

                                    
property, field, notEmpty, nItems; 

 char                 
              
 * strOut, * strRef, * strReturnValue, 

                                    
* arrayIn[] = { "a", "b" }, 

                                    
** arrayRef; 

 float                              
* arrayOut; 

 double                             
* arrayReturnValue, dblVal; 

MyNamespace_MyBaseClass            
objOut; 

MyNamespace_MyInterface            
objRef = 0; 

MyNamespace_MyEnum1                
enumOut, 

                                   
enumRef = MyNamespace_MyEnum1_MyValue2; 

MyNamespace_MyEnum2                
enumReturnValue; 

MyNamespace_MyStruct               
structure, objReturnValue; 

MyNamespace_MyClass1_MyNestedClass 
obj3; 

MyNamespace_MyDerivedClass         
objIn, derObj; 

System_Collections_ArrayList       
stringList; 

System_Collections_IEnumerator      enumerator; 

MyNamespace_MyGenericClass_T2       genObj; 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // NOTE - must call the Initialize function before calling other functions 

 Initialize_MyAssembly(); 

 Initialize_mscorlib(); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Creating objects 

 MyNamespace_MyClass1__Create(&obj1, 0); 

 MyNamespace_MyClass1__Create_1(&obj2, "hello", 0);

// NOTE - object handles must be discarded after use by calling CDotNetDiscardHandle 

 CDotNetDiscardHandle(obj2); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Calling instance methods 

 MyNamespace_MyClass1_MyMethod(obj1, 0, 0, 0);

// NOTE - Reference arguments must be allocated using CDotNetAllocateMemory 

 strRef = CDotNetAllocateMemory(sizeof(char) * (strlen("abc") + 1)); 

 strcpy(strRef, "abc"); 

 MyNamespace_MyClass1_MyStringMethod(obj1, "xyz", &strOut, &strRef, &strReturnValue, 0); 

 // NOTE - Output, return value, and reference arguments that are strings, arrays, 

 // or object handles must be disposed after use 

 CDotNetFreeMemory(strOut); 

 CDotNetFreeMemory(strRef); 

 CDotNetFreeMemory(strReturnValue);

// NOTE - Reference arguments must be allocated using CDotNetAllocateMemory 

 arrayRefLength = 3; 

 arrayRef = CDotNetAllocateMemory(sizeof(char *) * 3); 

 arrayRef[0] = CDotNetAllocateMemory(sizeof(char) * 2); 

 strcpy(arrayRef[0], "X"); 

 arrayRef[1] = CDotNetAllocateMemory(sizeof(char) * 2); 

 strcpy(arrayRef[1], "Y"); 

 arrayRef[2] = CDotNetAllocateMemory(sizeof(char) * 2); 

 strcpy(arrayRef[2], "Z");

MyNamespace_MyClass1_MyArrayMethod(obj1,
 arrayIn, sizeof(arrayIn) / sizeof(arrayIn[0]),
 &arrayOut, &arrayOutLength,
 &arrayRef, &arrayRefLength,
 &arrayReturnValue, &arrayReturnValueLength, 0);

// Creating a .NET list containing strings 

 System_Collections_ArrayList__Create(&stringList, 0); 

 for (i = 0; i < arrayRefLength; ++i) 

 {

CDotNetHandle handle; 

 CDotNetConvertValueToHandle(arrayRef[i], CDOTNET_STRING, &handle); 

 System_Collections_ArrayList_Add(stringList, handle, 0, 0); 

 CDotNetDiscardHandle(handle);

}

// Iterating through a collection using IEnumerator (for-each) 

 System_Collections_ArrayList_GetEnumerator(stringList, &enumerator, 0); 

 System_Collections_IEnumerator_MoveNext(enumerator, &notEmpty, 0); 

 while (notEmpty) 

 {

CDotNetHandle handle; 

 char * str; 

 System_Collections_IEnumerator_Get_Current(enumerator, &handle, 0); 

 CDotNetConvertHandleToValue(handle, CDOTNET_STRING, &str); 

 printf("%s\n", str); 

 CDotNetFreeMemory(str); 

 CDotNetDiscardHandle(handle); 

 System_Collections_IEnumerator_MoveNext(enumerator, &notEmpty, 0);

} 

 CDotNetDiscardHandle(enumerator);

// Iterating through a collection using indexer 

 System_Collections_ArrayList_Get_Count(stringList, &nItems, 0); 

 for (i = 0; i < nItems; ++i) 

 {

CDotNetHandle handle; 

 char * str; 

 System_Collections_ArrayList_Get_Item(stringList, i, &handle, 0); 

 CDotNetConvertHandleToValue(handle, CDOTNET_STRING, &str); 

 printf("%s\n", str); 

 CDotNetFreeMemory(str); 

 CDotNetDiscardHandle(handle);

}

CDotNetDiscardHandle(stringList);

// NOTE - Output, return value, and reference arguments that are strings, arrays, 

 // or object handles must be disposed after use 

 CDotNetFreeMemory(arrayOut); 

 for (i = 0; i < arrayRefLength; ++i)

CDotNetFreeMemory(arrayRef[i]);

CDotNetFreeMemory(arrayRef); 

 CDotNetFreeMemory(arrayReturnValue);

MyNamespace_MyDerivedClass__Create(&objIn, 0); 

 MyNamespace_MyClass1_MyObjectMethod(obj1, objIn, &objOut, &objRef, &objReturnValue, 0); 

 CDotNetDiscardHandle(objIn); 

 // NOTE - Output, return value, and reference arguments that are strings, arrays, 

 // or object handles must be disposed after use 

 CDotNetDiscardHandle(objOut); 

 CDotNetDiscardHandle(objRef); 

 CDotNetDiscardHandle(objReturnValue);

MyNamespace_MyClass1_MyEnumMethod(obj1, MyNamespace_MyEnum1_MyValue1, 
 &enumOut, &enumRef, &enumReturnValue, 0); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Calling static method 

 MyNamespace_MyClass1_MyStaticMethod(0); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Instance properties 

 MyNamespace_MyClass1_Get_MyReadWriteProperty(obj1, &property, 0); 

 MyNamespace_MyClass1_Set_MyReadWriteProperty(obj1, 2, 0);

MyNamespace_MyClass1_Get_MyReadOnlyProperty(obj1, &property, 0); 

 MyNamespace_MyClass1_Set_MyWriteOnlyProperty(obj1, 3, 0); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Static property 

 MyNamespace_MyClass1_Set_MyStaticProperty(4, 0); 

 MyNamespace_MyClass1_Get_MyStaticProperty(&property, 0); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Instance field 

 MyNamespace_MyClass1__Get__MyField(obj1, &field, 0); 

 MyNamespace_MyClass1__Set__MyField(obj1, field + 1, 0); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Static field 

 MyNamespace_MyClass1__Set__MyStaticField(field, 0); 

 MyNamespace_MyClass1__Get__MyStaticField(&field, 0); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Creating structure 

 MyNamespace_MyStruct__Create(&structure, 0);

// Accessing structure fields 

 MyNamespace_MyStruct__Set__Field1(structure, 1, 0); 

 MyNamespace_MyStruct__Set__Field2(structure, 3.1415, 0); 

 MyNamespace_MyStruct__Set__Field3(structure, "hello", 0); 

 MyNamespace_MyStruct__Get__Field1(structure, &field, 0);

// NOTE - object handles must be discarded after use by calling CDotNetDiscardHandle 

 CDotNetDiscardHandle(structure); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Nested class 

 MyNamespace_MyClass1_MyNestedClass__Create(&obj3, 0); 

 CDotNetDiscardHandle(obj3); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Inheritance 

 MyNamespace_MyDerivedClass__Create(&derObj, 0); 

 MyNamespace_MyDerivedClass_BaseClassFunc(derObj, 0); 

 MyNamespace_MyDerivedClass_InterfaceFunc(derObj, 0); 

 // NOTE - can also call the wrapper functions in base class or interface 

 // with type cast to CDotNetHandle or the base class/interface type 

 MyNamespace_MyBaseClass_BaseClassFunc((CDotNetHandle)derObj, 0); 

 MyNamespace_MyInterface_InterfaceFunc((MyNamespace_MyInterface)derObj, 0); 

 CDotNetDiscardHandle(derObj); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // Calling generic method of non-generic class 

 intVal = 1; 

 MyNamespace_MyClass1_MyGenericMethod(obj1, "System.Int32", "System.String", &intVal, "Hi", &result, 0); 

 //-----------------------------------------------------------------------------

// NOTE - object handles must be discarded after use by calling CDotNetDiscardHandle 

 CDotNetDiscardHandle(obj1);

//----------------------------------------------------------------------------- 

 // Creating and using generic class 

 MyNamespace_MyGenericClass_T2__Create(&genObj, "System.Int32", "System.String", 0); 

 MyNamespace_MyGenericClass_T2_Set_Type1(genObj, &intVal, 0); 

 strRef = "Hi"; 

 MyNamespace_MyGenericClass_T2_Set_Type2(genObj, &strRef, 0); 

 MyNamespace_MyGenericClass_T2_Get_Type1(genObj, &intVal, 0); 

 MyNamespace_MyGenericClass_T2_Get_Type2(genObj, &strOut, 0); 

 CDotNetFreeMemory(strOut); 

 intVal = 2; 

 MyNamespace_MyGenericClass_T2_MyMethod(genObj, &intVal, &result, 0); 

 dblVal = 1.1; 

 MyNamespace_MyGenericClass_T2_MyGenericMethod(genObj, "System.Double", &dblVal, &strOut, 0); 

 CDotNetDiscardHandle(genObj); 

 //-----------------------------------------------------------------------------

//----------------------------------------------------------------------------- 

 // NOTE - must call the Close function to fully clean up the .NET controller 

 Close_MyAssembly(); 

 Close_mscorlib(); 

 //-----------------------------------------------------------------------------

}

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidst.htm language=enus -->
## TOPIC 00320: DST

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidst.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidst.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DST

*Advanced Analysis Library Only*

AnalysisLibErrType DST (double inputArray[], ssize_t numberOfElements, ssize_t numberOfElementsInDST, double outputArray[]);

#### Purpose

Computes the one-dimensional Discrete Sine Transform (DST) of a sequence **inputArray**, which is defined as follows:

[IMAGE alt='image' src='dstform_9.png']

and

[IMAGE alt='image' src='dstform_10.png']

| where | N is the length of inputArray |
| --- | --- |
|  | is the n-th element of inputArray |
|  | is the k-th element of outputArray |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | The input sequence. |
| numberOfElements | ssize_t | The number of elements in inputArray. |
| numberOfElementsInDST | ssize_t | The length of the DST to be performed. If numberOfElementsInDST is greater than numberOfElements, the function pads inputArray with zeros to make its number of elements equal numberOfElementsInDST. If numberOfElementsInDST is less than numberOfElements, inputArray is truncated. That is, only the leading numberOfElementsInDST elements in inputArray are used to perform the DST. If numberOfElementsInDST is less than or equal to zero, the function uses numberOfElements as numberOfElementsInDST. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | The DST of inputArray. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvidst2d.htm language=enus -->
## TOPIC 00321: DST2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvidst2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvidst2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DST2D

*Advanced Analysis Library Only*

AnalysisLibErrType DST2D (void *inputArray, ssize_t numberOfRows, ssize_t numberOfColumns, void *outputArray);

#### Purpose

Computes the two-dimensional Discrete Sine Transform (DST) of a matrix **inputArray**, which is defined as follows:

[IMAGE alt='image' src='dst2dform_11.png']

| where | M and N are the number of rows and the number of columns in inputArray respectively |
| --- | --- |
|  | x(m,n) is the element in inputArray with row number m and column number n |
|  | y(u,v) is the element in outputArray with row number u and column number v |

DST2D

1. Performs a one-dimensional DST row-by-row on input matrix inputArray .
2. Performs a one-dimensional DST column-by-column.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | void * | The two-dimensional input signal. |
| numberOfRows | ssize_t | The number of rows in inputArray. |
| numberOfColumns | ssize_t | The number of columns in inputArray. |
| Output |  |  |
| Name | Type | Description |
| outputArray | void * | The two-dimensional DST of inputArray. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvieigenvback.htm language=enus -->
## TOPIC 00322: EigenVBack

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvieigenvback.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvieigenvback.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EigenVBack

*Advanced Analysis Library Only*

AnalysisLibErrType EigenVBack (void *inputEigenvectors, ssize_t numberOfEigenvectors, int side, int method, ssize_t indexLow, ssize_t indexHigh, double scale[], void *outputEigenvectors);

#### Purpose

Transforms the eigenvectors of a balanced matrix to those of the original matrix. If you want more accurate eigenvectors, complete the following steps:

1. Balance the original matrix using MatrixBalance .
2. Call GenEigenValueVector to get the eigenvectors of the balanced matrix.
3. Call EigenVBack to back-transform the eigenvectors of the balanced matrix to the eigenvectors of the original matrix. Call CxEigenVBack if the eigenvectors are complex.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEigenvectors | void * | The eigenvectors of the balanced matrix. |
| numberOfEigenvectors | ssize_t | The order of inputEigenvectors. |
| side | int | Specifies whether inputEigenvectors contains right side eigenvectors or left side eigenvectors. side must be one of the following values: RIGHT_EIGEN (0) : Right side eigenvectorsLEFT_EIGEN (1): Left side eigenvectors |
| method | int | Specifies how the original matrix is balanced. Pass the same value for method that was passed to MatrixBalance when the original matrix was balanced. |
| indexLow | ssize_t | The permutation information from MatrixBalance. |
| indexHigh | ssize_t | The permutation information from MatrixBalance. |
| scale | double [] | The scale information from MatrixBalance. |
| Output |  |  |
| Name | Type | Description |
| outputEigenvectors | void * | The eigenvectors of the original matrix. If you call EigenVBack with outputEigenvectors = NULL or outputEigenvectors = inputEigenvectors, the back-transformed eigenvectors overwrite inputEigenvectors. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvielp_coef.htm language=enus -->
## TOPIC 00323: Elp_Coef

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvielp_coef.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvielp_coef.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Elp_Coef

*Advanced Analysis Library Only*

AnalysisLibErrType Elp_Coef (int type, int order, double samplingFrequency, double lowerCutoffFreq, double upperCutoffFreq, double r1, double r2, double aCoefficientArray[], int numberOfACoefficients, double bCoefficientArray[], int numberOfBCoefficients);

#### Purpose

Generates the set of filter coefficients to implement an IIR filter as
specified by the elliptic (or Cauer) filter model.
**aCoefficientArray** and **bCoefficientArray** are the reverse and forward filter coefficients. Use [IIRFiltering](../../cvi/libref/cviiirfiltering.htm) to achieve the actual filtering.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| type | int | Controls the filter type of the elliptic IIR filter coefficients. type has the following valid values: lowpass = 0 (default) highpass = 1 bandpass = 2 bandstop = 3 |
| order | int | Order of the IIR filter. Default Value: 3. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| lowerCutoffFreq | double | Lower cutoff frequency of the filter in Hertz. |
| upperCutoffFreq | double | Upper cutoff frequency of the filter in Hertz. |
| ripple_db | double | Amplitude of the stop band ripple in decibels. Default Value: 0.1 db. |
| stopBandAtten_db | double | Stop band attenuation, in decibels, of the IIR filter to design. Default Value: 60.0. |
| numberOfACoefficients | int | Number of coefficients in aCoefficientArray. numberACoefficients = order + 1 for low or highpass filters numberACoefficients = 2 × order + 1 for bandpass or bandstop filters |
| numberOfBCoefficients | int | Number of coefficients in bCoefficientArray. numberBCoefficients = order + 1 for low or highpass filters numberBCoefficients = 2 × order + 1 for bandpass or bandstop filters |
| Output |  |  |
| Name | Type | Description |
| aCoefficientArray | double [] | Array that contains the reverse coefficients of the designed IIR filter. |
| bCoefficientArray | double [] | Array that contains the forward coefficients of the designed IIR filter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequi_ripple.htm language=enus -->
## TOPIC 00324: Equi_Ripple

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequi_ripple.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequi_ripple.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Equi_Ripple

*Advanced Analysis Library Only*

AnalysisLibErrType Equi_Ripple (int numberOfBands, double a[], double weights[], double samplingFrequency, double cutoffs[], int filterType, int numberOfCoef, double coefficientArray[], double *delta);

#### Purpose

Designs a multiband FIR linear phase filter, a differentiator, or a Hilbert Transform using the Parks-McClellan algorithm. The resulting frequency response in each band has equal ripples that you can adjust by a weighting factor. Equi_Ripple generates only the filter coefficients; it does not actually perform data filtering.

The Parks-McClellan algorithm does not always generate a completely accurate filter. Always verify the filter design by applying it to a sample impulse response.

Although Equi_Ripple is the most flexible way to design an FIR linear phase filter, it has more complex parameters and requires some digital signal processing (DSP) knowledge. You might find it more convenient to use [EquiRpl_LPF](../../cvi/libref/cviequirpl_lpf.htm), [EquiRpl_HPF](../../cvi/libref/cviequirpl_hpf.htm), [EquiRpl_BPF](../../cvi/libref/cviequirpl_bpf.htm), and [EquiRpl_BSF](../../cvi/libref/cviequirpl_bsf.htm). These functions, which provide lowpass, highpass, bandpass, and bandstop FIR filters with equal weighting factors in all bands, are special cases of Equi_Ripple with simplified parameters.

##### Example Code

/* Design a 24-point lowpass filter and filter the incoming signal. */ 

double x[256], coef[24], y[280], fs, delta; 

double A[2]; /* array of frequency responses */ 

double wts[2]; /* array of weighting factors */ 

double cutoffs[4]; /* frequency points */ 

int n, m; 

int bands; /* number of bands */ 

int type; /* filter type */ 

bands = 2; /* one pass band and one stop band */ 

fs = 1000.0; /* sampling frequency */ 

A[0] = 1.0; /* 1 for the pass band */ 

A[1] = 0.0; /* 0 for the stop band */ 

wts[0] = 1.0; /* weighting factor for the pass band */ 

wts[1] = 1.0; /* weighting factor for the stop band */ 

cutoffs[0] = 0.0; 

cutoffs[1] = 300.0; /* the first stop band [0, 300.0] */ 

cutoffs[2] = 400.0; 

cutoffs[3] = 500.0; /* the pass band [400, 500] */ 

type = 1; /* multiple band filter */ 

n = 24; /* filter length */ 

m = 256; 

Equi_Ripple (bands, A, wts, fs, cutoffs, type, n, coef, &delta); 

Convolve (coef, n, x, m, y); /* Convolve the filter with the signal. */

##### Example Code

/* Design a 31-point bandpass filter and filter the incoming signal. */ 

double x[256], coef[55], y[287], fs, delta; 

double A[3]; /* array of frequency responses */ 

double wts[3]; /* array of weighting factors */ 

double cutoffs[6]; /* frequency points */ 

int n, m; 

int bands; /* number of bands */ 

int type; /* filter type */ 

bands = 3; /* one pass band and two stop bands */ 

fs = 1000.0; /* sampling frequency */ 

A[0] = 0.0; /* 0 for the first stop band */ 

A[1] = 1.0; /* 1 for the stop band */ 

A[2] = 0.0; /* 0 for second stop band */ 

wts[0] = 10.0; /* weighting factor for the first stop band */ 

wts[1] = 1.0; /* weighting factor for the pass band */ 

wts[2] = 4.0; /* weighting factor for the second stop band */ 

cutoffs[0] = 0.0; 

cutoffs[1] = 200.0; /* the first stop band [0, 200.0] */ 

cutoffs[2] = 250.0; 

cutoffs[3] = 350.0; /* the pass band [250, 350] */ 

cutoffs[4] = 400.0; 

cutoffs[5] = 500.0; /* the second stop band */ 

type = 1; /* multiple band filter */ 

n = 31; /* filter length */ 

m = 256; 

Equi_Ripple (bands, A, wts, fs, cutoffs, type, n, coef, &delta); 

Convolve (coef, n, x, m, y); /* Convolve the filter with the signal. */

##### Example Code

/* Design a 30-point differentiator. */ 

double coef[30], fs, delta; 

double A[1]; /* array of frequency responses */ 

double wts[1]; /* array of weighting factors */ 

double cutoffs[2]; /* frequency points */ 

int n; 

int bands; /* number of bands */ 

int type; /* filter type */ 

bands = 1; /* one pass band and one stop band */ 

fs = 1000.0; /* sampling frequency */ 

A[0] = 1.0; /* 1 for the band */ 

wts[0] = 1.0; /* weighting factor for the band */ 

cutoffs[0] = 0.0; 

cutoffs[1] = 500.0; /* the entire frequency range */ 

type = 2; /* differentiator */ 

n = 30; /* filter length */ 

Equi_Ripple (bands, A, wts, fs, cutoffs, type, n, coef, &delta);

##### Example Code

/* Design a 20-point Hilbert transform. */ 

double coef[20], fs, delta; 

double A[1]; /* array of frequency responses */ 

double wts[1]; /* array of weighting factors */ 

double cutoffs[2]; /* frequency points */ 

int n; 

int bands; /* number of bands */ 

int type; /* filter type */ 

bands = 1; /* one pass band and one stop band */ 

fs = 1000.0; /* sampling frequency */ 

A[0] = 1.0; /* 1 for the band */ 

wts[0] = 1.0; /* weighting factor for the band */ 

cutoffs[0] = 100.0; 

cutoffs[1] = 500.0; 

type = 3; /* Hilbert transform */ 

n = 20; /* filter length */ 

Equi_Ripple (bands, A, wts, fs, cutoffs, type, n, coef, &delta);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfBands | int | Number of bands in the filter. Default Value: 2. |
| a | double [] | Frequency response magnitude of each band. The values in the array must be between 0.0 and 1.0. A value of 0.0 indicates that the corresponding band is a stopband. A value of 1.0 indicates that the corresponding band is a passband. If filterType is multiband and the numberOfCoef is even, then AnumberOfBands – 1 must be 0. |
| weights | double [] | Weighting factor for each band. The weighting factor determines the relative damping of the generated ripple for the band. A higher value causes a smaller ripple to be generated for the band. Whether a value is high or low depends on its relation to the average of all the weights in the array. To achieve uniform ripple for all bands, set each element of the array to the same positive value, for example, 1.0. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| cutoffs | double [] | An array that specifies the frequency values of the lower and upper end points of each band. The array contains two entries for each band, as follows: Cutoffs[0] - First band, lower Cutoffs[1] - First band, upper Cutoffs[2] - Second band, lower Cutoffs[3] - Second band, upper If filterType is multiband or differentiator, cutoffs[0] must be 0. If filterType is Hilbert transform, then cutoffs[0] must not be 0. NI recommends that you use a value slightly greater than zero to define a transitional region. For all filter types, cutoffs[(2*NumberOfBands) – 1] must be samplingFreq/2. |
| filterType | int | Filter type. When filterType is 1, the function generates filter coefficients for a multiband filter. numberOfBands must be greater than or equal to two. When filterType is 2, the function generates filter coefficients for a differentiator. numberOfCoef must be even. When filterType is 3, the function generates filter coefficients for a Hilbert transform. numberOfCoef must be even. |
| numberOfCoef | int | Length of the window FIR filter. If filterType is Hilbert transform or differentiator, the value must be even. Valid Range: 8 to 511. |
| Output |  |  |
| Name | Type | Description |
| coefficientArray | double [] | Calculated output window FIR filter coefficients. |
| delta | double | Calculated normalized ripple size. To obtain the amplitude of a passband ripple in decibels, use the following formula: 20*log(1 + Delta/Weights[i]) To obtain the attenuation of a stopband in decibels, use the following formula: 20*log(Delta/Weights[i]) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_bpf.htm language=enus -->
## TOPIC 00325: EquiRpl_BPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_bpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_bpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_BPF

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_BPF (double samplingFrequency, double f1, double f2, double f3, double f4, int numberOfCoef, double coefficientArray[], double *delta);

#### Purpose

Designs an optimal bandpass FIR linear phase filter using the Parks-McClellan algorithm. EquiRpl_BPF is a simplified case of the [Equi_Ripple](../../cvi/libref/cviequi_ripple.htm) function. EquiRpl_BPF generates only the filter coefficients; it does not actually perform data filtering.

##### Example Code

/* Design a 51-point bandpass filter and filter the incoming signal. */ 

double x[256], coef[25], y[301], fs, f1, f2, f3, f4, delta; 

int n, m; 

fs = 1000.0; /* sampling frequency */ 

f1 = 200.0; /* the first stop band [0, 200] */ 

f2 = 250.0; 

f3 = 350.0; /* the pass band [250, 350] */ 

f4 = 400.0; /* the second stop band [400, 500] */ 

n = 51; /* filter length */ 

m = 256; 

EquiRpl_BPF (fs, f1, f2, f3, f4, n, coef, &delta); 

Convolve (coef, n, x, m, y); /* Convolve the filter with the signal. */

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the lower stop band. The lower stop band is [0, f1]. |
| f2 | double | Lowest frequency of the pass band. The pass band is [f2, f3]. |
| f3 | double | Highest frequency of the pass band. The pass band is [f2, f3]. |
| f4 | double | Lowest frequency of the upper stop band. The upper stop band is [f4, samplingFreq/2]. |
| numberOfCoef | int | length of the window FIR filter. Valid Range: 8 to 511. |
| Output |  |  |
| Name | Type | Description |
| coefficientArray | double [] | Calculated output window FIR filter coefficients. |
| delta | double | Calculated normalized absolute ripple size. To obtain the amplitude of the passband ripple in decibels, use the following formula: 20*log(1+Delta) To obtain the attenuation of the stopband in decibels, use the following formula: 20*log(Delta) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_bpfiltering.htm language=enus -->
## TOPIC 00326: EquiRpl_BPFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_bpfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_bpfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_BPFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_BPFiltering (double inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double f1, double f2, double f3, double f4, double outputArray[]);

#### Purpose

Filter the real array using a optimal bandpass FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 51-point bandpass FIR filter and filter the real incoming signal. */ 

 double x[256], y[306]; 

 double fs, f1, f2, f3, f4; 

 int n, ncoef; 

 
 fs = 1000.0; // sampling frequency 

 f1 = 200.0; // first stop band [0, 200] 

 f2 = 250.0; // pass band [250, 350] 

 f3 = 350.0; 

 f4 = 400.0; // second stop band [400, fs/2] 

 n = 256; // input signal length 

 ncoef = 51; //filter length 

 WhiteNoise (n, 1, 17, x); 
 
 
 
 EquiRpl_BPFiltering(x, n, ncoef, fs, f1, f2, f3, f4, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the lower stop band. The lower stop band is [0, f1]. |
| f2 | double | Lowest frequency of the pass band. The pass band is [f2, f3]. |
| highestPassFreq | double | Highest frequency of the pass band. The pass band is [f2, f3]. |
| lowestStopFreq | double | Lowest frequency of the upper stop band. The upper stop band is [f4, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Filtered data. This array must be at least (n + ncoef - 1) elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_bsf.htm language=enus -->
## TOPIC 00327: EquiRpl_BSF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_bsf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_bsf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_BSF

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_BSF (double samplingFrequency, double f1, double f2, double f3, double f4, int numberOfCoef, double coefficientArray[], double *delta);

#### Purpose

Designs a bandstop FIR linear phase filter using the Parks-McClellan algorithm. EquiRpl_BSF is a simplified case of the [Equi_Ripple](../../cvi/libref/cviequi_ripple.htm) function. EquiRpl_BSF generates only the filter coefficients; it does not actually perform data filtering.

##### Example Code

/* Design a 51-point bandstop filter and filter the incoming signal. */ 

double x[256], coef[25], y[301], fs, f1, f2, f3, f4, delta; 

int n, m; 

fs = 1000.0; /* sampling frequency */ 

f1 = 200.0; /* the first pass band [0, 200] */ 

f2 = 250.0; 

f3 = 350.0; /* the stop band [250, 350] */ 

f4 = 400.0; /* the second pass band [400, 500] */ 

n = 51; /* filter length */ 

m = 256; 

EquiRpl_BSF (fs, f1, f2, f3, f4, n, coef, &delta); 

Convolve (coef, n, x, m, y); /* Convolve the filter with the signal. */

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the lower pass band. The lower pass band is [0, f1]. |
| f2 | double | Lowest frequency of the stop band. The stop band is [f2, f3]. |
| f3 | double | Highest frequency of the stop band. The stop band is [f2, f3]. |
| f4 | double | Lowest frequency of the upper pass band. The upper pass band is [f4, samplingFreq/2]. |
| numberOfCoef | int | Length of the window FIR filter. Valid Range: 8 to 511. |
| Output |  |  |
| Name | Type | Description |
| coefficientArray | double [] | Calculated output window FIR filter coefficients. |
| delta | double | Calculated normalized absolute ripple size. To obtain the amplitude of the passband ripple in decibels, use the following formula: 20*log(1+Delta) To obtain the attenuation of the stopband in decibels, use the following formula: 20*log(Delta) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_bsfiltering.htm language=enus -->
## TOPIC 00328: EquiRpl_BSFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_bsfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_bsfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_BSFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_BSFiltering (double inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double f1, double f2, double f3, double f4, double outputArray[]);

#### Purpose

Filter the real array using a optimal bandstop FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 51-point bandstop FIR filter and filter the real incoming signal. */ 

 double x[256], y[306]; 

 double fs, f1, f2, f3, f4; 

 int n, ncoef; 
 

 
 fs = 1000.0; // sampling frequency 

 f1 = 200.0; // first pass band [0, 200] 

 f2 = 250.0; // stop band [250, 350] 

 f3 = 350.0; 
 
 f4 = 400.0; // second pass band [400, fs/2] 

 n = 256; // input signal length 

 ncoef = 51; //filter length 

 WhiteNoise (n, 1, 17, x); 
 
 
 
 EquiRpl_BSFiltering(x, n, ncoef, fs, f1, f2, f3, f4, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. The algorithm introduces a large error when designing a bandstop filter for an even number of ncoef. To avoid this error, the EquiRpl_BSFiltering adjusts the ncoef to the next higher odd value if ncoef is even. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the lower pass band. The lower pass band is [0, f1]. |
| f2 | double | Lowest frequency of the stop band. The stop band is [f2, f3]. |
| highestStopFreq | double | Highest frequency of the stop band. The stop band is [f2, f3]. |
| lowestPassFreq | double | Lowest frequency of the upper pass band. The upper pass band is [f4, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Filtered data. This array must be at least (n + ncoef - 1) elements long when ncoef is odd. This array must be at least (n + ncoef) elements long when ncoef is even. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_hpf.htm language=enus -->
## TOPIC 00329: EquiRpl_HPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_hpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_hpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_HPF

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_HPF (double samplingFrequency, double f1, double f2, int numberOfCoef, double coefficientArray[], double *delta);

#### Purpose

Designs an optimal highpass FIR linear phase filter using the Parks-McClellan algorithm. EquiRpl_HPF is a simplified case of the [Equi_Ripple](../../cvi/libref/cviequi_ripple.htm) function. EquiRpl_HPF generates only the filter coefficients; it does not actually perform data filtering.

##### Example Code

/* Design a 25-point highpass filter and filter the incoming signal. */ 

double x[256], coef[25], y[281], fs, f1, f2, delta; 

int n, m; 

fs = 1000.0; /* sampling frequency */ 

f1 = 300.0; /* the stop band [0, 300] */ 

f2 = 400.0; /* the pass band [400, 500] */ 

n = 25; /* filter length */ 

m = 256; 

EquiRpl_HPF (fs, f1, f2, n, coef, &delta); 

Convolve (coef, n, x, m, y); /* Convolve the filter with the signal. */

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the stop band. The stop band is [0, f1]. |
| f2 | double | Lowest frequency of the pass band. The pass band is [f2, samplingFreq/2]. |
| numberOfCoef | int | Length of the window FIR filter. Valid Range: 8 to 511. |
| Output |  |  |
| Name | Type | Description |
| coefficientArray | double [] | Calculated output window FIR filter coefficients. |
| delta | double | Calculated normalized absolute ripple size. To obtain the amplitude of the passband ripple in decibels, use the following formula: 20*log(1+Delta) To obtain the attenuation of the stopband in decibels, use the following formula: 20*log(Delta) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_hpfiltering.htm language=enus -->
## TOPIC 00330: EquiRpl_HPFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_hpfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_hpfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_HPFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_HPFiltering (double inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double f1, double f2, double outputArray[]);

#### Purpose

Filter the real array using a optimal highpass FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 25-point highpass FIR filter and filter the real incoming signal. */ 

 double x[256], y[280]; 

 double fs, f1, f2; 

 int n, ncoef; 
 

 
 fs = 1000.0; // sampling frequency 

 f1 = 300.0; // stop band [0, 300] 

 f2 = 400.0; // pass band [400, fs/2] 

 n = 256; // input signal length 

 ncoef = 25; //filter length 

 WhiteNoise (n, 1, 17, x); 
 

 
 EquiRpl_HPFiltering(x, n, ncoef, fs, f1, f2, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. The algorithm introduces a large error when designing a highpass filter for an even number of ncoef. To avoid this error, the EquiRpl_HPFiltering adjusts the ncoef to the next higher odd value if ncoef is even. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the stop band. The stop band is [0, f1]. |
| f2 | double | Lowest frequency of the pass band. The pass band is [f2, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Filtered data. This array must be at least (n + ncoef - 1) elements long when ncoef is odd. This array must be at least (n + ncoef) elements long when ncoef is even. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_lpf.htm language=enus -->
## TOPIC 00331: EquiRpl_LPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_lpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_lpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_LPF

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_LPF (double samplingFrequency, double f1, double f2, int numberOfCoef, double coefficientArray[], double *delta);

#### Purpose

Designs an optimal lowpass FIR linear phase filter using the Parks-McClellan algorithm. EquiRpl_LPF is a simplified case of [Equi_Ripple](../../cvi/libref/cviequi_ripple.htm) function. EquiRpl_LPF generates only the filter coefficients; it does not actually perform data filtering.

##### Example Code

/* Design a 25-point lowpass filter and filter the incoming signal. */ 

double x[256], coef[25], y[281], fs, f1, f2, delta; 

int n, m; 

fs = 1000.0; /* sampling frequency */ 

f1 = 300.0; /* the pass band [0, 300] */ 

f2 = 400.0; /* the stop band [400, 500] */ 

n = 25; /* filter length */ 

m = 256; 

EquiRpl_LPF (fs, f1, f2, n, coef, &delta); 

Convolve (coef, n, x, m, y); /* Convolve the filter with the signal. */

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| samplingFrequency | double | Sampling frequency in Hertz. |
| f1 | double | Highest frequency of the pass band. The pass band is [0, f1]. |
| f2 | double | Lowest frequency of the stop band. The stop band is [f2, samplingFreq/2]. |
| numberOfCoef | int | Length of the window FIR filter. Valid Range: 8 to 511. |
| Output |  |  |
| Name | Type | Description |
| coefficientArray | double [] | Calculated output window FIR filter coefficients. |
| delta | double | Calculated normalized absolute ripple size. To obtain the amplitude of the passband ripple in decibels, use the following formula: 20*log(1+Delta) To obtain the attenuation of the stopband in decibels, use the following formula: 20*log(Delta) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviequirpl_lpfiltering.htm language=enus -->
## TOPIC 00332: EquiRpl_LPFiltering

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviequirpl_lpfiltering.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviequirpl_lpfiltering.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EquiRpl_LPFiltering

*Advanced Analysis Library Only*

AnalysisLibErrType EquiRpl_LPFiltering (double inputArray[], ssize_t numberOfElements, int numberOfCoeffs, double samplingFrequency, double passBand, double stopBand, double outputArray[]);

#### Purpose

Filter the real array using a optimal lowpass FIR linear phase filter with equi-ripple characteristics.

##### Example Code

/* Design a 25-point lowpass FIR filter and filter the real incoming signal. */ 

 double x[256], y[280]; 

 double fs, f1, f2; 

 int n, ncoef; 
 

 
 fs = 1000.0; // sampling frequency 

 f1 = 300.0; // pass band [0, 300] 

 f2 = 400.0; // stop band [400, fs/2] 

 n = 256; // input signal length 

 ncoef = 25; //filter length 

 WhiteNoise (n, 1, 17, x); 
 

 
 EquiRpl_LPFiltering(x, n, ncoef, fs, f1, f2, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Array containing the raw data to filter. |
| numberOfElements | ssize_t | Number of elements in the input array inputArray. |
| numberOfCoeffs | int | Length of the FIR filter. numberOfCoeffs must be greater than 2. |
| samplingFrequency | double | Sampling frequency in Hertz. |
| passBand | double | Highest frequency of the pass band. The pass band is [0, f1]. |
| stopBand | double | Lowest frequency of the stop band. The stop band is [f2, samplingFreq/2]. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Filtered data. This array must be at least (n + ncoef - 1) elements long. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifdopen.htm language=enus -->
## TOPIC 00333: fdopen

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifdopen.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifdopen.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### fdopen

FILE *fdopen (int fileHandle, const char mode[]);

#### Purpose

Obtains a pointer to a buffered I/O stream from a file handle returned by one of the following functions:

- open —Low-level I/O
- sopen —Low-level I/O (Windows only)

The returned value can be used as if it had been returned by
 [fopen](../../cvi/libref/cvifopen.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileHandle | int | A file handle returned by one of the following functions: OpenFile—Formatting and I/O library open—Low-level I/O sopen—Low-level I/O (Windows only) |
| mode | const char [] | Specifies the mode of reading and writing desired for the opened file. The possible modes are listed in the following chart. Note You should use a mode that is consistent with the mode in which you originally opened the file. If you use write capabilities not enabled when the file handle was originally opened, the call to fdopen succeeds, but any attempt to write fails. For instance, if you originally opened the file for reading only, you can pass "rw" to fdopen, but any call to fwrite fails. Modeargument Description r Open text file for reading. w Truncate to zero length or create text file for writing. a Append; open or create text file for writing at end-of-file. rb Open binary file for reading. wb Truncate to zero length or create binary file for writing. ab Append; open or create binary file for writing at end-of-file. r+ Open text file for reading and writing. w+ Truncate to zero length or create text file for reading and writing. a+ Append; open or create text file for reading and appending. rb+ Open binary file for reading and writing. wb+ Truncate to zero length or create binary file for reading and writing. ab+ Append; open or create binary file for reading and appending. |
|  | Note You should use a mode that is consistent with the mode in which you originally opened the file. If you use write capabilities not enabled when the file handle was originally opened, the call to fdopen succeeds, but any attempt to write fails. For instance, if you originally opened the file for reading only, you can pass "rw" to fdopen, but any call to fwrite fails. |  |
| Modeargument | Description |  |
| r | Open text file for reading. |  |
| w | Truncate to zero length or create text file for writing. |  |
| a | Append; open or create text file for writing at end-of-file. |  |
| rb | Open binary file for reading. |  |
| wb | Truncate to zero length or create binary file for writing. |  |
| ab | Append; open or create binary file for writing at end-of-file. |  |
| r+ | Open text file for reading and writing. |  |
| w+ | Truncate to zero length or create text file for reading and writing. |  |
| a+ | Append; open or create text file for reading and appending. |  |
| rb+ | Open binary file for reading and writing. |  |
| wb+ | Truncate to zero length or create binary file for reading and writing. |  |
| ab+ | Append; open or create binary file for reading and appending. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| stream | FILE * | Contains a pointer to the I/O stream associated with the openedfile if successful. If the open operation fails, fdopen returns NULL and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifflush.htm language=enus -->
## TOPIC 00334: fflush

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifflush.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifflush.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### fflush

int fflush (FILE *stream);

#### Purpose

Flushes the I/O buffer of the specified stream. If the
specified stream is open for output (write or append) or if it is open
for update (read/write or read/append) and the most recent I/O operation
was not an input operation, then this function writes any unwritten data
to that stream. If the specified stream is open for input
(read), this function clears the buffer contents of the stream.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Specifies the I/O stream that will have its buffer contents flushed. A flush occurs only if this stream is open for output or update (read/write or read/append), and the most recent operation is not an input operation. If the specified stream is open for input (read), this function clears the buffer contents of the stream. Note Entering NULL in this parameter flushes all output buffers. |
|  | Note Entering NULL in this parameter flushes all output buffers. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Contains the returned status of the function. On success, fflush returns 0. If an error occurs, fflush returns EOF and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifft.htm language=enus -->
## TOPIC 00335: FFT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifft.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifft.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FFT

*Advanced Analysis Library Only*

AnalysisLibErrType FFT (double arrayXReal[], double arrayXImaginary[], ssize_t numberOfElements);

#### Purpose

|  | Note This function has been superseded by CxFFTEx. CxFFTEx includes additional parameters, which makes it more versatile than FFT. |
| --- | --- |

Calculates the Fast Fourier Transform (FFT) of the complex data.

Let X = x + jy be the complex array:

Y = FFT(X)

FFT can perform the operation in place and overwrite the input arrays.

##### Example Code

/* Generate two arrays with random numbers and calculate the Fast Fourier Transform. */ 

double x[256], y[256]; 

n; 

n = 256; 

Uniform (n, 17, x); 

Uniform (n, 17, y); 

FFT (x, y, n);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements in the input arrays. |
| Output |  |  |
| Name | Type | Description |
| arrayX_Real | double [] | On input, the real part of complex array used to compute the FFT. On output, the real part of the FFT. This operation is performed in place, meaning the values in this array are overwritten. |
| arrayX_Imaginary | double [] | On input, the imaginary part of complex array used to compute the FFT. On output, the imaginary part of the FFT. This operation is performed in place, meaning the values in this array are overwritten. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

#### Examples

Refer to the following examples that use the FFT function:

- analysis\2dfft.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- analysis\parsevls.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- OpenMP\2dfft_omp.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifft2d.htm language=enus -->
## TOPIC 00336: FFT2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifft2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifft2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FFT2D

*Advanced Analysis Library Only*

AnalysisLibErrType FFT2D (void *timeDomainSignal, ssize_t numberOfRows, ssize_t numberOfColumns, ssize_t numberOfRowsForFFT, ssize_t numberOfColumnsForFFT, int shift, void *fft);

#### Purpose

Computes the Fast Fourier Transform (FFT) of a 2D time-domain signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| timeDomainSignal | void * | The real time-domain signal. |
| numberOfRows | ssize_t | The number of rows in timeDomainSignal. |
| numberOfColumns | ssize_t | The number of columns in timeDomainSignal. |
| numberOfRowsForFFT | ssize_t | The number of rows on which to perform the FFT. If numberOfRowsForFFT does not equal numberOfRows, this function truncates timeDomainSignal or pads timeDomainSignal with zeros to create a numberOfRowsForFFT by numberOfColumnsForFFT matrix for which it calculates the FFT. If numberOfRowsForFFT is less than 1, this function uses numberOfRows for this parameter. |
| numberOfColumnsForFFT | ssize_t | The number of columns on which to perform the FFT. If numberOfColumnsForFFT does not equal numberOfColumns, this function truncates timeDomainSignal or pads timeDomainSignal with zeros to create a numberOfRowsForFFT by numberOfColumnsForFFT matrix for which it calculates the FFT. If numberOfColumnsForFFT is less than 1, this function uses numberOfColumns for this parameter. |
| shift | int | Specifies whether to shift the DC component to the center of the FFT result. shift must be one of the following values: FALSE (0): Ordinary FFT. The first element of fft is the DC component.TRUE (1): DC-centered FFT. |
| Output |  |  |
| Name | Type | Description |
| FFT | void * | The FFT of the time-domain signal. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifftex.htm language=enus -->
## TOPIC 00337: FFTEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifftex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifftex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FFTEx

*Advanced Analysis Library Only*

AnalysisLibErrType FFTEx (double timeDomainSignal[], ssize_t numberOfElements, ssize_t numberOfElementsForFFT, PFFTTable fftTable, int shift, NIComplexNumber fft[]);

#### Purpose

Computes the Fast Fourier Transform (FFT) of a real time-domain signal. National Instruments recommends that you use this function instead of [ReFFT](../../cvi/libref/cvirefft.htm). FFTEx includes additional parameters, which makes it more versatile than ReFFT. For example, you can specify the number of elements for the FFT, which can be less or greater than the number of elements in the time-domain signal. You also can use FFTEx with a reusable FFT table, which can speed up computation. 

 

 If you want to perform the same size FFT repeatedly, you can use [CreateFFTTable](../../cvi/libref/cvicreateffttable.htm) to create an FFT table and then pass this table to FFTEx. If you pass NULL for **fftTable**, FFTEx creates the table internally and frees the table on exit. 

 

 The following code is the pseudocode for calling FFT routines:

```text
            N=1024; //Set length of signal
            tbl=CreateFFTTable(N);  //Create N-point table
            for(;;){
                Acquire_N_Point_Signal(signal); //Acquire N points
                FFT(signal,..., tbl,...);       //Perform FFT
            }
            DestroyFFTTable(tbl);       //End, release FFT table resources
```

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| timeDomainSignal | double [] | The real time-domain signal. |
| numberOfElements | ssize_t | The number of elements in timeDomainSignal. |
| numberOfElementsForFFT | ssize_t | The desired FFT size. If numberOfElementsForFFT is greater than numberOfElements, this function pads timeDomainSignal with trailing zeros to get a time-domain signal that has numberOfElementsForFFT elements. If numberOfElementsForFFT is smaller than numberOfElements, this function truncates timeDomainSignal. If numberOfElementsForFFT is less than 1, this function uses numberOfElements for this parameter. |
| FFTTable | PFFTTable | The FFT table created using CreateFFTTable. You can pass NULL for this parameter if you do not have a reusable FFT table. |
| shift | int | Specifies whether to shift the DC component to the center of the FFT result. shift must be one of the following values: FALSE (0): Ordinary FFT. The first element of fft is the DC component.TRUE (1): DC-centered FFT. The first element of fft is the -PI frequency element. The floor(numberOfElementsForFFT / 2)-th element of fft is the DC component. |
| Output |  |  |
| Name | Type | Description |
| FFT | NIComplexNumber [] | The FFT of the time-domain signal. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

#### Example

Refer to analysis\narrowbandfilter.cws for an example of using the FFTEx function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviflushoutq.htm language=enus -->
## TOPIC 00338: FlushOutQ

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviflushoutq.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviflushoutq.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FlushOutQ

int FlushOutQ (int portNumber);

#### Purpose

Removes all characters from the output queue of the specified port.

FlushOutQ returns an error if you have not opened the port or if you pass an invalid value for **portNumber**.

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

Refer to the following examples that use the FlushOutQ function:

- rs232\commcallback.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- rs232\serial.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviforwsub.htm language=enus -->
## TOPIC 00339: ForwSub

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviforwsub.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviforwsub.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ForwSub

*Advanced Analysis Library Only*

AnalysisLibErrType ForwSub (void *inputMatrixA, double knownVectory[], ssize_t arraySizes, double outputVectorx[], ssize_t permutationVector[]);

#### Purpose

Solves linear equations AX=Y using forward substitution. ForwSub assumes that A is an LU-decomposed lower triangular matrix. ForwSub obtains X using the following formulas:

x<sub>0</sub> = y<sub>0</sub>

[IMAGE alt='image' src='forwsub.gif'] for **i** = 1, 2, . . ., **arraySizes** – 1

ForwSub can perform the operation in place; that is, the input and output arrays can be the same.

##### Example Code

/* to solve a linear equation A*x = y */ 

double A[10][10], x[10], y[10]; 

int p[10]; /* permutation vector */ 

int sign, n; 

n = 10; 

LU (A, n, p, &sign); /* LU decomposition of A */ 

ForwSub (A, y, n, x, p); /* forward substitution */ 

BackSub (A, x, n, x); /* backward substitution */

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix_A | void * | The lower triangular matrix from LU decomposition. This matrix must be an array of doubles. |
| knownVector_y | double [] | Array that represents the set of known vector coefficients. |
| arraySizes | ssize_t | The number of rows and columns in the square input matrix and the number of elements in the known vector array. |
| permutationVector | ssize_t [] | The permutation vector obtained from the LU decomposition. This vector has the row exchange information. If there was no row exchange in LU, pi = i. |
| Output |  |  |
| Name | Type | Description |
| outputVector_x | double [] | The solution vector. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifscanf.htm language=enus -->
## TOPIC 00340: fscanf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifscanf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifscanf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### fscanf

int fscanf (FILE *stream, const char formatString[], ...);

#### Purpose

Reads input from the specified stream and converts it into a series of
values according to the specifications of the formatting string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Contains a pointer to the stream from which data is scanned. |
| formatString | const char [] | Contains the format string that specifies the admissible input sequences and how they are converted for assignment. Use standard ANSI C format specifiers. If insufficient arguments exist for the format, the behavior is undefined. If the format is exhausted while arguments remain, the excess arguments are evaluated but are otherwise ignored. Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |
|  | Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |  |
| Output |  |  |
| Name | Type | Description |
| target_s | ... | Contains a pointer to the object that receives the converted input from the specified stream. If there are multiple arguments, separate the arguments by commas. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| ItemsFormatted | int | Contains the number of parameters successfully matched and formatted or EOF (-1) in case of an invalid input. This value might be less than the number of parameters you pass in for matching in the following cases: The input or the format string contains fewer elements than parameters passed in. The function could not match one of the parameters. If an error occurs, this function sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifseek.htm language=enus -->
## TOPIC 00341: fseek

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifseek.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifseek.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### fseek

int fseek (FILE *stream, long offset, int origin);

#### Purpose

Sets the file position indicator for the specified stream. The value specified by **offset** is added to the position designated by **origin**. A successful call to this function clears the end-of-file indicator for the stream and undoes any effects of
[ungetc](../../cvi/libref/cviungetc.htm) on the same stream. After a call to this function, the next operation on an update stream (read/write or read/append) may be either input or output.

|  | Note This function is similar to fsetpos; however, fsetpos is more useful for huge files (over 2 billion bytes). |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Contains a pointer to the stream that has its associated file position indicator set. |
| offset | long | Contains the number of bytes beyond the designated origin to set the file position indicator. For binary files, this value is measured in characters and is added to the specified origin. For text files, one of the following must be true: offset must be zero. offset is the value returned by a previous call to ftell and origin is set to beginning-of-file. |
| origin | int | Contains the origin to which the specified offset is added in computing the new file position. The following describes the available selections: Origin Value Description Beginning SEEK_SET (0) Begin seek from beginning of file Current SEEK_CUR (1) Begin seek from the current value of file position indicator End SEEK_END (2) Begin seek from end of file |
| Origin | Value | Description |
| Beginning | SEEK_SET (0) | Begin seek from beginning of file |
| Current | SEEK_CUR (1) | Begin seek from the current value of file position indicator |
| End | SEEK_END (2) | Begin seek from end of file |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Contains the returned status of the function. If successful, fseek returns 0. If an error occurs, fseek returns a nonzero value and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifsetpos.htm language=enus -->
## TOPIC 00342: fsetpos

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifsetpos.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifsetpos.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### fsetpos

int fsetpos (FILE *stream, const fpos_t *newFilePosition);

#### Purpose

Sets the file position indicator for the specified stream according to the value obtained from an earlier call to [fgetpos](../../cvi/libref/cvifgetpos.htm). If successful, the end-of-file indicator for the stream is cleared and any effects of [ungetc](../../cvi/libref/cviungetc.htm) are undone. On streams open for update, this function allows for a switch between reading and writing.

|  | Note This function is similar to fseek but is more useful for files that contain more than 2 billion bytes. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Contains a pointer to the stream that has its associated file position indicator set. |
| newFilePosition | const fpos_t * | Contains a value obtained from an earlier call to fgetpos. The file position indicator for the specified stream is set according to this value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Contains the resulting status of the function. If successful, fsetpos returns 0. If an error occurs, fsetpos returns a nonzero value and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviftell.htm language=enus -->
## TOPIC 00343: ftell

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviftell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviftell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ftell

long ftell (FILE *stream);

#### Purpose

Returns the current value of the file position indicator
for the specified stream. For binary streams, the value is the
number of characters from the beginning of the file. For a text stream, the value is not necessarily a meaningful measure, but can be used by [fseek](../../cvi/libref/cvifseek.htm) to restore the file position indicator to the current position.

|  | Note This function is similar to fgetpos; however, fgetpos is more useful for huge files (over 2 billion bytes). |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Contains a pointer to the stream from which the file position indicator is returned. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentFilePosition | long | Contains the resulting value of the current file position indicator for the specified stream. If the operation fails, ftell returns -1 and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvifwrite.htm language=enus -->
## TOPIC 00344: fwrite

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvifwrite.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvifwrite.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### fwrite

size_t fwrite (const void *buffer, size_t elementSize, size_t numberOfElements, FILE *stream);

#### Purpose

Writes a block of data to the specified output stream.
The data to be written is stored in the specified buffer and the number
of elements successfully written is returned. The function advances the file position indicator by the number of characters successfully written.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| buffer | const void * | Contains a pointer to the data block written to the specified output stream. |
| elementSize | size_t | Specifies the size in bytes of the elements to be written. |
| numberOfElements | size_t | Specifies the number of elements to be written. If a write error is encountered, the number of elements actually written can be less than the number specified by this parameter. |
| stream | FILE * | Specifies the output stream to which data will be written. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| elementsWritten | size_t | Contains the number of elements successfully written. If a write error is encountered, the returned value can be less than that specified in the number_ofElements parameter. If an error occurs, fwrite sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigammac.htm language=enus -->
## TOPIC 00345: GammaC

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigammac.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigammac.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GammaC

*Advanced Analysis Library Only*

double GammaC (double x, double a);

#### Purpose

Computes the complementary regularized gamma function, which is defined as follows:

[IMAGE alt='image' src='gammacform_18.png']

The following equation relates the complement of the regularized gamma function to the regularized gamma function:

[IMAGE alt='image' src='gammacform_19.png']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | The point at which the function is evaluated. |
| a | double | The upper limit of the complementary regularized gamma function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | The value of the evaluated complementary regularized gamma function. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigaussnoise.htm language=enus -->
## TOPIC 00346: GaussNoise

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigaussnoise.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigaussnoise.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GaussNoise

*Advanced Analysis Library Only*

AnalysisLibErrType GaussNoise (ssize_t numberOfElements, double standardDeviation, int seed, double gaussianNoise[]);

#### Purpose

Generates an array of random Gaussian numbers distributed with expected zero mean value and the standard deviation you specify.

When **seed** ≥ 0, GaussNoise generates a new random sequence using the seed value.

When **seed** < 0, the previously generated random sequence continues.

##### Example Code

/* The following code generates an array of random Gaussian distributed numbers. */ 

double x[20], sDev; 

int n; 

n = 20; 

sDev = 5.0; 

GaussNoise (n, sDev, 17, x);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements to generate in the Gaussian noise pattern. |
| standardDeviation | double | Standard deviation of the Gaussian noise pattern. Default Value: 1.0. |
| seed | int | The seed value used to generate the random number. When seed ≥ 0, GaussNoise generates a new random sequence using the seed value. When seed < 0, the previously generated random sequence continues. |
| Output |  |  |
| Name | Type | Description |
| gaussianNoise | double [] | Generated Gaussian noise pattern. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

#### Examples

Refer to the following examples that use the GaussNoise function:

- analysis\convolve.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- analysis\correlat.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- analysis\nonlnfit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\sigproc\sigproc.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigausswin.htm language=enus -->
## TOPIC 00347: GaussWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigausswin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigausswin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GaussWin

*Advanced Analysis Library Only*

AnalysisLibErrType GaussWin (double arrayX[], ssize_t numberOfElements, double standardDeviation);

#### Purpose

Applies a Gaussian window to a real signal. If y represents the output sequence **arrayX**, GaussWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='gausswinform_10.png']

where n is the number of elements in **arrayX** and σ is the standard deviation of the Gaussian window. 

 

 This function applies an unsymmetric Gaussian window on the input signal. If you want to use a symmetric Gaussian window, call [SymWin](../../cvi/libref/cvisymwin.htm) instead. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in arrayX. |
| standardDeviation | double | The standard deviation of the Gaussian window normalized to the length of arrayX. The default value is 0.2. If standardDeviation <= 0, the default value is used. |
| Output |  |  |
| Name | Type | Description |
| arrayX | double [] | On input, the input signal. On output, this parameter returns the input signal with a Gaussian window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigenlsfit.htm language=enus -->
## TOPIC 00348: GenLSFit

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigenlsfit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigenlsfit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GenLSFit

*Advanced Analysis Library Only*

AnalysisLibErrType GenLSFit (void *hMatrix, ssize_t numberOfRows, ssize_t numberOfColumns, double yArray[], double standardDeviation[], int algorithm, double zArray[], double coefficientArray[], void *covariance, double *meanSquaredError);

#### Purpose

Finds the best fit **k**-dimensional plane and the set of linear coefficients using the least chi-squares method for observation data sets.

[IMAGE alt='image' src='genlsfitform_8.png']

| where | i = 0, 1, . . ., n – 1 |
| --- | --- |
|  | n = the number of your observation data sets |

You can use GenLSFit to solve multiple linear regression problems and to solve for the linear coefficients in a multiple-function equation.

The general least squares linear fit problem can be described as follows. Given a set of observation data, find a set of coefficients that fit the linear model:

[IMAGE alt='image' src='genlsfitform_9.png']

**[Equation 1]**

| where | b is the set of coefficients |
| --- | --- |
|  | n is the number of elements in YArray and the number of rows of HMatrix |
|  | k is the number of elements in coefficientArray |
|  | xij is the observation data, which HMatrix contains |

[IMAGE alt='image' src='genlsmatrix.gif']

You can write [Equation 1](#equation1) as Y = HB.

The previous discussion leads to a multiple linear regression model, which uses several variables:

x<sub>i0</sub>, x<sub>i1</sub>, ..., x<sub>ik – 1</sub>

to predict one variable y<sub>i</sub>. In contrast, [LinearFitEx](../../cvi/libref/cvilinearfitex.htm), [ExpFitEx](../../cvi/libref/cviexpfitex.htm), and [PolyFitEx](../../cvi/libref/cvipolyfitex.htm) are all based on a single predictor variable, which uses one variable to predict another variable.

In most cases, we have more observation data than coefficients. The formulas in [Equation 1](#equation1) might not produce the solution. The fit problem becomes to find the coefficients **B** that minimize the difference between the observed data, y<sub>i</sub>, and the predicted value:

[IMAGE alt='image' src='genlsa.gif']

GenLSFit uses the least chi-squares plane method to obtain the coefficients in [Equation 1](#equation1), that is, finding the solution, **B**, which minimizes the following quantity:

[IMAGE alt='image' src='genlseq3.gif']

**[Equation 2]**

where [IMAGE alt='image' src='genlsc.gif']

In the previous equation, σ<sub>i</sub> is the standard deviation, **stdDeviation**. If the measurement errors are independent and normally distributed with constant standard deviation σ<sub>i</sub> = σ, the previous equation is also the least squares estimation.

There are different ways to minimize χ<sup>2</sup>. One way to minimize χ<sup>2</sup> is to set the partial derivatives of χ<sup>2</sup> to zero with respect to b<sub>0</sub>, b<sub>1</sub>, ..., b<sub>k – 1</sub>:

[IMAGE alt='image' src='genlsd.gif']

The previous equations can be written as 
 

[IMAGE alt='image' src='genlse.gif']
[IMAGE alt='image' src='genlsf.gif'] is the transposition of H<sub>0</sub>.

The previous equation and [Equation 2](#equation2) are also called normal equations of the least squares problems. You can solve them using LU or Cholesky factorization algorithms, but the solution from the normal equations is susceptible to round-off error.

The preferred way to minimize χ<sup>2</sup> is to find the least squares solution of the equations:

H<sub>0</sub>B = Y<sub>0</sub>

You can use QR or Singular Value Decomposition factorization to find the solution, B. For QR factorization, you can choose Householder, Givens, or Givens2, also called fast Givens.

Different algorithms can give you different precision. In some cases, if one algorithm cannot solve the equation, perhaps another algorithm can. You can try different algorithms to find the one best suited to your data.

GenLSFit calculates the covariance matrix **covariance** as follows:

[IMAGE alt='image' src='genlsg.gif']

The best fitted curve z is given by the following formula:

[IMAGE alt='image' src='genlsa.gif']

GenLSFit obtains the mean squared error using the following formula:

[IMAGE alt='image' src='genlsmse.gif']

You can think of the polynomial fit that has a single predictor variable as a special case of multiple regression. If the observation data sets are (x<sub>i</sub>, y<sub>i</sub>) where **i** = 0, 1, . . ., n – 1, the model for polynomial fit is as follows:

[IMAGE alt='image' src='genlsh.gif']

**[Equation 3]** 
 

where **i** = 0, 1, 2, . . ., n – 1

Comparing [Equation 1](#equation1) and the Equation 3 shows that [IMAGE alt='image' src='genlsi.gif']. In other words:

[IMAGE alt='image' src='genlsj.gif']

In this case, you can build **HMatrix** as follows:

[IMAGE alt='image' src='genlsk.gif']

Instead of using [IMAGE alt='image' src='genlsl.gif'], you can choose another function formula to fit the data sets (x<sub>i</sub>, y<sub>i</sub>). In general, you can select x<sub>ij</sub> = f<sub>j</sub>(x<sub>i</sub>). Here, f<sub>j</sub>(x<sub>i</sub>) is the function model that you choose to fit your observation data. In polynomial fit, [IMAGE alt='image' src='genlsm.gif'].

In general, you can build **HMatrix** as follows:

[IMAGE alt='image' src='genlsn.gif']

Your fit model is

y<sub>i</sub> = b<sub>0</sub>f<sub>0</sub>(x) + b<sub>1</sub>f<sub>1</sub>(x) + ... + b<sub>k – 1</sub>f<sub>k – 1</sub>(x)

The following two examples show how to use GenLSFit. The first example uses the function to perform multiple regression analysis based entirely on tabulated observation data. The second solves for the linear coefficients in a multiple-function equation.

**Predicting Cost**

Suppose you want to estimate the total cost, in dollars, of a production of
baked scones using the quantity produced, X<sub>1</sub>, and the price of one pound of flour, X<sub>2</sub>. To keep things simple, the following five data points form the sample data table shown in the following table.

| Cost (dollars) Y | Quantity X1 | Flour Price X2 |
| --- | --- | --- |
| $150 | 295 | $3.00 |
| $75 | 100 | $3.20 |
| $120 | 200 | $3.10 |
| $300 | 700 | $2.80 |
| $50 | 60 | $2.50 |

You want to estimate the coefficients to the following formula:

Y = b<sub>0</sub> + b<sub>1</sub>X<sub>1</sub> + b<sub>2</sub>X<sub>2</sub>

The only parameters you must build are the H (observation matrix) and y arrays. Each column of H is the observed data for each independent variable: The first column is one because the coefficient b<sub>0</sub> is not associated with any independent variable.
Fill in H as follows:

[IMAGE alt='image' src='genlso.gif']

The following code is based on this example.

// Example of predicting cost using GenLSFit 

int k, n, algorithm, status; 

double H[5][3], y[5], z[5], b[3], X1[5], X2[5], mse; 

double *stdDev=0, *covar=0; /* Define empty arrays; the function will 

ignore these parameters. */ 

n = 5; 

k = 3; 

// Read in data for X1, X2, and y.

. 

. 

.

// Construct matrix H. 

for(i=0;i<n;i++) {

H[i][0] = 1; // Fill in the first column of H. 

H[i][1] = X1[i]; // Fill in the second column of H. 

H[i][2] = X2[i]; // Fill in the third column of H.

} 

algorithm = 0; // Use SVD algorithm. 

status = GenLSFit (H, n, k, y, stdDev, algorithm, z, b, covar, &mse);

**Linear Combinations**

Suppose that you have samples from a transducer, y values, and you want to solve for the coefficients of the model:

y = b<sub>0</sub> + b<sub>1</sub>sin(ωx) + b<sub>2</sub>cos(ωx) + b<sub>3</sub>x<sup>3</sup>

To build H, set each column to the independent functions evaluated at each x value. Assuming there are 100 x values, H would be the following array:

[IMAGE alt='image' src='genlsp.gif']

The following code is based on this example.

// Example of linear combinations using GenLSFit 

int i, k, n, algorithm, status; 

double H[100][4], y[100], z[100], b[4], x[100], mse, w; 

double *stdDev=0, *covar=0; /* Define empty arrays, the function will 

ignore these parameters.*/ 

n = 100; 

k = 4; 

w = 0.2; 

// Read in data for x and y.

. 

. 

.

// Construct matrix H. 

for(i=0;i<n;i++) {

H[i][0] = 1; // Fill in the first column of H. 

H[i][1] = sin(w*x[i]); // Fill in the second column of H. 

H[i][2] = cos(w*x[i]); // Fill in the third column of H. 

H[i][3] = pow(x[i],3); // Fill in the fourth column of H.

} 

algorithm = 0; // Use SVD algorithm. 

status = GenLSFit (H, n, k, y, stdDev, algorithm, z, b, covar, &mse);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| hMatrix | void * | An n-by-k matrix that contains the observation data (xi0, xi1, ..., xik – 1) for i = 0, 1, . . ., n – 1, where n is the number of rows in HMatrix, k is the number of columns in HMatrix. This matrix must be an array of doubles. |
| numberOfRows | ssize_t | Number of rows in HMatrix and the number of elements in YArray. |
| numberOfColumns | ssize_t | Number of columns of HMatrix and the number of elements in coefficientArray. |
| yArray | double [] | An array whose elements contain the y coordinates of the data sets to be fitted. The number of elements in YArray must equal the number of rows in HMatrix. |
| standardDeviation | double [] | Standard deviation δi for data point (xi, yi). If the standard deviations are equal or if you do not know the standard deviation, pass NULL, and GenLSFit ignores this parameter. The size of this array should equal numberOfRows. If any standard deviation is 0, this function will return a singular matrix error. |
| algorithm | int | Algorithm used to solve the multiple linear regression model. The algorithm has the following possible values. ALGORITHM_SVD (0)—Use Singular Value Decomposition to solve the multiple linear regression model. This value is the default. ALGORITHM_GIVENS (1)—Use Givens Decomposition to solve the multiple linear regression model. ALGORITHM_GIVENS2 (2)—Use Square Root Free Givens Decomposition to solve the multiple linear regression model. ALGORITHM_HOUSEHOLD (3)—Use Householder Transformation to solve the multiple linear regression model. ALGORITHM_LU_DECOMP (4)—Use LU Decomposition to solve the multiple linear regression model. ALGORITHM_CHOLESKY (5)—Use Cholesky Decomposition to solve the multiple linear regression model. |
| Output |  |  |
| Name | Type | Description |
| zArray | double [] | The best fitted curve. The size of this array must equal at least numberOfRows. |
| coefficientArray | double [] | Set of coefficients that best fit the multiple linear regression model in a least squares sense. |
| covariance | void | Matrix of covariances with k-by-k elements. cj, k is the covariance between bj and bk, and cj, j is the variance of bj. If you pass an empty array for covariance, GenLSFit does not calculate this matrix. |
| meanSquaredError | double | The mean squared error generated by the difference between the fitted curve and the raw data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetalltcphostaddresses.htm language=enus -->
## TOPIC 00349: GetAllTCPHostAddresses

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetalltcphostaddresses.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetalltcphostaddresses.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetAllTCPHostAddresses

int GetAllTCPHostAddresses (char ***addresses, int *numberOfAddresses);

#### Purpose

Obtains all the [network interface IP addresses](../../cvi/libref/cvitcp_clients_and_servers.htm) of the computer on which your program is currently running.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| addresses | char ** | Pass the address of a pointer to pointer to char variable. The library allocates an array of strings representing the network interface addresses and returns them in this output parameter. When no longer needed, you must free all the address strings and the address array using the TCPFreeMemory function, as follows: Example Code char ** addresses = NULL; int numAddresses; int index; GetAllTCPHostAddresses (&addresses, &numAddresses); /* Use the address strings... */ for (index = 0; index < numAddresses; index++) { /* Free address string */ TCPFreeMemory (addresses[index]); } /* Free addresses array */ TCPFreeMemory (addresses); |
| numberOfAddresses | int | Number of address strings returned in the addresses parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. You can call the GetTCPSystemErrorString function to obtain a system message that describes the error. The system messages can be more descriptive than the TCP Support Library error codes. To obtain the correct system error message, you must call GetTCPSystemErrorString immediately after calling the TCP Support Library function that failed. For RegisterTCPServer and RegisterTCPServerEx, the return value is the port number assigned by the system if you passed zero for the port and the function was successful. For functions that read or write data (ClientTCPRead, ClientTCPWrite, ServerTCPRead, ServerTCPWrite), if the function was successful, the return value is the number of bytes transferred. You can have a maximum of 255 concurrent conversations and up to 1,024 connections. If you exceed this limit, -kTCP_TooManyConnections will be returned. You may not be able to open the maximum number of connections allowed by LabWindows/CVI because of limitations imposed by the operating system. |

#### Additional Information

**Library:** [TCP Support Library](../../cvi/libref/cvitcp_library_function_tree.htm)

**Include file:** tcpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetanalysiserrorstring.htm language=enus -->
## TOPIC 00350: GetAnalysisErrorString

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetanalysiserrorstring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetanalysiserrorstring.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetAnalysisErrorString

char *GetAnalysisErrorString (int errorNumber);

#### Purpose

Returns the [error message](../../cvi/libref/cviadvanced_analysis_library_error.htm) associated with the Analysis Library error code specified in the **errorNumber** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorNumber | int | An error code returned by an Analysis Library function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| errorMessage | char * | The error message associated with the error code. Do not modify or free this string. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetbreakonfirstchanceexceptions.htm language=enus -->
## TOPIC 00351: GetBreakOnFirstChanceExceptions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetbreakonfirstchanceexceptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetbreakonfirstchanceexceptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetBreakOnFirstChanceExceptions

int GetBreakOnFirstChanceExceptions (void);

#### Purpose

Returns the state of the **Run»Break on»First Chance Exceptions** option for the thread that calls this function.

GetBreakOnFirstChanceExceptions returns a 1 if the option is enabled, or a 0 if it is disabled.

If debugging is disabled, this function always returns 0.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| state | int | The current state of the state of the Run»Break on»First Chance Exceptions option. Code Description 1 Run»Break on»First Chance Exceptions option is enabled. 0 Run»Break on»First Chance Exceptions option is disabled. |
| Code | Description |  |
| 1 | Run»Break on»First Chance Exceptions option is enabled. |  |
| 0 | Run»Break on»First Chance Exceptions option is disabled. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetbreakonlibraryerrors.htm language=enus -->
## TOPIC 00352: GetBreakOnLibraryErrors

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetbreakonlibraryerrors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetbreakonlibraryerrors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetBreakOnLibraryErrors

int GetBreakOnLibraryErrors (void);

#### Purpose

Returns the state of the [Run»Break on»Library Errors](../../cvi/usermanual/wksprunbreakon.htm)Run»Break on»Library Errors option for the thread that calls this function.

GetBreakOnLibraryErrors returns a 1 if you enable the **Run»Break on»Library Errors** option. If you disable debugging, GetBreakOnLibraryErrors always returns 0.

To change the state of the **Run»Break on»Library Errors** option interactively, enable or disable that option in the Workspace window. To change the state of the **Run»Break on»Library Errors** option programmatically, use [SetBreakOnLibraryErrors](../../cvi/libref/cvisetbreakonlibraryerrors.htm).

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| state | int | Current state of the Run»Break on»Library Errors option. Code Description 1 Run»Break on»Library Errors option is enabled. 0 Run»Break on»Library Errors option is disabled or debugging is disabled. |
| Code | Description |  |
| 1 | Run»Break on»Library Errors option is enabled. |  |
| 0 | Run»Break on»Library Errors option is disabled or debugging is disabled. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetbreakonprotectionerrors.htm language=enus -->
## TOPIC 00353: GetBreakOnProtectionErrors

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetbreakonprotectionerrors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetbreakonprotectionerrors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetBreakOnProtectionErrors

int GetBreakOnProtectionErrors (void);

#### Purpose

Returns the state of the break on protection errors feature.

GetBreakOnProtectionErrors returns a 1 if you enable the option. If you disable debugging GetBreakOnProtectionErrors always returns 0.

For more information, refer to [SetBreakOnProtectionErrors](../../cvi/libref/cvisetbreakonprotectionerrors.htm).

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| state | int | Current state of the break on protection errors option. Code Description 1 Break on protection errors option is enabled. 0 Break on protection errors option is disabled or debugging is disabled. |
| Code | Description |  |
| 1 | Break on protection errors option is enabled. |  |
| 0 | Break on protection errors option is disabled or debugging is disabled. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetc.htm language=enus -->
## TOPIC 00354: getc

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetc.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetc.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### getc

int getc (FILE *stream);

#### Purpose

Reads the next character from the specified input stream
and advances the file position indicator. If successful, the function
returns the character read; otherwise, the function returns EOF (-1).

|  | Note This function is equivalent to fgetc, except that if implemented as a macro, it may evaluate the stream more than once. Therefore, the argument passed to it should never be an expression with potential side effects. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Contains a pointer to the input stream from which a character is read. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| characterRead | int | Contains the next character read from the input stream pointed to by stream. Two cases cause the function to return EOF (-1): Read error—Error indicator for stream is set Stream at end-of-file—EOF indicator for stream is set If an error occurs, getc returns EOF and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetchar.htm language=enus -->
## TOPIC 00355: getchar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetchar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetchar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### getchar

int getchar (void);

#### Purpose

Returns the next character from the input stream pointed to by the standard input. If the stream is at end-of-file or a read error occurs, the end-of-file indicator for
the stream is set and the function returns EOF (-1).

|  | Note This function is equivalent to getc(stdin). |
| --- | --- |

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| characterRead | int | Contains the next character from the input stream pointed to by stdin. Two cases cause the function to return EOF (-1): Read Error—Error indicator for stream is set Stream at end-of-file—EOF indicator for stream is set If an error occurs, getchar returns EOF and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\standardio.cws for an example of using the getchar function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetcomlinestatus.htm language=enus -->
## TOPIC 00356: GetComLineStatus

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetcomlinestatus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetcomlinestatus.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetComLineStatus

unsigned int GetComLineStatus (int portNumber);

#### Purpose

Returns the modem control-register values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| portNumber | int | A number that indicates the COM port on which to operate. This number maps to the COM port specified by deviceName in the call to OpenCom or OpenComConfig. The portNumber 1, for example, may not necessarily map to COM1. (Linux) The portNumber 1, for example, may not necessarily map to /dev/ttyS0. Valid Range: 1—1,000 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| lineStatus | unsigned int | Hardware-specific information about the status of the selected port. The status word is comprised of individual bits, each with a different meaning. This parameter is filled in with a combination of the following values: Name Value Description kRS_CTS_ON 0x10 The CTS (clear-to-send) signal is on. kRS_DSR_ON 0x20 The DSR (data-set-ready) signal is on. kRS_RING_ON 0x40 The ring indicator signal is on. kRS_RLSD_ON 0x80 The RLSD (receive-line-signal-detect) signal is on. |
| Name | Value | Description |
| kRS_CTS_ON | 0x10 | The CTS (clear-to-send) signal is on. |
| kRS_DSR_ON | 0x20 | The DSR (data-set-ready) signal is on. |
| kRS_RING_ON | 0x40 | The ring indicator signal is on. |
| kRS_RLSD_ON | 0x80 | The RLSD (receive-line-signal-detect) signal is on. |

#### Additional Information

**Library:** [RS-232 Library](../../cvi/libref/cvirs232_library_function_tree.htm)

**Include file:** rs232.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetcviversion.htm language=enus -->
## TOPIC 00357: GetCVIVersion

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetcviversion.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetcviversion.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetCVIVersion

int GetCVIVersion (void);

#### Purpose

Returns the version of the LabWindows/CVI Run-Time Engine libraries that you are using.

The value is in the form *Nnn*, where *N.n.n* corresponds to the first two sections of the numeric version in the About LabWindows/CVI dialog box.

For example, for LabWindows/CVI version 5.0, GetCVIVersion returns 500. For version 4.0.1, it returns 401. The values always increase with each new version of LabWindows/CVI.

|  | Notes Versions of LabWindows/CVI that follow year-based versioning continue to use the major.minor.tiny versioning described previously when returning the value for this function. Refer to the LabWindows/CVI Year-Based and Major.Minor.Tiny Version Equivalents topic for the current major.minor.tiny version equivalent. Use the GetCVIVersionYear function to return the year-based version of the LabWindows/CVI Run-Time Engine libraries that you are using. |
| --- | --- |

Do not confuse the return value of GetCVIVersion with the predefined macro _CVI_, which specifies the version of LabWindows/CVI in which the source file is compiled.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| CVIVersion | int | Version number of the LabWindows/CVI Run-Time Engine libraries. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetddeerrorstring.htm language=enus -->
## TOPIC 00358: GetDDEErrorString

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetddeerrorstring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetddeerrorstring.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetDDEErrorString

char *GetDDEErrorString (int errorNumber);

#### Purpose

Returns the [error message](../../cvi/libref/cvidde_library_error_conditions.htm) associated with the DDE Support Library error code specified in the **errorNumber** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorNumber | int | An error code returned by a DDE Support Library function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| errorMessage | char * | The error message associated with the error code. Do not modify or free this string. |

#### Additional Information

**Library:** [DDE Support Library](../../cvi/libref/cvidde_library_function_tree.htm)

**Include file:** ddesupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetdir.htm language=enus -->
## TOPIC 00359: GetDir

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetdir.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetdir.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetDir

int GetDir (char currentDirectory[]);

#### Purpose

Gets the current working directory on the default drive.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| currentDirectory | char [] | The pathname of the current directory. currentDirectory must be at least MAX_PATHNAME_LEN bytes long. Note MAX_PATHNAME_LEN is only reliable for ANSI single byte strings. For UTF-8 strings, call the IsUTF8PathLengthValid function to confirm that the file path is within the operating system character limit. GetDir does not add a terminating \\ to currentDirectory. |
|  | Note MAX_PATHNAME_LEN is only reliable for ANSI single byte strings. For UTF-8 strings, call the IsUTF8PathLengthValid function to confirm that the file path is within the operating system character limit. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -3 General I/O error occurred. -4 Insufficient memory to complete operation. |
| Code | Description |  |
| 0 | Success. |  |
| -3 | General I/O error occurred. |  |
| -4 | Insufficient memory to complete operation. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetdrive.htm language=enus -->
## TOPIC 00360: GetDrive

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetdrive.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetdrive.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetDrive

int GetDrive (int *currentDriveNumber, int *numberOfDrives);

#### Purpose

Gets the current default drive number and the total number of logical drives
in the system.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| currentDriveNumber | int | The drive number of the new default drive. The mapping between the drive number and the logical drive letter is 0 = A, 1 = B, and so on. |
| numberOfDrives | int | The total number of drives in the system. The number of drives includes floppy disk drives, hard disk drives, RAM disks, and networked drives. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -1 Current directory is on a network drive that is not mapped to a local drive. currentDriveNumber is set correctly, but numberOfDrives is set to -1. -3 General I/O error occurred. -4 Insufficient memory to complete the operation. -6 Access denied. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | Current directory is on a network drive that is not mapped to a local drive. currentDriveNumber is set correctly, but numberOfDrives is set to -1. |  |
| -3 | General I/O error occurred. |  |
| -4 | Insufficient memory to complete the operation. |  |
| -6 | Access denied. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetenableresourcetracking.htm language=enus -->
## TOPIC 00361: GetEnableResourceTracking

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetenableresourcetracking.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetenableresourcetracking.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetEnableResourceTracking

int GetEnableResourceTracking (void);

#### Purpose

Determines whether resource tracking
 is enabled in the current thread.

|  | Note This function is available only in the LabWindows/CVI Full Development SystemLabWindows/CVI Full Development System. |
| --- | --- |

Resource tracking is available at both the extended and standard debugging levels. When you enable resource tracking, LabWindows/CVI tracks resources such as memory blocks, file handles, and panel handles that you allocate in your program. Selecting **Extended** as the **Debugging level** in the **Debugging Options** section of the [Build Options](../../cvi/usermanual/prjbuildopt.htm)Build Options dialog box enables resource tracking by default. LabWindows/CVI displays currently allocated and recently released resources in the [Resource Tracking](../../cvi/usermanual/prjwindowrestracking.htm)Resource Tracking window. If you select **Standard** as the **Debugging level** in the Build Options dialog box, you must use the [SetEnableResourceTracking](../../cvi/libref/cvisetenableresourcetracking.htm) function to enable resource tracking.

|  | Note (RT) On RT targets, leaked resources persist until you reboot the target. However, the Resource Tracking window displays only leaked resources from the most recent program execution. |
| --- | --- |

Display the Resource Tracking window by selecting **Resource Tracking** in the **Window** menu.

(Linux) This function is not supported.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| state | int | Indicates if resource tracking is enabled. Code Description 1 Resource tracking is enabled. 0 Resource tracking is disabled. |
| Code | Description |  |
| 1 | Resource tracking is enabled. |  |
| 0 | Resource tracking is disabled. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetfullpathfromproject.htm language=enus -->
## TOPIC 00362: GetFullPathFromProject

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetfullpathfromproject.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetfullpathfromproject.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFullPathFromProject

int GetFullPathFromProject (char simpleFileName[], char fullPathName[]);

#### Purpose

Gets the full pathname for the file you specify, if the file is in the currently loaded project.

You can use GetFullPathFromProject when your program needs to access a file in the project and you do not know what directory the file is in.

In a stand-alone executable, GetFullPathFromProject assumes that the file is in the same directory as the executable file.

##### Example Code

char *fileName; 

char fullPath[MAX_PATHNAME_LEN]; 

fileName = "myfile.c"; 

if (GetFullPathFromProject (fileName, fullPath) < 0)

FmtOut ("File %s is not in the project\n", fileName);

|  | Note LabWindows/CVI does not report run-time errors for GetFullPathFromProject. |
| --- | --- |

|  | Note MAX_PATHNAME_LEN is only reliable for ANSI single byte strings. For UTF-8 strings, call the IsUTF8PathLengthValid function to confirm that the file path is within the operating system character limit. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| simpleFileName | char [] | The name of a file that is in the currently loaded project. The name must be a simple filename and should not contain any directory paths. For example, file.c is a simple filename, whereas dir\\file.c is not. |
| Output |  |  |
| Name | Type | Description |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -1 Unable to find specified file in the project |
| Code | Description |  |
| 0 | Success. |  |
| -1 | Unable to find specified file in the project |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigethosttcpsockethandle.htm language=enus -->
## TOPIC 00363: GetHostTCPSocketHandle

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigethosttcpsockethandle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigethosttcpsockethandle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetHostTCPSocketHandle

int GetHostTCPSocketHandle (unsigned int conversationHandle, intptr_t *socketHandle);

#### Purpose

Obtains the system socket handle that corresponds to a [TCP Support Library](../../cvi/libref/cvitcp_clients_and_servers.htm) connection.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| conversationHandle | unsigned int | TCP Support Library conversation handle that you obtain from ConnectToTCPServer or ConnectToTCPServerEx or receive in a server callback as the handle parameter of a TCP_CONNECT message. |
| Output |  |  |
| Name | Type | Description |
| socketHandle | intptr_t | System socket handle for the connection that conversationHandle identifies. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. You can call the GetTCPSystemErrorString function to obtain a system message that describes the error. The system messages can be more descriptive than the TCP Support Library error codes. To obtain the correct system error message, you must call GetTCPSystemErrorString immediately after calling the TCP Support Library function that failed. For RegisterTCPServer and RegisterTCPServerEx, the return value is the port number assigned by the system if you passed zero for the port and the function was successful. For functions that read or write data (ClientTCPRead, ClientTCPWrite, ServerTCPRead, ServerTCPWrite), if the function was successful, the return value is the number of bytes transferred. You can have a maximum of 255 concurrent conversations and up to 1,024 connections. If you exceed this limit, -kTCP_TooManyConnections will be returned. You may not be able to open the maximum number of connections allowed by LabWindows/CVI because of limitations imposed by the operating system. |

#### Additional Information

**Library:** [TCP Support Library](../../cvi/libref/cvitcp_library_function_tree.htm)

**Include file:** tcpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetinterruptstate.htm language=enus -->
## TOPIC 00364: GetInterruptState

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetinterruptstate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetinterruptstate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetInterruptState

int GetInterruptState (void);

#### Purpose

|  | Note This function is obsolete and always returns 1. |
| --- | --- |

(Linux) This function is not supported.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| interruptState | int | This function is obsolete and always returns 1. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetkey.htm language=enus -->
## TOPIC 00365: GetKey

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetkey.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetkey.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetKey

int GetKey (void);

#### Purpose

Waits for the user to press a key and then returns the key code as an integer value.

If the user has already pressed a key, the key value is returned immediately.

|  | Note GetKey detects keystrokes only in the Standard I/O window or in the console window of a Windows console application. GetKey does not detect keystrokes in windows you create with the User Interface Library. (Linux) GetKey detects keystrokes only in the Standard I/O window. You must first call the SetStdioPort function to specify to use the Standard I/O window. |
| --- | --- |

The values GetKey returns are the same as the key values the User Interface Library uses. Refer to userint.h. The following table shows examples of keystrokes and the values GetKey returns for them.

**Example Keystrokes and GetKey Return Values**

| Keystroke | Return Value |
| --- | --- |
| <b> | 'b' |
| <Ctrl-b> | (VAL_MENUKEY_MODIFIER \| 'B') |
| <F4> | VAL_F4_VKEY |
| <Shift-F4> | (VAL_SHIFT_MODIFIER \| VAL_F4_VKEY) |

##### Example Code

/* Give the user a chance to quit the program. */ 

 int k; 

 FmtOut ("Enter 'q' to quit, any other key to continue"); 

 k = GetKey (); 

 if ((k == 0x0051) || (k == 0x0071)) /* q or Q */

exit (0);

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| keyCode | int | The value representing the key pressed by the user. Key codes can be formed by either an ASCII character, a virtual key, or by a logical OR operation on values representing a modifier key and either an ASCII character or a virtual key. A modifier key is a <Shift> key, <Alt> key, or <Ctrl> key. The following constants represent the modifier key: VAL_SHIFT_MODIFIER VAL_UNDERLINE_MODIFIER VAL_MENUKEY_MODIFIER VAL_SHIFT_AND_MENUKEY ASCII characters are represented by a literal character, for example, 'A' or 'D'. Multibyte characters are returned as two consecutive key codes. The first key code represents the lead byte while the second key code is the trail byte of the multibyte character. As a result you have to call GetKey twice in a multibyte setting to obtain the entire multibyte character. Virtual keys are non-ASCII keys represented by the following key codes: VAL_FWD_DELETE_VKEY VAL_BACKSPACE_VKEY VAL_ESC_VKEY VAL_TAB_VKEY VAL_ENTER_VKEY VAL_UP_ARROW_VKEY VAL_DOWN_ARROW_VKEY VAL_LEFT_ARROW_VKEY VAL_RIGHT_ARROW_VKEY VAL_INSERT_VKEY VAL_HOME_VKEY VAL_END_VKEY VAL_PAGE_UP_VKEY VAL_PAGE_DOWN_VKEY VAL_F1_VKEY VAL_F2_VKEY VAL_F3_VKEY VAL_F4_VKEY VAL_F5_VKEY VAL_F6_VKEY VAL_F7_VKEY VAL_F8_VKEY VAL_F9_VKEY VAL_F10_VKEY VAL_F11_VKEY VAL_F12_VKEY Note To use these define constants, you must include userint.h in your program. When the VAL_MENUKEY_MODIFIER is used in conjunction with a letter, the letter is always represented in its uppercase form. |
|  | Note To use these define constants, you must include userint.h in your program. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetnextfile.htm language=enus -->
## TOPIC 00366: GetNextFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetnextfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetnextfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNextFile

int GetNextFile (char fileName[]);

#### Purpose

Gets the next file found in the search that [GetFirstFile](../../cvi/libref/cvigetfirstfile.htm) starts. On Windows, the order in which these functions return the file names is dependent on the file system type. With the NTFS and CDFS file systems, the names are returned in alphabetical order. With FAT file systems, the names are returned in the order the files were written to the disk, which may or may not be in alphabetical order.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileName | char [] | The name of the next file found. fileName contains the basename and extension of the next matching file and must be at least MAX_FILENAME_LEN characters in length. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Result of the search. Code Description 0 Success. -1 No more files found that match criteria. -2 GetFirstFile must be called before GetNextFile. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | No more files found that match criteria. |  |
| -2 | GetFirstFile must be called before GetNextFile. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetoutqlen.htm language=enus -->
## TOPIC 00367: GetOutQLen

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetoutqlen.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetoutqlen.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetOutQLen

int GetOutQLen (int portNumber);

#### Purpose

Returns the number of characters in the output queue of the specified port.

You can use GetOutQLen to ensure the output queue empties before you close the port. This function has no effect on the output queue.

GetOutQLen returns an error if you have not opened the port or if you pass an invalid value for **portNumber**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| portNumber | int | A number that indicates the COM port on which to operate. This number maps to the COM port specified by deviceName in the call to OpenCom or OpenComConfig. The portNumber 1, for example, may not necessarily map to COM1. (Linux) The portNumber 1, for example, may not necessarily map to /dev/ttyS0. Valid Range: 1—1,000 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| outputQueueLength | int | The current length of the output queue. |

#### Additional Information

**Library:** [RS-232 Library](../../cvi/libref/cvirs232_library_function_tree.htm)

**Include file:** rs232.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to rs232\serial.cws for an example of using the GetOutQLen function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetprojectdir.htm language=enus -->
## TOPIC 00368: GetProjectDir

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetprojectdir.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetprojectdir.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetProjectDir

int GetProjectDir (char directoryName[]);

#### Purpose

Gets the name of the directory that contains the currently loaded project file.

You can use GetProjectDir when you distribute a project and its related files to multiple users who might place the files in a different directory on each computer. If your program needs to access a file that is in the same directory as the project, you can use GetProjectDir and [MakePathname](../../cvi/libref/cvimakepathname.htm) to construct the full pathname.

In a stand-alone executable, the function obtains the directory containing the executable file.

##### Example Code

/* Get the name of the directory that contains myfile.dat */ 

char *fileName; 

char projectDir[MAX_PATHNAME_LEN]; 

char fullPath[MAX_PATHNAME_LEN]; 

fileName = "myfile"; 

if (GetProjectDir (projectDir) < 0)

FmtOut ("Project is untitled\n");

else

MakePathname (projectDir, fileName, fullPath);// where fullPath has the following format: c:\myproject\myfile.dat

|  | Note MAX_PATHNAME_LEN is only reliable for ANSI single byte strings. For UTF-8 strings, call the IsUTF8PathLengthValid function to confirm that the file path is within the operating system character limit. |
| --- | --- |

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| directoryName | char [] | The buffer in which the project directory name is returned. directoryName must be at least MAX_PATHNAME_LEN bytes long. GetProjectDir does not add a terminating \\ to directoryName. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -1 Current project has no pathname; the project is untitled. -2 There is no current project. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | Current project has no pathname; the project is untitled. |  |
| -2 | There is no current project. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the GetProjectDir function:

- fileio\arrayfile.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treesort.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\hyperlinkctrl\simple.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvigetrs232errorstring.htm language=enus -->
## TOPIC 00369: GetRS232ErrorString

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvigetrs232errorstring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvigetrs232errorstring.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetRS232ErrorString

char *GetRS232ErrorString (int errorNumber);

#### Purpose

Returns the [error message](../../cvi/libref/cvirs232_error_conditions.htm) associated with the RS-232 Library error code specified in the **errorNumber** parameter.

If **errorNumber** is -1 (Unknown System Error), GetRS232ErrorString calls the Windows SDK function GetLastError and translates the return value to a Windows message string.

If this function returns -1 from a real-time or Linux application, an unspecified system error occurred.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorNumber | int | An error code returned by an RS-232 Library function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| errorMessage | char * | The error message associated with the error code. Do not modify or free this string. |

#### Additional Information

**Library:** [RS-232 Library](../../cvi/libref/cvirs232_library_function_tree.htm)

**Include file:** rs232.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviincrementcvitimeinterval.htm language=enus -->
## TOPIC 00370: IncrementCVITimeInterval

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviincrementcvitimeinterval.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviincrementcvitimeinterval.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### IncrementCVITimeInterval

int IncrementCVITimeInterval (CVITimeInterval *interval, CVITimeInterval increment);

#### Purpose

Increments a time interval value by the specified time interval value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| increment | CVITimeInterval | A time interval increment value. |
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetfreememory.htm language=enus -->
## TOPIC 00371: InetFreeMemory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetfreememory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetfreememory.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFreeMemory

int InetFreeMemory (void *pointer);

#### Purpose

Frees memory allocated by one of the Internet Library functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointer | void * | A pointer to the memory to be freed. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Examples

Refer to the following examples that use the InetFreeMemory function:

- internet\ftpclnt\ftpclnt.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- internet\pop3clnt\pop3clnt.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetftpautoretrieve.htm language=enus -->
## TOPIC 00372: InetFTPAutoRetrieve

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetftpautoretrieve.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetftpautoretrieve.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFTPAutoRetrieve

int InetFTPAutoRetrieve (const char *FTPServer, const char *userName, const char *password, const char *localFile, const char *remoteFile, int transferType);

#### Purpose

Transfers a file from a remote FTP server to the local machine.

This high–level function logs in, changes directories, transfers the file, and logs out. The function closes the connection before it returns.

|  | Note You might need to use the lower–level functions to avoid errors if your application runs behind a firewall. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FTPServer | const char * | The name or IP address of the remote machine. The remote machine must be running an FTP server on the standard FTP server port (21). If the FTP server is using a non-standard port, then you can specify the port using the syntax address:port. |
| userName | const char * | The user name to use when logging in to the FTP server. |
| password | const char * | The password to use when logging in to the FTP server. |
| localFile | const char * | The pathname of the destination file on the local machine. The path can be absolute or relative to the current working directory on the local machine. If the file already exists, it is overwritten. |
| remoteFile | const char * | The pathname of the remote file to retrieve. The path can be absolute or relative to the current working directory on the remote machine. |
| transferType | int | The mode in which the file is to be transferred. The following modes are valid: INET_FTP_FILE_TYPE_ASCII—The file is converted into the local machine's ASCII file format (with regard to newlines and carriage returns). INET_FTP_FILE_TYPE_BINARY—The file is transferred exactly as is. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to internet\simpftp\simpftp.cws for an example of using the InetFTPAutoRetrieve function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetftpautosend.htm language=enus -->
## TOPIC 00373: InetFTPAutoSend

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetftpautosend.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetftpautosend.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFTPAutoSend

int InetFTPAutoSend (const char *FTPServer, const char *userName, const char *password, const char *localFile, const char *remoteFile, int transferType);

#### Purpose

Transfers a file from the local machine to a remote FTP server.

This high–level function logs in, changes directories, transfers the file, and logs out. The function closes the connection before it returns.

|  | Note You might need to use the lower–level functions to avoid errors if your application runs behind a firewall. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FTPServer | const char * | The name or IP address of the remote machine. The remote machine must be running an FTP server on the standard FTP server port (21). If the FTP server is using a non-standard port, then you can specify the port using the syntax address:port. |
| userName | const char * | The user name to use when logging in to the FTP server. |
| password | const char * | The password to use when logging in to the remote machine. |
| localFile | const char * | The pathname of the local file to send. The path can be absolute or relative to the current working directory on the local machine. |
| remoteFile | const char * | The pathname of the destination file on the remote machine. The path can be absolute or relative to the current working directory on the remote machine. |
| transferType | int | The mode in which the file is to be transferred. The following modes are valid: INET_FTP_FILE_TYPE_ASCII The file is converted into the remote machine's ASCII file format (with regard to newlines and carriage returns). INET_FTP_FILE_TYPE_BINARY The file is transferred exactly as is. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to internet\simpftp\simpftp.cws for an example of using the InetFTPAutoSend function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetftpchangedir.htm language=enus -->
## TOPIC 00374: InetFTPChangeDir

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetftpchangedir.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetftpchangedir.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFTPChangeDir

int InetFTPChangeDir (int FTPHandle, const char *newDirectory);

#### Purpose

Changes the current working directory on the remote machine.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FTPHandle | int | A handle returned by the InetFTPLogin or InetFTPLoginEx function. The handle identifies an active FTP connection. |
| newDirectory | const char * | The pathname of the new directory on the remote machine. The path can be absolute or relative to the current working directory on the remote machine. To go up in the directory tree, use "..". |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to internet\ftpclnt\ftpclnt.cws for an example of using the InetFTPChangeDir function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetftpclose.htm language=enus -->
## TOPIC 00375: InetFTPClose

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetftpclose.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetftpclose.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFTPClose

int InetFTPClose (int FTPHandle);

#### Purpose

Logs out and closes down an active FTP connection.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FTPHandle | int | A handle returned by the InetFTPLogin or InetFTPLoginEx function. The handle identifies an active FTP connection. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to internet\ftpclnt\ftpclnt.cws for an example of using the InetFTPClose function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetftplogin.htm language=enus -->
## TOPIC 00376: InetFTPLogin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetftplogin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetftplogin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFTPLogin

int InetFTPLogin (const char *FTPServer, const char *userName, const char *password);

#### Purpose

|  | Note This function has been superseded by InetFTPLoginEx. |
| --- | --- |

Opens a new FTP connection to the FTP server on the specified machine.

|  | Note A timeout value of 60 seconds will be used when reading data packets from and writing data packets to the FTP server. Use InetFTPLoginEx to change the timeout value. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FTPServer | const char * | The name or IP address of a remote machine running an FTP server on the standard FTP server port (21). If the FTP server is using a non-standard port, then you can specify the port using the syntax address:port. |
| userName | const char * | The user name to use when logging in to the FTP server. |
| password | const char * | The password to use when logging in to the FTP server. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| FTPHandle | int | The value that you must use in subsequent function calls to specify this FTP connection. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to internet\ftpclnt\ftpclnt.cws for an example of using the InetFTPLogin function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetftpreceivedata.htm language=enus -->
## TOPIC 00377: InetFTPReceiveData

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetftpreceivedata.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetftpreceivedata.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFTPReceiveData

ssize_t InetFTPReceiveData (int FTPHandle, char data[], size_t dataSize);

#### Purpose

Receives data associated with your command. You must call this function only from an FTP command data callback. The return value of this function indicates the number of bytes received. Call this function iteratively until it returns zero, indicating that there is no additional data to read.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FTPHandle | int | A handle returned by the InetFTPLogin or InetFTPLoginEx function. The handle identifies an active FTP connection. |
| dataSize | size_t | The size, in bytes, of the data buffer. This function returns an error if you pass a value greater than LLONG_MAX. |
| Output |  |  |
| Name | Type | Description |
| data | char [] | The buffer to hold the data received from the server. The function does not NUL-terminate the output buffer. The number of bytes received is indicated by the function return value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | ssize_t | Return value indicating whether the function was successful. If the function was successful, the return value is the number of bytes read. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetftpremovedir.htm language=enus -->
## TOPIC 00378: InetFTPRemoveDir

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetftpremovedir.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetftpremovedir.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetFTPRemoveDir

int InetFTPRemoveDir (int FTPHandle, const char *directory);

#### Purpose

Removes a directory on the remote machine.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FTPHandle | int | A handle returned by the InetFTPLogin or InetFTPLoginEx function. The handle identifies an active FTP connection. |
| directory | const char * | The pathname of the directory to delete. The directory must exist on the remote machine. The path can be absolute or relative to the current working directory on the remote machine. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to internet\ftpclnt\ftpclnt.cws for an example of using the InetFTPRemoveDir function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetlaunchdefaultwebbrowser.htm language=enus -->
## TOPIC 00379: InetLaunchDefaultWebBrowser

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetlaunchdefaultwebbrowser.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetlaunchdefaultwebbrowser.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetLaunchDefaultWebBrowser

int InetLaunchDefaultWebBrowser (const char *URL);

#### Purpose

Launches the Web browser that is registered as the default viewer for .htm or .html files. This function launches the browser and instructs it to open the given URL.

RT This function is not supported on the LabWindows/CVI Real-Time Module.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| URL | const char * | The URL the Web browser is to display. You may pass NULL if no specific URL is desired. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviinetping.htm language=enus -->
## TOPIC 00380: InetPing

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviinetping.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviinetping.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InetPing

int InetPing (const char *address, int *available, unsigned int timeout);

#### Purpose

Pings a machine to check if it is available.

RT This function is not supported on the LabWindows/CVI Real-Time Module.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | const char * | The network address of the machine to ping. The address can be an IP address or a network name. |
| timeout | unsigned int | Time in milliseconds to wait for reply from server. |
| Output |  |  |
| Name | Type | Description |
| available | int | Indicates whether the machine is available. The output value is nonzero if the machine is available and 0 if the machine is not available. Pass the address of an integer variable to hold this value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [Internet Library](../../cvi/libref/cviinternet_library_function_tree.htm)

**Include file:** cvintwrk.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimblen.htm language=enus -->
## TOPIC 00381: mblen

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimblen.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimblen.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### mblen

int mblen (const char multibyteChar[], size_t byteLimit);

#### Purpose

Determines the number of bytes contained in the specified multibyte character.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| multibyteChar | const char [] | Contains a pointer to the multibyte character that is examined. |
| byteLimit | size_t | Specifies the maximum number of bytes that are examined to determine the length of the specified multibyte character. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| numberOfBytes | int | Contains the number of bytes in the multibyte character. If multibyteChar is a null pointer, the function returns zero if multibyte characters are not state-dependent; otherwise, a nonzero value is returned. The function returns -1 if byteLimit bytes do not form a valid multibyte character. The function returns zero if multibyteChar points to the null character. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimedian.htm language=enus -->
## TOPIC 00382: Median

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimedian.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimedian.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Median

*Advanced Analysis Library Only*

AnalysisLibErrType Median (double inputArray[], ssize_t numberOfElements, double *median);

#### Purpose

Finds the median value of the input array.

To find the median value, Median first sorts the input array in ascending order. Let **S** be the sorted array:

[IMAGE alt='image' src='median.gif']

|  | Note The input array does not change. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Input array used to determine the median. |
| numberOfElements | ssize_t | Number of elements used to determine the median. |
| Output |  |  |
| Name | Type | Description |
| median | double | Median value of the input array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimedianfilter.htm language=enus -->
## TOPIC 00383: MedianFilter

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimedianfilter.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimedianfilter.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MedianFilter

*Advanced Analysis Library Only*

AnalysisLibErrType MedianFilter (double xArray[], ssize_t numberOfXAndYElements, ssize_t leftRank, ssize_t rightRank, double y[]);

#### Purpose

Filters the input array using a median filter. MedianFilter can perform the operation in place; that is, the input and output arrays can be the same. MedianFilter filters the input array **xArray** using the following equation: 

 

 Y<sub>i</sub> = Median(J<sub>i</sub>) for i = 0, 1, 2, ..., n – 1 

 

 Where Y represents the output sequence of filtered data **y**, n is the number of elements in **xArray**, J<sub>i</sub> is a subset of the input **xArray** centered about the i<sup>th</sup> element of **xArray**, and the indexed elements outside the range of **xArray** equal zero. The following equation describes J<sub>i</sub>. 

 

 J<sub>i</sub> = {x<sub>i–rl</sub>, x<sub>i–rl+1</sub>, ..., x<sub>i–1</sub>, x<sub>i</sub>, x<sub>i+1</sub>, ..., x<sub>i+rr–1</sub>, x<sub>i+rr</sub>}, 

 

 Where rl is the left rank and rr is the right rank. 

 

 The following illustration shows the computation of y<sub>i</sub>. 

 

 [IMAGE alt='loc_eps_medfilter.gif' src='loc_eps_medfilter.gif']

##### Example Code

/* Generate a random signal and filter it using a median filter. */ 

 double x[256], y[256]; 

 ssize_t n, leftrank, rightrank; 

 int status; 


 n = 256; 

 leftrank = 2; 

 rightrank = 3; 

 Uniform (n, 17, x); 

 status = MedianFilter(x, n, leftrank, rightrank, y);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xArray | double [] | Array containing the raw data to filter. |
| numberOfXAndYElements | ssize_t | Number of elements in both the input and output array. |
| leftRank | ssize_t | Number of elements used to compute the median filter to the left side. leftRank must be greater than or equal to 0. |
| rightRank | ssize_t | Number of elements used to compute the median filter to the right side. rightRank must be less than leftRank. If rightRank is less than 0, rightRank is equal to leftRank. |
| Output |  |  |
| Name | Type | Description |
| y | double [] | Filtered data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimemchr.htm language=enus -->
## TOPIC 00384: memchr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimemchr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimemchr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### memchr

void *memchr (const void *buffer, int charToFind, size_t numberOfBytes);

#### Purpose

Locates the first occurrence of the specified character in a
given memory block.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| buffer | const void * | Contains a pointer to the memory block that is searched for the specified character. |
| charToFind | int | Contains the character for which to search in the specified memory block. The input to this parameter must be a character with integer value between 0 and 255. |
| numberOfBytes | size_t | Specifies the maximum number of bytes that are searched for the specified character. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| matchedByte | void * | Contains a pointer to the located character in the memory block or a NULL pointer if the character is not found. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimodbessel2nd.htm language=enus -->
## TOPIC 00385: ModBessel2nd

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimodbessel2nd.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimodbessel2nd.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ModBessel2nd

*Advanced Analysis Library Only*

double ModBessel2nd (int n, double x);

#### Purpose

Computes the modified Bessel function Kr = K(r,x) of the second kind of integer order r. The modified Bessel function of the second kind of order r is defined as follows:

[IMAGE alt='image' src='modbessel2ndform_10.png']

which is a solution of the following differential equation:

[IMAGE alt='image' src='modbessel2ndform_9.png']

For any integer value of order **n**, the function is defined for nonnegative real values of **x**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| n | int | The order of the function. |
| x | double | The point at which the Bessel function is evaluated. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | The value of the Bessel function evaluated at x. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimode.htm language=enus -->
## TOPIC 00386: Mode

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Mode

*Advanced Analysis Library Only*

AnalysisLibErrType Mode (double inputArray[], ssize_t numberOfElements, double base, double top, ssize_t intervals, double *mode);

#### Purpose

|  | Note This function has been superseded by ModeEx. This function supports only unimodal analysis, while ModeEx supports multimodal analysis as well. |
| --- | --- |

Finds the mode of the input array.

Modes refer to the most common values obtained in a set of observations. For example, for a data set (3, 7, 3, 9, 9, 3, 5, 1, 8, 5), the unique mode is 3.

This function determines the mode in terms of the histogram of the input array.

##### Example Code

/* Generate a Gaussian distributed random array and find its mode. */ 

double x[2000], max, min, modeval; 

int n, intervals, imax, imin; 

n = 2000; 

intervals = 50; 

GaussNoise (n, 1.0E0, 17, x); 

MaxMin1D (x, n, &max, &imax, &min, &imin); 

Mode (x, n, min, max, intervals, &modeval);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | The input data set used to determine the mode. |
| numberOfElements | ssize_t | The length of inputArray. |
| base | double | Lower range over which the mode value is determined. The mode value is in the range [base:top]. Default Value: 0.0. |
| top | double | Upper range over which the mode value is determined. The mode value is in the range [base:top]. Default Value: 0.0. |
| intervals | ssize_t | The number of bins of the histogram to use when computing the estimated mode. This value must be positive integer. Default Value: 1. |
| Output |  |  |
| Name | Type | Description |
| mode | double | Mode value of the input array inputArray. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

#### Example

Refer to analysis\mode.cws for an example of using the Mode function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimodeex.htm language=enus -->
## TOPIC 00387: ModeEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimodeex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimodeex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ModeEx

*Advanced Analysis Library Only*

AnalysisLibErrType ModeEx (double inputArray[], ssize_t numberOfElements, ssize_t intervals, double *modes, ssize_t *numberOfModes);

#### Purpose

Finds the mode(s) of a list of numbers. Modes refer to the most common values obtained in a set of observations. For example, for a data set (3, 7, 3, 9, 9, 3, 5, 1, 8, 5), the unique mode is 3. There can be more than one mode. For example, for a data set (2, 4, 9, 6, 4, 6, 6, 2, 8, 2), there are two modes: 2 and 6. A distribution with a single mode is said to be unimodal. A distribution with more than one mode is said to be bimodal, trimodal, and so on, or in general, multimodal. If no number occurs more than once in the set, then there is no mode for that set of numbers. 

 

 To find the exact modes of a set of observations, call this function with **intervals** <=0. If your observations contain noise, you may want to use the histogram algorithm to estimate the modes. In this case, **intervals** specifies the number of bins of the histogram. The function returns the center values of the histogram bins that contain the most values from the input data set.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | The input data set. |
| numberOfElements | ssize_t | The length of inputArray. |
| intervals | ssize_t | The number of bins of the histogram. If intervals > 0, the function uses the histogram algorithm to find the modes.Otherwise, the function finds the exact modes of the input set. Any two elements, a and b, from the input data set, are regarded as equal if \|a-b\|<=DBL_EPSILON*\|a\|. |
| Output |  |  |
| Name | Type | Description |
| modes | double | The modes found. Estimate how many modes might exist in the data set and allocate enough memory space for modes before calling this function. |
| numberOfModes | ssize_t | On input, numberOfModes specifies the size of the buffer pointed to by modes, as the number of double-precision float numbers. On output, numberOfModes specifies how many modes actually exist in the input data set. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvimodf.htm language=enus -->
## TOPIC 00388: modf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvimodf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvimodf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### modf

double modf (double inputValue, double *integralPart);

#### Purpose

Breaks a double value into its integral and fractional parts,
each of which will have the same sign as the argument.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputValue | double | Contains the value that will be broken into integral and fractional parts. |
| Output |  |  |
| Name | Type | Description |
| integralPart | double | Contains the resulting integral part of inputValue. It has the same sign as inputValue. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| fractionalPart | double | Contains the resulting fractional part of inputValue. It has the same sign as inputValue. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvin_dist.htm language=enus -->
## TOPIC 00389: N_Dist

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvin_dist.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvin_dist.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### N_Dist

*Advanced Analysis Library Only*

AnalysisLibErrType N_Dist (double x, double *probabilityOfX);

#### Purpose

Calculates the one-sided probability:

p = prob(X ≤ x)

where X is a random variable from a standard normal distribution.

For computing the two-sided probability

p2 = prob(–x ≤ X ≤ x)

you can use the following formula:

p2 = 1.0 – 2 × prob(X ≤ –x)

##### Example Code

double x, p; 

x = -123.456; 

N_Dist (x, &p);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | The point from which the probability is computed. Range: –∞ < x < ∞ |
| Output |  |  |
| Name | Type | Description |
| probabilityOfX | double | Calculated probability (0 < p < 1). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinetvardeploying.htm language=enus -->
## TOPIC 00390: Deploying Applications using Network Variables

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinetvardeploying.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinetvardeploying.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Deploying Applications using Network Variables

You must deploy support software to any computer that will host a network variable. Network variables that you configure with the NI Distributed System Manager cannot be automatically deployed; you can deploy only the System Manager. If the variable will be [implicitly created](cvinetworkvariables.htm#implicit) by a client application, then it is sufficient to deploy only the NI Variable Engine component. You can select both the System Manager and Variable Engine components from the [Drivers & Components](../usermanual/editinstallerdc.htm)Drivers & Components tab of the [Edit Installer](../usermanual/editinstallerdb.htm)Edit Installer dialog box.

If your application only accesses network variables on other computers, you do not need to include additional components in your distribution. The **Network Variable Support** subcomponent of the LabWindows/CVI Runtime is automatically selected for you if your application uses the Network Variable Library.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinetwork_variable_library_function_tree.htm language=enus -->
## TOPIC 00391: Network Variable Library Function Tree

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinetwork_variable_library_function_tree.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinetwork_variable_library_function_tree.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Function Tree, Network Variable Library

| Class/Panel Name | Function Name |
| --- | --- |
| Create Subscriber | CNVCreateSubscriber |
| Create Buffered Subscriber | CNVCreateBufferedSubscriber |
| Create Reader | CNVCreateReader |
| Create Asynchronous Reader | CNVCreateAsyncReader |
| Create Writer | CNVCreateWriter |
| Create Buffered Writer | CNVCreateBufferedWriter |
| Get Data from Buffer | CNVGetDataFromBuffer |
| Read | CNVRead |
| Read Asynchronously | CNVReadAsync |
| Put Data in Buffer | CNVPutDataInBuffer |
| Write | CNVWrite |
| Get Connection Attribute | CNVGetConnectionAttribute |
| Set Connection Attribute | CNVSetConnectionAttribute |
| Dispose | CNVDispose |
| Free Memory | CNVFreeMemory |
| Get Error Description | CNVGetErrorDescription |
| Finish | CNVFinish |
| Data Functions |  |
| Get Data Type | CNVGetDataType |
| Get Array Data Dimensions | CNVGetArrayDataDimensions |
| Get Scalar Data Value | CNVGetScalarDataValue |
| Get Array Data Value | CNVGetArrayDataValue |
| Get Number of Struct Fields | CNVGetNumberOfStructFields |
| Get Struct Fields | CNVGetStructFields |
| Create Scalar Data Value | CNVCreateScalarDataValue |
| Create Array Data Value | CNVCreateArrayDataValue |
| Create Struct Data Value | CNVCreateStructDataValue |
| Set Scalar Data Value | CNVSetScalarDataValue |
| Set Array Data Value | CNVSetArrayDataValue |
| Set Struct Data Value | CNVSetStructDataValue |
| Get Data Quality | CNVGetDataQuality |
| Get Data UTC Timestamp | CNVGetDataUTCTimestamp |
| Get Data Server Error | CNVGetDataServerError |
| Get Timestamp Info | CNVGetTimestampInfo |
| Check Data Quality | CNVCheckDataQuality |
| Get Data Quality Description | CNVGetDataQualityDescription |
| Dispose Data | CNVDisposeData |
| Browser Functions |  |
| Create Browser | CNVCreateBrowser |
| Browse | CNVBrowse |
| Browse Next Item | CNVBrowseNextItem |
| Dispose Browser | CNVDisposeBrowser |
| Register Machine | CNVRegisterMachine |
| Unregister Machine | CNVUnregisterMachine |
| Get Registered Machines | CNVGetRegisteredMachines |
| Configuration Functions |  |
| Variable Engine is Running | CNVVariableEngineIsRunning |
| Process Functions |  |
| Get Processes | CNVGetProcesses |
| Process Exists | CNVProcessExists |
| New Process | CNVNewProcess |
| Delete Process | CNVDeleteProcess |
| Start Process | CNVStartProcess |
| Stop Process | CNVStopProcess |
| Process is Running | CNVProcessIsRunning |
| Variable Functions |  |
| Get Variables | CNVGetVariables |
| Variable Exists | CNVVariableExists |
| New Variable | CNVNewVariable |
| New Variable Collection | CNVNewVariableCollection |
| Delete Variable | CNVDeleteVariable |
| Get Variable Attribute | CNVGetVariableAttribute |
| Set Variable Attribute | CNVSetVariableAttribute |
| Folder Functions |  |
| Get Folders | CNVGetFolders |
| Folder Exists | CNVFolderExists |
| New Folder | CNVNewFolder |
| Delete Folder | CNVDeleteFolder |
| Advanced Functions |  |
| Flush All Connections | CNVFlushAllConnections |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinetworkvariablelibrary.htm language=enus -->
## TOPIC 00392: Network Variable Library Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinetworkvariablelibrary.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinetworkvariablelibrary.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Network Variable Library Overview

The LabWindows/CVI Network Variable Library contains functions for reading and writing data to [network variables](cvinetworkvariables.htm). You can use the functions in this library to communicate with LabVIEW shared variables and Measurement Studio network variables. You also can use the Network Variable Library functions in real-time (RT) applications.

|  | Note This library supersedes the DataSocket library and has better performance and scalability. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinetworkvariables.htm language=enus -->
## TOPIC 00393: Network Variables

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinetworkvariables.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinetworkvariables.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Network Variables

A network variable is a variable that you can use to share data between applications running on the same or different computers. Network variables use the NI Publish-Subscribe Protocol (NI-PSP) data transfer protocol to write and allow users to read live data. NI-PSP is a proprietary technology that provides fast and reliable data transmission for large and small applications.

Reference a network variable using its pathname. The pathname is similar to network file share names, such as \\machine\myprocess\item on Windows. In this example, machine is the computer name, IP address, or Fully Qualified Domain name of the server machine that is hosting the variable; myprocess contains network variable folders or variables and is referred to as a network variable process; and item is the name of the network variable. Following are additional examples:

- \\localhost\my_process\my_variable
- \\test_machine\my_process\my_folder1\my_folder2\my_variable
- \\192.168.1.100\my_process\my_variable
- \\test_machine.my_network.com\my_process\my_variable
- \\localhost\System\DAQmx\Server Polling Rate
- \\localhost\system\my_variable

You must open TCP ports in addition to UDP ports to configure firewalls and Network Address Translating (NAT) routers to transmit network variables. Starting at TCP port 59110, open one TCP port for each application you run. By default, NI-PSP begins looking for available TCP ports at port 59110 and increments upward until it finds an available port for each running application. You manually can configure the range of TCP ports that NI-PSP uses by creating and editing a logosxt.ini file. For RT targets, you can configure the range of TCP ports in the ni-rt.ini configuration file.

#### Creating Network Variables

You can create network variables either explicitly or implicitly.

##### Explicitly Created Variables

You can create and configure network variables explicitly with the stand-alone NI Distributed System Manager or programmatically using Network Variable Library functions.

###### Using the NI Distributed System Manager

Select **Start»All Programs»National Instruments»Distributed System Manager** to access this application, which is included in the LabWindows/CVI installation. Use this application to create new processes and variables, delete existing processes and variables, start and stop processes, create variables with specific data types or the variant data type, allow multiple writers or restrict write access to a single client, configure server buffering, and so on. For more information, refer to the *NI Distributed System Manager Help*, which you can access from the Distributed System Manager.

|  | Note Although you cannot run the Distributed System Manager on an RT target, you can host network variables you create and configure with the Distributed System Manager on an RT target. You cannot export network variables you create using the Distributed System Manager to other computers. |
| --- | --- |

###### Using Network Variable Library Functions

Use the [Configuration Functions](cvinetwork_variable_library_function_tree.htm#configfuncs) in the Network Variable Library to programmatically create and configure network variables explicitly. You can create a single variable with the [CNVNewVariable](cvicnvnewvariable.htm) function or create a number of variables with the [CNVNewVariableCollection](cvicnvnewvariablecollection.htm) function. You also can create, delete, start, and stop network variable processes using the [Process Functions](cvinetwork_variable_library_function_tree.htm#processfuncs). Use the [Folder Functions](cvinetwork_variable_library_function_tree.htm#folderfunctions) to create and delete folders programmatically. Explicit variables that you create programmatically do not have a concrete data type by default and can hold values of any type. If you want to specify the data type for a network variable, call the [CNVSetVariableAttribute](cvicnvsetvariableattribute.htm) function and set the [CNVVariablePrototypeAttribute](cnvvariableprototypeattribute.html) attribute. Explicit variables continue to exist after the program terminates.

Although you can programmatically configure network variables, you must use the Distributed System Manager to configure security settings.

|  | Note When you create variables programmatically, you specify server buffer capacity as number of items. If you use the Distributed System Manager, you must specify server buffer capacity in bytes for certain data types. If you create a network variable programmatically and then want to configure the variable using the Distributed System Manager, the Distributed System Manager may change the buffer size to bytes. |
| --- | --- |

##### Implicitly Created Variables

You can implicitly create network variables in the system process: a new variable is created automatically when you connect to it, if the process name is system and the variable name you specify does not already exist in the system process. For example, \\localhost\system\test would implicitly create a variable called test in the system process on your local computer. If the variable already exists, then your program connects to the existing variable and does not create a new variable. An implicitly created variable is automatically deleted by the server when all of its clients have disconnected. Implicit variables have no concrete data type and can hold values of any type. They always have the single-writer restriction and their values are not buffered on the server, but their values can be buffered on the client. Implicit variables are easier [to deploy](cvinetvardeploying.htm) because they are automatically created and deleted.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinonlinearfitwithmaxiters.htm language=enus -->
## TOPIC 00394: NonLinearFitWithMaxIters

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinonlinearfitwithmaxiters.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinonlinearfitwithmaxiters.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NonLinearFitWithMaxIters

*Advanced Analysis Library Only*

AnalysisLibErrType NonLinearFitWithMaxIters (double arrayX[], double arrayY[], double fittedArray[], ssize_t numberOfElements, int maximumIterations, ModelFun *modelFunction, double coefficientArray[], int numberOfCoefficients, double *meanSquaredError);

#### Purpose

Uses the Levenberg-Marquardt algorithm to determine the least squares set of coefficients that best fit the set of input data points (X,Y) as expressed by a nonlinear function y = f(x,a) where **a** is the set of coefficients. NonLinearFitWithMaxIters also gives the best fit curve y = f(x,a).

You must pass a pointer to the nonlinear function f(x,a) along with a set of initial guess coefficients **a**. NonLinearFitWithMaxIters does not always give the correct answer. The correct output sometimes depends on the initial choice of a. It is very important to verify the final result.

NonLinearFitWithMaxIters calculates the output mean squared error using the following formula:

[IMAGE alt='image' src='nonlinfit.gif']

|  | Note If NonLinearFitWithMaxIters reaches the maximum number of iterations without reaching a solution, it returns an error. The outputs fittedArray, coefficientArray, and meanSquaredError contain the best filtered array, best fit coefficients, and the mean square error at the end of maximum iterations, respectively. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | double [] | An array whose elements contain the X coordinates of the (X,Y) data sets. |
| arrayY | double [] | An array whose elements contain the Y coordinates of the (X,Y) data sets. |
| numberOfElements | ssize_t | Number of elements in both XArray and YArray. |
| maximumIterations | int | Maximum number of iterations allowed. If NonLinearFitWithMaxIters reaches the maximum number of iterations without reaching a solution, it returns an error. The outputs fittedArray, coefficientArray, and meanSquaredError contain the best filtered array, best fit coefficients, and the mean square error at the end of maximum iterations, respectively. |
| modelFunction | ModelFun * | Pointer to the model function, f(xi,a), used in the nonlinear fitting algorithm. The model function must be defined as follows: double ModelFunct (double x, double a[], int ncoef); where a contains the function coefficients. |
| numberOfCoefficients | int | The number of coefficients in coefficientArray. Notice that this is the number of coefficients that modelFunction actually uses and not necessarily the number of allocated elements in coefficientArray. For example, if coefficientArray is allocated as shown in the following code: coef = malloc(10*sizeof(double)) and the model function myModel() looks like the following code: double myModel(double x, double coef[], int ncoef) { return (coef[0]*exp(coef[1]*x);); } then the correct number of coefficients for this model function is 2, even though the coefficient array is allocated with 10 elements. Specifying anything more than 2 for the number of coefficients results in an error. |
| Output |  |  |
| Name | Type | Description |
| fittedArray | double [] | The array of values, y = f(x,a), where f is the user-supplied nonlinear model function, and a is the set of best-fit coefficients. The size of this array must be at least numberOfElements. |
| coefficientArray | double [] | The initial guess of the nonlinear fit coefficients. If this is initial set of coefficients is significantly different from the best fit set, the function might fail to return the appropriate coeficients and best fit curve. On exit, this array contains the fitted coefficients that best describe the nonlinear curve fitting given the model user-supplied model function. |
| meanSquaredError | double | The mean squared error generated by the difference between the fitted curve and the raw data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

#### Examples

Refer to the following examples that use the NonLinearFitWithMaxIters function:

- analysis\nlinfit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- analysis\nonlnfit.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinonlinearfitwithweight.htm language=enus -->
## TOPIC 00395: NonLinearFitWithWeight

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinonlinearfitwithweight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinonlinearfitwithweight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NonLinearFitWithWeight

*Advanced Analysis Library Only*

AnalysisLibErrType NonLinearFitWithWeight (double arrayX[], double arrayY[], double weight[], double fittedArray[], ssize_t numberOfElements, int maximumIterations, ModelFun *modelFunction, double coefficientArray[], int numberOfCoefficients, double *meanSquaredError, int *actualIterations);

#### Purpose

Uses the Levenberg-Marquardt algorithm to determine the least squares set of coefficients that best fit the set of input data points (X,Y) as expressed by a nonlinear function y = f(x,a) where **a** is the set of coefficients. NonLinearFitWithWeight also gives the best fit curve y = f(x,a).

You must pass a pointer to the nonlinear function f(x,a) along with a set of initial guess coefficients **a**. NonLinearFitWithWeight does not always give the correct answer. The correct output sometimes depends on the initial choice of a. It is very important to verify the final result.

NonLinearFitWithWeight calculates the output weighted mean square error using the following formula:

[IMAGE alt='image' src='nonlinearfitwithweightform_16.png']

|  | Note If NonLinearFitWithWeight reaches the maximum number of iterations without reaching a solution, it returns an error. The outputs fittedArray, coefficientArray, and residue contain the best filtered array, best fit coefficients, and the weighted mean square error at the end of maximum iterations, respectively. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | double [] | An array whose elements contain the X coordinates of the (X,Y) data sets. |
| arrayY | double [] | An array whose elements contain the Y coordinates of the (X,Y) data sets. |
| weight | double [] | The weight of each data point. If weight is NULL, the function assumes all the weights are 1. |
| numberOfElements | ssize_t | Number of elements in both arrayX and arrayY. |
| maximumIterations | int | Maximum number of iterations allowed. If NonLinearFitWithWeight reaches the maximum number of iterations without reaching a solution, it returns an error. The outputs fittedArray, coefficientArray, and meanSquaredError contain the best filtered array, best fit coefficients, and the weighted mean square error at the end of maximum iterations, respectively. |
| modelFunction | ModelFun * | Pointer to the model function, f(xi,a), used in the nonlinear fitting algorithm. The model function must be defined as follows: double ModelFunct (double x, double a[], int ncoef); where a contains the function coefficients. |
| numberOfCoefficients | int | The number of coefficients in coefficientArray. Notice that this is the number of coefficients that modelFunction actually uses and not necessarily the number of allocated elements in coefficientArray. For example, if coefficientArray is allocated as shown in the following code: coef = malloc(10*sizeof(double)) and the model function myModel() looks like the following code: double myModel(double x, double coef[], int ncoef) { return (coef[0]*exp(coef[1]*x);); } then the correct number of coefficients for this model function is 2, even though the coefficient array is allocated with 10 elements. Specifying anything more than 2 for the number of coefficients results in an error. |
| Output |  |  |
| Name | Type | Description |
| fittedArray | double [] | The array of values, y = f(x,a), where f is the user-supplied nonlinear model function, and a is the set of best-fit coefficients. The size of this array must be at least numberOfElements. |
| coefficientArray | double [] | The initial guess of the nonlinear fit coefficients. If the initial set of coefficients is significantly different from the best fit set, the function might fail to return the appropriate coeficients and best fit curve. On exit, this array contains the fitted coefficients that best describe the nonlinear curve fitting given the model user-supplied model function. |
| meanSquaredError | double | The weighted mean square error generated by the difference between the fitted curve and the raw data. |
| actualIterations | int | The number of iterations to reach the final results. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinormal1d.htm language=enus -->
## TOPIC 00396: Normal1D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinormal1d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinormal1d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Normal1D

*Advanced Analysis Library Only*

AnalysisLibErrType Normal1D (double inputArray[], ssize_t numberOfElements, double outputArray[], double *mean, double *standardDeviation);

#### Purpose

Normalizes a 1D input vector. The output vector has the following form:

[IMAGE alt='image' src='normal1d.gif']

where **mean** and **standardDeviation** are the mean and the standard deviation of the input vector.

Refer to [StdDev](../../cvi/libref/cvistddev.htm) for the formulas Normal1D uses to find the mean and the standard deviation.

Normal1D can perform the operation in place; that is, the input and output arrays can be the same.

The following example uses the Normal1D function.

double inputData[10], normalizedData[10]; 

double mean, standardDeviation; 

AnalysisLibErrType status; 
 

// Generate an array of random numbers 
 
status = Uniform (10, 17, inputData); 
 

status = Normal1D (inputData, 10, normalizedData, &mean, &standardDeviation);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Input vector used as the basis for normalization. |
| numberOfElements | ssize_t | Number of elements used in the normalization of the input vector. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Normalized vector. |
| mean | double | The mean, or average, value used to normalize the vector. |
| standardDeviation | double | Standard deviation used to normalize the input vector. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinormal2d.htm language=enus -->
## TOPIC 00397: Normal2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinormal2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinormal2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Normal2D

*Advanced Analysis Library Only*

AnalysisLibErrType Normal2D (void *inputMatrix, ssize_t numberOfRows, ssize_t numberOfColumns, void *outputMatrix, double *mean, double *standardDeviation);

#### Purpose

Normalizes a 2D input matrix. The output matrix has the following form:

[IMAGE alt='image' src='normal2d.gif']

where **mean** and **sDeviation** are the mean and the standard deviation of the input matrix.

Refer to [StdDev](../../cvi/libref/cvistddev.htm) for the formulas Normal2D uses to find the mean and the standard deviation.

Normal2D can perform the operation in place; that is, the input and output arrays can be the same.

The following example uses the Normal2D function.

double inputData[10][10], normalizedData[10][10]; 

double mean, stdDev; 

int i, j, numRows, numCols; 

AnalysisLibErrType status; 
 

numRows = 10; 

numCols = 10; 
 

/* Use a For loop to generate a 2D array of random numbers between 0.0 and 1.0 */ 

for (j = 0; j < 10; j++)

for (i = 0; i < 10; i++)

inputData[i][j] = Random(0.0, 1.0);

status = Normal2D(inputData, numRows, numCols, normalizedData, &mean, &stdDev);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input matrix to normalize. This matrix must be an array of doubles. |
| numberOfRows | ssize_t | Number of rows used in the normalization of the matrix. |
| numberOfColumns | ssize_t | Number of columns used in the normalization of the matrix. |
| Output |  |  |
| Name | Type | Description |
| outputMatrix | void * | Normalized matrix, as an array of doubles. |
| mean | double | The mean, or average, value used to normalize the input matrix. |
| standardDeviation | double | Standard deviation used to normalize the input matrix. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinotification_of_srq_and_other_gp.htm language=enus -->
## TOPIC 00398: Notification of SRQ and Other GPIB Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinotification_of_srq_and_other_gp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinotification_of_srq_and_other_gp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Notification of SRQ and Other GPIB Events

#### Synchronous Callbacks

You can use ibInstallCallback to specify functions to invoke when any board-level or
device-level condition on which you can wait using ibwait occurs.

Callback functions you install with ibInstallCallback are *synchronous* callbacks; that is, LabWindows/CVI can invoke them only when it processes
events. LabWindows/CVI processes events when you call ProcessSystemEvents or GetUserEvent or when RunUserInterface is active and you are not in a callback function. Consequently, the latency between the occurrence of the GPIB event and the invocation of the callback can be large. However, you are not restricted in what you can do in the callback function.

#### Asynchronous Callbacks

You can use ibnotify to install *asynchronous* callbacks. LabWindows/CVI can call your asynchronous callbacks at any time
with respect to the rest of your program. Consequently, the latency between the
occurrence of the GPIB event and the invocation of the callback is smaller than
with synchronous callbacks, but the callback function must be multithreaded
safe. Refer to the [ibnotify](cviibnotify.htm) function description for more details.

#### Driver Version Requirements

You must have version 1.2 or later of the
NI-488.2M driver to use ibInstallCallback and ibnotify.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinumericintegration.htm language=enus -->
## TOPIC 00399: NumericIntegration

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinumericintegration.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinumericintegration.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NumericIntegration

*Advanced Analysis Library Only*

AnalysisLibErrType NumericIntegration (double inputArray[], ssize_t size, double dt, int integrationMethod, double *integrationResult);

#### Purpose

Performs numeric integration on the data the input array **x** contains using one of the following four numeric integration methods: Trapezoidal Rule, Simpson's Rule, Simpson's 3/8 Rule, or Bode Rule. You normally obtain the data to integrate by sampling some function f(t) at multiples of **dt**. Your samples are f(0), f(dt), f(2dt), and so on. **dt** is the sampling step size.

If you do not provide a sufficient number of points for the integration method you choose, NumericIntegration applies the method you choose to all points it can. For the points that remain, NumericIntegration uses the next possible lower-order method.

For example, if you choose Bode Rule as the integration method, the following table shows how NumericIntegration evaluates the integral for different numbers of data points. If you provide 224 points and choose the Bode Rule method, NumericIntegration arrives at the result by performing 55 Bode Rule method partial evaluations and one Simpson's 3/8 Rule method evaluation.

| Number of Points | Partial Evaluations Performed |
| --- | --- |
| 224 | 55 Bode, 1 Simpson's 3/8 |
| 225 | 56 Bode |
| 226 | 56 Bode, Trapezoidal |
| 227 | 56 Bode, 1 Simpson's |
| 228 | 57 Bode, 1 Simpson's 3/8 |

**Formulas for Integration Methods**

For i = 0, 1, 2, . . ., int((**n** – 1)/**k**),where **n** is the number of data points, **k** is an integer dependent on the method, and **inputArray** is the input array. The following shows the basic formulas for each of the four integration methods.

**Trapezoidal Rule**

(dt/2) × (x<sub>i</sub> + x<sub>i + 1</sub>) for k = 1

**Simpson's Rule**

(dt/3) × (x<sub>2i</sub> + 4x<sub>2i + 1</sub> + x<sub>2i + 2</sub>) for k = 2

**Simpson's 3/8 Rule**

(dt/8) × (3x<sub>3i</sub> + 9x<sub>3i + 1</sub> + 9x<sub>3i + 2</sub> + 3x<sub>3i + 3</sub>) for k = 3

**Bode Rule**

(dt/45) × (14x<sub>4i</sub> + 64x<sub>4i + 1</sub> + 24x<sub>4i + 2</sub> + 64X<sub>4i + 3</sub> + 14x<sub>4i + 4</sub>) for k = 4

Each method depends on the sampling interval, **dt**, and calculates the integral by using successive applications of the basic formula to perform partial evaluations. The number of points each partial evaluation uses represents the order of the method. The result is the sum of these successive partial evaluations.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Array that contains data to integrate. This data is obtained by sampling a function f(t) at multiples of dt, that is, f(0), f(dt), f(2dt), and so on. |
| size | ssize_t | Number of elements in inputArray. |
| dt | double | Interval size, which represents the sampling step size to use to obtain the data. |
| integrationMethod | int | Integration method used to perform the numeric integration. The following table shows valid integrationMethod values. integrationMethod Value Trapezoidal Rule 0 Simpson's Rule 1 Simpson's 3/8 Rule 2 Bode Rule 3 |
| integrationMethod | Value |  |
| Trapezoidal Rule | 0 |  |
| Simpson's Rule | 1 |  |
| Simpson's 3/8 Rule | 2 |  |
| Bode Rule | 3 |  |
| Output |  |  |
| Name | Type | Description |
| integrationResult | double | Result of the numeric integration. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinumericwinproperties.htm language=enus -->
## TOPIC 00400: NumericWinProperties

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinumericwinproperties.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinumericwinproperties.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NumericWinProperties

*Advanced Analysis Library Only*

AnalysisLibErrType NumericWinProperties (double coefficients[], int numberOfCoefficients, WindowConst *windowConstants);

#### Purpose

Computes the coherent gain and equivalent noise bandwidth of a window numerically. The coherent gain and equivalent noise bandwidth of a given window are defined as follows: 

 

 [IMAGE alt='noloc_eq_winprop1.gif' src='noloc_eq_winprop1.gif']
 

 [IMAGE alt='noloc_eq_winprop2.gif' src='noloc_eq_winprop2.gif']
 

 

 where w<sub>i</sub> are the window coefficients and n is the number of coefficients.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| coefficients | double [] | The coefficients of the window. |
| numberOfCoefficients | int | The number of elements in coefficients. |
| Output |  |  |
| Name | Type | Description |
| windowConstants | WindowConst | The equivalent noise bandwidth (ENBW) and coherent gain of the window defined by coefficients. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvinumfmtdbytes.htm language=enus -->
## TOPIC 00401: NumFmtdBytes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvinumfmtdbytes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvinumfmtdbytes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NumFmtdBytes

int NumFmtdBytes (void);

#### Purpose

Returns the number of bytes formatted or scanned by the previous formatting or scanning call.

##### Example Code

double f; 


int n; 
 


Scan ("3.1416", "%s>%f", &f); 
 


n = NumFmtdBytes (); 
 


/* n will have the value 6, indicating that */ 
 


/* 6 bytes were scanned from the source string. */

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| BytesFormatted | int | If the previous call was a formatting call, n represents the number of bytes placed into the target. If the previous call was a scanning call, n represents the number of bytes scanned from the source. n is undefined if there are no preceding formatting or scanning calls. |

#### Additional Information

**Library:** [Formatting and I/O Library](../../cvi/libref/cviformatting_and_io_library_functi.htm)

**Include file:** formatio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_get_thread_num.htm language=enus -->
## TOPIC 00402: omp_get_thread_num

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_get_thread_num.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_get_thread_num.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_get_thread_num

int omp_get_thread_num (void);

#### Purpose

Returns the thread number of the current thread executing the [parallel region](../../cvi/libref/openmpterminology.htm#parallelregion).

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

The number is an integer between 0 and one less than the value of the number of threads used in the parallel region.

**Binding thread set**: current team

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int | N—N is the number of the calling thread within the region. 0—The thread is the master thread that created the parallel region. Note This function also returns 0 if it is called from within a sequential region. |
|  | Note This function also returns 0 if it is called from within a sequential region. |  |

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_get_wtick.htm language=enus -->
## TOPIC 00403: omp_get_wtick

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_get_wtick.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_get_wtick.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_get_wtick

double omp_get_wtick (void);

#### Purpose

Returns the precision of the wall clock timer used by the [omp_get_wtime](../../cvi/libref/cviomp_get_wtime.htm) function, in seconds.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

**Binding thread set**: encountering thread

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | double | The precision of the wall clock timer used by the omp_get_wtime function, in seconds. |

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_get_wtime.htm language=enus -->
## TOPIC 00404: omp_get_wtime

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_get_wtime.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_get_wtime.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_get_wtime

double omp_get_wtime (void);

#### Purpose

Returns the elapsed wall clock time in seconds since an arbitrary, but consistent, point in the past.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

The value this function returns is bound to the calling thread and is consistent for each thread; however, it is not guaranteed to be globally consistent across all other threads in the program.

Use this function to measure the time taken by a task, as shown in the following example:

double startTime; 

double endTime; 

startTime = omp_get_wtime(); 

...code representing work you want to time... 

endTime = omp_get_wtime(); 

printf("This task took %f seconds\n", endTime - startTime);

**Binding thread set**: encountering thread

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | double | The elapsed wall clock time in seconds since an arbitrary, but consistent, point in the past. |

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

#### Example

Refer to OpenMP\matrixmult.cws for an example of using the omp_get_wtime function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_init_lock.htm language=enus -->
## TOPIC 00405: omp_init_lock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_init_lock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_init_lock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_init_lock

void omp_init_lock (omp_lock_t *lock);

#### Purpose

Initializes a simple, uninitialized OpenMP lock to the unlocked state. In the unlocked state, no thread owns the lock.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

Lock variables you pass to this function must be in the unintialized state. An uninitialized lock variable is one that has never been passed to this function or which has been destroyed by calling the [omp_destroy_lock](../../cvi/libref/cviomp_destroy_lock.htm) function.

**Binding thread set**: all threads

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lock | omp_lock_t | A pointer to a variable of type omp_lock_t. After this function returns, this variable represents an initialized lock in the unlocked state. |

#### Return Value

None.

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_init_nest_lock.htm language=enus -->
## TOPIC 00406: omp_init_nest_lock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_init_nest_lock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_init_nest_lock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_init_nest_lock

void omp_init_nest_lock (omp_nest_lock_t *lock);

#### Purpose

Initializes a nestable, uninitialized OpenMP lock to the unlocked state. In the unlocked state, no thread owns the lock.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

Lock variables you pass to this function must be in the unintialized state. An uninitialized lock variable is one that has never been passed to this function or which has been destroyed by calling the [omp_destroy_nest_lock](../../cvi/libref/cviomp_destroy_nest_lock.htm) function.

**Binding thread set**: all threads

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lock | omp_nest_lock_t | A pointer to a variable of type omp_nest_lock_t. After this function returns, this variable represents an initialized lock in the unlocked state. |

#### Return Value

None.

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_set_dynamic.htm language=enus -->
## TOPIC 00407: omp_set_dynamic

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_set_dynamic.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_set_dynamic.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_set_dynamic

void omp_set_dynamic (int dynamicThreads);

#### Purpose

LabWindows/CVI does not support dynamic adjustment of the number of threads. This function is provided for compatiblity reasons should you choose to port your code to another OpenMP-compatible compiler. Calling this function has no effect in LabWindows/CVI.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

**Binding thread set**: encountering thread

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| dynamicThreads | int | LabWindows/CVI ignores this parameter. |

#### Return Value

None.

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_set_nested.htm language=enus -->
## TOPIC 00408: omp_set_nested

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_set_nested.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_set_nested.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_set_nested

void omp_set_nested (int nested);

#### Purpose

LabWindows/CVI does not support nested parallelism. This function is provided for compatiblity reasons should you choose to port your code to another OpenMP-compatible compiler. This function always returns FALSE in LabWindows/CVI.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

**Binding thread set**: encountering thread

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| nested | int | Always returns FALSE in LabWindows/CVI. |

#### Return Value

None.

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_test_nest_lock.htm language=enus -->
## TOPIC 00409: omp_test_nest_lock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_test_nest_lock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_test_nest_lock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_test_nest_lock

int omp_test_nest_lock (omp_nest_lock_t *lock);

#### Purpose

Attempts to set a nestable OpenMP lock without blocking the execution of the calling thread.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

The function returns TRUE if the lock is successfully set and ownership of the lock is granted to the calling thread. Otherwise it returns FALSE.

Locks you pass to this function must be not be in the unintialized state.

**Binding thread set**: all threads

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lock | omp_nest_lock_t * | A pointer to a variable of type omp_nest_lock_t. If the function returns TRUE, the lock variable is then in the locked state. Otherwise the state of the lock remains unchanged. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int | Returns TRUE if the lock is successfully set. Otherwise it returns FALSE. |

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviomp_unset_nest_lock.htm language=enus -->
## TOPIC 00410: omp_unset_nest_lock

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviomp_unset_nest_lock.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviomp_unset_nest_lock.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### omp_unset_nest_lock

void omp_unset_nest_lock (omp_nest_lock_t *lock);

#### Purpose

Unsets a nestable OpenMP lock and causes the calling thread to release ownership of the lock.

|  | Note The OpenMP Run-Time Library is available only in the LabWindows/CVI Full Development System. |
| --- | --- |

The lock you pass to this function must be in the locked state and owned by the calling thread.

After this function executes, if one or more threads are waiting for this lock, LabWindows/CVI chooses one of the threads and gives the thread ownership of the lock.

**Binding thread set**: all threads

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lock | omp_nest_lock_t * | A pointer to a variable of type omp_nest_lock_t. After this function returns, the lock variable is in the unlocked state. |

#### Return Value

None.

#### Additional Information

**Library:** [OpenMP Run-Time Library](../../cvi/libref/cviopenmp_runtime_library_function_tree.htm)

**Include file:** omp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviouterproduct.htm language=enus -->
## TOPIC 00411: OuterProduct

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviouterproduct.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviouterproduct.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### OuterProduct

*Advanced Analysis Library Only*

AnalysisLibErrType OuterProduct (double vectorX[], ssize_t numberOfElementsInX, double vectorY[], ssize_t numberOfElementsInY, void *outerProduct);

#### Purpose

Calculates the outer product of the real input vectors x and y.

Let x<sub>i</sub> represent the elements of the **numberElementsX**-element vector x for i = 0, 1, 2, . . ., **numberElementsX** – 1.

Let y<sub>j</sub> represent the elements of the **numberElementsY**-element vector y for **j** = 0, 1, 2, . . ., **numberElementsY** – 1.

The outer product of these two vectors is a matrix O of dimensions n-by-m, where the (i, j)<sup>th</sup> element of O is given by

o<sub>i, j</sub> = x<sub>i</sub> × y<sub>j</sub>

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vectorX | double [] | The first vector used in the calculation of the outer product. |
| numberOfElementsInX | ssize_t | The number of elements in vectorX. |
| vectorY | double [] | The second vector used in the calculation of the outer product. |
| numberOfElementsInY | ssize_t | The number of elements in vectorY. |
| Output |  |  |
| Name | Type | Description |
| outerProduct | void * | Calculated outer product matrix, as an array of doubles. If vectorX is of dimensions m and vectorY is of dimensions n, the size of the matrix containing the outer product is m-by-n. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

#### Examples

Refer to the following examples that use the OuterProduct function:

- analysis\2dfft.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- OpenMP\2dfft_omp.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviparks_mcclellancoef.htm language=enus -->
## TOPIC 00412: Parks_McClellanCoef

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviparks_mcclellancoef.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviparks_mcclellancoef.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Parks_McClellanCoef

*Advanced Analysis Library Only*

AnalysisLibErrType Parks_McClellanCoef (int numberOfCoefficients, double samplingFrequency, BandParameter bandParameters[], ssize_t numberOfParameters, int filterType, double coefficients[], double *ripple);

#### Purpose

Designs a set of linear-phase FIR multiband digital filter coefficients. Parks_McClellanCoef generates only the filter coefficients; it does not actually perform data filtering. To filter a sequence X using the set of FIR filter coefficients **coefficients**, call [ConvolveEx](../../cvi/libref/cviconvolveex.htm) with X and **coefficients** as the input sequences. The equi-ripple filters use a similar technique to filter the data. 

 

 For more information, refer to Discrete-Time Signal Processing by Oppenheim and Schafer, cited in the [Bibliography](../../cvi/libref/cvibibliography_for_advanced_analys.htm).

##### Example Code

/* Design a 55-point linear-phase FIR multiband digital filter using Parks-McClellan algorithm. Filter the incoming signal with the designed filter. */

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfCoefficients | int | The total number of coefficients in coefficients. A coefficient corresponds to a multiplication and an addition. If there are n coefficients, every filtered sample requires n multiplications and n additions. This value must be greater than 2. |
| samplingFrequency | double | Sampling frequency in Hertz. This value must be greater than zero. |
| bandParameters | BandParameter [] | Pointer to the band parameters structure that contains the necessary information associated with each band for the FIR design. The definition of the filter structure is as follows: typedef struct { double amplitude; /* appropriate magnitude response, or gain, of the filter between fLow and fHigh */ double fLow; /* frequency at which the band begins */ double fHigh; /* frequency at which the band ends */ double wRipple; /* weighted ripple error that this function minimizes */ } BandParam, *BandParamPtr; amplitude—The appropriate magnitude response, or gain, of the filter between fLow and fHigh. fLow—The frequency at which the band begins. fHigh—frequency at which the band ends. wRipple—The weighted ripple error that this function minimizes. The higher the weight, the smaller the error in the band. For each band, fHigh must be greater than fLow, as shown by the following relationship. fhi < fli for i = 0, 1, 2, ..., m – 1 where fhi is the higher frequency in the ith band, fli is the lower frequency in the ith band, and m is the number of bands. For adjacent bands, the lower frequency in the higher band must be greater than the higher frequency in the adjacent lower band, as shown by the following relationship. fli < fhi – 1 for i = 1, 2, ..., m – 1 where fli is the lower frequency in the higher of the adjacent bands, fhi – 1 is the higher frequency in the lower of the adjacent bands, and m is the number of bands. The higher frequency in the last band must be equal to or less than half of samplingFrequency. |
| numberOfParameters | ssize_t | Size of bandParameters. |
| filterType | int | Filter type. filterType must be one of the following values. Constant Value Description PM_MULTIBAND 0 Specifies a multiband filter. If numberOfCoefficients is an odd number, this function does not place restrictions on the value of the amplitude. If numberOfCoefficients is an even number, the amplitude of the last band at half of the sampling frequency must be 0. PM_DIFFERENTIATOR 1 Specifies a differentiator. If numberOfCoefficients is an even number, this function does not place restrictions on the last band. If numberOfCoefficients is an odd number, the value of higher frequency in the last band must be less than half of the sampling freq. For example, a typical normalized band {0, 0.49} leaves a 0.01 transitional band at half of the sampling frequency, 0.5. PM_HILBERT 2 Specifies a Hilbert transformer. The value of lower frequency in the first band must be greater than 0. A typical normalized lower frequency in the first band is 0.03. If numberOfCoefficients is an even number, this function does not place restrictions on the last band. If numberOfCoefficients is an odd number, the value of higher frequency in the last band must be less than half of the sampling frequency. A typical normalized higher frequency in the last band is 0.49. |
| Constant | Value | Description |
| PM_MULTIBAND | 0 | Specifies a multiband filter. If numberOfCoefficients is an odd number, this function does not place restrictions on the value of the amplitude. If numberOfCoefficients is an even number, the amplitude of the last band at half of the sampling frequency must be 0. |
| PM_DIFFERENTIATOR | 1 | Specifies a differentiator. If numberOfCoefficients is an even number, this function does not place restrictions on the last band. If numberOfCoefficients is an odd number, the value of higher frequency in the last band must be less than half of the sampling freq. For example, a typical normalized band {0, 0.49} leaves a 0.01 transitional band at half of the sampling frequency, 0.5. |
| PM_HILBERT | 2 | Specifies a Hilbert transformer. The value of lower frequency in the first band must be greater than 0. A typical normalized lower frequency in the first band is 0.03. If numberOfCoefficients is an even number, this function does not place restrictions on the last band. If numberOfCoefficients is an odd number, the value of higher frequency in the last band must be less than half of the sampling frequency. A typical normalized higher frequency in the last band is 0.49. |
| Output |  |  |
| Name | Type | Description |
| coefficients | double [] | Array of FIR filter coefficients using the Parks-McClellan algorithm with the Remes exchange technique. |
| ripple | double | Optimal ripple that is a measure of deviation from the ideal filter specifications. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviparzenwin.htm language=enus -->
## TOPIC 00413: ParzenWin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviparzenwin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviparzenwin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ParzenWin

*Advanced Analysis Library Only*

AnalysisLibErrType ParzenWin (double signal[], ssize_t numberOfElements);

#### Purpose

Applies a Parzen window to a real signal. If y represents the output sequence **signal**, ParzenWin obtains the elements of y using the following equation:

[IMAGE alt='image' src='parzenwinform_14.png']

for i = 0, 1, 2, ..., n – 1, where n is the number of elements in **signal**. 

 

 This function applies an unsymmetrical Parzen window to the input signal. If you want to apply a symmetrical Parzen window, call [SymWin](../../cvi/libref/cvisymwin.htm) instead. 

 

 This function performs the window operation in place; that is, the windowed data replaces the input data.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in signal. |
| Output |  |  |
| Name | Type | Description |
| signal | double [] | On input, the input signal. On output, this parameter returns the input signal with a Parzen window applied. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvipowerfitinterval.htm language=enus -->
## TOPIC 00414: PowerFitInterval

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvipowerfitinterval.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvipowerfitinterval.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PowerFitInterval

*Advanced Analysis Library Only*

AnalysisLibErrType PowerFitInterval (double arrayX[], double arrayY[], double weight[], ssize_t numberOfElements, int intervalType, double confidenceLevel, double amplitude, double power, double upperBound[], double lowerBound[], double *deltaAmplitude, double *deltaPower);

#### Purpose

Calculates the confidence interval for the best power fitting function or the prediction interval for the observations. The confidence interval refers to the interval within which the actual function is expected to fall. The prediction interval refers to the interval within which the y values are expected to fall in repeated measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| arrayX | double [] | The x value of the data set (x, y). |
| arrayY | double [] | The y value of the data set (x, y). |
| weight | double [] | The weight of each data point. If weight is NULL, the function sets all the elements of weight to 1. |
| numberOfElements | ssize_t | The length of arrayX, arrayY, and weight. |
| intervalType | int | The type of interval. intervalType must be one of the following values: CONFIDENCE_INTVL (0)PREDICTION_INTVL (1) deltaAmplitude and deltaPower are not referenced if intervalType is PREDICTION_INTVL. |
| confidenceLevel | double | The level of certainty for the confidence interval or prediction interval. For the confidence interval, confidenceLevel specifies the probability that the actual function lies within the confidence interval. For the prediction interval, confidenceLevel specifies the probability that the y values lie within the prediction interval in repeated measurements. confidenceLevel must be between 0 and 1. |
| amplitude | double | The amplitude of the fitted power model calculated using the Least Square method. |
| power | double | The power of the fitted power model calculated using the Least Square method. |
| Output |  |  |
| Name | Type | Description |
| upperBound | double [] | The upper bound for the confidence interval or prediction interval. |
| lowerBound | double [] | The lower bound for the confidence interval or prediction interval. |
| deltaAmplitude | double | The uncertainty radius of amplitude. deltaAmplitude is available only when intervalType is CONFIDENCE_INTVL. |
| deltaPower | double | The uncertainty radius of power. deltaPower is available only when intervalType is CONFIDENCE_INTVL. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvipowerfrequencyestimate.htm language=enus -->
## TOPIC 00415: PowerFrequencyEstimate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvipowerfrequencyestimate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvipowerfrequencyestimate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PowerFrequencyEstimate

*Advanced Analysis Library Only*

AnalysisLibErrType PowerFrequencyEstimate (double autoSpectrum[], ssize_t numberOfElements, double searchFrequency, WindowConst windowConstants, double df, ssize_t frequencySpan, double *frequencyPeak, double *powerPeak);

#### Purpose

Calculates the estimated power and frequency around a peak in the power spectrum of a time-domain signal. With PowerFrequencyEstimate, you can achieve good frequency estimates for measured frequencies that lie between frequency lines on the spectrum. PowerFrequencyEstimate also makes corrections for the window function you use.

PowerFrequencyEstimate calculates the estimated frequency peak using the following formula:

[IMAGE alt='image' src='pwfreqa.gif']

PowerFrequencyEstimate calculates the estimated power peak as follows:

[IMAGE alt='image' src='pwfreqb.gif']

| where | i = index of the searchFreq |
| --- | --- |
|  | df is the frequency interval, usually in Hertz, as output by the AutoPowerSpectrum function |
|  | enbw is the equivalent noise bandwidth member of the structure windowConstants as output by the ScaledWindowEx function |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| autoSpectrum | double [] | Single-sided power spectrum as output by AutoPowerSpectrum. |
| numberOfElements | ssize_t | Number of elements in the input autoSpectrum array. |
| searchFrequency | double | Frequency, usually in Hertz, of the frequency around which you want to estimate the frequency and power. If searchFreq is less than zero or is not a valid frequency, PowerFrequencyEstimate automatically searches for the maximum peak in the autoSpectrum array and estimates the frequency and power around the maximum peak. Default Value: –1.0. |
| windowConstants | WindowConst | Structure that contains the following useful constants for the selected window: enbw is the equivalent noise bandwidth of the selected window. You can use this value to scale a sum of individual power spectra of the power spectrum or to calculate the power in a given frequency span. coherentgain is the peak gain of the window, relative to the peak gain of the Rectangular window. PowerFrequencyEstimate uses this value to normalize peak signal gains to that of the Rectangular window. ScaledWindowEx creates the windowConstants structure. |
| df | double | Frequency interval, in Hertz, as output by AmpPhaseSpectrum, AutoPowerSpectrum, CrossPowerSpectrum, NetworkFunctions, or TransferFunction. Default Value: 1.0. |
| frequencySpan | ssize_t | Number of frequency lines, or bins, around the peak to include in the peak frequency and power estimation. The estimation includes the power in freqSpan/2 frequency lines before the peak frequency line, the peak frequency line itself, and freqSpan/2 frequency lines after the peak. Default Value: 7. |
| Output |  |  |
| Name | Type | Description |
| frequencyPeak | double | Points to the estimated frequency of the estimated peak power in autospectrum. |
| powerPeak | double | Points to the estimated peak power in autospectrum. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

#### Example

Refer to analysis\peakest.cws for an example of using the PowerFrequencyEstimate function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvipulse.htm language=enus -->
## TOPIC 00416: Pulse

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvipulse.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvipulse.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Pulse

*Advanced Analysis Library Only*

AnalysisLibErrType Pulse (ssize_t numberOfElements, double amplitude, ssize_t delay, ssize_t width, double pulse[]);

#### Purpose

Generates an array that represents the pattern of a pulse waveform. Pulse obtains the i<sup>th</sup> element of the output array using the formula:

[IMAGE alt='image' src='pulsepattn.gif']

for **i** = 0, 1, 2, . . ., **numberOfElements** – 1

The value of **delay** + **width** cannot exceed the **numberOfElements**.

##### Example Code

/* The following code generates the following pulse pattern pulsePattern = {0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 0.0}. */ 

double pulsePattern[10], amp; 

n, delay, width; 

n = 10; 

delay = 3; 

width = 5; 

amp = 2.0; 

Pulse (n, amp, delay, width, pulsePattern);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | Number of elements to generate in the pulse pattern. |
| amplitude | double | Amplitude of the pulse to generate. Default Value: 1.0. |
| delay | ssize_t | Number of elements before the pulse pattern begins. For example, if the delay is 5, the pulse pattern begins at the sixth location of the array. If delay + width is greater than or equal to numberOfElements, Pulse returns an error code and does not generate the pattern. Default Value: 0. |
| width | ssize_t | Number of elements over which the pulse amplitude remains valid. If delay + width is greater than or equal to numberOfElements, Pulse returns an error code and does not generate the pattern. Default Value: 1. |
| Output |  |  |
| Name | Type | Description |
| pulse | double [] | The generated pulse pattern array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

#### Examples

Refer to the following examples that use the Pulse function:

- analysis\2dfft.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- analysis\transmit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- OpenMP\2dfft_omp.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvipulsemeas.htm language=enus -->
## TOPIC 00417: PulseMeas

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvipulsemeas.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvipulsemeas.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PulseMeas

*Advanced Analysis Library Only*

AnalysisLibErrType PulseMeas (double waveform[], ssize_t waveformSize, int polarity, ssize_t pulseNumber, double highRefLevel, double midRefLevel, double lowRefLevel, int referenceUnits, int method, ssize_t histogramBins, double *period, double *pulseDuration, double *dutyCycle, double *pulseCenter, double *lowRefValue, double *midRefValue, double *highRefValue);

#### Purpose

Calculates the period, **pulseDuration** (pulse width), **pulseCenter**, and **dutyCycle** (duty factor) of a waveform in user-defined cycle. 

 The distance between the **midRefLevel** and the **highRefLevel** must equal the distance between the **lowRefLevel** and the **midRefLevel**. If the two distances are not equal, LabWindows/CVI adjusts either the **highRefLevel** or the **lowRefLevel** to match the smaller of the two distances. For example, if you specify a **highRefLevel** of 90%, a **midRefLevel** of 50%, and a **lowRefLevel** of 20%, LabWindows/CVI uses 80% instead of 90% for the **highRefLevel**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| waveform | double [] | The waveform to measure. |
| waveformSize | ssize_t | The size of waveform x. |
| polarity | int | Defines a pulse as high or low. A high pulse consists of the interval between a rising midRefLevel crossing and the next falling midRefLevel crossing. Specify a nonzero value or ANALYSIS_HIGH or select High in the function panel to specify a high pulse. This is the default value. Specify 0 or ANALYSIS_LOW or select Low in the function panel to specify a low pulse. |
| pulseNumber | ssize_t | Specifies which pulse of polarity, high or low, to measure. |
| highRefLevel | double | The high reference level of the waveform in percent or absolute units. After the signal crosses the midRefLevel in the rising direction, it must cross the highRefLevel before this function can count the next falling midRefLevel crossing. |
| midRefLevel | double | The middle reference level in percent or absolute units. The interval between consecutive rising midRefLevel crossings defines one cycle, or period, of the waveform. At least one high/low reference level crossing must separate each midRefLevel crossing. |
| lowRefLevel | double | The low reference level of the waveform in percent or absolute units. After the signal crosses the midRefLevel in the falling direction, it must cross the lowRefLevel before this function can count the next rising midRefLevel crossing. |
| referenceUnits | int | Specifies whether the highRefLevel, midRefLevel, and lowRefLevel are interpreted as a percentage of the full range of the waveform or as absolute levels. Specify one of the following values: ABSOLUTE_LEVEL - The values you pass to highRefLevel, midRefLevel, and lowRefLevel are interpreted as absolute values.PERCENTAGE_LEVEL - The values you pass to highRefLevel, midRefLevel, and lowRefLevel are interpreted as percentages of the full range of the waveform. |
| method | int | The method of calculating high and low state levels of the waveform. Histogram method - Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform . Peak method - Searches the entire waveform for its maximum and minimum levels. Auto Select method - Determines whether the histogram bins corresponding to the high and low state levels both have over 5% of the total hits. If so, LabWindows/CVI returns those results. Otherwise, LabWindows/CVI uses the Peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and preshoot) or a triangle wave (where a histogram fails). |
| histogramBins | ssize_t | The number of bins in the Histogram method. LabWindows/CVI ignores histogramBins if you select Peak method as method. |
| Output |  |  |
| Name | Type | Description |
| period | double | The time between adjacent midRefLevel crossings in the same direction in samples. |
| pulseDuration | double | The time difference in samples between the first two midRefLevel crossings of the pulseNumber you specify. |
| dutyCycle | double | A fraction of a period. dutyCycle is also known as duty factor. LabWindows/CVI calculates dutyCycle by the following equation: dutyCycle = 100*(pulseDuration/period) |
| pulseCenter | double | The time instant of the midpoint of the pulseNumber. |
| lowRefValue | double | The returned low reference level of the waveform in absolute units. |
| midRefValue | double | The returned middle reference level of the waveform in absolute units. |
| highRefValue | double | The returned high reference level of the waveform in absolute units. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviputchar.htm language=enus -->
## TOPIC 00418: putchar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviputchar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviputchar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### putchar

int putchar (int character);

#### Purpose

Writes the specified character to the standard output. If successful, the function returns the
character written; otherwise, the function returns EOF (-1).

|  | Note This function is equivalent to fputc(Character, stdout). |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| character | int | Contains the character to be written to the standard output. The input must be a character with integer value between 0 and 255. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| characterWritten | int | Contains the character written. If an error occurs, putchar sets the error indicator for the stream, returns EOF, and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvirand.htm language=enus -->
## TOPIC 00419: rand

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvirand.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvirand.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### rand

int rand (void);

#### Purpose

Computes a pseudorandom integer in the range 0 to RAND_MAX.

|  | Note If this function is called before any call to srand, the seed value will default to 1. |
| --- | --- |

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| randomNumber | int | Contains the pseudorandom number generated by the function. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the rand function:

- analysis\interp.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\callback.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphs.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadedGuessers\ThreadedGuessers.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvireadfile.htm language=enus -->
## TOPIC 00420: ReadFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvireadfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvireadfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ReadFile

int ReadFile (int fileHandle, char buffer[], size_t count);

#### Purpose

Reads up to **count** bytes of data from a file or the Standard Input into **buffer**. Reading starts at the current position of the file pointer. When ReadFile completes, the file pointer points to the next unread character in the file.

The return value can be less than the number of bytes requested if ReadFile reaches the end of the file before the byte count is satisfied. If you open the file in ASCII mode, ReadFile counts each carriage return/linefeed (CR/LF) combination read as one character because the pair is translated into an LF when ReadFile stores it in the buffer.

|  | Note ReadFile does not terminate the buffer with an ASCII NUL. |
| --- | --- |

|  | Caution The Windows SDK also contains a function with the same name. Include windows.h before including formatio.h to ensure that there are no compilation errors as a result of this naming conflict. Define the SDK_CONFLICT_PRIORITYSDK_CONFLICT_PRIORITY macro to force LabWindows/CVI to use the Windows SDK implementation of this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileHandle | int | The file from which to read the data. Call OpenFile to obtain a fileHandle. To read from the Standard I/O window, pass 0 for fileHandle. |
| count | size_t | Maximum number of bytes to read. count must not be greater than buffer size. An error is returned if you pass a value greater than INT_MAX. |
| Output |  |  |
| Name | Type | Description |
| buffer | char [] | Buffer into which you read data. You must allocate space for this buffer before you call ReadFile. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| bytesRead | int | Number of bytes read. A value of –1 indicates that an error occurred during the read operation, possibly because of a bad file handle. You can use GetFmtIOError to get more information about the type of error that occurred. A return value of 0 indicates that ReadFile did not read any bytes because it reached the end of the file. Note If you opened the file in ASCII mode, the number of bytes returned does NOT include the CR in a CR/LF combination because each CR/LF combination is translated to an LF when the data is read. |
|  | Note If you opened the file in ASCII mode, the number of bytes returned does NOT include the CR in a CR/LF combination because each CR/LF combination is translated to an LF when the data is read. |  |

#### Additional Information

**Library:** [Formatting and I/O Library](../../cvi/libref/cviformatting_and_io_library_functi.htm)

**Include file:** formatio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviregistertcpserverex.htm language=enus -->
## TOPIC 00421: RegisterTCPServerEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviregistertcpserverex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviregistertcpserverex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RegisterTCPServerEx

int RegisterTCPServerEx (unsigned int portNumber, tcpFuncPtr callbackFunction, void *callbackData, const char localhostAddress[]);

#### Purpose

Registers your program as a valid [TCP server](../../cvi/libref/cvitcp_clients_and_servers.htm) on the specified localhost address and port and allows other applications to connect to it for network communication.

Clients attempting to connect to your program must use the same port number. Thereafter, all requests by the client are routed through the specified server callback function. You can register your program as a TCP server multiple times as long as you specify different localhost address and port number combinations.

|  | Note You must process messages to receive events in your callback. A thread processes messages when it calls RunUserInterface, ProcessSystemEvents, GetUserEvent, or any of the built-in User Interface Library pop-up functions. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| portNumber | unsigned int | The port number under which your program is registered as a TCP server. You can choose any port number in the range from 1 to 65,535. You can also pass zero if you want the operating system to use an unused port. If you pass zero, this function outputs the port number assigned by the system in the return value. |
| callbackFunction | tcpFuncPtr | Pointer to the synchronous callback function that processes client requests. The callback function must be of the following form: int (*tcpFuncPtr) (unsigned handle, int xType, int errCode, void *callbackData); xType specifies the type of message the server sends. The server callback function can receive the following transaction types: TCP_CONNECT—Received when a client requests a connection. TCP_DISCONNECT—Received when a client requests the termination of a connection or when a connection terminates because of an error. If the connection terminates because of an error, the errCode parameter contains a negative error code. TCP_DATAREADY—Received when there is data to be read by the server. Your program, acting as the server, calls ServerTCPRead to obtain the data. Note that this event is received again if you do not read all the available data. Use errCode only when the transaction type is TCP_DISCONNECT. Note The return value of the callback is ignored. Server callbacks should be short and should return as soon as possible. |
|  | Note The return value of the callback is ignored. Server callbacks should be short and should return as soon as possible. |  |
| callbackData | void * | A pointer-width value that the TCP Support Library passes to the callback function each time the library invokes the callback for the same server. You must define the meaning of the callback data. The following examples show how you can use the callback data. You can register your program as a TCP server multiple times under different port numbers. You can use the same callback function for all the server instances by using the callback data to differentiate between them. You can use the callback data as a pointer to a data object that you need to access in the callback function. This way, you can avoid declaring the data object as a global variable. You can pass zero if you do not want to use the callback data. |
| localhostAddress | const char [] | The address of the localhost network interface to be used for the connection. Use one of the addresses returned by the GetAllTCPHostAddresses function or the corresponding DNS name. You can pass NULL or an empty string if you have only one network interface. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. You can call the GetTCPSystemErrorString function to obtain a system message that describes the error. The system messages can be more descriptive than the TCP Support Library error codes. To obtain the correct system error message, you must call GetTCPSystemErrorString immediately after calling the TCP Support Library function that failed. For RegisterTCPServer and RegisterTCPServerEx, the return value is the port number assigned by the system if you passed zero for the port and the function was successful. For functions that read or write data (ClientTCPRead, ClientTCPWrite, ServerTCPRead, ServerTCPWrite), if the function was successful, the return value is the number of bytes transferred. You can have a maximum of 255 concurrent conversations and up to 1,024 connections. If you exceed this limit, -kTCP_TooManyConnections will be returned. You may not be able to open the maximum number of connections allowed by LabWindows/CVI because of limitations imposed by the operating system. |

#### Additional Information

**Library:** [TCP Support Library](../../cvi/libref/cvitcp_library_function_tree.htm)

**Include file:** tcpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvireporting_analysis_errors.htm language=enus -->
## TOPIC 00422: Reporting Analysis Errors

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvireporting_analysis_errors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvireporting_analysis_errors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Reporting Analysis Errors

Each analysis function returns an integer [error code](cviadvanced_analysis_library_error.htm). If the function executes
properly, the function returns a zero; otherwise, the function returns an
appropriate error value. You can use [GetAnalysisErrorString](cvigetanalysiserrorstring.htm) to get the error message associated with each Analysis Library error code.

The return value corresponds to one of the enumeration values of the type that AnalysisLibErrType declares in the header file analysis.h. The analysis functions are declared in the header file with this return type
so that the function panel controls for return values display the symbolic
name instead of the integer value of the error code. Declaring a variable to be
the type AnalysisLibErrType allows the Variables and Call Stack window to display the variable value as a symbolic name instead
of as an integer.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvireporting_rs232_errors.htm language=enus -->
## TOPIC 00423: Reporting RS-232 Errors

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvireporting_rs232_errors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvireporting_rs232_errors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Reporting RS-232 Errors

The functions in the RS-232 Library return negative values when an error
occurs. In addition, the global variable rs232err is updated after each call to a RS-232 Library function. If the function
executes properly, it sets rs232err to zero. Otherwise, the function sets rs232err to the same error code that it returns.

When an asynchronous write operation fails, the function sets rs232err to an error code unless rs232err already contains a negative value. ReturnRS232Error returns the same value as rs232err except that it keeps track of separate error codes for each thread in your
application. In a multithreaded application, use ReturnRS232Error rather than rs232err.

GetRS232ErrorString translates each possible error code into a meaningful error string.

[RS-232 Error Conditions](cvirs232_error_conditions.htm) lists the possible error conditions that can occur when you use the RS-232 Library functions.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvireverse.htm language=enus -->
## TOPIC 00424: Reverse

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvireverse.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvireverse.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Reverse

*Advanced Analysis Library Only*

AnalysisLibErrType Reverse (double inputArray[], ssize_t numberOfElements, double outputArray[]);

#### Purpose

Reverses the order of the elements of the input array using the following formula:

y<sub>i</sub> = x<sub>n – i – 1</sub>

for **i** = 0, 1, . . ., **n** – 1

Reverse can perform the operation in place; that is, the input and output arrays can be the same.

The following example uses the Reverse function.

double inputData[10], reverseData[10]; 

AnalysisLibErrType status; 
 

// Generate an array of random numbers 
 
status = Uniform (10, 17, inputData); 

status = Reverse(inputData, 10, reverseData);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Input array whose elements are placed in reverse order in the output array. |
| numberOfElements | ssize_t | Number of elements to reverse. |
| Output |  |  |
| Name | Type | Description |
| outputArray | double [] | Reversed array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvirewind.htm language=enus -->
## TOPIC 00425: rewind

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvirewind.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvirewind.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### rewind

void rewind (FILE *stream);

#### Purpose

Sets the file position indicator for the specified stream to the beginning of the
file. It is equivalent to the following, except that
the error indicator for the stream is also cleared:
 

 (void) [fseek](../../cvi/libref/cvifseek.htm)(stream, 0L, SEEK_SET)

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Contains a pointer to the stream that has had its file position indicator reset to the beginning of the file. |

#### Return Value

None.

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvirtcontrollerquery.htm language=enus -->
## TOPIC 00426: RTControllerQuery

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvirtcontrollerquery.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvirtcontrollerquery.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RTControllerQuery

int RTControllerQuery (char target[], RTControllerInfo *targetInformation);

#### Purpose

Retrieves information about the real-time target.

|  | Note This function is deprecated. Use the GetRTSystemInfo function in the Real-Time Utility Library instead. The Real-Time Utility Library is available when you install the LabWindows/CVI Real-Time Module. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| target | char [] | The name of the real-time target. The name can either be an alphabetical string, such as xyz.natinst.com, or a numerical string, such as 123.456.7.8. |
| Output |  |  |
| Name | Type | Description |
| targetInformation | RTControllerInfo | Information about the real-time target. typedef struct { unsigned long serialNumber; char ipAddress[16]; /* format: xxx.xxx.xxx.xxx */ char status[32]; /* running/install mode/etc. */ char modelDescription[32]; char hostName[32]; char macAddress[6]; /* returned as hex data */ } RTControllerInfo; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. Code Description 0 Success. kRTTargetIsInInstallMode The real-time target is installing software. kRTTargetIsLocked The real-time target is locked. kRTTargetOtherError The real-time target could not be rebooted. The function can also return error codes from the TCP/IP Library. |
| Code | Description |  |
| 0 | Success. |  |
| kRTTargetIsInInstallMode | The real-time target is installing software. |  |
| kRTTargetIsLocked | The real-time target is locked. |  |
| kRTTargetOtherError | The real-time target could not be rebooted. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvirtcontrollerreboot.htm language=enus -->
## TOPIC 00427: RTControllerReboot

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvirtcontrollerreboot.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvirtcontrollerreboot.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RTControllerReboot

int RTControllerReboot (char target[]);

#### Purpose

Reboots the real-time target.

|  | Note This function is deprecated. Use the RebootRTSystem function in the Real-Time Utility Library instead. The Real-Time Utility Library is available when you install the LabWindows/CVI Real-Time Module. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| target | char [] | The name of the real-time target. The name can either be an alphabetical string, such as xyz.natinst.com, or a numerical string, such as 123.456.7.8. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Return value indicating whether the function was successful. Code Description 0 Success. kRTTargetIsInInstallMode The real-time target is installing software. kRTTargetIsLocked The real-time target is locked. kRTTargetOtherError The real-time target could not be rebooted. The function can also return error codes from the TCP/IP Library. |
| Code | Description |  |
| 0 | Success. |  |
| kRTTargetIsInInstallMode | The real-time target is installing software. |  |
| kRTTargetIsLocked | The real-time target is locked. |  |
| kRTTargetOtherError | The real-time target could not be rebooted. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvirunexternalmodule.htm language=enus -->
## TOPIC 00428: RunExternalModule

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvirunexternalmodule.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvirunexternalmodule.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RunExternalModule

int RunExternalModule (int moduleID, const char buffer[]);

#### Purpose

|  | Note This class of functions is deprecated. National Instruments recommends that you instead use the Windows SDK functions LoadLibrary and GetProcAddress to load external modules. These functions allow you to load Windows DLLs, but not compiled object modules or libraries. |
| --- | --- |

Calls the pre-defined entry point function in an external object module that was loaded using [LoadExternalModule](../../cvi/libref/cviloadexternalmodule.htm).

|  | Note This function is not supported for 64-bit applications. |
| --- | --- |

RunExternalModule requires that the module define the following function:

void _xxx_entry_point (char [])

where xxx is the base name of the file, in lowercase. For example, if the pathname of the file is C:\LW\PROGRAMS\TEST01.OBJ, the name of the entry point must be _test01_entry_point.

##### Example Code

int module_id; 

int status; 

char *pathname; 

pathname = "EXTMOD.OBJ"; 

module_id = LoadExternalModule (pathname); 

if (module_id <0)

FmtOut ("Unable to load %s\n", pathname);

else {

RunExternalModule (module_id, ""); 

UnloadExternalModule (module_id);

}

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| moduleID | int | The value returned by LoadExternalModule. |
| buffer | const char [] | A buffer used to pass information to and from the external module entry point function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | Indicates the result of the operation. Code Description 0 Success. -1 Out of memory. -3 Entry point is undefined. -4 Invalid file format. -5 Undefined references. -8 Cannot open file. -9 Invalid module ID. -25 DLL initialization failed, for example, DLL file not found. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | Out of memory. |  |
| -3 | Entry point is undefined. |  |
| -4 | Invalid file format. |  |
| -5 | Undefined references. |  |
| -8 | Cannot open file. |  |
| -9 | Invalid module ID. |  |
| -25 | DLL initialization failed, for example, DLL file not found. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviscale2d.htm language=enus -->
## TOPIC 00429: Scale2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviscale2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviscale2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Scale2D

*Advanced Analysis Library Only*

AnalysisLibErrType Scale2D (void *inputArray, ssize_t numberOfRows, ssize_t numberOfColumns, void *outputArray, double *offsetValue, double *scalingFactor);

#### Purpose

Scales the input array and returns the scale and offset constants. The scaled output array is in the range [–1 : 1]. Scale2D can obtain 
the (i, j)<sup>th</sup> element of the scaled array using the following formulas:

[IMAGE alt='image' src='scale2da.gif']

[IMAGE alt='image' src='scale1db.gif']

offset = min + scale

where **max** and **min** are the maximum and minimum values in the input array, respectively.

You can use [LinEv2D](../../cvi/libref/cvilinev2d.htm) to reconstruct the input array using the scale and offset constants. Scale2D can perform the operation in place; that is, the input and output arrays can be the same.

The following uses the Scale2D function.

double inputData[10][10], scaledData[10][10]; 

double offset, scalingFactor; 

int i, j, numRows, numCols; 

AnalysisLibErrType status; 
 

numRows = 10; 

numCols = 10; 

/* Use a For loop to generate a 2D array of random numbers between 0.0 and 1.0 */ 

for (j = 0; j < 10; j++)

for (i = 0; i < 10; i++)

inputData[i][j] = Random(0.0, 1.0);

/* Scale inputData and return offset and scaling factor */ 

status = Scale2D(inputData, numRows, numCols, scaledData, &offset, &scalingFactor);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | void * | Input array used as the basis for the scaling operation. This matrix must be an array of doubles. |
| numberOfRows | ssize_t | Number of rows used in the scaling operation. |
| numberOfColumns | ssize_t | Number of columns used in the scaling operation. |
| Output |  |  |
| Name | Type | Description |
| outputArray | void * | Scaled array, as an array of doubles. |
| offsetValue | double | Offsetting constant of the input array. |
| scalingFactor | double | Scaling constant of the input array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviscaledwindowex.htm language=enus -->
## TOPIC 00430: ScaledWindowEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviscaledwindowex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviscaledwindowex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ScaledWindowEx

*Advanced Analysis Library Only*

AnalysisLibErrType ScaledWindowEx (double xArray[], ssize_t numberOfElements, int windowType, double windowParameter, WindowConst *windowConstants);

#### Purpose

ScaledWindowEx

ScaledWindow

ScaledWindowEx

ScaledWindow

This function scales the result so that when the power or amplitude spectrum of the windowed waveform is computed, all windows provide the same level within the accuracy constraints of the window. ScaledWindowEx also returns important window constants for the selected window. These constants are useful when you use functions that perform computations on the power spectrum, such as [PowerFrequencyEstimate](../../cvi/libref/cvipowerfrequencyestimate.htm) and [SpectrumUnitConversion](../../cvi/libref/cvispectrumunitconversion.htm).

If y represents the output sequence **xArray**, the ScaledWindowEx obtains the elements of y using the following equation:

[IMAGE alt='image' src='scaledwindowexform_15.png']

for i = 0, 1, 2, ...

where w<sub>i</sub> and cg are the coefficients and coherent gain of the window without scaling, respectively.

This function also returns the coherent gain (CG) and equivalent noise bandwidth (ENBW) of the selected window. For cosine windows, these two properties are constants, as listed in the following table.

| Window Type | Window Properties |  |
| --- | --- | --- |
| CG | ENBW |  |
| Rectangle | 1.0 | 1.0 |
| Hanning | 0.5 | 1.5 |
| Hamming | 0.54 | 1.362826 |
| Blackman-Harris | 0.42323 | 1.708538 |
| Exact Blackman | 0.42659071367 | 1.693699 |
| Blackman | 0.42 | 1.726757 |
| Flat Top | 0.215578948 | 3.770246506303 |
| 4 Term B-Harris | 0.35875 | 2.004353 |
| 7 Term B-Harris | 0.27105140069342415 | 2.631905 |
| Low Sidelobe | 0.323215218 | 2.215350782519 |
| Blackman Nuttall | 0.3635819 | 1.9761117 |

If **xArray** is an empty input array and the selected window is a cosine window, this function returns the window properties. If **xArray** is an empty input array and the selected window is not a cosine window, this function sets the window properties to NaN and returns an error. For **Triangle**, **Kaiser**, **Dolph-Chebyshev**, and **Gaussian** windows, the window properties depend on the window length and the window parameters.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| numberOfElements | ssize_t | The number of elements in xArray. |
| windowType | int | The type of window to apply. Specify one of the following values: Window Type Constant Value Rectangle RECTANGLE 0 Hanning HANNING 1 Hamming HAMMING 2 Blackman-Harris BLKHARRIS 3 Exact Blackman EXBLKMAN 4 Blackman BLKMAN 5 Flat Top FLATTOP 6 4-Term Blackman-Harris BH4TERM 7 7-Term Blackman-Harris BH7TERM 8 Lowside LB LOWSIDELB 9 Blackman-Nuttall BLKMANNUTTAL 11 Triangle TRIANGLE 30 Barthann BARTHANN 31 Bohman BOHMAN 32 Parzen PARZEN 33 Welch WELCH 34 Kaiser KAISER 60 Dolph-Chebyshev DOLCHEBYSHEV 61 Gaussian GAUSSIAN 62 |
| Window Type | Constant | Value |
| Rectangle | RECTANGLE | 0 |
| Hanning | HANNING | 1 |
| Hamming | HAMMING | 2 |
| Blackman-Harris | BLKHARRIS | 3 |
| Exact Blackman | EXBLKMAN | 4 |
| Blackman | BLKMAN | 5 |
| Flat Top | FLATTOP | 6 |
| 4-Term Blackman-Harris | BH4TERM | 7 |
| 7-Term Blackman-Harris | BH7TERM | 8 |
| Lowside LB | LOWSIDELB | 9 |
| Blackman-Nuttall | BLKMANNUTTAL | 11 |
| Triangle | TRIANGLE | 30 |
| Barthann | BARTHANN | 31 |
| Bohman | BOHMAN | 32 |
| Parzen | PARZEN | 33 |
| Welch | WELCH | 34 |
| Kaiser | KAISER | 60 |
| Dolph-Chebyshev | DOLCHEBYSHEV | 61 |
| Gaussian | GAUSSIAN | 62 |
| windowParameter | double | The window parameter. This parameter is referenced only if windowType is one of the following values: KAISER: windowParameter specifies the beta parameter for a Kaiser window.GAUSSIAN: windowParameter specifies the standard deviation for a Gaussian window. If windowParameter < 0, the function uses 0.2 for windowParameter instead.DOLCHEBYSHEV: windowParameter specifies the ratio of the mainlobe to the sidelobe, in dB, for a Dolph-Chebyshev window. If windowParameter < 0, the function uses 60dB for windowParameter instead. |
| Output |  |  |
| Name | Type | Description |
| xArray | double [] | On input, the input signal. On output, this parameter returns the input signal with the selected window applied. |
| windowConstants | WindowConst | Pointer to a structure that contains the following useful constants for the selected window: enbw is the equivalent noise bandwidth of the selected window. You can use this value to calculate the power in a given frequency span.coherentgain is the peak gain of the window, relative to the peak gain of the Rectangular window. ScaledWindowEx uses this value to normalize peak gains to those of the Rectangular window. WindowConst is defined by the following C typedef statement: typedef struct { double enbw; double coherentgain; } WindowConst; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviscan.htm language=enus -->
## TOPIC 00431: Scan

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviscan.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviscan.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Scan

int Scan (void *source, char formatString[], ...);

#### Purpose

Scans a single source item in memory and breaks it into component parts
according to format specifiers found in a **formatString**. Scan then places the components into the **target** parameter. You can specify up to 29 **target** arguments.

The [Using the Formatting and Scanning Functions](../../cvi/libref/cviusing_the_formatting_and_scannin.htm) section includes a complete discussion of Scan.

|  | Note This function cannot convert "NaN" and "Inf" to equivalent double-precision numbers. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| source | void * | Specifies the data to be scanned and formatted into the target items. Refer to the Using the Formatting and Scanning Functions section for more information. |
| formatString | char [] | Contains format specifiers that appropriately describe the source and target data to be formatted. For the three scan functions, the target specifiers must be provided in the format string. The source specifier may be omitted, in which case the source is assumed to be %s (string). If a source data type other than string is desired, the format string must begin with the specifier of the desired source type, plus the "›" symbol, followed by the target specifiers. For example, the following calls are equivalent: x = Scan (s, "%d", i) x = Scan (s, "%s›%d", i) The following list includes common specifiers: %d Indicates that the source or target is an integer. %i Same as %d. %f Indicates that the source or target is a double–precision real number. %s Indicates that the source or target is a string. You may convert numeric values into ASCII form using the %s target specifier. %10f Indicates that the source or target is an array of ten double–precision real numbers. Because the data formatting functions can describe many complex formatting operations, refer to the Using the Formatting and Scanning Functions section to make sure you are using the proper format specifier for your application. |
| %d | Indicates that the source or target is an integer. |  |
| %i | Same as %d. |  |
| %f | Indicates that the source or target is a double–precision real number. |  |
| %s | Indicates that the source or target is a string. You may convert numeric values into ASCII form using the %s target specifier. |  |
| %10f | Indicates that the source or target is an array of ten double–precision real numbers. |  |
| Output |  |  |
| Name | Type | Description |
| target_s | ... | Specifies the variables in which to store the scanned items. You can specify up to 29 arguments, and you must separate the arguments with commas. Only the value of the first argument is shown at the bottom of the control after you execute the function panel. Refer to the Using the Formatting and Scanning Functions section for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| ItemsFormatted | int | Number of target format specifiers satisfied. To get the number of bytes scanned from the source item, call NumFmtdBytes. If the return value is less than the number of target items, then the source did not contain the exact number and type of items specified in the format string. This function returns –1 to indicate an error in the format string or –2 to indicate an I/O error. |

#### Additional Information

**Library:** [Formatting and I/O Library](../../cvi/libref/cviformatting_and_io_library_functi.htm)

**Include file:** formatio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to analysis\stabilty.cws for an example of using the Scan function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviscanf.htm language=enus -->
## TOPIC 00432: scanf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviscanf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviscanf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### scanf

int scanf (const char formatString[], ...);

#### Purpose

Reads input from standard input and converts it into a series of
values according to the specifications of the formatting string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| formatString | const char [] | Contains the format string that specifies the admissible input sequences and how they are converted for assignment. Use standard ANSI C format specifiers. If insufficient arguments exist for the format, the behavior is undefined. If the format is exhausted while arguments remain, the excess arguments are evaluated but are otherwise ignored. Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |
|  | Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |  |
| Output |  |  |
| Name | Type | Description |
| target_s | ... | Contains a pointer to the variable that receives the converted input from the standard input. If there are multiple arguments, you must separate the arguments by commas. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| ItemsFormatted | int | Contains the number of parameters successfully matched and formatted or EOF (-1) in case of an invalid input. This value might be less than the number of parameters you pass in for matching in the following cases: The input or the format string contains fewer elements than parameters passed in. The function could not match one of the parameters. If an error occurs, this function sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\standardio.cws for an example of using the scanf function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviscanfile.htm language=enus -->
## TOPIC 00433: ScanFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviscanfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviscanfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ScanFile

int ScanFile (int fileHandle, char formatString[], ...);

#### Purpose

Scans source data from the file you specify in the **fileHandle** parameter and breaks the data into component parts according to format specifiers you specify in **formatString**. ScanFile then places the components into the **target** parameter. You can specify up to 29 **target** arguments.

The amount of data ScanFile reads from the file depends on the amount needed to fulfill the target format specifiers in the format string. The [Using the Formatting and Scanning Functions](../../cvi/libref/cviusing_the_formatting_and_scannin.htm) section includes a complete discussion of ScanFile.

|  | Note This function cannot convert NaN and Inf in ASCII files to double-precision numbers. This function can convert these special double-precision numbers in binary files. If your data contains these special double-precision numbers, National Instruments recommends using files in binary format with this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileHandle | int | Specifies which file to read the data from. This is the value that OpenFile originally returned or 0. If the value is 0, ScanFile reads data from the Standard I/O window. Refer to the Using the Formatting and Scanning Functions section for more information. |
| formatString | char [] | Contains format specifiers that appropriately describe the source and target data to be formatted. For the three scan functions, the target specifiers must be provided in the format string. The source specifier may be omitted, in which case the source is assumed to be %s (string). If a source data type other than string is desired, the format string must begin with the specifier of the desired source type, plus the "›" symbol, followed by the target specifiers. For example, the following calls are equivalent: x = Scan (s, "%d", i) x = Scan (s, "%s›%d", i) The following list includes common specifiers: %d Indicates that the source or target is an integer. %i Same as %d. %f Indicates that the source or target is a double–precision real number. %s Indicates that the source or target is a string. You may convert numeric values into ASCII form using the %s target specifier. %10f Indicates that the source or target is an array of ten double–precision real numbers. Because the data formatting functions can describe many complex formatting operations, refer to the Using the Formatting and Scanning Functions section to make sure you are using the proper format specifier for your application. |
| %d | Indicates that the source or target is an integer. |  |
| %i | Same as %d. |  |
| %f | Indicates that the source or target is a double–precision real number. |  |
| %s | Indicates that the source or target is a string. You may convert numeric values into ASCII form using the %s target specifier. |  |
| %10f | Indicates that the source or target is an array of ten double–precision real numbers. |  |
| Output |  |  |
| Name | Type | Description |
| target_s | ... | Specifies the variables in which to store the scanned items. You can specify up to 29 arguments, and you must separate the arguments with commas. Only the value of the first argument is shown at the bottom of the control after you execute the function panel. Refer to the Using the Formatting and Scanning Functions section for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| ItemsFormatted | int | Number of target format specifiers satisfied. To get the number of bytes scanned from the file, call NumFmtdBytes. If the return value is less than the number of target items, then the source did not contain the exact number and type of items specified in the format string. This function returns –1 to indicate an error in the format string or –2 to indicate an I/O error. If this value is –2, you can use GetFmtIOError to get more information about the type of error that occurred. |

#### Additional Information

**Library:** [Formatting and I/O Library](../../cvi/libref/cviformatting_and_io_library_functi.htm)

**Include file:** formatio.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviserverddewrite.htm language=enus -->
## TOPIC 00434: ServerDDEWrite

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviserverddewrite.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviserverddewrite.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ServerDDEWrite

int ServerDDEWrite (unsigned int conversationHandle, char itemName[], unsigned int dataFormat, void *dataPointer, size_t dataSize, unsigned int timeOut);

#### Purpose

Allows your program, acting as a DDE server, to write data to a DDE client application when the client requests data.

Call this function only when your **serverCallbackFunction** receives a DDE_REQUESTDATA message. If you call the function at any other time, ServerDDEWrite stores the data until the client requests the data. If you call the function multiple times on the same conversation before the client requests the data, ServerDDEWrite appends each new data set to the buffer that contains the stored data.

If the client has a hot or warm link and you need to send data other than in response to a DDE_REQUESTDATA message, use [AdviseDDEDataReady](../../cvi/libref/cviadviseddedataready.htm) or [BroadcastDDEDataReady](../../cvi/libref/cvibroadcastddedataready.htm).

If successful, ServerDDEWrite returns the number of bytes written. Otherwise, ServerDDEWrite returns a negative [error code](../../cvi/libref/cvidde_library_error_conditions.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| conversationHandle | unsigned int | The conversation handle that uniquely represents the connection between the server and the client. |
| itemName | char [] | The name that uniquely identifies the object to which the data refers; for example, an Excel cell name. Each server defines its own set of valid item names. The name must be a string of length from 1 to 255. itemName is case insensitive. |
| dataFormat | unsigned int | One of the data formats Microsoft Windows recognizes. Windows supports the following valid data formats: CF_TEXT CF_BITMAP CF_METAFILEPICT CF_SYLK CF_DIF CF_TIFF CF_OEMTEXT CF_DIB CF_PALETTE CF_PENDATA CF_RIFF CF_WAVE CF_OWNERDISPLAY CF_DSPTEXT CF_DSPBITMAP CF_DSPMETAFILEPICT Refer to www.msdn.com for more information about DDE programming and the meaning of each data format type. |
| dataPointer | void * | The pointer to the data to be written. NULL is not allowed unless dataSize is zero. |
| dataSize | size_t | The number of bytes to write. An error is returned if you pass a value greater than INT_MAX. |
| timeOut | unsigned int | The number of milliseconds to wait for a DDE read or write operation to complete. If a value of zero is passed, then a default timeout of 5000 milliseconds is used. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number represents the error code. For functions that read or write data (ClientDDERead, ClientDDEWrite, ServerDDEWrite, AdviseDDEDataReady, BroadcastDDEDataReady), if the function was successful, the return value is the number of bytes transferred. For other DDE Support Library functions, zero represents successful execution. The enumerated type that specifies the absolute values of the error codes is declared in ddesupp.h. For instance, if an invalid parameter is passed, –kDDE_InvalidParameter is returned. Currently, a maximum of 255 concurrent conversations are allowed at any one time. If you exceed this limit, –kDDE_TooManyConversations will be returned. Error codes from –16 to –33 are native DDEML errors, which correspond to Windows DDE error codes starting from 0x4000. |

#### Additional Information

**Library:** [DDE Support Library](../../cvi/libref/cvidde_library_function_tree.htm)

**Include file:** ddesupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviservertcpread.htm language=enus -->
## TOPIC 00435: ServerTCPRead

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviservertcpread.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviservertcpread.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ServerTCPRead

int ServerTCPRead (unsigned int conversationHandle, void *dataBuffer, size_t dataSize, unsigned int timeOut);

#### Purpose

Allows your program, acting as a [TCP server](../../cvi/libref/cvitcp_clients_and_servers.htm), to read data from a client.

The function waits until data is available at the port or until the specified interval expires.

|  | Note If the function call is successful the return value is the number of bytes read. It is possible that TCP is not able to read all the data in one call. If necessary, you can check the number of bytes read and call this function repeatedly to read the rest of the data as shown in the following example: |
| --- | --- |

##### Example Code

char * buffer; 

 int messageSize; 

 int bytesToRead; 

 int bytesRead;

/* Find messageSize and allocate buffer appropriately... */

bytesToRead = messageSize;

while (bytesToRead > 0)

{

bytesRead = ServerTCPRead (conversationHandle, &buffer[messageSize - bytesToRead], bytesToRead, 0);

bytesToRead -= bytesRead;

}

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| conversationHandle | unsigned int | The conversation handle that uniquely represents the connection between the server and the client. |
| dataBuffer | void * | The pointer to the buffer in which to store the data. NULL is not allowed. |
| dataSize | size_t | The maximum number of bytes to read. dataSize must be less than or equal to the size of dataBuffer. This function returns an error if you pass a value greater than UINT_MAX. |
| timeOut | unsigned int | Number of milliseconds that ServerTCPRead waits for data to be available on the connection. ServerTCPRead returns as soon as it reads some data from the connection. The function waits the entire timeout period only if no data is available. If you pass zero, the function uses a default timeout of 5,000 milliseconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. You can call the GetTCPSystemErrorString function to obtain a system message that describes the error. The system messages can be more descriptive than the TCP Support Library error codes. To obtain the correct system error message, you must call GetTCPSystemErrorString immediately after calling the TCP Support Library function that failed. For RegisterTCPServer and RegisterTCPServerEx, the return value is the port number assigned by the system if you passed zero for the port and the function was successful. For functions that read or write data (ClientTCPRead, ClientTCPWrite, ServerTCPRead, ServerTCPWrite), if the function was successful, the return value is the number of bytes transferred. You can have a maximum of 255 concurrent conversations and up to 1,024 connections. If you exceed this limit, -kTCP_TooManyConnections will be returned. You may not be able to open the maximum number of connections allowed by LabWindows/CVI because of limitations imposed by the operating system. |

#### Additional Information

**Library:** [TCP Support Library](../../cvi/libref/cvitcp_library_function_tree.htm)

**Include file:** tcpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to tcp\MultiClientServer.cws for an example of using the ServerTCPRead function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisetcomtime.htm language=enus -->
## TOPIC 00436: SetComTime

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisetcomtime.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisetcomtime.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetComTime

int SetComTime (int portNumber, double timeout_seconds);

#### Purpose

Sets timeout limit for input/output operations.

For read operations, timeout occurs when the COM port input queue is empty and no byte is read into the queue for the duration of the timeout time.

For write operations, timeout occurs when the COM port output queue is full and LabWindows/CVI cannot write to the queue for the duration of the timeout time.

SetComTime returns an error if you have not opened the port or if you pass an invalid parameter value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| portNumber | int | A number that indicates the COM port on which to operate. This number maps to the COM port specified by deviceName in the call to OpenCom or OpenComConfig. The portNumber 1, for example, may not necessarily map to COM1. (Linux) The portNumber 1, for example, may not necessarily map to /dev/ttyS0. Valid Range: 1—1,000 |
| timeout_seconds | double | The timeout limit for I/O operations for the selected port. For an RS-232 read operation, timeoutSeconds specifies the time the library allows from the start of the transfer to the arrival of the first byte. timeoutSeconds also specifies the time the library allows to elapse between the arrival of any two consecutive bytes. An RS-232 read operation waits for at least the amount of time you specify for the next incoming byte before it returns a timeout error. For an RS-232 write operation, timeoutSeconds specifies the time the library allows before the first byte is transferred to the output queue. timeoutSeconds also specifies the time the library allows between the transfer of any two consecutive bytes to the output queue. The transfer of bytes to the output queue can stall if the output queue is full and hardware or software handshaking is held off. If the holdoff is not resolved within the timeout period, the RS-232 write operation returns a timeout error. If timeoutSeconds is zero, timeouts are disabled, and the read or write functions wait indefinitely for the operation to complete. The default value is 5 seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int | The result of this function call. This code is a negative value that specifies the type of error that occurred. |

#### Additional Information

**Library:** [RS-232 Library](../../cvi/libref/cvirs232_library_function_tree.htm)

**Include file:** rs232.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to rs232\serial.cws for an example of using the SetComTime function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisetenableresourcetracking.htm language=enus -->
## TOPIC 00437: SetEnableResourceTracking

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisetenableresourcetracking.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisetenableresourcetracking.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetEnableResourceTracking

int SetEnableResourceTracking (int newState);

#### Purpose

Enables and disables [resource tracking](../../cvi/usermanual/prjwindowrestracking.htm)resource tracking in the current thread.

|  | Note This function is available only in the LabWindows/CVI Full Development SystemLabWindows/CVI Full Development System. |
| --- | --- |

Resource tracking is available at both the extended and standard debugging levels. When you enable resource tracking, LabWindows/CVI tracks resources such as memory blocks, file handles, and panel handles that you allocate in your program. Selecting **Extended** as the **Debugging level** in the **Debugging Options** section of the [Build Options](../../cvi/usermanual/prjbuildopt.htm)Build Options dialog box enables resource tracking by default. LabWindows/CVI displays currently allocated and recently released resources in the [Resource Tracking](../../cvi/usermanual/prjwindowrestracking.htm)Resource Tracking window. If you select **Standard** as the **Debugging level** in the Build Options dialog box, you must use this function to enable resource tracking. You also can use the [GetEnabledResourceTracking](../../cvi/libref/cvigetenableresourcetracking.htm) function to detect whether resource tracking is enabled.

|  | Note (RT) On RT targets, leaked resources persist until you reboot the target. However, the Resource Tracking window displays only leaked resources from the most recent program execution. |
| --- | --- |

Display the Resource Tracking window by selecting **Resource Tracking** in the **Window** menu.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newState | int | Specifies the new resource tracking state. Specify a nonzero value or select Enabled in the function panel to enable resource tracking. Specify 0 or select Disable in the function panel to disable resource tracking. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| previousState | int | Indicates if resource tracking was enabled previously. Code Description 1 Previously enabled. 0 Previously disabled or not available. |
| Code | Description |  |
| 1 | Previously enabled. |  |
| 0 | Previously disabled or not available. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisetfileattrs.htm language=enus -->
## TOPIC 00438: SetFileAttrs

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisetfileattrs.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisetfileattrs.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetFileAttrs

int SetFileAttrs (char fileName[], int readOnly, int system, int hidden, int archive);

#### Purpose

Sets the **readOnly**, **system**, **hidden**, and **archive** attributes of a file.

(Linux) This function sets only the **readOnly** parameter. Other parameters are ignored.

The **readOnly** attribute prevents a file from being overwritten and prevents a file with the same name from being created.

The **system** attribute and **hidden** attribute prevent the file from appearing in a directory list and exclude the file from normal searches.

The **archive** attribute is set whenever the file is modified. The DOS backup command clears the **archive** attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileName | char [] | The pathname of the file for which to get the attributes. If you specify an empty string "", SetFileAttrs uses the file found by the most recent call to GetFirstFile or GetNextFile. |
| readOnly | int | The state of the readOnly attribute. Values 1—Sets the attribute. 0—Clears the attribute. -1—Leaves the attribute unchanged. |
| system | int | The state of the system attribute. Values 1—Sets the attribute. 0—Clears the attribute. -1—Leaves the attribute unchanged. |
| hidden | int | The state of the hidden attribute. Values 1—Sets the attribute. 0—Clears the attribute. -1—Leaves the attribute unchanged. |
| archive | int | The state of the archive attribute. Values 1—Sets the attribute. 0—Clears the attribute. -1—Leaves the attribute unchanged. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -1 File not found, or attribute cannot be changed. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | File not found, or attribute cannot be changed. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisetstdiowindowvisibility.htm language=enus -->
## TOPIC 00439: SetStdioWindowVisibility

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisetstdiowindowvisibility.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisetstdiowindowvisibility.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetStdioWindowVisibility

void SetStdioWindowVisibility (int visible);

#### Purpose

This function either brings to the foreground or hides the console window.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| visible | int | 1 = bring to foreground 0 = hide |

#### Return Value

None.

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\standardio.cws for an example of using the SetStdioWindowVisibility function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisetsystemdate.htm language=enus -->
## TOPIC 00440: SetSystemDate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisetsystemdate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisetsystemdate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetSystemDate

int SetSystemDate (int month, int day, int year);

#### Purpose

Sets the system date.

(Linux) This function is not supported.

|  | Note You must have system administrator status to use this function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| month | int | The month in local calendar time. Valid values are 1 (January) to 12 (December). |
| day | int | The date of the month in local calendar time. Valid values are 1 to 31. |
| year | int | The year in local calendar time. Values before the year 1970 are not supported on Linux or in applications running on an RT target. Values before the year 1601 are not supported on Windows operating systems. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | int | The result of the call. Code Description 0 Success. -1 Operating system reported failure. |
| Code | Description |  |
| 0 | Success. |  |
| -1 | Operating system reported failure. |  |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisetupddewarmlink.htm language=enus -->
## TOPIC 00441: SetUpDDEWarmLink

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisetupddewarmlink.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisetupddewarmlink.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetUpDDEWarmLink

int SetUpDDEWarmLink (unsigned int conversationHandle, char itemName[], unsigned int dataFormat, unsigned int timeOut);

#### Purpose

Allows your program, acting as a DDE client, to set up a warm link with the server. The warm link applies to the data object specified in **itemName**. If the server grants the request for the warm link, the server notifies your program whenever the value of the data object changes. When this notification is received, your client callback function is invoked with a DDE_DATAREADY message.

|  | Note The DDE Support Library makes no distinction between warm links and hot links. In both cases, the data is received immediately through the client callback function. |
| --- | --- |

SetUpDDEWarmLink returns zero for success or a negative [error code](../../cvi/libref/cvidde_library_error_conditions.htm) for failure.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| conversationHandle | unsigned int | The conversation handle that uniquely represents the connection between the server and the client. |
| itemName | char [] | The name identifying the data object for which the warm link is being requested. The server defines the set of valid item names. The name must be a string of length from 1 to 255. itemName is case insensitive. Whenever the value of the data object is modified at the server site, your client callback function is called with a DDE_DATAREADY message. itemName identifies the information in the server application to which the DDE link applies. For example, the item name can represent an Excel range of cells by using the range description R1C1:R10C10. Note To the client, LabWindows/CVI does not distinguish between a hot link and a warm link. For both types of links, the DDE Support Library calls the client callback function with a DDE_DATAREADY message when the data item changes at the server site. The new data is available in the dataPtr parameter of the callback function. LabWindows/CVI has two different functions for setting up a warm link or hot link in case some applications accept only one or the other kind of link. |
|  | Note To the client, LabWindows/CVI does not distinguish between a hot link and a warm link. For both types of links, the DDE Support Library calls the client callback function with a DDE_DATAREADY message when the data item changes at the server site. The new data is available in the dataPtr parameter of the callback function. LabWindows/CVI has two different functions for setting up a warm link or hot link in case some applications accept only one or the other kind of link. |  |
| dataFormat | unsigned int | One of the data formats Microsoft Windows recognizes. Windows supports the following valid data formats: CF_TEXT CF_BITMAP CF_METAFILEPICT CF_SYLK CF_DIF CF_TIFF CF_OEMTEXT CF_DIB CF_PALETTE CF_PENDATA CF_RIFF CF_WAVE CF_OWNERDISPLAY CF_DSPTEXT CF_DSPBITMAP CF_DSPMETAFILEPICT Refer to www.msdn.com for more information about DDE programming and the meaning of each data format type. |
| timeOut | unsigned int | The number of milliseconds to wait for a DDE read or write operation to complete. If a value of zero is passed, then a default timeout of 5000 milliseconds is used. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number represents the error code. For functions that read or write data (ClientDDERead, ClientDDEWrite, ServerDDEWrite, AdviseDDEDataReady, BroadcastDDEDataReady), if the function was successful, the return value is the number of bytes transferred. For other DDE Support Library functions, zero represents successful execution. The enumerated type that specifies the absolute values of the error codes is declared in ddesupp.h. For instance, if an invalid parameter is passed, –kDDE_InvalidParameter is returned. Currently, a maximum of 255 concurrent conversations are allowed at any one time. If you exceed this limit, –kDDE_TooManyConversations will be returned. Error codes from –16 to –33 are native DDEML errors, which correspond to Windows DDE error codes starting from 0x4000. |

#### Additional Information

**Library:** [DDE Support Library](../../cvi/libref/cvidde_library_function_tree.htm)

**Include file:** ddesupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisetvbuf.htm language=enus -->
## TOPIC 00442: setvbuf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisetvbuf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisetvbuf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### setvbuf

int setvbuf (FILE *stream, char buffer[], int bufferingMode, size_t bufferSize);

#### Purpose

Specifies how to buffer the I/O stream. The mode of the stream can be set to full buffering, line buffering, or no
buffering. If no buffer is specified, the system dynamically allocates one.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stream | FILE * | Contains a pointer to the stream that has its buffering mode specified. This stream must be associated with an open file with no operations performed on it for the function to work correctly. |
| bufferingMode | int | Specifies the desired buffering mode for the stream. The following gives a description of the selections available: Mode Value (int) Description Full _IOFBF (2) Causes I/O to be fully buffered. Read and write operations involving a small number of bytes go through an in-memory buffer. The buffer is flushed only if it is full, if fflush is called, or if an input operation is completing. Buffering can significantly reduce execution time over multiple I/O operations. Line _IOLBF (1) Causes I/O to be line buffered. This is the same as full buffering except that the buffer is flushed when a newline character is written. None _IONBF (0) Causes I/O to be unbuffered. Each read or write operation acts directly on the file. If each operation involves only a small number of bytes, multiple operations can be very slow. |
| Mode | Value (int) | Description |
| Full | _IOFBF (2) | Causes I/O to be fully buffered. Read and write operations involving a small number of bytes go through an in-memory buffer. The buffer is flushed only if it is full, if fflush is called, or if an input operation is completing. Buffering can significantly reduce execution time over multiple I/O operations. |
| Line | _IOLBF (1) | Causes I/O to be line buffered. This is the same as full buffering except that the buffer is flushed when a newline character is written. |
| None | _IONBF (0) | Causes I/O to be unbuffered. Each read or write operation acts directly on the file. If each operation involves only a small number of bytes, multiple operations can be very slow. |
| bufferSize | size_t | Contains the size of the buffer that is used for the specified stream. If the input to buffer is not NULL, the value input to this parameter must be less than or equal to the number of bytes in the specified buffer. |
| Output |  |  |
| Name | Type | Description |
| buffer | char [] | Contains a pointer to the I/O buffer that is used. If NULL is entered into this parameter, this function dynamically allocates the specified size. The contents of this buffer at any time are indeterminate. Note This array must be declared with at least as many elements as specified in the bufferSize parameter. |
|  | Note This array must be declared with at least as many elements as specified in the bufferSize parameter. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Contains the resulting status of the function. If successful, setvbuf returns 0. If an error occurs, setvbuf returns a nonzero value and sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisscanf.htm language=enus -->
## TOPIC 00443: sscanf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisscanf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisscanf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### sscanf

int sscanf (const char sourceString[], const char formatString[], ...);

#### Purpose

Converts input from the specified source string into a series of values according to the specifiers in **formatString**.
If copying takes place between objects that overlap, the behavior is undefined.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceString | const char [] | Contains a pointer to the string that the input to be converted is obtained from. |
| formatString | const char [] | Contains the format string that specifies the admissible input sequences and how they are converted for assignment. Use standard ANSI C format specifiers. If insufficient arguments exist for the format, the behavior is undefined. If the format is exhausted while arguments remain, the excess arguments are evaluated but are otherwise ignored. Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |
|  | Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |  |
| Output |  |  |
| Name | Type | Description |
| target_s | ... | Contains a pointer to the object that receives the converted input from the source string. If there are multiple arguments, you must separate the arguments by commas. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| ItemsFormatted | int | Contains the number of parameters successfully matched and formatted or EOF (-1) in case of an invalid input. This value might be less than the number of parameters you pass in for matching in the following cases: The input or the format string contains fewer elements than parameters passed in. The function could not match one of the parameters. If an error occurs, this function sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the sscanf function:

- dll\basic\cvidll.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\colview.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistatelevels.htm language=enus -->
## TOPIC 00444: StateLevels

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistatelevels.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistatelevels.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### StateLevels

*Advanced Analysis Library Only*

AnalysisLibErrType StateLevels (double waveform[], ssize_t waveformSize, int method, ssize_t histogramBins, double *highStateLevel, double *lowStateLevel, double *amplitude);

#### Purpose

Calculates the high state level, low state level, and amplitude of a waveform.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| waveform | double [] | The waveform to measure. |
| waveformSize | ssize_t | The size of waveform x. |
| method | int | The method used to determine the high and low state levels of a waveform. Histogram method - Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. Peak method - Searches the entire waveform for its maximum and minimum levels. Auto Select method - Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabWindows/CVI returns those results. Otherwise, LabWindows/CVI uses the Peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and preshoot) or a triangle wave (where a histogram fails). |
| histogramBins | ssize_t | The number of bins in the Histogram method that LabWindows/CVI uses to determine the high and low state levels of the waveform. LabWindows/CVI ignores histogramBins if you select Peak method as method. |
| Output |  |  |
| Name | Type | Description |
| highStateLevel | double | The high state level of the waveform according to the method. |
| lowStateLevel | double | The low state level of the waveform according to the method. |
| amplitude | double | The amplitude of the waveform according to the method. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistddev.htm language=enus -->
## TOPIC 00445: StdDev

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistddev.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistddev.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### StdDev

AnalysisLibErrType StdDev (double inputArray[], ssize_t numberOfElements, double *mean, double *standardDeviation);

#### Purpose

Calculates the standard deviation and the mean, or average, values of the
input array. StdDev uses the following formulas to find the mean and the standard deviation:

[IMAGE alt='image' src='stddev.gif']

[IMAGE alt='image' src='stddev2.gif']

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Input array from which the mean and the standard deviation are determined. |
| numberOfElements | ssize_t | Number of elements used to find the mean and the standard deviation. |
| Output |  |  |
| Name | Type | Description |
| mean | double | Mean value of the input array. |
| standardDeviation | double | Standard deviation of the input array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Analysis Library](../../cvi/libref/cvianalysis_library.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to analysis\stats.cws for an example of using the StdDev function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistirling.htm language=enus -->
## TOPIC 00446: Stirling

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistirling.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistirling.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Stirling

*Advanced Analysis Library Only*

double Stirling (double x);

#### Purpose

Computes the Stirling approximation to the gamma function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | The point at which the function is evaluated. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | The value of the Stirling function evaluated at x. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrchr.htm language=enus -->
## TOPIC 00447: strchr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrchr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrchr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strchr

char *strchr (const char stringToSearch[], int charToFind);

#### Purpose

Locates the first occurrence of the specified character in a string. The terminating ASCII NUL byte is considered to be part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToSearch | const char [] | Contains a pointer to the null terminated string that is searched for the specified character. |
| charToFind | int | Contains the character that is searched for in the specified string. The input to this parameter must be a character with integer value between 0 and 255. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| matchedChar | char * | Contains a pointer to the located character or a NULL pointer if the character does not occur in the string. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the strchr function:

- functionpanels\Customization\SelectColor.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\DigGraphDAQmx.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrcmp.htm language=enus -->
## TOPIC 00448: strcmp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrcmp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrcmp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strcmp

int strcmp (const char string1[], const char string2[]);

#### Purpose

Compares two NUL-terminated strings. The comparison is
based upon the value of the characters in the strings. Each character is
interpreted as an unsigned char. The comparison is case-sensitive.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| string1 | const char [] | Contains a pointer to the string that is compared to string2. |
| string2 | const char [] | Contains a pointer to the string that is compared to string1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| comparisonResult | int | Contains the result of the comparison between the two specified strings. The comparison is based on the value of the characters which are interpreted as unsigned chars in the two strings. The comparison is case-sensitive. The following explains the possible return values: Result Description Positive integer string1 is greater than string2 Zero string1 is equal to string2 Negative integer string1 is less than string2 |
| Result | Description |  |
| Positive integer | string1 is greater than string2 |  |
| Zero | string1 is equal to string2 |  |
| Negative integer | string1 is less than string2 |  |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrcoll.htm language=enus -->
## TOPIC 00449: strcoll

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrcoll.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrcoll.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strcoll

int strcoll (const char string1[], const char string2[]);

#### Purpose

Compares two NUL-terminated strings, both interpreted as appropriate to the LC_COLLATE category of the
current locale. The comparison is based upon the value of the characters in the string which are interpreted as unsigned chars.

|  | Note You can use setlocale to change the locale specifically for strcoll. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| string1 | const char [] | Contains a pointer to the string that is compared to string2. |
| string2 | const char [] | Contains a pointer to the string that is compared to string1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| comparisonResult | int | Contains the result of the comparison between the two specified strings, both interpreted as appropriate to the LC_COLLATE category of the current locale. The comparison is based on the value of the characters, which are interpreted as unsigned char values, in the two strings. The following explains the possible return values: Result Description Positive integer string1 is greater than string2 Zero string1 is equal to string2 Negative integer string1 is less than string2 |
| Result | Description |  |
| Positive integer | string1 is greater than string2 |  |
| Zero | string1 is equal to string2 |  |
| Negative integer | string1 is less than string2 |  |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistring_processing.htm language=enus -->
## TOPIC 00450: String Processing

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistring_processing.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistring_processing.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### String Processing

strcoll is equivalent to the Windows lstrcmp function. strxfrm performs a string copy using strncpy and returns the length of its second argument.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrncmp.htm language=enus -->
## TOPIC 00451: strncmp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrncmp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrncmp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strncmp

int strncmp (const char string1[], const char string2[], size_t maxChars);

#### Purpose

Compares a specified number of characters of two NUL-terminated strings. Characters that follow an ASCII NUL byte are not compared. The comparison is
based upon the value of the characters in the strings interpreted as unsigned chars. The comparison is case-sensitive.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| string1 | const char [] | Contains a pointer to the string that is compared to string2. |
| string2 | const char [] | Contains a pointer to the string that is compared to string1. |
| maxChars | size_t | Specifies the maximum number of characters to compare between the two specified strings. Note Characters that follow an ASCII NUL byte are not compared. |
|  | Note Characters that follow an ASCII NUL byte are not compared. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| comparisonResult | int | Contains the result of the comparison between the two specified strings. The comparison is based on the value of the characters, interpreted as unsigned chars. The comparison is case-sensitive. The following explains the possible return values: Result Description Positive integer string1 is greater than string2 Zero string1 is equal to string2 Negative integer string1 is less than string2 |
| Result | Description |  |
| Positive integer | string1 is greater than string2 |  |
| Zero | string1 is equal to string2 |  |
| Negative integer | string1 is less than string2 |  |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the strncmp function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- functionpanels\Customization\SelectColor.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrrchr.htm language=enus -->
## TOPIC 00452: strrchr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrrchr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrrchr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strrchr

char *strrchr (const char stringToSearch[], int charToFind);

#### Purpose

Locates the last occurrence of the specified character in a string. The terminating ASCII NUL byte is considered
to be part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToSearch | const char [] | Contains a pointer to the NUL-terminated string that is searched for the specified character. |
| charToFind | int | Contains the character for which to search in the specified string. The input to this parameter must be a character with an integer value between 0 and 255. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| matchedChar | char * | Contains a pointer to the located character or a NUL pointer if the character does not occur in the string. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrspn.htm language=enus -->
## TOPIC 00453: strspn

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrspn.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrspn.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strspn

size_t strspn (const char stringToSearch[], const char characterSet[]);

#### Purpose

Locates the position of the first character in a string that is not in a specified set of characters. The return value corresponds to the length of the initial segment
of a string that contains only characters from the specified set.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToSearch | const char [] | Contains a pointer to the string that is searched for a character not in characterSet. |
| characterSet | const char [] | Contains a pointer to the character set containing the characters that are searched for in the specified string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| matchedCharIndex | size_t | Contains the index value of the string corresponding to the first character that does not match any in the specified character set. This value also corresponds to the length of the segment in the string that contains only characters from the character set. If all characters in the string are in the character set, the function returns the index of the terminating ASCII NUL byte. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrstr.htm language=enus -->
## TOPIC 00454: strstr

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrstr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrstr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strstr

char *strstr (const char stringToSearch[], const char substringToFind[]);

#### Purpose

Locates the first occurrence of a sequence of characters excluding the terminating ASCII NUL byte in a string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToSearch | const char [] | Contains a pointer to the string that is searched to locate the specified substring. |
| substringToFind | const char [] | Contains a pointer to the sequence of characters that are searched for in the specified string. The terminating ASCII NUL byte is not included during the search. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| matchedSubstring | char * | Contains a pointer to the matched substring or a NUL pointer if the substring is not found. If substring_toFind has zero length, the function returns string_toSearch. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtod.htm language=enus -->
## TOPIC 00455: strtod

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtod.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtod.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtod

double strtod (const char stringInput[], char **endPointer);

#### Purpose

Converts the initial portion of a string to double representation. The function skips whitespace characters at the beginning of
the string. The conversion stops when a character that cannot be part of a number is reached. strtod obtains a pointer to the
unconverted part of the string. The expected form of the subject sequence is an optional plus or minus sign,
then a nonempty sequence of digits optionally containing a decimal-point character, then an optional exponent part.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringInput | const char [] | Contains a pointer to the character sequence from which a conversion is made. |
| Output |  |  |
| Name | Type | Description |
| endPointer | char * | Contains a pointer to the first character in stringInput that cannot be part of the number converted, provided that NULL is not entered into this parameter. If the subject sequence is empty or does not have the expected form, the value of stringInput is stored in the object pointed to by this parameter, provided that NULL is not entered into this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| convertedValue | double | Contains the converted value, if any. If no conversion is possible, the function returns zero. If the correct value is outside the range of representable values, strtod returns ±HUGE_VAL, according to the sign of the value, and sets errno to ERANGE. If the correct value causes underflow, the function returns zero. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtoimax.htm language=enus -->
## TOPIC 00456: strtoimax

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtoimax.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtoimax.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtoimax

intmax_t strtoimax (const char stringInput[], char **endPointer, int base);

#### Purpose

Converts the initial portion of a string to an intmax_t integer representation with a specified base. Whitespace
characters at the beginning of the string are skipped. The conversion stops when the function reaches a character that cannot be part
of the number. The function obtains a pointer to the unconverted part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringInput | const char [] | A pointer to the character sequence from which a conversion is made. |
| base | int | The value of the radix that is used to make the appropriate conversion. If the base is zero, the expected form of the subject sequence is that of an integer constant. If the value of the base is between 2 and 36, the expected form of the subject sequence is a sequence of letters and digits representing an integer. Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |
|  | Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |  |
| Output |  |  |
| Name | Type | Description |
| endPointer | char * | A pointer to the first character in stringInput that cannot be part of the number converted. If the subject sequence is empty or does not have the expected form, the value of stringInput is stored in the object pointed to by this parameter. Pass NULL if you do not need the remainder. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| convertedValue | intmax_t | The converted value, if any. If no conversion is possible, the function returns zero. If the correct value is outside the range of representable values, strtoimax returns INTMAX_MAX or INTMAX_MIN, according to the sign of the value, and sets errno to ERANGE. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtok.htm language=enus -->
## TOPIC 00457: strtok

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtok.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtok.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtok

char *strtok (char stringToSeparate[], const char setOfDelimiters[]);

#### Purpose

Breaks a string into tokens, which are sequences of contiguous characters separated by one or more characters from the
specified set of delimiters. To find all tokens in a string, you must call strtok in a loop, once for
each token. The first call has the original string as the first argument and is followed by calls with a NULL pointer as their first
arguments. The set of delimiters can vary from call to call. If a character in the delimiter set is found, it is overwritten by an
ASCII NUL byte, which terminates the current token. A pointer to the next character is saved, from which the next search for
a token will start.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringToSeparate | char [] | Contains a pointer to the string that contains the tokens. Any character in this string that matches one found in the specified set of delimiters is overwritten with an ASCII NUL byte. To find all of the tokens in a string, subsequent calls must have NULL entered into this parameter, to continue searching where the last successful function call ended. Note The contents of this string are modified by this function. |
|  | Note The contents of this string are modified by this function. |  |
| setOfDelimiters | const char [] | Contains the set of delimiters that are searched for in the specified string. During a sequence of calls in which all tokens for a string are found, the contents of this set can vary. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentToken | char * | Contains a pointer to the first character of the current token or a NULL pointer if there is no token. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the strtok function:

- udp\DNSResolver.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\timeaxis.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtol.htm language=enus -->
## TOPIC 00458: strtol

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtol.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtol.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtol

long strtol (const char stringInput[], char **endPointer, int base);

#### Purpose

Converts the initial portion of a string to a long int representation with a specified base. Whitespace
characters at the beginning of the string are skipped. The conversion stops when the function reaches a character that cannot be part
of the number. The function obtains a pointer to the unconverted part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringInput | const char [] | Contains a pointer to the character sequence from which a conversion is made. |
| base | int | Contains the value of the radix that is used to make the appropriate conversion. If the base is zero, the expected form of the subject sequence is that of an integer constant. If the value of the base is between 2 and 36, the expected form of the subject sequence is a sequence of letters and digits representing an integer. Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |
|  | Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |  |
| Output |  |  |
| Name | Type | Description |
| endPointer | char * | Contains a pointer to the first character in stringInput that cannot be part of the number converted, provided that NULL is not entered into this parameter. If the subject sequence is empty or does not have the expected form, the value of stringInput is stored in the object pointed to by this parameter, provided that NULL is not entered into this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| convertedValue | long | Contains the converted value, if any. If no conversion can be performed, the function returns zero. If the correct value is outside the range of representable values, strtol returns LONG_MAX or LONG_MIN, according to the sign of the value, and sets errno to ERANGE. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtoll.htm language=enus -->
## TOPIC 00459: strtoll

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtoll.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtoll.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtoll

long long strtoll (const char stringInput[], char **endPointer, int base);

#### Purpose

Converts the initial portion of a string to a long long integer representation with a specified base. Whitespace
characters at the beginning of the string are skipped. The conversion stops when the function reaches a character that cannot be part
of the number. The function obtains a pointer to the unconverted part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringInput | const char [] | A pointer to the character sequence from which a conversion is made. |
| base | int | The value of the radix that is used to make the appropriate conversion. If the base is zero, the expected form of the subject sequence is that of an integer constant. If the value of the base is between 2 and 36, the expected form of the subject sequence is a sequence of letters and digits representing an integer. Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |
|  | Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |  |
| Output |  |  |
| Name | Type | Description |
| endPointer | char * | A pointer to the first character in stringInput that cannot be part of the number converted. If the subject sequence is empty or does not have the expected form, the value of stringInput is stored in the object pointed to by this parameter. Pass NULL if you do not need the remainder. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| convertedValue | long long | The converted value, if any. If no conversion is possible, the function returns zero. If the correct value is outside the range of representable values, strtoll returns LLONG_MAX or LLONG_MIN, according to the sign of the value, and sets errno to ERANGE. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to compiler\c99extensions\c99extensions.cws for an example of using the strtoll function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtoul.htm language=enus -->
## TOPIC 00460: strtoul

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtoul.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtoul.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtoul

unsigned long strtoul (const char stringInput[], char **endPointer, int base);

#### Purpose

Converts the initial portion of a string to an unsigned long int representation with a specified base.
The function skips whitespace characters at the beginning of the string. The conversion stops when the function reaches a character that cannot
be part of the number. The function obtains a pointer to the unconverted part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringInput | const char [] | Contains a pointer to the character sequence from which a conversion is made. |
| base | int | Contains the value of the radix that is used to make the appropriate conversion. If the base is zero, the expected form of the subject sequence is that of an integer constant. If the value of the base is between 2 and 36, the expected form of the subject sequence is a sequence of letters and digits representing an integer. Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |
|  | Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |  |
| Output |  |  |
| Name | Type | Description |
| endPointer | char * | Contains a pointer to the first character in stringInput that cannot be part of the number converted, provided that NULL is not entered into this parameter. If the subject sequence is empty or does not have the expected form, the value of stringInput is stored in the object pointed to by this parameter, provided that NULL is not entered into this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| convertedValue | unsigned long | Contains the converted value, if any. If no conversion is possible, the function returns zero. If the correct value is outside the range of representable values, strtoul returns ULONG_MAX and sets errno to ERANGE. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to functionpanels\Customization\SelectColor.cws for an example of using the strtoul function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtoull.htm language=enus -->
## TOPIC 00461: strtoull

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtoull.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtoull.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtoull

unsigned long long strtoull (const char stringInput[], char **endPointer, int base);

#### Purpose

Converts the initial portion of a string to an unsigned long long integer representation with a specified base.
The function skips whitespace characters at the beginning of the string. The conversion stops when the function reaches a character that cannot
be part of the number. The function obtains a pointer to the unconverted part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringInput | const char [] | A pointer to the character sequence from which a conversion is made. |
| base | int | The value of the radix that is used to make the appropriate conversion. If the base is zero, the expected form of the subject sequence is that of an integer constant. If the value of the base is between 2 and 36, the expected form of the subject sequence is a sequence of letters and digits representing an integer. Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |
|  | Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |  |
| Output |  |  |
| Name | Type | Description |
| endPointer | char * | A pointer to the first character in stringInput that cannot be part of the number converted. If the subject sequence is empty or does not have the expected form, the value of stringInput is stored in the object pointed to by this parameter. Pass NULL if you do not need the remainder. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| convertedValue | unsigned long long | The converted value, if any. If no conversion is possible, the function returns zero. If the correct value is outside the range of representable values, strtoull returns ULLONG_MAX and sets errno to ERANGE. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to compiler\c99extensions\c99extensions.cws for an example of using the strtoull function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvistrtoumax.htm language=enus -->
## TOPIC 00462: strtoumax

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvistrtoumax.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvistrtoumax.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### strtoumax

uintmax_t strtoumax (const char stringInput[], char **endPointer, int base);

#### Purpose

Converts the initial portion of a string to a uintmax_t integer representation with a specified base.
The function skips whitespace characters at the beginning of the string. The conversion stops when the function reaches a character that cannot
be part of the number. The function obtains a pointer to the unconverted part of the string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringInput | const char [] | A pointer to the character sequence from which a conversion is made. |
| base | int | The value of the radix that is used to make the appropriate conversion. If the base is zero, the expected form of the subject sequence is that of an integer constant. If the value of the base is between 2 and 36, the expected form of the subject sequence is a sequence of letters and digits representing an integer. Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |
|  | Note If the value of base is 16, the characters 0x or 0X can precede the sequence to be converted. |  |
| Output |  |  |
| Name | Type | Description |
| endPointer | char * | A pointer to the first character in stringInput that cannot be part of the number converted. If the subject sequence is empty or does not have the expected form, the value of stringInput is stored in the object pointed to by this parameter. Pass NULL if you do not need the remainder. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| convertedValue | uintmax_t | The converted value, if any. If no conversion is possible, the function returns zero. If the correct value is outside the range of representable values, strtoumax returns UINTMAX_MAX and sets errno to ERANGE. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisubtractcvitimeintervals.htm language=enus -->
## TOPIC 00463: SubtractCVITimeIntervals

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisubtractcvitimeintervals.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisubtractcvitimeintervals.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SubtractCVITimeIntervals

int SubtractCVITimeIntervals (CVITimeInterval interval1, CVITimeInterval interval2, CVITimeInterval *result);

#### Purpose

Subtracts two time interval values and returns the resulting time interval value.

Time interval values can be negative values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| interval1 | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |
| interval2 | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |
| Output |  |  |
| Name | Type | Description |
| result | CVITimeInterval | The result of the calculation, as a time interval value in National Instruments Binary Time Format. |

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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisubtractfromcviabsolutetime.htm language=enus -->
## TOPIC 00464: SubtractFromCVIAbsoluteTime

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisubtractfromcviabsolutetime.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisubtractfromcviabsolutetime.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SubtractFromCVIAbsoluteTime

int SubtractFromCVIAbsoluteTime (CVIAbsoluteTime absoluteTime, CVITimeInterval interval, CVIAbsoluteTime *result);

#### Purpose

Subtracts a time interval value from an absolute time value and returns the resulting absolute time value.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| absoluteTime | CVIAbsoluteTime | Absolute time value in National Instruments Binary Time Format. |
| interval | CVITimeInterval | Time interval value in National Instruments Binary Time Format. |
| Output |  |  |
| Name | Type | Description |
| result | CVIAbsoluteTime | The result of the calculation, as an absolute time value in National Instruments Binary Time Format. |

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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisum1d.htm language=enus -->
## TOPIC 00465: Sum1D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisum1d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisum1d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Sum1D

*Advanced Analysis Library Only*

AnalysisLibErrType Sum1D (double inputArray[], ssize_t numberOfElements, double *sum);

#### Purpose

Finds the **sum** of the elements of the input array. Sum1D obtains the **sum** of the elements using the following formula:

[IMAGE alt='image' src='sum1d.gif']

The following example uses the Sum1D function.

double inputData[10]; 

double Sum; 

AnalysisLibErrType status; 
 

// Generate an array of random numbers 

status = Uniform (10, 17, inputData); 
 

status = Sum1D (inputData, 10, &Sum);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | double [] | Input array whose elements are summed. |
| numberOfElements | ssize_t | Number of elements to sum. |
| Output |  |  |
| Name | Type | Description |
| sum | double | Sum of elements of the input array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

#### Example

Refer to analysis\parsevls.cws for an example of using the Sum1D function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisum2d.htm language=enus -->
## TOPIC 00466: Sum2D

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisum2d.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisum2d.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Sum2D

*Advanced Analysis Library Only*

AnalysisLibErrType Sum2D (void *inputArray, ssize_t numberOfRows, ssize_t numberOfColumns, double *sum);

#### Purpose

Finds the **sum** of the elements in the input 2D array. Sum2D obtains the **sum** using the following formula:

[IMAGE alt='image' src='sum2d.gif']

where **i** is the array row index, **j** is the array column index, **numberOfRows** is **numberRows**, and **numberOfColumns** is **numberColumns**.

The following example uses the Sum2D function.

double inputData[10][10]; 

double sum; 

int i, j, numRows, numCols; 

AnalysisLibErrType status; 
 

numRows = 10; 

numCols = 10; 
 

/*/ Use a For loop to generate a 2D array of random numbers between 0.0 and 1.0 */ 

for (j = 0; j < 10; j++)

for (i = 0; i < 10; i++)

inputData[i][j] = Random(0.0, 1.0);

status = Sum2D(inputData, numRows, numCols, &sum);

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputArray | void * | Input array whose elements are summed. This matrix must be an array of doubles. |
| numberOfRows | ssize_t | Number of rows used in generating the sum of elements. |
| numberOfColumns | ssize_t | Number of columns used in generating the sum of elements. |
| Output |  |  |
| Name | Type | Description |
| sum | double | Sum of the elements of the input array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisymeigenvaluevector.htm language=enus -->
## TOPIC 00467: SymEigenValueVector

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisymeigenvaluevector.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisymeigenvaluevector.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SymEigenValueVector

*Advanced Analysis Library Only*

AnalysisLibErrType SymEigenValueVector (void *inputMatrix, ssize_t matrixSize, int outputChoice, double eigenvalues[], void *eigenvectors);

#### Purpose

Calculates the eigenvalues λ and the corresponding eigenvectors x of a real, symmetric square input matrix A. The following formula defines the eigenvalues and the corresponding eigenvectors:

Ax = λx

The eigenvalues and the eigenvectors are all real-valued.

The **outputChoice** parameter determines what to calculate. Depending on your application, you can choose to calculate just the eigenvalues or to calculate both the eigenvalues and the eigenvectors.

The **eigenValues** output parameter is a 1D, real array of **matrixSize** elements.

The **eigenVectors** output parameter is a **matrixSize**-by-**matrixSize** real matrix (2D array). Each i<sup>th</sup> column of this matrix is the eigenvector that corresponds to the i<sup>th</sup> component of the **eigenValues**. Each eigenvector is normalized so that its largest component equals one.

The function does not check the symmetry of the input matrix. To use the function correctly, you must ensure the input matrix is symmetric.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputMatrix | void * | Input symmetric square matrix. |
| matrixSize | ssize_t | Number of elements in one dimension of the input matrix. |
| outputChoice | int | Specifies if the function computes eigenvectors. Pass one of the following values: 0: compute only the eigenvalues of inputMatrix.1: compute both eigenvalues and eigenvectors of inputMatrix. |
| Output |  |  |
| Name | Type | Description |
| eigenvalues | double [] | Resulting eigenvalues of the input matrix. |
| eigenvectors | void * | Resulting eigenvectors of the input matrix, as an array of doubles. If outputChoice is eigenvalues only, you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvisystemhelp.htm language=enus -->
## TOPIC 00468: SystemHelp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvisystemhelp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvisystemhelp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SystemHelp

int SystemHelp (char helpFile[], unsigned int command, unsigned long additionalLongData, char additionalStringData[]);

#### Purpose

|  | Note The Windows Help viewer (winhelp.exe) is not included Windows. Use the ShowHtmlHelp function to launch a Windows HTML help file. |
| --- | --- |

Starts Windows Help, winhelp.exe, on a specified help file.

You can pass optional data that indicates the nature of the help you want to display.

For information about creating help files, refer to www.msdn.com.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| helpFile | char [] | The string containing the name of the help file you want to display. The pathname can be followed by an angle bracket (>) and the name of a secondary window if you want the topic to appear in a secondary window rather than in the primary window. The [WINDOWS] section of the help project (.hpj) file must define the name of the secondary window. |
| command | unsigned int | The type of help you want to display. You can specify the following values: HELP_COMMAND—Executes a help macro or macro string. In this case, additionalStringData is the help macro to execute. HELP_CONTENTS—Displays the help contents topic as defined by the contents option in the [OPTIONS] section of the .hpj file. HELP_CONTENTS is for backward compatibility. New programs should provide a .cnt file and use the HELP_FINDER command. HELP_CONTEXT—Displays help for a particular topic identified by a context number that has been defined in the [MAP] section of the .hpj file. In this case, additionalLongData is the context number of the topic. HELP_CONTEXTPOPUP—Displays in a pop-up window a particular help topic identified by a context number that has been defined in the [MAP] section of the .hpj file. HELP_CONTEXTPOPUP does not display the main help window. In this case, additionalLongData is the context number of the topic. HELP_FINDER—Displays the Help Topics dialog box. In the Help Topics dialog box, you can select topics to display by viewing the titles of the topics, the keywords associated with the topics, or the words and phrases found in the topics. HELP_HELPONHELP—Displays the contents topic of the Using Help file if it is available. HELP_KEY—Displays the topic in the keyword list that matches the keyword passed in the additionalStringData parameter if one exact match exists. If more than one match exists, HELP_KEY displays the Topics Found dialog box. HELP_PARTIALKEY—Displays the topic found in the keyword list that matches the keyword passed in the additionalStringData parameter if one exact match exists. If more than one match exists, HELP_PARTIALKEY displays the Topics Found dialog box. If you want to display the Index without passing a keyword, pass an empty string (""). HELP_POPUPID—Displays in a pop-up window the topic identified by a context string. HELP_POPUPID does not display the main help window. HELP_QUIT—Closes the help file. HELP_QUIT has no effect if another executable opens the help file. HELP_SETCONTENTS—Determines which Contents topic help appears when the user chooses the Contents button in a help window if the help file does not have an associated .cnt file. If a help file has two or more Contents topics, you must assign one as the default. Call SystemHelp with command set to HELP_SETCONTENTS and the additionalLongData parameter specifying the corresponding context identifier. |
| additionalLongData | unsigned long | Depends on the command parameter. HELP_CONTEXT—The context number of the topic. HELP_CONTEXTPOPUP—The context number of the topic. HELP_SETCONTENTS—The context number of the topic that is to be designated as the Contents topic. |
| additionalStringData | char [] | Depends on the command parameter. HELP_POPUPID—The context string of the topic to be displayed. HELP_KEY—The keyword for the requested topic. HELP_PARTIALKEY—The partial keyword for the requested topic. HELP_COMMAND—The help macro to be executed. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Nonzero on success; zero on failure. |

#### Additional Information

**Library:** [Utility Library](../../cvi/libref/cviutility_library_function_tree.htm)

**Include file:** utility.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitan.htm language=enus -->
## TOPIC 00469: tan

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitan.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitan.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### tan

double tan (double inputValue);

#### Purpose

Computes the tangent of the specified argument. The argument must be measured in radians.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputValue | double | Contains the argument to the function. This value must be measured in radians. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| result | double | Contains the resulting tangent value. This value is valid only if inputValue is measured in radians. The function returns NaN when infinity or an unrepresentable number is used as the argument. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitcp_callback_function.htm language=enus -->
## TOPIC 00470: Using Callback Functions to Respond to TCP Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitcp_callback_function.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitcp_callback_function.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Using Callback Functions to Respond to TCP Events

Callback functions provide the mechanism for receiving notification of connection, connection termination, and data availability. Similar to the method in which a callback function responds to user interface events from User Interface Library object files, a TCP callback function responds to incoming TCP messages and information.

A callback function can respond to three types of TCP messages: TCP_CONNECT, TCP_DISCONNECT, and TCP_DATAREADY.

The parameter prototype for the TCP callback function in LabWindows/CVI is defined as follows:

int CallbackFunction (unsigned handle, int xType, int errCode, void *callbackData);

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | unsigned | Conversation handle. |
| xType | integer | Transaction type. |
| errCode | integer | When xType is TCP_DISCONNECT, errCode is negative if the connection terminates because of an error. |
| callbackData | void pointer | A user-defined data value. |

The following table lists the TCP transaction types, **xType**, that can trigger a callback function.

#### TCP Transaction Types (xType)

| xType | Server Can Respond To? | Client Can Respond To? | Occurs When? |
| --- | --- | --- | --- |
| TCP_CONNECT | Y | N | When a new client requests connection. |
| TCP_DISCONNECT | Y | Y | When a conversation partner quits or when a connection terminates because of an error. If the connection terminates because of an error, the errCode parameter contains a negative error code. |
| TCP_DATAREADY | Y | Y | When a conversation partner sends data. Your program, acting as the server, calls ServerTCPRead to obtain the data. Note that this event is received again if you do not read all the available data. |

|  | Note You must process messages in order to receive events in the callback. A thread processes messages when it calls RunUserInterface, ProcessSystemEvents, GetUserEvent, or any of the built-in User Interface Library pop-up functions. |
| --- | --- |

Refer to [RegisterTCPServer](cviregistertcpserver.htm) and [ConnectToTCPServer](cviconnecttotcpserver.htm) for more information about the TCP callback function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitcp_clients_and_servers.htm language=enus -->
## TOPIC 00471: Building Networked Applications with the LabWindows/CVI TCP Support Library

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitcp_clients_and_servers.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitcp_clients_and_servers.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Building Networked Applications with the LabWindows/CVI TCP Support Library

The Transmission Control Protocol/Internet Protocol (TCP/IP) suite is a set of protocols that govern how data is
transferred between networked computers. TCP/IP is the primary protocol of the Internet, the Web, and many private
networks and local area networks. Networking components rely on TCP transport for many activities, including the
following operations:

- Internet access using HTTP
- Access to remote file servers and printers
- Distributed Component Object Model (DCOM) services

Network communication using the TCP Support Library involves a client and a server in each connection. A TCP server can send and receive information to and from a client application through a network. A TCP client can send and request data to and from a server application. Once registered, a server waits for clients to request connection to it. A client can request connection only to an existing server.

The following image displays the interaction between a TCP server and TCP client application.

[IMAGE alt='image' src='tcpcomm.gif']

With the LabWindows/CVI TCP Support Library, you can write programs to act as a TCP client or server. Two sample programs, samples\tcp\server.cws and samples\tcp\client.cws, provide guidelines for structuring TCP programs as a server or a client. These programs are provided as templates only. You must modify these programs to operate them on your computer.

- server.cws 
 [IMAGE alt='image' src='../libref/open.gif'] Open example
- client.cws 
 [IMAGE alt='image' src='../libref/open.gif'] Open example

To connect to a TCP server from a LabWindows/CVI program, you must have some information about the application to which you would like to connect. All TCP server applications must run on a specified host, which has a known host name, such as aaa.bbb.ccc, or a known IP address, such as 123.456.78.90, associated with it. In addition, each server has a unique port number on the host computer. These two pieces of information identify different servers on the same computer or on different computers. Before any client program can connect to a server, the client must know the host name and server port number.

If you want a program to act as a TCP server, you must call [RegisterTCPServer](cviregistertcpserver.htm) or [RegisterTCPServerEx](cviregistertcpserverex.htm) in the program. These functions establish the program as the server associated with a port number on the local host. Call RegisterTCPServerEx to specify the address of the local host. Client applications can connect to the program by using the port number associated with the server and either the host name or the IP address of the computer on which the server application is currently running. The TCP Support Library calls the server callback function whenever the conversation partner requests communication.

Programs you write using the LabWindows/CVI TCP functions depend on the LabWindows/CVI TCP Support
Library, which is part of the LabWindows/CVI Runtime. The LabWindows/CVI TCP Support Library uses
the Windows Sockets (Winsock) API. Winsock provides direct access to services in the transport layer using the
TCP/IP protocol. TCP establishes a connection for data transmission, and IP defines the method for sending data
packets.

|  | Note You can call the LabWindows/CVI TCP Support Library GetHostTCPSocketHandle function to get the socket handle of a connection and then use the socket handle to call low-level socket functions. You should be familiar with system socket programming if you call low-level socket functions. System socket programming is beyond the scope of this document and is not described here. Refer www.msdn.com for more information about TCP and system socket programming. |
| --- | --- |

The following image displays components and dependencies in a LabWindows/CVI TCP application.

[IMAGE alt='image' src='tcpcomponents.gif']

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitcp_library.htm language=enus -->
## TOPIC 00472: TCP Support Library Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitcp_library.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitcp_library.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TCP Support Library Overview

This section describes the functions in the LabWindows/CVI Transmission
Control Protocol (TCP) Support Library. TCP Support Library functions provide a platform-independent interface to the reliable, connection-oriented, byte-stream, network communication protocol. To access information about each function, you can use the [function tree list](cvitcp_library_function_tree.htm) of TCP Support Library functions or click the function name in the *Library Reference»TCP Support Library»Alphabetical List of Functions* section of this help file.

#### Related Topics

[Building Networked Applications with the LabWindows/CVI TCP Support Library](cvitcp_clients_and_servers.htm) 

[Creating TCP Servers and Clients](creatingserversandclients.htm) 

[Using Callback Functions to Respond to TCP Events](cvitcp_callback_function.htm) 

[Transferring Data with TCP](tcpdatatransfer.htm) 

[Multithreaded TCP Applications](tcpandmultithreading.htm) 

[Writing TCP Applications on Multihomed Hosts](tcp_multihomed.htm) 

[Callback Data](../usermanual/callbackdata.htm) 

[Using LabWindows/CVI with TCP, UDP, and Other Low-Level Communications Applications](usingcommprotocols.htm) 

[TCP Support Library Error Conditions](cvitcp_library_error_conditions.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitcp_library_error_conditions.htm language=enus -->
## TOPIC 00473: TCP Support Library Error Codes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitcp_library_error_conditions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitcp_library_error_conditions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TCP Support Library Error Codes

The [TCP Support Library](cvitcp_clients_and_servers.htm) functions return negative values when they detect errors. TCP uses a common set of error codes and provides end-to-end error detection and correction and reliable data delivery. Specifically, TCP notifies the sender of packet delivery, guarantees that packets are delivered in the same order in which they were sent, retransmits lost packets, and ensures that data packets are not duplicated. TCP uses a checksum on both the headers and data of each segment to help detect network corruption. The following table lists the [error codes](../programmerref/statusreportingbytcplib.htm)error codes, defined constants, and error messages associated with functions in the the LabWindows/CVI TCP Support Library.

Use the [GetTCPErrorString](cvigettcperrorstring.htm) function to convert the error code, returned in the **status** parameter of TCP Support Library functions, into meaningful error messages.

|  | Note Because errors can occur in the underlying Winsock or other operating system components, call GetTCPSystemErrorString to obtain a system message that describes the error. The system messages can be more descriptive than the TCP Support Library error codes. To obtain the correct system error message, you must call GetTCPSystemErrorString immediately after calling the TCP Support Library function that failed. |
| --- | --- |

Error codes are defined in the cvi\include\tcpsupp.h file.

| Value | Code | Error Message |
| --- | --- | --- |
| 0 | -kTCP_NoError | No Error |
| -1 | -kTCP_UnableToRegisterService | Unable to register service |
| -2 | -kTCP_UnableToEstablishConnection | Unable to establish connection |
| -3 | -kTCP_ExistingServer | Existing server |
| -4 | -kTCP_FailedToConnect | Failed to connect |
| -5 | -kTCP_ServerNotRegistered | Server not registered |
| -6 | -kTCP_TooManyConnections | Too many connections |
| -7 | -kTCP_ReadFailed | Read failed |
| -8 | -kTCP_WriteFailed | Write failed |
| -9 | -kTCP_InvalidParameter | Invalid parameter |
| -10 | -kTCP_OutOfMemory | Insufficient memory |
| -11 | -kTCP_TimeOutErr | Timeout error |
| -12 | -kTCP_NoConnectionEstablished | No connection established |
| -13 | -kTCP_GeneralIOErr | General I/O error |
| -14 | -kTCP_ConnectionClosed | Connection closed |
| -15 | -kTCP_UnableToLoadWinsockDLL | Unable to load Winsock DLL |
| -16 | -kTCP_IncorrectWinsockDLLVersion | Incorrect Winsock DLL version |
| -17 | -kTCP_NetworkSubsystemNotReady | Network subsystem not ready |
| -18 | -kTCP_ConnectionsStillOpen | Connections still open |
| -19 | -kTCP_DisconnectPending | Disconnection pending |
| -20 | -kTCP_InfoNotAvailable | Information not available |
| -21 | -kTCP_HostAddressNotFound | Host address was not found |

###### Remarks

You can have a maximum of 255 concurrent conversations and 1,024 connections. If you exceed this limit, LabWindows/CVI returns -kTCP_TooManyConnections. You might not be able to open the maximum number of connections allowed by LabWindows/CVI because of limitations imposed by the operating system.

For functions that read or write data ([ClientTCPRead](cviclienttcpread.htm), [ClientTCPWrite](cviclienttcpwrite.htm), [ServerTCPRead](cviservertcpread.htm), [ServerTCPWrite](cviservertcpwrite.htm)), the return value indicates the number of bytes transferred if the function was successful.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitcp_library_function_tree.htm language=enus -->
## TOPIC 00474: TCP Support Library Function Tree

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitcp_library_function_tree.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitcp_library_function_tree.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Function Tree, TCP Support Library

| Class/Panel Name | Function Name |
| --- | --- |
| Server Functions |  |
| Register TCP Server | RegisterTCPServer |
| Register TCP Server (Extended) | RegisterTCPServerEx |
| Server TCP Read | ServerTCPRead |
| Server TCP Write | ServerTCPWrite |
| Unregister TCP Server | UnregisterTCPServer |
| Unregister TCP Server (Extended) | UnregisterTCPServerEx |
| Disconnect TCP Client | DisconnectTCPClient |
| Client Functions |  |
| Connect To TCP Server | ConnectToTCPServer |
| Connect To TCP Server (Extended) | ConnectToTCPServerEx |
| Client TCP Read | ClientTCPRead |
| Client TCP Write | ClientTCPWrite |
| Disconnect From TCP Server | DisconnectFromTCPServer |
| Support Functions |  |
| Get All Host IP Addresses | GetAllTCPHostAddresses |
| Get Host IP Address | GetTCPHostAddr |
| Get Host Machine Name | GetTCPHostName |
| Get Host Connection Address | GetTCPHostConnectionAddr |
| Get Peer IP Address | GetTCPPeerAddr |
| Get Peer Machine Name | GetTCPPeerName |
| Get System Socket Handle | GetHostTCPSocketHandle |
| Set Disconnect Mode | SetTCPDisconnectMode |
| Get Error String | GetTCPErrorString |
| Get System Error String | GetTCPSystemErrorString |
| Process TCP Events | ProcessTCPEvents |
| Free Memory | TCPFreeMemory |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitcpfreememory.htm language=enus -->
## TOPIC 00475: TCPFreeMemory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitcpfreememory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitcpfreememory.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TCPFreeMemory

void TCPFreeMemory (void *pointerToMemory);

#### Purpose

Frees memory allocated by this library.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointerToMemory | void * | Pointer to memory allocated by this library. |

#### Return Value

None.

#### Additional Information

**Library:** [TCP Support Library](../../cvi/libref/cvitcp_library_function_tree.htm)

**Include file:** tcpsupp.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_addchannelgroup.htm language=enus -->
## TOPIC 00476: TDMS_AddChannelGroup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_addchannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_addchannelgroup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AddChannelGroup

int TDMS_AddChannelGroup (TDMSFileHandle file, const char *name, const char *description, TDMSChannelGroupHandle *channelGroup);

#### Purpose

Adds a new channel group to a file. A valid file should contain one or more channel groups.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The handle of the file that will contain the new channel group. You obtain this handle from the TDMS_OpenFileEx, TDMS_CreateFileEx, TDMS_AdvancedOpenFile, or TDMS_AdvancedCreateFile function. |
| name | const char * | The value of the Name property of the channel group object. This property is stored in the channel group and can be accessed with the TDMS_SetChannelGroupProperty and TDMS_GetChannelGroupProperty functions. |
| description | const char * | The value of the Description property of the channel group object. This property is stored in the channel group and can be accessed with the TDMS_SetChannelGroupProperty and TDMS_GetChannelGroupProperty functions. |
| Output |  |  |
| Name | Type | Description |
| channelGroup | TDMSChannelGroupHandle | The handle for the requested channel group. Pass this handle to other TDM Streaming Library functions that require a channel group. LabWindows/CVI automatically discards this handle when you close the containing file handle with TDMS_CloseFile. To discard the channel group handle explicitly, call the TDMS_CloseChannelGroup function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_AddChannelGroup function:

- TDM Streaming\tdmsWriteBenchmark.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write\TDMS Advanced Async Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write Throughput Test\TDMS Advanced Async Write Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Write\TDMS Advanced Sync Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS In Memory Write and Read\TDMS In Memory Write and Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_advancedasyncread.htm language=enus -->
## TOPIC 00477: TDMS_AdvancedAsyncRead

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_advancedasyncread.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_advancedasyncread.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AdvancedAsyncRead

int TDMS_AdvancedAsyncRead (TDMSFileHandle file, void *samples, size_t numberOfSamples, TDMSDataType dataType, TDMSAsyncReadCallbackPtr callback, void *callbackData, int *readProcessFinished);

#### Purpose

Reads data from the specified .tdms file asynchronously.

This function can issue additional asynchronous reads while executing previously issued asynchronous reads in the background. When the number of asynchronous reads in the background reaches the maximum value, this function waits until a previously issued asynchronous read completes before issuing an additional asynchronous read. If the previously issued asynchronous read does not complete within the timeout value, this function returns error code TDMS_OperationTimedOut. Call [TDMS_ConfigureAsyncReads](../../cvi/libref/cvitdms_configureasyncreads.htm) to configure the maximum number of asynchronous reads and the timeout value.

Call [TDMS_GetAsyncReadStatus](../../cvi/libref/cvitdms_getasyncreadstatus.htm) to query the number of pending asynchronous reads.

(Linux) This function is not supported.

(Real-Time Module) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The file handle. You obtain this handle from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. You must specify the enable asynchronous operations option when you open or create the file. |
| numberOfSamples | size_t | The number of samples to read. Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncReads. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |
|  | Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncReads. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |  |
| dataType | TDMSDataType | The data type of the samples to read. This function does not support reading samples of type string. |
| callback | TDMSAsyncReadCallbackPtr | The function that the library calls when the asynchronous read operation is complete or fails due to an error. The library calls this function asynchronously in a worker thread. The TDM Streaming Library always calls your callbacks in the same order in which you issue the corresponding calls to this function. The function you pass for this parameter must have the following prototype: void CVICALLBACK Callback (TDMSFileHandle file, int error, void *samples, size_t numSamplesRead, void *callbackData); Upon entry to the callback, the file parameter contains the same file handle passed to this function. The error parameter contains an error code value indicating the reason the read operation failed or zero if the read operation succeeded. The samples parameter contains the same array pointer passed to this function. The numSamplesRead parameter contains the number of samples actually read from the file. This value can be less than the numberOfSamples value passed to this function. This happens when the number of samples remaining from the total passed to the totalSamplesToRead parameter of TDMS_ConfigureAsyncReads is less the value of numberOfSamples passed to this function. The callbackData parameter of the callback contains the value you provide in the callbackData parameter of this function. You can use this parameter to pass any additional information you choose. Note Return from this function as soon as possible to avoid blocking other asynchronous operations on the same file. If needed, you can use PostDeferredCallToThread or the Thread Pool functions to process this event in a different thread. From within this callback function, you must also avoid calling any functions in the TDM Streaming Library to perform an operation using the same file or any channel groups or channels within that file. The TDM Streaming Library will return an error in that case in order to prevent a deadlock. |
|  | Note Return from this function as soon as possible to avoid blocking other asynchronous operations on the same file. If needed, you can use PostDeferredCallToThread or the Thread Pool functions to process this event in a different thread. From within this callback function, you must also avoid calling any functions in the TDM Streaming Library to perform an operation using the same file or any channel groups or channels within that file. The TDM Streaming Library will return an error in that case in order to prevent a deadlock. |  |
| callbackData | void * | Specifies a pointer to user-defined data that the TDM Streaming Library will pass to your callback as the callbackData parameter. Do not pass the address of a local variable or any other variable or memory that might not be valid when the callback is executed. If you do not need callback data you can pass NULL for this parameter. |
| Output |  |  |
| Name | Type | Description |
| samples | void * | An array that receives the samples from the specified file. Because the read operation is asynchronous the array will not contain the samples read from the file immediately after this function call returns. Instead you must wait until the asynchronous operation completes before referencing the array contents. You can be notified when the asynchronous operation completes using the callback parameter. This array must be large enough to hold at least the number of samples specified by the numberOfSamples parameter. The type of this array should match the type of the samples you are reading. This function does not support reading samples of type string. If the type of the samples you are reading is TDMS_Timestamp, you must pass an array of type CVIAbsoluteTime. Refer to the Absolute Time functions in the Utility Library for more information about this type. Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this read operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |
|  | Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this read operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |  |
| readProcessFinished | int | Indicates whether this call completes the read operations configured by a corresponding call to TDMS_ConfigureAsyncReads. This value will be zero if additional calls to this function are needed and non-zero if no additional calls are needed. You can use this value to determine when to exit a loop that calls this function on each iteration. The read operations configured by a corresponding call to TDMS_ConfigureAsyncReads are complete if this function reaches the end of the file or finishes reading the number of samples specified by the totalSamplesToRead parameter of TDMS_ConfigureAsyncReads. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_AdvancedAsyncRead function:

- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read\TDMS Advanced Async Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read Throughput Test\TDMS Advanced Async Read Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_advancedasyncwrite.htm language=enus -->
## TOPIC 00478: TDMS_AdvancedAsyncWrite

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_advancedasyncwrite.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_advancedasyncwrite.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AdvancedAsyncWrite

int TDMS_AdvancedAsyncWrite (TDMSFileHandle file, void *samples, size_t numberOfSamples, TDMSDataType dataType, TDMSAsyncWriteCallbackPtr callback, void *callbackData);

#### Purpose

Writes data to the specified .tdms file asynchronously.

This function can issue additional asynchronous writes while executing previously issued asynchronous writes in the background. When the number of asynchronous writes in the background reaches the maximum value, this function waits until a previously issued asynchronous write completes before issuing an additional asynchronous write. If the previously issued asynchronous write does not complete within the timeout value, this function returns error code TDMS_OperationTimedOut. Call [TDMS_ConfigureAsyncWrites](../../cvi/libref/cvitdms_configureasyncwrites.htm) to configure the maximum number of asynchronous writes and the timeout value.

Call [TDMS_GetAsyncWriteStatus](../../cvi/libref/cvitdms_getasyncwritestatus.htm) to query the number of pending asynchronous writes.

(Linux) This function is not supported.

(Real-Time Module) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The file handle. You obtain this handle from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. You must specify the enable asynchronous operations option when you open or create the file. |
| samples | void * | An array containing samples that will be written to the specified file. Because the write operation is asynchronous you cannot modify the array contents or dispose of the array memory immediately after this function call returns. Instead you must wait until the asynchronous operation completes. You can be notified when the asynchronous operation completes using the callback parameter. The type of this array should match the type of the samples you are writing. This function does not support writing samples of type string. If the type of the samples you are writing is TDMS_Timestamp, you must pass an array of type CVIAbsoluteTime. Refer to the Absolute Time functions in the Utility Library for more information about this type. Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this write operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |
|  | Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this write operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |  |
| numberOfSamples | size_t | The number of samples to write. Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncWrites. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |
|  | Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncWrites. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |  |
| dataType | TDMSDataType | The data type of the samples to write. This function does not support writing samples of type string. |
| callback | TDMSAsyncWriteCallbackPtr | The function that the library calls when the asynchronous write operation is complete or fails due to an error. The library calls this function asynchronously in a worker thread. The TDM Streaming library will always call your callbacks in the same order in which you issue the corresponding calls to this function. The function you pass for this parameter must have the following prototype: void CVICALLBACK Callback (TDMSFileHandle file, int error, void *samples, size_t numSamplesWritten, void *callbackData); Upon entry to the callback, the file parameter contains the same file handle passed to this function. The error parameter contains an error code value indicating the reason the write operation failed or zero if the write operation succeeded. The samples parameter contains the same array pointer passed to this function. The numSamplesWritten parameter contains the number of samples written to the file. This will be the same number of samples passed to this function or will be zero if an error occurred. The callbackData parameter of the callback contains the value you provide in the callbackData parameter of this function. You can use this parameter to pass any additional information you choose. Note Return from this function as soon as possible to avoid blocking other asynchronous operations on the same file. If needed, you can use PostDeferredCallToThread or the Thread Pool functions to process this event in a different thread. From within this callback function, you must also avoid calling any functions in the TDM Streaming Library to perform an operation using the same file or any channel groups or channels within that file. The TDM Streaming Library will return an error in that case in order to prevent a deadlock. |
|  | Note Return from this function as soon as possible to avoid blocking other asynchronous operations on the same file. If needed, you can use PostDeferredCallToThread or the Thread Pool functions to process this event in a different thread. From within this callback function, you must also avoid calling any functions in the TDM Streaming Library to perform an operation using the same file or any channel groups or channels within that file. The TDM Streaming Library will return an error in that case in order to prevent a deadlock. |  |
| callbackData | void * | Specifies a pointer to user-defined data that the TDM Streaming Library will pass to your callback as the callbackData parameter. Do not pass the address of a local variable or any other variable or memory that might not be valid when the callback is executed. If you do not need callback data you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_AdvancedAsyncWrite function:

- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write\TDMS Advanced Async Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write Throughput Test\TDMS Advanced Async Write Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_advancedclosefile.htm language=enus -->
## TOPIC 00479: TDMS_AdvancedCloseFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_advancedclosefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_advancedclosefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AdvancedCloseFile

int TDMS_AdvancedCloseFile (TDMSFileHandle file, int truncate, double timeoutInSec);

#### Purpose

Closes a file handle and releases extra disk space reserved by [TDMS_ReserveFileSize](../../cvi/libref/cvitdms_reservefilesize.htm). This function also closes all open channel group and channel handles for the specified file.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The handle of the file to close. You obtain this handle from the TDMS_AdvancedCreateFile or TDMS_AdvancedOpenFile function. |
| truncate | int | Specifies whether to truncate the .tdms file when closing this file. If the value is nonzero, this function truncates the file at the current writing position. If the value is zero, this function does not truncate the file and only releases extra disk space reserved by TDMS_ReserveFileSize. |
| timeoutInSec | double | Specifies the maximum time, in seconds, that this function waits for pending asynchronous reads or writes to complete before closing the .tdms file. This function might take longer than the specified timeout to complete as the timeout does not apply to the time required to close the file or call callback functions for pending asynchronous operations. This value has an effect only if you called TDMS_AdvancedCreateFile or TDMS_AdvancedOpenFile with the option to enable asynchronous operations. If any asynchronous operations are still pending after the timeout has elapsed then those pending operations will be canceled. If you specified a callback for those operations, the callback will be called with the error parameter set to TDMS_OperationCancelled. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_AdvancedCloseFile function:

- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read\TDMS Advanced Async Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read Throughput Test\TDMS Advanced Async Read Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write\TDMS Advanced Async Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write Throughput Test\TDMS Advanced Async Write Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Read\TDMS Advanced Sync Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Write\TDMS Advanced Sync Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_advancedcreatefile.htm language=enus -->
## TOPIC 00480: TDMS_AdvancedCreateFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_advancedcreatefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_advancedcreatefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AdvancedCreateFile

int TDMS_AdvancedCreateFile (char *filePath, TDMSFileFormat fileFormat, unsigned int options, char *name, char *description, char *title, char *author, TDMSFileHandle *file, size_t *sectorSize);

#### Purpose

Creates a file handle for a new .tdms file that you write using the advanced synchronous or asychronous I/O functions. Pass the new file handle to other TDM Streaming Library functions to modify the file contents.

Call the [TDMS_AdvancedCloseFile](../../cvi/libref/cvitdms_advancedclosefile.htm) function to close the file handle when you finish using the file.

Files created with this function store data in the file using the byte order of the system. Unlike the [TDMS_CreateFileEx](../../cvi/libref/cvitdms_createfileex.htm) function, this function does not create a .tdms_index file.

|  | Note This function can only create files with a file format version of 2.0 or later. To create a version 1.0 file you must use the TDMS_CreateFileEx function. |
| --- | --- |

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filePath | char * | The path to the file to create. If this value is not an absolute pathname, then the pathname is relative to the current working directory. |
| fileFormat | TDMSFileFormat | The format of the file to create. This function requires you to specify the 2.0 file format version or later. Use the highest version of the file format supported by your system unless you have a specific need for a previous version. Some functionality in this library is available only when using newer versions of the file format. The 2.0 version of the TDM Streaming file format includes all features from version 1.0, as well as additional features. |
| options | unsigned int | Pass TDMS_CreateFileDisableBuffering if you want the TDM Streaming Library to write to and read from this file without Windows system buffering. If you disable system buffering, you must read and write data in multiples of the sector size of the hard disk. This is necessary so that reads and writes will operate on file positions that are aligned on a hard disk sector boundary. By disabling system buffering you can speed up data transfers in certain situations. If you have a small amount of data to transfer you might not notice a difference if you disable buffering. If the file is located on a Redundant Array of Independent Disks (RAID), consider accessing the file without buffering to speed up data transfers. To read the same set of data repeatedly from the computer, consider enabling buffering. The TDMS_CreateFileDisableBuffering option is only supported on Windows operating systems and when using version 2.0 or later of the TDM Streaming file format. Pass TDMS_CreateFileEnableAsynchronousOperations if you want to enable asynchronous reads and writes for the .tdms file. If you do not specify this flag you must use synchronous reads and writes instead. To specify two or more flags, combine them with the bitwise OR operator as shown: TDMS_CreateFileDisableBuffering \| TDMS_CreateFileEnableAsynchronousOperations To specify none of the flags, pass 0. (Real-Time Module) The TDMS_CreateFileDisableBuffering and TDMS_CreateFileEnableAsynchronousOperations flags are not supported. |
| name | char * | The value of the Name property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| description | char * | The value of the Description property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| title | char * | The value of the Title property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| author | char * | The value of the Author property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| Output |  |  |
| Name | Type | Description |
| file | TDMSFileHandle | The handle for the .tdms file. Pass this handle to TDM Streaming Library functions that require a file. Call TDMS_AdvancedCloseFile to close the file handle when you finish using the file. |
| sectorSize | size_t | The sector size of the hard disk. If you specify the disable buffering option for the options parameter, then several TDM Streaming library functions require you to specify read or write positions and read or write sizes that are based on the sector size of the hard disk. For example, read or write positions must correspond to sector boundaries and read or write sizes must be multiples of the sector size. This parameter provides the sector size which you can use for this purpose. The sector size is not available on all platforms. This function returns 0 for the sector size if it is not available. You can pass NULL for this parameter if you do not want this information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_AdvancedCreateFile function:

- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write\TDMS Advanced Async Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write Throughput Test\TDMS Advanced Async Write Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Write\TDMS Advanced Sync Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_advancedsyncread.htm language=enus -->
## TOPIC 00481: TDMS_AdvancedSyncRead

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_advancedsyncread.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_advancedsyncread.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AdvancedSyncRead

int TDMS_AdvancedSyncRead (TDMSFileHandle file, void *samples, size_t numberOfSamples, TDMSDataType dataType, size_t *numberOfSamplesRead);

#### Purpose

Reads data from the specified file.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The file handle. You obtain this handle from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. You must not specify the enable asynchronous operations option when you open or create the file. |
| numberOfSamples | size_t | The number of samples to read. Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncReads. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |
|  | Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncReads. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |  |
| dataType | TDMSDataType | The data type of the samples to read. This function does not support reading samples of type string. |
| Output |  |  |
| Name | Type | Description |
| samples | void * | An array that receives the samples from the specified file. This array must be large enough to hold at least the number of samples specified by the numberOfSamples parameter. The type of this array should match the type of the samples you are reading. This function does not support reading samples of type string. If the type of the samples you are reading is TDMS_Timestamp, you must pass an array of type CVIAbsoluteTime. Refer to the Absolute Time functions in the Utility Library for more information about this type. Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this read operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |
|  | Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this read operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |  |
| numberOfSamplesRead | size_t | The number of samples actually read from the file. This value can be less than numberOfSamples if the end of the file is reached before the specified number of samples have been read. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Example

Refer to TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Read\TDMS Advanced Sync Read.cws for an example of using the TDMS_AdvancedSyncRead function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_advancedsyncwrite.htm language=enus -->
## TOPIC 00482: TDMS_AdvancedSyncWrite

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_advancedsyncwrite.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_advancedsyncwrite.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AdvancedSyncWrite

int TDMS_AdvancedSyncWrite (TDMSFileHandle file, void *samples, size_t numberOfSamples, TDMSDataType dataType);

#### Purpose

Writes data to the specified file.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The file handle. You obtain this handle from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. You must not specify the enable asynchronous operations option when you open or create the file. |
| samples | void * | An array containing samples that will be written to the specified file. The type of this array should match the type of the samples you are writing. This function does not support writing samples of type string. If the type of the samples you are writing is TDMS_Timestamp, you must pass an array of type CVIAbsoluteTime. Refer to the Absolute Time functions in the Utility Library for more information about this type. Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this write operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |
|  | Note The alignment of the pointer value passed for this parameter can significantly impact the performance of this write operation. The performance impact varies depending on the hardware being used. National Instruments recommends a minimal alignment of 512 bytes and a preferred alignment of 4096 bytes. Call TDMS_AllocateAlignedMemory to allocate aligned memory for this parameter. |  |
| numberOfSamples | size_t | The number of samples to write. Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncWrites. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |
|  | Note If you specified the disable buffering option when you opened the file using TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile, then the number of samples should correspond to a number of bytes that is an even multiple of the sector size of the hard disk. This is necessary so that subsequent calls to this function will read from a position in the file that is aligned on a hard disk sector boundary. This requirement does not apply to the last call to this function that corresponds to a single call to TDMS_ConfigureAsyncWrites. The sector size of the hard disk is available as an output parameter from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. |  |
| dataType | TDMSDataType | The data type of the samples to write. This function does not support writing samples of type string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Example

Refer to TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Write\TDMS Advanced Sync Write.cws for an example of using the TDMS_AdvancedSyncWrite function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_allocatealignedmemory.htm language=enus -->
## TOPIC 00483: TDMS_AllocateAlignedMemory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_allocatealignedmemory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_allocatealignedmemory.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AllocateAlignedMemory

int TDMS_AllocateAlignedMemory (size_t memorySize, size_t memoryAlignment, void *memoryPointer);

#### Purpose

Allocates memory with the specified alignment. Using aligned memory can improve streaming performance in certain situations.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| memorySize | size_t | The size in bytes of the memory block this function will allocate. |
| memoryAlignment | size_t | The alignment in bytes of the memory block this function will allocate. This value must be an integer power of two. |
| Output |  |  |
| Name | Type | Description |
| memoryPointer | void * | The pointer to the memory block allocated by this function. Pass the address of a pointer variable. Call TDMS_FreeAlignedMemory to free memory allocated with this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_AllocateAlignedMemory function:

- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read\TDMS Advanced Async Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read Throughput Test\TDMS Advanced Async Read Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write\TDMS Advanced Async Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write Throughput Test\TDMS Advanced Async Write Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Read\TDMS Advanced Sync Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Write\TDMS Advanced Sync Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_appenddatavalues.htm language=enus -->
## TOPIC 00484: TDMS_AppendDataValues

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_appenddatavalues.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_appenddatavalues.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_AppendDataValues

int TDMS_AppendDataValues (TDMSChannelHandle channel, void *values, size_t numberOfValues, int saveFile);

#### Purpose

Appends data values for the specified channel. New data values will be added after existing data values. If the specified channel is empty the new data values will be added at the beginning of the channel.

To append data values to multiple channels at once refer to the [TDMS_AppendDataValuesMultiChannel](../../cvi/libref/cvitdms_appenddatavaluesmultichannel.htm) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| channel | TDMSChannelHandle | The handle of the channel that will contain the new data values. |
| values | void * | An array of data values. The type of this array must match the data type of the specified channel. You can call TDMS_GetDataType to get the data type of a channel. If the data type of the specified channel is TDMS_Timestamp, you must pass an array of type CVIAbsoluteTime. Refer to the Absolute Time functions in the Utility Library for more information about this type. If the data type of the specified channel is string, you must pass an array of type character pointer (char *). The following code illustrates one way to pass an array of strings: char *values[] = {"one", "two", "three", "four", "five"}; TDMS_AppendDataValues (channel, values, 5, 1); |
| numberOfValues | size_t | The number of values in the array specified by the values parameter. |
| saveFile | int | A flag indicating whether to save the file after appending the data values. Specify a nonzero value or select True in the function panel to save the file. Specify 0 or select False in the function panel if you do not want to save the file. If you pass False, you can save the file by calling TDMS_SaveFile. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_AppendDataValues function:

- TDM Streaming\tdmsWriteBenchmark.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS In Memory Write and Read\TDMS In Memory Write and Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_closechannel.htm language=enus -->
## TOPIC 00485: TDMS_CloseChannel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_closechannel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_closechannel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CloseChannel

int TDMS_CloseChannel (TDMSChannelHandle channel);

#### Purpose

Closes a channel handle.

Channel handles are automatically closed when the containing file handle is closed. You should only call this function if you want to close a channel handle explicitly.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| channel | TDMSChannelHandle | The handle of the channel to be closed. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_closechannelgroup.htm language=enus -->
## TOPIC 00486: TDMS_CloseChannelGroup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_closechannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_closechannelgroup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CloseChannelGroup

int TDMS_CloseChannelGroup (TDMSChannelGroupHandle channelGroup);

#### Purpose

Closes a channel group handle.

Channel group handles are automatically closed when the containing file handle is closed. You should only call this function if you want to close a channel group handle explicitly.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| channelGroup | TDMSChannelGroupHandle | The handle of the channel group to be closed. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_closefile.htm language=enus -->
## TOPIC 00487: TDMS_CloseFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_closefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_closefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CloseFile

int TDMS_CloseFile (TDMSFileHandle file);

#### Purpose

Closes a file handle. This function also closes all open channel group and channel handles for the specified file.

This function does not save the file before closing the file handle. Call [TDMS_SaveFile](../../cvi/libref/cvitdms_savefile.htm) to save the file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The handle of the file to be closed. You obtain this handle from the TDMS_OpenFileEx or TDMS_CreateFileEx function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_CloseFile function:

- TDM Streaming\tdmsReader.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\tdmsWriteBenchmark.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS In Memory Write and Read\TDMS In Memory Write and Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createfile.htm language=enus -->
## TOPIC 00488: TDMS_CreateFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateFile

int TDMS_CreateFile (const char *filePath, TDMSFileFormat fileFormat, const char *name, const char *description, const char *title, const char *author, TDMSFileHandle *file);

#### Purpose

|  | Note This function has been superseded by TDMS_CreateFileEx. The new function takes additional parameters for byte order and options. Calling TDMS_CreateFile is equivalent to calling TDMS_CreateFileEx with TDMS_Streaming1_0 for the fileFormat parameter, TDMS_ByteOrderLittleEndian for the byteOrder parameter, and 0 for the options parameter. |
| --- | --- |

Creates a file handle for a new .tdms file. Pass the new file handle to other TDM Streaming Library functions to modify the file contents. Call [TDMS_SaveFile](../../cvi/libref/cvitdms_savefile.htm) to save the file to disk.

Call the [TDMS_CloseFile](../../cvi/libref/cvitdms_closefile.htm) function to close the file handle when you finish using the file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filePath | const char * | The path to the file to create. If this value is not an absolute pathname, then the pathname is relative to the current working directory. |
| fileFormat | TDMSFileFormat | The format of the file to be created. Use the highest version of the file format supported by your system unless you have a specific need for a previous version. Some functionality in this library is only available when you use newer versions of the file format. The 2.0 version of the TDM Streaming file format includes all features from version 1.0, as well as additional features. |
| name | const char * | The value of the Name property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| description | const char * | The value of the Description property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| title | const char * | The value of the Title property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| author | const char * | The value of the Author property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| Output |  |  |
| Name | Type | Description |
| file | TDMSFileHandle | The handle for the TDM Streaming file. Pass this handle to TDM Streaming Library functions that require a file. Call TDMS_SaveFile to save the file to disk. Call TDMS_CloseFile to close the file handle when you finish using the file. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

#### Example

Refer to TDM Streaming\tdmsWriteBenchmark.cws for an example of using the TDMS_CreateFile function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createinmemoryfile.htm language=enus -->
## TOPIC 00489: TDMS_CreateInMemoryFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createinmemoryfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createinmemoryfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateInMemoryFile

int TDMS_CreateInMemoryFile (const char *name, const char *description, const char *title, const char *author, TDMSFileHandle *file);

#### Purpose

Creates a file handle for a new empty in-memory .tdms file. Pass the new file handle to other TDM Streaming Library functions to modify the file contents. Call [TDMS_SaveInMemoryFileToDisk](../../cvi/libref/cvitdms_saveinmemoryfiletodisk.htm) to save the file to disk.

Call the [TDMS_CloseFile](../../cvi/libref/cvitdms_closefile.htm) function to close the file handle when you finish using the file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | const char * | The value of the Name property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| description | const char * | The value of the Description property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| title | const char * | The value of the Title property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| author | const char * | The value of the Author property of the file object. This property is stored in the file and can be accessed with the TDMS_SetFileProperty and TDMS_GetFileProperty functions. |
| Output |  |  |
| Name | Type | Description |
| file | TDMSFileHandle | The handle for the TDM Streaming file. Pass this handle to TDM Streaming Library functions that require a file. Call TDMS_SaveInMemoryFileToDisk to save the file to disk. Call TDMS_CloseFile to close the file handle when you finish using the file. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2019 and later

© 2016 National Instruments. All rights reserved.

#### Example

Refer to TDM Streaming\Advanced Read and Write\TDMS In Memory Write and Read\TDMS In Memory Write and Read.cws for an example of using the TDMS_CreateInMemoryFile function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createlinearscalinginfo.htm language=enus -->
## TOPIC 00490: TDMS_CreateLinearScalingInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createlinearscalinginfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createlinearscalinginfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateLinearScalingInfo

int TDMS_CreateLinearScalingInfo (TDMSAnyHandle handle, double slope, double yIntercept, int inputSource, int *scaleID);

#### Purpose

Creates linear scaling information for one or more channels. A linear scale uses the equation *y=mx+b*, where *y* is a scaled value, *m* is the **slope**, *x* is a pre-scaled value, and *b* is the **y intercept**.

Once scaling information has been created for a channel, [TDMS_GetDataType](../../cvi/libref/cvitdms_getdatatype.htm) will report the type of the channel as **TDMS_Double** and [TDMS_GetDataValues](../../cvi/libref/cvitdms_getdatavalues.htm) will return the scaled data values. The read functions in the [Advanced Synchronous and Asynchronous I/O class](../../cvi/libref/advanced_synchronous_and_asynchronous_i_o_class_cvitdms.html) will still return the unscaled data values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | TDMSAnyHandle | A file, channel group, or channel handle. The scaling information is stored as properties of the specified file, channel group, or channel. If you pass a channel handle, the scaling information will apply only to that channel. If you pass a channel group handle, the scaling information will apply to all channels in that channel group. If you pass a file handle, the scaling information will apply to all channels in that file. If scaling information has been created at multiple levels, the scaling information at the most specific level will take precedence. For example, scaling information on a channel will take precedence over scaling information on the containing channel group or the containing file. |
| slope | double | The slope value for the linear scale. |
| yIntercept | double | The y intercept value for the linear scale. |
| inputSource | int | The scale ID representing the scaling information that will be applied before the scaling information added by this function is applied. Pass -1 if no scaling information should be applied first. When you pass -1 the scaling information added by this function will replace any existing scaling information for the specified file, channel group, or channel. You can use this parameter to combine multiple scales to create a compound scale. You do this by passing the value of the scaleID output parameter from one scaling function as the value of the inputSource input parameter of another scaling function. |
| Output |  |  |
| Name | Type | Description |
| scaleID | int | A scale ID representing the scaling information created by this function. If you passed a value other than -1 for the inputSource parameter, then this scale ID represents the cumulative scaling information represented by that parameter plus the scaling information created by this function. You only need this value if you want to pass it as the value of the inputSource parameter to another scaling function. If you do not need this value you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createpolynomialscalinginfo.htm language=enus -->
## TOPIC 00491: TDMS_CreatePolynomialScalingInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createpolynomialscalinginfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createpolynomialscalinginfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreatePolynomialScalingInfo

int TDMS_CreatePolynomialScalingInfo (TDMSAnyHandle handle, double coefficients[], size_t numberOfCoefficients, int inputSource, int *scaleID);

#### Purpose

Creates polynomial scaling information for one or more channels. A polynomial scale uses an *n*th-order polynomial equation of the form: 

P(*x*) = *a*<sub>0</sub> + *a*<sub>1</sub>*x* + *a*<sub>2</sub>*x*<sup>2</sup> + ... + *a*<sub>n</sub>*x*<sup>n</sup>

Once scaling information has been created for a channel, [TDMS_GetDataType](../../cvi/libref/cvitdms_getdatatype.htm) will report the type of the channel as **TDMS_Double** and [TDMS_GetDataValues](../../cvi/libref/cvitdms_getdatavalues.htm) will return the scaled data values. The read functions in the [Advanced Synchronous and Asynchronous I/O class](../../cvi/libref/advanced_synchronous_and_asynchronous_i_o_class_cvitdms.html) will still return the unscaled data values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | TDMSAnyHandle | A file, channel group, or channel handle. The scaling information is stored as properties of the specified file, channel group, or channel. If you pass a channel handle, the scaling information will apply only to that channel. If you pass a channel group handle, the scaling information will apply to all channels in that channel group. If you pass a file handle, the scaling information will apply to all channels in that file. If scaling information has been created at multiple levels, the scaling information at the most specific level will take precedence. For example, scaling information on a channel will take precedence over scaling information on the containing channel group or the containing file. |
| coefficients | double [] | The coefficients for the polynomial scale. Each element of the array corresponds to a term of the equation. For example, if the fourth item in the array (at index three) is 9, the fourth term of the equation is 9x3. |
| numberOfCoefficients | size_t | The number of coefficients in the array specified by the coefficients parameter. |
| inputSource | int | The scale ID representing the scaling information that will be applied before the scaling information added by this function is applied. Pass -1 if no scaling information should be applied first. When you pass -1 the scaling information added by this function will replace any existing scaling information for the specified file, channel group, or channel. You can use this parameter to combine multiple scales to create a compound scale. You do this by passing the value of the scaleID output parameter from one scaling function as the value of the inputSource input parameter of another scaling function. |
| Output |  |  |
| Name | Type | Description |
| scaleID | int | A scale ID representing the scaling information created by this function. If you passed a value other than -1 for the inputSource parameter, then this scale ID represents the cumulative scaling information represented by that parameter plus the scaling information created by this function. You only need this value if you want to pass it as the value of the inputSource parameter to another scaling function. If you do not need this value you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createreciprocalscalinginfo.htm language=enus -->
## TOPIC 00492: TDMS_CreateReciprocalScalingInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createreciprocalscalinginfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createreciprocalscalinginfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateReciprocalScalingInfo

int TDMS_CreateReciprocalScalingInfo (TDMSAnyHandle handle, int inputSource, int *scaleID);

#### Purpose

Creates reciprocal scaling information for one or more channels. A reciprocal scale divides the number 1 by an input value. If the input value is zero, this function uses zero as the reciprocal.

Once scaling information has been created for a channel, [TDMS_GetDataType](../../cvi/libref/cvitdms_getdatatype.htm) will report the type of the channel as **TDMS_Double** and [TDMS_GetDataValues](../../cvi/libref/cvitdms_getdatavalues.htm) will return the scaled data values. The read functions in the [Advanced Synchronous and Asynchronous I/O class](../../cvi/libref/advanced_synchronous_and_asynchronous_i_o_class_cvitdms.html) will still return the unscaled data values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | TDMSAnyHandle | A file, channel group, or channel handle. The scaling information is stored as properties of the specified file, channel group, or channel. If you pass a channel handle, the scaling information will apply only to that channel. If you pass a channel group handle, the scaling information will apply to all channels in that channel group. If you pass a file handle, the scaling information will apply to all channels in that file. If scaling information has been created at multiple levels, the scaling information at the most specific level will take precedence. For example, scaling information on a channel will take precedence over scaling information on the containing channel group or the containing file. |
| inputSource | int | The scale ID representing the scaling information that will be applied before the scaling information added by this function is applied. Pass -1 if no scaling information should be applied first. When you pass -1 the scaling information added by this function will replace any existing scaling information for the specified file, channel group, or channel. You can use this parameter to combine multiple scales to create a compound scale. You do this by passing the value of the scaleID output parameter from one scaling function as the value of the inputSource input parameter of another scaling function. |
| Output |  |  |
| Name | Type | Description |
| scaleID | int | A scale ID representing the scaling information created by this function. If you passed a value other than -1 for the inputSource parameter, then this scale ID represents the cumulative scaling information represented by that parameter plus the scaling information created by this function. You only need this value if you want to pass it as the value of the inputSource parameter to another scaling function. If you do not need this value you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_creatertdscalinginfo.htm language=enus -->
## TOPIC 00493: TDMS_CreateRTDScalingInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_creatertdscalinginfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_creatertdscalinginfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateRTDScalingInfo

int TDMS_CreateRTDScalingInfo (TDMSAnyHandle handle, double currentExcitation, double r0NominalResistance, double a, double b, double c, double leadWireResistance, TDMSResistanceConfig resistanceConfiguration, int inputSource, int *scaleID);

#### Purpose

Creates resistance temperature detector (RTD) scaling information for one or more channels. The RTD scaling information scales the data values in degrees Celsius.

Once scaling information has been created for a channel, [TDMS_GetDataType](../../cvi/libref/cvitdms_getdatatype.htm) will report the type of the channel as **TDMS_Double** and [TDMS_GetDataValues](../../cvi/libref/cvitdms_getdatavalues.htm) will return the scaled data values. The read functions in the [Advanced Synchronous and Asynchronous I/O class](../../cvi/libref/advanced_synchronous_and_asynchronous_i_o_class_cvitdms.html) will still return the unscaled data values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | TDMSAnyHandle | A file, channel group, or channel handle. The scaling information is stored as properties of the specified file, channel group, or channel. If you pass a channel handle, the scaling information will apply only to that channel. If you pass a channel group handle, the scaling information will apply to all channels in that channel group. If you pass a file handle, the scaling information will apply to all channels in that file. If scaling information has been created at multiple levels, the scaling information at the most specific level will take precedence. For example, scaling information on a channel will take precedence over scaling information on the containing channel group or the containing file. |
| currentExcitation | double | The amount of excitation, in amperes, that the sensor requires. Refer to the sensor documentation to determine this value. |
| r0NominalResistance | double | The sensor resistance, in ohms, at 0 degrees Celsius. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value. |
| a | double | The A coefficient for the Callendar-Van Dusen equation. Refer to the sensor documentation to determine this value. |
| b | double | The B coefficient for the Callendar-Van Dusen equation. Refer to the sensor documentation to determine this value. |
| c | double | The C coefficient for the Callendar-Van Dusen equation. Refer to the sensor documentation to determine this value. |
| leadWireResistance | double | The amount of resistance, in ohms, in the lead wires. Ideally, this value is the same for all leads. |
| resistanceConfiguration | TDMSResistanceConfig | The number of wires to use for resistance measurements. Value Description TDMS_ResistanceConfig2Wire 2-wires TDMS_ResistanceConfig3Wire 3-wires TDMS_ResistanceConfig4Wire 4-wires |
| Value | Description |  |
| TDMS_ResistanceConfig2Wire | 2-wires |  |
| TDMS_ResistanceConfig3Wire | 3-wires |  |
| TDMS_ResistanceConfig4Wire | 4-wires |  |
| inputSource | int | The scale ID representing the scaling information that will be applied before the scaling information added by this function is applied. Pass -1 if no scaling information should be applied first. When you pass -1 the scaling information added by this function will replace any existing scaling information for the specified file, channel group, or channel. You can use this parameter to combine multiple scales to create a compound scale. You do this by passing the value of the scaleID output parameter from one scaling function as the value of the inputSource input parameter of another scaling function. |
| Output |  |  |
| Name | Type | Description |
| scaleID | int | A scale ID representing the scaling information created by this function. If you passed a value other than -1 for the inputSource parameter, then this scale ID represents the cumulative scaling information represented by that parameter plus the scaling information created by this function. You only need this value if you want to pass it as the value of the inputSource parameter to another scaling function. If you do not need this value you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createstraingagescalinginfo.htm language=enus -->
## TOPIC 00494: TDMS_CreateStrainGageScalingInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createstraingagescalinginfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createstraingagescalinginfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateStrainGageScalingInfo

int TDMS_CreateStrainGageScalingInfo (TDMSAnyHandle handle, TDMSStrainGaugeConfig configuration, double poissonRatio, double gageResistance, double leadWireResistance, double initialBridgeVoltage, double gageFactor, double voltageExcitation, int inputSource, int *scaleID);

#### Purpose

Creates strain gage scaling information for one or more channels. Strain is the amount of deformation of a body due to an applied force. Specifically, strain is the fractional change in length.

Once scaling information has been created for a channel, [TDMS_GetDataType](../../cvi/libref/cvitdms_getdatatype.htm) will report the type of the channel as **TDMS_Double** and [TDMS_GetDataValues](../../cvi/libref/cvitdms_getdatavalues.htm) will return the scaled data values. The read functions in the [Advanced Synchronous and Asynchronous I/O class](../../cvi/libref/advanced_synchronous_and_asynchronous_i_o_class_cvitdms.html) will still return the unscaled data values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | TDMSAnyHandle | A file, channel group, or channel handle. The scaling information is stored as properties of the specified file, channel group, or channel. If you pass a channel handle, the scaling information will apply only to that channel. If you pass a channel group handle, the scaling information will apply to all channels in that channel group. If you pass a file handle, the scaling information will apply to all channels in that file. If scaling information has been created at multiple levels, the scaling information at the most specific level will take precedence. For example, scaling information on a channel will take precedence over scaling information on the containing channel group or the containing file. |
| configuration | TDMSStrainGaugeConfig | The bridge configuration for the strain gages. Value Description TDMS_StrainGageConfigFullBridgeI Full Bridge I TDMS_StrainGageConfigFullBridgeII Full Bridge II TDMS_StrainGageConfigFullBridgeIII Full Bridge III TDMS_StrainGageConfigHalfBridgeI Half Bridge I TDMS_StrainGageConfigHalfBridgeII Half Bridge II TDMS_StrainGageConfigQuarterBridgeI Quarter Bridge I TDMS_StrainGageConfigQuarterBridgeII Quarter Bridge II |
| Value | Description |  |
| TDMS_StrainGageConfigFullBridgeI | Full Bridge I |  |
| TDMS_StrainGageConfigFullBridgeII | Full Bridge II |  |
| TDMS_StrainGageConfigFullBridgeIII | Full Bridge III |  |
| TDMS_StrainGageConfigHalfBridgeI | Half Bridge I |  |
| TDMS_StrainGageConfigHalfBridgeII | Half Bridge II |  |
| TDMS_StrainGageConfigQuarterBridgeI | Quarter Bridge I |  |
| TDMS_StrainGageConfigQuarterBridgeII | Quarter Bridge II |  |
| poissonRatio | double | The ratio of lateral strain to axial strain in the material you are measuring. |
| gageResistance | double | The resistance, in ohms, of the gages in an unstrained position. Each gage in the bridge must have the same nominal gage resistance. The resistance across arms of the bridge that do not have strain gages also must be the same as the nominal gage resistance. Refer to the sensor documentation to determine this value. |
| leadWireResistance | double | The amount of resistance, in ohms, in the lead wires. Ideally, this value is the same for all leads. |
| initialBridgeVoltage | double | The output voltage of the bridge, in volts, in the unloaded condition. This function subtracts this value from any measurements before applying scaling equations. Perform a voltage measurement on the bridge with no strain applied to determine this value. |
| gageFactor | double | Specifies the sensitivity of the strain gages and relates the change in electrical resistance to the change in strain. Each gage in the bridge must have the same gage factor. Refer to the sensor documentation to determine this value. |
| voltageExcitation | double | The amount of excitation, in volts, that the sensor requires. Refer to the sensor documentation to determine this value. |
| inputSource | int | The scale ID representing the scaling information that will be applied before the scaling information added by this function is applied. Pass -1 if no scaling information should be applied first. When you pass -1 the scaling information added by this function will replace any existing scaling information for the specified file, channel group, or channel. You can use this parameter to combine multiple scales to create a compound scale. You do this by passing the value of the scaleID output parameter from one scaling function as the value of the inputSource input parameter of another scaling function. |
| Output |  |  |
| Name | Type | Description |
| scaleID | int | A scale ID representing the scaling information created by this function. If you passed a value other than -1 for the inputSource parameter, then this scale ID represents the cumulative scaling information represented by that parameter plus the scaling information created by this function. You only need this value if you want to pass it as the value of the inputSource parameter to another scaling function. If you do not need this value you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createtablescalinginfo.htm language=enus -->
## TOPIC 00495: TDMS_CreateTableScalingInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createtablescalinginfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createtablescalinginfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateTableScalingInfo

int TDMS_CreateTableScalingInfo (TDMSAnyHandle handle, double prescaledValues[], double scaledValues[], size_t numberOfValues, int inputSource, int *scaleID);

#### Purpose

Creates table scaling information for one or more channels. A table scale maps an array of pre-scaled values to an array of corresponding scaled values. If a value is less than the first value in the **prescaledValues** array it will map to the first value in the **scaledValues** array. If a value is greater than the last value in the **prescaledValues** array it will map to the last value in the **scaledValues** array. If a value is equal to any value in the **prescaledValues** array it will map to the corresponding value in the **scaledValues** array. If a value is between two consecutive values in the **prescaledValues** array it will map to a value between the two corresponding values in the **scaledValues** array in a proportional manner.

Once scaling information has been created for a channel, [TDMS_GetDataType](../../cvi/libref/cvitdms_getdatatype.htm) will report the type of the channel as **TDMS_Double** and [TDMS_GetDataValues](../../cvi/libref/cvitdms_getdatavalues.htm) will return the scaled data values. The read functions in the [Advanced Synchronous and Asynchronous I/O class](../../cvi/libref/advanced_synchronous_and_asynchronous_i_o_class_cvitdms.html) will still return the unscaled data values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | TDMSAnyHandle | A file, channel group, or channel handle. The scaling information is stored as properties of the specified file, channel group, or channel. If you pass a channel handle, the scaling information will apply only to that channel. If you pass a channel group handle, the scaling information will apply to all channels in that channel group. If you pass a file handle, the scaling information will apply to all channels in that file. If scaling information has been created at multiple levels, the scaling information at the most specific level will take precedence. For example, scaling information on a channel will take precedence over scaling information on the containing channel group or the containing file. |
| prescaledValues | double [] | The array of pre-scaled values. |
| scaledValues | double [] | The array of scaled values. |
| numberOfValues | size_t | The number of values in the prescaledValues and scaledValues arrays. |
| inputSource | int | The scale ID representing the scaling information that will be applied before the scaling information added by this function is applied. Pass -1 if no scaling information should be applied first. When you pass -1 the scaling information added by this function will replace any existing scaling information for the specified file, channel group, or channel. You can use this parameter to combine multiple scales to create a compound scale. You do this by passing the value of the scaleID output parameter from one scaling function as the value of the inputSource input parameter of another scaling function. |
| Output |  |  |
| Name | Type | Description |
| scaleID | int | A scale ID representing the scaling information created by this function. If you passed a value other than -1 for the inputSource parameter, then this scale ID represents the cumulative scaling information represented by that parameter plus the scaling information created by this function. You only need this value if you want to pass it as the value of the inputSource parameter to another scaling function. If you do not need this value you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_createthermocouplescalinginfo.htm language=enus -->
## TOPIC 00496: TDMS_CreateThermocoupleScalingInfo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_createthermocouplescalinginfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_createthermocouplescalinginfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_CreateThermocoupleScalingInfo

int TDMS_CreateThermocoupleScalingInfo (TDMSAnyHandle handle, TDMSThermocoupleType thermocoupleType, int inputSource, int *scaleID);

#### Purpose

Creates thermocouple scaling information for one or more channels. The thermocouple scaling information scales the data values from microvolts to degrees Celsius. If the data is not in microvolts, first convert the data to microvolts with an additional scale. For example, you can use [TDMS_CreateLinearScalingInfo](../../cvi/libref/cvitdms_createlinearscalinginfo.htm) to do the unit conversion. Pass the value of the **scaleID** output parameter from TDMS_CreateLinearScalingInfo as the value of the **inputSource** input parameter to TDMS_CreateThermocoupleScalingInfo.

Once scaling information has been created for a channel, [TDMS_GetDataType](../../cvi/libref/cvitdms_getdatatype.htm) will report the type of the channel as **TDMS_Double** and [TDMS_GetDataValues](../../cvi/libref/cvitdms_getdatavalues.htm) will return the scaled data values. The read functions in the [Advanced Synchronous and Asynchronous I/O class](../../cvi/libref/advanced_synchronous_and_asynchronous_i_o_class_cvitdms.html) will still return the unscaled data values.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handle | TDMSAnyHandle | A file, channel group, or channel handle. The scaling information is stored as properties of the specified file, channel group, or channel. If you pass a channel handle, the scaling information will apply only to that channel. If you pass a channel group handle, the scaling information will apply to all channels in that channel group. If you pass a file handle, the scaling information will apply to all channels in that file. If scaling information has been created at multiple levels, the scaling information at the most specific level will take precedence. For example, scaling information on a channel will take precedence over scaling information on the containing channel group or the containing file. |
| thermocoupleType | TDMSThermocoupleType | The type of the thermocouple. Thermocouple types differ in composition and measurement range. Value Description TDMS_ThermocoupleTypeB B-type thermocouple TDMS_ThermocoupleTypeE E-type thermocouple TDMS_ThermocoupleTypeJ J-type thermocouple TDMS_ThermocoupleTypeK K-type thermocouple TDMS_ThermocoupleTypeN N-type thermocouple TDMS_ThermocoupleTypeR R-type thermocouple TDMS_ThermocoupleTypeS S-type thermocouple TDMS_ThermocoupleTypeT T-type thermocouple |
| Value | Description |  |
| TDMS_ThermocoupleTypeB | B-type thermocouple |  |
| TDMS_ThermocoupleTypeE | E-type thermocouple |  |
| TDMS_ThermocoupleTypeJ | J-type thermocouple |  |
| TDMS_ThermocoupleTypeK | K-type thermocouple |  |
| TDMS_ThermocoupleTypeN | N-type thermocouple |  |
| TDMS_ThermocoupleTypeR | R-type thermocouple |  |
| TDMS_ThermocoupleTypeS | S-type thermocouple |  |
| TDMS_ThermocoupleTypeT | T-type thermocouple |  |
| inputSource | int | The scale ID representing the scaling information that will be applied before the scaling information added by this function is applied. Pass -1 if no scaling information should be applied first. When you pass -1 the scaling information added by this function will replace any existing scaling information for the specified file, channel group, or channel. You can use this parameter to combine multiple scales to create a compound scale. You do this by passing the value of the scaleID output parameter from one scaling function as the value of the inputSource input parameter of another scaling function. |
| Output |  |  |
| Name | Type | Description |
| scaleID | int | A scale ID representing the scaling information created by this function. If you passed a value other than -1 for the inputSource parameter, then this scale ID represents the cumulative scaling information represented by that parameter plus the scaling information created by this function. You only need this value if you want to pass it as the value of the inputSource parameter to another scaling function. If you do not need this value you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_flushfile.htm language=enus -->
## TOPIC 00497: TDMS_FlushFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_flushfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_flushfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_FlushFile

int TDMS_FlushFile (TDMSFileHandle file);

#### Purpose

Writes all buffers of the .tdms file data to the file identified by the tdms file handle.

Data written to a .tdms file often resides in a buffer until the buffer fills up or until you close the file. This function forces the operating system to write any buffer data to the .tdms file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The handle of the file to be flushed. You obtain this handle from the TDMS_OpenFileEx or TDMS_CreateFileEx function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2019 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_freealignedmemory.htm language=enus -->
## TOPIC 00498: TDMS_FreeAlignedMemory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_freealignedmemory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_freealignedmemory.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_FreeAlignedMemory

void TDMS_FreeAlignedMemory (void *memoryPointer);

#### Purpose

Frees memory allocated with [TDMS_AllocateAlignedMemory](../../cvi/libref/cvitdms_allocatealignedmemory.htm). To free memory allocated by any other TDM Streaming Library function, call [TDMS_FreeMemory](../../cvi/libref/cvitdms_freememory.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| memoryPointer | void * | A pointer to memory allocated by TDMS_AllocateAlignedMemory. |

#### Return Value

None.

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.

#### Examples

Refer to the following examples that use the TDMS_FreeAlignedMemory function:

- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read\TDMS Advanced Async Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Read Throughput Test\TDMS Advanced Async Read Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write\TDMS Advanced Async Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Async Write Throughput Test\TDMS Advanced Async Write Throughput Test.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Read\TDMS Advanced Sync Read.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- TDM Streaming\Advanced Read and Write\TDMS Advanced Sync Write\TDMS Advanced Sync Write.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_freememory.htm language=enus -->
## TOPIC 00499: TDMS_FreeMemory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_freememory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_freememory.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_FreeMemory

void TDMS_FreeMemory (void *memoryPointer);

#### Purpose

Frees memory allocated by any function in the TDM Streaming Library except [cviTDMS_AllocateAlignedMemory](../../cvi/libref/cvitdms_allocatealignedmemory.htm). To free memory allocated by TDMS_AllocAlignedMemory, call [TDMS_FreeAlignedMemory](../../cvi/libref/cvitdms_freealignedmemory.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| memoryPointer | void * | A pointer to memory allocated by this library. |

#### Return Value

None.

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_getasyncreadstatus.htm language=enus -->
## TOPIC 00500: TDMS_GetAsyncReadStatus

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_getasyncreadstatus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_getasyncreadstatus.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_GetAsyncReadStatus

int TDMS_GetAsyncReadStatus (TDMSFileHandle file, unsigned int *numberOfPendingReads);

#### Purpose

Returns the number of pending asynchronous reads issued by [TDMS_AdvancedAsyncRead](../../cvi/libref/cvitdms_advancedasyncread.htm).

Use this function to monitor an application that issues a series of asynchronous reads over a long period of time. By querying the number of pending reads and keeping track of the highest value, you can choose an appropriate value for the **maxNumConcurrentAsyncReads** parameter of [TDMS_ConfigureAsyncReads](../../cvi/libref/cvitdms_configureasyncreads.htm).

(Linux) This function is not supported.

(Real-Time Module) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| file | TDMSFileHandle | The file handle. You obtain this handle from TDMS_AdvancedOpenFile or TDMS_AdvancedCreateFile. You must specify the enable asynchronous operations option when you open or create the file. |
| Output |  |  |
| Name | Type | Description |
| numberOfPendingReads | unsigned int | The number of asynchronous reads that have not completed. You can use this information to monitor a read-from-disk operation. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2013 and later

© 2016 National Instruments. All rights reserved.
