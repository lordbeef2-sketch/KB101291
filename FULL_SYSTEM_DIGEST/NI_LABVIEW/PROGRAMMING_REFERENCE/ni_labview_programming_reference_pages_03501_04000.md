# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3501 ordinal=3501 -->
## Functions

Functions

Δ0 = [min: min + Δx)

Δ1 = [min + Δx:min + 2Δx)

⋮

Δi = [min + iΔx:min + (i+ 1)Δx)

⋮

Δk– 1 = [min + (k– 1)Δx:max]

If inclusion is set to upper, the bin widths are determined according to the following
equations.

Δ0 = [min:min + Δx]

Δ1 = (min + Δx:min + 2Δx]

⋮

Δi = (min + iΔx:min + (i+ 1)Δx]

⋮

Δk– 1 = (min + (k– 1)Δx:max]

      Note The first start point min and last end point max are always included in
       the first and last bins.

Defining the Function yi(x)

The following equation defines the function yi(x).


                                                    © National Instruments 3501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3502 ordinal=3502 -->
## Functions

Functions

       For example, if xfalls into the bin Δi, then yi(x) = 1.

      Evaluating the Histogram Sequence H

      The General Histogram VI evaluates the histogram sequence Hwith the following
       equation.


      where Hrepresents the elements of the output sequence Histogram, nis the number
       of elements in the input sequence X, hi is the total number of points in the input array
      X that fall into the bin Δi, i= 0, 1, …, k– 1, and kis the number of bins.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Running Histogram.vi

      CorrelationCorrelation CoefficientCoefficient

      Computes the linear correlation coefficient between input sequences X and Y.


      Inputs/Outputs

               •     X —

          X is the first input sequence.

               •      Y —

           Y is the second input sequence.


3502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3503 ordinal=3503 -->
## Functions

Functions

   •       correlation coefficient r —

    correlation coefficient r returns the correlation coefficient between X and Y.

   •      r^2 —

    r^2 returns the square of correlation coefficient r.


The linear correlation coefficient also is known as the product-moment coefficient of
correlation or Pearson's correlation. The following equation describes the linear
correlation coefficient:


where zx and zy are the standardized z-values of X and Y. The standardized z-values
indicate how many standard deviations X and Y are above or below the mean.

correlation coefficient r always is in the interval [–1, 1]. If correlation coefficient r is 1,
X and Y have a complete positive correlation. In other words, the data points from X
and Y lie on a perfectly straight, positively-sloped line. If correlation coefficient r is –1,
X and Y have a complete negative correlation. In other words, the data points from X
and Y lie on a perfectly straight, negatively-sloped line. If correlation coefficient r is 0,
X and Y have no correlation.

CorrelationCorrelation CoefficientCoefficient (Spearman)(Spearman)

Computes the Spearman's rank correlation coefficient between input sequences X and
Y.


Inputs/Outputs

   •     X —

    X is the first input sequence.


                                                    © National Instruments 3503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3504 ordinal=3504 -->
## Functions

Functions

               •      Y —

           Y is the second input sequence.

               •       correlation coefficient r —

             correlation coefficient r returns the correlation coefficient between X and Y.

               •      r^2 —

            r^2 returns the square of correlation coefficient r.


      The Spearman's rank correlation coefficient is a non-parametric measure of monotone
       association between two data sets and is defined as the linear correlation coefficient
       applied to the rank-transformations of X and Y. Use the Spearman's rank correlation
        coefficient when the distribution of the data makes the Pearson's correlation
        coefficient undesirable or misleading.

      CorrelationCorrelation CoefficientCoefficient (Kendall's(Kendall's Tau)Tau)

      Computes the Kendall's Tau correlation coefficient between input sequences X and Y.


      Inputs/Outputs

               •     X —

          X is the first input sequence.

               •      Y —

           Y is the second input sequence.

               •       correlation coefficient r —

             correlation coefficient r returns the correlation coefficient between X and Y.

               •      r^2 —


3504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3505 ordinal=3505 -->
## Functions

Functions


    r^2 returns the square of correlation coefficient r.


The Kendall's Tau correlation coefficient is a non-parametric measure of association
between two data sets.

In a population with the Kendall's Tau correlation coefficient r, the odds ratio Pc /Pd
of the concordant to discordant sets of observations equals (1+r)/(1–r). For example, in
a population with a cross correlation r of 1/2, X and Y are three times as likely to be
concordant than discordant.

ProbabilityProbability

Use the Probability VIs to perform probability distribution and random number
generation functions.

The VIs on this palette can return mathematics error codes.


 Palette             Description Object

           Computes the continuous cumulative distribution function (CDF), or the probability
 Continuous  that the random variate X, where Xdescribes the selected distribution type, has a
 CDF         value less than or equal to x. You must manually select the polymorphic instance to
              use.


 Continuous
           Computes the continuous inverse cumulative distribution function (CDF) of the
 Inverse
             various distributions. You must manually select the polymorphic instance to use.
 CDF


 Continuous Computes the continuous probability density function (PDF) of various distributions.
 PDF        You must manually select the polymorphic instance to use.


                                                    © National Instruments 3505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3506 ordinal=3506 -->
## Functions

Functions


         Palette                     Description
        Object

        Continuous Generates random values from a variate X, where X describes the selected distribution
       Random     type. You must manually select the polymorphic instance to use.


                    Returns the expected mean and variance of the random variate X, where Xdescribes        Continuous
                     the selected distribution type. You must manually select the polymorphic instance to       Moments
                      use.


                  Computes the discrete cumulative distribution function (CDF), or the probability that
         Discrete     the random variate X, where Xdescribes the selected distribution type, takes on a
       CDF         value less than or equal to x. You must manually select the polymorphic instance to
                      use.


                  Computes the discrete inverse cumulative distribution function (CDF), or the value x
         Discrete                   such that the probability that the random variate X, where Xdescribes the selected         Inverse
                       distribution type, takes on a value less than or equal to it is cdf(x). You must manually       CDF
                       select the polymorphic instance to use.


                  Computes the discrete probability function (PF), or the probability that the random
         Discrete PF  variate X, where Xdescribes the selected distribution type, takes on the value n. You
                  must manually select the polymorphic instance to use.


         Discrete     Generates random values from a variate X, where Xdescribes the selected distribution
       Random     type. You must manually select the polymorphic instance to use.


                    Returns the expected mean and variance of the random variate X, where Xdescribes         Discrete
                     the selected distribution type. You must manually select the polymorphic instance to       Moments
                      use.


3506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3507 ordinal=3507 -->
## Functions

Functions

ContinuousContinuous CDFCDF

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


  • Beta CDF VI
  • Cauchy CDF VI
  • Chi-Squared CDF VI
  • Chi-Squared (Non-Central) CDF VI
  • Exp CDF VI
  • Extreme Value CDF VI
  • F CDF VI
  • Gamma CDF VI
  • Laplace CDF VI
  • Logistic CDF VI
  • Lognormal CDF VI
  • Normal CDF VI
  • Pareto CDF VI
  • Rayleigh CDF VI
  • Student t CDF VI
  • Triangular CDF VI
  • Uniform CDF VI
  • Weibull CDF VI

When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.


                                                    © National Instruments 3507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3508 ordinal=3508 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   BetaBeta CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate and is bounded by the interval [0, 1].

               •      a —

           a specifies the first shape parameter of the beta variate.

               •     b —

          b specifies the second shape parameter of the beta variate.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —


3508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3509 ordinal=3509 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
CauchyCauchy CDFCDF VIVI

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate.

   •      a —


                                                    © National Instruments 3509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3510 ordinal=3510 -->
## Functions

Functions


           a specifies the location parameter and median of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative
        distribution function (CDF), the beta distribution function, or the incomplete beta
       function.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   Chi-SquaredChi-Squared CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


3510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3511 ordinal=3511 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •     k —

    k specifies the number of degrees of freedom and must be greater than 0.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3512 ordinal=3512 -->
## Functions

Functions

   Chi-SquaredChi-Squared (Non-Central)(Non-Central) CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ 0.

               •     k —

           k specifies the number of degrees of freedom and must be greater than 0.

               •     d —

          d specifies the noncentrality parameter, which must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative


3512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3513 ordinal=3513 -->
## Functions

Functions

distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
ExpExp CDFCDF VIVI

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ a.

   •      a —

    a specifies the offset parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.


                                                    © National Instruments 3513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3514 ordinal=3514 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative
        distribution function (CDF), the beta distribution function, or the incomplete beta
       function.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   ExtremeExtreme ValueValue CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate.

               •      a —


3514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3515 ordinal=3515 -->
## Functions

Functions


    a specifies the location parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
FF CDFCDF VIVI

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3516 ordinal=3516 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ 0.

               •      k1 —

           k1 specifies the number of degrees of freedom of the first chi-squared variate that forms the F
              variate. k1 must be greater than 0.

               •      k2 —

           k2 specifies the number of degrees of freedom of the second chi-squared variate that forms the
           F variate. k2 must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative
        distribution function (CDF), the beta distribution function, or the incomplete beta
       function.

     Examples

       Refer to the following example files included with LabVIEW.


3516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3517 ordinal=3517 -->
## Functions

Functions

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
GammaGamma CDFCDF VIVI

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •     b —

   b specifies the shape parameter of the variate and must be greater than 0.

   •      c —

    c specifies the scale parameter of the variate and must be greater than 0.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,


                                                    © National Instruments 3517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3518 ordinal=3518 -->
## Functions

Functions

      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative
        distribution function (CDF), the beta distribution function, or the incomplete beta
       function.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   LaplaceLaplace CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate.

               •      a —

           a specifies the location or mean parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •       cdf(x) —


3518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3519 ordinal=3519 -->
## Functions

Functions


     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
LogisticLogistic CDFCDF VIVI

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —


                                                    © National Instruments 3519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3520 ordinal=3520 -->
## Functions

Functions


           x specifies the quantile of the continuous random variate.

               •      a —

           a specifies the location or mean parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative
        distribution function (CDF), the beta distribution function, or the incomplete beta
       function.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   LognormalLognormal CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a

3520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3521 ordinal=3521 -->
## Functions

Functions

value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •     b —

   b specifies the scale or median parameter of the variate and must be greater than 0.

   •      c —

    c specifies the shape parameter of the variate and must be greater than 0.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.


                                                    © National Instruments 3521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3522 ordinal=3522 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   NormalNormal CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate.

               •     mean —

         mean specifies the location or mean parameter of the variate.

               •       std —

            std specifies the scale or standard deviation parameter of the variate and must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —


3522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3523 ordinal=3523 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
ParetoPareto CDFCDF VIVI

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ a.

   •      a —


                                                    © National Instruments 3523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3524 ordinal=3524 -->
## Functions

Functions


           a specifies the location parameter and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative
        distribution function (CDF), the beta distribution function, or the incomplete beta
       function.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    RayleighRayleigh CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


3524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3525 ordinal=3525 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3526 ordinal=3526 -->
## Functions

Functions

   StudentStudent tt CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate.

               •     k degrees of freedom —

           k degrees of freedom specifies the number of degrees of freedom and must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       1-cdf(x) —

             1–cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value greater than x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.


3526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3527 ordinal=3527 -->
## Functions

Functions

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
TriangularTriangular CDFCDF VIVI

Computes the continuous cumulative distribution function (CDF), or the probability
that the random variate X, where Xdescribes the selected distribution type, has a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate and is bounded by the interval [xmin,
    xmax].

   •     xmin —

    xmin specifies the lower limit parameter of the variate.

   •     xmode —

   xmode specifies the mode parameter of the variate. The default is NaN, which corresponds to a
   mode at the midpoint between xmin and xmax.

   •     xmax —

                                                    © National Instruments 3527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3528 ordinal=3528 -->
## Functions

Functions


         xmax specifies the upper limit parameter of the variate.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative
        distribution function (CDF), the beta distribution function, or the incomplete beta
       function.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   UniformUniform CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


3528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3529 ordinal=3529 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate and is bounded by the interval [xmin,
    xmax].

   •     xmin —

    xmin specifies the lower limit parameter of the variate.

   •     xmax —

   xmax specifies the upper limit parameter of the variate.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
which is restricted to a finite interval [0, 1], with given shape parameters a and b.

The CDF function with a beta distribution also is known as the beta cumulative
distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3530 ordinal=3530 -->
## Functions

Functions

    WeibullWeibull CDFCDF VIVI

      Computes the continuous cumulative distribution function (CDF), or the probability
       that the random variate X, where Xdescribes the selected distribution type, has a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ 0.

               •      a —

           a specifies the location parameter and must be greater than 0.

               •     b —

          b specifies the shape parameter of the variate and must be greater than 0.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Beta CDF instance of this VI, Xrepresents a beta-distributed variate,
      which is restricted to a finite interval [0, 1], with given shape parameters a and b.

      The CDF function with a beta distribution also is known as the beta cumulative


3530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3531 ordinal=3531 -->
## Functions

Functions

distribution function (CDF), the beta distribution function, or the incomplete beta
function.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi

ContinuousContinuous InverseInverse CDFCDF

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


  • Beta Inverse CDF VI
  • Cauchy Inverse CDF VI
  • Chi-Squared Inverse CDF VI
  • Chi-Squared (Non-Central) Inverse CDF VI
  • Exp Inverse CDF VI
  • Extreme Value Inverse CDF VI
  • F Inverse CDF VI
  • Gamma Inverse CDF VI
  • Laplace Inverse CDF VI
  • Logistic Inverse CDF VI
  • Lognormal Inverse CDF VI
  • Normal Inverse CDF VI
  • Pareto Inverse CDF VI
  • Rayleigh Inverse CDF VI
  • Student t Inverse CDF VI
  • Triangular Inverse CDF VI
  • Uniform Inverse CDF VI
  • Weibull Inverse CDF VI


                                                    © National Instruments 3531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3532 ordinal=3532 -->
## Functions

Functions

      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   BetaBeta InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •      a —

           a specifies the first shape parameter of the beta variate.

               •     b —

          b specifies the second shape parameter of the beta variate.

               •      x —

           x specifies the quantile of the continuous random variate and is bounded by the interval [0, 1].


3532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3533 ordinal=3533 -->
## Functions

Functions

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
CauchyCauchy InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •      a —

    a specifies the location parameter and median of the variate.

   •     b —


                                                    © National Instruments 3533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3534 ordinal=3534 -->
## Functions

Functions


          b specifies the scale parameter of the variate and must be greater than 0.

               •      x —

           x is the quantile of the continuous random variate.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   Chi-SquaredChi-Squared InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —


3534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3535 ordinal=3535 -->
## Functions

Functions


     cdf(x) is the cumulative probability Prob[X ≤ x].

   •     k —

    k specifies the number of degrees of freedom and must be greater than 0.

   •      x —

    x is the quantile of the continuous random variate with range x is greater than or equal to 0.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
Chi-SquaredChi-Squared (Non-Central)(Non-Central) InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


                                                    © National Instruments 3535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3536 ordinal=3536 -->
## Functions

Functions

      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •     k —

           k specifies the number of degrees of freedom and must be greater than 0.

               •     d —

          d specifies the noncentrality parameter, which must be greater than 0.

               •      x —

           x is the quantile of the continuous random variate with range x is greater than or equal to 0.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   ExpExp InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.

3536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3537 ordinal=3537 -->
## Functions

Functions


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •      a —

    a specifies the offset parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •      x —

    x is the quantile of the continuous random variate with range x is greater than or equal to a.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3538 ordinal=3538 -->
## Functions

Functions

   ExtremeExtreme ValueValue InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •      a —

           a specifies the location parameter and median of the variate.

               •     b —

          b specifies the scale parameter of the variate.

               •      x —

           x is the quantile of the continuous random variate.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)


3538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3539 ordinal=3539 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
FF InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •      k1 —

    k1 specifies the number of degrees of freedom of the first chi-squared variate that forms the F
     variate. k1 must be greater than 0.

   •      k2 —

    k2 specifies the number of degrees of freedom of the second chi-squared variate that forms the
    F variate. k2 must be greater than 0.

   •      x —

    x is the quantile of the continuous random variate with range x is greater than or equal to 0.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3540 ordinal=3540 -->
## Functions

Functions

      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
  GammaGamma InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •      x —

           x is the quantile of the continuous random variate with range x is greater than or equal to 0.


3540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3541 ordinal=3541 -->
## Functions

Functions

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
LaplaceLaplace InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •      a —

    a specifies the location or mean parameter of the variate.

   •     b —


                                                    © National Instruments 3541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3542 ordinal=3542 -->
## Functions

Functions


          b specifies the scale or median parameter of the variate and must be greater than 0.

               •      x —

           x is the quantile of the continuous random variate with range x is greater than or equal to 0.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    LogisticLogistic InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —


3542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3543 ordinal=3543 -->
## Functions

Functions


     cdf(x) is the cumulative probability Prob[X ≤ x].

   •      a —

    a specifies the location or mean parameter of the variate.

   •     b —

   b specifies the scale or median parameter of the variate and must be greater than 0.

   •      x —

    x is the quantile of the continuous random variate.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
LognormalLognormal InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


                                                    © National Instruments 3543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3544 ordinal=3544 -->
## Functions

Functions


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •     b —

          b specifies the scale or median parameter of the variate and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •      x —

           x is the quantile of the continuous random variate with range x is greater than or equal to 0.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi


3544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3545 ordinal=3545 -->
## Functions

Functions

NormalNormal InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •     mean —

   mean specifies the location or mean parameter of the variate.

   •       std —

    std specifies the scale or standard deviation parameter of the variate and must be greater than 0.

   •      x —

    x is the quantile of the continuous random variate.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)


                                                    © National Instruments 3545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3546 ordinal=3546 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    ParetoPareto InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •      a —

           a specifies the location parameter and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •      x —

           x is the quantile of the continuous random variate with range x is greater than or equal to 0.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that

3546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3547 ordinal=3547 -->
## Functions

Functions

the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
RayleighRayleigh InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •     b —

   b specifies the scale or median parameter of the variate and must be greater than 0.

   •      x —

    x is the quantile of the continuous random variate with range x is greater than or equal to 0.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3548 ordinal=3548 -->
## Functions

Functions

      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   StudentStudent tt InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •     k degrees of freedom —

           k degrees of freedom specifies the number of degrees of freedom and must be greater than 0.

               •      x —

           x specifies the quantile of the continuous random variate.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3549 ordinal=3549 -->
## Functions

Functions

The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
TriangularTriangular InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •     xmin —

    xmin specifies the lower limit parameter of the variate.

   •     xmode —

   xmode specifies the mode parameter of the variate. The default is NaN, which corresponds to a
   mode at the midpoint between xmin and xmax.

   •     xmax —


                                                    © National Instruments 3549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3550 ordinal=3550 -->
## Functions

Functions


         xmax specifies the upper limit parameter of the variate.

               •      x —

           x is the quantile of the continuous random variate and within the interval [xmin, xmax].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   UniformUniform InverseInverse CDFCDF VIVI

      Computes the continuous inverse cumulative distribution function (CDF) of the various
        distributions. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —


3550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3551 ordinal=3551 -->
## Functions

Functions


     cdf(x) is the cumulative probability Prob[X ≤ x].

   •     xmin —

    xmin specifies the lower limit parameter of the variate.

   •     xmax —

   xmax specifies the upper limit parameter of the variate.

   •      x —

    x is the quantile of the continuous random variate and within the interval [xmin, xmax].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to it.

Prob[X ≤ x] = cdf(x)
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
WeibullWeibull InverseInverse CDFCDF VIVI

Computes the continuous inverse cumulative distribution function (CDF) of the various
distributions. You must manually select the polymorphic instance to use.


                                                    © National Instruments 3551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3552 ordinal=3552 -->
## Functions

Functions


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •      a —

           a specifies the scale parameter of the variate and must be greater than 0.

               •     b —

          b specifies the shape parameter of the variate and must be greater than 0.

               •      x —

           x is the quantile of the continuous random variate with range x is greater than or equal to 0.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The Beta Inverse CDF instance finds the value x such that cdf(x) is the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to it.

       Prob[X ≤ x] = cdf(x)
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi


3552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3553 ordinal=3553 -->
## Functions

Functions

ContinuousContinuous PDFPDF

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


  • Beta PDF VI
  • Cauchy PDF VI
  • Chi-Squared PDF VI
  • Chi-Squared (Non-Central) PDF VI
  • Exp PDF VI
  • Extreme Value PDF VI
  • F PDF VI
  • Gamma PDF VI
  • Laplace PDF VI
  • Logistic PDF VI
  • Lognormal PDF VI
  • Normal PDF VI
  • Pareto PDF VI
  • Rayleigh PDF VI
  • Student t PDF VI
  • Triangular PDF VI
  • Uniform PDF VI
  • Weibull PDF VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3554 ordinal=3554 -->
## Functions

Functions

   BetaBeta PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate and is bounded by the interval [0, 1].

               •      a —

           a specifies the first shape parameter of the beta variate.

               •     b —

          b specifies the second shape parameter of the beta variate.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi


3554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3555 ordinal=3555 -->
## Functions

Functions

CauchyCauchy PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate.

   •      a —

    a specifies the location parameter and median of the variate.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3556 ordinal=3556 -->
## Functions

Functions

   Chi-SquaredChi-Squared PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ 0.

               •     k —

           k specifies the number of degrees of freedom and must be greater than 0.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   Chi-SquaredChi-Squared (Non-Central)(Non-Central) PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.


3556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3557 ordinal=3557 -->
## Functions

Functions

You must manually select the polymorphic instance to use.


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •     k —

    k specifies the number of degrees of freedom and must be greater than 0.

   •     d —

   d specifies the noncentrality parameter, which must be greater than 0.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
ExpExp PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.

                                                    © National Instruments 3557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3558 ordinal=3558 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ a.

               •      a —

           a specifies the offset parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   ExtremeExtreme ValueValue PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


3558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3559 ordinal=3559 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate.

   •      a —

    a specifies the location parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
FF PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3560 ordinal=3560 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ 0.

               •      k1 —

           k1 specifies the number of degrees of freedom of the first chi-squared variate that forms the F
              variate. k1 must be greater than 0.

               •      k2 —

           k2 specifies the number of degrees of freedom of the second chi-squared variate that forms the
           F variate. k2 must be greater than 0.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
  GammaGamma PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


3560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3561 ordinal=3561 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •      c —

    c specifies the shape parameter of the variate and must be greater than 0.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
LaplaceLaplace PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3562 ordinal=3562 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate.

               •      a —

           a specifies the location or mean parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    LogisticLogistic PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


3562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3563 ordinal=3563 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate.

   •      a —

    a specifies the location or mean parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
LognormalLognormal PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3564 ordinal=3564 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ 0.

               •     b —

          b specifies the scale or median parameter of the variate and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   NormalNormal PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


3564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3565 ordinal=3565 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate.

   •     mean —

   mean specifies the location or mean parameter of the variate.

   •       std —

    std specifies the scale or standard deviation parameter of the variate and must be greater than 0.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
ParetoPareto PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3566 ordinal=3566 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate with range x ≥ a.

               •      a —

           a specifies the location parameter and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    RayleighRayleigh PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


3566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3567 ordinal=3567 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
StudentStudent tt PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3568 ordinal=3568 -->
## Functions

Functions

      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate.

               •     k degrees of freedom —

           k degrees of freedom specifies the number of degrees of freedom and must be greater than 0.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    TriangularTriangular PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      x —


3568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3569 ordinal=3569 -->
## Functions

Functions


    x specifies the quantile of the continuous random variate and is bounded by the interval [xmin,
    xmax].

   •     xmin —

    xmin specifies the lower limit parameter of the variate.

   •     xmode —

   xmode specifies the mode parameter of the variate. The default is NaN, which corresponds to a
   mode at the midpoint between xmin and xmax.

   •     xmax —

   xmax specifies the upper limit parameter of the variate.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
UniformUniform PDFPDF VIVI

Computes the continuous probability density function (PDF) of various distributions.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3570 ordinal=3570 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the quantile of the continuous random variate and is bounded by the interval [xmin,
           xmax].

               •     xmin —

          xmin specifies the lower limit parameter of the variate.

               •     xmax —

         xmax specifies the upper limit parameter of the variate.

               •       pdf(x) —

             pdf(x) is the probability density function at x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    WeibullWeibull PDFPDF VIVI

      Computes the continuous probability density function (PDF) of various distributions.
      You must manually select the polymorphic instance to use.


3570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3571 ordinal=3571 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate with range x ≥ 0.

   •      a —

    a specifies the location parameter and must be greater than 0.

   •     b —

   b specifies the shape parameter of the variate and must be greater than 0.

   •       pdf(x) —

    pdf(x) is the probability density function at x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi

ContinuousContinuous RandomRandom

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


                                                    © National Instruments 3571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3572 ordinal=3572 -->
## Functions

Functions

            • Beta Random VI
            • Cauchy Random VI
            • Chi-Squared Random VI
            • Chi-Squared (Non-Central) Random VI
            • Exp Random VI
            • Extreme Value Random VI
            • F Random VI
            • Gamma Random VI
            • Laplace Random VI
            • Logistic Random VI
            • Lognormal Random VI
            • Normal Random VI
            • Pareto Random VI
            • Rayleigh Random VI
            • Student t Random VI
            • Triangular Random VI
            • Uniform Random VI
            • Weibull Random VI
   BetaBeta RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —


3572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3573 ordinal=3573 -->
## Functions

Functions


    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •      a —

    a specifies the first shape parameter of the beta variate.

   •     b —

   b specifies the second shape parameter of the beta variate.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      beta random data —

    beta random data contains randomized data distributed according to the beta distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

CauchyCauchy RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.


                                                    © National Instruments 3573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3574 ordinal=3574 -->
## Functions

Functions

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •      a —

           a specifies the location parameter and median of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •     Cauchy random data —

          Cauchy random data contains randomized data distributed according to the Cauchy
              distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   Chi-SquaredChi-Squared RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —


3574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3575 ordinal=3575 -->
## Functions

Functions


     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •     k —

    k specifies the number of degrees of freedom and must be greater than 0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      chi-squared random data —

    chi-squared random data contains randomized data distributed according to the chi-squared
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

Chi-SquaredChi-Squared (Non-Central)(Non-Central) RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —


                                                    © National Instruments 3575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3576 ordinal=3576 -->
## Functions

Functions


              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     k —

           k specifies the number of degrees of freedom and must be greater than 0.

               •     d —

          d specifies the noncentrality parameter, which must be greater than 0.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      chi-squared(nc) random data —

            chi-squared(nc) random data contains randomized data distributed according to the non-
             central chi-squared distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   ExpExp RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


3576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3577 ordinal=3577 -->
## Functions

Functions

Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •      a —

    a specifies the offset parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      exp random data —

    exp random data contains randomized data distributed according to the exponential
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

ExtremeExtreme ValueValue RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


                                                    © National Instruments 3577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3578 ordinal=3578 -->
## Functions

Functions


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •      a —

           a specifies the location parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      extreme value random numbers —

           extreme value random numbers contains randomized data distributed according to the extreme
            value distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   FF RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.

3578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3579 ordinal=3579 -->
## Functions

Functions


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •      k1 —

    k1 specifies the number of degrees of freedom of the first chi-squared variate that forms the F
     variate. k1 must be greater than 0.

   •      k2 —

    k2 specifies the number of degrees of freedom of the second chi-squared variate that forms the
    F variate. k2 must be greater than 0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •         f random numbers —

      f random numbers contains randomized data distributed according to the F distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3580 ordinal=3580 -->
## Functions

Functions

  GammaGamma RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •    gamma random numbers —

         gamma random numbers contains randomized data distributed according to the gamma
              distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3581 ordinal=3581 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.

LaplaceLaplace RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •      a —

    a specifies the location or mean parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      Laplace random numbers —

    Laplace random numbers contains randomized data distributed according to the Laplace
     distribution.


                                                    © National Instruments 3581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3582 ordinal=3582 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

    LogisticLogistic RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •      a —

           a specifies the location or mean parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •       logistic random data —


3582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3583 ordinal=3583 -->
## Functions

Functions


     logistic random data contains randomized data distributed according to the logistic
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

LognormalLognormal RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •     b —

   b specifies the scale or median parameter of the variate and must be greater than 0.

   •      c —

    c specifies the shape parameter of the variate and must be greater than 0.

   •      seed —


                                                    © National Instruments 3583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3584 ordinal=3584 -->
## Functions

Functions


            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      Lognormal random numbers —

           Lognormal random numbers contains randomized data distributed according to the lognormal
              distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   NormalNormal RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     mean —

         mean specifies the location or mean parameter of the variate.

               •       std —


3584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3585 ordinal=3585 -->
## Functions

Functions


    std specifies the scale or standard deviation parameter of the variate and must be greater than 0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      normal random data —

    normal random data contains randomized data distributed according to the normal
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

ParetoPareto RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •      a —


                                                    © National Instruments 3585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3586 ordinal=3586 -->
## Functions

Functions


           a specifies the location parameter and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      Pareto random data —

            Pareto random data contains randomized data distributed according to the Pareto distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

    RayleighRayleigh RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.


3586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3587 ordinal=3587 -->
## Functions

Functions

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      Rayleigh random data —

    Rayleigh random data contains randomized data distributed according to the Rayleigh
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

StudentStudent tt RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •     k degrees of freedom —


                                                    © National Instruments 3587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3588 ordinal=3588 -->
## Functions

Functions


           k degrees of freedom specifies the number of degrees of freedom and must be greater than 0.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      Student t random data —

           Student t random data contains randomized data distributed according to the Student's t
              distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

    TriangularTriangular RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     xmin —


3588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3589 ordinal=3589 -->
## Functions

Functions


    xmin specifies the lower limit parameter of the variate.

   •     xmode —

   xmode specifies the mode parameter of the variate. The default is NaN, which corresponds to a
   mode at the midpoint between xmin and xmax.

   •     xmax —

   xmax specifies the upper limit parameter of the variate.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •       triangular random data —

    triangular random data contains randomized data distributed according to the triangular
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

UniformUniform RandomRandom VIVI

Generates random values from a variate X, where X describes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —


                                                    © National Instruments 3589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3590 ordinal=3590 -->
## Functions

Functions


              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     xmin —

          xmin specifies the lower limit parameter of the variate.

               •     xmax —

         xmax specifies the upper limit parameter of the variate.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      uniform random data —

           uniform random data contains randomized data distributed according to the uniform
              distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

    WeibullWeibull RandomRandom VIVI

       Generates random values from a variate X, where X describes the selected distribution
       type. You must manually select the polymorphic instance to use.


3590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3591 ordinal=3591 -->
## Functions

Functions

Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •      a —

    a specifies the location parameter and must be greater than 0.

   •     b —

   b specifies the shape parameter of the variate and must be greater than 0.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      Weibull random numbers —

    Weibull random numbers contains randomized data distributed according to the Weibull
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


ContinuousContinuous MomentsMoments

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3592 ordinal=3592 -->
## Functions

Functions

            • Beta Moments VI
            • Chi-Squared Moments VI
            • Chi-Squared (Non-Central) Moments VI
            • Exp Moments VI
            • Extreme Value Moments VI
            • F Moments VI
            • Gamma Moments VI
            • Laplace Moments VI
            • Logistic Moments VI
            • Lognormal Moments VI
            • Normal Moments VI
            • Pareto Moments VI
            • Rayleigh Moments VI
            • Student t Moments VI
            • Triangular Moments VI
            • Uniform Moments VI
            • Weibull Moments VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   BetaBeta MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


3592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3593 ordinal=3593 -->
## Functions

Functions

Inputs/Outputs

   •      a —

    a specifies the first shape parameter of the beta variate.

   •     b —

   b specifies the second shape parameter of the beta variate.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
Chi-SquaredChi-Squared MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3594 ordinal=3594 -->
## Functions

Functions

      Inputs/Outputs

               •     k —

           k specifies the number of degrees of freedom and must be greater than 0.

               •     mean —

         mean is the expected mean of a chi-squared variate with the given parameter k.

               •      variance —

            variance is the expected variance of a chi-squared variate with the given parameter k.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   Chi-SquaredChi-Squared (Non-Central)(Non-Central) MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •     k —

3594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3595 ordinal=3595 -->
## Functions

Functions


    k specifies the number of degrees of freedom and must be greater than 0.

   •     d —

   d specifies the noncentrality parameter, which must be greater than 0.

   •     mean —

   mean is the expected mean of a chi-squared variate with the given parameter k.

   •      variance —

    variance is the expected variance of a chi-squared variate with the given parameter k.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
ExpExp MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3596 ordinal=3596 -->
## Functions

Functions

      Inputs/Outputs

               •      a —

           a specifies the offset parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   ExtremeExtreme ValueValue MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


3596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3597 ordinal=3597 -->
## Functions

Functions

Inputs/Outputs

   •      a —

    a specifies the location parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
FF MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3598 ordinal=3598 -->
## Functions

Functions

      Inputs/Outputs

               •      k1 —

           k1 specifies the number of degrees of freedom of the first chi-squared variate that forms the F
              variate. k1 must be greater than 0.

               •      k2 —

           k2 specifies the number of degrees of freedom of the second chi-squared variate that forms the
           F variate. k2 must be greater than 0.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
  GammaGamma MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


3598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3599 ordinal=3599 -->
## Functions

Functions


Inputs/Outputs

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •      c —

    c specifies the shape parameter of the variate and must be greater than 0.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
LaplaceLaplace MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3600 ordinal=3600 -->
## Functions

Functions


      Inputs/Outputs

               •      a —

           a specifies the location or mean parameter of the variate.

               •     b —

          b specifies the scale parameter of the variate and must be greater than 0.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
    LogisticLogistic MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


3600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3601 ordinal=3601 -->
## Functions

Functions


Inputs/Outputs

   •      a —

    a specifies the location or mean parameter of the variate.

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
LognormalLognormal MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3602 ordinal=3602 -->
## Functions

Functions


      Inputs/Outputs

               •     b —

          b specifies the scale or median parameter of the variate and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   NormalNormal MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


3602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3603 ordinal=3603 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x specifies the quantile of the continuous random variate.

   •     mean —

   mean specifies the location or mean parameter of the variate.

   •       std —

    std specifies the scale or standard deviation parameter of the variate and must be greater than 0.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3604 ordinal=3604 -->
## Functions

Functions

    ParetoPareto MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      a —

           a specifies the location parameter and must be greater than 0.

               •      c —

            c specifies the shape parameter of the variate and must be greater than 0.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi


3604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3605 ordinal=3605 -->
## Functions

Functions

RayleighRayleigh MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •     b —

   b specifies the scale parameter of the variate and must be greater than 0.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi


                                                    © National Instruments 3605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3606 ordinal=3606 -->
## Functions

Functions

   StudentStudent tt MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •     k degrees of freedom —

           k degrees of freedom specifies the number of degrees of freedom and must be greater than 0.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi


3606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3607 ordinal=3607 -->
## Functions

Functions

TriangularTriangular MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •     xmin —

    xmin specifies the lower limit parameter of the variate.

   •     xmode —

   xmode specifies the mode parameter of the variate. The default is NaN, which corresponds to a
   mode at the midpoint between xmin and xmax.

   •     xmax —

   xmax specifies the upper limit parameter of the variate.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3608 ordinal=3608 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi
   UniformUniform MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •     xmin —

          xmin specifies the lower limit parameter of the variate.

               •     xmax —

         xmax specifies the upper limit parameter of the variate.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3609 ordinal=3609 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Continuous Probability Distributions.vi
WeibullWeibull MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      a —

    a specifies the location parameter and must be greater than 0.

   •     b —

   b specifies the shape parameter of the variate and must be greater than 0.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3610 ordinal=3610 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Continuous Probability Distributions.vi

       DiscreteDiscrete CDFCDF

      Computes the discrete cumulative distribution function (CDF), or the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


            • Bernoulli CDF VI
            • Binomial CDF VI
            • Geometric CDF VI
            • Hypergeometric CDF VI
            • Neg Binomial CDF VI
            • Poisson CDF VI
            • Uniform (Discrete) CDF VI

     When you use the Bernoulli instance of this function, X represents a Bernoulli-
       distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
      The Bernoulli probability parameter p is the probability of success of a single trial or
       experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi


3610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3611 ordinal=3611 -->
## Functions

Functions

BernoulliBernoulli CDFCDF VIVI

Computes the discrete cumulative distribution function (CDF), or the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x is the number of successes and must be 0 or 1.

   •     p —

   p is the probability of success (probability that x = 1) and must be in the interval [0,1].

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Bernoulli instance of this function, X represents a Bernoulli-
distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
The Bernoulli probability parameter p is the probability of success of a single trial or
experiment.

Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 3611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3612 ordinal=3612 -->
## Functions

Functions

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   BinomialBinomial CDFCDF VIVI

      Computes the discrete cumulative distribution function (CDF), or the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x is the number of successes and must be in the interval [0,n].

               •     n —

          n is the number of independent Bernoulli trials.

               •     p —

          p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Bernoulli instance of this function, X represents a Bernoulli-


3612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3613 ordinal=3613 -->
## Functions

Functions

distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
The Bernoulli probability parameter p is the probability of success of a single trial or
experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
GeometricGeometric CDFCDF VIVI

Computes the discrete cumulative distribution function (CDF), or the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •     n —

   n is the number of independent Bernoulli trials.

   •     p —

   p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

   •       cdf(n) —

     cdf(n) is the cumulative probability Prob[X ≤ n].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 3613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3614 ordinal=3614 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


     When you use the Bernoulli instance of this function, X represents a Bernoulli-
       distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
      The Bernoulli probability parameter p is the probability of success of a single trial or
       experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   HypergeometricHypergeometric CDFCDF VIVI

      Computes the discrete cumulative distribution function (CDF), or the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x is the number of successes out of the sample of n items drawn from the population.

               •    M —

       M is the number of elements in the population.

               •     k —


3614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3615 ordinal=3615 -->
## Functions

Functions


    k is the number of successes in the population.

   •     n —

   n is the number of items drawn without replacement.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Bernoulli instance of this function, X represents a Bernoulli-
distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
The Bernoulli probability parameter p is the probability of success of a single trial or
experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
NegNeg BinomialBinomial CDFCDF VIVI

Computes the discrete cumulative distribution function (CDF), or the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to x. You must manually select the polymorphic instance to
use.


                                                    © National Instruments 3615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3616 ordinal=3616 -->
## Functions

Functions


      Inputs/Outputs

               •      y —

           y is the number of failures before the xth success.

               •      x —

           x is the number of successes and must be in the interval [0,inf].

               •     p —

          p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

               •       cdf(y) —

             cdf(y) is the cumulative probability Prob[X ≤ y].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Bernoulli instance of this function, X represents a Bernoulli-
       distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
      The Bernoulli probability parameter p is the probability of success of a single trial or
       experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi


3616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3617 ordinal=3617 -->
## Functions

Functions

PoissonPoisson CDFCDF VIVI

Computes the discrete cumulative distribution function (CDF), or the probability that
the random variate X, where Xdescribes the selected distribution type, takes on a
value less than or equal to x. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •      x —

    x is the number of events and must be greater than or equal to 0.

   •     lambda —

   lambda is the average number of events expected to occur within a specific time interval.

   •       cdf(x) —

     cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
    selected distribution type, has a value less than or equal to x.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When you use the Bernoulli instance of this function, X represents a Bernoulli-
distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
The Bernoulli probability parameter p is the probability of success of a single trial or
experiment.

Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 3617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3618 ordinal=3618 -->
## Functions

Functions

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   UniformUniform (Discrete)(Discrete) CDFCDF VIVI

      Computes the discrete cumulative distribution function (CDF), or the probability that
       the random variate X, where Xdescribes the selected distribution type, takes on a
       value less than or equal to x. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x is an integer in the range of [0,n].

               •     n —

          n is the maximum value of the uniform variate.

               •       cdf(x) —

             cdf(x) returns the cumulative probability that the random variate X, where Xdescribes the
             selected distribution type, has a value less than or equal to x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When you use the Bernoulli instance of this function, X represents a Bernoulli-
       distributed variate with one of two possible outcomes: success (x = 1) or failure (x = 0).
      The Bernoulli probability parameter p is the probability of success of a single trial or
       experiment.


3618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3619 ordinal=3619 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi

DiscreteDiscrete InverseInverse CDFCDF

Computes the discrete inverse cumulative distribution function (CDF), or the value x
such that the probability that the random variate X, where Xdescribes the selected
distribution type, takes on a value less than or equal to it is cdf(x). You must manually
select the polymorphic instance to use.


  • Bernoulli Inverse CDF VI
  • Binomial Inverse CDF VI
  • Geometric Inverse CDF VI
  • Hypergeometric Inverse CDF VI
  • Neg Binomial Inverse CDF VI
  • Poisson Inverse CDF VI
  • Uniform (Discrete) Inverse CDF VI

When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
probability parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi


                                                    © National Instruments 3619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3620 ordinal=3620 -->
## Functions

Functions

    BernoulliBernoulli InverseInverse CDFCDF VIVI

      Computes the discrete inverse cumulative distribution function (CDF), or the value x
      such that the probability that the random variate X, where Xdescribes the selected
        distribution type, takes on a value less than or equal to it is cdf(x). You must manually
        select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •     p —

          p is the probability of success (probability that x = 1) and must be in the interval [0,1].

               •      x —

           x is the number of successes, and will be either 0 or 1.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
       with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
       probability parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\

3620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3621 ordinal=3621 -->
## Functions

Functions

   Display Discrete Probability Distributions.vi
BinomialBinomial InverseInverse CDFCDF VIVI

Computes the discrete inverse cumulative distribution function (CDF), or the value x
such that the probability that the random variate X, where Xdescribes the selected
distribution type, takes on a value less than or equal to it is cdf(x). You must manually
select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •     n —

   n is the number of independent Bernoulli trials.

   •     p —

   p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

   •      x —

    x is the number of successes and must be in the interval [0,n]

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
probability parameter p is the probability of success of a single trial or experiment.


                                                    © National Instruments 3621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3622 ordinal=3622 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   GeometricGeometric InverseInverse CDFCDF VIVI

      Computes the discrete inverse cumulative distribution function (CDF), or the value x
      such that the probability that the random variate X, where Xdescribes the selected
        distribution type, takes on a value less than or equal to it is cdf(x). You must manually
        select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(n) —

             cdf(n) is the cumulative probability Prob[X ≤ n].

               •     p —

          p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

               •     n —

          n is the number of independent Bernoulli trials.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
       with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli

3622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3623 ordinal=3623 -->
## Functions

Functions

probability parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
HypergeometricHypergeometric InverseInverse CDFCDF VIVI

Computes the discrete inverse cumulative distribution function (CDF), or the value x
such that the probability that the random variate X, where Xdescribes the selected
distribution type, takes on a value less than or equal to it is cdf(x). You must manually
select the polymorphic instance to use.


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •    M —

   M is the number of elements in the population.

   •     k —

    k is the number of successes in the population.

   •     n —

   n is the number of items drawn without replacement.

   •      x —


                                                    © National Instruments 3623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3624 ordinal=3624 -->
## Functions

Functions


           x is the number of successes out of the sample of n items drawn from the population.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
       with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
       probability parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   NegNeg BinomialBinomial InverseInverse CDFCDF VIVI

      Computes the discrete inverse cumulative distribution function (CDF), or the value x
      such that the probability that the random variate X, where Xdescribes the selected
        distribution type, takes on a value less than or equal to it is cdf(x). You must manually
        select the polymorphic instance to use.


      Inputs/Outputs

               •       cdf(y) —

             cdf(y) is the cumulative probability Prob[X ≤ y].

               •      x —


3624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3625 ordinal=3625 -->
## Functions

Functions


    x is the number of successes and must be in the interval [0,inf].

   •     p —

   p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

   •      y —

    y is the number of failures before the xth success.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
probability parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
PoissonPoisson InverseInverse CDFCDF VIVI

Computes the discrete inverse cumulative distribution function (CDF), or the value x
such that the probability that the random variate X, where Xdescribes the selected
distribution type, takes on a value less than or equal to it is cdf(x). You must manually
select the polymorphic instance to use.


                                                    © National Instruments 3625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3626 ordinal=3626 -->
## Functions

Functions

      Inputs/Outputs

               •       cdf(x) —

             cdf(x) is the cumulative probability Prob[X ≤ x].

               •     lambda —

          lambda is the average number of events expected to occur within a specific time interval.

               •      x —

           x is the number of events and must be greater than or equal to 0.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
       with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
       probability parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   UniformUniform (Discrete)(Discrete) InverseInverse CDFCDF VIVI

      Computes the discrete inverse cumulative distribution function (CDF), or the value x
      such that the probability that the random variate X, where Xdescribes the selected
        distribution type, takes on a value less than or equal to it is cdf(x). You must manually
        select the polymorphic instance to use.


3626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3627 ordinal=3627 -->
## Functions

Functions


Inputs/Outputs

   •       cdf(x) —

     cdf(x) is the cumulative probability Prob[X ≤ x].

   •     n —

   n is the maximum value of the uniform variate.

   •      x —

    x is an integer in the range of [0,n].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


When using the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate
with one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
probability parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi

DiscreteDiscrete PFPF

Computes the discrete probability function (PF), or the probability that the random
variate X, where Xdescribes the selected distribution type, takes on the value n. You
must manually select the polymorphic instance to use.


                                                    © National Instruments 3627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3628 ordinal=3628 -->
## Functions

Functions


            • Bernoulli PF VI
            • Binomial PF VI
            • Geometric PF VI
            • Hypergeometric PF VI
            • Neg Binomial PF VI
            • Poisson PF VI
            • Uniform (Discrete) PF VI

        In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
       possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
      parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
    BernoulliBernoulli PFPF VIVI

      Computes the discrete probability function (PF), or the probability that the random
        variate X, where Xdescribes the selected distribution type, takes on the value n. You
      must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      x —

           x is the number of successes and must be 0 or 1.

               •     p —

3628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3629 ordinal=3629 -->
## Functions

Functions


   p is the probability of success (probability that x = 1) and must be in the interval [0,1].

   •      prob(x) —

    prob(x) is the probability Prob[X = x].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
BinomialBinomial PFPF VIVI

Computes the discrete probability function (PF), or the probability that the random
variate X, where Xdescribes the selected distribution type, takes on the value n. You
must manually select the polymorphic instance to use.


Inputs/Outputs

   •      x —

    x is the number of successes and must be in the interval [0,n].


                                                    © National Instruments 3629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3630 ordinal=3630 -->
## Functions

Functions

               •     n —

          n is the number of independent Bernoulli trials.

               •     p —

          p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

               •      prob(x) —

            prob(x) is the probability Prob[X = x].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
       possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
      parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   GeometricGeometric PFPF VIVI

      Computes the discrete probability function (PF), or the probability that the random
        variate X, where Xdescribes the selected distribution type, takes on the value n. You
      must manually select the polymorphic instance to use.


3630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3631 ordinal=3631 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x is the number of failures before the first success and must be greater than or equal to 0.

   •     p —

   p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

   •      prob(x) —

    prob(x) is the probability Prob[X = x].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
HypergeometricHypergeometric PFPF VIVI

Computes the discrete probability function (PF), or the probability that the random
variate X, where Xdescribes the selected distribution type, takes on the value n. You
must manually select the polymorphic instance to use.


                                                    © National Instruments 3631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3632 ordinal=3632 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x is the number of successes out of the sample of n items drawn from the population.

               •    M —

       M is the number of elements in the population.

               •     k —

           k is the number of successes in the population.

               •     n —

          n is the number of items drawn without replacement.

               •      prob(x) —

            prob(x) is the probability Prob[X = x].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
       possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
      parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi


3632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3633 ordinal=3633 -->
## Functions

Functions

NegNeg BinomialBinomial PFPF VIVI

Computes the discrete probability function (PF), or the probability that the random
variate X, where Xdescribes the selected distribution type, takes on the value n. You
must manually select the polymorphic instance to use.


Inputs/Outputs

   •      y —

    y is the number of failures before the xth success.

   •      x —

    x is the number of successes and must be in the interval [0,inf].

   •     p —

   p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

   •      prob(y) —

    prob(y) is the probability Prob[X = y].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.


                                                    © National Instruments 3633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3634 ordinal=3634 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   PoissonPoisson PFPF VIVI

      Computes the discrete probability function (PF), or the probability that the random
        variate X, where Xdescribes the selected distribution type, takes on the value n. You
      must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      x —

           x is the number of events and must be greater than or equal to 0.

               •     lambda —

          lambda is the average number of events expected to occur within a specific time interval.

               •      prob(x) —

            prob(x) is the probability Prob[X = x].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
       possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
      parameter p is the probability of success of a single trial or experiment.

3634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3635 ordinal=3635 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
UniformUniform (Discrete)(Discrete) PFPF VIVI

Computes the discrete probability function (PF), or the probability that the random
variate X, where Xdescribes the selected distribution type, takes on the value n. You
must manually select the polymorphic instance to use.


Inputs/Outputs

   •      x —

    x is an integer in the range of [0,n].

   •     n —

   n is the maximum value of the uniform variate.

   •      prob(x) —

    prob(x) is the probability Prob[X = x].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


In the Bernoulli instance, X represents a Bernoulli-distributed variate with one of two
possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

                                                    © National Instruments 3635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3636 ordinal=3636 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi

       DiscreteDiscrete RandomRandom

       Generates random values from a variate X, where Xdescribes the selected distribution
       type. You must manually select the polymorphic instance to use.


            • Bernoulli Random VI
            • Binomial Random VI
            • Geometric Random VI
            • Hypergeometric Random VI
            • Neg Binomial Random VI
            • Poisson Random VI
            • Random Permutation VI
            • Uniform (Discrete) Random VI
    BernoulliBernoulli RandomRandom VIVI

       Generates random values from a variate X, where Xdescribes the selected distribution
       type. You must manually select the polymorphic instance to use.

     When using the Bernoulli instance, X represents a Bernoulli-distributed variate with
      one of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli
       probability parameter p is the probability of success of a single trial or experiment.


3636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3637 ordinal=3637 -->
## Functions

Functions


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •     p —

   p is the probability of success (probability that x = 1) and must be in the interval [0,1].

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •       Bernoulli random numbers —

    Bernoulli random numbers contains randomized data distributed according to the Bernoulli
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

BinomialBinomial RandomRandom VIVI

Generates random values from a variate X, where Xdescribes the selected distribution
type. You must manually select the polymorphic instance to use.


                                                    © National Instruments 3637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3638 ordinal=3638 -->
## Functions

Functions


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     n —

          n is the number of independent Bernoulli trials.

               •     p —

          p is the probability of success (probability that x = 1) and must be in the interval [0,1].

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      binomial random data —

           binomial random data contains randomized data distributed according to the binomial
              distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   GeometricGeometric RandomRandom VIVI

       Generates random values from a variate X, where Xdescribes the selected distribution
       type. You must manually select the polymorphic instance to use.

3638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3639 ordinal=3639 -->
## Functions

Functions


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •     p —

   p is the probability of success (probability that x = 1) and must be in the interval [0,1].

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •      geometric random data —

    geometric random data contains randomized data distributed according to the geometric
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

HypergeometricHypergeometric RandomRandom VIVI

Generates random values from a variate X, where Xdescribes the selected distribution
type. You must manually select the polymorphic instance to use.


                                                    © National Instruments 3639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3640 ordinal=3640 -->
## Functions

Functions


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •    M —

       M is the number of elements in the population.

               •     k —

           k is the number of successes in the population.

               •     n —

          n is the number of items drawn without replacement.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      hypergeometric random data —

           hypergeometric random data contains randomized data distributed according to the
            hypergeometric distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3641 ordinal=3641 -->
## Functions

Functions

NegNeg BinomialBinomial RandomRandom VIVI

Generates random values from a variate X, where Xdescribes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •      samples —

    samples specifies the number of samples the output array contains. samples must be greater
    than or equal to 0. The default is 128.

   •      x —

    x is the number of successes and must be in the interval [0,inf].

   •     p —

   p is the probability of success (probability that x = 1) and must be in the interval [0,1].

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •     neg binomial random data —

    neg binomial random contains randomized data distributed according to the negative binomial
     distribution.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 3641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3642 ordinal=3642 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.

   PoissonPoisson RandomRandom VIVI

       Generates random values from a variate X, where Xdescribes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     lambda —

          lambda is the average number of events expected to occur within a specific time interval.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      Poisson random data —

           poisson random data contains randomized data distributed according to the Poisson
              distribution.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3643 ordinal=3643 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.

RandomRandom PermutationPermutation VIVI

Generates random values from a variate X, where Xdescribes the selected distribution
type. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •       reset —

     reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

   •    N —

   N sets the size of the random permutation by shuffling the sequence start..start+N–1.

   •       start —

     start sets the starting value of the random permutation by shuffling the sequence
     start..start+N–1.

    With start = 1 (default), LabVIEW generates a random permutation of the sequence 1, 2, …, N.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

   •     random permutation —

   random permutation contains randomized data generated by shuffling the sequence
     start..start+N–1.

   •       error —


                                                    © National Instruments 3643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3644 ordinal=3644 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   UniformUniform (Discrete)(Discrete) RandomRandom VIVI

       Generates random values from a variate X, where Xdescribes the selected distribution
       type. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •       reset —

              reset, if TRUE, resets the seed to the seed control value. The default is FALSE.

               •      samples —

           samples specifies the number of samples the output array contains. samples must be greater
           than or equal to 0. The default is 128.

               •     n —

          n is the maximum value of the uniform variate.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

               •      uniform (discrete) random data —

           uniform (discrete) random data contains randomized data distributed according to the uniform
              distribution.

               •       error —


3644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3645 ordinal=3645 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


DiscreteDiscrete MomentsMoments

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


  • Bernoulli Moments VI
  • Binomial Moments VI
  • Geometric Moments VI
  • Hypergeometric Moments VI
  • Neg Binomial Moments VI
  • Poisson Moments VI
  • Uniform (Discrete) Moments VI

In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
BernoulliBernoulli MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to

                                                    © National Instruments 3645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3646 ordinal=3646 -->
## Functions

Functions

       use.


      Inputs/Outputs

               •     p —

          p is the probability of success (probability that x = 1) and must be in the interval [0,1].

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
       of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
      parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   BinomialBinomial MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes

3646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3647 ordinal=3647 -->
## Functions

Functions

the selected distribution type. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •     n —

   n is the number of independent Bernoulli trials.

   •     p —

   p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi


                                                    © National Instruments 3647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3648 ordinal=3648 -->
## Functions

Functions

   GeometricGeometric MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •     p —

          p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
       of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
      parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi

3648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3649 ordinal=3649 -->
## Functions

Functions

HypergeometricHypergeometric MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •    M —

   M is the number of elements in the population.

   •     k —

    k is the number of successes in the population.

   •     n —

   n is the number of items drawn without replacement.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

                                                    © National Instruments 3649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3650 ordinal=3650 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   NegNeg BinomialBinomial MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •      x —

           x is the number of successes and must be in the interval [0,inf].

               •     p —

          p is the probability of success of each Bernoulli trial and must be in the interval [0,1].

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3651 ordinal=3651 -->
## Functions

Functions

In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi
PoissonPoisson MomentsMoments VIVI

Returns the expected mean and variance of the random variate X, where Xdescribes
the selected distribution type. You must manually select the polymorphic instance to
use.


Inputs/Outputs

   •     lambda —

   lambda is the average number of events expected to occur within a specific time interval.

   •     mean —

   mean is the expected mean of a variate with the given parameters.

   •      variance —

    variance is the expected variance of a variate with the given parameters.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3652 ordinal=3652 -->
## Functions

Functions

        In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
       of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
      parameter p is the probability of success of a single trial or experiment.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Probability and Statistics\
        Display Discrete Probability Distributions.vi
   UniformUniform (Discrete)(Discrete) MomentsMoments VIVI

       Returns the expected mean and variance of the random variate X, where Xdescribes
       the selected distribution type. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •     n —

          n is the maximum value of the uniform variate.

               •     mean —

         mean is the expected mean of a variate with the given parameters.

               •      variance —

            variance is the expected variance of a variate with the given parameters.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3653 ordinal=3653 -->
## Functions

Functions

In the Bernoulli instance of the VI, X represents a Bernoulli-distributed variate with one
of two possible outcomes: success (x = 1) or failure (x = 0). The Bernoulli probability
parameter p is the probability of success of a single trial or experiment.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Display Discrete Probability Distributions.vi

HypothesisHypothesis TestingTesting

Use the Hypothesis Testing VIs to test hypotheses about a population.

The VIs on this palette can return mathematics error codes.


 Palette Object  Description

                  Tests hypotheses about the mean of a population whose distribution is at least
 T Test                approximately normal but whose variance is unknown.


                  Tests hypotheses about the mean of a population whose distribution is at least
 Z Test
                approximately normal and whose variance is known.


 Correlation
                  Tests hypotheses about the association between two variables xand y. Test


                  Tests hypotheses about the median of continuous distributions. You must
 Sign Test
               manually select the polymorphic instance to use.


                                                    © National Instruments 3653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3654 ordinal=3654 -->
## Functions

Functions


         Palette Object  Description

        Wilcoxon        Tests hypotheses about the mean of populations whose distributions are
        Signed Rank    continuous and symmetric but not necessarily normal. You must manually select
         Test            the polymorphic instance to use.


                        Finds the rank order of each element in the x input and returns the order of each       Rank                      element in the rank order x output. For all tied rank values, the mean rank
         Transformation                         replaces the rank returned.


                     Computes the Pearson χ² test for independence. This function is used to test        Contingency                      whether the row and column categorical variables of the contingency table are         Table VI
                        independent.


     TT TestTest

       Tests hypotheses about the mean of a population whose distribution is at least
       approximately normal but whose variance is unknown.

      As in all hypothesis tests, the hypotheses are statements about the population, not
      about the sample set.


      Inputs/Outputs

               •     sample set —

           sample set specifies the randomly sampled data from the population of interest.

               •     mean —

         mean specifies the hypothesized mean value of the population. The null hypothesis is that the


3654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3655 ordinal=3655 -->
## Functions

Functions


  population mean is equal to mean.

  The mean of a normal distribution is a value of a normal random variable such that the
  probability that an observed value of the variable is less than or equal to the mean and the
  probability that the observed value is greater than or equal to the mean are both 50%.

•       significance level —

  significance level specifies the probability that the hypothesis test conclusion is wrong based on
  the sample set and the hypothesized mean.

•       alternative hypothesis —

  alternative hypothesis specifies the hypothesis to accept if LabVIEW rejects the null hypothesis
  that the population mean is equal to mean.

  –1 mean(pop) < mean—The population mean is less than mean.
  0  mean(pop) != mean—The population mean is not equal to mean.
  1  mean(pop) > mean—The population mean is greater than mean.

•       reject null hypothesis —

  reject null hypothesis indicates whether to reject the null hypothesis, with significance level
  being the probability of reaching the wrong conclusion.

   If p value is less than or equal to significance level, reject null hypothesis returns TRUE. Reject
  the null hypothesis and accept the alternative hypothesis. If p value is greater than significance
   level, reject null hypothesis returns FALSE. Accept the null hypothesis and reject the alternative
  hypothesis.

•     p value —

  p value returns the probability that you incorrectly rejected the null hypothesis.

•      confidence interval —

  confidence interval returns a lower and upper limit for the population mean, indicating the
  uncertainty in the estimate of the true population mean.

      •      low —


                                                   © National Instruments 3655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3656 ordinal=3656 -->
## Functions

Functions


              low returns the lower limit of the estimate of the population mean.

                     •      high —

                high returns the upper limit of the estimate of the population mean.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •        t test info —

               t test info returns the sample statistics used in the computation of the T test.

                     •     sample mean —

              sample mean returns the sample mean of the sample set.

                     •     sample std —

              sample std returns the sample standard deviation of the sample set.

                     •     sample se mean —

              sample se mean returns the standard error mean of the sample set.

                     •     sample t value —

              sample t value returns the sample test statistic used in the T test and is equal to (sample
            mean – mean)/(sample se mean).

                     •        t value —

                    t value returns the T value that corresponds to the significance level and the alternative
                hypothesis.


3656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3657 ordinal=3657 -->
## Functions

Functions

ZZ TestTest

Tests hypotheses about the mean of a population whose distribution is at least
approximately normal and whose variance is known.

As in all hypothesis tests, the hypotheses are statements about the population, not
about the sample set.


Inputs/Outputs

   •     sample set —

    sample set specifies the randomly sampled data from the population of interest.

   •     mean —

   mean specifies the hypothesized mean value of the population. The null hypothesis is that the
    population mean is equal to mean.

    The mean of a normal distribution is a value of a normal random variable such that the
     probability that an observed value of the variable is less than or equal to the mean and the
     probability that the observed value is greater than or equal to the mean are both 50%.

   •       significance level —

    significance level specifies the probability that the hypothesis test conclusion is wrong based on
    the sample set and the hypothesized mean.

   •       std —

    std specifies the known standard deviation of the population.

   •       alternative hypothesis —

    alternative hypothesis specifies the hypothesis to accept if LabVIEW rejects the null hypothesis
    that the population mean is equal to mean.


                                                    © National Instruments 3657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3658 ordinal=3658 -->
## Functions

Functions


           –1 mean(pop) < mean—The population mean is less than mean.
           0  mean(pop) != mean—The population mean is not equal to mean.
           1  mean(pop) > mean—The population mean is greater than mean.

               •       reject null hypothesis —

             reject null hypothesis indicates whether to reject the null hypothesis, with significance level
            being the probability of reaching the wrong conclusion.

                    If p value is less than or equal to significance level, reject null hypothesis returns TRUE. Reject
            the null hypothesis and accept the alternative hypothesis. If p value is greater than significance
              level, reject null hypothesis returns FALSE. Accept the null hypothesis and reject the alternative
             hypothesis.

               •     p value —

          p value returns the probability that you incorrectly rejected the null hypothesis.

               •      confidence interval —

            confidence interval returns a lower and upper limit for the population mean, indicating the
             uncertainty in the estimate of the true population mean.

                     •      low —

              low returns the lower limit of the estimate of the population mean.

                     •      high —

                high returns the upper limit of the estimate of the population mean.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      z test info —

            z test info returns the sample statistics used in the computation of the Z test.

                     •     sample mean —


3658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3659 ordinal=3659 -->
## Functions

Functions


       sample mean returns the sample mean of the sample set.

         •     sample std —

       sample std returns the sample standard deviation of the sample set.

         •     sample se mean —

       sample se mean returns the standard error mean of the sample set.

         •     sample z value —

       sample z value returns the sample test statistic used in the Z test and is equal to (sample
      mean – mean)/(sample se mean).

         •      z value —

         z value returns the Z value that corresponds to the significance level and the alternative
        hypothesis.


CorrelationCorrelation TestTest

Tests hypotheses about the association between two variables xand y.


Inputs/Outputs

   •     sample set x —

    sample set x contains the sampled data from the first variable x.

   •     sample set y —


                                                    © National Instruments 3659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3660 ordinal=3660 -->
## Functions

Functions


           sample set y contains the sampled data from the second variable y.

               •      type —

           type specifies the type of correlation test to perform.

           0        Pearson
           1       Spearman
           2         Kendall

               •       significance level —

             significance level specifies the probability that the hypothesis test conclusion is wrong based on
            the sample set x and sample set y.

               •       alternative hypothesis —

             alternative hypothesis specifies the hypothesis to accept if LabVIEW rejects the null hypothesis
             that the variables xand yare uncorrelated.

           –1  r > 0—The correlation coefficient r is greater than 0.
           0    r != 0—The correlation coefficient r is not equal to 0.
           1    r < 0—The correlation coefficient r is less than 0.

               •       reject null hypothesis —

             reject null hypothesis indicates whether to reject the null hypothesis, with significance level
            being the probability of reaching the wrong conclusion.

                    If p value is less than or equal to significance level, reject null hypothesis returns TRUE. Reject
            the null hypothesis and accept the alternative hypothesis. If p value is greater than significance
              level, reject null hypothesis returns FALSE. Accept the null hypothesis and reject the alternative
             hypothesis.

               •     p value —

          p value returns the probability that you incorrectly rejected the null hypothesis.

               •       rsig —

              rsig returns the minimum value of the correlation coefficient for which you should reject the null


3660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3661 ordinal=3661 -->
## Functions

Functions


    hypothesis.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •       correlation coefficient r —

    correlation coefficient r returns the linear correlation coefficient between xand y.


SignSign TestTest

Tests hypotheses about the median of continuous distributions. You must manually
select the polymorphic instance to use.

As in all hypothesis tests, the hypotheses are statements about the population, not
about the sample set. The sign test is a nonparametric test that makes no assumption
about the distribution of the underlying population.


  • Sign Test (median) VI
  • Sign Test (paired samples) VI
SignSign TestTest (median)(median) VIVI

Tests hypotheses about the median of continuous distributions. You must manually
select the polymorphic instance to use.

As in all hypothesis tests, the hypotheses are statements about the population, not
about the sample set. The sign test is a nonparametric test that makes no assumption
about the distribution of the underlying population.


                                                    © National Instruments 3661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3662 ordinal=3662 -->
## Functions

Functions


      Inputs/Outputs

               •     sample set —

           sample set specifies the randomly sampled data from the population of interest.

               •     median —

          median specifies the hypothesized median value of the population. The null hypothesis is that
            the population median is equal to median.

          The median of a distribution is a value of a random variable such that the probability that an
           observed value of the variable is less than or equal to the median and the probability that the
           observed value is greater than or equal to the median are both 50%.

               •       significance level —

             significance level specifies the probability that the hypothesis test conclusion is wrong based on
            the sample set and the hypothesized median.

               •       alternative hypothesis —

             alternative hypothesis specifies the hypothesis to accept if LabVIEW rejects the null hypothesis
             that the population median is equal to median.

           –1 median(pop) < median—The population median is less than median.
           0  median(pop) != median—The population median is not equal to median.
           1  median(pop) > median—The population median is greater than median.

               •       reject null hypothesis —

             reject null hypothesis indicates whether to reject the null hypothesis, with significance level
            being the probability of reaching the wrong conclusion.

                    If p value is less than or equal to significance level, reject null hypothesis returns TRUE. Reject
            the null hypothesis and accept the alternative hypothesis. If p value is greater than significance
              level, reject null hypothesis returns FALSE. Accept the null hypothesis and reject the alternative
             hypothesis.

               •     p value —

3662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3663 ordinal=3663 -->
## Functions

Functions


   p value returns the probability that you incorrectly rejected the null hypothesis.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

SignSign TestTest (paired(paired samples)samples) VIVI

Tests hypotheses about the median of continuous distributions. You must manually
select the polymorphic instance to use.

As in all hypothesis tests, the hypotheses are statements about the population, not
about the sample set. The sign test is a nonparametric test that makes no assumption
about the distribution of the underlying population.


Inputs/Outputs

   •     sample set x —

    sample set x contains the sampled data from the first variable x.

   •     sample set y —

    sample set y contains the sampled data from the second variable y.

   •       significance level —

    significance level specifies the probability that the hypothesis test conclusion is wrong based on
    the paired samples sets.

   •       alternative hypothesis —


                                                    © National Instruments 3663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3664 ordinal=3664 -->
## Functions

Functions


             alternative hypothesis specifies the hypothesis to accept if LabVIEW rejects the null hypothesis
             that the two variable populations have a common median. If the null hypothesis is true, the
          median of the differences between sample set x and sample set y is zero.

             median(x) < median(y)–The median of the first population is less than the median of the           –1             second population.
             median(x) != median(y)–The median of the first population is not equal to the median of the
           0             second population.
             median(x) > median(y)–The median of the first population is greater than the median of the           1             second population.

               •       reject null hypothesis —

             reject null hypothesis indicates whether to reject the null hypothesis, with significance level
            being the probability of reaching the wrong conclusion.

                    If p value is less than or equal to significance level, reject null hypothesis returns TRUE. Reject
            the null hypothesis and accept the alternative hypothesis. If p value is greater than significance
              level, reject null hypothesis returns FALSE. Accept the null hypothesis and reject the alternative
             hypothesis.

               •     p value —

          p value returns the probability that you incorrectly rejected the null hypothesis.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      WilcoxonWilcoxon SignedSigned RankRank TestTest

       Tests hypotheses about the mean of populations whose distributions are continuous
      and symmetric but not necessarily normal. You must manually select the polymorphic
       instance to use.

      As in all hypothesis tests, the hypotheses are statements about the population, not
      about the sample set.


3664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3665 ordinal=3665 -->
## Functions

Functions


  • Wilcoxon Signed-Rank Test (mean) VI
  • Wilcoxon Signed-Rank Test (paired samples) VI
WilcoxonWilcoxon Signed-RankSigned-Rank TestTest (mean)(mean) VIVI

Tests hypotheses about the mean of populations whose distributions are continuous
and symmetric but not necessarily normal. You must manually select the polymorphic
instance to use.

As in all hypothesis tests, the hypotheses are statements about the population, not
about the sample set.


Inputs/Outputs

   •     sample set —

    sample set specifies the randomly sampled data from the population of interest.

   •     mean —

   mean specifies the hypothesized mean value of the population. The null hypothesis is that the
    population mean is equal to mean.

    The mean of a symmetrical distribution is a value of a random variable such that the probability
    that an observed value of the variable is less than or equal to the mean and the probability that
    the observed value is greater than or equal to the mean are both 50%.

   •       significance level —

    significance level specifies the probability that the hypothesis test conclusion is wrong based on
    the sample set and the hypothesized mean.

   •       alternative hypothesis —


                                                    © National Instruments 3665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3666 ordinal=3666 -->
## Functions

Functions


             alternative hypothesis specifies the hypothesis to accept if LabVIEW rejects the null hypothesis
             that the population mean is equal to mean.

           –1 mean(pop) < mean—The population mean is less than mean.
           0  mean(pop) != mean—The population mean is not equal to mean.
           1  mean(pop) > mean—The population mean is greater than mean.

               •       reject null hypothesis —

             reject null hypothesis indicates whether to reject the null hypothesis, with significance level
            being the probability of reaching the wrong conclusion.

                    If p value is less than or equal to significance level, reject null hypothesis returns TRUE. Reject
            the null hypothesis and accept the alternative hypothesis. If p value is greater than significance
              level, reject null hypothesis returns FALSE. Accept the null hypothesis and reject the alternative
             hypothesis.

               •     p value —

          p value returns the probability that you incorrectly rejected the null hypothesis.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   WilcoxonWilcoxon Signed-RankSigned-Rank TestTest (paired(paired samples)samples)
    VIVI

       Tests hypotheses about the mean of populations whose distributions are continuous
      and symmetric but not necessarily normal. You must manually select the polymorphic
       instance to use.

           Note


3666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3667 ordinal=3667 -->
## Functions

Functions


        Tests hypotheses about the mean of two populations whose distributions are
       continuous and differ only in their means.


Inputs/Outputs

   •     sample set x —

    sample set x contains the sampled data from the first variable x.

   •     sample set y —

    sample set y contains the sampled data from the second variable y.

   •       significance level —

    significance level specifies the probability that the hypothesis test conclusion is wrong based on
    the sample set x and sample set y.

   •       alternative hypothesis —

    alternative hypothesis specifies the hypothesis to accept if LabVIEW rejects the null hypothesis
    that the two variable populations have a common mean.

      mean(x) < mean(y)–The mean of the first population is less than the mean of the second
    –1
       population.
      mean(x) != mean(y)–The mean of the first population is not equal to the mean of the second
    0
       population.
      mean(x) > mean(y)–The mean of the first population is greater than the mean of the second
    1
       population.

   •       reject null hypothesis —

     reject null hypothesis indicates whether to reject the null hypothesis, with significance level
    being the probability of reaching the wrong conclusion.


                                                    © National Instruments 3667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3668 ordinal=3668 -->
## Functions

Functions


                    If p value is less than or equal to significance level, reject null hypothesis returns TRUE. Reject
            the null hypothesis and accept the alternative hypothesis. If p value is greater than significance
              level, reject null hypothesis returns FALSE. Accept the null hypothesis and reject the alternative
             hypothesis.

               •     p value —

          p value returns the probability that you incorrectly rejected the null hypothesis.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     RankRank TransformationTransformation

       Finds the rank order of each element in the x input and returns the order of each
      element in the rank order x output. For all tied rank values, the mean rank replaces
       the rank returned.

      Rank transformations often are used to test hypotheses on data when an underlying
        distribution is unknown.


      Inputs/Outputs

               •      x —

           x is the data to rank.

               •      rank order x —

           rank order x is the rank order of each element in x.

               •     tsum - measure of ties —

          tsum - measure of ties is the sum of (tm3-tm), where tmis the number of ties in the mth group


3668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3669 ordinal=3669 -->
## Functions

Functions


     of ties.


ContingencyContingency TableTable VIVI

Computes the Pearson χ² test for independence. This function is used to test whether
the row and column categorical variables of the contingency table are independent.


Inputs/Outputs

   •      Table —

    Table is the input contingency table of counts or frequencies.

   •      x —

    x is the calculated Pearson's χ² test statistic.

   •       probability —

     probability, or p value, returns the probability of observing a sample statistic as extreme as the
     test statistic. If this value is less than a desired significance level, you should conclude that there
      is a relationship between the row and column variables.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Contingency Table VI uses the χ² test of homogeneity and the χ² test of
independence to test your hypothesis. Before testing your hypothesis, decide upon a
minimum value for probability for each test. The minimum value you decide upon for
probability is the value at which you accept or reject the hypothesis. Ordinarily, you
want to choose a small value for probability. 0.05 is a common choice. If the actual
value of probability returned by the VI is less than the value you decide upon, consider


                                                    © National Instruments 3669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3670 ordinal=3670 -->
## Functions

Functions

        rejecting the hypothesis.

      With the χ² test of homogeneity, the VI takes a random sample of some fixed size from
      each of the categories in one categorization scheme. For each of the samples, the VI
       categorizes the objects of experimentation according to the second scheme and tallies
      them. The VI tests the hypothesis to determine whether the populations from which
      each sample is taken are identically distributed with respect to the second
       categorization scheme.

      With the χ² test of independence, the VI takes only one sample from the total
       population. The VI then categorizes each object and tallies it in two categorization
      schemes. The VI tests the hypothesis that the categorization schemes are
       independent.

     Formulas

       Let yp, q be the number of occurrences in the (pq)th cell of the contingency table for

   p= 0, 1, …, (s– 1) and q= 0, 1, …, (k– 1),

      where sis the number of rows in the Contingency Table, and kis the number of
      columns in the Contingency Table.

       Let


3670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3671 ordinal=3671 -->
## Functions

Functions

The VI uses x to calculate the probability

p= Prob{X≥ x}

where Xis a random variable from the χ² distribution. If the hypothesis is true, x came
from a χ² distribution with (s– 1) and (k– 1) degrees of freedom.

AnalysisAnalysis ofof VarianceVariance

Use the Analysis of Variance VIs to perform analysis of variance functions.

The VIs on this palette can return mathematics error codes.

      Note The Analysis of Variance VIs can accept and convert input levels that do
       not begin with zero or input levels that have nonconsecutive values. For
        instance, if you enter an index that contains the levels 3, 5, and 7, the VIs on
         this palette automatically convert the levels to an index array with level
        values of 0, 1, and 2.


 Palette         Description Object

 1D      Takes an array, X, of experimental observations made at various levels of a factor, with at
 ANOVA  least one observation per level, and performs a one-way analysis of variance in the fixed
 VI        effect model.


 2D
         Takes an array of experimental observations made at various levels of two factors and
 ANOVA
         performs a two-way analysis of variance.
 VI

 3D
         Takes an array of experimental observations made at various levels of three factors and
 ANOVA
         performs a three-way analysis of variance.
 VI


                                                    © National Instruments 3671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3672 ordinal=3672 -->
## Functions

Functions

     1D1D ANOVAANOVA VIVI

      Takes an array, X, of experimental observations made at various levels of a factor, with
       at least one observation per level, and performs a one-way analysis of variance in the
        fixed effect model.


      Inputs/Outputs

               •     X —

          X contains all the observational data.

               •      Index —

            Index contains the level to which the corresponding observation belongs.

               •      # of levels —

           # of levels is the total number of levels.

               •         f —

                 f is a ratio where f = msa/mse.

               •      ssa —

            ssa is a measure of variation attributed to the factor.

               •      sse —

            sse is a measure of variation attributed to random fluctuation.

               •     mse —


3672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3673 ordinal=3673 -->
## Functions

Functions


   mse is the mean square quantity associated with sse. It is calculated by dividing sse by its own
    degree of freedom.

   •     msa —

   msa is the mean square quantity associated with ssa. It is calculated by dividing ssa by its
    degree of freedom.

   •       tss —

     tss is the total sum of squares, which is a measure of the total variation of the data from the
     overall population mean. It is calculated using tss = ssa + sse.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

   •       sig A —

     sig A, given a particular f, is the probability that you will get a value larger than f when sampling
    from an F distribution.


In the one-way analysis of variance, the VI tests whether the level of the factor has an
effect on the experimental outcome.

1D ANOVA Factors and Levels

A factor is a basis for categorizing data. For example, if you count the number of sit-ups
individuals can do, one basis of categorization is age. For age, you might have the
following levels.


 Level 0              6 years old to 10 years old

 Level 1              11 years old to 15 years old

 Level 2              16 years old to 20 years old

Now, suppose that you make a series of observations to see how many sit-ups people
can do. If you take a random sampling of five people, you might find the following


                                                    © National Instruments 3673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3674 ordinal=3674 -->
## Functions

Functions

        results.


        Person 1             8 years old (level 0)                           10 sit-ups

        Person 2             12 years old (level 1)                          15 sit-ups

        Person 3             16 years old (level 2)                          20 sit-ups

        Person 4             20 years old (level 2)                          25 sit-ups

        Person 5             13 years old (level 1)                          17 sit-ups

       Notice that you have made at least one observation per level. To perform an analysis of
       variance, you must make at least one observation per level.

      To perform the analysis of variance, you specify an array X of observations, with values
       10, 15, 20, 25, and 17. The array Index specifies the level (or category) to which each
       observation applies. In this case, Index has the values 0, 1, 2, 2, and 1. Finally, there are
       three possible levels, so you pass in a value of 3 for the # of levels parameter.

     1D ANOVA Statistical Model

       Performing the analysis of variance, you express each experimental outcome as the
     sum of three parts. Let xim be the mth observation from the ith level. Then each
       observation is written

     xim = µ + αi + εim

      where µ is a standard effect, called the overall mean.

        αi is the effect of the ith level of the factor, which is the difference between the mean of
       the ith level αi and the overall mean

        µ(µi) = µ + αi

      and εim is a random fluctuation.


3674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3675 ordinal=3675 -->
## Functions

Functions

1D ANOVA Hypothesis

This VI tests the hypothesis that αi = 0 for i= 0, 1, …, k– 1, where kis # of levels. In
other words, this hypothesis, referred to as the null hypothesis, states that no level
affects the experimental outcome and then looks for evidence to the contrary.

1D ANOVA Assumptions

Assume that the populations of measurements at each level are Normally distributed
with mean µi and variance σA², and assume that αi sum to zero. Finally, assume that
for each iand m, εim is Normally distributed with mean 0 and variance σA².

1D ANOVA General Method

This VI computes the total sum of squares, tss, which is a measure of the total variation
of the data from the overall population mean.

tss consists of two parts: ssa, a measure of variation attributed to the factor, and sse, a
measure of variation attributed to random fluctuation. In other words,

tss = ssa + sse.

The VI computes the two mean square quantities msa and mse from ssa and sse by
dividing ssa and sse by their own degrees of freedom. The larger msa is relative to
mse, the more significant effect the factor has on the experimental outcome.

In particular, if the null hypothesis is true, then the ratio f, f = msa/mse, is taken from
an F distribution with k– 1 and n– kdegrees of freedom, from which you can
calculate probabilities. Given a particular f, sigA is the probability that you get a value
larger than f when sampling from this distribution.

Testing the 1D ANOVA Hypothesis

Determine when to reject the null hypothesis by deciding how likely you want it to be
that you mistakenly reject the null hypothesis. This is the level of significance, a
common choice is 0.05. The output sigA is compared to the chosen level of significance
to determine whether to accept or reject the null hypothesis. If sigA is less than the


                                                    © National Instruments 3675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3676 ordinal=3676 -->
## Functions

Functions

      chosen level of significance, reject the null hypothesis. If you reject the null hypothesis,
      you must acknowledge that at least one level has some effect on the experimental
      outcome.

     1D ANOVA Formulas

       Let xim = the mth observation made at the ith level for m= 0, 1, …, ni – 1 and i= 0, 1,
     …, k– 1, where ni is the number of observations at the ith level and k= # of levels.


      then


       SigA = Prob{Fk– 1, n– k > f}

     Fk– 1, n– k


3676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3677 ordinal=3677 -->
## Functions

Functions

is the F distribution with k– 1 and n– kdegrees of freedom.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Probability and Statistics\
   Unbalanced ANOVA on Rainfall Data.vi

2D2D ANOVAANOVA VIVI

Takes an array of experimental observations made at various levels of two factors and
performs a two-way analysis of variance.


Inputs/Outputs

   •     A levels —

   A levels contains the number of levels in factor A. The sign of A levels is set to positive if A is fixed
    and negative if A is random.

   •     X —

    X contains all the observational data.

   •      Index A —

    Index A contains the level of factor A to which the corresponding observation belongs.

   •      Index B —

    Index B contains the level of factor B to which the corresponding observation belongs.

   •      observations per cell —


                                                    © National Instruments 3677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3678 ordinal=3678 -->
## Functions

Functions


            observations per cell is the number of observations in each cell. It is the same for all cells.

               •     B levels —

         B levels contains the number of levels in factor B. The sign of B levels is set to positive if B is
              fixed and negative if B is random.

               •       Info —

             Info is a 4-by-4 matrix organized where the first column corresponds to the sum of squares
            associated with factor A, factor B, AB interaction, and residual error. The second column
            corresponds to the respective degrees of freedom. The third column corresponds to the
             respective mean squares. The fourth column corresponds to the respective F values.


               •       sig A —

              sig A is the computed level of significance associated with factor A.

               •       sig B —

              sig B is the computed level of significance associated with factor B.

               •       sig AB —

              sig AB is the computed level of significance associated with the interaction of factors A and B.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D ANOVA Factors, Levels, and Cells

      A factor is a basis for categorizing data. For example, if you count the number of sit-ups
       individuals can do, one basis of categorization is age. For age, you might have the
       following levels:


         Level 0              6 years old to 10 years old

3678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3679 ordinal=3679 -->
## Functions

Functions


 Level 1              11 years old to 15 years old

Another possible factor is weight, with the following levels:


 Level 0                     less than 50 kg

 Level 1                between 50 and 75 kg

 Level 2               more than 75 kg

Now, suppose that you made a series of observations to see how many sit-ups people
could do. If you took a random sampling of npeople, you might find the following
results:


 Person 1        8 years old (level 0)                30 kg (level 0)           10 sit-ups

 Person 2        12 years old (level 1)               40 kg (level 0)           15 sit-ups

 Person 3        15 years old (level 1)               76 kg (level 2)           20 sit-ups

 Person 4        14 years old (level 1)               60 kg (level 1)           25 sit-ups

 Person 5        9 years old (level 0)                51 kg (level 1)           17 sit-ups

 Person 6        10 years old (level 0)               80 kg (level 2)           4 sit ups

and so on.

If you plot observations as a function of factor A and factor B, they fall into cells of a
matrix with factor A as rows and factor B as columns. Each cell must contain at least
one observation, and each cell must contain the same number of observations.

To perform the analysis of variance, you specify an array X of observations, with values
10, 15, 20, 25, 17, and 4. The array Index A specifies the level (or category) of factor A to
which each observation applies. In this case, the array would have the values 0, 1, 1, 1,
0, and 0.

The array Index B specifies the level (or category) of factor B to which each observation
applies. In this case, the array would have the values 0, 0, 2, 1, 1, and 2. Finally, there
are two possible levels for factor A and three possible levels for factor B, so you pass in


                                                    © National Instruments 3679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3680 ordinal=3680 -->
## Functions

Functions

      a value of 2 for the A levels parameter and a value of 3 for the B levels parameter.

      You can apply any one of the following models, where Lis the specified observations
      per cell:

            • Model 1: Fixed-effects with no interaction and one observation per cell (per
           specified levels x and y of the factors A and B, respectively).
            • Model 2: Fixed-effects with interaction and L> 1 observations per cell.
            • Model 3: Either of the fixed-effects models with interaction and L> 1 observations
          per cell.
            • Model 4: Random-effects with interaction and L> 1 observations per cell.

     2D ANOVA Random and Fixed Effects

      A factor is a random effect if it has a large population of levels about which you want to
      draw conclusions but such that you cannot sample from all levels. You thus pick levels
       at random and hope to generalize about all levels. A factor is a fixed effect if you can
      sample from all levels about which you want to draw conclusions.

      The input parameters A levels and B levels represent the number of levels in factors A
      and B, respectively, as well as whether the factors are random or fixed. For example, if
        factor A is random, you set A levels to be negative the number of levels in factor A.
       Notice that if there is only one observation per cell, both A levels and B levels must be
        positive. That is, you use model 1.

     2D ANOVA Statistical Model

       Let xpqr be the rth observation at the pth and qth levels of A and B respectively, where
    r= 0, 1, ..., L– 1.

      Model 1 expresses each observation as the sum of four components.

     xpqr = µ + αp + βq + εpqr

      Models 2, 3, and 4 express each observation as the sum of five components.

     xpqr = µ + αp + βq + (αβ)pq + εpqr

3680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3681 ordinal=3681 -->
## Functions

Functions

where

βq = µq – µ

  • µ is the overall mean response (the average of the mean response for all the
    populations).
  • αp is the effect of the pth level of factor A (equal to µp – µ where µp is the average
    of the pth level of factor A over all levels of factor B).
  • βq is the effect of the qth level of factor B (equal to µq – µ where µq is the average
    of the qth level of factor B over all levels of factor A).
  • (αβ)pq is the interaction between the pth level of factor A and the qth level of factor
   B (equal to µpq – (µ + αp + βq) where µpq is the population mean of the pqth cell).
  • εpqr is the deviation of xpqr from the population mean response for the pqth
    population.

2D ANOVA Hypotheses

Each of the following hypotheses is a different way of saying that a factor or an
interaction among factors has no effect on experimental outcomes. This VI assumes
that there are no effects and then seeks evidence to contradict this assumption. The
following are the three hypotheses:

  • (A) that αp = 0 for all levels pif factor A is fixed, and that σA² = 0 if factor A is
   random.
  • (B) that βq = 0 for all levels qif factor B is fixed, and that σB² = 0 if factor B is
   random.
  • (AB) that (αβ)pq = 0 for all levels pand qif both factors A and B are fixed, and that
    σA² = 0 if either factor A or factor B is random. (This does not apply to model 1. In
   model 1 there is no interaction, and the associated output parameters are
    superfluous.)

2D ANOVA Assumptions

The 2D ANOVA VI makes the following assumptions:


                                                    © National Instruments 3681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3682 ordinal=3682 -->
## Functions

Functions

            • Assume that for each p, q, and r, εpqr is Normally distributed with mean 0 and
           variance σe².
            •  If a factor such as A is fixed, assume that the populations of measurements at each
            level of A are Normally distributed with mean αp + µ and variance σA², and that all
          the populations at each of the levels have the same variance. In addition, assume
           that αp sum to zero. Analogous assumptions are made for B.
            •  If a factor such as A is random, assume that the effect of the level of A itself, αp, is a
        random variable Normally distributed with mean 0 and variance σe². Analogous
          assumptions are made for B.
            •  If all of the factors such as A and B associated with the effect of an interaction
         (αβ)pq are fixed, assume that the populations of measurements at each level are
          Normally distributed with mean µpq and variance σAB². For any fixed p, (αβ)pq
        sum to zero, when summing over all q. Similarly, for any fixed q, the means (αβ)pq
        sum to zero, when summing over all p.
            •  If any of the factors such as A and B associated with the effect of an interaction
         (αβ)pq are random, assume the effect is a random variable Normally distributed
          with mean 0 and variance σAB². If A is fixed but B is random, then also assume that
            for any fixed qthe means σAB² sum to zero, when summing over all p. Similarly, if
        B is fixed but A is random, assume that for any fixed pthe means σAB² sum to zero,
        when summing over all q.
            • Assume that all effects taken to be random variables are mutually independent.

     2D ANOVA General Method

        In each of the models, the VI breaks up the total sum of squares, tss, a measure of the
        total variation of the data from the overall population mean, into some number of
      component sums of squares. In model 1

        tss = ssa + ssb + sse

      whereas in models 2 through 4

        tss = ssa + ssb + ssab + sse

      Each component sum in tss is a measure of variation attributed to a certain factor or
       interaction among the factors. Here ssa is a measure of the variation due to factor A,

3682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3683 ordinal=3683 -->
## Functions

Functions

ssb is a measure of the variation due to factor B, ssab is a measure of the variation due
to the interaction between factors A and B, and sse is a measure of the variation due to
random fluctuation. Notice that with model 1 you have no ssab term. This is what no
interaction means.

The VI divides each of the values ssa, ssb, ssab, and sse by their own degrees of
freedom to compute the mean square quantities msa, msb, msab, and mse. If one
factor, such as factor A, has a strong effect on the experimental observations, the
respective mean square quantity msa will be relatively large.

Testing the 2D ANOVA Hypotheses

For each hypothesis, the VI computes a number f that is used to calculate the
associated sig probability. For example, for the hypothesis (A), that αp = 0 for all the
levels p, (fixed A), the VI computes


then

sigA = Prob{Fa– 1, (a– 1)(b– 1)} > fa

where

Fa– 1, (a– 1)(b– 1)

is an F distribution with degrees of freedom a– 1 and (a– 1)(b– 1). You then can use
the probabilities sigA, sigB, and sigAB to determine when you should reject the
associated hypotheses (A), (B), and (AB).

How do you know when to reject the null hypothesis? For each hypothesis, you choose
a level of significance. This level of significance is how likely you want it to be that you
mistakenly reject the hypothesis (a common choice is 0.05). Compare your chosen
level of significance with the associated sig probability output. If the sig probability is
less than your chosen level of significance, you should reject the null hypothesis.

For example, if A is a random effect, your chosen level of significance is 0.05, and the
output sigA is 0.03, then you must reject the hypothesis αA² = 0 and conclude that

                                                    © National Instruments 3683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3684 ordinal=3684 -->
## Functions

Functions

        factor A has an effect on the experimental observations.

     2D ANOVA Formulas

       Let xpqr be the rth observation at the pth and qth levels of A and B respectively, where
    r= 0, 1, …, L– 1.

       Let

   a= |A levels|

   b= |B levels|


      then


3684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3685 ordinal=3685 -->
## Functions

Functions


dofab= (a– 1)(b– 1) if L> 1

dofab= 0 if L= 1


dofe= ab(L– 1) if L> 1

dofe= (a– 1)(b– 1) if L= 1


sigA = Prob{Fa– 1, ab(L– 1) > fa}       if B is fixed

sigA = Prob{Fa– 1, (a– 1)(b– 1) > fa}   if B is random

sigB = Prob{Fa– 1, ab(L– 1) > fb}       if A is fixed

sigB = Prob{Fa– 1, (a– 1)(b– 1) > fb}   if A is random

sigAB = Prob{F(a– 1)(b– 1), ab(L– 1) > fab}

3D3D ANOVAANOVA VIVI

Takes an array of experimental observations made at various levels of three factors

                                                    © National Instruments 3685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3686 ordinal=3686 -->
## Functions

Functions

      and performs a three-way analysis of variance.


      Inputs/Outputs

               •      Levels —

            Levels is a cluster of three numeric values corresponding to number of levels in the A, B, and C
              factors, as well as the effects of the A, B, and C factors (fixed or random).

                     •      Level A —

                Level A is the number of levels in A if A is fixed, or the negative number of levels in A if A is
               random.

                     •      Level B —

                Level B is the number of levels in B if B is fixed, or the negative number of levels in B if B is
               random.

                     •      Level C —

                Level C is the number of levels in C if C is fixed, or the negative number of levels in C if C is
               random.


               •     X —

          X contains all the observational data.

               •      Index A —

            Index A contains the level of factor A to which the corresponding observation belongs.

               •      Index B —

            Index B contains the level of factor B to which the corresponding observation belongs.


3686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3687 ordinal=3687 -->
## Functions

Functions

•      Index C —

  Index C contains the level of factor C to which the corresponding observation belongs.

•      observations per cell —

  observations per cell is the number of observations in each cell. It is the same for all cells.

•       Info —

  Info is an 8 by 4 matrix organized where the first column corresponds to the sums of squares
  associated with the respective factors (A, B, C), the respective interactions (AB, AC, BC, ABC), and
  residual error.

  The second column corresponds to the respective degrees of freedom.

  The third column corresponds to the respective mean squares.

  The fourth column corresponds to the respective F values.


•       Significance —

  Significance is a cluster of seven numerical values corresponding to the significance levels.

      •       sig A —

       sig A is the computed level of significance associated with factor A.

      •       sig B —

       sig B is the computed level of significance associated with factor B.

      •       sig C —

       sig C is the computed level of significance associated with factor C.

      •       sig AB —


                                                   © National Instruments 3687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3688 ordinal=3688 -->
## Functions

Functions


                  sig AB is the computed level of significance associated with the interaction of factors A and
                  B.

                     •       sig AC —

                  sig AC is the computed level of significance associated with the interaction of factors A and
                  C.

                     •       sig BC —

                  sig BC is the computed level of significance associated with the interaction of factors B and
                  C.

                     •       sig ABC —

                  sig ABC is the computed level of significance associated with the interaction of factors A, B,
              and C.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


        In any ANOVA, you look for evidence that the factors or interactions among factors
      have a significant effect on experimental outcomes. What varies with each model is the
      method used to do this.

     3D ANOVA Random and Fixed Effects

      A factor is a random effect if it has a large population of levels about which you want to
      draw conclusions but such that you cannot sample from all levels. You thus pick levels
       at random and hope to generalize about all levels. A factor is a fixed effect if you can
      sample from all levels about which you want to draw conclusions.

     3D ANOVA Statistical Model

       Let xpqrs equation be the sth observation at the pth, qth, and rth levels of A, B, and C


3688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3689 ordinal=3689 -->
## Functions

Functions

respectively, where s= 0, 1, ..., L– 1. Express each observation as the sum of eight
components. Thus,

xpqrs = µ + αp + βq + γr + (αβ)pq + (αγ)pr + (βγ)qr + (αβγ)pqr + εpqrs

where

   • µ is the overall mean.
   • αp is the average effect of the pth level of factor A.
   • βq is the average effect of the qth level of factor B.
   • γr is the average effect of the rth level of factor C.
   • (αβ)pq is the two-factor interaction of the pth level of factor A with the qth level of
    factor B.
   • (αγ)pr is the two-factor interaction of the pth level of factor A with the rth level of
    factor C.
   • (βγ)qr is the two-factor interaction of the qth level of factor B with the rth level of
    factor C.
   • (αβγ)pqr is the three-factor interaction of the pth level of factor A, the qth level of
    factor B, and the rth level of factor C.
   • εpqrs is random fluctuation.

3D ANOVA Hypotheses

Each of the following hypotheses is a different way of saying that a factor or an
interaction among factors has no effect on experimental outcomes. This VI assumes
that there are no effects and then seeks evidence to contradict these assumptions. The
following are the seven hypotheses:

   • (A) that αp = 0 for all levels pif factor A is fixed, and that σA² = 0 if factor A is
   random.
   • (B) that βq = 0 for all levels qif factor B is fixed, and that σB² = 0 if factor B is
   random.
   • (C) that γr = 0 for all levels rif factor C is fixed, and that σC² = 0 if factor B is random.
   • (AB) that (αβ)pq = 0 for all levels pand qif factors A and B are fixed, and that σAB² =

                                                    © National Instruments 3689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3690 ordinal=3690 -->
## Functions

Functions

         0 if either factor A or B is random.
            • (AC) that (αγ)pr = 0 for all levels pand qif factors A and C are fixed, and that σAC² =
         0 if either factor A or C is random.
            • (BC) that (βγ)qr = 0 for all levels pand qif factors B and C are fixed, and that σBC² =
         0 if either factor B or C is random.
            • (ABC) that (αβγ)pqr = 0 for all levels p, q, and rif factors A, B, and C are fixed, and
           that σABC² = 0 if any of factors A, B, or C is random.

     3D ANOVA Assumptions

      The 3D ANOVA VI makes the following assumptions:

            • Assume that for each p, q, and r, εpqrs is Normally distributed with mean 0 and
           variance σe².
            •  If a factor A is fixed, assume the populations of measurements at each level of A are
          Normally distributed with mean αp + µ and variance σA² and that all the
          populations at each of the levels have the same variance. In addition, assume that
       αp sum to zero. Analogous assumptions are made for B and C.
            •  If a factor A is random, assume the effect of the level of A itself, αp, is a random
           variable Normally distributed with mean 0 and variance σA². Analogous
          assumptions are made for B and C.
            •  If some of the factors, such as A and B, associated with the effect of an interaction
          are (αβ)pq fixed, then assume that the populations of measurements at each level
           of A and B are Normally distributed with mean µ + αp + βq + (αβ)pq and variance
           σAB². For any fixed p, the means (αβ)pq sum to zero when summing over all q.
            Similarly, for any fixed q, (αβ)pq sum to zero when summing over all p.
            •  If any of the factors, such as A and B, associated with the effect of an interaction
         (αβ)pq are random, assume the effect is a random variable Normally distributed
          with mean 0 and variance σAB². If A is fixed but B is random, assume that for any
            fixed q, the means (αβ)pq sum to zero when summing over all p. Similarly, if B is
            fixed but A is random, assume that for any fixed pthe means (αβ)pq sum to zero
        when summing over all q.
            • Assume all effects taken to be random variables are mutually independent.


3690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3691 ordinal=3691 -->
## Functions

Functions

3D ANOVA General Method

In each of the models, the VI breaks up the total sum of squares, tss, a measure of the
total variation of the data from the overall population mean, into a number of
component sums of squares.

tss = ssa + ssb + ssc + ssab + ssac + ssbc + ssabc + sse

Each component in the sum tss is a measure of variation attributed to a certain factor
or interaction among the factors. Here ssa is a measure of the variation due to factor A;
ssb is a measure of the variation due to factor B; ssc is a measure of the variation due
to factor c; ssab is a measure of the variation due to the interaction between factors A
and B; and so on for ssac, ssbc, and ssabc. Also, sse is a measure of the variation due to
random fluctuation. The VI divides each by its own degrees of freedom to obtain the
corresponding averages msa, msb, msc, msab, msac, msbc, msabc, and mse. For
example, if factor A has a strong effect on the experimental observations, then msa will
be relatively large.

Testing the 3D ANOVA Hypotheses

For each hypothesis, the VI computes number f that is used to calculate the associated
sig probability. For example, for the hypothesis (A), that (p= 0 for all the levels p),
(fixed A), the VI computes


then

sigA = Prob{Fa– 1, abc(L– 1) > fa}

where

Fa– 1, abc(L– 1)

is an F distribution with degrees of freedom a – 1 and abc(L – 1). You then can use the
probabilities sigA, sigB, sigC, sigAB, …, sig ABC to determine when you should reject
the associated hypotheses (A), (B), (C), (AB), …, (ABC).


                                                    © National Instruments 3691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3692 ordinal=3692 -->
## Functions

Functions

     How do you know when to reject the null hypothesis? For each hypothesis, you choose
      a level of significance. This level of significance is how likely you want it to be that you
       mistakenly reject the hypothesis (a common choice is 0.05). Compare your chosen
        level of significance with the associated sig probability output. If the sig probability is
        less than your chosen level of significance, you should reject the null hypothesis. For
      example, if A is a random effect, your level of significance is 0.05, and sigA = 0.03, you
      must reject the hypothesis that σA² = 0 and conclude that factor A has an effect on the
       experimental observations.

      With some models there are no appropriate tests for certain hypotheses. If such is the
       case, the output parameters directly involved with the testing of these hypotheses are
        –1.0.

     3D ANOVA Formulas

       Let xpqrs be the sth observation at the pth, qth, and rth levels of A, B, and C
        respectively, where s= 0, 1, ..., L– 1.

       Let

   a= |A levels|

   b= |B levels|

    c= |C levels|

      then


3692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3693 ordinal=3693 -->
## Functions

Functions


© National Instruments 3693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3694 ordinal=3694 -->
## Functions

Functions


       StatisticsStatistics

       Returns the selected parameter of the first signal in a waveform.


      Dialog Box Options

        Option         Description

                        Contains the following options:

                                       • Arithmetic mean—

                              Calculates the mean, or average, of the values in Signals.

                                       • Median—          Statistical
         Calculations                            Finds the median value in Signals. The Express VI sorts the values in Signals
                        and selects the middle element of the sorted values.

                                       • Mode—

                            Finds the value that occurs most often in the values in Signals.


3694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3695 ordinal=3695 -->
## Functions

Functions


Option         Description

                          • Sum of values—

                     Calculates the value of the sum of all the values in Signals.

                          • Root mean square (RMS)—

                     Calculates the RMS of the values in Signals.

                          • Standard deviation—

                     Calculates the standard deviation of the values in Signals.

                          • Variance—

                     Calculates the calculated variance of the values in Signals.

                          • Kurtosis—

                     Calculates the kurtosis of the values in Signals. Kurtosis is a measure of
                  peakedness and is a normalized form of the fourth-order moment about the
                 mean.

                     Kurtosis is indicated by the following formula:

                     Kurtosis = Fourth Moment/σ4

                          • Skewness—

                     Calculates the skewness of the values in Signals. Skewness is a measure of
                 symmetry and is a normalized form of the third-order moment about the
                 mean.

                 Skewness is indicated by the following formula:

                 Skewness = Third Moment/σ3

               Contains the following options:

Extreme               • Maximum—
Values
                    Finds the highest point in a set of values in Signals.


                                                    © National Instruments 3695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3696 ordinal=3696 -->
## Functions

Functions


        Option         Description

                                       • Time of maximum—

                            Finds the time of the highest point in a set of values in Signals.

                                       • Index of maximum—

                            Finds the index value of the highest point in a set of values in Signals.

                                       • Minimum—

                            Finds the lowest point in a set of values in Signals.

                                       • Time of minimum—

                            Finds the time of the lowest point in a set of values in Signals.

                                       • Index of minimum—

                            Finds the index value of the lowest point in a set of values in Signals.

                                       • Range (maximum - minimum)—

                            Finds the value of the range from the lowest point to the highest point in a set
                               of values in Signals.

                                       •  First time—

                            Finds the first time value in a set of values in Signals.

                                       • Last time—

                            Finds the last time value in a set of values in Signals.

                                       •  First value—

                            Finds the first value in a set of values in Signals.

                                       • Last value—

                            Finds the last value in a set of values in Signals.

        Sampling      Contains the following options:


3696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3697 ordinal=3697 -->
## Functions

Functions


 Option         Description

                           •  Total number of samples—

                   Bases the calculation on the total number of samples in Signals.
 Characteristics
                           • Time between samples (dt)—

                   Bases the calculation on the time between samples in Signals.


                 Displays the input signal.

 Input Signal       If you wire data to the Express VI and run it, Input Signal displays real data. If you
                 close and reopen the Express VI, Input Signal displays sample data until you run
                the Express VI again.


                 Displays the measurements you configured this Express VI to perform and the
                 calculated values of those measurements. You can click any measurement listed in Results                the Measurement column, and the corresponding value or plot appears in the
                Result Preview graph.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •     Minimum —

    Returns the lowest point in a set of values in Signals.

   •     Range —

                                                    © National Instruments 3697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3698 ordinal=3698 -->
## Functions

Functions


            Returns the value of the range from the lowest point to the highest point in a set of values in
             Signals.

               •        First Value —

            Returns the first value in Signals.

               •      Last Value —

            Returns the last value in Signals.

               •      Arithmetic Mean —

            Returns the mean, or average, of the values in Signals.

               •      Standard Dev —

            Returns the standard deviation of the values in Signals.

               •     Median —

            Returns the median value in Signals. The Express VI sorts the values in Signals and selecting the
           middle element of the sorted values.

               •      Index of Min —

            Returns the index value of the lowest point of the values in Signals.

               •     Summation —

            Returns the value of the sum of all the values in Signals.

               •       Kurtosis —

            Returns the kurtosis of the values in Signals. Kurtosis is a measure of peakedness and
            corresponds to the fourth-order moment about the mean.

               •     Time of Maximum —

            Returns the time of the highest point of the values in Signals.

               •     Time of Minimum —

            Returns the time of the lowest point of the values in Signals.


3698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3699 ordinal=3699 -->
## Functions

Functions

   •      Last Time —

    Returns the last time value in Signals.

   •     RMS —

    Returns the calculated RMS of the values in Signals.

   •     Mode —

    Returns the value that occurs most often in the set values in Signals.

   •       Total Samples —

    Returns the total number of samples in Signals.

   •     Maximum —

    Returns the highest point in a set of values in Signals.

   •     Time Delta —

    Returns the time between samples in Signals.

   •      Index of Max —

    Returns the index value of the highest point of the values in Signals.

   •        First Time —

    Returns the first time value in Signals.

   •      Variance —

    Returns the calculated variance of the values in Signals.

   •     Skewness —

    Returns the skewness of the values in Signals. Skewness is a measure of symmetry and
    corresponds to the third-order moment about the mean.


Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 3699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3700 ordinal=3700 -->
## Functions

Functions

            • labview\examples\Express VIs\Express VI - Statistics.vi

     Components

       Calculates the skewness of the values in Signals. Skewness is a measure of symmetry
      and is a normalized form of the third-order moment about the mean.

       Calculates the kurtosis of the values in Signals. Kurtosis is a measure of peakedness
      and is a normalized form of the fourth-order moment about the mean.

       Displays the measurements you configured this Express VI to perform and the
       calculated values of those measurements. You can click any measurement listed in the
      Measurement column, and the corresponding value or plot appears in the Result
      Preview graph.

       Displays the input signal.

       Calculates the value of the sum of all the values in Signals.

       Finds the index value of the lowest point in a set of values in Signals.

       Finds the index value of the highest point in a set of values in Signals.

       Finds the last value in a set of values in Signals.

       Finds the last time value in a set of values in Signals.

       Finds the first value in a set of values in Signals.

       Finds the first time value in a set of values in Signals.

      Bases the calculation on the time between samples in Signals.

       Finds the value of the range from the lowest point to the highest point in a set of values
        in Signals.

       Finds the time of the lowest point in a set of values in Signals.

       Finds the lowest point in a set of values in Signals.

3700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3701 ordinal=3701 -->
## Functions

Functions

Finds the time of the highest point in a set of values in Signals.

Finds the highest point in a set of values in Signals.

Finds the value that occurs most often in the values in Signals.

Finds the median value in Signals. The Express VI sorts the values in Signals and
selects the middle element of the sorted values.

Calculates the calculated variance of the values in Signals.

Calculates the standard deviation of the values in Signals.

Calculates the RMS of the values in Signals.

Calculates the mean, or average, of the values in Signals.

Bases the calculation on the total number of samples in Signals.

CreateCreate HistogramHistogram

Computes a histogram for Signal.


Dialog Box Options

 Option          Description

                 Contains the following options:

                            • Number of bins—
 Configuration
                       Specifies the number of bins in the histogram. The default is 10.

                            • Maximum value—


                                                    © National Instruments 3701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3702 ordinal=3702 -->
## Functions

Functions


        Option          Description

                               Specifies the maximum value to include in the histogram. The default is 3.
                              This is best used with floating-point inputs. The maximum value is not
                              included, so values that match it exactly are not included in the histogram.

                                        • Minimum value—

                               Specifies the minimum value to include in the histogram. The default is –3.

                                        • Auto Configure—

                             Automatically configures the histogram settings based on the input data.

                         The Auto Configure button is enabled only after you wire valid data to Signal.

                        Contains the following options:

                                        • Percent of total—

        Amplitude          Represents the value of each bin as a percentage of the total.
        Representation
                                        • Sample count—

                            Represents the value of each bin as the number of samples in that bin.


                          Displays the input signal.

        Input Signal        If you wire data to the Express VI and run it, Input Signal displays real data. If you
                          close and reopen the Express VI, Input Signal displays sample data until you run
                        the Express VI again.


                          Displays a preview of the measurement. The Result Preview plot indicates the
                         value of the selected measurement with a dotted line.

         Result Preview   If you wire data to the Express VI and run the VI, Result Preview displays real data.
                                        If you close and reopen the Express VI, Result Preview displays sample data until
                      you run the VI again. If the cutoff frequency values are invalid, Result Preview
                      does not display valid data.


3702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3703 ordinal=3703 -->
## Functions

Functions

Inputs/Outputs

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •      Signal —

     Specifies the input signal. The signal can be a waveform, a real array, or a complex array.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •      Histogram —

    Returns the resulting histogram.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Statistics.vi

Components

Represents the value of each bin as the number of samples in that bin.

Represents the value of each bin as a percentage of the total.

Displays a preview of the measurement. The Result Preview plot indicates the value of
the selected measurement with a dotted line.


                                                    © National Instruments 3703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3704 ordinal=3704 -->
## Functions

Functions

       Displays the input signal.

       Automatically configures the histogram settings based on the input data.

       Specifies the minimum value to include in the histogram. The default is –3.

       Specifies the maximum value to include in the histogram. The default is 3. This is best
      used with floating-point inputs. The maximum value is not included, so values that
      match it exactly are not included in the histogram.

       Specifies the number of bins in the histogram. The default is 10.

     OptimizationOptimization

      Use the Optimization VIs to determine local minima and maxima of real 1D or
      n-dimension functions.

      You can choose between optimization algorithms based on derivatives of the function
      and algorithms working without these derivatives. You also can use special methods
        like Linear Programming, Levenberg-Marquardt in symbolic form, Pade, and
      Chebyshev Approximation.

      The VIs on this palette can return mathematics error codes.

      An overview of the optimization routines is shown in the following illustration.


3704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3705 ordinal=3705 -->
## Functions

Functions


Palette Object  Description

Linear
Programming              Determines the solution of a linear programming problem.Simplex
Method

              Uses either an interior point algorithm or an active set algorithm to solve the
Quadratic      problem: minimize 0.5x*Q*x + c*x, such that A*x=b and Imin are less than or equal
Programming   to D*x, which is less than or equal to Imax. You must manually select the
              polymorphic instance to use.


Unconstrained  Solves the unconstrained minimization problem for an arbitrary nonlinear
Optimization    function. You must manually select the polymorphic instance to use.


Constrained    Solves a general nonlinear optimization problem with nonlinear equality
Nonlinear       constraint and nonlinear inequality constraint bounds using a sequential quadratic
Optimization   programming method.


               Solves a global optimization equation with boundary constraints, nonlinearGlobal
                equality constraints, and nonlinear inequality constraints using the differentialOptimization                evolution (DE) method.


Brent with     Determines a local minimum of a given 1D function in a given interval. The method
Derivatives 1D   is based on derivatives of the function.


Golden        Determines a local minimum of a given 1D function with the help of a bracketing of
Section 1D     the minimum. The Golden Section Search method is used.


Conjugate     Determines a local minimum of a function of nindependent variables with the
Gradient nD    Conjugate Gradient method.


                                                    © National Instruments 3705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3706 ordinal=3706 -->
## Functions

Functions


         Palette Object  Description

        Downhill       Determines a local minimum of a function of nindependent variables with the
        Simplex nD     Downhill Simplex method.


         Find All                      Determines all local minima of a given function in a given interval.        Minima 1D


         Find All        Determines the minima of an n-dimension function in a given n-dimension
        Minima nD      interval.


        Chebyshev
                      Determines a given function using Chebyshev polynomials.        Approximation


      Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Transport
        Optimization Using Linear Programming.vi

      LinearLinear ProgrammingProgramming SimplexSimplex MethodMethod

      Determines the solution of a linear programming problem.


      Inputs/Outputs

               •     C —

          C is a vector describing the linear functional to maximize.

               •    M —

3706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3707 ordinal=3707 -->
## Functions

Functions


   M is a matrix describing the different constraints.

   •     B —

   B is a vector describing the right sides of the constraints inequalities.

   •     maximum —

   maximum is the maximal value, if it exists, of X under the constraints.

   •     X —

    X is the solution vector.

   •       ticks —

     ticks is the time in milliseconds for the whole calculation.

   •       error —

     error returns any error or warning condition from the VI. The nonexistence of a solution X leads
     to an error. You can wire error to the Error Cluster From Error Code VI to convert the error code or
    warning into an error cluster.


The following equation defines the optimization problem this VI solves.

cx= max!

with the constraints x≥ 0 and mx≥ b.

For the optimization problem cx= max!, use the following definitions:

X = (x1, …, xn) C = (c1, …, cn) B = (b1, …, bk) M is a k-by-nmatrix.

To solve the optimization problem, you must decide whether an optimal vector X does
exist. If the optimal vector does exist, then determine this vector X.

The solution of a linear programming problem is a two-step process. Complete the
following steps to solve a linear programming problem.


                                                    © National Instruments 3707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3708 ordinal=3708 -->
## Functions

Functions

         1. Transform the original problem into a problem in restricted normal form,
            essentially without inequalities in the formulation.
         2. Solve the restricted normal form problem.

           Note The restricted normal formulation seems to be special. But there are
           many ways to reformulate terms. For example, dx≤ e is equivalent to –dx≥
             –e and, dx= e is equivalent to the combination dx≥ e and –dx≥ –e.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Geometrical
        Analysis with Linear Programming.vi

     QuadraticQuadratic ProgrammingProgramming

      Uses either an interior point algorithm or an active set algorithm to solve the problem:
      minimize 0.5x*Q*x + c*x, such that A*x=b and Imin are less than or equal to D*x, which
         is less than or equal to Imax. You must manually select the polymorphic instance to
       use.


            • Quadratic Programming IP VI
            • Quadratic Programming AS VI

      QuadraticQuadratic ProgrammingProgramming IPIP VIVI

      Uses either an interior point algorithm or an active set algorithm to solve the problem:
      minimize 0.5x*Q*x + c*x, such that A*x=b and Imin are less than or equal to D*x, which
         is less than or equal to Imax. You must manually select the polymorphic instance to
       use.


3708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3709 ordinal=3709 -->
## Functions

Functions


Inputs/Outputs

   •       start —

     start is a point in ndimension at which the optimization process starts.

   •       objective function —

    objective function contains the coefficients of the quadratic and linear terms of the formula you
    want to minimize.

         •    Q —

      Q is the quadratic term, in the form of a matrix, of the objective function.

         •      c —

        c is the linear term, in the form of a vector, of the objective function.


   •      parameter bounds —

    parameter bounds contains the minimum and maximum values the parameters (x) can take.

         •     Xmin —

       xmin is the minimum value the parameters can accept.

         •     Xmax —

       xmax is the maximum value the parameters can accept.


   •      equality constraints —

    equality constraints defines the linear matrix equality constraint Ax=b.


                                                    © National Instruments 3709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3710 ordinal=3710 -->
## Functions

Functions


                     •     A —

             A is the matrix term of the linear equality constraint equation.

                     •     b —

             b is the vector term of the linear equality constraint equation.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       inequality constraints —

             inequality constraints contains the linear matrix inequality bounds Imin<Dx<Imax.

                     •     D —

            D is the matrix term of the linear inequality constraint expression.

                     •      Imin —

               Imin is the minimum value that the linear inequality constraint expression can accept.

                     •     Imax —

              Imax is the maximum value that the linear inequality constraint expression can accept.


               •      stopping criteria —

            stopping criteria is the collection of conditions that terminate the optimization. If (function
            tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
            function calls then optimization terminates.

                     •      function tolerance —

                function tolerance is the relative change in function value and is defined as abs(current f –
                prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
                function tolerance, the optimization terminates.


3710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3711 ordinal=3711 -->
## Functions

Functions


      •      parameter tolerance —

      parameter tolerance is the relative change in parameter values and is defined as
       abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
      parameter values falls below parameters tolerance, the optimization terminates.

      •     max iterations —

     max iterations is the largest number of iterations of the major loop of the optimization. If
      the number of major loop iterations exceeds max iterations, the optimization terminates.

      •     max function calls —

     max function calls is the largest number of objective function calls allowed before
      terminating the optimization process.

      •      gradient tolerance —

      gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
      gradient tolerance, the optimization terminates.

      •     max time (sec) —

     max time (sec) is the maximum amount of time LabVIEW allows between the start and the
     end of the optimization process. The default is –1. –1 indicates never to time out.


•     minimum —

  minimum is the set of values that minimizes the quadratic objective function while satisfying the
  bounds and constraints.

•      f(minimum) —

  f(minimum) is the value of the quadratic objective function 0.5x^TQx + cx at minimum.

•      lagrangian multipliers —

  lagrangian multipliers are the coefficients of the lagrangian function that corresponds to the
  equality and inequality constraints. If there are three equality constraints and two inequality
  constraints, the first three Lagrangian multipliers correspond to the equality constraints, and the
   last two Lagrangian multipliers correspond to the inequality constraints.

•       error out —

                                                   © National Instruments 3711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3712 ordinal=3712 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      QuadraticQuadratic ProgrammingProgramming ASAS VIVI

      Uses either an interior point algorithm or an active set algorithm to solve the problem:
      minimize 0.5x*Q*x + c*x, such that A*x=b and Imin are less than or equal to D*x, which
         is less than or equal to Imax. You must manually select the polymorphic instance to
       use.


      Inputs/Outputs

               •     warm start? —

         warm start? indicates whether to allow a warm start of the optimization. When warm start? is
           TRUE, LabVIEW uses the indexes of the active constraints from the previous solution as the initial
             set of active constraints for the current problem. The default is FALSE.

               •       start —

              start is a point in ndimension at which the optimization process starts.

               •       objective function —

            objective function contains the coefficients of the quadratic and linear terms of the formula you
          want to minimize.

                     •    Q —

           Q is the quadratic term, in the form of a matrix, of the objective function.

                     •      c —


3712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3713 ordinal=3713 -->
## Functions

Functions


      c is the linear term, in the form of a vector, of the objective function.


•      parameter bounds —

  parameter bounds contains the minimum and maximum values the parameters (x) can take.

      •     Xmin —

     xmin is the minimum value the parameters can accept.

      •     Xmax —

     xmax is the maximum value the parameters can accept.


•      equality constraints —

  equality constraints defines the linear matrix equality constraint Ax=b.

      •     A —

     A is the matrix term of the linear equality constraint equation.

      •     b —

     b is the vector term of the linear equality constraint equation.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       inequality constraints —

  inequality constraints contains the linear matrix inequality bounds Imin<Dx<Imax.

      •     D —


                                                   © National Instruments 3713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3714 ordinal=3714 -->
## Functions

Functions


            D is the matrix term of the linear inequality constraint expression.

                     •      Imin —

               Imin is the minimum value that the linear inequality constraint expression can accept.

                     •     Imax —

              Imax is the maximum value that the linear inequality constraint expression can accept.


               •      stopping criteria —

            stopping criteria is the collection of conditions that terminate the optimization. If (function
            tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
            function calls then optimization terminates.

                     •      function tolerance —

                function tolerance is the relative change in function value and is defined as abs(current f –
                prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
                function tolerance, the optimization terminates.

                     •      parameter tolerance —

               parameter tolerance is the relative change in parameter values and is defined as
                 abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
               parameter values falls below parameters tolerance, the optimization terminates.

                     •     max iterations —

            max iterations is the largest number of iterations of the major loop of the optimization. If
                the number of major loop iterations exceeds max iterations, the optimization terminates.

                     •     max function calls —

            max function calls is the largest number of objective function calls allowed before
                 terminating the optimization process.

                     •      gradient tolerance —


3714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3715 ordinal=3715 -->
## Functions

Functions


        gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
        gradient tolerance, the optimization terminates.

         •     max time (sec) —

      max time (sec) is the maximum amount of time LabVIEW allows between the start and the
       end of the optimization process. The default is –1. –1 indicates never to time out.


   •     minimum —

   minimum is the set of values that minimizes the quadratic objective function while satisfying the
    bounds and constraints.

   •      f(minimum) —

    f(minimum) is the value of the quadratic objective function 0.5x^TQx + cx at minimum.

   •      lagrangian multipliers —

    lagrangian multipliers are the coefficients of the lagrangian function that corresponds to the
    equality and inequality constraints. If there are three equality constraints and two inequality
     constraints, the first three Lagrangian multipliers correspond to the equality constraints, and the
     last two Lagrangian multipliers correspond to the inequality constraints.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

UnconstrainedUnconstrained OptimizationOptimization

Solves the unconstrained minimization problem for an arbitrary nonlinear function.
You must manually select the polymorphic instance to use.


  • Quasi Newton VI
  • Conjugate Gradient VI


                                                    © National Instruments 3715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3716 ordinal=3716 -->
## Functions

Functions

            • Downhill Simplex VI
            • Quasi Newton formula string VI
            • Conjugate Gradient formula string VI
            • Downhill simplex formula string VI

       For functions that are smooth and have first and second derivatives defined, the
      Broyden Quasi-Newton algorithm typically converges the fastest. If you experience
      problems with convergence of the Broyden Quasi-Newton algorithm, the Conjugate
       Gradient algorithm might be able to solve the problem. The Downhill Simplex
       algorithm relies only on function evaluations and often is able to find a solution when
       the function is not smooth and the other algorithms fail to converge.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Optimize
        Extended Rosenbrock.vi

      QuasiQuasi NewtonNewton VIVI

       Solves the unconstrained minimization problem for an arbitrary nonlinear function.
      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      function data —

            function data contains static data that the user-defined function needs at run time.

               •       objective function —


3716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3717 ordinal=3717 -->
## Functions

Functions


  objective function is a reference to the VI that implements the function to optimize.

  Create this VI by starting from the VI template located at labview\vi.lib\gmath\
  NumericalOptimization\ucno_objective function template.vit.

•       start —

  start is a point in ndimension at which the optimization process starts.

•      stopping criteria —

  stopping criteria is the collection of conditions that terminate the optimization. If (function
  tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
  function calls then optimization terminates.

      •      function tolerance —

      function tolerance is the relative change in function value and is defined as abs(current f –
      prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
      function tolerance, the optimization terminates.

      •      parameter tolerance —

      parameter tolerance is the relative change in parameter values and is defined as
       abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
      parameter values falls below parameters tolerance, the optimization terminates.

      •     max iterations —

     max iterations is the largest number of iterations of the major loop of the optimization. If
      the number of major loop iterations exceeds max iterations, the optimization terminates.

      •     max function calls —

     max function calls is the largest number of objective function calls allowed before
      terminating the optimization process.

      •      gradient tolerance —

      gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
      gradient tolerance, the optimization terminates.

      •     max time (sec) —


                                                   © National Instruments 3717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3718 ordinal=3718 -->
## Functions

Functions


            max time (sec) is the maximum amount of time LabVIEW allows between the start and the
              end of the optimization process. The default is –1. –1 indicates never to time out.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     minimum —

         minimum is the determined local minimum in ndimension.

               •      f(minimum) —

           f(minimum) is the function value of f(X) at the determined minimum.

               •     number of function evaluations —

          number of function evaluations is the number of times the objective function was called in the
            optimization process.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       For functions that are smooth and have first and second derivatives defined, the
      Broyden Quasi-Newton algorithm typically converges the fastest. If you experience
      problems with convergence of the Broyden Quasi-Newton algorithm, the Conjugate
       Gradient algorithm might be able to solve the problem. The Downhill Simplex
       algorithm relies only on function evaluations and often is able to find a solution when
       the function is not smooth and the other algorithms fail to converge.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Optimize
        Extended Rosenbrock.vi


3718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3719 ordinal=3719 -->
## Functions

Functions

ConjugateConjugate GradientGradient VIVI

Solves the unconstrained minimization problem for an arbitrary nonlinear function.
You must manually select the polymorphic instance to use.


Inputs/Outputs

   •      function data —

    function data contains static data that the user-defined function needs at run time.

   •       objective function —

    objective function is a reference to the VI that implements the function to optimize.

    Create this VI by starting from the VI template located at labview\vi.lib\gmath\
   NumericalOptimization\ucno_objective function template.vit.

   •       start —

     start is a point in ndimension at which the optimization process starts.

   •      conjugate gradient settings —

    conjugate gradient settings

         •      gradient method —

        gradient method specifies the algorithm used to compute the derivatives. A value of 0
         represents the Fletcher Reeves method. A value of 1 represents the Polak Ribiere method.
       The default is 0.

         •       line minimization —

          line minimization A value of 0 represents an algorithm without usage of the derivatives. A


                                                    © National Instruments 3719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3720 ordinal=3720 -->
## Functions

Functions


                value of 1 represents an algorithm with usage of the derivatives. The default is 0.


               •      stopping criteria —

            stopping criteria is the collection of conditions that terminate the optimization. If (function
            tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
            function calls then optimization terminates.

                     •      function tolerance —

                function tolerance is the relative change in function value and is defined as abs(current f –
                prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
                function tolerance, the optimization terminates.

                     •      parameter tolerance —

               parameter tolerance is the relative change in parameter values and is defined as
                 abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
               parameter values falls below parameters tolerance, the optimization terminates.

                     •     max iterations —

            max iterations is the largest number of iterations of the major loop of the optimization. If
                the number of major loop iterations exceeds max iterations, the optimization terminates.

                     •     max function calls —

            max function calls is the largest number of objective function calls allowed before
                 terminating the optimization process.

                     •      gradient tolerance —

                gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
                gradient tolerance, the optimization terminates.

                     •     max time (sec) —

            max time (sec) is the maximum amount of time LabVIEW allows between the start and the
              end of the optimization process. The default is –1. –1 indicates never to time out.


               •       error in (no error) —

3720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3721 ordinal=3721 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     minimum —

   minimum is the determined local minimum in ndimension.

   •      f(minimum) —

    f(minimum) is the function value of f(X) at the determined minimum.

   •     number of function evaluations —

   number of function evaluations is the number of times the objective function was called in the
    optimization process.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


For functions that are smooth and have first and second derivatives defined, the
Broyden Quasi-Newton algorithm typically converges the fastest. If you experience
problems with convergence of the Broyden Quasi-Newton algorithm, the Conjugate
Gradient algorithm might be able to solve the problem. The Downhill Simplex
algorithm relies only on function evaluations and often is able to find a solution when
the function is not smooth and the other algorithms fail to converge.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\Optimize
   Extended Rosenbrock.vi

DownhillDownhill SimplexSimplex VIVI

Solves the unconstrained minimization problem for an arbitrary nonlinear function.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3722 ordinal=3722 -->
## Functions

Functions

           Note

             Determines a local minimum of a function of n independent variables with
              the Downhill Simplex method.


      Inputs/Outputs

               •      function data —

            function data contains static data that the user-defined function needs at run time.

               •       objective function —

            objective function is a reference to the VI that implements the function to optimize.

            Create this VI by starting from the VI template located at labview\vi.lib\gmath\
         NumericalOptimization\ucno_objective function template.vit.

               •       start —

              start is a point in ndimension at which the optimization process starts.

               •      stopping criteria —

            stopping criteria is the collection of conditions that terminate the optimization. If (function
            tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
            function calls then optimization terminates.

                     •      function tolerance —

                function tolerance is the relative change in function value and is defined as abs(current f –
                prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below


3722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3723 ordinal=3723 -->
## Functions

Functions


      function tolerance, the optimization terminates.

      •      parameter tolerance —

      parameter tolerance is the relative change in parameter values and is defined as
       abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
      parameter values falls below parameters tolerance, the optimization terminates.

      •     max iterations —

     max iterations is the largest number of iterations of the major loop of the optimization. If
      the number of major loop iterations exceeds max iterations, the optimization terminates.

      •     max function calls —

     max function calls is the largest number of objective function calls allowed before
      terminating the optimization process.

      •      gradient tolerance —

      gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
      gradient tolerance, the optimization terminates.

      •     max time (sec) —

     max time (sec) is the maximum amount of time LabVIEW allows between the start and the
     end of the optimization process. The default is –1. –1 indicates never to time out.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     minimum —

  minimum is the determined local minimum in ndimension.

•      f(minimum) —

  f(minimum) is the function value of f(X) at the determined minimum.

•     number of function evaluations —


                                                   © National Instruments 3723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3724 ordinal=3724 -->
## Functions

Functions


          number of function evaluations is the number of times the objective function was called in the
            optimization process.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       For functions that are smooth and have first and second derivatives defined, the
      Broyden Quasi-Newton algorithm typically converges the fastest. If you experience
      problems with convergence of the Broyden Quasi-Newton algorithm, the Conjugate
       Gradient algorithm might be able to solve the problem. The Downhill Simplex
       algorithm relies only on function evaluations and often is able to find a solution when
       the function is not smooth and the other algorithms fail to converge.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Optimize
        Extended Rosenbrock.vi

      QuasiQuasi NewtonNewton formulaformula stringstring VIVI

       Solves the unconstrained minimization problem for an arbitrary nonlinear function.
      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •     X —

          X is an array of strings representing the x variables.


3724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3725 ordinal=3725 -->
## Functions

Functions

•        f(X) —

   f(X) is the string representing the function of the x variables. The formulas can contain any
  number of valid variables.

•       start —

  start is a point in ndimension at which the optimization process starts.

•      stopping criteria —

  stopping criteria is the collection of conditions that terminate the optimization. If (function
  tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
  function calls then optimization terminates.

      •      function tolerance —

      function tolerance is the relative change in function value and is defined as abs(current f –
      prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
      function tolerance, the optimization terminates.

      •      parameter tolerance —

      parameter tolerance is the relative change in parameter values and is defined as
       abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
      parameter values falls below parameters tolerance, the optimization terminates.

      •     max iterations —

     max iterations is the largest number of iterations of the major loop of the optimization. If
      the number of major loop iterations exceeds max iterations, the optimization terminates.

      •     max function calls —

     max function calls is the largest number of objective function calls allowed before
      terminating the optimization process.

      •      gradient tolerance —

      gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
      gradient tolerance, the optimization terminates.

      •     max time (sec) —


                                                   © National Instruments 3725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3726 ordinal=3726 -->
## Functions

Functions


            max time (sec) is the maximum amount of time LabVIEW allows between the start and the
              end of the optimization process. The default is –1. –1 indicates never to time out.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     minimum —

         minimum is the determined local minimum in ndimension.

               •      f(minimum) —

           f(minimum) is the function value of f(X) at the determined minimum.

               •     number of function evaluations —

          number of function evaluations is the number of times the objective function was called in the
            optimization process.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       For functions that are smooth and have first and second derivatives defined, the
      Broyden Quasi-Newton algorithm typically converges the fastest. If you experience
      problems with convergence of the Broyden Quasi-Newton algorithm, the Conjugate
       Gradient algorithm might be able to solve the problem. The Downhill Simplex
       algorithm relies only on function evaluations and often is able to find a solution when
       the function is not smooth and the other algorithms fail to converge.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Optimize
        Extended Rosenbrock.vi


3726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3727 ordinal=3727 -->
## Functions

Functions

ConjugateConjugate GradientGradient formulaformula stringstring VIVI

Solves the unconstrained minimization problem for an arbitrary nonlinear function.
You must manually select the polymorphic instance to use.


Inputs/Outputs

   •     X —

    X is an array of strings representing the x variables.

   •        f(X) —

     f(X) is the string representing the function of the x variables. The formulas can contain any
   number of valid variables.

   •       start —

     start is a point in ndimension at which the optimization process starts.

   •      conjugate gradient settings —

    conjugate gradient settings

         •      gradient method —

        gradient method specifies the algorithm used to compute the derivatives. A value of 0
         represents the Fletcher Reeves method. A value of 1 represents the Polak Ribiere method.
       The default is 0.

         •       line minimization —

          line minimization A value of 0 represents an algorithm without usage of the derivatives. A
        value of 1 represents an algorithm with usage of the derivatives. The default is 0.


                                                    © National Instruments 3727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3728 ordinal=3728 -->
## Functions

Functions

               •      stopping criteria —

            stopping criteria is the collection of conditions that terminate the optimization. If (function
            tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
            function calls then optimization terminates.

                     •      function tolerance —

                function tolerance is the relative change in function value and is defined as abs(current f –
                prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
                function tolerance, the optimization terminates.

                     •      parameter tolerance —

               parameter tolerance is the relative change in parameter values and is defined as
                 abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
               parameter values falls below parameters tolerance, the optimization terminates.

                     •     max iterations —

            max iterations is the largest number of iterations of the major loop of the optimization. If
                the number of major loop iterations exceeds max iterations, the optimization terminates.

                     •     max function calls —

            max function calls is the largest number of objective function calls allowed before
                 terminating the optimization process.

                     •      gradient tolerance —

                gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
                gradient tolerance, the optimization terminates.

                     •     max time (sec) —

            max time (sec) is the maximum amount of time LabVIEW allows between the start and the
              end of the optimization process. The default is –1. –1 indicates never to time out.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     minimum —

3728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3729 ordinal=3729 -->
## Functions

Functions


   minimum is the determined local minimum in ndimension.

   •      f(minimum) —

    f(minimum) is the function value of f(X) at the determined minimum.

   •     number of function evaluations —

   number of function evaluations is the number of times the objective function was called in the
    optimization process.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


For functions that are smooth and have first and second derivatives defined, the
Broyden Quasi-Newton algorithm typically converges the fastest. If you experience
problems with convergence of the Broyden Quasi-Newton algorithm, the Conjugate
Gradient algorithm might be able to solve the problem. The Downhill Simplex
algorithm relies only on function evaluations and often is able to find a solution when
the function is not smooth and the other algorithms fail to converge.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\Optimize
   Extended Rosenbrock.vi

DownhillDownhill simplexsimplex formulaformula stringstring VIVI

Solves the unconstrained minimization problem for an arbitrary nonlinear function.
You must manually select the polymorphic instance to use.


                                                    © National Instruments 3729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3730 ordinal=3730 -->
## Functions

Functions


      Inputs/Outputs

               •     X —

          X is an array of strings representing the x variables.

               •        f(X) —

               f(X) is the string representing the function of the x variables. The formulas can contain any
          number of valid variables.

               •       start —

              start is a point in ndimension at which the optimization process starts.

               •      stopping criteria —

            stopping criteria is the collection of conditions that terminate the optimization. If (function
            tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
            function calls then optimization terminates.

                     •      function tolerance —

                function tolerance is the relative change in function value and is defined as abs(current f –
                prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
                function tolerance, the optimization terminates.

                     •      parameter tolerance —

               parameter tolerance is the relative change in parameter values and is defined as
                 abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
               parameter values falls below parameters tolerance, the optimization terminates.

                     •     max iterations —

            max iterations is the largest number of iterations of the major loop of the optimization. If
                the number of major loop iterations exceeds max iterations, the optimization terminates.


3730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3731 ordinal=3731 -->
## Functions

Functions


         •     max function calls —

      max function calls is the largest number of objective function calls allowed before
         terminating the optimization process.

         •      gradient tolerance —

        gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
        gradient tolerance, the optimization terminates.

         •     max time (sec) —

      max time (sec) is the maximum amount of time LabVIEW allows between the start and the
       end of the optimization process. The default is –1. –1 indicates never to time out.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     minimum —

   minimum is the determined local minimum in ndimension.

   •      f(minimum) —

    f(minimum) is the function value of f(X) at the determined minimum.

   •     number of function evaluations —

   number of function evaluations is the number of times the objective function was called in the
    optimization process.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


For functions that are smooth and have first and second derivatives defined, the
Broyden Quasi-Newton algorithm typically converges the fastest. If you experience
problems with convergence of the Broyden Quasi-Newton algorithm, the Conjugate
Gradient algorithm might be able to solve the problem. The Downhill Simplex

                                                    © National Instruments 3731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3732 ordinal=3732 -->
## Functions

Functions

       algorithm relies only on function evaluations and often is able to find a solution when
       the function is not smooth and the other algorithms fail to converge.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Optimize
        Extended Rosenbrock.vi

     ConstrainedConstrained NonlinearNonlinear OptimizationOptimization

       Solves a general nonlinear optimization problem with nonlinear equality constraint
      and nonlinear inequality constraint bounds using a sequential quadratic programming
      method.


      Inputs/Outputs

               •      function data —

            function data contains static data that the user-defined function needs at run time.

               •       objective and constraint function —

            objective and constraint function is a reference to the VI that implements the nonlinear
             function to minimize, the nonlinear equality constraints function, and the nonlinear inequality
             constraints function as separate outputs. The objective function output must not be empty. The
             constraint functions are optional. Therefore, the equality constraints output, the inequality
             constraints output, or both can be empty.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         NumericalOptimization\cno_objective function template.vit.


3732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3733 ordinal=3733 -->
## Functions

Functions

•       start —

  start are the points in ndimension at which the optimization process starts.

•     bounds —

  bounds is a cluster that contains the upper and lower numeric limits for the parameters being
  optimized and the inequality constraints.

      •     X minimum —

     X minimum contains the lowest allowed value of the parameters being optimized. The
      length of this array must match the length of X maximum and can be 0 or the same as the
      length of the start array. The array does not accept exceptional values, such as Inf, –Inf, or
      NaN.

      •     X maximum —

     X maximum contains the highest allowed value of the parameters being optimized. The
      length of this array must match the length of X minimum and can be 0 or the same as the
      length of the start array. The array does not accept exceptional values, such as Inf, –Inf, or
      NaN.

      •       inequality constraint minimum —

       inequality constraint minimum contains the lowest allowed value of the inequality
       constraints. The length of this array must match the length of the inequality constraints
      returned from the objective and constraint function. This array does not accept exceptional
       values, such as Inf, –Inf, or NaN.

      •       inequality constraint maximum —

       inequality constraint maximum contains the highest allowed value of the inequality
       constraints. The length of this array must match the length of the inequality constraints
      returned from the objective and constraint function. This array does not accept exceptional
       values, such as Inf, –Inf, or NaN.


•      beginning state —

  beginning state contains the initial values of the inequality constraint function, the Lagrangian
  multipliers, and the Hessian. beginning state is typically the ending state of a previous
  optimization and allows a warm start of the optimization.


                                                   © National Instruments 3733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3734 ordinal=3734 -->
## Functions

Functions


                     •       inequality constraints —

                 inequality constraints contains the value of the inequality constraint functions, typically
               from a previous call to the Constrained Nonlinear Optimization VI.

                     •      lagrangian multipliers —

                lagrangian multipliers contains the value of the Lagrangian multipliers, typically from a
                previous call to the Constrained Nonlinear Optimization VI.

                     •      hessian —

                hessian contains an estimate of the Hessian, typically from a previous call to the
                Constrained Nonlinear Optimization VI.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     cno settings —

          cno settings contains additional tolerance and termination settings that are specific to this
             algorithm.

                     •       constraint weight —

                 constraint weight is a relative weighting of the constraints as compared to the objective
                 function and controls the distance that the optimization search travels outside the feasible
                range to seek an optimal solution. A value greater than 1 forces the search to stay close to
                the known feasible range, and a smaller value allows a broader range of searching.

                     •     maximum minor iterations —

            maximum minor iterations is an upper bound on the number of iterations allowed to solve
                the quadratic problem. If the constraint functions are highly nonlinear, the linearized
                  constraints used in the quadratic problem might not be very accurate. In this case, it might
              be sensible to limit the number of minor iterations, forcing the linear approximation to be
               updated more often.


               •      stopping criteria —


3734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3735 ordinal=3735 -->
## Functions

Functions


  stopping criteria is the collection of conditions that terminate the optimization. If (function
  tolerance AND parameter tolerance AND gradient tolerance) OR max iterations OR max
  function calls then optimization terminates.

      •      function tolerance —

      function tolerance is the relative change in function value and is defined as abs(current f –
      prev f)/(abs(curr f)+machine eps). If the relative change in the function value falls below
      function tolerance, the optimization terminates.

      •      parameter tolerance —

      parameter tolerance is the relative change in parameter values and is defined as
       abs(current p – prev p)/(abs(curr p)+machine eps). If the relative change of all the
      parameter values falls below parameters tolerance, the optimization terminates.

      •     max iterations —

     max iterations is the largest number of iterations of the major loop of the optimization. If
      the number of major loop iterations exceeds max iterations, the optimization terminates.

      •     max function calls —

     max function calls is the largest number of objective function calls allowed before
      terminating the optimization process.

      •      gradient tolerance —

      gradient tolerance is the 2–norm of the gradient. If the 2–norm of the gradient falls below
      gradient tolerance, the optimization terminates.

      •     max time (sec) —

     max time (sec) is the maximum amount of time LabVIEW allows between the start and the
     end of the optimization process. The default is –1. –1 indicates never to time out.


•     number of function calls —

  number of function calls is the number of times the objective function calls in the optimization
  process.

•     minimum —


                                                   © National Instruments 3735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3736 ordinal=3736 -->
## Functions

Functions


         minimum is the determined local minimum in ndimension.

               •      f(minimum) —

           f(minimum) is the function value of objective function at the determined minimum.

               •      ending state —

           ending state contains the final values of the inequality constraint function, the Lagrange
              multipliers, and the Hessian.

                     •       inequality constraints —

                 inequality constraints contains the value of the inequality constraint functions at the end of
                the optimization.

                     •      lagrangian multipliers —

                lagrangian multipliers contains the value of the Lagrangian multipliers at the end of the
                 optimization.

                     •      hessian —

                hessian contains an estimate of the Hessian at the end of the optimization.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Fitting\Nonlinear Spring
        Constant fit.vi

     GlobalGlobal OptimizationOptimization

       Solves a global optimization equation with boundary constraints, nonlinear equality


3736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3737 ordinal=3737 -->
## Functions

Functions

constraints, and nonlinear inequality constraints using the differential evolution (DE)
method.


Inputs/Outputs

   •      function data —

    function data contains static data that the user-defined function needs at run time.

   •       objective and constraint function —

    objective and constraint function is a reference to the VI that implements the nonlinear
     function, the nonlinear equality constraints function, and the nonlinear inequality constraints
    function as separate outputs. In the referenced VI, the objective function output must not be
    empty, but the constraint functions are optional. Therefore, the equality constraints output, the
     inequality constraints output, or both can be empty.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   GlobalOptimization.llb\Global Optimization_Objective Function.vit.

   •        Init Parameters —

     Init Parameters are the initial parameters at which the optimization process starts. LabVIEW
    uses Init Parameters when Beginning State is empty. Each row of Init Parameters is one set of
    parameters. The number of columns in Init Parameters must equal the length of Min and Max in
    Bounds.

       If the number of rows in Init Parameters is less than population size, LabVIEW initializes the
    remaining sets of parameters. If the number of rows in Init Parameters is larger than population
     size, LabVIEW ignores the additional sets of parameters.

   •     Bounds —

    Bounds is a cluster that contains the upper and lower numeric limits for the parameters being
    optimized.


                                                    © National Instruments 3737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3738 ordinal=3738 -->
## Functions

Functions


                     •     Min —

              Min contains the lowest allowed value of the parameters being optimized. Min cannot be
               empty. The length of Min must be equal to the length of Max. Min does not accept
                 exceptional values, such as Inf, –Inf, or NaN.

                     •     Max —

             Max contains the highest allowed value of the parameters being optimized. Max cannot be
               empty. The length of Max must be equal to the length of Min. Max does not accept
                 exceptional values, such as Inf, –Inf, or NaN.


               •      Beginning State —

           Beginning State contains the initial values of the populations and Pareto indexes. Beginning
            State is typically the ending state of a previous optimization and allows a warm start of the
             optimization. If Beginning State has values, LabVIEW ignores Init Parameters.

                     •      Population —

                Population contains a set of parameters, which includes values of parameters, objective
                  functions, equality constraints, inequality constraints, and the base index.

                           •      Parameters —

                   Parameters contains the values of candidate parameters.

                           •      Objective Functions —

                           •      Equality Constraints —

                           •       Inequality Constraints —


                     •      Pareto Indexes —

                Pareto Indexes contains index that determines the selection of parameters from all
                 candidates.


               •       error in (no error) —


3738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3739 ordinal=3739 -->
## Functions

Functions


  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     DE settings —

  DE Settings contains additional settings that are specific to the differential evolution (DE)
  method.

      •      population size —

      population size is the number of sets of candidate parameters that LabVIEW calculates at
      each loop iteration in the optimization process. This size also indicates the number of
       objective function calls at each loop iteration in the optimization process. A larger
      population size usually results in better optimization results and a longer execution time.
     The default is 10.

      •       scale factor —

       scale factor is the diversity factor that LabVIEW uses to generate mutant parameters. Larger
      values of scale factor result in more diverse mutant parameters. The default is 0.9.

      •      crossover probability —

      crossover probability is the probability that LabVIEW inherits the trial parameters from the
      mutant parameters. A larger value of crossover probability results in a higher probability
       that LabVIEW accepts the mutant parameters. The default is 0.95.

      •     bound mapping method —

     bound mapping method is the method that LabVIEW maps the trial parameters into
      bounds.

      0 None
      1 Random between Bounds and Values (default)
      2 Re-Initialize

      •      mutation method —

      mutation method is the method that LabVIEW generates mutant parameters.


                                                   © National Instruments 3739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3740 ordinal=3740 -->
## Functions

Functions


               0    Random (default)
               1     Either Or
               2     Best
               3     Target to Best

                     •      crossover method —

                crossover method is the method that LabVIEW crosses candidate parameters with mutant
                parameters.

               0    Uniform (default)
               1     Exponential


               •      stopping criteria —

            stopping criteria is the collection of conditions that terminate the optimization process.

                     •     max iterations —

            max iterations is the maximum number of loop iteration in the optimization process. If the
             number of loop iteration exceeds max iterations, the optimization process terminates. The
                 default is 50.

                     •     max function calls —

            max function calls is the maximum number of objective function calls allowed before the
                 optimization process terminates. The default is -1.

            -1 indicates that the optimization process never terminates and does not rely on the
             number of objective function calls. The formula that determines the actual number of
                 objective function calls is population size * (max iterations + 1).

                     •     max time (sec) —

            max time (sec) is the maximum amount of time LabVIEW allows between the start and the
              end of the optimization process. The default is -1. -1 indicates that the optimization
                process never times out.


               •     number of function calls —

3740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3741 ordinal=3741 -->
## Functions

Functions


  number of function calls is the number of times the objective function calls in the optimization
  process.

   If max function calls is -1, number of function calls equals population size * (max iterations +
   1).

•     Minimum —

  Minimum is the determined global minimum among all minimum possibilities.

•     F(Minimum) —

  F(Minimum) is the function value of the objective function at Minimum.

•      Ending State —

  Ending State contains the final values of the populations and Pareto indexes at the end of the
  optimization process.

      •      Population —

      Population contains a set of populations, which includes values of candidate parameters,
       objective functions, equality constraints, and inequality constraints at the end of the
       optimization process.

             •      Parameters —

          Parameters contains the values of candidate parameters at the end of optimization
           process.

             •      Objective Functions —

           Objective Functions contains the values of objective functions at Parameters.

             •      Equality Constraints —

           Equality Constraints contains the values of equality constraints at Parameters.

             •       Inequality Constraints —

           Inequality Constraints contains the values of inequality constraints at Parameters.


                                                   © National Instruments 3741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3742 ordinal=3742 -->
## Functions

Functions


                     •      Pareto Indexes —

                Pareto Indexes contains the index that determines the selection of parameters from all
                 candidates.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This VI solves a global optimization equation by finding xto minimize f(x), which is
       subject to the following constraints:

        Boundary constraints                     min≤ x≤ max
         Equality constraints                                   g(x) = 0
         Inequality constraints                                 h(x) ≤ 0

    xis the set of parameters to optimize. f(x) is the set of objective functions to minimize.
      The equality and inequality constraints are optional in this problem.

        Differential evolution (DE) is one method used to solve the global optimization
      problem. It approximates the actual global optimum by iteratively mutating and
      improving the candidate parameters from the initial ones.

           Note The DE method cannot guarantee the global optimum is found. The
              best parameters return depending on the choice of the DE settings as well as
              the problem itself.

           If object function evaluation takes long time, the DE method needs to call the object
       function several times, depending on population size, during each loop iteration in the
       optimization process. This VI enables parallel loop iterations on the For Loop to call the
       object function so that LabVIEW can take advantage of multiple processors. In order to
        utilize the parallel loop iterations, you need to do the following:


3742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3743 ordinal=3743 -->
## Functions

Functions

  • Change the VI that implements the objective function to a reentrant VI that shares
    clones.
  • Open a reference to a VI with a 0x40 option, as the following shown in the following
   image.


The following illustration shows how the VI solves a global optimization equation.


                                                    © National Instruments 3743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3744 ordinal=3744 -->
## Functions

Functions


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Find Global Min
        on Surface.vi
            • labview\examples\Mathematics\Optimization\Two Circles
        Optimization.vi

     BrentBrent withwith DerivativesDerivatives 1D1D

      Determines a local minimum of a given 1D function in a given interval. The method is

3744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3745 ordinal=3745 -->
## Functions

Functions

based on derivatives of the function.


Inputs/Outputs

   •      accuracy —

    accuracy controls the accuracy of the determined minimum of formula. The method stops if two
    consecutive approximations differ not more than the value of accuracy.

   •      a (start) —

    a is the left point of the bracketing interval. The default is 0.0.

   •     b (start) —

   b is the middle point of the bracketing interval. The default is 0.0.

   •      c (start) —

    c is the right point of the bracketing interval. The default is 0.0.

   •      formula —

    formula is a string describing the function under investigation. The formula can contain any
   number of valid variables.

   •     minimum —

   minimum is the determined local minimum of formula.

   •      f(minimum) —

    f(minimum) is the function value at the determined local minimum.

   •       ticks —

     ticks is the time in milliseconds for the whole calculation.

   •       error —

                                                    © National Instruments 3745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3746 ordinal=3746 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Refer to the Golden Section 1D VI description for the definition of a bracketing interval.
      Here the derivative of formula is used. This leads to a faster algorithm, because the
     new bracketing interval has better properties than those of the Golden Section 1D VI.

     GoldenGolden SectionSection 1D1D

      Determines a local minimum of a given 1D function with the help of a bracketing of the
      minimum. The Golden Section Search method is used.


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the determined minimum of formula. The method stops if two
            consecutive approximations differ not more than the value of accuracy.

               •      a (start) —

           a is the left point of the bracketing interval. The default is 0.0.

               •     b (start) —

          b is the middle point of the bracketing interval. The default is 0.0.

               •      c (start) —

            c is the right point of the bracketing interval. The default is 0.0.

               •      formula —

           formula is a string describing the function under investigation. The formula can contain any


3746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3747 ordinal=3747 -->
## Functions

Functions


   number of valid variables.

   •     minimum —

   minimum is the determined local minimum of formula.

   •      f(minimum) —

    f(minimum) is the function value at the determined local minimum.

   •       ticks —

     ticks is the time in milliseconds for the whole calculation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


A bracketing triplet (a,b,c)of a 1D continuous function fis a combination of three
points with f(a)> f(b) and f(c)> f(b). This guarantees the existence of a local
minimum of fin the interval (a,c).

Beginning with a bracketing triplet (a, b, c), the Golden Section Search method
determines a new bracketing triplet with a considerably smaller expansion. Repeating
this scheme often yields a good approximation of the local minimum. The following
equation essentially calculates the new bracketing point.


(Golden Section Search Method)

The following front panel shows the relationship between a,b,cand f(a),f(b), f(c).


                                                    © National Instruments 3747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3748 ordinal=3748 -->
## Functions

Functions


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Scripts and Formulas\Street
        Illumination Problem.vi

     ConjugateConjugate GradientGradient nDnD

      Determines a local minimum of a function of nindependent variables with the
      Conjugate Gradient method.


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the minimum. The method stops if two consecutive
            approximations differ no more than the value of accuracy. The default is 1.00E-8.

               •      gradient method —


3748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3749 ordinal=3749 -->
## Functions

Functions


    gradient method specifies the algorithm used to compute the derivatives. A value of 0
    represents the Fletcher Reeves method. A value of 1 represents the Polak Ribiere method. The
     default is 0.

   •       line minimization —

     line minimization A value of 0 represents an algorithm without usage of the derivatives. A value
     of 1 represents an algorithm with usage of the derivatives. The default is 0.

   •       Start —

     Start is a point in ndimension at which the optimization process starts.

   •     X —

    X is an array of strings representing the xvariables. If the array of strings contains the variable t,
    the VI returns an error.

   •        f(X) —

     f(X) is the string representing the function of the xvariables. The formula can contain any
   number of valid variables.

   •     Minimum —

   Minimum is the determined local minimum in ndimension.

   •      f(Minimum) —

    f(Minimum) is the function value of f(X) at the determined minimum.

   •       ticks —

     ticks is the time in milliseconds for the whole calculation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Fletcher Reeves and the Polak Ribiere algorithm is based on the determination of
best-suited directions and 1D sub-minimization.

                                                    © National Instruments 3749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3750 ordinal=3750 -->
## Functions

Functions

      The following illustration shows a start point and a start direction. New points and new
       directions are calculated by the Conjugate Gradient nD VI.


     DownhillDownhill SimplexSimplex nDnD

      Determines a local minimum of a function of nindependent variables with the
       Downhill Simplex method.


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the minimum. The method stops if two consecutive
            approximations differ no more than the value of accuracy. The default is 1.00E-8.

               •       Start —


3750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3751 ordinal=3751 -->
## Functions

Functions


     Start is an array of points at which the optimization process is starting. These points form a
    simplex in ndimension.

   •     X —

    X is an array of strings representing the xvariables. If the array of strings contains the variable t,
    the VI returns an error.

   •        f(X) —

     f(X) is the string representing the function of the xvariables. The formula can contain any
   number of valid variables.

   •     Minimum —

   Minimum is the determined local minimum in ndimension.

   •      f(Minimum) —

    f(Minimum) is the function value of f(X) at the determined minimum.

   •       ticks —

     ticks is the time in milliseconds for the whole calculation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Downhill Simplex algorithm, also called the Nelder and Mead method, works
without partial derivatives. The Downhill Simplex algorithm consists of catching the
minimum of the function f(X) with the help of simple geometrical bodies, specifically a
simplex.

A simplex in 2D is a triangle; a simplex in 3D is a tetrahedron, and so on. You must have
(n+1) starting points, each of dimension n, forming the initial simplex. You must enter
only one point of these (n+1) starting points. The (n+1) dimensional simplex is
constructed automatically.


                                                    © National Instruments 3751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3752 ordinal=3752 -->
## Functions

Functions

       For example, the following equation defines a function.

        f(x, y) = x² + y²

       For the function defined by the preceding equation, you must enter two numbers,
       describing exactly one point in 2D. The algorithm generates a new simplex by some
      elementary operations such as reflections, expansions, and contractions. In the end,
       the minimum is concentrated in a very small simplex.

      To find the simplex sequence tending to the minimum (0, 0) of the preceding function,
       enter the following values on the front panel of the Downhill Simplex nD VI:

            • Start: [3.2, 1]
            • X: [x, y]
            •  f(X): [x*x + y*y]

      The following illustration shows the simplex sequence tending to the minimum (0, 0)
       of the preceding function.


     FindFind AllAll MinimaMinima 1D1D

      Determines all local minima of a given function in a given interval.


3752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3753 ordinal=3753 -->
## Functions

Functions


Inputs/Outputs

   •      accuracy —

    accuracy controls the accuracy of the minimum. The method stops if two consecutive
    approximations differ no more than the value of accuracy. The default is 1.00E-8.

   •      step type —

    step type controls the spacing used for the function values. A step type value of 0, fixed function,
    represents uniformly spaced function values. A value of 1, modified function, represents the
    optimal step size. In general, modified function leads to more accurate Minima. The default is 0.

   •      algorithm —

    algorithm specifies the method used by the VI. The default is 0.

    0  Golden Section Search (default)
    1  Brent with Derivatives

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      formula —

    formula is a string representing the function under investigation. The formula can contain any
   number of valid variables.

   •     Minima —

    Minima is an array of all found minima of formula in the interval (start, end).

   •      f(Minima) —


                                                    © National Instruments 3753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3754 ordinal=3754 -->
## Functions

Functions


            f(Minima) is the function values at the points Minima.

               •       ticks —

             ticks is the time in milliseconds for the whole calculation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           Note If you want to find out the maxima of a function, you must take
               –function as the inputs. The –f(Minima) are the correct maximal function
               values.

      The Find All Minima 1D VI finds all minima in the given interval (start, end). To find all
      minima 1D of f(x)= cos(x²), enter the following values on the front panel:

            •  start: -1.0
            • end: 6.0
            • formula: cos(x^2)

      The following illustration shows the plot of f(x). The boxes on the plot are the locations
       of the minima.


3754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3755 ordinal=3755 -->
## Functions

Functions

      Note If the start or end values are close to the minimum value, use the
       modified function step type.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\1D Explorer.vi

FindFind AllAll MinimaMinima nDnD

Determines the minima of an n-dimension function in a given n-dimension interval.


Inputs/Outputs

   •      accuracy —

    accuracy controls the accuracy of the minima. The default is 1.00E-8.

   •      algorithm —

    algorithm specifies the method used by the VI. When algorithm is 0 it represents the Conjugate
    Gradient method. When algorithm is 1, it represents the Downhill Simplex method. The default
      is 0.

   •      gradient method —

    gradient method specifies the algorithm used to compute the derivatives. A value of 0
    represents the Fletcher Reeves method. A value of 1 represents the Polak Ribiere method. The
     default is 0.

   •       line minimum —

                                                    © National Instruments 3755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3756 ordinal=3756 -->
## Functions

Functions


              line minimum A value of 0 represents the line optimization without derivatives. A line minimum
            value of 1 represents the line optimization with derivatives. The default is 0.

               •     number of trials —

          number of trials is the number of the randomly chosen start points of the optimization process.
           These points belong to the interval (start,end). The default is 5.

               •       Start —

             Start is the start point in ndimension.

               •     End —

          End is the end point in ndimension.

               •     X —

          X is an array of strings describing the nvariables.

               •       F(X) —

             F(X) is a string describing the ndimension function of X. The formula can contain any number of
              valid variables.

               •     X Values —

          X Values is a matrix describing all determined local minima.

               •      F Values —

           F Values is the function values at the points X Values.

               •       ticks —

             ticks is the time in milliseconds for the whole calculation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3757 ordinal=3757 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\2D Explorer.vi

ChebyshevChebyshev ApproximationApproximation

Determines a given function using Chebyshev polynomials.


Inputs/Outputs

   •     number of points —

   number of points is the number of equidistant points in the interval (start,end). The default is
     10.

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      order —

    order is the degree of the Chebyshev approximation. The default is 3.

    The degree is the number of different Chebyshev polynomials T0(x), T1(x), …, Tn(x) describing
    the formula.

   •      formula —

    formula is a string describing the function under investigation. The formula can contain any
   number of valid variables.


                                                    © National Instruments 3757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3758 ordinal=3758 -->
## Functions

Functions

               •     C —

          C is an array of coefficients.

          The array of coefficients belongs to T0(x), T1(x), …, Tn(x).

               •     X —

          X is the x values dividing (start,end) in equidistant subintervals.

               •      Y —

           Y is the y values of the Chebyshev polynomial at points X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       For a given natural number n, the following equation approximately represents the
       function f(x).

        f(x) = c0T0(x) + … + cnTn(x)

      where T0(x), …, Tn(x) are the first Chebyshev polynomials. You can calculate the c0,
     …, cn as sums of the form


      where            for k= 1, ..., n.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\Sequence of
        Chebyshev Approximations.vi


3758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3759 ordinal=3759 -->
## Functions

Functions

DifferentialDifferential EquationsEquations

Use the Differential Equations VIs to solve differential equations.


 Palette Object               Description

 Ordinary Differential        Use the Differential Equations VIs to solve ordinary differential
 Equations                   equations.


                         Use the Differential Equations VIs to solve partial differential Partial Differential Equations
                              equations.


OrdinaryOrdinary DifferentialDifferential EquationsEquations

Use the Differential Equations VIs to solve ordinary differential equations.

The VIs on this palette can return mathematics error codes.


 Palette
            Description
 Object

 ODE       Solves ordinary differential equations with initial conditions of the following form:
 Solver       X'=F(X,t). You must manually select the polymorphic instance to use.

 ODE
 Runge      Solves ordinary differential equations with initial conditions using the Runge Kutta
 Kutta 4th   method.
 Order


                                                    © National Instruments 3759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3760 ordinal=3760 -->
## Functions

Functions


         Palette                    Description
        Object

       ODE Cash                    Solves ordinary differential equations with initial conditions using the Cash Karp        Karp 5th                  method.        Order

       ODE Euler                    Solves ordinary differential equations with initial conditions using the Euler method.       Method

       ODE
         Linear nth  Solves an nth-order, homogeneous linear differential equation with constant
        Order       coefficients in numeric form.
        Numeric

       ODE
         Linear nth  Solves an nth-order, homogeneous linear differential equation with constant
        Order       coefficients in symbolic form.
        Symbolic

       ODE
         Linear      Solves an n-dimension, homogeneous linear system of differential equations with
        System     constant coefficients, for a given start condition.
        Numeric

       ODE                    Solves an n-dimension linear system of differential equations with a given start         Linear
                     condition. The solution is based on the determination of the eigenvalues and        System
                    eigenvectors of the underlying matrix. The solution is given in symbolic form.        Symbolic

       DAE                    Solves differential algebraic equations (DAEs) with initial conditions by using the
       Radau 5th
                 Radau IIA method. You must manually select the polymorphic instance to use.
        Order

     ODEODE SolverSolver

       Solves ordinary differential equations with initial conditions of the following form:
        X'=F(X,t). You must manually select the polymorphic instance to use.


3760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3761 ordinal=3761 -->
## Functions

Functions

  • ODE Solver main VI
  • ODE Solver formula string VI
ODEODE SolverSolver mainmain VIVI

Solves ordinary differential equations with initial conditions of the following form:
X'=F(X,t). You must manually select the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that you can use to pass arbitrary values to the ODE F(X,t) VI.

   •     ODE F(X,t) —

   ODE F(X,t) is a strictly typed reference to the VI that implements the right-hand side of an
    ordinary differential equation dX/dt=F(X,t).

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   ode.llb\ODE rhs.vit.

   •      x0 —

    x0 is the vector of initial values of the ODE states.

   •      simulation parameters —

    simulation parameters specifies the set of parameters used to configure the numerical solution
     of the differential equation.

         •        Initial Time —

           Initial Time specifies the time at which to start the ordinary differential equation (ODE)


                                                    © National Instruments 3761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3762 ordinal=3762 -->
## Functions

Functions


                   solver. The default is 0.

                     •       Final Time —

                 Final Time is the time at which the ODE solver stops.

                     •     Time Step —

              Time Step is the interval between the times at which the ODE solver evaluates the model
              and updates the model output, in seconds. LabVIEW uses this parameter only if you select a
                  fixed step-size ODE solver.

                     •      Absolute Tolerance —

                Absolute Tolerance specifies the absolute tolerance the ODE solver uses to control the
                    error.

                For y' = f(y), the ODE solver maintains error ≈ |y| * relative tolerance + absolute tolerance.

              LabVIEW uses this parameter only if you select a variable step-size solver. Variable step-size
                  solvers use this error to adjust the step size. If the error is too large, the variable step-size
                  solver reduces the step size. If the error is too small, the variable step-size solver increases
                the step size. Absolute tolerance is most significant when yis small.

                     •       Relative Tolerance —

                 Relative Tolerance specifies the relative tolerance the ODE solver uses to control the error.

                For y' = f(y), the ODE solver maintains error ≈ |y| * relative tolerance + absolute tolerance.

              LabVIEW uses this parameter only if you select a variable step-size solver. Variable step-size
                  solvers use this error to adjust the step size. If the error is too large, the variable step-size
                  solver reduces the step size. If the error is too small, the variable step-size solver increases
                the step size. Relative tolerance is most significant when yis large.

                     •      Continuous Solver —

               Continuous Solver is the type of ODE solver used to evaluate the simulation diagram. The
                 default is Runge-Kutta 45 (variable).


3762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3763 ordinal=3763 -->
## Functions

Functions


  0   Runge-Kutta 1 (Euler)
  1   Runge-Kutta 2
  2   Runge-Kutta 3
  3   Runge-Kutta 4
  4   Runge-Kutta 23 (variable)
  5   Runge-Kutta 45 (variable)
  6  BDF (variable)
  7   Adams-Moulton (variable)
  8   Rosenbrock (variable)
  9   Discrete States Only

•       Discrete Time Step —

  Discrete Time Step specifies the base time step to use for discrete functions, in seconds.
  The ODE solver might not evaluate a discrete function every Discrete Time Step. The ODE
  solver evaluates the discrete function and updates the function output every ndiscrete
  time steps, where nis the sample rate divisor parameter you specify for that function.

        Note If you select a fixed step-size solver, the Discrete Time Step must be an
            integer multiple of the Time Step. If you specify a Discrete Time Step that is not
         an integer multiple of the Time Step, LabVIEW displays a run-time error when
          you attempt to run the simulation.

•     Minimum Time Step —

  Minimum Time Step specifies the smallest time step size the ODE solver can use to evaluate
  the simulation diagram. LabVIEW uses this parameter only if you select a variable step-size
   solver.

•     Maximum Time Step —

  Maximum Time Step specifies the largest time step size the ODE solver can use to evaluate
  the simulation diagram. LabVIEW uses this parameter only if you select a variable step-size
   solver.

•        Initial Time Step —

   Initial Time Step specifies the time step size for the first time step of the simulation diagram
  evaluation. LabVIEW uses this parameter only if you select a variable step-size solver.


                                                © National Instruments 3763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3764 ordinal=3764 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      times —

           times is the array of points in time at which the differential equation solver stepped or was
             evaluated. If you select a fixed step-size solver, then times contains evenly spaced values.

               •      outputs —

           outputs is a two-dimensional array of y values. Each row corresponds to the vector of y-values
            evaluated at a particular time. Each column is history of a particular y-value over time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   ODEODE SolverSolver formulaformula stringstring VIVI

       Solves ordinary differential equations with initial conditions of the following form:
        X'=F(X,t). You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •     ODE RHS —

         ODE RHS is a cluster of formula strings and variable strings that implements the right-hand-side
             of an ordinary differential equation X'=F(X,t).

                     •        F(X,t) —

                   F(X,t) is a 1D array of strings representing the right sides of the differential equations. The


3764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3765 ordinal=3765 -->
## Functions

Functions


      formulas can contain any number of valid variables.

      •     X —

     X is an array of strings of variables. When naming these variables, you must use either one
       character only or one character and one number.

      •      time —

      time is the string denoting the time variable. The default variable is t.


•      x0 —

  x0 is the vector of initial values of the ODE states.

•      simulation parameters —

  simulation parameters specifies the set of parameters used to configure the numerical solution
  of the differential equation.

      •        Initial Time —

        Initial Time specifies the time at which to start the ordinary differential equation (ODE)
       solver. The default is 0.

      •       Final Time —

       Final Time is the time at which the ODE solver stops.

      •     Time Step —

     Time Step is the interval between the times at which the ODE solver evaluates the model
     and updates the model output, in seconds. LabVIEW uses this parameter only if you select a
       fixed step-size ODE solver.

      •      Absolute Tolerance —

      Absolute Tolerance specifies the absolute tolerance the ODE solver uses to control the
        error.


                                                   © National Instruments 3765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3766 ordinal=3766 -->
## Functions

Functions


                For y' = f(y), the ODE solver maintains error ≈ |y| * relative tolerance + absolute tolerance.

              LabVIEW uses this parameter only if you select a variable step-size solver. Variable step-size
                  solvers use this error to adjust the step size. If the error is too large, the variable step-size
                  solver reduces the step size. If the error is too small, the variable step-size solver increases
                the step size. Absolute tolerance is most significant when yis small.

                     •       Relative Tolerance —

                 Relative Tolerance specifies the relative tolerance the ODE solver uses to control the error.

                For y' = f(y), the ODE solver maintains error ≈ |y| * relative tolerance + absolute tolerance.

              LabVIEW uses this parameter only if you select a variable step-size solver. Variable step-size
                  solvers use this error to adjust the step size. If the error is too large, the variable step-size
                  solver reduces the step size. If the error is too small, the variable step-size solver increases
                the step size. Relative tolerance is most significant when yis large.

                     •      Continuous Solver —

               Continuous Solver is the type of ODE solver used to evaluate the simulation diagram. The
                 default is Runge-Kutta 45 (variable).

               0   Runge-Kutta 1 (Euler)
               1   Runge-Kutta 2
               2   Runge-Kutta 3
               3   Runge-Kutta 4
               4   Runge-Kutta 23 (variable)
               5   Runge-Kutta 45 (variable)
               6  BDF (variable)
               7   Adams-Moulton (variable)
               8   Rosenbrock (variable)
               9   Discrete States Only

                     •       Discrete Time Step —

                 Discrete Time Step specifies the base time step to use for discrete functions, in seconds.
              The ODE solver might not evaluate a discrete function every Discrete Time Step. The ODE
                  solver evaluates the discrete function and updates the function output every ndiscrete


3766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3767 ordinal=3767 -->
## Functions

Functions


      time steps, where nis the sample rate divisor parameter you specify for that function.

           Note If you select a fixed step-size solver, the Discrete Time Step must be an
                integer multiple of the Time Step. If you specify a Discrete Time Step that is not
             an integer multiple of the Time Step, LabVIEW displays a run-time error when
             you attempt to run the simulation.

      •     Minimum Time Step —

     Minimum Time Step specifies the smallest time step size the ODE solver can use to evaluate
      the simulation diagram. LabVIEW uses this parameter only if you select a variable step-size
       solver.

      •     Maximum Time Step —

     Maximum Time Step specifies the largest time step size the ODE solver can use to evaluate
      the simulation diagram. LabVIEW uses this parameter only if you select a variable step-size
       solver.

      •        Initial Time Step —

        Initial Time Step specifies the time step size for the first time step of the simulation diagram
       evaluation. LabVIEW uses this parameter only if you select a variable step-size solver.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      times —

  times is the array of points in time at which the differential equation solver stepped or was
  evaluated. If you select a fixed step-size solver, then times contains evenly spaced values.

•      outputs —

  outputs is a two-dimensional array of y values. Each row corresponds to the vector of y-values
  evaluated at a particular time. Each column is history of a particular y-value over time.

•       error out —


                                                   © National Instruments 3767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3768 ordinal=3768 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     ODEODE RungeRunge KuttaKutta 4th4th OrderOrder

       Solves ordinary differential equations with initial conditions using the Runge Kutta
      method.


      Inputs/Outputs

               •     X (name of variables) —

          X is an array of strings of variables.

               •      time start —

           time start is the start point of the ODE. The default is 0.

               •      time end —

           time end is the end point of the time interval under investigation. The default is 1.0.

               •     h (step rate) —

          h is the fixed step rate. The default is 0.1.

               •     X0 —

          X0 is the vector of the start condition x[10], …, x[n0].

           There is a one-to-one relation between the components of X0 and X.

               •      time —


3768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3769 ordinal=3769 -->
## Functions

Functions


    time is the string denoting the time variable. The default variable is t.

   •        F(X,t) (right sides of the ODE as functions of X and t) —

     F(X,t) is a 1D array of strings representing the right sides of the differential equations. The
    formulas can contain any number of valid variables.

   •      Times —

    Times is an array representing the time steps. The Runge Kutta method yields equidistant time
    steps between time start and time end.

   •     X Values (solution) —

    X Values is a 2D array of the solution vector x[10], …, x[n].

    The top index runs over the time steps, as specified in the Times array, and the bottom index
    runs over the elements of x[10], …, x[n].

   •       ticks —

     ticks is the time in milliseconds for the whole calculation.

   •       error —

    error returns any error or warning from the VI. Errors are produced by using the wrong inputs X,
    X0, and F(X,t). You can wire error to the Error Cluster From Error Code VI to convert the error
    code or warning into an error cluster.


The Runge Kutta method of 4th order works with a higher degree of accuracy than the
common Euler method and with a fixed step rate as a five stage process, more
precisely


and


                                                    © National Instruments 3769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3770 ordinal=3770 -->
## Functions

Functions

       with

      The method ends if

     tn ≥ time end.

      The following illustration shows the solution of the following system of ordinary
        differential equations:


       Enter the following equations on the front panel:

            • time start: 0.00
            • time end: 50.00
            • X: [x, y, z]
            • X0: [1, 1, 1]
            •  F(X,t): [10*(y - x), x*(28 - z) - y, x*y - (8/3)*z]


3770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3771 ordinal=3771 -->
## Functions

Functions

      Note Even though there are actually three solutions, a first glance at the
       graph almost seems to show only two solutions. This is because the solutions
         for x and y are very similar, so they almost overlap.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   ODE\Shooting Method.vi
  • labview\examples\Mathematics\Differential Equations -
   ODE\Process Control Explorer.vi

ODEODE CashCash KarpKarp 5th5th OrderOrder

Solves ordinary differential equations with initial conditions using the Cash Karp
method.


Inputs/Outputs

   •     X (name of variables) —

    X is an array of strings of variables.

   •      time start —

    time start is the start point of the ODE. The default is 0.

   •      time end —

    time end is the end point of the time interval under investigation. The default is 1.0.


                                                    © National Instruments 3771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3772 ordinal=3772 -->
## Functions

Functions

               •     h (step rate) —

          h is the step rate at the beginning of the algorithm. The Cash Karp algorithm works with an
            adaptive step rate. The default is 0.1.

               •     X0 —

          X0 is the vector of the start condition x[10], …, x[n0].

           There is a one-to-one relation between the components of X0 and X.

               •      accuracy —

            accuracy controls the accuracy of the solutions. The default is 0.0, which specifies the maximum
             deviation of the calculated solution from the actual solution.

               •      time —

           time is the string denoting the time variable. The default variable is t.

               •        F(X,t) (right sides of the ODE as functions of X and t) —

              F(X,t) is a 1D array of strings representing the right sides of the differential equations. The
            formulas can contain any number of valid variables.

               •      Times —

           Times is a 1D array representing the time steps. The ODE Cash Karp method yields arbitrarily
           chosen time steps between time start and time end.

               •     X Values (solution) —

          X Values is a 2D array of the solution vector x[10], …, x[n].

          The top index runs over the time steps, as specified in the Times array, and the bottom index
            runs over the elements of x[10], …, x[n].

               •       ticks —

             ticks is the time in milliseconds for the whole calculation.

               •       error —

             error returns any error or warning from the VI. Errors are produced by using the wrong inputs X,
             X0, and F(X,t). You can wire error to the Error Cluster From Error Code VI to convert the error


3772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3773 ordinal=3773 -->
## Functions

Functions


    code or warning into an error cluster.


The Cash Karp method works with an adaptive step rate and is computationally more
efficient than the Euler method and the Runge Kutta method. The Cash Karp method is
an embedded Runge Kutta formula and is based on a fifth-order strategy (with six
steps).


and


with

tn+ 1 = tn + h

The a2, …, a6; b21, …, b65; c1, …, c6; and c1*, …, c6* are fixed real numbers. This
choice determines the quality of the method.

You can determine the actual step size hnew with the help of the accuracy value, the
old step size h, the difference Δ = |X(tn+ 1) – X*(tn+ 1)|, and the following equation.


      Note It might happen that the value of the last element in Times turns out to
       be greater than the value entered in time end. This is a property of the Cash
       Karp method. This method is very accurate, but you have no control of the
        step rate. In order to guarantee that the end point specified in time end is
       taken into consideration, the last step might turn out to be too long.


                                                    © National Instruments 3773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3774 ordinal=3774 -->
## Functions

Functions

      The following illustration shows the solution of the following system of ordinary
        differential equations in a 3D representation.


      The previous equations and boundary conditions are entered on the front panel as:

            • time start: 0.00
            • time end: 40.00
            • X0: [0.6, 0.6, 0.6]
            •  F(X,t): [10*(y-x), x*(28-z) - y, x*y - (8/3)*z]
            • X: [x,y,z]

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        ODE\Planar Three Body Problem.vi

     ODEODE EulerEuler MethodMethod

       Solves ordinary differential equations with initial conditions using the Euler method.


3774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3775 ordinal=3775 -->
## Functions

Functions


Inputs/Outputs

   •     X (name of variables) —

    X is an array of strings of variables.

   •      time start —

    time start is the start point of the ODE. The default is 0.

   •      time end —

    time end is the end point of the time interval under investigation. The default is 1.0.

   •     h (step rate) —

   h is the fixed step rate. The default is 0.1.

   •     X0 —

    X0 is the vector of the start condition x[10], …, x[n0].

    There is a one-to-one relation between the components of X0 and X.

   •      time —

    time is the string denoting the time variable. The default variable is t.

   •        F(X,t) (right sides of the ODE as functions of X and t) —

     F(X,t) is a 1D array of strings representing the right sides of the differential equations. The
    formulas can contain any number of valid variables.

   •      Times —

    Times is an array representing the time steps. The Euler method yields equidistant time steps
    between time start and time end.

   •     X Values (solution) —

                                                    © National Instruments 3775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3776 ordinal=3776 -->
## Functions

Functions


          X Values is a 2D array of the solution vector x[10], …, x[n].

          The top index runs over the time steps, as specified in the Times array, and the bottom index
            runs over the elements of x[10], …, x[n].

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.

               •       error —

             error returns any error or warning from the VI. Errors are produced by using the wrong inputs X,
             X0, and F(X,t). You can wire error to the Error Cluster From Error Code VI to convert the error
           code or warning into an error cluster.


      The general form of an ordinary differential equation (ODE) is


       with


      The functions f1, …, fn, the numbers, and the start point t= t0 are given. With the
       conventions F= (f1, …, fn); X(t) = (x1(t), …, xn(t)); and X0 = (x10, …, xn0),

     we have


      You have to determine functions X fulfilling the previous equations.

      The Euler method is the most basic and often useful strategy to solve ODEs. Beginning
       with t0 and a fixed step rate h, usually relatively small, the new values

3776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3777 ordinal=3777 -->
## Functions

Functions


                                                            ⋮X(t0 + h) = X(t0) + hF(X(t0), t) X(t0 + 2h) = X(t0 + h) + hF(X(t0 + h), t0 + h)

are calculated. This process stops, if time start + nh ≥ time end, where time end is the
right endpoint of the time interval under investigation.

The following illustration shows the solution of the following ordinary differential
equation.


The previous equation and initial condition are entered on the front panel as:

   • time start: 0.00
   • time end: 20.00
   • X0: 1.00
   •  F(X,t): sin(t*x) + sinc(t + x) + cos(t - x)
   • X: x

ODEODE LinearLinear nthnth OrderOrder NumericNumeric

Solves an nth-order, homogeneous linear differential equation with constant
coefficients in numeric form.


                                                    © National Instruments 3777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3778 ordinal=3778 -->
## Functions

Functions


      Inputs/Outputs

               •     A (a0,a1,...an-1) —

          A is the vector of coefficients of the different derivatives of a function x(t), starting with the
              coefficient of the lowest order term. The coefficient of the highest order derivative is assumed to
          be equal to 1.0 and does not need to be entered.

               •     X0 —

          X0 is the vector of the start condition x[10], …, x[n0].

           There is a one-to-one relation between the components of X0 and X.

               •     number of points —

          number of points is the number of equidistant time points between time start and time end.
          The default is 10.

               •      time start —

           time start is the start point of the ODE. The default is 0.

               •      time end —

           time end is the end point of the time interval under investigation. The default is 1.0.

               •      Times —

           Times is an array representing the time steps. The method yields equidistant time steps
           between time start and time end.

               •     X —

          X is the vector of the solution x at the equidistant time points as specified in the Times array.

               •       error —

             error returns any error or warning from the VI. Errors are produced by using the wrong inputs X,


3778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3779 ordinal=3779 -->
## Functions

Functions


     X0, and F(X,t). You can wire error to the Error Cluster From Error Code VI to convert the error
    code or warning into an error cluster.


Consider the nth-order linear homogeneous differential equation

x(n) + an– 1x(n– 1) + … + a1x(1) + a0x= 0

with

x(0) = x00 x(1)(0) = x10      –                   ⋮ x(n  1)(0) = xn– 10

where 0 represents the more general value of time start. There is a strong connection
between the equation

x(n) + an– 1x(n– 1) + … + a1x(1) + a0x= 0

and the zero finding problem

 n     n–z + an– 1z   1+ … + a1z+ a0 = 0

The nzeros of the last equation determine the structure of the solution of the ODE. If
we have ndistinct complex zeros λ1, …, λ n, the general solution of the nth-order
differential equation can be expressed by

x(t) = β1exp(λ1t) + … + βnexp(λnt)

The unknowns can be determined by the start condition

x(0) = β1 + … + βnx(1)(0) = β1λ1 + … + βnλn      –              – 1              – 1                                    ⋮ x(n  1)(0) = β1λ1n  + … + βnλnn

      Note

       The case of repeated eigenvalues λ1, …, λn is more complex and is not


                                                    © National Instruments 3779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3780 ordinal=3780 -->
## Functions

Functions


               treated here. An error code of –23017 is given if this happens.

            By convention, the value of the highest coefficient is taken as 1.0, and does
              not need to be entered in the A control. The other coefficients are entered
                starting with the lowest order coefficient.


      To solve the differential equation

        x'' – 3 x' + 2 x= 0

       with the I.C. as with x(0) = 2 and x'(0) = 3, enter A = [2, -3] and X0 = [2, 3].

     ODEODE LinearLinear nthnth OrderOrder SymbolicSymbolic

       Solves an nth-order, homogeneous linear differential equation with constant
        coefficients in symbolic form.


      Inputs/Outputs

               •     A (a0,a1,...an-1) —

          A is the vector of coefficients of the different derivatives of a function x(t), starting with the
              coefficient of the lowest order term. The coefficient of the highest order derivative is assumed to
          be equal to 1.0 and does not need to be entered.

               •     X0 —

          X0 is the vector of the start condition x[10], …, x[n0].

           There is a one-to-one relation between the components of X0 and X.

               •      formula —

           formula is the symbolic solution.


3780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3781 ordinal=3781 -->
## Functions

Functions

   •       error —

     error returns any error or warning from the VI. Errors are produced by using the wrong inputs X,
     X0, and F(X,t). You can wire error to the Error Cluster From Error Code VI to convert the error
    code or warning into an error cluster.


The general solution has the following form.

x(t) = β1exp(λ1t) + … + βnexp(λnt)

with complex

β1, …, βn

and

λ1, …, λn

But all inputs are real, and thus the solution also has this property. As a consequence,
the symbolic solution is a linear combination of exp, sin-, and cos-functions with real
coefficients.

      Note Only the case of pairwise different λ1, …, λn is treated. For the case of
       repeated eigenvalues, an error code of –23017 is given. By convention, the
        value of the highest coefficient is taken as 1.0, and does not need to be
       entered in the A control. The other coefficients are entered starting with the
        lowest order coefficient.

To solve the differential equation

x'' – 3 x' + 2 x= 0

with the I.C. as with x(0) = 2 and x'(0) = 3, enter A = [2, -3] and X0 = [2, 3].

Refer to the ODE Linear nth Order Numeric VI for more information about nth-order,
homogeneous linear differential equations.


                                                    © National Instruments 3781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3782 ordinal=3782 -->
## Functions

Functions

     ODEODE LinearLinear SystemSystem NumericNumeric

       Solves an n-dimension, homogeneous linear system of differential equations with
       constant coefficients, for a given start condition.


      Inputs/Outputs

               •     A (matrix of coefficients) —

          A is the n-by-nmatrix describing the linear system.

               •     X0 (start value) —

          X0 is the nvector describing the start condition, x[10], …, x[n0].

           There is a one-to-one relation between the components of X0 and X.

               •     number of points —

          number of points is the number of equidistant time points between time start and time end.
          The default is 10.

               •      time start —

           time start is the start point of the ODE. The default is 0.

               •      time end —

           time end is the end point of the time interval under investigation. The default is 1.0.

               •      Times —

           Times is an array representing the time steps. The method yields equidistant time steps
           between time start and time end.

               •     X Values —


3782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3783 ordinal=3783 -->
## Functions

Functions


    X Values is the matrix of the solution X at the equidistant time points.

   •       error —

     error returns any error or warning from the VI. Errors are produced by using the wrong inputs X,
     X0, and F(X,t). You can wire error to the Error Cluster From Error Code VI to convert the error
    code or warning into an error cluster.


The solution of the VI is based on the determination of the eigenvalues and
eigenvectors of the underlying matrix A. The solution is given in numeric form.

      Note This VI works properly for almost all cases of real matrices A that can
       have repeated eigenvalues, complex conjugate eigenvalues, and so on. The
        exception is the case of a singular eigenvector matrix, that is, a matrix in
       which the eigenvectors do not span the entire space. An error of –23016 is
        given if the eigenvector matrix is singular.

Linear systems can be described by

           X(0) = X0

if time start = 0.

Here

X(t) = (x0(t), …, xn(t))

and A represents an n-by-nreal matrix. The linear system can be solved by the
determination of the eigenvalues and eigenvectors of A. Let Sbe the set of all
eigenvectors spanning the whole n-dimensional space. The transformation Y(t) =
SX(t) yields

               Y(0) = SX0

The matrix SAS–1 has diagonal form, so that the solution is obvious. The solution X(t)

                                                    © National Instruments 3783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3784 ordinal=3784 -->
## Functions

Functions

      can be determined by back-transformation

       X(t) = S–1Y(t)

           Note No ticks output is implemented because the essential operation is the
               calculation of eigenvectors and eigenvalues of the matrix A. This operation is
                negligible for relatively small dimensions of A.

      The following illustration shows the four components of the solution of the linear
        differential equation described by the following system:


       with

        x1(0) = 1 x2(0) = 2 x3(0) = 3 x4(0) = 4


      The following list of parameters shows how to enter the previous equations on the
       front panel:

            • A: [-7, -6, 4, 1; -6, 2, 1, -2; 4, 1, 0, 2; -1, -2, 2, -7]
            • X0: [1, 2, 3, 4]


3784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3785 ordinal=3785 -->
## Functions

Functions

  • time start: 0.00
  • time end: 1.00

ODEODE LinearLinear SystemSystem SymbolicSymbolic

Solves an n-dimension linear system of differential equations with a given start
condition. The solution is based on the determination of the eigenvalues and
eigenvectors of the underlying matrix. The solution is given in symbolic form.


Inputs/Outputs

   •     A (matrix of coefficients) —

   A is the n-by-nmatrix describing the linear system.

   •     X0 (start value) —

    X0 is the nvector describing the start condition, x[10], …, x[n0].

    There is a one-to-one relation between the components of X0 and X.

   •      formula —

    formula is a string with the solution of the linear system in the standard formula notation of
    LabVIEW. The solution vector elements are separated by carriage return.

   •       error —

    error returns any error or warning from the VI. Errors are produced by using the wrong inputs X,
    X0, and F(X,t). You can wire error to the Error Cluster From Error Code VI to convert the error
    code or warning into an error cluster.


      Note This VI works properly for almost all cases of real matrices A that can
       have repeated eigenvalues, complex conjugate eigenvalues, and so on. The
       exception is the case of a singular eigenvector matrix, that is, a matrix in
       which the eigenvectors do not span the whole space. An error of –23016 is

                                                    © National Instruments 3785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3786 ordinal=3786 -->
## Functions

Functions


              given if the eigenvector matrix is singular.

      The linear differential equation described by the following system:


       with

        x1(0) = 1 x2(0) = 2 x3(0) = 3 x4(0) = 4

      has the solution

      + 1.62*e(–12.46*t) – 1.28*e(–6.30*t) + 0.63*e(1.34*t) + 0.04*e(5.42*t) + 0.84*e(–12.46*t) –
        0.29*e(–6.30*t) + 1.51*e(1.34*t) – 0.06*e(5.42*t) –0.73*e(–12.46*t) + 0.01*e(–6.30*t) +
        3.69*e(1.34*t) + 0.02*e(5.42*t) + 0.87*e(–12.46*t) + 2.67*e(–6.30*t) + 0.45*e(1.34*t) +
        0.01*e(5.42*t)


      The following list of parameters shows how to enter the previous equations on the
       front panel:

            • A: [-7, -6, 4, 1; -6, 2, 1, -2; 4, 1, 0, 2; -1, -2, 2, -7]


3786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3787 ordinal=3787 -->
## Functions

Functions

  • X0: [1, 2, 3, 4]

DAEDAE RadauRadau 5th5th OrderOrder

Solves differential algebraic equations (DAEs) with initial conditions by using the
Radau IIA method. You must manually select the polymorphic instance to use.


  • DAE Radau 5th Order (VIRef) VI
  • DAE Radau 5th Order (Formula) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   ODE\DAE Simple Pendulum Simulation.vi
  • labview\examples\Mathematics\Differential Equations -
   ODE\DAE Spring Pendulum Simulation.vi
DAEDAE RadauRadau 5th5th OrderOrder (VIRef)(VIRef) VIVI

Solves differential algebraic equations (DAEs) with initial conditions by using the
Radau IIA method. You must manually select the polymorphic instance to use.


Inputs/Outputs

   •      data —


                                                    © National Instruments 3787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3788 ordinal=3788 -->
## Functions

Functions


           data is a variant that passes arbitrary values to the VI.

               •     DAE F(X,X',t) —

          DAE F(X,X',t) provides a strictly typed reference to the VI that implements the differential
             algebraic equation (DAE).

           You can use the function template located in vi.lib\gmath\dae.llb\DAE Radau 5th
         Order Func Template.vit to create this strictly typed reference.

               •        Initial Values —

               Initial Values specify the values of the initial state of the VI.

               •        Initial Derivatives —

               Initial Derivatives specify the values of the initial state derivative. The length of the Initial
             Derivative must equal the length of the Initial Values.

               •      simulation parameters —

            simulation parameters specifies the set of parameters used to configure the differential
             algebraic equation (DAE) solver.

                     •        initial time —

                     initial time specifies the time at which to start the DAE solver. The default is 0.

                     •       final time —

                   final time is the time at which the DAE solver stops. The final time must be larger than the
                     initial time. The default value is 10.

                     •      Absolute Tolerance —

                Absolute Tolerance specifies the absolute tolerance the DAE solver uses to control the local
                  error for each variable. You can specify either a scalar tolerance which applies to all
                  variables, or an array of tolerance which applies to each variable respectively. The Absolute
                Tolerance cannot be negative. The corresponding Absolute Tolerance and Relative
                Tolerance cannot both be zeroes. The default is 0.001.

              The DAE solver calculates the local error by the following equation: |X|*relative tolerance +


3788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3789 ordinal=3789 -->
## Functions

Functions


      absolute tolerance

      LabVIEW uses this error to adjust the step size. If the error is too large, the DAE solver rejects
      the current step and reduces the step size for another try. If the error is too small, the DAE
       solver accepts the current step and increases the step size for next try. The Absolute
      Tolerance is most significant when X is small.

      •       Relative Tolerance —

       Relative Tolerance specifies the relative tolerance the DAE solver uses to control the local
       error for each variable state. You can specify either a scalar tolerance which applies to all
       variables or an array of tolerance which applies to each variable respectively. The Relative
      Tolerance cannot be negative. The Absolute Tolerance and Relative Tolerance cannot both
     be zeroes. The default is 0.001.

     The DAE solver calculates the local error by the following equation: |X|*relative tolerance +
      absolute tolerance

      LabVIEW uses this error to adjust the step size. If the error is too large, the solver rejects the
       current step and reduces the step size for another try. If the error is too small, the solver
      accepts the current step and increases the step size for next try. The Relative Tolerance is
     most significant when X is large.

      •     minimum time step —

     minimum time step specifies the smallest time step size the DAE solver can use to evaluate
      the state. The minimum time step must be larger than 0. The default value is 1 E-8.

      •     maximum time step —

     maximum time step specifies the largest time step size the DAE solver can use to evaluate
      the state. The maximum time step must be larger than minimum time step. The default is
        1.

      •        initial time step —

        initial time step specifies the time step size for the first time step that the DAE solver can
       use. The initial time step must be in range of the minimum time step and maximum time
       step. The default is 0.01.


•       error in (no error) —


                                                   © National Instruments 3789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3790 ordinal=3790 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Times —

           Times returns the times at which the differential algebraic equation (DAE) solver evaluates the
              state.

               •     X Values —

          X Values returns the values of the initial state over time. For X Values and X Derivatives, each
          row contains the values evaluated at a particular time and each column contains a history of a
             particular value over time.

               •     X Derivatives —

          X Derivatives returns the values of the derivatives of the state over time. For X Values and X
             Derivatives, each row contains the values evaluated at a particular time and each column
            contains a history of a particular value over time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        ODE\DAE Simple Pendulum Simulation.vi
            • labview\examples\Mathematics\Differential Equations -
        ODE\DAE Spring Pendulum Simulation.vi
   DAEDAE RadauRadau 5th5th OrderOrder (Formula)(Formula) VIVI

       Solves differential algebraic equations (DAEs) with initial conditions by using the
      Radau IIA method. You must manually select the polymorphic instance to use.


3790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3791 ordinal=3791 -->
## Functions

Functions


Inputs/Outputs

   •     DAE F(X,X',t) —

   DAE (F,X',t) is a cluster of formula strings and variable strings that implements differential
    algebraic equations (DAEs).

    For this VI, F(X,X',t)=0.

         •        F(X,X',t) —

           F(X,X',t) is an array of strings specifying the DAEs. The specified formulas can contain any
       number of valid variables.

         •     X —

       X is an array of strings that specify the variables of the initial state.

         •       X' —

         X' is an array of strings that specify the variables of derivatives of the initial state. The length
         of X must be equal to the length of X'.

         •      time —


   •        Initial Values —

     Initial Values specify the values of the initial state of the VI.

   •        Initial Derivatives —

     Initial Derivatives specify the values of the initial state derivative. The length of the Initial
    Derivative must equal the length of the Initial Values.

   •      simulation parameters —

    simulation parameters specifies the set of parameters used to configure the differential
    algebraic equation (DAE) solver.


                                                    © National Instruments 3791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3792 ordinal=3792 -->
## Functions

Functions


                     •        initial time —

                     initial time specifies the time at which to start the DAE solver. The default is 0.

                     •       final time —

                   final time is the time at which the DAE solver stops. The final time must be larger than the
                     initial time. The default value is 10.

                     •      Absolute Tolerance —

                Absolute Tolerance specifies the absolute tolerance the DAE solver uses to control the local
                  error for each variable. You can specify either a scalar tolerance which applies to all
                  variables, or an array of tolerance which applies to each variable respectively. The Absolute
                Tolerance cannot be negative. The corresponding Absolute Tolerance and Relative
                Tolerance cannot both be zeroes. The default is 0.001.

              The DAE solver calculates the local error by the following equation: |X|*relative tolerance +
                absolute tolerance

              LabVIEW uses this error to adjust the step size. If the error is too large, the DAE solver rejects
                the current step and reduces the step size for another try. If the error is too small, the DAE
                  solver accepts the current step and increases the step size for next try. The Absolute
                Tolerance is most significant when X is small.

                     •       Relative Tolerance —

                 Relative Tolerance specifies the relative tolerance the DAE solver uses to control the local
                  error for each variable state. You can specify either a scalar tolerance which applies to all
                  variables or an array of tolerance which applies to each variable respectively. The Relative
                Tolerance cannot be negative. The Absolute Tolerance and Relative Tolerance cannot both
              be zeroes. The default is 0.001.

              The DAE solver calculates the local error by the following equation: |X|*relative tolerance +
                absolute tolerance

              LabVIEW uses this error to adjust the step size. If the error is too large, the solver rejects the
                 current step and reduces the step size for another try. If the error is too small, the solver
                accepts the current step and increases the step size for next try. The Relative Tolerance is
              most significant when X is large.

                     •     minimum time step —


3792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3793 ordinal=3793 -->
## Functions

Functions


     minimum time step specifies the smallest time step size the DAE solver can use to evaluate
      the state. The minimum time step must be larger than 0. The default value is 1 E-8.

      •     maximum time step —

     maximum time step specifies the largest time step size the DAE solver can use to evaluate
      the state. The maximum time step must be larger than minimum time step. The default is
        1.

      •        initial time step —

        initial time step specifies the time step size for the first time step that the DAE solver can
       use. The initial time step must be in range of the minimum time step and maximum time
       step. The default is 0.01.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Times —

  Times returns the times at which the differential algebraic equation (DAE) solver evaluates the
   state.

•     X Values —

  X Values returns the values of the initial state over time. For X Values and X Derivatives, each
  row contains the values evaluated at a particular time and each column contains a history of a
  particular value over time.

•     X Derivatives —

  X Derivatives returns the values of the derivatives of the state over time. For X Values and X
  Derivatives, each row contains the values evaluated at a particular time and each column
  contains a history of a particular value over time.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 3793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3794 ordinal=3794 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        ODE\DAE Simple Pendulum Simulation.vi
            • labview\examples\Mathematics\Differential Equations -
        ODE\DAE Spring Pendulum Simulation.vi

      PartialPartial DifferentialDifferential EquationsEquations

      Use the Differential Equations VIs to solve partial differential equations.

      The VIs on this palette can return mathematics error codes.


         Palette Object     Description

                            Defines the right side of a partial differential equation and its coefficients. You         Define PDE
                       must manually select the polymorphic instance to use.


         Define PDE         Defines the domain where you solve the partial differential equation. You must
       Domain           manually select the polymorphic instance to use.


         Define PDE
                            Defines the boundary condition of partial differential equations. You must
        Boundary
                         manually select the polymorphic instance to use.
         Condition


         Define PDE Initial   Defines the initial condition of a partial differential equation. You must
         Condition         manually select the polymorphic instance to use.


       PDE Solver         Solves a partial differential equation. You must manually select the


3794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3795 ordinal=3795 -->
## Functions

Functions


 Palette Object     Description

                  polymorphic instance to use.


                  Renders the solution of the partial differential equation. You must manually PDE Rendering                     select the polymorphic instance to use.


DefineDefine PDEPDE

Defines the right side of a partial differential equation and its coefficients. You must
manually select the polymorphic instance to use.


  • Define 2D Helmholtz PDE (Numeric) VI
  • Define 2D Helmholtz PDE (VIRef) VI
  • Define 1D Heat PDE (Numeric) VI
  • Define 1D Heat PDE (VIRef) VI
  • Define 2D Heat PDE (Numeric) VI
  • Define 2D Heat PDE (VIRef) VI
  • Define 1D Wave PDE (Numeric) VI
  • Define 1D Wave PDE (VIRef) VI
  • Define 2D Wave PDE (Numeric) VI
  • Define 2D Wave PDE (VIRef) VI

Helmholtz Equation

The following equation defines the Helmholtz equation:


where kand aare constant coefficients, uis the unknown function, and fis the right
side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
coordinates is defined as

                                                    © National Instruments 3795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3796 ordinal=3796 -->
## Functions

Functions


        in two-dimensional space and


        in three-dimensional space.

     Heat Equation

      The following equation defines the general form of the heat equation:


     Wave Equation

      The following equation defines the general form of the wave equation:


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D HelmholtzHelmholtz PDEPDE (Numeric)(Numeric) VIVI

       Defines the right side of a partial differential equation and its coefficients. You must

3796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3797 ordinal=3797 -->
## Functions

Functions

manually select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       F(x, y) —

     F(x, y) specifies the value of the right side of the equation.

       If the equation is defined on a rectangular domain, its size must be # of y-points-by-# of x-points
    from the Define PDE Domain VI. Each row or column of F(x, y) stores the values of the right side
     of the function evaluated on a particular y- or x-point. If the equation is defined on a polygonal
    domain, the number of columns must be equal to the number of Grid Points from the Define
   PDE Domain VI. LabVIEW uses only the first row of F(x, y), which stores the values of the right
    side of the function evaluated on Grid Points. By default, LabVIEW assumes the values of F(x, y)
    are zeros.

   •     k —

    k is a squared value that specifies the coefficient of the second order partial derivative of the
   unknown function in the equation. k cannot be 0. The default is 1.

   •      a —

    a specifies the coefficient of the unknown function in the equation. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns the right side of PDE in and its coefficients.


                                                    © National Instruments 3797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3798 ordinal=3798 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Helmholtz Equation

      The following equation defines the Helmholtz equation:


      where kand aare constant coefficients, uis the unknown function, and fis the right
       side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
       coordinates is defined as


        in two-dimensional space and


        in three-dimensional space.

     Heat Equation

      The following equation defines the general form of the heat equation:


     Wave Equation

      The following equation defines the general form of the wave equation:


3798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3799 ordinal=3799 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D HelmholtzHelmholtz PDEPDE (VIRef)(VIRef) VIVI

Defines the right side of a partial differential equation and its coefficients. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the F(x, y) VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       F(x, y) —

     F(x, y) is a strictly typed reference to the VI that implements the right side of the equation.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   pde.llb\Common\2D Stationary PDE Func Template.vit.

   •     k —

                                                    © National Instruments 3799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3800 ordinal=3800 -->
## Functions

Functions


           k is a squared value that specifies the coefficient of the second order partial derivative of the
          unknown function in the equation. k cannot be 0. The default is 1.

               •      a —

           a specifies the coefficient of the unknown function in the equation. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns the right side of PDE in and its coefficients.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Helmholtz Equation

      The following equation defines the Helmholtz equation:


      where kand aare constant coefficients, uis the unknown function, and fis the right
       side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
       coordinates is defined as


        in two-dimensional space and


        in three-dimensional space.

3800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3801 ordinal=3801 -->
## Functions

Functions

Heat Equation

The following equation defines the general form of the heat equation:


Wave Equation

The following equation defines the general form of the wave equation:


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D HeatHeat PDEPDE (Numeric)(Numeric) VIVI

Defines the right side of a partial differential equation and its coefficients. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

                                                    © National Instruments 3801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3802 ordinal=3802 -->
## Functions

Functions


         PDE in is the class that stores the data of the equation.

               •        F(t, x) —

               F(t, x) specifies the value of right side of the equation.

          The size of the right side of the equation must be # of t-points-by-# of x-points from the Define
          PDE Domain VI. Each row or column of F(t, x) stores the value of the right side of the equation
            evaluated on point X from the Define PDE Domain VI at a particular time step. By default,
           LabVIEW assumes the values of F(t, x) are zeros.

               •     k —

           k is a squared value that specifies the coefficient of the second order partial derivative of the
          unknown function in the equation. k cannot be 0. The default is 1.

               •      a —

           a specifies the coefficient of the unknown function in the equation. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns the right side of PDE in and its coefficients.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Helmholtz Equation

      The following equation defines the Helmholtz equation:


      where kand aare constant coefficients, uis the unknown function, and fis the right
       side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian

3802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3803 ordinal=3803 -->
## Functions

Functions

coordinates is defined as


in two-dimensional space and


in three-dimensional space.

Heat Equation

The following equation defines the general form of the heat equation:


Wave Equation

The following equation defines the general form of the wave equation:


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi


                                                    © National Instruments 3803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3804 ordinal=3804 -->
## Functions

Functions

    DefineDefine 1D1D HeatHeat PDEPDE (VIRef)(VIRef) VIVI

       Defines the right side of a partial differential equation and its coefficients. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      data —

           data is a variant that passes arbitrary values to the F(t, x) VI.

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •        F(t, x) —

               F(t, x) is a strictly typed reference to the VI that implements the right side of the function.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\1D Evolutionary PDE Func Template.vit.

               •     k —

           k is a squared value that specifies the coefficient of the second order partial derivative of the
          unknown function in the equation. k cannot be 0. The default is 1.

               •      a —

           a specifies the coefficient of the unknown function in the equation. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


3804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3805 ordinal=3805 -->
## Functions

Functions

   •     PDE out —

   PDE out returns the right side of PDE in and its coefficients.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Helmholtz Equation

The following equation defines the Helmholtz equation:


where kand aare constant coefficients, uis the unknown function, and fis the right
side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
coordinates is defined as


in two-dimensional space and


in three-dimensional space.

Heat Equation

The following equation defines the general form of the heat equation:


Wave Equation

The following equation defines the general form of the wave equation:


                                                    © National Instruments 3805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3806 ordinal=3806 -->
## Functions

Functions


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D HeatHeat PDEPDE (Numeric)(Numeric) VIVI

       Defines the right side of a partial differential equation and its coefficients. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •        F(t, x, y) —

               F(t, x, y) specifies the value of the right side of the equation.

          The size of the right side of the equation must be # of t-points-by-# of y-points-by-# of x-points
           from the Define PDE Domain VI. Each page of F(t, x, y) stores the value of the right side of the
            equation evaluated on mesh grid points (X, Y) from the Define PDE Domain VI at a particular time
              step. On one page of F(t, x, y), each row or column stores the values of the right side of the


3806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3807 ordinal=3807 -->
## Functions

Functions


    equation evaluated on a particular y- or x-point. By default, LabVIEW assumes the values of F(t,
     x, y) are zeros.

   •     k —

    k is a squared value that specifies the coefficient of the second order partial derivative of the
   unknown function in the equation. k cannot be 0. The default is 1.

   •      a —

    a specifies the coefficient of the unknown function in the equation. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns the right side of PDE in and its coefficients.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Helmholtz Equation

The following equation defines the Helmholtz equation:


where kand aare constant coefficients, uis the unknown function, and fis the right
side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
coordinates is defined as


in two-dimensional space and


                                                    © National Instruments 3807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3808 ordinal=3808 -->
## Functions

Functions


        in three-dimensional space.

     Heat Equation

      The following equation defines the general form of the heat equation:


     Wave Equation

      The following equation defines the general form of the wave equation:


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D HeatHeat PDEPDE (VIRef)(VIRef) VIVI

       Defines the right side of a partial differential equation and its coefficients. You must
      manually select the polymorphic instance to use.


3808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3809 ordinal=3809 -->
## Functions

Functions


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the F(t, x, y) VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •        F(t, x, y) —

     F(t, x, y) is a strictly typed reference to the VI that implements the right side of the equation.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   pde.llb\Common\2D Evolutionary PDE Func Template.vit.

   •     k —

    k is a squared value that specifies the coefficient of the second order partial derivative of the
   unknown function in the equation. k cannot be 0. The default is 1.

   •      a —

    a specifies the coefficient of the unknown function in the equation. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns the right side of PDE in and its coefficients.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 3809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3810 ordinal=3810 -->
## Functions

Functions

     Helmholtz Equation

      The following equation defines the Helmholtz equation:


      where kand aare constant coefficients, uis the unknown function, and fis the right
       side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
       coordinates is defined as


        in two-dimensional space and


        in three-dimensional space.

     Heat Equation

      The following equation defines the general form of the heat equation:


     Wave Equation

      The following equation defines the general form of the wave equation:


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -

3810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3811 ordinal=3811 -->
## Functions

Functions

   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D WaveWave PDEPDE (Numeric)(Numeric) VIVI

Defines the right side of a partial differential equation and its coefficients. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •        F(t, x) —

     F(t, x) specifies the value of right side of the equation.

    The size of the right side of the equation must be # of t-points-by-# of x-points from the Define
   PDE Domain VI. Each row or column of F(t, x) stores the value of the right side of the equation
    evaluated on point X from the Define PDE Domain VI at a particular time step. By default,
    LabVIEW assumes the values of F(t, x) are zeros.

   •     k —

    k is a squared value that specifies the coefficient of the second order partial derivative of the
   unknown function in the equation. k cannot be 0. The default is 1.

   •      a —

    a specifies the coefficient of the unknown function in the equation. The default is 0.


                                                    © National Instruments 3811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3812 ordinal=3812 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns the right side of PDE in and its coefficients.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Helmholtz Equation

      The following equation defines the Helmholtz equation:


      where kand aare constant coefficients, uis the unknown function, and fis the right
       side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
       coordinates is defined as


        in two-dimensional space and


        in three-dimensional space.

     Heat Equation

      The following equation defines the general form of the heat equation:


3812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3813 ordinal=3813 -->
## Functions

Functions

Wave Equation

The following equation defines the general form of the wave equation:


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D WaveWave PDEPDE (VIRef)(VIRef) VIVI

Defines the right side of a partial differential equation and its coefficients. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.


                                                    © National Instruments 3813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3814 ordinal=3814 -->
## Functions

Functions

               •        F(t, x) —

               F(t, x) is a strictly typed reference to the VI that implements the right side of the function.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\1D Evolutionary PDE Func Template.vit.

               •     k —

           k is a squared value that specifies the coefficient of the second order partial derivative of the
          unknown function in the equation. k cannot be 0. The default is 1.

               •      a —

           a specifies the coefficient of the unknown function in the equation. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns the right side of PDE in and its coefficients.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Helmholtz Equation

      The following equation defines the Helmholtz equation:


      where kand aare constant coefficients, uis the unknown function, and fis the right
       side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
       coordinates is defined as


3814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3815 ordinal=3815 -->
## Functions

Functions

in two-dimensional space and


in three-dimensional space.

Heat Equation

The following equation defines the general form of the heat equation:


Wave Equation

The following equation defines the general form of the wave equation:


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D WaveWave PDEPDE (Numeric)(Numeric) VIVI

Defines the right side of a partial differential equation and its coefficients. You must
manually select the polymorphic instance to use.


                                                    © National Instruments 3815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3816 ordinal=3816 -->
## Functions

Functions


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •        F(t, x, y) —

               F(t, x, y) specifies the value of the right side of the equation.

          The size of the right side of the equation must be # of t-points-by-# of y-points-by-# of x-points
           from the Define PDE Domain VI. Each page of F(t, x, y) stores the value of the right side of the
            equation evaluated on mesh grid points (X, Y) from the Define PDE Domain VI at a particular time
              step. On one page of F(t, x, y), each row or column stores the values of the right side of the
            equation evaluated on a particular y- or x-point. By default, LabVIEW assumes the values of F(t,
              x, y) are zeros.

               •     k —

           k is a squared value that specifies the coefficient of the second order partial derivative of the
          unknown function in the equation. k cannot be 0. The default is 1.

               •      a —

           a specifies the coefficient of the unknown function in the equation. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns the right side of PDE in and its coefficients.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


3816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3817 ordinal=3817 -->
## Functions

Functions

Helmholtz Equation

The following equation defines the Helmholtz equation:


where kand aare constant coefficients, uis the unknown function, and fis the right
side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
coordinates is defined as


in two-dimensional space and


in three-dimensional space.

Heat Equation

The following equation defines the general form of the heat equation:


Wave Equation

The following equation defines the general form of the wave equation:


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -

                                                    © National Instruments 3817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3818 ordinal=3818 -->
## Functions

Functions

        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D WaveWave PDEPDE (VIRef)(VIRef) VIVI

       Defines the right side of a partial differential equation and its coefficients. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •      data —

           data is a variant that passes arbitrary values to the F(t, x, y) VI.

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •        F(t, x, y) —

               F(t, x, y) is a strictly typed reference to the VI that implements the right side of the equation.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\2D Evolutionary PDE Func Template.vit.

               •     k —

           k is a squared value that specifies the coefficient of the second order partial derivative of the
          unknown function in the equation. k cannot be 0. The default is 1.

               •      a —


3818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3819 ordinal=3819 -->
## Functions

Functions


    a specifies the coefficient of the unknown function in the equation. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns the right side of PDE in and its coefficients.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Helmholtz Equation

The following equation defines the Helmholtz equation:


where kand aare constant coefficients, uis the unknown function, and fis the right
side of the equation. The operator    is the Laplacian. The Laplacian in Cartesian
coordinates is defined as


in two-dimensional space and


in three-dimensional space.

Heat Equation

The following equation defines the general form of the heat equation:

                                                    © National Instruments 3819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3820 ordinal=3820 -->
## Functions

Functions


     Wave Equation

      The following equation defines the general form of the wave equation:


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi

      DefineDefine PDEPDE DomainDomain

       Defines the domain where you solve the partial differential equation. You must
      manually select the polymorphic instance to use.


            • Define 2D Helmholtz PDE Domain (Rect) VI
            • Define 2D Helmholtz PDE Domain (Polygon) VI
            • Define 1D Heat PDE Domain VI
            • Define 2D Heat PDE Domain (Rect) VI
            • Define 1D Wave PDE Domain VI
            • Define 2D Wave PDE Domain (Rect) VI

      The following illustration shows the uniform mesh grid on a rectangular domain with
       the default values. Both the x- and y-axes range from 0 to 1 with 11 evenly spaced grid
       points. The black circle points are the points on the boundary of the rectangular

3820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3821 ordinal=3821 -->
## Functions

Functions

domain. The red square points are the inner points on the mesh grid.


The following illustration shows the unit circle on a polygonal domain. The black circle
points are the points on the boundary of the domain that generate evenly on the unit
circle. The red square points are the inner grid points that generate automatically with
the default of grid factor.

      Note You must specify the boundary points in a clockwise or
       counterclockwise direction.


                                                    © National Instruments 3821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3822 ordinal=3822 -->
## Functions

Functions


      The following block diagram illustrates a VI that defines the polygonal domain, as
      shown in the previous illustration.


           If you do not wire a value to Grid Points, LabVIEW generates the boundary points
       automatically based on grid factor, which determines the density of the grid points.
      LabVIEW performs triangulation on the grid points before solving the equation. The
       grid factor approximates the ratio of the average area of the triangles to the area of the
      whole polygonal domain.

           If you have prior knowledge of the unknown function, wire a value to Grid Points. You
      can use sparse grid points in areas where the unknown function varies smoothly and

3822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3823 ordinal=3823 -->
## Functions

Functions

use dense grid points in areas where the unknown function varies sharply. For some
problems, this flexibility in the choice of grid points can return better results than a set
of uniformly distributed grid points.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D HelmholtzHelmholtz PDEPDE DomainDomain (Rect)(Rect) VIVI

Defines the domain where you solve the partial differential equation. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     X —

    X specifies the uniform mesh grid along the x-axis.

         •       start x —


                                                    © National Instruments 3823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3824 ordinal=3824 -->
## Functions

Functions


                  start x specifies the starting mesh grid point x0 along the x-axis. start x must be less than
              end x. The default is 0.

                     •     end x —

              end x specifies the ending mesh grid point xm along the x-axis. end x must be greater than
                  start x. The default is 1.

                     •      # of x-points —

              # of x-points specifies the number of grid points along the x-axis. # of x-points is equal to m
               + 1 and must be greater than 2. The default is 11.


               •      Y —

           Y specifies the uniform mesh grid along the y-axis.

                     •       start y —

                  start y specifies the starting mesh grid point y0 along the y-axis. start y must be less than
              end y. The default is 0.

                     •     end y —

              end y specifies the ending mesh grid point yn along the y-axis. end y must be greater than
                  start y. The default is 1.

                     •      # of y-points —

              # of y-points specifies the number of grid points along the y-axis. # of y-points is equal to n
               + 1 and must be greater than 2. The default is 11.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —


3824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3825 ordinal=3825 -->
## Functions

Functions


   PDE out returns PDE in with the domain.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following illustration shows the uniform mesh grid on a rectangular domain with
the default values. Both the x- and y-axes range from 0 to 1 with 11 evenly spaced grid
points. The black circle points are the points on the boundary of the rectangular
domain. The red square points are the inner points on the mesh grid.


The following illustration shows the unit circle on a polygonal domain. The black circle
points are the points on the boundary of the domain that generate evenly on the unit
circle. The red square points are the inner grid points that generate automatically with
the default of grid factor.

      Note You must specify the boundary points in a clockwise or
       counterclockwise direction.


                                                    © National Instruments 3825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3826 ordinal=3826 -->
## Functions

Functions


      The following block diagram illustrates a VI that defines the polygonal domain, as
      shown in the previous illustration.


           If you do not wire a value to Grid Points, LabVIEW generates the boundary points
       automatically based on grid factor, which determines the density of the grid points.
      LabVIEW performs triangulation on the grid points before solving the equation. The
       grid factor approximates the ratio of the average area of the triangles to the area of the
      whole polygonal domain.

           If you have prior knowledge of the unknown function, wire a value to Grid Points. You
      can use sparse grid points in areas where the unknown function varies smoothly and

3826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3827 ordinal=3827 -->
## Functions

Functions

use dense grid points in areas where the unknown function varies sharply. For some
problems, this flexibility in the choice of grid points can return better results than a set
of uniformly distributed grid points.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D HelmholtzHelmholtz PDEPDE DomainDomain (Polygon)(Polygon)
VIVI

Defines the domain where you solve the partial differential equation. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •       grid factor —

    grid factor specifies the density of the grid points that LabVIEW automatically generates. A
    smaller grid factor leads to denser grid points, which results in a more accurate solution but
   more computation time and memory. LabVIEW ignores grid factor if you wire a value to Grid
     Points. grid factor must be greater than 0 and less than 1. The default is 0.005.

   •     PDE in —


                                                    © National Instruments 3827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3828 ordinal=3828 -->
## Functions

Functions


         PDE in is the class that stores the data of the equation.

               •     Boundary Points —

          Boundary Points specifies the boundary points that define a polygonal domain. The boundary
            points must be in a clockwise or counterclockwise direction. The number of points must be
             greater than 2.

                     •     X —

              X specifies the x-coordinate of Boundary Points.

                     •      Y —

               Y specifies the y-coordinate of Boundary Points.


               •      Grid Points —

            Grid Points specifies the grid points for the equation. The grid points must be in the polygonal
           domain. LabVIEW removes the points that are not in the polygonal domain. If you do not wire a
            value to Grid Points, LabVIEW automatically generates the grid points based on grid factor.

                     •     X —

              X specifies the x-coordinate of Grid Points.

                     •      Y —

               Y specifies the y-coordinate of Grid Points.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the domain.

               •       error out —


3828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3829 ordinal=3829 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


The following illustration shows the uniform mesh grid on a rectangular domain with
the default values. Both the x- and y-axes range from 0 to 1 with 11 evenly spaced grid
points. The black circle points are the points on the boundary of the rectangular
domain. The red square points are the inner points on the mesh grid.


The following illustration shows the unit circle on a polygonal domain. The black circle
points are the points on the boundary of the domain that generate evenly on the unit
circle. The red square points are the inner grid points that generate automatically with
the default of grid factor.

      Note You must specify the boundary points in a clockwise or
       counterclockwise direction.


                                                    © National Instruments 3829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3830 ordinal=3830 -->
## Functions

Functions


      The following block diagram illustrates a VI that defines the polygonal domain, as
      shown in the previous illustration.


           If you do not wire a value to Grid Points, LabVIEW generates the boundary points
       automatically based on grid factor, which determines the density of the grid points.
      LabVIEW performs triangulation on the grid points before solving the equation. The
       grid factor approximates the ratio of the average area of the triangles to the area of the
      whole polygonal domain.

           If you have prior knowledge of the unknown function, wire a value to Grid Points. You
      can use sparse grid points in areas where the unknown function varies smoothly and

3830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3831 ordinal=3831 -->
## Functions

Functions

use dense grid points in areas where the unknown function varies sharply. For some
problems, this flexibility in the choice of grid points can return better results than a set
of uniformly distributed grid points.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D HeatHeat PDEPDE DomainDomain VIVI

Defines the domain where you solve the partial differential equation. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     T —

   T specifies the uniform time steps.

         •        initial t —


                                                    © National Instruments 3831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3832 ordinal=3832 -->
## Functions

Functions


                     initial t specifies the initial time step t0. initial t must be less than final t. The default is 0.

                     •       final t —

                   final t specifies the final time step tl. final t must be greater than initial t. The default is 1.

                     •      # of t-points —

              # of t-points specifies the number of time steps. # of t-points is equal to l+ 1 and must be
                 greater than 1. The default is 11.


               •     X —

          X specifies the evenly spaced points along the x-axis.

                     •       start x —

                  start x specifies the starting point x0 along the x-axis. start x must be less than end x. The
                 default is 0.

                     •     end x —

              end x specifies the ending point xm along the x-axis. end x must be greater than start x. The
                 default is 1.

                     •      # of x-points —

              # of x-points specifies the number of points along the x-axis. # of x-points is equal to m+ 1
              and must be greater than 2. The default is 11.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the domain.

               •       error out —

3832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3833 ordinal=3833 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


The following illustration shows the uniform mesh grid on a rectangular domain with
the default values. Both the x- and y-axes range from 0 to 1 with 11 evenly spaced grid
points. The black circle points are the points on the boundary of the rectangular
domain. The red square points are the inner points on the mesh grid.


The following illustration shows the unit circle on a polygonal domain. The black circle
points are the points on the boundary of the domain that generate evenly on the unit
circle. The red square points are the inner grid points that generate automatically with
the default of grid factor.

      Note You must specify the boundary points in a clockwise or
       counterclockwise direction.


                                                    © National Instruments 3833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3834 ordinal=3834 -->
## Functions

Functions


      The following block diagram illustrates a VI that defines the polygonal domain, as
      shown in the previous illustration.


           If you do not wire a value to Grid Points, LabVIEW generates the boundary points
       automatically based on grid factor, which determines the density of the grid points.
      LabVIEW performs triangulation on the grid points before solving the equation. The
       grid factor approximates the ratio of the average area of the triangles to the area of the
      whole polygonal domain.

           If you have prior knowledge of the unknown function, wire a value to Grid Points. You
      can use sparse grid points in areas where the unknown function varies smoothly and

3834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3835 ordinal=3835 -->
## Functions

Functions

use dense grid points in areas where the unknown function varies sharply. For some
problems, this flexibility in the choice of grid points can return better results than a set
of uniformly distributed grid points.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D HeatHeat PDEPDE DomainDomain (Rect)(Rect) VIVI

Defines the domain where you solve the partial differential equation. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     T —

   T specifies the uniform time steps.

         •        initial t —


                                                    © National Instruments 3835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3836 ordinal=3836 -->
## Functions

Functions


                     initial t specifies the initial time step t0. initial t must be less than final t. The default is 0.

                     •       final t —

                   final t specifies the final time step tl. final t must be greater than initial t. The default is 1.

                     •      # of t-points —

              # of t-points specifies the number of time steps. # of t-points is equal to l+ 1 and must be
                 greater than 1. The default is 11.


               •     X —

          X specifies the uniform mesh grid along the x-axis.

                     •       start x —

                  start x specifies the starting mesh grid point x0 along the x-axis. start x must be less than
              end x. The default is 0.

                     •     end x —

              end x specifies the ending mesh grid point xm along the x-axis. end x must be greater than
                  start x. The default is 1.

                     •      # of x-points —

              # of x-points specifies the number of grid points along the x-axis. # of x-points is equal to m
               + 1 and must be greater than 2. The default is 11.


               •      Y —

           Y specifies the uniform mesh grid along the y-axis.

                     •       start y —

                  start y specifies the starting mesh grid point y0 along the y-axis. start y must be less than


3836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3837 ordinal=3837 -->
## Functions

Functions


       end y. The default is 0.

         •     end y —

       end y specifies the ending mesh grid point yn along the y-axis. end y must be greater than
          start y. The default is 1.

         •      # of y-points —

       # of y-points specifies the number of grid points along the y-axis. # of y-points is equal to n
        + 1 and must be greater than 2. The default is 11.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in with the domain.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following illustration shows the uniform mesh grid on a rectangular domain with
the default values. Both the x- and y-axes range from 0 to 1 with 11 evenly spaced grid
points. The black circle points are the points on the boundary of the rectangular
domain. The red square points are the inner points on the mesh grid.


                                                    © National Instruments 3837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3838 ordinal=3838 -->
## Functions

Functions


      The following illustration shows the unit circle on a polygonal domain. The black circle
       points are the points on the boundary of the domain that generate evenly on the unit
         circle. The red square points are the inner grid points that generate automatically with
       the default of grid factor.

           Note You must specify the boundary points in a clockwise or
              counterclockwise direction.


3838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3839 ordinal=3839 -->
## Functions

Functions


The following block diagram illustrates a VI that defines the polygonal domain, as
shown in the previous illustration.


If you do not wire a value to Grid Points, LabVIEW generates the boundary points
automatically based on grid factor, which determines the density of the grid points.
LabVIEW performs triangulation on the grid points before solving the equation. The
grid factor approximates the ratio of the average area of the triangles to the area of the
whole polygonal domain.

If you have prior knowledge of the unknown function, wire a value to Grid Points. You
can use sparse grid points in areas where the unknown function varies smoothly and

                                                    © National Instruments 3839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3840 ordinal=3840 -->
## Functions

Functions

      use dense grid points in areas where the unknown function varies sharply. For some
       problems, this flexibility in the choice of grid points can return better results than a set
       of uniformly distributed grid points.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 1D1D WaveWave PDEPDE DomainDomain VIVI

       Defines the domain where you solve the partial differential equation. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •     T —

          T specifies the uniform time steps.

                     •        initial t —


3840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3841 ordinal=3841 -->
## Functions

Functions


        initial t specifies the initial time step t0. initial t must be less than final t. The default is 0.

      •       final t —

       final t specifies the final time step tl. final t must be greater than initial t. The default is 1.

      •      # of t-points —

      # of t-points specifies the number of time steps. # of t-points is equal to l+ 1 and must be
       greater than 1. The default is 11.


•     X —

  X specifies the evenly spaced points along the x-axis.

      •       start x —

       start x specifies the starting point x0 along the x-axis. start x must be less than end x. The
       default is 0.

      •     end x —

     end x specifies the ending point xm along the x-axis. end x must be greater than start x. The
       default is 1.

      •      # of x-points —

      # of x-points specifies the number of points along the x-axis. # of x-points is equal to m+ 1
     and must be greater than 2. The default is 11.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     PDE out —

  PDE out returns PDE in with the domain.

•       error out —

                                                   © National Instruments 3841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3842 ordinal=3842 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


      The following illustration shows the uniform mesh grid on a rectangular domain with
       the default values. Both the x- and y-axes range from 0 to 1 with 11 evenly spaced grid
       points. The black circle points are the points on the boundary of the rectangular
      domain. The red square points are the inner points on the mesh grid.


      The following illustration shows the unit circle on a polygonal domain. The black circle
       points are the points on the boundary of the domain that generate evenly on the unit
         circle. The red square points are the inner grid points that generate automatically with
       the default of grid factor.

           Note You must specify the boundary points in a clockwise or
              counterclockwise direction.


3842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3843 ordinal=3843 -->
## Functions

Functions


The following block diagram illustrates a VI that defines the polygonal domain, as
shown in the previous illustration.


If you do not wire a value to Grid Points, LabVIEW generates the boundary points
automatically based on grid factor, which determines the density of the grid points.
LabVIEW performs triangulation on the grid points before solving the equation. The
grid factor approximates the ratio of the average area of the triangles to the area of the
whole polygonal domain.

If you have prior knowledge of the unknown function, wire a value to Grid Points. You
can use sparse grid points in areas where the unknown function varies smoothly and

                                                    © National Instruments 3843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3844 ordinal=3844 -->
## Functions

Functions

      use dense grid points in areas where the unknown function varies sharply. For some
       problems, this flexibility in the choice of grid points can return better results than a set
       of uniformly distributed grid points.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D WaveWave PDEPDE DomainDomain (Rect)(Rect) VIVI

       Defines the domain where you solve the partial differential equation. You must
      manually select the polymorphic instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •     T —

          T specifies the uniform time steps.

                     •        initial t —


3844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3845 ordinal=3845 -->
## Functions

Functions


        initial t specifies the initial time step t0. initial t must be less than final t. The default is 0.

      •       final t —

       final t specifies the final time step tl. final t must be greater than initial t. The default is 1.

      •      # of t-points —

      # of t-points specifies the number of time steps. # of t-points is equal to l+ 1 and must be
       greater than 1. The default is 11.


•     X —

  X specifies the uniform mesh grid along the x-axis.

      •       start x —

       start x specifies the starting mesh grid point x0 along the x-axis. start x must be less than
     end x. The default is 0.

      •     end x —

     end x specifies the ending mesh grid point xm along the x-axis. end x must be greater than
       start x. The default is 1.

      •      # of x-points —

      # of x-points specifies the number of grid points along the x-axis. # of x-points is equal to m
      + 1 and must be greater than 2. The default is 11.


•      Y —

  Y specifies the uniform mesh grid along the y-axis.

      •       start y —

       start y specifies the starting mesh grid point y0 along the y-axis. start y must be less than


                                                   © National Instruments 3845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3846 ordinal=3846 -->
## Functions

Functions


              end y. The default is 0.

                     •     end y —

              end y specifies the ending mesh grid point yn along the y-axis. end y must be greater than
                  start y. The default is 1.

                     •      # of y-points —

              # of y-points specifies the number of grid points along the y-axis. # of y-points is equal to n
               + 1 and must be greater than 2. The default is 11.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the domain.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following illustration shows the uniform mesh grid on a rectangular domain with
       the default values. Both the x- and y-axes range from 0 to 1 with 11 evenly spaced grid
       points. The black circle points are the points on the boundary of the rectangular
      domain. The red square points are the inner points on the mesh grid.


3846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3847 ordinal=3847 -->
## Functions

Functions


The following illustration shows the unit circle on a polygonal domain. The black circle
points are the points on the boundary of the domain that generate evenly on the unit
circle. The red square points are the inner grid points that generate automatically with
the default of grid factor.

      Note You must specify the boundary points in a clockwise or
       counterclockwise direction.


                                                    © National Instruments 3847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3848 ordinal=3848 -->
## Functions

Functions


      The following block diagram illustrates a VI that defines the polygonal domain, as
      shown in the previous illustration.


           If you do not wire a value to Grid Points, LabVIEW generates the boundary points
       automatically based on grid factor, which determines the density of the grid points.
      LabVIEW performs triangulation on the grid points before solving the equation. The
       grid factor approximates the ratio of the average area of the triangles to the area of the
      whole polygonal domain.

           If you have prior knowledge of the unknown function, wire a value to Grid Points. You
      can use sparse grid points in areas where the unknown function varies smoothly and

3848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3849 ordinal=3849 -->
## Functions

Functions

use dense grid points in areas where the unknown function varies sharply. For some
problems, this flexibility in the choice of grid points can return better results than a set
of uniformly distributed grid points.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi

DefineDefine PDEPDE BoundaryBoundary ConditionCondition

Defines the boundary condition of partial differential equations. You must manually
select the polymorphic instance to use.


  • Define 2D Helmholtz PDE BC (Numeric) VI
  • Define 2D Helmholtz PDE BC (VIRef) VI
  • Define 1D Heat PDE BC (Numeric) VI
  • Define 1D Heat PDE BC (VIRef) VI
  • Define 2D Heat PDE BC (Numeric) VI
  • Define 2D Heat PDE BC (VIRef) VI
  • Define 1D Wave PDE BC (Numeric) VI
  • Define 1D Wave PDE BC (VIRef) VI
  • Define 2D Wave PDE BC (Numeric) VI
  • Define 2D Wave PDE BC (VIRef) VI

The following table gives the definitions of a normal derivative for one-dimensional
equations and for two-dimensional equations defined on a rectangular domain.


                                                    © National Instruments 3849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3850 ordinal=3850 -->
## Functions

Functions

           Note If the boundary type is Neumann, you must specify the value of the
             normal derivative of the unknown function and not the value of derivatives
              along the x- or y-axes. Moreover, you cannot specify the Neumann condition
            on a polygonal domain.


         Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

       Start X


       End X


       Start Y  N/A


       End Y     N/A


      The following block diagram is an example of defining the boundary condition for a
      one-dimensional wave equation. The boundary condition at Start X is
     Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
      which the numeric array defines.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -

3850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3851 ordinal=3851 -->
## Functions

Functions

   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D HelmholtzHelmholtz PDEPDE BCBC (Numeric)(Numeric) VIVI

Defines the boundary condition of partial differential equations. You must manually
select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     Boundary Condition —

    Boundary Condition specifies the value of the boundary condition.

       If you define the equation on the rectangular domain, Boundary Condition stores the values of
    the unknown function evaluated at position. When position is Start X or End X, the length
     of Boundary Condition must be # of y-points from the Define PDE Domain VI. When position is
   Start Y or End Y, the length of Boundary Condition must be # of x-points from the Define
   PDE Domain VI. If the equation is defined on the polygonal domain, Boundary Condition stores
    the values of the unknown function evaluated at Boundary Points from the Define PDE Domain
      VI. The length of Boundary Condition must equal the number of Boundary Points. By default,
    LabVIEW assumes that the boundary condition values are zeros.

   •      type —

    type specifies the type of boundary condition. If you define the equation on the polygonal
    domain, type must be Dirichlet.

    0 Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function


                                                    © National Instruments 3851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3852 ordinal=3852 -->
## Functions

Functions


              to specify the boundary condition.
          Neumann—The boundary of the domain evaluates the value of the normal derivative of the           1           unknown function to specify the boundary condition.

               •      position —

            position specifies the position of the boundary condition. If you define the equation on the
            polygonal domain, position must be Start X.

              Start X (default)—LabVIEW evaluates the boundary condition with start x of the rectangular
           0           domain or Boundary Points of the polygonal domain from the Define PDE Domain VI.
           1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.
              Start Y—LabVIEW evaluates the boundary condition with start y from the Define PDE Domain           2
                  VI.
           3 End Y—LabVIEW evaluates the boundary condition with end y from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the boundary condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following table gives the definitions of a normal derivative for one-dimensional
       equations and for two-dimensional equations defined on a rectangular domain.

           Note If the boundary type is Neumann, you must specify the value of the
             normal derivative of the unknown function and not the value of derivatives
              along the x- or y-axes. Moreover, you cannot specify the Neumann condition
            on a polygonal domain.


3852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3853 ordinal=3853 -->
## Functions

Functions


 Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

 Start X


 End X


 Start Y  N/A


 End Y     N/A


The following block diagram is an example of defining the boundary condition for a
one-dimensional wave equation. The boundary condition at Start X is
Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
which the numeric array defines.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi


                                                    © National Instruments 3853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3854 ordinal=3854 -->
## Functions

Functions

    DefineDefine 2D2D HelmholtzHelmholtz PDEPDE BCBC (VIRef)(VIRef) VIVI

       Defines the boundary condition of partial differential equations. You must manually
        select the polymorphic instance to use.


      Inputs/Outputs

               •      data —

           data is a variant that passes arbitrary values to the VI.

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •     Boundary Condition —

          Boundary Condition is a strictly typed reference to the VI that implements the boundary
             condition.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\2D Stationary PDE Func Template.vit.

               •      type —

           type specifies the type of boundary condition. If you define the equation on the polygonal
           domain, type must be Dirichlet.

               Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function
           0
              to specify the boundary condition.
          Neumann—The boundary of the domain evaluates the value of the normal derivative of the
           1
           unknown function to specify the boundary condition.

               •      position —


3854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3855 ordinal=3855 -->
## Functions

Functions


    position specifies the position of the boundary condition. If you define the equation on the
    polygonal domain, position must be Start X.

      Start X (default)—LabVIEW evaluates the boundary condition with start x of the rectangular
    0     domain or Boundary Points of the polygonal domain from the Define PDE Domain VI.
    1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.
      Start Y—LabVIEW evaluates the boundary condition with start y from the Define PDE Domain    2       VI.
    3 End Y—LabVIEW evaluates the boundary condition with end y from the Define PDE Domain VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in with the boundary condition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following table gives the definitions of a normal derivative for one-dimensional
equations and for two-dimensional equations defined on a rectangular domain.

      Note If the boundary type is Neumann, you must specify the value of the
       normal derivative of the unknown function and not the value of derivatives
       along the x- or y-axes. Moreover, you cannot specify the Neumann condition
      on a polygonal domain.


 Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

 Start X


 End X


                                                    © National Instruments 3855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3856 ordinal=3856 -->
## Functions

Functions


         Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

       Start Y  N/A


       End Y     N/A


      The following block diagram is an example of defining the boundary condition for a
      one-dimensional wave equation. The boundary condition at Start X is
     Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
      which the numeric array defines.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 1D1D HeatHeat PDEPDE BCBC (Numeric)(Numeric) VIVI

       Defines the boundary condition of partial differential equations. You must manually
        select the polymorphic instance to use.


3856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3857 ordinal=3857 -->
## Functions

Functions


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     Boundary Condition —

    Boundary Condition specifies the value of the boundary condition. Its length must be # of t-
    points from the Define PDE Domain VI. It stores the values of the unknown function evaluated at
    position over time. By default, LabVIEW assumes that the boundary condition values are zeros.

   •      type —

    type specifies the type of the boundary condition.

      Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function    0
      to specify the boundary condition.
    Neumann—The boundary of the domain evaluates the value of the normal derivative of the    1
    unknown function to specify the boundary condition.

   •      position —

    position specifies the position of the boundary condition.

      Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE
    0
     Domain VI.
    1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in with the boundary condition.


                                                    © National Instruments 3857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3858 ordinal=3858 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following table gives the definitions of a normal derivative for one-dimensional
       equations and for two-dimensional equations defined on a rectangular domain.

           Note If the boundary type is Neumann, you must specify the value of the
             normal derivative of the unknown function and not the value of derivatives
              along the x- or y-axes. Moreover, you cannot specify the Neumann condition
            on a polygonal domain.


         Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

       Start X


       End X


       Start Y  N/A


       End Y     N/A


      The following block diagram is an example of defining the boundary condition for a
      one-dimensional wave equation. The boundary condition at Start X is
     Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
      which the numeric array defines.


3858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3859 ordinal=3859 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D HeatHeat PDEPDE BCBC (VIRef)(VIRef) VIVI

Defines the boundary condition of partial differential equations. You must manually
select the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     Boundary Condition —

    Boundary Condition is a strictly typed reference to the VI that implements the boundary
    condition.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   pde.llb\Common\1D Evolutionary PDE Func Template.vit.


                                                    © National Instruments 3859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3860 ordinal=3860 -->
## Functions

Functions

               •      type —

           type specifies the type of the boundary condition.

               Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function           0              to specify the boundary condition.
          Neumann—The boundary of the domain evaluates the value of the normal derivative of the           1           unknown function to specify the boundary condition.

               •      position —

            position specifies the position of the boundary condition.

              Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE
           0           Domain VI.
           1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the boundary condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following table gives the definitions of a normal derivative for one-dimensional
       equations and for two-dimensional equations defined on a rectangular domain.

           Note If the boundary type is Neumann, you must specify the value of the
             normal derivative of the unknown function and not the value of derivatives
              along the x- or y-axes. Moreover, you cannot specify the Neumann condition
            on a polygonal domain.


3860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3861 ordinal=3861 -->
## Functions

Functions


 Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

 Start X


 End X


 Start Y  N/A


 End Y     N/A


The following block diagram is an example of defining the boundary condition for a
one-dimensional wave equation. The boundary condition at Start X is
Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
which the numeric array defines.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi


                                                    © National Instruments 3861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3862 ordinal=3862 -->
## Functions

Functions

    DefineDefine 2D2D HeatHeat PDEPDE BCBC (Numeric)(Numeric) VIVI

       Defines the boundary condition of partial differential equations. You must manually
        select the polymorphic instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •     Boundary Condition —

          Boundary Condition specifies the value of boundary condition.

         When position is Start X or End X, the size of Boundary Condition must be # of t-
            points-by-# of y-points from the Define PDE Domain VI. Each row of Boundary Condition stores
            the values of the unknown function evaluated on points Y from the Define PDE Domain VI at a
             particular time step. Each column of Boundary Condition stores the values of the unknown
             function evaluated at a particular y-point over time. When position is Start Y or End Y, the
              size of Boundary Condition must be # of t-points-by-# of x-points from the Define PDE Domain
                VI. Each row of Boundary Condition stores the values of the unknown function evaluated on
            points X from the Define PDE Domain VI at a particular time step. Each column of Boundary
            Condition stores the values of the unknown function evaluated at particular x-points over time.
           By default, LabVIEW assumes that the boundary condition values are zeros.

               •      type —

           type specifies the type of the boundary condition.

               Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function
           0
              to specify the boundary condition.
          Neumann—The boundary of the domain evaluates the value of the normal derivative of the
           1
           unknown function to specify the boundary condition.


3862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3863 ordinal=3863 -->
## Functions

Functions

   •      position —

    position specifies the position of the boundary condition.

      Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE    0     Domain VI.
    1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.
      Start Y—LabVIEW evaluates the boundary condition with start y from the Define PDE Domain
    2       VI.
    3 End Y—LabVIEW evaluates the boundary condition with end y from the Define PDE Domain VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in with the boundary condition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following table gives the definitions of a normal derivative for one-dimensional
equations and for two-dimensional equations defined on a rectangular domain.

      Note If the boundary type is Neumann, you must specify the value of the
       normal derivative of the unknown function and not the value of derivatives
       along the x- or y-axes. Moreover, you cannot specify the Neumann condition
      on a polygonal domain.


 Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

 Start X


 End X


                                                    © National Instruments 3863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3864 ordinal=3864 -->
## Functions

Functions


         Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

       Start Y  N/A


       End Y     N/A


      The following block diagram is an example of defining the boundary condition for a
      one-dimensional wave equation. The boundary condition at Start X is
     Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
      which the numeric array defines.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D HeatHeat PDEPDE BCBC (VIRef)(VIRef) VIVI

       Defines the boundary condition of partial differential equations. You must manually
        select the polymorphic instance to use.


3864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3865 ordinal=3865 -->
## Functions

Functions


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     Boundary Condition —

    Boundary Condition is a strictly typed reference to the VI that implements the boundary
    condition.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   pde.llb\Common\2D Stationary PDE Func Template.vit.

   •      type —

    type specifies the type of the boundary condition.

      Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function    0      to specify the boundary condition.
    Neumann—The boundary of the domain evaluates the value of the normal derivative of the    1
    unknown function to specify the boundary condition.

   •      position —

    position specifies the position of the boundary condition.

      Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE
    0
     Domain VI.
    1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.
      Start Y—LabVIEW evaluates the boundary condition with start y from the Define PDE Domain
    2
       VI.


                                                    © National Instruments 3865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3866 ordinal=3866 -->
## Functions

Functions


           3 End Y—LabVIEW evaluates the boundary condition with end y from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the boundary condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following table gives the definitions of a normal derivative for one-dimensional
       equations and for two-dimensional equations defined on a rectangular domain.

           Note If the boundary type is Neumann, you must specify the value of the
             normal derivative of the unknown function and not the value of derivatives
              along the x- or y-axes. Moreover, you cannot specify the Neumann condition
            on a polygonal domain.


         Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

       Start X


       End X


       Start Y  N/A


       End Y     N/A


      The following block diagram is an example of defining the boundary condition for a
      one-dimensional wave equation. The boundary condition at Start X is

3866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3867 ordinal=3867 -->
## Functions

Functions

Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
which the numeric array defines.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D WaveWave PDEPDE BCBC (Numeric)(Numeric) VIVI

Defines the boundary condition of partial differential equations. You must manually
select the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.


                                                    © National Instruments 3867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3868 ordinal=3868 -->
## Functions

Functions

               •     Boundary Condition —

          Boundary Condition specifies the value of the boundary condition. Its length must be # of t-
            points from the Define PDE Domain VI. It stores the values of the unknown function evaluated at
            position over time. By default, LabVIEW assumes that the boundary condition values are zeros.

               •      type —

           type specifies the type of the boundary condition.

               Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function           0              to specify the boundary condition.
          Neumann—The boundary of the domain evaluates the value of the normal derivative of the           1           unknown function to specify the boundary condition.

               •      position —

            position specifies the position of the boundary condition.

              Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE           0
           Domain VI.
           1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the boundary condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following table gives the definitions of a normal derivative for one-dimensional
       equations and for two-dimensional equations defined on a rectangular domain.

           Note If the boundary type is Neumann, you must specify the value of the


3868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3869 ordinal=3869 -->
## Functions

Functions


       normal derivative of the unknown function and not the value of derivatives
       along the x- or y-axes. Moreover, you cannot specify the Neumann condition
      on a polygonal domain.


 Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

 Start X


 End X


 Start Y  N/A


 End Y     N/A


The following block diagram is an example of defining the boundary condition for a
one-dimensional wave equation. The boundary condition at Start X is
Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
which the numeric array defines.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi

                                                    © National Instruments 3869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3870 ordinal=3870 -->
## Functions

Functions

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 1D1D WaveWave PDEPDE BCBC (VIRef)(VIRef) VIVI

       Defines the boundary condition of partial differential equations. You must manually
        select the polymorphic instance to use.


      Inputs/Outputs

               •      data —

           data is a variant that passes arbitrary values to the VI.

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •     Boundary Condition —

          Boundary Condition is a strictly typed reference to the VI that implements the boundary
             condition.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\1D Evolutionary PDE Func Template.vit.

               •      type —

           type specifies the type of the boundary condition.

               Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function
           0
              to specify the boundary condition.
           1 Neumann—The boundary of the domain evaluates the value of the normal derivative of the


3870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3871 ordinal=3871 -->
## Functions

Functions


    unknown function to specify the boundary condition.

   •      position —

    position specifies the position of the boundary condition.

      Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE    0     Domain VI.
    1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in with the boundary condition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following table gives the definitions of a normal derivative for one-dimensional
equations and for two-dimensional equations defined on a rectangular domain.

      Note If the boundary type is Neumann, you must specify the value of the
       normal derivative of the unknown function and not the value of derivatives
       along the x- or y-axes. Moreover, you cannot specify the Neumann condition
      on a polygonal domain.


 Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

 Start X


 End X


                                                    © National Instruments 3871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3872 ordinal=3872 -->
## Functions

Functions


         Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

       Start Y  N/A


       End Y     N/A


      The following block diagram is an example of defining the boundary condition for a
      one-dimensional wave equation. The boundary condition at Start X is
     Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
      which the numeric array defines.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D WaveWave PDEPDE BCBC (Numeric)(Numeric) VIVI

       Defines the boundary condition of partial differential equations. You must manually
        select the polymorphic instance to use.


3872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3873 ordinal=3873 -->
## Functions

Functions


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •     Boundary Condition —

    Boundary Condition specifies the value of boundary condition.

   When position is Start X or End X, the size of Boundary Condition must be # of t-
    points-by-# of y-points from the Define PDE Domain VI. Each row of Boundary Condition stores
    the values of the unknown function evaluated on points Y from the Define PDE Domain VI at a
     particular time step. Each column of Boundary Condition stores the values of the unknown
    function evaluated at a particular y-point over time. When position is Start Y or End Y, the
     size of Boundary Condition must be # of t-points-by-# of x-points from the Define PDE Domain
      VI. Each row of Boundary Condition stores the values of the unknown function evaluated on
    points X from the Define PDE Domain VI at a particular time step. Each column of Boundary
    Condition stores the values of the unknown function evaluated at particular x-points over time.
    By default, LabVIEW assumes that the boundary condition values are zeros.

   •      type —

    type specifies the type of the boundary condition.

      Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function    0
      to specify the boundary condition.
    Neumann—The boundary of the domain evaluates the value of the normal derivative of the
    1
    unknown function to specify the boundary condition.

   •      position —

    position specifies the position of the boundary condition.

      Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE
    0
     Domain VI.
    1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.


                                                    © National Instruments 3873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3874 ordinal=3874 -->
## Functions

Functions


              Start Y—LabVIEW evaluates the boundary condition with start y from the Define PDE Domain           2
                  VI.
           3 End Y—LabVIEW evaluates the boundary condition with end y from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the boundary condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following table gives the definitions of a normal derivative for one-dimensional
       equations and for two-dimensional equations defined on a rectangular domain.

           Note If the boundary type is Neumann, you must specify the value of the
             normal derivative of the unknown function and not the value of derivatives
              along the x- or y-axes. Moreover, you cannot specify the Neumann condition
            on a polygonal domain.


         Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

       Start X


       End X


       Start Y  N/A


       End Y     N/A


3874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3875 ordinal=3875 -->
## Functions

Functions

The following block diagram is an example of defining the boundary condition for a
one-dimensional wave equation. The boundary condition at Start X is
Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
which the numeric array defines.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D WaveWave PDEPDE BCBC (VIRef)(VIRef) VIVI

Defines the boundary condition of partial differential equations. You must manually
select the polymorphic instance to use.


                                                    © National Instruments 3875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3876 ordinal=3876 -->
## Functions

Functions

      Inputs/Outputs

               •      data —

           data is a variant that passes arbitrary values to the VI.

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •     Boundary Condition —

          Boundary Condition is a strictly typed reference to the VI that implements the boundary
             condition.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\2D Stationary PDE Func Template.vit.

               •      type —

           type specifies the type of the boundary condition.

               Dirichlet (default)—The boundary of the domain evaluates the value of the unknown function           0              to specify the boundary condition.
          Neumann—The boundary of the domain evaluates the value of the normal derivative of the           1           unknown function to specify the boundary condition.

               •      position —

            position specifies the position of the boundary condition.

              Start X (default)—LabVIEW evaluates the boundary condition with start x from the Define PDE
           0
           Domain VI.
           1 End X—LabVIEW evaluates the boundary condition with end x from the Define PDE Domain VI.
              Start Y—LabVIEW evaluates the boundary condition with start y from the Define PDE Domain
           2
                  VI.
           3 End Y—LabVIEW evaluates the boundary condition with end y from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


3876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3877 ordinal=3877 -->
## Functions

Functions

   •     PDE out —

   PDE out returns PDE in with the boundary condition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The following table gives the definitions of a normal derivative for one-dimensional
equations and for two-dimensional equations defined on a rectangular domain.

      Note If the boundary type is Neumann, you must specify the value of the
       normal derivative of the unknown function and not the value of derivatives
       along the x- or y-axes. Moreover, you cannot specify the Neumann condition
      on a polygonal domain.


 Position   Normal Derivative (One-Dimension)    Normal Derivative (Rectangular Domain)

 Start X


 End X


 Start Y  N/A


 End Y     N/A


The following block diagram is an example of defining the boundary condition for a
one-dimensional wave equation. The boundary condition at Start X is
Dirichlet, which the VI defines. The boundary condition at End X is Neumann,
which the numeric array defines.


                                                    © National Instruments 3877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3878 ordinal=3878 -->
## Functions

Functions


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi

      DefineDefine PDEPDE InitialInitial ConditionCondition

       Defines the initial condition of a partial differential equation. You must manually select
       the polymorphic instance to use.


            • Define 1D Heat PDE IC (Numeric) VI
            • Define 1D Heat PDE IC (VIRef) VI
            • Define 2D Heat PDE IC (Numeric) VI
            • Define 2D Heat PDE IC (VIRef) VI
            • Define 1D Wave PDE IC (Numeric) VI
            • Define 1D Wave PDE IC (VIRef) VI
            • Define 2D Wave PDE IC (Numeric) VI
            • Define 2D Wave PDE IC (VIRef) VI

      The heat equation requires only the initial value to solve the equation. However, for
       the wave equation, specify the value and the derivative value with respect to the time

3878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3879 ordinal=3879 -->
## Functions

Functions

variable at initial time. The following block diagram is an example of how to define the
initial condition for a one-dimensional wave equation. The VI defines the initial value,
and the numeric array defines the initial derivative.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D HeatHeat PDEPDE ICIC (Numeric)(Numeric) VIVI

Defines the initial condition of a partial differential equation. You must manually select
the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •        Initial Condition —


                                                    © National Instruments 3879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3880 ordinal=3880 -->
## Functions

Functions


               Initial Condition specifies the value of the initial condition.

          The length of Initial Condition must be # of x-points from the Define PDE Domain VI. Initial
            Condition stores the values of the unknown function evaluated on points X at initial t from the
            Define PDE Domain VI. By default, LabVIEW assumes that its values are zeros.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the initial condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The heat equation requires only the initial value to solve the equation. However, for
       the wave equation, specify the value and the derivative value with respect to the time
       variable at initial time. The following block diagram is an example of how to define the
         initial condition for a one-dimensional wave equation. The VI defines the initial value,
      and the numeric array defines the initial derivative.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -

3880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3881 ordinal=3881 -->
## Functions

Functions

   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D HeatHeat PDEPDE ICIC (VIRef)(VIRef) VIVI

Defines the initial condition of a partial differential equation. You must manually select
the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •        Initial Condition —

     Initial Condition is a strictly typed reference to the VI that implements the initial condition.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   pde.llb\Common\1D Evolutionary PDE Func Template.vit.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in with the initial condition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 3881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3882 ordinal=3882 -->
## Functions

Functions

      The heat equation requires only the initial value to solve the equation. However, for
       the wave equation, specify the value and the derivative value with respect to the time
       variable at initial time. The following block diagram is an example of how to define the
         initial condition for a one-dimensional wave equation. The VI defines the initial value,
      and the numeric array defines the initial derivative.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D HeatHeat PDEPDE ICIC (Numeric)(Numeric) VIVI

       Defines the initial condition of a partial differential equation. You must manually select
       the polymorphic instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •        Initial Condition —

3882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3883 ordinal=3883 -->
## Functions

Functions


     Initial Condition specifies the value of the initial condition. The size of Initial Condition must be
    # of y-points-by-# of x-points from the Define PDE Domain VI. Each row or column of Initial
    Condition stores the values of the unknown function evaluated on a particular y- or x-point,
     respectively, at initial t from the Define PDE Domain VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in with the initial condition.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The heat equation requires only the initial value to solve the equation. However, for
the wave equation, specify the value and the derivative value with respect to the time
variable at initial time. The following block diagram is an example of how to define the
initial condition for a one-dimensional wave equation. The VI defines the initial value,
and the numeric array defines the initial derivative.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -


                                                    © National Instruments 3883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3884 ordinal=3884 -->
## Functions

Functions

        PDE\PDE Thermal Distribution.vi
    DefineDefine 2D2D HeatHeat PDEPDE ICIC (VIRef)(VIRef) VIVI

       Defines the initial condition of a partial differential equation. You must manually select
       the polymorphic instance to use.


      Inputs/Outputs

               •      data —

           data is a variant that passes arbitrary values to the VI.

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •        Initial Condition —

               Initial Condition is a strictly typed reference to the VI that implements the initial condition.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\2D Evolutionary PDE Func Template.vit.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the initial condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


3884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3885 ordinal=3885 -->
## Functions

Functions

The heat equation requires only the initial value to solve the equation. However, for
the wave equation, specify the value and the derivative value with respect to the time
variable at initial time. The following block diagram is an example of how to define the
initial condition for a one-dimensional wave equation. The VI defines the initial value,
and the numeric array defines the initial derivative.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D WaveWave PDEPDE ICIC (Numeric)(Numeric) VIVI

Defines the initial condition of a partial differential equation. You must manually select
the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.


                                                    © National Instruments 3885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3886 ordinal=3886 -->
## Functions

Functions

               •        Initial Condition —

               Initial Condition specifies the value of the initial condition.

          The length of Initial Condition must be # of x-points from the Define PDE Domain VI. Initial
            Condition stores the values of the unknown function evaluated on points X at initial t from the
            >Define PDE Domain VI. By default, LabVIEW assumes that its values are zeros.

               •      type —

           type specifies the type of the initial condition.

             Value (default)—The initial condition evaluates the unknown function at initial t from the           0              Define PDE Domain VI.
             Derivative—The initial condition evaluates the value of the partial derivative for the time
           1              variable at initial t from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the initial condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The heat equation requires only the initial value to solve the equation. However, for
       the wave equation, specify the value and the derivative value with respect to the time
       variable at initial time. The following block diagram is an example of how to define the
         initial condition for a one-dimensional wave equation. The VI defines the initial value,
      and the numeric array defines the initial derivative.


3886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3887 ordinal=3887 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 1D1D WaveWave PDEPDE ICIC (VIRef)(VIRef) VIVI

Defines the initial condition of a partial differential equation. You must manually select
the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •        Initial Condition —


                                                    © National Instruments 3887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3888 ordinal=3888 -->
## Functions

Functions


               Initial Condition is a strictly typed reference to the VI that implements the initial condition.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         pde.llb\Common\1D Evolutionary PDE Func Template.vit.

               •      type —

           type specifies the type of the initial condition.

             Value (default)—The initial condition evaluates the unknown function at initial t from the           0              Define PDE Domain VI.
             Derivative—The initial condition evaluates the value of the partial derivative for the time
           1              variable at initial t from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the initial condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The heat equation requires only the initial value to solve the equation. However, for
       the wave equation, specify the value and the derivative value with respect to the time
       variable at initial time. The following block diagram is an example of how to define the
         initial condition for a one-dimensional wave equation. The VI defines the initial value,
      and the numeric array defines the initial derivative.


3888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3889 ordinal=3889 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
DefineDefine 2D2D WaveWave PDEPDE ICIC (Numeric)(Numeric) VIVI

Defines the initial condition of a partial differential equation. You must manually select
the polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •        Initial Condition —

     Initial Condition specifies the value of the initial condition. The size of Initial Condition must be
    # of y-points-by-# of x-points from the Define PDE Domain VI. Each row or column of Initial
    Condition stores the values of the unknown function evaluated on a particular y- or x-point,
     respectively, at initial t from the Define PDE Domain VI.

   •      type —

    type specifies the type of the initial condition.

     Value (default)—The initial condition evaluates the unknown function at initial t from the
    0
      Define PDE Domain VI.
    1 Derivative—The initial condition evaluates the value of the partial derivative for the time


                                                    © National Instruments 3889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3890 ordinal=3890 -->
## Functions

Functions


              variable at initial t from the Define PDE Domain VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in with the initial condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The heat equation requires only the initial value to solve the equation. However, for
       the wave equation, specify the value and the derivative value with respect to the time
       variable at initial time. The following block diagram is an example of how to define the
         initial condition for a one-dimensional wave equation. The VI defines the initial value,
      and the numeric array defines the initial derivative.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi


3890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3891 ordinal=3891 -->
## Functions

Functions

DefineDefine 2D2D WaveWave PDEPDE ICIC (VIRef)(VIRef) VIVI

Defines the initial condition of a partial differential equation. You must manually select
the polymorphic instance to use.


Inputs/Outputs

   •      data —

    data is a variant that passes arbitrary values to the VI.

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •        Initial Condition —

     Initial Condition is a strictly typed reference to the VI that implements the initial condition.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   pde.llb\Common\2D Evolutionary PDE Func Template.vit.

   •      type —

    type specifies the type of the initial condition.

     Value (default)—The initial condition evaluates the unknown function at initial t from the
    0
      Define PDE Domain VI.
     Derivative—The initial condition evaluates the value of the partial derivative for the time
    1
      variable at initial t from the Define PDE Domain VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 3891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3892 ordinal=3892 -->
## Functions

Functions

               •     PDE out —

         PDE out returns PDE in with the initial condition.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The heat equation requires only the initial value to solve the equation. However, for
       the wave equation, specify the value and the derivative value with respect to the time
       variable at initial time. The following block diagram is an example of how to define the
         initial condition for a one-dimensional wave equation. The VI defines the initial value,
      and the numeric array defines the initial derivative.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi

     PDEPDE SolverSolver

       Solves a partial differential equation. You must manually select the polymorphic
       instance to use.


3892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3893 ordinal=3893 -->
## Functions

Functions

  • 2D Helmholtz PDE Solver (Rect Domain) VI
  • 2D Helmholtz PDE Solver (Polygon Domain) VI
  • 1D Heat PDE Solver VI
  • 2D Heat PDE Solver (Rect Domain) VI
  • 1D Wave PDE Solver VI
  • 2D Wave PDE Solver (Rect Domain) VI

Before you use the PDE Solver VI, use the Define PDE, Define PDE Domain, and Define
PDE Boundary Condition VIs to define the equation, domain, and boundary
conditions. For an evolutionary equation, such as the heat or wave equations, use the
Define PDE Initial Condition VI to define the initial condition. For each VI, select the
appropriate polymorphic instance according to the type of equation you need to solve.
The following block diagram illustrates how to define and solve a one-dimensional
wave equation.


For a one-dimensional problem, LabVIEW solves the equation on evenly spaced points
with the finite difference method. For a two-dimensional problem defined on the
rectangular domain, LabVIEW solves the equation on a uniform mesh grid with the
finite difference method. For a two-dimensional problem defined on the polygonal
domain, LabVIEW solves the equation on specified grid points with the finite element
method. In this case, the grid points are not required to be a uniform mesh.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi


                                                    © National Instruments 3893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3894 ordinal=3894 -->
## Functions

Functions

   2D2D HelmholtzHelmholtz PDEPDE SolverSolver (Rect(Rect Domain)Domain) VIVI

       Solves a partial differential equation. You must manually select the polymorphic
       instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in unchanged.

               •       U(x, y) —

             U(x, y) returns the calculated solution of the equation.

          The size of the right-sided function is # of y-points-by-# of x-points from the Define PDE Domain
                VI. Each column and row of U(x, y) stores the solution on a particular y- or x-point, respectively.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Solver VI, use the Define PDE, Define PDE Domain, and Define
     PDE Boundary Condition VIs to define the equation, domain, and boundary
       conditions. For an evolutionary equation, such as the heat or wave equations, use the
       Define PDE Initial Condition VI to define the initial condition. For each VI, select the
       appropriate polymorphic instance according to the type of equation you need to solve.

3894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3895 ordinal=3895 -->
## Functions

Functions

The following block diagram illustrates how to define and solve a one-dimensional
wave equation.


For a one-dimensional problem, LabVIEW solves the equation on evenly spaced points
with the finite difference method. For a two-dimensional problem defined on the
rectangular domain, LabVIEW solves the equation on a uniform mesh grid with the
finite difference method. For a two-dimensional problem defined on the polygonal
domain, LabVIEW solves the equation on specified grid points with the finite element
method. In this case, the grid points are not required to be a uniform mesh.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
2D2D HelmholtzHelmholtz PDEPDE SolverSolver (Polygon(Polygon Domain)Domain)
VIVI

Solves a partial differential equation. You must manually select the polymorphic
instance to use.


                                                    © National Instruments 3895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3896 ordinal=3896 -->
## Functions

Functions


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in unchanged.

               •       U(x, y) —

             U(x, y) returns the calculated solution of the equation at Grid Points.

               •      Grid Points —

            Grid Points returns the grid points for the equation.

                     •     X —

              X returns the x-coordinate of Grid Points.

                     •      Y —

               Y returns the y-coordinate of Grid Points.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Solver VI, use the Define PDE, Define PDE Domain, and Define
     PDE Boundary Condition VIs to define the equation, domain, and boundary
       conditions. For an evolutionary equation, such as the heat or wave equations, use the

3896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3897 ordinal=3897 -->
## Functions

Functions

Define PDE Initial Condition VI to define the initial condition. For each VI, select the
appropriate polymorphic instance according to the type of equation you need to solve.
The following block diagram illustrates how to define and solve a one-dimensional
wave equation.


For a one-dimensional problem, LabVIEW solves the equation on evenly spaced points
with the finite difference method. For a two-dimensional problem defined on the
rectangular domain, LabVIEW solves the equation on a uniform mesh grid with the
finite difference method. For a two-dimensional problem defined on the polygonal
domain, LabVIEW solves the equation on specified grid points with the finite element
method. In this case, the grid points are not required to be a uniform mesh.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
1D1D HeatHeat PDEPDE SolverSolver VIVI

Solves a partial differential equation. You must manually select the polymorphic
instance to use.


                                                    © National Instruments 3897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3898 ordinal=3898 -->
## Functions

Functions

      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in unchanged.

               •       U(t, x) —

              U(t, x) returns the calculated solution of the equation.

          The size of the right-sided function is # of t-points-by-# of x-points from the Define PDE Domain
                VI. Each row of U(t, x) stores the solution at points X from the Define PDE Domain VI at a
             particular time step. Each column of U(t, x) stores the solution on a particular x-point over time.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Solver VI, use the Define PDE, Define PDE Domain, and Define
     PDE Boundary Condition VIs to define the equation, domain, and boundary
       conditions. For an evolutionary equation, such as the heat or wave equations, use the
       Define PDE Initial Condition VI to define the initial condition. For each VI, select the
       appropriate polymorphic instance according to the type of equation you need to solve.
      The following block diagram illustrates how to define and solve a one-dimensional
      wave equation.


       For a one-dimensional problem, LabVIEW solves the equation on evenly spaced points

3898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3899 ordinal=3899 -->
## Functions

Functions

with the finite difference method. For a two-dimensional problem defined on the
rectangular domain, LabVIEW solves the equation on a uniform mesh grid with the
finite difference method. For a two-dimensional problem defined on the polygonal
domain, LabVIEW solves the equation on specified grid points with the finite element
method. In this case, the grid points are not required to be a uniform mesh.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
2D2D HeatHeat PDEPDE SolverSolver (Rect(Rect Domain)Domain) VIVI

Solves a partial differential equation. You must manually select the polymorphic
instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —


                                                    © National Instruments 3899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3900 ordinal=3900 -->
## Functions

Functions


         PDE out returns PDE in unchanged.

               •       U(t, x, y) —

              U(t, x, y) returns the calculated solution of the equation.

          The size of the right-sided function is # of t-points-by-# of y-points-by-# of x-points from the
            Define PDE Domain VI. Each page of U(t, x, y) stores the solution at mesh grid points (X, Y) from
            the Define PDE Domain VI at a particular time step. On one page of U(t, x, y), each row or column
             stores the solution on a particular y- or x-point, respectively.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Solver VI, use the Define PDE, Define PDE Domain, and Define
     PDE Boundary Condition VIs to define the equation, domain, and boundary
       conditions. For an evolutionary equation, such as the heat or wave equations, use the
       Define PDE Initial Condition VI to define the initial condition. For each VI, select the
       appropriate polymorphic instance according to the type of equation you need to solve.
      The following block diagram illustrates how to define and solve a one-dimensional
      wave equation.


       For a one-dimensional problem, LabVIEW solves the equation on evenly spaced points
       with the finite difference method. For a two-dimensional problem defined on the
       rectangular domain, LabVIEW solves the equation on a uniform mesh grid with the
         finite difference method. For a two-dimensional problem defined on the polygonal
      domain, LabVIEW solves the equation on specified grid points with the finite element
      method. In this case, the grid points are not required to be a uniform mesh.

     Examples

       Refer to the following example files included with LabVIEW.

3900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3901 ordinal=3901 -->
## Functions

Functions

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
1D1D WaveWave PDEPDE SolverSolver VIVI

Solves a partial differential equation. You must manually select the polymorphic
instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in unchanged.

   •       U(t, x) —

     U(t, x) returns the calculated solution of the equation.

    The size of the right-sided function is # of t-points-by-# of x-points from the Define PDE Domain
      VI. Each row of U(t, x) stores the solution at points X from the Define PDE Domain VI at a
     particular time step. Each column of U(t, x) stores the solution on a particular x-point over time.

   •       error out —


                                                    © National Instruments 3901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3902 ordinal=3902 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Solver VI, use the Define PDE, Define PDE Domain, and Define
     PDE Boundary Condition VIs to define the equation, domain, and boundary
       conditions. For an evolutionary equation, such as the heat or wave equations, use the
       Define PDE Initial Condition VI to define the initial condition. For each VI, select the
       appropriate polymorphic instance according to the type of equation you need to solve.
      The following block diagram illustrates how to define and solve a one-dimensional
      wave equation.


       For a one-dimensional problem, LabVIEW solves the equation on evenly spaced points
       with the finite difference method. For a two-dimensional problem defined on the
       rectangular domain, LabVIEW solves the equation on a uniform mesh grid with the
         finite difference method. For a two-dimensional problem defined on the polygonal
      domain, LabVIEW solves the equation on specified grid points with the finite element
      method. In this case, the grid points are not required to be a uniform mesh.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi


3902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3903 ordinal=3903 -->
## Functions

Functions

2D2D WaveWave PDEPDE SolverSolver (Rect(Rect Domain)Domain) VIVI

Solves a partial differential equation. You must manually select the polymorphic
instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in unchanged.

   •       U(t, x, y) —

     U(t, x, y) returns the calculated solution of the equation.

    The size of the right-sided function is # of t-points-by-# of y-points-by-# of x-points from the
    Define PDE Domain VI. Each page of U(t, x, y) stores the solution at mesh grid points (X, Y) from
    the Define PDE Domain VI at a particular time step. On one page of U(t, x, y), each row or column
     stores the solution on a particular y- or x-point, respectively.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Before you use the PDE Solver VI, use the Define PDE, Define PDE Domain, and Define
PDE Boundary Condition VIs to define the equation, domain, and boundary
conditions. For an evolutionary equation, such as the heat or wave equations, use the


                                                    © National Instruments 3903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3904 ordinal=3904 -->
## Functions

Functions

       Define PDE Initial Condition VI to define the initial condition. For each VI, select the
       appropriate polymorphic instance according to the type of equation you need to solve.
      The following block diagram illustrates how to define and solve a one-dimensional
      wave equation.


       For a one-dimensional problem, LabVIEW solves the equation on evenly spaced points
       with the finite difference method. For a two-dimensional problem defined on the
       rectangular domain, LabVIEW solves the equation on a uniform mesh grid with the
         finite difference method. For a two-dimensional problem defined on the polygonal
      domain, LabVIEW solves the equation on specified grid points with the finite element
      method. In this case, the grid points are not required to be a uniform mesh.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi

     PDEPDE RenderingRendering

      Renders the solution of the partial differential equation. You must manually select the
      polymorphic instance to use.


            • 2D Helmholtz PDE Rendering (Rect Domain) VI

3904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3905 ordinal=3905 -->
## Functions

Functions

  • 2D Helmholtz PDE Rendering (Polygon Domain) VI
  • 1D Heat PDE Rendering VI
  • 2D Heat PDE Rendering (Rect Domain) VI
  • 1D Wave PDE Rendering VI
  • 2D Wave PDE Rendering (Rect Domain) VI

Before you use the PDE Rendering VI, use the PDE Solver VI to solve the equation.

The following block diagram illustrates how to set the scale offset and multiplier of
PDE Plot by X Scale and Y Scale.


If you do not set the scale offset and multiplier, LabVIEW uses the default settings of
the intensity graph.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
2D2D HelmholtzHelmholtz PDEPDE RenderingRendering (Rect(Rect Domain)Domain)
VIVI

Renders the solution of the partial differential equation. You must manually select the


                                                    © National Instruments 3905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3906 ordinal=3906 -->
## Functions

Functions

      polymorphic instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •       U(x, y) —

             U(x, y) specifies the solution of the equation.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in unchanged.

               •     PDE Plot —

         PDE Plot returns an intensity graph that renders U(x, y).

               •     X Scale —

          X Scale returns the offset and multiplier of the x-scale. X Scale returns the offset and multiplier
             of the PDE Plot x-scale.

                     •       Offset —

                 Offset returns the offset of the x-scale.

                     •       Multiplier —


3906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3907 ordinal=3907 -->
## Functions

Functions


         Multiplier returns the multiplier of the x-scale.


   •      Y Scale —

    Y Scale returns the offset and multiplier of y-scale. Y Scalereturns the offset and multiplier of the
   PDE Plot y-scale.

         •       Offset —

         Offset returns the offset of the y-scale.

         •       Multiplier —

         Multiplier returns the multiplier of the y-scale.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Before you use the PDE Rendering VI, use the PDE Solver VI to solve the equation.

The following block diagram illustrates how to set the scale offset and multiplier of
PDE Plot by X Scale and Y Scale.


If you do not set the scale offset and multiplier, LabVIEW uses the default settings of
the intensity graph.

Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 3907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3908 ordinal=3908 -->
## Functions

Functions

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
   2D2D HelmholtzHelmholtz PDEPDE RenderingRendering (Polygon(Polygon
   Domain)Domain) VIVI

      Renders the solution of the partial differential equation. You must manually select the
      polymorphic instance to use.


      Inputs/Outputs

               •       plot style —

             plot style specifies how LabVIEW draws the solution for PDE Plot.

           0 Wireframe—Draws the solution with line segments that connect at Grid Points.
           1 Polygons (default)—Draws the solution with filled geometry.

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •       U(x, y) —

             U(x, y) specifies the solution of the equation in Grid Points from the PDE Solver VI.

               •      Grid Points —


3908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3909 ordinal=3909 -->
## Functions

Functions


    Grid Points specifies the grid points for the equation.

         •     X —

       X specifies the x-coordinate of Grid Points.

         •      Y —

        Y specifies the y-coordinate of Grid Points.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in unchanged.

   •     PDE Plot —

   PDE Plot returns a reference to a 3D scene object. Wire this output to the 3D picture control to
    view the solution.

   •      Triangulation Plot —

    Triangulation Plot returns an XY graph that illustrates triangulation.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Before you use the PDE Rendering VI, use the PDE Solver VI to solve the equation.

The following block diagram illustrates how to set the scale offset and multiplier of
PDE Plot by X Scale and Y Scale.


                                                    © National Instruments 3909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3910 ordinal=3910 -->
## Functions

Functions


           If you do not set the scale offset and multiplier, LabVIEW uses the default settings of
       the intensity graph.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
   1D1D HeatHeat PDEPDE RenderingRendering VIVI

      Renders the solution of the partial differential equation. You must manually select the
      polymorphic instance to use.


      Inputs/Outputs

               •     PDE in —

         PDE in is the class that stores the data of the equation.

               •       U(t, x) —

3910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3911 ordinal=3911 -->
## Functions

Functions


  U(t, x) specifies the solution of the equation.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     PDE out —

  PDE out returns PDE in unchanged.

•     PDE Plot —

  PDE Plot returns an intensity graph that renders U(t, x).

•     X Scale —

  X Scale returns the offset and multiplier of the x-scale. X Scale returns the offset and multiplier
  of the PDE Plot x-scale.

      •       Offset —

       Offset returns the offset of the x-scale.

      •       Multiplier —

       Multiplier returns the multiplier of the x-scale.


•      Y Scale —

  Y Scale returns the offset and multiplier of y-scale. Y Scalereturns the offset and multiplier of the
  PDE Plot y-scale.

      •       Offset —

       Offset returns the offset of the y-scale.

      •       Multiplier —

       Multiplier returns the multiplier of the y-scale.


•       error out —

                                                   © National Instruments 3911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3912 ordinal=3912 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Rendering VI, use the PDE Solver VI to solve the equation.

      The following block diagram illustrates how to set the scale offset and multiplier of
     PDE Plot by X Scale and Y Scale.


           If you do not set the scale offset and multiplier, LabVIEW uses the default settings of
       the intensity graph.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Flexible Element.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE String Vibration.vi
            • labview\examples\Mathematics\Differential Equations -
        PDE\PDE Thermal Distribution.vi
   2D2D HeatHeat PDEPDE RenderingRendering (Rect(Rect Domain)Domain) VIVI

      Renders the solution of the partial differential equation. You must manually select the
      polymorphic instance to use.


3912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3913 ordinal=3913 -->
## Functions

Functions


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       U(t, x, y) —

     U(t, x, y) specifies the solution of the equation.

   •      index (time step) —

    index (time step) specifies the index of the time step.

       If index (time step) is negative or greater than # of t-points from the Define PDE Domain VI,
    LabVIEW renders the solution at final t. Otherwise, LabVIEW renders the solution at index (time
     step). The default is –1.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in unchanged.

   •     PDE Plot —

   PDE Plot returns an intensity graph that renders U(t, x, y) at index (time step).

   •     X Scale —

    X Scale returns the offset and multiplier of the x-scale. X Scale returns the offset and multiplier
     of the PDE Plot x-scale.

         •       Offset —


                                                    © National Instruments 3913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3914 ordinal=3914 -->
## Functions

Functions


                 Offset returns the offset of the x-scale.

                     •       Multiplier —

                  Multiplier returns the multiplier of the x-scale.


               •      Y Scale —

           Y Scale returns the offset and multiplier of y-scale. Y Scalereturns the offset and multiplier of the
         PDE Plot y-scale.

                     •       Offset —

                 Offset returns the offset of the y-scale.

                     •       Multiplier —

                  Multiplier returns the multiplier of the y-scale.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Rendering VI, use the PDE Solver VI to solve the equation.

      The following block diagram illustrates how to set the scale offset and multiplier of
     PDE Plot by X Scale and Y Scale.


           If you do not set the scale offset and multiplier, LabVIEW uses the default settings of
       the intensity graph.


3914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3915 ordinal=3915 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
1D1D WaveWave PDEPDE RenderingRendering VIVI

Renders the solution of the partial differential equation. You must manually select the
polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       U(t, x) —

     U(t, x) specifies the solution of the equation.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     PDE out —

   PDE out returns PDE in unchanged.


                                                    © National Instruments 3915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3916 ordinal=3916 -->
## Functions

Functions

               •     PDE Plot —

         PDE Plot returns an intensity graph that renders U(t, x).

               •     X Scale —

          X Scale returns the offset and multiplier of the x-scale. X Scale returns the offset and multiplier
             of the PDE Plot x-scale.

                     •       Offset —

                 Offset returns the offset of the x-scale.

                     •       Multiplier —

                  Multiplier returns the multiplier of the x-scale.


               •      Y Scale —

           Y Scale returns the offset and multiplier of y-scale. Y Scalereturns the offset and multiplier of the
         PDE Plot y-scale.

                     •       Offset —

                 Offset returns the offset of the y-scale.

                     •       Multiplier —

                  Multiplier returns the multiplier of the y-scale.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       Before you use the PDE Rendering VI, use the PDE Solver VI to solve the equation.

      The following block diagram illustrates how to set the scale offset and multiplier of
     PDE Plot by X Scale and Y Scale.


3916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3917 ordinal=3917 -->
## Functions

Functions


If you do not set the scale offset and multiplier, LabVIEW uses the default settings of
the intensity graph.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi
2D2D WaveWave PDEPDE RenderingRendering (Rect(Rect Domain)Domain) VIVI

Renders the solution of the partial differential equation. You must manually select the
polymorphic instance to use.


Inputs/Outputs

   •     PDE in —

   PDE in is the class that stores the data of the equation.

   •       U(t, x, y) —

                                                    © National Instruments 3917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3918 ordinal=3918 -->
## Functions

Functions


              U(t, x, y) specifies the solution of the equation.

               •      index (time step) —

            index (time step) specifies the index of the time step.

                    If index (time step) is negative or greater than # of t-points from the Define PDE Domain VI,
           LabVIEW renders the solution at final t. Otherwise, LabVIEW renders the solution at index (time
              step). The default is –1.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     PDE out —

         PDE out returns PDE in unchanged.

               •     PDE Plot —

         PDE Plot returns an intensity graph that renders U(t, x, y) at index (time step).

               •     X Scale —

          X Scale returns the offset and multiplier of the x-scale. X Scale returns the offset and multiplier
             of the PDE Plot x-scale.

                     •       Offset —

                 Offset returns the offset of the x-scale.

                     •       Multiplier —

                  Multiplier returns the multiplier of the x-scale.


               •      Y Scale —

           Y Scale returns the offset and multiplier of y-scale. Y Scalereturns the offset and multiplier of the
         PDE Plot y-scale.

                     •       Offset —


3918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3919 ordinal=3919 -->
## Functions

Functions


         Offset returns the offset of the y-scale.

         •       Multiplier —

         Multiplier returns the multiplier of the y-scale.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Before you use the PDE Rendering VI, use the PDE Solver VI to solve the equation.

The following block diagram illustrates how to set the scale offset and multiplier of
PDE Plot by X Scale and Y Scale.


If you do not set the scale offset and multiplier, LabVIEW uses the default settings of
the intensity graph.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Flexible Element.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE String Vibration.vi
  • labview\examples\Mathematics\Differential Equations -
   PDE\PDE Thermal Distribution.vi


                                                    © National Instruments 3919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3920 ordinal=3920 -->
## Functions

Functions

    GeometryGeometry

      Use the Geometry VIs to manipulate coordinates and angles.

      The VIs on this palette can return mathematics error codes.


         Palette Object  Description

       2D Cartesian    Shifts two-dimensional Cartesian coordinates along the x- and y-axes. Wire data to
        Coordinate     the X input to determine the polymorphic instance to use or manually select the
          Shift            instance.


       2D Cartesian    Rotates a two-dimensional Cartesian coordinate system in the counterclockwise
        Coordinate      direction. Wire data to the X input to determine the polymorphic instance to use or
         Rotation       manually select the instance.


       3D Cartesian    Shifts three-dimensional Cartesian coordinates along the x-, y-, and z-axes. Wire
        Coordinate     data to the X input to determine the polymorphic instance to use or manually
          Shift            select the instance.


       3D Cartesian    Rotates a three-dimensional Cartesian coordinate system in the counterclockwise
        Coordinate      direction using the Euler angles method and returns the new coordinate of the
         Rotation        given point. Wire data to the X input to determine the polymorphic instance to use
          (Euler)         or manually select the instance.


       3D Cartesian
                        Rotates a three-dimensional Cartesian coordinate in the counterclockwise
        Coordinate
                          direction using the direction method. Wire data to the X input to determine the
         Rotation
                      polymorphic instance to use or manually select the instance.
          (Direction)

         Cross Product   Calculates the cross product of A Vector and B Vector.


3920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3921 ordinal=3921 -->
## Functions

Functions


 Palette Object  Description

 Euler Angles                Converts Euler angles into a 3-by-3 matrix of direction cosines. The VI accepts both
 To Direction                proper and Tait-Bryan angle types. Cosines

 Direction
 Cosines To     Converts a 3-by-3 matrix of direction cosines into Euler angles.
 Euler Angles

                Converts coordinates between the Cartesian, spherical, and cylindrical coordinate 3D Coordinate                systems. Wire data to the Axis 1 input to determine the polymorphic instance to Conversion               use or manually select the instance.


 Angle         Use the Angle VIs to manipulate angles.


 Computational              Use the Computational Geometry VIs to compute a geometrical problem. Geometry

2D2D CartesianCartesian CoordinateCoordinate ShiftShift

Shifts two-dimensional Cartesian coordinates along the x- and y-axes. Wire data to the
X input to determine the polymorphic instance to use or manually select the instance.


   • 2D Cartesian Coordinate Shift (Array) VI
   • 2D Cartesian Coordinate Shift (Scalar) VI

The following illustration shows the shift of a two-dimensional Cartesian coordinate by
dxand dy:


                                                    © National Instruments 3921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3922 ordinal=3922 -->
## Functions

Functions


       Before the shift, the coordinate of point Pis (x, y). After the shift operation, the
       coordinate of point Pis (x', y'), where

       x' = x+ dxy' = y+ dy
     2D2D CartesianCartesian CoordinateCoordinate ShiftShift (Array)(Array) VIVI

        Shifts two-dimensional Cartesian coordinates along the x- and y-axes. Wire data to the
      X input to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X specifies the input x-coordinates.

               •      Y —

           Y specifies the input y-coordinates.

               •        shift —

              shift specifies the shift amount along each of the axes.

                     •     dx —

              dx specifies the shift amount along the x-axis.


3922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3923 ordinal=3923 -->
## Functions

Functions


          •     dy —

       dy specifies the shift amount along the y-axis.


   •     X Out —

    X Out returns the shifted x-coordinates.

   •      Y Out —

    Y Out returns the shifted y-coordinates.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following illustration shows the shift of a two-dimensional Cartesian coordinate by
dxand dy:


Before the shift, the coordinate of point Pis (x, y). After the shift operation, the
coordinate of point Pis (x', y'), where

x' = x+ dxy' = y+ dy
2D2D CartesianCartesian CoordinateCoordinate ShiftShift (Scalar)(Scalar) VIVI

Shifts two-dimensional Cartesian coordinates along the x- and y-axes. Wire data to the
X input to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 3923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3924 ordinal=3924 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x is the real input x-component for the two-element vector.

               •      y —

           y is the real input y-component for the two-element vector.

               •        shift —

              shift specifies the shift amount along each of the axes.

                     •     dx —

              dx specifies the shift amount along the x-axis.

                     •     dy —

              dy specifies the shift amount along the y-axis.


               •      x out —

           x out returns the shifted x-coordinate.

               •      y out —

           y out returns the shifted y-coordinate.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following illustration shows the shift of a two-dimensional Cartesian coordinate by
    dxand dy:


3924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3925 ordinal=3925 -->
## Functions

Functions


Before the shift, the coordinate of point Pis (x, y). After the shift operation, the
coordinate of point Pis (x', y'), where

x' = x+ dxy' = y+ dy
2D2D CartesianCartesian CoordinateCoordinate RotationRotation

Rotates a two-dimensional Cartesian coordinate system in the counterclockwise
direction. Wire data to the X input to determine the polymorphic instance to use or
manually select the instance.

      Note This VI does notrotate points within a fixed coordinate system. This VI
        rotates the coordinate system about the origin.


   • 2D Cartesian Coordinate Rotation (Array) VI
   • 2D Cartesian Coordinate Rotation (Scalar) VI

The following illustration shows the rotation of a two-dimensional Cartesian
coordinate in the counterclockwise direction by θ (–π < θ ≤ π):


                                                    © National Instruments 3925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3926 ordinal=3926 -->
## Functions

Functions


       Before the rotation, the coordinate of point Pis (x, y). After the rotation, the
       coordinate of point Pis (x', y'), where


        for the rotation matrix

                                          .

     2D2D CartesianCartesian CoordinateCoordinate RotationRotation (Array)(Array) VIVI

       Rotates a two-dimensional Cartesian coordinate system in the counterclockwise
        direction. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.

           Note This VI does notrotate points within a fixed coordinate system. This VI
                rotates the coordinate system about the origin.


      Inputs/Outputs

               •     X —

          X specifies the input x-coordinates.


3926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3927 ordinal=3927 -->
## Functions

Functions

   •      Y —

    Y specifies the input y-coordinates.

   •      theta —

    theta specifies the rotation angle in radians.

   •     X Out —

    X Out returns the rotated x-coordinates.

   •      Y Out —

    Y Out returns the rotated y-coordinates.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following illustration shows the rotation of a two-dimensional Cartesian
coordinate in the counterclockwise direction by θ (–π < θ ≤ π):


Before the rotation, the coordinate of point Pis (x, y). After the rotation, the
coordinate of point Pis (x', y'), where


for the rotation matrix


                                                    © National Instruments 3927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3928 ordinal=3928 -->
## Functions

Functions


                                          .

     2D2D CartesianCartesian CoordinateCoordinate RotationRotation (Scalar)(Scalar) VIVI

       Rotates a two-dimensional Cartesian coordinate system in the counterclockwise
        direction. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.

           Note This VI does notrotate points within a fixed coordinate system. This VI
                rotates the coordinate system about the origin.


      Inputs/Outputs

               •      x —

           x is the real input x-component for the two-element vector.

               •      y —

           y is the real input y-component for the two-element vector.

               •      theta —

            theta specifies the rotation angle in radians.

               •      x out —

           x out returns the rotated x-coordinate.

               •      y out —

           y out returns the rotated y-coordinate.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3929 ordinal=3929 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.


The following illustration shows the rotation of a two-dimensional Cartesian
coordinate in the counterclockwise direction by θ (–π < θ ≤ π):


Before the rotation, the coordinate of point Pis (x, y). After the rotation, the
coordinate of point Pis (x', y'), where


for the rotation matrix

                              .

3D3D CartesianCartesian CoordinateCoordinate ShiftShift

Shifts three-dimensional Cartesian coordinates along the x-, y-, and z-axes. Wire data
to the X input to determine the polymorphic instance to use or manually select the
instance.


  • 3D Cartesian Coordinate Shift (Array) VI
  • 3D Cartesian Coordinate Shift (Scalar) VI


                                                    © National Instruments 3929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3930 ordinal=3930 -->
## Functions

Functions

      The following illustration shows the shift of a three-dimensional Cartesian coordinate
      by dx, dy, and dz:


       Before the shift, the coordinate of point Pis (x, y, z). After the shift operation, the
       coordinate of point Pis (x', y', z'), where

       x' = x+ dxy' = y+ dyz' = z+ dz
     3D3D CartesianCartesian CoordinateCoordinate ShiftShift (Array)(Array) VIVI

        Shifts three-dimensional Cartesian coordinates along the x-, y-, and z-axes. Wire data
       to the X input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •     X —

          X specifies the input x-coordinates.

               •      Y —

3930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3931 ordinal=3931 -->
## Functions

Functions


    Y specifies the input y-coordinates.

   •     Z —

    Z specifies the input z-coordinates.

   •        shift —

     shift specifies the shift amount along each of the axes.

         •     dx —

       dx specifies the shift amount along the x-axis.

         •     dy —

       dy specifies the shift amount along the y-axis.

         •      dz —

        dz specifies the shift amount along the z-axis.


   •     X Out —

    X Out returns the shifted x-coordinates.

   •      Y Out —

    Y Out returns the shifted y-coordinates.

   •     Z Out —

    Z Out returns the shifted z-coordinates.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following illustration shows the shift of a three-dimensional Cartesian coordinate
by dx, dy, and dz:


                                                    © National Instruments 3931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3932 ordinal=3932 -->
## Functions

Functions


       Before the shift, the coordinate of point Pis (x, y, z). After the shift operation, the
       coordinate of point Pis (x', y', z'), where

       x' = x+ dxy' = y+ dyz' = z+ dz
     3D3D CartesianCartesian CoordinateCoordinate ShiftShift (Scalar)(Scalar) VIVI

        Shifts three-dimensional Cartesian coordinates along the x-, y-, and z-axes. Wire data
       to the X input to determine the polymorphic instance to use or manually select the
       instance.


      Inputs/Outputs

               •      x —

           x is the real input x-component for the two-element vector.

               •      y —

           y is the real input y-component for the two-element vector.

               •      z —

3932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3933 ordinal=3933 -->
## Functions

Functions


    z specifies the input z-coordinate.

   •        shift —

     shift specifies the shift amount along each of the axes.

         •     dx —

       dx specifies the shift amount along the x-axis.

         •     dy —

       dy specifies the shift amount along the y-axis.

         •      dz —

        dz specifies the shift amount along the z-axis.


   •      x out —

    x out returns the shifted x-coordinate.

   •      y out —

    y out returns the shifted y-coordinate.

   •      z out —

    z out returns the shifted z-coordinate.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following illustration shows the shift of a three-dimensional Cartesian coordinate
by dx, dy, and dz:


                                                    © National Instruments 3933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3934 ordinal=3934 -->
## Functions

Functions


       Before the shift, the coordinate of point Pis (x, y, z). After the shift operation, the
       coordinate of point Pis (x', y', z'), where

       x' = x+ dxy' = y+ dyz' = z+ dz
    3D3D CartesianCartesian CoordinateCoordinate RotationRotation (Euler)(Euler)

       Rotates a three-dimensional Cartesian coordinate system in the counterclockwise
       direction using the Euler angles method and returns the new coordinate of the given
       point. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


            • 3D Cartesian Coordinate Rotation (Euler) (Array) VI
            • 3D Cartesian Coordinate Rotation (Euler) (Scalar) VI

       According to Euler's rotation theory, you can describe a coordinate rotation with the
       Euler angles ϕ, θ, and ψ as shown below (use the default rotation order Z-X-Z as an
       example):


3934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3935 ordinal=3935 -->
## Functions

Functions


The following three steps describe the rotation:

 1. Rotate the X-, Y-, and Z-axes about the Z-axis by ϕ (–π < ϕ ≤ π), resulting in the X'-,
     Y'-, and Z-axes.
 2. Rotate the X'-, Y'-, and Z-axes about the X'-axis by θ (0 ≤ θ ≤ π), resulting in the X'-,
     Y''-, and Z'-axes.
 3. Rotate the X'-, Y''-, and Z'-axes about the Z'-axis by ψ (–π < ψ ≤ π), resulting in the
     X''-, Y'''-, and Z'-axes.

If you express the rotation of point (x, y, z) in terms of the following three matrices B,
C, and D:


                                     ;                                   ;                                       ,


the coordinates, (x', y', z'), of the point in the new coordinate frame are


where A= BCD.

3D3D CartesianCartesian CoordinateCoordinate RotationRotation (Euler)(Euler) (Array)(Array) VIVI

Rotates a three-dimensional Cartesian coordinate system in the counterclockwise
direction using the Euler angles method and returns the new coordinate of the given


                                                    © National Instruments 3935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3936 ordinal=3936 -->
## Functions

Functions

       point. Wire data to the X input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •     X —

          X specifies the input x-coordinates.

               •      Y —

           Y specifies the input y-coordinates.

               •     Z —

          Z specifies the input z-coordinates.

               •      Euler Angles —

            Euler Angles specifies the Euler angles in radians.

                     •      phi —

                phi specifies the rotation angle about the first axis in radians.

                     •      theta —

                theta specifies the rotation angle about the second axis in radians.

                     •       psi —

                  psi specifies the rotation angle about the third axis in radians.


               •       rotation order —

             rotation order specifies the order of the axes to rotate the coordinates around.


3936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3937 ordinal=3937 -->
## Functions

Functions


    For example, X-Y-Z specifies the first, second, and third rotations are about the x-, y-, and z-axes
     respectively. Z-X-Z is the default order.

    0                              X-Y-Z
    1                              X-Z-Y
    2                              Y-X-Z
    3                              Y-Z-X
    4                              Z-X-Y
    5                              Z-Y-X
    6                              X-Y-X
    7                             X-Z-X
    8                               Y-X-Y
    9                               Y-Z-Y
    10                            Z-X-Z
    11                             Z-Y-Z

   •     X Out —

    X Out returns the rotated x-coordinates.

   •      Y Out —

    Y Out returns the rotated y-coordinates.

   •     Z Out —

    Z Out returns the rotated z-coordinates.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


According to Euler's rotation theory, you can describe a coordinate rotation with the
Euler angles ϕ, θ, and ψ as shown below (use the default rotation order Z-X-Z as an
example):


                                                    © National Instruments 3937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3938 ordinal=3938 -->
## Functions

Functions


      The following three steps describe the rotation:

         1. Rotate the X-, Y-, and Z-axes about the Z-axis by ϕ (–π < ϕ ≤ π), resulting in the X'-,
               Y'-, and Z-axes.
         2. Rotate the X'-, Y'-, and Z-axes about the X'-axis by θ (0 ≤ θ ≤ π), resulting in the X'-,
               Y''-, and Z'-axes.
         3. Rotate the X'-, Y''-, and Z'-axes about the Z'-axis by ψ (–π < ψ ≤ π), resulting in the
               X''-, Y'''-, and Z'-axes.

           If you express the rotation of point (x, y, z) in terms of the following three matrices B,
      C, and D:


                                                 ;                                   ;                                       ,


       the coordinates, (x', y', z'), of the point in the new coordinate frame are


      where A= BCD.

     3D3D CartesianCartesian CoordinateCoordinate RotationRotation (Euler)(Euler) (Scalar)(Scalar) VIVI

       Rotates a three-dimensional Cartesian coordinate system in the counterclockwise
       direction using the Euler angles method and returns the new coordinate of the given


3938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3939 ordinal=3939 -->
## Functions

Functions

point. Wire data to the X input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      x —

    x is the real input x-component for the two-element vector.

   •      y —

    y is the real input y-component for the two-element vector.

   •      z —

    z specifies the input z-coordinate.

   •      Euler Angles —

    Euler Angles specifies the Euler angles in radians.

         •      phi —

        phi specifies the rotation angle about the first axis in radians.

         •      theta —

        theta specifies the rotation angle about the second axis in radians.

         •       psi —

         psi specifies the rotation angle about the third axis in radians.


   •       rotation order —

    rotation order specifies the order of the axes to rotate the coordinates around.


                                                    © National Instruments 3939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3940 ordinal=3940 -->
## Functions

Functions


            For example, X-Y-Z specifies the first, second, and third rotations are about the x-, y-, and z-axes
              respectively. Z-X-Z is the default order.

           0                              X-Y-Z
           1                              X-Z-Y
           2                              Y-X-Z
           3                              Y-Z-X
           4                              Z-X-Y
           5                              Z-Y-X
           6                              X-Y-X
           7                             X-Z-X
           8                               Y-X-Y
           9                               Y-Z-Y
           10                            Z-X-Z
           11                             Z-Y-Z

               •      x out —

           x out returns the rotated x-coordinate.

               •      y out —

           y out returns the rotated y-coordinate.

               •      z out —

            z out returns the rotated z-coordinate.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       According to Euler's rotation theory, you can describe a coordinate rotation with the
       Euler angles ϕ, θ, and ψ as shown below (use the default rotation order Z-X-Z as an
       example):


3940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3941 ordinal=3941 -->
## Functions

Functions


The following three steps describe the rotation:

 1. Rotate the X-, Y-, and Z-axes about the Z-axis by ϕ (–π < ϕ ≤ π), resulting in the X'-,
     Y'-, and Z-axes.
 2. Rotate the X'-, Y'-, and Z-axes about the X'-axis by θ (0 ≤ θ ≤ π), resulting in the X'-,
     Y''-, and Z'-axes.
 3. Rotate the X'-, Y''-, and Z'-axes about the Z'-axis by ψ (–π < ψ ≤ π), resulting in the
     X''-, Y'''-, and Z'-axes.

If you express the rotation of point (x, y, z) in terms of the following three matrices B,
C, and D:


                                     ;                                   ;                                       ,


the coordinates, (x', y', z'), of the point in the new coordinate frame are


where A= BCD.

3D3D CartesianCartesian CoordinateCoordinate RotationRotation (Direction)(Direction)

Rotates a three-dimensional Cartesian coordinate in the counterclockwise direction
using the direction method. Wire data to the X input to determine the polymorphic

                                                    © National Instruments 3941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3942 ordinal=3942 -->
## Functions

Functions

       instance to use or manually select the instance.


            • 3D Cartesian Coordinate Rotation (Direction) (Array) VI
            • 3D Cartesian Coordinate Rotation (Direction) (Scalar) VI

       For a point P, α, β, and γ are the direction angles of vector OP, as shown in the
       following illustration:


      The cosines of the direction angles are direction cosines.

       Before the rotation, the coordinate of point Pis (x, y, z). After the rotation, the
       coordinate of point Pis (x', y', z'), where


    A is the Rotation Matrix defined by:


        α1, β1, and γ1 are the direction angles of the X'-axis to the X-, Y-, and Z-axes. α2, β2, and
       γ2 are the direction angles of the Y'-axis to the X-, Y-, and Z-axes. α3, β3, and γ3 are the


3942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3943 ordinal=3943 -->
## Functions

Functions

direction angles of the Z'-axis to the X-, Y-, and Z-axes.

3D3D CartesianCartesian CoordinateCoordinate RotationRotation (Direction)(Direction) (Array)(Array) VIVI

Rotates a three-dimensional Cartesian coordinate in the counterclockwise direction
using the direction method. Wire data to the X input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X specifies the input x-coordinates.

   •      Y —

    Y specifies the input y-coordinates.

   •     Z —

    Z specifies the input z-coordinates.

   •      Rotation Matrix —

    Rotation Matrix specifies the 3-by-3 direction cosine matrix. If rotation matrix type is Direction
    Cosines, each element in Rotation Matrix must be in the range of [-1, 1].

   •       rotation matrix type —

    rotation matrix type determines whether the Rotation Matrix contains the direction angles or
    the direction cosines.

      Direction Angles (default)—Indicates that the Rotation Matrix contains the direction angles, or
    0 the angles between the x-, y-, and z-axes and the line segments from the origin to the input
      coordinates.


                                                    © National Instruments 3943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3944 ordinal=3944 -->
## Functions

Functions


              Direction Cosines—Indicates that the Rotation Matrix contains the direction cosines, or the           1
              cosines of the direction angles.

               •     X Out —

          X Out returns the rotated x-coordinates.

               •      Y Out —

           Y Out returns the rotated y-coordinates.

               •     Z Out —

          Z Out returns the rotated z-coordinates.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       For a point P, α, β, and γ are the direction angles of vector OP, as shown in the
       following illustration:


      The cosines of the direction angles are direction cosines.

       Before the rotation, the coordinate of point Pis (x, y, z). After the rotation, the
       coordinate of point Pis (x', y', z'), where


3944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3945 ordinal=3945 -->
## Functions

Functions


A is the Rotation Matrix defined by:


α1, β1, and γ1 are the direction angles of the X'-axis to the X-, Y-, and Z-axes. α2, β2, and
γ2 are the direction angles of the Y'-axis to the X-, Y-, and Z-axes. α3, β3, and γ3 are the
direction angles of the Z'-axis to the X-, Y-, and Z-axes.

3D3D CartesianCartesian CoordinateCoordinate RotationRotation (Direction)(Direction) (Scalar)(Scalar) VIVI

Rotates a three-dimensional Cartesian coordinate in the counterclockwise direction
using the direction method. Wire data to the X input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •      x —

    x is the real input x-component for the two-element vector.

   •      y —

    y is the real input y-component for the two-element vector.

   •      z —

    z specifies the input z-coordinate.

   •      Rotation Matrix —

                                                    © National Instruments 3945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3946 ordinal=3946 -->
## Functions

Functions


            Rotation Matrix specifies the 3-by-3 direction cosine matrix. If rotation matrix type is Direction
            Cosines, each element in Rotation Matrix must be in the range of [-1, 1].

               •       rotation matrix type —

             rotation matrix type determines whether the Rotation Matrix contains the direction angles or
            the direction cosines.

              Direction Angles (default)—Indicates that the Rotation Matrix contains the direction angles, or
           0 the angles between the x-, y-, and z-axes and the line segments from the origin to the input
              coordinates.
              Direction Cosines—Indicates that the Rotation Matrix contains the direction cosines, or the           1              cosines of the direction angles.

               •      x out —

           x out returns the rotated x-coordinate.

               •      y out —

           y out returns the rotated y-coordinate.

               •      z out —

            z out returns the rotated z-coordinate.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       For a point P, α, β, and γ are the direction angles of vector OP, as shown in the
       following illustration:


3946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3947 ordinal=3947 -->
## Functions

Functions


The cosines of the direction angles are direction cosines.

Before the rotation, the coordinate of point Pis (x, y, z). After the rotation, the
coordinate of point Pis (x', y', z'), where


A is the Rotation Matrix defined by:


α1, β1, and γ1 are the direction angles of the X'-axis to the X-, Y-, and Z-axes. α2, β2, and
γ2 are the direction angles of the Y'-axis to the X-, Y-, and Z-axes. α3, β3, and γ3 are the
direction angles of the Z'-axis to the X-, Y-, and Z-axes.

CrossCross ProductProduct

Calculates the cross product of A Vector and B Vector.


                                                    © National Instruments 3947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3948 ordinal=3948 -->
## Functions

Functions

      Inputs/Outputs

               •     A Vector —

          A Vector specifies the first vector for the cross product. A Vector must contain three elements
             that specify the x-, y-, and z-coordinate of A Vector.

               •     B Vector —

         B Vector specifies the second vector for the cross product. B Vector must contain three elements
             that specify the x-, y-, and z-coordinate of B Vector.

               •      Cross Product —

            Cross Product returns the cross product of A Vector and B Vector. Cross Product contains three
           elements that specify the x-, y-, and z-coordinate of cross product vector.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Cross product is perpendicular to A Vector and B Vector. The following figure shows A
       Vector, B Vector, and Cross product of A x B.


      The VI uses the following equation to calculate the cross product of A x B:


      Ax, Ay, and Az are x-, y-, and z-coordinates of A Vector. Bx, By, and Bz are x-, y-, and z-

3948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3949 ordinal=3949 -->
## Functions

Functions

coordinates of B Vector. x̂, ŷ, and ẑ are unit vectors in Euclidean space.

EulerEuler AnglesAngles ToTo DirectionDirection CosinesCosines

Converts Euler angles into a 3-by-3 matrix of direction cosines. The VI accepts both
proper and Tait-Bryan angle types.


Inputs/Outputs

   •      Euler Angles —

    Euler Angles specifies the Euler angles in radians.

         •      phi —

        phi specifies the rotation angle about the first axis in radians.

         •      theta —

        theta specifies the rotation angle about the second axis in radians.

         •       psi —

         psi specifies the rotation angle about the third axis in radians.


   •       rotation order —

    rotation order specifies the order of the axes to rotate the coordinates around.

    For example, X-Y-Z specifies the first, second, and third rotations are about the x-, y-, and z-axes
     respectively. Z-X-Z is the default order.

    0                              X-Y-Z
    1                              X-Z-Y
    2                              Y-X-Z
    3                              Y-Z-X


                                                    © National Instruments 3949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3950 ordinal=3950 -->
## Functions

Functions


           4                              Z-X-Y
           5                              Z-Y-X
           6                              X-Y-X
           7                             X-Z-X
           8                               Y-X-Y
           9                               Y-Z-Y
           10                            Z-X-Z
           11                             Z-Y-Z

               •       Direction Cosines —

             Direction Cosines returns the 3-by-3 direction cosine matrix, which maps points in the old
            coordinate frame to points in the new coordinate frame. Each element in Direction Cosines must
          be in the range of [-1, 1].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      You can express a rotation using direction cosines or Euler angles. The following
       equation describes the relationship between Euler Angles and Direction Cosines
      (assume the rotation is the default Z-X-Z order):

   R=


      where Ris the output 3-by-3 Direction Cosines matrix. ϕ (–π < ϕ ≤ π), θ (0 ≤ θ ≤ π), and
    ψ (–π < ψ ≤ π) are the input Euler Angles in radians.

      DirectionDirection CosinesCosines ToTo EulerEuler AnglesAngles

       Converts a 3-by-3 matrix of direction cosines into Euler angles.


3950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3951 ordinal=3951 -->
## Functions

Functions

Inputs/Outputs

   •       Direction Cosines —

    Direction Cosines specifies the 3-by-3 direction cosine matrix, which maps points in the old
    coordinate frame to points in the new coordinate frame. Each element in Direction Cosines must
    be in the range of [-1, 1].

   •       rotation order —

    rotation order specifies the order of the axes to rotate the coordinates around.

    For example, X-Y-Z specifies the first, second, and third rotations are about the x-, y-, and z-axes
     respectively. Z-X-Z is the default order.

    0                              X-Y-Z
    1                              X-Z-Y
    2                              Y-X-Z
    3                              Y-Z-X
    4                              Z-X-Y
    5                              Z-Y-X
    6                              X-Y-X
    7                             X-Z-X
    8                               Y-X-Y
    9                               Y-Z-Y
    10                            Z-X-Z
    11                             Z-Y-Z

   •      Euler Angles —

    Euler Angles returns the Euler angles in radians.

         •      phi —

        phi returns the rotation angle about the first axis in radians.

         •      theta —

        theta returns the rotation angle about the second axis in radians.

         •       psi —


                                                    © National Instruments 3951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3952 ordinal=3952 -->
## Functions

Functions


                  psi returns the rotation angle about the third axis in radians.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      You can express a rotation using direction cosines or Euler angles. The following
       equation describes the relationship between Direction Cosines and Euler Angles
      (assume the rotation is the default Z-X-Z order):

   R=


      where Ris the input 3-by-3 Direction Cosines matrix. ϕ (–π < ϕ ≤ π), θ (0 ≤ θ ≤ π), and ψ
       (–π < ψ ≤ π) are the output Euler Angles in radians.

    3D3D CoordinateCoordinate ConversionConversion

       Converts coordinates between the Cartesian, spherical, and cylindrical coordinate
       systems. Wire data to the Axis 1 input to determine the polymorphic instance to use or
      manually select the instance.


            • 3D Coordinate Conversion (Array) VI
            • 3D Coordinate Conversion (Scalar) VI

      The following illustrations show a point Pin different three-dimensional coordinate
       systems:


3952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3953 ordinal=3953 -->
## Functions

Functions


The Cartesian, or rectangular, coordinate system is the most widely used coordinate
system. The cylindrical coordinate system is a generalization of two-dimensional polar
coordinates to three dimensions. The following equations describe the relationship
between a Cartesian coordinate and a cylindrical coordinate:

x= ρ · cosθ, y= ρ · sinθ, z= z

ρ is the radial coordinate, and θ (–π < θ ≤ π) is the azimuthal coordinate.

The spherical coordinate system is a system of curvilinear coordinates that is natural
for describing positions on a sphere. The following equations describe the relationship
between a Cartesian coordinate and a spherical coordinate:

x= r· sinϕ · cosθ, y= r· sinθ · sinϕ, z= r· cosϕ

ris the distance from point Pto the origin. θ (–π < θ ≤ π) is the azimuthal angle, and ϕ
(0 ≤ ϕ ≤ π) is the polar angle.

3D3D CoordinateCoordinate ConversionConversion (Array)(Array) VIVI

Converts coordinates between the Cartesian, spherical, and cylindrical coordinate
systems. Wire data to the Axis 1 input to determine the polymorphic instance to use or
manually select the instance.


                                                    © National Instruments 3953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3954 ordinal=3954 -->
## Functions

Functions

      Inputs/Outputs

               •       Axis 1 —

             Axis 1 specifies the X-coordinates in a Cartesian coordinate system, rho-coordinates in a
              cylindrical coordinate system, or radius-coordinates in a spherical coordinate system.

               •       Axis 2 —

             Axis 2 specifies the Y-coordinates in a Cartesian coordinate system, theta-coordinates in a
              cylindrical coordinate system, or theta-coordinates in a spherical coordinate system.

               •       Axis 3 —

             Axis 3 specifies the Z-coordinates in a Cartesian coordinate system, z-coordinates in a cylindrical
            coordinate system, or phi-coordinates in a spherical coordinate system.

               •      conversion type —

            conversion type specifies the type of conversion to perform.

           0   Cartesian to spherical (default)
           1   spherical to Cartesian
           2   Cartesian to cylindrical
           3   cylindrical to Cartesian
           4   spherical to cylindrical
           5   cylindrical to spherical

               •       Axis 1 Out —

             Axis 1 Out returns the coordinates on the first axis in the new coordinate system.

               •       Axis 2 Out —

             Axis 2 Out returns the coordinates on the second axis in the new coordinate system.

               •       Axis 3 Out —

             Axis 3 Out returns the coordinates on the third axis in the new coordinate system.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


3954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3955 ordinal=3955 -->
## Functions

Functions


    Code VI to convert the error code or warning into an error cluster.


The following illustrations show a point Pin different three-dimensional coordinate
systems:


The Cartesian, or rectangular, coordinate system is the most widely used coordinate
system. The cylindrical coordinate system is a generalization of two-dimensional polar
coordinates to three dimensions. The following equations describe the relationship
between a Cartesian coordinate and a cylindrical coordinate:

x= ρ · cosθ, y= ρ · sinθ, z= z

ρ is the radial coordinate, and θ (–π < θ ≤ π) is the azimuthal coordinate.

The spherical coordinate system is a system of curvilinear coordinates that is natural
for describing positions on a sphere. The following equations describe the relationship
between a Cartesian coordinate and a spherical coordinate:

x= r· sinϕ · cosθ, y= r· sinθ · sinϕ, z= r· cosϕ

ris the distance from point Pto the origin. θ (–π < θ ≤ π) is the azimuthal angle, and ϕ
(0 ≤ ϕ ≤ π) is the polar angle.

3D3D CoordinateCoordinate ConversionConversion (Scalar)(Scalar) VIVI

Converts coordinates between the Cartesian, spherical, and cylindrical coordinate
systems. Wire data to the Axis 1 input to determine the polymorphic instance to use or
manually select the instance.


                                                    © National Instruments 3955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3956 ordinal=3956 -->
## Functions

Functions


      Inputs/Outputs

               •       axis 1 —

             axis 1 specifies the X-coordinate in a Cartesian coordinate system, rho-coordinate in a cylindrical
            coordinate system, or radius-coordinate in a spherical coordinate system.

               •       axis 2 —

             axis 2 specifies the Y-coordinate in a Cartesian coordinate system, theta-coordinate in a
              cylindrical coordinate system, or theta-coordinate in a spherical coordinate system.

               •       axis 3 —

             axis 3 specifies the Z-coordinate in a Cartesian coordinate system, z-coordinate in a cylindrical
            coordinate system, or phi-coordinate in a spherical coordinate system.

               •      conversion type —

            conversion type specifies the type of conversion to perform.

           0   Cartesian to spherical (default)
           1   spherical to Cartesian
           2   Cartesian to cylindrical
           3   cylindrical to Cartesian
           4   spherical to cylindrical
           5   cylindrical to spherical

               •       axis 1 out —

             axis 1 out returns the coordinate on the first axis in the new coordinate system.

               •       axis 2 out —

             axis 2 out returns the coordinate on the second axis in the new coordinate system.

               •       axis 3 out —


3956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3957 ordinal=3957 -->
## Functions

Functions


     axis 3 out returns the coordinate on the third axis in the new coordinate system.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following illustrations show a point Pin different three-dimensional coordinate
systems:


The Cartesian, or rectangular, coordinate system is the most widely used coordinate
system. The cylindrical coordinate system is a generalization of two-dimensional polar
coordinates to three dimensions. The following equations describe the relationship
between a Cartesian coordinate and a cylindrical coordinate:

x= ρ · cosθ, y= ρ · sinθ, z= z

ρ is the radial coordinate, and θ (–π < θ ≤ π) is the azimuthal coordinate.

The spherical coordinate system is a system of curvilinear coordinates that is natural
for describing positions on a sphere. The following equations describe the relationship
between a Cartesian coordinate and a spherical coordinate:

x= r· sinϕ · cosθ, y= r· sinθ · sinϕ, z= r· cosϕ

ris the distance from point Pto the origin. θ (–π < θ ≤ π) is the azimuthal angle, and ϕ
(0 ≤ ϕ ≤ π) is the polar angle.


                                                    © National Instruments 3957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3958 ordinal=3958 -->
## Functions

Functions

     AngleAngle

      Use the Angle VIs to manipulate angles.

      The VIs on this palette can return mathematics error codes and signal processing error
       codes.


         Palette Object    Description

                       Wraps the input angle to a value within the range you specify with angle range.
       Wrap Angle                          Wire data to any of the angle inputs to determine the polymorphic instance to
                         use or manually select the instance.


                            Calculates the complementary angle of the input angle.
        Complementary
        Angle            Wire data to any of the angle inputs to determine the polymorphic instance to
                         use or manually select the instance.


                            Calculates the supplementary angle of the input angle.
        Supplementary
        Angle            Wire data to any of the angle inputs to determine the polymorphic instance to
                         use or manually select the instance.


                           Rotates the input angle counterclockwise.
        Angle Rotation                          Wire data to the angle input to determine the polymorphic instance to use or
                         manually select the instance.


                            Calculates the angle that bisects the start angle and the end angle into two
         Bisect Angle
                         equal parts.


3958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3959 ordinal=3959 -->
## Functions

Functions


 Palette Object    Description

                  Wire data to any of the angle inputs to determine the polymorphic instance to
                 use or manually select the instance.


                 Checks whether one or multiple input angles are within the counterclockwise
                   range. Check for
 Included Angle                  Wire data to any of the angle inputs to determine the polymorphic instance to
                 use or manually select the instance.


                    Calculates the absolute difference between two input angles or multiple pairs of
                   input angles. Absolute Angle
 Difference                  Wire data to any of the angle inputs to determine the polymorphic instance to
                 use or manually select the instance.


WrapWrap AngleAngle

Wraps the input angle to a value within the range you specify with angle range.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


   • Wrap Angle (scalar) VI
   • Wrap Angle (array) VI

This VI wraps an angle to a value within the angle range you specify.

For example, if angle units is degree in, degree out and angle range is 0 to
360, the VI wraps the angle according to the following formula.

y= x– 360 * floor(x/360)

                                                    © National Instruments 3959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3960 ordinal=3960 -->
## Functions

Functions

      where xis angle in and y is angle out.
   WrapWrap AngleAngle (scalar)(scalar) VIVI

      Wraps the input angle to a value within the range you specify with angle range.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      angle units —

            angle units specifies the units of the input and output angles of the VI.

           0   radian in, radian out (default)
           1   radian in, degree out
           2   degree in, degree out
           3   degree in, radian out

               •      angle in —

           Angle In specifies the input angles the VI wraps.

               •      angle range —

            angle range specifies the range of the elements in Angle Out.

           0 none—The VI does not wrap the input angle. The range is [-Inf, Inf].
             -180 to 180 (-pi to pi) (default)—The VI wraps the input angle to a range of [-180, 180] in
           1
             degrees or [-pi, pi] in radians.
            0 to 360 (0 to 2pi)—The VI wraps the input angle to a range of [0, 360] in degrees or [0, 2pi] in
           2
               radians.

               •      angle out —

3960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3961 ordinal=3961 -->
## Functions

Functions


    Angle Out returns the angles within angle range. The elements in Angle Out correspond to the
    elements in Angle In.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI wraps an angle to a value within the angle range you specify.

For example, if angle units is degree in, degree out and angle range is 0 to
360, the VI wraps the angle according to the following formula.

y= x– 360 * floor(x/360)

where xis angle in and y is angle out.
WrapWrap AngleAngle (array)(array) VIVI

Wraps the input angle to a value within the range you specify with angle range.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out


                                                    © National Instruments 3961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3962 ordinal=3962 -->
## Functions

Functions


           2   degree in, degree out
           3   degree in, radian out

               •      Angle In —

            angle in specifies the input angle the VI wraps.

               •      angle range —

            angle range specifies the range of angle out.

           0 none—The VI does not wrap the input angle. The range is [—Inf, Inf].
            –180 to 180 (–pi to pi) (default)—The VI wraps the input angle to a range of [–180, 180] in           1             degrees or [–pi, pi] in radians.
            0 to 360 (0 to 2pi)—The VI wraps the input angle to a range of [0, 360] in degrees or [0, 2pi] in
           2               radians.

               •      Angle Out —

            angle out returns the angle within angle range.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       This VI wraps an angle to a value within the angle range you specify.

       For example, if angle units is degree in, degree out and angle range is 0 to
       360, the VI wraps the angle according to the following formula.

   y= x– 360 * floor(x/360)

      where xis angle in and y is angle out.

     ComplementaryComplementary AngleAngle

       Calculates the complementary angle of the input angle.


3962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3963 ordinal=3963 -->
## Functions

Functions

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


  • Complementary Angle (scalar) VI
  • Complementary Angle (array) VI
ComplementaryComplementary AngleAngle (scalar)(scalar) VIVI

Calculates the complementary angle of the input angle.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •      angle —

    angle specifies the input angle. angle must be in the range of [0, 90] in degrees or [0, pi/2] in
     radians.

   •     complementary angle —


                                                    © National Instruments 3963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3964 ordinal=3964 -->
## Functions

Functions


          complementary angle returns the complementary angle of angle. complementary angle is in
            the range of [0, 90] in degrees or [0, pi/2] in radians.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   ComplementaryComplementary AngleAngle (array)(array) VIVI

       Calculates the complementary angle of the input angle.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      angle units —

            angle units specifies the units of the input and output angles of the VI.

           0   radian in, radian out (default)
           1   radian in, degree out
           2   degree in, degree out
           3   degree in, radian out

               •      Angle —

           Angle specifies the input angles. Angle must be in the range of [0, 90] in degrees or [0, pi/2] in
             radians.

               •     Complementary Angle —


3964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3965 ordinal=3965 -->
## Functions

Functions


    Complementary Angle returns the complementary angles of Angle. The elements in
    Complementary Angle correspond to the elements in Angle. Complementary Angle is in the
    range of [0, 90] in degrees or [0, pi/2] in radians.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


SupplementarySupplementary AngleAngle

Calculates the supplementary angle of the input angle.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


  • Supplementary Angle (scalar) VI
  • Supplementary Angle (array) VI
SupplementarySupplementary AngleAngle (scalar)(scalar) VIVI

Calculates the supplementary angle of the input angle.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      angle units —


                                                    © National Instruments 3965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3966 ordinal=3966 -->
## Functions

Functions


            angle units specifies the units of the input and output angles of the VI.

           0   radian in, radian out (default)
           1   radian in, degree out
           2   degree in, degree out
           3   degree in, radian out

               •      angle —

            angle specifies the input angle. angle must be in the range of [0, 180] in degrees or [0, pi] in
             radians.

               •      supplementary angle —

           supplementary angle returns the supplementary angle of the angle input. supplementary
            angle is in the range of [0, 180] in degrees or [0, pi] in radians.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   SupplementarySupplementary AngleAngle (array)(array) VIVI

       Calculates the supplementary angle of the input angle.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      angle units —


3966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3967 ordinal=3967 -->
## Functions

Functions


    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •      Angle —

    Angle specifies the input angles. Angle must be in the range of [0, 180] in degrees or [0, pi] in
     radians.

   •      Supplementary Angle —

    Supplementary Angle returns the supplementary angles of the Angle input. The elements in
    Supplementary Angle correspond to the elements in Angle. Supplementary Angle is in the
    range of [0, 180] in degrees or [0, pi] in radians.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


AngleAngle RotationRotation

Rotates the input angle counterclockwise.

Wire data to the angle input to determine the polymorphic instance to use or manually
select the instance.


  • Angle Rotation (scalar) VI
  • Angle Rotation (array) VI
  • Angle Rotation with Same Angle (array) VI


                                                    © National Instruments 3967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3968 ordinal=3968 -->
## Functions

Functions

   AngleAngle RotationRotation (scalar)(scalar) VIVI

       Rotates the input angle counterclockwise.

       Wire data to the angle input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •      angle units —

            angle units specifies the units of the input and output angles of the VI.

           0   radian in, radian out (default)
           1   radian in, degree out
           2   degree in, degree out
           3   degree in, radian out

               •      angle —

            angle specifies the angle the VI rotates.

               •      counterclockwise rotation —

            counterclockwise rotation specifies the amount that the VI uses to rotate the angle in the
            counterclockwise direction. counterclockwise rotation must have the same unit as angle.

               •      rotated angle range —

            rotated angle range specifies the range of values for the rotated angle. When an angle exceeds
          one side of the range, the rotated angle continues on the other side of the range.

           0 none—The range is [–Inf, Inf].
           1 –180 to 180 (–pi to pi) (default)—The range is [–180, 180] in degrees or [–pi, pi] in radians.


3968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3969 ordinal=3969 -->
## Functions

Functions


    2 0 to 360 (0 to 2pi)—The range is [0, 360] in degrees or [0, 2pi] in radians.

   •      rotated angle —

    rotated angle returns the angle that the VI rotates counterclockwise.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

AngleAngle RotationRotation (array)(array) VIVI

Rotates the input angle counterclockwise.

Wire data to the angle input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •      Angle —

    Angle specifies the angles the VI rotates.

   •      Counterclockwise Rotation —

                                                    © National Instruments 3969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3970 ordinal=3970 -->
## Functions

Functions


           Counterclockwise Rotation specifies the amount that the VI pairs with the elements in Angle to
             rotate the angle in the counterclockwise direction. The elements in Counterclockwise Rotation
          must have the same units as the elements in Angle.

           Angle and Counterclockwise Rotation must have the same number of elements or the VI returns
             error code –20002.

               •      rotated angle range —

            rotated angle range specifies the range of values for the rotated angle. When an angle exceeds
          one side of the range, the rotated angle continues on the other side of the range.

           0 none—The range is [–Inf, Inf].
           1 –180 to 180 (–pi to pi) (default)—The range is [–180, 180] in degrees or [–pi, pi] in radians.
           2 0 to 360 (0 to 2pi)—The range is [0, 360] in degrees or [0, 2pi] in radians.

               •      Rotated Angle —

           Rotated Angle returns the angles that the VI rotates counterclockwise.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   AngleAngle RotationRotation withwith SameSame AngleAngle (array)(array) VIVI

       Rotates the input angle counterclockwise.

       Wire data to the angle input to determine the polymorphic instance to use or manually
        select the instance.

           Note Use this instance to rotate a set of input angles the same amount.


3970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3971 ordinal=3971 -->
## Functions

Functions


Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •      Angle —

    Angle specifies the angles the VI rotates.

   •      counterclockwise rotation —

    counterclockwise rotation specifies the amount that the VI uses to rotate the angles in the
    counterclockwise direction. counterclockwise rotation must have the same unit as Angle.

   •      rotated angle range —

    rotated angle range specifies the range of values for the rotated angle. When an angle exceeds
    one side of the range, the rotated angle continues on the other side of the range.

    0 none—The range is [–Inf, Inf].
    1 –180 to 180 (–pi to pi) (default)—The range is [–180, 180] in degrees or [–pi, pi] in radians.
    2 0 to 360 (0 to 2pi)—The range is [0, 360] in degrees or [0, 2pi] in radians.

   •      Rotated Angle —

    Rotated Angle returns the angles that the VI rotates counterclockwise.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3972 ordinal=3972 -->
## Functions

Functions

       BisectBisect AngleAngle

       Calculates the angle that bisects the start angle and the end angle into two equal
        parts.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


            • Bisect Angle (scalar) VI
            • Bisect Angle (array) VI

      The following images show examples of the angle bisector between a start angle and
      an end angle.


    BisectBisect AngleAngle (scalar)(scalar) VIVI

       Calculates the angle that bisects the start angle and the end angle into two equal
        parts.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


3972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3973 ordinal=3973 -->
## Functions

Functions

Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •       start angle —

     start angle specifies one angle the VI uses to calculate the angle bisector in the clockwise
     direction.

   •     end angle —

    end angle specifies the other angle the VI uses to calculate the angle bisector. end angle must
    have the same unit as start angle.

   •      angle bisector range —

    angle bisector range specifies the range of the angle bisector.

    0 none—The range is equal to [–Inf, Inf].
    1 –180 to 180 (–pi to pi) (default)—The range is [–180, 180] in degrees or [–pi, pi] in radians.
    2 0 to 360 (0 to 2pi)—The range is [0, 360] in degrees or [0, 2pi] in radians.

   •      angle bisector —

    angle bisector returns the angle that bisects start angle and end angle into two equal parts.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following images show examples of the angle bisector between a start angle and
an end angle.


                                                    © National Instruments 3973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3974 ordinal=3974 -->
## Functions

Functions


    BisectBisect AngleAngle (array)(array) VIVI

       Calculates the angle that bisects the start angle and the end angle into two equal
        parts.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      angle units —

            angle units specifies the units of the input and output angles of the VI.

           0   radian in, radian out (default)
           1   radian in, degree out
           2   degree in, degree out
           3   degree in, radian out

               •       Start Angle —

             Start Angle specifies one set of angles that the VI pairs with the elements in End Angle to
             calculate the angle bisectors in the clockwise direction.

               •     End Angle —

          End Angle specifies another set of the angles the VI pairs with the elements in Start Angle to
             calculate the angle bisectors. The elements in End Angle must have the same units as Start
             angle.


3974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3975 ordinal=3975 -->
## Functions

Functions


     Start Angle and End Angle must have the same number of elements or the VI returns error code
    –20002.

   •      angle bisector range —

    angle bisector range specifies the range of the angle bisector.

    0 none—The range is equal to [–Inf, Inf].
    1 –180 to 180 (–pi to pi) (default)—The range is [–180, 180] in degrees or [–pi, pi] in radians.
    2 0 to 360 (0 to 2pi)—The range is [0, 360] in degrees or [0, 2pi] in radians.

   •      Angle Bisector —

    Angle Bisector returns the angles that bisect each corresponding pairs of elements in Start
    Angle and End Angle into two equal parts.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following images show examples of the angle bisector between a start angle and
an end angle.


CheckCheck forfor IncludedIncluded AngleAngle

Checks whether one or multiple input angles are within the counterclockwise range.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


                                                    © National Instruments 3975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3976 ordinal=3976 -->
## Functions

Functions

            • Check for Included Angle (scalar) VI
            • Check for Included Angle (array) VI

      The following image shows an example of the input angle withinthe range from the
        start angle to the end angle.


      The following image shows an example of the input angle outof the range from the
        start angle to the end angle.


           If you use this VI to check whether a range includes the angle in the previous image,
       the VI coerces angle out to start angle if coerce angle is TRUE.
   CheckCheck forfor IncludedIncluded AngleAngle (scalar)(scalar) VIVI

      Checks whether one or multiple input angles are within the counterclockwise range.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


3976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3977 ordinal=3977 -->
## Functions

Functions


Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •      angle in —

    angle in specifies the input angle the VI checks.

   •       start angle —

     start angle specifies the angle at the beginning of the range. The range continues in the
    counterclockwise direction.

   •     end angle —

    end angle specifies the angle at the end of the range. end angle must have the same unit as the
     start angle.

   •      output angle range —

    output angle range specifies the range of the output angle. When the angle exceeds one side of
    the range, the angle continues on the opposite side of the range.

    0 none—The range is [–Inf, Inf].
    1 –180 to 180 (–pi to pi) (default)—The range is [–180, 180] in degrees or [–pi, pi] in radians.
    2 0 to 360 (0 to 2pi)—The range is [0, 360] in degrees or [0, 2pi] in radians.

   •      coerce angle —


                                                    © National Instruments 3977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3978 ordinal=3978 -->
## Functions

Functions


            coerce angle determines whether angle out is in the range when angle in is not in range. If
            FALSE, angle out returns the same value as angle in. If TRUE, angle out returns the value of the
            angle that is nearest to the beginning or end of the range.

            coerce angle does not do anything when angle in is in the range.

               •      angle out —

            angle out returns angle in if coerce angle is FALSE. If coerce angle is TRUE and angle in is
           between the range of start angle and end angle, angle out also returns angle in.

                    If coerce angle is TRUE and angle in is out of the range, the VI coerces angle out to the nearest
            angle in the range.

               •       in range? —

             in range? returns whether angle in is between start angle and end angle.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following image shows an example of the input angle withinthe range from the
        start angle to the end angle.


      The following image shows an example of the input angle outof the range from the
        start angle to the end angle.


3978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3979 ordinal=3979 -->
## Functions

Functions


If you use this VI to check whether a range includes the angle in the previous image,
the VI coerces angle out to start angle if coerce angle is TRUE.
CheckCheck forfor IncludedIncluded AngleAngle (array)(array) VIVI

Checks whether one or multiple input angles are within the counterclockwise range.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •      Angle In —

    Angle In specifies a set of input angles the VI checks. The elements in Angle In correspond to the
    elements in Start Angle and End Angle.


                                                    © National Instruments 3979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3980 ordinal=3980 -->
## Functions

Functions

               •       Start Angle —

             Start Angle specifies the set of angles at the beginning of the ranges. The ranges continue in the
            counterclockwise direction.

               •     End Angle —

          End Angle specifies the set of angles at the end of the ranges. The elements in End Angle must
           have the same units as the elements in Start Angle.

           Angle In, Start Angle, and End Angle must have the same number of elements or the VI returns
             error code –20002.

               •      output angle range —

           output angle range specifies the range of the output angle. When the angle exceeds one side of
            the range, the angle continues on the opposite side of the range.

           0 none—The range is [–Inf, Inf].
           1 –180 to 180 (–pi to pi) (default)—The range is [–180, 180] in degrees or [–pi, pi] in radians.
           2 0 to 360 (0 to 2pi)—The range is [0, 360] in degrees or [0, 2pi] in radians.

               •      coerce angle —

            coerce angle determines whether angle out is in the range when angle in is not in range. If
            FALSE, angle out returns the same value as angle in. If TRUE, angle out returns the value of the
            angle that is nearest to the beginning or end of the range.

            coerce angle does not do anything when angle in is in the range.

               •      Angle Out —

           Angle Out returns the elements in Angle In if coerce angle is FALSE. If coerce angle is TRUE and
            corresponding elements of Angle In are between the ranges of Start Angle and End Angle, Angle
          Out also returns Angle In.

                    If coerce angle is TRUE and the corresponding elements of Angle In are out of range, the VI
            coerces the elements of Angle Out to the nearest angle of each range.

               •       In Range? —

             In Range? returns whether Angle In is within the range between Start Angle and End Angle.

               •       error —


3980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3981 ordinal=3981 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following image shows an example of the input angle withinthe range from the
start angle to the end angle.


The following image shows an example of the input angle outof the range from the
start angle to the end angle.


If you use this VI to check whether a range includes the angle in the previous image,
the VI coerces angle out to start angle if coerce angle is TRUE.

AbsoluteAbsolute AngleAngle DifferenceDifference

Calculates the absolute difference between two input angles or multiple pairs of input
angles.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


                                                    © National Instruments 3981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3982 ordinal=3982 -->
## Functions

Functions

            • Absolute Angle Difference (scalar) VI
            • Absolute Angle Difference (array) VI
   AbsoluteAbsolute AngleAngle DifferenceDifference (scalar)(scalar) VIVI

       Calculates the absolute difference between two input angles or multiple pairs of input
       angles.

       Wire data to any of the angle inputs to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •      angle units —

            angle units specifies the units of the input and output angles of the VI.

           0   radian in, radian out (default)
           1   radian in, degree out
           2   degree in, degree out
           3   degree in, radian out

               •      angle 1 —

            angle 1 specifies one input angle the VI uses to calculate the absolute angle difference.

               •      angle 2 —

            angle 2 specifies another input angle the VI uses to calculate the absolute angle difference.
            angle 2 must have the same units as angle 1.

               •      absolute angle difference —

            absolute angle difference returns the absolute difference between angle 1 and angle 2.

               •       error —

3982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3983 ordinal=3983 -->
## Functions

Functions


    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

AbsoluteAbsolute AngleAngle DifferenceDifference (array)(array) VIVI

Calculates the absolute difference between two input angles or multiple pairs of input
angles.

Wire data to any of the angle inputs to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •      angle units —

    angle units specifies the units of the input and output angles of the VI.

    0   radian in, radian out (default)
    1   radian in, degree out
    2   degree in, degree out
    3   degree in, radian out

   •      Angle 1 —

    Angle 1 specifies one set of input angles that the VI pairs with the elements in Angle 2 to
     calculate the absolute angle difference.

   •      Angle 2 —

    Angle 2 specifies another set of angles that the VI pairs with the elements in Angle 1 to calculate
    the absolute angle difference. The elements in Angle 2 must have the same units as the
    elements in Angle 1.


                                                    © National Instruments 3983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3984 ordinal=3984 -->
## Functions

Functions


           Angle 1 and Angle 2 must have the same number of elements or the VI returns error code
            –20002.

               •      Absolute Angle Difference —

            Absolute Angle Difference returns the absolute angle differences between each corresponding
             pair of elements in Angle 1 and Angle 2.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

     ComputationalComputational GeometryGeometry

      Use the Computational Geometry VIs to compute a geometrical problem.


         Palette Object     Description

        Contour Line      Calculates and returns the contour lines of a surface and the contour graph.


        Polygon Area      Calculates the signed area of a simple polygon.


         Point in Polygon    Verifies whether a point is inside a polygon.


        Polygon Centroid  Computes the centroid of a polygon.


        Delaunay
                       Computes the Delaunay triangulation of the specified points in the plane.
         Triangulation


3984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3985 ordinal=3985 -->
## Functions

Functions


 Palette Object     Description

 Voronoi Diagram  Computes the Voronoi diagram of specified points in a plane.


                Computes the vertices of a convex polygon, which are the set of points that Convex Hull               make up the polygon that contains all the points.


 Convex Polygon                Computes the intersection of two convex polygons. Intersection

ContourContour LineLine

Calculates and returns the contour lines of a surface and the contour graph.

You must manually select the polymorphic instance to use.


   • Contour Line (Number of Heights) VI
   • Contour Line (Scalar) VI
   • Contour Line (Array) VI

Contour lines of a surface are line segments that connect points at the same height, as
shown in the following equation.

f(x,y) = h

The following image provides an example of an open contour line and a closed
contour line.


                                                    © National Instruments 3985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3986 ordinal=3986 -->
## Functions

Functions


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Geometry\Contour Line
        Plot.vi
   ContourContour LineLine (Number(Number ofof Heights)Heights) VIVI

       Calculates and returns the contour lines of a surface and the contour graph.

      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •     X —

          X specifies the x-coordinates of the surface.


3986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3987 ordinal=3987 -->
## Functions

Functions


   If X is not empty, the length of X must equal the number of columns in Z. If X is empty, this VI
  gives X values of [0, 1, …, N– 1], where Nis the number of columns in Z.

•      Y —

  Y specifies the y-coordinates of the surface.

   If Y is not empty, the length of Y must equal the number of rows in Z. If Y is empty, this VI gives Y
  values of [0, 1, …, M– 1], where Mis the number of rows in Z.

•     Z —

  Z is the 2D array that specifies values of the surface.

•     number of heights —

  number of heights specifies the number of contour lines the VI calculates. The default is 10.

•      Contour Graph —

  Contour Graph returns an XY graph that draws the contour lines.

•      Contour Line —

  Contour Line returns an array of the contour lines. Each element of the array contains the
  contour lines for each height.

      •      height —

      height returns the height of the contour line.

      •      Contour Segments —

      Contour Segments returns an array of the contour lines at height.

             •     X —

         X returns the x-coordinates of the contour line.

             •      Y —


                                                   © National Instruments 3987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3988 ordinal=3988 -->
## Functions

Functions


                   Y returns the y-coordinates of the contour line. The first point to form at (X, Y) is
                       different from the last point.

                           •      closed? —

                    closed? indicates that all points form a closed contour line if TRUE. If FALSE, the
                    contour line is open.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Contour lines of a surface are line segments that connect points at the same height, as
      shown in the following equation.

       f(x,y) = h

      The following image provides an example of an open contour line and a closed
       contour line.


3988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3989 ordinal=3989 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Geometry\Contour Line
   Plot.vi
ContourContour LineLine (Scalar)(Scalar) VIVI

Calculates and returns the contour lines of a surface and the contour graph.

You must manually select the polymorphic instance to use.


Inputs/Outputs

   •     X —

    X specifies the x-coordinates of the surface.

       If X is not empty, the length of X must equal the number of columns in Z. If X is empty, this VI
    gives X values of [0, 1, …, N– 1], where Nis the number of columns in Z.

   •      Y —

    Y specifies the y-coordinates of the surface.

       If Y is not empty, the length of Y must equal the number of rows in Z. If Y is empty, this VI gives Y
    values of [0, 1, …, M– 1], where Mis the number of rows in Z.

   •     Z —

    Z is the 2D array that specifies values of the surface.

   •      height —


                                                    © National Instruments 3989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3990 ordinal=3990 -->
## Functions

Functions


            height specifies the height where the VI calculates the contour line.

               •      Contour Graph —

           Contour Graph returns an XY graph that draws the contour lines.

               •      Contour Line —

           Contour Line returns the contour line at height.

                     •      height —

                height returns the height of the contour line.

                     •      Contour Segments —

               Contour Segments returns an array of the contour lines at height.

                           •     X —

                 X returns the x-coordinates of the contour line.

                           •      Y —

                   Y returns the y-coordinates of the contour line. The first point to form at (X, Y) is
                       different from the last point.

                           •      closed? —

                    closed? indicates that all points form a closed contour line if TRUE. If FALSE, the
                    contour line is open.


               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Contour lines of a surface are line segments that connect points at the same height, as
      shown in the following equation.


3990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3991 ordinal=3991 -->
## Functions

Functions

f(x,y) = h

The following image provides an example of an open contour line and a closed
contour line.


Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Mathematics\Geometry\Contour Line
   Plot.vi
ContourContour LineLine (Array)(Array) VIVI

Calculates and returns the contour lines of a surface and the contour graph.

You must manually select the polymorphic instance to use.


                                                    © National Instruments 3991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3992 ordinal=3992 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X specifies the x-coordinates of the surface.

                    If X is not empty, the length of X must equal the number of columns in Z. If X is empty, this VI
             gives X values of [0, 1, …, N– 1], where Nis the number of columns in Z.

               •      Y —

           Y specifies the y-coordinates of the surface.

                    If Y is not empty, the length of Y must equal the number of rows in Z. If Y is empty, this VI gives Y
            values of [0, 1, …, M– 1], where Mis the number of rows in Z.

               •     Z —

          Z is the 2D array that specifies values of the surface.

               •      Heights —

            Heights specifies an array of heights where the VI calculates the contour line.

               •      Contour Graph —

           Contour Graph returns an XY graph that draws the contour lines.

               •      Contour Line —

           Contour Line returns an array of the contour lines. Each element of the array contains the
            contour lines for each height.

                     •      height —

                height returns the height of the contour line.

                     •      Contour Segments —

               Contour Segments returns an array of the contour lines at height.

                           •     X —


3992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3993 ordinal=3993 -->
## Functions

Functions


           X returns the x-coordinates of the contour line.

                •      Y —

            Y returns the y-coordinates of the contour line. The first point to form at (X, Y) is
               different from the last point.

                •      closed? —

             closed? indicates that all points form a closed contour line if TRUE. If FALSE, the
            contour line is open.


   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Contour lines of a surface are line segments that connect points at the same height, as
shown in the following equation.

f(x,y) = h

The following image provides an example of an open contour line and a closed
contour line.


                                                    © National Instruments 3993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3994 ordinal=3994 -->
## Functions

Functions


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Geometry\Contour Line
        Plot.vi

      PolygonPolygon AreaArea

       Calculates the signed area of a simple polygon.


      Inputs/Outputs

               •     X —

          X specifies the x-coordinates of the vertices of the polygon. The length of X must be greater than
            or equal to 3.

               •      Y —

           Y specifies the y-coordinates of the vertices of the polygon. The length of Y must equal the length
             of X.


3994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3995 ordinal=3995 -->
## Functions

Functions

   •      signed area —

    signed area returns the signed area of the polygon. The signed area is positive if the vertices of
    the polygon are in counterclockwise order. Otherwise, signed area is negative.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


A simple polygon is a polygon with no boundaries that cross each other. The following
equation defines the signed area of a simple polygon with nvertices.


where (xi, yi) is the ith vertex and (xn, yn) = (x0, y0).

PointPoint inin PolygonPolygon

Verifies whether a point is inside a polygon.

Wire data to the x or y input to determine the polymorphic instance to use or manually
select the instance.


  • Point in Polygon (Scalar) VI
  • Point in Polygon (Array) VI
PointPoint inin PolygonPolygon (Scalar)(Scalar) VIVI

Verifies whether a point is inside a polygon.

Wire data to the x or y input to determine the polymorphic instance to use or manually
select the instance.

                                                    © National Instruments 3995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3996 ordinal=3996 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x specifies the x-coordinate of the point.

               •      y —

           y specifies the y-coordinate of the point.

               •      Polygon X —

           Polygon X specifies the x-coordinates of the vertices of the polygon. The length of Polygon X
          must be greater than or equal to 3.

               •      Polygon Y —

           Polygon Y specifies the y-coordinates of the vertices of the polygon. The length of Polygon Y
          must equal the length of Polygon X.

               •      tolerance —

            tolerance controls the accuracy of verifying whether a point lies on the boundary. The default is
            1E–9. If tolerance is less than 0, the VI sets tolerance to 1E–9.

               •      position —

            position specifies the position of the given point relative to the polygon.

           0 Inside—The given point is inside the polygon.
           1 On Boundary—The given point is on the boundary of the polygon.
           2 Outside—The given point is outside the polygon.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


3996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3997 ordinal=3997 -->
## Functions

Functions

PointPoint inin PolygonPolygon (Array)(Array) VIVI

Verifies whether a point is inside a polygon.

Wire data to the x or y input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •     X —

    X specifies the x-coordinates of the points.

   •      Y —

    Y specifies the y-coordinates of the points. The length of Y must equal the length of X.

   •      Polygon X —

    Polygon X specifies the x-coordinates of the vertices of the polygon. The length of Polygon X
    must be greater than or equal to 3.

   •      Polygon Y —

    Polygon Y specifies the y-coordinates of the vertices of the polygon. The length of Polygon Y
    must equal the length of Polygon X.

   •      tolerance —

    tolerance controls the accuracy of verifying whether a point lies on the boundary. The default is
    1E–9. If tolerance is less than 0, the VI sets tolerance to 1E–9.

   •      Position —

    Position specifies the positions of given points relative to the polygon.


                                                    © National Instruments 3997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3998 ordinal=3998 -->
## Functions

Functions


           0 Inside—The given point is inside the polygon.
           1 On Boundary—The given point is on the boundary of the polygon.
           2 Outside—The given point is outside the polygon.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      PolygonPolygon CentroidCentroid

      Computes the centroid of a polygon.

           If either input contains NaN or Inf, the VI returns NaN to Centroid X and Centroid Y,
      and it also returns an error. If the polygon degenerates to a line, the VI returns NaN to
       Centroid X and Centroid Y without an error.


      Inputs/Outputs

               •     X —

          X specifies the x-coordinates of the vertices of the polygon. The length of X must be greater than
            or equal to 3.

               •      Y —

           Y specifies the y-coordinates of the vertices of the polygon. The length of Y must equal the length
             of X.

               •      Centroid X —

            Centroid X returns the x-coordinate of the centroid.

               •      Centroid Y —


3998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3999 ordinal=3999 -->
## Functions

Functions


    Centroid Y returns the y-coordinate of the centroid.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The centroid of a polygon is the arithmetic mean of all vertices in the polygon. Any line
through the centroid divides the polygon with equal area.

DelaunayDelaunay TriangulationTriangulation

Computes the Delaunay triangulation of the specified points in the plane.


Inputs/Outputs

   •     X —

    X specifies the x-coordinates of the points in the plane. The length of X must be greater than or
    equal to 3.

   •      Y —

    Y specifies the y-coordinates of the points in the plane. The length of Y must equal the length of
     X.

   •       Triangles —

    Triangles returns an n-by-3 array, where nequals the number of triangles in the Delaunay
     triangulation. Each row of Triangles represents a triangle of the Delaunay triangulation, using
    the indexes of the input points (X, Y).

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 3999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:3999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4000 ordinal=4000 -->
## Functions

Functions

      Delaunay is a triangulation algorithm that meets the condition that no point is inside
       the circumcircle, which the points of the triangle determine. A unique Delaunay
       triangulation exists if no three points are on the same line and no four points are on
       the same circle.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Geometry\Voronoi and
        Delaunay Plot.vi

      VoronoiVoronoi DiagramDiagram

      Computes the Voronoi diagram of specified points in a plane.


      Inputs/Outputs

               •     X —

          X specifies the x-coordinates of the points in the plane. The length of X must be greater than or
            equal to 3.

               •      Y —

           Y specifies the y-coordinates of the points in the plane. The length of Y must equal the length of
              X.

               •      Voronoi X —

           Voronoi X returns the x-coordinates of Voronoi points.

               •      Voronoi Y —

           Voronoi Y returns the y-coordinates of Voronoi points.

               •      Voronoi Edges —

4000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4000 -->

