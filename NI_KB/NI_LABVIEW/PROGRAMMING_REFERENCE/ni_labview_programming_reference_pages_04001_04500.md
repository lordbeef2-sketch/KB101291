# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4001 ordinal=4001 -->
## Functions

Functions


    Voronoi Edges returns an n-by-2 array. nrepresents the number of edges in the Voronoi
    diagram. Each row of Voronoi Edges represents an edge of the Voronoi diagram that uses the
    indexes of Voronoi points.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


For ngiven points in the plane, the Voronoi diagram divides the plane into nVoronoi
cells. Each given point belongs to one Voronoi cell. The point in a Voronoi cell is closer
to the corresponding given point than to any of the other given points. The following
illustration shows an example of a Voronoi diagram of 8 given points.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Geometry\Voronoi and
   Delaunay Plot.vi

ConvexConvex HullHull

Computes the vertices of a convex polygon, which are the set of points that make up
the polygon that contains all the points.


                                                    © National Instruments 4001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4002 ordinal=4002 -->
## Functions

Functions


      Inputs/Outputs

               •     X —

          X specifies the x-coordinates of the points in the plane. The length of X must be greater than or
            equal to 3.

               •      Y —

           Y specifies the y-coordinates of the points in the plane. The length of Y must equal the length of
              X.

               •     Convex Hull —

          Convex Hull returns the indexes of the points that compose the convex hull. The first element in
          Convex Hull is the same as the last element so that the first and last elements form a closed
           convex hull.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The convex hull of a finite set of points is the smallest convex set that contains all
       points. In the following illustration, the convex hull is the line that connects the points.


      ConvexConvex PolygonPolygon IntersectionIntersection

      Computes the intersection of two convex polygons.

           If two polygons do not intersect, the VI returns empty arrays to Intersection X and


4002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4003 ordinal=4003 -->
## Functions

Functions

Intersection Y with no error.


Inputs/Outputs

   •     X 1 —

    X 1 specifies the x-coordinates of the vertices of the first polygon. The length of X 1 must be
    greater than or equal to 3.

   •      Y 1 —

    Y 1 specifies the y-coordinates of the vertices of the first polygon. The length of Y 1 must be
    equal to X 1.

   •     X 2 —

    X 2 specifies the x-coordinates of the vertices of the second polygon. The length of X 2 must be
    greater than or equal to 3.

   •      Y 2 —

    Y 2 specifies the y-coordinates of the vertices of the second polygon. The length of Y 2 must be
    equal to X 2.

   •       Intersection X —

    Intersection X returns the x-coordinates of the vertices of the intersection polygon.

   •       Intersection Y —

    Intersection Y returns the y-coordinates of the vertices of the intersection polygon.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The intersection of two convex polygons is the area contained in both polygons, as

                                                    © National Instruments 4003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4004 ordinal=4004 -->
## Functions

Functions

      shown in the following front panel.


     PolynomialPolynomial

      Use the Polynomial VIs to perform calculations and evaluations with polynomials.

      The VIs on this palette can return mathematics error codes.


         Palette Object  Description

       Add          Adds two polynomials P(x) and Q(x). The data types you wire to the P(x) and Q(x)
        Polynomials    inputs determine the polymorphic instance to use.


         Subtract        Subtracts polynomial Q(x) from polynomial P(x). The data types you wire to the
        Polynomials     P(x) and Q(x) inputs determine the polymorphic instance to use.


4004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4005 ordinal=4005 -->
## Functions

Functions


Palette Object  Description

Multiply         Multiplies polynomial P(x) by polynomial Q(x). The data types you wire to the P(x)
Polynomials    and Q(x) inputs determine the polymorphic instance to use.


Divide          Divides polynomial P(x) by polynomial Q(x). The data types you wire to the P(x)
Polynomials    and Q(x) inputs determine the polymorphic instance to use.


Polynomials    Computes the composition of polynomials P(x) and Q(x). The data types you wire
Composition    to the P(x) and Q(x) inputs determine the polymorphic instance to use.


             Computes the greatest common divisor for two polynomials P(x) and Q(x) withGCD of P(x)               the tolerance you specify. The data types you wire to the P(x) and Q(x) inputsand Q(x)
               determine the polymorphic instance to use.


             Computes the least common multiple of two polynomials P(x) and Q(x) with theLCM of P(x)                tolerance you specify. The data types you wire to the P(x) and Q(x) inputs
and Q(x)               determine the polymorphic instance to use.


nth Derivative   Calculates the nth order derivative of P(x). Wire data to the P(x) input to
of Polynomial   determine the polymorphic instance to use or manually select the instance.


Indefinite
                Calculates the indefinite integral of P(x). Wire data to the P(x) input to determine
Integral of
               the polymorphic instance to use or manually select the instance.
Polynomial


Integral of       Integrates the real polynomial P(x) over the interval a and b define. Integrating a
Polynomial     polynomial over an interval [a,b] is the same as calculating the definite integral of
over [a,b]       the polynomial.


Polynomial     Finds the roots of polynomial P(x). This VI removes leading coefficients of the
Roots          polynomial that are equal to zero. Wire data to the P(x) input to determine the


                                                    © National Instruments 4005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4006 ordinal=4006 -->
## Functions

Functions


         Palette Object  Description

                       polymorphic instance to use or manually select the instance.


        Polynomial                         Calculates the number of zeros of the real polynomial P(x) in a real interval         Real Zeros                        defined by start and end without determining the values of the zeros.        Counter

        Roots                            Classifies Roots into real, complex conjugate pair, and pure complex roots.          Classification


         Sort Complex   Sorts an array of complex numbers in ascending or descending order with respect
       Numbers       to real and imaginary parts or magnitude.


        Unique         Obtains all the unique numbers from the input array and determines the
       Numbers and    multiplicity of each unique number. Wire data to the Numbers input to determine
          Multiplicity     the polymorphic instance to use or manually select the instance.


         Create                         Creates polynomial P(x) from its roots. Wire data to the Roots input to determine        Polynomial                        the polymorphic instance to use or manually select the instance.
       From Roots


                    Removes from P(x) In the trailing coefficients near zero whose absolute values are       Remove Zero                            less than threshold. Wire data to the P(x) In input to determine the polymorphic          Coefficients                         instance to use or manually select the instance.


                        Finds the order, or polynomial degree, of polynomial P(x). Wire data to the P(x)
        Order of
                         input to determine the polymorphic instance to use or manually select the
        Polynomial
                          instance.


        Polynomial      Plots the evaluations of polynomial P(x). Wire data to the X input to determine the
         Plot           polymorphic instance to use or manually select the instance.


4006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4007 ordinal=4007 -->
## Functions

Functions


 Palette Object  Description

                Performs a linear evaluation on every element of X using the scale a and the offset
 Linear                  b. Wire data to the X input to determine the polymorphic instance to use or Evaluation               manually select the instance.


                 Evaluates the polynomial P(x) with a single value or multiple values. The data Polynomial                types you wire to the a and P(x) inputs determine the polymorphic instance to
 Evaluation                 use.


 Evaluate                 Evaluates the polynomial P(x) with matrix A. The data types you wire to the P(x) Polynomial              and A inputs determine the polymorphic instance to use. with Matrix


 Partial Fraction  Calculates the partial fraction expansion of a polynomial using the Heaviside
 Expansion      cover-up method.

 Create
 Polynomial     Uses partial fraction expansion to reconstruct a rational polynomial.
 From PFE

 Polynomial                Solves the polynomial eigenvalue problem. Wire data to the Input Matrices input Eigenvalues
                 to determine the polymorphic instance to use or manually select the instance. and Vectors

 Orthogonal &
 Non-          Use this class of polynomial functions to perform calculations and evaluations
 orthogonal     with orthogonal or non-orthogonal polynomials.
 Polynomials

 Rational       Use the Rational Polynomial VIs to perform calculations and evaluations with
 Polynomial      rational polynomials.


AddAdd PolynomialsPolynomials

Adds two polynomials P(x) and Q(x). The data types you wire to the P(x) and Q(x)
inputs determine the polymorphic instance to use.

                                                    © National Instruments 4007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4008 ordinal=4008 -->
## Functions

Functions


            • Add Polynomials (DBL) VI
            • Add Polynomials (CDB) VI

     AddAdd PolynomialsPolynomials (DBL)(DBL) VIVI

      Adds two polynomials P(x) and Q(x). The data types you wire to the P(x) and Q(x)
       inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •      Q(x) —

            Q(x) contains the real polynomial coefficients in ascending order of power.

               •      threshold —

            threshold specifies the level at which the VI removes from P(x)+Q(x) the trailing elements whose
            absolute values or relative values are less than or equal to threshold.

                    If all the elements in P(x)+Q(x) are less than or equal to threshold, P(x)+Q(x) returns a one-
           element array.

               •      threshold type —

            threshold type specifies how the VI removes the trailing elements from P(x)+Q(x). If threshold
           type is Absolute Value, the VI removes the trailing elements from P(x)+Q(x) whose absolute
            values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
               trailing elements from P(x)+Q(x) whose absolute values are less than or equal to threshold * |x|,
           where xis the coefficient which has the maximum absolute value in resulting polynomial.


4008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4009 ordinal=4009 -->
## Functions

Functions


    0   Absolute Value (default)
    1    Relative Value

   •      P(x)+Q(x) —

    P(x)+Q(x) returns the real coefficients for the sum polynomial in ascending order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


AddAdd PolynomialsPolynomials (CDB)(CDB) VIVI

Adds two polynomials P(x) and Q(x). The data types you wire to the P(x) and Q(x)
inputs determine the polymorphic instance to use.


Inputs/Outputs

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •      Q(x) —

    Q(x) contains the complex polynomial coefficients in ascending order of power.

   •      threshold —

    threshold specifies the level at which the VI removes from P(x)+Q(x) the trailing elements whose
    absolute values or relative values are less than or equal to threshold.

       If all the elements in P(x)+Q(x) are less than or equal to threshold, P(x)+Q(x) returns a one-
    element array.

   •      threshold type —

                                                    © National Instruments 4009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4010 ordinal=4010 -->
## Functions

Functions


            threshold type specifies how the VI removes the trailing elements from P(x)+Q(x). If threshold
           type is Absolute Value, the VI removes the trailing elements from P(x)+Q(x) whose absolute
            values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
               trailing elements from P(x)+Q(x) whose absolute values are less than or equal to threshold * |x|,
           where xis the coefficient which has the maximum absolute value in resulting polynomial.

           0   Absolute Value (default)
           1    Relative Value

               •      P(x)+Q(x) —

            P(x)+Q(x) returns the complex coefficients, in ascending order of power, of the polynomial that
              results from the addition of P(x) and Q(x).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

      SubtractSubtract PolynomialsPolynomials

       Subtracts polynomial Q(x) from polynomial P(x). The data types you wire to the P(x)
      and Q(x) inputs determine the polymorphic instance to use.


            • Subtract Polynomials (DBL) VI
            • Subtract Polynomials (CDB) VI

      SubtractSubtract PolynomialsPolynomials (DBL)(DBL) VIVI

       Subtracts polynomial Q(x) from polynomial P(x). The data types you wire to the P(x)
      and Q(x) inputs determine the polymorphic instance to use.


4010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4011 ordinal=4011 -->
## Functions

Functions


Inputs/Outputs

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power.

   •      Q(x) —

    Q(x) contains the real polynomial coefficients in ascending order of power.

   •      threshold —

    threshold specifies the level at which the VI removes from P(x)-Q(x) the trailing elements whose
    absolute values or relative values are less than or equal to threshold.

       If all the elements in P(x)-Q(x) are less than or equal to threshold, P(x)-Q(x) returns a one-
    element array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from P(x)-Q(x). If threshold
    type is Absolute Value, the VI removes the trailing elements from P(x)-Q(x) whose absolute
    values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
     trailing elements from P(x)-Q(x) whose absolute values are less than or equal to threshold * |x|,
    where xis the coefficient which has the maximum absolute value in resulting polynomial.

    0   Absolute Value (default)
    1    Relative Value

   •       P(x)-Q(x) —

    P(x)-Q(x) returns the real polynomial coefficients for the resulting polynomial in ascending order
     of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 4011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4012 ordinal=4012 -->
## Functions

Functions

      SubtractSubtract PolynomialsPolynomials (CDB)(CDB) VIVI

       Subtracts polynomial Q(x) from polynomial P(x). The data types you wire to the P(x)
      and Q(x) inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the complex polynomial coefficients in ascending order of power.

               •      Q(x) —

            Q(x) contains the complex polynomial coefficients in ascending order of power.

               •      threshold —

            threshold specifies the level at which the VI removes from P(x)-Q(x) the trailing elements whose
            absolute values or relative values are less than or equal to threshold.

                    If all the elements in P(x)-Q(x) are less than or equal to threshold, P(x)-Q(x) returns a one-
           element array.

               •      threshold type —

            threshold type specifies how the VI removes the trailing elements from P(x)-Q(x). If threshold
           type is Absolute Value, the VI removes the trailing elements from P(x)-Q(x) whose absolute
            values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
               trailing elements from P(x)-Q(x) whose absolute values are less than or equal to threshold * |x|,
           where xis the coefficient which has the maximum absolute value in resulting polynomial.

           0   Absolute Value (default)
           1    Relative Value

               •       P(x)-Q(x) —


4012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4013 ordinal=4013 -->
## Functions

Functions


    P(x)-Q(x) returns the complex polynomial coefficients for the resulting polynomial in ascending
    order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

MultiplyMultiply PolynomialsPolynomials

Multiplies polynomial P(x) by polynomial Q(x). The data types you wire to the P(x) and
Q(x) inputs determine the polymorphic instance to use.


  • Multiply Polynomials (DBL) VI
  • Multiply Polynomials (CDB) VI

MultiplyMultiply PolynomialsPolynomials (DBL)(DBL) VIVI

Multiplies polynomial P(x) by polynomial Q(x). The data types you wire to the P(x) and
Q(x) inputs determine the polymorphic instance to use.


Inputs/Outputs

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power.

   •      Q(x) —

    Q(x) contains the real polynomial coefficients in ascending order of power.


                                                    © National Instruments 4013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4014 ordinal=4014 -->
## Functions

Functions

               •      threshold —

            threshold specifies the level at which the VI removes from P(x)*Q(x) the trailing elements whose
            absolute values or relative values are less than or equal to threshold.

                    If all the elements in P(x)*Q(x) are less than or equal to threshold, P(x)*Q(x) returns a one-
           element array.

               •      threshold type —

            threshold type specifies how the VI removes the trailing elements from P(x)*Q(x). If threshold
           type is Absolute Value, the VI removes the trailing elements from P(x)*Q(x) whose absolute
            values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
               trailing elements from P(x)*Q(x) whose absolute values are less than or equal to threshold * |x|,
           where xis the coefficient which has the maximum absolute value in resulting polynomial.

           0   Absolute Value (default)
           1    Relative Value

               •       P(x)*Q(x) —

            P(x)*Q(x) returns the real coefficients for the product polynomial in ascending order of power.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       MultiplyMultiply PolynomialsPolynomials (CDB)(CDB) VIVI

        Multiplies polynomial P(x) by polynomial Q(x). The data types you wire to the P(x) and
       Q(x) inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •       P(x) —

4014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4015 ordinal=4015 -->
## Functions

Functions


    P(x) contains the complex polynomial coefficients in ascending order of power.

   •      Q(x) —

    Q(x) contains the complex polynomial coefficients in ascending order of power.

   •      threshold —

    threshold specifies the level at which the VI removes from P(x)*Q(x) the trailing elements whose
    absolute values or relative values are less than or equal to threshold.

       If all the elements in P(x)*Q(x) are less than or equal to threshold, P(x)*Q(x) returns a one-
    element array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from P(x)*Q(x). If threshold
    type is Absolute Value, the VI removes the trailing elements from P(x)*Q(x) whose absolute
    values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
     trailing elements from P(x)*Q(x) whose absolute values are less than or equal to threshold * |x|,
    where xis the coefficient which has the maximum absolute value in resulting polynomial.

    0   Absolute Value (default)
    1    Relative Value

   •       P(x)*Q(x) —

    P(x)*Q(x) returns the complex coefficients for the product polynomial in ascending order of
    power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

DivideDivide PolynomialsPolynomials

Divides polynomial P(x) by polynomial Q(x). The data types you wire to the P(x) and
Q(x) inputs determine the polymorphic instance to use.


                                                    © National Instruments 4015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4016 ordinal=4016 -->
## Functions

Functions


            • Divide Polynomials (DBL) VI
            • Divide Polynomials (CDB) VI

       DivideDivide PolynomialsPolynomials (DBL)(DBL) VIVI

       Divides polynomial P(x) by polynomial Q(x). The data types you wire to the P(x) and
       Q(x) inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the real coefficients for the dividend polynomial in ascending order of power.

               •      Q(x) —

            Q(x) contains the real coefficients for the divisor polynomial in ascending order of power.

               •      threshold —

            threshold specifies the level at which the VI removes from P(x)/Q(x) the trailing elements whose
            absolute values or relative values are less than or equal to threshold.

                    If all the elements in P(x)/Q(x) are less than or equal to threshold, P(x)/Q(x) returns a one-
           element array.

               •      threshold type —

            threshold type specifies how the VI removes the trailing elements from P(x)/Q(x). If threshold
           type is Absolute Value, the VI removes the trailing elements from P(x)/Q(x) whose absolute
            values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
               trailing elements from P(x)/Q(x) whose absolute values are less than or equal to threshold *|x|,
           where xis the coefficient which has the maximum absolute value in resulting polynomial.


4016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4017 ordinal=4017 -->
## Functions

Functions


    0   Absolute Value (default)
    1    Relative Value

   •       P(x)/Q(x) —

    P(x)/Q(x) returns the real coefficients for the quotient polynomial in ascending order of power.

   •     Remainder —

    Remainder returns the real coefficients for the remainder polynomial in ascending order of
    power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


DivideDivide PolynomialsPolynomials (CDB)(CDB) VIVI

Divides polynomial P(x) by polynomial Q(x). The data types you wire to the P(x) and
Q(x) inputs determine the polymorphic instance to use.


Inputs/Outputs

   •       P(x) —

    P(x) contains the complex coefficients for the dividend polynomial in ascending order of power.

   •      Q(x) —

    Q(x) contains the complex coefficients for the divisor polynomial in ascending order of power.

   •      threshold —

    threshold specifies the level at which the VI removes from P(x)/Q(x) the trailing elements whose


                                                    © National Instruments 4017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4018 ordinal=4018 -->
## Functions

Functions


            absolute values or relative values are less than or equal to threshold.

                    If all the elements in P(x)/Q(x) are less than or equal to threshold, P(x)/Q(x) returns a one-
           element array.

               •      threshold type —

            threshold type specifies how the VI removes the trailing elements from P(x)/Q(x). If threshold
           type is Absolute Value, the VI removes the trailing elements from P(x)/Q(x) whose absolute
            values are less than or equal to threshold. If threshold type is Relative Value, the VI removes the
               trailing elements from P(x)/Q(x) whose absolute values are less than or equal to threshold *|x|,
           where xis the coefficient which has the maximum absolute value in resulting polynomial.

           0   Absolute Value (default)
           1    Relative Value

               •       P(x)/Q(x) —

             P(x)/Q(x) returns the complex coefficients for the quotient polynomial in ascending order of
            power.

               •     Remainder —

          Remainder returns the complex coefficients for the remainder polynomial in ascending order of
            power.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

     PolynomialsPolynomials CompositionComposition

      Computes the composition of polynomials P(x) and Q(x). The data types you wire to
       the P(x) and Q(x) inputs determine the polymorphic instance to use.


4018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4019 ordinal=4019 -->
## Functions

Functions

   • Polynomials Composition (DBL) VI
   • Polynomials Composition (CDB) VI

The following polynomial defines the nth order polynomial described by the (n+ 1)
element array P[0…n]:


The following polynomial defines the mth order polynomial described by the (m+ 1)
element array Q[0…m]:


The VI uses the following equation to compose P(x) and Q(x):

                                        – 1P(Q(x)) = P[n](Q[m]xm + Q[m– 1]xm  + … + Q[1]x+ Q[0])n + P[n– 1](Q[m]xm +
Q[m– 1]xm– 1 + … + Q[1]x+ Q[0])n– 1 + … + P[1](Q[m]xm + Q[m– 1]xm– 1 + … +
Q[1]x+ Q[0]) + P[0]
PolynomialsPolynomials CompositionComposition (DBL)(DBL) VIVI

Computes the composition of polynomials P(x) and Q(x). The data types you wire to
the P(x) and Q(x) inputs determine the polymorphic instance to use.


Inputs/Outputs

   •       P(x) —

     P(x) contains the real polynomial coefficients in ascending order of power.

   •      Q(x) —


                                                    © National Instruments 4019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4020 ordinal=4020 -->
## Functions

Functions


            Q(x) contains the real polynomial coefficients in ascending order of power.

               •      threshold —

            threshold specifies the level at which the VI removes from P(Q(x)) the trailing elements whose
            absolute values or relative values are less than or equal to threshold.

                    If all the elements in P(Q(x)) are less than or equal to threshold, P(Q(x)) returns a one-element
              array.

               •      threshold type —

            threshold type specifies how the VI removes the trailing elements from P(Q(x)). If threshold
           type is Absolute Value, the VI removes the trailing elements from P(Q(x)) whose absolute values
            are less than or equal to threshold. If threshold type is Relative Value, the VI removes the trailing
           elements from P(Q(x)) whose absolute values are less than or equal to threshold * |x|, where x
                is the coefficient which has the maximum absolute value in resulting polynomial.

           0   Absolute Value (default)
           1    Relative Value

               •       P(Q(x)) —

             P(Q(x)) returns the real polynomial coefficients, in ascending order of power, for the polynomial
             that results from composing P(x) and Q(x).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following polynomial defines the nth order polynomial described by the (n+ 1)
      element array P[0…n]:


      The following polynomial defines the mth order polynomial described by the (m+ 1)
      element array Q[0…m]:


4020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4021 ordinal=4021 -->
## Functions

Functions


The VI uses the following equation to compose P(x) and Q(x):

                                        – 1P(Q(x)) = P[n](Q[m]xm + Q[m– 1]xm  + … + Q[1]x+ Q[0])n + P[n– 1](Q[m]xm +
Q[m– 1]xm– 1 + … + Q[1]x+ Q[0])n– 1 + … + P[1](Q[m]xm + Q[m– 1]xm– 1 + … +
Q[1]x+ Q[0]) + P[0]
PolynomialsPolynomials CompositionComposition (CDB)(CDB) VIVI

Computes the composition of polynomials P(x) and Q(x). The data types you wire to
the P(x) and Q(x) inputs determine the polymorphic instance to use.


Inputs/Outputs

   •       P(x) —

     P(x) contains the complex polynomial coefficients in ascending order of power.

   •      Q(x) —

    Q(x) contains the complex polynomial coefficients in ascending order of power.

   •      threshold —

    threshold specifies the level at which the VI removes from P(Q(x)) the trailing elements whose
    absolute values or relative values are less than or equal to threshold.

       If all the elements in P(Q(x)) are less than or equal to threshold, P(Q(x)) returns a one-element
     array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from P(Q(x)). If threshold
    type is Absolute Value, the VI removes the trailing elements from P(Q(x)) whose absolute values


                                                    © National Instruments 4021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4022 ordinal=4022 -->
## Functions

Functions


            are less than or equal to threshold. If threshold type is Relative Value, the VI removes the trailing
           elements from P(Q(x)) whose absolute values are less than or equal to threshold * |x|, where x
                is the coefficient which has the maximum absolute value in resulting polynomial.

           0   Absolute Value (default)
           1    Relative Value

               •       P(Q(x)) —

             P(Q(x)) returns the complex polynomial coefficients, in ascending order of power, for the
            polynomial that results from composing P(x) and Q(x).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following polynomial defines the nth order polynomial described by the (n+ 1)
      element array P[0…n]:


      The following polynomial defines the mth order polynomial described by the (m+ 1)
      element array Q[0…m]:


      The VI uses the following equation to compose P(x) and Q(x):

                                                – 1       P(Q(x)) = P[n](Q[m]xm + Q[m– 1]xm  + … + Q[1]x+ Q[0])n + P[n– 1](Q[m]xm +
    Q[m– 1]xm– 1 + … + Q[1]x+ Q[0])n– 1 + … + P[1](Q[m]xm + Q[m– 1]xm– 1 + … +
      Q[1]x+ Q[0]) + P[0]


4022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4023 ordinal=4023 -->
## Functions

Functions

GCDGCD ofof P(x)P(x) andand Q(x)Q(x)

Computes the greatest common divisor for two polynomials P(x) and Q(x) with the
tolerance you specify. The data types you wire to the P(x) and Q(x) inputs determine
the polymorphic instance to use.


  • GCD of P(x) and Q(x) (DBL) VI
  • GCD of P(x) and Q(x) (CDB) VI

GCDGCD ofof P(x)P(x) andand Q(x)Q(x) (DBL)(DBL) VIVI

Computes the greatest common divisor for two polynomials P(x) and Q(x) with the
tolerance you specify. The data types you wire to the P(x) and Q(x) inputs determine
the polymorphic instance to use.


Inputs/Outputs

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power.

   •      Q(x) —

    Q(x) contains the real polynomial coefficients in ascending order of power.

   •      tolerance —

    tolerance specifies the numerical threshold to use for the calculation.

   •      algorithm —

    algorithm specifies the algorithm this VI uses to compute the polynomial greatest common


                                                    © National Instruments 4023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4024 ordinal=4024 -->
## Functions

Functions


               divisor.

            Euclidean (0) is the classical method for polynomial GCD calculation. Approximate GCD (1) is
          more suitable in calculating the GCD of one polynomial and its derivative.

           0     Euclidean (default)
           1    Approximate GCD

               •      Greatest Common Divisor —

            Greatest Common Divisor returns the greatest common divisor of P(x) and Q(x).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     GCDGCD ofof P(x)P(x) andand Q(x)Q(x) (CDB)(CDB) VIVI

      Computes the greatest common divisor for two polynomials P(x) and Q(x) with the
       tolerance you specify. The data types you wire to the P(x) and Q(x) inputs determine
       the polymorphic instance to use.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the complex polynomial coefficients in ascending order of power.

               •      Q(x) —

            Q(x) contains the complex polynomial coefficients in ascending order of power.

               •      tolerance —


4024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4025 ordinal=4025 -->
## Functions

Functions


    tolerance specifies the numerical threshold to use for the calculation.

   •      algorithm —

    algorithm specifies the algorithm this VI uses to compute the polynomial greatest common
     divisor.

    Euclidean (0) is the classical method for polynomial GCD calculation. Approximate GCD (1) is
   more suitable in calculating the GCD of one polynomial and its derivative.

    0     Euclidean (default)
    1    Approximate GCD

   •      Greatest Common Divisor —

    Greatest Common Divisor returns the greatest common divisor of P(x) and Q(x).

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

LCMLCM ofof P(x)P(x) andand Q(x)Q(x)

Computes the least common multiple of two polynomials P(x) and Q(x) with the
tolerance you specify. The data types you wire to the P(x) and Q(x) inputs determine
the polymorphic instance to use.


  • LCM of P(x) and Q(x) (DBL) VI
  • LCM of P(x) and Q(x) (CDB) VI

LCMLCM ofof P(x)P(x) andand Q(x)Q(x) (DBL)(DBL) VIVI

Computes the least common multiple of two polynomials P(x) and Q(x) with the
tolerance you specify. The data types you wire to the P(x) and Q(x) inputs determine


                                                    © National Instruments 4025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4026 ordinal=4026 -->
## Functions

Functions

       the polymorphic instance to use.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •      Q(x) —

            Q(x) contains the real polynomial coefficients in ascending order of power.

               •      tolerance —

            tolerance specifies the numerical threshold to use for the calculation.

               •      algorithm —

            algorithm specifies the algorithm this VI uses to compute the polynomial least common
             multiple.

            Euclidean (0) is the classical method for polynomial LCM calculation. Approximate GCD (1) is
          more suitable in calculating the LCM of one polynomial and its derivative.

           0     Euclidean (default)
           1    Approximate GCD

               •      Least Common Multiple —

            Least Common Multiple returns the least common multiple of P(x) and Q(x).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4027 ordinal=4027 -->
## Functions

Functions

LCMLCM ofof P(x)P(x) andand Q(x)Q(x) (CDB)(CDB) VIVI

Computes the least common multiple of two polynomials P(x) and Q(x) with the
tolerance you specify. The data types you wire to the P(x) and Q(x) inputs determine
the polymorphic instance to use.


Inputs/Outputs

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •      Q(x) —

    Q(x) contains the complex polynomial coefficients in ascending order of power.

   •      tolerance —

    tolerance specifies the numerical threshold to use for the calculation.

   •      algorithm —

    algorithm specifies the algorithm this VI uses to compute the polynomial least common
     multiple.

    Euclidean (0) is the classical method for polynomial LCM calculation. Approximate GCD (1) is
   more suitable in calculating the LCM of one polynomial and its derivative.

    0     Euclidean (default)
    1    Approximate GCD

   •      Least Common Multiple —

    Least Common Multiple returns the least common multiple of P(x) and Q(x).

   •       error —


                                                    © National Instruments 4027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4028 ordinal=4028 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

     nthnth DerivativeDerivative ofof PolynomialPolynomial

       Calculates the nth order derivative of P(x). Wire data to the P(x) input to determine the
      polymorphic instance to use or manually select the instance.


            • nth Derivative of Polynomial (DBL) VI
            • nth Derivative of Polynomial (CDB) VI

      nthnth DerivativeDerivative ofof PolynomialPolynomial (DBL)(DBL) VIVI

       Calculates the nth order derivative of P(x). Wire data to the P(x) input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •      order —

            order specifies the derivative order to calculate. If order is less than zero, the VI sets Nth
             Derivative of P(x) to an empty array and returns an error.

               •     Nth Derivative of P(x) —

          Nth Derivative of P(x) returns the real coefficients for the nth derivative of P(x) in ascending


4028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4029 ordinal=4029 -->
## Functions

Functions


    order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


nthnth DerivativeDerivative ofof PolynomialPolynomial (CDB)(CDB) VIVI

Calculates the nth order derivative of P(x). Wire data to the P(x) input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •      order —

    order specifies the derivative order to calculate. If order is less than zero, the VI sets Nth
    Derivative of P(x) to an empty array and returns an error.

   •     Nth Derivative of P(x) —

    Nth Derivative of P(x) returns the complex coefficients for the nth derivative of P(x) in ascending
    order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 4029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4030 ordinal=4030 -->
## Functions

Functions

      IndefiniteIndefinite IntegralIntegral ofof PolynomialPolynomial

       Calculates the indefinite integral of P(x). Wire data to the P(x) input to determine the
      polymorphic instance to use or manually select the instance.


            • Indefinite Integral of Polynomial (DBL) VI
            • Indefinite Integral of Polynomial (CDB) VI

       IndefiniteIndefinite IntegralIntegral ofof PolynomialPolynomial (DBL)(DBL) VIVI

       Calculates the indefinite integral of P(x). Wire data to the P(x) input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •       Indefinite Integral of P(x) —

             Indefinite Integral of P(x) returns the real polynomial coefficients of the indefinite integral of
             P(x) in ascending order of power.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       IndefiniteIndefinite IntegralIntegral ofof PolynomialPolynomial (CDB)(CDB) VIVI

       Calculates the indefinite integral of P(x). Wire data to the P(x) input to determine the

4030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4031 ordinal=4031 -->
## Functions

Functions

polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •       Indefinite Integral of P(x) —

     Indefinite Integral of P(x) returns the complex polynomial coefficients of the indefinite integral
     of P(x) in ascending order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

IntegralIntegral ofof PolynomialPolynomial overover [a,b][a,b]

Integrates the real polynomial P(x) over the interval a and b define. Integrating a
polynomial over an interval [a,b] is the same as calculating the definite integral of the
polynomial.


Inputs/Outputs

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power.

   •      a —


                                                    © National Instruments 4031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4032 ordinal=4032 -->
## Functions

Functions


           a specifies the leftmost point of the integral interval. The default is 0.

               •     b —

          b specifies the rightmost point of the integral interval. The default is 0.

               •       integral of P(x) —

             integral of P(x) returns the integral of P(x) over [a,b].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

     PolynomialPolynomial RootsRoots

       Finds the roots of polynomial P(x). This VI removes leading coefficients of the
      polynomial that are equal to zero. Wire data to the P(x) input to determine the
      polymorphic instance to use or manually select the instance.


            • Polynomial Roots (DBL) VI
            • Polynomial Roots (CDB) VI

      PolynomialPolynomial RootsRoots (DBL)(DBL) VIVI

       Finds the roots of polynomial P(x). This VI removes leading coefficients of the
      polynomial that are equal to zero. Wire data to the P(x) input to determine the
      polymorphic instance to use or manually select the instance.


4032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4033 ordinal=4033 -->
## Functions

Functions

Inputs/Outputs

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power. P(x) cannot equal 0.

   •      option —

    option specifies the option for root finding. The default is Simple Classification.

     General—Specifies that the real polynomial P(x) is regarded as a complex polynomial. Roots    0     might not be exact real or complex conjugate.
     Simple Classification—Based on the results of the General option, the roots are divided into
    1 two kinds: real (remove the imaginary part) or complex conjugate (average the real parts and
     imaginary parts respectively).
     Refinement—Based on the results of the Simple Classification option, the roots are refined
     again by the Newton method for real roots and the Bairstow method for complex conjugate
    2      roots. With this option the Roots can be more accurate, but the computation might be
      numerically unstable.
     Advanced Refinement—Finds the roots more accurately and stably, especially when the
    3 polynomial has repeated roots. The resulting roots are exact real or complex conjugate. Due to
     the computation complexity, this method is time-consuming.

   •      Roots —

    Roots returns the real and complex conjugate roots of P(x).

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


PolynomialPolynomial RootsRoots (CDB)(CDB) VIVI

Finds the roots of polynomial P(x). This VI removes leading coefficients of the
polynomial that are equal to zero. Wire data to the P(x) input to determine the
polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4034 ordinal=4034 -->
## Functions

Functions

      Inputs/Outputs

               •       P(x) —

             P(x) contains the complex polynomial coefficients in ascending order of power.

               •      option —

            option specifies the option for root finding. The default is General.

            General—Performs the Newton-based method to find the roots. This root-finding method is           0                fast but has low precision.
            Advanced Refinement—Finds the roots more accurately and stably, especially when the
           3 polynomial has repeated roots. Due to the computation complexity, this method is time-
            consuming.

               •      Roots —

           Roots returns the complex roots of P(x).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

     PolynomialPolynomial RealReal ZerosZeros CounterCounter

       Calculates the number of zeros of the real polynomial P(x) in a real interval defined by
        start and end without determining the values of the zeros.


      Inputs/Outputs

               •       P(x) —

             P(x) is an array that represents the polynomial. The first element of this array relates to the
            constant coefficient of P(x).


4034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4035 ordinal=4035 -->
## Functions

Functions

   •       start —

     start is the leftmost point of the interval. The default is 0.0.

   •     end —

    end is the rightmost point of the interval. The default is 0.0.

   •     number of zeros —

   number of zeros is the exact number of zeros of P(x) in the interval (start, end).

   •       error —

     error returns any error or warning from the VI. When start > end, the application interprets it as
    an error. You can wire error to the Error Cluster From Error Code VI to convert the error code or
    warning into an error cluster.


This VI uses the Sturm algorithm to calculate the number of zeros. The Sturm
algorithm deals with two situations. Let p(x) be a real polynomial in xand let p'(x) be
the derivative of p(x). If d(x) denotes the greatest common divisor of p(x) and p'(x),

d(x) = gcd(p(x), p´(x))

so p(x) has multiple zeros, if d(x) is a nonconstant polynomial. In other words, the
polynomial p(x)/d(x) has only single zeros.

Repeating this idea, you can combine the polynomial p(x) as the product of simple
polynomials, each of which has single real zeros. The number of zeros of p(x) is equal
to the sum of all zeros of the defined simple polynomials that have only single zeros.

To determine the number of zeros of a real polynomial p(x) with the single zero
property, use the following Euclidean algorithm:

                                           ⋮p(x) = q1(x)p1(x) – p2(x) p1(x) = q2(x)p2(x) – p3(x)                                   pr– 2(x) = qr– 1(x)pr– 1(x) – pr(x)

The Sturm's chain

(p(x), p1(x), …, pr(x))

                                                    © National Instruments 4035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4036 ordinal=4036 -->
## Functions

Functions

      determines two values W(start) and W(end). W(x) is the number of sign changes of the
       chain

        (p(x), p1(x), …, pr(x))

      The number of all zeros of p(x) is exactly equal to W(end)–W(start).

           Note

                       If you are interested in all real zeros of a real polynomial, choose

                start = –max{(|a0| + … + |an–1|)/|an|, 1}

            and end = max{(|a0| + … + |an–1|)/|an|, 1}

            where a0, a1, …, an are the elements of the polynomial.

     RootsRoots ClassificationClassification

        Classifies Roots into real, complex conjugate pair, and pure complex roots.


      Inputs/Outputs

               •      Roots —

           Roots contains the complex roots for a polynomial.

               •      tolerance for real roots —

            tolerance for real roots specifies the tolerance for classifying real roots. If the imaginary part of a
           complex root is less than or equal to tolerance for real roots, the VI classifies the complex root
            as a real root.


4036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4037 ordinal=4037 -->
## Functions

Functions


    The complex root (a2 + b2i) is a real root if the following relationship is true. |b2| ≤ tolerance for
     real roots

   •      tolerance for conjugate pair —

    tolerance for conjugate pair specifies the tolerance for classifying complex conjugate pairs.

    The VI classifies the complex roots Z0 and Z1 as a complex conjugate pair if the following
     relationship is true. |(Z0 – Z1)/Z0| ≤ tolerance for conjugate pair

   •      Real Roots —

    Real Roots returns the real roots.

   •     Complex Pair Roots —

    Complex Pair Roots returns the complex conjugate pair roots.

   •      Pure Complex Roots —

    Pure Complex Roots returns the pure complex roots.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

SortSort ComplexComplex NumbersNumbers

Sorts an array of complex numbers in ascending or descending order with respect to
real and imaginary parts or magnitude.


Inputs/Outputs

   •     Complex Numbers —


                                                    © National Instruments 4037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4038 ordinal=4038 -->
## Functions

Functions


          Complex Numbers contains the complex numbers to sort.

               •      order —

            order specifies in what order the VI sorts Complex Numbers.

                    Ascending           0                        (default)
           1       Descending

               •     method —

          method specifies the sorting criteria.

                    If you set method to Magnitude, Real, Imaginary, the VI sorts elements with respect to their
           magnitude first. For the elements with the same magnitude, the VI sorts them with respect to
              their real parts and then with respect to their imaginary parts.

             Real & Imaginary (default)—The VI sorts the elements with respect to their real parts first. For           0             the elements with same real parts, the VI sorts them by their imaginary parts.
            Magnitude, Real, Imaginary—The VI sorts the elements with respect to their magnitude first.
           1 For the elements with same magnitude, the VI sorts them by their real parts and then by their
             imaginary parts.
            Magnitude, Phase Angle—The VI sorts the elements with respect to their magnitude first. For
           2 the elements with same magnitude, the VI sorts them by their phase angle. The phase angle is
               in the ranges of negative pi to pi.

               •      Sorted Complex Numbers —

           Sorted Complex Numbers returns the complex numbers sorted according to order.

               •      Sorted Index —

           Sorted Index returns for each element of Sorted Complex Numbers the corresponding index in
          Complex Numbers.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4039 ordinal=4039 -->
## Functions

Functions

UniqueUnique NumbersNumbers andand MultiplicityMultiplicity

Obtains all the unique numbers from the input array and determines the multiplicity of
each unique number. Wire data to the Numbers input to determine the polymorphic
instance to use or manually select the instance.


  • Unique Numbers and Multiplicity (DBL) VI
  • Unique Numbers and Multiplicity (CDB) VI

UniqueUnique NumbersNumbers andand MultiplicityMultiplicity (DBL)(DBL) VIVI

Obtains all the unique numbers from the input array and determines the multiplicity of
each unique number. Wire data to the Numbers input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •     Numbers —

   Numbers is an array of real numbers.

   •      Unique Numbers —

    Unique Numbers returns all the unique numbers in Numbers. The nth element of Unique
   Numbers has multiplicity given by the nth element of Multiplicity.

   •       Multiplicity —

     Multiplicity returns the number of occurrences of each unique number in Numbers. The nth
    element of Multiplicity corresponds to the nth element of Unique Numbers.

   •       error —


                                                    © National Instruments 4039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4040 ordinal=4040 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      UniqueUnique NumbersNumbers andand MultiplicityMultiplicity (CDB)(CDB) VIVI

       Obtains all the unique numbers from the input array and determines the multiplicity of
      each unique number. Wire data to the Numbers input to determine the polymorphic
       instance to use or manually select the instance.


      Inputs/Outputs

               •     Complex Numbers —

          Complex Numbers is an array of complex numbers.

               •      Unique Complex Numbers —

           Unique Complex Numbers returns all the unique numbers in Complex Numbers. The nth
           element of Unique Complex Numbers has multiplicity given by the nth element of Multiplicity.

               •       Multiplicity —

              Multiplicity returns the number of occurrences of each unique number in Complex Numbers.
          The nth element of Multiplicity corresponds to the nth element of Unique Complex Numbers.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

      CreateCreate PolynomialPolynomial FromFrom RootsRoots

       Creates polynomial P(x) from its roots. Wire data to the Roots input to determine the
      polymorphic instance to use or manually select the instance.

4040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4041 ordinal=4041 -->
## Functions

Functions


  • Create Polynomial From Roots (DBL) VI
  • Create Polynomial From Roots (CDB) VI

The VI uses the following equation to create P(x):

                                               – 1P(x) = (x– r1)(x– r2)…(x– rn) = xn + Pn– 1xn  + … + P1x+ P0
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Polynomial\Create Polynomial
   from Roots of Unity.vi

CreateCreate PolynomialPolynomial FromFrom RootsRoots (DBL)(DBL) VIVI

Creates polynomial P(x) from its roots. Wire data to the Roots input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •      Roots —

    Roots contains the real roots for a polynomial. If Roots is empty, the VI sets P(x) to 1.

   •       P(x) —

    P(x) returns the real polynomial coefficients in ascending order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error


                                                    © National Instruments 4041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4042 ordinal=4042 -->
## Functions

Functions


          Code VI to convert the error code or warning into an error cluster.


      The VI uses the following equation to create P(x):

                                                       – 1       P(x) = (x– r1)(x– r2)…(x– rn) = xn + Pn– 1xn  + … + P1x+ P0
     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Polynomial\Create Polynomial
        from Roots of Unity.vi

      CreateCreate PolynomialPolynomial FromFrom RootsRoots (CDB)(CDB) VIVI

       Creates polynomial P(x) from its roots. Wire data to the Roots input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Roots —

           Roots contains the complex roots for a polynomial. If Roots is empty, the VI sets P(x) to 1.

               •       P(x) —

             P(x) returns the complex polynomial coefficients in ascending order of power.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI uses the following equation to create P(x):

4042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4043 ordinal=4043 -->
## Functions

Functions


                                               – 1P(x) = (x– r1)(x– r2)…(x– rn) = xn + Pn– 1xn  + … + P1x+ P0
Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Polynomial\Create Polynomial
   from Roots of Unity.vi

RemoveRemove ZeroZero CoefficientsCoefficients

Removes from P(x) In the trailing coefficients near zero whose absolute values are less
than threshold. Wire data to the P(x) In input to determine the polymorphic instance
to use or manually select the instance.


  • Remove Zero Coefficients (DBL) VI
  • Remove Zero Coefficients (CDB) VI

RemoveRemove ZeroZero CoefficientsCoefficients (DBL)(DBL) VIVI

Removes from P(x) In the trailing coefficients near zero whose absolute values are less
than threshold. Wire data to the P(x) In input to determine the polymorphic instance
to use or manually select the instance.


Inputs/Outputs

   •       P(x) In —

    P(x) In contains the real polynomial coefficients in ascending order of power.

   •      threshold —


                                                    © National Instruments 4043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4044 ordinal=4044 -->
## Functions

Functions


            threshold specifies the level at which the VI removes from P(x) In the trailing elements whose
            absolute values or relative values are less than or equal to threshold. If all the elements in P(x)
             In are less than or equal to threshold, P(x) Out returns a one-element array that contains the
                 first element of P(x) In.

               •      threshold type —

            threshold type specifies how the VI removes the trailing elements from P(x) In. If threshold type
                is Absolute Value, the VI removes the trailing elements from P(x) In whose absolute values are
              less than or equal to threshold. If threshold type is Relative Value, the VI removes the trailing
           elements from P(x) In whose absolute values are less than or equal to threshold * |x|, where xis
            the coefficient which has the maximum absolute value in P(x) In.

           0   Absolute Value (default)
           1    Relative Value

               •       P(x) Out —

             P(x) Out returns the result of removing the trailing coefficients near zero from P(x) In.

               •     number of zero coefficients —

          number of zero coefficients returns the number of trailing near-zero coefficients that LabVIEW
           removed.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     RemoveRemove ZeroZero CoefficientsCoefficients (CDB)(CDB) VIVI

      Removes from P(x) In the trailing coefficients near zero whose absolute values are less
      than threshold. Wire data to the P(x) In input to determine the polymorphic instance
       to use or manually select the instance.


4044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4045 ordinal=4045 -->
## Functions

Functions

Inputs/Outputs

   •       P(x) In —

    P(x) In contains the complex polynomial coefficients in ascending order of power.

   •      threshold —

    threshold specifies the level at which the VI removes from P(x) In the trailing elements whose
    absolute values or relative values are less than or equal to threshold. If all the elements in P(x)
     In are less than or equal to threshold, P(x) Out returns a one-element array that contains the
      first element of P(x) In.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from P(x) In. If threshold type
      is Absolute Value, the VI removes the trailing elements from P(x) In whose absolute values are
     less than or equal to threshold. If threshold type is Relative Value, the VI removes the trailing
    elements from P(x) In whose absolute values are less than or equal to threshold * |x|, where xis
    the coefficient which has the maximum absolute value in P(x) In.

    0   Absolute Value (default)
    1    Relative Value

   •       P(x) Out —

    P(x) Out returns the result of removing the trailing coefficients near zero from P(x) In.

   •     number of zero coefficients —

   number of zero coefficients returns the number of trailing near-zero coefficients that LabVIEW
    removed.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

OrderOrder ofof PolynomialPolynomial

Finds the order, or polynomial degree, of polynomial P(x). Wire data to the P(x) input
to determine the polymorphic instance to use or manually select the instance.

                                                    © National Instruments 4045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4046 ordinal=4046 -->
## Functions

Functions


            • Order of Polynomial (DBL) VI
            • Order of Polynomial (CDB) VI

      OrderOrder ofof PolynomialPolynomial (DBL)(DBL) VIVI

       Finds the order, or polynomial degree, of polynomial P(x). Wire data to the P(x) input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •      order —

            order returns the highest order power, or polynomial degree, of P(x).

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      OrderOrder ofof PolynomialPolynomial (CDB)(CDB) VIVI

       Finds the order, or polynomial degree, of polynomial P(x). Wire data to the P(x) input
       to determine the polymorphic instance to use or manually select the instance.


4046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4047 ordinal=4047 -->
## Functions

Functions

Inputs/Outputs

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •      order —

    order returns the highest order power, or polynomial degree, of P(x).

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

PolynomialPolynomial PlotPlot

Plots the evaluations of polynomial P(x). Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


  • Polynomial Plot (Samples) VI
  • Polynomial Plot (Range) VI

PolynomialPolynomial PlotPlot (Samples)(Samples) VIVI

Plots the evaluations of polynomial P(x). Wire data to the X input to determine the
polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —


                                                    © National Instruments 4047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4048 ordinal=4048 -->
## Functions

Functions


          X is the input data to be used in the polynomial evaluation.

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •      polynomial plot —

           polynomial plot displays the evaluations of P(x) as an XY graph.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      PolynomialPolynomial PlotPlot (Range)(Range) VIVI

       Plots the evaluations of polynomial P(x). Wire data to the X input to determine the
      polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      samples —

           samples is the number of values of x between start and end for which to evaluate P(x). The
             default is 100.

           samples must be greater than or equal to 2.

               •       start —

              start is the first value of x for which to evaluate P(x). The default is 0.

               •     end —

          end is the last value of x for which to evaluate P(x). The default is 1.


4048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4049 ordinal=4049 -->
## Functions

Functions

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power.

   •      polynomial plot —

    polynomial plot displays the evaluations of P(x) as an XY graph.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

LinearLinear EvaluationEvaluation

Performs a linear evaluation on every element of X using the scale a and the offset b.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


  • 1D Linear Evaluation (DBL) VI
  • 1D Linear Evaluation (CDB) VI
  • 2D Linear Evaluation (DBL) VI
  • 2D Linear Evaluation (CDB) VI

1D1D LinearLinear EvaluationEvaluation (DBL)(DBL) VIVI

Performs a linear evaluation on every element of X using the scale a and the offset b.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


                                                    © National Instruments 4049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4050 ordinal=4050 -->
## Functions

Functions

      Inputs/Outputs

               •     X —

          X contains the real values to evaluate.

               •      a —

           a specifies the multiplicative constant.

               •     b —

          b specifies the additive constant.

               •       Y[i]=X[i]*a+b —

             Y[i]=X[i]*a+b returns the result of the linear evaluation of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D1D LinearLinear EvaluationEvaluation (CDB)(CDB) VIVI

      Performs a linear evaluation on every element of X using the scale a and the offset b.
       Wire data to the X input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •     X —

          X contains the complex values to evaluate.

               •      a —


4050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4051 ordinal=4051 -->
## Functions

Functions


    a specifies the multiplicative constant.

   •     b —

   b specifies the additive constant.

   •       Y[i]=X[i]*a+b —

     Y[i]=X[i]*a+b returns the result of the linear evaluation of X.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


2D2D LinearLinear EvaluationEvaluation (DBL)(DBL) VIVI

Performs a linear evaluation on every element of X using the scale a and the offset b.
Wire data to the X input to determine the polymorphic instance to use or manually
select the instance.


Inputs/Outputs

   •     X —

    X contains the real values to evaluate.

   •      a —

    a specifies the multiplicative constant.

   •     b —

   b specifies the additive constant.

   •       Y[i,j]=X[i,j]*a+b —


                                                    © National Instruments 4051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4052 ordinal=4052 -->
## Functions

Functions


              Y[i,j]=X[i,j]*a+b returns the result of the linear evaluation of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D2D LinearLinear EvaluationEvaluation (CDB)(CDB) VIVI

      Performs a linear evaluation on every element of X using the scale a and the offset b.
       Wire data to the X input to determine the polymorphic instance to use or manually
        select the instance.


      Inputs/Outputs

               •     X —

          X contains the complex values to evaluate.

               •      a —

           a specifies the multiplicative constant.

               •     b —

          b specifies the additive constant.

               •       Y[i,j]=X[i,j]*a+b —

              Y[i,j]=X[i,j]*a+b returns the result of the linear evaluation of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4053 ordinal=4053 -->
## Functions

Functions

PolynomialPolynomial EvaluationEvaluation

Evaluates the polynomial P(x) with a single value or multiple values. The data types
you wire to the a and P(x) inputs determine the polymorphic instance to use.


  • Scalar Polynomial Evaluation (DBL) VI
  • Scalar Polynomial Evaluation (CDB) VI
  • 1D Polynomial Evaluation (DBL) VI
  • 1D Polynomial Evaluation (CDB) VI
  • 2D Polynomial Evaluation (DBL) VI
  • 2D Polynomial Evaluation (CDB) VI

ScalarScalar PolynomialPolynomial EvaluationEvaluation (DBL)(DBL) VIVI

Evaluates the polynomial P(x) with a single value or multiple values. The data types
you wire to the a and P(x) inputs determine the polymorphic instance to use.


Inputs/Outputs

   •      a —

    a specifies the real value at which the VI evaluates P(x).

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power.

   •       P(a) —

    P(a) returns the result of evaluating P(x) at a.

   •       error —


                                                    © National Instruments 4053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4054 ordinal=4054 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       ScalarScalar PolynomialPolynomial EvaluationEvaluation (CDB)(CDB) VIVI

       Evaluates the polynomial P(x) with a single value or multiple values. The data types
      you wire to the a and P(x) inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •      a —

           a specifies the complex value at which the VI evaluates P(x).

               •       P(x) —

             P(x) contains the complex polynomial coefficients in ascending order of power.

               •       P(a) —

             P(a) returns the result of evaluating P(x) at a.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D1D PolynomialPolynomial EvaluationEvaluation (DBL)(DBL) VIVI

       Evaluates the polynomial P(x) with a single value or multiple values. The data types
      you wire to the a and P(x) inputs determine the polymorphic instance to use.


4054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4055 ordinal=4055 -->
## Functions

Functions

Inputs/Outputs

   •     A —

   A is an array of real values.

   •       P(x) —

    P(x) contains the real polynomial coefficients in ascending order of power.

   •      P(A) —

    P(A) returns the result of evaluating P(x) on an element-by-element basis with the values in A.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D1D PolynomialPolynomial EvaluationEvaluation (CDB)(CDB) VIVI

Evaluates the polynomial P(x) with a single value or multiple values. The data types
you wire to the a and P(x) inputs determine the polymorphic instance to use.


Inputs/Outputs

   •     A —

   A is an array of complex values.

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •      P(A) —

    P(A) returns the result of evaluating P(x) on an element-by-element basis with the values in A.

   •       error —

                                                    © National Instruments 4055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4056 ordinal=4056 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D2D PolynomialPolynomial EvaluationEvaluation (DBL)(DBL) VIVI

       Evaluates the polynomial P(x) with a single value or multiple values. The data types
      you wire to the a and P(x) inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •     A —

          A is a matrix of real values.

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •      P(A) —

            P(A) returns the result of evaluating P(x) on an element-by-element basis with the values in A.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D2D PolynomialPolynomial EvaluationEvaluation (CDB)(CDB) VIVI

       Evaluates the polynomial P(x) with a single value or multiple values. The data types
      you wire to the a and P(x) inputs determine the polymorphic instance to use.


4056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4057 ordinal=4057 -->
## Functions

Functions

Inputs/Outputs

   •     A —

   A is a matrix of complex values.

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •      P(A) —

    P(A) returns the result of evaluating P(x) on an element-by-element basis with the values in A.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

EvaluateEvaluate PolynomialPolynomial withwith MatrixMatrix

Evaluates the polynomial P(x) with matrix A. The data types you wire to the P(x) and A
inputs determine the polymorphic instance to use.


  • Evaluate Polynomial with Matrix (DBL) VI
  • Evaluate Polynomial with Matrix (CDB) VI

The VI evaluates the polynomial P(x) with the square matrix A. For example, the
following polynomial defines the second-order polynomial described by the three-
element array P[0…2]:

P[2]x² + P[1]x+ p[0]

The evaluation of the preceding polynomial by the VI yields the following result:

P([A]) = P[2]A² + P[1]A + P[0]I


                                                    © National Instruments 4057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4058 ordinal=4058 -->
## Functions

Functions

      where Iis the identity matrix and the same size as A.

      EvaluateEvaluate PolynomialPolynomial withwith MatrixMatrix (DBL)(DBL) VIVI

       Evaluates the polynomial P(x) with matrix A. The data types you wire to the P(x) and A
       inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •     A —

          A is a square matrix of real values. A acts as the independent variable of P(x). If A is not square,
            the VI sets P([A]) to an empty array and returns an error.

               •       P(x) —

             P(x) contains the real polynomial coefficients in ascending order of power.

               •       P([A]) —

              P([A]) returns the evaluation of the real polynomial P(x) at the real values A contains.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI evaluates the polynomial P(x) with the square matrix A. For example, the
       following polynomial defines the second-order polynomial described by the three-
      element array P[0…2]:

       P[2]x² + P[1]x+ p[0]

      The evaluation of the preceding polynomial by the VI yields the following result:

        P([A]) = P[2]A² + P[1]A + P[0]I


4058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4059 ordinal=4059 -->
## Functions

Functions

where Iis the identity matrix and the same size as A.

EvaluateEvaluate PolynomialPolynomial withwith MatrixMatrix (CDB)(CDB) VIVI

Evaluates the polynomial P(x) with matrix A. The data types you wire to the P(x) and A
inputs determine the polymorphic instance to use.


Inputs/Outputs

   •     A —

   A is a square matrix of complex values. A acts as the independent variable of P(x). If A is not
    square, the VI sets P([A]) to an empty array and returns an error.

   •       P(x) —

    P(x) contains the complex polynomial coefficients in ascending order of power.

   •       P([A]) —

     P([A]) returns the evaluation of the complex polynomial P(x) at the complex values A contains.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The VI evaluates the polynomial P(x) with the square matrix A. For example, the
following polynomial defines the second-order polynomial described by the three-
element array P[0…2]:

P[2]x² + P[1]x+ p[0]

The evaluation of the preceding polynomial by the VI yields the following result:

P([A]) = P[2]A² + P[1]A + P[0]I


                                                    © National Instruments 4059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4060 ordinal=4060 -->
## Functions

Functions

      where Iis the identity matrix and the same size as A.

      PartialPartial FractionFraction ExpansionExpansion

       Calculates the partial fraction expansion of a polynomial using the Heaviside cover-up
      method.


      Inputs/Outputs

               •      Numerator —

           Numerator contains the rational polynomial coefficients, in ascending order of power, for the
           numerator polynomial.

               •      Denominator —

           Denominator contains the rational polynomial coefficients, in ascending order of power, for the
           denominator polynomial.

               •      tolerance —

            tolerance defines a level for multiplicity.

               •      option —

            option specifies how the VI handles the co-factors of Numerator and Denominator.

                    If option is Cancel Co-factors, this VI performs polynomial GCD of Numerator and Denominator
                  first. If option is Reserve Co-factors, this VI keeps Denominator unchanged.

           0   Cancel Co-factors
           1   Reserve Co-factors (default)

               •       Multiplicity —


4060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4061 ordinal=4061 -->
## Functions

Functions


     Multiplicity returns the number of times each root in Poles occurs. Multiplicity occurs when the
     difference between two elements in Poles is less than tolerance.

   •      Polynomial —

    Polynomial returns the coefficients, in ascending order of power, for the quotient polynomial
    that results from the division of Numerator by Denominator.

   •      Poles —

    Poles returns the unique roots of Denominator. The roots of Denominator result from removing
      all common factors between Numerator and Denominator.

   •      Residues —

    Residues returns the numerators of the partial fractions that result for each pole.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

CreateCreate PolynomialPolynomial FromFrom PFEPFE

Uses partial fraction expansion to reconstruct a rational polynomial.


Inputs/Outputs

   •       Multiplicity —

     Multiplicity specifies the number of times each root in Poles occurs.

    Use the Partial Fraction Expansion VI to obtain the Multiplicity. If Multiplicity is empty, the VI
     calculates the number of nonzero elements in each row of Residues and regards that number as
    the multiplicity of the corresponding pole.


                                                    © National Instruments 4061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4062 ordinal=4062 -->
## Functions

Functions

               •      Polynomial —

           Polynomial contains the coefficients for the quotient polynomial in ascending order of power.

           Use the Partial Fraction Expansion VI to obtain the Polynomial.

               •      Poles —

            Poles contains the unique roots of Denominator.

           Use the Partial Fraction Expansion VI to obtain the Poles.

               •      Residues —

           Residues contains the numerators of the partial fractions that result for each pole.

           Use the Partial Fraction Expansion VI to obtain the Residues.

               •      option —

            option specifies how the VI handles the co-factors of Numerator and Denominator.

                    If option is Cancel Co-factors, this VI performs polynomial GCD of Numerator and Denominator
                  first. If option is Reserve Co-factors, this VI keeps Denominator unchanged.

           0   Cancel Co-factors
           1   Reserve Co-factors (default)

               •      Numerator —

           Numerator returns the rational polynomial coefficients, in ascending order of power, for the
           numerator polynomial.

               •      Denominator —

           Denominator returns the rational polynomial coefficients, in ascending order of power, for the
           denominator polynomial.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4063 ordinal=4063 -->
## Functions

Functions

The VI uses the following equation to reconstruct the rational polynomial:


where P(x) is Numerator, Q(x) is Denominator, A(x) is Polynomial, nis the number of
elements in Poles, ri is the ith element in Poles, mi is the ith element in Multiplicity,
and aik is the (i, k)th element in Residues.

The following block diagram shows how to use the Create Polynomial From PFE VI to
reconstruct a rational polynomial from the Partial Fraction Expansion VI.


PolynomialPolynomial EigenvaluesEigenvalues andand VectorsVectors

Solves the polynomial eigenvalue problem. Wire data to the Input Matrices input to
determine the polymorphic instance to use or manually select the instance.


  • Polynomial Eigenvalues and Vectors (DBL) VI
  • Polynomial Eigenvalues and Vectors (CDB) VI

The following equation defines the polynomial eigenvalue problem.


where


                                                    © National Instruments 4063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4064 ordinal=4064 -->
## Functions

Functions

       C0, C1, …, Cp– 1 are square n× nmatrices in Input Matrices λj is the jth element in
       Eigenvalues xj has length nand is the jth column in Eigenvectors with j= 0, 1, …, n*p
      – 1

           If p= 1, the VI calculates eigenvalues and eigenvectors using the following equation.

      C0xj = λjxj

           If p= 2, the VI calculates generalized eigenvalues and eigenvectors using the following
       equation.

      C0xj = –λjC1xj
      PolynomialPolynomial EigenvaluesEigenvalues andand VectorsVectors (DBL)(DBL) VIVI

       Solves the polynomial eigenvalue problem. Wire data to the Input Matrices input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •      Input Matrices —

            Input Matrices is a 3D array of size n*n*pand contains square input matrices of the same size.
          The input matrices must be square. The matrices are in ascending order of power for
            Eigenvalues.

               •      output option —

           output option determines whether the VI computes Eigenvectors.

           0  eigenvalues
           1  eigenvalues and vectors (default)

               •      Eigenvalues —


4064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4065 ordinal=4065 -->
## Functions

Functions


    Eigenvalues is a complex vector of n*pelements and contains all the computed eigenvalues.

   •      Eigenvectors —

    Eigenvectors is an n× (n*p) complex matrix and contains all the computed eigenvectors in its
    columns.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the polynomial eigenvalue problem.


where

C0, C1, …, Cp– 1 are square n× nmatrices in Input Matrices λj is the jth element in
Eigenvalues xj has length nand is the jth column in Eigenvectors with j= 0, 1, …, n*p
– 1

If p= 1, the VI calculates eigenvalues and eigenvectors using the following equation.

C0xj = λjxj

If p= 2, the VI calculates generalized eigenvalues and eigenvectors using the following
equation.

C0xj = –λjC1xj
PolynomialPolynomial EigenvaluesEigenvalues andand VectorsVectors (CDB)(CDB) VIVI

Solves the polynomial eigenvalue problem. Wire data to the Input Matrices input to
determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4066 ordinal=4066 -->
## Functions

Functions


      Inputs/Outputs

               •      Input Matrices —

            Input Matrices is a 3D array of size n*n*pand contains square input matrices of the same size.
          The input matrices must be square. The matrices are in ascending order of power for
            Eigenvalues.

               •      output option —

           output option determines whether the VI computes Eigenvectors.

           0  eigenvalues
           1  eigenvalues and vectors (default)

               •      Eigenvalues —

            Eigenvalues is a complex vector of n*pelements and contains all the computed eigenvalues.

               •      Eigenvectors —

            Eigenvectors is an n× (n*p) complex matrix and contains all the computed eigenvectors in its
           columns.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the polynomial eigenvalue problem.


      where

       C0, C1, …, Cp– 1 are square n× nmatrices in Input Matrices λj is the jth element in
       Eigenvalues xj has length nand is the jth column in Eigenvectors with j= 0, 1, …, n*p

4066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4067 ordinal=4067 -->
## Functions

Functions

– 1

If p= 1, the VI calculates eigenvalues and eigenvectors using the following equation.

C0xj = λjxj

If p= 2, the VI calculates generalized eigenvalues and eigenvectors using the following
equation.

C0xj = –λjC1xj
OrthogonalOrthogonal && Non-orthogonalNon-orthogonal PolynomialsPolynomials

Use this class of polynomial functions to perform calculations and evaluations with
orthogonal or non-orthogonal polynomials.

The VIs on this palette can return mathematics error codes.


 Palette Object            Description

 Create Orthogonal                           Creates orthogonal polynomial coefficients.
 Polynomial


 Bessel Polynomial VI       Calculates the Bessel Polynomial of order n for any real number x.


 Chebyshev Polynomial VI   Calculates the Chebyshev polynomial of order n at the point x.


                            Calculates the associated Legendre polynomial of degree n and order
 Legendre Polynomial
              m at point x.


                                                    © National Instruments 4067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4068 ordinal=4068 -->
## Functions

Functions

      CreateCreate OrthogonalOrthogonal PolynomialPolynomial

       Creates orthogonal polynomial coefficients.


      Inputs/Outputs

               •      type —

           type specifies the type of orthogonal polynomial coefficients to create.

                Chebyshev I
           0                    (default)
           1    Chebyshev II
           2    Legendre
           3     Laguerre
           4    Hermite
           5     Associate Laguerre
           6    Gegenbauer

               •      order —

            order specifies the order of the orthogonal polynomial coefficients. If order is less than zero, the
              VI sets P(x) to an empty array and returns an error.

               •      alpha —

           alpha specifies the alpha value the VI needs to create associate Laguerre and Gegenbauer
            polynomial coefficients. When type is Gegenbauer, alpha must be a nonzero value.

               •       P(x) —

             P(x) returns the orthogonal polynomial coefficients in ascending order of power.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4069 ordinal=4069 -->
## Functions

Functions

BesselBessel PolynomialPolynomial VIVI

Calculates the Bessel Polynomial of order n for any real number x.


Inputs/Outputs

   •      x —

    x is any real number.

   •     n —

    n is the nonnegative order (integer) of the Bessel polynomial.

   •      Bessel polynomial (n,x) —

    Bessel polynomial (n,x) is the result of the calculation of the order n Bessel polynomial at the
    given value of x.


The following equation shows a recurrence relation that defines the Bessel polynomial
Pn(x) of order n.


where P0(x) = 1 and P1(x) = 1 + x.

The following illustration shows the first four Bessel polynomials from bottom to top
on the right side. The range of x is from [–6, 6].


                                                    © National Instruments 4069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4070 ordinal=4070 -->
## Functions

Functions


      ChebyshevChebyshev PolynomialPolynomial VIVI

       Calculates the Chebyshev polynomial of order n at the point x.


      Inputs/Outputs

               •      x —

           x is any real number.

               •     n —

          n is the nonnegative order (integer) of the Chebyshev polynomial.

               •       T(n,x) —

             T(n,x) is the value of the nth Chebyshev polynomial at the point x.


      The following equation defines the Chebyshev polynomial Tn(x).

       Tn(x) = cos(n arccos(x)) for n = 0, 1, 2, ..., and real numbers x.

           Note The result of this definition does not look like a polynomial at first
               glance, but you can use trigonometric rules to show that Tn is a polynomial


4070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4071 ordinal=4071 -->
## Functions

Functions


        of degree n in the variable x.

Tn(x) forms the base of the Chebyshev approximation. For i≠ j, the following equation
gives the Chebyshev approximation.


All Tn(x) form an orthogonal system over the weight function


The following illustration shows the graph for the first four Chebyshev polynomials of
degrees 0, 1, 2, and 3.


LegendreLegendre PolynomialPolynomial

Calculates the associated Legendre polynomial of degree n and order m at point x.


                                                    © National Instruments 4071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4072 ordinal=4072 -->
## Functions

Functions

      Inputs/Outputs

               •      x —

           x is a real number between -1 and 1.

               •     n —

          n is the degree of the Legendre polynomial. n must be nonnegative.

               •   m —

       m is the order of the Legendre polynomial. m must be nonnegative and less than or equal to n.

               •      type —

           type specifies the type of Legendre polynomial.

           0 Standard (default)—Computes the associated Legendre function.
           1 Semi-Normalized—Computes the semi-normalized Legendre function.
           2 Normalized—Computes the normalized associated Legendre function.

               •      Legendre (n,m,x) —

           Legendre (n,m,x) returns the value of the associated Legendre polynomial of degree n and order
       m at point x.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The associated Legendre polynomial of degree n and order m is the solution of the
       following associated Legendre differential equation.


      The following graph shows four associated Legendre polynomials of degree 3 (n=3).


4072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4073 ordinal=4073 -->
## Functions

Functions


RationalRational PolynomialPolynomial

Use the Rational Polynomial VIs to perform calculations and evaluations with rational
polynomials.

The VIs on this palette can return mathematics error codes.


 Palette Object  Description

              Adds the rational polynomials G1 and G2. The data types you wire to the Add Rational
              Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs determine Polynomials
                the polymorphic instance to use.


 Subtract        Subtracts rational polynomial G2 from rational polynomial G1. The data types you
 Rational        wire to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
 Polynomials    determine the polymorphic instance to use.


 Multiply
                  Multiplies rational polynomial G1 by rational polynomial G2. The data types you Rational
                wire to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs Polynomials


                                                    © National Instruments 4073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4074 ordinal=4074 -->
## Functions

Functions


         Palette Object  Description

                      determine the polymorphic instance to use.


         Divide          Divides rational polynomial G1 by rational polynomial G2. The data types you wire
         Rational        to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
        Polynomials    determine the polymorphic instance to use.


         Negative                         Calculates the negative feedback equation. The data types you wire to the        Feedback with                     Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs determine         Rational
                        the polymorphic instance to use.        Polynomials

          Positive
                         Calculates the positive feedback equation. The data types you wire to the        Feedback with                     Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs determine         Rational
                        the polymorphic instance to use.        Polynomials


        Pade          Determines the coefficients of a rational polynomial to best suit a given set of
        Approximation  derivatives.


        Normalize      Normalizes numerator and denominator polynomials with the highest
        with Highest   denominator term. The data types you wire to the Numerator and Denominator
       Den Term       inputs determine the polymorphic instance to use.


        Normalize      Normalizes numerator and denominator polynomials with the lowest denominator
        with Lowest    term. The data types you wire to the Numerator and Denominator inputs
       Den Term      determine the polymorphic instance to use.


       Remove      Removes the residue from the denominator if the numerator equals zero. The data
        Residue from   types you wire to the Numerator and Denominator inputs determine the
        Denominator   polymorphic instance to use.


4074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4075 ordinal=4075 -->
## Functions

Functions


 Palette Object  Description

                Evaluates a rational polynomial at the points you specify in A. P(x) and Q(x) specify
 1D Rational                the numerator and denominator polynomial coefficients, respectively. The data Polynomial                types you wire to the P(x) and Q(x) inputs determine the polymorphic instance to Evaluation                 use.


 nth Derivative                 Calculates the nth order derivative of a rational polynomial. The data types you of Rational
                wire to the P(x) and Q(x) inputs determine the polymorphic instance to use. Polynomial

 Partial                 Calculates the partial fraction expansion of a polynomial using the Heaviside Fraction                cover-up method.
 Expansion

 Create
 Polynomial    Uses partial fraction expansion to reconstruct a rational polynomial.
 From PFE

AddAdd RationalRational PolynomialsPolynomials

Adds the rational polynomials G1 and G2. The data types you wire to the Numerator 1,
Denominator 1, Numerator 2, and Denominator 2 inputs determine the polymorphic
instance to use.


  • Add Rational Polynomials (DBL) VI
  • Add Rational Polynomials (CDB) VI

The following equation defines G1 and G2:


                                                    © National Instruments 4075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4076 ordinal=4076 -->
## Functions

Functions

   AddAdd RationalRational PolynomialsPolynomials (DBL)(DBL) VIVI

      Adds the rational polynomials G1 and G2. The data types you wire to the Numerator 1,
      Denominator 1, Numerator 2, and Denominator 2 inputs determine the polymorphic
       instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
             of the first rational polynomial G1.

               •      Numerator 2 —

           Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
            the second rational polynomial G2.

               •      Denominator 2 —

           Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
             of the second rational polynomial G2.

               •      threshold —

            threshold specifies the level at which the VI removes from Numerator Out or Denominator Out
            the trailing elements whose absolute values or relative values are less than or equal to
            threshold.


4076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4077 ordinal=4077 -->
## Functions

Functions


       If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
    Numerator Out or Denominator Out returns a one-element array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from Numerator Out or
    Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
    Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
       If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or
    Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
     coefficient which has the maximum absolute value in resulting numerator or denominator
    polynomial.

    0   Absolute Value (default)
    1    Relative Value

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

    Denominator Out returns the denominator polynomial coefficients, in ascending order of
    power, of the rational polynomial that results from the mathematical operation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines G1 and G2:


AddAdd RationalRational PolynomialsPolynomials (CDB)(CDB) VIVI

Adds the rational polynomials G1 and G2. The data types you wire to the Numerator 1,


                                                    © National Instruments 4077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4078 ordinal=4078 -->
## Functions

Functions

      Denominator 1, Numerator 2, and Denominator 2 inputs determine the polymorphic
       instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
             of the first rational polynomial G1.

               •      Numerator 2 —

           Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
            the second rational polynomial G2.

               •      Denominator 2 —

           Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
             of the second rational polynomial G2.

               •      threshold —

            threshold specifies the level at which the VI removes from Numerator Out or Denominator Out
            the trailing elements whose absolute values or relative values are less than or equal to
            threshold.

                    If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
           Numerator Out or Denominator Out returns a one-element array.

               •      threshold type —


4078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4079 ordinal=4079 -->
## Functions

Functions


    threshold type specifies how the VI removes the trailing elements from Numerator Out or
    Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
    Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
       If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or
    Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
     coefficient which has the maximum absolute value in resulting numerator or denominator
    polynomial.

    0   Absolute Value (default)
    1    Relative Value

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

    Denominator Out returns the denominator polynomial coefficients, in ascending order of
    power, of the rational polynomial that results from the mathematical operation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines G1 and G2:


SubtractSubtract RationalRational PolynomialsPolynomials

Subtracts rational polynomial G2 from rational polynomial G1. The data types you wire
to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
determine the polymorphic instance to use.


                                                    © National Instruments 4079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4080 ordinal=4080 -->
## Functions

Functions

            • Subtract Rational Polynomials (DBL) VI
            • Subtract Rational Polynomials (CDB) VI

      The following equation defines G1 and G2.


    SubtractSubtract RationalRational PolynomialsPolynomials (DBL)(DBL) VIVI

       Subtracts rational polynomial G2 from rational polynomial G1. The data types you wire
       to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
      determine the polymorphic instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
             of the first rational polynomial G1.

               •      Numerator 2 —

           Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
            the second rational polynomial G2.

               •      Denominator 2 —


4080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4081 ordinal=4081 -->
## Functions

Functions


    Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
     of the second rational polynomial G2.

   •      threshold —

    threshold specifies the level at which the VI removes from Numerator Out or Denominator Out
    the trailing elements whose absolute values or relative values are less than or equal to
    threshold.

       If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
    Numerator Out or Denominator Out returns a one-element array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from Numerator Out or
    Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
    Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
       If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or
    Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
     coefficient which has the maximum absolute value in resulting numerator or denominator
    polynomial.

    0   Absolute Value (default)
    1    Relative Value

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

    Denominator Out returns the denominator polynomial coefficients, in ascending order of
    power, of the rational polynomial that results from the mathematical operation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines G1 and G2.

                                                    © National Instruments 4081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4082 ordinal=4082 -->
## Functions

Functions


    SubtractSubtract RationalRational PolynomialsPolynomials (CDB)(CDB) VIVI

       Subtracts rational polynomial G2 from rational polynomial G1. The data types you wire
       to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
      determine the polymorphic instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
             of the first rational polynomial G1.

               •      Numerator 2 —

           Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
            the second rational polynomial G2.

               •      Denominator 2 —

           Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
             of the second rational polynomial G2.

               •      threshold —

            threshold specifies the level at which the VI removes from Numerator Out or Denominator Out


4082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4083 ordinal=4083 -->
## Functions

Functions


    the trailing elements whose absolute values or relative values are less than or equal to
    threshold.

       If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
    Numerator Out or Denominator Out returns a one-element array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from Numerator Out or
    Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
    Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
       If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or
    Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
     coefficient which has the maximum absolute value in resulting numerator or denominator
    polynomial.

    0   Absolute Value (default)
    1    Relative Value

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

    Denominator Out returns the denominator polynomial coefficients, in ascending order of
    power, of the rational polynomial that results from the mathematical operation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines G1 and G2.


                                                    © National Instruments 4083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4084 ordinal=4084 -->
## Functions

Functions

       MultiplyMultiply RationalRational PolynomialsPolynomials

        Multiplies rational polynomial G1 by rational polynomial G2. The data types you wire
       to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
      determine the polymorphic instance to use.


            • Multiply Rational Polynomials (DBL) VI
            • Multiply Rational Polynomials (CDB) VI

      The following equation defines G1 and G2.


    MultiplyMultiply RationalRational PolynomialsPolynomials (DBL)(DBL) VIVI

        Multiplies rational polynomial G1 by rational polynomial G2. The data types you wire
       to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
      determine the polymorphic instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —


4084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4085 ordinal=4085 -->
## Functions

Functions


  Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
  of the first rational polynomial G1.

•      Numerator 2 —

  Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
  the second rational polynomial G2.

•      Denominator 2 —

  Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
  of the second rational polynomial G2.

•      threshold —

  threshold specifies the level at which the VI removes from Numerator Out or Denominator Out
  the trailing elements whose absolute values or relative values are less than or equal to
  threshold.

   If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
  Numerator Out or Denominator Out returns a one-element array.

•      threshold type —

  threshold type specifies how the VI removes the trailing elements from Numerator Out or
  Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
  Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
   If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or
  Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
  coefficient which has the maximum absolute value in resulting numerator or denominator
  polynomial.

  0   Absolute Value (default)
  1    Relative Value

•      Numerator Out —

  Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
  the rational polynomial that results from the mathematical operation.

•      Denominator Out —


                                                   © National Instruments 4085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4086 ordinal=4086 -->
## Functions

Functions


           Denominator Out returns the denominator polynomial coefficients, in ascending order of
            power, of the rational polynomial that results from the mathematical operation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines G1 and G2.


    MultiplyMultiply RationalRational PolynomialsPolynomials (CDB)(CDB) VIVI

        Multiplies rational polynomial G1 by rational polynomial G2. The data types you wire
       to the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs
      determine the polymorphic instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
             of the first rational polynomial G1.

               •      Numerator 2 —

4086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4087 ordinal=4087 -->
## Functions

Functions


  Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
  the second rational polynomial G2.

•      Denominator 2 —

  Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
  of the second rational polynomial G2.

•      threshold —

  threshold specifies the level at which the VI removes from Numerator Out or Denominator Out
  the trailing elements whose absolute values or relative values are less than or equal to
  threshold.

   If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
  Numerator Out or Denominator Out returns a one-element array.

•      threshold type —

  threshold type specifies how the VI removes the trailing elements from Numerator Out or
  Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
  Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
   If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or
  Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
  coefficient which has the maximum absolute value in resulting numerator or denominator
  polynomial.

  0   Absolute Value (default)
  1    Relative Value

•      Numerator Out —

  Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
  the rational polynomial that results from the mathematical operation.

•      Denominator Out —

  Denominator Out returns the denominator polynomial coefficients, in ascending order of
  power, of the rational polynomial that results from the mathematical operation.

•       error —


                                                   © National Instruments 4087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4088 ordinal=4088 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines G1 and G2.


       DivideDivide RationalRational PolynomialsPolynomials

       Divides rational polynomial G1 by rational polynomial G2. The data types you wire to
       the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs determine
       the polymorphic instance to use.


            • Divide Rational Polynomials (DBL) VI
            • Divide Rational Polynomials (CDB) VI

      The following equation defines G1 and G2.

    DivideDivide RationalRational PolynomialsPolynomials (DBL)(DBL) VIVI

       Divides rational polynomial G1 by rational polynomial G2. The data types you wire to
       the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs determine
       the polymorphic instance to use.


4088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4089 ordinal=4089 -->
## Functions

Functions


Inputs/Outputs

   •      Numerator 1 —

    Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
    the first rational polynomial G1.

   •      Denominator 1 —

    Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
     of the first rational polynomial G1.

   •      Numerator 2 —

    Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
    the second rational polynomial G2.

   •      Denominator 2 —

    Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
     of the second rational polynomial G2.

   •      threshold —

    threshold specifies the level at which the VI removes from Numerator Out or Denominator Out
    the trailing elements whose absolute values or relative values are less than or equal to
    threshold.

       If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
    Numerator Out or Denominator Out returns a one-element array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from Numerator Out or
    Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
    Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
       If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or


                                                    © National Instruments 4089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4090 ordinal=4090 -->
## Functions

Functions


           Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
              coefficient which has the maximum absolute value in resulting numerator or denominator
            polynomial.

           0   Absolute Value (default)
           1    Relative Value

               •      Numerator Out —

           Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
            the rational polynomial that results from the mathematical operation.

               •      Denominator Out —

           Denominator Out returns the denominator polynomial coefficients, in ascending order of
            power, of the rational polynomial that results from the mathematical operation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines G1 and G2.

    DivideDivide RationalRational PolynomialsPolynomials (CDB)(CDB) VIVI

       Divides rational polynomial G1 by rational polynomial G2. The data types you wire to
       the Numerator 1, Denominator 1, Numerator 2, and Denominator 2 inputs determine
       the polymorphic instance to use.


4090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4091 ordinal=4091 -->
## Functions

Functions

Inputs/Outputs

   •      Numerator 1 —

    Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
    the first rational polynomial G1.

   •      Denominator 1 —

    Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
     of the first rational polynomial G1.

   •      Numerator 2 —

    Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
    the second rational polynomial G2.

   •      Denominator 2 —

    Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
     of the second rational polynomial G2.

   •      threshold —

    threshold specifies the level at which the VI removes from Numerator Out or Denominator Out
    the trailing elements whose absolute values or relative values are less than or equal to
    threshold.

       If all the elements in Numerator Out or Denominator Out are less than or equal to threshold,
    Numerator Out or Denominator Out returns a one-element array.

   •      threshold type —

    threshold type specifies how the VI removes the trailing elements from Numerator Out or
    Denominator Out. If threshold type is Absolute Value, the VI removes the trailing elements from
    Numerator Out or Denominator Out whose absolute values are less than or equal to threshold.
       If threshold type is Relative Value, the VI removes the trailing elements from Numerator Out or
    Denominator Out whose absolute values are less than or equal to threshold * |x|, where xis the
     coefficient which has the maximum absolute value in resulting numerator or denominator
    polynomial.

    0   Absolute Value (default)


                                                    © National Instruments 4091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4092 ordinal=4092 -->
## Functions

Functions


           1    Relative Value

               •      Numerator Out —

           Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
            the rational polynomial that results from the mathematical operation.

               •      Denominator Out —

           Denominator Out returns the denominator polynomial coefficients, in ascending order of
            power, of the rational polynomial that results from the mathematical operation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines G1 and G2.


      NegativeNegative FeedbackFeedback withwith RationalRational PolynomialsPolynomials

       Calculates the negative feedback equation. The data types you wire to the Numerator
        1, Denominator 1, Numerator 2, and Denominator 2 inputs determine the
      polymorphic instance to use.


            • Negative Feedback with Rational Polynomials (DBL) VI
            • Negative Feedback with Rational Polynomials (CDB) VI

      The following equation defines the negative feedback equation.


      where G1 and G2 are rational polynomials, G1 = N1/D1, and G2 = N2/D2.

4092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4093 ordinal=4093 -->
## Functions

Functions

NegativeNegative FeedbackFeedback withwith RationalRational
PolynomialsPolynomials (DBL)(DBL) VIVI

Calculates the negative feedback equation. The data types you wire to the Numerator
1, Denominator 1, Numerator 2, and Denominator 2 inputs determine the
polymorphic instance to use.


Inputs/Outputs

   •      Numerator 1 —

    Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
    the first rational polynomial G1.

   •      Denominator 1 —

    Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
     of the first rational polynomial G1.

   •      Numerator 2 —

    Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
    the second rational polynomial G2.

   •      Denominator 2 —

    Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
     of the second rational polynomial G2.

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

                                                    © National Instruments 4093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4094 ordinal=4094 -->
## Functions

Functions


           Denominator Out returns the denominator polynomial coefficients, in ascending order of
            power, of the rational polynomial that results from the mathematical operation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the negative feedback equation.


      where G1 and G2 are rational polynomials, G1 = N1/D1, and G2 = N2/D2.
   NegativeNegative FeedbackFeedback withwith RationalRational
   PolynomialsPolynomials (CDB)(CDB) VIVI

       Calculates the negative feedback equation. The data types you wire to the Numerator
        1, Denominator 1, Numerator 2, and Denominator 2 inputs determine the
      polymorphic instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,


4094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4095 ordinal=4095 -->
## Functions

Functions


     of the first rational polynomial G1.

   •      Numerator 2 —

    Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
    the second rational polynomial G2.

   •      Denominator 2 —

    Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
     of the second rational polynomial G2.

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

    Denominator Out returns the denominator polynomial coefficients, in ascending order of
    power, of the rational polynomial that results from the mathematical operation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the negative feedback equation.


where G1 and G2 are rational polynomials, G1 = N1/D1, and G2 = N2/D2.

PositivePositive FeedbackFeedback withwith RationalRational PolynomialsPolynomials

Calculates the positive feedback equation. The data types you wire to the Numerator
1, Denominator 1, Numerator 2, and Denominator 2 inputs determine the
polymorphic instance to use.


                                                    © National Instruments 4095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4096 ordinal=4096 -->
## Functions

Functions


            • Positive Feedback with Rational Polynomials (DBL) VI
            • Positive Feedback with Rational Polynomials (CDB) VI

      The following equation defines the positive feedback equation.


      where G1 and G2 are rational polynomials, G1 = N1/D1, and G2 = N2/D2.
    PositivePositive FeedbackFeedback withwith RationalRational PolynomialsPolynomials
   (DBL)(DBL) VIVI

       Calculates the positive feedback equation. The data types you wire to the Numerator
        1, Denominator 1, Numerator 2, and Denominator 2 inputs determine the
      polymorphic instance to use.


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
             of the first rational polynomial G1.

               •      Numerator 2 —

4096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4097 ordinal=4097 -->
## Functions

Functions


    Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
    the second rational polynomial G2.

   •      Denominator 2 —

    Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
     of the second rational polynomial G2.

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

    Denominator Out returns the denominator polynomial coefficients, in ascending order of
    power, of the rational polynomial that results from the mathematical operation.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equation defines the positive feedback equation.


where G1 and G2 are rational polynomials, G1 = N1/D1, and G2 = N2/D2.
PositivePositive FeedbackFeedback withwith RationalRational PolynomialsPolynomials
(CDB)(CDB) VIVI

Calculates the positive feedback equation. The data types you wire to the Numerator
1, Denominator 1, Numerator 2, and Denominator 2 inputs determine the
polymorphic instance to use.


                                                    © National Instruments 4097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4098 ordinal=4098 -->
## Functions

Functions


      Inputs/Outputs

               •      Numerator 1 —

           Numerator 1 contains the numerator polynomial coefficients, in ascending order of power, of
            the first rational polynomial G1.

               •      Denominator 1 —

           Denominator 1 contains the denominator polynomial coefficients, in ascending order of power,
             of the first rational polynomial G1.

               •      Numerator 2 —

           Numerator 2 contains the numerator polynomial coefficients, in ascending order of power, of
            the second rational polynomial G2.

               •      Denominator 2 —

           Denominator 2 contains the denominator polynomial coefficients, in ascending order of power,
             of the second rational polynomial G2.

               •      Numerator Out —

           Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
            the rational polynomial that results from the mathematical operation.

               •      Denominator Out —

           Denominator Out returns the denominator polynomial coefficients, in ascending order of
            power, of the rational polynomial that results from the mathematical operation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equation defines the positive feedback equation.


4098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4099 ordinal=4099 -->
## Functions

Functions


where G1 and G2 are rational polynomials, G1 = N1/D1, and G2 = N2/D2.

PadePade ApproximationApproximation

Determines the coefficients of a rational polynomial to best suit a given set of
derivatives.


Inputs/Outputs

   •       Derivatives —

    Derivatives is the array that describes the derivatives of the given function.

   •   m —

  m specifies the degree of the Numerator polynomial.

   •     n —

   n specifies the degree of the Denominator polynomial.

   •      Numerator —

    Numerator returns the numerator polynomial coefficients in ascending order of power.

   •      Denominator —

    Denominator returns the denominator polynomial coefficients in ascending order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let fbe a given function with known derivatives and values

                                                    © National Instruments 4099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4100 ordinal=4100 -->
## Functions

Functions

        f(0), f´(0), …, f(m + n)(0)

      There is a unique rational polynomial

    m ≥ n

       with

       R(0) = f(0), R´(0) = f´(0), …, R(m + n)(0) = f(m + n)(0)

      The rational polynomial can be determined by solving a special linear equation.

      NormalizeNormalize withwith HighestHighest DenDen TermTerm

       Normalizes numerator and denominator polynomials with the highest denominator
       term. The data types you wire to the Numerator and Denominator inputs determine
       the polymorphic instance to use.


            • Normalize with Highest Den Term (DBL) VI
            • Normalize with Highest Den Term (CDB) VI

      The following equations define the Numerator and Denominator polynomials:


      where Dm ≠ 0.

      The VI uses the following expression to normalize the Numerator and Denominator
       polynomials with the highest nonzero Denominator term:


4100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4101 ordinal=4101 -->
## Functions

Functions


NormalizeNormalize withwith HighestHighest DenDen TermTerm (DBL)(DBL) VIVI

Normalizes numerator and denominator polynomials with the highest denominator
term. The data types you wire to the Numerator and Denominator inputs determine
the polymorphic instance to use.


Inputs/Outputs

   •      Numerator —

    Numerator contains the numerator polynomial coefficients, in ascending order of power.

   •      Denominator —

    Denominator contains the denominator polynomial coefficients, in ascending order of power.

   •      Normalized Numerator —

    Normalized Numerator returns the normalized numerator polynomial coefficients, in ascending
    order of power.

   •      Normalized Denominator —

    Normalized Denominator returns the normalized denominator polynomial coefficients, in
    ascending order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


                                                    © National Instruments 4101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4102 ordinal=4102 -->
## Functions

Functions

      The following equations define the Numerator and Denominator polynomials:


      where Dm ≠ 0.

      The VI uses the following expression to normalize the Numerator and Denominator
       polynomials with the highest nonzero Denominator term:


   NormalizeNormalize withwith HighestHighest DenDen TermTerm (CDB)(CDB) VIVI

       Normalizes numerator and denominator polynomials with the highest denominator
       term. The data types you wire to the Numerator and Denominator inputs determine
       the polymorphic instance to use.


      Inputs/Outputs

               •      Numerator —

           Numerator contains the numerator polynomial coefficients, in ascending order of power.

               •      Denominator —

           Denominator contains the denominator polynomial coefficients, in ascending order of power.

               •      Normalized Numerator —


4102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4103 ordinal=4103 -->
## Functions

Functions


    Normalized Numerator returns the normalized numerator polynomial coefficients, in ascending
    order of power.

   •      Normalized Denominator —

    Normalized Denominator returns the normalized denominator polynomial coefficients, in
    ascending order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equations define the Numerator and Denominator polynomials:


where Dm ≠ 0.

The VI uses the following expression to normalize the Numerator and Denominator
polynomials with the highest nonzero Denominator term:


NormalizeNormalize withwith LowestLowest DenDen TermTerm

Normalizes numerator and denominator polynomials with the lowest denominator
term. The data types you wire to the Numerator and Denominator inputs determine
the polymorphic instance to use.


                                                    © National Instruments 4103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4104 ordinal=4104 -->
## Functions

Functions

            • Normalize with Lowest Den Term (DBL) VI
            • Normalize with Lowest Den Term (CDB) VI

      The following equations define the Numerator and Denominator polynomials:


      where Dj ≠ 0 and Dj– 1 = Dj– 2 = … = D1 = D0 = 0.

      The VI uses the following expression to normalize the Numerator and Denominator
       polynomials with the lowest nonzero Denominator term:


   NormalizeNormalize withwith LowestLowest DenDen TermTerm (DBL)(DBL) VIVI

       Normalizes numerator and denominator polynomials with the lowest denominator
       term. The data types you wire to the Numerator and Denominator inputs determine
       the polymorphic instance to use.


      Inputs/Outputs

               •      Numerator —

           Numerator contains the numerator polynomial coefficients, in ascending order of power.

               •      Denominator —


4104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4105 ordinal=4105 -->
## Functions

Functions


    Denominator contains the denominator polynomial coefficients, in ascending order of power.

   •      Normalized Numerator —

    Normalized Numerator returns the normalized numerator polynomial coefficients, in ascending
    order of power.

   •      Normalized Denominator —

    Normalized Denominator returns the normalized denominator polynomial coefficients, in
    ascending order of power.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The following equations define the Numerator and Denominator polynomials:


where Dj ≠ 0 and Dj– 1 = Dj– 2 = … = D1 = D0 = 0.

The VI uses the following expression to normalize the Numerator and Denominator
polynomials with the lowest nonzero Denominator term:


NormalizeNormalize withwith LowestLowest DenDen TermTerm (CDB)(CDB) VIVI

Normalizes numerator and denominator polynomials with the lowest denominator
term. The data types you wire to the Numerator and Denominator inputs determine

                                                    © National Instruments 4105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4106 ordinal=4106 -->
## Functions

Functions

       the polymorphic instance to use.


      Inputs/Outputs

               •      Numerator —

           Numerator contains the numerator polynomial coefficients, in ascending order of power.

               •      Denominator —

           Denominator contains the denominator polynomial coefficients, in ascending order of power.

               •      Normalized Numerator —

           Normalized Numerator returns the normalized numerator polynomial coefficients, in ascending
            order of power.

               •      Normalized Denominator —

           Normalized Denominator returns the normalized denominator polynomial coefficients, in
            ascending order of power.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The following equations define the Numerator and Denominator polynomials:


      where Dj ≠ 0 and Dj– 1 = Dj– 2 = … = D1 = D0 = 0.

      The VI uses the following expression to normalize the Numerator and Denominator

4106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4107 ordinal=4107 -->
## Functions

Functions

polynomials with the lowest nonzero Denominator term:


RemoveRemove ResidueResidue fromfrom DenominatorDenominator

Removes the residue from the denominator if the numerator equals zero. The data
types you wire to the Numerator and Denominator inputs determine the polymorphic
instance to use.


  • Remove Residue from Denominator (DBL) VI
  • Remove Residue from Denominator (CDB) VI
RemoveRemove ResidueResidue fromfrom DenominatorDenominator (DBL)(DBL) VIVI

Removes the residue from the denominator if the numerator equals zero. The data
types you wire to the Numerator and Denominator inputs determine the polymorphic
instance to use.


Inputs/Outputs

   •      Numerator —

    Numerator contains the numerator polynomial coefficients, in ascending order of power, of the
     rational polynomial.

   •      Denominator —


                                                    © National Instruments 4107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4108 ordinal=4108 -->
## Functions

Functions


           Denominator contains the denominator polynomial coefficients, in ascending order of power, of
            the rational polynomial.

               •      Numerator Out —

           Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
            the rational polynomial that results from the mathematical operation.

               •      Denominator Out —

           Denominator Out returns the denominator polynomial coefficients, in ascending order of
            power, of the rational polynomial that results from the mathematical operation. If Numerator is
             0, the VI sets Denominator Out to 1.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   RemoveRemove ResidueResidue fromfrom DenominatorDenominator (CDB)(CDB) VIVI

      Removes the residue from the denominator if the numerator equals zero. The data
       types you wire to the Numerator and Denominator inputs determine the polymorphic
       instance to use.


      Inputs/Outputs

               •      Numerator —

           Numerator contains the numerator polynomial coefficients, in ascending order of power, of the
              rational polynomial.

               •      Denominator —

           Denominator contains the denominator polynomial coefficients, in ascending order of power, of


4108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4109 ordinal=4109 -->
## Functions

Functions


    the rational polynomial.

   •      Numerator Out —

    Numerator Out returns the numerator polynomial coefficients, in ascending order of power, of
    the rational polynomial that results from the mathematical operation.

   •      Denominator Out —

    Denominator Out returns the denominator polynomial coefficients, in ascending order of
    power, of the rational polynomial that results from the mathematical operation. If Numerator is
    0, the VI sets Denominator Out to 1.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D1D RationalRational PolynomialPolynomial EvaluationEvaluation

Evaluates a rational polynomial at the points you specify in A. P(x) and Q(x) specify the
numerator and denominator polynomial coefficients, respectively. The data types you
wire to the P(x) and Q(x) inputs determine the polymorphic instance to use.


  • 1D Rational Polynomial Evaluation (DBL) VI
  • 1D Rational Polynomial Evaluation (CDB) VI
1D1D RationalRational PolynomialPolynomial EvaluationEvaluation (DBL)(DBL) VIVI

Evaluates a rational polynomial at the points you specify in A. P(x) and Q(x) specify the
numerator and denominator polynomial coefficients, respectively. The data types you
wire to the P(x) and Q(x) inputs determine the polymorphic instance to use.


                                                    © National Instruments 4109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4110 ordinal=4110 -->
## Functions

Functions


      Inputs/Outputs

               •       P(x) —

             P(x) contains the numerator polynomial coefficients, in ascending order of power.

               •      Q(x) —

            Q(x) contains the denominator polynomial coefficients, in ascending order of power.

               •     A —

          A is an array of real values.

               •      P(A)/Q(A) —

            P(A)/Q(A) returns the result of the rational polynomial evaluation at the points in A.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   1D1D RationalRational PolynomialPolynomial EvaluationEvaluation (CDB)(CDB) VIVI

       Evaluates a rational polynomial at the points you specify in A. P(x) and Q(x) specify the
      numerator and denominator polynomial coefficients, respectively. The data types you
       wire to the P(x) and Q(x) inputs determine the polymorphic instance to use.


      Inputs/Outputs

               •       P(x) —


4110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4111 ordinal=4111 -->
## Functions

Functions


    P(x) contains the numerator polynomial coefficients, in ascending order of power.

   •      Q(x) —

    Q(x) contains the denominator polynomial coefficients, in ascending order of power.

   •     A —

   A is an array of complex values.

   •      P(A)/Q(A) —

    P(A)/Q(A) returns the result of the rational polynomial evaluation at the points in A.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


nthnth DerivativeDerivative ofof RationalRational PolynomialPolynomial

Calculates the nth order derivative of a rational polynomial. The data types you wire to
the P(x) and Q(x) inputs determine the polymorphic instance to use.


  • nth Derivative of Rational Polynomial (DBL) VI
  • nth Derivative of Rational Polynomial (CDB) VI
nthnth DerivativeDerivative ofof RationalRational PolynomialPolynomial (DBL)(DBL)
VIVI

Calculates the nth order derivative of a rational polynomial. The data types you wire to
the P(x) and Q(x) inputs determine the polymorphic instance to use.


                                                    © National Instruments 4111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4112 ordinal=4112 -->
## Functions

Functions


      Inputs/Outputs

               •       P(x) —

             P(x) contains the numerator polynomial coefficients, in ascending order of power.

               •      Q(x) —

            Q(x) contains the denominator polynomial coefficients, in ascending order of power.

               •      order —

            order specifies the derivative order. If order is less than zero, the VI sets Numerator
             d[P(x)/Q(x)]/dx and Denominator d[P(x)/Q(x)]/dx to empty arrays and returns an error.

               •      Numerator d[P(x)/Q(x)]/dx —

           Numerator d[P(x)/Q(x)]/dx returns the numerator polynomial coefficients, in ascending order of
            power, of the nth order derivative of the rational polynomial.

               •      Denominator d[P(x)/Q(x)]/dx —

           Denominator d[P(x)/Q(x)]/dx returns the denominator polynomial coefficients, in ascending
            order of power, of the nth order derivative of the rational polynomial.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

   nthnth DerivativeDerivative ofof RationalRational PolynomialPolynomial (CDB)(CDB)
    VIVI

       Calculates the nth order derivative of a rational polynomial. The data types you wire to
       the P(x) and Q(x) inputs determine the polymorphic instance to use.


4112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4113 ordinal=4113 -->
## Functions

Functions


Inputs/Outputs

   •       P(x) —

    P(x) contains the numerator polynomial coefficients, in ascending order of power.

   •      Q(x) —

    Q(x) contains the denominator polynomial coefficients, in ascending order of power.

   •      order —

    order specifies the derivative order. If order is less than zero, the VI sets Numerator
    d[P(x)/Q(x)]/dx and Denominator d[P(x)/Q(x)]/dx to empty arrays and returns an error.

   •      Numerator d[P(x)/Q(x)]/dx —

    Numerator d[P(x)/Q(x)]/dx returns the numerator polynomial coefficients, in ascending order of
    power, of the nth order derivative of the rational polynomial.

   •      Denominator d[P(x)/Q(x)]/dx —

    Denominator d[P(x)/Q(x)]/dx returns the denominator polynomial coefficients, in ascending
    order of power, of the nth order derivative of the rational polynomial.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


PartialPartial FractionFraction ExpansionExpansion

Calculates the partial fraction expansion of a polynomial using the Heaviside cover-up
method.


                                                    © National Instruments 4113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4114 ordinal=4114 -->
## Functions

Functions


      Inputs/Outputs

               •      Numerator —

           Numerator contains the rational polynomial coefficients, in ascending order of power, for the
           numerator polynomial.

               •      Denominator —

           Denominator contains the rational polynomial coefficients, in ascending order of power, for the
           denominator polynomial.

               •      tolerance —

            tolerance defines a level for multiplicity.

               •      option —

            option specifies how the VI handles the co-factors of Numerator and Denominator.

                    If option is Cancel Co-factors, this VI performs polynomial GCD of Numerator and Denominator
                  first. If option is Reserve Co-factors, this VI keeps Denominator unchanged.

           0   Cancel Co-factors
           1   Reserve Co-factors (default)

               •       Multiplicity —

              Multiplicity returns the number of times each root in Poles occurs. Multiplicity occurs when the
             difference between two elements in Poles is less than tolerance.

               •      Polynomial —

           Polynomial returns the coefficients, in ascending order of power, for the quotient polynomial
             that results from the division of Numerator by Denominator.

               •      Poles —


4114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4115 ordinal=4115 -->
## Functions

Functions


    Poles returns the unique roots of Denominator. The roots of Denominator result from removing
      all common factors between Numerator and Denominator.

   •      Residues —

    Residues returns the numerators of the partial fractions that result for each pole.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


CreateCreate PolynomialPolynomial FromFrom PFEPFE

Uses partial fraction expansion to reconstruct a rational polynomial.


Inputs/Outputs

   •       Multiplicity —

     Multiplicity specifies the number of times each root in Poles occurs.

    Use the Partial Fraction Expansion VI to obtain the Multiplicity. If Multiplicity is empty, the VI
     calculates the number of nonzero elements in each row of Residues and regards that number as
    the multiplicity of the corresponding pole.

   •      Polynomial —

    Polynomial contains the coefficients for the quotient polynomial in ascending order of power.

    Use the Partial Fraction Expansion VI to obtain the Polynomial.

   •      Poles —

    Poles contains the unique roots of Denominator.


                                                    © National Instruments 4115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4116 ordinal=4116 -->
## Functions

Functions


           Use the Partial Fraction Expansion VI to obtain the Poles.

               •      Residues —

           Residues contains the numerators of the partial fractions that result for each pole.

           Use the Partial Fraction Expansion VI to obtain the Residues.

               •      option —

            option specifies how the VI handles the co-factors of Numerator and Denominator.

                    If option is Cancel Co-factors, this VI performs polynomial GCD of Numerator and Denominator
                  first. If option is Reserve Co-factors, this VI keeps Denominator unchanged.

           0   Cancel Co-factors
           1   Reserve Co-factors (default)

               •      Numerator —

           Numerator returns the rational polynomial coefficients, in ascending order of power, for the
           numerator polynomial.

               •      Denominator —

           Denominator returns the rational polynomial coefficients, in ascending order of power, for the
           denominator polynomial.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI uses the following equation to reconstruct the rational polynomial:


      where P(x) is Numerator, Q(x) is Denominator, A(x) is Polynomial, nis the number of
      elements in Poles, ri is the ith element in Poles, mi is the ith element in Multiplicity,


4116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4117 ordinal=4117 -->
## Functions

Functions

and aik is the (i, k)th element in Residues.

The following block diagram shows how to use the Create Polynomial From PFE VI to
reconstruct a rational polynomial from the Partial Fraction Expansion VI.


ScriptsScripts && FormulasFormulas

Use the Scripts & Formulas VIs to evaluate mathematical formulae and expressions on
the block diagram.

The nodes on this palette can return mathematics error codes.


 Palette            Description Object

            Evaluates mathematical formulas and expressions similar to C on the block diagram.
           The following built-in functions are allowed in formulas: abs, acos, acosh, asin, asinh,
 Formula    atan, atan2, atanh, ceil, cos, cosh, cot, csc, exp, expm1, floor, getexp, getman, int, intrz,
 Node        ln, lnp1, log, log2, max, min, mod, pow, rand, rem, sec, sign, sin, sinc, sinh, sizeOfDim,
              sqrt, tan, tanh. There are some differences between the parser in the Mathematics VIs
          and the Formula Node.

           Use the script nodes to parse formulas, which are in the form of a string, and convert
 Script
            the formula strings to a form that can be used for evaluating results. The script nodes
 Nodes
           use a variety of routines to handle the formulas.


                                                    © National Instruments 4117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4118 ordinal=4118 -->
## Functions

Functions


         Palette                    Description
        Object

                  Uses a calculator interface to create mathematical formulas. You can use this Express VI        Formula                     to perform most math functions that a basic scientific calculator can compute.


        Formula   Use the Formula Parsing VIs to interpret input strings as formulas, transform the
         Parsing     formulas into numeric calculations, and return the results.

                  Use the Expression Node to calculate expressions that contain a single variable. The
         Expression  following built-in functions are allowed in formulas: abs, acos, acosh, asin, asinh, atan,
       Node       atanh, ceil, cos, cosh, cot, csc, exp, expm1, floor, getexp, getman, int, intrz, ln, lnp1, log,
                      log2, max, min, mod, rand, rem, sec, sign, sin, sinc, sinh, sizeOfDim, sqrt, tan, tanh.

                  Use the 1D & 2D Evaluation VIs to examine 1D and 2D functions given in symbolic form,
       1D & 2D                  where parameterization is allowed. You can numerically calculate extrema and partial         Evaluation                       derivatives.


         Calculus   Use the Calculus VIs for calculus and to solve differential equations.


                  Use the Zeros VIs to find the zeros of 1D or n-dimension, linear or nonlinear functions        Zeros
                    or systems of functions.


     FormulaFormula NodeNode

       Evaluates mathematical formulas and expressions similar to C on the block diagram.
      The following built-in functions are allowed in formulas: abs, acos, acosh, asin, asinh,
       atan, atan2, atanh, ceil, cos, cosh, cot, csc, exp, expm1, floor, getexp, getman, int, intrz,
         ln, lnp1, log, log2, max, min, mod, pow, rand, rem, sec, sign, sin, sinc, sinh, sizeOfDim,
        sqrt, tan, tanh. There are some differences between the parser in the Mathematics VIs
      and the Formula Node.

       Refer to Creating Formula Nodes and Formula Node Syntax for more information
      about the Formula Node and the Formula Node syntax. Also, keep in mind the allowed


4118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4119 ordinal=4119 -->
## Functions

Functions

operators in the Formula Node.

Formula Nodes have the following restrictions:

  • Formula Nodes accept only the period (.) as a decimal separator. The nodes do
   not recognize localized decimal separators.
  • Formula Nodes accept only pi as a constant. The constant is case-sensitive.
  • You cannot add Formula Nodes to a VI on which you enable inlining.


ScriptScript NodesNodes

Use the script nodes to parse formulas, which are in the form of a string, and convert
the formula strings to a form that can be used for evaluating results. The script nodes
use a variety of routines to handle the formulas.

The script nodes on this palette can return script node error codes or formula parsing
and mathematics error codes.


 Palette          Description
 Object

           Calls the MATLAB(R) software to execute scripts. You must have a licensed copy of the
 MATLAB MATLAB software version 6.5 or later installed on your computer to use MATLAB script
 script   nodes because the script nodes invoke the MATLAB software script server to execute
 node     scripts written in the MATLAB language syntax. Because LabVIEW uses ActiveX technology
          to implement MATLAB script nodes, they are available only on Windows.

MATLABMATLAB scriptscript nodenode

Calls the MATLAB(R) software to execute scripts. You must have a licensed copy of the
MATLAB software version 6.5 or later installed on your computer to use MATLAB script

                                                    © National Instruments 4119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4120 ordinal=4120 -->
## Functions

Functions

      nodes because the script nodes invoke the MATLAB software script server to execute
        scripts written in the MATLAB language syntax. Because LabVIEW uses ActiveX
       technology to implement MATLAB script nodes, they are available only on Windows.

      Add this node to the block diagram and enter the script. You also can right-click the
      node border to import text into the node. Right-click the node border to add input and
      output terminals. Right-click a terminal to set its data type. When you create a script in
       the MATLAB script node, you must use supported data types.


      Inputs/Outputs

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Scripts and Formulas\MATLAB
        script node - Lorenz Diff Eq.vi
            • labview\examples\Mathematics\Scripts and Formulas\MATLAB
        script node - Fractal.vi

     FormulaFormula

      Uses a calculator interface to create mathematical formulas. You can use this Express
        VI to perform most math functions that a basic scientific calculator can compute.


4120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4121 ordinal=4121 -->
## Functions

Functions


Dialog Box Options

 Option     Description

             Displays the formula as you enter it. You can enter variables and operations into this
 Formula              text box by using the Input buttons or by directly entering a formula.


 Errors      Indicates if the formula is valid.


             Enters a variable (X1-X8) into the formula. Enter a new variable name in the Label text X1
           box associated with the variable to rename the variable.


             Displays the name of the variable. Enter a new variable name in this text box to rename X1 (STR)
            the default variable (X1-X8).


 Home     Moves the cursor to the beginning of the text in the formula text box.


 Backspace  Deletes the last character entered in the formula text box.


 Clear      Completely clears the text in the formula text box.


 End       Moves the cursor to the end of the text in the formula text box.


 e           Enters the value of e into the formula.


                                                    © National Instruments 4121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4122 ordinal=4122 -->
## Functions

Functions


        Option     Description

                     Enters ** into the formula. This operator computes the value of x raised to the y         **
                   power.


         log         Enters log( into the formula. This operator computes the logarithm to the base 10.


         ln          Enters ln( into the formula. This operator computes the natural base e logarithm.


                     Enters mod( into the formula. This operator computes the remainder of x/y, when the      mod
                    quotient is rounded toward –Infinity.


                     Enters min( into the formula. This operator compares two integer values and returns       min
                    the smaller value.


         Pi          Enters the value of Pi into the formula.


         sqrt        Enters sqrt( into the formula. This operator computes the square root.


        log2        Enters log2( into the formula. This operator computes the base-2 logarithm.


        exp        Enters exp( into the formula. This operator computes the value of e raised to a power.


                     Enters rem( into the formula. This operator computes the remainder of x/y, when the       rem
                    quotient is rounded toward –Infinity.


                     Enters max( into the formula. This operator compares two integer values and returns      max
                    the larger value.


4122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4123 ordinal=4123 -->
## Functions

Functions


Option     Description

/           Right parenthesis.


            Enters sin( into the formula. This operator computes the sine of x, where x is insin
            radians.


abs        Enters abs( into the formula. This operation computes the absolute value of x.


*            Left parenthesis.


            Enters cos( into the formula. This operator computes the cosine of x, where x is incos
            radians.


int         Enters int( into the formula. This operation rounds x to the nearest integer.


-            Addition.


            Enters tan( into the formula. This operation computes the tangent of x, where x is intan
            radians.


            Enters sign( into the formula. This operation returns 1 if x is greater than 0, returns 0sign
                   if x is equal to 0, and returns –1 if x is less than 0.


            Enters the decimal separator into the formula. Regardless of the decimal pointer
             settings, this dialog box only uses the period (.) as a decimal separator.Decimal
Point            This Express VI uses the Formula Node, and the Formula Node does not recognize
             localized decimal separators and reserves the comma for another use.


                                                    © National Instruments 4123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4124 ordinal=4124 -->
## Functions

Functions


        Option     Description

       E           Enters the value of e into the formula.


        +            Division.


            (            Multiplication.


            )           Subtraction.


       More       Contains more advanced functions, such as acos, expm1, floor, gamma, and sinc,
        Functions  that you can use in the Formula Express VI.


      Inputs/Outputs

               •       error in (no error) —
            Describes error conditions that occur before this node runs.
               •     X1 —
             (X1-X8) are the input values for the formula you specified in the configuration dialog box.
               •       error out —
            Contains error information. This output provides standard error out functionality.
               •      Result —
            Returns the resulting data based on the configuration of the Express VI.

     Components

       error out passes error or warning information out of a VI to be used by other VIs. Right-
        click the error out indicator on the front panel and select Explain Error or Explain
      Warning from the shortcut menu for more information about the error.

      source string describes the origin of the error or warning. Right-click the error out
       indicator on the front panel and select Explain Error or Explain Warning from the
       shortcut menu for more information about the error.


4124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4125 ordinal=4125 -->
## Functions

Functions

code is the error or warning code. Right-click the error out indicator on the front panel
and select Explain Error or Explain Warning from the shortcut menu for more
information about the error.

status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or
that no error occurred. Right-click the error out indicator on the front panel and select
Explain Error or Explain Warning from the shortcut menu for more information about
the error.

error in can accept error information wired from VIs previously called. Use this
information to decide if any functionality should be bypassed in the event of errors
from other VIs. Right-click the error in control on the front panel and select Explain
Error or Explain Warning from the shortcut menu for more information about the
error.

source describes the origin of the error or warning. Right-click the error in control on
the front panel and select Explain Error or Explain Warning from the shortcut menu
for more information about the error.

code is the error or warning code. Right-click the error in control on the front panel
and select Explain Error or Explain Warning from the shortcut menu for more
information about the error.

status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or
that no error occurred. Right-click the error in control on the front panel and select
Explain Error or Explain Warning from the shortcut menu for more information about
the error.

Enters a variable (X1-X8) into the formula. Enter a new variable name in the Label text
box associated with the variable to rename the variable.

Displays the name of the variable. Enter a new variable name in this text box to rename
the default variable (X1-X8).

Contains more advanced functions, such as acos, expm1, floor, gamma, and sinc,
that you can use in the Formula Express VI.

Enters the value of e into the formula.


                                                    © National Instruments 4125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4126 ordinal=4126 -->
## Functions

Functions

       Enters ** into the formula. This operator computes the value of x raised to the y
      power.

       Enters ln( into the formula. This operator computes the natural base e logarithm.

       Enters exp( into the formula. This operator computes the value of e raised to a power.

       Enters sqrt( into the formula. This operator computes the square root.

       Enters rem( into the formula. This operator computes the remainder of x/y, when the
       quotient is rounded toward –Infinity.

       Enters mod( into the formula. This operator computes the remainder of x/y, when the
       quotient is rounded toward –Infinity.

       Enters log2( into the formula. This operator computes the base-2 logarithm.

       Enters log( into the formula. This operator computes the logarithm to the base 10.

       Enters the value of Pi into the formula.

       Deletes the last character entered in the formula text box.

      Moves the cursor to the end of the text in the formula text box.

      Moves the cursor to the beginning of the text in the formula text box.

       Enters a variable (X1-X8) into the formula. Enter a new variable name in the Label text
      box associated with the variable to rename the variable.

       Enters cos( into the formula. This operator computes the cosine of x, where x is in
       radians.

       Enters tan( into the formula. This operation computes the tangent of x, where x is in
       radians.

       Enters sin( into the formula. This operator computes the sine of x, where x is in
       radians.


4126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4127 ordinal=4127 -->
## Functions

Functions

Enters abs( into the formula. This operation computes the absolute value of x.

Enters int( into the formula. This operation rounds x to the nearest integer.

Enters E into the formula, where E represents the power of 10 exponent.

Enters the decimal separator into the formula. Regardless of the decimal pointer
settings, this dialog box only uses the period (.) as a decimal separator.

Right parenthesis.

Completely clears the text in the formula text box.

Left parenthesis.

Enters sign( into the formula. This operation returns 1 if x is greater than 0, returns 0
if x is equal to 0, and returns –1 if x is less than 0.

Addition.

Subtraction.

Multiplication.

Division.

Enters min( into the formula. This operator compares two integer values and returns
the smaller value.

Enters max( into the formula. This operator compares two integer values and returns
the larger value.

Indicates if the formula is valid.

Displays the formula as you enter it. You can enter variables and operations into this
text box by using the Input buttons or by directly entering a formula.


                                                    © National Instruments 4127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4128 ordinal=4128 -->
## Functions

Functions

     FormulaFormula ParsingParsing

      Use the Formula Parsing VIs to interpret input strings as formulas, transform the
       formulas into numeric calculations, and return the results.

      The VIs on this palette can return formula parsing and mathematics error codes.


         Palette                       Description        Object

         Parse                       Analyzes a string as a formula and produces two numeric arrays. These arrays can be
        Formula                    used by the Eval Parsed Formula String VI.         String

         Parse                       Analyzes Eval Formula Node VI inputs and yields an intermediate state as an input        Formula
                          for the Eval Parsed Formula Node VI.       Node


         Substitute     Substitutes a formula string by given rules. The rules have a parameter name -
         Variables     parameter content structure.


      ParseParse FormulaFormula StringString

       Analyzes a string as a formula and produces two numeric arrays. These arrays can be
      used by the Eval Parsed Formula String VI.


      Inputs/Outputs

               •      formula —


4128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4129 ordinal=4129 -->
## Functions

Functions


    formula is a string representing the formula. The formula can contain any number of valid
     variables.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Parsed Formula —

    Parsed Formula can be wired directly to the corresponding input of the Eval Parsed Formula
     String VI.

         •      Table —

        Table is a 2D array with 3 columns. The first column contains a code that stands for the
         operator. The other two columns contain codes that stand for the operands.

         •      Y Values —

        Y Values is a 1D array of numbers representing a storage of detected and analyzed numbers
         of formula.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Usually, the Parse Formula String VI is used at the beginning of the calculation of
function values. The Eval Parsed Formula String VI completes the calculation. This
division works well if the analyzing process of the Parse Formula String VI finishes
before the calculation processes. Keep this in mind for your own programming.

ParseParse FormulaFormula NodeNode

Analyzes Eval Formula Node VI inputs and yields an intermediate state as an input for
the Eval Parsed Formula Node VI.


                                                    © National Instruments 4129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4130 ordinal=4130 -->
## Functions

Functions


      Inputs/Outputs

               •       Variables Input —

             Variables Input is an array of input strings, each of which represents a valid variable name.

               •       Variables Output —

             Variables Output is an array of output strings, each of which represents a valid variable name.

               •      formula —

           formula is a string consisting of one or more formulas separated by semicolons.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Parsed Formula Node —

           Parsed Formula Node is a cluster containing the following subparameters.

                     •      Y Values —

               Y Values is a 2D array of numbers representing a storage of detected and analyzed numbers
                  of formula.

                     •      Tables —

                Tables is a 3D array with 3 columns. The first column contains a code that stands for the
                 operator. The other two columns contain codes that stand for the operands.

                     •       Variables input decode —

                 Variables input decode is the intermediate and coded state of Variables Input.

                     •       Variables output decode —


4130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4131 ordinal=4131 -->
## Functions

Functions


         Variables output decode is the intermediate and coded state of Variables Output.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


SubstituteSubstitute VariablesVariables

Substitutes a formula string by given rules. The rules have a parameter name -
parameter content structure.


Inputs/Outputs

   •       original formula —

     original formula is a string representing the formula where parameter names stand for
    formulas.

   •      Substitution Rules —

    Substitution Rules is an array of clusters describing the substitution rules.

         •      parameter name —

        parameter name can have any length.

       A parameter name that begins with a capital letter E can produce unpredictable errors, if
         parts of the original string represent numbers like 1E–2. Avoid terms beginning with E in
        such cases.

         •      parameter content —

        parameter content must have a one-to-one relation with parameter name.


                                                    © National Instruments 4131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4132 ordinal=4132 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      formula after substitution —

           formula after substitution is the final formula after all substitution rules are performed.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       For example, the inputs have the following values:

            • original formula: ALPHA*cos(t) + beta

            • Substitution Rules:

        ALPHA → sin(t)

        beta → 2 * t * exp(t)

      The resulting formula after substitution is (sin(t))*cos(t) + (2*t*exp(t)).

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Scripts and Formulas\Street
        Illumination Problem.vi

      ExpressionExpression NodeNode

      Use the Expression Node to calculate expressions that contain a single variable. The
       following built-in functions are allowed in formulas: abs, acos, acosh, asin, asinh, atan,
       atanh, ceil, cos, cosh, cot, csc, exp, expm1, floor, getexp, getman, int, intrz, ln, lnp1, log,
       log2, max, min, mod, rand, rem, sec, sign, sin, sinc, sinh, sizeOfDim, sqrt, tan, tanh.


4132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4133 ordinal=4133 -->
## Functions

Functions


Inputs/Outputs

   •    —

    input is the value that the Expression Node uses as the variable.

   •    —

    output returns the value of the calculation.


Expression Nodes are useful when an expression has only one variable but is otherwise
complicated. Use the correct syntax, operators, and functions when creating
Expression Nodes.

Expression Nodes have the following restrictions:

  • Expression Nodes accept any non-complex numeric data type.
  • Expression Nodes accept only the period (.) as a decimal separator. The nodes do
   not recognize localized decimal separators.
  • Expression Nodes accept only pi as a constant. The constant is case-sensitive.
  • You cannot add Expression Nodes to a VI on which you enable inlining.

1D1D && 2D2D EvaluationEvaluation

Use the 1D & 2D Evaluation VIs to examine 1D and 2D functions given in symbolic form,
where parameterization is allowed. You can numerically calculate extrema and partial
derivatives.

The VIs on this palette can return mathematics error codes.


                                                    © National Instruments 4133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4134 ordinal=4134 -->
## Functions

Functions


         Palette                     Description
        Object

         Eval
        Formula     Interprets a string as a numeric calculation and determines the result.
         String

         Eval
         Single-      Calculates exactly one function value of a given 1D function y = f(x), where f is the
         Variable     function specified by the user formula.
         Scalar

         Eval
         Single-      Calculates an array of function values at given points in a given interval by y[i] = f(x[i])
         Variable     for i = 1, …n, where f is the 1D function given by the user formula.
         Array

         Eval Multi-
         Variable     Calculates exactly one function value based on a given formula.
         Scalar

         Eval Multi-                      Calculates the function values of a given function at an arbitrarily given set of n         Variable
                   dimension points.         Array

         Eval
        Parsed      Takes the output of the Parse Formula String VI and fixes input values to calculate
        Formula    function values.
         String

         Eval         Similar to the Formula Node but with variables that can be entered on the front panel.
        Formula    Refer to Formula Parsing VIs in More Detail for more information on the differences
       Node      between the Eval Formula Node VI and the Formula Node.


         Eval
                    Separates the parsing process from the evaluating process of the Eval Formula Node VI
        Parsed
                 and improves the run-time behavior of a program containing Eval Formula Node VIs at
        Formula
                        different locations.
       Node


                      Calculates the values of a 1D function given by a formula at equidistant points in an
         Eval y=f(x)
                        interval.


4134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4135 ordinal=4135 -->
## Functions

Functions


Palette            Description
Object

Eval y=f(x)
Optimal     Calculates the values of a more complex 1D function given by a formula.
Step

Eval       A generalized version of the Eval y=f(x) VI with the possibility of adding some
y=f(a,x)     parameters into the formula.


Eval             Calculates a 2D array of function values defined on a grid.y=f(x1,x2)

Eval             Calculates a 2D array of function values defined on a grid.y=f(a,x1,x2)

Eval X-Y-
            Describes a surface in 3D with two variables running over two different intervals.Z(t1,t2)

Eval X-Y-            Describes a surface in 3D with two variables running over two different intervals.Z(a,t1,t2)


             Calculates the values of a function (f(t), g(t)), where t runs over an interval. Both
Eval X-Y(t)  components are given by Formulas. The t-values are chosen equidistantly in the
              interval.


Eval X-Y(t)             Calculates the coordinates of a curve by calculating function values of x= f(t) and y=Optimal
              g(t), where truns over an interval.Step


Eval X-      Calculates the (x, y) coordinates of a curve by calculating the parametric function
Y(a,t)       values of x= f(t) and y= g(t), where truns over an interval.


Eval Polar
             Calculates the values of a polar parametric curve in 2D.
to Rect


                                                    © National Instruments 4135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4136 ordinal=4136 -->
## Functions

Functions


         Palette                     Description
        Object

         Eval Polar
         to Rect     Operates like the Eval Polar to Rect VI but with a significantly higher degree of
        Optimal     accuracy.
        Step

       EvalEval FormulaFormula StringString

       Interprets a string as a numeric calculation and determines the result.


      Inputs/Outputs

               •      formula —

           formula is a string representing the calculation without any variables.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      y value —

           y value is the result of the calculation.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following input, formula

     sin(pi(1/2)) + 3*5 - 2

        results in y value 14.00.


4136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4137 ordinal=4137 -->
## Functions

Functions

EvalEval Single-VariableSingle-Variable ScalarScalar

Calculates exactly one function value of a given 1D function y = f(x), where f is the
function specified by the user formula.


Inputs/Outputs

   •      formula —

    formula is a string representing the function under investigation. Only one variable can be
    integrated in this formula.

   •      x value —

    x value is the 1D point, x, at which the value of the function, given by the formula, has to be
     calculated.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      y value —

    y value is the value of formula(x value).

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Refer to the Eval Single-Variable Array VI for an example that applies to the Eval Single-
Variable Scalar VI, except that x value and y value are scalars for the Eval Single-
Variable Scalar VI.

The Eval Single-Variable Scalar VI calculates only one value of a given 1D function. It is
difficult to analyze the formula in the background. Therefore, if you want to calculate a
collection of Eval Single-Variable Scalar VIs, use the Eval Single-Variable Array, Parse

                                                    © National Instruments 4137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4138 ordinal=4138 -->
## Functions

Functions

      Formula String, and Eval Parsed Formula String VIs.

       For an example of using the Eval Single-Variable Scalar VI, enter the following values
      on the front panel:

            • formula: x*sin(x)
            • x value: 2.56

      The resulting y value is 1.41.

       EvalEval Single-VariableSingle-Variable ArrayArray

       Calculates an array of function values at given points in a given interval by y[i] = f(x[i])
        for i = 1, …n, where f is the 1D function given by the user formula.


      Inputs/Outputs

               •      formula —

           formula is a string representing the function under investigation. The formula can contain any
          number of valid variables.

               •     X Values —

          X Values is the given array of input values X[i].

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Y Values —

           Y Values is the 1D array of function values of formula at the given points in the array X Values.
            For example, Y Values = formula (X Values).

               •       error out —


4138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4139 ordinal=4139 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


To calculate the formula y= x² for x= 1, 2, 3, 4, and 5, use the following values for the
input arrays:

  • formula: x^2
  • X Values: [1, 2, 3, 4, 5]

The resulting Y Values output array is [1, 4, 9, 16, 25].

EvalEval Multi-VariableMulti-Variable ScalarScalar

Calculates exactly one function value based on a given formula.


Inputs/Outputs

   •      formula —

    formula is a string representing the formula of n independent Variables. The formula can
    contain any number of valid variables.

   •     X Values —

    X Values is an array of x values corresponding to the n Variables.

   •       Variables —

    Variables is an array of strings representing the n independent variables of the given formula.
    There is a one-to-one relation between Variables and X Values.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 4139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4140 ordinal=4140 -->
## Functions

Functions

               •      y value —

           y value is the value of formula(X Values).

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The VI calculates the function using the following equation.

   y= f(x1, x2, …, xn)

      The following inputs result in y value 3.00:

            • formula: 3*x1 + 4*x2 + x3^2
            • X Values: [1, -1, 2]
            • Variables: [x1, x2, x3]

           Note This VI calculates only one value of a given ndimension function. To
               calculate a collection of function values, use the Eval Multi-Variable Array,
              Parse Formula String, and Eval Parsed Formula String VIs.

       EvalEval Multi-VariableMulti-Variable ArrayArray

       Calculates the function values of a given function at an arbitrarily given set of n
      dimension points.


      Inputs/Outputs

               •      formula —

           formula is a string representing the ndimension function under investigation. The formula can


4140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4141 ordinal=4141 -->
## Functions

Functions


    contain any number of valid variables.

   •     X Values —

    X Values is a 2D array of xvalues. Each row of the array represents the fixed values of each of the
     Variables of the n-dimensional function. The other dimension of the array marks the different
    n-dimension points at which the function has to be calculated.

   •       Variables —

     Variables is an array of strings. Each element of the array stands for a variable name of the
    n-dimension independent terms.

   •       error in (no error) —

     error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Y Values —

    Y Values is the 1D array of the evaluated values Y[i] using formula(X Values).

    Each element of Y Values corresponds to the corresponding column of X Values.

   •       error out —

     error out contains error information. This output provides standard error out functionality.


The VI calculates the function values using the following equation.

yi = f(x1i, x2i, …, xni),

where fis an n-dimensional function given by the formula, and (x1, x2, …, xn) are n
independent variables.

The following inputs result in Y Values [3, 17]:

   • formula: 3*x1 + 4*x2 + x3^2
   • X Values: [1, 0; -1, 4; 2, 1] ([1, -1, 2] are the values for [x1, x2, x3] in the first
    iteration; [0, 4, 1] for the second)

                                                    © National Instruments 4141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4142 ordinal=4142 -->
## Functions

Functions

            • Variables: [x1, x2, x3] for (x1, x2, x3)

       EvalEval ParsedParsed FormulaFormula StringString

      Takes the output of the Parse Formula String VI and fixes input values to calculate
       function values.


      Inputs/Outputs

               •     X Values —

          X Values is an array of x values corresponding to the n Variables.

               •       Variables —

             Variables is an array of strings representing the n independent variables of the given formula.
           There is a one-to-one relation between Variables and X Values.

               •      Parsed Formula —

           Parsed Formula can be wired directly from the corresponding output of the Parse Formula
             String VI.

           Parsed Formula is a cluster containing the following parameters.

                     •      Table —

                Table is a 2D array with 3 columns. The first column contains a code that stands for the
                 operator. The other two columns contain codes that stand for the operands.

                     •      Y Values —

               Y Values is a 1D array of numbers representing a storage of detected and analyzed numbers
                  of the formula input of the Parse Formula String VI.


               •       error in (no error) —


4142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4143 ordinal=4143 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      y value —

    y value is the result of the interpretation process, such as the function value.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


EvalEval FormulaFormula NodeNode

Similar to the Formula Node but with variables that can be entered on the front panel.
Refer to Formula Parsing VIs in More Detail for more information on the differences
between the Eval Formula Node VI and the Formula Node.


Inputs/Outputs

   •      Input Values —

    Input Values is an array of numbers with a one-to-one relation to Variables Input.

   •       Variables Input —

    Variables Input is an array of input strings, each of which represents a valid variable name.

   •       Variables Output —

    Variables Output is an array of output strings, each of which represents a valid variable name.

   •      formula —

    formula is a string consisting of one or more formulas separated by semicolons. Each formula is


                                                    © National Instruments 4143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4144 ordinal=4144 -->
## Functions

Functions


              built up by Variables Input on the right side of an equation and Variables Output on the left
              side. The formulas can contain any number of valid variables.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Output Values —

           Output Values is a 1D array of numbers corresponding to Variables Output and formula. The
          numbers in Output Values represent the results.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The following inputs:

            • formula: y = 3*x + 4*z; p = q^2 - 5;
            • Variables Input: [x, z, q]
            • Input Values: [1,2,3]
            • Variables Output: [y, p]

        result in Output Values [11.00, 4.00].

       EvalEval ParsedParsed FormulaFormula NodeNode

       Separates the parsing process from the evaluating process of the Eval Formula Node VI
      and improves the run-time behavior of a program containing Eval Formula Node VIs at
        different locations.


      Inputs/Outputs

               •      Input Values —

4144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4145 ordinal=4145 -->
## Functions

Functions


  Input Values is an array of numbers, each of which corresponds to the value that is given to each
  of the variables.

  These variables can be input in the Variables Input control of the Parse Formula Node VI. The
  coded form of these variables is available in the Variables input decode parameter of the Parsed
  Formula Node cluster.

•      Parsed Formula Node —

  Parsed Formula Node is a pre-parsed formula string. You can wire the Parsed Formula Node
  cluster directly from the corresponding output of the Parse Formula Node VI.

  Parsed Formula Node is a cluster containing the following parameters.

      •      Y Values —

      Y Values is a 2D array of numbers representing a storage of detected and analyzed numbers
       of formula of the Parse Formula Node VI.

      •      Tables —

      Tables is a 3D array with 3 columns. The first column contains a code that stands for the
       operator. The other two columns contain codes that stand for the operands.

      •       Variables input decode —

       Variables input decode is the intermediate and coded state of Variables Input.

      •       Variables output decode —

       Variables output decode is the intermediate and coded state of Variables Output.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Output Values —

  Output Values is a 1D array of numbers corresponding to Variables Output Decode, Y Values,
  and Tables.

•       error out —

                                                   © National Instruments 4145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4146 ordinal=4146 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


       This VI has a direct connection from the Parse Formula Node VI and completes an Eval
      Formula Node VI calculation. You can wire the Parsed Formula Node input of this VI
        directly from the Parsed Formula Node output of the Parse Formula Node VI.

       EvalEval y=f(x)y=f(x)

       Calculates the values of a 1D function given by a formula at equidistant points in an
        interval.

       For additional accuracy, consider using the Eval y=f(x) Optimal Step VI.


      Inputs/Outputs

               •     number of points —

          number of points is the number of all calculated points. The independent variable is split into
             equidistant subpoints. The default is 10.

               •       start —

              start is the start point of the interval. The default is 0.0.

               •     end —

          end is the end point of the interval. The default is 1.0.

               •      formula —

           formula is a string describing the function under investigation. The formula can contain any
          number of valid variables.

               •     X Values —


4146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4147 ordinal=4147 -->
## Functions

Functions


    X Values is the array of equidistant points between start and end.

   •      Y Values —

    Y Values is the array of function values from the corresponding points of X Values.

   •       ticks —

     ticks is the time in milliseconds to analyze the formula and to produce the X Values and the Y
    Values arrays.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


      Note Use the Bundle function to wire the X Values and Y Values arrays
         directly to an XY Graph, as shown in the following illustration, to view the
        result of this VI.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\1D Explorer.vi
  • labview\examples\Mathematics\Optimization\Sequence of
   Chebyshev Approximations.vi
  • labview\examples\Mathematics\Scripts and Formulas\Street
   Illumination Problem.vi

EvalEval y=f(x)y=f(x) OptimalOptimal StepStep

Calculates the values of a more complex 1D function given by a formula.


                                                    © National Instruments 4147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4148 ordinal=4148 -->
## Functions

Functions

      The values are calculated with higher accuracy than by the Eval y=f(x) VI.


      Inputs/Outputs

               •     number of points —

          number of points is the number of calculated points at the beginning of the execution. The
             default is 10. Usually, many more points will be added.

               •      epsilon —

            epsilon controls the construction of specific points between the start and end points that will be
           used in the calculation.

               •       start —

              start is the start point of the interval under investigation. The default is 0.0.

               •     end —

          end is the end point of the interval. The default is 1.0.

               •      formula —

           formula is a string describing the function under investigation. The formula can contain any
          number of valid variables.

               •     X Values —

          X Values is the array of equidistant points between start and end.

               •      Y Values —

           Y Values is the array of function values from the corresponding points of X Values.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the X Values and the Y


4148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4149 ordinal=4149 -->
## Functions

Functions


    Values arrays.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\1D Explorer.vi

EvalEval y=f(a,x)y=f(a,x)

A generalized version of the Eval y=f(x) VI with the possibility of adding some
parameters into the formula.


Inputs/Outputs

   •     number of points —

   number of points is the number of all calculated points. The independent variable is split into
    equidistant subpoints. The default is 10.

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      Parameters —


                                                    © National Instruments 4149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4150 ordinal=4150 -->
## Functions

Functions


           Parameters is an array of clusters describing the parameters.

                     •     name —

            name of the parameter that uses the conventions of the Formula Parsing VIs.

                     •      value —

                value is the user-defined value of the parameter.


               •      formula —

           formula is a string describing the function under investigation. The formula can contain any
          number of valid variables.

               •     X —

          X is the array of equidistant points between start and end.

               •      Y —

           Y is the function values at the points X.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the X and the Y array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       EvalEval y=f(x1,x2)y=f(x1,x2)

       Calculates a 2D array of function values defined on a grid.


4150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4151 ordinal=4151 -->
## Functions

Functions


Inputs/Outputs

   •     number of points —

   number of points describes the number of grid points for both variables. The default is 25.

   •       Start —

     Start specifies the start points of both variables, that is, an array of length 2. The default values
    are (0, 0).

   •     End —

   End specifies the end points of both variables, that is, an array of length 2. The default values are
     (1, 1).

   •      formula —

    formula is a string representing a function definition of exactly two different variables. The
    formulas can contain any number of valid variables.

   •       Variables —

    Variables is an array of two strings representing the two variables with respect to the naming
    conventions of the Formula Parsing VIs. The default variables are (x1, x2).

   •     X1 Values —

    X1 Values is a 1D array of the used x1 arguments.

   •     X2 Values —

    X2 Values is a 1D array of the used x2 arguments.

   •      Y Values —

    Y Values is the resulting 2D array of the function values.

   •       error —


                                                    © National Instruments 4151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4152 ordinal=4152 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.


      The following illustration shows the visualization of the function

       f(x1, x2) = sin(3*x1) * cos(3*x2)

        in the interval

        (–2, 2) × (–2, 2).


       EvalEval y=f(a,x1,x2)y=f(a,x1,x2)

       Calculates a 2D array of function values defined on a grid.


4152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4153 ordinal=4153 -->
## Functions

Functions

Inputs/Outputs

   •     number of points —

   number of points describes the number of grid points for both variables. The default is 25.

   •       Start —

     Start specifies the start points of both variables, that is, an array of length 2. The default values
    are (0, 0).

   •     End —

   End specifies the end points of both variables, that is, an array of length 2. The default values are
     (1, 1).

   •      Parameters —

    Parameters is an array of clusters describing the parameters.

         •     name —

      name of the parameter that uses the conventions of the Formula Parsing VIs.

         •      value —

        value is the user-defined value of the parameter.


   •      formula —

    formula is a string describing a function, where both variables and parameters can be used. The
    formula can contain any number of valid variables.

   •       Variables —

    Variables is an array of two strings representing the two variables with respect to the naming
    conventions of the Formula Parsing VIs. The default variables are (x1, x2).

   •     X1 Values —

    X1 Values is a 1D array of the used x1 arguments.

   •     X2 Values —


                                                    © National Instruments 4153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4154 ordinal=4154 -->
## Functions

Functions


          X2 Values is a 1D array of the used x2 arguments.

               •      Y Values —

           Y Values is the resulting 2D array of the function values.

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      Use this VI to integrate an arbitrary set of parameters where any parameter gets its
       value with the help of an element of an array of parameter clusters on the front panel.

      The function

        f(a, b, x1, x2) = a*sinc(gamma(x1 + x2)) – b*sin(x1)*cos(x2)

       with a= 1 and b= 2 is a common function in x1 and x2. The variables aand bstand for
       Parameters. Only the right hand side of this equation needs to be entered on the
      Formula control. Thus enter the following values on the front panel:

            • Parameters:
     ◦ parameters(0)a: 1.00
     ◦ parameters(1)b: 2.00
            • formula: a*sinc(gamma(x1 + x2)) – b*sin(x1)*cos(x2)

       EvalEval X-Y-Z(t1,t2)X-Y-Z(t1,t2)

       Describes a surface in 3D with two variables running over two different intervals.


4154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4155 ordinal=4155 -->
## Functions

Functions


Inputs/Outputs

   •     number of points —

   number of points describes the number of grid points for both variables. The default is 25.

   •       Start —

     Start specifies the start points of both variables, that is, an array of length 2. The default values
    are (0, 0).

   •     End —

   End specifies the end points of both variables, that is, an array of length 2. The default values are
     (1, 1).

   •      Formulas —

    Formulas is an array of three strings describing the three functions. Each of the functions
    represents a component of the surface under investigation. The formulas can contain any
   number of valid variables.

   •       Variables —

    Variables is an array of two strings representing the two variables with respect to the naming
    conventions of the Formula Parsing VIs. The default variables are (t1, t2).

   •     X —

    X is the array of the x values at the grid points defined by the parameters.

   •      Y —

    Y is the array of the y values at the grid points defined by the parameters.

   •     Z —

    Z is the array of the z values at the grid points defined by the parameters.

   •       error —

                                                    © National Instruments 4155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4156 ordinal=4156 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.


      The following equations describe a part of the unit sphere in 3D:

       x(t1, t2) = sin(t1)

       y(t1, t2) = cos(t1)sin(t2)

       z(t1, t2) = cos(t1)cos(t2)

        In the Formulas control, only the right hand side of the previous three equations
      needs to be entered.

       EvalEval X-Y-Z(a,t1,t2)X-Y-Z(a,t1,t2)

       Describes a surface in 3D with two variables running over two different intervals.


      Inputs/Outputs

               •     number of points —

          number of points describes the number of grid points for both variables. The default is 25.

               •       Start —

             Start specifies the start points of both variables, that is, an array of length 2. The default values
            are (0, 0).


4156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4157 ordinal=4157 -->
## Functions

Functions

•     End —

  End specifies the end points of both variables, that is, an array of length 2. The default values are
   (1, 1).

•      Parameters —

  Parameters is an array of clusters describing the parameters.

      •     name —

     name of the parameter that uses the conventions of the Formula Parsing VIs.

      •      value —

      value is the user-defined value of the parameter.


•      Formulas —

  Formulas is an array of three strings describing the three functions. Each of the functions
  represents a component of the surface under investigation. The formulas can contain any
  number of valid variables.

•       Variables —

  Variables is an array of two strings representing the two variables with respect to the naming
  conventions of the Formula Parsing VIs. The default variables are (t1, t2).

•     X —

  X is a 1D array of the x values at the grid points. These values are calculated on a 2D grid defined
  by the discrete values of the Variables, usually t[1] and t[2]. The size of X is given by number of
  points.

•      Y —

  Y is a 1D array of the y values at the grid points. These values are calculated on a 2D grid defined
  by the discrete values of the Variables, usually t[1] and t[2]. The size of Y is given by number of
  points.

•     Z —

  Z is a 1D array of the z values at the grid points. These values are calculated on a 2D grid defined


                                                   © National Instruments 4157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4158 ordinal=4158 -->
## Functions

Functions


           by the discrete values of the Variables, usually t[1] and t[2]. The size of Z is given by number of
             points.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.


      Use this VI to integrate an arbitrary set of parameters, where any parameter gets its
       value with the help of an element of an array of parameter clusters on the front panel.

      As an example, consider the ellipsoid given by


      Choosing the parameter values in the Parameters cluster as a= 1, b= 2, and c= 3, you
      can input the following three equations in the Formulas control on the front panel to
       get the X, Y and Z values of the ellipsoid.

     a*cos(t1) b*sin(t1)*sin(t2) c*sin(t1)*cos(t2)
       EvalEval X-Y(t)X-Y(t)

       Calculates the values of a function (f(t), g(t)), where t runs over an interval. Both
      components are given by Formulas. The t-values are chosen equidistantly in the
        interval.

      To obtain more accurate output values, consider using the Eval X-Y(t) Optimal Step VI.


4158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4159 ordinal=4159 -->
## Functions

Functions

Inputs/Outputs

   •     number of points —

   number of points is the number of all calculated points. The independent variable is split into
    equidistant subpoints. The default is 10.

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      Formulas —

    Formulas is an array of two strings describing the two function components f(t) and g(t). The
    formula can contain any number of valid variables.

   •     X —

    X is the array of the values of the first component, r(phi)cos(phi).

   •      Y —

    Y is the array of the values of the second component, r(phi)sin(phi).

   •       ticks —

     ticks is the time in milliseconds to analyze the formula and to produce the X and the Y array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The functions t*sin(t), sqrt((t)*cos(t)) describe a curve in the plane, with tranging
between (0, 12). The following illustration shows this curve.

Enter the data on the front panel as shown:

  • number of points: 100

                                                    © National Instruments 4159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4160 ordinal=4160 -->
## Functions

Functions

            •  start: 0
            • end: 12
            • Formulas: (t*sin(t), sqrt(t)*cos(t) )


       EvalEval X-Y(t)X-Y(t) OptimalOptimal StepStep

       Calculates the coordinates of a curve by calculating function values of x= f(t) and y=
        g(t), where truns over an interval.

       This VI produces more accurate output values than the Eval X-Y(t) VI.


      Inputs/Outputs

               •     number of points —

          number of points is the number of calculated points at the beginning of the execution. The
             default is 10. Usually, many more points will be added.

               •      epsilon —

4160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4161 ordinal=4161 -->
## Functions

Functions


    epsilon controls the construction of points in between. The default is 0.05.

   •       start —

     start is the start point of the interval under investigation. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      Formulas —

    Formulas is an array of two strings describing the two function components f(t) and g(t). The
    formula can contain any number of valid variables.

   •     X —

    X returns the values of the x-coordinates of the curve. The values are obtained by calculating the
    function values of f(t)in Formulas.

   •      Y —

    Y returns the values of the y-coordinates of the curve. The values are obtained by calculating the
    function values of g(t)in Formulas.

   •       ticks —

     ticks is the time in milliseconds to analyze the formula and to produce the X and the Y array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


EvalEval X-Y(a,t)X-Y(a,t)

Calculates the (x, y) coordinates of a curve by calculating the parametric function
values of x= f(t) and y= g(t), where truns over an interval.


                                                    © National Instruments 4161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4162 ordinal=4162 -->
## Functions

Functions


      Inputs/Outputs

               •     number of points —

          number of points is the number of all calculated points. The independent variable is split into
             equidistant subpoints. The default is 10.

               •       start —

              start is the start point of the interval under investigation. The default is 0.0.

               •     end —

          end is the end point of the interval. The default is 1.0.

               •      Parameters —

           Parameters is an array of clusters describing the parameters.

                     •     name —

            name of the parameter that uses the conventions of the Formula Parsing VIs.

                     •      value —

                value is the user-defined value of the parameter.


               •      Formulas —

           Formulas is an array of two strings describing the two function components f(t) and g(t). The
            formula can contain any number of valid variables.

               •     X —

          X returns the values of the x-coordinates of the curve. The values are obtained by calculating the
             function values of f(t)in Formulas.

               •      Y —


4162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4163 ordinal=4163 -->
## Functions

Functions


    Y returns the values of the y-coordinates of the curve. The values are obtained by calculating the
    function values of g(t)in Formulas.

   •       ticks —

     ticks is the time in milliseconds to analyze the formula and to produce the X and the Y array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


EvalEval PolarPolar toto RectRect

Calculates the values of a polar parametric curve in 2D.


Inputs/Outputs

   •     number of points —

   number of points is the number of all calculated points. The independent variable is split into
    equidistant subpoints. The default is 10.

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      radius as function of angle —

    radius as function of angle is a string representing the formula


                                                    © National Instruments 4163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4164 ordinal=4164 -->
## Functions

Functions


       r= r(phi). The formula can contain any number of valid variables.

               •     X —

          X is the array of the values of the first component, r(phi)cos(phi).

               •      Y —

           Y is the array of the values of the second component, r(phi)sin(phi).

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the X and the Y array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let φbe the angle and r(φ) the radius in polar coordinate notation. Then it is:

    x= r(φ)cos φy= r(φ)sin φ

      where φruns over the interval.

      The function

        r(t) = exp(cos(t)) – 2*cos(4*t) + sin(t/12)5

       describes a butterfly curve in the plane in polar coordinates, as shown in the following
        illustration. You can generate the illustration by entering the following values on the
       front panel:

            • number of points: 1000
            •  start: 0
            • end: 30
            • radius as function of angle: exp(cos(t))-2*cos(4*t)+sin(t/12)^5


4164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4165 ordinal=4165 -->
## Functions

Functions


EvalEval PolarPolar toto RectRect OptimalOptimal StepStep

Operates like the Eval Polar to Rect VI but with a significantly higher degree of
accuracy.


Inputs/Outputs

   •     number of points —

   number of points is the number of calculated points at the beginning of the execution. The
     default is 10. Usually, many more points will be added.

   •      epsilon —

    epsilon controls the construction of points in between. The default is 0.05.

   •       start —

     start is the start point of the interval under investigation. The default is 0.0.


                                                    © National Instruments 4165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4166 ordinal=4166 -->
## Functions

Functions

               •     end —

          end is the end point of the interval. The default is 1.0.

               •      radius as function of angle —

            radius as function of angle is a string representing the formula

       r= r(phi). The formula can contain any number of valid variables.

               •     X —

          X is the array of the values of the first component, r(phi)cos(phi).

               •      Y —

           Y is the array of the values of the second component, r(phi)sin(phi).

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the X and the Y array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

      CalculusCalculus

      Use the Calculus VIs for calculus and to solve differential equations.

      The VIs on this palette can return mathematics error codes.


         Palette Object  Description

                         Calculates both the function values and the integral of a 1D function between start
         Integration
                    and end. The function is defined by a formula. The number of points to be


4166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4167 ordinal=4167 -->
## Functions

Functions


 Palette Object  Description

                calculated depends on the complexity of the given function.


                Calculates both function values and the values of the derivative of a given 1D Differentiation                function defined by a formula at equidistant points in an interval.


 Limit          Determines the left and right limits of a 1D function at a given point.


 Curve Length   Calculates the curve length of a 1D function between start and end.


 Partial                Calculates a 2D array of the partial derivatives of a function of two independent Derivatives of                  variables.
 f(x1,x2)


             The algorithm looks for local extrema of a given function of two variables on a Extrema of                given rectangle. The absolute distance between two extrema must be equal to or
 f(x1,x2)                 greater than 1E–6 for the two vectors to register as different from each other.


 Zeros and               Determines all zeros and extrema of a 1D function in a given interval. Extrema of f(x)

IntegrationIntegration

Calculates both the function values and the integral of a 1D function between start and
end. The function is defined by a formula. The number of points to be calculated
depends on the complexity of the given function.


                                                    © National Instruments 4167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4168 ordinal=4168 -->
## Functions

Functions

      Inputs/Outputs

               •       start —

              start is the start point of the interval. The default is 0.0.

               •     end —

          end is the end point of the interval. The default is 1.0.

               •      formula —

           formula is a string describing the function under investigation. The formula can contain any
          number of valid variables.

               •     X Values —

          X Values is the array of all regarded points in the interval (start, end).

               •      Y Values —

           Y Values are the values of the function.

               •       Integral of Y —

             Integral of Y are the values of the integral of formula between start and end at all X Values
             values.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the X Values array and
            the Integral of Y array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let f(t)be the given function. The calculation of


4168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4169 ordinal=4169 -->
## Functions

Functions

can be reformulated as an ordinary differential equation,

          I(start) = 0

The algorithm is based on this reformulation. The VI uses the Runge Kutta method for
accuracy.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\1D Explorer.vi

DifferentiationDifferentiation

Calculates both function values and the values of the derivative of a given 1D function
defined by a formula at equidistant points in an interval.


Inputs/Outputs

   •     number of points —

   number of points is the number of all calculated points. The independent variable is split into
    equidistant subpoints. The default is 10.

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      formula —


                                                    © National Instruments 4169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4170 ordinal=4170 -->
## Functions

Functions


           formula is a string describing the function under investigation. The formula can contain any
          number of valid variables.

               •     X Values —

          X Values is the array of equidistant points between start and end.

               •      Y Values —

           Y Values are the values of the function.

               •       Derivative of Y —

             Derivative of Y are the values of the derivative of the function at the points X Values.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the X Values array, Y
            Values array, and Derivative of Y array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           Note Even though there is a modified method called optimal step for
               functions, LabVIEW does not have an optimal step for the Differentiation VI. If
            you are interested in highly accurate values of differentiation, start with the
              symbolic differentiation by hand. Then use the Eval y = f(x) Optimal Step VI,
            where fis the derivative of the function.

      The function and the derivative of f(x) = sin(sinc(x)) are investigated in the interval
        (–20, 20). The following illustration shows both f(x)and f'(x).


4170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4171 ordinal=4171 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\1D Explorer.vi

LimitLimit

Determines the left and right limits of a 1D function at a given point.


Inputs/Outputs

   •      point —

    point is the point at which the limits have to be calculated. The default is 0.0.

   •       delta —

    delta is the distance to the left and right neighbor of point. The default is 1E–10.

   •      formula —

    formula is a string describing the function under investigation. The formula can contain any
   number of valid variables.


                                                    © National Instruments 4171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4172 ordinal=4172 -->
## Functions

Functions

               •        left limit —

               left limit is the left limit of the given function at point. The accuracy is up to 8 decimal digits.

               •       right limit —

             right limit is the right limit of the given function at point. The accuracy is up to 8 decimal digits.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce limits.

             Usually, the time is negligible for the limit operations.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The algorithm calculates only the two values f(point–delta) and f(point + delta).
       Furthermore, delta is internally rounded to a power of 2.

           Note A very small delta value can result in numerical inaccuracies. You
              should take a value of delta = 1E–10 in all cases.

      The function

        f(x) = (1 + 1/x)x

      has the famous limit e(Euler) if xtends to infinity. You can use the Limit VI to
      determine the Euler number if you define

       g(x) = (1 + x)(1/x)

        for small positive x. By entering

     (1+x)^(1/x)


4172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4173 ordinal=4173 -->
## Functions

Functions

in the formula control on the front panel, you can find the limit. The following
illustration shows the convergence of f(x)to e.


CurveCurve LengthLength

Calculates the curve length of a 1D function between start and end.


Inputs/Outputs

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      formula —

    formula is a string describing the function under investigation. The formula can contain any
   number of valid variables.

   •     X Values —

    X Values is the array of all regarded points in the interval (start, end).


                                                    © National Instruments 4173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4174 ordinal=4174 -->
## Functions

Functions

               •      Curve Length —

           Curve Length is an array of the values of the curve length of formula between start and end at
                all X Values.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the X Values array and
            the Curve Length array.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The VI calculates Curve Length of a given function f(t) between start and end using the
       following equation.


      The VI implements this calculation using the Integration VI, which is why the
       calculations are based on the Runge Kutta method.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\1D Explorer.vi

       PartialPartial DerivativesDerivatives ofof f(x1,x2)f(x1,x2)

       Calculates a 2D array of the partial derivatives of a function of two independent
        variables.


4174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4175 ordinal=4175 -->
## Functions

Functions


Inputs/Outputs

   •     number of points —

   number of points describes the number of grid points for both variables. The default is 25.

   •       Start —

     Start specifies the start points of both variables, that is, an array of length 2. The default values
    are (0, 0).

   •     End —

   End specifies the end points of both variables, that is, an array of length 2. The default values are
     (1, 1).

   •       derivative —

    derivative specifies which partial derivative is calculated. A value of 0 represents the partial
     derivative of the first variable. A value of 1 represents the partial derivative of the second
     variable.

   •      formula —

    formula is a string describing the function. The formula can contain any number of valid
     variables.

   •       Variables —

    Variables is an array of two strings representing the two variables with respect to the naming
    conventions of the Formula Parsing VIs. The default variables are (x1, x2).

   •     X1 Values —

    X1 Values is the resulting 1D array.

   •     X2 Values —


                                                    © National Instruments 4175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4176 ordinal=4176 -->
## Functions

Functions


          X2 Values is the resulting 1D array.

               •       Partial derivative of f(x1,x2) —

             Partial derivative of f(x1,x2) is the 2D array of the fixed partial derivative at the defined grid
             points.

            For a derivative of 0, the function df(x1, x2)/dx1 is calculated. For a derivative of 1 the function
            df(x1, x2)/dx2 is calculated.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.


      The x1-derivative of the function

        f(x1, x2) = sin(x1² – x2) – cos(sin(x2) – x1)

         is investigated in the interval (–2, 2) by (–2, 2). The values are obtained by entering the
       following on the front panel:

            • Start: [-2, -2]
            • End: [2, 2]
            • Formula: sin(x1*x1 - x2) - cos(sin(x2) - x1)

      ExtremaExtrema ofof f(x1,x2)f(x1,x2)

      The algorithm looks for local extrema of a given function of two variables on a given
       rectangle. The absolute distance between two extrema must be equal to or greater
      than 1E–6 for the two vectors to register as different from each other.


4176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4177 ordinal=4177 -->
## Functions

Functions


Inputs/Outputs

   •       Start —

     Start specifies the start points of both variables, that is, an array of length 2. The default values
    are (0, 0).

   •     End —

   End specifies the end points of both variables, that is, an array of length 2. The default values are
     (1, 1).

   •      formula —

    formula is a string describing the function. The formula can contain any number of valid
     variables.

   •       Variables —

    Variables is an array of two strings representing the two variables with respect to the naming
    conventions of the Formula Parsing VIs. The default variables are (x1, x2).

   •     number of trials —

   number of trials is the number of randomly chosen 2D starting points of the algorithm.

   •     Minima —

    Minima is a 2D array of all local minima of the given function. Any local minimum is presented by
    two coordinates.

   •     Maxima —

   Maxima is a 2D array of all local maxima of the given function. Any local maximum is presented
    by two coordinates.

   •       ticks —

     ticks is the time effort for the whole calculation of the function values in milliseconds.


                                                    © National Instruments 4177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4178 ordinal=4178 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       While the number of trials can be very large, there is no guarantee you can find all or at
        least one zero, local minimum or local maximum of the given function. Moreover, such
       points do not exist in all cases.

      Though the randomly chosen start points of the extrema algorithm belong to the
         initially given rectangle, sometimes the determined extrema can be found outside of
       the rectangle. In this case, these values will also be presented.

      ZerosZeros andand ExtremaExtrema ofof f(x)f(x)

      Determines all zeros and extrema of a 1D function in a given interval.


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the zeros and the extrema. The default is 1.00E-8.

               •      step type —

            step type controls the spacing used for the function values.

              In general, modified function leads to more accurate zeros and extrema.

           0 fixed function (default)—Represents uniformly spaced function values.
           1 modified function—Represents the optimal step size.


4178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4179 ordinal=4179 -->
## Functions

Functions

•      algorithm —

  algorithm is the method used by the VI.

  0     Ridders (default)
  1    Newton Raphson

•       start —

  start is the start point of the interval under investigation. The default is 0.0.

•     end —

  end is the end point of the interval. The default is 1.0.

•      formula —

  formula is a string representing the function under investigation. The formula can contain any
  number of valid variables.

•     Minima —

  Minima are the determined minimal values of formula.

•      f(Minima) —

  f(Minima) are the function values at Minima.

•      Zeros —

  Zeros are the determined zeros of formula.

•       f(Zeros) —

  f(Zeros) contains the function values of Zeros.

  Usually, these values are close to 0.

•     Maxima —

  Maxima are the determined maximal values of formula.

•      f(Maxima) —


                                                   © National Instruments 4179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4180 ordinal=4180 -->
## Functions

Functions


           f(Maxima) are the function values at Maxima.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the Minima, Zeros,
           andMaxima.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

     ZerosZeros

      Use the Zeros VIs to find the zeros of 1D or n-dimension, linear or nonlinear functions
       or systems of functions.

      The VIs on this palette can return mathematics error codes.


         Palette                      Description
        Object

         Find All      Determines all zeros of a 1D function in a given interval. You must manually select the
        Zeros of f(x)  polymorphic instance to use.


       Newton     Determines a zero of a 1D function close to two points with the help of the derivative
       Raphson     of this 1D function. The two values form a search limit for the unknown zero of the 1D
        Zero Finder  function. You must manually select the polymorphic instance to use.


                    Determines a zero of a 1D function in a given interval. The function has to be
         Ridders
                     continuous and has to have different signs at the end points of the interval. You must
        Zero Finder
                    manually select the polymorphic instance to use.


4180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4181 ordinal=4181 -->
## Functions

Functions


 Palette              Description
 Object

 nD
 Nonlinear    Determines the solutions of nonlinear systems of equations in ndimensions
 System      beginning with a starting point in ndimensions. You must manually select the
 Single       polymorphic instance to use.
 Solution

 nD             Determines a set of solutions of a nonlinear system of equations in ndimensions Nonlinear
             beginning with a randomly chosen start point in ndimensions. You must manually System
               select the polymorphic instance to use. Solver


FindFind AllAll ZerosZeros ofof f(x)f(x)

Determines all zeros of a 1D function in a given interval. You must manually select the
polymorphic instance to use.


  • Find All Zeros of f(x) (Formula) VI
  • Find All Zeros of f(x) (VI) VI

To obtain the zeros of sin(sinc(gamma(x))) in the interval (–2, 2), enter the following
values on the front panel:

  •  start: -2.00
  • end: 2.00
  • formula: sin(sinc(gamma(x)))

The following illustration shows the graph and the zeros of sin(sinc(gamma(x))) in the
interval (–2, 2).


                                                    © National Instruments 4181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4182 ordinal=4182 -->
## Functions

Functions


           Note For some functions, Zeros may contain false zeros that are actually
                 singularities. For true zeros, f(Zeros) is close to 0.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\1D Explorer.vi
   FindFind AllAll ZerosZeros ofof f(x)f(x) (Formula)(Formula) VIVI

      Determines all zeros of a 1D function in a given interval. You must manually select the
      polymorphic instance to use.


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the zeros and the extrema. The default is 1.00E-8.

               •      step type —

4182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4183 ordinal=4183 -->
## Functions

Functions


  step type controls the spacing used for the function values.

  In general, modified function leads to more accurate zeros and extrema.

  0 fixed function (default)—Represents uniformly spaced function values.
  1 modified function—Represents the optimal step size.

•      algorithm —

  algorithm is the method used by the VI.

  0     Ridders (default)
  1    Newton Raphson

•       start —

  start is the start point of the interval. The default is 0.0.

•     end —

  end is the end point of the interval. The default is 1.0.

•      formula —

  formula is a string describing the function. The formula can contain any number of valid
  variables.

•      Zeros —

  Zeros are the determined zeros of formula.

•       f(Zeros) —

  f(Zeros) contains the function values of Zeros.

  Usually, these values are close to 0.

•       ticks —

  ticks is the time in milliseconds for the whole calculation.

•       error —


                                                   © National Instruments 4183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4184 ordinal=4184 -->
## Functions

Functions


             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      To obtain the zeros of sin(sinc(gamma(x))) in the interval (–2, 2), enter the following
       values on the front panel:

            •  start: -2.00
            • end: 2.00
            • formula: sin(sinc(gamma(x)))

      The following illustration shows the graph and the zeros of sin(sinc(gamma(x))) in the
        interval (–2, 2).


           Note For some functions, Zeros may contain false zeros that are actually
                 singularities. For true zeros, f(Zeros) is close to 0.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Optimization\1D Explorer.vi


4184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4185 ordinal=4185 -->
## Functions

Functions

FindFind AllAll ZerosZeros ofof f(x)f(x) (VI)(VI) VIVI

Determines all zeros of a 1D function in a given interval. You must manually select the
polymorphic instance to use.


Inputs/Outputs

   •      accuracy —

    accuracy controls the accuracy of the zeros and the extrema. The default is 1.00E-8.

   •      step type —

    step type controls the spacing used for the function values.

     In general, modified function leads to more accurate zeros and extrema.

    0 fixed function (default)—Represents uniformly spaced function values.
    1 modified function—Represents the optimal step size.

   •      algorithm —

    algorithm is the method used by the VI.

    0     Ridders (default)
    1    Newton Raphson

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —


                                                    © National Instruments 4185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4186 ordinal=4186 -->
## Functions

Functions


          end is the end point of the interval. The default is 1.0.

               •        f(x) —

               f(x) is a strictly typed reference to the VI that implements the 1D function.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         zero.llb\Zero Finder f(x) 1D.vit.

               •      data —

           data contains arbitrary values that pass to the VI that implements the function.

               •      Zeros —

            Zeros are the determined zeros of f(x).

               •       f(Zeros) —

             f(Zeros) contains the function values of Zeros.

             Usually, these values are close to 0.

               •       ticks —

             ticks is the time in milliseconds for the whole calculation.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      To obtain the zeros of sin(sinc(gamma(x))) in the interval (–2, 2), enter the following
       values on the front panel:

            •  start: -2.00
            • end: 2.00
            • formula: sin(sinc(gamma(x)))

      The following illustration shows the graph and the zeros of sin(sinc(gamma(x))) in the
        interval (–2, 2).

4186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4187 ordinal=4187 -->
## Functions

Functions


      Note For some functions, Zeros may contain false zeros that are actually
         singularities. For true zeros, f(Zeros) is close to 0.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Optimization\1D Explorer.vi

NewtonNewton RaphsonRaphson ZeroZero FinderFinder

Determines a zero of a 1D function close to two points with the help of the derivative of
this 1D function. The two values form a search limit for the unknown zero of the 1D
function. You must manually select the polymorphic instance to use.


  • Newton Raphson Zero Finder (Formula) VI
  • Newton Raphson Zero Finder (VI) VI

Let fbe the given function. The Newton Raphson Zero Finder VI uses a method that
combines the simple midpoint strategy and the Newton strategy.

  • Midpoint strategy:
  • Newton strategy:


                                                    © National Instruments 4187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4188 ordinal=4188 -->
## Functions

Functions

      where x1 and x2 are given guesses with

        f(x1) · f(x2) < 0

      The following illustration demonstrates the Newton strategy.


   NewtonNewton RaphsonRaphson ZeroZero FinderFinder (Formula)(Formula) VIVI

      Determines a zero of a 1D function close to two points with the help of the derivative of
        this 1D function. The two values form a search limit for the unknown zero of the 1D
       function. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the zero determination. The default is 1.00E-8, which specifies
            the maximum deviation of the calculated solution from the actual solution.

               •     h —

          h is the delta value to calculate the derivative of the given formula. The default is 1E-8.


4188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4189 ordinal=4189 -->
## Functions

Functions

   •       start —

     start is the start point of the interval. The default is 0.0.

   •     end —

    end is the end point of the interval. The default is 1.0.

   •      formula —

    formula is a string representing the function under investigation. The formula can contain any
    number of valid variables.

   •      zero —

    zero is the determined zero of formula. zero is a good approximation only for the exact value.

   •       f(zero) —

     f(zero) is the function value at the point given by zero. The answer should be very close to zero.

   •       ticks —

     ticks is the time effort for the whole calculation of the function values in milliseconds.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let fbe the given function. The Newton Raphson Zero Finder VI uses a method that
combines the simple midpoint strategy and the Newton strategy.

   • Midpoint strategy:
   • Newton strategy:

where x1 and x2 are given guesses with

f(x1) · f(x2) < 0

The following illustration demonstrates the Newton strategy.


                                                    © National Instruments 4189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4190 ordinal=4190 -->
## Functions

Functions


   NewtonNewton RaphsonRaphson ZeroZero FinderFinder (VI)(VI) VIVI

      Determines a zero of a 1D function close to two points with the help of the derivative of
        this 1D function. The two values form a search limit for the unknown zero of the 1D
       function. You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the zero determination. The default is 1.00E-8, which specifies
            the maximum deviation of the calculated solution from the actual solution.

               •     h —

          h is the delta value to calculate the derivative of the given formula. The default is 1E-8.

               •       start —

              start is the start point of the interval. The default is 0.0.

               •     end —


4190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4191 ordinal=4191 -->
## Functions

Functions


    end is the end point of the interval. The default is 1.0.

   •        f(x) —

     f(x) is a strictly typed reference to the VI that implements the 1D function.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   zero.llb\Zero Finder f(x) 1D.vit.

   •      data —

    data contains arbitrary values that pass to the VI that implements the function.

   •      zero —

    zero is the determined zero of f(x). zero is a good approximation for only the exact value.

   •       f(zero) —

     f(zero) is the function value at the point given by zero. The answer should be very close to zero.

   •       ticks —

     ticks is the time effort for the whole calculation of the function values in milliseconds.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let fbe the given function. The Newton Raphson Zero Finder VI uses a method that
combines the simple midpoint strategy and the Newton strategy.

   • Midpoint strategy:
   • Newton strategy:

where x1 and x2 are given guesses with

f(x1) · f(x2) < 0


                                                    © National Instruments 4191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4192 ordinal=4192 -->
## Functions

Functions

      The following illustration demonstrates the Newton strategy.


      RiddersRidders ZeroZero FinderFinder

      Determines a zero of a 1D function in a given interval. The function has to be
       continuous and has to have different signs at the end points of the interval. You must
      manually select the polymorphic instance to use.


            • Ridders Zero Finder (Formula) VI
            • Ridders Zero Finder (VI) VI

      Given the function f(x) with f(a)*f(b) < 0, Ridders' method determines c= (a+ b)/2 and
       calculates the new guess using the following equation:


      The values start, cnew, and end are the base for the new iteration, depending on which
       of the following inequalities is true:

        f(start) · f(cnew) < 0 f(cnew) · f(end) < 0

      The algorithm stops if |a– b| < accuracy.


4192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4193 ordinal=4193 -->
## Functions

Functions

Ridders' method is very fast and reliable.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Scripts and Formulas\Street
   Illumination Problem.vi
RiddersRidders ZeroZero FinderFinder (Formula)(Formula) VIVI

Determines a zero of a 1D function in a given interval. The function has to be
continuous and has to have different signs at the end points of the interval. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      accuracy —

    accuracy controls the accuracy of the zero determination. The default is 1.00E-8.

   •       start —

     start is the leftmost point of the interval. The default is 0.0.

   •     end —

    end is the rightmost point of the interval. The default is 0.0.

   •      formula —

    formula is a string describing the function. The formula can contain any number of valid
     variables.

   •      zero —


                                                    © National Instruments 4193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4194 ordinal=4194 -->
## Functions

Functions


            zero is the determined zero of formula. zero is a good approximation only for the exact value.

               •       f(zero) —

              f(zero) is the function value at the point given by zero. The answer should be very close to zero.

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.

               •       error —

             error returns any error or warning from the VI. When start > end, the application interprets it as
          an error condition. The function values at the points start and end must have different signs to
            guarantee the existence of a zero in (start,end). You can wire error to the Error Cluster From
             Error Code VI to convert the error code or warning into an error cluster.


      Given the function f(x) with f(a)*f(b) < 0, Ridders' method determines c= (a+ b)/2 and
       calculates the new guess using the following equation:


      The values start, cnew, and end are the base for the new iteration, depending on which
       of the following inequalities is true:

        f(start) · f(cnew) < 0 f(cnew) · f(end) < 0

      The algorithm stops if |a– b| < accuracy.

       Ridders' method is very fast and reliable.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Scripts and Formulas\Street
        Illumination Problem.vi


4194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4195 ordinal=4195 -->
## Functions

Functions

RiddersRidders ZeroZero FinderFinder (VI)(VI) VIVI

Determines a zero of a 1D function in a given interval. The function has to be
continuous and has to have different signs at the end points of the interval. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      accuracy —

    accuracy controls the accuracy of the zero determination. The default is 1.00E-8.

   •       start —

     start is the leftmost point of the interval. The default is 0.0.

   •     end —

    end is the rightmost point of the interval. The default is 0.0.

   •        f(x) —

     f(x) is a strictly typed reference to the VI that implements the 1D function.

    Create this VI by starting from the VI template located in labview\vi.lib\gmath\
   zero.llb\Zero Finder f(x) 1D.vit.

   •      data —

    data contains arbitrary values that pass to the VI that implements the function.

   •      zero —

    zero is the determined zero of f(x). zero is a good approximation for only the exact value.

   •       f(zero) —


                                                    © National Instruments 4195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4196 ordinal=4196 -->
## Functions

Functions


              f(zero) is the function value at the point given by zero. The answer should be very close to zero.

               •       ticks —

             ticks is the time effort for the whole calculation of the function values in milliseconds.

               •       error —

             error returns any error or warning from the VI. When start > end, the application interprets it as
          an error condition. The function values at the points start and end must have different signs to
            guarantee the existence of a zero in (start,end). You can wire error to the Error Cluster From
             Error Code VI to convert the error code or warning into an error cluster.


      Given the function f(x) with f(a)*f(b) < 0, Ridders' method determines c= (a+ b)/2 and
       calculates the new guess using the following equation:


      The values start, cnew, and end are the base for the new iteration, depending on which
       of the following inequalities is true:

        f(start) · f(cnew) < 0 f(cnew) · f(end) < 0

      The algorithm stops if |a– b| < accuracy.

       Ridders' method is very fast and reliable.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Scripts and Formulas\Street
        Illumination Problem.vi

     nDnD NonlinearNonlinear SystemSystem SingleSingle SolutionSolution

      Determines the solutions of nonlinear systems of equations in ndimensions beginning

4196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4197 ordinal=4197 -->
## Functions

Functions

with a starting point in ndimensions. You must manually select the polymorphic
instance to use.


   • nD Nonlinear System Single Solution (Formula) VI
   • nD Nonlinear System Single Solution (VI) VI

Let Fbe the ndimension function and let Xbe a given point in ndimensions.

Furthermore, let

f= 0.5F²

The algorithm is looking for such a vector Pthat

F(X+ dP) ≤ F(X)

for all 0 ≤ d≤ 1.

In a second step, an appropriate value, d*, is calculated, so that

F(X+ d*P)

is considerably smaller than F(X). This process is repeated until F(X) ≈ 0 is reached.
What follows is an approximation for F(X) = 0.
nDnD NonlinearNonlinear SystemSystem SingleSingle SolutionSolution
(Formula)(Formula) VIVI

Determines the solutions of nonlinear systems of equations in ndimensions beginning
with a starting point in ndimensions. You must manually select the polymorphic
instance to use.


                                                    © National Instruments 4197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4198 ordinal=4198 -->
## Functions

Functions


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the zero determination. The default is 1.00E-8, which specifies
            the maximum deviation of the calculated solution from the actual solution.

               •     h —

          h is a small distance to calculate derivatives. The default is 1E-8.

               •       Start —

             Start is the start point in ndimension.

               •     X —

          X is an array of strings representing the xvariables. If the array of strings contains the variable t,
            the VI returns an error.

               •       F(X) —

             F(X) is an array of strings defining the functions in ndimensions. The formula can contain any
          number of valid variables.

               •      Zeroes —

           Zeroes contains the determined zeros of F(X).

               •       f(Zeroes) —

             f(Zeroes) contains the function values of Zeroes.

             Usually, these values are close to 0.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the Zeros.


4198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4199 ordinal=4199 -->
## Functions

Functions

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


Let Fbe the ndimension function and let Xbe a given point in ndimensions.

Furthermore, let

f= 0.5F²

The algorithm is looking for such a vector Pthat

F(X+ dP) ≤ F(X)

for all 0 ≤ d≤ 1.

In a second step, an appropriate value, d*, is calculated, so that

F(X+ d*P)

is considerably smaller than F(X). This process is repeated until F(X) ≈ 0 is reached.
What follows is an approximation for F(X) = 0.
nDnD NonlinearNonlinear SystemSystem SingleSingle SolutionSolution (VI)(VI) VIVI

Determines the solutions of nonlinear systems of equations in ndimensions beginning
with a starting point in ndimensions. You must manually select the polymorphic
instance to use.


                                                    © National Instruments 4199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4200 ordinal=4200 -->
## Functions

Functions

      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the zero determination. The default is 1.00E-8, which specifies
            the maximum deviation of the calculated solution from the actual solution.

               •     h —

          h is a small distance to calculate derivatives. The default is 1E-8.

               •       Start —

             Start is the start point in ndimension.

               •      data —

           data contains arbitrary values that pass to the VI that implements the function.

               •       F(X) —

             F(X) is a strictly typed reference to the VI that implements the function.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\
         zero.llb\Zero Finder f(x) nD.vit.

               •      Zeroes —

           Zeroes contains the determined zeros of F(X).

               •       f(Zeroes) —

             f(Zeroes) contains the function values of Zeroes.

             Usually, these values are close to 0.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the Zeros.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


4200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4201 ordinal=4201 -->
## Functions

Functions

Let Fbe the ndimension function and let Xbe a given point in ndimensions.

Furthermore, let

f= 0.5F²

The algorithm is looking for such a vector Pthat

F(X+ dP) ≤ F(X)

for all 0 ≤ d≤ 1.

In a second step, an appropriate value, d*, is calculated, so that

F(X+ d*P)

is considerably smaller than F(X). This process is repeated until F(X) ≈ 0 is reached.
What follows is an approximation for F(X) = 0.

nDnD NonlinearNonlinear SystemSystem SolverSolver

Determines a set of solutions of a nonlinear system of equations in ndimensions
beginning with a randomly chosen start point in ndimensions. You must manually
select the polymorphic instance to use.


   • nD Nonlinear System Solver (Formula) VI
   • nD Nonlinear System Solver (VI) VI

As an example of using the nD Nonlinear System Solver VI, determine the solutions for
the following nonlinear system.

2x+ 3y+ z² – 6 = 0 –4x+ y² – 4z+ 7 = 0 x² + y+ z– 3 = 0

To obtain solutions for the preceding nonlinear system, enter the following values on

                                                    © National Instruments 4201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4202 ordinal=4202 -->
## Functions

Functions

       the front panel.

            • Start: [-1, -1, -1]
            • End: [4, 4, 4]
            • X: [x, y, z]
            • F(X): [2*x + 3*y + z*z - 6, -4*x + y*y - 4*z + 7, x*x + y + z
        - 3]

           Note You only need to enter the left side of the equations describing the
              nonlinear system into F(X). The VI assumes that the right side is zero.

      The solutions determined by the VI and returned in Zeros are (1.0000, 1.0000, 1.0000)
      and (–0.4050, 0.5931, 2.2429).

       This algorithm is based on the nD Nonlinear System Single Solution VI.

           Note The algorithm used to find the solution to the nonlinear system is
              fundamentally stochastic in nature. For example, if number of trials is 3, the
                 VI generates three separate n-dimensional starting points and finds a
               solution to the system using each of the three starting points. If the nonlinear
             system has two solutions, the VI might not find both solutions. Generally, the
                 VI finds the solution closest to the starting point for a particular trial. If all
               three starting points are closest to a particular solution than other solutions,
              the VI finds the solution closest to the three starting points three times and
             does not identify other solutions. To improve the chances of finding all
                solutions, increase number of trials.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Scripts and Formulas\
        Equation Explorer.vi


4202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4203 ordinal=4203 -->
## Functions

Functions

nDnD NonlinearNonlinear SystemSystem SolverSolver (Formula)(Formula) VIVI

Determines a set of solutions of a nonlinear system of equations in ndimensions
beginning with a randomly chosen start point in ndimensions. You must manually
select the polymorphic instance to use.


Inputs/Outputs

   •      accuracy —

    accuracy controls the accuracy of the zero determination. The default is 1.00E-8, which specifies
    the maximum deviation of the calculated solution from the actual solution.

   •     number of trials —

   number of trials is the elaborate number of randomly chosen start points. The algorithm starts
    with these points and looks for zeros close to these points. The default is 5.

   •     h —

   h is a small distance to calculate derivatives. The default is 1E-8.

   •       Start —

     Start is an array describing the left corner of the n-dimension interval. The randomly chosen
     start points of the zero-finding algorithm can be found in the n-dimensional rectangle spanned
    by Start and End.

   •     End —

   End is an array describing the right corner of the n-dimension interval. The randomly chosen
     start points of the zero-finding algorithm can be found in the n-dimensional rectangle spanned
    by Start and End.


                                                    © National Instruments 4203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4204 ordinal=4204 -->
## Functions

Functions

               •     X —

          X is an array of strings representing the xvariables. If the array of strings contains the variable t,
            the VI returns an error.

               •       F(X) —

             F(X) is an array of strings defining the functions in ndimensions. The formula can contain any
          number of valid variables.

               •      Zeroes —

            Zeros contains the determined zeros of F(X).

               •       f(Zeroes) —

            F(Zeros) contains the function values of Zeros.

             Usually, these values are close to 0.

               •       ticks —

             ticks is the time in milliseconds to analyze the formula and to produce the Zeros.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      As an example of using the nD Nonlinear System Solver VI, determine the solutions for
       the following nonlinear system.

     2x+ 3y+ z² – 6 = 0 –4x+ y² – 4z+ 7 = 0 x² + y+ z– 3 = 0

      To obtain solutions for the preceding nonlinear system, enter the following values on
       the front panel.

            • Start: [-1, -1, -1]
            • End: [4, 4, 4]
            • X: [x, y, z]
            • F(X): [2*x + 3*y + z*z - 6, -4*x + y*y - 4*z + 7, x*x + y + z


4204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4205 ordinal=4205 -->
## Functions

Functions

   - 3]

      Note You only need to enter the left side of the equations describing the
        nonlinear system into F(X). The VI assumes that the right side is zero.

The solutions determined by the VI and returned in Zeros are (1.0000, 1.0000, 1.0000)
and (–0.4050, 0.5931, 2.2429).

This algorithm is based on the nD Nonlinear System Single Solution VI.

      Note The algorithm used to find the solution to the nonlinear system is
       fundamentally stochastic in nature. For example, if number of trials is 3, the
         VI generates three separate n-dimensional starting points and finds a
        solution to the system using each of the three starting points. If the nonlinear
       system has two solutions, the VI might not find both solutions. Generally, the
         VI finds the solution closest to the starting point for a particular trial. If all
        three starting points are closest to a particular solution than other solutions,
       the VI finds the solution closest to the three starting points three times and
       does not identify other solutions. To improve the chances of finding all
        solutions, increase number of trials.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Scripts and Formulas\
   Equation Explorer.vi
nDnD NonlinearNonlinear SystemSystem SolverSolver (VI)(VI) VIVI

Determines a set of solutions of a nonlinear system of equations in ndimensions
beginning with a randomly chosen start point in ndimensions. You must manually
select the polymorphic instance to use.


                                                    © National Instruments 4205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4206 ordinal=4206 -->
## Functions

Functions


      Inputs/Outputs

               •      accuracy —

            accuracy controls the accuracy of the zero determination. The default is 1.00E-8, which specifies
            the maximum deviation of the calculated solution from the actual solution.

               •     number of trials —

          number of trials is the elaborate number of randomly chosen start points. The algorithm starts
            with these points and looks for zeros close to these points. The default is 5.

               •     h —

          h is a small distance to calculate derivatives. The default is 1E-8.

               •       Start —

             Start is an array describing the left corner of the n-dimension interval. The randomly chosen
              start points of the zero-finding algorithm can be found in the n-dimensional rectangle spanned
           by Start and End.

               •     End —

          End is an array describing the right corner of the n-dimension interval. The randomly chosen
              start points of the zero-finding algorithm can be found in the n-dimensional rectangle spanned
           by Start and End.

               •      data —

           data contains arbitrary values that pass to the VI that implements the function.

               •       F(X) —

             F(X) is a strictly typed reference to the VI that implements the function.

            Create this VI by starting from the VI template located in labview\vi.lib\gmath\


4206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4207 ordinal=4207 -->
## Functions

Functions


   zero.llb\Zero Finder f(x) nD.vit.

   •      Zeroes —

    Zeros contains the determined zeros of F(X).

   •       f(Zeroes) —

    F(Zeros) contains the function values of Zeros.

     Usually, these values are close to 0.

   •       ticks —

     ticks is the time in milliseconds to analyze the formula and to produce the Zeros.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


As an example of using the nD Nonlinear System Solver VI, determine the solutions for
the following nonlinear system.

2x+ 3y+ z² – 6 = 0 –4x+ y² – 4z+ 7 = 0 x² + y+ z– 3 = 0

To obtain solutions for the preceding nonlinear system, enter the following values on
the front panel.

  • Start: [-1, -1, -1]
  • End: [4, 4, 4]
  • X: [x, y, z]
  • F(X): [2*x + 3*y + z*z - 6, -4*x + y*y - 4*z + 7, x*x + y + z
   - 3]

      Note You only need to enter the left side of the equations describing the
        nonlinear system into F(X). The VI assumes that the right side is zero.


                                                    © National Instruments 4207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4208 ordinal=4208 -->
## Functions

Functions

      The solutions determined by the VI and returned in Zeros are (1.0000, 1.0000, 1.0000)
      and (–0.4050, 0.5931, 2.2429).

       This algorithm is based on the nD Nonlinear System Single Solution VI.

           Note The algorithm used to find the solution to the nonlinear system is
              fundamentally stochastic in nature. For example, if number of trials is 3, the
                 VI generates three separate n-dimensional starting points and finds a
               solution to the system using each of the three starting points. If the nonlinear
             system has two solutions, the VI might not find both solutions. Generally, the
                 VI finds the solution closest to the starting point for a particular trial. If all
               three starting points are closest to a particular solution than other solutions,
              the VI finds the solution closest to the three starting points three times and
             does not identify other solutions. To improve the chances of finding all
                solutions, increase number of trials.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Scripts and Formulas\
        Equation Explorer.vi

     AdditionalAdditional InformationInformation aboutabout thethe MathematicsMathematics VIsVIs

       This book contains additional information about the Mathematics VIs.

      DifferencesDifferences betweenbetween thethe ParserParser inin thethe MathematicsMathematics VIsVIs andand thethe
     FormulaFormula NodeNode

      The parser in the Mathematics VIs supports all elements that Formula Nodes support
       with the following exceptions:

            • Variables—Only a, a0, …, a9, … z, z0, …, z9, are valid.
            • Logical, conditional, inequality, equality—?:, |, ||, &, &&, !=, ==,<, >, <=, and >= are
          not valid.


4208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4209 ordinal=4209 -->
## Functions

Functions

  • Functions—atan2, max, min, mod, pow, rem, and sizeOfDim are not valid. You can
   use these functions in a Formula Node or use their corresponding LabVIEW
    functions.

The following table lists functions that the parser in the Mathematics VIs supports but
Formula Nodes do not.


           Corresponding Function                           Description          LabVIEW VI

                                    Evaluates the cosine integral for any real nonnegative ci(x)       Cosine Integral                             number x.

                                    Evaluates the gamma function or incomplete gamma gamma(x) Gamma                                     function for x.

                                 Produces a floating-point number between 0 and 1
 rand( )    Random Number (0 – 1)                                         exclusively.

 si(x)       Sine Integral             Evaluates the sine integral for any real number x.

 spike(x)    Spike                   Generates the spike function for any real number x.

 square(x)  Square                 Generates the square function for any real number x.

 step(x)    Step                   Generates the step function for any real number x.

To use these functions with a Formula Node, place their corresponding VIs on the
block diagram and wire their outputs to the Formula Node. For example, use the
Cosine Integral VI in place of ci.

The following table lists cases where Formula Nodes and the parser in the
Mathematics VIs use different syntax.


 Element        Formula Node                 Parser VI Routine

 π                 pi                                  pi(1) =π, pi(2) = 2π, 2pi or 2(pi) return an error

 Exponentiation   **                          ^

 int            Rounds to the nearest integer.   Rounds to the next smaller integer.

The precedence of operators is the same for the Mathematics VIs as in Formula Nodes.
Refer to Formula Parsing VIs for more information about specific Formula Parsing VIs.

                                                    © National Instruments 4209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4210 ordinal=4210 -->
## Functions

Functions

      The parser in the Mathematics VIs uses the following syntax:

     function (argument)

     MathematicsMathematics RelatedRelated DocumentationDocumentation

      The following references might be helpful to you as you use the Mathematics VIs:

      Asmar, Nakhle H. Partial Differential Equations with Fourier Series and Boundary Value
      Problems. 2d ed. Englewood Cliffs, N.J.: Prentice Hall, 2004.

        Barrett, Richard et al. Templates for the Solution of Linear Systems: Building Blocks for
        Iterative Methods. 2d ed. Philadelphia: SIAM, 1994.

       Brenner, Susanne C., and L. Ridgway Scott. The Mathematical Theory of Finite Element
      Methods. New York: Springer, 1994.

       Chugani, Mahesh L., Abhay R. Samant, and Michael Cerna. LabVIEW Signal Processing.
      Upper Saddle River, N.J.: Prentice Hall, 1998.

       Crandall, Richard E. Projects in Scientific Computation. Berlin: Springer, 2009.

      De Boor, Carl. A Practical Guide to Splines. New York: Springer, 2001.

       Ecker, Joseph G., and Michael Kupferschmid. Introduction to Operations Research.
     New York: Krieger Publishing, 2004.

      Fahmy, M. F. "Generalized Bessel Polynomials with Application to the Design of
      Bandpass Filters." Circuit Theory and Applications 5, (1977): 337-342.

       Gander, Walter, and Jiri Hrebicek. Solving Problems in Scientific Computing Using
      Maple and MATLAB. 4th ed. Berlin: Springer, 2008.

       Lanczos, C. A. "Precision Approximation of the Gamma Function." Journal of the
       Society for Industrial and Applied Mathematics. Series B, Numerical Analysis 1, (1964):
       86-96.

      Montgomery, Douglas C., and George C. Runger. Applied Statistics and Probability for


4210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4211 ordinal=4211 -->
## Functions

Functions

Engineers. 4th ed. New York: John Wiley & Sons, 2006.

Nocedal, Jorge, and Stephen J. Wright. Numerical Optimization. 2d ed. New York:
Springer, 2006.

Oppenheim, Alan V., and Alan S. Willsky. Signals and Systems. 2d ed. New York:
Prentice Hall, 1996.

Press, William H. et al. Numerical Recipes in C++: The Art of Scientific Computing. 2d
ed. Cambridge: Cambridge University Press, 2002.

Rockey, K. C. et al. The Finite Element Method: A Basic Method. Oxford: Blackwell
Science, 1991.

Wilkinson, J. H., and C. Reinsch. Linear Algebra, Vol. 2 of Handbook for Automatic
Computation. New York: Springer, 1986.

Zwillinger, Daniel. Handbook of Differential Equations. 3d ed. San Diego: Academic
Press, 1998.

MathematicsMathematics VIsVIs andand FunctionsFunctions forfor thethe LabVIEWLabVIEW BaseBase DevelopmentDevelopment
SystemSystem

The Numeric functions are available in the LabVIEW Base Development System. The
following list includes the other Mathematics VIs and functions available in the
LabVIEW Base Development System.

Elementary & Special Functions VIs
Linear Algebra VIs
Probability & Statistics VIs
Exponential Functions
Hyperbolic Functions
Trigonometric Functions
Linear Algebra VIs
A x B
Determinant
Dot Product
Inverse Matrix
Matrix Exp

                                                    © National Instruments 4211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4212 ordinal=4212 -->
## Functions

Functions

       Elementary & Special Functions VIs
        Linear Algebra VIs
        Probability & Statistics VIs
        Matrix Logarithm
        Matrix Power
        Matrix Square Root
        Outer Product
         Probability & Statistics VIs
        Create Histogram
        Histogram
      Mean
       Median
      Mode
        Standard Deviation and Variance

     MathematicsMathematics VIsVIs ExamplesExamples

      Study the mathematics examples to learn some of the possible theoretical and
        practical applications of the Mathematics VIs. These examples are located in
     labview\examples\math and are grouped into the following LLBs:

            • Refer to the labview\examples\Mathematics directory for examples of
          mathematics.
            • Refer to the labview\examples\Mathematics\Optimization directory
            for examples related to optimization.
            • Refer to the labview\examples\Signal Processing\Transforms
           directory for examples applied to signal processing.

        Also, many of the Mathematics VIs have example text on the front panel of the VI
      showing how to input various parameters. Double-click the VI icon to open the front
       panel of the VI and view the text.

      Using the Mathematics VIs

      The following examples provide possible applications for the Mathematics VIs. In many
       applications, being able to enter formulas directly on the front panel is extremely
        useful. This is possible using the Formula Parsing VIs. The first two examples below
       describe some typical scenarios where you might use the Formula Parsing VIs.


4212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4213 ordinal=4213 -->
## Functions

Functions

Example 1

Given a set of measurements (xi, yi) where i = 0, 1, …, n – 1 fit the set of data points into
a model equation, such as the following.

Y = asin(bX) + ccos(dX)

or

Y = a + bX + cexp(dX)

or more generally

Y = f(X, a, b, …, c)

(where a, b, …, c are the unknown model parameters)

LabVIEW can calculate such optimal system parameters as


LabVIEW uses the Levenberg Marquardt method to solve this minimization problem.
Before now, the model equation had to be fixed in the Formula Node before running
the program. With the Formula Parsing VIs, you can input the model equation on the
front panel.

Example 2

Another typical example consists of the following three-step process.

 1. Collect a set of discrete measurements

     (xi, yi, zi)

    for i = 0, 1, …, n – 1
 2.  Fit this set based on a model such as


                                                    © National Instruments 4213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4214 ordinal=4214 -->
## Functions

Functions

                (xi, yi, zi)

            for i = 0, 1, …, n – 1
         3. Determining those points (x, y) with

           z = f(x, y, a, b, …, c) = 0

           or

           z = f(x, y, a, b, …, c) = max!

           or

           z = f(x, y, a, b, …, c) = min!

      An easy way to input discrete measurements on a LabVIEW front panel makes
       calculating the roots, minima, and maxima for a general model simple for your end
        user. Notice that at the beginning of the previous process, the correct formula Z = f(X, Y,
        a, b, …, c) is not known.

     Example 3

      Another application for the Mathematics VIs is to help control an x-y step motor or a
       robot control that positions objects in 2D or 3D space during run time. The path of the
       object can be calculated with these VIs.

      Another 2D and 3D application of the Mathematics VIs is for surface description. Wings
       of airplanes, among other parts of machines and instruments in the real technical
       world, can be described by mathematical curves and surfaces. In nondestructive
        testing, such as using ultrasound, eddy currents, or X-rays, a pre-scan of the structure
      under test is initially done and followed by a more accurate scan in areas where the
      measured and expected values differ.

       Taking a set of coarse measurements as a preparatory step is necessary because it is
        virtually impossible to store the measurements of all the curves and surfaces of an
       entire structure. The pre-scan of the wing of a plane is then followed by a more
       accurate scan of a smaller part of this wing. Because the Formula Parsing VIs can
      handle formulas on the front panel, you can use them to calculate the 2D and 3D


4214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4215 ordinal=4215 -->
## Functions

Functions

curves of the wing in an effective manner.

Example 4

The study of solutions of differential equations, especially parameter studies, is not
only a question of appropriate numeric algorithms such as the Euler method, Runge
Kutta method, or the Cash Karp method, but also a question of formula manipulation.
With the Mathematics VIs you can manipulate differential equations on the front panel.
Refer to the labview\examples\Mathematics for examples of this approach to
solving differential equations.

OutputOutput ValuesValues forfor InvalidInvalid OperationsOperations withwith MatrixMatrix FunctionsFunctions

The Matrix functions manipulate the elements, diagonals, and submatrices of a matrix
or 2D numeric array. When the functions attempt to get data that is not available or use
more data than is available, the functions perform an invalid operation. In the case of
an invalid operation, LabVIEW returns or fills in values at exterior locations in the
original matrix or 2D array input. These values that appear in the output matrix or 2D
array depend on the data and element type of the original matrix or 2D array input.
You perform an invalid operation when the values in the following table appear in the
output.

      Note During invalid operations, LabVIEW returns the values in this table
      when the operations extract data from a matrix. During special matrix
       coercion cases, LabVIEW returns a new data type to pad new locations when
       you add new elements to a matrix, causing the matrix to expand.

ProbabilityProbability DistributionsDistributions

The following table describes the probability distributions that the Probability VIs can
compute.


 Distribution                                  Equation(s)

 Cumulative Distribution Function (CDF)


                                                    © National Instruments 4215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4216 ordinal=4216 -->
## Functions

Functions


         Distribution                                  Equation(s)

         Probability Density Function (PDF)

         Probability Function (PF)

      SpecialSpecial MatrixMatrix CoercionCoercion CasesCases forfor thethe MatrixMatrix FunctionsFunctions

      The Matrix functions manipulate the elements, diagonals, and submatrices of a matrix
       or 2D numeric array. When you use the Set Matrix Diagonal, Set Matrix Elements, and
       Set Submatrix functions, you can add new elements to the original matrix or 2D array.
      However, when the input matrix cannot store new elements without a loss of
       precision, the function changes the output data type. The following table defines the
      output data type when the input matrix cannot store the data type of new elements.

           Note The matrix functions do not support I64, U64, EXT, and CXT numeric
               types. Use the Conversion functions to convert the data to a data type the
               Matrix functions support.

      CreatingCreating thethe FormulaFormula StringString oror FittingFitting ModelModel toto SpecifySpecify aa NonlinearNonlinear
     FunctionFunction

      The Nonlinear Curve Fit VI assumes that you have prior knowledge of the nonlinear
       relationship between the independent variable x and dependent variable y, as shown
        in the equation below.

      Y = f( X; a 1, a 2, ..., aM)

      where M is the number of unknown coefficients.

      The Levenberg-Marquardt algorithm determines the set of coefficients (a 1, a 2, ..., aM)
       that best fits the observations. The best fit coefficients minimize the following
       equation, which describes the distance between the curve and the fitted model.


4216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4217 ordinal=4217 -->
## Functions

Functions

where N is the length of Y and yi, xi and wi are the i-th element of Y,X and Weight,
respectively.

You can use a formula string or a model VI with the Nonlinear Curve Fit VI to specify the
nonlinear function Y = f( X; a 1, a 2, ..., aM).

In the Nonlinear Curve Fit LM Formula String instance of the Nonlinear Curve Fit VI, you
can describe the nonlinear function f in model description. The following block
diagram shows how to define f according to the following equation:

                      2f(x) = a1 + a2*x + a3*x

where x is the independent variable and a1, a2, and a3 are three unknown coefficients.


In the Nonlinear Curve Fit LM instance of the Nonlinear Curve Fit VI, you must provide a
model VI with the connector pattern shown in the following illustration.


Then create a reference to the model VI and wire the reference to the f(x,a) input of the
Nonlinear Curve Fit VI.

The model VI accepts X and the set of coefficients (a 1, a 2, ..., aM) as inputs and returns
f( X; a 1, a 2, ..., aM) and a 2D array of the partial derivatives with respect to the
coefficients.

                                                    © National Instruments 4217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4218 ordinal=4218 -->
## Functions

Functions

      The following example describes the layout of the partial derivative matrix of a
       function with three coefficients and n X values.


      The number of columns in the matrix is equal to the number of coefficients, while the
      number of rows in the matrix is equal to the number of X values.

      The calculation of the partial derivatives is optional. If you do not calculate the
       derivatives in the model VI and you wire an empty array indicator to the f'(X,a) output,
       the Nonlinear Curve Fit VI calculates the derivatives numerically.

     FormulaFormula ParsingParsing VIsVIs inin MoreMore DetailDetail

      A Formula Parsing VI scans an input string and interprets this string as a formula, or a
       collection of formulas. Then, the Formula Parsing VI transforms the formulas into
      numeric calculations and outputs the results. The Formula Parsing VI routines deal
       only with real numbers.

      The following are three main kinds of formula routines:

            • The VIs representing the functionality of the Formula Node (Eval Formula Node,
          Parse Formula Node, and Eval Parsed Formula Node VIs)
            • The VIs analyzing a simple string as one formula ( Eval Formula String, Parse
         Formula String, and Eval Parsed Formula String VIs)
            • The VIs producing whole sets of function values (Eval Single-Variable Array,Eval
           Single-Variable Scalar, and Eval Multi-Variable Scalar VIs)

      The first two categories of Formula Parsing VIs can be further divided into two
       subcategories, the direct form and the indirect form. As an example, the direct version

4218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4219 ordinal=4219 -->
## Functions

Functions

of the Eval Formula Node VI is represented by the following block diagram.


On the other hand, the indirect form splits evaluation explicitly into parsing and
evaluation steps. The following illustration shows a simple example. You can use the
indirect form in larger applications where the efficiency of this two-step process,
parsing and then evaluating, outweighs the additional complexity and logic.


There are differences in the behavior of the parser if you are using Mathematics VIs or
the Formula Node. Refer to Formula Node and Expression Node Functions for
functions you can use with Formula Parsing VIs.

FormulaFormula ParsingParsing VIVI VariablesVariables

The Formula Parsing VIs accept only the following variables:

      Note Use these same variables to specify the formula string description for
       the Nonlinear Curve Fit VI.

a, a0, ..., a9

b, b0, ..., b9


                                                    © National Instruments 4219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4220 ordinal=4220 -->
## Functions

Functions

            .

            .

            .

         z, z0, ..., z9

       For variable and function names, only lowercase letters are allowed. The VIs interpret
        capital letters as errors.

         All numbers in exponential notation use the 1E–1 convention with the capital letter E.
       Using 1e–1 with the lowercase letter e results in an error message.

     SignalSignal ProcessingProcessing

      Use the Signal Processing VIs to perform signal generation, digital filtering, data
      windowing, and spectrum analysis.


         Palette Object  Description

       Waveform     Use the Waveform Generation VIs to generate different types of single and multi-
        Generation     tone signals, function generator signals, and noise signals.


       Waveform
                     Use the Waveform Conditioning VIs to perform digital filtering and windowing.
         Conditioning


                     Use the Waveform Measurements VIs to perform common time and frequency
       Waveform
                    domain measurements, such as DC, RMS, Tone Frequency/Amplitude/Phase,
        Measurements
                     Harmonic Distortion, SINAD, and Averaged FFT Measurements.


         Signal
                     Use the Signal Generation VIs to generate one-dimensional arrays with specific
        Generation


4220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4221 ordinal=4221 -->
## Functions

Functions


 Palette Object  Description

              waveform patterns. The Signal Generation VIs generate digital patterns and
               waveforms.


 Signal              Use the Signal Operation VIs to manipulate signals and return a signal output. Operation


              Use the Windows VIs to implement smoothing windows and to perform data Windows               windowing.


 Filters        Use the Filters VIs to implement IIR, FIR, and nonlinear filters.


 Spectral              Use the Spectral Analysis VIs to perform array-based analysis on a spectrum.
 Analysis


              Use the Transforms VIs to implement common transforms used in signal Transforms                 processing. The LabVIEW FFT-based VIs use different output units and scale factors.


              Use the Point By Point VIs to conveniently and efficiently process data a point at a
 Point By Point  time. Point By Point VIs are included in the LabVIEW Full Development and
                 Professional Development Systems.

WaveformWaveform GenerationGeneration

Use the Waveform Generation VIs to generate different types of single and multi-tone
signals, function generator signals, and noise signals.

The VIs on this palette can return waveform error codes.


                                                    © National Instruments 4221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4222 ordinal=4222 -->
## Functions

Functions


         Palette Object  Description

         Basic
         Function       Creates an output waveform based on signal type.
        Generator

        Tones and
        Noise         Generates a waveform composed of a sum of sine tones, noise, and DC offset.
       Waveform

        Formula       Creates an output waveform using a formula string to specify the time function to
       Waveform     be used.


         Sine
                       Generates a waveform containing a sine wave.       Waveform

        Square                       Generates a waveform containing a square wave.
       Waveform

         Triangle
                       Generates a waveform containing a triangle wave.       Waveform

        Sawtooth                       Generates a waveform containing a sawtooth wave.       Waveform

         Basic                       Generates a waveform that is the sum of integer cycle sine tones.
         Multitone

         Basic
         Multitone with Generates a waveform that is the sum of integer cycle sine tones.
        Amplitudes

         Multitone
                       Generates a waveform that is the sum of integer cycle sine tones.
        Generator

        Uniform White                       Generates a uniformly distributed pseudorandom pattern whose values are in the
        Noise                       range [–a:a], where ais the absolute value of amplitude.       Waveform


4222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4223 ordinal=4223 -->
## Functions

Functions


Palette Object  Description

Gaussian              Generates a Gaussian distributed pseudorandom pattern whose statistical profile is
White Noise                    (0,s), where s is the absolute value of the specified standard deviation.Waveform

Periodic
Random              Generates a waveform containing periodic random noise (PRN).Noise
Waveform

Inverse f              Generates a continuous noise waveform with a power spectral density that isNoise                inversely proportional to frequency over a specified frequency range.Waveform


Gamma Noise  Generates a pseudorandom pattern of values which are the waiting times to the
Waveform     order number event of a unit mean Poisson process.


Poisson Noise  Generates a pseudorandom sequence of values which are the number of discrete
Waveform     events occurring in the interval specified by mean of a unit rate Poisson process.


Binomial      Generates a binomially-distributed pseudorandom pattern whose values are the
Noise        number of occurrences of an event given the probability of that event occurring
Waveform     and the number of trials.


Bernoulli      Generates a pseudorandom pattern of ones and zeros, where the probability of
Noise          generating a one is one probability and the probability of generating a zero is
Waveform     (1–one probability).


MLS Sequence  Generates a maximum length sequence of ones and zeros using a modulo-2
Waveform      primitive polynomial of order polynomial order.


Simulate
               Simulates a sine wave, square wave, triangle wave, sawtooth wave, or noise signal.
Signal


                                                    © National Instruments 4223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4224 ordinal=4224 -->
## Functions

Functions


         Palette Object  Description

        Simulate
          Arbitrary       Simulates a signal that you define.
         Signal

    WaveformWaveform ConditioningConditioning

      Use the Waveform Conditioning VIs to perform digital filtering and windowing.

           Note The VIs on this palette return an error if an input waveform has a dt
                less than or equal to zero.

           Note The Waveform Conditioning VIs presently do not accept waveforms
               that contain complex data.

      The VIs on this palette can return waveform error codes.


         Palette                      Description
        Object

                           Filters signals in either single or multiple waveforms. If you are filtering multiple
          Digital FIR    waveforms, the VI maintains separate filter states for each waveform. The data types
           Filter       you wire to the signal in and FIR filter specifications inputs determine the
                    polymorphic instance to use.


                           Filters signals in either single or multiple waveforms. If you are filtering multiple
          Digital IIR    waveforms, the VI maintains separate filter states for each waveform. The data types
           Filter       you wire to the signal in and IIR filter specifications inputs determine the
                    polymorphic instance to use.


4224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4225 ordinal=4225 -->
## Functions

Functions


Palette             Description
Object

Continuous  Convolves single or multiple waveforms and one or more kernels with state, allowing
Convolution  subsequent calls to be processed in a continuous manner. If you are convolving
(FIR)         multiple waveforms, the VI maintains separate convolution states for each waveform.


              Applies a scaled window to the time-domain signal and outputs window constants
Scaled               for further analysis. Wire data to the signal in input to determine the polymorphicWindow              instance to use or manually select the instance.


Align        Performs element-wise alignment of waveforms and returns the aligned waveforms.
Waveforms   The data types you wire to the waveform inputs determine the polymorphic instance
(continuous)  to use.


Align        Performs element-wise alignment of two waveforms and returns the aligned
Waveforms   waveforms. The data types you wire to the waveform inputs determine the
(single shot)  polymorphic instance to use.


Resample    Resamples an input waveform according to the user-defined values for t0 and dt.
Waveforms   Wire data to the waveform in input to determine the polymorphic instance to use or
(continuous) manually select the instance.


Resample    Resamples input waveforms or data according to the user-defined t0 and dt values.
Waveforms   Wire data to the waveform or data input to determine the polymorphic instance to
(single shot)  use or manually select the instance.


Filter        Processes signals through filters and windows.


             Performs an alignment of signals by changing the start time or performs a
Align and
             resampling of signals by changing the time delta. This Express VI returns the adjusted
Resample
               signals.


                                                    © National Instruments 4225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4226 ordinal=4226 -->
## Functions

Functions


         Palette                      Description
        Object

                    Uses triggering to extract a segment out of a signal. The trigger conditions can be
         Trigger and   based on a start or stop trigger threshold or can be static. When a trigger condition is
        Gate           static, the trigger occurs immediately and this Express VI returns a predefined
                  number of samples.


       DigitalDigital FIRFIR FilterFilter

        Filters signals in either single or multiple waveforms. If you are filtering multiple
      waveforms, the VI maintains separate filter states for each waveform. The data types
      you wire to the signal in and FIR filter specifications inputs determine the
      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


            • FIR Filter for 1 Chan VI
            • FIR Filter for N Chan VI
            • FIR Filter by N Specs for N Chan VI
            • FIR Filter for 1 Chan (CDB) VI
            • FIR Filter for N Chan (CDB) VI
            • FIR Filter by N Specs for N Chan (CDB) VI

       This VI filters the signal(s) in a waveform array according to the FIR filter specifications
      and optional FIR filter specifications arrays. If you are filtering multiple waveforms,
       the VI applies a different filter to each of the input waveforms and maintains a separate
         filter state for each waveform. The VI uses the optional FIR filter specifications only if
        Filter topology is FIR by Specification or Windowed FIR. You do not need to wire reset
         filter. This VI resets itself the first time it is called.


4226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4227 ordinal=4227 -->
## Functions

Functions

The Digital FIR Filter VI can perform single-channel measurements in both one-shot
mode (single call) and continuous mode (multiple calls with history). It can perform
multi-channel measurements only in one-shot mode. If you want to make multiple-
channel measurements in continuous mode, either use the multichannel instance of
this VI or use one instance of this VI per channel.

The single-channel instance of this VI is intended primarily for continuous processing
of a single channel. Do not generalize this behavior to the multi-channel case, typically
by using this single-channel VI in a For Loop to continuously process multiple channels
by indexing an array of waveforms.

The single-channel instance of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history
using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering and Response.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering Using Optional Specs.vi

FIRFIR FilterFilter forfor 11 ChanChan VIVI

Filters signals in either single or multiple waveforms. If you are filtering multiple
waveforms, the VI maintains separate filter states for each waveform. The data types
you wire to the signal in and FIR filter specifications inputs determine the
polymorphic instance to use.

      Note Do not use the single-channel instance of this VI for continuous
        multiple-channel processing.


                                                    © National Instruments 4227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4228 ordinal=4228 -->
## Functions

Functions


      Inputs/Outputs

               •       reset filter —

             reset filter forces the filter coefficients to be redesigned and the internal filter states to be reset
             to zero when it is TRUE.

               •       signal in —

             signal in is the waveform to be filtered.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications are the minimum values needed to specify the FIR filter.

                     •      Topology —

               Topology determines the design type of the filter.

                        Off               0                         (default)
               1    FIR by Specification
               2    Equi-ripple FIR
               3   Windowed FIR

                     •      Type —

              Type specifies the passband of the filter according to the following values.

               0        Lowpass


4228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4229 ordinal=4229 -->
## Functions

Functions


      1        Highpass
      2        Bandpass
      3        Bandstop

      •      #Taps —

      #Taps is the number of taps in the FIR filter. The default is 50.

      •     Lower PB —

     Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

      •     Upper PB —

     Upper PB is the higher of the two passband frequencies. The default is 0.

      •     Lower SB —

     Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

      •     Upper SB —

     Upper SB is the higher of the two stopband frequencies. The default is 0.


•      optional FIR filter specifications —

  optional FIR filter specifications is a cluster of additional parameters that can be used when
  specifying an FIR filter.

      •     PB Gain —

     PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
      dB. The default is –3dB.

      •     SB Gain —

     SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
     The default is –60dB.

      •      Scale —


                                                   © National Instruments 4229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4230 ordinal=4230 -->
## Functions

Functions


                Scale determines how the PB Gain and SB Gain parameters are interpreted.

                     •     Window —

             Window controls which smoothing window is applied to the truncated coefficients.

              Smoothing windows decrease ripple in the filter passband and improve the ability of the
                       filter to attenuate frequency components in the filter stopband.

               0    None
               1    Hanning
               2    Hamming
               3     Triangular
               4    Blackman
               5     Exact Blackman
               6     Blackman-Harris
               7     Kaiser-Bessel
               8      Flat Top


               •       signal out —

             signal out is the filtered waveform.

               •        filter information —

                filter information contains the magnitude and phase responses of the filter in a cluster that is
            ready to graph. filter information also contains the order of the filter.

                     •      magnitude H(w) —

              magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

                           •       f0 —

                      f0 is the start frequency of the magnitude response.

                           •       df —


4230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4231 ordinal=4231 -->
## Functions

Functions


             df is the spacing between elements of the magnitude response in hertz.

                •     Mag H(w) —

          Mag H(w) is an array of values containing the magnitude response of the filter.


         •      phase H(w) —

       phase H(w) is the phase response of the filter.

                •       f0 —

              f0 is the start frequency of the phase response.

                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •      Phase H(w) —

           Phase H(w) is an array of values containing the phase response of the filter, expressed
              in degrees.


         •      order —

        order is the order of the filter.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI filters the signal(s) in a waveform array according to the FIR filter specifications
and optional FIR filter specifications arrays. If you are filtering multiple waveforms,
the VI applies a different filter to each of the input waveforms and maintains a separate
filter state for each waveform. The VI uses the optional FIR filter specifications only if
Filter topology is FIR by Specification or Windowed FIR. You do not need to wire reset


                                                    © National Instruments 4231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4232 ordinal=4232 -->
## Functions

Functions

         filter. This VI resets itself the first time it is called.

      The Digital FIR Filter VI can perform single-channel measurements in both one-shot
     mode (single call) and continuous mode (multiple calls with history). It can perform
       multi-channel measurements only in one-shot mode. If you want to make multiple-
      channel measurements in continuous mode, either use the multichannel instance of
        this VI or use one instance of this VI per channel.

      The single-channel instance of this VI is intended primarily for continuous processing
       of a single channel. Do not generalize this behavior to the multi-channel case, typically
      by using this single-channel VI in a For Loop to continuously process multiple channels
      by indexing an array of waveforms.

      The single-channel instance of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history
       using the reset filter control results in an unexpected behavior of this VI because the
        internal state information is passed from one channel to another.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        FIR Filtering and Response.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        FIR Filtering Using Optional Specs.vi

       FIRFIR FilterFilter forfor NN ChanChan VIVI

        Filters signals in either single or multiple waveforms. If you are filtering multiple
      waveforms, the VI maintains separate filter states for each waveform. The data types
      you wire to the signal in and FIR filter specifications inputs determine the
      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


4232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4233 ordinal=4233 -->
## Functions

Functions


Inputs/Outputs

   •       reset filters —

    reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
    to zero for each input waveform when it is TRUE.

   •       signal(s) in —

     signal(s) in is an array of waveforms containing the signals to filter.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      FIR filter specifications —

    FIR filter specifications are the minimum values needed to specify the FIR filter.

         •      Topology —

        Topology determines the design type of the filter.

               Off
        0
                (default)
        1    FIR by Specification
        2    Equi-ripple FIR
        3   Windowed FIR

         •      Type —

       Type specifies the passband of the filter according to the following values.


                                                    © National Instruments 4233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4234 ordinal=4234 -->
## Functions

Functions


               0        Lowpass
               1        Highpass
               2        Bandpass
               3        Bandstop

                     •      #Taps —

               #Taps is the number of taps in the FIR filter. The default is 50.

                     •     Lower PB —

              Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

                     •     Upper PB —

              Upper PB is the higher of the two passband frequencies. The default is 0.

                     •     Lower SB —

              Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

                     •     Upper SB —

              Upper SB is the higher of the two stopband frequencies. The default is 0.


               •      optional FIR filter specifications —

            optional FIR filter specifications is a cluster of additional parameters that can be used when
             specifying an FIR filter.

                     •     PB Gain —

             PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
                dB. The default is –3dB.

                     •     SB Gain —

             SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
              The default is –60dB.


4234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4235 ordinal=4235 -->
## Functions

Functions


      •      Scale —

      Scale determines how the PB Gain and SB Gain parameters are interpreted.

      •     Window —

     Window controls which smoothing window is applied to the truncated coefficients.

      Smoothing windows decrease ripple in the filter passband and improve the ability of the
         filter to attenuate frequency components in the filter stopband.

      0    None
      1    Hanning
      2    Hamming
      3     Triangular
      4    Blackman
      5     Exact Blackman
      6     Blackman-Harris
      7     Kaiser-Bessel
      8      Flat Top


•       signal(s) out —

  signal(s) out is an array of signals that have been filtered according to the filter specifications
  controls.

•        filter information —

   filter information contains the magnitude and phase responses of the filter in a cluster that is
  ready to graph. filter information also contains the order of the filter.

      •      magnitude H(w) —

      magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

             •       f0 —

            f0 is the start frequency of the magnitude response.


                                                   © National Instruments 4235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4236 ordinal=4236 -->
## Functions

Functions


                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •     Mag H(w) —

                Mag H(w) is an array of values containing the magnitude response of the filter.


                     •      phase H(w) —

              phase H(w) is the phase response of the filter.

                           •       f0 —

                      f0 is the start frequency of the phase response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •      Phase H(w) —

                  Phase H(w) is an array of values containing the phase response of the filter, expressed
                       in degrees.


                     •      order —

                order is the order of the filter.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This VI filters the signal(s) in a waveform array according to the FIR filter specifications
      and optional FIR filter specifications arrays. If you are filtering multiple waveforms,
       the VI applies a different filter to each of the input waveforms and maintains a separate
         filter state for each waveform. The VI uses the optional FIR filter specifications only if
        Filter topology is FIR by Specification or Windowed FIR. You do not need to wire reset

4236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4237 ordinal=4237 -->
## Functions

Functions

filter. This VI resets itself the first time it is called.

The Digital FIR Filter VI can perform single-channel measurements in both one-shot
mode (single call) and continuous mode (multiple calls with history). It can perform
multi-channel measurements only in one-shot mode. If you want to make multiple-
channel measurements in continuous mode, either use the multichannel instance of
this VI or use one instance of this VI per channel.

The single-channel instance of this VI is intended primarily for continuous processing
of a single channel. Do not generalize this behavior to the multi-channel case, typically
by using this single-channel VI in a For Loop to continuously process multiple channels
by indexing an array of waveforms.

The single-channel instance of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history
using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering and Response.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering Using Optional Specs.vi

FIRFIR FilterFilter byby NN SpecsSpecs forfor NN ChanChan VIVI

Filters signals in either single or multiple waveforms. If you are filtering multiple
waveforms, the VI maintains separate filter states for each waveform. The data types
you wire to the signal in and FIR filter specifications inputs determine the
polymorphic instance to use.

      Note Do not use the single-channel instance of this VI for continuous
        multiple-channel processing.


                                                    © National Instruments 4237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4238 ordinal=4238 -->
## Functions

Functions


      Inputs/Outputs

               •       reset filters —

             reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
             to zero for each input waveform when it is TRUE.

               •       signal(s) in —

              signal(s) in is an array of waveforms containing the signals to filter.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications is an array of filter specifications. This array must have the same size as
            the signal(s) in array of waveforms.

                     •      Topology —

               Topology determines the design type of the filter.

                        Off
               0
                         (default)
               1    FIR by Specification
               2    Equi-ripple FIR
               3   Windowed FIR

                     •      Type —

              Type specifies the passband of the filter according to the following values.


4238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4239 ordinal=4239 -->
## Functions

Functions


      0        Lowpass
      1        Highpass
      2        Bandpass
      3        Bandstop

      •      #Taps —

      #Taps is the number of taps in the FIR filter. The default is 50.

      •     Lower PB —

     Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

      •     Upper PB —

     Upper PB is the higher of the two passband frequencies. The default is 0.

      •     Lower SB —

     Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

      •     Upper SB —

     Upper SB is the higher of the two stopband frequencies. The default is 0.


•      optional FIR filter specifications —

  optional FIR filter specifications is an array of optional filter specifications. This array may be
  empty or must have the same size as the FIR filter specifications array.

      •     PB Gain —

     PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
      dB. The default is –3dB.

      •     SB Gain —

     SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
     The default is –60dB.


                                                   © National Instruments 4239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4240 ordinal=4240 -->
## Functions

Functions


                     •      Scale —

                Scale determines how the PB Gain and SB Gain parameters are interpreted.

                     •     Window —

             Window controls which smoothing window is applied to the truncated coefficients.

              Smoothing windows decrease ripple in the filter passband and improve the ability of the
                       filter to attenuate frequency components in the filter stopband.

               0    None
               1    Hanning
               2    Hamming
               3     Triangular
               4    Blackman
               5     Exact Blackman
               6     Blackman-Harris
               7     Kaiser-Bessel
               8      Flat Top


               •       signal(s) out —

              signal(s) out is an array of signals that have been filtered according to the filter specifications
             controls.

               •        filter information —

                filter information is an array of clusters containing information about each of the designed
                 filters.

                     •      magnitude H(w) —

              magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

                           •       f0 —

                      f0 is the start frequency of the magnitude response.


4240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4241 ordinal=4241 -->
## Functions

Functions


                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •     Mag H(w) —

          Mag H(w) is an array of values containing the magnitude response of the filter.


         •      phase H(w) —

       phase H(w) is the phase response of the filter.

                •       f0 —

              f0 is the start frequency of the phase response.

                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •      Phase H(w) —

           Phase H(w) is an array of values containing the phase response of the filter, expressed
              in degrees.


         •      order —

        order is the order of the filter.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI filters the signal(s) in a waveform array according to the FIR filter specifications
and optional FIR filter specifications arrays. If you are filtering multiple waveforms,
the VI applies a different filter to each of the input waveforms and maintains a separate
filter state for each waveform. The VI uses the optional FIR filter specifications only if
Filter topology is FIR by Specification or Windowed FIR. You do not need to wire reset

                                                    © National Instruments 4241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4242 ordinal=4242 -->
## Functions

Functions

         filter. This VI resets itself the first time it is called.

      The Digital FIR Filter VI can perform single-channel measurements in both one-shot
     mode (single call) and continuous mode (multiple calls with history). It can perform
       multi-channel measurements only in one-shot mode. If you want to make multiple-
      channel measurements in continuous mode, either use the multichannel instance of
        this VI or use one instance of this VI per channel.

      The single-channel instance of this VI is intended primarily for continuous processing
       of a single channel. Do not generalize this behavior to the multi-channel case, typically
      by using this single-channel VI in a For Loop to continuously process multiple channels
      by indexing an array of waveforms.

      The single-channel instance of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history
       using the reset filter control results in an unexpected behavior of this VI because the
        internal state information is passed from one channel to another.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        FIR Filtering and Response.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        FIR Filtering Using Optional Specs.vi

       FIRFIR FilterFilter forfor 11 ChanChan (CDB)(CDB) VIVI

        Filters signals in either single or multiple waveforms. If you are filtering multiple
      waveforms, the VI maintains separate filter states for each waveform. The data types
      you wire to the signal in and FIR filter specifications inputs determine the
      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


4242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4243 ordinal=4243 -->
## Functions

Functions


Inputs/Outputs

   •       reset filter —

    reset filter forces the filter coefficients to be redesigned and the internal filter states to be reset
    to zero when it is TRUE.

   •       signal in —

    signal in is the waveform to be filtered.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      FIR filter specifications —

    FIR filter specifications are the minimum values needed to specify the FIR filter.

         •      Topology —

        Topology determines the design type of the filter.

               Off
        0
                (default)
        1    FIR by Specification
        2    Equi-ripple FIR
        3   Windowed FIR

         •      Type —

       Type specifies the passband of the filter according to the following values.


                                                    © National Instruments 4243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4244 ordinal=4244 -->
## Functions

Functions


               0        Lowpass
               1        Highpass
               2        Bandpass
               3        Bandstop

                     •      #Taps —

               #Taps is the number of taps in the FIR filter. The default is 50.

                     •     Lower PB —

              Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

                     •     Upper PB —

              Upper PB is the higher of the two passband frequencies. The default is 0.

                     •     Lower SB —

              Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

                     •     Upper SB —

              Upper SB is the higher of the two stopband frequencies. The default is 0.


               •      optional FIR filter specifications —

            optional FIR filter specifications is a cluster of additional parameters that can be used when
             specifying an FIR filter.

                     •     PB Gain —

             PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
                dB. The default is –3dB.

                     •     SB Gain —

             SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
              The default is –60dB.


4244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4245 ordinal=4245 -->
## Functions

Functions


      •      Scale —

      Scale determines how the PB Gain and SB Gain parameters are interpreted.

      •     Window —

     Window controls which smoothing window is applied to the truncated coefficients.

      Smoothing windows decrease ripple in the filter passband and improve the ability of the
         filter to attenuate frequency components in the filter stopband.

      0    None
      1    Hanning
      2    Hamming
      3     Triangular
      4    Blackman
      5     Exact Blackman
      6     Blackman-Harris
      7     Kaiser-Bessel
      8      Flat Top


•       signal out —

  signal out is the filtered waveform.

•        filter information —

   filter information contains the magnitude and phase responses of the filter in a cluster that is
  ready to graph. filter information also contains the order of the filter.

      •      magnitude H(w) —

      magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

             •       f0 —

            f0 is the start frequency of the magnitude response.

             •       df —


                                                   © National Instruments 4245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4246 ordinal=4246 -->
## Functions

Functions


                     df is the spacing between elements of the magnitude response in hertz.

                           •     Mag H(w) —

                Mag H(w) is an array of values containing the magnitude response of the filter.


                     •      phase H(w) —

              phase H(w) is the phase response of the filter.

                           •       f0 —

                      f0 is the start frequency of the phase response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •      Phase H(w) —

                  Phase H(w) is an array of values containing the phase response of the filter, expressed
                       in degrees.


                     •      order —

                order is the order of the filter.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This VI filters the signal(s) in a waveform array according to the FIR filter specifications
      and optional FIR filter specifications arrays. If you are filtering multiple waveforms,
       the VI applies a different filter to each of the input waveforms and maintains a separate
         filter state for each waveform. The VI uses the optional FIR filter specifications only if
        Filter topology is FIR by Specification or Windowed FIR. You do not need to wire reset


4246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4247 ordinal=4247 -->
## Functions

Functions

filter. This VI resets itself the first time it is called.

The Digital FIR Filter VI can perform single-channel measurements in both one-shot
mode (single call) and continuous mode (multiple calls with history). It can perform
multi-channel measurements only in one-shot mode. If you want to make multiple-
channel measurements in continuous mode, either use the multichannel instance of
this VI or use one instance of this VI per channel.

The single-channel instance of this VI is intended primarily for continuous processing
of a single channel. Do not generalize this behavior to the multi-channel case, typically
by using this single-channel VI in a For Loop to continuously process multiple channels
by indexing an array of waveforms.

The single-channel instance of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history
using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering and Response.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering Using Optional Specs.vi

FIRFIR FilterFilter forfor NN ChanChan (CDB)(CDB) VIVI

Filters signals in either single or multiple waveforms. If you are filtering multiple
waveforms, the VI maintains separate filter states for each waveform. The data types
you wire to the signal in and FIR filter specifications inputs determine the
polymorphic instance to use.

      Note Do not use the single-channel instance of this VI for continuous
        multiple-channel processing.


                                                    © National Instruments 4247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4248 ordinal=4248 -->
## Functions

Functions


      Inputs/Outputs

               •       reset filters —

             reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
             to zero for each input waveform when it is TRUE.

               •       signal(s) in —

              signal(s) in is an array of waveforms containing the signals to filter.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications are the minimum values needed to specify the FIR filter.

                     •      Topology —

               Topology determines the design type of the filter.

                        Off
               0
                         (default)
               1    FIR by Specification
               2    Equi-ripple FIR
               3   Windowed FIR

                     •      Type —

              Type specifies the passband of the filter according to the following values.


4248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4249 ordinal=4249 -->
## Functions

Functions


      0        Lowpass
      1        Highpass
      2        Bandpass
      3        Bandstop

      •      #Taps —

      #Taps is the number of taps in the FIR filter. The default is 50.

      •     Lower PB —

     Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

      •     Upper PB —

     Upper PB is the higher of the two passband frequencies. The default is 0.

      •     Lower SB —

     Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

      •     Upper SB —

     Upper SB is the higher of the two stopband frequencies. The default is 0.


•      optional FIR filter specifications —

  optional FIR filter specifications is a cluster of additional parameters that can be used when
  specifying an FIR filter.

      •     PB Gain —

     PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
      dB. The default is –3dB.

      •     SB Gain —

     SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
     The default is –60dB.


                                                   © National Instruments 4249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4250 ordinal=4250 -->
## Functions

Functions


                     •      Scale —

                Scale determines how the PB Gain and SB Gain parameters are interpreted.

                     •     Window —

             Window controls which smoothing window is applied to the truncated coefficients.

              Smoothing windows decrease ripple in the filter passband and improve the ability of the
                       filter to attenuate frequency components in the filter stopband.

               0    None
               1    Hanning
               2    Hamming
               3     Triangular
               4    Blackman
               5     Exact Blackman
               6     Blackman-Harris
               7     Kaiser-Bessel
               8      Flat Top


               •       signal(s) out —

              signal(s) out is an array of signals that have been filtered according to the filter specifications
             controls.

               •        filter information —

                filter information contains the magnitude and phase responses of the filter in a cluster that is
            ready to graph. filter information also contains the order of the filter.

                     •      magnitude H(w) —

              magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

                           •       f0 —

                      f0 is the start frequency of the magnitude response.


4250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4251 ordinal=4251 -->
## Functions

Functions


                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •     Mag H(w) —

          Mag H(w) is an array of values containing the magnitude response of the filter.


         •      phase H(w) —

       phase H(w) is the phase response of the filter.

                •       f0 —

              f0 is the start frequency of the phase response.

                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •      Phase H(w) —

           Phase H(w) is an array of values containing the phase response of the filter, expressed
              in degrees.


         •      order —

        order is the order of the filter.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI filters the signal(s) in a waveform array according to the FIR filter specifications
and optional FIR filter specifications arrays. If you are filtering multiple waveforms,
the VI applies a different filter to each of the input waveforms and maintains a separate
filter state for each waveform. The VI uses the optional FIR filter specifications only if
Filter topology is FIR by Specification or Windowed FIR. You do not need to wire reset

                                                    © National Instruments 4251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4252 ordinal=4252 -->
## Functions

Functions

         filter. This VI resets itself the first time it is called.

      The Digital FIR Filter VI can perform single-channel measurements in both one-shot
     mode (single call) and continuous mode (multiple calls with history). It can perform
       multi-channel measurements only in one-shot mode. If you want to make multiple-
      channel measurements in continuous mode, either use the multichannel instance of
        this VI or use one instance of this VI per channel.

      The single-channel instance of this VI is intended primarily for continuous processing
       of a single channel. Do not generalize this behavior to the multi-channel case, typically
      by using this single-channel VI in a For Loop to continuously process multiple channels
      by indexing an array of waveforms.

      The single-channel instance of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history
       using the reset filter control results in an unexpected behavior of this VI because the
        internal state information is passed from one channel to another.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        FIR Filtering and Response.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        FIR Filtering Using Optional Specs.vi

       FIRFIR FilterFilter byby NN SpecsSpecs forfor NN ChanChan (CDB)(CDB) VIVI

        Filters signals in either single or multiple waveforms. If you are filtering multiple
      waveforms, the VI maintains separate filter states for each waveform. The data types
      you wire to the signal in and FIR filter specifications inputs determine the
      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


4252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4253 ordinal=4253 -->
## Functions

Functions


Inputs/Outputs

   •       reset filters —

    reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
    to zero for each input waveform when it is TRUE.

   •       signal(s) in —

     signal(s) in is an array of waveforms containing the signals to filter.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      FIR filter specifications —

    FIR filter specifications is an array of filter specifications. This array must have the same size as
    the signal(s) in array of waveforms.

         •      Topology —

        Topology determines the design type of the filter.

               Off
        0
                (default)
        1    FIR by Specification
        2    Equi-ripple FIR
        3   Windowed FIR

         •      Type —

       Type specifies the passband of the filter according to the following values.


                                                    © National Instruments 4253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4254 ordinal=4254 -->
## Functions

Functions


               0        Lowpass
               1        Highpass
               2        Bandpass
               3        Bandstop

                     •      #Taps —

               #Taps is the number of taps in the FIR filter. The default is 50.

                     •     Lower PB —

              Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

                     •     Upper PB —

              Upper PB is the higher of the two passband frequencies. The default is 0.

                     •     Lower SB —

              Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

                     •     Upper SB —

              Upper SB is the higher of the two stopband frequencies. The default is 0.


               •      optional FIR filter specifications —

            optional FIR filter specifications is an array of optional filter specifications. This array may be
          empty or must have the same size as the FIR filter specifications array.

                     •     PB Gain —

             PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
                dB. The default is –3dB.

                     •     SB Gain —

             SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
              The default is –60dB.


4254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4255 ordinal=4255 -->
## Functions

Functions


      •      Scale —

      Scale determines how the PB Gain and SB Gain parameters are interpreted.

      •     Window —

     Window controls which smoothing window is applied to the truncated coefficients.

      Smoothing windows decrease ripple in the filter passband and improve the ability of the
         filter to attenuate frequency components in the filter stopband.

      0    None
      1    Hanning
      2    Hamming
      3     Triangular
      4    Blackman
      5     Exact Blackman
      6     Blackman-Harris
      7     Kaiser-Bessel
      8      Flat Top


•       signal(s) out —

  signal(s) out is an array of signals that have been filtered according to the filter specifications
  controls.

•        filter information —

   filter information is an array of clusters containing information about each of the designed
   filters.

      •      magnitude H(w) —

      magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

             •       f0 —

            f0 is the start frequency of the magnitude response.


                                                   © National Instruments 4255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4256 ordinal=4256 -->
## Functions

Functions


                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •     Mag H(w) —

                Mag H(w) is an array of values containing the magnitude response of the filter.


                     •      phase H(w) —

              phase H(w) is the phase response of the filter.

                           •       f0 —

                      f0 is the start frequency of the phase response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •      Phase H(w) —

                  Phase H(w) is an array of values containing the phase response of the filter, expressed
                       in degrees.


                     •      order —

                order is the order of the filter.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


       This VI filters the signal(s) in a waveform array according to the FIR filter specifications
      and optional FIR filter specifications arrays. If you are filtering multiple waveforms,
       the VI applies a different filter to each of the input waveforms and maintains a separate
         filter state for each waveform. The VI uses the optional FIR filter specifications only if
        Filter topology is FIR by Specification or Windowed FIR. You do not need to wire reset

4256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4257 ordinal=4257 -->
## Functions

Functions

filter. This VI resets itself the first time it is called.

The Digital FIR Filter VI can perform single-channel measurements in both one-shot
mode (single call) and continuous mode (multiple calls with history). It can perform
multi-channel measurements only in one-shot mode. If you want to make multiple-
channel measurements in continuous mode, either use the multichannel instance of
this VI or use one instance of this VI per channel.

The single-channel instance of this VI is intended primarily for continuous processing
of a single channel. Do not generalize this behavior to the multi-channel case, typically
by using this single-channel VI in a For Loop to continuously process multiple channels
by indexing an array of waveforms.

The single-channel instance of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history
using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering and Response.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   FIR Filtering Using Optional Specs.vi

DigitalDigital IIRIIR FilterFilter

Filters signals in either single or multiple waveforms. If you are filtering multiple
waveforms, the VI maintains separate filter states for each waveform. The data types
you wire to the signal in and IIR filter specifications inputs determine the
polymorphic instance to use.

      Note Do not use the single-channel instance of this VI for continuous
        multiple-channel processing.


                                                    © National Instruments 4257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4258 ordinal=4258 -->
## Functions

Functions


            •  IIR Filter for 1 Chan VI
            •  IIR Filter for N Chan VI
            •  IIR Filter by N Specs for N Chan VI
            •  IIR Filter for 1 Chan (CDB) VI
            •  IIR Filter for N Chan (CDB) VI
            •  IIR Filter by N Specs for N Chan (CDB) VI

      The Digital IIR Filter VI filters the signal(s) in a waveform array according to the IIR filter
       specifications and optional IIR filter specifications arrays. If you are filtering multiple
      waveforms, the VI applies a different filter to each of the input waveforms and
       maintains a separate filter state for each waveform. The VI uses optional IIR filter
       specifications only if Filter Order is less than or equal to zero. You do not need to wire
       reset filter. This VI resets itself the first time it is called.

           Note In general, IIR second-order stages provide more stable results than
              the IIR fourth-order stages. National Instruments recommends that you
               specify IIR 2nd Order as the filter structure option with Bandpass or
           Bandstop as the Type for extreme IIR filter specifications, such as very
             narrow passband or stopband.

      The Digital IIR Filter VI can perform single-channel measurements in both one-shot
     mode (single call) and continuous mode (multiple calls with history). It can perform
       multichannel measurements only in one-shot mode. If you want to make multiple-
      channel measurements in continuous mode, either use the multi-channel instance of
        this VI or use one instance of this VI per channel.

      The single-channel instance of this VI is intended primarily for continuous processing
       of a single channel. Do not generalize this behavior to the multi-channel case, typically
      by using this single-channel VI in a For Loop to continuously process multiple channels
      by indexing an array of waveforms.

      The single-channel instance of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history


4258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4259 ordinal=4259 -->
## Functions

Functions

using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Frequency Analysis of a Filter Design.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   IIR Filtering Using Optional Specs.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   IIR Filtering and Response.vi

IIRIIR FilterFilter forfor 11 ChanChan VIVI

Filters signals in either single or multiple waveforms. If you are filtering multiple
waveforms, the VI maintains separate filter states for each waveform. The data types
you wire to the signal in and IIR filter specifications inputs determine the
polymorphic instance to use.

      Note Do not use the single-channel instance of this VI for continuous
        multiple-channel processing.


Inputs/Outputs

   •       reset filter —

    reset filter forces the filter coefficients to be redesigned and the internal filter states to be reset
    to zero when it is TRUE.

   •       signal in —

                                                    © National Instruments 4259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4260 ordinal=4260 -->
## Functions

Functions


             signal in is the waveform data you want to filter for channel 1.

               •        filter structure option —

                filter structure option specifies the order of the IIR cascade filter.

           0 IIR 2nd Order—Returns IIR second-order filter stages.
           1 IIR 4th Order—Returns IIR fourth-order filter stages.
            Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
           2 according to the type. If type is Lowpass or Highpass, the VI returns IIR second-order filter
               stages. If type is Bandpass or Bandstop, the VI returns IIR fourth-order filter stages.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       IIR filter specifications —

              IIR filter specifications is the cluster containing design parameters for an IIR filter.

                     •      Topology —

               Topology determines the design type of the filter.

               0     Off
               1    Butterworth
               2    Chebyshev
               3     Inverse Chebyshev
               4      Elliptic
               5    Bessel

                     •      Type —

              Type specifies the passband of the filter according to the following values.

               0        Lowpass
               1        Highpass
               2        Bandpass


4260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4261 ordinal=4261 -->
## Functions

Functions


      3        Bandstop

      •      Order —

      Order is the filter order.

          If Order ≤ 0, the filter uses optional IIR filter specification to compute the order.

      •     Lower Fc —

     Lower Fc is the low cutoff frequency and must observe the Nyquist criterion.

     The Nyquist criterion is 0 < fl < 0.5fs, where fl is the cutoff frequency, and fs is the sampling
       frequency. If Lower Fc is less than zero or greater than half the sampling frequency, the VI
       sets the signal out waveform to be empty and returns an error. The default is 100.

      •     Upper Fc —

     Upper Fc is the high cutoff frequency. This parameter is ignored when Type is 0 (lowpass) or
      1 (highpass).

      •     PB Ripple —

     PB Ripple must be greater than zero, and you must express it in decibels. If PB Ripple is less
      than or equal to zero, the VI sets the signal out waveform to be empty and returns an error.
     The default is 1.0.

      •     SB Attenuation —

     SB Attenuation specifies the stopband attenuation. SB Attenuation must be greater than
      zero and expressed in decibels. If SB Attenuation is less than or equal to zero, the VI sets the
       signal output to zero or an empty array and returns an error. The default is 60.0.


•      optional IIR filter specifications —

  optional IIR filter specifications is a cluster containing information necessary to compute the
  order of an IIR filter.

      •     Lower PB —


                                                   © National Instruments 4261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4262 ordinal=4262 -->
## Functions

Functions


              Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

                     •     Upper PB —

              Upper PB is the higher of the two passband frequencies. The default is 0.

                     •     Lower SB —

              Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

                     •     Upper SB —

              Upper SB is the higher of the two stopband frequencies. The default is 0.

                     •     PB Gain —

             PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
                dB. The default is –3dB.

                     •     SB Gain —

             SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
              The default is –60dB.

                     •      Scale —

                Scale determines how the Passband and Stopband gain parameters are interpreted.


               •       signal out —

             signal out is the generated waveform.

               •        filter information —

                filter information contains the magnitude and phase responses of the filter in a cluster that is
            ready to graph. filter information also contains the order of the filter.

                     •      magnitude H(w) —

              magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.


4262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4263 ordinal=4263 -->
## Functions

Functions


                •       f0 —

              f0 is the start frequency of the magnitude response.

                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •     Mag H(w) —

          Mag H(w) is an array of values containing the magnitude response of the filter.


         •      phase H(w) —

       phase H(w) is the phase response of the filter.

                •       f0 —

              f0 is the start frequency of the phase response.

                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •      Phase H(w) —

           Phase H(w) is an array of values containing the phase response of the filter, expressed
              in degrees.


         •      order —

        order is the order of the filter.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Digital IIR Filter VI filters the signal(s) in a waveform array according to the IIR filter


                                                    © National Instruments 4263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4264 ordinal=4264 -->
## Functions

Functions

       specifications and optional IIR filter specifications arrays. If you are filtering multiple
      waveforms, the VI applies a different filter to each of the input waveforms and
       maintains a separate filter state for each waveform. The VI uses optional IIR filter
       specifications only if Filter Order is less than or equal to zero. You do not need to wire
       reset filter. This VI resets itself the first time it is called.

           Note In general, IIR second-order stages provide more stable results than
              the IIR fourth-order stages. National Instruments recommends that you
               specify IIR 2nd Order as the filter structure option with Bandpass or
           Bandstop as the Type for extreme IIR filter specifications, such as very
             narrow passband or stopband.

      The Digital IIR Filter VI can perform single-channel measurements in both one-shot
     mode (single call) and continuous mode (multiple calls with history). It can perform
       multichannel measurements only in one-shot mode. If you want to make multiple-
      channel measurements in continuous mode, either use the multi-channel instance of
        this VI or use one instance of this VI per channel.

      The single-channel instance of this VI is intended primarily for continuous processing
       of a single channel. Do not generalize this behavior to the multi-channel case, typically
      by using this single-channel VI in a For Loop to continuously process multiple channels
      by indexing an array of waveforms.

      The single-channel instance of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history
       using the reset filter control results in an unexpected behavior of this VI because the
        internal state information is passed from one channel to another.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Frequency Analysis of a Filter Design.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        IIR Filtering Using Optional Specs.vi
            • labview\examples\Signal Processing\Waveform Conditioning\

4264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4265 ordinal=4265 -->
## Functions

Functions

   IIR Filtering and Response.vi

IIRIIR FilterFilter forfor NN ChanChan VIVI

Filters signals in either single or multiple waveforms. If you are filtering multiple
waveforms, the VI maintains separate filter states for each waveform. The data types
you wire to the signal in and IIR filter specifications inputs determine the
polymorphic instance to use.

      Note Do not use the single-channel instance of this VI for continuous
        multiple-channel processing.


Inputs/Outputs

   •       reset filters —

    reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
    to zero for each input waveform when it is TRUE.

   •       signal(s) in —

     signal(s) in is an array of waveforms containing the signals to filter.

   •        filter structure option —

      filter structure option specifies the order of the IIR cascade filter.

    0 IIR 2nd Order—Returns IIR second-order filter stages.
    1 IIR 4th Order—Returns IIR fourth-order filter stages.
     Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
    2 according to the type. If type is Lowpass or Highpass, the VI returns IIR second-order filter
      stages. If type is Bandpass or Bandstop, the VI returns IIR fourth-order filter stages.


                                                    © National Instruments 4265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4266 ordinal=4266 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       IIR filter specifications —

              IIR filter specifications is the cluster containing design parameters for an IIR filter.

                     •      Topology —

               Topology determines the design type of the filter.

               0     Off
               1    Butterworth
               2    Chebyshev
               3     Inverse Chebyshev
               4      Elliptic
               5    Bessel

                     •      Type —

              Type specifies the passband of the filter according to the following values.

               0        Lowpass
               1        Highpass
               2        Bandpass
               3        Bandstop

                     •      Order —

               Order is the filter order.

                           If Order ≤ 0, the filter uses optional IIR filter specification to compute the order.

                     •     Lower Fc —

              Lower Fc is the low cutoff frequency and must observe the Nyquist criterion.

              The Nyquist criterion is 0 < fl < 0.5fs, where fl is the cutoff frequency, and fs is the sampling
                 frequency. If Lower Fc is less than zero or greater than half the sampling frequency, the VI


4266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4267 ordinal=4267 -->
## Functions

Functions


       sets the signal out waveform to be empty and returns an error. The default is 100.

      •     Upper Fc —

     Upper Fc is the high cutoff frequency. This parameter is ignored when Type is 0 (lowpass) or
      1 (highpass).

      •     PB Ripple —

     PB Ripple must be greater than zero, and you must express it in decibels. If PB Ripple is less
      than or equal to zero, the VI sets the signal out waveform to be empty and returns an error.
     The default is 1.0.

      •     SB Attenuation —

     SB Attenuation specifies the stopband attenuation. SB Attenuation must be greater than
      zero and expressed in decibels. If SB Attenuation is less than or equal to zero, the VI sets the
       signal output to zero or an empty array and returns an error. The default is 60.0.


•      optional IIR filter specifications —

  optional IIR filter specifications is a cluster containing information necessary to compute the
  order of an IIR filter.

      •     Lower PB —

     Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

      •     Upper PB —

     Upper PB is the higher of the two passband frequencies. The default is 0.

      •     Lower SB —

     Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

      •     Upper SB —

     Upper SB is the higher of the two stopband frequencies. The default is 0.

      •     PB Gain —


                                                   © National Instruments 4267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4268 ordinal=4268 -->
## Functions

Functions


             PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
                dB. The default is –3dB.

                     •     SB Gain —

             SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
              The default is –60dB.

                     •      Scale —

                Scale determines how the Passband and Stopband gain parameters are interpreted.


               •       signal(s) out —

              signal(s) out is an array of signals that have been filtered according to the filter specifications
             controls.

               •        filter information —

                filter information contains the magnitude and phase responses of the filter in a cluster that is
            ready to graph. filter information also contains the order of the filter.

                     •      magnitude H(w) —

              magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

                           •       f0 —

                      f0 is the start frequency of the magnitude response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •     Mag H(w) —

                Mag H(w) is an array of values containing the magnitude response of the filter.


                     •      phase H(w) —


4268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4269 ordinal=4269 -->
## Functions

Functions


       phase H(w) is the phase response of the filter.

                •       f0 —

              f0 is the start frequency of the phase response.

                •       df —

             df is the spacing between elements of the magnitude response in hertz.

                •      Phase H(w) —

           Phase H(w) is an array of values containing the phase response of the filter, expressed
              in degrees.


         •      order —

        order is the order of the filter.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Digital IIR Filter VI filters the signal(s) in a waveform array according to the IIR filter
specifications and optional IIR filter specifications arrays. If you are filtering multiple
waveforms, the VI applies a different filter to each of the input waveforms and
maintains a separate filter state for each waveform. The VI uses optional IIR filter
specifications only if Filter Order is less than or equal to zero. You do not need to wire
reset filter. This VI resets itself the first time it is called.

      Note In general, IIR second-order stages provide more stable results than
       the IIR fourth-order stages. National Instruments recommends that you
        specify IIR 2nd Order as the filter structure option with Bandpass or
      Bandstop as the Type for extreme IIR filter specifications, such as very
       narrow passband or stopband.


                                                    © National Instruments 4269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4270 ordinal=4270 -->
## Functions

Functions

      The Digital IIR Filter VI can perform single-channel measurements in both one-shot
     mode (single call) and continuous mode (multiple calls with history). It can perform
       multichannel measurements only in one-shot mode. If you want to make multiple-
      channel measurements in continuous mode, either use the multi-channel instance of
        this VI or use one instance of this VI per channel.

      The single-channel instance of this VI is intended primarily for continuous processing
       of a single channel. Do not generalize this behavior to the multi-channel case, typically
      by using this single-channel VI in a For Loop to continuously process multiple channels
      by indexing an array of waveforms.

      The single-channel instance of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history
       using the reset filter control results in an unexpected behavior of this VI because the
        internal state information is passed from one channel to another.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Frequency Analysis of a Filter Design.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        IIR Filtering Using Optional Specs.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        IIR Filtering and Response.vi

        IIRIIR FilterFilter byby NN SpecsSpecs forfor NN ChanChan VIVI

        Filters signals in either single or multiple waveforms. If you are filtering multiple
      waveforms, the VI maintains separate filter states for each waveform. The data types
      you wire to the signal in and IIR filter specifications inputs determine the
      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


4270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4271 ordinal=4271 -->
## Functions

Functions


Inputs/Outputs

   •       reset filters —

    reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
    to zero for each input waveform when it is TRUE.

   •       signal(s) in —

     signal(s) in is an array of waveforms containing the signals to filter.

   •        filter structure option —

      filter structure option specifies the order of the IIR cascade filter.

    0 IIR 2nd Order—Returns IIR second-order filter stages.
    1 IIR 4th Order—Returns IIR fourth-order filter stages.
     Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
    2 according to the type. If type is Lowpass or Highpass, the VI returns IIR second-order filter
      stages. If type is Bandpass or Bandstop, the VI returns IIR fourth-order filter stages.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       IIR filter specifications —

     IIR filter specifications is an array of filter parameters. The size of this array must be the same as
    the number of waveforms in the signal(s) in array. The default is an empty array.

         •      Topology —

        Topology determines the design type of the filter.


                                                    © National Instruments 4271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4272 ordinal=4272 -->
## Functions

Functions


               0     Off
               1    Butterworth
               2    Chebyshev
               3     Inverse Chebyshev
               4      Elliptic
               5    Bessel

                     •      Type —

              Type specifies the passband of the filter according to the following values.

               0        Lowpass
               1        Highpass
               2        Bandpass
               3        Bandstop

                     •      Order —

               Order is the filter order.

                           If Order ≤ 0, the filter uses optional IIR filter specification to compute the order.

                     •     Lower Fc —

              Lower Fc is the low cutoff frequency and must observe the Nyquist criterion.

              The Nyquist criterion is 0 < fl < 0.5fs, where fl is the cutoff frequency, and fs is the sampling
                 frequency. If Lower Fc is less than zero or greater than half the sampling frequency, the VI
                  sets the signal out waveform to be empty and returns an error. The default is 100.

                     •     Upper Fc —

              Upper Fc is the high cutoff frequency. This parameter is ignored when Type is 0 (lowpass) or
               1 (highpass).

                     •     PB Ripple —

             PB Ripple must be greater than zero, and you must express it in decibels. If PB Ripple is less
               than or equal to zero, the VI sets the signal out waveform to be empty and returns an error.


4272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4273 ordinal=4273 -->
## Functions

Functions


     The default is 1.0.

      •     SB Attenuation —

     SB Attenuation specifies the stopband attenuation. SB Attenuation must be greater than
      zero and expressed in decibels. If SB Attenuation is less than or equal to zero, the VI sets the
       signal output to zero or an empty array and returns an error. The default is 60.0.


•      optional IIR filter specifications —

  optional IIR filter specifications is an array of additional filter parameters. This array must either
  be empty or must have the same size as the IIR filter specifications array.

      •     Lower PB —

     Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

      •     Upper PB —

     Upper PB is the higher of the two passband frequencies. The default is 0.

      •     Lower SB —

     Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

      •     Upper SB —

     Upper SB is the higher of the two stopband frequencies. The default is 0.

      •     PB Gain —

     PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
      dB. The default is –3dB.

      •     SB Gain —

     SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
     The default is –60dB.

      •      Scale —


                                                   © National Instruments 4273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4274 ordinal=4274 -->
## Functions

Functions


                Scale determines how the Passband and Stopband gain parameters are interpreted.


               •       signal(s) out —

              signal(s) out is an array of signals that have been filtered according to the filter specifications
             controls.

               •        filter information —

                filter information contains the magnitude and phase responses of the filter in a cluster that is
            ready to graph. filter information also contains the order of the filter.

                     •      magnitude H(w) —

              magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

                           •       f0 —

                      f0 is the start frequency of the magnitude response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •     Mag H(w) —

                Mag H(w) is an array of values containing the magnitude response of the filter.


                     •      phase H(w) —

              phase H(w) is the phase response of the filter.

                           •       f0 —

                      f0 is the start frequency of the phase response.

                           •       df —


4274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4275 ordinal=4275 -->
## Functions

Functions


             df is the spacing between elements of the magnitude response in hertz.

                •      Phase H(w) —

           Phase H(w) is an array of values containing the phase response of the filter, expressed
              in degrees.


         •      order —

        order is the order of the filter.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Digital IIR Filter VI filters the signal(s) in a waveform array according to the IIR filter
specifications and optional IIR filter specifications arrays. If you are filtering multiple
waveforms, the VI applies a different filter to each of the input waveforms and
maintains a separate filter state for each waveform. The VI uses optional IIR filter
specifications only if Filter Order is less than or equal to zero. You do not need to wire
reset filter. This VI resets itself the first time it is called.

      Note In general, IIR second-order stages provide more stable results than
       the IIR fourth-order stages. National Instruments recommends that you
        specify IIR 2nd Order as the filter structure option with Bandpass or
      Bandstop as the Type for extreme IIR filter specifications, such as very
       narrow passband or stopband.

The Digital IIR Filter VI can perform single-channel measurements in both one-shot
mode (single call) and continuous mode (multiple calls with history). It can perform
multichannel measurements only in one-shot mode. If you want to make multiple-
channel measurements in continuous mode, either use the multi-channel instance of
this VI or use one instance of this VI per channel.


                                                    © National Instruments 4275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4276 ordinal=4276 -->
## Functions

Functions

      The single-channel instance of this VI is intended primarily for continuous processing
       of a single channel. Do not generalize this behavior to the multi-channel case, typically
      by using this single-channel VI in a For Loop to continuously process multiple channels
      by indexing an array of waveforms.

      The single-channel instance of this VI maintains internal state information for a single
      channel only. Calling this VI to process another channel without clearing the history
       using the reset filter control results in an unexpected behavior of this VI because the
        internal state information is passed from one channel to another.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Measurements\
        Frequency Analysis of a Filter Design.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        IIR Filtering Using Optional Specs.vi
            • labview\examples\Signal Processing\Waveform Conditioning\
        IIR Filtering and Response.vi

        IIRIIR FilterFilter forfor 11 ChanChan (CDB)(CDB) VIVI

        Filters signals in either single or multiple waveforms. If you are filtering multiple
      waveforms, the VI maintains separate filter states for each waveform. The data types
      you wire to the signal in and IIR filter specifications inputs determine the
      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


4276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4277 ordinal=4277 -->
## Functions

Functions

Inputs/Outputs

   •       reset filter —

    reset filter forces the filter coefficients to be redesigned and the internal filter states to be reset
    to zero when it is TRUE.

   •       signal in —

    signal in is the waveform data you want to filter for channel 1.

   •        filter structure option —

      filter structure option specifies the order of the IIR cascade filter.

    0 IIR 2nd Order—Returns IIR second-order filter stages.
    1 IIR 4th Order—Returns IIR fourth-order filter stages.
     Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
    2 according to the type. If type is Lowpass or Highpass, the VI returns IIR second-order filter
      stages. If type is Bandpass or Bandstop, the VI returns IIR fourth-order filter stages.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       IIR filter specifications —

     IIR filter specifications is the cluster containing design parameters for an IIR filter.

         •      Topology —

        Topology determines the design type of the filter.

        0     Off
        1    Butterworth
        2    Chebyshev
        3     Inverse Chebyshev
        4      Elliptic
        5    Bessel

         •      Type —


                                                    © National Instruments 4277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4278 ordinal=4278 -->
## Functions

Functions


              Type specifies the passband of the filter according to the following values.

               0        Lowpass
               1        Highpass
               2        Bandpass
               3        Bandstop

                     •      Order —

               Order is the filter order.

                           If Order ≤ 0, the filter uses optional IIR filter specification to compute the order.

                     •     Lower Fc —

              Lower Fc is the low cutoff frequency and must observe the Nyquist criterion.

              The Nyquist criterion is 0 < fl < 0.5fs, where fl is the cutoff frequency, and fs is the sampling
                 frequency. If Lower Fc is less than zero or greater than half the sampling frequency, the VI
                  sets the signal out waveform to be empty and returns an error. The default is 100.

                     •     Upper Fc —

              Upper Fc is the high cutoff frequency. This parameter is ignored when Type is 0 (lowpass) or
               1 (highpass).

                     •     PB Ripple —

             PB Ripple must be greater than zero, and you must express it in decibels. If PB Ripple is less
               than or equal to zero, the VI sets the signal out waveform to be empty and returns an error.
              The default is 1.0.

                     •     SB Attenuation —

             SB Attenuation specifies the stopband attenuation. SB Attenuation must be greater than
                 zero and expressed in decibels. If SB Attenuation is less than or equal to zero, the VI sets the
                  signal output to zero or an empty array and returns an error. The default is 60.0.


               •      optional IIR filter specifications —


4278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4279 ordinal=4279 -->
## Functions

Functions


  optional IIR filter specifications is a cluster containing information necessary to compute the
  order of an IIR filter.

      •     Lower PB —

     Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

      •     Upper PB —

     Upper PB is the higher of the two passband frequencies. The default is 0.

      •     Lower SB —

     Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

      •     Upper SB —

     Upper SB is the higher of the two stopband frequencies. The default is 0.

      •     PB Gain —

     PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
      dB. The default is –3dB.

      •     SB Gain —

     SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
     The default is –60dB.

      •      Scale —

      Scale determines how the Passband and Stopband gain parameters are interpreted.


•       signal out —

  signal out is the generated waveform.

•        filter information —

   filter information contains the magnitude and phase responses of the filter in a cluster that is
  ready to graph. filter information also contains the order of the filter.


                                                   © National Instruments 4279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4280 ordinal=4280 -->
## Functions

Functions


                     •      magnitude H(w) —

              magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

                           •       f0 —

                      f0 is the start frequency of the magnitude response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •     Mag H(w) —

                Mag H(w) is an array of values containing the magnitude response of the filter.


                     •      phase H(w) —

              phase H(w) is the phase response of the filter.

                           •       f0 —

                      f0 is the start frequency of the phase response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •      Phase H(w) —

                  Phase H(w) is an array of values containing the phase response of the filter, expressed
                       in degrees.


                     •      order —

                order is the order of the filter.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


4280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4281 ordinal=4281 -->
## Functions

Functions

The Digital IIR Filter VI filters the signal(s) in a waveform array according to the IIR filter
specifications and optional IIR filter specifications arrays. If you are filtering multiple
waveforms, the VI applies a different filter to each of the input waveforms and
maintains a separate filter state for each waveform. The VI uses optional IIR filter
specifications only if Filter Order is less than or equal to zero. You do not need to wire
reset filter. This VI resets itself the first time it is called.

      Note In general, IIR second-order stages provide more stable results than
       the IIR fourth-order stages. National Instruments recommends that you
        specify IIR 2nd Order as the filter structure option with Bandpass or
      Bandstop as the Type for extreme IIR filter specifications, such as very
       narrow passband or stopband.

The Digital IIR Filter VI can perform single-channel measurements in both one-shot
mode (single call) and continuous mode (multiple calls with history). It can perform
multichannel measurements only in one-shot mode. If you want to make multiple-
channel measurements in continuous mode, either use the multi-channel instance of
this VI or use one instance of this VI per channel.

The single-channel instance of this VI is intended primarily for continuous processing
of a single channel. Do not generalize this behavior to the multi-channel case, typically
by using this single-channel VI in a For Loop to continuously process multiple channels
by indexing an array of waveforms.

The single-channel instance of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history
using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Frequency Analysis of a Filter Design.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   IIR Filtering Using Optional Specs.vi

                                                    © National Instruments 4281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4282 ordinal=4282 -->
## Functions

Functions

            • labview\examples\Signal Processing\Waveform Conditioning\
        IIR Filtering and Response.vi

        IIRIIR FilterFilter forfor NN ChanChan (CDB)(CDB) VIVI

        Filters signals in either single or multiple waveforms. If you are filtering multiple
      waveforms, the VI maintains separate filter states for each waveform. The data types
      you wire to the signal in and IIR filter specifications inputs determine the
      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


      Inputs/Outputs

               •       reset filters —

             reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
             to zero for each input waveform when it is TRUE.

               •       signal(s) in —

              signal(s) in is an array of waveforms containing the signals to filter.

               •        filter structure option —

                filter structure option specifies the order of the IIR cascade filter.

           0 IIR 2nd Order—Returns IIR second-order filter stages.
           1 IIR 4th Order—Returns IIR fourth-order filter stages.
            Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
           2             according to the type. If type is Lowpass or Highpass, the VI returns IIR second-order filter


4282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4283 ordinal=4283 -->
## Functions

Functions


    stages. If type is Bandpass or Bandstop, the VI returns IIR fourth-order filter stages.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       IIR filter specifications —

   IIR filter specifications is the cluster containing design parameters for an IIR filter.

      •      Topology —

      Topology determines the design type of the filter.

      0     Off
      1    Butterworth
      2    Chebyshev
      3     Inverse Chebyshev
      4      Elliptic
      5    Bessel

      •      Type —

      Type specifies the passband of the filter according to the following values.

      0        Lowpass
      1        Highpass
      2        Bandpass
      3        Bandstop

      •      Order —

      Order is the filter order.

          If Order ≤ 0, the filter uses optional IIR filter specification to compute the order.

      •     Lower Fc —

     Lower Fc is the low cutoff frequency and must observe the Nyquist criterion.


                                                   © National Instruments 4283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4284 ordinal=4284 -->
## Functions

Functions


              The Nyquist criterion is 0 < fl < 0.5fs, where fl is the cutoff frequency, and fs is the sampling
                 frequency. If Lower Fc is less than zero or greater than half the sampling frequency, the VI
                  sets the signal out waveform to be empty and returns an error. The default is 100.

                     •     Upper Fc —

              Upper Fc is the high cutoff frequency. This parameter is ignored when Type is 0 (lowpass) or
               1 (highpass).

                     •     PB Ripple —

             PB Ripple must be greater than zero, and you must express it in decibels. If PB Ripple is less
               than or equal to zero, the VI sets the signal out waveform to be empty and returns an error.
              The default is 1.0.

                     •     SB Attenuation —

             SB Attenuation specifies the stopband attenuation. SB Attenuation must be greater than
                 zero and expressed in decibels. If SB Attenuation is less than or equal to zero, the VI sets the
                  signal output to zero or an empty array and returns an error. The default is 60.0.


               •      optional IIR filter specifications —

            optional IIR filter specifications is a cluster containing information necessary to compute the
            order of an IIR filter.

                     •     Lower PB —

              Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

                     •     Upper PB —

              Upper PB is the higher of the two passband frequencies. The default is 0.

                     •     Lower SB —

              Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

                     •     Upper SB —


4284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4285 ordinal=4285 -->
## Functions

Functions


     Upper SB is the higher of the two stopband frequencies. The default is 0.

      •     PB Gain —

     PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
      dB. The default is –3dB.

      •     SB Gain —

     SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.
     The default is –60dB.

      •      Scale —

      Scale determines how the Passband and Stopband gain parameters are interpreted.


•       signal(s) out —

  signal(s) out is an array of signals that have been filtered according to the filter specifications
  controls.

•        filter information —

   filter information contains the magnitude and phase responses of the filter in a cluster that is
  ready to graph. filter information also contains the order of the filter.

      •      magnitude H(w) —

      magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

             •       f0 —

            f0 is the start frequency of the magnitude response.

             •       df —

           df is the spacing between elements of the magnitude response in hertz.

             •     Mag H(w) —


                                                   © National Instruments 4285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4286 ordinal=4286 -->
## Functions

Functions


                Mag H(w) is an array of values containing the magnitude response of the filter.


                     •      phase H(w) —

              phase H(w) is the phase response of the filter.

                           •       f0 —

                      f0 is the start frequency of the phase response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •      Phase H(w) —

                  Phase H(w) is an array of values containing the phase response of the filter, expressed
                       in degrees.


                     •      order —

                order is the order of the filter.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The Digital IIR Filter VI filters the signal(s) in a waveform array according to the IIR filter
       specifications and optional IIR filter specifications arrays. If you are filtering multiple
      waveforms, the VI applies a different filter to each of the input waveforms and
       maintains a separate filter state for each waveform. The VI uses optional IIR filter
       specifications only if Filter Order is less than or equal to zero. You do not need to wire
       reset filter. This VI resets itself the first time it is called.

           Note In general, IIR second-order stages provide more stable results than

4286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4287 ordinal=4287 -->
## Functions

Functions


       the IIR fourth-order stages. National Instruments recommends that you
        specify IIR 2nd Order as the filter structure option with Bandpass or
      Bandstop as the Type for extreme IIR filter specifications, such as very
       narrow passband or stopband.

The Digital IIR Filter VI can perform single-channel measurements in both one-shot
mode (single call) and continuous mode (multiple calls with history). It can perform
multichannel measurements only in one-shot mode. If you want to make multiple-
channel measurements in continuous mode, either use the multi-channel instance of
this VI or use one instance of this VI per channel.

The single-channel instance of this VI is intended primarily for continuous processing
of a single channel. Do not generalize this behavior to the multi-channel case, typically
by using this single-channel VI in a For Loop to continuously process multiple channels
by indexing an array of waveforms.

The single-channel instance of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history
using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Frequency Analysis of a Filter Design.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   IIR Filtering Using Optional Specs.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   IIR Filtering and Response.vi

IIRIIR FilterFilter byby NN SpecsSpecs forfor NN ChanChan (CDB)(CDB) VIVI

Filters signals in either single or multiple waveforms. If you are filtering multiple
waveforms, the VI maintains separate filter states for each waveform. The data types
you wire to the signal in and IIR filter specifications inputs determine the

                                                    © National Instruments 4287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4288 ordinal=4288 -->
## Functions

Functions

      polymorphic instance to use.

           Note Do not use the single-channel instance of this VI for continuous
              multiple-channel processing.


      Inputs/Outputs

               •       reset filters —

             reset filters forces the filter coefficients to be redesigned and the internal filter states to be reset
             to zero for each input waveform when it is TRUE.

               •       signal(s) in —

              signal(s) in is an array of waveforms containing the signals to filter.

               •        filter structure option —

                filter structure option specifies the order of the IIR cascade filter.

           0 IIR 2nd Order—Returns IIR second-order filter stages.
           1 IIR 4th Order—Returns IIR fourth-order filter stages.
            Auto Select (default)—Returns either IIR second-order or IIR fourth-order filter stages
           2 according to the type. If type is Lowpass or Highpass, the VI returns IIR second-order filter
               stages. If type is Bandpass or Bandstop, the VI returns IIR fourth-order filter stages.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       IIR filter specifications —

              IIR filter specifications is an array of filter parameters. The size of this array must be the same as


4288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4289 ordinal=4289 -->
## Functions

Functions


the number of waveforms in the signal(s) in array. The default is an empty array.

   •      Topology —

    Topology determines the design type of the filter.

    0     Off
    1    Butterworth
    2    Chebyshev
    3     Inverse Chebyshev
    4      Elliptic
    5    Bessel

   •      Type —

    Type specifies the passband of the filter according to the following values.

    0        Lowpass
    1        Highpass
    2        Bandpass
    3        Bandstop

   •      Order —

    Order is the filter order.

       If Order ≤ 0, the filter uses optional IIR filter specification to compute the order.

   •     Lower Fc —

    Lower Fc is the low cutoff frequency and must observe the Nyquist criterion.

    The Nyquist criterion is 0 < fl < 0.5fs, where fl is the cutoff frequency, and fs is the sampling
    frequency. If Lower Fc is less than zero or greater than half the sampling frequency, the VI
     sets the signal out waveform to be empty and returns an error. The default is 100.

   •     Upper Fc —

    Upper Fc is the high cutoff frequency. This parameter is ignored when Type is 0 (lowpass) or
    1 (highpass).


                                                 © National Instruments 4289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4290 ordinal=4290 -->
## Functions

Functions


                     •     PB Ripple —

             PB Ripple must be greater than zero, and you must express it in decibels. If PB Ripple is less
               than or equal to zero, the VI sets the signal out waveform to be empty and returns an error.
              The default is 1.0.

                     •     SB Attenuation —

             SB Attenuation specifies the stopband attenuation. SB Attenuation must be greater than
                 zero and expressed in decibels. If SB Attenuation is less than or equal to zero, the VI sets the
                  signal output to zero or an empty array and returns an error. The default is 60.0.


               •      optional IIR filter specifications —

            optional IIR filter specifications is an array of additional filter parameters. This array must either
          be empty or must have the same size as the IIR filter specifications array.

                     •     Lower PB —

              Lower PB is the lower of the two passband frequencies. The default is 100 Hz.

                     •     Upper PB —

              Upper PB is the higher of the two passband frequencies. The default is 0.

                     •     Lower SB —

              Lower SB is the lower of the two stopband frequencies. The default is 200 Hz.

                     •     Upper SB —

              Upper SB is the higher of the two stopband frequencies. The default is 0.

                     •     PB Gain —

             PB Gain is the gain at the passband frequencies. Gain may be specified in linear terms or
                dB. The default is –3dB.

                     •     SB Gain —

             SB Gain is the gain at the stopband frequencies. Gain may be specified in linear terms or dB.


4290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4291 ordinal=4291 -->
## Functions

Functions


     The default is –60dB.

      •      Scale —

      Scale determines how the Passband and Stopband gain parameters are interpreted.


•       signal(s) out —

  signal(s) out is an array of signals that have been filtered according to the filter specifications
  controls.

•        filter information —

   filter information contains the magnitude and phase responses of the filter in a cluster that is
  ready to graph. filter information also contains the order of the filter.

      •      magnitude H(w) —

      magnitude H(w) is the magnitude response of the filter. You can wire this cluster to a graph.

             •       f0 —

            f0 is the start frequency of the magnitude response.

             •       df —

           df is the spacing between elements of the magnitude response in hertz.

             •     Mag H(w) —

        Mag H(w) is an array of values containing the magnitude response of the filter.


      •      phase H(w) —

      Phase H(w) is an array of values containing the phase response of the filter, expressed in
      degrees.

             •       f0 —


                                                   © National Instruments 4291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4292 ordinal=4292 -->
## Functions

Functions


                      f0 is the start frequency of the phase response.

                           •       df —

                     df is the spacing between elements of the magnitude response in hertz.

                           •      Phase H(w) —

                  phase H(w) is the phase response of the filter.


                     •      order —

                order is the order of the filter.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The Digital IIR Filter VI filters the signal(s) in a waveform array according to the IIR filter
       specifications and optional IIR filter specifications arrays. If you are filtering multiple
      waveforms, the VI applies a different filter to each of the input waveforms and
       maintains a separate filter state for each waveform. The VI uses optional IIR filter
       specifications only if Filter Order is less than or equal to zero. You do not need to wire
       reset filter. This VI resets itself the first time it is called.

           Note In general, IIR second-order stages provide more stable results than
              the IIR fourth-order stages. National Instruments recommends that you
               specify IIR 2nd Order as the filter structure option with Bandpass or
           Bandstop as the Type for extreme IIR filter specifications, such as very
             narrow passband or stopband.

      The Digital IIR Filter VI can perform single-channel measurements in both one-shot
     mode (single call) and continuous mode (multiple calls with history). It can perform
       multichannel measurements only in one-shot mode. If you want to make multiple-


4292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4293 ordinal=4293 -->
## Functions

Functions

channel measurements in continuous mode, either use the multi-channel instance of
this VI or use one instance of this VI per channel.

The single-channel instance of this VI is intended primarily for continuous processing
of a single channel. Do not generalize this behavior to the multi-channel case, typically
by using this single-channel VI in a For Loop to continuously process multiple channels
by indexing an array of waveforms.

The single-channel instance of this VI maintains internal state information for a single
channel only. Calling this VI to process another channel without clearing the history
using the reset filter control results in an unexpected behavior of this VI because the
internal state information is passed from one channel to another.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Measurements\
   Frequency Analysis of a Filter Design.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   IIR Filtering Using Optional Specs.vi
  • labview\examples\Signal Processing\Waveform Conditioning\
   IIR Filtering and Response.vi

ContinuousContinuous ConvolutionConvolution (FIR)(FIR)

Convolves single or multiple waveforms and one or more kernels with state, allowing
subsequent calls to be processed in a continuous manner. If you are convolving
multiple waveforms, the VI maintains separate convolution states for each waveform.


  • Continuous Waveform Convolution for 1 Chan VI
  • Continuous Waveform Convolution for N Chan VI


                                                    © National Instruments 4293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4294 ordinal=4294 -->
## Functions

Functions

      ContinuousContinuous WaveformWaveform ConvolutionConvolution forfor 11 ChanChan VIVI

      Convolves single or multiple waveforms and one or more kernels with state, allowing
      subsequent calls to be processed in a continuous manner. If you are convolving
       multiple waveforms, the VI maintains separate convolution states for each waveform.


      Inputs/Outputs

               •       reset —

             reset forces the internal history buffer to be reset to zero when it is TRUE.

               •       signal in —

             signal in is the signal to be convolved with kernel.

               •      kernel —

            kernel is the sequence by which signal in is convolved.

               •      algorithm —

            algorithm specifies the method used for computing the convolution. When algorithm is set to
              direct, the VI computes convolution using the direct form of linear convolution: x*y[i] =
             Sum(x[k]y[i-k]) When algorithm is set to frequency domain (default), the VI computes
            convolution using an FFT-based technique.

           0     direct
           1     frequency domain

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      delay output with half kernel length —

4294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4295 ordinal=4295 -->
## Functions

Functions


    delay output with half kernel length causes signal out to be delayed in time by half the length
     of the kernel when TRUE. Half kernel length is computed by 0.5*N*dt where N is the number of
    elements in kernel, and dt is from signal in.

   •       signal out —

    signal out is the result of the convolution of the of signal in and kernel.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ContinuousContinuous WaveformWaveform ConvolutionConvolution forfor NN ChanChan VIVI

Convolves single or multiple waveforms and one or more kernels with state, allowing
subsequent calls to be processed in a continuous manner. If you are convolving
multiple waveforms, the VI maintains separate convolution states for each waveform.


Inputs/Outputs

   •       reset —

    reset forces the internal history buffer to be reset to zero when it is TRUE.

   •       signals in —

    signals in are the signals to be convolved with kernels.

   •      kernels —

    kernels are the sequences by which signals in are convolved.

   •      algorithm —


                                                    © National Instruments 4295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4296 ordinal=4296 -->
## Functions

Functions


            algorithm specifies the method used for computing the convolution. When algorithm is set to
              direct, the VI computes convolution using the direct form of linear convolution: x*y[i] =
             Sum(x[k]y[i-k]) When algorithm is set to frequency domain (default), the VI computes
            convolution using an FFT-based technique.

           0     direct
           1     frequency domain

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      delay output with half kernel length —

            delay output with half kernel length causes signal out to be delayed in time by half the length
             of the kernel when TRUE. Half kernel length is computed by 0.5*N*dt where N is the number of
           elements in kernel, and dt is from signal in.

               •       signals out —

             signals out is the result of the convolution of each element of signals in with the corresponding
          row of kernels.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     ScaledScaled WindowWindow

       Applies a scaled window to the time-domain signal and outputs window constants for
       further analysis. Wire data to the signal in input to determine the polymorphic
       instance to use or manually select the instance.


            • Scaled Window for 1 Chan VI
            • Scaled Window for N Chan VI


4296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4297 ordinal=4297 -->
## Functions

Functions

  • Scaled Window for 1 Chan (CDB) VI
  • Scaled Window for N Chan (CDB) VI

The windowed time-domain signal is scaled so that when the power or amplitude
spectrum of the windowed waveform is computed, all windows provide the same level
within the accuracy constraints of the window. This VI also returns important window
constants for the selected window. These constants are useful when you use VIs that
perform computations on the power spectrum, such as the Power & Frequency
Estimate VI.

Defining Equations

All cosine windows without scaling are defined by the following equation.


where            , nis the number of elements in X, and mis the number of elements in
the window coefficient array a[].

For this VI, the preceding equation is modified to include division by the coherent gain
(cg), as shown in the following equation.


Coefficients and Window Parameters for the Different Window Types

This section provides information about the acoefficients and window parameters for
each window type available in this VI. Each window type has the following window
parameters:

  • coherent gain (cg)
  • equivalent noise bandwidth (enbw)
  • 6dB bandwidth (6dB BW)


                                                    © National Instruments 4297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4298 ordinal=4298 -->
## Functions

Functions


        Rectangle
         a[] is empty because no window is applied.                 cg = 1
       The window equation is yi = xi                      enbw = 1

                                                      6dB BW = 1.21
       a0 = 0.5                                                cg = 0.5
       a1 = 0.5                                       enbw = 1.5

                                                      6dB BW = 2.0
       a0 = 0.42323                                           cg = 0.42323
       a1 = 0.49755                                    enbw = 1.708538
       a2 = 0.07922                                      6dB BW = 2.27
       a0 = 0.42659071367153911200                            cg = 0.42659071367
       a1 = 0.49656061908856408100                       enbw = 1.693699
       a2 = 0.07684866723989682010                        6dB BW = 2.25
       a0 = 0.42                                               cg = 0.42
       a1 = 0.5                                       enbw = 1.726757
       a2 = 0.08                                        6dB BW = 2.3
       a0 = 0.215578948                                       cg = 0.215578948
       a1 = 0.41663158                                 enbw = 3.770246506303
       a2 = 0.277263158                                  6dB BW = 4.58
       a3 = 0.083578947
       a4 = 0.006947368
       a0 = 0.35875                                           cg = 0.35875
       a1 = 0.48829                                    enbw = 2.004353
       a2 = 0.14128                                      6dB BW = 2.67
       a3 = 0.01168


4298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4299 ordinal=4299 -->
## Functions

Functions


 Rectangle
 a0 = 0.27105140069342415                               cg = 0.27105140069342415
 a1 = 0.43329793923448606                         enbw = 2.631905
 a2 = 0.21812299954311062                           6dB BW = 3.5
 a3 = 0.065925446388030898
 a4 = 0.010811742098372268
 a5 = 7.7658482522509342E-4
 a6 = 1.3887217350903198E-5
 a0 = 0.323215218                                       cg = 0.323215218
 a1 = 0.471492057                                enbw = 2.215350782519
 a2 = 0.17553428                                   6dB BW = 2.95
 a3 = 0.028497078
 a4 = 0.001261367

ScaledScaled WindowWindow forfor 11 ChanChan VIVI

Applies a scaled window to the time-domain signal and outputs window constants for
further analysis. Wire data to the signal in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •       signal in —

    signal in is the signal to be windowed.

   •     window —


                                                    © National Instruments 4299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4300 ordinal=4300 -->
## Functions

Functions


          window specifies the time-domain window used.

               •     window parameter —

          window parameter is the beta parameter for a Kaiser window, the standard deviation for a
            Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       signal out —

             signal out is the windowed signal.

               •     window constants —

          window constants contains important constants for the selected window.

                     •     eq noise BW —

              eq noise BW is the equivalent noise bandwidth of the selected window.

               To compute the power in a given frequency span, divide a sum of individual FFT lines by eq
                noise BW.

                     •      coherent gain —

               coherent gain is the inverse of the scaling factor applied due to the window.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The windowed time-domain signal is scaled so that when the power or amplitude
      spectrum of the windowed waveform is computed, all windows provide the same level

4300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4301 ordinal=4301 -->
## Functions

Functions

within the accuracy constraints of the window. This VI also returns important window
constants for the selected window. These constants are useful when you use VIs that
perform computations on the power spectrum, such as the Power & Frequency
Estimate VI.

Defining Equations

All cosine windows without scaling are defined by the following equation.


where            , nis the number of elements in X, and mis the number of elements in
the window coefficient array a[].

For this VI, the preceding equation is modified to include division by the coherent gain
(cg), as shown in the following equation.


Coefficients and Window Parameters for the Different Window Types

This section provides information about the acoefficients and window parameters for
each window type available in this VI. Each window type has the following window
parameters:

  • coherent gain (cg)
  • equivalent noise bandwidth (enbw)
  • 6dB bandwidth (6dB BW)


 Rectangle
 a[] is empty because no window is applied.                 cg = 1
 The window equation is yi = xi                      enbw = 1

                                                6dB BW = 1.21
 a0 = 0.5                                                cg = 0.5


                                                    © National Instruments 4301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4302 ordinal=4302 -->
## Functions

Functions


        Rectangle
       a1 = 0.5                                       enbw = 1.5

                                                      6dB BW = 2.0
       a0 = 0.42323                                           cg = 0.42323
       a1 = 0.49755                                    enbw = 1.708538
       a2 = 0.07922                                      6dB BW = 2.27
       a0 = 0.42659071367153911200                            cg = 0.42659071367
       a1 = 0.49656061908856408100                       enbw = 1.693699
       a2 = 0.07684866723989682010                        6dB BW = 2.25
       a0 = 0.42                                               cg = 0.42
       a1 = 0.5                                       enbw = 1.726757
       a2 = 0.08                                        6dB BW = 2.3
       a0 = 0.215578948                                       cg = 0.215578948
       a1 = 0.41663158                                 enbw = 3.770246506303
       a2 = 0.277263158                                  6dB BW = 4.58
       a3 = 0.083578947
       a4 = 0.006947368
       a0 = 0.35875                                           cg = 0.35875
       a1 = 0.48829                                    enbw = 2.004353
       a2 = 0.14128                                      6dB BW = 2.67
       a3 = 0.01168
       a0 = 0.27105140069342415                               cg = 0.27105140069342415
       a1 = 0.43329793923448606                         enbw = 2.631905
       a2 = 0.21812299954311062                           6dB BW = 3.5
       a3 = 0.065925446388030898


4302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4303 ordinal=4303 -->
## Functions

Functions


 Rectangle
 a4 = 0.010811742098372268
 a5 = 7.7658482522509342E-4
 a6 = 1.3887217350903198E-5
 a0 = 0.323215218                                       cg = 0.323215218
 a1 = 0.471492057                                enbw = 2.215350782519
 a2 = 0.17553428                                   6dB BW = 2.95
 a3 = 0.028497078
 a4 = 0.001261367

ScaledScaled WindowWindow forfor NN ChanChan VIVI

Applies a scaled window to the time-domain signal and outputs window constants for
further analysis. Wire data to the signal in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •       signals in —

    signals in is the array of signals to window.

   •     window —

   window specifies the time-domain window used.

   •     window parameter —

   window parameter is the beta parameter for a Kaiser window, the standard deviation for a
    Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev


                                                    © National Instruments 4303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4304 ordinal=4304 -->
## Functions

Functions


           window. If window is any other window, this VI ignores this input.

          The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
            standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       signals out —

             signals out returns the array of windowed signals.

               •     window constants —

          window constants contains important constants for the selected window.

                     •     eq noise BW —

              eq noise BW is the equivalent noise bandwidth of the selected window.

               To compute the power in a given frequency span, divide a sum of individual FFT lines by eq
                noise BW.

                     •      coherent gain —

               coherent gain is the inverse of the scaling factor applied due to the window.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The windowed time-domain signal is scaled so that when the power or amplitude
      spectrum of the windowed waveform is computed, all windows provide the same level
       within the accuracy constraints of the window. This VI also returns important window
       constants for the selected window. These constants are useful when you use VIs that
      perform computations on the power spectrum, such as the Power & Frequency
       Estimate VI.


4304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4305 ordinal=4305 -->
## Functions

Functions

Defining Equations

All cosine windows without scaling are defined by the following equation.


where            , nis the number of elements in X, and mis the number of elements in
the window coefficient array a[].

For this VI, the preceding equation is modified to include division by the coherent gain
(cg), as shown in the following equation.


Coefficients and Window Parameters for the Different Window Types

This section provides information about the acoefficients and window parameters for
each window type available in this VI. Each window type has the following window
parameters:

  • coherent gain (cg)
  • equivalent noise bandwidth (enbw)
  • 6dB bandwidth (6dB BW)


 Rectangle
 a[] is empty because no window is applied.                 cg = 1
 The window equation is yi = xi                      enbw = 1

                                                6dB BW = 1.21
 a0 = 0.5                                                cg = 0.5
 a1 = 0.5                                       enbw = 1.5

                                                6dB BW = 2.0
 a0 = 0.42323                                           cg = 0.42323


                                                    © National Instruments 4305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4306 ordinal=4306 -->
## Functions

Functions


        Rectangle
       a1 = 0.49755                                    enbw = 1.708538
       a2 = 0.07922                                      6dB BW = 2.27
       a0 = 0.42659071367153911200                            cg = 0.42659071367
       a1 = 0.49656061908856408100                       enbw = 1.693699
       a2 = 0.07684866723989682010                        6dB BW = 2.25
       a0 = 0.42                                               cg = 0.42
       a1 = 0.5                                       enbw = 1.726757
       a2 = 0.08                                        6dB BW = 2.3
       a0 = 0.215578948                                       cg = 0.215578948
       a1 = 0.41663158                                 enbw = 3.770246506303
       a2 = 0.277263158                                  6dB BW = 4.58
       a3 = 0.083578947
       a4 = 0.006947368
       a0 = 0.35875                                           cg = 0.35875
       a1 = 0.48829                                    enbw = 2.004353
       a2 = 0.14128                                      6dB BW = 2.67
       a3 = 0.01168
       a0 = 0.27105140069342415                               cg = 0.27105140069342415
       a1 = 0.43329793923448606                         enbw = 2.631905
       a2 = 0.21812299954311062                           6dB BW = 3.5
       a3 = 0.065925446388030898
       a4 = 0.010811742098372268
       a5 = 7.7658482522509342E-4
       a6 = 1.3887217350903198E-5

4306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4307 ordinal=4307 -->
## Functions

Functions


 Rectangle
 a0 = 0.323215218                                       cg = 0.323215218
 a1 = 0.471492057                                enbw = 2.215350782519
 a2 = 0.17553428                                   6dB BW = 2.95
 a3 = 0.028497078
 a4 = 0.001261367

ScaledScaled WindowWindow forfor 11 ChanChan (CDB)(CDB) VIVI

Applies a scaled window to the time-domain signal and outputs window constants for
further analysis. Wire data to the signal in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •       signal in —

    signal in is the complex signal to be windowed.

   •     window —

   window specifies the time-domain window used.

   •     window parameter —

   window parameter is the beta parameter for a Kaiser window, the standard deviation for a
    Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •       error in (no error) —

                                                    © National Instruments 4307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4308 ordinal=4308 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       signal out —

             signal out is the complex windowed signal.

               •     window constants —

          window constants contains important constants for the selected window.

                     •     eq noise BW —

              eq noise BW is the equivalent noise bandwidth of the selected window.

               To compute the power in a given frequency span, divide a sum of individual FFT lines by eq
                noise BW.

                     •      coherent gain —

               coherent gain is the inverse of the scaling factor applied due to the window.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The windowed time-domain signal is scaled so that when the power or amplitude
      spectrum of the windowed waveform is computed, all windows provide the same level
       within the accuracy constraints of the window. This VI also returns important window
       constants for the selected window. These constants are useful when you use VIs that
      perform computations on the power spectrum, such as the Power & Frequency
       Estimate VI.

      Defining Equations

         All cosine windows without scaling are defined by the following equation.


4308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4309 ordinal=4309 -->
## Functions

Functions

where            , nis the number of elements in X, and mis the number of elements in
the window coefficient array a[].

For this VI, the preceding equation is modified to include division by the coherent gain
(cg), as shown in the following equation.


Coefficients and Window Parameters for the Different Window Types

This section provides information about the acoefficients and window parameters for
each window type available in this VI. Each window type has the following window
parameters:

  • coherent gain (cg)
  • equivalent noise bandwidth (enbw)
  • 6dB bandwidth (6dB BW)


 Rectangle
 a[] is empty because no window is applied.                 cg = 1
 The window equation is yi = xi                      enbw = 1

                                                6dB BW = 1.21
 a0 = 0.5                                                cg = 0.5
 a1 = 0.5                                       enbw = 1.5

                                                6dB BW = 2.0
 a0 = 0.42323                                           cg = 0.42323
 a1 = 0.49755                                    enbw = 1.708538
 a2 = 0.07922                                      6dB BW = 2.27
 a0 = 0.42659071367153911200                            cg = 0.42659071367
 a1 = 0.49656061908856408100                       enbw = 1.693699
 a2 = 0.07684866723989682010                        6dB BW = 2.25

                                                    © National Instruments 4309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4310 ordinal=4310 -->
## Functions

Functions


        Rectangle
       a0 = 0.42                                               cg = 0.42
       a1 = 0.5                                       enbw = 1.726757
       a2 = 0.08                                        6dB BW = 2.3
       a0 = 0.215578948                                       cg = 0.215578948
       a1 = 0.41663158                                 enbw = 3.770246506303
       a2 = 0.277263158                                  6dB BW = 4.58
       a3 = 0.083578947
       a4 = 0.006947368
       a0 = 0.35875                                           cg = 0.35875
       a1 = 0.48829                                    enbw = 2.004353
       a2 = 0.14128                                      6dB BW = 2.67
       a3 = 0.01168
       a0 = 0.27105140069342415                               cg = 0.27105140069342415
       a1 = 0.43329793923448606                         enbw = 2.631905
       a2 = 0.21812299954311062                           6dB BW = 3.5
       a3 = 0.065925446388030898
       a4 = 0.010811742098372268
       a5 = 7.7658482522509342E-4
       a6 = 1.3887217350903198E-5
       a0 = 0.323215218                                       cg = 0.323215218
       a1 = 0.471492057                                enbw = 2.215350782519
       a2 = 0.17553428                                   6dB BW = 2.95
       a3 = 0.028497078
       a4 = 0.001261367

4310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4311 ordinal=4311 -->
## Functions

Functions

ScaledScaled WindowWindow forfor NN ChanChan (CDB)(CDB) VIVI

Applies a scaled window to the time-domain signal and outputs window constants for
further analysis. Wire data to the signal in input to determine the polymorphic
instance to use or manually select the instance.


Inputs/Outputs

   •       signals in —

    signals in is the array of complex signals to window.

   •     window —

   window specifies the time-domain window used.

   •     window parameter —

   window parameter is the beta parameter for a Kaiser window, the standard deviation for a
    Gaussian window, and the ratio, s, of the main lobe to the side lobe for a Dolph-Chebyshev
    window. If window is any other window, this VI ignores this input.

    The default value of window parameter is NaN, which sets beta to 0 for a Kaiser window, the
    standard deviation to 0.2 for a Gaussian window, and sto 60 for a Dolph-Chebyshev window.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       signals out —

    signals out returns the array of complex windowed signals.

   •     window constants —

   window constants contains important constants for the selected window.


                                                    © National Instruments 4311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4312 ordinal=4312 -->
## Functions

Functions


                     •     eq noise BW —

              eq noise BW is the equivalent noise bandwidth of the selected window.

               To compute the power in a given frequency span, divide a sum of individual FFT lines by eq
                noise BW.

                     •      coherent gain —

               coherent gain is the inverse of the scaling factor applied due to the window.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The windowed time-domain signal is scaled so that when the power or amplitude
      spectrum of the windowed waveform is computed, all windows provide the same level
       within the accuracy constraints of the window. This VI also returns important window
       constants for the selected window. These constants are useful when you use VIs that
      perform computations on the power spectrum, such as the Power & Frequency
       Estimate VI.

      Defining Equations

         All cosine windows without scaling are defined by the following equation.


      where            , nis the number of elements in X, and mis the number of elements in
       the window coefficient array a[].

       For this VI, the preceding equation is modified to include division by the coherent gain
        (cg), as shown in the following equation.


4312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4313 ordinal=4313 -->
## Functions

Functions

Coefficients and Window Parameters for the Different Window Types

This section provides information about the acoefficients and window parameters for
each window type available in this VI. Each window type has the following window
parameters:

  • coherent gain (cg)
  • equivalent noise bandwidth (enbw)
  • 6dB bandwidth (6dB BW)


 Rectangle
 a[] is empty because no window is applied.                 cg = 1
 The window equation is yi = xi                      enbw = 1

                                                6dB BW = 1.21
 a0 = 0.5                                                cg = 0.5
 a1 = 0.5                                       enbw = 1.5

                                                6dB BW = 2.0
 a0 = 0.42323                                           cg = 0.42323
 a1 = 0.49755                                    enbw = 1.708538
 a2 = 0.07922                                      6dB BW = 2.27
 a0 = 0.42659071367153911200                            cg = 0.42659071367
 a1 = 0.49656061908856408100                       enbw = 1.693699
 a2 = 0.07684866723989682010                        6dB BW = 2.25
 a0 = 0.42                                               cg = 0.42
 a1 = 0.5                                       enbw = 1.726757
 a2 = 0.08                                        6dB BW = 2.3
 a0 = 0.215578948                                       cg = 0.215578948
 a1 = 0.41663158                                 enbw = 3.770246506303


                                                    © National Instruments 4313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4314 ordinal=4314 -->
## Functions

Functions


        Rectangle
       a2 = 0.277263158                                  6dB BW = 4.58
       a3 = 0.083578947
       a4 = 0.006947368
       a0 = 0.35875                                           cg = 0.35875
       a1 = 0.48829                                    enbw = 2.004353
       a2 = 0.14128                                      6dB BW = 2.67
       a3 = 0.01168
       a0 = 0.27105140069342415                               cg = 0.27105140069342415
       a1 = 0.43329793923448606                         enbw = 2.631905
       a2 = 0.21812299954311062                           6dB BW = 3.5
       a3 = 0.065925446388030898
       a4 = 0.010811742098372268
       a5 = 7.7658482522509342E-4
       a6 = 1.3887217350903198E-5
       a0 = 0.323215218                                       cg = 0.323215218
       a1 = 0.471492057                                enbw = 2.215350782519
       a2 = 0.17553428                                   6dB BW = 2.95
       a3 = 0.028497078
       a4 = 0.001261367

      AlignAlign WaveformsWaveforms (continuous)(continuous)

      Performs element-wise alignment of waveforms and returns the aligned waveforms.
      The data types you wire to the waveform inputs determine the polymorphic instance
       to use.


4314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4315 ordinal=4315 -->
## Functions

Functions


  • Align N Waveforms (continuous) VI
  • Align M + N Waveforms (continuous) VI
  • Align N + 1 Waveforms (continuous) VI
  • Align 1 + N Waveforms (continuous) VI
  • Align two Waveforms (continuous) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Align and Subtract two Waveforms (continuous).vi

AlignAlign NN WaveformsWaveforms (continuous)(continuous) VIVI

Performs element-wise alignment of waveforms and returns the aligned waveforms.
The data types you wire to the waveform inputs determine the polymorphic instance
to use.


Inputs/Outputs

   •       reset —

    reset resets the phase to the phase control value and the time stamp to zero. The default is
    FALSE.

   •     waveforms in —

    waveforms in is an array of waveforms to align.


                                                    © National Instruments 4315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4316 ordinal=4316 -->
## Functions

Functions

               •       interpolation mode —

             interpolation mode specifies the interpolation method.

           0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.
             Linear (default)—Each output sample value is a linear interpolation between the two input           1            samples that are closest to it in time.
           2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
             FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled           3               values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •       interpolation —

             interpolation specifies whether interpolation is performed. The default is TRUE.

               •     waveforms out —

          waveforms out contains the aligned waveforms.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


4316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4317 ordinal=4317 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Align and Subtract two Waveforms (continuous).vi

AlignAlign MM ++ NN WaveformsWaveforms (continuous)(continuous) VIVI

Performs element-wise alignment of waveforms and returns the aligned waveforms.
The data types you wire to the waveform inputs determine the polymorphic instance
to use.


Inputs/Outputs

   •       reset —

    reset resets the phase to the phase control value and the time stamp to zero. The default is
    FALSE.

   •    M waveforms in —

   M waveforms in is an array of waveforms to align.

   •    N waveforms in —

   N waveforms in is an array of waveforms to align.

   •       interpolation mode —

    interpolation mode specifies the interpolation method.

    0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.


                                                    © National Instruments 4317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4318 ordinal=4318 -->
## Functions

Functions


             Linear (default)—Each output sample value is a linear interpolation between the two input           1
            samples that are closest to it in time.
           2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
             FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled           3               values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •       interpolation —

             interpolation specifies whether interpolation is performed. The default is TRUE.

               •    M aligned waveforms out —

       M aligned waveforms out is an array of aligned waveforms.

               •    N aligned waveforms out —

        N aligned waveforms out is an array of aligned waveforms.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


4318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4319 ordinal=4319 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Align and Subtract two Waveforms (continuous).vi

AlignAlign NN ++ 11 WaveformsWaveforms (continuous)(continuous) VIVI

Performs element-wise alignment of waveforms and returns the aligned waveforms.
The data types you wire to the waveform inputs determine the polymorphic instance
to use.


Inputs/Outputs

   •       reset —

    reset resets the phase to the phase control value and the time stamp to zero. The default is
    FALSE.

   •     waveforms in —

    waveforms in is an array of waveforms to align.

   •     waveform in —

    waveform in is a waveform to align.

   •       interpolation mode —

    interpolation mode specifies the interpolation method.

    0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.


                                                    © National Instruments 4319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4320 ordinal=4320 -->
## Functions

Functions


             Linear (default)—Each output sample value is a linear interpolation between the two input           1
            samples that are closest to it in time.
           2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
             FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled           3               values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •       interpolation —

             interpolation specifies whether interpolation is performed. The default is TRUE.

               •      aligned waveforms out —

            aligned waveforms out is an array of aligned waveforms.

               •      aligned waveform out —

            aligned waveform out contains an aligned waveform.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


4320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4321 ordinal=4321 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Align and Subtract two Waveforms (continuous).vi

AlignAlign 11 ++ NN WaveformsWaveforms (continuous)(continuous) VIVI

Performs element-wise alignment of waveforms and returns the aligned waveforms.
The data types you wire to the waveform inputs determine the polymorphic instance
to use.


Inputs/Outputs

   •       reset —

    reset resets the phase to the phase control value and the time stamp to zero. The default is
    FALSE.

   •     waveform in —

    waveform in is a waveform to align.

   •     waveforms in —

    waveforms in is an array of waveforms to align.

   •       interpolation mode —

    interpolation mode specifies the interpolation method.

    0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.


                                                    © National Instruments 4321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4322 ordinal=4322 -->
## Functions

Functions


             Linear (default)—Each output sample value is a linear interpolation between the two input           1
            samples that are closest to it in time.
           2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
             FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled           3               values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •       interpolation —

             interpolation specifies whether interpolation is performed. The default is TRUE.

               •      aligned waveform out —

            aligned waveform out contains an aligned waveform.

               •      aligned waveforms out —

            aligned waveforms out is an array of aligned waveforms.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


4322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4323 ordinal=4323 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Align and Subtract two Waveforms (continuous).vi

AlignAlign twotwo WaveformsWaveforms (continuous)(continuous) VIVI

Performs element-wise alignment of waveforms and returns the aligned waveforms.
The data types you wire to the waveform inputs determine the polymorphic instance
to use.

      Note

      The time and component values of the result are the same as those of
      waveform A in. If the dt values are not equal, error out returns a warning and
      waveform A out and waveform B out are empty.


Inputs/Outputs

   •       reset —

    reset resets the phase to the phase control value and the time stamp to zero. The default is
    FALSE.

   •     waveform A in —

    waveform A in is a waveform to align.

   •     waveform B in —

                                                    © National Instruments 4323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4324 ordinal=4324 -->
## Functions

Functions


          waveform B in is a waveform to align.

               •       interpolation mode —

             interpolation mode specifies the interpolation method.

           0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.
             Linear (default)—Each output sample value is a linear interpolation between the two input           1            samples that are closest to it in time.
           2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
             FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled           3               values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •       interpolation —

             interpolation specifies whether interpolation is performed. The default is TRUE.

               •     waveform A out —

          waveform A out is the waveform that results from aligning waveform A in and waveform B in.

               •     waveform B out —


4324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4325 ordinal=4325 -->
## Functions

Functions


    waveform B out is the waveform that results from aligning waveform B in and waveform A in.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Align and Subtract two Waveforms (continuous).vi

AlignAlign WaveformsWaveforms (single(single shot)shot)

Performs element-wise alignment of two waveforms and returns the aligned
waveforms. The data types you wire to the waveform inputs determine the
polymorphic instance to use.


  • Align N Waveforms (single shot) VI
  • Align M + N Waveforms (single shot) VI
  • Align N + 1 Waveforms (single shot) VI
  • Align 1 + N Waveforms (single shot) VI
  • Align two Waveforms (single shot) VI

AlignAlign NN WaveformsWaveforms (single(single shot)shot) VIVI

Performs element-wise alignment of two waveforms and returns the aligned
waveforms. The data types you wire to the waveform inputs determine the
polymorphic instance to use.


                                                    © National Instruments 4325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4326 ordinal=4326 -->
## Functions

Functions


      Inputs/Outputs

               •      exported interval —

           exported interval defines the time stamp of the waveform outputs.

           0   Common (default)
           1     Global

               •     open interval? (T) —

          open interval? defines the interval over which the input waveform extends. The default is TRUE,
           which selects an open interval.

            For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
              interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
              interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

               •     waveforms in —

          waveforms in is an array of waveforms to align.

               •       interpolation mode —

             interpolation mode specifies the interpolation method.

           0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.
             Linear (default)—Each output sample value is a linear interpolation between the two input
           1
            samples that are closest to it in time.
           2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
             FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled
           3
               values.

               •       error in (no error) —


4326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4327 ordinal=4327 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      FIR filter specifications —

    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •       interpolation —

    interpolation specifies whether interpolation is performed. The default is TRUE.

   •      aligned waveforms out —

    aligned waveforms out is an array of aligned waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AlignAlign MM ++ NN WaveformsWaveforms (single(single shot)shot) VIVI

Performs element-wise alignment of two waveforms and returns the aligned
waveforms. The data types you wire to the waveform inputs determine the
polymorphic instance to use.


                                                    © National Instruments 4327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4328 ordinal=4328 -->
## Functions

Functions


      Inputs/Outputs

               •      exported interval —

           exported interval defines the time stamp of the waveform outputs.

           0   Common (default)
           1     Global

               •     open interval? (T) —

          open interval? defines the interval over which the input waveform extends. The default is TRUE,
           which selects an open interval.

            For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
              interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
              interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

               •    M waveforms in —

       M waveforms in is an array of waveforms to align.

               •    N waveforms in —

        N waveforms in is an array of waveforms to align.

               •       interpolation mode —

             interpolation mode specifies the interpolation method.

           0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.
             Linear (default)—Each output sample value is a linear interpolation between the two input
           1
            samples that are closest to it in time.
           2 Spline—Uses the spline interpolation algorithm to compute the resampled values.


4328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4329 ordinal=4329 -->
## Functions

Functions


     FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled    3
      values.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      FIR filter specifications —

    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •       interpolation —

    interpolation specifies whether interpolation is performed. The default is TRUE.

   •    M aligned waveforms out —

   M aligned waveforms out is an array of aligned waveforms.

   •    N aligned waveforms out —

   N aligned waveforms out is an array of aligned waveforms.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


AlignAlign NN ++ 11 WaveformsWaveforms (single(single shot)shot) VIVI

Performs element-wise alignment of two waveforms and returns the aligned

                                                    © National Instruments 4329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4330 ordinal=4330 -->
## Functions

Functions

      waveforms. The data types you wire to the waveform inputs determine the
      polymorphic instance to use.


      Inputs/Outputs

               •      exported interval —

           exported interval defines the time stamp of the waveform outputs.

           0   Common (default)
           1     Global

               •     open interval? (T) —

          open interval? defines the interval over which the input waveform extends. The default is TRUE,
           which selects an open interval.

            For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
              interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
              interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

               •     waveforms in —

          waveforms in is an array of waveforms to align.

               •     waveform in —

          waveform in is a waveform to align.

               •       interpolation mode —

             interpolation mode specifies the interpolation method.


4330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4331 ordinal=4331 -->
## Functions

Functions


  0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.
   Linear (default)—Each output sample value is a linear interpolation between the two input  1   samples that are closest to it in time.
  2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
   FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled  3
    values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      FIR filter specifications —

  FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

      •       alias rejection (dB) —

       alias rejection (dB) specifies the minimum attenuation level of signal components aliased
       after any resampling operation. The default is 120.

      •      normalized bandwidth —

      normalized bandwidth specifies the fraction of the new sampling rate that is not
       attenuated. The default is 0.4536.


•       interpolation —

  interpolation specifies whether interpolation is performed. The default is TRUE.

•      aligned waveforms out —

  aligned waveforms out is an array of aligned waveforms.

•      aligned waveform out —

  aligned waveform out contains an aligned waveform.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 4331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4332 ordinal=4332 -->
## Functions

Functions

       AlignAlign 11 ++ NN WaveformsWaveforms (single(single shot)shot) VIVI

      Performs element-wise alignment of two waveforms and returns the aligned
      waveforms. The data types you wire to the waveform inputs determine the
      polymorphic instance to use.


      Inputs/Outputs

               •      exported interval —

           exported interval defines the time stamp of the waveform outputs.

           0   Common (default)
           1     Global

               •     open interval? (T) —

          open interval? defines the interval over which the input waveform extends. The default is TRUE,
           which selects an open interval.

            For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
              interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
              interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

               •     waveform in —

          waveform in is a waveform to align.

               •     waveforms in —

          waveforms in is an array of waveforms to align.

               •       interpolation mode —


4332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4333 ordinal=4333 -->
## Functions

Functions


  interpolation mode specifies the interpolation method.

  0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.
   Linear (default)—Each output sample value is a linear interpolation between the two input  1   samples that are closest to it in time.
  2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
   FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled
  3    values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      FIR filter specifications —

  FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

      •       alias rejection (dB) —

       alias rejection (dB) specifies the minimum attenuation level of signal components aliased
       after any resampling operation. The default is 120.

      •      normalized bandwidth —

      normalized bandwidth specifies the fraction of the new sampling rate that is not
       attenuated. The default is 0.4536.


•       interpolation —

  interpolation specifies whether interpolation is performed. The default is TRUE.

•      aligned waveform out —

  aligned waveform out contains an aligned waveform.

•      aligned waveforms out —

  aligned waveforms out is an array of aligned waveforms.

•       error out —


                                                   © National Instruments 4333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4334 ordinal=4334 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


       AlignAlign twotwo WaveformsWaveforms (single(single shot)shot) VIVI

      Performs element-wise alignment of two waveforms and returns the aligned
      waveforms. The data types you wire to the waveform inputs determine the
      polymorphic instance to use.

           Note

            The time and component values of the result are the same as those of
            waveform A in. If the dt values are not equal, error out returns a warning and
            waveform A out and waveform B out are empty.


      Inputs/Outputs

               •      exported interval —

           exported interval defines the time stamp of the waveform outputs.

           0   Common (default)
           1     Global

               •     open interval? (T) —

          open interval? defines the interval over which the input waveform extends. The default is TRUE,
           which selects an open interval.


4334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4335 ordinal=4335 -->
## Functions

Functions


  For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
  interval defines the waveform as extending over the time interval 0 ≤ t< 2dt, and a closed
  interval defines the waveform as extending over the time interval 0 ≤ t< 3dt.

•     waveform A in —

  waveform A in is a waveform to align.

•     waveform B in —

  waveform B in is a waveform to align.

•       interpolation mode —

  interpolation mode specifies the interpolation method.

  0 Coerce—Each output sample is set equal to the input sample value that is closest to it in time.
   Linear (default)—Each output sample value is a linear interpolation between the two input  1   samples that are closest to it in time.
  2 Spline—Uses the spline interpolation algorithm to compute the resampled values.
   FIR filter—Uses a finite impulse response (FIR) filtering algorithm to compute the resampled
  3    values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      FIR filter specifications —

  FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

      •       alias rejection (dB) —

       alias rejection (dB) specifies the minimum attenuation level of signal components aliased
       after any resampling operation. The default is 120.

      •      normalized bandwidth —

      normalized bandwidth specifies the fraction of the new sampling rate that is not
       attenuated. The default is 0.4536.


                                                   © National Instruments 4335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4336 ordinal=4336 -->
## Functions

Functions

               •       interpolation —

             interpolation specifies whether interpolation is performed. The default is TRUE.

               •     waveform A out —

          waveform A out is the waveform that results from aligning waveform A in and waveform B in.

               •     waveform B out —

          waveform B out is the waveform that results from aligning waveform B in and waveform A in.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     ResampleResample WaveformsWaveforms (continuous)(continuous)

      Resamples an input waveform according to the user-defined values for t0 and dt. Wire
       data to the waveform in input to determine the polymorphic instance to use or
      manually select the instance.


            • Resample Waveform (continuous) VI
            • Resample N Waveforms (continuous) VI
            • Resample Waveform (continuous, t0 DBL) VI
            • Resample N Waveforms (continuous, t0 DBL) VI

           If t0 is less than the actual t0 value of the input waveform, that is the time stamp of the
         first input sample, the VI coerces t0 to the first value greater than the actual t0 that
          fulfills the following equation.

      used t0 – t0 = n*dt

      where n is an integer.


4336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4337 ordinal=4337 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Resampling a Waveform (continuous).vi

ResampleResample WaveformWaveform (continuous)(continuous) VIVI

Resamples an input waveform according to the user-defined values for t0 and dt. Wire
data to the waveform in input to determine the polymorphic instance to use or
manually select the instance.


Inputs/Outputs

   •       reset —

    reset resets the phase to the phase control value and the time stamp to zero. The default is
    FALSE.

   •     waveform in —

    waveform in is a waveform to align.

   •      dt —

    dt is the user-defined sampling interval for resampled waveform out.

   •       t0 —

    t0 is the user-defined start time value for resampled waveform out.

   •       interpolation mode —


                                                    © National Instruments 4337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4338 ordinal=4338 -->
## Functions

Functions


             interpolation mode specifies the resampling algorithm used for the resampling.

             Coerce—Specifies that each output sample is set equal to the input sample value that is closest
           0              to it in time.
             Linear (default)—Specifies that each output sample value is a linear interpolation between the           1           two input samples that are closest to it in time.
             Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled
           2               values.
             FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to           3           compute the resampled values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —

            FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

                     •       alias rejection (dB) —

                   alias rejection (dB) specifies the minimum attenuation level of signal components aliased
                   after any resampling operation. The default is 120.

                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •      resampled waveform out —

           resampled waveform out contains the resampled waveform.

               •      next t0 —

            next t0 is the start time of the next resampled waveform out, if reset is FALSE.

               •      used t0 —

           used t0 returns the actual start time of resampled waveform out.


4338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4339 ordinal=4339 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       t0 adjusted warning —

    t0 adjusted warning returns TRUE if used t0 does not equal t0.


If t0 is less than the actual t0 value of the input waveform, that is the time stamp of the
first input sample, the VI coerces t0 to the first value greater than the actual t0 that
fulfills the following equation.

used t0 – t0 = n*dt

where n is an integer.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Resampling a Waveform (continuous).vi

ResampleResample NN WaveformsWaveforms (continuous)(continuous) VIVI

Resamples an input waveform according to the user-defined values for t0 and dt. Wire
data to the waveform in input to determine the polymorphic instance to use or
manually select the instance.

      Note Resamples waveforms in according to the user-defined t0 and dt
        values.


                                                    © National Instruments 4339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4340 ordinal=4340 -->
## Functions

Functions


      Inputs/Outputs

               •       reset —

             reset resets the phase to the phase control value and the time stamp to zero. The default is
            FALSE.

               •     waveforms in —

          waveforms in is an array of waveforms to align.

               •      dt —

            dt is the user-defined sampling interval for resampled waveforms out.

               •       t0 —

             t0 is the user-defined time stamp value for resampled waveforms out.

               •       interpolation mode —

             interpolation mode specifies the resampling algorithm used for the resampling.

             Coerce—Specifies that each output sample is set equal to the input sample value that is closest
           0              to it in time.
             Linear (default)—Specifies that each output sample value is a linear interpolation between the
           1
           two input samples that are closest to it in time.
             Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled
           2
               values.
             FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to
           3
           compute the resampled values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


4340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4341 ordinal=4341 -->
## Functions

Functions

   •      FIR filter specifications —

    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      resampled waveforms out —

    resampled waveforms out returns an array containing the resampled waveforms.

   •      next t0's —

    next t0's is the timestamp of the next resampled waveform out, if reset is FALSE.

   •      used t0's —

    used t0's returns the array of actual time stamps for resampled waveforms out.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       t0 adjusted warnings —

    t0 adjusted warnings returns TRUE in each element of the array where the corresponding used
     t0's element does not equal t0.


If t0 is less than the actual t0 value of the input waveform, that is the time stamp of the
first input sample, the VI coerces t0 to the first value greater than the actual t0 that
fulfills the following equation.

used t0 – t0 = n*dt

where n is an integer.

                                                    © National Instruments 4341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4342 ordinal=4342 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Resampling a Waveform (continuous).vi

      ResampleResample WaveformWaveform (continuous,(continuous, t0t0 DBL)DBL) VIVI

      Resamples an input waveform according to the user-defined values for t0 and dt. Wire
       data to the waveform in input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •       reset —

             reset resets the phase to the phase control value and the time stamp to zero. The default is
            FALSE.

               •     waveform in —

          waveform in is a waveform to align.

               •      dt —

            dt is the user-defined sampling interval for resampled waveform out.

               •       t0 —

             t0 is the user-defined start time value for resampled waveform out.

               •       interpolation mode —


4342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4343 ordinal=4343 -->
## Functions

Functions


  interpolation mode specifies the resampling algorithm used for the resampling.

   Coerce—Specifies that each output sample is set equal to the input sample value that is closest
  0    to it in time.
   Linear (default)—Specifies that each output sample value is a linear interpolation between the  1   two input samples that are closest to it in time.
   Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled
  2    values.
   FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to  3   compute the resampled values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      FIR filter specifications —

  FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

      •       alias rejection (dB) —

       alias rejection (dB) specifies the minimum attenuation level of signal components aliased
       after any resampling operation. The default is 120.

      •      normalized bandwidth —

      normalized bandwidth specifies the fraction of the new sampling rate that is not
       attenuated. The default is 0.4536.


•      resampled waveform out —

  resampled waveform out contains the resampled waveform.

•      next t0 —

  next t0 is the start time of the next resampled waveform out, if reset is FALSE.

•      used t0 —

  used t0 returns the actual start time of resampled waveform out.


                                                   © National Instruments 4343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4344 ordinal=4344 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       t0 adjusted warning —

             t0 adjusted warning returns TRUE if used t0 does not equal t0.


           If t0 is less than the actual t0 value of the input waveform, that is the time stamp of the
         first input sample, the VI coerces t0 to the first value greater than the actual t0 that
          fulfills the following equation.

      used t0 – t0 = n*dt

      where n is an integer.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Resampling a Waveform (continuous).vi

      ResampleResample NN WaveformsWaveforms (continuous,(continuous, t0t0 DBL)DBL) VIVI

      Resamples an input waveform according to the user-defined values for t0 and dt. Wire
       data to the waveform in input to determine the polymorphic instance to use or
      manually select the instance.


      Inputs/Outputs

               •       reset —

4344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4345 ordinal=4345 -->
## Functions

Functions


  reset resets the phase to the phase control value and the time stamp to zero. The default is
  FALSE.

•     waveforms in —

  waveforms in is an array of waveforms to align.

•      dt —

  dt is the user-defined sampling interval for resampled waveform out.

•       t0 —

  t0 is the user-defined start time value for resampled waveform out.

•       interpolation mode —

  interpolation mode specifies the resampling algorithm used for the resampling.

   Coerce—Specifies that each output sample is set equal to the input sample value that is closest  0    to it in time.
   Linear (default)—Specifies that each output sample value is a linear interpolation between the  1   two input samples that are closest to it in time.
   Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled  2    values.
   FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to  3   compute the resampled values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      FIR filter specifications —

  FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

      •       alias rejection (dB) —

       alias rejection (dB) specifies the minimum attenuation level of signal components aliased
       after any resampling operation. The default is 120.


                                                   © National Instruments 4345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4346 ordinal=4346 -->
## Functions

Functions


                     •      normalized bandwidth —

               normalized bandwidth specifies the fraction of the new sampling rate that is not
                 attenuated. The default is 0.4536.


               •      resampled waveforms out —

           resampled waveforms out returns an array containing the resampled waveforms.

               •      next t0's —

            next t0's is the timestamp of the next resampled waveform out, if reset is FALSE.

               •      used t0's —

           used t0's returns the array of actual time stamps for resampled waveforms out.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       t0 adjusted warnings —

             t0 adjusted warnings returns TRUE in each element of the array where the corresponding used
              t0's element does not equal t0.


           If t0 is less than the actual t0 value of the input waveform, that is the time stamp of the
         first input sample, the VI coerces t0 to the first value greater than the actual t0 that
          fulfills the following equation.

      used t0 – t0 = n*dt

      where n is an integer.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Resampling a Waveform (continuous).vi

4346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4347 ordinal=4347 -->
## Functions

Functions

ResampleResample WaveformsWaveforms (single(single shot)shot)

Resamples input waveforms or data according to the user-defined t0 and dt values.
Wire data to the waveform or data input to determine the polymorphic instance to use
or manually select the instance.


  • Resample Waveform (single shot) VI
  • Resample N Waveforms (single shot) VI
  • Resample Array of Pairs (single shot) VI
  • Resample Pair of Arrays (single shot) VI
  • Resample N Arrays of Pairs (single shot) VI
  • Resample N Pairs of Arrays (single shot) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Resampling a Waveform (single-shot).vi

ResampleResample WaveformWaveform (single(single shot)shot) VIVI

Resamples input waveforms or data according to the user-defined t0 and dt values.
Wire data to the waveform or data input to determine the polymorphic instance to use
or manually select the instance.


                                                    © National Instruments 4347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4348 ordinal=4348 -->
## Functions

Functions

      Inputs/Outputs

               •     open interval? (F) —

          open interval? defines the interval over which the VI resamples the input waveform. The default
                is FALSE, which selects a closed interval.

            For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
              interval yields resampled data over the time interval 0 ≤ t< 2dt, and a closed interval yields
           resampled data over the time interval 0 ≤ t< 3dt.

               •     waveform in —

          waveform in is a waveform to align.

               •      dt —

            dt is the user-defined sampling interval for resampled waveform out.

               •       t0 —

             t0 is the user-defined start time value for resampled waveform out.

               •       interpolation mode —

             interpolation mode specifies the resampling algorithm used for the resampling.

             Coerce—Specifies that each output sample is set equal to the input sample value that is closest           0              to it in time.
             Linear (default)—Specifies that each output sample value is a linear interpolation between the           1           two input samples that are closest to it in time.
             Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled
           2
               values.
             FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to
           3
           compute the resampled values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      FIR filter specifications —


4348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4349 ordinal=4349 -->
## Functions

Functions


    FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

         •       alias rejection (dB) —

          alias rejection (dB) specifies the minimum attenuation level of signal components aliased
          after any resampling operation. The default is 120.

         •      normalized bandwidth —

        normalized bandwidth specifies the fraction of the new sampling rate that is not
         attenuated. The default is 0.4536.


   •      resampled waveform out —

    resampled waveform out contains the resampled waveform.

   •      used t0 —

    used t0 returns the actual start time of resampled waveform out.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       t0 adjusted warning —

    t0 adjusted warning returns TRUE if used t0 does not equal t0.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Resampling a Waveform (single-shot).vi

ResampleResample NN WaveformsWaveforms (single(single shot)shot) VIVI

Resamples input waveforms or data according to the user-defined t0 and dt values.
Wire data to the waveform or data input to determine the polymorphic instance to use


                                                    © National Instruments 4349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4350 ordinal=4350 -->
## Functions

Functions

       or manually select the instance.

           Note

             Resamples waveforms in according to the user-defined t0 and dt values.


      Inputs/Outputs

               •     open interval? (F) —

          open interval? defines the interval over which the VI resamples the input waveform. The default
                is FALSE, which selects a closed interval.

            For example, assume an input waveform contains 3 data elements at t= {0, dt, 2dt}. An open
              interval yields resampled data over the time interval 0 ≤ t< 2dt, and a closed interval yields
           resampled data over the time interval 0 ≤ t< 3dt.

               •     waveforms in —

          waveforms in is an array of waveforms to align.

               •      dt —

            dt is the user-defined sampling interval for resampled waveforms out.

               •       t0 —

             t0 is the user-defined time stamp value for resampled waveforms out.

               •       interpolation mode —

             interpolation mode specifies the resampling algorithm used for the resampling.


4350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4351 ordinal=4351 -->
## Functions

Functions


   Coerce—Specifies that each output sample is set equal to the input sample value that is closest  0
    to it in time.
   Linear (default)—Specifies that each output sample value is a linear interpolation between the  1   two input samples that are closest to it in time.
   Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled  2
    values.
   FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to  3   compute the resampled values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      FIR filter specifications —

  FIR filter specifications specifies the minimum values this VI needs to specify the FIR filter.

      •       alias rejection (dB) —

       alias rejection (dB) specifies the minimum attenuation level of signal components aliased
       after any resampling operation. The default is 120.

      •      normalized bandwidth —

      normalized bandwidth specifies the fraction of the new sampling rate that is not
       attenuated. The default is 0.4536.


•      resampled waveforms out —

  resampled waveforms out returns an array containing the resampled waveforms.

•      used t0's —

  used t0's returns the array of actual time stamps for resampled waveforms out.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•       t0 adjusted warnings —


                                                   © National Instruments 4351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4352 ordinal=4352 -->
## Functions

Functions


             t0 adjusted warnings returns TRUE in each element of the array where the corresponding used
              t0's element does not equal t0.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Resampling a Waveform (single-shot).vi

      ResampleResample ArrayArray ofof PairsPairs (single(single shot)shot) VIVI

      Resamples input waveforms or data according to the user-defined t0 and dt values.
       Wire data to the waveform or data input to determine the polymorphic instance to use
       or manually select the instance.

           Note Resamples the input waveform represented by XY-data in according to
              the user-defined t0 and dt values. This VI does not assume any signal history.
            Use this VI to resample a finite-length, unevenly-sampled signal that is
              considered complete.


      Inputs/Outputs

               •      XY-data in —

            XY-data in is the array of XY pairs representing the signal to resample.

                     •      x —


4352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4353 ordinal=4353 -->
## Functions

Functions


      x is the X component of the XY pair.

      •      y —

      y is the Y component of the XY pair.


•      dt —

  dt is the user-defined sampling interval for resampled waveform out.

•       t0 —

  t0 is the user-defined time stamp value for resampled waveform out. If t0 is less than the first X
  value of XY-data in, the value is adjusted.

•       interpolation mode —

  interpolation mode specifies the resampling algorithm used for the resampling.

   Coerce—Specifies that each output sample is set equal to the input sample value that is closest  0    to it in time.
   Linear (default)—Specifies that each output sample value is a linear interpolation between the  1   two input samples that are closest to it in time.
   Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled  2    values.
   FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to  3   compute the resampled values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      resampled waveform out —

  resampled waveform out contains the resampled waveform.

•      XY-data out —

  XY-data out is the array of XY pairs containing the resampled signal.


                                                   © National Instruments 4353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4354 ordinal=4354 -->
## Functions

Functions


                     •      x —

               x is the X component of the XY pair.

                     •      y —

               y is the Y component of the XY pair.


               •      used t0 —

           used t0 returns the actual time stamp of resampled waveform out and also is the first X value of
            XY-data out.

                    If t0 is less than the first X value of XY-data in, used t0 is the lowest value greater than t0 that
                 fulfills the following equation. used t0 = t0 + n*dt where n is an integer.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       t0 adjusted warning —

             t0 adjusted warning returns TRUE if used t0 does not equal t0.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Resampling a Waveform (single-shot).vi

      ResampleResample PairPair ofof ArraysArrays (single(single shot)shot) VIVI

      Resamples input waveforms or data according to the user-defined t0 and dt values.
       Wire data to the waveform or data input to determine the polymorphic instance to use
       or manually select the instance.

           Note


4354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4355 ordinal=4355 -->
## Functions

Functions


       Resamples the input waveform represented by XY-data in according to the
        user-defined t0 and dt values. This VI does not assume any signal history. Use
         this VI to resample a finite-length, non-evenly sampled signal that is
       considered complete.


Inputs/Outputs

   •      XY-data in —

    XY-data in is a pair of X and Y arrays that represents the signal to resample.

         •       X-array —

         X-array is the array of x values.

         •       Y-array —

         Y-array is the array of y values.


   •      dt —

    dt is the user-defined sampling interval for resampled waveform out.

   •       t0 —

    t0 is the user-defined time stamp value for resampled waveform out. If t0 is less than the first X
    value of XY-data in, the value is adjusted.

   •       interpolation mode —

    interpolation mode specifies the resampling algorithm used for the resampling.


                                                    © National Instruments 4355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4356 ordinal=4356 -->
## Functions

Functions


             Coerce—Specifies that each output sample is set equal to the input sample value that is closest           0
              to it in time.
             Linear (default)—Specifies that each output sample value is a linear interpolation between the           1           two input samples that are closest to it in time.
             Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled           2
               values.
             FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to           3           compute the resampled values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      resampled waveform out —

           resampled waveform out contains the resampled waveform.

               •      XY-data out —

            XY-data out is the pair of X and Y arrays containing the resampled signal.

                     •       X-array —

                 X-array is the array of x values.

                     •       Y-array —

                 Y-array is the array of y values.


               •      used t0 —

           used t0 returns the actual time stamp of resampled waveform out and also is the first X value of
            XY-data out.

                    If t0 is less than the first X value of XY-data in, used t0 is the lowest value greater than t0 that
                 fulfills the following equation. used t0 = t0 + n*dt where n is an integer.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


4356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4357 ordinal=4357 -->
## Functions

Functions

   •       t0 adjusted warning —

    t0 adjusted warning returns TRUE if used t0 does not equal t0.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Waveform Conditioning\
   Resampling a Waveform (single-shot).vi

ResampleResample NN ArraysArrays ofof PairsPairs (single(single shot)shot) VIVI

Resamples input waveforms or data according to the user-defined t0 and dt values.
Wire data to the waveform or data input to determine the polymorphic instance to use
or manually select the instance.

      Note

       Resamples the input waveforms represented by Multiple XY-data in
       according to the user-defined t0 and dt values. This VI does not assume any
        signal history. Use this VI to resample finite-length, unevenly-sampled signals
        that are considered complete.


Inputs/Outputs

   •      Multiple XY-data in —

    Multiple XY-data in is an array of clusters containing arrays of XY pairs representing the signals to
    resample.


                                                    © National Instruments 4357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4358 ordinal=4358 -->
## Functions

Functions


                     •      XY-data in —

                XY-data in is the array of XY pairs representing the signal to resample.

                           •      x —

                   x is the X component of the XY pair.

                           •      y —

                   y is the Y component of the XY pair.


               •      dt —

            dt is the user-defined sampling interval for resampled waveforms out.

               •       t0 —

             t0 is the user-defined time stamp value for resampled waveforms out. If t0 is less than the first X
            value of Multiple XY-data in, the value is adjusted.

               •       interpolation mode —

             interpolation mode specifies the resampling algorithm used for the resampling.

             Coerce—Specifies that each output sample is set equal to the input sample value that is closest           0
              to it in time.
             Linear (default)—Specifies that each output sample value is a linear interpolation between the           1
           two input samples that are closest to it in time.
             Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled
           2
               values.
             FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to
           3
           compute the resampled values.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      resampled waveforms out —


4358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4359 ordinal=4359 -->
## Functions

Functions


    resampled waveforms out returns an array containing the resampled waveforms.

   •      Multiple XY-data out —

    Multiple XY-data out is the array of arrays of XY pairs containing the resampled signals.

         •      XY-data out —

        XY-data out is the array of XY pairs containing the resampled signal.

                •      x —

            x is the X component of the XY pair.

                •      y —

            y is the Y component of the XY pair.


   •      used t0's —

    used t0's returns the array of actual time stamps for resampled waveforms out. The time
    stamps are also the first X values in Multiple XY-data out.

    For each element of Multiple XY-data in, if t0 is less than the first X value (x0) of that element, the
    corresponding element value of used t0's is the lowest value greater than x0 that also fulfills the
    following equation. used t0 = t0 + n*dt where n is an integer.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       t0 adjusted warnings —

    t0 adjusted warnings returns TRUE in each element of the array where the corresponding used
     t0's element does not equal t0.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 4359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4360 ordinal=4360 -->
## Functions

Functions

            • labview\examples\Signal Processing\Waveform Conditioning\
        Resampling a Waveform (single-shot).vi

      ResampleResample NN PairsPairs ofof ArraysArrays (single(single shot)shot) VIVI

      Resamples input waveforms or data according to the user-defined t0 and dt values.
       Wire data to the waveform or data input to determine the polymorphic instance to use
       or manually select the instance.

           Note

             Resamples the input waveforms represented by Multiple XY-data in
              according to the user-defined t0 and dt values. This VI does not assume any
                signal history. Use this VI to resample finite-length, non-evenly sampled
                signals that are considered complete.


      Inputs/Outputs

               •      Multiple XY-data in —

            Multiple XY-data in is the array of pairs of X and Y arrays representing the waveforms to
            resample.

                     •       X-array —

                 X-array is the array of x values.

                     •       Y-array —

                 Y-array is the array of y values.


               •      dt —

4360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4361 ordinal=4361 -->
## Functions

Functions


  dt is the user-defined sampling interval for resampled waveforms out.

•       t0 —

  t0 is the user-defined time stamp value for resampled waveforms out. If t0 is less than the first X
  value of Multiple XY-data in, the value is adjusted.

•       interpolation mode —

  interpolation mode specifies the resampling algorithm used for the resampling.

   Coerce—Specifies that each output sample is set equal to the input sample value that is closest  0    to it in time.
   Linear (default)—Specifies that each output sample value is a linear interpolation between the  1
   two input samples that are closest to it in time.
   Spline—Specifies that this VI uses the spline interpolation algorithm to compute the resampled  2
    values.
   FIR filter—Specifies that this VI uses a finite impulse response (FIR) filtering algorithm to  3
   compute the resampled values.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      resampled waveforms out —

  resampled waveforms out returns an array containing the resampled waveforms.

•      Multiple XY-data out —

  Multiple XY-data out is the array of pairs of X and Y arrays containing the resampled waveforms.

      •       X-array —

       X-array is the array of x values.

      •       Y-array —

       Y-array is the array of y values.


•      used t0's —

                                                   © National Instruments 4361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4362 ordinal=4362 -->
## Functions

Functions


           used t0's returns the array of actual time stamps for resampled waveforms out.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       t0 adjusted warnings —

             t0 adjusted warnings returns TRUE in each element of the array where the corresponding used
              t0's element does not equal t0.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Waveform Conditioning\
        Resampling a Waveform (single-shot).vi

       FilterFilter

       Processes signals through filters and windows.


      Dialog Box Options

        Option        Description

                          Specifies the following types of filters to use: lowpass, highpass, bandpass,
          Filtering Type
                       bandstop, or smoothing. The default is Lowpass.

                       Contains the following options:
          Filter
         Specifications     •  Cutoff Frequency (Hz)—


4362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4363 ordinal=4363 -->
## Functions

Functions


Option        Description

                     Specifies the cutoff frequency of the filter. This option is available only when
                 you select Lowpass or Highpass from the Filtering Type pull-down menu. The
                    default is 100.

                         • Low cutoff frequency (Hz)—

                     Specifies the low cutoff frequency of the filter. Low cutoff frequency (Hz) must
                be less than High cutoff frequency (Hz) and observe the Nyquist criterion. The
                    default is 100. This option is available only when you select Bandpass or
                 Bandstop from the Filtering Type pull-down menu.

                         • High cutoff frequency (Hz)—

                     Specifies the high cutoff frequency of the filter. High cutoff frequency (Hz)
                must be greater than Low cutoff frequency (Hz) and observe the Nyquist
                       criterion. The default is 400. This option is available only when you select
                 Bandpass or Bandstop from the Filtering Type pull-down menu.

                         •  Finite impulse response (FIR) filter—

                   Creates an FIR filter, which depends only on the current and past inputs.

                 Because the filter does not depend on past outputs, the impulse response
                  decays to zero in a finite amount of time. Because FIR filters return a linear
                 phase response, use FIR filters for applications that require linear phase
                   responses.

                         • Taps—

                     Specifies the total number of FIR coefficients, which must be greater than zero.
                The default is 29. This option is available only when you select the Finite
                  impulse response (FIR) filter option.

                    Increasing the value of Taps causes the transition between the passband and
                   the stopband to become steeper. However, as the value of Taps increases, the
                   processing speed becomes slower.

                         •  Infinite impulse response (IIR) filter—

                   Creates an IIR filter that is a digital filter with impulse responses that can
                     theoretically be infinite in length or duration.


                                                    © National Instruments 4363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4364 ordinal=4364 -->
## Functions

Functions


        Option        Description

                                      • Topology—

                          Determines the design type of the filter. You can create either a Butterworth,
                          Chebyshev, Inverse Chebyshev, Elliptic, or Bessel filter design. This option is
                              available only when you select the Infinite impulse response (IIR) filter
                             option. The default is Butterworth.

                                      • Order—

                          Order of the IIR filter, which must be greater than zero. This option is available
                            only when you select the Infinite impulse response (IIR) filter option. The
                              default is 3.

                             Increasing the value of Order causes the transition between the passband and
                           the stopband to become steeper. However, as the value of Order increases, the
                            processing speed becomes slower, and the number of distorted points at the
                                 start of the signal increases.

                                      • Moving average—

                               Yields forward-only (FIR) coefficients. This option is available only when you
                               select Smoothing from the Filtering Type pull-down menu.

                                      • Rectangular—

                              Specifies that all samples in the moving-average window are weighted equally
                                in computing each smoothed output sample. This option is available only
                      when you select Smoothing from the Filtering Type pull-down menu and the
                        Moving average option.

                                      • Triangular—

                              Specifies that the moving weighting window applied to the samples is
                              triangular with the peak centered in the middle of the window, ramping down
                            symmetrically on both sides of the center sample. This option is available only
                      when you select Smoothing from the Filtering Type pull-down menu and the
                        Moving average option.

                                      • Half-width of moving average—

                              Specifies the half-width of the moving-average window in samples. The


4364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4365 ordinal=4365 -->
## Functions

Functions


Option        Description

                    default is 1. For a half-width of moving average of M, the full width of the
                  moving-average window is N = 1 + 2M samples. Therefore, the full width N is
                  always an odd number of samples. This option is available only when you
                     select Smoothing from the Filtering Type pull-down menu and the Moving
                  average option.

                         • Exponential—

                     Yields first-order IIR coefficients. This option is available only when you select
                Smoothing from the Filtering Type pull-down menu.

                         • Time constant of exponential average—

                     Specifies the time constant of the exponential-weighting filter in seconds. The
                    default is 0.001. This option is available only when you select Smoothing from
                   the Filtering Type pull-down menu and the Exponential option.


               Displays the input signal.

Input Signal     If you wire data to the Express VI and run it, Input Signal displays real data. If you
                close and reopen the Express VI, Input Signal displays sample data until you run
               the Express VI again.


               Displays a preview of the measurement. The Result Preview plot indicates the
               value of the selected measurement with a dotted line.
Result                        If you wire data to the Express VI and run the VI, Result Preview displays real data.
Preview                        If you close and reopen the Express VI, Result Preview displays sample data until
             you run the VI again. If the cutoff frequency values are invalid, Result Preview does
              not display valid data.

               Contains the following options:

                 Note Changing the options in the View Mode section does not impact
View Mode             the behavior of the Filter Express VI. Use the View Mode options to
                           visualize what the filter does to the signal. LabVIEW does not save these
                        options when you close the configuration dialog box.


                                                    © National Instruments 4365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4366 ordinal=4366 -->
## Functions

Functions


        Option        Description

                                      • Signals—

                             Displays the filter response as real signals.

                                      •  Transfer function—

                             Displays the filter response as a transfer function.

                                      • Show as spectrum—

                              Specifies whether to display the real signals of the filter response as a
                           frequency spectrum or to leave the display as a time-based display. The
                           frequency display is useful for viewing how the filter affects the various
                           frequency components of the signal. The default is to display the filter
                          response as a time-based display. This option is available only when you select
                           the Signals option.

                       Contains the following options:

                                      • Magnitude in dB—

                            Presents the magnitude response of the filter in decibels.         Scale Mode
                                      • Frequency in log—

                            Presents the frequency response of the filter on a logarithmic scale.


        Magnitude     Displays the magnitude response of the filter. This display is available only when
        Response     you set View Mode to Transfer function.


        Phase         Displays the phase response of the filter. This display is available only when you set
        Response     View Mode to Transfer function.


      Inputs/Outputs

               •      Signal —


4366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4367 ordinal=4367 -->
## Functions

Functions


     Specifies the input signal. The signal can be a waveform, a real array, or a complex array.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •     Upper Cut-Off —

     Specifies the high cutoff frequency of the filter. Upper Cut-Off must be greater than Lower Cut-
    Off and observe the Nyquist criterion. The default is 400.

   •     Lower Cut-Off —

     Specifies the low cutoff frequency of the filter. Lower Cut-Off must be less than Upper Cut-Off
    and observe the Nyquist criterion. The default is 100.

   •       Filtered Signal —

    Returns the filtered signal.

   •       error out —

    Contains error information. This output provides standard error out functionality.


      Note Use the Filters PtByPt VIs to implement continuous, point-by-point
          filtering.

Components

Yields forward-only (FIR) coefficients. This option is available only when you select
Smoothing from the Filtering Type pull-down menu.

Yields first-order IIR coefficients. This option is available only when you select
Smoothing from the Filtering Type pull-down menu.

Specifies that all samples in the moving-average window are weighted equally in
computing each smoothed output sample. This option is available only when you
select Smoothing from the Filtering Type pull-down menu and the Moving average
option.

                                                    © National Instruments 4367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4368 ordinal=4368 -->
## Functions

Functions

       Specifies that the moving weighting window applied to the samples is triangular with
       the peak centered in the middle of the window, ramping down symmetrically on both
       sides of the center sample. This option is available only when you select Smoothing
      from the Filtering Type pull-down menu and the Moving average option.

       Specifies the low cutoff frequency of the filter. Low cutoff frequency (Hz) must be less
      than High cutoff frequency (Hz) and observe the Nyquist criterion. The default is 100.
       This option is available only when you select Bandpass or Bandstop from the Filtering
      Type pull-down menu.

       Displays the input signal.

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.

       Specifies the following types of filters to use: lowpass, highpass, bandpass, bandstop,
       or smoothing. The default is Lowpass.

       Specifies the time constant of the exponential-weighting filter in seconds. The default
         is 0.001. This option is available only when you select Smoothing from the Filtering
      Type pull-down menu and the Exponential option.

       Specifies the half-width of the moving-average window in samples. The default is 1.
       For a half-width of moving average of M, the full width of the moving-average window
         is N = 1 + 2M samples. Therefore, the full width N is always an odd number of samples.
       This option is available only when you select Smoothing from the Filtering Type pull-
     down menu and the Moving average option.

       Specifies the half-width of the moving-average window in samples. The default is 1.
       For a half-width of moving average of M, the full width of the moving-average window
         is N = 1 + 2M samples. Therefore, the full width N is always an odd number of samples.
       This option is available only when you select Smoothing from the Filtering Type pull-
     down menu and the Moving average option.

       Specifies the time constant of the exponential-weighting filter in seconds. The default
         is 0.001. This option is available only when you select Smoothing from the Filtering
      Type pull-down menu and the Exponential option.


4368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4369 ordinal=4369 -->
## Functions

Functions

Presents the frequency response of the filter on a logarithmic scale.

Presents the magnitude response of the filter in decibels.

Displays the filter response as real signals.

Displays the filter response as a transfer function.

Specifies whether to display the real signals of the filter response as a frequency
spectrum or to leave the display as a time-based display. The frequency display is
useful for viewing how the filter affects the various frequency components of the
signal. The default is to display the filter response as a time-based display. This option
is available only when you select the Signals option.

Creates an IIR filter that is a digital filter with impulse responses that can theoretically
be infinite in length or duration.

Creates an FIR filter, which depends only on the current and past inputs.

Order of the IIR filter, which must be greater than zero. This option is available only
when you select the Infinite impulse response (IIR) filter option. The default is 3.

Determines the design type of the filter. You can create either a Butterworth,
Chebyshev, Inverse Chebyshev, Elliptic, or Bessel filter design. This option is available
only when you select the Infinite impulse response (IIR) filter option. The default is
Butterworth.

Specifies the high cutoff frequency of the filter. High cutoff frequency (Hz) must be
greater than Low cutoff frequency (Hz) and observe the Nyquist criterion. The default
is 400. This option is available only when you select Bandpass or Bandstop from the
Filtering Type pull-down menu.

Specifies the cutoff frequency of the filter. This option is available only when you select
Lowpass or Highpass from the Filtering Type pull-down menu. The default is 100.

Specifies the total number of FIR coefficients, which must be greater than zero. The
default is 29. This option is available only when you select the Finite impulse response
(FIR) filter option.


                                                    © National Instruments 4369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4370 ordinal=4370 -->
## Functions

Functions

       Displays the magnitude response of the filter. This display is available only when you
       set View Mode to Transfer function.

       Displays the phase response of the filter. This display is available only when you set
      View Mode to Transfer function.

      AlignAlign andand ResampleResample

      Performs an alignment of signals by changing the start time or performs a resampling
       of signals by changing the time delta. This Express VI returns the adjusted signals.


      Dialog Box Options

        Option        Description

                      Contains the following options:

                                     •  Single segment—

         Acquisition        Aligns and/or resamples each iteration separately.
        Type
                                     • Continuous—

                             Aligns and/or resamples all iterations as one continuous segment.


         Align          Aligns the signals to have the same start time.

                      Contains the following options:

        Alignment         • Global—
         Interval
                             Aligns the start and end times of signals by adding zero values to the beginning


4370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4371 ordinal=4371 -->
## Functions

Functions


Option        Description

                    of the signal that starts last and to the end of the signal that ends first.

                        • Common—

                    Aligns the start and end times of signals by using the start time of the signal
                   that starts last and the end time of the signal that ends first.


Resample    Resamples the signals to have the same sampling interval.

              Contains the following options:

                        • Lowest dt—

                Resamples all the signals to have the same sampling interval as the signal with
                  the smallest sampling interval.

                        •  Specific dt—

Resampling      Resamples all the signals to have a user-defined sampling interval.
Interval
        ◦ dt—

                    Sampling interval you define. The default is 1.

                        • Reference signal—

                Resamples all the signals to have the same sampling interval as a reference
                     signal.


           When resampling, you might need to add points to the signal. Interpolation Mode
               controls how LabVIEW calculates the amplitude of the new points. Interpolation
           Mode contains the following options:
Interpolation
Mode                • Linear—

                  Returns an output sample value equal to a linear interpolation between the two
                  input samples that are closest to the output sample value in time.


                                                    © National Instruments 4371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4372 ordinal=4372 -->
## Functions

Functions


        Option        Description

                                     • Coerce—

                          Returns an output sample value equal to the input sample value that is closest
                            to the output sample value in time.

                                     • Spline—

                         Uses the spline interpolation algorithm to compute the resampled values.

                                     • FIR filter—

                         Uses an FIR filter to compute the resampled values.

                      Contains the following options:

                                     •  Alias rejection (dB)—

                             Specifies the minimum attenuation level of signal components aliased after any
                          resampling operation. The default is 120. This option is available only when you        FIR Filter
                              select FIR filter.        Parameters
                                     • Normalized bandwidth—

                             Specifies the fraction of the new sampling rate that is not attenuated. The
                             default is 0.4536. This option is available only when you select FIR filter.


                       Defines whether an input signal is an open or closed interval. The default is TRUE,
       Open        which selects an open interval. For example, assume an input signal has t0 = 0, dt =
         interval        1, and Y = {0, 1, 2}. An open interval returns a final time value of 2. A closed interval
                        returns a final time value of 3.


                        Displays sample input signals you can use as a reference to determine how the
                        configuration options you select affect the actual input signals.
       Sample
        Input Data       If you wire data to the Express VI and run it, Sample Input Data displays real data. If
                    you close and reopen the Express VI, Sample Input Data displays sample data until
                    you run the VI again.


4372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4373 ordinal=4373 -->
## Functions

Functions


 Option        Description

               Displays a preview of the measurement. The Result Preview plot indicates the value
                of the selected measurement with a dotted line.
 Result                        If you wire data to the Express VI and run the VI, Result Preview displays real data. If
 Preview             you close and reopen the Express VI, Result Preview displays sample data until you
              run the VI again. If the cutoff frequency values are invalid, Result Preview does not
                display valid data.


Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •      Signals 2 —

    Contains the input signal(s).

   •      Signals —

    Contains the input signal or signals.

   •      Reference Signal —

    Contains a reference signal whose sampling interval is used as the rate at which this Express VI
    resamples the input signals. If you wire a value to this input, the wired value overrides the value
    you set in the configuration dialog box.

   •      dt —

     Specifies a sampling interval you define. If you wire a value to this input, the wired value
    overrides the value you set in the configuration dialog box.

   •     Resampled Signals —

    Returns the resampled signals.


                                                    © National Instruments 4373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4374 ordinal=4374 -->
## Functions

Functions

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •     Resampled Signals 2 —

            Returns the resampled signals.


     Components

      Resamples the signals to have the same sampling interval.

      Uses an FIR filter to compute the resampled values.

      Uses the spline interpolation algorithm to compute the resampled values.

       Returns an output sample value equal to a linear interpolation between the two input
      samples that are closest to the output sample value in time.

       Returns an output sample value equal to the input sample value that is closest to the
      output sample value in time.

       Aligns the signals to have the same start time.

       Aligns the start and end times of signals by adding zero values to the beginning of the
       signal that starts last and to the end of the signal that ends first.

       Aligns and/or resamples all iterations as one continuous segment.

       Aligns and/or resamples each iteration separately.

      Resamples all the signals to have the same sampling interval as a reference signal.

      Resamples all the signals to have a user-defined sampling interval.

      Resamples all the signals to have the same sampling interval as the signal with the
       smallest sampling interval.

       Defines whether an input signal is an open or closed interval. The default is TRUE,

4374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4375 ordinal=4375 -->
## Functions

Functions

which selects an open interval. For example, assume an input signal has t0 = 0, dt = 1,
and Y = {0, 1, 2}. An open interval returns a final time value of 2. A closed interval
returns a final time value of 3.

Aligns the start and end times of signals by using the start time of the signal that starts
last and the end time of the signal that ends first.

Sampling interval you define. The default is 1.

Specifies the fraction of the new sampling rate that is not attenuated. The default is
0.4536. This option is available only when you select FIR filter.

Specifies the minimum attenuation level of signal components aliased after any
resampling operation. The default is 120. This option is available only when you select
FIR filter.

Displays sample input signals you can use as a reference to determine how the
configuration options you select affect the actual input signals.

When resampling, you might need to add points to the signal. Interpolation Mode
controls how LabVIEW calculates the amplitude of the new points. Interpolation Mode
contains the following options:

Displays a preview of the measurement. The Result Preview plot indicates the value of
the selected measurement with a dotted line.

TriggerTrigger andand GateGate

Uses triggering to extract a segment out of a signal. The trigger conditions can be
based on a start or stop trigger threshold or can be static. When a trigger condition is
static, the trigger occurs immediately and this Express VI returns a predefined number
of samples.


                                                    © National Instruments 4375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4376 ordinal=4376 -->
## Functions

Functions

      Dialog Box Options

        Option   Description

                  Contains the following options:

                              • Threshold—

                     Uses a threshold to indicate when to start triggering.

          ◦  Start sense—

                             Specifies on what edge of the signal to start taking samples. The options are
                            Rising edge, Rising or Falling edge, or Falling edge. This option is available only
                     when you select Threshold.

          ◦  Start level—         Start
         Trigger                         Amplitude that the signal must cross in the Start sense direction before the
                           Express VI starts taking samples. The default is 0. This option is available only
                     when you select Threshold.

          ◦ Pre samples—

                             Specifies the number of samples that occur before the start trigger to return.
                       The default is 0. This option is available only when you select Threshold.

                              • Immediate—

                      Begins the triggering immediately. The start of the signal is the start trigger.

                  Contains the following options:

                              • Number of samples—

                    Ends the triggering when the Express VI collects Samples.
        Stop          ◦ Samples—         Trigger
                             Specifies the number of samples to collect before stopping the trigger. The
                             default is 1000.

                              • Threshold—


4376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4377 ordinal=4377 -->
## Functions

Functions


Option   Description

             Uses a threshold to indicate when to start triggering.

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

               Specifies the channel to use if the dynamic data type input contains multiple
                signals. The default is 0.

                 • Reset after each trigger found—

              Resets the trigger conditions after finding each trigger. When you select this option,
              the Trigger and Gate Express VI does not buffer data with each iteration of a loop.
               Select this checkbox when you have a new data set for each iteration and you want
               to find data related only to the first trigger point. Deselect this checkbox when you
            want to pass only one set of data into a loop and then call the Trigger and GateGeneral
              Express VI in a loop to get all the triggers in the data.

                 Note When you do not select this option, the Trigger and Gate Express VI
                        buffers data. In this case, if the Trigger and Gate Express VI is called in a
                        loop, it can start a backlog of data if there is new data for each loop
                      (because one set of data can contain several trigger points). Because
                       there is no reset, it buffers all the data from each loop so that it can find
                              all the triggers, but all the triggers might not be found.

                 • Remain triggered after trigger found—

            Remains triggered after finding a trigger. This option is available only when you


                                                    © National Instruments 4377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4378 ordinal=4378 -->
## Functions

Functions


        Option   Description

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

                         Specifies that the Express VI returns the portion of the signal that matches the
        Output        trigger criteria.
       segment
          size            • Number of output samples—

                         Specifies the number of samples to include in each output segment. This option is
                        available only if the Automatic number of samples checkbox does not contain a
                     checkmark.


                   Displays the input signal.

                              If you wire data to the Express VI and run it, Input Signal displays real data. If you close
                and reopen the Express VI, Input Signal displays sample data until you run the Express VI        Input
                    again.         Signal
                              • Number of points in the data—

                         Specifies the number of points in the data. The default is 4400.


         Results   Displays a preview of the measurement. The Results Preview plot indicates the value of
        Preview  the selected measurement with a dotted line.


4378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4379 ordinal=4379 -->
## Functions

Functions


 Option   Description

                 If you wire data to the Express VI and run the VI, Results Preview displays real data. If you
           close and reopen the Express VI, Results Preview displays sample data until you run the
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


                                                    © National Instruments 4379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4380 ordinal=4380 -->
## Functions

Functions


           output contains the most recent segment that meet the requirements of the trigger.

               •      Triggered Signals —

            Returns the resulting segment between Start Trigger and Stop Trigger. If no data meets the
            requirements of the trigger, this output returns an empty signal.

    WaveformWaveform MeasurementsMeasurements

      Use the Waveform Measurements VIs to perform common time and frequency domain
      measurements, such as DC, RMS, Tone Frequency/Amplitude/Phase, Harmonic
        Distortion, SINAD, and Averaged FFT Measurements.

           Note The Waveform Measurements VIs presently do not accept waveforms
               that contain complex data.

      The VIs on this palette can return waveform error codes. In addition, the VIs on this
       palette return an error if an input waveform has a dt less than or equal to zero.


         Palette Object  Description

         Basic           Calculates the DC and RMS values of an input waveform or array of waveforms.
        Averaged DC-   This VI is similar to the Averaged DC-RMS VI, but this VI returns only one DC value
      RMS         and one RMS value per input waveform.


                         Calculates the DC and RMS values of an input waveform or array of waveforms.
        Averaged DC-
                         This VI is similar to the Basic Averaged DC-RMS VI, but this VI gives more precise
      RMS
                         control over the individual DC and RMS calculations.


         Cycle Average
                       Returns the average and RMS levels of a selected cycle of a periodic waveform or
       and RMS


4380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4381 ordinal=4381 -->
## Functions

Functions


Palette Object  Description

             an array of periodic waveforms. Wire data to the signal in input to determine the
              polymorphic instance to use or manually select the instance.


Waveform     Use the Waveform Monitoring VIs to analyze the waveforms for trigger points, to
Monitoring     search for peaks, and to perform limit mask testing.


               Accepts an input signal of a single waveform or an array of waveforms and
              measures the transition duration (rise or fall time), slew rate, undershoot, andTransition               overshoot of a selected positive or negative transition in each waveform. Wire dataMeasurements                to the signal in input to determine the polymorphic instance to use or manually
                 select the instance.


               Accepts a periodic waveform or an array of periodic waveforms and returns the
Pulse          period, pulse duration (pulse width), duty cycle (duty factor), and pulse center of
Measurements a selected pulse and period. Wire data to the signal in input to determine the
              polymorphic instance to use or manually select the instance.


               Returns the amplitude, high state level, and low state level of a waveform or anAmplitude
                array of waveforms. Wire data to the signal in input to determine the polymorphicand Levels                instance to use or manually select the instance.


              Takes a signal in, finds the single tone with the highest amplitude or searches a
Extract Single   specified frequency range, and returns the single tone frequency, amplitude, and
Tone          phase. The input signal can be real or complex and single-channel or multichannel.
Information    Wire data to the time signal in input to determine the polymorphic instance to use
               or manually select the instance.


Extract         Returns the frequency, amplitude, and phase for each signal tone whose
Multiple Tone  amplitude exceeds a specified threshold. Wire data to the time signal in input to
Information    determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4382 ordinal=4382 -->
## Functions

Functions


         Palette Object  Description

                       Takes a signal in and performs a full harmonic analysis, including measuring the
        Harmonic     fundamental frequency tone and harmonics, and returning the fundamental
         Distortion      frequency, all harmonic amplitude levels, and the total harmonic distortion (THD).
         Analyzer       Wire data to the signal in input to determine the polymorphic instance to use or
                      manually select the instance.


                       Takes a signal in and performs a full Signal in Noise and Distortion (SINAD)
        SINAD           analysis, including measuring the fundamental frequency tone and returning the
         Analyzer       fundamental frequency and SINAD level in dB. Wire data to the signal in input to
                      determine the polymorphic instance to use or manually select the instance.


        FFT Power     Computes the averaged auto power spectrum of time signal. Wire data to the time
        Spectrum and  signal input to determine the polymorphic instance to use or manually select the
       PSD            instance.


                    Computes the averaged FFT spectrum of time signal. This VI returns the FFT results        FFT Spectrum                       as magnitude and phase. Wire data to the time signal input to determine the        (Mag-Phase)
                      polymorphic instance to use or manually select the instance.


                    Computes the averaged FFT spectrum of time signal. This VI returns the FFT results        FFT Spectrum
                       as real and imaginary parts. Wire data to the time signal input to determine the         (Real-Im)                      polymorphic instance to use or manually select the instance.

        Frequency
        Response     Computes the frequency response and the coherence based on the input signals.
         Function       Results are returned as magnitude, phase, and coherence.
        (Mag-Phase)

        Frequency
        Response     Computes the frequency response and the coherence based on the input signals.
         Function       Results are returned as real part, imaginary part, and coherence.
         (Real-Im)

         Cross
        Spectrum     Computes the averaged cross power spectrum of the input signals. Results are
        (Mag-Phase)

4382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4383 ordinal=4383 -->
## Functions

Functions


 Palette Object  Description

                returned as magnitude and phase.


 Cross             Computes the averaged cross power spectrum of the input signals. Results are Spectrum                returned as real and imaginary parts. (Real-Im)


 Spectral       Performs FFT-based spectral measurements, such as the averaged magnitude
 Measurements spectrum, power spectrum, and phase spectrum on a signal.


 Dual Channel   Measures the frequency response of the input signals and the coherence based on
 Spectral       the current and previous input signals. This Express VI returns results such as
 Measurement  Magnitude, Phase, Coherence, Real, and Imaginary.


 Distortion      Performs distortion measurements on a signal, such as tone analysis, total
 Measurements harmonic distortion (THD), and signal in noise and distortion (SINAD).


                Finds the single tone with the highest amplitude or searches a specified frequency
 Tone               range to find the single tone with the highest amplitude. You also can find the Measurements               frequency and phase for a single tone.


 Timing and               Performs timing and transition measurements, such as frequency, period, or duty Transition
                  cycle, on a signal, usually a pulse.
 Measurements

 Amplitude
 and Level      Performs voltage measurements on a signal.
 Measurements

SignalSignal GenerationGeneration

Use the Signal Generation VIs to generate one-dimensional arrays with specific
waveform patterns. The Signal Generation VIs generate digital patterns and
waveforms.

                                                    © National Instruments 4383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4384 ordinal=4384 -->
## Functions

Functions

      The VIs on this palette can return signal processing error codes.


         Palette                       Description        Object

         Signal
        Generator by  Generates a signal with a shape given by the signal type.
         Duration

        Tones and                      Generates an array composed of a sum of sine tones, noise, and DC offset.        Noise

        Gaussian
        Modulated    Generates an array that contains a Gaussian-modulated sinusoidal pattern.
         Sine Pattern

        Gaussian
                      Generates an array that contains a Gaussian monopulse.        Monopulse


         Sinc Pattern   Generates an array containing a sinc pattern.


         Periodic Sinc                      Generates an array containing a periodic sinc pattern.
         Pattern


         Sine Pattern   Generates an array containing a sinusoidal pattern.


         Triangle
                      Generates an array that contains a triangle pattern.
         Pattern


         Pulse Pattern  Generates an array containing a pulse pattern.


                      Generates an array containing a ramp pattern. You must manually select the
      Ramp Pattern
                      polymorphic instance you want to use.


4384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4385 ordinal=4385 -->
## Functions

Functions


Palette               Description
Object

Chirp Pattern  Generates an array containing a chirp pattern.


Sine Wave     Generates an array containing a sine wave.


Triangle Wave  Generates an array containing a triangle wave.


Square Wave  Generates an array containing a square wave.


Sawtooth              Generates an array containing a sawtooth wave.Wave

Arbitrary              Generates an array containing an arbitrary wave.
Wave


Uniform       Generates a uniformly distributed, pseudorandom pattern whose values are in the
White Noise   range [–a:a], where ais the absolute value of amplitude.


Gaussian      Generates a Gaussian-distributed, pseudorandom pattern whose statistical profile
White Noise     is (mu, sigma) = (0, s), where sis standard deviation.

Periodic
Random      Generates an array containing periodic random noise (PRN).
Noise

              Generates a maximum length sequence of ones and zeros using a modulo-2
Binary MLS
                primitive polynomial of order polynomial order.


Impulse
              Generates an array containing an impulse pattern.
Pattern


                                                    © National Instruments 4385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4386 ordinal=4386 -->
## Functions

Functions


         Palette                       Description
        Object

                      Generates a pseudorandom pattern of values that are the waiting times to the order      Gamma Noise                   number event of a unit mean Poisson process.


                      Generates a pseudorandom sequence of values that are the number of discrete
        Poisson Noise  events that occur in a given interval, specified by mean, of a unit rate Poisson
                        process.


                      Generates a binomially-distributed, pseudorandom pattern whose values are the        Binomial                   number of occurrences of an event, given the probability of that event occurring        Noise
                    and the number of trials.


         Bernoulli      Generates a pseudorandom pattern of ones and zeros. LabVIEW computes each
        Noise         element of bernoulli noise as if flipping a coin weighted by ones probability.


                      Generates an array that concatenates a series of pulses according to the Prototype
         Pulse Train     Pulse. This VI constructs the Pulse Train output by the specified interpolation
                    method.


        Quasi         Generates quasi-random Halton or Richtmeyer sequences, which are low-
       Random       discrepancy number sequences.


      SignalSignal GeneratorGenerator byby DurationDuration

       Generates a signal with a shape given by the signal type.


4386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4387 ordinal=4387 -->
## Functions

Functions


Inputs/Outputs

   •       reset phase —

    reset phase determines the initial phase of output signal. The default is TRUE.

       If reset phase is TRUE, the initial phase is set to phase in. If reset phase is FALSE, the initial
    phase is set to the value of phase out when this VI was last executed.

   •      duration —

    duration is the time, in seconds, of the duration of the generated output signal. The default is
     1.0.

   •       signal type —

    signal type is the type of signal to generate.

           Sine    0            (default)
    1     Cosine
    2      Triangle
    3     Square
    4     Sawtooth
    5      Increasing ramp
    6     Decreasing ramp

   •      # of samples —

    # of samples is the number of samples of the output signal. The default is 100.

   •      frequency —

    frequency is the frequency of the output signal in Hz. The default is 10.


                                                    © National Instruments 4387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4388 ordinal=4388 -->
## Functions

Functions


          The unit of frequency is Hz, or cycles/sec, and so represents the number of cycles of one period
             of the waveform type that is generated in 1 second of the output signal.

               •      amplitude —

           amplitude is the amplitude of the output signal. The default is 1.0.

               •      dc offset —

           dc offset is the constant offset, or dc value, of the generated output signal. The default is 0.

               •      phase in —

           phase in is the initial phase, in degrees, of output signal when reset phase is TRUE. The default
                is 0.

               •      square wave duty cycle (%) —

           square wave duty cycle is the percentage of time a square wave remains high versus low over
          one period. The VI uses this parameter only if the signal type is a square wave. The default is 50.

               •       signal —

             signal is the generated array of signal samples.

               •     sample rate —

           sample rate is the output signal sample rate and is equal to # of samples/duration.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.

               •      phase out —

           phase out is the phase, in degrees, of the next sample of output signal.


      The frequency of the signal is given in Hz (cycles/sec) and the duration is given in
       seconds.

      # of samples and duration completely define a sample rate, which must be greater


4388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4389 ordinal=4389 -->
## Functions

Functions

than 2 times the appropriate signal frequency to meet the Nyquist criterion

  • sample rate > 2*frequency
  • (samples/duration) > 2*frequency

If the Nyquist criterion is not met, you must adjust # of samples, duration, or
frequency in one of the following ways:

  • Increasing # of samples
  • Decreasing duration
  • Decreasing frequency

The Signal Generator by Duration VI is reentrant, so you can use it to simulate a
continuous acquisition from a function generator. If the input control reset phase is
FALSE, subsequent calls to the Signal Generator by Duration VI produce an array
containing the next nsamples of the selected waveform.

When reset phase is FALSE, the Signal Generator by Duration VI uses the phase out
value as its new phase in the next time the VI executes.

TonesTones andand NoiseNoise

Generates an array composed of a sum of sine tones, noise, and DC offset.


Inputs/Outputs

   •       reset signal —

    reset signal, if TRUE, resets the phase of each tone to the phase value from the tones array, the
    seed to the seed control value, and the time stamp to zero. The default is FALSE.

   •      samples —


                                                    © National Instruments 4389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4390 ordinal=4390 -->
## Functions

Functions


           samples specifies the number of samples to generate in the output array tones and noise. The
             default is 1000.

               •      tones —

           tones contains the parameters for each sine tone.

                     •      frequency —

               frequency specifies the frequency of the sine tone in hertz.

                     •      amplitude —

               amplitude specifies the amplitude of the sine tone.

                     •      phase —

              phase specifies the initial phase of the sine tone in degrees. The default is 0.


               •      noise (rms) —

            noise specifies the rms level of the additive Gaussian noise. The default is 0.0.

               •       offset —

             offset is the DC offset of the signal. The default is 0.0.

               •      Fs —

            Fs is the sampling rate in samples per second. The default is 1000.

               •      seed —

            seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

           LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
            For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
            noise generator, and the noise generator resumes producing noise samples as a continuation of
            the previous noise sequence.

               •      tones and noise —


4390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4391 ordinal=4391 -->
## Functions

Functions


    tones and noise is the generated output array.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.

GaussianGaussian ModulatedModulated SineSine PatternPattern

Generates an array that contains a Gaussian-modulated sinusoidal pattern.


Inputs/Outputs

   •      attenuation (dB) —

    attenuation (dB) is related to the drop in power on either side of the center frequency, which
    must be greater than zero. The default is 6 dB.

   •      center frequency (Hz) —

    center frequency (Hz) is the center frequency, or frequency of the carrier, in Hertz. The default is
     1.

   •      samples —

    samples is the number of samples of the Gauss-Mod Sine Pattern. If samples is less than 1, the
     VI sets Gauss-Mod Sine Pattern to an empty array and returns an error. The default is 128.

   •      amplitude —

    amplitude is the amplitude of the Gauss-Mod Sine Pattern. The default is 1.

   •      delay (s) —


                                                    © National Instruments 4391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4392 ordinal=4392 -->
## Functions

Functions


            delay (s) shifts the peak of the Gauss-Mod Sine Pattern. The default is 0.

               •       delta t (s) —

            delta t (s) is the sampling interval. delta t (s) must be greater than zero. If delta t (s) is less than
            or equal to zero, the VI sets Gauss-Mod Sine Pattern to an empty array and returns an error. The
             default is 0.1.

               •      normalized bandwidth —

           normalized bandwidth is the value multiplied by center frequency to normalize the bandwidth
             at attenuation (dB) in the power spectrum. normalized bandwidth must be greater than zero.
          The default is 0.15.

               •     Gauss-Mod Sine Pattern —

          Gauss-Mod Sine Pattern is an array that contains a Gaussian-modulated sinusoidal pattern of
            samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents Gauss-Mod Sine Pattern, the Gaussian Modulated Sine
       Pattern VI generates the pattern according to the following equations:


      and


      where Ais the amplitude, bis the normalized bandwidth, qis the attenuation, fc is
       the center frequency (Hz), dis the delay, and Nis the samples.

      The following equation represents the envelope of the Gaussian-modulated sine
       pattern:


4392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4393 ordinal=4393 -->
## Functions

Functions


The following equation represents the Fourier transform of the envelope:


In its power spectrum, at frequency point fc, the power spectrum density reaches the
peak value      . When at frequency points               , the power spectrum density
decreases qdB from the peak value, where qdenotes attenuation, as shown by the
following screenshot.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Generation\
   Gauss Mod Sine Generation.vi

GaussianGaussian MonopulseMonopulse

Generates an array that contains a Gaussian monopulse.


                                                    © National Instruments 4393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4394 ordinal=4394 -->
## Functions

Functions


      Inputs/Outputs

               •      center frequency (Hz) —

            center frequency (Hz) is the center frequency, or frequency of the carrier, in Hertz. The default is
               1.

               •      samples —

           samples is the number of samples of the Gaussian Monopulse. If samples is less than 1, the VI
             sets Gaussian Monopulse to an empty array and returns an error. The default is 128.

               •      amplitude —

           amplitude is the amplitude of the Gaussian Monopulse. The default is 1.

               •      delay (s) —

            delay (s) shifts the midpoint of the Gaussian Monopulse. The default is 0.

               •       delta t (s) —

            delta t (s) is the sampling interval. delta t (s) must be greater than zero. If delta t (s) is less than
            or equal to zero, the VI sets Gaussian Monopulse to an empty array and returns an error. The
             default is 0.1.

               •      Gaussian Monopulse —

           Gaussian Monopulse is an array that contains a Gaussian monopulse of samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents Gaussian Monopulse, the Gaussian Monopulse VI
       generates the pattern according to the following equations.

4394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4395 ordinal=4395 -->
## Functions

Functions


and

Xi = i* Δt-d

for i=0,1,…N—1,

where ais the amplitude, dis the delay, fc is the center frequency (Hz), and Nis the
samples.

The Gaussian monopulse has a very low DC component and a wide bandwidth.

SincSinc PatternPattern

Generates an array containing a sinc pattern.


Inputs/Outputs

   •      samples —

    samples is the number of samples of the Sinc Pattern. The default is 128.

    samples must be greater than or equal to 0. If samples is less than zero, the VI sets Sinc Pattern
     to an empty array and returns an error.

   •      amplitude —

    amplitude is the amplitude of Sinc Pattern. The default is 1.0.

   •      delay —

    delay shifts the peak value within the Sinc Pattern as the VI generates the pattern. The default is
     0.0.


                                                    © National Instruments 4395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4396 ordinal=4396 -->
## Functions

Functions


          The peak value of the Sinc Pattern occurs at the index value i = delay/(delta t).

               •       delta t —

            delta t is the sampling interval. The default is 0.1.

                  It is a floating-point number inversely proportional to the width of the main sinc lobe. That is,
            the smaller the sampling interval, the wider the main lobe; the larger the sampling interval, the
            smaller the main lobe. Notice that when delta t is 1, and delay is an integer value, the VI sets
            Sinc Pattern to zero except at the point where i = delay. At this point, the value is equal to
            amplitude. The recommended range of values for the sampling interval is 0 < delta t < 1. delta t
          must be greater than 0.0. If delta t is less than or equal to zero, the VI sets Sinc Pattern to an
          empty array and returns an error.

               •      Sinc Pattern —

            Sinc Pattern returns the array containing the sinc pattern of samples.

          The largest Sinc Pattern the VI can generate depends on the amount of memory in your system
          and is theoretically limited to 2,147,483,647 (231 – 1) elements.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents Sinc Pattern, the Sinc Pattern VI generates the pattern
       according to the following equation.

      yi = asinc(iΔt– d)

        for i= 0, 1, 2, …, n– 1,

      where                       , ais the amplitude, Δ tis the sampling interval delta t, dis the
       delay, and nis the number of samples.

      The main lobe of the sinc function, sinc(x), is the part of the sinc curve bounded by the
       region –1 ≤ x≤ 1.


4396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4397 ordinal=4397 -->
## Functions

Functions

When |x| = 1, the sinc(x) = 0.0, and the peak value of the sinc function occurs when x=
0. Using L'Hopital's Rule, you can show that sinc(0) = 1 and that this is also its peak
value. Thus, the main lobe is the region of the sinc curve encompassed by the first set
of zeros to the left and the right of the sinc value.

PeriodicPeriodic SincSinc PatternPattern

Generates an array containing a periodic sinc pattern.


Inputs/Outputs

   •      delay (s) —

    delay (s) shifts the peak of the Periodic Sinc Pattern. The default is 0.

   •      samples —

    samples is the number of samples of the Periodic Sinc Pattern. If samples is less than 1, the VI
     sets Periodic Sinc Pattern to an empty array and returns an error. The default is 128.

   •      amplitude —

    amplitude is the amplitude of the Periodic Sinc Pattern. The default is 1.

   •      order —

    order specifies the number of zero crossings between two adjacent peaks, which is equal to
    order – 1. The default is 9.

   •       delta t (s) —

    delta t (s) is the sampling interval. delta t (s) must be greater than zero. If delta t (s) is less than
    or equal to zero, the VI sets Periodic Sinc Pattern to an empty array and returns an error. The
     default is 0.1.

   •      Periodic Sinc Pattern —


                                                    © National Instruments 4397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4398 ordinal=4398 -->
## Functions

Functions


            Periodic Sinc Pattern is an array that contains the periodic sinc pattern of samples.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents Periodic Sinc Pattern, the Periodic Sinc Pattern VI
       generates the pattern according to the following equation.


        for i= 0, 1, 2, …, N– 1, where ais the amplitude, nis the order, dis the delay (s), and
   Nis the samples. A higher value nresults in a wider bandwidth.

     SineSine PatternPattern

       Generates an array containing a sinusoidal pattern.


      Inputs/Outputs

               •      samples —

           samples is the number of samples of the Sinusoidal Pattern. samples must be greater than or
            equal to 0. The default is 128.

                    If samples is less than zero, the VI sets Sinusoidal Pattern to an empty array and returns an
               error.

               •      amplitude —

           amplitude is the amplitude of Sinusoidal Pattern. The default is 1.0.


4398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4399 ordinal=4399 -->
## Functions

Functions

   •      phase(degrees) —

    phase is the phase in of the sine wave without reset and must be in degrees. The default is 0.0.

          Note phase must be in degrees rather than radians. If phase is in radians, make sure
           you convert it to degrees, as shown in the following illustration, before using the Sine
             Pattern VI.


   •       cycles —

    cycles is the number of complete periods of the Sinusoidal Pattern. The default value is 1.0.

          Note Because cycles is a floating-point number, fractional cycles are possible for the
             Sinusoidal Pattern. Furthermore, setting cycles to a negative number does not
             generate an error condition because it is mathematically correct and useful to
             consider negative frequencies in Fourier and spectral analysis.

   •      Sinusoidal Pattern —

    Sinusoidal Pattern returns an array containing a sinusoidal pattern of samples.

    The largest Sinusoidal Pattern the VI can generate depends on the amount of memory in your
    system and is theoretically limited to 2,147,483,647 (231 – 1) elements.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If the sequence Yrepresents Sinusoidal Pattern, the Sine Pattern VI generates the
pattern according to the following equations.

yi = asin(xi)

for i= 0, 1, 2, …, n– 1,

                                                    © National Instruments 4399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4400 ordinal=4400 -->
## Functions

Functions

      where ais the amplitude, kis the number of cycles in the pattern, ϕ0 is the initial
      phase in degrees, and nis the number of samples

      TriangleTriangle PatternPattern

       Generates an array that contains a triangle pattern.


      Inputs/Outputs

               •      width (s) —

           width (s) is the width of the Triangle Pattern. width (s) must be greater than zero. The default is
           10.

               •      samples —

           samples is the number of samples of the Triangle Pattern. If samples is less than 1, the VI sets
            Triangle Pattern to an empty array and returns an error. The default is 128.

               •      amplitude —

           amplitude is the amplitude of the Triangle Pattern. The default is 1.0.

               •      delay (s) —

            delay (s) shifts the starting point of the Triangle Pattern in the time axis. The default is 0.

               •       delta t (s) —

            delta t (s) is the sampling interval. delta t (s) must be greater than zero. If delta t (s) is less than
            or equal to zero, the VI sets Triangle Pattern to an empty array and returns an error. The default
                is 0.1.

               •     asymmetry —


4400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4401 ordinal=4401 -->
## Functions

Functions


    asymmetry specifies the asymmetric character of the Triangle Pattern. The asymmetry is the
     projection of the line segment between the start and the peak divided by the width. The default
      is 0.5.

   •       Triangle Pattern —

    Triangle Pattern returns an array that contains the triangle pattern of samples.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If the sequence Yrepresents Triangle Pattern, the Triangle Pattern VI generates the
pattern according to the following equations.


for i= 0,1,2, …,N–1, 0 ≤ k≤ 1,

where wis the width (s), kis the asymmetry, ais the amplitude, Nis the samples,
and

Xi = Δt*i-d

where dis the delay (s).

The following illustration shows the definition of asymmetry. D is the projection of B
on AC.


                                                    © National Instruments 4401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4402 ordinal=4402 -->
## Functions

Functions


     PulsePulse PatternPattern

       Generates an array containing a pulse pattern.


      Inputs/Outputs

               •      samples —

           samples is the number of samples of the Pulse Pattern. The default is 128.

           samples must be greater than or equal to delay + width. If samples is less than zero, the VI sets
            Pulse Pattern to an empty array and returns an error.

               •      amplitude —

           amplitude is the amplitude of Pulse Pattern. The default is 1.0.

               •      delay —

            delay must be greater than or equal to 0. The default is 0.

               •      width —

           width must be greater than or equal to 0. The default is 1.

               •      Pulse Pattern —

            Pulse Pattern returns the pulse pattern of samples.

          The largest Pulse Pattern the VI can generate depends on the amount of memory in your system,


4402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4403 ordinal=4403 -->
## Functions

Functions


    and it is theoretically limited to 2,147,483,647 (231 – 1) elements.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If the sequence Xrepresents Pulse Pattern, the Pulse Pattern VI generates the pattern
according to the following equation.


for i= 0, 1, 2, …, n– 1,

where ais the amplitude, dis the delay, wis the width, and nis the number of
samples.

RampRamp PatternPattern

Generates an array containing a ramp pattern. You must manually select the
polymorphic instance you want to use.


   • Ramp Pattern by Samples VI
   • Ramp Pattern by Delta VI

Let the sequence Xrepresent Ramp Pattern. For the Ramp Pattern by Samples
instance, if type is Linear, the Ramp Pattern VI generates the pattern according to the
following equation:

xi = x0 + iΔx

for i= 0, 1, 2, …, n– 1


                                                    © National Instruments 4403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4404 ordinal=4404 -->
## Functions

Functions

      where x0 is the start. Δx= (end – start)/m. nis the samples. m= nif exclude end? is
      TRUE. Otherwise, m= n– 1.

       Let the sequence Xrepresent Ramp Pattern. If type is Logarithmic, the Ramp Pattern
        VI generates the pattern according to the following equation:

      xi = exp[ln(x0) + iΔx]

        for i= 0, 1, 2, …, n– 1

      where x0 is the start. Δx= [ln(end) – ln(start)]/m. start and end must be greater than
        0. nis the samples. m= nif exclude end? is TRUE. Otherwise, m= n– 1.

       For the Ramp Pattern by Delta instance, this VI generates the pattern according to the
       following equation:


        for i= 0, 1, 2, …, n– 1, and

      where x0 is the start, Δxis delta, and [ ] means round towards -Infinity.

      The Ramp Pattern VI does not impose conditions on the relationship between start
      and end. Therefore, the Ramp Pattern VI can generate ramp-up and ramp-down
       patterns.

      The following block diagram illustrates how to use the Ramp Pattern VI to generate the
      ramp pattern of any size greater than or equal to 1.


4404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4405 ordinal=4405 -->
## Functions

Functions


RampRamp PatternPattern byby SamplesSamples VIVI

Generates an array containing a ramp pattern. You must manually select the
polymorphic instance you want to use.


Inputs/Outputs

   •      samples —

    samples is the number of samples of the Ramp Pattern. If samples is less than two, the VI sets
   Ramp Pattern to an empty array and returns an error. The default is 128.

       If samples is 1 and exclude end? is TRUE, the VI returns an array with one element of start.

   •     end —

    end is the ending value, or final value, of Ramp Pattern. The default is 1.

   •       start —

     start is the starting value, or first value, of Ramp Pattern. The default is 0.

   •      exclude end? —

    exclude end? specifies whether Ramp Pattern includes end. Ramp Pattern does not include end


                                                    © National Instruments 4405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4406 ordinal=4406 -->
## Functions

Functions


                    if exclude end? is TRUE. The default is FALSE.

                    If samples is 1 and exclude end? is TRUE, the VI returns an array with one element of start, with
          no error.

               •      type —

           type specifies the type of Ramp Pattern to generate.

           0      Linear (default)
           1      Logarithmic

               •     Ramp Pattern —

         Ramp Pattern returns the ramp pattern of samples.

          The largest Ramp Pattern this VI can generate depends on the amount of memory in your
            system, and it is theoretically limited to 2,147,483,647 (231 – 1) elements.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let the sequence Xrepresent Ramp Pattern. For the Ramp Pattern by Samples
       instance, if type is Linear, the Ramp Pattern VI generates the pattern according to the
       following equation:

      xi = x0 + iΔx

        for i= 0, 1, 2, …, n– 1

      where x0 is the start. Δx= (end – start)/m. nis the samples. m= nif exclude end? is
      TRUE. Otherwise, m= n– 1.

       Let the sequence Xrepresent Ramp Pattern. If type is Logarithmic, the Ramp Pattern
        VI generates the pattern according to the following equation:


4406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4407 ordinal=4407 -->
## Functions

Functions

xi = exp[ln(x0) + iΔx]

for i= 0, 1, 2, …, n– 1

where x0 is the start. Δx= [ln(end) – ln(start)]/m. start and end must be greater than
0. nis the samples. m= nif exclude end? is TRUE. Otherwise, m= n– 1.

For the Ramp Pattern by Delta instance, this VI generates the pattern according to the
following equation:


for i= 0, 1, 2, …, n– 1, and

where x0 is the start, Δxis delta, and [ ] means round towards -Infinity.

The Ramp Pattern VI does not impose conditions on the relationship between start
and end. Therefore, the Ramp Pattern VI can generate ramp-up and ramp-down
patterns.

The following block diagram illustrates how to use the Ramp Pattern VI to generate the
ramp pattern of any size greater than or equal to 1.


RampRamp PatternPattern byby DeltaDelta VIVI

Generates an array containing a ramp pattern. You must manually select the
polymorphic instance you want to use.

                                                    © National Instruments 4407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4408 ordinal=4408 -->
## Functions

Functions


      Inputs/Outputs

               •       delta —

            delta is the interval between two adjacent samples in Ramp Pattern. The default is 0.

               •     end —

          end is the ending value, or final value, of Ramp Pattern. The default is 1.

               •       start —

              start is the starting value, or first value, of Ramp Pattern. The default is 0.

               •     Ramp Pattern —

         Ramp Pattern returns the ramp pattern of samples.

          The largest Ramp Pattern this VI can generate depends on the amount of memory in your
            system, and it is theoretically limited to 2,147,483,647 (231 – 1) elements.

               •      samples —

           samples is the number of samples of the Ramp Pattern.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


       Let the sequence Xrepresent Ramp Pattern. For the Ramp Pattern by Samples
       instance, if type is Linear, the Ramp Pattern VI generates the pattern according to the
       following equation:

      xi = x0 + iΔx

        for i= 0, 1, 2, …, n– 1

4408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4409 ordinal=4409 -->
## Functions

Functions

where x0 is the start. Δx= (end – start)/m. nis the samples. m= nif exclude end? is
TRUE. Otherwise, m= n– 1.

Let the sequence Xrepresent Ramp Pattern. If type is Logarithmic, the Ramp Pattern
VI generates the pattern according to the following equation:

xi = exp[ln(x0) + iΔx]

for i= 0, 1, 2, …, n– 1

where x0 is the start. Δx= [ln(end) – ln(start)]/m. start and end must be greater than
0. nis the samples. m= nif exclude end? is TRUE. Otherwise, m= n– 1.

For the Ramp Pattern by Delta instance, this VI generates the pattern according to the
following equation:


for i= 0, 1, 2, …, n– 1, and

where x0 is the start, Δxis delta, and [ ] means round towards -Infinity.

The Ramp Pattern VI does not impose conditions on the relationship between start
and end. Therefore, the Ramp Pattern VI can generate ramp-up and ramp-down
patterns.

The following block diagram illustrates how to use the Ramp Pattern VI to generate the
ramp pattern of any size greater than or equal to 1.


                                                    © National Instruments 4409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4410 ordinal=4410 -->
## Functions

Functions


      ChirpChirp PatternPattern

       Generates an array containing a chirp pattern.


      Inputs/Outputs

               •      samples —

           samples is the number of samples of the Chirp Pattern. The default is 128.

               •      amplitude —

           amplitude is the amplitude of Chirp Pattern. The default is 1.0.

               •       f1 —

             f1 is the beginning frequency of Chirp Pattern in normalized units of cycles/sample.

               •       f2 —

             f2 is the ending frequency of Chirp Pattern in normalized units of cycles/sample.

               •      Chirp Pattern —

            Chirp Pattern is a signal with frequency ramping from f1*fsto f2*fs, where fsis the sampling
               rate.


4410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4411 ordinal=4411 -->
## Functions

Functions

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If the sequence Yrepresents Chirp Pattern, the Chirp Pattern VI obtains the elements
of Yusing the following equation:

yi = A*sin((0.5*a*i+ b)*i)

for i= 0, 1, 2, …, n– 1

where Ais amplitude,

a= 2π(f2 – f1)/n, b= 2πf1, f1 is the beginning frequency in normalized units of cycles/
sample, f2 is the ending frequency in normalized units of cycles/sample, nis the
number of samples.
SineSine WaveWave

Generates an array containing a sine wave.


Inputs/Outputs

   •       reset phase —

     reset phase determines the initial phase of sine wave. The default is TRUE.

       If reset phase is TRUE, LabVIEW sets the initial phase to phase in. If reset phase is FALSE,
    LabVIEW uses the value of phase out from when the VI last executed as the initial phase of sine
    wave.

   •      samples —

                                                    © National Instruments 4411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4412 ordinal=4412 -->
## Functions

Functions


           samples is the number of samples of the sine wave. The default is 128.

               •      amplitude —

           amplitude is the amplitude of sine wave. The default is 1.0.

               •      frequency —

           frequency is the frequency of sine wave in normalized units of cycles/sample. The default is 1
            cycle/128 samples or 7.8125E–3 cycles/sample.

               •      phase in —

           phase in is the initial phase, in degrees, of sine wave when reset phase is TRUE.

               •       sine wave —

            sine wave is the output sine wave.

               •      phase out —

           phase out is the phase, in degrees, of the next sample of sine wave.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents sine wave, the Sine Wave VI generates the pattern
       according to the following equation.

      yi = a*sin(phase[i])

        for i= 0, 1, 2, …, n– 1 and where

   ais amplitude, phase[i] = initial_phase + f*360*i, frequency is the frequency in
      normalized units of cycles/sample, initial_phase is phase in if reset phase is TRUE,
       initial_phase is the phase out from the previous execution of this instance of the VI if
       reset phase is FALSE.


4412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4413 ordinal=4413 -->
## Functions

Functions

The Sine Wave VI is reentrant, so you can use it to simulate a continuous acquisition
from a sine wave function generator. If the input control reset phase is FALSE,
subsequent calls to a specific instance of the Sine Wave VI produce the output sine
wave array containing the next samples of a sine wave. The VI uses the phase out
value as the new phase in the next time the VI executes.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Generation\
   Function Generator with FM.vi

TriangleTriangle WaveWave

Generates an array containing a triangle wave.


Inputs/Outputs

   •       reset phase —

    reset phase determines the initial phase of triangle wave. The default is TRUE.

       If reset phase is TRUE, LabVIEW sets the initial phase to phase in. If reset phase is FALSE,
    LabVIEW uses the value of phase out from when the VI last executed as the initial phase of
     triangle wave.

   •      samples —

    samples is the number of samples of the triangle wave. The default is 128.

   •      amplitude —

    amplitude is the amplitude of triangle wave. The default is 1.0.


                                                    © National Instruments 4413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4414 ordinal=4414 -->
## Functions

Functions

               •      frequency —

           frequency is the frequency of triangle wave in normalized units of cycles/sample. The default is
           1 cycle/128 samples, or 7.8125E–3 cycles/sample

               •      phase in —

           phase in is the initial phase, in degrees, of triangle wave when reset phase is TRUE. The default
                is 0.

               •       triangle wave —

             triangle wave is the output triangle wave.

               •      phase out —

           phase out is the phase, in degrees, of the next sample of triangle wave.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents triangle wave, the Triangle Wave VI generates the pattern
       according to the following equation.

      yi = a*tri(phase[i])

        for i= 0, 1, 2, …, n– 1 and where ais amplitude and nis the number of samples.

        tri(phase[i] is defined by the following equation.


                                                             ,


      where

   p= (phase[i] modulo 360), phase[i] = initial_phase + frequency*360*i, frequency is the
       frequency in normalized units of cycles/sample, initial_phase is phase in if reset phase

4414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4415 ordinal=4415 -->
## Functions

Functions

is TRUE, initial_phase is the phase out from the previous execution of this instance of
the VI if reset phase is FALSE.

The Triangle Wave VI is reentrant, so you can use it to simulate a continuous
acquisition from a triangle wave function generator. If the input control reset phase is
FALSE, subsequent calls to a specific instance of the Triangle Wave VI produce the
output triangle wave array containing the next samples of a triangle wave.

Because the Triangle Wave VI is reentrant, when reset phase is FALSE , the Triangle
Wave VI uses the phase out value as its new phase in the next time the VI executes.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Generation\
   Function Generator with FM.vi

SquareSquare WaveWave

Generates an array containing a square wave.


Inputs/Outputs

   •       reset phase —

    reset phase determines the initial phase of square wave. The default is TRUE.

       If reset phase is TRUE, LabVIEW sets the initial phase to phase in. If reset phase is FALSE,
    LabVIEW uses the value of phase out from when the VI last executed as the initial phase of
    square wave.

   •      samples —


                                                    © National Instruments 4415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4416 ordinal=4416 -->
## Functions

Functions


           samples is the number of samples of the square wave. The default is 128.

               •      amplitude —

           amplitude is the amplitude of square wave. The default is 1.0.

               •      frequency —

           frequency is the frequency of square wave in normalized units of cycles/sample. The default is 1
            cycle/128 samples or 7.8125E–3 cycles/sample.

               •      phase in —

           phase in is the initial phase, in degrees, of square wave when reset phase is TRUE. The default is
               0.

               •      duty cycle (%) —

           duty cycle is the percentage of time a square wave remains high versus low over one period. The
             default is 50.

               •      square wave —

           square wave is the output square wave.

               •      phase out —

           phase out is the phase, in degrees, of the next sample of square wave.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents square wave, the Square Wave VI generates the pattern
       according to the following equation.

      yi = a*square(phase[i])

        for i= 0, 1, …, n– 1 and where ais amplitude and nis the number of samples.


4416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4417 ordinal=4417 -->
## Functions

Functions

This VI calculates square(phase[i]) using the following equation:


                                                             ,


where

p= phase[i] modulo 360, duty is duty cycle, phase[i] = initial_phase +
frequency*360*i, frequency is the frequency in normalized units of cycles/sample,
initial_phase is phase in if reset phase is TRUE, initial_phase is the phase out from the
previous execution of this instance of the VI if reset phase is FALSE.

The Square Wave VI is reentrant, so you can use it to simulate a continuous acquisition
from a square wave function generator. If the input control reset phase is FALSE,
subsequent calls to a specific instance of the Square Wave VI produce the output
square wave array containing the next samples of a square wave.

Because the Square Wave VI is reentrant, if reset phase is FALSE, the VI uses the phase
out value as its new phase in the next time the VI executes.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Signal Generation\
   Function Generator with FM.vi

SawtoothSawtooth WaveWave

Generates an array containing a sawtooth wave.


                                                    © National Instruments 4417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4418 ordinal=4418 -->
## Functions

Functions

      Inputs/Outputs

               •       reset phase —

             reset phase determines the initial phase of sawtooth wave. The default is TRUE.

                    If reset phase is TRUE, LabVIEW sets the initial phase to phase in. If reset phase is FALSE,
           LabVIEW uses the value of phase out from when the VI last executed as the initial phase of
           sawtooth wave.

               •      samples —

           samples is the number of samples of the sawtooth wave. The default is 128.

               •      amplitude —

           amplitude is the amplitude of sawtooth wave. The default is 1.0.

               •      frequency —

           frequency is the frequency of sawtooth wave in normalized units of cycles/sample. The default
                is 1 cycle/128 samples, or 7.8125E–3 cycles/sample.

               •      phase in —

           phase in is the initial phase, in degrees, of sawtooth wave when reset phase is TRUE. The
             default is 0.

               •      sawtooth wave —

           sawtooth wave is the output sawtooth wave.

               •      phase out —

           phase out is the phase, in degrees, of the next sample of sawtooth wave.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents sawtooth wave, the Sawtooth Wave VI generates the
       pattern according to the following equation.


4418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4419 ordinal=4419 -->
## Functions

Functions

y[i] = a*sawtooth(phase[i])

for i= 0, 1, 2, …, n– 1 and where ais amplitude and nis the number of samples.

This VI calculates sawtooth(phase[i]) using the following equation:


                                                          ,


where

p= phase[i] modulo 360, phase[i] = initial_phase + frequency*360*i, frequency is the
frequency in normalized units of cycles/sample, initial_phase is phase in if reset phase
is TRUE, initial_phase is phase out from the previous execution of this instance of the
VI if reset phase is FALSE.

The preceding equations can be represented by the following equation.


The Sawtooth Wave VI is reentrant, so you can use it to simulate a continuous
acquisition from a sawtooth wave function generator. If the input control reset phase
is FALSE, subsequent calls to a specific instance of the Sawtooth Wave VI produce the
output sawtooth wave array containing the next samples of a sawtooth wave.

Because the Sawtooth Wave VI is a reentrant VI, when reset phase is set to FALSE, the
Sawtooth Wave VI uses the phase out value as its new phase in the next time the VI
executes.

Examples

Refer to the following example files included with LabVIEW.

   • labview\examples\Signal Processing\Signal Generation\
   Function Generator with FM.vi


                                                    © National Instruments 4419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4420 ordinal=4420 -->
## Functions

Functions

      ArbitraryArbitrary WaveWave

       Generates an array containing an arbitrary wave.


      Inputs/Outputs

               •     Wave Table —

          Wave Table is one cycle of the waveform used in creating the output arbitrary wave.

               •      samples —

           samples is the number of samples in arbitrary wave. The default is 128.

           samples must be greater than or equal to 0. If samples is less than zero, the VI sets arbitrary
          wave to an empty array and returns an error.

               •      amplitude —

           amplitude is the amplitude of arbitrary wave. The default is 1.

               •      frequency —

           frequency is the frequency of arbitrary wave in normalized units of cycles/sample. The default
                is 1 cycle/128 samples or 7.8125E–3 cycles/sample.

               •      phase in —

           phase in is the initial phase, in degrees, of arbitrary wave when reset phase is 0.

               •       reset phase —

             reset phase determines the initial phase of arbitrary wave. The default is TRUE.

                    If reset phase is TRUE, LabVIEW sets the initial phase to phase in. If reset phase is FALSE,


4420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4421 ordinal=4421 -->
## Functions

Functions


    LabVIEW uses the value of phase out from when the VI last executed as the initial phase of
     arbitrary wave.

   •       interpolation —

     interpolation determines the type of interpolation the VI uses to generate arbitrary wave from
    the Wave Table array. The default is 0 (no interpolation).

       If interpolation is 0, the VI does not use interpolation. If interpolation is 1, the VI uses linear
     interpolation.

   •       arbitrary wave —

     arbitrary wave is the output arbitrary wave.

   •      phase out —

    phase out is the phase of the waveform in degrees.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If the sequence Yrepresents arbitrary wave, the Arbitrary Wave VI generates the
sequence according to the following equation:

yi = a*arb(phasei)

for i= 0, 1, 2, …, n– 1

where ais amplitude and nis samples.

This VI calculates arb(phasei) using the following equation:


where


                                                    © National Instruments 4421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4422 ordinal=4422 -->
## Functions

Functions

  mis the size of the Wave Table array, WT(x) = Wave Table[int(x)] if interpolation = 0
       (no interpolation), WT(x) is the linearly interpolated value of Wave Table[int(x)] and
     Wave Table[(int(x) + 1) modulo m] if interpolation = 1 (linear interpolation), phasei =
       initial_phase + frequency*360.0*i, frequency is the frequency in normalized units of
       cycles/sample, initial_phase is phase in if reset phase is TRUE, initial_phase is the
      phase out from the previous execution of this instance of the VI if reset phase is FALSE.

      The Arbitrary Wave VI is reentrant, so you can use it to simulate a continuous
       acquisition from an arbitrary wave function generator. If reset phase is FALSE,
      subsequent calls to a specific instance of this VI produce arbitrary wave containing the
       next samples of the arbitrary wave. LabVIEW sets phase out to phasen, and this
       reentrant VI uses this value as the new phase in if reset phase is FALSE the next time
        this VI executes.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Signal Generation\
        Arbitrary Wave Display.vi

     UniformUniform WhiteWhite NoiseNoise

       Generates a uniformly distributed, pseudorandom pattern whose values are in the
      range [–a:a], where ais the absolute value of amplitude.


      Inputs/Outputs

               •        initialize? —

               initialize? controls the reseeding of the noise sample generator after the first call of the VI.


4422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4423 ordinal=4423 -->
## Functions

Functions


       If initialize? is TRUE, accepts a new state or new seed value and begins producing noise samples
    based on the new state or new seed value. If initialize? is FALSE, this VI maintains the initial
     internal seed state and resumes producing noise samples as a continuation of the previous
    noise sequence. The default is TRUE.

   •      samples —

    samples is the number of the samples of the uniform white noise. samples must be greater
    than 0. The default is 128.

   •      amplitude —

    amplitude is the amplitude of uniform white noise. The default is 1.0.

   •      seed —

    seed determines how to generate the internal seed state when initialize? is TRUE.

       If seed is greater than 0, this VI uses seed to generate the internal state directly. If seed is less
    than or equal to 0, this VI uses a random number to generate the internal state. seed must not be
    a multiple of 16384. If initialize? is FALSE, this VI ignores seed. The default is -1.

   •      uniform white noise —

    uniform white noise contains the uniformly distributed, pseudorandom pattern.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Uniform White Noise VI generates the pseudorandom sequence using the
Wichmann-Hill generator. The pseudorandom number generator implements a triple-
seeded linear congruential algorithm. Given that the probability density function, f(x),
of the uniformly distributed uniform white noise is


where ais the absolute value of the specified amplitude.


                                                    © National Instruments 4423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4424 ordinal=4424 -->
## Functions

Functions

      The following equations define the expected mean value, µ, and the expected
       standard deviation value, σ, of the pseudorandom sequence:

     µ = E{x} = 0

      The pseudorandom sequence produces approximately 6.95 * 1012 samples before the
       pattern repeats itself.

      You can use uniform white noise as a stimulus to measure the frequency response of
       amplifiers and electronic filters.

      You can use the initialize? input to generate a long random noise sequence block by
       block. The following block diagram shows two ways to generate identical 300-sample
      uniform white noise sequences with a seed of 2.


      You also can use the Uniform White Noise Waveform VI to generate a uniform white
       noise signal or the Continuous Random VI to generate random values from a
       continuous uniform-distributed variate.

     GaussianGaussian WhiteWhite NoiseNoise

       Generates a Gaussian-distributed, pseudorandom pattern whose statistical profile is
      (mu, sigma) = (0, s), where sis standard deviation.


4424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4425 ordinal=4425 -->
## Functions

Functions

Inputs/Outputs

   •        initialize? —

     initialize? controls the reseeding of the noise sample generator after the first call of the VI.

       If initialize? is TRUE, accepts a new state or new seed value and begins producing noise samples
    based on the new state or new seed value. If initialize? is FALSE, this VI maintains the initial
     internal seed state and resumes producing noise samples as a continuation of the previous
    noise sequence. The default is TRUE.

   •      samples —

    samples is the number of samples of the Gaussian noise pattern. samples must be greater than
     0. The default is 128.

   •      standard deviation —

    standard deviation is the standard deviation of the Gaussian probability density function. The
     default is 1.0.

   •      seed —

    seed determines how to generate the internal seed state when initialize? is TRUE.

       If seed is greater than 0, this VI uses seed to generate the internal state directly. If seed is less
    than or equal to 0, this VI uses a random number to generate the internal state. seed must not be
    a multiple of 16384. If initialize? is FALSE, this VI ignores seed. The default is -1.

   •      Gaussian noise pattern —

    Gaussian noise pattern returns the Gaussian-distributed, pseudorandom pattern.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Gaussian White Noise VI generates the Gaussian-distributed pseudorandom
sequence using a modified version of the Box-Muller method to transform uniformly
distributed random numbers into Gaussian-distributed random numbers. This VI
generates the uniform pseudorandom numbers using the Wichmann-Hill generator.


                                                    © National Instruments 4425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4426 ordinal=4426 -->
## Functions

Functions

      Given that the probability density function, f(x), of the Gaussian-distributed Gaussian
       noise pattern is


      where sis the absolute value of the specified standard deviation. You can compute
       the expected values, E{·}, using the following formula:


      The following equations define the expected mean value, µ, and the expected
       standard deviation value, σ, of the pseudorandom sequence:

     µ = E{x} = 0 σ = [E{x – µ}²]1/2 = s

      The pseudorandom sequence produces approximately 6.95 * 1012 samples before the
       pattern repeats itself. The probability density function (PDF) of the pseudorandom
      sequence approximates a Gaussian PDF with peak values of at least 6σ.

      Gaussian white noise provides a realistic simulation of some real-world situations.
      Because of its independent statistical characteristics, Gaussian white noise also often
       acts as the source of other random number generators. The additive white Gaussian
       noise (AWGN) channel model is widely used in communications.

      You can use the initialize? input to generate a long random noise sequence block by
       block. The following block diagram shows two ways to generate identical 300-sample
      Gaussian white noise sequences with a seed of 2.


4426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4427 ordinal=4427 -->
## Functions

Functions


You also can use the Gaussian White Noise Waveform VI to generate a Gaussian white
noise signal.

PeriodicPeriodic RandomRandom NoiseNoise

Generates an array containing periodic random noise (PRN).


Inputs/Outputs

   •      samples —

    samples is the number of samples of the periodic random noise. The default is 128.

   •       spectral amplitude —

    spectral amplitude is the magnitude of the frequency domain components of the periodic
   random noise.

   •      seed —

    seed, when greater than 0, causes reseeding of the noise sample generator. The default is –1.

    LabVIEW maintains the internal seed state independently for each instance of this reentrant VI.
    For a specific instance of this VI, if seed is less than or equal to 0, LabVIEW does not reseed the
    noise generator, and the noise generator resumes producing noise samples as a continuation of
    the previous noise sequence.

   •      periodic random noise —


                                                    © National Instruments 4427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4428 ordinal=4428 -->
## Functions

Functions


            periodic random noise is the output array containing periodic random noise.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The output array contains all frequencies that can be represented with an integral
      number of cycles in the requested number of samples. Each frequency-domain
      component has a magnitude of spectral amplitude and random phase.

      Another way of thinking of the output array of the Periodic Random Noise VI is that it is
      a summation of sinusoidal signals with the same amplitudes but with random phases.
      The unit of spectral amplitude is the same as the output periodic random noise and is
      a linear measure of amplitude, similar to other signal generation VIs.

      The Periodic Random Noise VI generates the same periodic random sequence for a
       given positive seed value. The Periodic Random Noise VI does not reseed the random
      phase generator if seed is negative.

      The output periodic random noise is bounded by the following values


      You can use periodic random noise to compute the frequency response of a linear
      system in one time record instead of averaging the frequency response over several
      time records, as you must for nonperiodic random noise sources.

      You do not need to window periodic random noise before performing spectral analysis
      because periodic random noise is self-windowing and therefore has no spectral
       leakage. This is because periodic random noise contains only integral-cycle sinusoids.

      BinaryBinary MLSMLS

       Generates a maximum length sequence of ones and zeros using a modulo-2 primitive
      polynomial of order polynomial order.


4428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4429 ordinal=4429 -->
## Functions

Functions


Inputs/Outputs

   •        initialize? —

     initialize? controls the reseeding of the noise sample generator after the first call of the VI.

       If initialize? is TRUE, accepts a new state or new seed value and begins producing noise samples
    based on the new state or new seed value. If initialize? is FALSE, this VI maintains the initial
     internal seed state and resumes producing noise samples as a continuation of the previous
    noise sequence. The default is TRUE.

   •      samples —

    samples specifies the number of samples contained in the mls sequence output array. samples
    must be greater than 0. The default is 128.

   •      polynomial order —

    polynomial order specifies the order of the modulo-2 primitive polynomial used to generate mls
    sequence. If the input value is out of range, this VI truncates the polynomial order to [3, 62]. The
     default is 31.

   •      seed —

    seed determines how to generate the internal seed state when initialize? is TRUE.

       If seed is greater than 0, this VI uses seed to generate the internal state directly. If seed is less
    than or equal to 0, this VI uses a random number to generate the internal state. seed must not be
    a multiple of 16384. If initialize? is FALSE, this VI ignores seed. The default is -1.

   •      mls sequence —

    mls sequence contains the uniformly distributed, pseudorandom pattern.

   •       error code —

    error code specifies a numeric error code.


                                                    © National Instruments 4429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4430 ordinal=4430 -->
## Functions

Functions

      The Binary MLS VI uses a modulo-2 primitive polynomial to generate the binary
     Maximum Length Sequence (MLS). The mls sequence is periodic with a period of 2n –
                                      – 1              – 1        1. Each period consists of 2n  ones and 2n  – 1 zeros, where nis the polynomial
       order. The mls sequence is spectrally flat, with a near-zero DC term.

       For example, if the polynomial order is 4, the Binary MLS VI uses the polynomial g(p) =
     p4 + p+ 1 to generate the mls sequence with a period of 15 in the following manner:


      where   is the modulo-2 addition, and a0, a1, a2 and a3 are the shift registers.

      The following 15-point sequence comprises each period of the generated sequence: 0,
        0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1. However, the starting point might be different for each
       sequence.

      The MLS, also known as a type of Pseudo-Random Binary Sequence (PRBS), is widely
      used in spread-spectrum transmission systems.

      You can use the initialize? input to generate a long random noise sequence block by
       block. The following block diagram shows two ways to generate identical 300-sample
       Binary MLS noise sequences with a seed of 2.


      You also can use the MLS Sequence Waveform VI to generate a MLS sequence.


4430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4431 ordinal=4431 -->
## Functions

Functions

ImpulseImpulse PatternPattern

Generates an array containing an impulse pattern.


Inputs/Outputs

   •      samples —

    samples is the number of samples of the Impulse Pattern. samples must be greater than delay.
    The default is 128.

       If samples is negative or zero, the VI sets Impulse Pattern to an empty array and returns an error.

   •      amplitude —

    amplitude is the amplitude of Impulse Pattern. The default is 1.0.

   •      delay —

    delay is the index within Impulse Pattern at which the impulse occurs.

    delay must be greater than or equal to 0. If delay is less than zero, or greater than or equal to the
   number of samples, the VI sets Impulse Pattern to zero and returns an error.

   •      Impulse Pattern —

    Impulse Pattern is the output array containing the impulse pattern.

    The largest Impulse Pattern the VI can generate depends on the amount of memory in your
    system and is theoretically limited to 2,147,483,647 (231 – 1) elements.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


If the Impulse Pattern is represented by the sequence X, the Impulse Pattern VI


                                                    © National Instruments 4431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4432 ordinal=4432 -->
## Functions

Functions

       generates the pattern according to the following equation.


        for i= 0, 1, 2, …, n– 1,

      where Ais the amplitude, dis the delay, and nis the number of samples.

    GammaGamma NoiseNoise

       Generates a pseudorandom pattern of values that are the waiting times to the order
      number event of a unit mean Poisson process.


      Inputs/Outputs

               •        initialize? —

               initialize? controls the reseeding of the noise sample generator after the first call of the VI.

                    If initialize? is TRUE, accepts a new state or new seed value and begins producing noise samples
           based on the new state or new seed value. If initialize? is FALSE, this VI maintains the initial
             internal seed state and resumes producing noise samples as a continuation of the previous
            noise sequence. The default is TRUE.

               •      samples —

           samples specifies the number of samples contained in the output array. samples must be
             greater than 0. The default is 128.

               •      order —

            order specifies the event number of the unit mean Poisson process. order must be greater than
               0. The default is 1.

               •      seed —


4432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4433 ordinal=4433 -->
## Functions

Functions


    seed determines how to generate the internal seed state when initialize? is TRUE.

       If seed is greater than 0, this VI uses seed to generate the internal state directly. If seed is less
    than or equal to 0, this VI uses a random number to generate the internal state. seed must not be
    a multiple of 16384. If initialize? is FALSE, this VI ignores seed. The default is -1.

   •    gamma noise —

   gamma noise contains the gamma-distributed, pseudorandom pattern.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Gamma Noise VI generates a Gamma-distributed pseudorandom pattern whose
values are the waiting times that correspond to order. Given the Gamma function,


the probability density function, f(x), of the gamma noise is


where ris the order.

The following equations define the mean value, µ, and the standard deviation value, σ,
of the pseudorandom sequence:

µ = E{x} = r

You can use the initialize? input to generate a long random noise sequence block by
block. The following block diagram shows two ways to generate identical 300-sample
Gamma noise sequences with a seed of 2.


                                                    © National Instruments 4433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4434 ordinal=4434 -->
## Functions

Functions


      You also can use the Gamma Noise Waveform VI to generate a Gamma noise signal or
       the Continuous Random VI to generate random variables from a gamma-distributed
        variate.

     PoissonPoisson NoiseNoise

       Generates a pseudorandom sequence of values that are the number of discrete events
       that occur in a given interval, specified by mean, of a unit rate Poisson process.


      Inputs/Outputs

               •        initialize? —

               initialize? controls the reseeding of the noise sample generator after the first call of the VI.

                    If initialize? is TRUE, accepts a new state or new seed value and begins producing noise samples
           based on the new state or new seed value. If initialize? is FALSE, this VI maintains the initial
             internal seed state and resumes producing noise samples as a continuation of the previous
            noise sequence. The default is TRUE.

               •      samples —

           samples specifies the number of samples contained in the output array. samples must be
             greater than 0. The default is 128.

               •     mean —


4434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4435 ordinal=4435 -->
## Functions

Functions


   mean specifies the interval of a unit rate Poisson process. mean must be greater than or equal to
     0. The default is 1.0.

   •      seed —

    seed determines how to generate the internal seed state when initialize? is TRUE.

       If seed is greater than 0, this VI uses seed to generate the internal state directly. If seed is less
    than or equal to 0, this VI uses a random number to generate the internal state. seed must not be
    a multiple of 16384. If initialize? is FALSE, this VI ignores seed. The default is -1.

   •      poisson noise —

    poisson noise contains the Poisson-distributed, pseudorandom pattern.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Poisson Noise VI generates a Poisson-distributed pseudorandom sequence whose
values are the number of discrete events that occur in a given interval. The following
equation defines the probability density function of the poisson noise:


where λ is the mean.

The following equations define the mean value, µ, and the standard deviation value, σ,
of the pseudorandom sequence:

µ = E{x} = λ σ = [E{(x– µ)²}]1/2 =

Poisson noise is the result of the Poisson process. You can use the Poisson process to
describe the probability of a certain number of events happening in a given period of
time. For example, you can use the Poisson process to describe the nuclear decay of
atoms and the number of messages a transmitting station receives.

You can use the initialize? input to generate a long random noise sequence block by

                                                    © National Instruments 4435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4436 ordinal=4436 -->
## Functions

Functions

       block. The following block diagram shows two ways to generate identical 300-sample
       Poisson noise sequences with a seed of 2.


      You also can use the Poisson Noise Waveform VI to generate a Poisson noise signal or
       the Discrete Random VI to generate random values from a Poisson-distributed variate.

     BinomialBinomial NoiseNoise

       Generates a binomially-distributed, pseudorandom pattern whose values are the
      number of occurrences of an event, given the probability of that event occurring and
       the number of trials.


      Inputs/Outputs

               •        initialize? —

               initialize? controls the reseeding of the noise sample generator after the first call of the VI.

                    If initialize? is TRUE, accepts a new state or new seed value and begins producing noise samples
           based on the new state or new seed value. If initialize? is FALSE, this VI maintains the initial
             internal seed state and resumes producing noise samples as a continuation of the previous
            noise sequence. The default is TRUE.

               •      samples —


4436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4437 ordinal=4437 -->
## Functions

Functions


    samples specifies the number of samples contained in the output array. samples must be
    greater than 0. The default is 128.

   •        trials —

     trials is the number of trials performed for each element of binomial noise. trials must be
    greater than or equal to zero. The default is 1.

   •        trial probability —

     trial probability is the probability that a given trial is true (1). trial probability must be in the
    range [0, 1]. The default is 0.5.

   •      seed —

    seed determines how to generate the internal seed state when initialize? is TRUE.

       If seed is greater than 0, this VI uses seed to generate the internal state directly. If seed is less
    than or equal to 0, this VI uses a random number to generate the internal state. seed must not be
    a multiple of 16384. If initialize? is FALSE, this VI ignores seed. The default is -1.

   •      binomial noise —

    binomial noise contains the binomially-distributed, pseudorandom pattern.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Binomial Noise VI generates a binomially-distributed, pseudorandom pattern
whose values are the number of occurrences of an event. The following equation
defines the probability density function of the binomial noise:


where nis the number of trials, pis the trial probability, and   equals            . To
generalize, P(X= i) is the probability that iof the ntrials equals 1, and n– iequals
zero. When nequals 1, the Binomial noise degenerates into Bernoulli noise.


                                                    © National Instruments 4437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4438 ordinal=4438 -->
## Functions

Functions

      The following equations define the mean value, µ, and the standard deviation value, σ,
       of the pseudorandom sequence:

     µ = E{x} = np

      You can use the initialize? input to generate a long random noise sequence block by
       block. The following block diagram shows two ways to generate identical 300-sample
       Binomial noise sequences with a seed of 2.


      You also can use the Binomial Noise Waveform VI to generate a Binomial noise signal
       or the Discrete Random VI to generate random values from a binomial-distributed
        variate.

      BernoulliBernoulli NoiseNoise

       Generates a pseudorandom pattern of ones and zeros. LabVIEW computes each
      element of bernoulli noise as if flipping a coin weighted by ones probability.


      Inputs/Outputs

               •        initialize? —

               initialize? controls the reseeding of the noise sample generator after the first call of the VI.


4438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4439 ordinal=4439 -->
## Functions

Functions


       If initialize? is TRUE, accepts a new state or new seed value and begins producing noise samples
    based on the new state or new seed value. If initialize? is FALSE, this VI maintains the initial
     internal seed state and resumes producing noise samples as a continuation of the previous
    noise sequence. The default is TRUE.

   •      samples —

    samples specifies the number of samples contained in the output array. samples must be
     greater than 0. The default is 128.

   •      ones probability —

    ones probability specifies the probability of a given element of bernoulli noise being true (1).
    ones probability must be in the range [0, 1]. The default is 0.5.

   •      seed —

    seed determines how to generate the internal seed state when initialize? is TRUE.

       If seed is greater than 0, this VI uses seed to generate the internal state directly. If seed is less
    than or equal to 0, this VI uses a random number to generate the internal state. seed must not be
    a multiple of 16384. If initialize? is FALSE, this VI ignores seed. The default is -1.

   •       bernoulli noise —

     bernoulli noise contains the Bernoulli-distributed, pseudorandom pattern.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Bernoulli Noise VI generates a pseudorandom pattern of ones and zeros that
guarantees the Bernoulli distribution. The following equation defines the probability
density function of the bernoulli noise:

                    – iP(X= i) = pi(1 – p)1     (i= 0, 1)

where pis the ones probability. If ones probability is 0.7, each element of bernoulli
noise has a 70% chance of being one and a 30% chance of being zero. Bernoulli noise
is a special case of Binomial noise.

                                                    © National Instruments 4439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4440 ordinal=4440 -->
## Functions

Functions

      The following equations define the mean value, µ, and the standard deviation value, σ
            , of the pseudorandom sequence:

     µ = E{x} = p

      You can use the initialize? input to generate a long random noise sequence block by
       block. The following block diagram shows two ways to generate identical 300-sample
       Bernoulli noise sequences with a seed of 2.


      You also can use the Bernoulli Noise Waveform VI to generate a Bernoulli noise signal
       or the Discrete Random VI to generate random values from a bernoulli-distributed
        variate.

     PulsePulse TrainTrain

       Generates an array that concatenates a series of pulses according to the Prototype
       Pulse. This VI constructs the Pulse Train output by the specified interpolation
      method.


      Inputs/Outputs

               •       interpolation method —


4440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4441 ordinal=4441 -->
## Functions

Functions


  interpolation method specifies the interpolation method used to construct the Pulse Train. The
  default is Linear (1).

  0      Nearest
  1      Linear (default)
  2      Spline
  3      Cubic Hermite

•      samples —

  samples is the number of samples of the Pulse Train. If samples is less than 1, the VI sets Pulse
  Train to an empty array and returns an error. The default is 128.

•       delta t of pulse train (s) —

  delta t of pulse train (s) is the sampling interval of Pulse Train. The default is 0.1.

•      Amplitude —

  Amplitude specifies the amplitudes of each duplication of the Prototype Pulse in the Pulse
  Train.

•      Delay (s) —

  Delay (s) specifies the delay of each duplication of the Prototype Pulse in Pulse Train.

•      prototype spec —

  prototype spec specifies the prototype pulse of the Pulse Train.

      •      Prototype Pulse —

      Prototype Pulse specifies the prototype pulse, which starts at zero in the time axis.

      •       delta t of Prototype Pulse (s) —

       delta t of Prototype Pulse (s) is the sampling interval of Prototype Pulse. The default is 0.1.


•      Pulse Train —

  Pulse Train is an array that contains a pulse train of samples.


                                                   © National Instruments 4441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4442 ordinal=4442 -->
## Functions

Functions

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


           If the sequence Yrepresents Pulse Train, the Pulse Train VI generates the pattern
       according to the following equation.


      where fis the Prototype Pulse, Δtis the delta t of pulse train, Am is the m-th element
       of Amplitude, and Dm is the m-th element of Delay (s), whose size must be equal to
       the size of Amplitude.

           If Di – Dj is less than the width of the prototype pulse for any i, jbetween 0 to M–1,
       overlap occurs.

     When the sampling of the pulse train is not exactly in time with the prototype pulse
       sampling, this VI uses the specified interpolation method to get the pulse train
       samples.

      The following two front panels show a prototype pulse and its pulse train.


4442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4443 ordinal=4443 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Generation\
   Pulse Train demo.vi

QuasiQuasi RandomRandom

Generates quasi-random Halton or Richtmeyer sequences, which are low-discrepancy
number sequences.

You must manually select the polymorphic instance to use.


  • Halton Sequence VI
  • Richtmeyer Sequence VI

The quasi-random sequence is a sequence with low discrepancy that uniformly
distributes in the interval [0,1].

Use a prime number as the seed to generate a Halton sequence.

Use an irrational number as the seed to generate a Richtmeyer sequence.


                                                    © National Instruments 4443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4444 ordinal=4444 -->
## Functions

Functions

        In the VI, use the initialize? input to generate a long quasi-random noise sequence
       block-by-block. The following block diagram shows two ways to generate identical
      300-sample Halton sequences.


      HaltonHalton SequenceSequence VIVI

       Generates quasi-random Halton or Richtmeyer sequences, which are low-discrepancy
      number sequences.

      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •        initialize? —

               initialize? controls whether the noise sample generator seeds with a new value.

                    If initialize? is TRUE, the VI updates noise samples according to the value of seed. If initialize? is
            FALSE, the VI produces noise samples as a continuation of the previous noise sequence. The
             default is TRUE.

               •      samples —

           samples specifies the number of samples the VI returns in the output array. The number of
           samples must be greater than 0. The default is 128.


4444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4445 ordinal=4445 -->
## Functions

Functions

   •      seed —

    seed determines the seed to generate the sequence. seed must be a prime number. If seed is
     negative, LabVIEW takes the absolute value. The default is 3.

   •      Halton Pattern —

    Halton Pattern returns a Halton sequence in the interval [0,1].

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The quasi-random sequence is a sequence with low discrepancy that uniformly
distributes in the interval [0,1].

Use a prime number as the seed to generate a Halton sequence.

Use an irrational number as the seed to generate a Richtmeyer sequence.

In the VI, use the initialize? input to generate a long quasi-random noise sequence
block-by-block. The following block diagram shows two ways to generate identical
300-sample Halton sequences.


RichtmeyerRichtmeyer SequenceSequence VIVI

Generates quasi-random Halton or Richtmeyer sequences, which are low-discrepancy
number sequences.

                                                    © National Instruments 4445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4446 ordinal=4446 -->
## Functions

Functions

      You must manually select the polymorphic instance to use.


      Inputs/Outputs

               •        initialize? —

               initialize? controls whether the noise sample generator seeds with a new value.

                    If initialize? is TRUE, the VI updates noise samples according to the value of seed. If initialize? is
            FALSE, the VI produces noise samples as a continuation of the previous noise sequence. The
             default is TRUE.

               •      samples —

           samples specifies the number of samples the VI returns in the output array. The number of
           samples must be greater than 0. The default is 128.

               •      seed —

           seed determines the seed to generate the sequence. seed must be an irrational number. If seed
                is negative, LabVIEW takes the absolute value. The default is the square root of 3.

               •      Richtmeyer Pattern —

           Richtmeyer Pattern contains a Richtmeyer sequence in the interval [0,1].

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


      The quasi-random sequence is a sequence with low discrepancy that uniformly
        distributes in the interval [0,1].

      Use a prime number as the seed to generate a Halton sequence.

      Use an irrational number as the seed to generate a Richtmeyer sequence.


4446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4447 ordinal=4447 -->
## Functions

Functions

In the VI, use the initialize? input to generate a long quasi-random noise sequence
block-by-block. The following block diagram shows two ways to generate identical
300-sample Halton sequences.


SignalSignal OperationOperation

Use the Signal Operation VIs to manipulate signals and return a signal output.

The VIs on this palette can return signal processing error codes.


 Palette Object    Description

               Computes the convolution of the input sequences X and Y. Wire data to the X and
 Convolution     Y inputs to determine the polymorphic instance to use or manually select the
                   instance.


 Deconvolution   Computes the deconvolution of the input sequences X * Y and Y.


               Computes the autocorrelation of the input sequence X. Wire data to the X input
 AutoCorrelation
                   to determine the polymorphic instance to use or manually select the instance.


                                                    © National Instruments 4447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4448 ordinal=4448 -->
## Functions

Functions


         Palette Object    Description

                      Computes the cross correlation of the input sequences X and Y. Wire data to the
         CrossCorrelation X and Y inputs to determine the polymorphic instance to use or manually select
                         the instance.


                      Computes the autocorrelation matrix of the input sequence X. Wire data to the X         AutoCorrelation                          input to determine the polymorphic instance to use or manually select the
         Matrix                            instance.


           Y[i]=X[i-n]         Shifts the elements in the Input Array by the specified number of shifts: n.


                           Resizes the input sequence Input Array to the next higher valid power of 2, sets
                         the new trailing elements of the sequence to zero, and leaves the first n elements
        Zero Padder     unchanged, where n is the number of samples in the input sequence. Wire data
                           to the Input Array input to determine the polymorphic instance to use or
                        manually select the instance.


                      Unwraps the Phase array by eliminating discontinuities whose absolute values
       Unwrap Phase                        exceed either pi or 180, depending on the units you specify in phase unit.


          Digital Reversed                          Modifies the input array according to the digital-reversed order of the index.
        Order


                        Decimates the input sequence X by the decimating factor and the averaging
        Decimate (single
                       Boolean control. Wire data to the X input to determine the polymorphic instance
         shot)
                           to use or manually select the instance.


                         Continuously decimates the input sequence X by the decimating factor and the
        Decimate
                         averaging Boolean control. Wire data to the X input to determine the
         (continuous)
                        polymorphic instance to use or manually select the instance.


4448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4449 ordinal=4449 -->
## Functions

Functions


Palette Object    Description

                   Inserts zeros in input sequence X by upsampling factor. Wire data to the X input
Upsample                  to determine the polymorphic instance to use or manually select the instance.


               Resamples the input signal X by interpolating X, passing the interpolated signalRational                through an FIR filter, and decimating the filtered signal. Wire data to the X inputResample                  to determine the polymorphic instance to use or manually select the instance.


Resample       Resamples input signal X according to delay and dt using an FIR filter
(constant to      implementation. Wire data to the X input to determine the polymorphic instance
constant)         to use or manually select the instance.


Resample       Resamples input signal X according to Time using an FIR filter implementation.
(constant to      Wire data to the X input to determine the polymorphic instance to use or
variable)        manually select the instance.


                 Finds the norm of the Input Vector and obtains its corresponding Unit Vector byUnit Vector                 normalizing the original Input Vector with its norm.


              Removes the offset of an input signal X and then scales the result so that theScale                output sequence is in the range [–1:1].


                Determines the maximum absolute value of the input X and then scales X using
Quick Scale
                    this value.


                Normalizes the input vector or matrix using its statistical profile (µ,s), where µ is
Normalize       the mean and sis the standard deviation, to obtain a Normalized Vector or
               Normalized Matrix whose statistical profile is (0,1).


Y[i]=Clip{X[i]}      Clips the elements of Input Array to within the bounds specified by upper limit


                                                    © National Instruments 4449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4450 ordinal=4450 -->
## Functions

Functions


         Palette Object    Description

                      and lower limit.


                                Riffles the elements in the input array X. Wire data to the X input to determine           Riffle                         the polymorphic instance to use or manually select the instance.


       AC &amp; DC                          Estimates the AC and DC levels of the input Signal.         Estimator


                          Finds the location, amplitude, and second derivative of peaks or valleys in the        Peak Detector VI
                          input signal.


                          Analyzes the input sequence X for valid peaks and keeps a count of the number
        Threshold                            of peaks encountered and a record of Indices, which locates the points that         Detector VI                        exceed the threshold in a valid peak.


        Convolution and                        Performs convolution, deconvolution, or correlation on the input signals.         Correlation

         Scaling and                       Changes the amplitude of a signal by scaling or mapping the signal.        Mapping

        Z-Transform      Stores data from one VI execution or loop iteration to the next. This node is the
        Delay Node      Feedback Node in z-transform view.

      Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Signal Operation\
        Signal Operation.lvproj


4450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4451 ordinal=4451 -->
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


                                                    © National Instruments 4451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4452 ordinal=4452 -->
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


4452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4453 ordinal=4453 -->
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


                                                    © National Instruments 4453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4454 ordinal=4454 -->
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


4454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4455 ordinal=4455 -->
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

1D1D ConvolutionConvolution (DBL)(DBL) VIVI

Computes the convolution of the input sequences X and Y. Wire data to the X and Y
inputs to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the first input sequence.

   •      Y —

    Y is the second input sequence.

   •      algorithm —


                                                    © National Instruments 4455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4456 ordinal=4456 -->
## Functions

Functions


            algorithm specifies the convolution method to use. When algorithm is direct, this VI computes
            the convolution using the direct method of linear convolution. When algorithm is frequency
           domain, this VI computes the convolution using an FFT-based technique.

                    If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
          domain method typically is faster. Additionally, slight numerical differences can exist between
            the two methods.

           0     direct
                  frequency domain           1                     (default)

               •     X * Y —

          X * Y is the convolution of X and Y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D Convolution

      The linear convolution of the signals x(t) and y(t) is defined as:


      where the symbol * denotes linear convolution.

     When algorithm is direct, this VI uses the following equation to perform the discrete
      implementation of the linear convolution and obtain the elements of X * Y.


        for i= 0, 1, 2, … , M+N–2

      where his X * Y

4456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4457 ordinal=4457 -->
## Functions

Functions

Nis the number of elements in X, Mis the number of elements in Y, the indexed
elements outside the ranges of X and Y are equal to zero, as shown in the following
relationships:

xj = 0, j< 0, or j≥ N

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


                                                    © National Instruments 4457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4458 ordinal=4458 -->
## Functions

Functions


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Signal Processing\Signal Operation\Edge
        Detection with 2D Convolution.vi

     1D1D ConvolutionConvolution (CDB)(CDB) VIVI

      Computes the convolution of the input sequences X and Y. Wire data to the X and Y
       inputs to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the first complex valued input sequence.

               •      Y —

           Y is the second complex valued input sequence.

               •      algorithm —

            algorithm specifies the convolution method to use. When algorithm is direct, this VI computes
            the convolution using the direct method of linear convolution. When algorithm is frequency
           domain, this VI computes the convolution using an FFT-based technique.


4458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4459 ordinal=4459 -->
## Functions

Functions


       If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
    domain method typically is faster. Additionally, slight numerical differences can exist between
    the two methods.

    0     direct
          frequency domain    1            (default)

   •     X * Y —

    X * Y is the convolution of X and Y.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D Convolution

The linear convolution of the signals x(t) and y(t) is defined as:


where the symbol * denotes linear convolution.

When algorithm is direct, this VI uses the following equation to perform the discrete
implementation of the linear convolution and obtain the elements of X * Y.


for i= 0, 1, 2, … , M+N–2

where his X * Y

Nis the number of elements in X, Mis the number of elements in Y, the indexed
elements outside the ranges of X and Y are equal to zero, as shown in the following

                                                    © National Instruments 4459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4460 ordinal=4460 -->
## Functions

Functions

        relationships:

      xj = 0, j< 0, or j≥ N

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


4460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4461 ordinal=4461 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Signal Processing\Signal Operation\Edge
   Detection with 2D Convolution.vi

2D2D ConvolutionConvolution (DBL)(DBL) VIVI

Computes the convolution of the input sequences X and Y. Wire data to the X and Y
inputs to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the first input sequence.

   •      Y —

    Y is the second input sequence.

   •      algorithm —

    algorithm specifies the convolution method to use. When algorithm is direct, this VI computes
    the convolution using the direct method of linear convolution. When algorithm is frequency


                                                    © National Instruments 4461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4462 ordinal=4462 -->
## Functions

Functions


           domain, this VI computes the convolution using an FFT-based technique.

                    If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
          domain method typically is faster. Additionally, slight numerical differences can exist between
            the two methods.

           0     direct
                  frequency domain
           1                     (default)

               •      output size —

           output size determines the size of X * Y.

                 full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets           0             the height of X * Y to one less than the sum of the heights of X and Y.
           1 size X—Sets the width and height of X * Y to the width and height of X.
            compact—Sets the width of X * Y to one more than the difference of the widths of X and Y and
               sets the height of X * Y to one more than the difference of the heights of X and Y. The width and           2              height of X must be greater than or equal to the width and height of Y, respectively, when
            output size is compact.

               •     X * Y —

          X * Y is the convolution of X and Y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D Convolution

     When algorithm is direct, this VI uses the following equation to compute the two-
      dimensional convolution of the input matrices X and Y.


4462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4463 ordinal=4463 -->
## Functions

Functions

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


   • Second, this VI calculates the Fourier transform of X' and Y' according to the
    following equations.

X'(f) = FFT(x') Y'(f) = FFT(y')

   • Third, this VI multiplies X'(f) by Y'(f) and calculates the inverse Fourier transform of
    the product. The result is the two-dimensional convolution of X and Y, as shown in
    the following equation.

X * Y = IFFT(X'(f) · Y'(f))

The output size determines the size of the output matrix X * Y as shown in the

                                                    © National Instruments 4463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4464 ordinal=4464 -->
## Functions

Functions

       following illustration.


         1.  full

         The output matrix X * Y is (M1+M2–1)-by-(N1+N2–1).

         2. size X

           This is useful in image processing. If Xis the image you want to filter, Yis a small
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


4464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4465 ordinal=4465 -->
## Functions

Functions

   Detection with 2D Convolution.vi

2D2D ConvolutionConvolution (CDB)(CDB) VIVI

Computes the convolution of the input sequences X and Y. Wire data to the X and Y
inputs to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the first complex valued input sequence.

   •      Y —

    Y is the second complex valued input sequence.

   •      algorithm —

    algorithm specifies the convolution method to use. When algorithm is direct, this VI computes
    the convolution using the direct method of linear convolution. When algorithm is frequency
    domain, this VI computes the convolution using an FFT-based technique.

       If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
   domain method typically is faster. Additionally, slight numerical differences can exist between
    the two methods.

    0     direct
          frequency domain
    1
            (default)

   •      output size —

    output size determines the size of X * Y.

    0 full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets


                                                    © National Instruments 4465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4466 ordinal=4466 -->
## Functions

Functions


             the height of X * Y to one less than the sum of the heights of X and Y.
           1 size X—Sets the width and height of X * Y to the width and height of X.
            compact—Sets the width of X * Y to one more than the difference of the widths of X and Y and
               sets the height of X * Y to one more than the difference of the heights of X and Y. The width and           2              height of X must be greater than or equal to the width and height of Y, respectively, when
            output size is compact.

               •     X * Y —

          X * Y is the convolution of X and Y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


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


4466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4467 ordinal=4467 -->
## Functions

Functions

y(m,n) , m< 0 or m≥ M2 or n< 0 or n≥ N2.

When algorithm is frequency domain, this VI completes the following steps, in
order, to compute the two-dimensional convolution:

   •  First, this VI pads the end of X and Y with zeros to make their sizes (M1 + M2 – 1)-by-
   (N1 + N2 – 2), as shown in the following equations.


   • Second, this VI calculates the Fourier transform of X' and Y' according to the
    following equations.

X'(f) = FFT(x') Y'(f) = FFT(y')

   • Third, this VI multiplies X'(f) by Y'(f) and calculates the inverse Fourier transform of
    the product. The result is the two-dimensional convolution of X and Y, as shown in
    the following equation.

X * Y = IFFT(X'(f) · Y'(f))

The output size determines the size of the output matrix X * Y as shown in the
following illustration.


                                                    © National Instruments 4467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4468 ordinal=4468 -->
## Functions

Functions

         1.  full

         The output matrix X * Y is (M1+M2–1)-by-(N1+N2–1).

         2. size X

           This is useful in image processing. If Xis the image you want to filter, Yis a small
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

     DeconvolutionDeconvolution

      Computes the deconvolution of the input sequences X * Y and Y.

      The deconvolution operation is performed using Fourier transform pairs.


      Inputs/Outputs

               •     X * Y —


4468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4469 ordinal=4469 -->
## Functions

Functions


    X * Y is the set of input data. The number of elements in X * Y must be greater than or equal to
    the number of elements in Y: n greater than or equal to m.

       If the number of elements in X * Y is less than the number of elements in Y, the VI sets X to an
    empty array and returns an error.

   •      Y —

    Y is the array of dependent values.

   •     X —

    X is the deconvolved sequence of X * Y and Y.

    The number of elements in X is size = n– m+ 1 where nis the number of elements in X * Y and
  mis the number of elements in Y.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


The Deconvolution VI can use Fourier identities to realize the convolution operation
because

x(t) * y(t) ⇔ X(f) Y(f)

is a Fourier transform pair, where the symbol * denotes convolution, and the
deconvolution is the inverse of the convolution operation. If h(t) is the signal resulting
from the deconvolution of the signals x(t) and y(t), the Deconvolution VI obtains h(t)
using the equation

                   ,

where X(f) is the Fourier transform of x(t), and Y(f) is the Fourier transform of y(t).

The Deconvolution VI performs the discrete implementation of the deconvolution
using the following steps.


                                                    © National Instruments 4469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4470 ordinal=4470 -->
## Functions

Functions

         1. Compute the Fourier transform of the input sequence X * Y.
         2. Compute the Fourier transform of the input sequence Y.
         3. Divide the Fourier transform of X * Y by the Fourier transform of Y. Call the new
         sequence h.
         4. Compute the inverse Fourier transform of hto obtain the deconvolved sequence X.

           Note The deconvolution operation is a numerically unstable operation and
                      it is not always possible to solve the system numerically. Computing the
              deconvolution by FFTs is perhaps the most stable generic algorithm that
             does not require sophisticated DSP techniques. However, it is not free of
                errors, for example, when there are zeros in the Fourier transform of the
              input sequence Y.

      AutoCorrelationAutoCorrelation

      Computes the autocorrelation of the input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


            • 1D Auto Correlation (DBL) VI
            • 1D Auto Correlation (CDB) VI
            • 2D Auto Correlation (DBL) VI
            • 2D Auto Correlation (CDB) VI

     1D Autocorrelation

      The autocorrelation Rxx(t) of a function x(t) is defined as


      where the symbol ⊗ denotes correlation.

       For the discrete implementation of the AutoCorrelation VI, let Yrepresent a sequence

4470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4471 ordinal=4471 -->
## Functions

Functions

whose indexing can be negative, let Nbe the number of elements in the input
sequence X, and assume that the indexed elements of X that lie outside its range are
equal to zero, as shown in the following relationship:

xj = 0, j< 0 or j≥ N

Then the AutoCorrelation VI obtains the elements of Yusing the following formula:

                       ,

for j= –(N–1), –(N–2), …, –1, 0, 1, …, (N–2), (N–1)

The elements of the output sequence Rxx are related to the elements in the sequence
Yby

Rxxi = yi–(N–1)

for i= 0, 1, 2, … , 2N–2

Notice that the number of elements in the output sequence Rxx is 2N–1. Because you
cannot use negative numbers to index LabVIEW arrays, the corresponding correlation
value at t= 0 is the Nth element of the output sequence Rxx. Therefore, Rxx represents
the correlation values that the AutoCorrelation VI shifts Ntimes in indexing. The
following block diagram shows one way to display the correct indexing for the
AutoCorrelation VI.


The following graph results from the preceding block diagram.


                                                    © National Instruments 4471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4472 ordinal=4472 -->
## Functions

Functions


        In order to make the autocorrelation calculation more accurate, normalization is
       required in some situations. This VI provides biased and unbiased normalization.

         1. Biased normalization

                 If the normalization is biased, LabVIEW applies biased normalization as follows:


            for j= –(N–1), –(N–2), …, –1, 0, 1, … , (N–2), (N–1), and

         Rxx(biased)i=yi–(N–1)

            for i= 0, 1, 2, … , 2N–2

         2. Unbiased normalization

                 If the normalization is unbiased, LabVIEW applies unbiased normalization as
           follows:


            for j= –(N–1), –(N–2), …, –1, 0, 1, … , (N–2), (N–1), and

         Rxx(unbiased)i=yi–(N–1)

            for i= 0, 1, 2, … , 2N–2


4472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4473 ordinal=4473 -->
## Functions

Functions

2D Autocorrelation

The AutoCorrelation VI computes two-dimensional autocorrelation using the following
equation:


for i= –(M–1), …, –1, 0, 1, … , (M–1) and j= –(N–1), …, –1, 0, 1, … , (N–1)

where Mis the number of rows of matrix X and Nis the number of columns of matrix X.
The indexed elements of X that lie outside its range are equal to zero, as shown in the
following relationship:

x(m,n)= 0, m< 0 or m≥ Mor n< 0 or n≥ N
1D1D AutoAuto CorrelationCorrelation (DBL)(DBL) VIVI

Computes the autocorrelation of the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the input sequence.

   •      normalization —

    normalization specifies the normalization method to use to compute the autocorrelation of X.

             none
    0
                 (default)
    1         unbiased
    2          biased


                                                    © National Instruments 4473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4474 ordinal=4474 -->
## Functions

Functions

               •      Rxx —

           Rxx is the autocorrelation of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D Autocorrelation

      The autocorrelation Rxx(t) of a function x(t) is defined as


      where the symbol ⊗ denotes correlation.

       For the discrete implementation of the AutoCorrelation VI, let Yrepresent a sequence
      whose indexing can be negative, let Nbe the number of elements in the input
      sequence X, and assume that the indexed elements of X that lie outside its range are
       equal to zero, as shown in the following relationship:

      xj = 0, j< 0 or j≥ N

      Then the AutoCorrelation VI obtains the elements of Yusing the following formula:

                                   ,

        for j= –(N–1), –(N–2), …, –1, 0, 1, …, (N–2), (N–1)

      The elements of the output sequence Rxx are related to the elements in the sequence
   Yby

      Rxxi = yi–(N–1)


4474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4475 ordinal=4475 -->
## Functions

Functions

for i= 0, 1, 2, … , 2N–2

Notice that the number of elements in the output sequence Rxx is 2N–1. Because you
cannot use negative numbers to index LabVIEW arrays, the corresponding correlation
value at t= 0 is the Nth element of the output sequence Rxx. Therefore, Rxx represents
the correlation values that the AutoCorrelation VI shifts Ntimes in indexing. The
following block diagram shows one way to display the correct indexing for the
AutoCorrelation VI.


The following graph results from the preceding block diagram.


In order to make the autocorrelation calculation more accurate, normalization is
required in some situations. This VI provides biased and unbiased normalization.

 1. Biased normalization

      If the normalization is biased, LabVIEW applies biased normalization as follows:


    for j= –(N–1), –(N–2), …, –1, 0, 1, … , (N–2), (N–1), and

                                                    © National Instruments 4475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4476 ordinal=4476 -->
## Functions

Functions

         Rxx(biased)i=yi–(N–1)

            for i= 0, 1, 2, … , 2N–2

         2. Unbiased normalization

                 If the normalization is unbiased, LabVIEW applies unbiased normalization as
           follows:


            for j= –(N–1), –(N–2), …, –1, 0, 1, … , (N–2), (N–1), and

         Rxx(unbiased)i=yi–(N–1)

            for i= 0, 1, 2, … , 2N–2

     1D1D AutoAuto CorrelationCorrelation (CDB)(CDB) VIVI

      Computes the autocorrelation of the input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •      normalization —

            normalization specifies the normalization method to use to compute the autocorrelation of X.

           0        none


4476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4477 ordinal=4477 -->
## Functions

Functions


                 (default)
    1         unbiased
    2          biased

   •      Rxx —

    Rxx is the autocorrelation of X.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


1D Autocorrelation

The autocorrelation Rxx(t) of a function x(t) is defined as


where the symbol ⊗ denotes correlation.

For the discrete implementation of the AutoCorrelation VI, let Yrepresent a sequence
whose indexing can be negative, let Nbe the number of elements in the input
sequence X, and assume that the indexed elements of X that lie outside its range are
equal to zero, as shown in the following relationship:

xj = 0, j< 0 or j≥ N

Then the AutoCorrelation VI obtains the elements of Yusing the following formula:

                       ,

for j= –(N–1), –(N–2), …, –1, 0, 1, …, (N–2), (N–1)

The elements of the output sequence Rxx are related to the elements in the sequence


                                                    © National Instruments 4477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4478 ordinal=4478 -->
## Functions

Functions

   Yby

      Rxxi = yi–(N–1)

        for i= 0, 1, 2, … , 2N–2

       Notice that the number of elements in the output sequence Rxx is 2N–1. Because you
      cannot use negative numbers to index LabVIEW arrays, the corresponding correlation
       value at t= 0 is the Nth element of the output sequence Rxx. Therefore, Rxx represents
       the correlation values that the AutoCorrelation VI shifts Ntimes in indexing. The
       following block diagram shows one way to display the correct indexing for the
       AutoCorrelation VI.


      The following graph results from the preceding block diagram.


        In order to make the autocorrelation calculation more accurate, normalization is
       required in some situations. This VI provides biased and unbiased normalization.

         1. Biased normalization

                 If the normalization is biased, LabVIEW applies biased normalization as follows:


4478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4479 ordinal=4479 -->
## Functions

Functions


    for j= –(N–1), –(N–2), …, –1, 0, 1, … , (N–2), (N–1), and

   Rxx(biased)i=yi–(N–1)

    for i= 0, 1, 2, … , 2N–2

 2. Unbiased normalization

      If the normalization is unbiased, LabVIEW applies unbiased normalization as
    follows:


    for j= –(N–1), –(N–2), …, –1, 0, 1, … , (N–2), (N–1), and

   Rxx(unbiased)i=yi–(N–1)

    for i= 0, 1, 2, … , 2N–2

2D2D AutoAuto CorrelationCorrelation (DBL)(DBL) VIVI

Computes the autocorrelation of the input sequence X. Wire data to the X input to
determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the real input sequence.

   •      Rxx —


                                                    © National Instruments 4479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4480 ordinal=4480 -->
## Functions

Functions


           Rxx is the autocorrelation of X.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     2D Autocorrelation

      The AutoCorrelation VI computes two-dimensional autocorrelation using the following
       equation:


        for i= –(M–1), …, –1, 0, 1, … , (M–1) and j= –(N–1), …, –1, 0, 1, … , (N–1)

      where Mis the number of rows of matrix X and Nis the number of columns of matrix X.
      The indexed elements of X that lie outside its range are equal to zero, as shown in the
       following relationship:

     x(m,n)= 0, m< 0 or m≥ Mor n< 0 or n≥ N
     2D2D AutoAuto CorrelationCorrelation (CDB)(CDB) VIVI

      Computes the autocorrelation of the input sequence X. Wire data to the X input to
      determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the complex valued input sequence.

               •      Rxx —

4480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4481 ordinal=4481 -->
## Functions

Functions


    Rxx is the autocorrelation of X.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


2D Autocorrelation

The AutoCorrelation VI computes two-dimensional autocorrelation using the following
equation:


for i= –(M–1), …, –1, 0, 1, … , (M–1) and j= –(N–1), …, –1, 0, 1, … , (N–1)

where Mis the number of rows of matrix X and Nis the number of columns of matrix X.
The indexed elements of X that lie outside its range are equal to zero, as shown in the
following relationship:

x(m,n)= 0, m< 0 or m≥ Mor n< 0 or n≥ N
CrossCorrelationCrossCorrelation

Computes the cross correlation of the input sequences X and Y. Wire data to the X and
Y inputs to determine the polymorphic instance to use or manually select the instance.


   • 1D Cross Correlation (DBL) VI
   • 1D Cross Correlation (CDB) VI
   • 2D Cross Correlation (DBL) VI
   • 2D Cross Correlation (CDB) VI


                                                    © National Instruments 4481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4482 ordinal=4482 -->
## Functions

Functions

     1D Cross Correlation

      The cross correlation Rxy(t) of the sequences x(t) and y(t) is defined by the following
       equation:


      where the symbol ⊗ denotes correlation.

      The discrete implementation of the CrossCorrelation VI is as follows. Let hrepresent a
      sequence whose indexing can be negative, let Nbe the number of elements in the
       input sequence X, let Mbe the number of elements in the sequence Y, and assume
       that the indexed elements of X and Y that lie outside their range are equal to zero, as
      shown by the following equations:

      xj = 0, j< 0 or j≥ N

      and

      yj = 0, j< 0 or j≥ M.

      Then the CrossCorrelation VI obtains the elements of husing the following equation:


        for j= –(N–1), –(N–2), … , –1, 0, 1, … , (M–2), (M–1)

      The elements of the output sequence Rxy are related to the elements in the sequence
   hby

      Rxyi = hi – (N–1)

        for i= 0, 1, 2, … , N+M–2.

      Because you cannot index LabVIEW arrays with negative numbers, the corresponding

4482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4483 ordinal=4483 -->
## Functions

Functions

cross correlation value at t= 0 is the Nth element of the output sequence Rxy.
Therefore, Rxy represents the correlation values that the CrossCorrelation VI shifts N
times in indexing.

The following block diagram shows one way to index the CrossCorrelation VI.


The following graph is the result of the preceding block diagram.


In order to make the cross correlation calculation more accurate, normalization is
required in some situations. This VI provides biased and unbiased normalization.

 1. Biased normalization

      If the normalization is biased, LabVIEW applies biased normalization as follows:

   Rxy(biased)j =

    for j= 0, 1, 2, … , M+N–2

   where Rxy is the cross correlation between xand ywith no normalization.


                                                    © National Instruments 4483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4484 ordinal=4484 -->
## Functions

Functions

         2. Unbiased normalization

                 If the normalization is unbiased, LabVIEW applies unbiased normalization as
           follows:

         Rxy(unbiased)j =

            for j= 0, 1, 2, … , M+N–2

         where Rxy is the cross correlation between xand ywith no normalization. f(j)is:


     2D Cross Correlation

      The CrossCorrelation VI computes two-dimensional cross correlation as follows:


        for i= –(M1–1), … , –1, 0, 1, … , (M2–1) and j= –(N1–1), … , –1, 0, 1, … , (N2–1)

      where M1 is the number of rows of matrix X,

    N1 is the number of columns of matrix X, M2 is the number of rows of matrix Y, N2 is
       the number of columns of matrix Y, the indexed elements outside the ranges of X and Y
       are equal to zero, as shown in the following relationships:

      x(m,n) = 0, m < 0 or m≥ M1 or n < 0 or n≥ N1

      and

      y(m,n) = 0, m < 0 or m≥ M2 or n < 0 or n≥ N2.


4484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4485 ordinal=4485 -->
## Functions

Functions

The elements of the output matrix Rxyare related to the elements in has follows:

Rxy(I,j) = h(i–(M1–1), j–(N1–1)) for i= 0, 1, 2, … , M1+M2–2 and j= 0, 1, 2, … ,
N1+N2–2.
1D1D CrossCross CorrelationCorrelation (DBL)(DBL) VIVI

Computes the cross correlation of the input sequences X and Y. Wire data to the X and
Y inputs to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the first input sequence.

   •      Y —

    Y is the second input sequence.

   •      algorithm —

    algorithm specifies the correlation method to use. When algorithm is direct, this VI computes
    the cross correlation using the direct method of linear correlation. When algorithm is frequency
    domain, this VI computes the cross correlation using an FFT-based technique.

       If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
    domain method typically is faster. Additionally, slight numerical differences can exist between
    the two methods.

    0     direct
          frequency domain
    1
            (default)

   •      normalization —


                                                    © National Instruments 4485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4486 ordinal=4486 -->
## Functions

Functions


            normalization specifies the normalization method to use to compute the cross correlation
           between X and Y.

                    none           0                          (default)
           1         unbiased
           2          biased

               •      Rxy —

           Rxy is the cross correlation of X and Y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D Cross Correlation

      The cross correlation Rxy(t) of the sequences x(t) and y(t) is defined by the following
       equation:


      where the symbol ⊗ denotes correlation.

      The discrete implementation of the CrossCorrelation VI is as follows. Let hrepresent a
      sequence whose indexing can be negative, let Nbe the number of elements in the
       input sequence X, let Mbe the number of elements in the sequence Y, and assume
       that the indexed elements of X and Y that lie outside their range are equal to zero, as
      shown by the following equations:

      xj = 0, j< 0 or j≥ N

      and


4486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4487 ordinal=4487 -->
## Functions

Functions

yj = 0, j< 0 or j≥ M.

Then the CrossCorrelation VI obtains the elements of husing the following equation:


for j= –(N–1), –(N–2), … , –1, 0, 1, … , (M–2), (M–1)

The elements of the output sequence Rxy are related to the elements in the sequence
hby

Rxyi = hi – (N–1)

for i= 0, 1, 2, … , N+M–2.

Because you cannot index LabVIEW arrays with negative numbers, the corresponding
cross correlation value at t= 0 is the Nth element of the output sequence Rxy.
Therefore, Rxy represents the correlation values that the CrossCorrelation VI shifts N
times in indexing.

The following block diagram shows one way to index the CrossCorrelation VI.


The following graph is the result of the preceding block diagram.


                                                    © National Instruments 4487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4488 ordinal=4488 -->
## Functions

Functions


        In order to make the cross correlation calculation more accurate, normalization is
       required in some situations. This VI provides biased and unbiased normalization.

         1. Biased normalization

                 If the normalization is biased, LabVIEW applies biased normalization as follows:

         Rxy(biased)j =

            for j= 0, 1, 2, … , M+N–2

         where Rxy is the cross correlation between xand ywith no normalization.

         2. Unbiased normalization

                 If the normalization is unbiased, LabVIEW applies unbiased normalization as
           follows:

         Rxy(unbiased)j =

            for j= 0, 1, 2, … , M+N–2

         where Rxy is the cross correlation between xand ywith no normalization. f(j)is:


4488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4489 ordinal=4489 -->
## Functions

Functions

1D1D CrossCross CorrelationCorrelation (CDB)(CDB) VIVI

Computes the cross correlation of the input sequences X and Y. Wire data to the X and
Y inputs to determine the polymorphic instance to use or manually select the instance.


Inputs/Outputs

   •     X —

    X is the first complex valued input sequence.

   •      Y —

    Y is the second complex valued input sequence.

   •      algorithm —

    algorithm specifies the correlation method to use. When algorithm is direct, this VI computes
    the cross correlation using the direct method of linear correlation. When algorithm is frequency
    domain, this VI computes the cross correlation using an FFT-based technique.

       If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
   domain method typically is faster. Additionally, slight numerical differences can exist between
    the two methods.

    0     direct
          frequency domain
    1
            (default)

   •      normalization —

    normalization specifies the normalization method to use to compute the cross correlation
    between X and Y.

             none
    0
                 (default)


                                                    © National Instruments 4489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4490 ordinal=4490 -->
## Functions

Functions


           1         unbiased
           2          biased

               •      Rxy —

           Rxy is the cross correlation of X and Y.

               •       error —

             error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
          Code VI to convert the error code or warning into an error cluster.


     1D Cross Correlation

      The cross correlation Rxy(t) of the sequences x(t) and y(t) is defined by the following
       equation:


      where the symbol ⊗ denotes correlation.

      The discrete implementation of the CrossCorrelation VI is as follows. Let hrepresent a
      sequence whose indexing can be negative, let Nbe the number of elements in the
       input sequence X, let Mbe the number of elements in the sequence Y, and assume
       that the indexed elements of X and Y that lie outside their range are equal to zero, as
      shown by the following equations:

      xj = 0, j< 0 or j≥ N

      and

      yj = 0, j< 0 or j≥ M.

      Then the CrossCorrelation VI obtains the elements of husing the following equation:


4490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4491 ordinal=4491 -->
## Functions

Functions


for j= –(N–1), –(N–2), … , –1, 0, 1, … , (M–2), (M–1)

The elements of the output sequence Rxy are related to the elements in the sequence
hby

Rxyi = hi – (N–1)

for i= 0, 1, 2, … , N+M–2.

Because you cannot index LabVIEW arrays with negative numbers, the corresponding
cross correlation value at t= 0 is the Nth element of the output sequence Rxy.
Therefore, Rxy represents the correlation values that the CrossCorrelation VI shifts N
times in indexing.

The following block diagram shows one way to index the CrossCorrelation VI.


The following graph is the result of the preceding block diagram.


                                                    © National Instruments 4491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4492 ordinal=4492 -->
## Functions

Functions

        In order to make the cross correlation calculation more accurate, normalization is
       required in some situations. This VI provides biased and unbiased normalization.

         1. Biased normalization

                 If the normalization is biased, LabVIEW applies biased normalization as follows:

         Rxy(biased)j =

            for j= 0, 1, 2, … , M+N–2

         where Rxy is the cross correlation between xand ywith no normalization.

         2. Unbiased normalization

                 If the normalization is unbiased, LabVIEW applies unbiased normalization as
           follows:

         Rxy(unbiased)j =

            for j= 0, 1, 2, … , M+N–2

         where Rxy is the cross correlation between xand ywith no normalization. f(j)is:


     2D2D CrossCross CorrelationCorrelation (DBL)(DBL) VIVI

      Computes the cross correlation of the input sequences X and Y. Wire data to the X and
      Y inputs to determine the polymorphic instance to use or manually select the instance.


4492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4493 ordinal=4493 -->
## Functions

Functions


Inputs/Outputs

   •     X —

    X is the first input sequence.

   •      Y —

    Y is the second input sequence.

   •      algorithm —

    algorithm specifies the correlation method to use. When algorithm is direct, this VI computes
    the cross correlation using the direct method of linear correlation. When algorithm is frequency
    domain, this VI computes the cross correlation using an FFT-based technique.

       If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
   domain method typically is faster. Additionally, slight numerical differences can exist between
    the two methods.

    0     direct
          frequency domain    1
            (default)

   •      Rxy —

    Rxy is the cross correlation of X and Y.

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


2D Cross Correlation

The CrossCorrelation VI computes two-dimensional cross correlation as follows:


                                                    © National Instruments 4493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4494 ordinal=4494 -->
## Functions

Functions


        for i= –(M1–1), … , –1, 0, 1, … , (M2–1) and j= –(N1–1), … , –1, 0, 1, … , (N2–1)

      where M1 is the number of rows of matrix X,

    N1 is the number of columns of matrix X, M2 is the number of rows of matrix Y, N2 is
       the number of columns of matrix Y, the indexed elements outside the ranges of X and Y
       are equal to zero, as shown in the following relationships:

      x(m,n) = 0, m < 0 or m≥ M1 or n < 0 or n≥ N1

      and

      y(m,n) = 0, m < 0 or m≥ M2 or n < 0 or n≥ N2.

      The elements of the output matrix Rxyare related to the elements in has follows:

       Rxy(I,j) = h(i–(M1–1), j–(N1–1)) for i= 0, 1, 2, … , M1+M2–2 and j= 0, 1, 2, … ,
      N1+N2–2.
     2D2D CrossCross CorrelationCorrelation (CDB)(CDB) VIVI

      Computes the cross correlation of the input sequences X and Y. Wire data to the X and
      Y inputs to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •     X —

          X is the first complex valued input sequence.

               •      Y —


4494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4495 ordinal=4495 -->
## Functions

Functions


    Y is the second complex valued input sequence.

   •      algorithm —

    algorithm specifies the correlation method to use. When algorithm is direct, this VI computes
    the cross correlation using the direct method of linear correlation. When algorithm is frequency
    domain, this VI computes the cross correlation using an FFT-based technique.

       If X and Y are small, the direct method typically is faster. If X and Y are large, the frequency
    domain method typically is faster. Additionally, slight numerical differences can exist between
    the two methods.

    0     direct
          frequency domain
    1            (default)

   •      Rxy —

    Rxy is the cross correlation of X and Y.

   •       error —

     error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


2D Cross Correlation

The CrossCorrelation VI computes two-dimensional cross correlation as follows:


for i= –(M1–1), … , –1, 0, 1, … , (M2–1) and j= –(N1–1), … , –1, 0, 1, … , (N2–1)

where M1 is the number of rows of matrix X,

N1 is the number of columns of matrix X, M2 is the number of rows of matrix Y, N2 is
the number of columns of matrix Y, the indexed elements outside the ranges of X and Y
are equal to zero, as shown in the following relationships:

                                                    © National Instruments 4495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4496 ordinal=4496 -->
## Functions

Functions

      x(m,n) = 0, m < 0 or m≥ M1 or n < 0 or n≥ N1

      and

      y(m,n) = 0, m < 0 or m≥ M2 or n < 0 or n≥ N2.

      The elements of the output matrix Rxyare related to the elements in has follows:

       Rxy(I,j) = h(i–(M1–1), j–(N1–1)) for i= 0, 1, 2, … , M1+M2–2 and j= 0, 1, 2, … ,
      N1+N2–2.
      AutoCorrelationAutoCorrelation MatrixMatrix

      Computes the autocorrelation matrix of the input sequence X. Wire data to the X input
       to determine the polymorphic instance to use or manually select the instance.


            • AutoCorrelation Matrix (DBL) VI
            • AutoCorrelation Matrix (CDB) VI

       This VI uses the following equation to calculate the autocorrelation matrix.


      where Mis AutoCorrelation Matrix, Ris data matrix, sis normalization factor. RH is
       the conjugate transpose of matrix R.

           If method is AutoCorrelation, Ris a matrix of size (N+k)-by-(k+1) defined as follows.


4496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4497 ordinal=4497 -->
## Functions

Functions

where xi is the i-th element in X, Nis the length of X , and kis the order. The
normalization factor, s, is equal to N.

If method is Pre-Windowed, Ris a matrix of size N-by-(k+1) defined as follows.


The normalization factor, s, is equal to N.

If method is Post-Windowed, Ris a matrix of size N-by-(k+1) defined as follows.


The normalization factor, s, is equal to N.

If method is Covariance, Ris a matrix of size (N-k)-by-(k+1) defined as follows.


The normalization factor, s, is equal to N-k.

If method is Modified Covariance, Ris a matrix of size 2(N-k)-by-(k+1) defined as
follows.


                                                    © National Instruments 4497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4498 ordinal=4498 -->
## Functions

Functions

          *      where xi is the complex conjugate of xi. The normalization factor, s, is equal to 2*(N-
         k).

       This VI supports both single shot and continuous mode. The following figure illustrates
     how to use the AutoCorrelation Matrix VI in single shot and continuous mode. The two
       outputs, AutoCorrelation Matrix 1 and AutoCorrelation Matrix 2, always produce the
     same results.


       Autocorrelation matrix is widely used in the field of spectrum analysis to estimate the
       spectral components within the input signal. In general, Covariance and Modified
      Covariance methods give better results in spectral estimation processing than the
       AutoCorrelation, Pre-Windowed and Post-Windowed methods. National Instruments
      recommends that you use the Covariance or the Modified Covariance method to
       estimate the autocorrelation matrix when performing spectrum analysis.

      AutoCorrelationAutoCorrelation MatrixMatrix (DBL)(DBL) VIVI

      Computes the autocorrelation matrix of the input sequence X. Wire data to the X input
       to determine the polymorphic instance to use or manually select the instance.


      Inputs/Outputs

               •        initial? —

4498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4499 ordinal=4499 -->
## Functions

Functions


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
    4   Modified Covariance

   •      AutoCorrelation Matrix —

    AutoCorrelation Matrix returns the autocorrelation matrix of X of the size of (order+1) multiplied
    by (order+1).

   •       error —

    error returns any error or warning from the VI. You can wire error to the Error Cluster From Error
    Code VI to convert the error code or warning into an error cluster.


This VI uses the following equation to calculate the autocorrelation matrix.


                                                    © National Instruments 4499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4500 ordinal=4500 -->
## Functions

Functions

      where Mis AutoCorrelation Matrix, Ris data matrix, sis normalization factor. RH is
       the conjugate transpose of matrix R.

           If method is AutoCorrelation, Ris a matrix of size (N+k)-by-(k+1) defined as follows.


      where xi is the i-th element in X, Nis the length of X , and kis the order. The
       normalization factor, s, is equal to N.

           If method is Pre-Windowed, Ris a matrix of size N-by-(k+1) defined as follows.


      The normalization factor, s, is equal to N.

           If method is Post-Windowed, Ris a matrix of size N-by-(k+1) defined as follows.


      The normalization factor, s, is equal to N.

           If method is Covariance, Ris a matrix of size (N-k)-by-(k+1) defined as follows.


4500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:4500 -->

